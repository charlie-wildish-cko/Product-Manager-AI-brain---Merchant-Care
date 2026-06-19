# Reflex Plan for Q2

**Date:** 2026-03-31  
**Attendees:** Charlie Wildish, Jiro Farah (engineering lead), Imran Khan, Pao Igarteburu, Lachie Fielding (data engineer, joined previous week)  
**Drive source:** 14OsaRaUzJknlqrbri_VIiJuS60JknYABDqRZJpb7fo8

## Context

First cross-team planning session for Reflex with the analytics/data team. Jiro Farah confirmed as engineering lead. Goal: align on data architecture, AI tooling decisions, and Q2 deliverables.

## Key Points

**Scope and outputs**
- Two Q2 outputs: (1) formal monthly/quarterly report, (2) self-service query interface (similar to the "Whale" hackathon project).
- Cost data is central: attaching operational cost-per-ticket to insights is the mechanism to force product team prioritisation. Both direct CKO cost and merchant cost should be surfaced.
- Every aggregated insight must be traceable back to specific ticket/conversation IDs — loss of traceability during LLM aggregation was flagged as a key risk.

**Architecture decisions**
- Do NOT build a separate DBT model. Reflex must consolidate onto the existing merchant care data products in BigQuery/DBT — not fork a parallel model.
- Batch processing only (not live/streaming).
- Backfill 3 months minimum (back to Jan 2026).
- LLM platform decision pending: Bedrock vs Vertex. Claude flagged as a candidate (already in use for the support consultant).
- Prompting logic owned by Charlie/Imran/Vi. Summary format: merchant query + conversation thread + agent resolution.

**Future data sources**
- Slack support conversations: a large volume of support-equivalent queries currently bypasses Zendesk/Fin entirely via Slack — contact metrics undercount total support burden.
- Biannual NPS data from Airtable (needs client ID added to enable joining).

**Taxonomy dependency**
- The new product catalogue must be 100% mapped to ticket fields before reliable reporting is possible. Product field values are agent-set; QA layer may be needed.

## Insights

- Reflex is explicitly framed as the mechanism to make care costs visible and non-negotiable for product teams. Cost-per-ticket × volume is the forcing function.
- The Slack finding is significant: equivalent support queries bypass the official support funnel entirely. True support burden is higher than Zendesk data shows.
- NPS joining would connect support contact data to merchant sentiment — a potential leading indicator for the CSAT guardrail metric.
- Model drift QA at scale is an unsolved problem — important for long-term Reflex reliability.
- The "no separate DBT model" decision is a significant data governance call and should be maintained as the canonical position.
