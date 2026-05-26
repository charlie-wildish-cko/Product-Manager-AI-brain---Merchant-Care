# Care Product Model 2030 — Comprehensive Product Mapping

> **Status**: Working draft  
> **Owner**: Charlie Wildish  
> **Created**: 2026-04-21  
>
> **Source of truth**: This doc owns the product mapping — what products (existing, adjacent, build, buy, agentic) are needed within each flywheel capability and stack layer. It does not own the model structure or delivery sequencing.
> - Model structure (flywheel + stack definitions): [Care Product Model](../../01-knowledge-base/strategy/care-product-model.md)

Classification key:
- **EXISTING (Care)** — already in the Care product set
- **EXISTING (Checkout)** — exists at Checkout but not currently modelled as Care
- **BUILD** — new product to be defined and built
- **BUY** — third-party product to evaluate and procure
- **AGENTIC** — scoped AI agent that needs to be designed as a discrete product

---

## Part 1: Flywheel — Product mapping per stage

### Stage 1: Input

| Capability | Products | Build/Buy/Existing | Gap by 2030 | Dependencies |
|---|---|---|---|---|
| B2B query taxonomy | Reflex; **Taxonomy Registry (BUILD)** — versioned, API-addressable store of Case Type / Issue Type / Reason nodes with product mappings; **Taxonomy Governance Workflow (BUILD)** | EXISTING (Reflex) + BUILD | Taxonomy is markdown today. 2030 needs a machine-readable registry consumed by Fin, Zendesk, Reflex, and Knowledge Graph as the single source of truth | Product Catalogue CSV; Reflex MCP |
| B2C query taxonomy | Reflex; Taxonomy Registry; **Consumer Duty Taxonomy Module (BUILD)** — vulnerable customer, complaint, agentic-commerce-liability reason codes | BUILD | Does not exist. Wallet launch 2027 forces this | Wallet product scope mid-2026; Legal & Compliance input |
| B2B Banking taxonomy | Reflex; Taxonomy Registry; **Banking Taxonomy Module (BUILD)** — balances, yield, treasury, working capital | BUILD | Does not exist. 2028+ launch | Banking product scope 2027 |
| Support channels — B2B | Fin; Zendesk; **Dashboard In-Product Support SDK (BUILD)** — embeddable support widget across Dashboard surfaces; **Voice Platform (BUY)** — Aircall, Dialpad, Zendesk Talk, or Amazon Connect for Premium phone; **IM/Slack Connector (BUILD on BUY)** — Slack Connect or Microsoft Teams bridge into Zendesk | EXISTING + BUY + BUILD | Phone and IM/Slack channels do not exist. Dashboard contextual Fin needs a reusable SDK rather than per-page integrations | Fin CC handoff; Success Plans Premium tier; Voice vendor selection |
| Support channels — B2C | Fin; **Mobile SDK for Support (BUILD)** — iOS/Android in-app chat component for wallet; **Voice Platform (BUY)**; **Complaint Intake Portal (BUILD)** — regulated complaint entry separate from ticket entry | BUILD + BUY | All net-new. Must exist at wallet launch 2027 | Wallet product; Consumer Duty process |
| Support channels — Platform | Platform Embedded AI; **Platform Identity Service (BUILD)** — tags every inbound contact with Platform ID and optional Platform-merchant ID; **Platform Portal SDK (BUILD)** — embeds Fin inside ISV portals | EXISTING + BUILD | Platform identification does not exist on inbound today. Embedded AI is vision only | ISV commercial agreements; Platform merchant data APIs |
| Taxonomy automation | Reflex; **Taxonomy Curator Agent (AGENTIC)** — continuously proposes taxonomy changes from contact data and Fin misclassification signals | EXISTING + AGENTIC | Taxonomy updates are still human-curated quarterly. 2030 target is proposed-and-approved without manual trigger | Reflex MCP; Taxonomy Registry API |

