# Care Capability Model (2026–2030)

> **Related**: [Care Product Flywheel](care-product-model.md) · [Support Scale Principles](support-scale-principles.md) · [2026 Deliverables](../../2026%20deliverables.md)

This document defines the capability model for scaling Care from the current 2026 state to the 2030 vision. For each flywheel stage, it maps the discrete capabilities required, which Care products deliver them, how they mature year by year, the metric they drive, and what must be true before they can advance.

The flywheel model and strategic principles live in the documents above. This document is the operational translation: what we need to build, in what order, and by when.

---

## Care products

The following named products deliver capabilities across the flywheel. Each appears in the capability tables below using these names consistently.

| Product | What it does | Flywheel stages | 2026 state | 2030 vision |
|---|---|---|---|---|
| **Fin** | Customer-facing AI Agent (Intercom Fin) — first-line self-service resolution via Dashboard, email, and mobile | Input, Orchestration, Handle | Partially deployed; email + Dashboard contextual in progress | Majority channel across B2B, B2C, and Platform; resolves 80%+ of contacts autonomously |
| **Agent Toolkit** | Zendesk sidebar panel — surfaces Customer 360 data, payments context, and alerts to human agents during ticket handling | Agent Experience, Fuel | Merchant context (entity, processing profile, balances) surfacing in Q1 | Full data access across all customer types; proactive anomaly alerts |
| **Agent Consultant** | AI layer within Zendesk — suggests actions, executes permitted tasks autonomously, and requests agent approval for actions requiring human-in-the-loop confirmation; also performs internal QA | Agent Experience | Foundation phase — data retrieval and SOP-based suggestions live; NL queries and QA in delivery | Agents get AI-suggested action on every ticket; 90%+ of tasks automated or AI-assisted; autonomous for permitted actions, HITL for sensitive ones |
| **Reflex** | Support insights engine — analyses contact data to identify root causes and surface them to Product and Content teams; evolves by 2030 into an autonomous insights agent that triages contact drivers, generates action plans, and executes targeted fixes in relevant product team codebases | Insight & Prevention | Early delivery — on-demand insights dashboard live; MCP in development | Autonomous agent: weekly action plans generated, triage handled, fixes executed; human team reviews and approves |
| **Reflex MCP** | Programmatic API layer for Reflex — enables AI agents and tools to query support insights directly; unlocks AI-to-AI insight sharing | Insight & Prevention | In development; planned Q3 2026 | Standard interface for all internal AI tooling to query contact drivers |
| **Customer 360** | Centralised customer context data aggregated across all Checkout sources — entity structure, processing profile, balances, configuration — covering merchants, platforms, and consumers | Fuel, Orchestration | Merchant entity + processing profile live in Q1; balances and advanced data in progress | Real-time context for all customer types; proactive anomaly detection; low latency |
| **Zendesk** | Ticketing system for human agent handling — routing, SLA management, QA, and integrations | Agent Experience, Governance | Live for B2B; basic routing; limited SLA differentiation | Scaled for B2B and B2C; automated classification, routing, and SLA enforcement |
| **Platform Embedded AI** | Fin AI component embedded in Platform portals — enables Platforms to resolve sub-merchant queries using Fin before escalating to Checkout | Input, Orchestration | Vision only; depends on 2026 Platform identification foundations | Platforms self-serve the majority of sub-merchant queries; Checkout handles complex escalations only |
| **Success Plans** | Merchant support tier model — Standard, Enterprise, Premium — defining channel access, SLAs, and service features per segment | Orchestration, Governance | Phase I rolling out 2026; Standard live Q2, Enterprise/Premium Q3 | Full B2B and B2C tiering; dynamic re-routing on tier change; 90%+ CSAT |
| **Docs and Education Hub** | Self-service knowledge covering customer-facing content (support.checkout.com, checkout.com/docs, api-reference.checkout.com) and internal agent knowledge (SOPs, process guides, internal knowledge base) | Fuel, Fix | ~60% taxonomy coverage; reactive monthly updates | 90%+ taxonomy coverage; AI-proposed updates; weekly human approval cycle |

---

## How to read this document

Each flywheel stage contains a capability table with the following columns:

- **Capability**: A discrete, named capability the Care product must possess
- **Care Products**: The named products above that deliver this capability
- **2026 → 2030**: Year-by-year maturity — each cell leads with the product name doing the work, then describes what changes that year
- **Metric**: The primary measure of this capability's performance
- **Blocker / Dependency**: What must be resolved before this capability can advance

