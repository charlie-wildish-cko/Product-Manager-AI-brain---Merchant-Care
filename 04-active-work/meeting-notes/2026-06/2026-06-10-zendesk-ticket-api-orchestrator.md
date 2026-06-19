# Access to Create ZD Ticket Endpoint

**Date:** 2026-06-10  
**Attendees:** Charles Forson (commercial/AM AI), Jiro Farah (Engineering), Charlie Wildish  
**Drive source:** 1WpBWrNjt8Kh7weGhGlBtxmvXGPiMSMAOxOqUa9Ne9oM

## Context

Technical and architectural alignment on Charles Forson's Slack-based AI orchestrator for commercial/AM queries. The orchestrator needs to create Zendesk tickets on behalf of AMs — requiring a public-facing gateway to the internal ZD API.

## Key Points

**Charles's orchestrator**
- Takes a merchant query from an AM, runs upstream checks (DataDog, product catalogue in Airtable, public docs), routes to the right support channel, or creates a well-formatted ZD ticket if the issue needs to go to Care.
- Goal: by the time a ticket lands in Care, the analysis is already done (DataDog links, issue categorised, routing correct) — reducing L2 and L3 legwork.
- Human-triggered ticket creation: AM clicks a button after the bot completes its diagnostic flow. No fully automated creation at this stage.

**Division of responsibility**
- Charles's team: upstream analysis, well-formatted ticket with consistent schema.
- Care/Jiro's team: downstream routing, escalation logic, optimisation.
- Consultant bot will not add suggestions to Slack threads to avoid duplication.

**Technical blocker**
- ZD ticket creation API is internal-only. A public-facing gateway is needed for Slack to call it.
- Jiro to investigate whether Maring's performance bot architecture (which accesses services behind Cloudflare from Slack) can be reused. New build may require ARB approval.

**A2A alternative**
- Jiro: rather than building a gateway, use Fin as the downstream agent. Charles's upstream agent passes context to Fin via A2A protocol; Fin creates the ticket. Removes the gateway requirement. Charlie was sceptical about A2A maturity.

**Timeline**: late Q3 or Q4 2026.

## Insights

- Cost per Fin resolution confirmed at $0.93 in this session.
- The Charles orchestrator is an adjacent AI product (commercial/AM-facing) converging with Care's Agent Consultant. Worth treating as an integration opportunity rather than a separate initiative — both create well-structured Zendesk tickets from upstream analysis.
- A2A protocol is on the table as a gateway alternative — architecturally cleaner if Fin already has ZD ticket creation capability.
- L3 gating through L2 is confirmed. The orchestrator improves L3 routing quality but does not bypass the L2 gate.
