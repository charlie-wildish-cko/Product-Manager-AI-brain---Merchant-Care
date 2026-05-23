# CLAUDE.md — Charlie PM Brain

Charlie Wildish is PM for Merchant Care (Customer Support) at Checkout.com, a global PSP.

---

## Starting a New Task

When given a new task or topic without a clear output format:

1. **Orient** — Check `04-active-work/` (including `04-active-work/roadmap-items/` for active PRDs) for existing work on the topic. If a file exists, read it before starting.
2. **Anchor** — Check `2026 deliverables.md` to confirm the task maps to a named deliverable and quarter. If it doesn't, flag this before proceeding.
3. **Clarify the output format** — PRD · memo · Slack update · stakeholder update · analysis · exploration
4. **Draft** — Apply the relevant template and writing style. Ask one clarifying question at most before producing output.

---

## The One Principle

> **All work must tie back to strategy. Never produce work that floats.**

Every document, analysis, or recommendation must connect to:
- A **strategic goal**: reduce contact rate · reduce cost of support
- A **north star metric**: Contact rate (contacts per 1M transactions) · Cost per contact
- A **guardrail metric**: Merchant CSAT (must not decline as we automate)
- A **2026 deliverable**: a named initiative scoped to a specific quarter, listed in `2026 deliverables.md`
- A **flywheel domain**: Input → Orchestration → Fuel → Agent Experience → Insight & Prevention → Governance

---

## Project Structure

```
01-knowledge-base/   # Reference docs — strategy, products, processes, payment domain, metrics
02-workflows/        # Step-by-step process guides
03-templates/        # Reusable document templates (PRD, memo, user story, etc.)
04-active-work/      # Current sprint work, active PRDs, stakeholder updates
05-archive/          # Completed work by year/quarter
```

---

## Key Reference Files

| Purpose | File |
|---|---|
| Strategic goals & 2026 roadmap | `2026 deliverables.md` |
| Care Product flywheel model | `01-knowledge-base/strategy/care-product-model.md` |
| Care Product strategy 2026–2030 (Rumelt strategy kernel, VP/Director audience) | `04-active-work/care-product-strategy-2026-2030.md` |
| Care strategy 2026–2030 (narrative + TPV/contact forecasts, co-authored with Oliver Westlake-Simm) | `04-active-work/care-strategy-2026-2030.md` |
| Team structure & stakeholders | `01-knowledge-base/teams.md` |
| Support workflows & operations | `01-knowledge-base/processes/support-workflows.md` |
| Ticket taxonomy & contact volumes | `01-knowledge-base/processes/support-taxonomy.md` |
| Care Agent SOPs & KB (526 articles, 125 folders from Zendesk KB) | `01-knowledge-base/processes/Care Agent SOPs/INDEX.md` |
| Merchant segments | `01-knowledge-base/products/customer-segments.md` |
| Product catalogue (products, teams, pillars) | `01-knowledge-base/Checkout Products and teams.csv` |
| Product definitions with contact risk tags | `01-knowledge-base/products/product-definitions.md` |
| Payment domain terminology (200 terms: acquirer, authorization, chargeback, settlement, SCA, APM, etc.) | `01-knowledge-base/payment-domain/checkout-terminology.md` |
| Platform segment model | `01-knowledge-base/products/platform-segment.md` |
| Platform Embedded AI vision | `01-knowledge-base/products/platform-embedded-ai-support-vision.md` |
| Customer personas (merchant + internal) | `01-knowledge-base/products/customer-personas.md` |
| KPI definitions | `01-knowledge-base/metrics/kpi-definitions.md` |
| Contact volume forecasts 2026–2030 by segment (Enterprise, Platforms ISV, Platforms SMB, Consumer) | `01-knowledge-base/metrics/contact forecasting.md` |
| Reflex product reference (components, metrics, vision, why it matters) | `01-knowledge-base/products/reflex.md` |
| Reflex phased plan (components + build sequence, Q1–Q4 2026) | `04-active-work/reflex-phased-plan.md` |
| Agent Consultant capabilities (full list) and interaction model | `01-knowledge-base/products/agent-consultant.md` · vision: `04-active-work/agent-consultant-vision.md` |
| Fin AI Agent — how it works, Checkout.com deployment, Procedures/Tasks, analytics, terminology | `01-knowledge-base/products/fin-ai-agent.md` |
| Zendesk — ticket lifecycle, business rules, routing, Guide/Knowledge, AI tooling, analytics, terminology | `01-knowledge-base/products/zendesk.md` |
| Product reference doc template (why it matters + components + metrics) | `03-templates/product-reference-template.md` |
| PRD template | `03-templates/prd-template.md` |
| PRD example | `03-templates/prd-template-example.md` |
| Product strategy template | `03-templates/product-strategy-template.md` |
| Writing style by audience | `01-knowledge-base/processes/writing-style-guide.md` |
| Zendesk platform decision RFC (Build/Buy/Keep, Q3–Q4 2026) | `04-active-work/zendesk-platform-decision-rfc.md` |
| Zendesk viability research (AI, pricing, market, 2024–2026) | `04-active-work/Zendesk Viability_ AI, Pricing, Market.md` |
| Support articles (879 markdown files, 14 topic folders — Payments, Disputes, Settlements, Platforms, etc.) | `01-knowledge-base/Support content/checkout-support-site-main/Support articles/` |
| Technical documentation articles (~700 files) | `01-knowledge-base/Support content/Tech Docs/` |
| API reference (Swagger YAML + paths, components, code samples) | `01-knowledge-base/Support content/API reference/` |