### Maturity scale

| Level | Label | Definition |
|---|---|---|
| **L0** | None | Does not exist |
| **L1** | Ad hoc | Exists but inconsistent, manual, or partial coverage |
| **L2** | Defined | Consistent process or tooling, limited coverage |
| **L3** | Managed | Broad coverage, measured, actively improving |
| **L4** | Optimised | Automated, self-improving, high coverage, stable |

Cells show the maturity level achieved **by end of that year**.

---

## Stage 1: Input

**Strategic intent**: Capture every support contact with the right query classification and through the right channel. Input quality determines the accuracy of everything downstream — orchestration, AI resolution, and insight generation. By 2030, the taxonomy is LLM-driven and updated quarterly; channels cover B2B, B2C, and Platform with Fin as the primary entry point across all.

| Capability | Care Products | 2026 | 2027 | 2028 | 2029 | 2030 | Metric | Blocker / Dependency |
|---|---|---|---|---|---|---|---|---|
| **B2B query taxonomy** | Reflex, taxonomy management process | L2 — **Reflex**: LLM-assisted analysis used in manual reviews; 13 case types, 41 issue types refreshed 6–12 monthly | L3 — **Reflex**: quarterly LLM-driven taxonomy audit; gaps surfaced for Content team review | L3 — Taxonomy extended: banking reason types added (balances, interest, yield) | L3 — **Reflex**: mature coverage across full B2B product set | L4 — **Reflex**: fully LLM-driven, self-auditing quarterly; changes proposed and approved without manual trigger | Taxonomy coverage % vs contact volume | Reflex MCP (Q3 2026) to enable LLM-driven automation |
| **B2C query taxonomy** | Reflex, taxonomy management process | L0 — Does not exist | L2 — Taxonomy defined before wallet launch: balance disputes, card management, rewards, cashback, vulnerable customer escalation | L3 — Banking product reason types added | L3 — **Reflex**: stable B2C taxonomy; measured coverage | L4 — **Reflex**: LLM-driven, B2C-specific quarterly refresh | B2C taxonomy coverage % | Wallet product definition required mid-2026 before taxonomy design begins |
| **B2B Banking taxonomy** | Reflex, taxonomy management process | L0 | L0 | L2 — Taxonomy defined at banking product launch: balance management, interest/yield, working capital, treasury | L3 — Coverage improves; AM/TAM knowledge added | L4 — **Reflex**: LLM-driven | Banking taxonomy coverage % | Banking product scope definition required 2027 |
| **Support channels — B2B** | Fin, Email, Dashboard contextual | L2 — **Fin**: Dashboard + email partially deployed; Dashboard contextual answers live Q1; webform still primary for many merchants | L3 — **Fin**: primary B2B channel; webform retired Q3; Dashboard contextual live; **Success Plans**: phone available for Premium merchants | L3 — **Success Plans**: phone extended to Enterprise; IM/Slack piloted; live chat with human agent available for eligible tiers | L3 — IM/Slack live across eligible tiers; live chat fully operational | L4 — **Fin**: majority of B2B volume; all channels live (email, AI Agent, live chat, IM, phone); webform fully deprecated | Channel mix %; Fin resolution rate | Fin CC handoff capability required before webform retirement (Q3 2026) |
| **Support channels — B2C** | Fin, Mobile app, Phone | L0 | L2 — **Fin**: deployed on B2C at wallet launch; phone live from day one (required at launch); mobile app chat channel defined | L3 — In-app support and mobile app chat embedded in product UX; **Success Plans**: B2C tiered channel access live | L3 — Stable | L4 — **Fin**: AI-first for all B2C channels (mobile app chat, phone); support embedded in product experience | B2C channel mix %; B2C AI resolution rate | Fin B2C configuration; Consumer Duty requirements defined before launch |
| **Support channels — Platform** | Platform Embedded AI, Fin, Zendesk | L1 — Platform identification in webform begins Q1; no Fin context for Platform contacts yet | L2 — **Fin**: Platform identification live; sub-merchant context surfaced in Zendesk; Platform-specific agent queue | L3 — **Platform Embedded AI**: Fin component embedded in Platform portals; Platforms self-serve first | L3 — **Platform Embedded AI**: stable; coverage improves across Platform portfolio | L4 — **Platform Embedded AI**: resolves majority of sub-merchant queries; Checkout handles complex escalations only | Platform routing accuracy %; Platform ticket volume to Checkout | Platform Embedded AI requires ISV commercial agreement and API access (2027) |
| **Taxonomy automation** | Reflex | L1 — Manual reviews monthly; some LLM assistance in analysis | L2 — **Reflex**: quarterly LLM-driven taxonomy audit; new reason gaps surfaced automatically | L3 — **Reflex**: automated gap detection; draft new reason types proposed for Content review | L3 — **Reflex**: automated across B2B + B2C | L4 — **Reflex**: self-auditing; taxonomy changes proposed and approved without manual trigger | Taxonomy accuracy %; reason tagging % | Reflex MCP (Q3 2026); Content team capacity for review and approval |

