# MCP x Agents alignment

**Date:** 2026-10-15  
**Attendees:** Ana Escobar (organiser, MCP), Charlie Wildish, Joseph El Choueiri (Dashboard product), Hamish Chreseson (owns PLC, Payment Lifecycle data)  
**Drive source:** 1YRbiN6qIA25rGVL4iFNGr3zNYCMHiIy1wDBGSU4X3tY

## Context

Align the Checkout MCP with the Care and dashboard agents on a single data source, so every merchant-facing AI gives the same answer. Follows the dashboard agent document where Charlie flagged PLC as an equal data source for anything merchant-facing.

## Key Points

**MCP vs agents**
- The MCP is "glue to all our APIs for an LLM": phase zero, few tools, no playbooks or guardrails. It points at public APIs (get payments, get actions).
- Care and dashboard agents add context, guardrails and next-step guidance.

**PLC**
- Consolidates gateway events (request, auth, capture), authentication events, fraud outcomes and disputes into one record per payment. Main use is analytics, not API-log replacement.
- Adds semantic definitions (raw codes become readable flags). Downstream of the public endpoints, so field names can differ from MCP data.
- Care has BigQuery tables (pay-in, card payout, bank payout) with natural-language schema docs per field, and a service that resolves any identifier to a payment ID.

**Retention**
- Raw API payloads: about 2 weeks in gateway logs, about 1 month in Datadog. Charlie believes payloads are not persisted in BigQuery.
- PLC holds months to years but only some payload fields. The dashboard decoder needs PLC because merchants ask about older payments.

**Gaps**
- PLC lacks routing, third-party acquirer and scheme authorization messages. These exist only in gateway logs, with no proper data product.
- Care agents lack Datadog session and API log access. A full-trace MCP capability would help Care.
- Internal tools shown: the gateway AI tool (payment ID in, codes, flow, routing, scheme messages, recommendations out) and Traffic Insight (Retool, gateway/fraud/auth logs). Used by TAMs, solutions engineers and the gateway team. Merchant Care does not use them. Charlie would not be comfortable making the gateway tool customer facing.

**Decoder**
- Joseph writes a payments-page decoder proposal today: PLC as source of truth plus webhook info and global failure context, giving a one-liner and detail on demand. Modelled on the gateway tool, merchant-first.

**Tribal knowledge**
- Checkout docs lack LLM context. Solutions engineers tell merchants "go ahead" and it fails in production because key knowledge sits in people's heads.
- Joseph's analytics assistant instructions (vetted with performance and data engineering) need ongoing maintenance and are not shared. Ana is mapping all AI efforts across the business.

## Insights

- Conflicting answers across MCP, dashboard decoder, Fin and Care agents is the risk. A shared PLC-based source is the mitigation.
- No persisted payloads and no routing or scheme data is a pipeline gap for Care as well.
- The decoder consumes PLC, so it overlaps Care's data work.
- Using the Care source for the MCP has cost and usage implications.
- No formal decisions. Agreement that MCP and agents call the same underlying source.