**Stage summary.** Input is well-covered for existing B2B email/Dashboard channels but has four structural gaps: (1) the taxonomy is a document, not a product — a Taxonomy Registry is the single most under-scoped item in the current model; (2) phone is a buy decision not yet made and is regulator-forced by 2027; (3) Platform identification has no product owner today; (4) no mobile SDK exists for the 2027 wallet. Net-new products needed: Taxonomy Registry, Platform Identity Service, Mobile Support SDK, Complaint Intake Portal, Voice Platform, Dashboard Support SDK, Taxonomy Curator Agent.

---

### Stage 2: Orchestration

| Capability | Products | Build/Buy/Existing | Gap by 2030 | Dependencies |
|---|---|---|---|---|
| Auto-classification | Fin; Zendesk; **Classification Service (BUILD)** — model-agnostic classifier sitting in front of Zendesk/Fin that tags every contact against the Taxonomy Registry, independent of channel | EXISTING + BUILD | Today classification is split between Fin (Dashboard/email) and manual routing (webform, escalations). A single service removes the split | Taxonomy Registry; training data from Reflex |
| Channel eligibility rules | Customer 360; Success Plans; **Entitlements Service (BUILD)** — real-time eligibility for channels, tiers, SLA by merchant/consumer ID | EXISTING + BUILD | Success Plans defines rules but there is no runtime service exposing them. Entitlements should be one API consumed by Fin, Zendesk, Dashboard SDK | Customer 360 completeness; Salesforce (tier source of truth) |
| Merchant tier routing | Success Plans; Zendesk; Entitlements Service; **Salesforce (EXISTING Checkout)** — tier data source | EXISTING + BUILD | Tier data is in Salesforce; Care has no automated feed today. Reliance on manual updates in Zendesk | Salesforce integration |
| Platform routing | Platform Embedded AI; Zendesk; Platform Identity Service; **Platform Merchant Directory (BUILD)** — joined directory of Platform → Platform merchants with entity, KYB, status | BUILD | Neither Platform ID nor Platform merchant lookup exists. Blocker for all Platform orchestration | Platform Identity Service; ISV data contracts |
| AI-to-human escalation logic | Fin; Zendesk; **Fin Procedures Library (BUILD within Fin)**; **Escalation Policy Engine (BUILD)** — declarative rules per reason × tier × confidence | EXISTING + BUILD | Escalation logic is hard-coded in Fin today. A policy engine decouples rules from model | Fin Procedures; Entitlements Service |
| B2C routing | Fin; Success Plans; **Vulnerable Customer Triage Agent (AGENTIC)** — routes sensitive/vulnerable contacts away from self-service to human | EXISTING + AGENTIC | Does not exist. Consumer Duty forces this pre-launch 2027 | Wallet; B2C taxonomy; vulnerability detection model |
| SLA rules by merchant level and reason type | Zendesk; Success Plans; Entitlements Service | EXISTING | SLA definitions exist per tier but not per reason. 2030 needs reason × tier matrix enforced in real time | Support model completion; SLA matrix definition |

**Stage summary.** Orchestration is currently spread across Fin, Zendesk configuration, and manual routing, with no runtime abstraction. The critical new products are the Entitlements Service (who can access what channel/SLA right now) and the Classification Service (one consistent tagger across all channels). Platform routing is entirely absent and must be net-new. Net-new products: Classification Service, Entitlements Service, Platform Merchant Directory, Escalation Policy Engine, Vulnerable Customer Triage Agent.

---

### Stage 3: Fuel (Data + Knowledge)

