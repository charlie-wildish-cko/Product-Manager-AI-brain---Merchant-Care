# Welcome to the Care Product Team — Data Engineer Onboarding

---

## Who we are

The Care Product team builds the technology and data infrastructure that powers Checkout.com's merchant support. We sit at the intersection of AI, operations, and product — our job is to make support faster, smarter, and cheaper, without degrading merchant experience.

The team in 2026:

- 1 PM (Charlie Wildish)
- 4 Engineers + 1 Engineering Manager
- 2 Zendesk Admins
- 1 Product Data Scientist
- 1 Data Engineer (you)

---

## The strategy in one paragraph

We have two north star goals: reduce the **contact rate** (contacts per 1M transactions) and reduce **cost per contact**. We do both through a flywheel: better data fuels better AI (Fin), which deflects more contacts, which surfaces better insights, which feed back into the product to eliminate contact drivers at source. Every piece of work you do should connect to one of those two goals.

**Unit cost benchmarks**: Fin costs $0.90/resolution. A human agent costs ~$40/contact. The economics of shifting volume to AI are significant — your data work directly enables that shift.

---

## The tech landscape

### Support channels

- **Fin (Intercom)** — AI chat agent deployed in the Checkout Dashboard. Merchants start a conversation; Fin resolves it autonomously or escalates to a Zendesk ticket if it can't.
- **Zendesk** — Ticket management platform. Email and webform contacts land here directly. Agents handle everything Fin can't resolve.
- **Fin Copilot (Intercom)** — AI assistant for Care agents inside Zendesk. Surfaces suggested responses and data lookups to reduce average handle time.

### Key internal data sources

| Source | What it contains | Used for |
|---|---|---|
| Zendesk | Ticket data, tags, case type / issue type, channel, SLA status, agent actions | Contact volume reporting, routing, cost analysis |
| Intercom / Fin | Chat conversations, resolution flags, escalation events | Fin involvement rate, AI resolution rate |
| Merchant 360 / Entity DB | Merchant entity, processing profile, segment (Standard / Enterprise / Premium) | Contextual data surfaced in Fin and the agent toolkit |
| Salesforce | Account owner, territory, AM / TAM records | Merchant segmentation, territory-level breakdowns |
| Payments Search API | Payment transaction lookups by reference or ARN | Data Fin calls during live conversations (via Procedures) |
| Airtable | Product Catalogue, Merchant NPS | Product team mapping in Reflex; VoC correlation |

### The canonical data asset — support contacts flat table

The primary analytics dataset is the **support contacts flat table**: a denormalised view of all support interactions combining Zendesk tickets and Fin-only resolved conversations.

Ask Imran to share this with you alongside the taxonomy mapping files.

**Key columns:**

| Column | Definition |
|---|---|
| `zendesk_tickets` | Count of Zendesk tickets (solved or closed; excludes test, deleted, no-action, follow-ups) |
| `fin_only_resolved` | Conversations Fin resolved without creating a Zendesk ticket |
| `support_contacts` | `zendesk_tickets` + `fin_only_resolved` — no double-counting; one contact counted once |
| `case_type` | High-level category (e.g. PAYMENTS IN, ACCOUNT MANAGEMENT & ACCESS) |
| `issue_type` | More specific category within case_type (e.g. Refunds, Login & Access) |
| `support_segment` | Customer tier: Premium, Enterprise, or Standard |
| `channel` | How the merchant contacted us — see channel definitions below |
| `sales_territory` | Salesforce Account Owner territory (e.g. UK, NORAM, UAE) |
| `billing_region` | Account billing region (e.g. EEA, APAC) |

**Channel values:**

| Channel value | Meaning |
|---|---|
| Email (Merchant) | Submitted via email by the merchant |
| Email (Internal) | Submitted by Checkout.com internally — **not Fin-eligible; structurally unreachable by Fin** |
| Webform & API | Submitted via Dashboard webform or API |
| Fin (Dashboard) | Started in the Fin chat on Dashboard — counts as Fin-involved |
| Account unlock form | Subset of Other: case_type = ACCOUNT MANAGEMENT & ACCESS + issue_type = Login & Access |
| Other | Phone, Slack/IM, AM/TAM-submitted; mostly Fin-unreachable |

**Critical aggregation rule**: rows in the flat table are split by segment / channel / territory. Individual rows are not totals. Always `SUM(support_contacts) GROUP BY case_type, issue_type` before reporting — never use a row value as a headline figure.

**Derived metrics from the flat table:**
- **Fin involvement rate** = contacts where `channel = Fin (Dashboard)` / total `support_contacts`
- **Fin involved** = contacts where Fin participated (resolved or escalated)

---

## Contact taxonomy

All contacts are classified with a three-level system: **Case Type → Issue Type → Reason**.

The taxonomy is in active evolution in 2026 — do not assume field values are stable without checking with Charlie first.

**Volume by case type (last 6 months, actuals):**

| Case Type | Contacts | % of Volume |
|---|---|---|
| PAYMENTS (IN) | 10,049 | 42.8% |
| ACCOUNT MANAGEMENT & ACCESS | 3,961 | 16.9% |
| PAYOUTS | 2,345 | 10.0% |
| TECHNICAL ISSUE | 1,828 | 7.8% |
| GENERAL | 1,802 | 7.7% |
| FUNDS AND FEES | 1,760 | 7.5% |
| DATA AND ANALYTICS | 763 | 3.2% |
| NON MERCHANT REQUESTS | 350 | 1.5% |
| COMPLIANCE & AUDIT | 283 | 1.2% |
| ISSUING | 88 | 0.4% |
| PLATFORMS | 85 | 0.4% |
| FEEDBACK | 142 | 0.6% |
| IDENTITY VERIFICATION | 25 | 0.1% |
| **Total** | **23,481** | **100%** |

