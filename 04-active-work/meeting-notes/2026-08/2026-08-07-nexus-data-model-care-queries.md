# Nexus Data Model and Care Query Needs

**Date:** 2026-08-07
**Attendees:** Charlie Wildish, Paul Jaines (Gemini merged both speakers under the room label "LON-03-02", so individual attribution is unreliable)
**Drive source:** 1HTieFjZdKhgHJSSbDGxc2LjjJQzAprsc6uEUw5jiC-E

## Context

Walkthrough of the Nexus transaction data platform roadmap to work out whether Nexus can become the single source of truth for Care's transaction-status and fee queries, replacing the current fragmented lookups.

## Key Points

**Nexus status and roadmap**
- Live since 1 July 2026 with a "first cut" implementation. Billions of records ingested since go-live.
- Target: 100% of trading activity covered by end of 2026. All live schemes (Visa, Mastercard, Amex) are in now.
- Clearing data lands "the 27th"; blocked until upstream teams complete their work.
- Standardises IDs across disparate source systems, then configures per transaction type (e.g. acquiring) to pull in gateway costs into one consolidated transaction view.
- BigQuery is the storage layer: one long row per transaction, enriched with additional events over time. Looker MCP is being configured on top so the data product can be certified and queried.
- A PM is being recruited specifically for Nexus to own the requirements backlog. Current data structure was built by engineers in roughly 4 months.

**What Care needs from it**
- The two highest-value additions for Care are `scheme advised` and `cash matched` events. These would answer "the payment says captured but I have not received the funds", which today goes to a human agent for a manual check.
- Care needs roughly 40 data points for transaction tracing. Current accessible services hold about 20 of them.
- Fee explanation is a second gap: reconciling the actual fee against what the merchant expected, and explaining why the fee is what it is.
- Existing lookup tooling (the Cloud IO app built by Mariano and Andrew) allows payment-ID lookup but is not a reliable, stable source for AI tooling.
- Care's effectiveness metric is AI resolution rate. Where no data exists for a query type, Fin cannot answer and the contact routes straight to a human.

**Transaction lifecycle and settlement**
- Nexus models two lifecycles per transaction: Checkout-to-scheme (captured, cleared, advised, cash matched) and Checkout-to-merchant (pricing and billing events, balance impact).
- Predicted values from point of capture: interchange, scheme fees, settlement amount, settlement date/time. Scheme-advised amount and final cash match are tracked separately for liquidity management.
- Client settlements now settle balances rather than individual transactions. Merchants cannot trace a specific transaction to a settlement run or to funds held back. Alex's team is building the backwards trace (transaction to balance, including negative-balance deductions and minimum-balance holdbacks).
- Dashboard settlement matches are currently inaccurate (scheme-to-Checkout side); Alex's team is fixing.
- Gateway implementation for exposing the extra statuses to merchants is unlikely to land in 2026. Internal query access is available regardless, which limits this to internal use in the near term.

**Card payouts**
- Card payouts are ~10% of volume against ~50% for pay-ins.
- Payout data is poorly validated before the sanctions process. Overly generic data triggers a sanctions hit, leaving merchants with stuck payments and no visibility of where they are stuck. Rich internal enrichment data exists but is not exposed.
- Payouts also clear and support reversals; Mastercard supplies that data but Care has no access.

**Productisation model**
- Nexus is moving to a "Nexus contract" model: a new product (card payouts was the example) publishes standardised documentation, UX design, and training procedures rather than each team coordinating manually with finance and treasury.
- Charlie's parallel ask for the operations equivalent: a product is not shippable until it has documentation, designed fail states, and agent training/procedures. Input likely via MCP, output auto-generated into requirements.

**Financial controls**
- A control framework is being built on top of Nexus for horizontal querying, e.g. flagging a transaction missing an expected cost-of-sales event after two days.
- Engineering sync planned for the following week with Paul and the Talon engineers to agree the query source. Some Talon engineers are out (August).

## Insights

- Nexus is the credible long-term answer to Care's transaction-data fragmentation. It is live, holds real data, and its owner is actively inviting Care requirements into the backlog. This is the moment to get Care's 40 data points prioritised.
- Care currently has access to about half the data it needs for transaction tracing. That gap is a direct cap on Fin's resolution rate for payment-status and fee contacts, not a nice-to-have.
- The "captured but funds not received" contact type is resolvable with two fields (scheme advised, cash matched). It is the cheapest large deflection win available from Nexus.
- Balance-based client settlement created a new structural contact driver: merchants can no longer reconcile individual transactions to settlement runs. Volume here will grow with Business Account adoption.
- Merchant-facing exposure of the new statuses depends on gateway work that is not expected in 2026. Plan Care use as internal-only (agent and Fin lookups) rather than self-service deflection in the near term.
- Card payouts carry a disproportionate contact risk relative to their 10% volume share: sanctions-driven stuck payments with no merchant visibility.
- Consumer scale changes the tolerance for manual workarounds. Consumer protection and complaints-handling obligations mean the data platform has to be scalable and auditable from the start, which was explicitly stated as a reason to reject "hacky" solutions.
