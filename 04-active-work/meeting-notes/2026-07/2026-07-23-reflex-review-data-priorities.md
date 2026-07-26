# Reflex review

**Date:** 2026-07-23  
**Attendees:** Charlie Wildish (PM); Imran Khan (leaving in ~2 weeks)  
**Drive source:** 1cTTQqVqwcj08DcoBein02KxczH0fXCpWt9EuWEzZGEM

## Context

Review of the Reflex dashboard against ~30 pieces of feedback plus George's UX review, to set priorities before releasing the feature backlog. Also covered two marketing comms campaigns to lift dashboard-user coverage.

## Key Points

**Marketing comms for missing support users**
- Two campaigns for dashboard users missing from support: (1) full list of all missing users with merchants/client IDs; (2) list organised by client admin, excluding non-domain-matching emails (e.g. gmail.com), capped at ~5 missing users per admin per email. Marketing uploads and sends.
- Goal: lift the current 65% dashboard-user coverage, raise Fin involvement rate, and lift email resolution rate by enabling data sharing. Admin outreach is the only lever because accounts can't be self-created.

**Data fixes (top priority)**
- Product name filter is wrongly mapped to the escalation field. It should map to product team then product pillar (from the catalogue extract). Product team should be the primary filter (e.g. "I'm payment processing, where's my data?"). Team/pillar assumed roughly 1:1.
- Catalogue sync: recent major catalogue review cut many low-volume issuing items; core payment methods largely unchanged. Zendesk triggers set product category/name fields and must stay in sync. Imran to check label coverage and whether older tickets can be back-enriched (April onward).
- Backend topic mismatch: dashboard topics don't match Imran's local topics. Catch-all topics ("transaction failures", "transaction status inquiries") are each capturing ~700 tickets. Needs backend investigation.

**Charts and reporting model**
- Current charts show only absolute lines: no relative change over time, % of total, or growth. Need to tie data to contact rate and cost at product level.
- Cost attribution is feasible (ticket-level data exists). Contact rate is harder: needs to know which products each merchant is configured for (product catalogue dependency).
- Topic becomes the primary driver in reports/graphs once trusted; stop showing taxonomy/issue-type labels to avoid confusion. Product team and pillar are the primary drill-down filters. Issue type is shown now only because topic didn't exist earlier.

**UX and feature requests**
- Ticket-detail expansion renders as a raw plain-text block; truncated labels don't render dynamically; no feedback mechanism.
- Requested: simple feedback modal writing to a Google Sheet; export feature (both confirmed).

## Insights

- Priority order: fix data (product name fields, redo IDs, add Fin to the dataset) → topic-driven main charts → topic breakdown only → primary filter = product team → cost attribution (later) → George's UX feedback. "Otherwise everything else is just a symptom." Data fixes run as a separate parallel workstream (Imran owns data).
- In-house build justification (quotable): Fin generated its own ~200-level topic taxonomy that was mostly duplicative, acts as a black box, and lacks nuance and control, creating third-party dependency and data lock-in. Third-party tools fit simple e-commerce/retail (Fin can automate ~80% of simple volume with a couple of commands); Checkout's product and architecture complexity requires in-house to keep the taxonomy nuanced and sustainable. Complexity drives the in-house build.
- Reflex external validation: demoed at a Product Tank event; 5 people sought Charlie out. Framing that resonated: "support is a hidden data source" and merging disparate datasets (NPS, support) into an insights layer. Interested parties spanned publishing, project management, and micro-mobility (French company "DOT"), reinforcing Reflex as an industry-agnostic concept.
- Knowledge brainstorm session postponed one week to prioritise tactical dashboard work; Imran writing a strategy doc for it.
