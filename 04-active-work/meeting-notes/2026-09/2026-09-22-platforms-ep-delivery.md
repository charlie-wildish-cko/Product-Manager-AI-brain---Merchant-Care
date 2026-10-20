# Platforms / EP Delivery Meeting

**Date:** 2026-09-22  
**Attendees:** Pierre Biasutti, Helder Goncalves, Milan Jani, Chris Liness, Gilles Beausseron, Antonio Vasilev, Guido Van Der Hart, Pao Igarteburu, Mark Gossa, Charlie Wildish, Davine Ittoo, Kunal Patel, Ignas Sakalauskas, Jamie Sims, Richard Ding, Kehinde Ladipo, Stephen Adams  
**Drive source:** 1fME3a18qQMPFzh44kjvZRBSPVNdAd-YXouoQH3M-sXY

## Context

Last Platforms/EP delivery meeting of Q3. Most speakers were in room LON-06-11, so individual attribution is limited. No explicit Care discussion. Charlie did not speak.

## Key Points

**Onboarding milestones**
- MCR (business details): ready for production, docs awaiting one sign-off (Antonio).
- Representatives: UAT and docs this sprint is "touch and go".
- UI on track for end of month. Checkout automation RCA: production coding starts Q4.
- Checkout-initiated termination: end-to-end testing finishing that week.

**Email templates (Care-relevant)**
- The one blocker on the automation work. No copy owner since Gabriele Usonyte handed over before long-term leave. SendGrid templates need copy from UX writers or content. Assuming no webhooks for now.

**UAE**
- Two tracks: QA-test the existing settlements configuration, and submit a Q4 prioritisation request to client settlements.
- Open: ship UAE onboarding API-first without dashboard (as done for ISVs) or ship together.

**Mark Gossa's initiatives**
- Rail scale: volumes expected similar to consumer.
- Self-serve setup UI extending the flow runner. ISV seller onboarding moves to Kau and Steven's team.
- Data collection architecture: collect all data upfront so risk can automate decisions. Prompted by a war room over a "flurry of incidents" in data collection.
- Agreed: technical initiatives sit under 3-4 top-down Q4 milestones (expansion, platform hardening, risk asks). Harness migration is the exception.
- Unified workflow metrics: new scope must include metrics in its definition of done.

**Ray**
- Ray global legal entity implementation on hold one week while Ben Leah and Joe design how the issuing entity relates to the customer entity (different Checkout legal entities, needing transfer pricing alignment with compliance, accounting, treasury).
- "Ray Global" entity configuration proceeds as non-regret work.
- Target: internal app for a subset of developers by mid-October, "exactly Braavos phase one", reusing Braavos builds.

**In-person payments (IPP)**
- Went green, red, green. Downstream teams (pricing, billing) could not integrate with the ARB-approved "everything is an entity" account structure.
- Interim: gateway forces the e-commerce model to unblock the end-of-September pilot with Molly. Long term: the ARB design.
- Lesson: ARB checks technical viability, not downstream capacity. Downstream impact was never tracked at programme level.

**Other**
- Brazil activation blocked on an underwriting decision (Richard Ding).

## Insights

- Unowned merchant notification copy (onboarding emails) is a contact-driver risk and an opening for Care's Content Strategist to shape wording.
- Upfront data collection redesign is a contact-prevention lever that fits Insight & Prevention.
- UAE may launch API-first. Care SOPs and Fin content need to match whichever path ships.
- Ray issuing and customer entities sit in different legal entities, which matters for Care customer identification.
- IPP pilot runs on an interim account model. The later migration creates reporting, pricing and billing contact risk.
