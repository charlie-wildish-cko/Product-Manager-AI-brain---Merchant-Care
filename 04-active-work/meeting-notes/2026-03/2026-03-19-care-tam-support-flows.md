# Care & TAM Support Flows / AI Ideas

**Date:** 2026-03-19  
**Attendees:** Charlie Wildish, Charles Forson, Joel Petrosino, Oliver Westlake-Simm  
**Drive source:** 1t0_mzoQcTJWf6lEp5RKsK0xHieYQGVa2bU

## Context

Discussion on automating internal commercial/TAM ticket volume — a distinct support segment separate from merchant-initiated contacts.

## Key Points

- 8–10% of annual support tickets originate from internal commercial personnel (TAM/sales), not merchants.
- Proposal: content-based AI agent to triage and resolve these queries before they reach care agents or L3 engineers. Access to centralised public-facing content (tech docs, support articles) via GitHub repository.
- Preferred interface: Slack bot embedded in the commercial team's existing workflow. Falls back to human support with pre-populated metadata if unresolved.
- Reducing L3 escalations is the primary cost driver — not just care agent time.
- Success target: 50% reduction in internal ticket volume (from ~8–10% down to ~4% of total).

## Insights

- Internal commercial queries are a distinct, material, and quick-win automation target. They are separable from merchant-originated contacts and can be tackled independently.
- The Slack-embedded agent pattern (meeting the user in their workflow without forcing a channel change) is worth carrying into Agent Consultant design thinking.
- Maps to the Orchestration flywheel stage — reducing volume before it reaches care agents entirely.