---

## Stage 2: Orchestration

**Strategic intent**: Route every contact to the right resolution channel, first time, with no human involvement for standard queries. By 2030, AI handles 80%+ of B2B contacts and the majority of B2C contacts, with human agents reserved for complex issues and premium customers. Routing accuracy eliminates unnecessary escalations and reassignments.

| Capability | Care Products | 2026 | 2027 | 2028 | 2029 | 2030 | Metric | Blocker / Dependency |
|---|---|---|---|---|---|---|---|---|
| **Auto-classification** | Fin, Support platform | L2 — **Fin**: classification live for Dashboard and email contacts; support platform applies manual routing for edge cases and complex contacts | L3 — **Fin**: classification across all B2B channels + B2C at wallet launch; any contact escalated to a human agent is auto-classified to taxonomy before routing | L3 — Banking reason types classifiable; auto-classification applies across all segments | L3 — High accuracy; measured per reason type | L4 — Auto-classification at >95% accuracy across all channels and segments; self-improving; zero manual routing for standard contacts | Classification accuracy %; first assignment time | B2C taxonomy (2027); banking taxonomy (2028) must exist before classification can extend |
| **Channel eligibility rules** | Customer 360, Success Plans, Support platform | L1 — No eligibility rules live at year start; **Success Plans** rules engine starts Q2 | L2 — **Success Plans**: Standard/Enterprise/Premium B2B rules live; B2C channel rules defined at wallet launch | L3 — Banking merchant eligibility added | L3 — **Success Plans**: stable across all segments | L4 — **Customer 360**: real-time eligibility; adapts dynamically on merchant lifecycle events; support platform uses customisable company and individual customer fields to drive routing logic | Routing accuracy %; routed ticket acceptance rate | Customer 360 data completeness; Support model (Q2–Q3 2026) |
| **Merchant tier routing** | Success Plans, Zendesk, Fin | L1 — **Success Plans** rolling out; Standard live Q2, Enterprise/Premium Q3 | L2 — **Success Plans**: full B2B routing live; B2C model defined | L3 — B2B Banking tier routing added | L3 — Stable | L4 — **Success Plans**: automated re-routing on tier change | % contacts routed correctly first time; reopen rate | Success Plans rollout (Q2–Q3 2026) |
| **Platform routing** | Platform Embedded AI, Zendesk, Fin | L1 — **Fin**: Platform identification starts Q1; context surfacing in **Zendesk** | L2 — **Fin**: sub-merchant context live; **Zendesk**: Platform-specific agent queue active | L3 — **Platform Embedded AI**: reduces direct Checkout contacts from Platform sources | L3 — Stable | L4 — **Platform Embedded AI**: automated escalation to Checkout for complex cases only | Platform routing accuracy %; skip/reassignment rate for Platform tickets | Platform Embedded AI (2027); commercial agreements with Platforms |
| **AI-to-human escalation logic** | Fin, Zendesk | L2 — **Fin**: basic handoff logic; escalates to **Zendesk** when unresolved | L3 — **Fin**: structured escalation criteria per reason type and merchant level; context passed on handoff | L3 — Banking escalation criteria added | L3 — Measured and improving | L4 — **Fin**: dynamic escalation threshold; adjusts based on resolution confidence score | Escalation rate; reopen rate post-escalation | Fin procedures (Q2 2026) to define structured escalation criteria |
| **B2C routing** | Fin, Success Plans | L0 | L2 — **Fin**: B2C routing live at wallet launch; **Success Plans**: B2C channel and SLA model defined | L3 — Routing covers banking product contacts | L3 — Stable | L4 — **Fin**: AI-first routing for all B2C; human escalation only for complex or regulated contacts | B2C routing accuracy %; B2C AI resolution rate | B2C taxonomy and wallet product definition (2026) |
| **SLA rules by merchant level and reason type** | Zendesk, Success Plans | L1 — **Zendesk**: basic SLAs configured; not differentiated by reason type | L2 — **Success Plans**: SLAs defined per merchant level; B2C SLAs defined at wallet launch | L3 — Banking-specific SLAs added | L3 — **Zendesk**: automated SLA breach alerting | L4 — **Zendesk**: SLA performance feeds routing priority dynamically | SLA adherence % by merchant level; time to first response | Support model completion (Q3 2026); B2C regulatory SLA requirements |