---

## Writing Style

### Default (formal documents, PRDs, briefs)
- Lead with the point — conclusion first, evidence after
- Structured with headers and bullets
- Short paragraphs (2–3 sentences), active voice, specific numbers
- Always end with a clear next step or recommendation

### Always avoid
- Em dashes (`—`) as clause connectors
- Hedging language ("may", "could potentially", "somewhat")
- Burying the conclusion or leading with context instead of the point
- Semicolons to connect clauses
- Flattery or affirmations ("Great question!", "Certainly!", "Absolutely!")
- Padding or filler sentences
- Rewriting entire files when only a small change is needed
- Unsolicited summaries of what was just done

For Leadership, Engineering, Slack, and Reports style: see `01-knowledge-base/processes/writing-style-guide.md`.

---

## Data Rules

**Interview transcripts**: WEBVTT format. Stored in `04-active-work/merchant-interview-transcripts-2025/`. Two subfolders: `Direct merchants/` (Participant 2 is the merchant) and `Platforms/` (Alcinda Lee is the interviewer; other speakers are Platform ops users). Files are large — use Explore agents with chunked reads.

**Large files in 04-active-work/:** Files exported from Google Docs or containing embedded images may exceed the Read tool limit despite having few lines. Use `strings <file> | grep -v "^data:"` to extract readable text content.

**Always use real data; never use placeholder numbers:**
- Source: `01-knowledge-base/metrics/support_contacts_flat_table_2025_last_6m.csv`
- Column definitions: `01-knowledge-base/metrics/support_contacts_flat_table_2025_metric_definitions.md`
- Case-type breakdown: `01-knowledge-base/processes/support-taxonomy.md`

**Note:** Volume totals in `support-taxonomy.md` and the flat CSV will differ — the taxonomy doc draws on a broader dataset. Use the CSV for relative prioritisation and actuals; use the taxonomy doc for issue type structure.

**To aggregate volumes from the CSV:** Use a Python script to sum `support_contacts` grouped by `case_type` and `issue_type` — rows are split by segment/channel/territory so individual rows are not totals. Run `pip3 install pandas` first if pandas is not available.

