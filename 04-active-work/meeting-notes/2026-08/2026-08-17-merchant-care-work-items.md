# Merchant Care Work Items

**Date:** 2026-08-17
**Attendees:** Pao Igarteburu, Fraser Bryant, Charlie Wildish, Imran Khan, Lachie Fielding, Sundy Munusami
**Drive source:** 1DCySKxXfSvMOFUKARA8LPz9wYulSIYj3IBn67vtY6Rs

## Key Points

- Reflex data: adding an additional column resolves a chunk of missing production data. Group agreed to run a backfill for complete coverage.
- Client filtering: Zendesk is the source of truth for client names, with Fin/Intercom data as fallback. Client name becomes the standard filtering mechanism.
- Entity granularity: Charlie argued the entity field is too granular and randomly populated for business-level filtering. Use a primary legal entity field as the default for better coverage when the specific user entity is unknown.
- MALP regulatory reporting logic: check the client's CKO legal entity and tag tickets where the primary CKO legal entity matches MALP, so Ops can extract tickets for impacted merchants.
- Payment lookup service (built by Hish's team, testable within ~2 weeks): identifies the transaction type and the exact location of its metadata (table and partition), removing manual mapping. Domain knowledge lives in the service response rather than in each consumer.
- Data source strategy: streaming events for recent data (roughly the last hour), BigQuery for historical data and disputes. The lookup service routes queries by transaction type.
- Iceberg versus DynamoDB: plan to test the lookup service against Iceberg to see whether it fixes earlier performance problems caused by non-indexed data. Iceberg preferred on cost provided data is properly sorted.
- Fin webhooks for back-office automation: TPA lookups, refund reversals, manual refunds. Estimated to remove 10-15% of current agent work volume from manual Zendesk processing.

## Decisions

- Exclude entity-level granularity from filtering logic.
- The lookup service returns transaction type plus its specific data source, centralising domain knowledge in the service.
- Unresolved: how schema determination is handled inside the lookup service.

## Insights

- Zendesk, not Fin, is the agreed client-name source of truth, and entity-level filtering is out. This settles a recurring reporting argument.
- The 10-15% agent-work reduction from Fin webhook back-office automation is a concrete number for Agent Consultant and task automation business cases.
- The payment lookup service is a shared dependency and the practical unblock for both agent tooling and Reflex-style analysis. Confirm its scope before building on it.
