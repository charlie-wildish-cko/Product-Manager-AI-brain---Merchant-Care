# Identifying a Customer

**Date:** 2026-08-20
**Attendees:** Joseph El Choueiri (chair), Hei Lap Man, Roberta Conrad, Chris Wade, Erez Segal, Hamish Chreseson, Charlie Wildish, Michael Cummings, Reenah Muldavski
**Drive source:** 19ReIjeT-e42_wgiFNspdk_zyk9aB5IpcFLsB0ZwFftA

## Context

Working session following the customer object product review, defining a customer at merchant level to improve the merchant dashboard. Charlie attended without speaking; the value here is the identity-resolution ceiling.

## Key Points

- The Customer ID field is only populated 20% of the time. Vault populates a Customer ID on every transaction but it is not reliable: some merchants misuse it, generating multiple IDs for one person, and the same card matches multiple Customer IDs. Not a persistent single-person identifier.
- Proposed waterfall identification using email, phone, IP, device fingerprint and card number. Secondary aim is to find where the waterfall fails, so fixes go upstream to product teams (Vault Customer ID, APMs carrying account-holder name rather than customer name).
- Erez Segal's graph modelling: 57% of payments belong to an entity, 45% of payments link to a previous payment. He proposes calling graph entities "user" or "online user", covering both genuine customers and fraudsters.
- Chris Wade: keep terminology in sync with the fraud investigation tooling planned for early next year, so merchants are not confused switching between identifying good customers and identifying fraudsters.
- Legal constraint: prior legal counsel feedback advised against profiling customers outside agreed T&Cs, specifically about showing risk scores to merchants. Joseph confirmed network-level benchmarking will be aggregate and anonymised with no PII. Chris to circulate the legal email.
- Data quality: common names and restaurant-generated emails will pollute graph linking and must be filtered. Mitigation is giving merchants transparency on how customers are calculated and letting them edit the schema in the UI.
- Success metric for iteration one: the percentage of payments that can be linked to a single person at merchant level, not merchant utility.

## Decisions

- Proceed with the waterfall approach for the merchant-level customer definition.
- Split scope explicitly: V0 is merchant-level customer, V1 is network-level customer, documented separately so both can be prioritised independently.
- Hamish Chreseson owns the customer-definition analysis and identification success rates. Hei Lap Man reports on the source of Customer IDs within two weeks. Joseph consults Ramy on whether merchants send Customer ID or it is system-generated, and updates the PRD with the V0/V1 split.

## Insights

- Customer 360 and identity resolution have a hard ceiling today: 20% Customer ID population, 57% graph entity coverage. Any Care use case depending on identifying a merchant's end customer (consumer-side disputes context, Ray, fraud contacts) inherits that ceiling.
- The guest-user identification problem in the Plain architecture session is the same problem. Open banking payers are identifiable only via the transaction's customer object, which is exactly this waterfall. The two workstreams should be linked.
- Legal's position on profiling constrains any Care-facing feature that would surface a risk score or behavioural profile to a merchant.