| Capability | Products | Build/Buy/Existing | Gap by 2030 | Dependencies |
|---|---|---|---|---|
| Customer context data | Customer 360; Agent Toolkit; **Customer 360 MCP (BUILD)** — MCP interface to Customer 360 for Fin and Agent Consultant | EXISTING + BUILD | Customer 360 is a data surface in Agent Toolkit; needs an MCP to be AI-addressable at low latency | Customer 360 data completeness |
| Payments data | Agent Toolkit; Agent Consultant; Fin; **Payments MCP (BUILD)** — payin/payout data served to Fin/Consultant | EXISTING + BUILD | Exists as agent tool but not as MCP; high latency today | MCP infra; data team capacity |
| Settlements and balances data | Agent Toolkit; Agent Consultant; Fin; **Settlements MCP (BUILD)**; **Balances MCP (BUILD)** | EXISTING + BUILD | Data latency is the critical blocker for Agent Consultant phase 2 and Fin settlement resolution | Settlements team data product; latency fix |
| Webhooks and error data | Agent Toolkit; **Datadog RUM Connector (BUILD on EXISTING Checkout)** — Datadog RUM is already collected by Engineering but not piped to Care tools; **VisionNotify Connector (BUILD on EXISTING Checkout)** — NOC incident data surfaced to Fin/Consultant for outage queries | EXISTING + BUILD | Datadog RUM and VisionNotify exist but are not connected to Care. Fin should detect incidents in-progress and adjust responses | Datadog RUM API access; VisionNotify owner alignment |
| Content coverage — customer-facing | Docs and Education Hub; **Knowledge Graph (BUILD)** — Reason ↔ Article ↔ Data edges; currently in design | EXISTING + BUILD | Knowledge Graph is vision; no authoritative gap matrix exists today | Reflex MCP; Taxonomy Registry |
| Content coverage — internal (SOPs and agent knowledge) | Docs and Education Hub; Agent Consultant; **SOP Management System (BUILD or BUY)** — structured SOP authoring, versioning, and Fin Procedure generation; current SOPs are Confluence pages | EXISTING + BUILD/BUY | SOPs are unstructured Confluence pages that Fin/Consultant cannot reliably parse. Need structured authoring with validation | Process Architect capacity; Fin Procedures spec |
| Content review cadence — reactive | Reflex; Docs and Education Hub; **Content Ops Agent (AGENTIC)** — scans Fin failure signals, drafts content updates, queues for Content team | EXISTING + AGENTIC | Weekly auto-review is vision; currently monthly and manual | Reflex MCP; Knowledge Graph |
| Content review cadence — proactive | Docs and Education Hub; **Product Release Content Workflow** — Engineering outputs technical docs and a support article draft at ship time; Content team reviews, tags to taxonomy Reason nodes, maps to product, publishes. Workflow: `02-workflows/product-release-content-workflow.md` | BUILD (process) | Not enforced today. Requires ship gate: release is not complete until documentation outputs exist. Prevents content gaps before they produce Fin failures or contacts. | Engineering ship process; Content team capacity; Knowledge Graph for coverage tracking |
| B2C knowledge base | Docs and Education Hub; Fin; Knowledge Graph | EXISTING | Net-new content build for wallet. Product exists, content does not | Wallet scope; B2C taxonomy |
| B2B Banking knowledge base | Docs and Education Hub; Fin; Knowledge Graph; **Sonar (EXISTING Checkout)** — AM/TAM knowledge tool owned outside Care; needs banking content and bidirectional flow with Care KB | EXISTING (Care + Checkout) | Sonar is not in the Care model today but is the AM/TAM knowledge tool. Banking content must land in both | Banking product scope; Sonar ownership alignment |

**Stage summary.** Fuel is the rate-limiting flywheel stage and has the largest product-mapping gap. Two structural issues: (1) the "MCP layer" is referenced as a single concept but is actually 5+ distinct data products (Customer 360, Payments, Settlements, Balances, Webhooks/Errors, Platform), each with its own owner and latency profile; (2) Sonar is in the 2028 critical path but is not listed as a Care product — ownership and content-sync are unresolved. Net-new: Customer 360 MCP, Payments MCP, Settlements MCP, Balances MCP, Datadog RUM Connector, VisionNotify Connector, Knowledge Graph, SOP Management System, Content Ops Agent. Adjacent products to bring into the model: Sonar.

---

### Stage 4: Agent Experience

