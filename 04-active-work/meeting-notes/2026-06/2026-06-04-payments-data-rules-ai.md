# Payments Data Rules for AI

**Date:** 2026-06-04  
**Attendees:** Charlie Wildish, Patrick O'Connor (Solution Engineer / TAM)  
**Drive source:** 1nFCLb-cGKCbbZVzRFudeS1GK6nlybV_9H_uIpdaVsgQ

## Context

Strategic alignment between Care PM and a senior SE/TAM on the payments data semantic layer and competitive AI positioning.

## Key Points

**The three-layer context model (Patrick's framing)**
1. CKO API docs and schema knowledge.
2. Merchant's own codebase.
3. Merchant-specific configuration (MCC, processing profile, reporting config, fund transfer types, etc.).

Layer 3 is missing and blocks accurate AI troubleshooting. This context lives in CAT (internal merchant config interface) but is read-only and its field values are not semantically enriched — what each config value means is held in the heads of the Merchant Config team, not documented anywhere.

**Payments data schema**
- Charlie shared a conceptual payments data schema (spreadsheet, field names → definitions and value meanings for AI interpretation). Patrick reviewed pre-meeting.
- Patrick flagged: field names don't always match API payload syntax; sub-domains (AVS, card check, disputes, ECI, response codes) should be chunked out for efficient AI querying rather than parsing the whole sheet.
- Charlie confirmed: Markdown or JSON format, topic-level segmentation, sub-agents per domain to reduce token-heavy queries.

**Docs-from-code**
- Core infrastructure problem: documentation, BigQuery, DataHub, and schemas have inconsistent field names and are not connected. Documentation updates are manually requested from the docs team after backend changes — frequent desync.
- Agreed principle: documentation should be maintained at the schema source; code deployments should auto-update docs via PR.
- API reference GitHub repo (OpenAPI YAML/JSON) is machine-readable and covers authentication requirements and field validation — potential AI tooling foundation.

**Competitive context**
- Stripe led with MCP (1–2 years ahead). Adyen is quiet on AI, which is suppressing their valuation. Checkout is performing well on AI narrative.
- Patrick's competitive book is Adyen and Nuve, not Stripe. AI-driven faster time-to-live answers is a real differentiator vs. Adyen.

**Glean**
- Decision expected this month. Charlie noted the prerequisite is a company-wide knowledge quality programme with accountability (referencing Klarna's approach of tracking document cleanup as a measured company obligation).

**MCP v2 pilots**
- Patrick running behind-authentication MCP v2 pilots with eToro and NewDay.
- Charlie shared three new unpublished dashboard/payment help guides for Patrick to review and sense-check with eToro.

## Insights

- Layer 3 (merchant configuration context) is the hardest and most valuable data gap. CAT data exists but values are semantically opaque. Jamie Sims is flagged as the domain owner for merchant config/entity data.
- Response code mitigation guides from the payment performance team are the best existing source of response code definitions — but contain upsell recommendations (to Intelligent Acceptance) that are inappropriate to surface via a care agent. Filtering or forking needed.
- The "docs-from-code" principle was independently validated in this session and the Jun 3 Preethy session — a strong cross-team signal for engineering sponsorship.
- Checkout is well-positioned on AI narrative relative to Adyen — reinforces the case for the care AI roadmap as a competitive differentiator, not just a cost play.
