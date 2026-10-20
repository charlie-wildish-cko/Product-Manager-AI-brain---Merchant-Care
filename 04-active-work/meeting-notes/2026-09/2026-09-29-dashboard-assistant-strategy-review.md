# Dashboard Assistant Strategy Review

**Date:** 2026-09-29  
**Attendees:** Aman Khare (presenter), Charlie Wildish, Joseph El Choueiri (analytics assistant), Mark Boulton, Sammie Spector, Chrisi Webster (in-page guidance), Irene Liao, Andrew Stager, Alcinda Lee, Veronika Galkina, Carolina Corvo, Pierre Roudaut, Gbemi Abijo, plus unnamed speakers. Anna (MCP security) not present.  
**Drive source:** 1Ikor_M3rIkPqdQav2xcSkrsg2keBq8IJohlDox4CM-M

## Context

Review of Aman's strategy doc for a single merchant-facing Dashboard Assistant. Charlie commented on the doc ("UI versus AI" and the Fin data-source point were cited).

## Key Points

**Proposal**
- One Dashboard Assistant as the start of the merchant AI journey, powered by specialist agents: help (help MCP plus docs), pay-ops (MCPs in public beta), analytics (live, owned by Joseph), support (powered by Fin). Disputes and reporting MCPs are being built by other teams.
- An orchestrator interprets intent and routes to agents. It is P0 for the dashboard core team.
- The assistant will not answer everything at launch (no fraud agent, for example). Expectation-setting is a UX requirement.
- Aman proposed that support ticket volume prioritise which MCPs and agents are built next.

**Governance**
- MCPs sit under a Checkout MCP domain with security validation led by Anna. The analytics assistant has no MCP framework today. Ownership of a global plug-in framework is undefined.
- Charlie flagged a data-source mismatch: Fin uses one source, the pay-ops MCP another. Fixing it is MCP-team work.
- A senior data voice: agents launch only on verified, documented data products.

**Fin coexistence**
- Aman: Fin goes "behind the scenes" as one agent, not a second homepage assistant. A month ago the team assumed Fin could not be integrated. Fin APIs now exist.
- Concerns: users will not know which assistant to use, and answers could conflict across search bar, Fin, orchestrator and a future payments decoder. One attendee accepted a short overlap period.

**UI vs AI**
- Undecided per action (bulk refund is live in the UI and needs confirmation). Aman: "AI and UI", not replacement, including H1. Enterprise and SMB differ in comfort, and SMBs show tech distrust.
- Roughly 70% of support queries are basic. Chrisi's in-page guidance project aims to stop users jumping straight to a ticket or Fin, and an assistant could undercut it. Division of labour across guidance, assistant and Fin is not agreed.
- Joseph: analytics assistant token cost is "surprisingly extremely cheap" (about 5,000 users, no B2C). Penetration is 10% from the payment lifecycle page because merchants miss it or will not wait for load, and a bounce is not recorded as a conversation.

**Scope**
- Minimum Lovable Product: at least as good as Fin today, answers basic payment and status questions, unanswerable queries fall back to a support ticket, query data feeds an improvement flywheel. Internal rollout first this quarter with quality bars before external release.
- 2026 and 2027 scope is the existing live MCPs and agents. Open: which actions to allow (for example refunds), and source transparency.

## Insights

- Fin becomes a hidden support agent under the assistant, moving from visible Dashboard Messenger to an API integration. Care owns the effort estimate with Aman.
- Care contact data and taxonomy are named inputs to the dashboard AI roadmap.
- Support ticket creation remains the safety net, so Care absorbs assistant-originated escalations.
- Three deflection layers (in-page guidance, assistant, Fin) lack a division of labour.
- Decisions (aligned): single assistant with multiple agents, dashboard core team builds the orchestrator, Fin kept behind the scenes.
