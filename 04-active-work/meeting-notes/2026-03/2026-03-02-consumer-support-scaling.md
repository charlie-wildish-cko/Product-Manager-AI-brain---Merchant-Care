# Consumer Support Scaling Review (B2C / Braavos)

**Date:** 2026-03-02  
**Attendees:** Charlie Wildish, Umang Sota (Consumer Product), Averof Stylianidis (Consumer Product, day 1 in role)  
**Drive source:** 1cVTbdtf9WBdqKzJFT2ToznWtJHahI9_lNzBEghf4d4E

## Context

First formal alignment between Care Product and the B2C product team on support architecture. Charlie presented his contact volume forecasting model to initiate H1 2026 planning for the Braavos consumer support solution.

## Key Points

**Volume model**
- Current: ~40,000 contacts/year (B2B enterprise, flat).
- Projected: ~3.4 million contacts/year as Platforms and Consumer scale. Consumer contacts will be ~50% of all volume by 2030 (~8–9 million active users).
- B2C contact rate assumption: 20% of active users submit a support ticket annually (aspiration is 5%, PayPal benchmark). Conservative but directionally appropriate.
- Alternative model: 2% of transactions generate a contact.

**Fin model for B2C**
- Involvement rate: 90% (all app traffic routes through Fin first).
- Starting resolution rate: 70% (matching current B2B baseline). Optimisation target: 90%.
- Fin embedded in iOS/Android via SDK, or via Fin API for fully custom UI.

**Product/ops split**
- Product owns: infrastructure, channel routing, content library, data sources, agent tooling, data product for insights.
- Operations owns: human agent model (shift patterns, training, SOPs). A new B2C ops team is expected — likely BPO, possibly in a new Mexico hub. No ops leader hired yet.
- Umang endorsed this split. Merchant and consumer vocabulary are fundamentally different; mixing them would break the agent experience.

**Tech stack**
- Shared back-end (Zendesk, which already has a Consumer brand set up for the Remember Me pilot). Delineated front-end customer experiences and interfaces. B2C and B2B agents are virtually separated with walled permissions.

**Phase 0/1 (50 internal employees)**
- Use the existing Remember Me infrastructure. No critical path items — simple web form is sufficient.

## Insights

- B2C contact volume will dwarf current B2B volume. Even halving the forecast is still an order-of-magnitude shift. The cost case for AI-first is existential, not optional.
- This meeting established Charlie as the infrastructure owner for B2C support from day one — before any product launch decisions are made.
- B2C is an opportunity to build the support model correctly from scratch: self-fulfilling loop, correct data infrastructure, Fin-first, insights feeding prevention — without B2B legacy debt.
- Consumer Duty obligations were not discussed in this meeting but apply at B2C launch.
- Umang Sota is the primary B2C Product counterpart for Charlie. A B2C requirements doc (originally drafted by Greg and Ankita) exists but had not been converted to a PRD at time of meeting.
