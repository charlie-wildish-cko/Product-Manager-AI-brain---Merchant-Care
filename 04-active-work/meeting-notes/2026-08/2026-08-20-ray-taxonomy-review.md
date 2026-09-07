# Ray Taxonomy Review

**Date:** 2026-08-20
**Attendees:** Charlie Wildish, Joel Petrosino
**Drive source:** 1HcaadORNcJXqoiNMy-BfqYfSC1bAm_IopPWxcRmXLUE

## Key Points

**Reflex as a customer insights platform**
- Charlie is giving the commercial team (Charles Forson, Philippe Leonhardt, Andy Cornforth) the Reflex schema so they map their data onto it. "I don't want it to be the care insights platform. I want it to be the customer insights platform. That was always the goal, that's why it's called something that's not called support."
- Proposed mechanic: a type field (type=support, type=commercial insight) with filterable entities, so a PM sees per-merchant support cost alongside TPV and opportunity.
- Charlie's stated risk is available Reflex engineering capacity for the rest of the year, but he does not want that to block integration because duplication is worse.

**Ray taxonomy**
- Max's first pass is built off the archived Braavos taxonomy with per-launch requirements added. 100 of 230 issues flagged as self-serve potential.
- Charlie's critique: that ratio is meaningless without volume weighting at category level, because 80% of volume could sit in three topics. Action: redo with category-level (ideally sub-issue-level) weighting, then forecast resolution rate off resolution-type mix.
- Charlie cannot personally critique the crypto content and is reliant on Max there.

**Specific taxonomy decisions**
- Web rescue / account lockout: the draft assumed email as the contact route for lost-phone lockout. Rejected: there is no way to authenticate over email and they do not want the precedent. Joel's model from prior fintechs is full account suspension, then an automated liveness check against the historic liveness capture on a new device. Monzo's web rescue form (magic link, limited actions such as freeze card) reviewed as a comparator.
- Disputes: pre-dispute inquiries where the consumer has already contacted the merchant bypass Care entirely and go to the disputes team. Agreed a pass-through mechanism for every escalation so traceability and timestamps flow through one system.
- Fraud, phishing, scams and vishing: human handling, gated by severity. Money-mule and consumer-unaware cases are intent-based and hard to classify.
- Compliance-initiated contacts are internal, not customer-exposed. The initiating team takes the action and fires a macro, and the customer's reply returns to the initiating team's queue, not Care. Requires the Ray app to build inbox and notification capability, otherwise email is the only outbound channel.
- Account closure automation is an ops design decision and hard given fragmented systems. DSARs are human-led, compiling conversations plus masking sensitive data, not AI-suitable.
- Accessibility: physical impairment and disability contacts route to humans, not AI. If the app is down, Fin can be served on the web form.
- Structure: collapse self-serve and FAQ into one bucket. Delete FSCS and deposit-insurance rows, since no protection applies.
- Tiering: Max wants a Monzo/Revolut-style subscription tier model when Ray matures. Charlie wants tier and plan designation calculated upstream in customer data, and notes merchants need to move away from tiering because it will not work for SMB, with Success Plans codified as a feature instead.

## Decisions

- 50% AI resolution at Ray launch is Charlie's forecast, against a ~70% number quoted on an earlier call which he pushed back on: you cannot hit that before a live product and tuning. The closed beta exists to find what to fix.
- At launch Fin does content only, no data procedures. Procedures are expensive to build and the investment targets are not yet known.
- Ray alpha ships December without Fin: web form only, volume too low to justify Fin. Add Fin post-launch once there is data.
- Orchestration-layer architecture approved in principle. Core services owned by Checkout, never coupled directly to vendors. Channels, then orchestration, then enrichment, then AI. A machine user invokes the Fin API into a thread, controls Fin's actions until handoff, and can re-invoke Fin mid-conversation (today Fin is trigger-on-assign only). Jiro and Tina are estimating the orchestration layer, config-as-code repo and workflows.
- Not resolved: automation-level strategy. There is no granular data on effort or cost per ops workflow, so engineering-versus-ops investment ROI cannot be calculated.

## Insights

- The ROI question of engineering and product investment versus hiring ops headcount cannot be answered today, because there is no measurement of time or cost by workflow across ops teams. No workflow inventory, no complexity or time data, so no ranking and no prioritisation.
- Karolina wrote a levels-of-automation framework (layer 5 full automation, cascading to layer 0). Charlie rates it and wants it shared with Joel. The gap is that you cannot pick a layer per workflow without the workflow inventory.
- Both concluded an Operational Excellence role with a product mindset is the missing function to bridge product and ops.
- Reusable AI boundary rule: AI can tell a locked-out user their status and the action to take. AI must not take the action for them.
- Charlie is away 26 August to 4 September and wants the architecture decision landed before then to unblock procurement.
