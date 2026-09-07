# Reflex: Consolidating Customer Insight Tooling

**Date:** 2026-08-20
**Attendees:** Charles Forson, Charlie Wildish, Pao Igarteburu, Hugo Ducruc, Philippe Leonhardt, Andy Cornforth, Nicolas Maalouf
**Drive source:** 1DtJRHk7eN63gfiae5--MGYzOlOZ07GTnVpCmSVeYsEk

## Context

Three overlapping insight tools in one room: Charles Forson's conversational-intelligence prototype, Philippe and Andy's commercial intake app, and Reflex.

## Key Points

- Charles Forson's "listen" prototype: vibe-coded, local, processes call transcripts and attributes product feedback to merchants and prospects. His own assessment: "what I've got on my local machine is not any good."
- Philippe and Andy's commercial intake app: takes qualitative merchant requests and attaches commercial value, potential processing volume and revenue opportunity. V1 rolling out to commercial and product users now.
- Reflex: support ticket data summarised and clustered into topics via LLM, with cost and volume attached. Pao: "for us this is not a proof of concept anymore, this is a real product working." Ingestion and clustering are solved and rollout to PMs is under way.
- Reflex origin: last year's hackathon, goal was improving product roadmaps with real customer feedback. Never care-only. Intended sources include WhatsApp complaints and AM emails alongside Care tickets.
- Reflex demo detail: topic-level view rather than ticket-level, spanning multiple merchants and problem types, with volume count and blended cost per contact (blended across AI and human resolution, sourced live from the ops cost model). Filters by product pillar, product team, individual product and tier, with merchant filter being added, and drill-down to actual merchant queries. Ticket summaries are queryable in Looker and reachable via the Looker MCP because they sit in the semantic layer.
- Example cited: Remitly spiked payout volume and a volume-proportional share landed in pending due to sanctions screening. "Card payout stuck in pending" is the top issue, framed as the model case for a PM owning the fix.
- Charlie's merge model: Reflex insights carry a type. Support is one type, feature requests and TPV unlocks are another. Commercial contributes TPV upside, Care contributes cost reduction. "If you can reduce cost and increase TPV with doing something, then it's an easy one."
- Integration blocker is schema, not intent. It requires a data contract with clean joins on merchant identifier plus the Airtable product catalogue entry. Andy confirmed the commercial intake app is already fully mapped to the Airtable product catalogue, which makes the join simple. Philippe cannot commit engineering capacity to change his schema during V1 rollout.
- Charles wants to broaden beyond PMs to product marketing, partnerships and account plans, since merchants also talk about competitors, partners, schemes and Checkout's service levels. His AI CoE big bet with Emma Nox captures meeting notes, Slack and email from BDR outreach through to AM.
- Charlie pushed back on user-based segmentation: the difference is not the user, it is the aggregation level. Commercial views are merchant-focused, PM views are aggregate.

## Decisions

- Consolidate into a single roadmap-prioritisation view. Andy wants the product-priority output merged but the commercial account and target layer kept separate.
- Direction of integration settled: commercial feeds into Reflex. Reflex publishes its minimum requirements for adding a new data source and the commercial side reacts, rather than Reflex absorbing Philippe's schema. Anish or Loi to help define the ingested schema.
- Pao shares minimum data-source requirements; Philippe documents the commercial intake schema; Charles summarises listen's capability and vision; Charlie creates a shared Slack channel.

## Insights

- Reflex is now the de facto company-wide customer-insight ingestion layer and Charlie's team owns it. Pao's caveat: capacity was scoped for deployment and maintenance, not for scaling to new sources. Each new source is a reason to reinvest in clustering methodology and evals, and that has to be funded.
- Pao's advocacy point: enterprise-grade means real engineering, not vibe-coded prototypes. Reflex has engineers, AWS architecture and hosted models behind it.
- The Airtable product catalogue plus merchant ID is emerging as the company-wide join key for insight tooling.
