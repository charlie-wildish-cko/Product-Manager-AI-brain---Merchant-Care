# Reflex — Components and Build Sequence

## Context

Reflex is the Insight & Prevention engine for Merchant Care. It analyses support data to identify contact root causes and surfaces them to Product and Content teams for action. The full architecture comprises:

- **Inputs**: Fin AI Agent conversations (Intercom) + Zendesk agent-handled tickets + Product Catalogue / Merchant NPS (Airtable)
- **Centralised data layer**: BigQuery — all data stored mapped to Merchant data and Product Catalogue
- **AI engine ("the whale")**: Extracts, summarises, and aggregates themes for analysis and tagging
- **Insights Query Interface**: Makes data available for reporting; linked to Product teams; users can query for detailed information
- **Jira**: Issues assigned to Product team backlogs; deliveries tracked quarterly

**Strategic goal**: Reduce contact rate
**Flywheel domain**: Insight & Prevention (Learn)
**Jira**: MCD-565

---

## Part 1: Components of Reflex

### 1. Data Ingestion Layer
Pipelines that bring raw support data into a centralised BigQuery dataset.

| Component | Source | Data |
|---|---|---|
| Zendesk ticket ingestion | Zendesk (already in BQ) | Tickets, comments, metadata, tags, org/user info |
| Fin conversation metadata | Intercom API | Involvement, resolution status, escalation flag, topic tags |
| Fin conversation content | Intercom (TBD — Webhooks or Data Export API) | Conversation text for AI summarisation |
| Product Catalogue mapping | Airtable | Product → pillar → team mapping, joined to ticket metadata |
| Merchant NPS | Airtable | NPS scores joined to Zendesk organisations via client ID |

> **Open question**: Intercom API export does not include conversation-level text. A separate solution (Webhooks, Data Export API) is needed before Fin conversation content can be used for root cause analysis.

---

### 2. AI Engine ("The Whale")
LLM-powered enrichment and aggregation layer that runs on top of the raw data in BigQuery.

| Component | Description |
|---|---|
| **Per-ticket root cause summary** | For each Zendesk ticket, LLM generates a structured root cause summary: root_cause_summary (text), root_cause_category (enum), product_area, resolution_type; also maps to support taxonomy (case_type → issue_type) |
| **Theme aggregation** | Groups per-ticket summaries into recurring theme clusters by product_area, root_cause_category, and taxonomy mapping; surfaces top themes by volume and cost |
| **Product team mapping** | Maps theme clusters to Product teams using Product Catalogue metadata (product → pillar → team) and taxonomy-to-product mapping |
| **Spike detection** | Monitors inbound volume for anomalies by issue type; triggers alerts when thresholds exceeded |
| **VoC correlation** | Correlates contact theme clusters with NPS data to surface merchant sentiment trends |
| **Content gap identification** | Surfaces knowledge article gaps to Content/Knowledge Manager based on unresolved or recurring queries |

---

### 3. Insights Query Interface
Self-serve reporting and query layer for Support Leaders, PMs, and Product teams.

| Component | Description |
|---|---|
| **Contact driver dashboard** | Top contact drivers by volume, cost ($40/contact), trend — filterable by product, segment, territory |
| **Product team view** | Top contact drivers mapped to each Product team's scope; quarter-on-quarter comparison |
| **Spike alert log** | History of detected spikes; triage and escalation status |
| **VoC view** | Merged support + NPS view; contact reason correlation with NPS movement |
| **Self-serve query** | Users can ask questions against Reflex data without direct BQ access (tool TBD) |

---

### 4. Reflex MCP
Programmatic API layer that makes Reflex insights queryable by AI tools and agents.

| Endpoint | Description |
|---|---|
| `GET /top-contact-drivers` | Returns ranked list of contact drivers by volume and cost |
| `GET /issue-detail/:issue_type` | Returns root cause summary and theme breakdown for a specific issue type (mapped via support taxonomy) |
| `GET /product-insights/:product_id` | Returns contact drivers mapped to a specific product |
| `GET /spike-alerts` | Returns current and recent spike alerts |

Key cross-deliverable dependency for MCD-568 (Fin Procedures) and MCD-564 (Agent Consultant).

---

### 5. Jira Integration
Routes Reflex insights to Product team backlogs for action.

| Component | Description |
|---|---|
| **Quarterly auto-creation** | Top 5–10 contact drivers stack-ranked by volume and cost auto-surface as Jira issues each quarter; pre-populated with volume, cost, trend, example tickets, and recommended Product team (human review before publish) |
| **Product team mapping** | Issues routed to correct Jira project/board based on Product Catalogue pillar → team mapping |

---

## Part 2: Build Sequence

### Phase 1 — Q1 2026: Data Foundation + Per-Ticket Root Cause Summaries
**Goal: get data flowing; generate AI root cause summaries for every ticket**

- Stand up BQ ingestion: Zendesk tickets (validate), Fin metadata (Intercom API), Product Catalogue (Airtable mapping)
- Build AI engine component 1: per-ticket root cause summaries written back to BQ enrichment table
- Build basic contact driver dashboard: top drivers by volume and cost

**Done when**: Per-ticket summaries live in BQ

---

### Phase 2 — Q2 2026: Theme Aggregation + Product Mapping + Query Interface
**Goal: aggregate summaries into themes; map to Product teams; make insights self-serve**

- Build AI engine component 2: theme cluster aggregation + product team mapping
- Build Insights Query Interface (tool TBD): Product team views, self-serve querying, shareable insight links
- Establish quarterly reporting cadence to Product leads

**Done when**: Aggregated theme clusters live; top 10 contact drivers quantified and shared with VP Product and Director of Operations; at least one Product team using Reflex output for prioritisation

---

### Phase 3 — Q3 2026: Reflex MCP
**Goal: make Reflex programmable; enable query interface and other team access**

- Build and deploy Reflex MCP with read endpoints
- Enables Insights Query Interface and other internal teams to query Reflex insights programmatically

**Done when**: MCP live; Insights Query Interface connected; Product fix governance cycle started

---

### Phase 4 — Q4 2026: VoC, Spike Detection, and Governance Automation
**Goal: broaden the signal; automate the governance loop**

- Fin conversation content ingestion (if solution confirmed for Intercom export)
- NPS data merge into VoC view (Airtable source; joined via client ID)
- Spike detection and alert mechanism
- Weekly Reflex digest to Product team leads
- Content gap identification surfaced to Knowledge Manager

**Done when**: VoC dashboard live; spike detection running; Product teams on weekly digest; attribution model tracking contact rate reduction from Reflex-originated fixes

---

### Phase 5 — Q4 2026 / Q1 2027: Jira Integration (TBC)
**Goal: automate the quarterly Product fix backlog from Reflex**

- Automated quarterly creation of top 5–10 stack-ranked Jira issues per product pillar
- Pre-populated with volume, cost, trend, example tickets, and recommended Product team (mapped via product catalogue)
- Issues routed to correct Jira project/board based on pillar → team mapping
- Human review step before issues publish

**Done when**: Quarterly Jira issues auto-created and reviewed by Product leads; Product team contact reduction targets tracked against Reflex-originated fixes

---

## Open Questions

1. **Fin conversation content**: Intercom API export lacks conversation text. Webhooks or Data Export API solution needed before Phase 4.
2. **Insights Query Interface tool**: Confirm available tooling (Looker, Retool, or other) before Phase 2 build starts.
3. **MCP hosting**: Standalone service or shared infra with Agent Consultant?
