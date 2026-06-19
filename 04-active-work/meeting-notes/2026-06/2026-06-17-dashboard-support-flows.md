# Dashboard Support Flows

**Date:** 2026-06-17  
**Attendees:** Charlie Wildish, Joel Petrosino, Aman Khare  
**Drive source:** 1YOcVeG2yy4S8azVoxT6_4HpPKU5naX9U6Q6XEYsGVok

## Context

Working session on routing dashboard-related tickets to the correct internal team, and review of adjacent workstreams (Fin Copilot deprecation, Charles's AM portal, Milan's unified customer layer proposal).

## Key Points

**Dashboard support routing**
- Agents lack clarity on which dashboard section/page belongs to which team — leads to catch-all "ask-dashboard" escalations that waste time.
- Proposed fix: Zendesk side conversation macros linked to specific Slack channels per dashboard section. Agent clicks macro → Slack message auto-created → updates flow back to Zendesk ticket.
- ~80% of dashboard issues are quick discoveries/fixes — don't require a Jira ticket. Some teams (card processing/API acquiring) require formal Jira tickets.
- Long-term: agents search Glean/internal knowledge first; if unresolved, macro routes to correct team.
- A mapping document exists (dashboard pages → teams → Slack channels) — needs to be built into Zendesk macro architecture.

**Fin Copilot deprecation**
- Low adoption, high cost. Being phased out.
- Glean being pursued as replacement for internal knowledge retrieval. Team comms needed to explain the transition.

**Charles's AM portal**
- Charles (commercial/AM side) building an AI portal that takes merchant queries, triages them, attempts self-serve resolution, then creates a Zendesk ticket if unresolved. MCR creation via Salesforce also being automated.
- Converges with Agent Consultant scope — worth aligning.

**Milan's unified customer layer proposal**
- New workstream: merge data from all systems, create single communications record (internal and external), unify case threading across all teams so merchants see one thread regardless of which internal team handles it.
- Dashboard notifications control center (Joseph's team) is dependent on a foundational customer identity layer that does not yet exist.
- Current customer record governance is entirely manual (AMs update Salesforce) — no staleness reviews, no bounce management, no merchant self-service.

**Decision**: Zendesk macro routing strategy adopted — macros linked to Slack side conversations, mapped to dashboard sections.

## Insights

- Fin Copilot deprecation is active. This is unannounced to the team — comms needed. Affects agent tool perception and may require managing against expectations set during rollout.
- The Charles AM portal (AI triage + Zendesk ticket creation) directly overlaps with Agent Consultant scope. Aligning these prevents duplicate tooling.
- The customer identity gap is now blocking multiple teams simultaneously: notifications, comms, analytics, consumer launch, B2C regulatory requirements. Strongest cross-team case yet for the unified identity workstream.
- Milan's proposal is the leadership-level articulation of what Charlie has been building the evidence base for.
