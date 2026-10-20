# Ray Readiness Steerco - Ops and Product

**Date:** 2026-10-08  
**Attendees:** Sarah Edmonds (chair), James Walters (program lead, unconfirmed: Gemini labels the speaker "LON-06-11"), Charlie Wildish (Care), Fabio Marques (ops readiness, consumer fraud ops), Daniel Kliza, Joe Foulds (issuing/disputes tech), Ben Leah (on-chain funds), Gilles Beausseron (product controls), Ayesha Ghoshal (product, terminations). About 30 invitees. Dispute owner (Akshav Ramkalawon) off sick.  
**Drive source:** 1AS5E8i9ftP6aCIFTEyr7JZTf3pLPgG3YdeB-2xMEdZQ

## Context

Steerco checking Ray launch readiness by domain against the PRD. Shared doc (owner Sarah Butterfield). Gemini name transcription is inconsistent (Fabio Marquez/Marques, Ashin/Ashen/Ashman, Stefan/Stephen).

## Key Points

**Timeline (aligned)**
- Internal testing 15 Oct 2026. Friends and family (F&F) progressive rollout from 1 Dec 2026, capped at 500 users. GA target 1 Apr 2027.
- Planning-stage requirements in Hive due 14/15 Oct.
- 10 countries approved by legal, in business risk review. Original plan was 3 launch countries. Which three is unresolved.

**Care and in-app support (Charlie, RED)**
- Formal in-app support cannot launch for 1 Dec: depends on app completion and app data.
- Mitigation: F&F is light-touch, so use a support flow outside the app. In-app flows plug in during F&F once dependencies land.
- Without Fin in-app, every contact goes straight to Care humans. F&F contact channel is undefined.
- Care capacity (via Ashin) is unconfirmed and could block F&F.
- Sarah wants Care in testing to capture issues and build knowledge. Timing (internal test vs November pre-F&F) and people unresolved.

**Disputes**
- Owned by shared services as a Checkout product. Mastercard partly automated, Visa not.
- Visa disputes can be raised manually by disputes ops as issuer, with no connectivity from dispute lifecycle back to issuing.
- F&F users cannot be given Slack access, so intake channel is undefined.
- Manual handling requires returning funds on-chain to embedded wallets, a process not done today. Workable for 500 users, no back-end automation.
- Product automation was H2 2027. Max is checking Q1. Joe Foulds: full Visa automation by Q1 is impossible (about four months, no discovery done).

**Controls and risk**
- Q4 control scope agreed. Transaction monitoring (Sphinx) out of Q4 scope. External launch marked RED: no plan or resources for required scope by end Q1. Next step: controls plan with landing dates, then risk-acceptance conversation with Fabio and Brian.
- Fraud policy and complaints policy in final review. Fraud TOM in review. Sardine technical workshop 8-9 Oct. AML/screening SOPs in final draft, blocked on Sphinx workflows and automation level.

**Terminations**
- Termination statuses defined. Scenarios leading to them (AML, fraud, Care issues such as bereavement) still to define. Fabio is interim owner of operational ownership.
- Open: in-progress fund flows (authorised, blocked, not on-chain) and returning funds to sanctioned or terminated users. Returning balance to last known wallet needs risk acceptance and an MLRO decision.

## Insights

- Ray F&F on 1 Dec has no in-app Care and no Fin: all contacts are human-handled, off-app, capped at 500 users.
- GA in-app support depends on app data milestones that are not yet confirmed.
- Ray disputes are manual through at least F&F and likely GA (Visa automation not before H2 2027). Expect manual load on Care and disputes ops, plus an intake mechanism that is not Slack.
- Transaction monitoring is the biggest GA risk. Gilles wants December made not-red first, then external.
- Terminations are a multi-stage, unowned process (Fabio interim). Funds-return policy needs an MLRO decision and drives Care scripts and escalation paths.
- Country scope is unsettled (10 approved vs 3 originally), which affects Care language and market coverage.
- Consistent with the Ray timeline in `01-knowledge-base/products/ray.md` (external beta end Q1 2027 = GA target 1 Apr).
