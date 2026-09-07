# Consumer (Braavos) Ops Readiness Steerco

**Date:** 2026-08-11
**Attendees:** Sarah Edmonds (chair), Umang Sota, Oliver Westlake-Simm, Charlie Wildish, Fabio Marques, Akshav Ramkalawon, Gabriele Usonyte, Ana Muschici, Hen Pekar, plus ~30 invited across compliance, fraud, issuing and product
**Drive source:** 1qTp5QM90gSijQY4Ry42sCuFtW01v4vaXgrLU52hpCKI

## Context

New steerco format using a RAG-rated deck as the agenda, covering Phase 1 internal launch readiness and Phase 2 gaps. Held one week before the Braavos pause decision (2026-08-18), so the content is a snapshot of the programme as live.

## Key Points

**Phase 1**
- Internal launch on track for Tuesday 18 August 2026. Root cause of the timing was Apple Pay certification.
- Training rolled out to 50 participants. Oliver describes the test population as "our internal thousand users."
- Two Braavos PMs accepted offers, starting 1 and 20 September. Umang covering PM work until then.
- Only outstanding Phase 1 ops item: a Care plus engineering session on how care tickets are managed, delayed by the lead engineer's emergency leave.

**Care and content**
- Social media complaints out of scope for Phase 2 but must be handled internally eventually.
- Charlie clarified the treasury AI agent is for merchant queries (settlement/payout diagnosis), not consumers. Umang's point stands that the consumer analogue lands on Care regardless, because treasury cannot scale to consumer volume.
- Content coverage is the headcount lever. Work started with the content team (Sammy, Seb) on an exhaustive Phase 2 list structured by area (money movement, account-related).
- Net-new content is the known unknown. Oliver wants a dedicated resource and a defined turnaround from issue detected to content published.
- BPO is the main cost driver. Oliver has reallocated 2m from his back-office budget and is reviewing BPO numbers with Fabio.

**Product and data (Charlie's item)**
- Charlie rated Phase 3 red, not Phase 2. Reason: no milestone from the data team on the customer identification and transaction data requirements Care submitted. Plans must land within the month, or engineering has no runway.
- Umang: the month delivers the plan, not the data. Eugenio Cocchi has scoped the customer data plan; Jenny and Alice are building it. Transaction-level data exists; customer-level is net new.

**Access and permissions**
- Charlie: "Care should be able to see everything but not necessarily do everything. The actual actions of control should be limited to domain teams who have the expertise."
- Fabio pushed back on read-all for consumer data. Net position: Care gets visibility with PII carve-outs, control actions stay with domain teams. Ownership mapping outstanding.

**Fraud, disputes, regulatory**
- Hen Pekar raised releasing users from decline loops (UK user transacting in Atlanta gets blocked). Oliver's challenge: that should be an in-app self-service feature, not a contact.
- Phase 1 disputes is manual. A test chargeback failed, suspected file format/naming and DPI constraints, with no validations on the issuing side. Not a launch blocker.
- Card-issuing disputes stay with the issuing team, not the core disputes team, until end of H1 2027 (per Carolina Corral, from a disputes product review).
- Chargeback window is 120 days, not 180, counted from the date goods or service were due, always evidence-based. Oliver to add the Section 75 and long-lead purchase delineation question to the disputes PRD.
- Unauthorised (ATO) and authorised fraud policies merged into a single anti-fraud policy, to committee 18 August then board.
- Decision: share draft policies with banking partners (JP Morgan, ClearBank) rather than waiting for board approval. Phase 2 and external launch both depend on partner approval.
- Q3 onboarding is compliance-only (IDV, KYC, CRA profile). Fraud checks at onboarding land in Q4.
- Gabriele presented a consolidated roles and responsibilities sheet decomposing ownership across data collection, detection, triage, decision, outcomes, enforcement and consumer outreach. Teams to fill their rows within a week.

## Insights

- Phase 2 and external launch were gated on banking-partner approval of policies and procedures: a non-product dependency on the critical path.
- Zendesk, Fin, Plain and Ray are not mentioned anywhere in this forum. Flow mapping was happening ahead of any recorded tooling decision, and the care ticket-management process was still an unscheduled workshop.
- The BPO versus content trade was the explicit cost lever, with no AI deflection or automation quantified. Fin unit economics (0.90 per resolution against ~40 per human contact) were absent from the consumer cost model.
- The net-new-content loop had no owner and no target latency: the consumer analogue of the Reflex insight loop.
- Care's consumer operating model is read-heavy, act-light, with a PII carve-out merchant care does not have. Consumer agent tooling needs field-level redaction, not just role-level access.
- Care was being handed treasury's work by default on the argument that treasury cannot scale, with tooling unscoped.
- Consumer Duty was not mentioned once, despite vulnerability routing being decided in the flow-mapping session the same day. The decisions existed but had not surfaced to the governance forum.
