# Consumer Ops Application Workshop

**Date:** 2026-08-12
**Attendees:** Charlie Wildish, Joel Petrosino, Georgios Maninis
**Drive source:** 1m9A-t4vve7bk252IkeJIcjh6Dot_-Zdt8vSTfw7XPEQ

## Context

Working session on what a consumer ops application should be, using Starling Bank's internal ops tool as the reference model, ahead of presenting a vision prototype at the 25 August state meeting.

## Key Points

**Starling reference model**
- One ops management tool consolidating KYC/verification data, transaction data and payments data, with embedded support flows. In-app chat launched from a data point in the consumer app arrives pre-populated with that transaction.
- Onboarding queues, monitoring, risk reviews and fraud reviews all in the same tool, with role-based permission layers (a frontline agent can see that a risk review exists but not its detail).
- Starling packaged and sells this as Starling Engine. Tam in the commercial team knows a PM who led Starling Engine in Australia and is the route to a case study.

**The core distinction**
- Merchant/B2B Care exposes information to agents by data point. Consumer support must expose information by entity.
- With an async merchant experience, agents get away with hopping between Payment Toolkit, CAT and Genesis for one query. A live consumer chat experience makes that unworkable.
- Proposed "Entity 360": search a customer and immediately surface onboarding, risk, transaction, consents, flags, vulnerability status and contact history in one view, with actions in context (freeze card, reversal, clearing).

**AI and case management**
- AI as sidekick: automate triage and simple queries end to end, summarise tickets, execute discrete actions via an MCP-style layer mapping task to action without the agent leaving the interface. Hypothetical split floated at roughly 80% automated, 20% human for sensitive actions. Consumer actions judged largely binary and far less complex than merchant queries.
- Keep the workflow tool and the case system separate. The new tool triggers tasks and executes actions; the case system is the immutable log and source of truth, with bidirectional sync. Framing used: "your case doesn't start in Salesforce, it ends in Salesforce."
- SLA insight: for teams like onboarding, the clock should start when the event enters Checkout's systems, not when a case is assigned.

**Gaps and constraints**
- Contact history was a requirement Care gave the upstream team and is absent from what was built.
- Data requirements have been given to Fraser's team so they know what Care needs to consume. Day-one expectation: customer record, possibly transactions.
- Running the toolkit app locally inside Zendesk was painful, which argues against hosting inside restrictive systems.
- Ray and Braavos assumed to share infrastructure with different content filtering and downstream routing by audience, and a potentially higher fraud/risk profile for Ray.

## Decisions

- Build the consumer toolkit as an independent, host-agnostic application, not embedded into the existing portal or Zendesk.
- Split the toolkit UI so search and workflow queues are separate from account detail views, with queues laid out per team and task.
- Keep case management and workflow tooling as separate, linked systems.

## Insights

- Entity-centric versus data-point-centric support is the strategic wedge. It is the argument that unlocks a separate consumer ops platform rather than another layer on Genesis, CAT and Payment Toolkit.
- Open question left unresolved: is this built for Care only, or as a foundation other ops teams extend? Charlie's preference is agnostic-for-all-ops, which would address tooling fragmentation directly.
- Caveat raised in the room: Starling could afford this with a large team and heavy investment. Checkout may need far less bespoke tooling if the help desk covers it.
