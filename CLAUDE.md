# CLAUDE.md — Charlie PM Brain

Charlie Wildish is PM for Merchant Care (Customer Support) at Checkout.com, a global PSP.

---

## Starting a New Task

When given a new task or topic without a clear output format:

1. **Orient** — Check `04-active-work/` for existing work. PRDs live in `04-active-work/prds/<initiative>/`; long-horizon strategy in `04-active-work/strategy/`; research and supporting analysis in `04-active-work/research/`; CSVs and data artefacts in `04-active-work/working-files/`. If a file exists, read it before starting.
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
04-active-work/      # Active work — prds/, strategy/, research/, working-files/
05-archive/          # Completed work by year/quarter
```

**Keep `README.md` in sync with this structure** — when a top-level directory is added, removed, or its purpose changes, update `README.md`'s directory tree and key reference table in the same pass, not as separate cleanup later.

---

## Key Reference Files

| Purpose | File |
|---|---|
| Strategic goals & 2026 roadmap | `2026 deliverables.md` |
| Care Product flywheel model | `01-knowledge-base/strategy/care-product-model.md` |
| Care Product strategy 2026–2030 (Rumelt strategy kernel, VP/Director audience) | `04-active-work/strategy/care-product-strategy-2026-2030.md` |
| Care strategy 2026–2030 (narrative + TPV/contact forecasts, co-authored with Oliver Westlake-Simm) | `04-active-work/strategy/care-strategy-2026-2030.md` |
| Team structure & stakeholders | `01-knowledge-base/teams.md` |
| Support workflows & operations | `01-knowledge-base/processes/support-workflows.md` |
| Ticket taxonomy & contact volumes | `01-knowledge-base/processes/support-taxonomy.md` |
| Fin Attribute value definitions (Intercom-ready format) | `01-knowledge-base/processes/fin-attributes-definitions.md` |
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
| Reflex phased plan (components + build sequence, Q1–Q4 2026) | `04-active-work/prds/reflex/phased-plan.md` |
| Agent Consultant capabilities (full list) and interaction model | `01-knowledge-base/products/agent-consultant.md` · vision: `04-active-work/prds/agent-consultant/vision.md` |
| Fin AI Agent — how it works, Checkout.com deployment, Procedures/Tasks, analytics, terminology | `01-knowledge-base/products/fin-ai-agent.md` |
| Zendesk — ticket lifecycle, business rules, routing, Guide/Knowledge, AI tooling, analytics, terminology | `01-knowledge-base/products/zendesk.md` |
| Product reference doc template (why it matters + components + metrics) | `03-templates/product-reference-template.md` |
| PRD template | `03-templates/prd-template.md` |
| PRD example | `03-templates/prd-template-example.md` |
| Product strategy template | `03-templates/product-strategy-template.md` |
| Writing style by audience | `01-knowledge-base/processes/writing-style-guide.md` |
| Zendesk platform decision RFC (Build/Buy/Keep, Q3–Q4 2026) | `04-active-work/research/zendesk-platform-decision-rfc.md` |
| Zendesk viability research (AI, pricing, market, 2024–2026) | `05-archive/2026/investigations/Zendesk Viability_ AI, Pricing, Market.md` |
| Support articles (879 markdown files, 14 topic folders — Payments, Disputes, Settlements, Platforms, etc.) | `01-knowledge-base/Support content/checkout-support-site-main/Support articles/` |
| Technical documentation articles (~700 files) | `01-knowledge-base/Support content/Tech Docs/` |
| API reference — full OpenAPI 3.0.1 spec (JSON, 3.4MB; all endpoints, schemas, tags) | `01-knowledge-base/Support content/API reference/api-reference.json` |

---

## Writing Style

### Default (formal documents, PRDs, briefs)
- Lead with the point — conclusion first, evidence after
- Structured with headers and bullets
- Short paragraphs (2–3 sentences), active voice, specific numbers
- Always end with a clear next step or recommendation

### Always avoid
- Em dashes (`—`) as clause connectors (use a colon or full stop). Max 2-3 per document.
- Hedging language: "may", "could potentially", "somewhat", "we believe", "we could", "may not necessarily", "suggest a [timeframe]". State claims directly. For an estimate, write "estimate: X%", not "we estimate it could be around X%".
- Burying the conclusion or leading with context instead of the point
- Semicolons to connect clauses
- Flattery or affirmations ("Great question!", "Certainly!", "Absolutely!")
- Padding or filler sentences
- Rewriting entire files when only a small change is needed
- Unsolicited summaries of what was just done
- Unicode decoration: curly/smart quotes, `->` arrows. Type straight quotes and plain ASCII.
- AI writing tropes (applies to all output, not just formal docs). Top offenders: magic adverbs ("quietly", "deeply", "fundamentally", "arguably"); "leverage"/"utilize"/"robust"/"streamline"/"harness"; grandiose nouns ("tapestry", "landscape", "ecosystem", "paradigm", "synergy"); "serves as"/"represents" instead of "is"; negative parallelism ("it's not X, it's Y"); rhetorical Q&A ("The result? ..."); empty transitions ("it's worth noting", "notably", "importantly"); signposted conclusions ("in summary", "in conclusion"). Full list: `01-knowledge-base/processes/writing-style-guide.md` → "AI Writing Tropes to Avoid".

**Before writing any styled document, consult `01-knowledge-base/processes/writing-style-guide.md` and apply the matching audience profile:** Leadership / C-suite · Slack updates · Engineering · Reports & readouts · Strategy & analysis. That guide is the source of truth for audience-specific structure (exec-summary length, TLDR/Note/Ask callouts, hypothesis framing, action-item rules); the tropes and hedging bans above are always on regardless of audience.

---

## Data Rules

**Deliverable dates and quarters**: `2026 deliverables.md` is the single source of truth for what quarter a deliverable or sub-component is scoped to, including TBC/unscheduled items. When writing or editing any doc that states a quarter for a deliverable (e.g. "Q3 2026," "in delivery"), verify it against `2026 deliverables.md` first — do not carry forward a date from another doc without checking it there. If `2026 deliverables.md` marks something TBC, downstream docs must say TBC too, not assert a settled quarter. When editing any file that states deliverable timing, grep other active docs for the same deliverable name and fix mismatches in the same pass rather than leaving them to drift.

**Interview transcripts**: WEBVTT format. Stored in `04-active-work/merchant-interview-transcripts-2025/`. Two subfolders: `Direct merchants/` (Participant 2 is the merchant) and `Platforms/` (Alcinda Lee is the interviewer; other speakers are Platform ops users). Files are large — use Explore agents with chunked reads.

**Large files in 04-active-work/:** Files exported from Google Docs or containing embedded images may exceed the Read tool limit despite having few lines. Use `strings <file> | grep -v "^data:"` to extract readable text content.

**Always use real data; never use placeholder numbers:**
- Source (case type / issue type / reason volume, native V4 taxonomy, since 1 April 2026): `04-active-work/working-files/Contact breakdown since April 2026.md`
- Case-type breakdown: `01-knowledge-base/processes/support-taxonomy.md`
- Column definitions: `01-knowledge-base/metrics/support_contacts_flat_table_2025_metric_definitions.md`

**Archived (2026-07-02):** `support_contacts_flat_table_2025_last_6m.csv` is superseded by the file above for taxonomy mix and volume actuals — moved to `05-archive/2026/data-exports/support_contacts_flat_table_2025_last_6m.csv`. It has no live replacement yet for Fin involvement rate, segment (Premium/Enterprise/Standard), sales_territory, or billing_region — those dimensions aren't in the new file. Use the archived CSV only for those metrics until a refreshed source exists; do not use it for case-type/issue-type volume.

**Note:** Volume totals in `support-taxonomy.md` and the archived CSV will differ — the taxonomy doc draws on a broader dataset.

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

**Keep this section in sync with `.claude/skills/`** — when a skill is added or removed, update its entry here too, and update the skills table in `README.md` in the same pass.

### Document Review Panel
Apply to any PRD, memo, or spec before finalising.
- Workflow: `02-workflows/document-review-panel.md`
- Personas: `01-knowledge-base/processes/review-panel-personas.md`
- Always run 5 core personas (Oliver, Casey, Imran, Preethy, Taylor). Add conditional personas based on PRD type — see personas file for rules.

### Draft → Critique → Refine
Run for any significant document from scratch: Draft → Critique (panel) → Refine → Condense (PRDs: ~250–350 lines).
- Workflow: `02-workflows/draft-critique-refine.md`

### PRD Re-Review
No dedicated re-review skill exists yet. Use `/create-prd` for new PRDs; for auditing an existing PRD against the current template, do it manually against `03-templates/prd-template.md`.

### Create PRD
Run the full PRD creation workflow (Draft → Review Panel Critique → Refine → Condense).
- Skill: `/create-prd [topic or deliverable name]` — outputs a finished PRD to `04-active-work/`

### Strategic Review
Deep strategic review of any initiative, topic, or document. Opus analyses alignment and surfaces tensions; Sonnet writes the output.
- Skill: `/strategic-review [topic, file path, or initiative name]` — outputs a memo to `04-active-work/`

### Sync Meeting Notes
Pull new Gemini-generated meeting notes from Google Drive and write structured notes files. Run weekly or monthly to keep the PM brain current.
- Skill: `/sync-meeting-notes [optional: YYYY-MM-DD cutoff]` — scans Drive folder since last sync date, filters recurring syncs, writes to `04-active-work/meeting-notes/YYYY-MM/`
- Drive folder: `1Mnz7XMPGYaeZG0nHQ4_R9mYn06188zU8`
- Merchant interview outputs go to `04-active-work/research/merchant-support-needs/`
- Inserts key findings into knowledge base files where relevant

### Classifier Definitions
Generate AI-readable classification definitions (TSV, paste-ready for Google Sheets) from taxonomy or product catalogue.
- Skill: `/classify-definitions [taxonomy|products|both] [optional filter]`
- Output: one row per class, columns include include_when, exclude_when, disambiguation, keywords, phrases, entities, examples
- Saved to: `04-active-work/classifier-definitions-<scope>-<date>.tsv`

### Sync Product Catalogue
Sync the Airtable Product Catalogue to local files: updates `Checkout Products and teams.csv`, adds new product definitions to `product-definitions.md`, and (given a Zendesk export) produces an implementation sheet for Zendesk admins.
- Skill: `/sync-product-catalogue`

### Taxonomy Classification QA
QA Fin's contact classifications against the support taxonomy. Pulls the current batch from Looker (Look 18808) by default. Runs incrementally, appends to persistent log files, skips already-reviewed tickets.
- Skill: `/taxonomy-classification-qa [file-path | look:<id>]` — defaults to `look:18808`

### Workspace Review
Audit `04-active-work/`, assign keep/update/archive/delete verdicts per file, execute cleanup on confirmation. Also checks `04-active-work/` and `01-knowledge-base/` for deliverable dates/status that drift from `2026 deliverables.md`, and fixes them on confirmation.
- Skill: `/workspace-review`

### Write Fin Attribute
Draft or update a single Fin Attribute value definition (Case Type, Issue Type, Reason) in Intercom's Applies-if/Does-not-apply-if/Likely-keywords format. Writes to both `fin-attributes-definitions.md` (Intercom-ready) and `support-taxonomy.md` (QA skill's parseable source). Enforces Intercom's 2500-character limit.
- Skill: `/write-fin-attribute` — then supply value name, taxonomy path, definition, example queries

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

**Care product model 2030 mapping**: Full product mapping per flywheel stage and stack layer (existing, build, buy, agentic) is in `04-active-work/strategy/care-product-model-2030-mapping.md`.

**Operating model at scale**: Implications of 80%+ AI resolution by 2030 (agent roles, governance, knowledge infra, ownership, successor metrics) in `01-knowledge-base/strategy/operating-model-at-scale.md`.

**Platform segment (2026)**: Distinct B2B customer segment alongside Direct Merchants. Checkout is L2; Platform is L1 for its Platform merchants. US ISV launch in active delivery 2026. Platform Embedded AI (Fin in ISV portals) is a 2027 capability. Checkout-as-PayFac (2028+, unconfirmed) would make Checkout L1 for Platform merchants directly.
