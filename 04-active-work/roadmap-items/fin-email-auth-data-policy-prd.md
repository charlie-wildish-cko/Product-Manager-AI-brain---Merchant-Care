# Fin on Email — Authentication & Data Access Policy

**Status**: Draft  
**Owner**: Charlie Wildish  
**Last Updated**: February 2026  
**Stakeholders**: Care Operations, Operational Excellence, Zendesk Admins, Engineering, Security, Legal & Compliance


## Executive Summary

Fin today only runs in the authenticated Dashboard; email is unauthenticated so Fin can’t do payment lookups there. At least 50% of email queries are payment-by-ID/Reference — the biggest lever for AI resolution. This PRD defines auth and data access so Fin can safely return payment data on email. Fin’s native verification-code flow removes the need for custom OTP; work is mainly config, policy, and integration with identification infrastructure.


## Problem

**What problem are we solving, and who has it?**  
Fin can do FAQ over email but not payment lookups — it can’t verify who is asking. ~50% of email is payment-by-ID/Reference; all of that goes to humans. That’s the main gap to AI resolution on email. Affects: merchant ops (wait for agents), CX (handle automatable volume), Care Ops/Op Ex (capped resolution), Premium/Enterprise (email is their channel). **Baseline**: Agents already return payment data over email; Fin’s marginal risk is scale and no human judgment, not a new data class.

**How are they solving it today?**  
All payment-data email → humans. No partial automation. Standard → Dashboard; Premium/Enterprise (bulk of volume) use email.

**Why solve this now?**  
Email is P/E’s primary channel; half of queries are payment lookup, automatable with verified identity. Identification work (domain mapping, Salesforce/Dashboard) is in flight — build on it now.


## Goals & Success Metrics

| Metric | Current State | Target | Timeline |
| --- | --- | --- | --- |
| AI resolution rate on email channel | FAQ-only (low baseline) | Target informed by 50%+ addressable query volume — TBC once baseline established | 6 months post-launch |
| % of payment-by-ID/Reference queries handled by Fin without human intervention | ~0% | TBC — represents at least 50% of current email volume | 6 months post-launch |
| % of payment queries escalated to human due to unidentified org (Level 0) | Baseline TBC | Decreasing — drives domain mapping and Salesforce identification coverage | 3 months post-launch |
| Security incidents attributable to email data disclosure | 0 | 0 (maintained) | Ongoing |
| PCI DSS / GDPR policy compliance | N/A | 100% — no prohibited data returned over email | At launch and ongoing |


## User Stories

### Merchant ops team member: querying a specific payment by ID or Reference

**As a** merchant payment ops team member who emails support with a Payment ID or Payment Reference to ask what happened to a transaction,  
**I want** Fin to look up that payment and return its status and outcome,  
**So that** I get an immediate answer without waiting for a human agent to investigate.

**Acceptance Criteria**:

- Fin recognises that the query contains a Payment ID or Reference and that it requires a data lookup
- Fin identifies the requester's org via Salesforce/Dashboard lookup or domain mapping
- If the org cannot be identified (Level 0), Fin routes to a human agent — it cannot return payment data without knowing which merchant is asking
- If the org is identified (Level 1 or above), Fin looks up the payment by the provided ID or Reference against Checkout.com's payments API
- Fin returns a summary: payment status, outcome code, and a brief plain-language explanation of what happened
- Fin includes a direct deep link to the payment record in the Merchant Dashboard so the merchant can view full details there
- No consumer personal data (cardholder name, full card number, email) is included in the email response — the Dashboard is the path to richer data
- If the Payment ID or Reference does not match any payment on the identified merchant's account, Fin responds clearly and routes to a human agent


### Merchant ops team member: asking an org-level configuration question via email

**As a** merchant ops team member who emails support to ask whether 3DS is enabled on their account,  
**I want** Fin to answer directly without requiring me to take additional verification steps,  
**So that** simple configuration queries are resolved immediately.

**Acceptance Criteria**:

- If the requester's org is identified (via Salesforce/Dashboard or domain mapping), Fin returns org-level configuration status without step-up
- No transaction-level or consumer data is included in the response
- Fin clearly attributes the answer to the identified merchant org


### CX agent: reviewing a Fin-handled email ticket

**As a** CX agent reviewing a ticket Fin handled on email,  
**I want** to see what authentication level was established and what data Fin returned,  
**So that** I can verify it was handled correctly and pick up escalations with full context.

