# Nicolas / Charlie: Care and Commercial Product Partnerships

**Date:** 2026-08-14
**Attendees:** Nicolas Maalouf (Commercial Product Partnerships), Charlie Wildish
**Drive source:** 1hMufvVHFJyRHQk9D224-dtEpDIrzTSRBqWJFIYa-iEU

## Key Points

**Measurement gaps**
- The NPS survey asks a generic question about "experience with support at Checkout." Merchants read "support" as their account manager, a competitor, or a salesperson on WhatsApp. Last wave rated support very highly and leadership celebrated it, but it was not measuring Merchant Care.
- CSAT response rate is ~3% of tickets. Charlie: support CSAT is one of the worst metrics in the industry, capturing only very angry or very happy respondents. The only broad quality signal today is Fin's own AI-scored conversation assessment, which is an AI grading its own interaction.
- Only tier 4 and tier 5 merchants give a clean read on Care quality, because they have no account manager. Tier 4 AMs may cover ~30 accounts. Tier 4/5 are the proxy for future unmanaged SMB accounts, so their pain points are an early-warning signal.

**Insight tool demo**
- Tickets carry taxonomy, then an LLM plus embedding model clusters ticket content into topics, with impact and cost quantified per topic. Top topic currently: card payout stuck in pending.
- Intended end state: topics land on product teams' roadmaps. "If you are the PM for card processing, you get card payout stuck on pending on your roadmap to investigate."

**Remitly incident (week of ~2026-08-08)**
- Remitly migrated card payouts from a previous provider and ramped fast. Payouts onboarding was not properly configured and payment routes were not enabled, so volume flagged into sanctions and returned pending status.
- ~1,000 tickets in one week, roughly Checkout's normal total weekly volume. Raised as a non-tech incident. Fin resolved ~30% of it.
- Root causes: no managed merchant release/readiness gate, and Remitly's own support team untrained with no self-serve path.

**Commercial intake**
- Nicolas soft-launched an MVP of the CPP commercial intake and triage tool on 2026-08-13. Tester feedback: it needs to ingest NPS responses to detect product requests.
- Nicolas wants Care's topic-clustered ticket data as a signal source, ideally readable as an MCP. Not built yet; the tool is UI-only today.
- Charles Forson is separately leading analysis of merchant sales calls and QBRs, with Philipp's team doing ingestion.
- Alicia Hamer covers NPS while Tash leaves (Monday was Tash's last day).

## Decisions

- Give the commercial team access to Care's support ticket theme data to improve cross-functional product prioritisation.
- Wait for the current NPS wave results before changing survey framing.
- Care's signal type stays distinct: Care surfaces existing product quality issues, NPS and commercial intake surface feature requests. A joined view is the goal.

## Insights

- Remitly is a concrete, quotable case for merchant launch-readiness gating: a single misconfigured onboarding doubled weekly ticket volume.
- Charlie's framing to defend: AI resolving 30% of a bad-experience spike is not a good outcome. Fix the product cause.
- The insight tool needs a data-extract feature before commercial can consume it. UI-only is the current blocker.
