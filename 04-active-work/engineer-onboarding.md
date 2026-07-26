# Engineering Onboarding — Care Product

**Owner**: Charlie Wildish (PM, Care Product)
**Last updated**: 2026-06-02
**For**: Javed — new engineer joining the Care Product team

---

## What This Team Does

Care Product builds the systems that handle merchant support at Checkout.com. Our job is to reduce the volume of contacts merchants need to raise, and reduce the cost of resolving them when they do. Everything we build serves one or both of those goals.

Two north star metrics:
- **Contact rate** — contacts per 1M transactions (reduce or maintain as transaction volume grows)
- **Cost per contact** — unit cost of resolving a contact (Fin costs $0.90/resolution; a human agent costs ~$40)

Guardrail: **CSAT & SLO must not decline as we automate**.

**Team composition (2026)**:
- 1 PM: Charlie Wildish
- 5 engineers + 1 Engineering Manager
- 2 Zendesk admins (separate function — Zendesk configuration is their domain, not engineering)
- Product Data Scientist
- Data Engineer (shared with wider teams)

---

## The Product Model

### The Care Flywheel

We think about our product surface as a flywheel with six stages. Every contact that arrives passes through all of them. Every product we build sits in one or more stages, and the value compounds — improving Input quality makes Orchestration more accurate; better Fuel makes AI resolution higher; better Insight closes the loop back to Input.

| Stage | What it covers | Key metric |
|---|---|---|
| **Input** | How a contact arrives and how it's classified. Channel mix, query taxonomy, AI as first point of contact | Fin involvement rate; taxonomy coverage % |
| **Orchestration** | Routing the contact to the right resolution path — AI or human, and which queue | First assignment accuracy; AI resolution rate |
| **Fuel** | The data and knowledge powering resolution — for both Fin and human agents | Data coverage vs taxonomy; content coverage % |
| **Agent Experience** | What human agents see, do, and can automate. Ticket handling, AI-assisted actions, diagnostics | Average handle time (AHT); AI suggestion acceptance rate |
| **Insight & Prevention** | Turning closed tickets into product fixes that eliminate future contacts | % of top contact drivers addressed by a product fix per quarter |
| **Governance** | SLA adherence, QA scoring, complaint handling | CSAT; SLA adherence % |

When you pick up a ticket or PRD, the first questions are: which stage does this sit in, and what metric does it move?

### Now vs. 2030

We are in early 2026. The model has strong foundations in Agent Experience and Orchestration, but significant gaps in Fuel (data latency is a known blocker) and Insight & Prevention (Reflex is in delivery). The 2030 target state is an AI-first support operation — Fin resolves 80%+ of contacts autonomously, Agent Consultant handles 90%+ of routine agent tasks, and Reflex operates as an autonomous insights agent generating weekly action plans and fix PRs for product teams.

| Capability | 2026 (now) | 2030 (target) |
|---|---|---|
| **AI resolution** | Fin on Dashboard + email, partial coverage. Resolves a minority of contacts | Fin is the majority channel across B2B, B2C, and Platform. 80%+ autonomous resolution |
| **Agent data tooling** | Merchant 360 context in sidebar (Q1 delivery). Payment data accessible but with latency | Real-time data across all sources, queryable via natural language. Proactive anomaly alerts before agent reads the ticket |
| **Agent AI assistance** | SOP-based suggestions live. Agent Consultant in foundation phase | Every ticket gets an AI-suggested action. 90%+ acceptance rate. Autonomous for permitted tasks; human approval for sensitive ones |
| **Insights and prevention** | Reflex in build. Support leaders present themes to Product manually and quarterly | Reflex runs weekly. Automated action plans sent to Product leads. Autonomous triage and fix PRs generated for engineering review by 2029 |
| **Content** | ~60% taxonomy coverage. Reactive monthly reviews | 90%+ coverage. AI-proposed updates weekly; Content team approves |
| **Customer segments** | B2B Direct Merchants + Platforms (ISV, 2026) | B2B Direct, Platforms, B2C consumer wallet (2027), B2B Banking (2028+) |

The work you join in 2026 is foundational — the decisions made this year on data architecture, AI tooling, and the support platform determine what's possible in 2027 and beyond.

---

## The Capability Stack

The Care capability stack has eight layers. Engineering owns or integrates with most of them. Understanding where each layer sits — and how they depend on each other — matters for any work that touches more than one.