**Acceptance Criteria**:

- Zendesk ticket includes a Fin conversation log showing: authentication level achieved, data returned, and reason for any escalation
- Agent can see whether OTP step-up was completed or timed out
- No out-of-policy data is visible in the ticket log

**Edge cases**:

- **Level 0 — org cannot be identified**: Fin routes to a human agent; no payment data returned regardless of query type
- **Domain-mapped user (Level 1) requests transaction data**: Fin returns transaction status and outcome for the provided Payment ID — consistent with agent practice; no step-up required
- **Shared inbox — data visible to multiple team members**: Accepted baseline — agents already send to shared inboxes; Fin applies data minimisation (status and outcome, no consumer PII)
- **Deprovisioned email address matches a domain**: Step-up email is delivered to a deprovisioned account (no response). Fin times out and routes to human — no data returned
- **Query contains multiple Payment IDs or References**: Fin processes each lookup individually and returns a consolidated response; if any lookup would return consumer PII, that result is omitted and routed to human
- **Payment ID belongs to a different merchant than the identified org**: Fin declines to return the data and routes to human — cross-merchant data access must never occur
- **Reference matches multiple payments**: Fin returns summary status for all matched payments; if the list is large, Fin summarises and suggests the merchant refine their query or use the Dashboard
- **Query requires consumer PII or PAN**: Fin declines regardless of authentication level; routes to human agent with explanation
- **A @checkout.com address is CC'd**: Fin does not respond — ticket routes directly to human agent. Checkout.com staff on the thread signals the conversation is already being handled by a human.
- **More than 2 people CC'd**: Fin does not respond — ticket routes directly to human agent. High CC count indicates a complex or escalated situation where automated data sharing is inappropriate.
- **≤2 people CC'd, no @checkout.com address**: Fin proceeds normally under the standard data policy.


## Requirements

#### Must Have (P0)

- Formal data access policy, approved by Security and Legal & Compliance, calibrated against current agent practice and defining what Fin may return at each identification level
- Identification level assessment on every inbound email ticket: classify the requester as unidentified (Level 0) / domain-mapped (Level 1) / known Salesforce or Dashboard contact (Level 2)
- **Gate for payment data is org identification, not OTP**: Fin may return transaction status and outcome data to Level 1 and Level 2 requesters — consistent with what agents return today. OTP is available as an optional identity confirmation tool, not a mandatory blocker.
- **Fin exclusion rules (evaluated before any Fin involvement)**: Fin must not respond to any ticket where (a) a @checkout.com email address is CC'd, or (b) more than 2 people are CC'd. Implemented via Zendesk trigger and ticket field logic.
- Hard block: Fin must never return PANs, consumer personal data, or cardholder-identifying information over email regardless of identification level
- Every payment lookup response must include a direct deep link to the payment record in the Merchant Dashboard
- Fin escalates to human agent if: org cannot be identified (Level 0) for a payment data query, or the query falls outside the data policy
- Zendesk ticket logging: identification level and data returned must be recorded on the ticket for agent review

#### Should Have (P1)

- Confirmation of Fin's native verification code behaviour: expiry window, single-use enforcement, and delivery failure handling — verified against Fin's implementation before launch
- Fin explicitly communicates to the merchant what auth level has been established and why certain data cannot be returned
- Configurable data policy rules (Zendesk admins or Engineering can update policy without a code deployment)
- Audit log of all data returned over email by Fin, queryable for compliance review

#### Nice to Have (P2)

- Step-up completion rate tracking and drop-off analysis (to optimise the flow)
- Differentiated data policy by merchant tier (subject to Security review)
- **Settlement status lookup**: Fin can respond to "where is my settlement?" queries by looking up the status of a pending or recent settlement for the identified org — returning settlement date, amount, and status. Addresses FUNDS AND FEES queries (~15% of contact volume). Requires settlement data API access scoped for Fin; Security/Legal policy approval needed before enabling (same process as payment data). **Note: this is also a requirement for Fin over chat (Dashboard) — the API and policy work is shared; this PRD should be treated as the driver for the API access and policy approval, with chat channel configuration following separately.**
- **Balance lookup**: Fin can respond to balance queries (current available balance, negative balance explanation) for the identified org. Requires balance data API access scoped for Fin. Same policy approval process applies. **Note: same cross-channel requirement as settlement status — API access and policy approval needed once and reused across email and chat.**