---

## Stage 3: Fuel (Data + Knowledge)

**Strategic intent**: Provide AI and human agents with accurate, complete, low-latency data and knowledge at the point of resolution. Fuel is the rate-limiting factor for every other flywheel stage — without it, AI resolution rates plateau, agent handle times stay high, and Reflex insights lack precision. By 2030, data coverage spans all Checkout product lines via MCPs, and content covers 90%+ of the taxonomy with weekly AI-assisted updates.

| Capability | Care Products | 2026 | 2027 | 2028 | 2029 | 2030 | Metric | Blocker / Dependency |
|---|---|---|---|---|---|---|---|---|
| **Customer context data** | Customer 360, Agent Toolkit | L2 — **Customer 360**: entity structure, processing profile, and balances surfaced in **Agent Toolkit** (Q1); high-level context added to **Fin** (Q2) | L3 — **Customer 360**: full context available to **Fin** + agents; B2C consumer data added | L3 — **Customer 360**: banking product data (merchant balances, interest accrual, yield) added | L3 — Stable across all customer types | L4 — **Customer 360**: real-time context; proactive alerts on anomalies surfaced in **Agent Toolkit** | Data coverage vs taxonomy %; agent context adoption rate per ticket | Entity data API availability; data latency fix required for real-time use |
| **Payments data** | Agent Toolkit, Agent Consultant, Fin | L2 — **Agent Toolkit**: payin data accessible; some latency; **Agent Consultant**: payment queries via data retrieval tool | L3 — **Fin**: low-latency payin data via MCP; payment query resolution improves | L3 — Stable | L3 — High accuracy | L4 — **Fin** and **Agent Consultant**: real-time, fully queryable via natural language | Fin resolution rate for payment queries | MCP infrastructure; data team capacity |
| **Settlements and balances data** | Agent Toolkit, Agent Consultant, Fin | L1 — **Agent Toolkit**: data available but high latency; not suitable for AI use yet | L2 — **Agent Consultant**: low-latency access via MCP live (phase 2); **Agent Toolkit**: settlement data accessible | L3 — **Fin**: resolves balance queries autonomously for B2B; banking balance data added | L3 — Stable | L4 — **Fin** and **Agent Consultant**: real-time queryable; settlement queries fully autonomous | Agent query success rate for settlement/balance issues | Data latency fix is the critical blocker — gates Agent Consultant phase 2 |
| **Webhooks and error data** | Agent Toolkit | L1 — Datadog RUM API referenced but not connected to Agent tools or Fin | L2 — **Agent Toolkit**: webhook and error data accessible; **Fin**: uses error data for outage queries | L3 — Stable | L3 — **Agent Toolkit**: proactive alerting from error data surfaced to agents | L4 — **Fin**: error data enables proactive merchant notifications; **Agent Toolkit**: real-time error context | Fin resolution rate for technical and outage queries | Datadog RUM API integration; data access permissions from Engineering |
| **Content coverage — customer-facing** | Docs and Education Hub | L2 — Coverage ~60% of taxonomy; reactive updates monthly; **Education Hub** live Q2 | L3 — 80%+ coverage; quarterly AI-driven gap analysis; B2C wallet content added | L3 — **Docs and Education Hub**: banking product docs and guides added | L3 — Weekly gap analysis and updates | L4 — 90%+ coverage; **Reflex** proposes content updates; Content team approves weekly | Content coverage % vs taxonomy; Fin resolution rate attributed to content | Reflex content gap analysis (Q2+); Content team capacity |
| **Content coverage — internal (SOPs and agent knowledge)** | Docs and Education Hub, Agent Consultant | L2 — SOPs exist for known reason types; not systematically complete; **Agent Consultant** uses SOPs for suggestions | L2 — **Agent Consultant**: Fin Procedures added (Q2); **Reflex**: gaps identified and flagged | L3 — SOPs cover B2B banking reason types; AM/TAM knowledge base updated | L3 — High coverage; auto-reviewed quarterly | L4 — 90%+ SOP coverage; **Agent Consultant** validates accuracy against contact outcomes | SOP coverage % vs taxonomy; agent escalation rate for "no SOP" | Reflex gap analysis; Process Architect capacity |
| **Content review cadence** | Reflex, Docs and Education Hub | L1 — Manual, reactive monthly reviews via Fin conversation analysis and agent knowledge captures | L2 — **Reflex**: quarterly AI-assisted gap analysis; **Docs and Education Hub**: Content team reviews gaps | L3 — **Reflex**: monthly AI-driven review across B2B + B2C | L3 — Weekly review cycle | L4 — **Reflex**: continuous AI-driven gap detection; weekly human approval cycle in **Docs and Education Hub** | Time from gap identification to published content; Fin accuracy delta | Reflex MCP (Q3 2026); Content team review process |
| **B2C knowledge base** | Docs and Education Hub, Fin | L0 | L2 — **Docs and Education Hub**: wallet product docs, Fin content, and agent SOPs defined at launch | L3 — Coverage improves via **Reflex** gap analysis | L3 — 80%+ B2C taxonomy coverage | L4 — 90%+ coverage; **Reflex**-driven updates; LLM-proposed content | B2C Fin resolution rate; B2C content coverage % | Wallet product scope defined mid-2026 for content build to begin |
| **B2B Banking knowledge base** | Docs and Education Hub, Fin | L0 | L0 | L2 — **Docs and Education Hub**: banking product docs and agent SOPs defined at launch | L3 — Coverage improves; AM/TAM knowledge updated in Sonar | L4 — Full coverage; **Reflex**-driven updates | Banking reason type Fin resolution rate | Banking product scope required 2027 before content build |

