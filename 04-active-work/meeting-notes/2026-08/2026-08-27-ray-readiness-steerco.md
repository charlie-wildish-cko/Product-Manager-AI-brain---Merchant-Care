# Ray Readiness Steerco - Ops and Product

**Date:** 2026-08-27
**Attendees:** Sarah Edmonds (chair), Max Rothman, Joel Petrosino (gave the Care update on Charlie's behalf; Charlie on leave), Oliver Westlake-Simm, Brian Weir, Fabio Marques, Gilles Beausseron, Joe Foulds, Daniel Kliza, Pooja Lutchmun, Bernard Ryan, Bhinti Seedeen, Tejash Chunnoo, Chris Wade, Ana Muschici, Madeleine Gunn, Nick Taylor, Alex Jordan, Charlie Wildish (invited)
**Drive source:** 1VYthLqZExtjPRCvOq_6mL2Tb7-Suv5tR0y3-BrBmRzQ

## Context

First of a new bi-weekly Ops and Product alignment forum for Ray launch readiness, surfacing operational gaps and blockers.

## Key Points

**Launch phases and policy**
- Internal testing launch October, friends and family December, external launch Q1. Four policies required for go-live.
- Brian Weir has first drafts for CDD, transaction monitoring screening, and AML, over 90% complete pending feedback. Fabio Marques owns the fraud policy. Policies are structured to MiCA standards but for an unregulated entity. Draft TM rules sent to Maddie.
- Documentation hierarchy agreed: Policy (regulatory, high level), then Standards, then Business Rules (operational implementation). Gilles Beausseron owns business rules and will work in parallel because development cannot start without them.
- Final policy sign-off sits with two individuals in Ops and Risk. Max Rothman to confirm with Jenny by end of week.
- Ray is not subject to UK Consumer Duty, but Brian Weir said most of the Braavos work is reusable at a more relaxed standard. Fabio Marques will consult ex-Revolut colleagues on UAE, Philippines and Brazil local requirements.

**Jurisdiction and access controls**
- Global, borderless policy approach adopted. No per-market licensing because Checkout is not actively soliciting those markets. Local regulatory compliance not needed unless a Visa scheme threshold of $5M cumulative processing or significant scale is hit. Ten country legal opinions due in 1-2 weeks. Visa cross-border issuance rules may restrict marketing in specific markets.
- October internal launch blocks the UK app store and uses country-specific app store geofencing. User residency collected and verified against onboarding data, plus device intelligence and IP checks. Q1 physical card orders will require a delivery address to corroborate residency.

**Headcount and tooling**
- Planning assumes 200,000 users by end of year 1, from the original Ray GTM doc. Built from alert volumes, manual KYC, and care escalations, adjusted for AI efficiency, with phased hiring. Ana Muschici asked Max for the volume numbers in writing.
- Sphinx (AML and screening tooling): procedure development is blocked on final policies and confirmation of automation level (Sphinx versus manual). Implementation estimated at a matter of weeks.
- SOPs: Oliver challenged the need for long SOPs for frontline teams and proposed job aids. Max held that SOPs are strictly required for scheme audits and future licensing, but agreed timing can slip.
- Knowledge and training are at an early stage. A knowledge management analyst role has just gone live.

**Care and support model**
- Joel: the team worked through Max's taxonomy to separate what can be handled up front, what needs a human, and what Fin can deliver. Open support-channel questions drive the Care requirements, workflow count, and SOP volume.
- Phone: the Braavos model required a phone line for vulnerable customers under Consumer Duty. With that requirement gone, the phone requirement drops. Joe Foulds argued multi-country phone support balloons in complexity against text-based support with AI translation. Oliver confirmed phone is not required for Ray, but is required for Brazil merchant of record, a separate project with its own back office.
- Max: "definitely no phone... we don't even really want to expose an email if possible. Everything is in app... in chat Fin, AI first as possible."
- Joel flagged that phone is a significant requirement on the Plain side if Plain is used for phase one or external launch, and that Fraser's team must define the phone integration requirements.
- Charlie's blocker as recorded: confirmation of the customer and transaction data model, and whether it matches Braavos. Joe Foulds said it was never confirmed for Braavos either, and will resolve it directly with Charlie.
- Oliver: user authentication is a hard gate for external go-live, noting there is no authentication for merchants today and that this is problematic. Named it a fraud priority via Fabio. Joe Foulds separated the concerns: the customer transaction data model is distinct from authenticating inbound contacts.
- Max: sensitive account actions (information requests and changes) will be biometrically guarded, which is the stated reason for avoiding email, since an emailer cannot be validated.
- Joe Foulds is building an entire new back office for Ray. The data model does not exist yet and is being hashed out with Care. Stated design constraint: no fragmented data sets requiring agents to go across four different tools.
- Next Care steps: get the taxonomy signed off (Max has reviewed), then estimate the work needed for the new platform and whether December is feasible.

**Fraud and disputes**
- Anti-fraud policy in draft. Daniel Kliza will base the consumer fraud procedure on it, repurposing existing issuing dispute extensions.
- Issuing disputes are currently manual, adequate for internal launch, but Daniel flagged scalability risk from January when external volumes arrive. There is no Visa API for disputes, which increases manual effort. Daniel to ask Alex McSweeney whether he will build a scalable system.
- Termination procedures not started. Will be a lift-and-shift from Braavos.

**Decisions**
- Policy, standards and business-rules structure and ownership confirmed, with Gilles on business rules.
- Global borderless regulatory strategy for launch markets.
- App store geofencing plus mandatory residency verification. Block users declaring restricted-territory residency.
- SOP completion targeted for Phase 2 (December), not the October launch.
- No phone support. In-app, AI-first text support via Fin instead.
- Sardine adopted for initial fraud case management and rule configuration, with possible later migration to the Ray back office.

## Insights

- The Ray service model is now settled: no phone, minimal email, in-app AI-first chat via Fin, biometric gating on sensitive actions. That is a far cheaper Care model than the Braavos design and should be the baseline assumption for Ray Care scoping.
- December is the pressure point. SOPs, taxonomy sign-off, and new-platform feasibility all land there, and the platform decision is on the critical path.
- Two unresolved dependencies own Charlie's Ray work: the customer and transaction data model (Joe Foulds) and taxonomy sign-off (Sarah Edmonds and Max).
- 200,000 users in year 1 is the number Ops headcount is built on. Hold it against Care contact forecasts.
- Issuing disputes are the clearest known scalability gap for post-Q1 Ray volume, made worse by the absence of a Visa disputes API.
- Joe Foulds building a separate Ray back office cuts against the single-platform consolidation argument. Worth resolving explicitly rather than letting two back offices emerge by default.
