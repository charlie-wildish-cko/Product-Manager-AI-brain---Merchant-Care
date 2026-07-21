# Charlie PM Brain

Charlie Wildish's workspace for Merchant Care (Customer Support) PM work at Checkout.com. A markdown-native second brain: knowledge base, templates, workflows, active work, and archive, with Claude Code operating on top via `CLAUDE.md`, skills, and agents.

## The One Principle

All work ties back to strategy. Never produce work that floats.

Every document, analysis, or recommendation connects to a strategic goal (reduce contact rate, reduce cost of support), a north star metric (contact rate, cost per contact), a guardrail metric (merchant CSAT), a named 2026 deliverable, and a flywheel domain (Input → Orchestration → Fuel → Agent Experience → Insight & Prevention → Governance).

Full detail: [CLAUDE.md](CLAUDE.md) — the source of truth for how Claude should work in this repo. Read it before making structural changes here.

## Directory Structure

```
Charlie PM brain/
├── CLAUDE.md                       # AI context: role, principles, style, workflows, stakeholders
├── 2026 deliverables.md            # 2026 roadmap: goals, quarters, flywheel map (source of truth for dates)
│
├── 01-knowledge-base/              # Reference — strategy, products, processes, payment domain, metrics
│   ├── strategy/                   # Flywheel model, scaling principles, competitive audits
│   ├── products/                   # Product reference docs (segments, Reflex, Agent Consultant, Fin, Zendesk)
│   ├── processes/                  # Support workflows, taxonomy, SOPs, review panel personas
│   ├── payment-domain/             # Payment/fintech terminology (200 terms)
│   ├── metrics/                    # KPI definitions, contact forecasts
│   ├── bigquery-queries/           # Saved SQL query library
│   ├── Support content/            # Support articles, tech docs, API reference (exported)
│   └── Checkout Products and teams.csv
│
├── 02-workflows/                   # Step-by-step process guides (ticket analysis, PRD writing, reviews)
├── 03-templates/                   # Reusable document templates (PRD, memo, RFC, postmortem, etc.)
├── 04-active-work/                 # Active work — prds/, strategy/, research/, working-files/, meeting-notes/
├── 05-archive/                     # Completed work, by year/quarter
│
└── .claude/skills/                 # Slash-command skills (see below)
```

Each major directory has its own `README.md` with a current file-by-file index — check there for specifics.

## Starting a New Task

1. **Orient** — check `04-active-work/` for existing work before starting from scratch. PRDs live in `04-active-work/prds/<initiative>/`, strategy in `04-active-work/strategy/`, research in `04-active-work/research/`, data artefacts in `04-active-work/working-files/`.
2. **Anchor** — confirm the task maps to a named deliverable and quarter in `2026 deliverables.md`. Flag it if it doesn't.
3. **Clarify the output format** — PRD, memo, Slack update, stakeholder update, analysis, exploration.
4. **Draft** — use the relevant template and writing style (see `01-knowledge-base/processes/writing-style-guide.md`).

## Skills

Invoke with `/<skill-name> [args]`. Full definitions in `.claude/skills/`.

| Skill | Purpose |
|---|---|
| `/create-prd [topic]` | Full PRD workflow: Draft → Review Panel Critique → Refine → Condense. Saves to `04-active-work/` |
| `/strategic-review [topic]` | Deep strategic review of an initiative or document; surfaces tensions and alignment |
| `/sync-meeting-notes [cutoff date]` | Pull new Gemini meeting notes from Drive, write structured notes to `04-active-work/meeting-notes/` |
| `/classify-definitions [taxonomy\|products\|both]` | Generate AI-readable classification definitions (TSV) from taxonomy or product catalogue |
| `/sync-product-catalogue` | Sync the Airtable product catalogue to local CSV + product definitions |
| `/taxonomy-classification-qa [source]` | QA Fin's contact classifications against the support taxonomy (defaults to Looker Look 18808) |
| `/workspace-review` | Audit `04-active-work/`, assign keep/update/archive/delete verdicts, fix deliverable-date drift |
| `/write-fin-attribute` | Draft or update a single Fin Attribute value definition (Intercom format) |

## Key Reference Files

| Purpose | File |
|---|---|
| 2026 roadmap (goals, quarters, flywheel map) | `2026 deliverables.md` |
| Care Product flywheel model | `01-knowledge-base/strategy/care-product-model.md` |
| Care Product strategy 2026-2030 (Rumelt kernel) | `04-active-work/strategy/care-product-strategy-2026-2030.md` |
| Team structure & stakeholders | `01-knowledge-base/teams.md` |
| Support taxonomy & contact volumes | `01-knowledge-base/processes/support-taxonomy.md` |
| Fin Attribute definitions (Intercom-ready) | `01-knowledge-base/processes/fin-attributes-definitions.md` |
| Care Agent SOPs & KB index | `01-knowledge-base/processes/Care Agent SOPs/INDEX.md` |
| Product catalogue | `01-knowledge-base/Checkout Products and teams.csv` |
| Product definitions + contact risk tags | `01-knowledge-base/products/product-definitions.md` |
| Payment domain terminology (200 terms) | `01-knowledge-base/payment-domain/checkout-terminology.md` |
| KPI definitions | `01-knowledge-base/metrics/kpi-definitions.md` |
| Contact volume forecasts 2026-2030 | `01-knowledge-base/metrics/contact forecasting.md` |
| Reflex product reference | `01-knowledge-base/products/reflex.md` |
| Fin AI Agent reference | `01-knowledge-base/products/fin-ai-agent.md` |
| Zendesk reference | `01-knowledge-base/products/zendesk.md` |
| PRD template + example | `03-templates/prd-template.md`, `03-templates/prd-template-example.md` |
| Writing style guide (by audience) | `01-knowledge-base/processes/writing-style-guide.md` |

See `CLAUDE.md` for the full reference table, data rules (real data only, no placeholders), and PRD framework.

## Working with Claude

Ask Claude to draft documents, analyze ticket data, explain payment concepts, review drafts, or run any skill above. Claude has role and domain context loaded from `CLAUDE.md` — no need to re-explain who you are or what the strategic goals are each time.

**Examples**:
> "Draft a PRD for [feature] — run `/create-prd`"

> "What quarter is [deliverable] scoped to?"

> "Analyze this ticket data and identify the top 3 product opportunities"

> "Run a strategic review on [initiative]"

## Maintenance

- **Deliverable dates**: `2026 deliverables.md` is the single source of truth for quarters. When editing any doc that states a quarter, verify against it first; fix drift in the same pass.
- **Archive before drafting**: search `05-archive/` and `04-active-work/` for prior versions before creating a new document from scratch.
- **Run `/workspace-review` periodically** to catch stale `04-active-work/` files and deliverable-date drift.
- **Real data only**: never use placeholder numbers. See the Data Rules section in `CLAUDE.md` for canonical sources.

---

**Owner**: Charlie Wildish, PM — Merchant Care (Customer Support), Checkout.com