| Capability | Products | Build/Buy/Existing | Gap by 2030 | Dependencies |
|---|---|---|---|---|
| B2B ticketing | Zendesk; **Zendesk Alternative (BUY decision pending)** — RFC in flight; outcome may reshape this row | EXISTING + BUY (TBC) | Pending build/buy/keep decision Q3–Q4 2026. Walled-permissions requirement is a key criterion for 500-agent scale | Zendesk RFC outcome |
| B2C ticketing | Zendesk (Checkout Consumer brand); **Walled Permissions Layer (BUILD)** — B2C vs B2B data isolation | EXISTING + BUILD | B2C brand exists but walled-permissions model is not designed. BPO access required by 2027 launch | Zendesk RFC; Consumer Duty |
| Agent data tooling | Agent Toolkit; Customer 360 | EXISTING | Toolkit exists; gap is data-source coverage (see Fuel) | MCPs across all data domains |
| AI suggested actions | Agent Consultant | EXISTING | Core product exists; needs NL query capability, broader data access, and HITL confirmation UX | Data MCPs; Fin Procedures |
| Natural language data queries | Agent Consultant; **Agent NL Query Interface (BUILD within Consultant)** | EXISTING + BUILD | UI surface in Zendesk sidebar is not built | Data MCPs |
| QA scoring and automation | Agent Consultant; Zendesk; **QA Criteria Service (BUILD)** — versioned QA rubric consumed by Consultant | EXISTING + BUILD | QA rubric is a document; needs to be a product so criteria drift is controlled | Consultant QA module |
| Jira integration | Zendesk; **Jira (EXISTING Checkout)** — not currently listed as a Care product | EXISTING (Care + Checkout) | Manual escalation today. Bi-directional integration Q1–Q2 2026 | Jira API access; Zendesk connector |
| Salesforce integration | Support platform; **Salesforce (EXISTING Checkout)** | EXISTING (Checkout) | Not listed as Care product. Tier-of-truth and CS handoff dependency | Commercial team alignment |
| Cross-team escalation integrations | Support platform; Jira; **Treasury API Connector (BUILD)**; **Card Processing Connector (BUILD)**; **Engineering Escalation API (BUILD)** | BUILD | Today these are manual Slack/email handoffs. One-connector-per-team pattern needed | Per-team API contracts |
| Skill-based routing | Zendesk; **Agent Skill Profile Service (BUILD)** — stores per-agent specialisms, languages, tier clearance; feeds routing engine | EXISTING + BUILD | Skill definitions live in Zendesk config; not a product. 500-agent scale needs a proper service | Agent specialism definitions |

**Stage summary.** Agent Experience is the most product-dense flywheel stage and has the largest pending strategic decision (Zendesk build/buy/keep). Three hidden products behind named capabilities: Walled Permissions Layer (B2C/B2B isolation — regulator-forced), Agent Skill Profile Service (to make skill-routing a product not a config screen), and the per-team cross-escalation connectors (Treasury, Card Processing, Engineering, AM/TAM via Salesforce). Jira and Salesforce need to be explicitly acknowledged as Care-adjacent products. Net-new: Walled Permissions Layer, Agent Skill Profile Service, QA Criteria Service, per-team Escalation Connectors, Agent NL Query Interface.

---

### Stage 5: Insight and Prevention

| Capability | Products | Build/Buy/Existing | Gap by 2030 | Dependencies |
|---|---|---|---|---|
| Contact reason reporting | Reflex | EXISTING | Quarterly/weekly cadence maturing; product exists | Taxonomy accuracy; Reflex MCP |
| Voice of Customer integration | Reflex; **VoC Aggregator (BUILD)** — merged support + NPS + research + in-app feedback stream feeding Reflex | EXISTING + BUILD | NPS and research data are not connected to Reflex today. A normalisation layer is required before the "merged view" is real | NPS data access; research tool access |
| AI action plans for Product | Reflex; Reflex MCP; **Action Plan Agent (AGENTIC within Reflex)** | EXISTING + AGENTIC | Vision is autonomous plan generation. Today manual by Support leaders | Reflex MCP; Product governance model |
| Autonomous triage and codebase fixes | Reflex; **Reflex Fix Agent (AGENTIC)** — generates PRs in product team repos; human-reviewed | EXISTING + AGENTIC | L0 today. Requires code access and engineering governance | Reflex MCP maturity; code access; eng governance |
| Content gap identification | Reflex; Docs and Education Hub; Knowledge Graph; Content Ops Agent | EXISTING + AGENTIC | Knowledge Graph is the authoritative source by 2030; not built today | Knowledge Graph Phase 2 |
| Product fix governance | Reflex; **Contact Reduction Scorecard (BUILD)** — per-domain target tracking product, published back to Product teams | EXISTING + BUILD | No shared scorecard exists. Without it, Reflex insights have no accountability loop | Product team commitments |
| Taxonomy accuracy | Reflex; Zendesk; Taxonomy Curator Agent | EXISTING + AGENTIC | Variable accuracy today. 2030 target >95% needs continuous monitoring | Reflex phase 1 |