**Payment domain terms**: When defining or using payment/fintech terms (e.g. authorization, capture, settlement, chargeback, APM, SCA, MID, acquirer, issuer), use `01-knowledge-base/payment-domain/checkout-terminology.md` as the authoritative source. Do not paraphrase or re-define terms that already exist there.

---

## PRD Framework

Anchor in strategy first:

1. Which **strategic goal** does this serve? (reduce contact rate / reduce cost)
2. Which **2026 deliverable** does it map to?
3. Which **flywheel domain** does it sit in?
4. Which **metrics** will it move?
5. Which **strategic lever** does it pull? (contact reduction, AI deflection, agent efficiency, self-service)

Then use `03-templates/prd-template.md`. Quality rules are enforced in the template. For PRD sharpening, use Socratic questions from `01-knowledge-base/processes/socratic-questioning-prds.md`.

**PRD scope sections must map to named deliverable line items verbatim** — copy the exact bullet text from `2026 deliverables.md` into In Scope. Do not paraphrase or regroup them.

**PRD format (updated 2026-04-09)**: Executive Summary = 3 sentences max (problem + data point / solution / deliverable + goal). Rollout Plan = single table (one column per phase), not prose phase blocks. See `03-templates/prd-template.md`.

For product strategy documents (1–3 year horizon, VP/Director audience): use `03-templates/product-strategy-template.md`. Framework: Rumelt's Strategy Kernel (Diagnosis → Guiding Policy → Coherent Actions) — reference doc at `01-knowledge-base/strategy/rumelt-strategy-kernel.md`.

---

## Workflows & Skills

### Document Review Panel
Apply to any PRD, memo, or spec before finalising.
- Workflow: `02-workflows/document-review-panel.md`
- Personas: `01-knowledge-base/processes/review-panel-personas.md`
- Always run 5 core personas (Oliver, Casey, Imran, Preethy, Taylor). Add conditional personas based on PRD type — see personas file for rules.

### Draft → Critique → Refine
Run for any significant document from scratch: Draft → Critique (panel) → Refine → Condense (PRDs: ~250–350 lines).
- Workflow: `02-workflows/draft-critique-refine.md`

### PRD Re-Review
Run against any existing PRD when the template has been updated or scope has changed significantly.
- Skill: `/prd-review [file path]` — audits PRD against current `03-templates/prd-template.md`, produces gap report, offers to apply fixes

### Classifier Definitions
Generate AI-readable classification definitions (TSV, paste-ready for Google Sheets) from taxonomy or product catalogue.
- Skill: `/classify-definitions [taxonomy|products|both] [optional filter]`
- Output: one row per class, columns include include_when, exclude_when, disambiguation, keywords, phrases, entities, examples
- Saved to: `04-active-work/classifier-definitions-<scope>-<date>.tsv`

### Model Routing in Skills
Skills use Opus for strategic/analytical phases and Sonnet for writing/output phases.
- Spawn `Agent(model: "opus")` for: roadmap anchoring, review panel critique, disambiguation analysis
- Current model (Sonnet) handles: drafting, editing, file output
- Add `Agent` to the `tools:` line in any skill that uses this pattern

### Publish to Confluence
Add YAML front matter to any markdown file:
```yaml
---
confluence_space_key: MTC
confluence_page_id: <id if updating>
confluence_parent_page_id: 8041431176  # PRDs folder
title: Page Title
---
```
Then say "publish to Confluence". Default space: `MTC` (Merchant Care Product).

**Important:** When publishing, strip the leading `# H1 title` from the body. Confluence automatically renders the page title as an H1 — including it in the body creates a duplicate title.

---

## Stakeholders

| Role | Relationship |
|---|---|
| VP of Product | Charlie's manager; approves roadmap |
| Director of Operations | Decision-maker; owns support delivery |
| Director of Operations Excellence | Decision-maker; owns quality & process |
| Engineering Manager | Engineering counterpart |
| Knowledge Manager | Collaborator; owns knowledge base |
| Process Architect | Collaborator; owns support processes |
| Content Strategist | Collaborator; owns agent-facing content |

