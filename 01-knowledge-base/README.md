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
- `merchant-segments.md` - All merchant segments and their support model
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
- `ai-agent-operations.md` - Fin AI Agent operations and improvement process
- `incident-response.md` - How to handle service incidents
- `known-challenges.md` - Known operational challenges and workarounds
- `US Platforms - support needs - 2025_07_17.md` - Transcript: US sales team interview on Platform segment support challenges (onboarding, terminations, payout visibility, payment lifecycle)

### 💳 `payment-domain/`
Payment industry knowledge and PSP concepts
- `psp-fundamentals.md` - Core payment processing concepts
- `common-issues.md` - Typical payment problems and solutions

### 📊 `metrics/`
KPIs and measurement frameworks
- `kpi-definitions.md` - All metrics organised by Care Flywheel domain

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
