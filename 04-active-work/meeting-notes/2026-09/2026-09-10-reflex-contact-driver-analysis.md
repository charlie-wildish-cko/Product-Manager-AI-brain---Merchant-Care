# Harlie / Charlie catchup - Reflex contact driver analysis

**Date:** 2026-09-10
**Attendees:** Charlie Wildish, Harlie Patel
**Drive source:** 19J4Pu_xe1sJs26It7qRyNy4s-TwA0qqagY74RXLaRpo

## Context

Catch-up covering Harlie's first analysis assignment on Reflex support data, plus the monthly operational update going to the COO and CPO.

## Key Points

**Monthly update**
- Charlie is preparing the monthly operational update for the COO and CPO (Jenny) for the following Monday. It includes the recommendation to replace Zendesk. Charlie explicitly wants more due diligence first to avoid appearing narrow-minded.

**Org dynamics**
- Historical friction between operations leaders and product teams, but the current relationship is strong and aligned.
- Support drivers and support-team requests have sometimes been delayed or deprioritised by product teams. A leader is organising a session to investigate why.
- Communication framing: tailor detail level by audience (ops versus product) using the framework in the onboarding plan.
- Elevate Profiles is the PM competency framework by level. Harlie sits at associate level for upcoming goal setting.

**Harlie's assignment**
- Review Reflex support data to understand customer problems, reduce resolution friction, automate with AI where possible, and push unresolved issues back to originating teams.
- Reconciliation analysis: high-cost tickets where merchants see discrepancies caused by time zones, fees, currency rounding, and day-boundary reporting differences. Proposed fixes: make reports easier to reconcile, add a sorting process to filter out harmless discrepancies, and give weekly breakdowns with transaction-level drill-down for self-sufficiency.
- Method limitation acknowledged: manual review of a small sample (top 10 highest-cost tickets, top 10 most recent, plus a couple of random) with no BigQuery access.
- 3DS analysis: a significant volume of merchant tickets. Charlie's framing: 3DS is mandated in Europe and the UK and can be frictionless or challenge based on risk analysis. Merchants misconfigure it or misread decline codes. Error codes 20151-20156 relate to 3DS. Codes around 4000000 indicate internal declines. Issuer declines originate at the cardholder's bank.
- Charlie's coaching points: verify merchant dashboard access and replicate the merchant problem directly; use merchant IDs from Zendesk tickets to cross-reference the dashboard; identify which internal teams (L1, L2, engineering) touched each ticket, since cross-team involvement is the key cost driver and the basis for prioritising pain points.
- Deliverable goes to PM Alexa.

**Decisions**
- Target completion of the initial report and PM handover by end of the following week, with recommendations, suggested actions, and an appendix of supporting detail.

## Insights

- The first Reflex-driven contact-driver analysis is being produced by an associate PM with no BigQuery access and a ~22-ticket manual sample. The findings need caveating before they reach Alexa or leadership.
- The reusable methodology point is Charlie's own: cross-team involvement per ticket is the cost signal that should rank pain points. That is exactly the Reflex accountability thesis, and it is not currently a Reflex dimension.
- The Zendesk replacement recommendation goes to the COO and CPO on 2026-09-14, ahead of the end-of-month procurement decision described in the Sunil 1:1. The due-diligence gap Charlie names is the platform assessment document itself.
- Reconciliation discrepancy causes are now enumerated (time zones, fees, currency rounding, day-boundary reporting). Most are presentation problems, not data problems, which makes them addressable through reporting changes rather than engineering.
- 3DS decline-code ranges (20151-20156 for 3DS, ~4000000 for internal declines) are concrete enough to seed a Fin procedure or support article.
