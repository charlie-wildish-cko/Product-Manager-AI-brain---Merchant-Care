# AI Assistance on Dashboard

**Date:** 2026-10-13  
**Attendees:** Joseph El Choueiri (lead), Chrisi Webster (designer), Charlie Wildish, Pierre Roudaut, Andrew Stager, Gbemi Abijo, Veronika Galkina, Burak Akkor (engineer), Justin Thomas. Some speakers unattributed (LON-03-01).  
**Drive source:** 1yJGZR7FmV6GSsCYyUXhN_ARaNj3cAxjAnxNDlUdGKCs

## Context

Dashboard product planning for AI across four pillars (onboard, implement, monitor, manage). No onboarding product exists and almost no implement features, so AI focuses on monitor and manage.

## Key Points

**Three AI tool types**
1. Explainer: an advanced tooltip on a decline code, dispute code or ARN. No payment context, pulls from the docs MCP. Chrisi has a prototype. First rollout scoped to payment statuses and decline reasons.
2. Decoder: context-applied one-liner on the payment detail page (e.g. declined for insufficient funds, hard decline, will not retry). Tied to the payments revamp.
3. Conversational orchestration layer: one interface merging Fin, the analytics assistant and other agents. Joseph: a separate chatbot is not the priority, since Fin exists.

**Orchestration layer**
- No technical discovery done on Fin integration. Engineering is building its own agent on the Checkout MCP tools, short-term session storage, queries stored to tune prompts, evaluating AWS Bedrock.
- Charlie: the Fin widget holds auth, token and logic. Next year Care moves to Fin's API product for email. Fin can be called via API and acts per Care's config. Fin could be exposed as an MCP tool. Fin should end in a resolution or support handover, so handing back to another agent is harder. Charlie asked for roadmap items affecting Care because H1 next year is busy.

**Timeline (Joseph)**
- Q4: build decoder, improve analytics assistant UI, rough test UI by end of Q4.
- Q1: release decoder, technical discovery on Fin and other agents.
- Q2: release orchestration layer if discovery succeeds. MVP is Fin plus the analytics assistant.

**Actions and liability**
- Conversational AI should not execute payment actions (refund etc.) where UI buttons exist. Fix the UI instead.
- The Checkout MCP is strictly read-only. Capture, refund and payment-link tools were removed to ship in the Anthropic directory because Anthropic declined liability.

## Insights

- Fin is to be absorbed into a dashboard orchestrator (Q2 target). Care owns Fin config, so Care needs to be in the discovery.
- Explainer, decoder, conversation, then human is the dashboard-side deflection model.
- The read-only MCP constraint shapes any Agent Consultant idea needing MCP actions.
- Decisions: consolidate conversational AI into a single interface (Fin plus analytics assistant). Keep the MCP read-only for payment actions.