**Constraints**:
- **Security**: Fin's native email verification code flow handles OTP generation and delivery. Security must review and approve Fin's implementation of this flow (expiry, single-use enforcement, delivery failure behaviour) before it is used to gate data access.
- **Compliance**: Data policy must be formally signed off by Legal & Compliance. No data-return capability goes live without this approval. Policy must be reviewed at least annually or when regulations change (PCI DSS, GDPR, PSD3).
- **Auditability**: Every instance of data returned by Fin over email must be logged with: timestamp, ticket ID, authentication level, data type returned. Logs retained per applicable data retention policy.
- **Privacy**: Fin responses must apply data minimisation — return the minimum data necessary to resolve the query.
- **Availability**: OTP delivery depends on email infrastructure; failure to deliver OTP must fall back to human agent routing, not block the ticket silently.


## Approach

### Fin Involvement Rules

Before Fin takes any action on an email ticket, two sets of rules are evaluated in order: **exclusion rules** (should Fin be involved at all?) and **identification level** (what data can Fin return?).

#### Step 1 — Exclusion rules (Fin stands down entirely)

Evaluated at ticket creation via Zendesk trigger. If any condition is met, `fin_eligible = false`, Fin is not assigned, and the ticket routes directly to a human agent. These rules apply to **all Fin email involvement** — including FAQ responses, not just payment data lookups.

| Rule | Condition | Rationale |
| --- | --- | --- |
| Checkout.com staff on CC | Any CC'd address has domain `@checkout.com` | Conversation already involves a Checkout.com employee — human handling in progress |
| High CC count | More than 2 people CC'd | Indicates a complex or escalated thread; Fin should not be involved at any level |

#### Step 2 — Identification level (what can Fin return?)

Only reached if `fin_eligible = true`. Fin assesses who is asking and responds within the corresponding data entitlement.

| Level | How established | Payment data? |
| --- | --- | --- |
| 0 — Unidentified | No match anywhere | No — route to human for any data query |
| 1 — Domain-mapped | Email domain matches org record | Yes — status and outcome for provided Payment ID |
| 2 — Known contact | Salesforce or Dashboard match | Yes — status, outcome, dispute data |
| 3 — Dashboard session | Authenticated Dashboard login | Yes — full Fin capability |

#### Step 3 — Hard limits (apply regardless of level)

Even within an eligible, identified conversation, Fin must never return:

- **PANs** (full or partial) — PCI DSS absolute prohibition
- **Consumer personal data** (cardholder name, email, address) — GDPR; shared inbox risk
- **Payout recipient personal data** — never without legal review
- **Data for a Payment ID that doesn't belong to the identified org** — route to human

#### Decision flow summary

```
Email ticket received
        ↓
Exclusion check: @checkout.com on CC OR >2 CC'd?
  → Yes: fin_eligible = false → human agent (no Fin involvement at all)
  → No: proceed
        ↓
Identification level: Salesforce / Dashboard / domain mapping lookup
  → Level 0: FAQ only; data query → human agent
  → Level 1+: proceed with data lookup
        ↓
Data policy check: does the request fall within level entitlements?
  → Hard limit hit (PAN, consumer PII, wrong org): decline + human agent
  → Within policy: return summary + Dashboard deep link
```


### Identification Levels & Data Entitlements

The data policy is enforced based on the identification level established at the point of Fin's response. The gate for payment data is **org identification**, not step-up verification — consistent with how agents handle email today.

```
Level 0 — Unidentified
  No match in Salesforce, Dashboard, or domain mapping
  → FAQ and documentation only
  → No payment or account data
  → Fin routes to human agent for any data query

Level 1 — Domain-mapped
  Email domain matches a configured org record
  → Org-level configuration and status data: yes
  → Transaction status / outcome for a provided Payment ID
    or Reference: yes — consistent with agent practice
  → Consumer personal data: never
  → PANs: never

Level 2 — Known contact (Salesforce or Dashboard match)
  Email address found in Salesforce or Dashboard as a
  verified contact for this merchant
  → All Level 1 data: yes
  → Transaction and dispute data: yes — stronger identification
    than Level 1; no step-up required
  → Consumer personal data: never
  → PANs: never

Level 3 — Authenticated Dashboard session
  User is logged into the Dashboard; Fin's full capability applies
  → All data accessible per existing Dashboard Fin policy
  → This PRD does not change Level 3 behaviour

Email verification step-up (optional)
  Fin's native verification code flow is available as a
  confirmatory tool — e.g. when org identification is borderline,
  for audit purposes, or if Security requires it for specific
  data types. It is NOT a mandatory gate for standard payment
  data at Level 1 or Level 2.
```