**Decision model**: Consultative. Consensus across Director of Operations, Director of Operations Excellence, Charlie, and VP of Product.

---

## Support Channels

Channels: Email (Zendesk) · Dashboard webform (Zendesk) · AI deflection (Intercom Fin). Priority tiers: P0–P3 across Standard / Enterprise / Premium.

---

## Product Terminology and Key Facts

| Term | Use | Not |
|---|---|---|
| Customer 360 | Centralised customer context across all Checkout sources | Merchant 360 |
| Platform / ISV | Vertical SaaS businesses that embed Checkout payments as PayFacs for their Platform merchants | Sub-merchant (use "Platform merchant") |
| Fin involvement rate | % of contacts where Fin was applied as the first point of contact. Distinct from AI resolution rate (% resolved without escalation to a human). | — |
| Fin Procedures | Fin's equivalent of SOPs: define the steps Fin follows to resolve a specific contact type, including API calls, data retrieval, and response logic. Data integrations are accessed via Procedures, not ad hoc. Related deliverable: Improve Fin Resolution Through Procedures (Q2 2026) | — |

**Unit cost benchmarks**: Fin costs $0.90/resolution; human agent ~$40/contact (44x difference). Use these when framing AI investment cases.

**Team composition (2026 baseline)**: 1 PM (Charlie); 4 engineers + 1 EM (max span ~8 including ZD admins); 2 Zendesk admins; shared Product Data Scientist; part-time Data Engineer shared with wider teams. Fin administration is a shared responsibility across Product and Content with no dedicated owner.

**Fin deployment setup**: Fin Messenger is installed in the Checkout.com Dashboard (merchant-facing live chat); unresolved conversations escalate to Zendesk as tickets. Fin for Zendesk handles inbound email/tickets. Copilot (Intercom's agent AI assistant) is connected to Zendesk for Care agents — maps to the Agent Consultant product concept.

**Zendesk setup**: Checkout.com uses Zendesk Support + Zendesk Guide (help centre at support.checkout.com). Fin (Intercom) is the AI resolution layer via the Zendesk integration — Zendesk's native AI agents are not used. Zendesk Auto Assist (Copilot) is connected for agents.

**Agent Consultant modes**: Autonomous (data lookups, knowledge retrieval, approved API calls, QA on closed tickets) vs Human-in-the-loop (refunds, reversals, 3rd-party API actions). Full list: `01-knowledge-base/products/agent-consultant.md`.

**Reflex 2030 vision**: AI-generated action plan recommendations and fix PRs for engineering review, not autonomous deployment to production.

**Reflex MCP (TBC)**: Surfaces Reflex insights in engineering workflows. Timing is TBC — dependent on Phase 3 (Q3 2026) attribution model stability. Insights available via data product regardless; MCP improves shareability.

**B2C wallet launch (2027)**: Consumer Duty obligations apply from day one. Complaint handling and vulnerable customer identification in Fin must be live at launch, not added post-launch.

**Care product model 2030 mapping**: Full product mapping per flywheel stage and stack layer (existing, build, buy, agentic) is in `04-active-work/care-product-model-2030-mapping.md`.

**Operating model at scale**: Implications of 80%+ AI resolution by 2030 (agent roles, governance, knowledge infra, ownership, successor metrics) in `01-knowledge-base/strategy/operating-model-at-scale.md`.

**Platform segment (2026)**: Distinct B2B customer segment alongside Direct Merchants. Checkout is L2; Platform is L1 for its Platform merchants. US ISV launch in active delivery 2026. Platform Embedded AI (Fin in ISV portals) is a 2027 capability. Checkout-as-PayFac (2028+, unconfirmed) would make Checkout L1 for Platform merchants directly.