**Stage summary.** Reflex is the anchor product and is well-scoped. Two accountability gaps: (1) there is no Contact Reduction Scorecard product that Product teams own — Reflex generates insight but insight without a scorecard does not close the loop; (2) VoC data (NPS, research) is referenced but the aggregation product is not defined. Three AI agents are implicit in the Reflex roadmap but should be named as discrete products: Action Plan Agent, Reflex Fix Agent, Content Ops Agent. Net-new: VoC Aggregator, Contact Reduction Scorecard, and the three Reflex-family agents.

---

### Stage 6: Governance

| Capability | Products | Build/Buy/Existing | Gap by 2030 | Dependencies |
|---|---|---|---|---|
| SLA monitoring | Zendesk; Success Plans; **Real-Time SLA Dashboard (BUILD)** — routing priority adjustment on SLA risk | EXISTING + BUILD | Real-time adjustment is not live; monitoring is post-hoc | Support model; SLA matrix |
| CSAT measurement | Zendesk; Fin; **CSAT Attribution Service (BUILD)** — splits CSAT cleanly between Fin, agent, and hybrid interactions | EXISTING + BUILD | Today CSAT is measured per-system; joined attribution is absent | Fin CSAT integration; B2C survey design |
| Consumer Duty and complaint handling | Zendesk; **Complaint Management System (BUILD or BUY)** — separate from ticketing; tracks 8-week SLA, FOS referrals, final response letters; **Consumer Duty Audit Trail (BUILD)** | BUILD/BUY | L0 today. Regulator-forced by 2027 wallet launch. Complaints are not tickets — different retention, different regulator exposure, different SLA | Legal & Compliance process design; Zendesk or alternative |
| Vulnerable customer identification | Fin; Agent Toolkit; **Vulnerability Detection Model (BUILD)** — NLU classifier embedded in Fin; **Vulnerability Specialist Queue (BUILD)** in Zendesk | BUILD | L0 today. Regulator-forced by 2027. Model must be embedded in Fin, not bolted on | Consumer Duty design; Fin model access |

**Stage summary.** Governance has the most severe regulatory clock: four capabilities move from L0 to L2+ at wallet launch 2027 and none have defined product owners today. Complaint Management is distinct from ticketing and is a build/buy decision in its own right (Zendesk has a weak complaints module; specialist tools like Aveni, Soteria, or RightIndem exist). Net-new: Real-Time SLA Dashboard, CSAT Attribution Service, Complaint Management System, Consumer Duty Audit Trail, Vulnerability Detection Model, Vulnerability Specialist Queue.

---

## Part 2: Stack — Product mapping per layer

### Layer 1: Channel

| Product | Role | Build/Buy/Existing |
|---|---|---|
| Fin | Primary AI channel across B2B, B2C, Platform | EXISTING |
| Zendesk (email + webform) | Email and web capture | EXISTING |
| Dashboard In-Product Support SDK | Contextual support in Dashboard surfaces | BUILD |
| Mobile Support SDK | In-app chat for consumer wallet | BUILD |
| Voice Platform | Phone channel (Aircall/Dialpad/Zendesk Talk/Amazon Connect) | BUY |
| IM/Slack Connector | Slack Connect / Teams into ticketing | BUILD on BUY |
| Platform Portal SDK | Fin inside ISV portals | BUILD |
| Complaint Intake Portal | Regulated B2C complaints | BUILD |

**Layer summary.** Today the Channel layer is Zendesk + Fin only. By 2030 it is 8 distinct products, 3 channel types are not started (voice, mobile, in-product SDK), and the build/buy mix is significant. The Channel layer is where 2027 regulatory risk concentrates.