---

## Stage 4: Agent Experience

**Strategic intent**: Reduce the cost and time of every human-handled ticket by giving agents accurate data, AI-suggested actions, and automated workflows. By 2030, 90% of agent tasks are automated or AI-assisted, handle time is below target thresholds, and agents focus exclusively on complex and VIP contacts. Human agents are a premium product, not a first-line cost. The support platform must scale to ~500 agents across B2B and B2C by 2030, with strict data separation between segments. The platform architecture is modular and build-around: our AI agents, data sources, and integrations connect to the platform without being constrained by it. The platform must support customisable company and individual customer fields (for routing and context), a flexible tagging system for taxonomy and analytics, and customisable ticket fields.

| Capability | Care Products | 2026 | 2027 | 2028 | 2029 | 2030 | Metric | Blocker / Dependency |
|---|---|---|---|---|---|---|---|---|
| **B2B ticketing** | Support platform | L2 — Support platform live for B2B; basic routing; no skill-based assignment yet | L3 — Skill-based routing live; SLA rules per merchant level; Jira integration live | L3 — Banking ticket categories added; AM/TAM escalation flows updated | L3 — Stable | L4 — Full 7-step agent workflow: ticket creation + enrichment → auto-classification + routing → agent assignment with Consultant suggestion → agent approves and acts → reply to customer → cross-team escalation via Jira or custom API integrations (Treasury, Engineering, other business teams) → ticket close triggers Reflex data feed; automated SLA management | Tickets handled within SLA %; AHT | Support model rollout (Q3 2026); support platform configuration |
| **B2C ticketing** | Support platform | L0 | L2 — Support platform B2C configuration live at wallet launch; Consumer Duty complaint handling process live; B2C agents and B2B agents are virtually separated — walled permissions model ensures B2C agents (including any BPO) cannot access B2B customer data | L3 — Banking complaint flows added; vulnerable customer flags surfaced; multi-tenancy model stable | L3 — Stable | L4 — Full 7-step agent workflow applies across B2B and B2C; automated classification across both; data isolation enforced at platform level | B2C AHT; complaint resolution time | Support platform B2C configuration; Consumer Duty and complaint handling process design (2026); walled permissions design |
| **Agent data tooling** | Agent Toolkit, Customer 360 | L2 — **Agent Toolkit**: Customer 360 data in sidebar (Q1); payment and user data accessible | L3 — **Agent Toolkit**: settlements, balances, and webhooks accessible; **Customer 360**: consumer data added | L3 — **Agent Toolkit**: banking product data added | L3 — Stable | L4 — **Agent Toolkit**: agents access any data source from sidebar; proactive context surfaced before agent reads ticket | Agent tool adoption rate per ticket; time to data retrieval | Data latency fix for settlements/balances is critical path for phase 2 |
| **AI suggested actions** | Agent Consultant | L2 — **Agent Consultant**: SOP-based next best action suggestions live (Q1); human reviews and sends | L3 — **Agent Consultant**: two-mode operation — (1) autonomous for permitted actions (data lookups, approved API calls); (2) human-in-the-loop: requests agent confirmation before executing sensitive actions | L3 — **Agent Consultant**: banking-aware action suggestions added | L3 — High adoption | L4 — **Agent Consultant**: every ticket gets AI-suggested action; 90%+ acceptance rate; autonomous actions cover majority of routine tasks | AI suggestion acceptance rate; AHT reduction | Agent Consultant phase 2 (Q2 2026); data access completeness |
| **Natural language data queries** | Agent Consultant | L1 — Basic data views only; no natural language interface | L2 — **Agent Consultant**: NL queries live across Payments, Settlements, Balances, Webhooks, User Management (Q2) | L3 — **Agent Consultant**: banking data queryable via NL | L3 — High accuracy | L4 — **Agent Consultant**: any data source queryable; zero training required for new agents | Query accuracy rate; agent NL query volume | Production data access for settlements/balances — critical blocker |
| **QA scoring and automation** | Agent Consultant, Zendesk | L1 — Manual QA sampling in **Zendesk**; no AI involvement | L2 — **Agent Consultant**: QA capability live; AI scores tickets against defined criteria; **Zendesk**: QA results stored and reported | L3 — **Agent Consultant**: QA criteria cover B2C contacts; banking QA criteria added | L3 — **Agent Consultant**: high coverage; automated sampling triggers | L4 — **Agent Consultant**: automated QA on 100% of human-handled tickets; human QA team reviews exceptions and calibrates | QA score % by agent and reason type; automated QA coverage % | QA criteria must be defined and stable before automation is reliable |
| **Jira integration** | Zendesk | L1 — Manual escalation to Jira; no sync | L2 — **Zendesk**: bi-directional Zendesk ↔ Jira integration live (Q1/Q2 2026) | L3 — **Zendesk**: engineering bug routing automated | L3 — Stable | L4 — **Zendesk**: automated Jira ticket creation on defined trigger criteria | Escalation-to-Jira time; engineering resolution feedback rate | Jira API access; Zendesk integration configuration |
| **Salesforce integration** | Support platform | L1 — Manual handoff for SF-owned contacts | L2 — Support platform: Salesforce integration scoped (TBC — depends on commercial team alignment) | L3 — Bi-directional sync live if confirmed | L3 — Stable if live | L4 — Automated routing for SF-owned contacts | SF ticket handoff time; duplicate handling rate | Commercial team alignment on shared ticket ownership; TBC |
| **Cross-team escalation integrations** | Support platform | L1 — Manual escalation to other teams (Treasury, Card Processing, Engineering); no trackable integration | L2 — Jira integration live (Q1/Q2 2026); escalation to Engineering trackable in support ticket | L3 — Custom API integrations to key internal teams (Treasury, Card Processing) available; agent can escalate and track in-ticket | L3 — Stable; agents can read/write to external team systems from support ticket | L4 — Full cross-team escalation via Jira and custom API integrations; agent updates customer from a single ticket view; escalation status tracked without leaving support platform | Cross-team escalation time; escalation resolution rate | Jira integration (Q1/Q2 2026); API integrations per team scoped and built |
| **Skill-based routing** | Zendesk | L1 — Basic queue routing; no skill matching | L2 — **Zendesk**: agent specialisms defined; skill-based routing live (Q2–Q4 2026) | L3 — **Zendesk**: banking specialist queue added | L3 — Stable | L4 — **Zendesk**: dynamic routing based on agent availability, skill, and SLA urgency | First assignment acceptance rate; reassignment rate | Agent specialism definitions; Zendesk routing configuration |