### Data Classification

| Data type | Level 0 | Level 1 | Level 2 (+ OTP) | Level 3 | Hard limit |
| --- | --- | --- | --- | --- | --- |
| Documentation / FAQs | ✅ | ✅ | ✅ | ✅ | — |
| Org config status (3DS enabled, routing rules) | ❌ | ✅ | ✅ | ✅ | — |
| Account-level settlement schedule | ❌ | ✅ | ✅ | ✅ | — |
| Transaction status / outcome code (masked) | ❌ | ✅ | ✅ | ✅ | — |
| Dispute / chargeback status | ❌ | ✅ | ✅ | ✅ | — |
| Aggregate reporting data | ❌ | ✅ | ✅ | ✅ | — |
| Settlement status (pending/recent settlement) | ❌ | ✅ | ✅ | ✅ | P2 — requires API access + policy sign-off |
| Current balance / available funds | ❌ | ✅ | ✅ | ✅ | P2 — requires API access + policy sign-off |
| Consumer personal data (name, email, address) | ❌ | ❌ | ❌ | ❌ | **Never over email** |
| Full or partial PAN | ❌ | ❌ | ❌ | ❌ | **Never — PCI DSS** |
| Payout recipient personal data | ❌ | ❌ | ❌ | ❌ | **Never without legal review** |

### Email Verification (Optional Confirmation Tool)

Fin's native email verification code flow is available but is **not a mandatory gate** for standard payment data. It is used in the following circumstances:

- **Level 0 (unidentified)**: Fin may offer step-up as an attempt to confirm inbox ownership before routing to human — but confirmation of inbox ownership alone does not authorise payment data without org identification
- **Specific data types**: If Security determines during policy review that certain data types require step-up even at Level 1/2, the flow can be applied selectively
- **Audit and compliance**: Where a specific interaction warrants a higher assurance record

```
When step-up is triggered:

1. Fin sends a verification code to the requester's email address
   from a separate verification sender (not the support thread address)

2. User replies to that verification email with the code
   → Fin reads the reply and verifies the code
   → Identity confirmed to inbox level
   → Note: this is a separate thread from the original support
     conversation; the merchant must check for and reply to
     a different email to complete verification
   → Fin proceeds based on the underlying identification level —
     inbox confirmation alone does not change the data entitlement
     if org identification has not been established

3. Step-up not completed (no reply / timed out):
   → Fin routes ticket to human agent
   → Fin adds note to ticket explaining context
```

### Standard Payment Response Pattern

Every payment lookup response from Fin follows this structure:

```
1. Plain-language summary
   "Payment [ID] was declined on [date]. Outcome: Insufficient funds.
    The card issuer rejected the authorisation request."

2. Direct Dashboard link
   "View full payment details in your Dashboard: [deep link to payment]"
```

The email response is intentionally minimal — enough to answer the immediate question. The Dashboard link is always included and serves as the path to full transaction detail, dispute management, and any action the merchant needs to take. This pattern keeps data in email to the minimum necessary, drives Dashboard engagement, and reduces the need for Fin to return progressively more data over email.

Deep linking to a specific payment requires the merchant to be authenticated. If not already logged in, the link should route them to the Dashboard login page and forward to the correct payment record.

### Shared Inbox

Agents already return payment data to shared inboxes; Fin aligns with that. CC exclusions route high-visibility threads to humans. Fin returns minimum data (status, outcome, Dashboard link); no consumer PII or PANs.

### Technical Components

| Component | Detail |
|----------|--------|
| Auth level classifier | Ticket creation → Salesforce + Dashboard + domain lookup → tag ticket. Engineering. |
| Fin verification flow | Native verification code; config only; Security review before data gating. |
| Fin config | Reads `fin_eligible`, `fin_auth_level`; applies rules. Config only. |
| Audit log | Log all data responses (ticket, timestamp, level, type). Engineering. |

### APIs & Integrations

