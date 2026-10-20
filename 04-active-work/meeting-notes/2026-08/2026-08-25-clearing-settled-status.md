# Jason / Charlie - Clearing/Settled status & Care

**Date:** 2026-08-25
**Attendees:** Charlie Wildish, Jason Dantzer
**Drive source:** 1hOxj2qpHxDuqI9GSyFa2yxaymWYU-hNatvmUhuJmiS8

## Context

Review of Jason's clearing and settlement status roadmap and what it gives Care for settlement-visibility contacts.

## Key Points

**New status step**
- A "settlement scheme to Checkout" status is being added (scheme-to-Checkout, not Checkout-to-merchant), with success and failure states plus failure detail. Naming is not settled: it depends on the granularity engineering can provide.
- Scheme coverage: Visa, Mastercard, AMEX, DCI. Engineering targets all schemes by end of year; Jason is planning Q1 to guarantee full coverage.

**Why it slipped**
- Deliverables originally due Q2 moved to Q3, which stalled discovery. Technical specs for failure-state events have not been received and failure-state event granularity is undocumented.
- The work was prioritised largely because of Braavos. The Braavos pause caused engineering to slow their definition work, so Jason still has no data.

**Failure states are not final**
- Per Hugh and Paul, a reported failure can change later: the scheme may send a settlement a month afterwards when no transaction-to-settlement match was made after N days. A Visa 93-type retry produces the same effect.
- Named merchant pain points today: C1 stop payments (Visa) and Mastercard returns. A third case is an erroneous clearing-team retry, where Care told merchants a payment had failed when it was actually a clearing retry.
- Trade-off: waiting longer gives higher accuracy but affects liability and the timing of paying money out before funds are visible.

**Data availability**
- A `settled` event exists under capture and refund. A `clearing failed` event exists in the schema but exposure is uncertain: the last check said it would not be exposed.
- Settlement data gives enough retrospective visibility into failed clearing cases, which Jason considers sufficient for most cases.
- Paul demonstrated that some of these data points already exist in BigQuery. Jason described the owning engineering team as very hard to extract information from.

**Decisions**
- Prioritise accuracy and finality for settlement failure statuses: accept a longer reporting delay rather than publish a preliminary failure state that later needs correcting.
- Scheme integration timeline moves into Q1 for full coverage.

## Insights

- The clearing/settled status work is behind, and the root cause is a chain: Braavos pause, engineering deprioritised event definitions, no spec, no discovery. Care's settlement-visibility deflection depends on the end of that chain.
- The finality decision has a direct Care consequence: merchants get accurate statuses but later, so "where is my payment" contacts will not be removed in the window between clearing and confirmed settlement.
- BigQuery already holds some of the data, so a Care-side Looker or data-product workaround is feasible ahead of the productised status.
- The erroneous clearing-retry case is a confirmed instance of Care giving merchants wrong information from incomplete status data, which is a quality argument, not just a deflection argument.
