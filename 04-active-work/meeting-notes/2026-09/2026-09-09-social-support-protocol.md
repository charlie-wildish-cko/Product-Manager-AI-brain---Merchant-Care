# Social support quick sync

**Date:** 2026-09-09
**Attendees:** Carolina Corral, Charlie Wildish, Joel Petrosino, Oliver Westlake-Simm
**Drive source:** 1VGPR6utPf3C7IcQskWkxRKuXUbT46W5J1osSSBCHsL4

## Context

Carolina proposed a social-media support protocol drawing on her Uber and Tap to Pay experience, covering how public complaints route into Care.

## Key Points

**Proposed protocol**
- First public reply always expresses empathy and directs the user to official support channels, preventing channel fragmentation across marketing and support tools and managing trolls.
- Tiered escalation: public redirect, then a second nudge for persistent or highly dissatisfied users (including those meeting UK FCA complaint standards), then move to DM to collect contact details, then route to support for end-to-end handling, with resolution status fed back to the social team.
- Joel's objection: redirecting end users into support creates a frustrating loop if support then rejects the query and tells them to contact their bank. The group agreed to prioritise FAQ and web-rescue resources.
- Charlie and Oliver discussed segmenting support pages by customer type and using separate social handles for Ray and Checkout, to stop end-user queries routing into enterprise queues.
- Charlie's near-term mechanism for social cases: use the existing Retool with added fields and templates to capture name, number and email, avoiding giving the social team back-office access.

**Timelines and markets**
- Oliver confirmed Ray launches Q1, and SMB not before mid-2027 at the earliest.
- Brazil: upcoming contracting under a merchant-of-record model creates direct contractual relationships with end users, generating a new social complaint vector. Carolina and Francisco speak Portuguese.

**Compliance thread**
- Joel and Oliver debated whether high volumes of end-user complaints (for example "remember me" functionality, illegal selling) should trigger merchant reviews or due diligence, referencing recent Japan audit findings.
- Oliver to raise an event-driven review process with compliance (Brian and Pua).

**Resourcing and tooling**
- Carolina argued for hiring program managers who own a line of business, track P&L, and build structured process engines for engineering to automate, rather than hiring large agent pools.
- Oliver noted SMB and consumer volumes need high automation rates to control headcount cost, citing Stripe and Uber models.
- Carolina detailed Uber's Bliss: an internal front-end case management system API-connected to backend systems, letting agents complete ~90% of work without leaving the tool. SMEs built detailed decision charts that product converted into policy engines and automation workflows.
- Charlie updated on moving off Zendesk and work with Milan and Hélder on the operations back office. Joel raised tool sprawl: teams building disparate platforms and URLs rather than one unified system. Charlie and Joel discussed mitigating this with MCP interfaces and embedded AI fetching data inside case management.
- Care agent performance in Mexico reported as very good on Joel's QA of their tickets. Jonathan travelling there to start L2 work with Brandon. ISV team and Hector's team onboarding well.

**Decisions**
- Unresolved: whether to scope v1 of the social support playbook to merchants only, with a separate Ray version later. Pending marketing review.

## Insights

- Ray forces a channel and brand split (separate handles, separate support pages, separate playbook) before Q1. That is new scope not currently in the Ray Care plan.
- The Bliss architecture Carolina describes is the same central-work-distribution-hub plus action-portals thesis Charlie argued to Sunil the next day. There is now a second senior voice backing it, which strengthens the platform case.
- Emerging governance idea worth tracking: end-user complaint data feeding merchant due diligence and event-driven merchant reviews. That makes Care data a compliance input, not just a product input.
- Joel's loop objection is the real design constraint: redirecting end users into Care only works if Care can actually resolve, otherwise the protocol manufactures frustration and a second contact.
- SMB is confirmed as not before mid-2027 at the earliest, which is later than the "next year" framing used elsewhere. Worth reconciling against the roadmap.
