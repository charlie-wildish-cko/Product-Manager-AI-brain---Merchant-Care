# Engineering Onboarding: Care Product

**Owner**: Charlie Wildish (PM, Care Product)
**Last updated**: 2026-04-20
**For**: New engineers joining the Care Product team

---

## What This Team Does

Care Product builds the systems that handle merchant support at Checkout.com. Our job is to reduce the volume of contacts merchants need to raise, and reduce the cost of resolving them when they do. Everything we build serves one or both of those goals.

Two north star metrics:
- **Contact rate** — contacts per 1M transactions (reduce or maintain as transaction volume grows)
- **Cost per contact** — unit cost of resolving a contact (Fin costs $0.90/resolution; a human agent costs ~$40)

The guardrail: **Merchant CSAT must not decline as we automate**.

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

## The Agentic Support Stack

We are building three interconnected AI systems. They are distinct products but share data and depend on each other. Understanding how they connect matters for any engineering work that touches more than one.

### The three systems

**Fin** is the customer-facing AI agent. It is the first point of contact for most merchants — deployed in the Checkout Dashboard and handling email tickets via the Zendesk integration. Fin resolves queries autonomously using knowledge articles and structured Procedures (Fin's equivalent of SOPs: step-by-step resolution flows that can call APIs, retrieve data, and respond). When Fin cannot resolve, it hands off to Zendesk with context attached.

**Agent Consultant** is the internal AI agent for human agents in Zendesk. When an agent opens a ticket, Consultant proactively surfaces context, suggests a next action based on SOPs, and — for permitted task types — can execute actions with agent approval (human-in-the-loop). It also runs QA on closed tickets and flags content gaps. It runs inside Zendesk as a sidebar application.

**Reflex** is the insight and prevention engine. It ingests every closed ticket and Fin conversation, applies LLM analysis to extract root causes and theme clusters, maps them to Product teams via the Product Catalogue, and surfaces ranked contact drivers to Product leads. By 2028–29, it begins generating autonomous fix PRs — operating like Stripe Minions, where an agent does the analysis and drafting and humans review and ship.

### How they connect

```
Merchant contacts → Fin attempts resolution
                          ↓ (if unresolved)
                    Zendesk ticket created (with Fin context attached)
                          ↓
              Agent opens ticket → Agent Consultant activates
                          ↓ (on ticket close)
              Ticket content summary → Reflex ingestion pipeline
                          ↓
              Reflex surfaces contact driver to Product team
                          ↓
              Product fix shipped → contact driver resolved
```

There is a fourth component that connects them programmatically: the **Reflex MCP** (in delivery, Q3 2026). It exposes Reflex insights via a read API so that Fin, Agent Consultant, and other internal tools can query contact drivers and knowledge gaps without manual reporting. This is the infrastructure that makes the insight loop automatic rather than manual.

### Why this matters for engineering

- **Fin Procedures** depend on data API access. Every new data source we connect (payments, settlements, balances, user management) directly expands the set of contacts Fin can resolve without a human. The bottleneck today is data latency and coverage — not the AI.
- **Agent Consultant** depends on the same data. An Agent Consultant action that retrieves settlement data relies on the same underlying API as a Fin Procedure for that query type. Build data integrations to serve both, not one at a time.
- **Reflex** depends on ticket quality. The LLM analysis is only as good as what's in the tickets — taxonomy tagging, ticket content, Fin conversation metadata. Work that improves ticket data quality (classification, enrichment) directly improves Reflex output.
- **Reflex MCP** is a cross-deliverable dependency. When it ships (Q3 2026), it unlocks Agent Consultant improvements and enables Fin to query contact driver signals directly.

---

## The Tech Stack (from a PM lens)

You'll need to understand these systems. Engineering owns the APIs and integrations; Zendesk admins own the configuration inside Zendesk itself.

| System | What it does | Who owns it |
|---|---|---|
| **Zendesk** | Ticketing, routing, SLA, QA, help centre (support.checkout.com) | Zendesk Admins (ops/admin function, not Engineering) |
| **Fin (Intercom)** | AI Agent — resolves contacts before a human sees them, embedded in the Checkout Dashboard. Fin for Zendesk handles email/tickets | Product + Content (shared ownership) |
| **Agent Consultant** | AI assistant inside Zendesk — suggests data, answers, and actions for agents on every ticket | Engineering builds; agents use |
| **Reflex** | AI-powered ticket analysis that surfaces top contact drivers to Product and Engineering teams | Engineering builds |
| **Agent Toolkit** | Data surfaced to agents inside Zendesk (payment data, merchant profile, fraud signals, etc.) | Engineering builds |
| **Merchant 360 / Entity data** | Merchant account data used for context in Fin and Agent Toolkit | Integration dependency — Engineering connects |
| **Jira** | Cross-team escalation from Zendesk (bi-directional integration in progress) | Engineering |

Zendesk configuration (triggers, routing rules, ticket forms, SLAs) is done by the Zendesk Admins — that is not Engineering work. Engineering builds anything that sits outside Zendesk or integrates with it via API.

---

## 2026 Roadmap: What We're Building

### Goal 1: Reduce / Maintain Contact Rate

| Deliverable | Status | What it is |
|---|---|---|
| Merchant Education Hub | Q1–Q4 | 20 tutorials on support.checkout.com covering top how-to tasks |
| Reflex | Q1–Q4 | AI ticket analysis surfacing top contact drivers to Product/Eng teams for prioritisation |
| Merchant Ticket Submission & Visibility | Q3 | Unified ticket submission via Fin + ticket status tracking in Dashboard |
| Proactive Notifications | TBC | Real-time alerts for payment events before merchants contact support |
| Dashboard Onboarding | TBC (Dashboard team dependency) | Guided in-app onboarding to reduce new merchant support contacts |

### Goal 2: Reduce Cost of Support

| Deliverable | Status | What it is |
|---|---|---|
| AI First Resolution (Fin Procedures + data) | Q2–Q3 | Expand Fin's data access and structured Procedures to resolve more contact types autonomously, including over email |
| AI Contextual Answers on Dashboard | Q2–Q3 | Contextual Fin buttons on Dashboard pages for instant, in-context answers |
| Merchant Context for Fin and Agents | Q1 ✓ / TBC | Merchant 360 data surfaced to Fin and Agent Toolkit; channel eligibility rules |
| Platform Support Channels | Q1 ✓ | ISV contact identification and routing; Platform merchant context in Zendesk |
| Agent Consultant | Q1–Q4 | Proactive AI suggestions in Zendesk — data lookups, SOP-based answers, action automation |
| Support Model | Q2–Q3 | Tiered support model (Standard / Enterprise / Premium) with matched channels and SLAs |
| Replace Webform with Fin | Q3 | Retire the static webform; make Fin the primary intake channel |
| Agent Productivity Tools | Q1–Q4 | Zendesk/Jira integration, fraud data in toolkit, skill-based routing, SLA by issue type |
| Reduce Agent Effort (Dispatch + Email Rules) | Q2 | Zendesk configuration and domain-mapping improvements to cut manual triage |

---

## Customer Segments

Two B2B segments in 2026:

**Direct Merchants** — companies that use Checkout.com payments directly. This is the majority of our current support volume.

**Platforms (ISVs)** — vertical SaaS businesses that embed Checkout payments and act as a PayFac for their own merchants. Checkout is L2; the Platform is L1 for its Platform merchants. The US ISV launch is in active delivery this year. When a Platform contacts us, they may be asking about their own account or about a specific Platform merchant's issue — distinguishing these is important for routing and data access.

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

## How PM and Engineering Work Together

- **Jira board**: All work tracked in Jira under MCD project. Each deliverable has a linked ticket.
- **PRDs**: Major deliverables have a PRD in `04-active-work/`. Read the PRD before picking up work on a new deliverable — it has the why, scope, and success metrics.
- **Scope rule**: PRD scope maps verbatim to named roadmap deliverables. If something isn't in the PRD, raise it with Charlie before building it.
- **Definition of done**: Each deliverable has a "Done when" statement. Use it to align on when something is truly complete, not just deployed.
- **Data access**: Never use placeholder data. Real contact volume data is in `01-knowledge-base/metrics/support_contacts_flat_table_2025_last_6m.csv`. Column definitions in the adjacent metric definitions file.

---

## Orientation Reading (priority order)

1. `01-knowledge-base/strategy/care-product-model.md` — the flywheel and capability stack in full
2. `2026 deliverables.md` — the full 2026 roadmap with detail per deliverable
3. `01-knowledge-base/products/reflex.md` — Reflex product reference (you'll likely touch this)
4. `01-knowledge-base/products/agent-consultant.md` — Agent Consultant capabilities
5. `01-knowledge-base/products/fin-ai-agent.md` — how Fin works and how we've deployed it
6. `01-knowledge-base/products/zendesk.md` — Zendesk setup, business rules, data pipeline
7. `01-knowledge-base/products/platform-segment.md` — Platform segment detail for ISV context
