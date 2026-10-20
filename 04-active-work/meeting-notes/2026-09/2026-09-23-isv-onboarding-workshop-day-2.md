# ISV onboarding and management workshop, day 2

**Date:** 2026-09-23  
**Attendees:** As day 1 (Milan Jani likely facilitator). Named in discussion: Georgios, Arthur Magnes, Brendan Cain, Ignas, Jamie, Antonio, Daria, Mirabel Tay, Joe, Chris, Michael, Matthew Bum (credit risk), Isabel Scavieta, Alex M, Bernard (Ops Excellence), Jill  
**Drive source:** 1yYEfmp61eoH_nblW7EkgHAFOZ4IRPL95XZxiBuqyONo

## Context

Second workshop session. Mapped US onboarding data to the nine automated checks and aligned on an 18-item fix list. Speakers mostly under room LON-06-10.

## Key Points

**Problem framing**
- Onboarding escalation rate opened at "1 in 6,000". System built for the happy path. No end-to-end observability, internal or external.
- TagadaPay complained about a 5-day onboarding when the information was already known.
- Goal: time-to-feedback from days to minutes, or a definitive no.

**Data and checks**
- US data blocks: agreement terms, legal info, contact details, processing details, seller category (pre-filled by platform pricing packages), system auto-pulled data. Bank accounts via a separate instrument API checked against Validify.
- Nine checks: KYB, KYC, automated screening, scheme matching, website/URL screening, credit risk, internal block lists, merchant screening, bank account validation.
- 30-50% of document submissions fail first attempt (Arthur Magnes).
- API does not validate against policy, so customers wait days for manual review instead of getting an instant error.
- URL disclosures: enterprise needs 7. ISVs move to a risk-based 2 (legal name, governing law).
- Daria: engineering and data teams use inconsistent entity-status names. Proposal: dashboard points at a new analytics-owned data model.

**Customer communications gap (Care-specific)**
- Brendan asked who owns the email telling a platform or seller a requirement is due: "no one was taking responsibility".
- RA has started drafting termination emails. Emails to platforms are manual with "no infrastructure, no process, no agreed ways". Nothing goes to the seller directly.
- Named as a Checkout-wide gap: Jill needs it for risk, "Charlie definitely will need it from a care perspective", as do activation and configuration.
- Risk tone differs from what a customer relationship needs. No shared directory of who to contact for which email type.

**Risk agent SOPs**
- About 30% of requirements are raised more than once against the same property. Review owned by Alex M and Mirabel with ops, plus Bernard from Oliver's Ops Excellence team.

**Decisions (aligned)**
1. Static policy-based API validation on submission.
2. Document quality checks on submission (blurry, expired, missing corners).
3. Standard "requirements due" language.
4. Requirements-due webhooks fire immediately on check failure.
5. Check-level decisions for hard failures at first.
6. Default permitted and restricted MCCs on day one for single line-of-business platforms.
7. Stripe-style schema builder wizard in the docs site, fed by one schema registry ("no regrets").

Needs further discussion: unified customer lifecycle status and data products, and a table of which fields can be overridden internally.

**Measurement**
- Each team measures differently. Facilitator to build one customer-centric dashboard. New requirement stages must publish events to analytics, "otherwise the feature's not done".
- Items ship behind feature flags. Two of 18 were already done by day 2.

## Insights

- Care is named as a stakeholder in an unowned Checkout-wide communications gap: requirement-due and termination emails to platforms and sellers. No infrastructure, templates, owner or contact directory. Charlie should claim a role or push for an ownership decision.
- Instant webhooks, standard requirements language, API validation, document pre-checks and the schema wizard should cut "where is my onboarding" and "what do I fix" contacts. Track which of the 18 items ship to update the Platforms ISV contact forecast.
- Use Daria's lifecycle status data product as the onboarding-status source for Customer 360 and Agent Consultant. Do not build a Care-specific one.
- Ops Excellence (Bernard) joining risk SOP review is a link to Care SOP and quality work.
- Metrics: 30-50% document first-attempt failure, 50% bank statement failure, about 30% duplicated requirements, 85 checks for 17 applications, about 20 platforms by Easter, 50,000 platform merchants targeted next year.
