# Charlie / Joseph: Reframing the Customer Object

**Date:** 2026-08-14
**Attendees:** Joseph El Choueiri, Charlie Wildish
**Drive source:** 1xyBkJiDQytpTiBGyVFxjQrVUO6U7ZNBLZ6rl8GVz7ZQ

## Context

Follow-up after the customer object proposal failed to land at the 13 August product review.

## Key Points

- Joseph's diagnosis: he framed it as fixing the payments page and support (downstream to upstream) rather than stating the business need. His admission: "I don't have a merchant-facing problem that is tangible and quantifiable today."
- Charlie's counter-framing: there is a fundamental gap in the customer data Checkout stores, and internal consumers (OCS/Care, fraud, payment setup) are the biggest consumers of it. Not optional for them.
- Data quality specifics: APMs return account-holder names not emails; dummy emails get populated; Vault customer_id populates with duplicates in roughly 20% of cases; card payments give a name, not an email.
- Joseph's plan: run a waterfall analysis with the analytics team (with Hish) to measure current confidence, for example "for Netflix we can identify 80% of traffic as having a customer, 20% we can't, and here's why." Target roughly 80% of merchant transactions populated into customers, using existing mechanisms (Flow, Remember Me) rather than adding schema burden on merchants.
- Care requirement: enough attributes to identify who contacted them and trace them to a transaction. The attribute set can differ per consumer; Care may need only three (email, name, one more).
- Regulatory angle: new end-user products (Issuing, Open Banking) carry end-user support regulations. A legal document states requirements to support these customers (must hold email plus phone number) with no guidance on identification. Charlie cannot size the risk without volume data on affected users.
- Monetisation: Remember Me already does customer matching but across a narrow slice of transactions. Network-level data can be sold as card-instrument analytics without pure customer matching. Vault is Ramy's packaging play, appetite unproven.
- SMB angle: the more SMB a merchant is, the more they use their processor as a CRM. Stripe does this today. Joseph to research Shopify and other SMB platforms as evidence.

**Data certification**
- The BigQuery migration did not deliver certified data products. Charlie raised it and was told certification was not in scope. Half the business has uncertified data products.
- Certified means in DataHub with a schema and a semantic LookML definition. With that in place, an AI or Looker MCP can interpret the data and convert a query into the data's semantics, which is exactly what Care has already done for its own care data.
- Timelines: authentication data correction took 9 months and is still not fully done; risk is in UAT; disputes will not be done in Q1. Value-added services, settlements and financial data untouched.
- Root cause is not the data platform team. Individual product teams must onboard and certify their data, which was supposed to happen last year and was not enforced. Charlie: weak enforcement will bite when propositions scale.

## Decisions

- Reframe the customer proposal to lead on SMB dashboard plus monetisation potential, gated behind a first data-analysis phase validating customer identification confidence.

## Insights

- The customer object is a dependency for Care's Customer 360 and for end-user support of Issuing and Open Banking. It is currently unfunded and its PM has no merchant-facing problem statement. If Care needs it, Care must supply the problem statement and the volume data.
- Care's Looker MCP and semantic-layer work is the internal proof point for why certification matters. Reusable with the data platform org.
- Charlie has a two-year audit trail of raising data certification. Useful when a Care deliverable slips on a data dependency.
