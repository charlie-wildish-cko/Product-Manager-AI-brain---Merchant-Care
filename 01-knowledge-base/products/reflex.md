# Reflex

> Support insights solution that analyzes support data to identify root causes and publishes them on demand or on schedule.

## What it is

**Reflex** analyzes support data to identify contact root causes. It can publish insights on demand or on a schedule (e.g. weekly, quarterly).

## Users

- **Care Product team** — understand what issues their products create
- **Product Managers** — see contact drivers and prevention opportunities for their products

## Components

| Component | Description |
|---|---|
| **Data Ingestion Layer** | BQ pipelines: Zendesk tickets, Fin conversation metadata (Intercom API), Product Catalogue (Airtable), Merchant NPS (Airtable, joined via client ID). Fin conversation content (full text) is TBD — Intercom API export does not include it. |
| **AI Engine ("the whale")** | LLM enrichment layer on BQ: per-ticket root cause summaries, theme aggregation, product team mapping (via taxonomy + product catalogue), spike detection, VoC correlation, content gap identification |
| **Insights Query Interface** | Self-serve reporting for Support Leaders, PMs, and Product teams: contact driver dashboard, product team views, spike alert log, VoC view, self-serve query (tool TBD) |
| **Reflex MCP** | Programmatic API: `GET /top-contact-drivers`, `GET /issue-detail/:issue_type`, `GET /product-insights/:product_id`, `GET /spike-alerts`. Enables query interface and other internal teams to query insights. Cross-deliverable dependency for MCD-568 (Fin Procedures) and MCD-564 (Agent Consultant). |
| **Jira Integration** | Quarterly auto-creation of top 5–10 stack-ranked contact drivers as Jira issues per product pillar; pre-populated with volume, cost, trend, example tickets, recommended team; human review before publish |

## 2026 Roadmap

**Jira**: MCD-565 · **Full phased plan**: `04-active-work/reflex-phased-plan.md`

| Phase | Quarter | Goal |
|---|---|---|
| Phase 1 | Q1 2026 | BQ data foundation + per-ticket LLM root cause summaries |
| Phase 2 | Q2 2026 | Theme aggregation + product team mapping + Insights Query Interface |
| Phase 3 | Q3 2026 | Reflex MCP |
| Phase 4 | Q4 2026 | VoC, spike detection, governance automation |
| Phase 5 | Q4 2026 / Q1 2027 | Jira integration (TBC) |

## Vision: Insight & Prevention solution (2030 end goal)

**End goal by 2030:** Reflex operates like **Stripe Minions** — an autonomous Insight & Prevention solution that identifies root causes, generates action plans (and potentially code/PRs), and escalates to Care & Product teams for triage and resolution as BAU. Humans review and ship; Reflex does the analysis and drafting.

### Stripe Minions (analogy)

[Stripe Minions](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents) are Stripe’s internal AI coding agents: they write code end-to-end in one shot, producing 1000+ merged PRs per week. Humans review and merge; Minions do the work. The parallel for Reflex: autonomous agents that produce actionable outputs (action plans, PRs) for humans to triage and ship — rather than humans doing the analysis and drafting from scratch.


**Related**: [Care Product Model](../strategy/care-product-model.md) (Insight & Prevention domain), [Support Scale Principles](../strategy/support-scale-principles.md)