---

## Stage 5: Insight and Prevention

**Strategic intent**: Convert every support contact into an actionable signal. By 2030, Reflex operates as an autonomous insights agent — producing weekly action plans for Product and Content teams, triaging contact drivers, and executing targeted fixes directly in product team codebases. The goal is not to handle contacts faster — it is to eliminate the contacts that should not happen.

| Capability | Care Products | 2026 | 2027 | 2028 | 2029 | 2030 | Metric | Blocker / Dependency |
|---|---|---|---|---|---|---|---|---|
| **Contact reason reporting** | Reflex | L2 — **Reflex**: AI-powered contact analysis dashboard live (Q1); quantified recurring issues surfaced for Product prioritisation | L3 — **Reflex**: reporting covers B2B + B2C; weekly cadence | L3 — **Reflex**: banking reason types included | L3 — Stable; high tagging accuracy | L4 — **Reflex**: fully automated weekly reports; no manual curation required | Contact reason tagging accuracy %; Product review rate of Reflex outputs | Zendesk taxonomy tagging accuracy (Input stage dependency) |
| **Voice of Customer integration** | Reflex | L1 — NPS and support data exist separately; no merged view | L2 — **Reflex**: merged support + NPS + research view (Q2); proactive spike analysis dashboard | L3 — **Reflex**: B2C VoC added (in-app feedback, CSAT, NPS) | L3 — Stable | L4 — **Reflex**: full 360 VoC; automated correlation between contact drivers and NPS movement | NPS-to-contact correlation %; proportion of product prioritisation decisions driven by merged VoC | NPS data access; Reflex phase 2 delivery (Q2 2026) |
| **AI action plans for Product** | Reflex, Reflex MCP | L1 — Manual output: Support leaders present contact themes to Product quarterly | L2 — **Reflex MCP** (Q3): AI action plans for top 5 B2B contact drivers; queryable by AI tools | L3 — **Reflex**: B2C and banking action plans added; Product teams receive weekly briefing | L3 — Reviewed and actioned weekly | L4 — **Reflex**: automated weekly action plans; Product teams triage and commit on a defined cadence | % of top contact drivers addressed by a product fix per quarter | Reflex MCP (Q3 2026); Product team governance model for consuming Reflex outputs |
| **Autonomous triage and codebase fixes** | Reflex | L0 | L0 | L1 — **Reflex**: capability scoped and designed; initial autonomous actions identified | L2 — **Reflex**: autonomous triage of defined contact driver categories; targeted codebase fix PRs generated for human review | L4 — **Reflex**: fully autonomous insights agent — triages contact drivers, generates action plans, and executes targeted fixes in relevant product team codebases; human team approves | % of contact drivers resolved via autonomous Reflex action; time from contact spike to fix deployed | Reflex MCP maturity; Product team governance and code access required |
| **Content gap identification** | Reflex, Docs and Education Hub | L1 — Manual identification via Fin conversation review; monthly | L2 — **Reflex**: surfaces content gaps automatically; **Docs and Education Hub** Content team reviews quarterly | L3 — **Reflex**: weekly content gap output | L3 — Gaps resolved within defined SLA | L4 — **Reflex**: automated weekly brief to Content team; AI-suggested draft content; human approved | Time from gap identification to published content | Reflex phase 2 (Q2 2026); Content team review process |
| **Product fix governance** | Reflex | L1 — No formal process; ad hoc escalation from Support leaders | L2 — **Reflex**: quarterly governance review; top contact drivers presented to Product with costed impact | L3 — **Reflex**: monthly review cycle; Product teams commit to fix targets | L3 — Weekly cycle | L4 — **Reflex**: automated triage; Product teams own contact reduction targets per domain | % of top reason types resolved by a product fix per quarter | Product team commitment to contact reduction ownership; Reflex MCP |
| **Taxonomy accuracy** | Reflex, Zendesk | L2 — Manual tagging in **Zendesk**; accuracy variable | L2 — **Reflex**: validates tagging accuracy; gaps flagged for agent training | L3 — **Reflex**: automated accuracy monitoring; retraining triggered automatically | L3 — High accuracy | L4 — **Reflex**: AI auto-corrects mis-tags; accuracy >95% | Taxonomy tagging accuracy % | Reflex phase 1 (Q1 2026); agent training programme |

