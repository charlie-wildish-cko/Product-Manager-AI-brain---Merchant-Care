# Analytics: Proactive Trends

**Date:** 2026-09-16
**Attendees:** Karan Jagmohansing, Ashvin Pudaruth, Joanie Vencatasamy, Charlie Wildish, Francisco Goncalves, Tim Win, Ling Wong
**Drive source:** 1XXK_Gu2rsNXb5CcRk9di6pFbCkHwZP4pi-0dE4zLxHc

## Context

Designing the reporting layer Care needs: daily execution monitoring, trend analysis for capacity planning, and proactive breach alerting. Gemini anonymised all transcript speakers as "LON-03-09", so attribution below is only where Gemini named someone.

## Key Points

**Two-dashboard split**

1. **Daily execution dashboard:** tickets received/solved/on-hold, SLO %, day-over-day arrows, drill-down to examples. Scheduled 9:00 AM delivery, layered by leadership / team / IC.
2. **Trend dashboard:** case types, merchant activity, abnormal internal-dependency rates, inbound volume, high-priority ticket growth, pickup times, YoY/MoM for capacity planning (Black Friday was miscalculated previously).

- Today's problem is navigating several reports to answer "what happened yesterday". Looker refreshes every 2-3 hours, near-live enough for start-of-day monitoring. Idea raised: plug in Looker MCP for an AI anomaly summary.

**Proactive breach alerting**

- No Looker report currently shows minutes-to-breach per ticket. Zendesk views show SLA budget per ticket but cannot be monitored in aggregate.
- Want alerts for internal dependency teams (Treasury named), e.g. "10 tickets will breach today if you don't act".
- Alerting within Zendesk is hard because Zendesk lacks the feature **Plain demoed to them**. Workaround is scheduled Looker distribution lists per dependent team.

**Leading indicators for ticket spikes**

- The Remitly volume surge was driven by transaction-count/TPV growth, not error rates: flagged payments stayed at 3%.
- Proposed additional leading indicators: merchant onboarding pipeline, Genesis records, platform entities, incident-impacted merchant thresholds via the operations control centre.

**Regional SLO reporting**

- Quarterly requirement: map tickets by primary legal entity ID across UK (LTD), France (SAS), APAC/Singapore, Hong Kong, and "Blue". Unmapped tickets distributed proportionally across mapped regions. Joanie to supply the definitive 4-region list.

**Data quality**

- **External-dependency calculation bug:** running a second macro on a ticket overwrites "waiting on external" with an internal dependency, so external delays are wrongly charged to internal teams and depress SLO. Joanie to send ticket examples, Tim to trace root cause in code.
- Looker's opacity drives teams to build fragmented workaround reports. Tim to write a plain-English document of the data model and lineage.
- SLO dashboard filters currently exclude test, deleted, no-action-required, knowledge-request and QA tickets. A recent taxonomy change nested legacy issue types under General Inquiries, so spam / no-action-required filters need updating.
- **Looker explore fragmentation:** Imran built performance dashboards and the attribution model on the **Zendesk agent performance** explore; Joanie built hers on the **support contract** explore. No field parity or filter alignment, so numbers diverge. Only those two explores should be used and Looker must deliver field parity. Separate complaint: engineers change data models without notice, to be escalated to Pal and engineering.

**Fin in SLO scope**

- Contact workflows split three ways: Fin-only resolutions, Zendesk-to-Fin escalations, Fin-plus-human. Fin-only resolutions are instant and therefore sit at 100% SLO.
- Charlie's earlier objection was recorded: including them inflates the headline and looks like gaming. The counter-argument that carried: human-only SLO is expected to fall to ~60% next year, and merchants experience the blended service.
- Fin/human edge cases: breaches occur when Fin picks up a ticket after it is marked solved (chatbot and account-unlock flows). Transfer rate to L2 is low, ~10%. Naming between "Zendesk-to-Fin" and "Fin-to-Zendesk" in the data model needs clarifying.

**SLO downtrend diagnosis**

- Decline since June/July is driven by volume outpacing capacity, not harder work. Ticket mix was flat-to-easier (a figure moved from 18% to 14%), and auto-routed tickets show higher FCR than manually routed ones.
- Ticket volume dropped from May and July after routing changes and a higher ticket-creation threshold. Need a throughput metric: cases solved per agent.

## Decisions

- Build two separate dashboards (daily execution, long-term trend) plus alerting on trend parameters.
- Include Zendesk-to-Fin automated resolutions in SLO metrics, with a **decoupled two-line reporting structure**: human line and automated line shown separately.
- Zendesk agent performance explore to be confirmed as the primary source for performance scorecards.

## Insights

- The decision to include Fin resolutions in SLO is defensible only because the two lines stay decoupled. If the decoupling slips, the headline SLO becomes uninterpretable and the inflation objection returns.
- Human-only SLO is forecast to fall to ~60% in 2027. That is the number to plan automation and headcount against.
- The SLO decline is a capacity story, not a complexity story. Evidence: stable-to-easier mix, higher FCR on auto-routing.
- Zendesk cannot do dependency-team breach alerting; Plain demoed that it can. A concrete, operator-sourced datapoint for `04-active-work/research/zendesk-platform-decision-rfc.md`.
