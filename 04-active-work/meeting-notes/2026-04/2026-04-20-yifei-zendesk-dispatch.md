# Yifei / Charlie — Zendesk Dispatch & Clean-Up Work

**Date:** 2026-04-20  
**Attendees:** Charlie Wildish, Yifei Zhang (Engineer)  
**Drive source:** 1s3YGaBTb3lpUDYi7fE4bIrdRKsmrUbHjhBWkJx-QnnY

## Context

Working session to address two structural data quality issues driving unnecessary manual work: unrecognized inbound users dropping into dispatch, and stale AM/TAM records in Zendesk.

## Key Points

**Domain mapping**
- Repeat contacts from known merchant email domains (e.g. ByteDance) are not being matched to their Zendesk organization on inbound. Tickets drop into dispatch and require manual identification and assignment.
- Fix: Zendesk's native domain mapping feature — set email domain at organization level, Zendesk enriches user records automatically on inbound.
- API-based implementation preferred over UI. Anna and AJ (Zendesk admins) to be consulted.
- Risk: if a generic domain (e.g. Gmail) is set, all contacts from that domain get assigned to the wrong org. Guard rails deferred to a later phase.

**AM/TAM record sync**
- AM/TAM fields in Zendesk organizations only update when a ticket is received — not on a schedule. Data is often stale when agents check relationship ownership.
- Fix: weekly scheduled sync pulling from the Salesforce BigQuery table to update Zendesk organization records.

**Third item shelved**: enrichment via organization/external ID — potentially a breaking change to existing flow, deprioritized.

## Insights

- Dispatch volume from unrecognized users is a data quality problem, not a routing problem. Domain mapping is a low-cost fix with potentially high impact.
- Stale AM/TAM data has practical consequences — agents routing escalations or adding context to tickets may be working with outdated relationship data.
- These are foundational data quality items. Resolving them reduces agent noise without any AI dependency.
