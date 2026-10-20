# Platforms / EP Delivery Meeting

**Date:** 2026-09-15
**Attendees:** Invited: Pierre Biasutti, Andre Verhaeg, Milan Jani, Chris Liness, Gilles Beausseron, Gabriele Usonyte, Arthur Magnes, Antonio Vasilev, Guido Van Der Hart, Pao Igarteburu, Mark Gossa, Fraser Bryant, Charlie Wildish, Davine Ittoo, Kunal Patel, Ignas Sakalauskas, Jamie Sims, Richard Ding, Kehinde Ladipo, Stephen Adams
**Drive source:** 1Cdk1gfjxYXbHhdKblJBAU8v4mvBL8sETiGo8yQ-QUGA

## Context

Weekly Platforms / Embedded Payments delivery meeting. Gemini labelled speakers by meeting room (LON-03-09, PAR-03-Madeleine) rather than name, so individual attribution is unreliable.

## Key Points

**Care items**

- Charlie's item: **Q4 North Star is to manage all of Geographic Expansion in Plain, not Zendesk.** All Care sub-deliverables sit under this. Business sign-off targeted within two weeks via meetings with Commercial Operations. No help needed from this group; resourcing covered via Gilles.
- Merchant-initiated termination slipped from Q3 to Q4. It was a hard commitment, so the external-facing roadmap must show both original and actual quarter. Open scope questions: bulk/batch termination requests, which termination reasons to offer, and notification emails to merchants with an effective date. Care owns the interface and initiation point and must plug into the correct downstream workflow.

**Delivery status**

- Dashboard go-live for merchants targeted 30 September. MCRs are a dependency for the ARC migration; only a subset were in Q3 scope and those are green minus terminations.
- Geographic expansion (Arthur Magnes): provider selection underway across in-house providers BVD, Trulio, Kaiser plus others, recommendation due end of September. Separate BAC discussion with the APM team and compliance, as APM plans to integrate a BAC provider in GE early 2027; open question whether that provider fits the GE use case.
- Match automation: discovery complete, now in development. Andre circulated an SDR on match automation improvements awaiting review.
- Monitoring: email templates need consolidation. Sandbox testing can proceed with placeholder content.
- Webhooks: agreed to map core journeys against existing webhooks to find coverage gaps. Not required for Q3, whose goal was control of core events to protect Checkout, not customers. Risk flagged: existing webhooks carry a `sub_entity_id` field and the term "sub-entity" is being reconsidered, so publishing new webhooks with it commits Checkout to revising public documentation later.
- UAE IP sub-entity settlements: needed to service UAE IP sub-entities, integration planned early October, go-live November. Two bad options: the legacy client settlements API, being deprecated with unknown risk and actively discouraged; or the new client services API used for ISVs, which does not support pay-ins/payouts for sub-entities because it was built strictly for ISVs. Change is reportedly small but needs a roadmap slot from the client settlements team.
- Self-serve test entity setup: flow runner key flows expanded, covering ISV platform onboarding on the legacy stack. ISV onboarding on the new stack not covered, activation team to pick up. Open question whether an equivalent flow is needed for consumer GE.
- Harness migration: map API deployed, traffic switching pending, downstream API issues found at staging need re-test. Final Unifi ticket in progress (Gilles).
- In-person payments: downstream integration gaps found against the ARB-approved account structure configuration model. The ARB model never reached downstream teams (gateway, dashboard, pricing, bidding and others), so it now surfaces as an unexpected breaking change. Gateway will implement a temporary hack to unblock testing for the end-September go-live.

**Ray**

- The Braavos milestone was renamed "Consumer". The existing Braavos milestone is kept in case Braavos returns.
- Internal alpha October (equivalent of Braavos Phase 1, largely current behaviour), friends-and-family December with 500 invited users.
- Consumer entity structure definition is the blocker that unlocks the end-to-end scalable model. Four-tier entity architecture with products underneath. Argued that by 2027 policies must be product-based, not keyed off static customer types.

## Decisions

- Dual-track on UAE settlements: raise an intake request with the client settlements team for new-API support while doing discovery on the legacy API as a hedge.
- Whether to proceed with the ARB-approved account configuration model or an alternative needs further discussion. Product-versus-tech ownership of that decision is unresolved; Charlie asked to be involved.
- Each milestone should have a single named owner.
- Business Account: likely push back on the ask, since the team building it needs information rather than delivery from this group.

## Insights

- Care's Q4 North Star is now on the platform delivery record: all Geographic Expansion managed in Plain, not Zendesk, with business sign-off targeted by end of September 2026. First Plain commitment visible outside Care.
- Committed-then-slipped deliverables must show both original and actual quarter externally. Relevant to how `2026 deliverables.md` is reported.
- The "sub-entity" term is unstable. Any Care-facing field or taxonomy using it inherits a future rename cost.
- ARB approval does not propagate changes to downstream teams. Assume nothing lands downstream just because it passed ARB.
- Ray dates here (internal alpha October, friends-and-family December with 500 users) sit earlier than the "internal launch end Dec 2026" recorded in CLAUDE.md. Reconcile against `2026 deliverables.md`.