---

## Stage 6: Governance

**Strategic intent**: Maintain consistent service quality across merchant levels, channels, and geographies as the Care model scales from thousands to millions of contacts. By 2030, SLA adherence and CSAT are automated and self-reported, with exceptions escalated rather than manually reviewed. Governance enables scale — it does not cap it.

| Capability | Care Products | 2026 | 2027 | 2028 | 2029 | 2030 | Metric | Blocker / Dependency |
|---|---|---|---|---|---|---|---|---|
| **SLA monitoring** | Zendesk, Success Plans | L2 — **Zendesk**: SLAs configured; manual monitoring | L3 — **Success Plans**: SLA rules by merchant level and reason type; **Zendesk**: automated breach alerting | L3 — **Zendesk**: B2C SLAs added; banking SLAs defined | L3 — Automated reporting | L4 — **Zendesk**: real-time SLA dashboard; routing priority adjusts dynamically on SLA risk | SLA adherence % by merchant level and reason type | Support model completion (Q3 2026); SLA definition per reason type |
| **CSAT measurement** | Zendesk, Fin | L2 — **Zendesk**: CSAT surveys live for B2B; manual reporting; no B2C CSAT yet | L3 — **Zendesk** + **Fin**: CSAT across B2B + B2C; AI Agent CSAT tracked separately from human agent CSAT | L3 — Banking contacts included | L3 — Automated weekly CSAT reporting | L4 — **Zendesk**: real-time CSAT; **Reflex**: identifies low-CSAT patterns and flags to QA | CSAT score by channel and merchant level; AI Agent CSAT vs human agent CSAT | B2C CSAT survey design; Fin CSAT integration |
| **Consumer Duty and complaint handling** | Zendesk, Consumer Duty process | L0 — B2B only; no formal complaint handling | L2 — Consumer Duty compliance process and formal complaint handling live at B2C wallet launch: 8-week final response letters, FOS referral rights, tracked SLAs — built into the product from day one | L3 — **Zendesk**: banking complaints process covers B2B banking products too | L3 — Stable; auditable | L4 — **Zendesk**: automated complaint tracking; regulatory reporting generated without manual effort | Complaint resolution time; % within 8-week SLA; FOS escalation rate | Legal and Compliance must define process before wallet launch (2026 design); embedded in product design not added afterwards |
| **Vulnerable customer identification** | Fin, Agent Toolkit, agent training | L0 — B2B only; no vulnerability detection | L2 — Embedded across all B2C channels from day one as part of Consumer Duty: **Fin** detects vulnerability signals; **Agent Toolkit** flags; agents trained to handle; specialist escalation path live | L3 — Detection accuracy measured; coverage improves | L3 — High accuracy | L4 — **Fin**: proactive identification; adapts interaction style in real-time; seamless escalation to specialist agent | Vulnerable customer detection rate; escalation success rate | Consumer Duty design completed 2026; must be embedded in Fin and Agent Toolkit before B2C launch — not added after |

