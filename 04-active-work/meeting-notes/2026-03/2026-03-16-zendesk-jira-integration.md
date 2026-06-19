# Zendesk & JSM/JIRA Integration Kick-Off

**Date:** 2026-03-16  
**Attendees:** Charlie Wildish, Karan Jagmohansing, Ajay Paul, Ana Cachapa Cuomo, Ramyaa Ranganathan, Arnold Sadrijaj  
**Drive source:** 191nXpfyhiPhHpdTpoA3zih9-qOu9aS5LaXIJIPZzjRc

## Context

Kick-off for a Zendesk-to-Jira/JSM integration using an existing marketplace app. Problem: 5–10% of merchant care tickets require engineering team (L3) assistance and frequently breach SLAs. Agents currently manually create Jira tickets and copy-paste information.

## Key Points

- 5–10% of total volume requires L3 escalation to engineering. At 40,000+ contacts/year, this is thousands of tickets; they tend to be more complex and SLA-breaching.
- Today: agents manually create Jira tickets, input fields, then manually link the Jira URL back into Zendesk — significant waste.
- Proposed flow: agent creates a Jira ticket directly from Zendesk with fields auto-populated (summary, description, priority, client ID, client name, ticket ID, SLA). Bidirectional sync: care sees Jira status and comments; Jira sees Zendesk merchant context.
- Critical field from Ramyaa's team: "Is this a merchant care request?" (yes/no, mandatory in JSM form) — all SLA population and field flows trigger only when set to "Yes."
- Constraint: no dedicated Jira sandbox exists. Arnold to create a sandbox project in production Jira to isolate PoC from real tickets.

## Insights

- This is workflow automation, not AI. It doesn't reduce contact rate but eliminates waste in the handling of a high-complexity, SLA-critical 5–10% of volume.
- Bidirectional visibility (agents seeing Jira status without leaving Zendesk) is directly consistent with the Agent Consultant vision — context surfaced within the agent's primary workspace.
- Key stakeholders: Ana Cachapa Cuomo (Zendesk admin), Arnold Sadrijaj (Jira/JSM config), Ramyaa Ranganathan (engineering/L3 internal customer).
