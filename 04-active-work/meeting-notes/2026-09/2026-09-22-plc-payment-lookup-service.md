# PLC payment lookup service

**Date:** 2026-09-22  
**Attendees:** Charlie Wildish, Federico Arduini (analytics/PLC). Lachie Fielding declined. Fraser away.  
**Drive source:** 1pLkEN2017js47vSxjunCsmI_CR5L8nR9WIMv57z0SpM

## Context

Review of Federico's payment lookup prototype and how Fin and Agent Consultant consume it. Follows the 2026-09-16 payment index and data context meeting.

## Key Points

**Prototype results**
- Works. Latency 2-5 seconds, slightly above promise but acceptable.
- Cost is a fraction of a cent per request on the standard PLC BigQuery reservation. Scales considerably.

**Q4 scope (Charlie)**
- Migrate existing lookups to the lookup service plus BigQuery for payments.
- Test with Agent Consultant first (no customer impact), then move Fin.
- Both call one central retrieval layer and interpret for their own audience. Today the internal agent uses fct_payin (full data) while Fin's dataset lacks fields, so Fin answers fewer questions.

**Architecture**
- The lookup contains business logic: dedup, choosing fct_payin vs fct_payout vs other sources, a new dispute yes/no indicator.
- Consumers call a Lambda or API endpoint, not BigQuery directly, so the logic is not duplicated.
- Evolve from returning the location (payment ID, table, partition) to returning the full payload.

**Field subsetting**
- Charlie does not want all 500+ pay-in fields. Use the existing field spec (pay-in and pay-out, up to about 50 fields each).
- Federico: requests can specify fields, all available by default. Charlie wants minimal field-management overhead and no bottleneck on Federico's team.

**Semantic layer**
- End state: pass an ID, get payload plus semantic descriptions, so the AI interprets data without Care maintaining large prompts.
- Hamish leads the semantic initiative. Interim (v0/v1): payment index plus BigQuery payload plus dbt schemas from GitHub.

**Domain expansion**
- Order: pay-in and pay-out, then Financial Actions, then FX settlements and balances. Later, integration data (owner unknown, small share of contacts).
- Principle: Care is domain-agnostic, a customer of every domain. Domain owners provide definitions. Federico agreed.
- Charlie wants the same pattern for Ray consumer transactions, as a general "transaction lookup".

**Latency budget**
- Chat: about 30 seconds ideal, 30-60 seconds acceptable with expectations set. Email: a couple of minutes.
- Current internal flow (payment search then BigQuery pay-in) is about 3-4 seconds.

**Productionisation**
- A pay-in implementation is already a goal for Federico's half. Federico's team has no software engineers and one data engineer. Lambda access and engineering practice go to Fraser, Anish and Jiro.
- Checkout previously had four inconsistent payment lookup options. This replaces them.

## Insights

- The lookup service is the single data retrieval backbone for Fin and Agent Consultant (Fuel domain).
- Fin data parity with the internal agent directly lifts Fin resolution, feeding contact rate and cost per contact.
- Chat latency budget: 30-60 seconds end to end (service plus AI reasoning).
- Domain teams own semantics. Care does not maintain data definitions.
- Field spec is `04-active-work/research/payin-payout-data-requirements-master-list.md`.