---

### Layer 2: Customer AI Agent

| Product | Role | Build/Buy/Existing |
|---|---|---|
| Fin | Core autonomous resolution agent | EXISTING (BUY — Intercom) |
| Fin Procedures Library | Structured resolution flows | BUILD within Fin |
| Platform Embedded AI | Fin inside ISV portals | EXISTING (vision) |
| Vulnerable Customer Triage Agent | Protective routing out of self-service | AGENTIC BUILD |
| Agentic Commerce Verification Service | Verifies AI-initiated consumer purchases at dispute time | BUILD |

**Layer summary.** Fin is the single vendor. Two risks: Intercom Fin benchmarks at 55–65% autonomous resolution versus specialist platforms at 70–85% — platform capability is a constraint to monitor. Agentic Commerce Verification is not in the current model but is required by the 2027 wallet to distinguish user-authorised from AI-initiated purchases in disputes.

---

### Layer 3: Routing and Human Agent Experience

| Product | Role | Build/Buy/Existing |
|---|---|---|
| Zendesk (or successor) | Ticketing core | EXISTING + pending RFC |
| Classification Service | Channel-agnostic tagger | BUILD |
| Entitlements Service | Runtime tier/channel/SLA rules | BUILD |
| Escalation Policy Engine | Declarative Fin→human rules | BUILD |
| Agent Skill Profile Service | Agent-side skill data product | BUILD |
| Walled Permissions Layer | B2C/B2B data isolation | BUILD |
| Agent Toolkit | Sidebar Customer 360 + data | EXISTING |

**Layer summary.** Zendesk and Agent Toolkit are the only existing products. The 2030 vision ("auto-classified routing, 500 agents, walled permissions, cross-system escalation") requires 5 net-new products behind the ticketing core.

---

### Layer 4: Agent AI Assistant

| Product | Role | Build/Buy/Existing |
|---|---|---|
| Agent Consultant | AI suggestions + execution + QA | EXISTING |
| Agent NL Query Interface | In-Zendesk NL query UI | BUILD |
| QA Criteria Service | Versioned rubric | BUILD |
| Agent Coaching Agent | Real-time coaching based on QA signals | AGENTIC BUILD |

**Layer summary.** Agent Consultant is a single brand covering several discrete products that deserve naming for clarity. A missing capability: real-time agent coaching (not just retrospective QA) — an agentic product that supports agent development rather than just scoring performance.

---

### Layer 5: Integration and Data

| Product | Role | Build/Buy/Existing |
|---|---|---|
| Customer 360 | Context data product | EXISTING (Care) |
| Customer 360 MCP | AI-addressable interface | BUILD |
| Payments MCP | Payin/payout data for AI | BUILD |
| Settlements MCP | Settlements data | BUILD |
| Balances MCP | Balances (including banking from 2028) | BUILD |
| Platform Merchant Directory | Platform → merchant entity map | BUILD |
| Datadog RUM Connector | Error/webhook data | BUILD on EXISTING Checkout |
| VisionNotify Connector | NOC incident data | BUILD on EXISTING Checkout |
| User Management API Connector | Identity/auth queries | BUILD on EXISTING Checkout |
| Salesforce Connector | Tier of truth, CS context | BUILD on EXISTING Checkout |
| Jira Connector | Engineering escalation | BUILD on EXISTING Checkout |

**Layer summary.** The "Integration and Data" box hides the largest number of net-new products in the entire model — 10+. Each MCP/connector is a distinct product with its own owner, SLO, and roadmap. The current Care product list under-represents this layer by a factor of ~10.

---

### Layer 6: Knowledge

| Product | Role | Build/Buy/Existing |
|---|---|---|
| Docs and Education Hub | Customer-facing KB + support site + api-reference.checkout.com | EXISTING |
| Knowledge Graph | Reason↔Content↔Data edges | BUILD |
| SOP Management System | Structured SOP authoring + Fin Procedure generation | BUILD or BUY |
| Sonar | AM/TAM knowledge tool | EXISTING Checkout (not in Care model today) |
| Content Ops Agent | Continuous gap detection and draft proposal | AGENTIC BUILD |
| Taxonomy Registry | Canonical taxonomy as a product | BUILD |