- Existing Salesforce + Dashboard user lookup (leverages identification work already in flight)
- Checkout.com payments data API:
  - `GET /payments/{id}` — look up payment by Payment ID
  - `GET /payments?reference={ref}` — look up payment by merchant Reference (may return multiple results)
  - Scoped read-only access; Fin must be constrained to payments belonging to the identified merchant org — cross-merchant lookup must be prevented at the API permission level
- **Dashboard deep link**: Every payment response must include a direct URL to the payment record (e.g. `dashboard.checkout.com/payments/{id}`). Confirm with Dashboard Engineering that stable deep link URLs exist for individual payment records.
- **(P2) Settlement status API**: endpoint to retrieve status of pending/recent settlements for an identified org (e.g. settlement date, amount, processing state). API endpoint and scoping TBC with Engineering. Policy approval required before enabling.
- **(P2) Balance API**: endpoint to retrieve current available balance for an identified org. API endpoint and scoping TBC with Engineering. Policy approval required before enabling. Dashboard deep link to the Balances section to accompany all balance responses.

### Zendesk Configuration

**Ticket fields set by Zendesk triggers:**
- `fin_eligible` (boolean) — set by exclusion triggers on ticket creation; Fin config reads this field before engaging
- `fin_auth_level` (0–3) — set by the identification classifier on ticket creation; Fin config reads this to determine data entitlements

**Zendesk triggers:**
- **Exclusion — Checkout.com staff on CC**: on ticket creation, if any CC'd address has domain `@checkout.com` → set `fin_eligible = false`
- **Exclusion — high CC count**: on ticket creation, if CC count > 2 → set `fin_eligible = false`
- **Identification classifier**: on ticket creation, run Salesforce / Dashboard / domain mapping lookup → set `fin_auth_level` (0–3)
- **Step-up verified**: when OTP is confirmed → update `fin_auth_level` if applicable


## Out of Scope

- Fin Dashboard behaviour (Level 3 unchanged); Standard tier (no email entitlement); Consumer/B2C; voice/chat auth
- PAN/consumer PII return (hard limits); mandating Dashboard for ops (would help Level 2 but out of scope)


## Launch Plan

- **Phase 1 — Policy approval**: Draft data classification policy and OTP flow spec; submit to Security and Legal & Compliance for sign-off. No code written until this is approved. Estimated effort: 2–3 weeks.
- **Phase 2 — Authentication classifier**: Build and deploy the identification classifier that tags Zendesk tickets with auth level (Salesforce + Dashboard + domain mapping lookup). This is a dependency for all subsequent phases. Estimated effort: Engineering scoping required.
- **Phase 3 — Fin verification flow configuration**: Configure Fin's native email verification code flow to gate data access at the correct auth levels. Security review of Fin's native OTP implementation must be completed in this phase. Estimated effort: 1–2 days configuration + Security review timeline.
- **Phase 4 — Fin data policy enforcement**: Configure Fin with data policy rules; test all levels including negative cases (Fin correctly declining out-of-policy requests). UAT with Care Operations. Document: data classification policy (Security / Legal sign-off), agent guidance on what Fin handles vs. what routes to human, and merchant-facing guidance on the verification step.
- **Phase 5 — Limited rollout**: Enable on a controlled set of email tickets (Premium/Enterprise only); monitor auth completion rates and escalation patterns.
- **Phase 6 — Full rollout & monitoring**: Enable across all email tiers; establish ongoing audit log review cadence.

**Rollback**: Disable Fin data return on email (FAQ-only) via config; investigate. No code rollback.


## Risks, Dependencies & Open Questions

**Dependencies**:

| Dependency | Owner | Status | Risk if Delayed |
| --- | --- | --- | --- |
| Data policy approval by Security | Security | Not started | Blocks all data-return capability — hard gate |
| Data policy approval by Legal & Compliance | Legal & Compliance | Not started | Blocks all data-return capability — hard gate |
| Salesforce + Dashboard identification classifier | Engineering | In flight (domain mapping PRD) | Blocks auth level tagging; OTP step-up partially compensates |
| Fin native email verification flow | Fin (Intercom) — configuration only | Existing capability | Security review of native implementation required before use |
| Fin data policy enforcement configuration | Zendesk Admins / Engineering | Not started | Blocks safe data return |
| Payments data API read access scoped for Fin | Engineering | TBC | Blocks transaction-level lookups |
| Dashboard deep link URL format for payment records | Dashboard Engineering | TBC | Blocks the standard response pattern |
| Settlement status API read access scoped for Fin | Engineering | TBC (P2) | Blocks settlement status lookups on email and chat |
| Balance API read access scoped for Fin | Engineering | TBC (P2) | Blocks balance lookups on email and chat |

