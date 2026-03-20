# Platform embedded AI support — future channel vision

> **Purpose**: Capture the target support experience where Platforms use Checkout.com's AI inside their own portal, so AI resolves Platform-related queries before they reach our human agents. This is a **channel offering** we would build and provide to Platforms, distinct from the 2026 "Platform support channels" work (identification, routing, webform context).
>
> **Terminology**: In this doc, "AI Agent" means **Fin AI Agent** (our in-dashboard support AI); the embedded component would be powered by Fin in the backend.
>
> **Strategic link**: Supports **reduce contact rate** and **reduce cost** — AI resolves queries in the Platform's workflow; only unresolved cases escalate to Checkout. Flywheel: **Handle** (AI first in Platform experience) + **Orchestration** (escalation rules to us).


## Why it matters

Every Platform query that reaches Checkout.com's agents represents a failure of self-service: the Platform couldn't resolve it, and Checkout.com bears the cost (~$40/contact). At scale — with US ISV expansion in 2026 and more Platforms onboarded — that contact volume compounds.

The embedded AI vision addresses the root cause rather than optimising the symptom. Instead of making Checkout.com better at handling Platform escalations, it reduces the number of queries that need to escalate at all. Platforms get a resolution capability inside their own workflow; Checkout.com only sees the genuinely complex cases that require direct investigation.

This also strengthens the Platform relationship. Providing AI-powered support tooling as a Platform capability — not just a cost reduction measure — creates a differentiated service that competitors can't easily replicate. It positions Checkout.com as a partner in the Platform's support operations, not just a payment infrastructure provider they escalate to.

## Vision in one sentence

We provide the Platform with an AI support component designed for integration into their internal portal, so their support teams can resolve merchant queries relating to our services (payments lifecycle, onboarding) using our AI first, and escalate to us only when needed.


## How it works

| Layer | What we do |
|-------|------------|
| **Component** | We build and provide a component for the Platform to plug into their internal portal. It uses the Fin AI Agent in the backend (e.g. over API to our services). |
| **Fuel** | Fin has access to our knowledge and data to solve merchant queries relating to our services (payments lifecycle, onboarding). |
| **Escalation** | If Fin does not solve for the Platform, we have rules to escalate to us. Light Fin AI Agent configuration for the Platform is under consideration (TBC). |
| **Commercial** | Could be an optional add-on service, as it would incur cost to us. |

**Why it helps**: We help Platforms reduce their support burden, but because the experience is embedded in their portal we do not insert ourselves between the Platform and their merchants. Merchants continue to contact the Platform and get a response from the Platform; they have no direct interaction with Checkout.com.


## Platform experience (end to end)

1. **Merchant** contacts the Platform support team for help.
2. **Platform support/ops** optionally use our AI support component in their portal. The component has access to our knowledge and data to solve merchant queries relating to our services (payments lifecycle, onboarding).
3. **Platform** handles queries with the Fin AI Agent first; escalates to Checkout when needed (complexity or lack of access to information). Escalation creates a Zendesk ticket with us.
4. **Checkout.com** solves escalations and provides updates back to the Platform (via Zendesk ticket updates; status visible on Platform portal side where we integrate).
5. **Platform** provides the answer back to their merchant on their portal.
6. **Merchant** gets a response from the Platform support team. No direct interaction with Checkout.com.


## Relationship to current work

| Current (2026) | This vision (future) |
|----------------|----------------------|
| Platform support channels: identify Platform/ISV, link merchant to ticket, route correctly in Zendesk | Embed our AI in the Platform's portal so they resolve with AI first; escalation to us only when needed |
| Fin and webform in *our* dashboard | AI component in *their* portal, powered by our backend |
| Reduce cost via correct routing and context | Reduce cost and contact rate by resolving in their workflow before tickets reach our agents |

This vision depends on the 2026 foundations (identification, context, routing) and extends them with an **outbound** capability: we deliver our AI as a channel they consume inside their experience.


## Open questions / TBC

- Light Fin AI Agent configuration for the Platform (what can they customise, if anything).
- Commercial model: optional add-on, pricing, cost recovery.
- Technical form: API contract, component packaging (embed widget, SDK, etc.), and how Zendesk ticket updates are reflected on the Platform portal side.


**Last updated**: March 2026  
**Owner**: Charlie Wildish  
**Status**: Vision / future direction — not yet scoped for delivery