---

## Capability dependencies and sequencing

Some capabilities are blocked by others. Resolving blockers in the right order accelerates the entire flywheel.

**Critical path for 2026:**

```
Data latency fix (Settlements, Balances via MCP) [Fuel]
  → Agent Consultant phase 2: NL data queries live [Agent Experience]
  → AI suggestion accuracy and adoption increases [Agent Experience]
  → AHT reduction [Agent Experience]

Reflex phase 1 (Q1) → Reflex phase 2 (Q2) → Reflex MCP (Q3) [Insight & Prevention]
  → Content gap identification becomes automated [Fuel]
  → AI action plans for Product become possible [Insight & Prevention]
  → Product fix governance cycle starts [Insight & Prevention]

Success Plans rollout (Q2 Standard → Q3 Enterprise/Premium) [Orchestration]
  → Customer 360 channel eligibility rules go live [Orchestration]
  → Merchant level routing becomes accurate [Orchestration]
  → SLA rules by merchant level enforced in Zendesk [Governance]
```

**Critical path for 2027 (B2C wallet launch):**

```
B2C taxonomy definition (mid-2026) [Input]
  → Docs and Education Hub B2C content build (H2 2026) [Fuel]
  → Fin B2C configuration [Input, Orchestration]
  → B2C channel eligibility and routing rules [Orchestration]

Consumer Duty and complaint handling process design (2026) [Governance]
  → Zendesk B2C complaint tracking live at launch [Governance]
  → Regulatory SLA compliance from day one [Governance]

Vulnerable customer process design (2026)
  → Fin AI detection embedded at launch — not bolted on after [Governance]
  → Consumer Duty compliance from day one [Governance]
```

**Critical path for 2028 (B2B Banking):**

```
Banking product scope definition (2027) [Input]
  → Banking taxonomy design [Input]
  → Docs and Education Hub banking content build [Fuel]
  → Zendesk banking routing rules and agent specialist queues [Orchestration, Agent Experience]
  → AM/TAM knowledge base update in Sonar [Fuel]
```

---

**Last Updated**: March 2026
**Owner**: Charlie Wildish
**Status**: Working draft