**Layer summary.** The KB is modelled as a single product today but is architecturally three: customer-facing content, internal SOPs, and AM/TAM knowledge in Sonar. All three will need banking content by 2028 and there is no product owner for sync across them. Sonar must be brought into the Care model.

---

### Layer 7: Analytics and Insight

| Product | Role | Build/Buy/Existing |
|---|---|---|
| Reflex | Core insights product | EXISTING |
| Reflex MCP | Programmatic API layer | EXISTING (in delivery) |
| Action Plan Agent | Autonomous plan generator | AGENTIC BUILD |
| Reflex Fix Agent | Code-level PR generator | AGENTIC BUILD |
| VoC Aggregator | Merged support+NPS+research | BUILD |
| Contact Reduction Scorecard | Accountability surface for Product teams | BUILD |
| CSAT Attribution Service | Joined CSAT across Fin + agent | BUILD |

**Layer summary.** Reflex is well-scoped but three of its ambition statements (action plans, autonomous fixes, content ops) are agentic products in their own right. Scoring them as "Reflex features" understates the design work. VoC Aggregator and Contact Reduction Scorecard are structural gaps — insight without accountability does not reduce contacts.

---

### Layer 8: Operations and Governance

| Product | Role | Build/Buy/Existing |
|---|---|---|
| Zendesk SLA + QA | Current core | EXISTING |
| Real-Time SLA Dashboard | Dynamic priority on SLA risk | BUILD |
| Complaint Management System | Regulated complaint handling | BUILD or BUY |
| Consumer Duty Audit Trail | Regulated outcome logging | BUILD |
| Vulnerability Detection Model | NLU classifier in Fin | BUILD |
| Vulnerability Specialist Queue | Trained agent pool | BUILD + Ops |
| Workforce Management (WFM) | Scheduling, capacity planning — not in Care model today | BUY (Assembled, Playvox, Verint) |

**Layer summary.** Governance is the most regulator-exposed layer and has the largest L0 population today. WFM (workforce management) is missing from the current model but is essential at 500-agent scale — most Care orgs of this size use Assembled, Playvox WFM, or Verint. This is a build/buy gap for 2027–2028.

---

## Part 3: New products to define

Consolidated list of products not currently named in the Care model that need scoping.

### Data / Integration layer
1. **Taxonomy Registry** — versioned, API-addressable taxonomy (Input, all stages)
2. **Classification Service** — channel-agnostic tagger (Orchestration)
3. **Entitlements Service** — runtime tier/channel/SLA rules (Orchestration)
4. **Customer 360 MCP** — AI-addressable context (Fuel)
5. **Payments MCP** (Fuel)
6. **Settlements MCP** (Fuel)
7. **Balances MCP** (Fuel, Banking 2028)
8. **Datadog RUM Connector** (Fuel)
9. **VisionNotify Connector** (Fuel)
10. **Salesforce Connector** (Orchestration + Agent Experience)
11. **Jira Connector** (Agent Experience)
12. **Platform Identity Service** (Input)
13. **Platform Merchant Directory** (Orchestration)
14. **User Management API Connector** (Fuel)

### Knowledge layer
15. **Knowledge Graph** — Reason↔Content↔Data edges (Fuel, Insight)
16. **SOP Management System** — structured authoring + Fin Procedure generation
17. **Sonar** (existing at Checkout) — needs bringing into Care model for banking

### Channel layer
18. **Dashboard In-Product Support SDK** (Input B2B)
19. **Mobile Support SDK** (Input B2C)
20. **Voice Platform** — buy decision (Input B2B Premium + B2C)
21. **IM/Slack Connector** (Input B2B)
22. **Platform Portal SDK** (Input Platform)
23. **Complaint Intake Portal** (Governance, B2C)

### Agent Experience
24. **Walled Permissions Layer** (B2B/B2C isolation)
25. **Agent Skill Profile Service** (skill-based routing)
26. **Agent NL Query Interface** (Agent Consultant UI)
27. **QA Criteria Service** (versioned QA rubric)
28. **Per-team Escalation Connectors** — Treasury, Card Processing, Engineering
29. **Workforce Management (WFM)** — buy (Assembled / Playvox / Verint)

