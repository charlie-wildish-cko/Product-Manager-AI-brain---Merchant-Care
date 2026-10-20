# Agent X Adoption Check-in

**Date:** 2026-09-11
**Attendees:** Charlie Wildish, Joel Petrosino, Claudia Zheng, Tasha Richards, Anthony Tsoi, Raymond Guo
**Drive source:** 182vVGEIqO-6PG1AGRRobiHj6eBCzFIsca1m1rmtcV0A

## Context

First check-in after Agent X rolled out to Merchant Care senior analysts. Agent X is a Treasury/settlements query agent built by Claudia's team, querying BigQuery tables, so analysts can answer settlement and reconciliation queries without escalating to Treasury.

## Key Points

**Adoption metrics**

- Launch happened the prior week while Charlie was out, with Joel's help, to senior leads in Merchant Care.
- **~40 to 47 queries from 7 active users in about a week, 5 ratings submitted.** There are only 8 senior analysts in total, so this is near-total capture of the eligible group.
- Raymond considers 5 ratings non-indicative and wants more thumbs up/down plus qualitative feedback.
- Joel's read: 47 queries from 7 agents in a week roughly matches normal Treasury ticket volume, suggesting use on live cases rather than exploratory work.
- Joel will run the queries against the ticket base to identify tickets and trace the lifecycle: closed by the analyst, or still escalated to Treasury.

**Expansion**

- Expansion to Analyst 2s agreed in principle. Claudia is comfortable on factual correctness and is also rolling out self-service to the commercial team. Raymond monitors a backend accuracy threshold with alerting.
- Security condition (Anthony): new users must go through the OAuth model rather than the current service-account setup, otherwise the rollout bypasses access controls. Joel believes analysts already have BigQuery access through daily Looker settlement work but will verify. Claudia: expansion proceeds only once access is verified.
- Rollout mechanics: no Merchant Care all-hands, so Joel will go via the original demo leaders Karan, Joanie and Ling, and circulate a recorded demo video.

**Architecture position**

- Charlie: Care is moving to an orchestration model. Tools are called when needed rather than each shipping its own UI. Proliferating UIs is acceptable short-term to unblock something, but long-term it forces reconciliation of interfaces holding different data and makes agents use many tools to do one job.
- Orchestration is embedded at the point of receiving support: on inbound, decide whether it goes to Fin or straight to a human, and either path can call a sub-agent. The aim is to front-load triage, because by the time work reaches a human they still have to triage again. Ad hoc human invocation of Agent X remains a valid use case.
- Interface: Charlie has no preference between API and MCP, they are "basically the same". Choose whichever is easier and more scalable, with latency mattering for customer-facing paths and less for internal.
- Agent-to-agent is not ruled out but unproven. Anthony's view: A2A helps if sub-agents overlap, but strict domain boundaries are better, so start with an API and move to A2A only if needed. Charlie may use skills on one agent rather than true sub-agents.
- Likely overlap zone: payments against settlements ("is this payment settled"), which Charlie would rather fix by consolidating the data source.
- Timing: orchestration will not land until next year because it is part of the Zendesk replatforming and new architecture. Integrating Agent X today is not easily feasible. Claudia's concern: rolling out now forms an Agent X habit that orchestration will later disrupt.

**Traceability and metrics**

- Design intent: ticket ID passed through in the payload, one Agent X session per unique ticket ID, so an unresolved query has an audit trail back to the human. If Agent X returns a "cannot solve", Care logs the failure case and both sides get metrics on where it did not help.
- Currently no ticket IDs are captured, as analysts paste queries directly, so traceability is lost. Charlie asked for ticket IDs in queries; Joel had only asked for Agent X output in ticket internal notes.
- Resolution time currently tracked in Salesforce, averaging 1 to 3 days, inflated by timezone waits for Treasury. The test is whether analysts trusted the answer, copy-pasted it and closed the ticket. Joel will track Treasury escalation reduction and SLO improvement.
- Charlie flagged that the commercial team will want the same API/MCP. Charles wants to wire tools into Glean so commercial can resolve merchant queries directly. Same pattern every time.
- Interim testing: Charlie and Joel can beta-test an MCP in their own Claude or Glean before anything is production-ready. Kzia, the level 2 lead analyst, would have been the ideal tester but is going on maternity leave.

## Decisions

- Build an API interface first for Agent X integration. Revisit A2A later if needed.
- Expansion to Analyst 2s proceeds once BigQuery access is verified and the OAuth model is followed.
- Follow-up check-in in two weeks, feedback async via Slack.

## Insights

- Clearest statement yet of Care's target architecture: front-load triage at the point of inbound, orchestrate tool calls from Fin or an internal agent, and stop agents shipping their own UIs. Orchestration is explicitly scoped to the Zendesk replatform in 2027, not before.
- Charlie is deliberately not claiming domain ownership. The orchestrator only needs to know when to call a domain agent, which abstracts away having to understand every part of Checkout.
- Every internal AI tool should expose an API or MCP from day one. Care, commercial via Glean, and Treasury all need the same thing, and standalone UIs create integration debt.
- Adoption measured against the right denominator: 7 of 8 senior analysts is near-total capture, not low usage. Useful framing for any small-population Care rollout.
- The metric that matters is Treasury escalation reduction and SLO improvement, not query count. Ticket ID capture is the prerequisite and is currently missing on both sides.
- Rolling out a standalone tool now has a known cost: habit formation that orchestration will later break. Accepted knowingly for interim benefit across three teams plus commercial.
