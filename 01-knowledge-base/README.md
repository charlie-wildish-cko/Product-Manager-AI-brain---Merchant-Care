# Knowledge Base

This directory contains domain knowledge, process documentation, and reference material for customer support PM work at Checkout.com.

## Directory Structure

### 🎯 `strategy/`
High-level strategic frameworks and source documents
- `care-product-model.md` - The Care Product flywheel (6-domain capability model)
- `support-scale-principles.md` - Principles for scaling support to 2030
- `competitive-support-audit-2026.md` - Competitor benchmark: Stripe, Adyen, Worldpay, Razorpay, Braintree
- `care-success-plans-proposal.md` - Source proposal for the three-tier B2B support model

### 📦 `products/`
Product reference documentation
- `customer-segments.md` - All customer segments and their support model
- `care-success-plans.md` - Tier model (Standard / Enterprise / Premium) + Stripe benchmark
- `platform-segment.md` - Platform / ISV deep-dive (primary 2026 focus)
- `reflex.md` - Reflex: AI-powered support contact insights product
- `checkout-products.md` - Checkout.com product overview

### 🏢 Root-level reference files
Checkout.com business context and data references (in `01-knowledge-base/` root, not a subdirectory)
- `checkout-business-context.md` - Company overview, product pillars, payment methods, strategy, P&L context
- `data-sources.md` - All data sources: BigQuery, Confluence, GitHub, Airtable, Drive, docs sites
- `teams.md` - Internal team names and stakeholder groups (canonical reference for PRDs and docs)

### 🔄 `processes/`
Internal support processes and workflows
- `support-workflows.md` - Standard ticket handling procedures
- `agent-toolkit-zendesk.md` - Agent toolkit in Zendesk (user profile, payment tool, Dispatch search)
- `ai-agent-operations.md` - Fin AI Agent operations and improvement process
- `incident-response.md` - How to handle service incidents
- `known-challenges.md` - Known operational challenges and workarounds
- `review-panel-personas.md` - Six reviewer personas (PM, Eng, Ops, CPO, COO, Data Scientist) for document review and stakeholder comms; used by the Document Review Panel workflow
- `US Platforms - support needs - 2025_07_17.md` - Transcript: US sales team interview on Platform segment support challenges (onboarding, terminations, payout visibility, payment lifecycle)

### 💳 `payment-domain/`
Payment industry knowledge and PSP concepts
- `psp-fundamentals.md` - Core payment processing concepts
- `common-issues.md` - Typical payment problems and solutions

### 📊 `metrics/`
KPIs and measurement frameworks
- `kpi-definitions.md` - All metrics organised by Care Flywheel domain
- `support_contacts_flat_table_2025_metric_definitions.md` - Count and derived metric definitions for support contacts flat table (full-year and last-6m)
- `Q4_2025_metrics_handover.md` - Q4 2025 Fin metrics: formulas and how to compute (Total support contacts, Fin involved, Fin involvement/resolution rates)
- `q4_2025_metrics.py` - Script to compute Q4 2025 Fin metrics from the flat table CSV
- `support_contacts_flat_table_2025.csv`, `support_contacts_flat_table_2025_last_6m.csv`, `support_contacts_flat_table_2025_q4.csv` - Canonical data for volume and involvement metrics

### 🗄️ `bigquery-queries/`
Saved SQL query library for Zendesk ticket analysis

## How to Use This Knowledge Base

### For Daily Work
- Reference when answering stakeholder questions
- Link to relevant docs in tickets and updates
- Use as foundation for training new team members

### For AI Assistance
- Files in this directory provide context to Claude
- Ask questions like "What's our process for handling SEV 1 incidents?"
- Claude can reference these docs to provide consistent, accurate answers

### Maintenance
- Update documents as processes change
- Add new issues to `common-issues.md` as patterns emerge
- Keep metrics definitions aligned with actual tracking
- Mark last updated date and owner on each document

## Quick Reference

**Need to understand a payment term?** → `payment-domain/psp-fundamentals.md`

**How do we handle support tickets?** → `processes/support-workflows.md`

**What metrics should I track?** → `metrics/kpi-definitions.md`

**Service is down - what do I do?** → `processes/incident-response.md`

**What products do we offer?** → `products/checkout-products.md`

**What's the correct name for a team?** → `teams.md`
