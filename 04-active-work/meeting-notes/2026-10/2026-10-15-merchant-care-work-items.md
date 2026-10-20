# Merchant Care - work items

**Date:** 2026-10-15  
**Attendees:** Pao Igarteburu, Fraser Bryant (EM), Charlie Wildish, Lachie Fielding, Harlie Patel  
**Drive source:** 1LwszkSiobQm1i-7IBcJ6eSifYrGTfxzLux5YBAID4Ms

## Context

Team sync on staffing, the product summit, the engineering roadmap and ops data. Gemini notes only, no transcript.

## Key Points

**Staffing**
- Will joins next week as a product data scientist in a pooled-project model, supporting Merchant Care and other pillars. Charlie prepares a starter task list.
- A Zendesk admin (AJ) is leaving (relocating to Spain). Fraser is working with a recruiter on a replacement and wants an open-minded hire without deep Zendesk UI habits.

**Product summit**
- Charlie has a slot to showcase features Anish built: an export feature and extra Looker data points.
- Export options: basic CSV button, Looker link, or direct Looker API download. The link or API route is simple (URL params).
- Reflex needs adoption traction and enforcement before more resource goes in. The summit is the exposure platform.
- Decision: broadcast the data product at the summit and make its usage mandatory.

**Engineering roadmap (Fraser, next 6 months)**
- Q4: build the Ray consumer experience in Plain (taxonomy, triggers, SLAs, queues), pending ops confirmation.
- Ray consumer requests route directly into Plain, not Zendesk. Human escalations handled in Plain by end of Q4.
- Merchant migration to Plain is slated for 2027 (H1 per the quick notes). Verify against `2026 deliverables.md` before reusing.
- Fiverr support in Plain arrives in January. Then data moves to BigQuery and Plain data goes into models in Q1. No Plain data intake this year.
- Ray friends-and-family release around December, subject to app readiness and back-office regulatory processes.

**Certified data product**
- Single source of truth for cross-Checkout merchant care. Covers Fin and Zendesk now, potentially Plain in H1 2027.

**Finance and ops data**
- Support P&L is misallocated to Platforms and must be re-apportioned with finance.
- Charlie is developing a vision and program for cross-ops platforms and wants case volumes, work types, FTE and back-office counts (via Dylan, Tim's team). Cost and headcount data needs People Analytics.
- Ops runs manual Google Sheets for merchant care cost-to-serve and scorecards. Lachie and Tim are migrating these into dbt this half.

## Insights

- Ray goes direct to Plain, so Plain data is absent from Q4 models.
- The Zendesk admin vacancy is a risk for the Zendesk to Plain transition.
- P&L misallocation distorts cost-per-contact reporting.
- Sheets-to-dbt migration is the basis for the scalability and cost analysis.