### Governance
30. **Complaint Management System** — build or buy; distinct from ticketing
31. **Consumer Duty Audit Trail**
32. **Vulnerability Detection Model** — NLU classifier embedded in Fin
33. **Vulnerability Specialist Queue** (Zendesk config + ops)
34. **Real-Time SLA Dashboard**
35. **CSAT Attribution Service**
36. **Agentic Commerce Verification Service** — 2027 wallet liability capability

### Insight
37. **VoC Aggregator** (Insight)
38. **Contact Reduction Scorecard** — Product team accountability surface
39. **Escalation Policy Engine** — declarative Fin→human rules

### Agentic products (discrete AI agents with defined scope)
40. **Taxonomy Curator Agent** — proposes taxonomy changes (Input)
41. **Content Ops Agent** — drafts content updates from gaps (Fuel)
42. **Action Plan Agent** — generates weekly product-fix plans (Insight)
43. **Reflex Fix Agent** — generates PRs in product team repos (Insight)
44. **Vulnerable Customer Triage Agent** — protective routing (Orchestration/Governance)
45. **Agent Coaching Agent** — real-time agent coaching from QA signals (Agent AI Assistant)

---

## Part 4: Cross-cutting observations

**1. The current Care product list is 10 products; the 2030 model requires ~45.** The 4.5x expansion is not evenly distributed: the Integration/Data layer alone adds 10+ products, and Governance adds 7. The current model under-represents these two layers specifically because they are largely invisible from the flywheel narrative. Every unnamed product is an unowned product.

**2. "Care product" is conflated with "product Care builds."** Several products in the 2030 model already exist at Checkout but sit outside the Care product set (Salesforce, Jira, Sonar, Datadog RUM, VisionNotify, User Management API). Treating them as external integrations rather than as Care-managed surfaces means SLAs, roadmap influence, and data contracts are unowned. A "Care-adjacent product" register with a named counterpart PM for each is the structural fix.

**3. Agentic products are hidden inside umbrella brands.** Reflex, Fin, and Agent Consultant each carry multiple distinct AI agents (Reflex = reporting + Action Plan Agent + Fix Agent + Content Ops Agent + Taxonomy Curator; Fin = autonomous resolver + Vulnerable Customer Triage Agent; Agent Consultant = suggestion + execution + QA + Coaching). Naming them discretely clarifies scope, accelerates design decisions, and lets engineering ownership be split without breaking the user-facing brand.

**4. Regulatory products are not on the 2026 roadmap but must launch in 2027.** Six Governance/B2C products (Complaint Management System, Consumer Duty Audit Trail, Vulnerability Detection Model, Vulnerability Specialist Queue, Complaint Intake Portal, Voice Platform) are L0 today and must be L2+ at wallet launch. None appear in current 2026 deliverables as named products. Consumer Duty compliance depends on products that have no scope documents.

**5. The Taxonomy Registry and Knowledge Graph are single points of leverage.** Every flywheel stage depends on them: Input (canonical reasons), Orchestration (classification targets), Fuel (content coverage matrix), Agent Experience (skill routing), Insight (gap detection), Governance (reason-level SLAs). Neither exists as a product today. Prioritising these two ahead of individual MCPs or per-capability work would unlock more of the roadmap simultaneously than any other single investment.

**6. Build vs buy decisions are concentrated in three areas, all 2027-forced.** Zendesk (RFC in flight), Voice Platform, and Complaint Management are three independent buy decisions, all with regulatory or SLA consequences at wallet launch. Running them as a single 2026 "support platform buy cycle" rather than three sequential decisions would reduce vendor integration overhead and give commercial leverage.

**7. Fuel is the critical path but has the most diffused ownership.** MCPs for Payments, Settlements, Balances, and Customer 360 depend on data teams outside Care. If any of the four slips, Agent Consultant and Fin resolution rates plateau. A dedicated "Care Data Product" workstream with its own PM is the organisational gap that matches the product gap.
