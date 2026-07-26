# Care customer agent and payments diagnostics scoping

**Date:** 2026-07-20  
**Attendees:** Charlie Wildish; Javed Iqbal (building the new Care payments agent); Amol Kashetwar (built the existing internal Gateway AI diagnostic tool)  
**Drive source:** 1XC7JVjSu-cG2qMNVU1K54Bm4fpXm76kQ0XkKKEPWru0

## Context

Scoping an internal service that Fin queries via API (payment ID, ARN, merchant reference), analyses what happened to a payment, and returns a succinct explanation. Fin is the messenger only; all analysis runs on Checkout infrastructure. Knowledge-share with Amol, who already built a comparable Gateway diagnostic tool.

## Key Points

**Volume and value**
- ~900,000 tickets/week total; 50–60% payment-related (50% payins, ~10% payouts) = ~5,600 payment tickets/week, ~100/day. Highly automatable.
- Core value: explain why a payment declined and the merchant's next action, not just return a decline code. The Dashboard lacks this depth today; Care agents do it manually.

**Amol's tool — knowledge sources**
- Four sources: (1) public docs (can be stale); (2) gateway code; (3) card processing code (main branch, may not match production state at incident time; rare); (4) logs (always accurate). Proposed 5th: query the Payment Performance API instead of configs directly (richer history/origins). Also uses uploaded KB docs and manually-answered questions for curation.
- Prompt managed/versioned in Bedrock, currently v6. Structured output: summary → flow chart → exact points of failure → when it happened → problem → solution.

**Data freshness and coverage**
- 90% of payment queries occur within 90 days of the transaction. >50% of payin queries within 15 days; payouts >80% covered near-term. ~10% of queries fall beyond 90 days (typically refunds).
- 2-hour freshness gap: ~5% of queries arrive within 2 hours of payment creation; 62% of those fail because underlying data hasn't updated. Requirement: source no staler than ~30 min, ideally real-time. Payins often only reach support after ~7 days (capture/void cycle).

**Missing-data problem**
- Critical failure detail (42-response errors across gateway/routing/vault/sessions/CP, internal API failures between services, network token provisioning failures, ART issues, cryptogram refresh failures) lives in internal logs only, not in public events and not in BigQuery. Network token provisioning fails ~50% of the time (mostly issuer-side). Archived logs are hard to retrieve (indexed separately per service). Charlie to ask the data team about capturing internal API 42 failures in the main dataset to reduce Datadog reliance.

**Cost**
- Complex failure analysis up to $1/query (300–400 log entries + code + docs, retries, 3DS); simple/successful cases under ~5 cents. A comparable tool ("Giam's") optimised to 50–60 cents/query. Amol's recommendation: do not sacrifice context to cut cost — less context degrades answer quality.

## Insights

- This is the technical scoping for the Customer Agent / payment diagnostics internal service that feeds Fin (Fuel + Agent Experience flywheel domains): give Fin vetted payment-outcome analysis so it can explain declines like a Care agent would.
- The hard blocker is data, not AI: the 2-hour freshness gap (62% failure on immediate queries) and root-cause detail sitting only in internal logs, not BigQuery. Fixing the data pipeline (fresh source ≤30 min, internal API failures in the main dataset) is the prerequisite for coverage.
- Unit economics hold against the CLAUDE.md benchmark: even $1 for a complex query is far below the ~$40 human-agent cost; complex-failure queries are the cost-optimisation target.
- Decisions: merchant-facing output restricted to succinct, vetted explanations (no raw log traces or class/method names); reuse Amol's v6 Bedrock prompt as the baseline; iterative build (start with public docs + payment API schema, add Datadog/codebase/config over time), prioritising context quality over cost.
- Datadog is an enhancement layer on top of the core dataset for richer answers on recent (<15 day) payments, not the core query source. A separate hackathon team is tackling payment misconfiguration detection.
- Next step: Amol to share the v6 prompt and related markdown docs with Charlie and Javed.
