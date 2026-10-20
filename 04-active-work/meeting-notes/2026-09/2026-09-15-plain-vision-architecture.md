# Plain Vision: Target Architecture

**Date:** 2026-09-15
**Attendees:** Yifei Zhang, Sreekanth Nair, Fraser Bryant (presenting, with Jiro Farah and Ellis), Javed Iqbal, Anish Mavadia, Pragya Sinha, Charlie Wildish, Harlie Patel, Ana Cachapa Cuomo
**Drive source:** 1xHVZcjDgvbfrtU6lu_oMRKicXBKKiObKxrWC1K3my9A

## Context

Engineering-oriented walkthrough of the current Zendesk architecture, its failure modes, and the target Plain architecture. ~40 minutes.

## Key Points

**Current state and its flaws**

- Today: request arrives by channel, Fin attempts deflection, falls through to Zendesk, Agent Toolkit surfaces payment IDs in a side panel, Consultant Bot posts an AI diagnostic assessment as an internal note. Characterised as "as primitive as it gets": the agent cannot ask it anything.
- Framing: Zendesk is a platform for humans to support tickets with AI dancing around the edges.
- **Enrichment is the core pain.** Merchant Profile Builder and related services race to populate ticket data on creation, take up to 3 minutes, alert constantly, and break. Anything expecting data to be present immediately hits race conditions. Tickets get routed before enrichment lands.
- **Taxonomy is dual-sourced.** Anna and AJ configure one source of truth, engineers configure another in separate services. They drift.
- Consultant Bot serves internal agents only, fetching unrestricted background data. Customer Bot exists to feed Fin more data without Fin reaching into core sources directly, and applies heavy PCI/PII filtering. The two duplicate payment expertise. Javed is finishing Customer Bot.

**Target state**

- **Machine users.** Plain assigns a machine user, not a human, to every incoming thread. The machine user orchestrates and decides whether to hand to a human. Initially it always hands off, then progressively absorbs standardised requests like refunds, possibly with a quick agent check.
- This sits **below** Fin: Fin still deflects above, Plain automates what gets through. People will always bypass Fin and ask for a human.
- **Four orchestrators:** internal merchant (helping the agent), external merchant (talking to Fin), plus two for consumer/Ray. Consumer is split out because it needs entirely different context; merging would create agents with unmanageably broad knowledge.
- **Decoupled specialist agents** beneath the orchestrators: a payment agent that diagnoses payments and does not know or care whether the request came from Fin or a support agent. PCI/PII filtering moves up to the orchestrator layer. Consultant Bot and Customer Bot collapse into these specialists, reusing existing code.
- The payoff: an agent in Mauritius and a merchant talking to Fin access the same information, filtered differently. Fin can then deflect materially more because it has access to much more data.
- **Field consolidation: 50-60 standardised fields cover ~90% of payment queries.** Payment Search exposes about 30, named inconsistently, a stop-gap symptom of years of divergent payment sources, now consolidating on a proper naming convention.
- Consumer versus merchant: B2C deals in "transactions", not "payments". An entirely separate specialist agent, possibly plus a refund agent.
- **Sidekick** is Plain's built-in ticket-level AI conversation UI. Plan is to hook Sidekick to Checkout's agents so Mauritius and Mexico agents can converse in-UI, replacing static internal notes. Mechanics unproven.
- **Enrichment simplification:** push Salesforce merchant records into Plain on change, Plain enriches threads automatically. Removes the brittle enrichment services entirely for merchants. Consumer enrichment still to be figured out. Flagged as needing proving out.
- **A Fin-less variant of the vision exists.** Fraser: Fin was and is very useful but is much easier to replicate these days, which raises whether Checkout can do it itself. Removing Fin would require building a classification agent to replace Fin auto-classify.

**Fin metrics given in the room**

- Involvement ~25%, target 60-70% by year end.
- When involved on email, 80-85% resolution. Extremely effective on email, less so on chat.
- Overall ~21%, of which 5 points is one merchant's recent volume, so the true figure is ~16%.
- Charlie: ideally it would be stable, not the roller coaster it is now.
- Named dependency: the payment-data-over-email deliverable (~+10%), which also feeds the new payment agent.

**Operations platform, not a Care platform**

- Explicit ambition: an operations orchestrator alongside Care. Merchant onboarding moves from Salesforce to Plain threads. Checkout-generated work (fraud checks, transaction screening alerts) creates threads for the risk team.
- Charlie: every ops team has the same three needs, receive work, classify work, complete work. Zendesk expresses this with forms (a named collection of fields per team). Plain threads lack that grouping today, so Plain would likely need field-set bucketing (care set, dispute set, other team sets) to avoid a flat list of hundreds of fields. Charlie has shared a doc with the Plain team for feedback.
- "We're trying to build an operations platform, not a care platform." Likely eventual rename of the team to an operations product team.

**Segments and sequencing**

- Segmentation: acquiring (any business) against consumer (any individual). Within acquiring: large merchants, platforms, and SMB in future. Customer groups likely defined in Salesforce with rules flowing downstream.
- **Platform merchants** are supported in Plain via an additional data property naming the sub-merchant the thread is raised on behalf of, not a separate orchestrator. Rationale: avoid microservice sprawl.
- **SMB** (next year): human support very hard to get, by exception only, separate mobile app experience, a new PM joined that week leading it. Care needs SMB identified up front to control support level.

## Decisions

- **Build consumer support in Plain first as the foundation, then port B2B merchant workflows over from Zendesk.** Driver is Ray going live at end of Q1 next year. Consumer is expected to be light because it is much simpler than Braavos was.
- Q4 is the technical-detail phase: engineers start the following week on stepping from current state toward the vision. Some pieces (the payment agent) convert to product wins immediately, so the intent is to start moving them in Q4.
- Plain approval target: end of this month. Charlie has scored Plain against the evaluation indicators and it rates very highly against alternatives.
- Intercom is a tick-box competitor, not a real option: being absorbed into Salesforce Service Cloud so it will not solve the problem in a few years, it has raised prices, and Checkout is not a priority customer. Charlie has an Intercom session that week and will produce a heat map of differences.

## Insights

- **The 50-60 field consolidation is the hinge of the Fin resolution-rate story.** Payment Search exposes ~30 inconsistently named fields today. Standardising to 50-60 covering 90% of payment queries is what lets Fin deflect materially more. Same dependency as the payment-data-over-email deliverable.
- Plain's machine-user model is architecturally different from Fin deflection, not a substitute. Fin deflects above the platform, machine users automate what lands. Both layers persist.
- A post-Fin future is now explicitly in the architecture. Decoupled specialist agents make Fin swappable and the residual gap is classification. Consistent with Charlie's vendor-independence position in the AI Assistant alignment meeting.
- The ambition has widened from Care to Operations: onboarding, risk review and fraud screening as threads in Plain. This reframes the platform decision as a company-wide operations bet, raising the stakes on the end-of-month approval and likely reshaping the team's remit.
- Braavos-to-Ray simplification is a real scope reduction, stated in-room: consumer support in Plain is expected to be a light build.