| # | Layer | What it is | Today | 2030 target |
|---|---|---|---|---|
| 1 | **Channel** | How contacts arrive | Email and Dashboard webform (Zendesk) | Email, Dashboard, in-app chat, IM/Slack, Phone across B2B and B2C; Platform-tagged structured entry for ISV contacts |
| 2 | **Customer AI Agent** | AI that resolves contacts before a human sees them | Fin on Dashboard and some email; no Platform identification | Fin as triage on most channels; 80%+ autonomous resolution; embedded in ISV portals from 2027 |
| 3 | **Routing and Human Agent Experience** | Where tickets go, where agents work, cross-team escalation | Zendesk with manual and partial AI routing; limited cross-system escalation | Auto-classified routing; ~500-agent platform across B2B and B2C with walled permissions; cross-system escalation via Jira and custom APIs |
| 4 | **Agent AI Assistant** | Internal AI that assists human agents | Early investment — SOP-based suggestions live; Agent Consultant in foundation phase | Proactive action suggestion on every ticket; 90% of agent tasks automated or semi-automated; human approval for sensitive actions |
| 5 | **Integration and Data** | Joined-up merchant, payments, and ops data surfaced to AI and agents | Payin data with high latency; other sources not AI-ready; no Platform merchant data access | Accurate, low-latency data via MCPs across all sources; data layer graph tracks coverage per taxonomy Reason node (four states: no source / gaps / blocked / live) |
| 6 | **Knowledge** | Content published to the support site and to AI and agent tools | Reactive monthly content reviews; manual gap detection | Knowledge graph maps every Reason node to its content (`COVERED_BY` edges); 90%+ taxonomy coverage; proactive weekly AI-assisted updates |
| 7 | **Analytics and Insight** | Support data product for reporting, root-cause analysis, and prevention | Reflex in build | Weekly automated contact-driver reports; AI-generated action plans and fix PRs for engineering review |
| 8 | **Operations and Governance** *(cross-cutting)* | SLA, QA, scheduling, complaint handling | Zendesk SLAs, Zendesk QA, ad hoc scheduling | Automated QA at 90%+ scores; 95% SLA adherence; formal B2C complaint handling for Consumer Duty |

### How a contact flows through all eight layers

```
Merchant contacts via Channel (layer 1)
        ↓
Fin attempts resolution (layer 2 — Customer AI Agent)
        ↓ (if unresolved)
Zendesk ticket created — routed using routing rules (layer 3)
        ↓
Agent opens ticket → Agent Consultant activates (layer 4)
        ↓ (both Fin and Consultant draw on layers 5 and 6)
Integration & Data (layer 5) + Knowledge (layer 6) power resolution
        ↓ (on ticket close)
Ticket content → Reflex ingestion pipeline (layer 7)
        ↓
Reflex surfaces contact driver to Product team
        ↓
Product fix shipped → contact driver resolved → fewer future contacts
```

SLA adherence, QA, and complaint handling govern the whole flow (layer 8).

### Why this matters for engineering

- **Data (layer 5) is the main bottleneck.** Every new API we connect expands what Fin and Agent Consultant can resolve. Build data integrations to serve both simultaneously — the same data source powers Fin Procedures and Agent Consultant lookups.
- **Knowledge (layer 6) depends on data.** The knowledge graph needs the data graph to know whether a gap is a content problem or a data problem. Don't treat them as independent.
- **Reflex (layer 7) depends on ticket quality.** LLM analysis is only as good as the taxonomy tagging and Fin metadata in the tickets. Work that improves ticket data quality directly improves Reflex output.
- **Reflex MCP** (TBC — timing dependent on Phase 3 attribution model stability) exposes layer 7 insights as a read API so Fin, Agent Consultant, and other internal tools can query contact drivers programmatically — without manual reporting. This is a cross-deliverable dependency.
- **Zendesk config is not Engineering work.** Triggers, routing rules, ticket forms, and SLAs are owned by the Zendesk Admins. Engineering builds around Zendesk via API — not inside it.

---

## 2026 Roadmap: What We're Building

### Goal 1: Reduce / Maintain Contact Rate

| Deliverable | Status | What it is |
|---|---|---|
| Merchant Education Hub | Q1–Q4 | 20 tutorials on support.checkout.com covering top how-to tasks |
| Reflex | Q1–Q4 | AI ticket analysis surfacing top contact drivers to Product/Eng teams for prioritisation |
| Merchant Ticket Submission & Visibility | Q4 | Unified ticket submission via Fin + ticket status tracking in Dashboard |
| Consumer Support — Braavos App | Q4 | Support infrastructure for the B2C consumer wallet: Zendesk flows, taxonomy, agent content, and Fin mobile as the primary entry point |
| Proactive Notifications | 2027 | Real-time alerts for payment events before merchants contact support |

