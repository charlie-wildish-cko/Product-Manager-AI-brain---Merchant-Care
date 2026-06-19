# Quick Chat on Creating SF Cases Over API

**Date:** 2026-06-19  
**Attendees:** Charlie Wildish, Anneliese Hainz (leaving Jul 31), Priya Nair  
**Drive source:** 1HxP1zwES6pHi3KW5QOOpAbmCgqHQ48Jged8fUpaDNqA

## Context

Handover meeting. Anneliese leaving Jul 31 — Priya Nair is the handover contact. Discussion surfaced significant delivery risk for the B2C consumer programme.

## Key Points

**Consumer programme infrastructure gaps**
- Programme management has stated "no Salesforce impact" for the consumer programme. Anneliese disputes this.
- Every existing ops team (Care, Risk, Disputes, Compliance) will need to service consumer queries — same teams, different regulatory environment (FCA, tighter SLAs, no tolerance for manual handling delays).
- Consumer data will NOT be stored in Salesforce (decision made — separate CRM/system TBD, likely synced to BigQuery). But ops teams work in Salesforce Service Cloud — a connection between the consumer data system and Salesforce must be designed. It has not been.
- Consumer entity IDs risk overlapping with merchant entity IDs in Salesforce — data segregation and access controls are an unresolved requirement.

**Zendesk integration gap**
- Current Zendesk → Salesforce integration is email-to-case only: no structured data transfer, no inter-system SLA tracking, no ability to pass key data fields. Not fit for consumer programme requirements.

**Central consumer data system**
- Does not yet exist. Data model still being defined.

**Cross-team servicing design**
- End-to-end servicing design for consumers (which team handles which query type, what actions each team takes) has not been done. Assumed Care covers everything — it doesn't.

**Decision**
- Escalate to Oliver next week to confirm Salesforce impact and rescope H2 plan as needed. Flag to PMO.
- Priya Nair is the handover contact for this workstream.

## Insights

- This is a live delivery risk for the B2C consumer launch: foundational ops infrastructure not built, Salesforce integration not scoped, no cross-team SLA tracking, no consumer servicing design. The "no Salesforce impact" assumption may cause a planning gap to surface late.
- The B2C launch is already present in the Intercom renewal forecast (40,000 resolution volume) and the May 28 Klarna/knowledge session noted October delivery was at risk. This session confirms those concerns are well-founded.
- Consumer and merchant entity ID collision in Salesforce is a compliance and data quality risk — needs a deliberate data architecture decision, not just access controls.
- Anneliese's departure Jul 31 means continuity must be managed through Priya Nair and Oliver before Charlie's leave starts Jun 22.
