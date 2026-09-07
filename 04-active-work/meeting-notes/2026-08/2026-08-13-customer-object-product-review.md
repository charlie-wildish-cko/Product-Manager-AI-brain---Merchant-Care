# Product Review: Introducing the Customer Object at CKO

**Date:** 2026-08-13
**Attendees:** Joseph El Choueiri (presenter), Madhavi Misra, Chris Wade, Jamie Sims, Helder Goncalves, Manika Singh, Charlie Wildish, Umang Sota, Oliver Westlake-Simm, plus a wide product, GTM and CTO/CPO staff invite list
**Drive source:** 1UDsnAJg8tuvooZ7j2HRLnoElk-dLudpDBmkiIphOUcA

## Context

Company product review on introducing a centralised customer object on the dashboard, motivated in part by support volume on the payments page.

## Key Points

- The payments page drives 40-45% of all support tickets. It is the most heavily used merchant page; merchants struggle to consolidate information to help their own end users. Cost framing used in the room: ~40 per ticket to close. Current posture described as reactive KTLO.
- Proposal: a centralised customer object with schemas for customer ID, email, phone, card details/fingerprint, instrument ID, device ID, risk levels and audit logs.
- Identification method is a waterfall: take the merchant-provided customer ID first, then validate and resolve using email, phone, device ID and card fingerprint.
- Known data problems: Vault generates customer IDs inconsistently, producing one-person-to-many-IDs mappings; APM payloads lack standard customer/card structures and generate placeholder emails.
- Value beyond the page: merchant-facing analytics (GMV, LTV) comparable to competitors, fraud signals at customer level rather than payment level, future regulatory obligations, and support for the multi-product future (in-person, payouts, SMB).
- Challenge from the room: scepticism that a customer object reduces ticket volume. Joseph conceded the presentation conflated two workstreams (revamping the payments page versus introducing the customer object) and clarified the object provides the hierarchy that lets the page scale and fixes underlying data issues, rather than being a direct ticket-reduction lever.
- Chris Wade: device IP is a strong identification signal but adoption and fill rates are low, and genuine customers must be distinguished from bad actors actively avoiding identification.
- Jamie Sims and Helder Goncalves: a person may evolve from user to consumer to SMB user. Unifying identity across products reduces duplicated risk assessments and underwriting cost.
- Technical plan: make the customer object part of a payment lifecycle streaming source of truth, enabling real-time consistency and future integrations (open banking, in-person).
- Charlie argued the internal case: critical infrastructure to meet regulatory and servicing obligations, especially for products like open banking where Checkout must identify and support end users currently unknown to the system.
- Manika Singh on monetisation: large merchants ask for network-level insight on customer behaviour, but are generally unwilling to pay, so internal use cases are the primary driver. Monetisation model undefined.
- Scope of ask: no large investment, only analytics-team support to define the object. Initial customer identification floated for H1 2027.

## Decisions

- Proceed with foundational definition and testing of the customer object as a scalable base that many internal teams can develop against, despite undetermined quantitative ticket impact.
- Charlie to provide the regulatory obligations for identifying customers.

## Insights

- The 40-45% of tickets from the payments page and the ~40 per ticket cost now have company-wide airing. The causal claim that a customer object reduces contact rate was challenged and withdrawn, so it is not an agreed position.
- Care's leverage on this programme is the regulatory and servicing argument, not the ticket-volume argument, and Charlie owns articulating it. Open banking's unknown end user is the sharpest version.
- Consumer and SMB identity unification bears directly on Ray Care scoping.