### Goal 2: Reduce Cost of Support

| Deliverable | Status | What it is |
|---|---|---|
| AI First Resolution (Fin Procedures + data) | Q2–Q4 | Expand Fin's data access and structured Procedures to resolve more contact types autonomously, including over email |
| AI Contextual Answers on Dashboard | Q3–Q4 | Contextual Fin buttons on Dashboard pages for instant, in-context answers |
| Merchant Context for Fin and Agents | Q1 ✓ / TBC | Merchant 360 data surfaced to Fin and Agent Toolkit; channel eligibility rules |
| Platform Support Channels | Q1 ✓ | ISV contact identification and routing; Platform merchant context in Zendesk |
| Agent Consultant | Q1–Q4 | Proactive AI suggestions in Zendesk — data lookups, SOP-based answers, action automation |
| Support Model | H2 | Tiered support model (Standard / Enterprise / Premium) with matched channels and SLAs |
| Replace Webform with Fin | Q3 | Retire the static webform; make Fin the primary intake channel |
| Agent Productivity Tools | Q1–Q4 | Zendesk/Jira integration, fraud data in toolkit, skill-based routing, SLA by issue type |
| Reduce Agent Effort (Dispatch + Email Rules) | Q2 | Zendesk config and domain-mapping improvements to cut manual triage |

Full detail per deliverable: `2026 deliverables.md`

---

## Customer Segments

**Direct Merchants** — companies that use Checkout.com payments directly. This is the majority of current support volume.

**Platforms (ISVs)** — vertical SaaS businesses that embed Checkout payments and act as a PayFac for their own merchants. Checkout is L2; the Platform is L1 for its Platform merchants. US ISV launch is in active delivery in 2026. When a Platform contacts us, they may be asking about their own account or about a specific Platform merchant's issue — distinguishing these matters for routing and data access.

**Consumers (B2C)** — individual users of the Braavos consumer wallet app, launching Q4 2026. This is a new segment entirely separate from B2B merchant support — different channel (in-app), different taxonomy, different regulatory obligations. Consumer Duty (UK) applies from day one, which means complaint handling and vulnerable customer identification must be live at launch, not added later. B2C agent permissions will be walled from B2B data.

---

## Key Stakeholders

| Role | Why they matter to Engineering |
|---|---|
| **Care Operations** | Day-to-day support ops — primary users of the Agent Toolkit and Zendesk; main feedback source on agent tooling |
| **Operational Excellence** | QA, SLA governance, process quality — co-owners on anything touching routing or ticket handling |
| **Zendesk Admins** | Own Zendesk configuration; Engineering coordinates with them on integrations but does not do Zendesk config |
| **Dashboard Engineering** | Owns the merchant-facing Dashboard — relevant for Fin integration, webform, ticket submission page |
| **Knowledge Manager** | Owns the knowledge base and Fin content — relevant for Fin Procedures and content integrations |

Decision model: consultative across Director of Operations, Director of Operations Excellence, PM (Charlie), and VP of Product.

---

## Systems Access

Request these on day one:

| System | Purpose |
|---|---|
| **Zendesk** | View ticket lifecycle, routing, and configuration; context for what agents experience |
| **Intercom** | Fin AI Agent config — Procedures, Guidance, Attributes, Copilot |
| **BigQuery** | Support contact data, Reflex pipelines, analytics |
| **Airtable** | Product Catalogue (product → team mapping); NPS data |
| **Confluence** | Team documentation; Agent Consultant task backlog (page ID 7847149938) |
| **GitHub** | Org: `github.com/cko-compass` — Care team repos are prefixed `care-` |
| **Salesforce** | Merchant account data (read access for context) |

Zendesk admin access is handled separately by the Zendesk admins — flag if you need it.

---

## How PM and Engineering Work Together

- **Jira board**: All work tracked in Jira under MCD project. Each deliverable has a linked ticket.
- **PRDs**: Major deliverables will have a PRD. Read the PRD before picking up work on a new deliverable — it has the why, scope, and success metrics.
- **Planning**: We plan on an annual, half, and quarterly basis. This helps shape scope long-term but allows agility in adapting the roadmap as needed.

