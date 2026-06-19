# Francisco / Charlie — Glean Pilot + AI Data Layer

**Date:** 2026-04-20  
**Attendees:** Charlie Wildish, Francisco Goncalves (L2 Ops lead)  
**Drive source:** 1DooP6y3770ML0rK2GxwVV9n2Be-y8BepQuK8yC660bw

## Context

Catch-up between Charlie and Francisco on two topics: (1) piloting Glean as an AI knowledge search tool for the L2 team, and (2) mapping the AI data layer for payment explanations.

## Key Points

**Glean pilot**
- Glean is an AI knowledge search tool being piloted company-wide, already integrated within Zendesk with 2–3 spare licenses.
- Features: ticket summarisation, next-step generation, draft responses, cross-system search (Confluence, Jira, Slack, Zendesk, BigQuery). Positioned as superior to Fin Copilot.
- Fin Copilot has not reduced L2 average handling time — difficult to sell to the team after past failures.
- Agreed to pilot with Hanzo (L2 agent, China — smart, proactive, curious; ideal tester).
- Data governance: search scope to be limited to checkout.com public site + curated Zendesk knowledge base.

**AI data layer for payment explanations**
- Charlie described the mapping table approach: payment method status + response code + authentication status → human-readable English description. Fin calls this table when querying a payment ID.
- Agreed: 2-hour post-leave workshop (Francisco, Kazia, Joly, Jonathan) to build scenario cards for top 5–10 payment issues.
- Francisco recommended: focus on card schemes and TPA issues; exclude APM refunds (mostly bugs, manual work, not suitable for codification). Authentication is straightforward.

**FDS calculation tool**
- Francisco requested approval to build a Claude-based app to reduce laborious manual FDS (Fraud Detection System) calculation (currently 3+ hours → target 30–15 minutes per ticket).
- Charlie approved with one requirement: design as a reusable API service, hookable into Zendesk later — not a siloed app.

**Root cause signal from Francisco**
- Reconciliation tickets arise because the dashboard doesn't meet merchant needs, not because AI is insufficient: "Invoices should be clearer, dashboard should be better — that's the thing. Report should be something self-served. If they're coming to us in a complex way it's because the dashboard is not doing a good job."

## Insights

- Current AI tools (Fin Copilot) have not reduced L2 average handling time. Complex tickets are edge cases; Fin Copilot adds little for these.
- Glean vs Fin Copilot is a live comparison that may affect the Agent Consultant / knowledge search layer decisions in the Zendesk platform RFC.
- The root cause signal from Francisco (dashboard failures driving reconciliation contacts) is exactly what Reflex should be surfacing systematically to the dashboard product team.
- Ops team is self-building Claude-based tools (FDS calculator). Without architectural guardrails, these risk becoming isolated non-reusable workarounds — Charlie's API-service constraint is the right intervention.
