# Charlie / Hamish: Lookup Service and Data Sources

**Date:** 2026-08-17
**Attendees:** Charlie Wildish, Hamish Chreseson
**Drive source:** 1UcA0SKg47_LYIo8JZmzJh5h69g3oSayXh-KC3J9bnv0

## Key Points

- Two workstreams Care depends on: the lookup service, and the right data sources to read from off the back of it. 2026 scope is card pay-in, card payout and bank payout. Consumer and issuing transactions come later.
- Care previously aligned these timelines to the portal connect deprecation project. Both agreed to decouple: Care can get value before portal connect delivers.
- Federico targeting a testable lookup service by end of w/c 17 August, with functional delivery within Q3 2026.
- Current constraint: Care only uses the dashboard search API (a narrower dataset than the full payment search API) and is not querying card payouts at all, despite a good card payouts data product existing. The lookup service is the blocking dependency.
- Lookup service design: input is one of three identifiers, output is object plus partition plus payment ID. Hamish's team provides the lookup table; Care's engineering consumes and routes. The point is to abstract away pointing logic so Care does not hardcode source paths and the AI agent can retrieve data without them.
- The streaming data product (facts pay-in) covers gateway-derived data only: request, auth, capture, refunds, near real time, plus existing authentication data. It does not contain dispute, fraud or routing data. Dispute data depends on the disputes team's own data product, nominally Q1, which Hamish doubts given disputes has already slipped roughly half a year.
- BigQuery latency for pay-ins is now under 2 seconds when the requested date is supplied, which undercuts the short-term latency argument for streaming. Internal use is latency-tolerant; customer-facing is not.
- Charlie flagged the branching-logic risk: a time-based cutoff adds engineering complexity. Preferred resolution is the lookup service itself declaring where to go (if this payment has a dispute, use BigQuery; otherwise use the stream), with source traceability logged per query.
- Care wants an explicit list of what is not in the stream so routing rules can be derived by feature depth rather than by time.
- Looker MCP floated for non-payment-ID lookups (currency account IDs, entity IDs, balances) and for consumer and issuing. Both agreed MCP is the end state. Charlie's constraint: engineering does not want to manage three different APIs for different use cases.
- Remitly incident detail: they switched off another provider and ramped card payout volume 300-400% without proper training or configured payout routes and regions, so volume hit sanctions screening, generating RFIs and declines. Care cannot automatically detect whether a card payout has a sanctions-screening flag or RFI attached, because that depth is absent from the dashboard search API. The card payouts data product does contain it.
- Charlie is interviewing for Imran's replacement.

## Decisions

- BigQuery is the primary source where the streaming product lacks parity, specifically for dispute, fraud and routing context.
- The lookup service is adopted as the central routing and abstraction layer. No hardcoded pointing logic in downstream Care services.
- Phased rollout: the lookup service replaces the payment and dashboard search APIs first for merchant transactions, with issuing and other types added later via schema extension.

## Insights

- The lookup service decouples Care from every individual product team's data-product timeline. Once it exists, Care adds a use case by extending the lookup schema rather than contracting with each source. This is the argument to use when other teams slip.
- The Remitly incident is quantified evidence for data depth: a 300-400% volume ramp, preventable contacts, and a missing capability (sanctions and RFI flag detection on card payouts).