**Risks**:

| Risk | Likelihood | Impact | Mitigation |
| --- | --- | --- | --- |
| Fin returns out-of-policy data due to misconfiguration | Low with enforcement layer | Critical — security/compliance breach | Policy enforcement layer is mandatory P0; negative UAT test cases required before launch; audit log enables detection |
| Fin returns transaction data to an unrelated person from the same merchant domain | Low — they would need the specific Payment ID | Low-Medium | Payment ID must be provided by the requester; data minimisation applied; consistent with agent baseline practice |
| Fin returns transaction data to a deprovisioned account on a mapped domain | Very low | Medium if account compromised | Step-up requires a reply from the inbox — a deprovisioned account cannot reply; Fin times out and routes to human |
| Compliance requirements change (PCI DSS v4, PSD3) | Medium over time | High if policy not updated | Annual policy review cadence; Legal & Compliance as standing stakeholder |
| Domain-mapped user disputes data access decision | Low | Low-Medium | Clear Fin messaging about what auth level authorises; escalation path to human always available |

**Open questions**:

- [ ] What is the approved scope of Checkout.com payments data that Fin is permitted to query on behalf of a merchant (transaction fields, dispute fields, account config)? *(Owner: Security / Legal & Compliance + Engineering — determines what Fin can actually return at Level 2)*
- [ ] Settlement status and balance API access are also required for Fin over chat (Dashboard channel) — should the policy approval and API scoping work be driven by this PRD and shared, or treated as a separate workstream? *(Owner: Charlie Wildish + Engineering — recommend treating this PRD as the driver to avoid duplicating Security/Legal approval effort)*
- [ ] Should the data policy differ by merchant tier (e.g. Enterprise merchants treated as higher-trust at Level 1 than Standard merchants)? *(Owner: Security + Care Leadership)*
- [ ] Agents currently return payment data under an existing legal basis (presumably the merchant DPA). Does that same basis extend to Fin returning the same data automatically? *(Owner: Legal & Compliance — almost certainly yes, but requires formal confirmation before launch)*
- [ ] What is the expiry window and single-use behaviour of Fin's native email verification code? Does it meet Security's requirements for gating data access? *(Owner: Security + Intercom/Fin platform team)*


## Timeline

| Milestone | Date | Owner | Status |
| --- | --- | --- | --- |
| PRD complete | Feb 2026 | Charlie Wildish | Draft |
| Open questions resolved | TBC | Multiple | ⏳ |
| Data policy approved (Security + Legal) | TBC | Security / Legal & Compliance | ⏳ |
| Auth classifier built and deployed | TBC | Engineering | ⏳ |
| Fin verification flow configured + Security reviewed | TBC | Zendesk Admins / Security | ⏳ |
| Fin policy enforcement configured | TBC | Zendesk Admins / Engineering | ⏳ |
| UAT complete | TBC | Care Operations | ⏳ |
| Limited rollout (Premium/Enterprise) | TBC | Care Operations / Engineering | ⏳ |
| Full rollout | TBC | Care Operations | ⏳ |


## Appendix

- `01-knowledge-base/processes/known-challenges.md` — Email authentication gap and AI resolution rate constraint (full analysis)
- `01-knowledge-base/processes/ai-agent-operations.md` — Fin AI Agent operations, email pilot findings, AI resolution rate context
- `04-active-work/roadmap-items/zendesk-org-domain-mapping-prd.md` — Domain mapping and user identification hierarchy (authentication classifier dependency)

| Level | How established | Org data | Transaction data | Consumer PII / PAN |
| --- | --- | --- | --- | --- |
| 0 — Unidentified | No match anywhere | ❌ | ❌ | Never |
| 1 — Domain-mapped | Email domain matches org record | ✅ | ✅ — consistent with agent practice | Never |
| 2 — Known contact | Salesforce/Dashboard match | ✅ | ✅ | Never |
| 3 — Dashboard session | Authenticated Dashboard login | ✅ | ✅ (full) | Never |
