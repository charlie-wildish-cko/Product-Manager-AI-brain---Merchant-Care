# Breaking a product domain into Components

**Date:** 2026-08-04
**Attendees:** Henry Zhang (Financial Platform product lead), Charlie Wildish (PM, Merchant Care), Gilles Beausseron (Risk & Compliance)
**Drive source:** 1a5Z2loo1WMWRM0Prbhapuu9hEYwyzIJbYw5g2FXvax4

## Context

Charlie and Gilles asked Henry to walk through how he decomposed the Financial Platform domain into independent components, to borrow the pattern for Merchant Care and Risk/Compliance.

## Key Points

**Charlie's stated problem**

- Care and Risk/Compliance both depend on how well products are integrated and supported, but neither is built to be consumed as a service.
- Product-launch handoff today is manual and messy: someone says "this is launching in a month, can you do this?" with no structured requirements.
- Open questions at launch: is the product ready for support, is documentation complete, are teams ready, are checks/compliance/reporting in place. Some products and requirements appear with no notice. MCAP helps as an input but does not solve it.
- Target: a productised launch-readiness service that auto-generates requirements. Splits into a technical component and a human-readiness component.

**Henry's Financial Platform model**

- Diagnosis on joining: no centralised, accessible transaction-level data platform for merchant transactions. No unified schema across products, no end-to-end transaction monitoring. Contrast with Stripe, where a warehouse lets you look up a transaction and see when it happened, when it cleared, when cash settled, fees, and safeguarding rules.
- Charlie's Care use case was one of Henry's validation points: a care agent on a call needs to look up a transaction and cannot.
- Layered abstraction: product to set of transactions to transactions to "legs" (states and state transitions). Rules such as accounting triggers attach at each state transition.
- Every user activity with financial impact is a transaction. Every transaction has exactly one correct outcome, defined a priori. Flexibility lives in execution, not outcome. Example: accelerated payouts can be funded via corporate cash, local FX partners, or a cross-border wire, with the same outcome.
- Schema tested against roughly 40 existing products to confirm it was extensible enough.
- Two main drags on launch velocity for finance readiness: accounting and safeguarding.
  - Accounting logic currently lives in code, so Finance hand-builds it per launch. Moving to configuration: code still executes, but chart of accounts, debit/credit, and timing are expressed in config. Easier to audit.
  - Safeguarding (still being vetted): model per product/merchant as config. Fund type, when liability starts (logical money vs cash arrival), when it is extinguished, triggers. Goal is self-service per product.
  - Third, less tractable: cost of sales. Own-product costs are a database lookup; network bulletins are complex, so they are building a link from bulletin feeds to invoices.
- Nexus is the linking engine plus data lake: connects upstream systems into one cohesive transaction view. Streaming layer for millisecond access, persisted into BigQuery for analytics.
- Tooling: a UI service that helps product teams model transactions, legs and states, with AI-proposed accounting rules inferred from similar existing workflows. Output is a fund flow plus recommended accounting rules that Finance approves in a day or two.
- Fund flow is the crux. Last year's planning churned because no comprehensive fund flow existed, so each cross-functional team discovered a partial version.

**Corrected anti-pattern**

- Previously, linked data was aggregated and fed only into Workday, with Workday as the sole internal consumer. Henry called this wrong: too much logic in Workday and no company-wide access to transaction-level data.
- Reversed: accounting logic sits inside Checkout, not Workday. Workday is a GL and may do aggregation only. Reconciliation, checks and analytics move in-house.
- Duplication is the enemy. Safeguarding alone has dozens of unsynced duplicate copies, and Finance operators absorb the cost through reconciliation. Target state: one canonical view per use case (tens of views, not hundreds), authored on demand on shared underlying data, gated by a data model review. AI makes authoring views cheap, so teams should stop keeping local copies.

**Where the analogy breaks for Care and Risk**

- Gilles: Risk/Compliance splits in two. Gathering information about parties in relation to customers does not fit the transaction model at all. Historical actions on an account is unique to Care and Risk, and nobody else holds it.
- Gilles' framing: "you're the happy path, I'm the unhappy path", and they sometimes merge. What is missing is a central customer-relationship view: when they contacted us, through which channel, their pain point, decisions made, data captured, questions asked, when an action was permitted.
- Gilles flagged a volume shift: as Checkout adds more customers, each customer makes fewer transactions, so the unit of analysis becomes the transaction in relation to the customer's activity and lifecycle, not the transaction alone.
- Charlie's Care equivalent of the transaction is the query. The data model is queries plus the query's relationship to the customer. Worked example: merchants using fast money movement (A2A transfers) generate queries when things go wrong, because intent is high. At launch the chain should run: how the product works, what questions people will ask, does that fit the taxonomy, does that taxonomy link to existing content, what new pieces are needed.
- Charlie's view: Care already has a strong data model and data product. The gap is being driven by question type, which determines everything downstream.
- Both Charlie and Gilles landed on needing an identity layer / central customer-relationship view. Charlie said Care intends to build this next year.
- Henry's read: Care and Risk should pull transactions from Nexus as source of truth and treat merchant care history as enrichment. Onboarding/compliance may need a separate model because it is pre-launch and may not depend on transactions. Gilles pushed back that his domain is not transaction-based, though there is plenty they want to layer on top of transactions.

## Insights

- The transferable template is data model first, controls at state transitions, applications last. Not applications with data bolted on.
- Care's analogue of the transaction is the query; the analogue of legs and states is the query lifecycle. Modelling the states is what allows rules (routing, escalation, content scoping) to attach at defined points.
- The launch-readiness ask has a proven precedent: Financial Platform solved "every launch needs bespoke manual work from my team" by moving per-launch logic into configuration. Care can argue the same shape for support readiness.
- Care and Risk jointly own the only dataset nobody else holds: the history of the relationship with the account. That is the strongest claim to owning an identity/relationship layer, and the natural boundary against Nexus (Nexus owns transactions, Care owns relationship history as enrichment).
- Fund flow ambiguity was the single biggest source of cross-functional churn in last year's planning. The Care equivalent to watch for is an incomplete view of what a launching product does, with each team inferring its own partial version.
- Data governance precedent: one canonical view per use case, reviewed. Teams that keep local copies create reconciliation work for operators downstream.