**Prioritisation logic**: PAYMENTS (IN) at 42.8% is the single highest-leverage area. ACCOUNT MANAGEMENT & ACCESS at 16.9% is second. These two case types are the primary targets for AI resolution improvement and data investment in 2026.

---

## The 2026 roadmap — where data engineering fits

### Reflex (highest data priority — Q1 through Q4)

Reflex is the team's intelligence engine. It analyses support tickets using LLMs to identify recurring contact drivers, maps them to product teams, and surfaces costed insights for Product prioritisation. The goal is to turn support data into a prevention engine — if a product team can see that a bug is generating 500 contacts/month at $40 each, the ROI of fixing it becomes undeniable.

**Why it matters**: Today, support contacts are a lagging signal that never reaches Product. Zendesk ticket queues are unread at scale by PMs. No product team is measured on the contacts their features generate. Reflex closes that loop.

**Architecture:**

| Component | What it does |
|---|---|
| Data Ingestion Layer | BigQuery pipelines: Zendesk tickets, Fin conversation metadata (Intercom API), Product Catalogue (Airtable), Merchant NPS (Airtable, joined via client ID) |
| AI Engine | LLM enrichment on BQ: per-ticket root cause summaries, theme aggregation, product team mapping, spike detection, content gap identification |
| Insights Query Interface | Self-serve dashboards for Support Leaders and Product teams; contact driver view, product team views, spike alert log |
| Reflex MCP | Programmatic API exposing: `GET /top-contact-drivers`, `GET /issue-detail/:issue_type`, `GET /product-insights/:product_id`, `GET /spike-alerts` |
| Jira Integration | Quarterly auto-creation of top contact drivers as Jira issues per product pillar (human review before publish) |

**Your phased build plan:**

| Phase | Quarter | Goal |
|---|---|---|
| Phase 1 | Q1 2026 (now) | BQ data foundation + per-ticket LLM root cause summaries POC |
| Phase 2 | Q2 2026 | Theme aggregation + product team mapping + Insights Query Interface |
| Phase 3 | Q3 2026 | Reflex MCP |
| Phase 4 | Q4 2026 | VoC correlation, spike detection, content gap identification, monthly digest |
| Phase 5 | Q4 2026 / Q1 2027 | Jira integration (TBC) |

---

### Merchant Context for Fin and Agents (Q1–Q2)

Pulling merchant data from Entity DB / Merchant 360 into Fin and the agent toolkit. Fin needs to know who it's talking to — entity structure, processing profile, segment — to give personalised, accurate responses. Involves integration between Zendesk, Intercom, and internal APIs.

---

### AI First Resolution Using Fin (Q2–Q3)

Extending Fin's data access via Procedures — structured scripts that define how Fin calls internal APIs during a live conversation. Current targets: payments lookups by reference/ARN, outages API, user management API. Data pipelines must be reliable and low-latency; Fin calls these synchronously.

---

### Agent Productivity and Routing (ongoing)

Zendesk routing rules, domain-to-org mapping for merchant attribution, Salesforce sync for AM/TAM records. Involves Engineering-side work (as distinct from Zendesk Admin configuration).

---

## Key metrics you will be building towards

| Metric | Definition | Why it matters |
|---|---|---|
| Contact rate | Contacts per 1M transactions | North star — demand side |
| Cost per contact | Total support cost / total contacts | North star — cost side |
| Fin involvement rate | % of contacts where Fin was first touchpoint | Deployment breadth; prerequisite for AI resolution rate improvements |
| AI resolution rate | % of Fin conversations resolved without human escalation | Primary AI quality metric |
| Re-contact rate | Merchants who contact again after a "resolved" Fin conversation | Quality check — high AI resolution rate with poor accuracy is invisible until this rises |
| Taxonomy automation rate | % of ticket fields auto-populated without agent input | Agent efficiency lever; also a data quality signal |
| Data attribution rate | % of tickets successfully attributed to a product / issue type | Reflex health metric; must be ≥95% for insights to be reliable |

---

## The flywheel model

All work maps to one of six stages:

```
Input → Orchestration → Fuel → Agent Experience → Insight & Prevention → Governance
```

**Where data engineering sits:**

- **Insight & Prevention** — Reflex analytics stack (BQ pipelines, LLM enrichment, MCP)

Good data at the Fuel stage improves AI resolution quality directly. Good data at the Insight & Prevention stage drives contact rate reduction by surfacing what to fix. These are the two highest-leverage places to be.

---

## Stakeholders you'll work with

| Stakeholder | Role | When relevant |
|---|---|---|
| Charlie Wildish | PM — your day-to-day product partner | All work |
| Engineering Manager | EM — engineering lead | Delivery and technical decisions |
| Care Operations | Day-to-day support operations team | Routing, SLA, agent-facing tooling |
| Operational Excellence | QA and process governance | Reporting requirements, QA tooling |
| Knowledge Manager | Owns the help centre content | Reflex content gap outputs |
| Zendesk Admins | Own all Zendesk configuration | Routing rules, triggers, org setup |

---

## How we work

- **Sprint cadence**: Managed in Jira (project: MCD). Link all work to the relevant ticket.
- **Data decisions**: Run significant data model or pipeline decisions past Charlie and the EM before implementing. Changes to the flat table schema or key metric definitions need explicit sign-off.
- **Taxonomy is live**: The support taxonomy is actively changing in March 2026.

---
