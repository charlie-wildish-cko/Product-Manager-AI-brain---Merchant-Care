# Payment diagnostics for AI — required data points (Armi)

**Date:** 2026-07-29
**Attendees:** Charlie Wildish (PM, Merchant Care), Armi Mujica (payments team, ex-Care)
**Drive source:** 1GcfH2sFwnIsm_dRl4MCfIUUMYhVmEXLSE5JtGdg6Un4

## Context

Second SME review of the merchant-facing transaction analyzer. Armi is stepping in as payments SME cover while Keziah Zhou is on maternity leave from mid-September 2026. Purpose was to enumerate the data points a diagnosis actually needs.

## Key Points

**Architecture**
- Fin receives a merchant payment query, passes the query plus payment ID to the in-house Customer Agent, which fetches data, diagnoses, and returns an answer. Fin completes the interaction.
- Not using Fin directly: it is third-party, cannot reach internal data, and Checkout's APIs are weak for retrieving complete data.
- Not using the payment performance solution: built for internal consumption, too slow, too risky. Its data sits in a payment-performance-specific BigQuery table.
- Existing transaction analyzers (payment performance, gateway) are internal-only. No merchant-facing equivalent exists.

**Data source and roadmap**
- Today: payment search API (the one behind the dashboard), keyed on payment ID / ARN / RRN / reference fields. Has the core data points but not the historical trend data payment performance uses. Charlie's judgement: trend data isn't needed for most merchant queries, which are single-decline questions. AR-type questions are out of initial scope.
- Merchant-facing data is being replumbed onto the PLC streaming dataset, and the payment search API is in scope to be swapped onto full PLC data. Design on the assumption all pay-in and pay-out data becomes available.
- Looker fields are the mapping target: "the Looker fields directly map to the sources of truth now." Three explores: payments, pay-to-card, authentication.

**Data points required — pay-in**
- Card type (debit/credit/prepaid); network token type (VTS vs MDS); preferred scheme (e.g. Cartes Bancaires vs Mastercard dual setup in France); region and regional regulation; wallets (Apple Pay / Google Pay); payment method; transaction type (regular, recurring, installment); entity; processing channel name and ID (merchants recognise the name from the dashboard); currency; amount format (merchants send formats that don't match documentation: decimals, commas); MCC; response codes; issuer; acquirer routing; AFD flag; scheme monitoring programs; card fingerprint retry counts (a fingerprint retried 16 times triggers suspected-fraud declines); 422 errors.

**Data points required — pay-to-card / payouts**
- Funds transfer type (derived from how the merchant is onboarded, configured on the processor table); enabled destination countries (example: Puerto Rico not enabled for card payouts); destination and sender country; geographic scope (domestic vs cross-border). Example failure: a Belgian issuer declining transactions originating from a French entity.

**Authentication**
- Authentication status, ECI, hosted vs unhosted integration. Confirmed in scope as a functional requirement.

**Main flow**
- Fetch record, read outcome using response code as the primary checkpoint (status plus response code), identify which data points drove that response code, consult the decline debugger, produce output.
- Escalation flag returned to Fin for hand-off. Non-self-resolvable cases (e.g. configuration issues) escalate to a human. Charlie is cataloguing these edge cases.
- Merchant-facing output: what happened / why / what to do next. Separate internal trace log for audit, never exposed.

## Insights

- The strategy is data-availability-led, not reasoning-led. Confirm the field list first, then codify rules off the returned values: "once we get those back it's really easy to write the rules off the back of those."
- Looker field names are the canonical bridge between SME knowledge and what the agent can actually access. Any field an SME names has to resolve to a Looker field or it isn't buildable.
- A 40x-range response code means something different on a payout than on a pay-in. Payout logic cannot be a copy of pay-in logic.
- Sequence simple queries (declines) first, add complexity over time.
- Next step for Charlie: pass the required data points list to the data team to verify availability in the current dataset. Armi to share the payments and authentication Looker dashboards (the payments one is already shared with merchants and kept current) and review both AI flow docs for gaps.
