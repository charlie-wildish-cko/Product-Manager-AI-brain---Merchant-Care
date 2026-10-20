# Charlie / Joseph Bi-Weekly: Dashboard AI Duplication

**Date:** 2026-09-14
**Attendees:** Charlie Wildish, Joseph El Choueiri
**Drive source:** 191ZajVwe8VLq3JK0ENzofMy2tD-R4Aew5umI5TE-E98

## Context

Bi-weekly 1:1. Dominated by the conflict between a planned general-purpose dashboard AI agent and Fin.

## Key Points

- **AI knowledge ownership gap:** nobody owns Checkout-wide knowledge quality. Alex (Knowledge Manager) owns operations knowledge only. Charlie's framing: access to knowledge is not the same as quality of knowledge, and five-year-old Confluence docs in an AI's corpus make the AI wrong.
- **Payment Lifecycle assistant penetration is 10%** (PLC into assistant). Joseph attributes it to three causes: users do not notice it exists, latency of 10 to 30 seconds depending on merchant size and data volume, and no persistent conversation memory (every open is a fresh full-page modal).
- Joseph's Q4 fix: replace the full modal with an overlay drawer / sidenav in Analytics, retaining conversation for up to 15 minutes (the technical maximum). Full sidenav is blocked by dashboard work, so the interim is the overlay drawer. Trade-off accepted: losing visualisations, which merchants can build elsewhere.
- **Charlie's objection:** a global dashboard AI directly duplicates and conflicts with Fin. Two AI agents with unclear purposes giving different answers is an instant trust breaker. Fin costs ~$20k/year and is self-serve configurable (language, colours, customisation) without engineering involvement, which is the part hardest to replicate in-house.
- Prior approach superseded: Chrissy's proposal for low-effort inline contextual help buttons using the Checkout MCP (e.g. explain a negative balance in place, replacing docs links). That is contextual help, a one-off answer, not a chat agent. It has been displaced by a full agentic chat platform.
- Agreed guardrail: scope the Q4 build narrowly and name it honestly, "Analytics assistant", answering only "tell me about my performance". Fin remains the route for help on anything.
- Aman's doc proposes an intent-based orchestrator with handoffs. Charlie: agent-to-agent is unproven and Intercom itself says A2A is unreliable and recommends MCP or APIs. Charlie wants to move to the API version of Fin for UI control, so if dashboard builds the widget, Fin runs under the hood. The handoff mechanism (does the Fin conversation stop dead?) is unresolved, as is who owns the orchestrator.
- Fin does not take sensitive actions by design. Refunds are deliberately routed to the dashboard UI where controls already exist, even though Fin could technically do it.
- **Vendor risk:** Intercom flagged a possible Fin price increase following the Salesforce acquisition. Charlie does not want to over-couple dashboard architecture to Fin specifically, since Checkout may move off it.
- **In-house build benchmark: 50 to 200 engineers** for a comparable agent once guardrails, security, prompt injection defence, controls and analytics are counted. The dashboard team cannot build this: it is an all-in company decision, not a team project. Joseph notes engineering wrongly believes Fin is just an orchestrator that creates Zendesk tickets.
- Latency mitigation idea: let queries run in the background, Glean-style, so users leave and return.
- Team capacity: consumer requests plus the move off Zendesk will consume roughly half of Care's next year. Charlie will not commit to rebuilding Fin a different way without a product review first.
- Joseph mentioned Rammy Joseph approached him about moving teams to lead orchestration.

## Decisions

- Both open items deferred: the analytics side drawer is contingent on a unified AI experience plan, and the overall dashboard AI architecture awaits a formal product review.
- Next steps agreed: hold a product review to align on merchant problems, use cases and which agent solves what; Joseph to brief engineering on Fin's real scope against in-house build cost; group to produce a unified AI experience proposal with no duplicative agents.

## Insights

- Charlie's stated position: do not put the current design in front of leadership. It will be sent back for a unified plan. The ask is a product review before any commitment.
- The defensible rule from this: either label an agent narrowly enough that its scope is obvious ("Analytics assistant"), or limit its use case until agents can be merged. Never ship two general-purpose AI bubbles.
- Two numbers to reuse: Fin at ~$20k/year against a 50-200 engineer in-house build, plus Fin price increase risk from the Salesforce acquisition.
- Start from the customer problem, not from Fin. Designing around Fin means designing around a vendor and a support process that may not be the right frame for dashboard help.
- Nobody owns Checkout-wide knowledge quality. A standing risk to every AI initiative claiming knowledge access, and a candidate Care argument.
