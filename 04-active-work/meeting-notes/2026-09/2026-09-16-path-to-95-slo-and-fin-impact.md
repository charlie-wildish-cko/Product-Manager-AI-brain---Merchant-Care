# Path to 95% SLO and 2026 Fin Impact

**Date:** 2026-09-16
**Attendees:** Ashvin Pudaruth, Karan Jagmohansing, Joanie Vencatasamy, Charlie Wildish, Francisco Goncalves, Ling Wong, Joel Petrosino, Harlie Patel
**Drive source:** 12Nn0cd-69StmF1QKWY18bk3jeUa1U_oKQipMO9uz4g4

## Context

Whether Care can reach a 95% SLO, and how much Fin contributes in 2026. Gemini attributed most non-Charlie speech to the room LON-06-11, so individual attribution below is unreliable.

## Key Points

**Three levers to 95%**

1. Fin coverage.
2. Separate Zendesk SLOs for internal-dependency teams where 24-48h turnaround is impossible, with merchant expectations reset.
3. Piloting the config bot.

- **17% of dependency tickets are merchant configuration.** Treasury plus billing plus config would clear most of the dependency problem. Needs a drill-down on what the config bot can actually solve.

**Fin metrics**

- Involvement rate hit 30% in August then dropped. Overall automation rate 16% excluding Remitly, 21% including. Automation rate = involvement rate x resolution rate.
- The August drop is unexplained and possibly a data artefact. Charlie disputes a reported ~40-41% resolution-rate drop: Fin's own data shows something different. Hypothesis: Remitly volume surge shifted mix into lower-performing reason codes. Payment verification / status checks went from 148 (July) to 897 (August). Charlie to query with Locky.
- Data quality problems: refund reversal showing 100% Fin resolution indicates deflection, not resolution. Issue types and reasons are mixed in the report and denominators need fixing.
- **Involvement ceiling is ~70-80%.** The remaining 20% is AM-originated, WeChat and IM tickets (~10% each) that Fin cannot touch today.
- Channel coverage: in the Dashboard Fin handles everything. On email Fin only responds to certain reasons (e.g. payment authentication). Removing the webform pushes more volume into Fin.
- Payment metadata over email has no InfoSec blocker (no PCI/PII). Settlement and balance amounts await a GPO decision. Charlie's team is building the email authentication piece, still planned for this year.
- Charlie rejected redirecting email answers to the dashboard: top-tier merchants expect a reply in email and added friction would be resented. Tier 4/5 merchants already get the dashboard-only experience.

**Commercial pushback on AI**

- MENA and UK commercial teams report merchants frustrated with "generic and AI-generated responses". Some stakeholders including Tier 0 / private-emerging asked to turn AI off entirely.
- Charlie's position: account managers often misattribute non-Fin responses to AI. Feedback must come with specific examples so correctness can be tested. Where answers are wrong, that is a content gap to fix.

**Operational effort analysis (agent hours x AHT)**

- **Manual refunds / refund failed = 7% of total Care volume but the number one driver of manual effort.**
- Fee inquiries: fully automatable once transaction-level fee data is available to Fin.
- Payouts / declined payout: highly solvable.
- Account updates: too varied, needs breakdown.
- Sandbox and risk rules: too unpredictable, keep human.
- Reconciliation: a product fix, not an AI fix. Babak and Angelica on dashboard self-service; Harlie analysing recon data.
- API 4xx solvable, 5xx is a Checkout problem.
- 3DS liability shift: legally sensitive, human-driven. Harlie investigating.
- IDV and account migrations: complex but low volume.
- Apple Pay / Google Pay / plugin integration: mostly documentation guidance, concentrated in lower tiers.

**SLO mechanics**

- Fin-only resolutions appear to be excluded from the reported SLO. They were intended to be combined, but the change may never have been made. Confirm with Tim.
- The one-ticket-at-a-time routing change moved the delay from mid-ticket to ticket start, making the bottleneck visible. Merchant service is slightly faster but not where they want it.

## Decisions

- Short-term Fin optimisation indexes on **Accepting Payments and Payouts** case types, targeting consistently above 80% resolution there.
- **No per-merchant AI toggles.** Taxonomy-level exceptions are acceptable. Merchant-level on/off breaks reporting consistency and is unmaintainable.
- Fin target: **40% this year (holding), ~60% next year** (+20%, not +30%, because of diminishing returns). Charlie to produce a more accurate forecast.
- Shift content measurement to volume-based: article performance by Fin volume and resolution per article, used to build the content team's backlog.

## Insights

- The path to 60% Fin resolution next year runs through **backend execution, not better answers**. Manual refund and refund reversal are the named candidates (~+10% resolution) because Fin can call backend systems, do the work, then inform the merchant. For manual refunds, Fin pulls and posts the data and a human validates entries.
- Involvement is near its ceiling. Future gains come from resolution rate, which means solving more types of problem, not covering more channels.
- Charlie's position on AI pushback is a usable precedent: correctness is the standard, not sentiment, and no merchant-level opt-outs.
- Reconciliation and settlement-ID discoverability are explicitly refused as AI problems and pushed back to Product for accountability.
- Fin's automation figure is stated three ways across meetings this week (16% excluding Remitly, 21% including, ~25% involvement in the Plain Vision session against 30% August involvement here). Reconcile before any of these go into a document. The decided year-end target is the one agreed here: 40% this year, 60% next.
