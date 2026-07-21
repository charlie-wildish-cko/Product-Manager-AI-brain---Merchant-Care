# Mapping out all the support asks

**Date:** 2026-07-13  
**Attendees:** Charlie Wildish (PM, Merchant Care), Oliver Westlake-Simm (Support ops, consumer + acquiring)  
**Drive source:** 1f3nwTUoyQX1aOQH5K5TbayCGEuJWW7X7_nuGy8w6nTM

## Context

Charlie and Oliver mapped every new support ask landing on Merchant Care (consumer wallet, open banking, Brazil FX, Blue AMI migration) to identify what is known, what is missing, and what to escalate. Purpose was to reach decisions before Oliver's bereavement leave and to prep a steering committee (STO/stick code) input for the following Monday.

## Key Points

**Consumer segregation (regulatory)**
- Open banking falls under Consumer Duty, same as Braavos. Requires dedicated consumer channels: phone line, email ingress point, vulnerable-customer handling.
- Consumer complaints cannot go to complaints@checkout.com: the acquiring team cannot determine whether a contact is a consumer or a merchant user, and will mishandle them.
- Decision: segregate support into consumer and acquiring teams. Ray X, open banking, and Brazil FX all route to the consumer team. Fabio and a new head of consumer support report to Jenny as a separate business unit.
- Conflict flagged: compliance wants to keep everyone under one PUA model (agents handling both acquiring and consumer), which breaks the segregated model.

**Ray / Ray X (consumer custodial wallet)**
- Custodial crypto wallet, owned by Max, built by Helder as a fast/lean launch. Fewer regulatory obligations than Braavos (custodial), but some FCA exposure remains for UK consumers.
- Named "Ray" (DM dislikes "Ray X"). Distinct product from Braavos; naming overlap and separate entry points are a source of confusion to resolve.
- UAE is the #2 year-1 market: requires Arabic knowledge base. Max is asking for ~6 languages. Guide can switch language by IP once knowledge exists. Main knowledge locations: EU/UK (English), UAE/Middle East, Argentina, Brazil, Philippines.
- Headcount modelled in Mexico, Dubai, Mauritius, plus 1-2 in UK for treasury ops (transaction investigations sit within Merchant Care).
- Volume model: 60,000 monthly active users by end of year 1. 35% contact rate on active users (deliberate overestimate; Braavos assumes 20-25%, realistic is 8-12%), plus 15% for new-registration contacts (verification, first deposit). ~29,000 contacts/year in year 1. Total ~40 headcount for Ray.
- Query types: deposits, declines, fees, verification/KYC, tax ID or name mismatch, verification delays, pricing/FX transparency, unclear exchange rate, double payment.

**Deflection assumption removed from model**
- Oliver had modelled 50% Fin deflection. Charlie removed the Fin deflection assumption from headcount planning ("I can't say that, that's really hard") in favour of conservative total-contact volume. Max's cost case still assumes AI-first.

**Brazil / FX (remittance)**
- Remittance: collect Brazilian rails from a consumer, convert to foreign currency, remit to a foreign merchant (e.g. Brazilian consumer paying Netflix US). Consumer agrees to Checkout T&Cs.
- Requires 24/7 phone and online support. Query types uncertain: likely failed payments, double/accidental payments, fraud ("this wasn't me"). Fraud routes to Fabio's team.
- Headcount: external/contractors, low expected complaint volume.

**Open banking**
- Uses token.io, who subcontract via Modulr. Data access appears locked down; the level of access Checkout actually has is unconfirmed and needs verifying.
- Once Checkout contracts directly with the payer, the consumer can complain about end-to-end service failure even where token.io or the payer's bank caused the issue.
- Query types: consent/disclosure (didn't agree to terms / data access), unauthorised payments, wrong amount / duplicate, wrong beneficiary, failed/missing/delayed transfers, refund issues, fraud/scams, AIS consent (90-day limit, access after withdrawal/expiry), bank-selection confusion (didn't understand pay-by-bank vs card), servicing complaints.
- Headcount: likely absorbed by Braavos team (low expected volume). Not yet agreed with Braavos lead.

**Blue AMI migration: deferred**
- Request to migrate Care to Blue AMI. Decision: not happening this year. White-labelling (rebranding everything for Blue AMI) is high-effort and needs separate Zendesk instances / full separation.
- Care has no capacity; team cannot support Blue AMI and Checkout simultaneously. Revisit after a new system lands (targeted July 2027).

**Consumer launch timeline: October unrealistic**
- FCA-required flows have not been mapped. Charlie generated draft flows via Claude but they need validation for completeness.
- Oliver needs ~6 more headcount in ~4 weeks to get consumer off the ground; Jenny has approved 6 (not yet opened). Knowledge management is the biggest lever but cannot be built until a product, systems, and tooling exist.
- Direction: internal launch July/August; external launch deferred to March 2027 or later. Reasoning to be framed as a trade-off for the steering committee, not a flat "no".

**Plane platform (operations)**
- Plane is the intended long-term operational platform for all of operations; Helder aligned that Care is priority #1, then other teams onboard over time.
- Needs ~4 months for SOPs and system training after implementation. A March consumer launch implies Plane implemented by Oct/Nov 2026 (December holiday erodes a month).
- Vendor assessment pending. Stephanie (Shield's team) is evaluating sanctions screening as another migration use case. Different teams likely need the same workflow system with access to different data.

## Insights

- The consumer launch (Ray, open banking, Brazil FX) has landed on Care with no product-side definition of users, query types, CRM, authentication, or data access. Charlie and Oliver are reverse-engineering requirements the PMs (esp. Alexa on open banking) have not supplied. This is the central risk to flag to the steering committee.
- October external consumer launch is judged unachievable by both. Realistic path: internal July/Aug, external ~March 2027. This should be treated as the working assumption until formally re-baselined, and checked against `2026 deliverables.md` / consumer roadmap docs before citing elsewhere.
- Consumer/acquiring team segregation is decided operationally but contradicts compliance's single-PUA model. Unresolved: this needs escalation, or ticket routing and support quality break.
- Fin deflection is deliberately excluded from consumer headcount modelling: Charlie will not commit to a deflection rate for an unbuilt product. Any consumer capacity plan should be read as gross contact volume, not net of AI.
- Data access is the recurring blocker across all three consumer products: open banking (token.io/Modulr lock-down), Brazil FX, and Ray all require system access to investigate contacts that may not exist. Confirm data access before committing support SLAs.
- Ray year-1 volume assumption to carry forward: 60k MAU, ~29k contacts/year, ~40 headcount, on a deliberately conservative (high) 35% contact-rate estimate. Braavos comparator is 20-25%.
- Open unknown with regulatory weight: if a consumer contacts Checkout and the issue is routed to a merchant, is Checkout still bound by regulatory response times? Unanswered, needs compliance input.
- Blue AMI migration is off the table for 2026: do not plan Care capacity against it. Revisit alongside the new-system decision (July 2027 target).
