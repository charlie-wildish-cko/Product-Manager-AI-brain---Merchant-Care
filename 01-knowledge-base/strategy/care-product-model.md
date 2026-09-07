# The Care product model

> **Source of truth**: This doc owns the model structure — the two lenses (flywheel + stack), their definitions, and stack-to-flywheel mapping.
>
> **2026 delivery**: See `2026 deliverables.md` in the workspace root for the full roadmap mapped against these stages.
>
> **Taxonomy reference**: The current support query taxonomy (Case Type → Issue Type → Reason) is documented in [`../processes/support-taxonomy.md`](../processes/support-taxonomy.md) — 13 case types, 41 issue types, ~107 reasons. Gaps for B2C (2027) and B2B banking (2027+) are noted there.

## Two lenses on the same model

This doc holds two lenses on Care. They are not alternatives. Each answers a different question, and both are used at leadership level.

- **Care flywheel**: the lifecycle of a support contact through six stages, plus Stage 0 (Product onboarding) — a once-per-launch stage that configures the other six for a new product before its first contact arrives. Best for roadmap narrative, how each stage compounds to move contact rate and cost per contact, and ops alignment.
- **Capability stack**: the architectural layers we own, build, or buy. Best for vendor and build/buy/keep decisions (e.g. the [Zendesk platform RFC](../../04-active-work/research/zendesk-platform-decision-rfc.md)), eng investment framing, and "where does system X fit" questions.

Every product and deliverable can be placed on both. The stack-to-flywheel mapping is immediately after the stack section.

## The Core Logic

**Start with who the customer is.** Customer segment sets the support contract before any product decision is made. An Enterprise B2B merchant expects expert technical resolution and measures Checkout on time-to-fix. A consumer wallet user expects instant in-app resolution and has no tolerance for an email thread. A Platform needs us to understand a three-tier support relationship before we can say anything useful (Sub merchant > their Platform > Checkout). And if Checkout takes on direct SMB support (unconfirmed, covered under the SMB Horizon below), the model must scale to serve 100,000s if not millions of small merchants directly, potentially by 2030.

That contract — channel, response time, resolution path — is determined by the customer. The Care model exists to deliver against it.

Segment is one of five pieces of **Customer Context**: segment, business model, account configuration, product & usage, and support history. All five are resolved once per contact and read by whichever stage needs them — segment and business model shape Input's channel/taxonomy contract; account configuration is what actually gates eligibility in Orchestration (can this contact be deflected to Fin at all, or does the account's configuration force human routing regardless of what Fin is capable of); product usage and support history scope Fuel's data retrieval to what applies to this specific merchant. Customer Context is not a stage the contact moves through — it's cross-cutting, read at every stage, not owned by one. Full breakdown in the Customer Context row of the Operating Model table below.

**Apply AI where it can resolve.** Fin is the primary resolution layer across all segments. But Fin's resolution rate is not a property of the model — it's a function of what we've equipped it with for each specific query type. A Fin that knows how to check settlement status for `Funds and Fees > Settlements > Delayed / Missing Settlement` resolves that contact. A Fin that doesn't escalates it. The difference is deliberate investment, not configuration.

Fin does not retrieve or reason over data directly. For any data-dependent query, Fin calls **Customer Agent** — a Care-owned data and reasoning layer. Customer Agent retrieves from internal systems, reasons over the results, and returns a structured explanation. Fin converts that explanation into merchant-facing language. Raw data never leaves Care's systems. This removes cross-team API dependencies, uses data access the Consultant already holds, and is portable — any future AI agent can replace Fin without changing the Customer Agent interface. See [Agent Consultant](../products/agent-consultant.md).

**The intelligence layer is what makes AI able to resolve.** Four inputs power it:

- **Taxonomy** — a structured map of what customers ask, at three levels: Case Type → Issue Type → Reason. Today: 13 Case Types, 41 Issue Types, ~107 Reason codes.
- **Product mapping** — which Checkout product each Reason traces back to. `Accepting payments > Authentication (3DS) > 3DS Decline` maps to the Authentication product; `Technical Issue > Webhooks > Signature Verification Failure` maps to Notifications.
- **Contact data** — which Reason codes drive the highest volume, where Fin is failing, where agents are spending the most time.
- **Coverage matrix** — for each Reason, whether Fin has the content and data to resolve it end-to-end. `Funds and Fees > Balances > Balance Confirmation` is resolvable if the Balances data and a Fin Procedure exist. `Accepting payments > Fraud & Risk Controls > Risk Rules` requires the merchant's rule configuration and a policy decision on what Fin is allowed to read.

This is a gap map, not a knowledge base. Every Reason node either has what it needs or it doesn't — and the model makes that explicit.

**The three layers form a closed loop.** Contacts arrive → the intelligence layer identifies what Fin can and can't resolve → we close the gaps → Fin resolves more → fewer contacts arrive. That is the flywheel.

**Known structural gaps (validated January 2026 AM research):**

- **Fin cannot reach top-tier merchants in its current channel setup.** eBay, Temu, Shein, and Ant Financial — among the highest TPV accounts — deliberately bypass the Checkout dashboard (compliance policies, API-first operations, or strategic preference). Fin is dashboard-bound; the resolution layer is structurally inaccessible to this segment. Any deflection strategy that depends on dashboard adoption will miss these accounts entirely.
- **~25% of all annual contacts have no automation path.** TPA and regional payment method issues — Mada refunds in KSA/MENA, APM disputes and status queries in APAC — require manual intervention at every step. No batch refund API exists; scheme portal access is manual; dispute handling for APMs is email-only. This category must be excluded from deflection rate targets until product or commercial conditions change.
- **True contact volume is undercounted.** APAC enterprise merchants (Ant Financial on DingTalk, ByteDance on Lark, Temu on proprietary IM) and eBay (multiple dedicated Slack channels) conduct most support interactions outside Zendesk. The care team logs APAC IM tickets manually via screenshot. Reported contact volumes from top-tier merchants understate actual support effort.
- **Transaction status and payment confirmation = ~60–70% of all B2B contacts.** Independently validated across 8 AM conversations in January 2026. This is the clearest automation target and the primary rationale for extending Fin to email/non-dashboard channels. Principal blocker: authentication over email (no login token) and PCI/data handling sign-off.

### How the layers map to the flywheel

| Layer                                                                                            | Flywheel stage                                  |
| -------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| New product launches                                                                              | Product Onboarding                              |
| Customer Context — segment & business model set channel, priority, taxonomy scope                | **Input**                                       |
| Customer Context — account configuration gates eligibility (deflect to Fin, or force human routing) | **Orchestration**                               |
| Customer Context — product usage & support history scope what's relevant to retrieve             | **Fuel**                                        |
| Fin equipped with Procedures, data, content                                                       | **Orchestration + Fuel**                        |
| Taxonomy, product map, contact data, coverage matrix                                              | **Fuel → Insight & Prevention → back to Input** |

### Three examples

**1. Enterprise merchant: `Funds and Fees > Settlements > Delayed / Missing Settlement`**

Medium-volume, data-intensive. The merchant wants to know where their money is. The intelligence layer tells us this Reason exists in the taxonomy, maps to the Settlements product, and is solvable if Fin has live settlement data and a Procedure. With the Settlements MCP connected, Fin queries the status and responds. Without it, Fin escalates to a specialist who runs the same query manually — 44x the cost. Reflex tracks this as a contact driver; if it's top-5 for the quarter, the Settlements product team gets an action plan to fix the root cause.

**2. Platform ISV: `Platforms > Sub-Merchant Onboarding > Merchant Activation and Verification`**

A Platform contacts us because one of their merchants is stuck in KYC. Without Platform identification, Fin responds as if this is a Direct Merchant query. With it, Fin knows this is an L2 query, surfaces the Platform merchant's KYC status from the Platform Merchant Directory, and gives the ISV what they need to unblock their merchant. The intelligence layer — specifically the Platform Identity tag and the merchant data — is what turns an escalation into a resolution.

**3. B2C consumer: `Accepting payments > Disputes > Dispute status`** *(2027, wallet launch — B2C taxonomy not yet defined; using the B2B path illustratively)*

A consumer asks where their disputed transaction is. Channel is in-app chat; resolution expectation is under 60 seconds. Before Fin responds, Orchestration checks for vulnerability signals (Consumer Duty requirement). The Reason maps to a Fin Procedure that queries the consumer's dispute record and returns a plain-language status. If unresolved, it routes to a B2C-walled agent who cannot see any B2B merchant data. Insight tracks consumer dispute drivers separately; the wallet product team, not the B2B payments team, is accountable for the fix.

### Note: Domain tool consolidation (exploration, 2026-07-30)

2026's company-wide AI push has left every domain (Payments, Settlements, Configuration, Fraud) building its own AI interface at its own pace, with no shared standard. This is a live extension of the Fuel/Customer Agent pattern above, not yet a committed roadmap item.

Target state: one interface per domain, exposed as a tool any AI agent can call, not just Fin. Build internal-first — land a new domain tool on Agent Consultant, where a human reviews every output, before exposing the same interface to Fin or a future customer agent. Same tool, same interface, more consumers over time as it's proven.

Given the cost of building a bespoke interface per domain (data mapping, semantic layer, ongoing maintenance, all still unowned), Glean is an interim lever worth testing for the knowledge-retrieval slice of Fuel — it already searches across Confluence, Jira, Slack, Zendesk, and BigQuery without Care having to build a connector. It doesn't replace a domain tool where the query needs live data, reasoning, and action (e.g. the Settlements MCP example above) — only where it's knowledge-lookup-shaped.

Related: Q3 2026 "Consolidation of Agent Tools" deliverable (unifies existing agent toolkit into one interface — this is the natural next stage after that, not a replacement for it).

---

## Stage 0: Product Onboarding (pre-Input)

> Concept raised at the Care/Risk/Compliance product HBR, July 2026, on servicing readiness at scale. Now a core layer of both the flywheel and Capability stack below.

Every stage below assumes the flywheel is already spinning for the product generating the contact. That holds for existing products. It breaks the moment a new or changed product launches — taxonomy, routing, content, and data access don't exist yet, so Care discovers the gap from live contacts instead of ahead of them. The B2C and B2B Banking sections in this doc already treat their launches as a discrete transition to plan for, not something the flywheel absorbs automatically. Stage 0 generalises that same discipline to every product launch, not just major segment launches — the volume that makes this necessary: 150+ initiatives reviewed at 2027 planning, several of which (BlueEMI, Ray, eFX, Interest) shipped with no Care assessment at all.

**What it is.** A stage that runs once per product launch, not once per contact. A launching product team declares, before the first contact arrives, what Input, Orchestration, and Fuel need to already contain. This turns "Care discovers this after the fact" into "the product team configures this before launch," gated by the intake process product teams already go through.

**How it interacts with the rest of the flywheel:**
- **Input** — new query types are classified against the existing taxonomy at intake, not discovered from ticket backlog after launch.
- **Orchestration** — routing, SLA, and resolution complexity (does this need a data lookup, an action, or does content alone answer it?) are declared at intake, not improvised per ticket.
- **Fuel** — a content commitment and a data-access commitment are made explicit before launch, closing the gap between "product ships" and "content or data exists to support it."
- **Insight and Prevention** — the product is tagged for attribution from day one, so contact volume is owned by the launching team from the first contact, not discovered later.
- **Agent Experience and Governance** are not configured by Stage 0 — they operate on whatever Stage 0 has already set up, the same as any other contact.

**How it sits on the stack.** Stage 0 is layer 0 in the Capability stack below — Product onboarding. It configures Channel, Customer AI Agent, Routing and Human Agent Experience, Integration and Data, Knowledge, and Analytics and Insight for a new product before launch, rather than being configured bespoke per launch. Stage 0 is **sequential, not cross-cutting**: it is a first step that runs once per product, before any contact exists, then it's done. That's different from Customer Context and Governance below, which are cross-cutting because they stay active *continuously, across every contact*, in parallel with whichever sequential stage that contact is in.

**Why it matters at scale.** Contact rate and cost per contact only compound correctly if the flywheel is fully configured when volume starts. A launch that skips Stage 0 isn't a visible failure at launch — it shows up later as elevated cost per contact and unattributed contact volume.

---

## Operating model: the Care flywheel

| Type | Stage                                               | Components                                                        | Definition                                                                                                                                                                                    | Metrics                                                                                                                                                        | Product capabilities                                                                                                                                          | Vision state                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| :--- | :-------------------------------------------------- | :---------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cross-cutting | **Customer Context**                     | Segment · Business model · Account configuration · Product & usage · Support history | Who the customer is and what they're entitled to. Resolved once per contact and read by every stage the contact passes through — not owned by any single stage, and not a step the contact "moves through" like Input or Orchestration. | % contacts with context resolved before Orchestration Context resolution latency Eligibility-override rate (contacts routed to human despite Fin capability, due to account configuration) | Customer Agent (context resolution) Platform Merchant Directory Account/entitlement lookup | Every contact carries resolved segment, business model, account configuration, and product usage/support history before it reaches Orchestration. **Input** uses segment and business model to set channel and taxonomy scope. **Orchestration** uses account configuration to gate eligibility — can this contact be deflected to Fin at all, or does account configuration force human routing regardless of Fin's capability. **Fuel** uses product usage and support history to scope Customer Agent's data retrieval to what's relevant for this merchant, and to give resolution context for repeat/escalated issues. **Insight & Prevention** uses segment to attribute contact drivers correctly. Resolved once by Customer Agent, consumed everywhere — never re-derived per stage. |
| Sequential | **0\. Product onboarding**                          | Support readiness components                                      | What components are needed in support before product launch                                                                                                                                   | % products fully onboarded into Care stack                                                                                                                     | Support Readiness Agent                                                                                                                                       | When launching a product at Checkout, all launches are triaged and passed through the Support readiness agent. The agent reads the information about the product, what it does and who it solves for. It then determines the support requirements across the stack and scopes these for the Care product team to implement. There is minimal to no manual work done once the product is well understood to implementation in the Care stack.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Sequential | **1\. Input**                                       | **Query Taxonomy & Product mappings  Support Channels**           | What the customer is asking and the medium they are using to ask it.                                                                                                                          | Query mix % Channel mix % Self serve resolution potential %                                                                                                    | Channels across B2B/B2C: Email Dashboard Webform Dashboard requests page Fin AI Agent IM/Slack Phone Taxonomy values & definitions.                           | We review our taxonomy bi-annually to ensure completeness and relevance We link tickets to Products in the Product Catalogue B2B channels: Email, AI Agent with escalation, live chat with human agent, IM, Phone B2C channels: Mobile app chat, Phone Fin AI Agent is majority channel for customer support; applied as triage on most channels before contacts reach a human agent Platform contacts arrive with Platform identification and Platform merchant context where needed; Fin AI Agent is configured for Platform users                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Sequential | **2\. Orchestration**                               | **Triage Logic Routing Rules**                                    | Deciding where the contact goes and who is best suited to answer it.                                                                                                                          | % contacts resolved by AI Agent First assignment time Routed ticket acceptance/skip rate AHT/first solve times First contact resolution rate Reopen Rate       | Auto-classification AI Classification logic Routing rules B2C team B2B team                                                                                   | Fin AI Agent is solving 80% of contacts Any contact escalated to a human agent is auto-classified to taxonomy before routing — no manually routed tickets Human Agents are specialists in product domains and offer fast, high quality technical support Routing gets tickets to right owners first time Platform contacts identified and routed; Fin operates with L2 context for Platform queries; Platform Embedded AI live from 2027                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Sequential | **3\. Fuel**                                        | **Data Knowledge Base**                                           | The knowledge and contextual data provided to Agents and AI to enable efficient and accurate issue resolution. This is critical to any automation or AI solutions.                            | Data coverage vs taxonomy Customer facing  Internal facing Content coverage vs taxonomy Customer facing Internal facing AI Agent resolution rate % for Content | Data B2B: Payins, Payouts, Settlements, Balances, Integration,  Configuration… B2C: Consumer data, payments Knowledge Docs & SOPs Knowledge Product knowledge | Necessary Checkout data is easily available and joined up, we can leverage MCPs/AI Agents to query data from any source we need to solve queries Content is kept current through two mechanisms: (1) proactively — Engineering outputs technical docs and a support article draft at ship time, Content team reviews and publishes (workflow: `02-workflows/product-release-content-workflow.md`); (2) reactively — Content Ops Agent scans Fin failure signals via Reflex and drafts updates. Our content covers 90% of our taxonomy Our AI Agent and Agent tools access APIs which can solve 90% of our issue types/reasons Platform merchant data accessible to agents and Fin via MCP for applicable query types A knowledge graph maps every Reason node to its content (`COVERED_BY` edges) and data (`DATA_AVAILABLE_FOR` edges), producing a unified resolvability matrix — which Reasons Fin can resolve end-to-end, and whether the gap is content, data, or both |
| Sequential | **4\. Agent Experience**                            | **Agent tools (Support platform, Diagnostics, Agent Consultant)** | The interface the human agent uses and the actions they can perform.                                                                                                                          | Average Handle Time (AHT) Taxonomy automation % Agent tool adoption rate per ticket Issue type/reason automation %                                             | Ticketing system (support platform) Agent tools [Agent AI Consultant](../products/agent-consultant.md) Diagnostic tooling Knowledge access                    | 90% of Agent tasks are automated/semi-automated using AI-assisted tools Agents get AI-suggested actions on every ticket The support platform operates a 7-step agent workflow: ticket creation and enrichment → auto-classification and routing → agent assignment with Consultant suggestion → agent approves and acts → reply to customer → cross-team escalation via Jira or custom API to other teams (Treasury, Engineering, other business teams) as needed → ticket close triggers Reflex data feed Support platform scales to ~500 agents across B2B and B2C with walled permissions — B2C agents (including any BPO) cannot access B2B customer data Platform architecture is modular and build-around: our AI agents, data sources, and integrations plug into the platform — we do not build for the platform's constraints                                                                                                                                      |
| Sequential | **5\. Insight and prevention**                      | **Support contact data sources Analytics on the sources**         | The process and tooling used to translate individual customer issues into actionable product, process, or documentation improvements, and the measure of success in preventing future issues. | Quarterly top contact reasons per issue type % of top X contact reasons resolved by a product fix per quarter Contact Product tagging accuracy                 | Insights Support data product [Reflex](../products/reflex.md)                                                                                                 | Automated outputs for Product/Engineering to prioritize and commit to fixing the top 5 contact drivers (B2B) Automated outputs for B2C contact drivers reviewed weekly to address Support data insights used across the Care flywheel (Input, Fuel, Governance, etc.)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Cross-cutting | **6\. Governance (this is more Ops, less Product)** | **Scheduling SLA Management** **Quality Assurance (QA)**          | The operating principles, processes, and metrics (SLA, QA) that ensure consistent delivery of service speed and quality, and compliance with regulatory or internal standards.                | CSAT (AI Agent and Agent) SLA adherence Internal QA scores                                                                                                     | Zendesk SLAs Support CSAT survey QA in Zendesk                                                                                                                | We have a 90%+ CSAT We meet 95% SLA Full automated, QA scores of 90%+                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |


## Capability stack

Nine layers describe Care's architecture — how each stands today and what it must become by 2030. Layer 8 (Operations and Governance) is cross-cutting, active continuously across every contact. Layer 0 (Product onboarding) and layers 1–7 are sequential — layer 0 runs once per product before any contact exists, then layers 1–7 run in order per contact. See Stage 0 above for how layer 0 works.

| #   | Layer                                           | Definition                                                                                                                    | Today                                                                                                      | 2030                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --- | ----------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0   | **Product onboarding** *(sequential — once per product, registration time)* | Registration interface product teams go through before launch, declaring what Input, Orchestration, and Fuel need to already contain | No registration step exists. Care discovers new products from live contacts after launch. 150+ initiatives reviewed at 2027 planning; several (BlueEMI, Ray, eFX, Interest) shipped with no Care assessment | Every launch gated by a standard intake via the Support Readiness Agent: taxonomy classification, routing/SLA declaration, content and data commitments, and attribution tagging set before the first contact arrives |
| 1   | **Channel**                                     | How contacts arrive from customers                                                                                            | Email and Dashboard webform (Zendesk). B2C webform via Checkout Consumer brand                             | Email, Dashboard, in-app chat, IM/Slack, Phone across B2B and B2C. Platform-tagged structured entry for ISV contacts                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 2   | **Customer AI Agent**                           | AI that resolves customer contacts before a human sees them                                                                   | Fin on Dashboard and some email. No Platform identification                                                | Fin as triage on most channels. 80%+ resolution. Fin embedded in ISV portals (2027+)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 3   | **Routing and Human Agent Experience**          | Where tickets are routed, where human agents work, and how they escalate to other teams and systems (Salesforce, Jira, Slack). Account-configuration eligibility (from Customer Context) is enforced here — some contacts are routed to a human regardless of what Fin could otherwise resolve | Zendesk with manual and partial AI routing. Limited cross-system escalation                                | Auto-classified routing. ~500-agent platform across B2B and B2C with walled permissions. Cross-system escalation via Jira and custom APIs                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 4   | **Agent AI Assistant**                          | Internal AI that assists human agents with suggested actions, data lookups, and knowledge retrieval                           | Early investment in internal AI Agent with human-in-the-loop                                               | Agent Consultant proactively suggests action on every ticket. Agent approves and acts. 90% of agent tasks automated or semi-automated                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 5   | **Integration and Data**                        | Joined-up customer, payments, and ops data surfaced to AI and agents                                                          | Payin data via agent tools with high latency. Other sources not AI-ready. No Platform merchant data access | Accurate, low-latency data via MCPs across all sources. Platform merchant data traversal for applicable queries. Data layer graph tracks data coverage per Reason node — four states (no source / source with gaps / blocked / live) — and drives Fin Procedures prioritisation. **Customer Agent**: Care-owned data and reasoning layer that Fin (and future AI agents) call for data-dependent queries; retrieves from internal systems, reasons over results, returns structured explanation to Fin; raw data never exposed to Fin. Removes cross-team API dependencies and is portable across AI agents. |
| 6   | **Knowledge**                                   | Centrally hosted content, published to the customer-facing support site and to AI and agent tools                             | Reactive monthly content reviews. Manual gap detection. Focus on tutorials and video                       | Knowledge graph maps every Reason node to its content articles (`COVERED_BY` edges, LLM-tagged by Reflex); coverage matrix shows gaps by volume before they produce Fin failures. 90% taxonomy coverage. Vertical-specific knowledge for Platform agents                                                                                                                                                                                                                                                                                                                                                                  |
| 7   | **Analytics and Insight**                       | Support data product for reporting, root-cause analysis, and prevention                                                       | Reflex in build                                                                                            | Weekly automated contact-driver reports. AI-generated action plans and fix PRs for eng review                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 8   | **Operations and Governance** *(cross-cutting)* | SLA, QA, scheduling, and complaint-handling tooling                                                                           | Zendesk SLAs, Zendesk QA, ad hoc scheduling                                                                | Automated QA at 90%+ scores. AI-audit tooling. 95% SLA adherence. Formal B2C complaint handling for Consumer Duty                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

## How the stack maps to the flywheel

Every stack layer maps to one or more flywheel stages, and every flywheel stage is covered by at least one stack layer.

| Stack layer | Flywheel stage(s) |
|---|---|
| Product onboarding | Product onboarding |
| Channel | Input |
| Customer AI Agent | Orchestration (deflection) |
| Routing and Human Agent Experience | Orchestration (routing) and Agent Experience (UI); account-configuration eligibility for **Customer Context** |
| Agent AI Assistant | Agent Experience |
| Integration and Data | Fuel (data); Customer Agent's context resolution for **Customer Context** |
| Knowledge | Fuel (content) and Input (publishing to support site) |
| Analytics and Insight | Insight and Prevention |
| Operations and Governance | Governance |

**Note:** Product onboarding maps 1:1 to its own flywheel stage — it's sequential, a first step that runs once per product before any contact exists. Operations and Governance also maps 1:1, but it's cross-cutting like Customer Context: both stay active continuously, across every contact, rather than being confined to one step in the sequence. Customer Context has no dedicated stack layer of its own — it's resolved via Integration and Data (Customer Agent) and enforced via Routing and Human Agent Experience (eligibility), which is why it fans across two layers above.

**When to use which lens.** Use the flywheel for roadmap narrative and the metric compounding story (contact rate and cost per contact). Use the stack for vendor and build/buy/keep decisions, eng investment framing, and architectural diagrams that show where a given system fits.

## Direct Merchants — Current State (B2B Baseline)

Direct Merchants (Enterprise, Growth, Premium) are Checkout's current primary B2B segment and the baseline the Core Logic, Operating model, and Capability stack sections above are written against. Platforms, B2C, and B2B Banking below describe deltas from this baseline, not a fresh model.

**Current state**: Email and Dashboard channels; Fin partially deployed (Dashboard and some email). Taxonomy: 13 Case Types, 41 Issue Types, ~107 Reasons (see [support-taxonomy.md](../processes/support-taxonomy.md)). Known structural gaps (above): top-tier merchants (eBay, Temu, Shein, Ant Financial) structurally unreachable via the dashboard-bound channel; ~25% of contacts have no automation path (TPA/regional APMs); true contact volume undercounted (APAC IM channels logged manually); transaction status and payment confirmation (~60–70% of contacts) is the clearest deflection target.

**2030 target**: 80%+ AI resolution via Fin, 90%+ taxonomy content and data coverage, and a closed intelligence loop (taxonomy → product mapping → contact data → coverage matrix) that closes gaps continuously rather than reactively. Full detail in the Now vs 2030 table below.

## B2C — Current State and Launch Considerations

> Sourced from competitive analysis of Monzo, Revolut, Starling, Zilch, and Klarna. Full research: `B2C Fintech Support Competitive Analysis.md`. **Note**: this research benchmarks neobanks and was written for Braavos, Checkout.com's earlier (now ended) neobank proposition. Ray — the crypto/stablecoin wallet going ahead in Braavos's place — is not a neobank; re-validate which considerations below actually transfer before using them to inform Ray design.

**B2C support exists today in seed form.** Remember Me — Checkout.com's consumer card-saving product (via Flow) — is live. Consumers contact support via a webform on the Remember Me portal; tickets flow into the **Checkout Consumer** Zendesk brand. Volume is <10 tickets/week. There is no AI Agent, no formal SLA framework, and no tier structure for these contacts. The Checkout Consumer brand is the foundation for the Ray support model, but requires significant configuration expansion before Ray's external beta (Q1 2027).

Four considerations from the competitive landscape that are not yet captured in the 2030 model and may inform B2C product design decisions ahead of Ray's external beta (Q1 2027) — subject to the neobank-vs-crypto-wallet caveat above.

### 1. B2C Support Tiering

The 2030 model describes B2C channels but does not define a B2C care tier structure. Competitors (Revolut Standard/Premium/Ultra, Monzo, Starling) use tiered support as both a service model and a revenue lever:

| Tier | Channel | SLA | Model |
| --- | --- | --- | --- |
| Standard | AI Agent / self-service | Hours | 24/7 automated resolution |
| Premium | Priority in-app chat (human) | < 5 minutes | Dedicated human expert |
| VIP / Ultra | Priority voice + callback | Instant | Account management |

There may be an equivalent structure in the B2C wallet product, but no plans are confirmed yet.

### 2. AI Resolution Rate — Ambition Check

The 2030 vision targets 80% AI resolution. The competitive analysis benchmarks the industry at 70–75% FCR today, with high performers already targeting >85% by 2027. This suggests:

- 80% may be the industry average at launch in 2027, not a differentiating target
- The 2030 B2C ambition should likely be **>85–90%** to be genuinely differentiated
- Intercom Fin (our current platform) benchmarks at 55–65% autonomous resolution — below specialist agentic platforms (Fini: 70–85%). Platform capability will be a constraint to track as B2C scales.

### 3. Embedded Support as a Product Feature

The most effective B2C support models (Klarna, Monzo, Starling) don't surface support as a separate flow — they embed it directly into the transaction and product experience:

- **Klarna**: dispute flow embedded in the transaction view; invoice auto-paused during investigation
- **Monzo**: "Report Missing Cashback" accessible from the specific transaction, not a generic help menu
- **Starling**: natural language spending queries eliminate an entire category of "where did my money go?" contacts

For the consumer wallet, this means the support model should be designed in conjunction with the product UX — not bolted on after. Key moments to embed support: missing cashback, disputed merchant transactions, rewards status tracking.

### 4. Banking Regulation Changes the B2C Support Floor *(2027 launch)*

The 2027 consumer wallet launches as a **banking product** — Checkout.com will hold consumer funds and earn interest on balances. This is not a future consideration; it applies at launch and raises the regulatory floor materially above what a PSP is required to provide:

| Obligation | PSP (current) | Bank (future) |
| --- | --- | --- |
| Complaint handling | Best practice | Mandatory — 8-week final response letters, FOS referral rights |
| Phone support | Optional | Typically required for accessibility compliance and Consumer Duty |
| Consumer Duty | Not applicable | Mandatory — requires demonstrable good outcomes for retail customers |
| Deposit protection communications | N/A | FSCS (or equivalent) disclosure obligations |
| Vulnerable customer identification | Best practice | Regulatory expectation (FCA Consumer Duty) |

**Support model implications:**
- Phone channel is a regulatory requirement at B2C launch for at least Complaints handling, not just a feature decision — plan for it accordingly in the channel roadmap
- Complaint handling needs a formal process (distinct from support ticket handling) with tracked SLAs before any banking product goes live
- Vulnerable customer policy — including proactive identification in the AI Agent flow — needs to be designed in, not added later (Zilch's AI-driven vulnerability detection is a relevant reference in the B2C competitive analysis)
- New B2B query categories will emerge as merchants hold balances: interest and yield queries, balance statements, treasury-style questions. These aren't in the current support taxonomy and will need to be added before merchant banking products launch.

> Full banking direction context: `../checkout-business-context.md` → Banking Evolution.

## Upstream data gaps cap AI resolution (2026-08-20)

Source: `04-active-work/meeting-notes/2026-08/2026-08-20-merchant-care-ai-resolution-blockers.md`.

Roughly **20% of merchant Care contact volume is blocked on three upstream data gaps**, none of which sit inside Care. Against a 2026 target of resolving at least 40% of merchant volume through Fin, this is the arithmetic reason Care cannot reach the target through Care-side work alone. Percentages are estimates, not measured.

| Blocker | Share of contact volume | State |
|---|---|---|
| TPA / MPGS integration failures (MENA) | ~10% | MPGS and CyberSource fail between statuses; merchants see "captured" or "declined" when Checkout's truth differs. NPG migration is the fix; adoption ~10%, most KSA processing still on MPGS via SAB |
| Clearing invisibility | 5-8% | Clearing is a real state between captured and settled, never exposed to merchants and not internally queryable, so Fin cannot answer it either. Exposure slips to Q1 2027 and delivers settlement information, not clearing |
| Settlement delays | ~5% | Settlement arrival in the merchant's bank cannot be confirmed. The settlement-debited event is the strongest available evidence and covers 90% of TPV processed. Payout replatforming completes ~end Q3 2026, then migration |

Gateway-level status syncing is 2027 work. Nothing in this list lands in time to move the 2026 target.

Two framings established in that forum:
- These are fundamental payment-lifecycle issues that **scale linearly with acquiring volume**. They get worse as Checkout onboards more processing merchants; they do not decay.
- "Historically it's not been the AI that's been the blocker, it's the data that the AI has access to." An exec in the room also stated that consumer (Braavos) was paused in significant part because Care projected rapid headcount scaling, since it could not rely on AI. Care's automation ceiling now gates which businesses Checkout will launch, with Platforms and SMB named as the next tests.

The asset Care must produce to convert that goodwill into delivery is a canonical document listing key Care use cases, the data points each needs, the data owner for each, and a by-when. That becomes the contract with the data platform teams.

## Agentic Commerce Liability (B2B and B2C)

By 2027, a meaningful share of support contacts will involve queries where an AI agent — not the human — made a purchase and something went wrong. This applies across both segments: a B2C wallet user whose AI assistant makes an unintended purchase, and a B2B merchant or Platform whose procurement or ops agent triggers an erroneous payment. This is a new category that existing support models (and consumer protection frameworks) don't cleanly address.

The support model needs to distinguish between:
- **Unauthorised transactions** (fraud — bank is liable under existing frameworks)
- **Unintended transactions** (AI agent error — liability depends on terms of service and what the user explicitly authorised)

This requires a product design decision (cryptographic or logged proof of user consent for AI-initiated purchases) and a policy decision (where Checkout's liability sits) before the wallet launches. Legal & Compliance should be involved early.

## Platforms — B2B Customer Segment

Platforms (ISVs) are a distinct B2B customer segment alongside Direct Merchants. A Platform is a vertical SaaS business that embeds Checkout payments into its product, acting as a PayFac for its own merchants (Platform merchants). The three-tier relationship:

```
Checkout.com → Platform (ISV) → Platform merchant
```

Checkout is L2 for Platform contacts; the Platform is L1 for its Platform merchants. Checkout has no direct relationship with Platform merchants — all contacts come from the Platform itself, either about their own account or on behalf of a Platform merchant. The US ISV launch is in active delivery in 2026.

There are two models within the Platforms initiative:
1. **ISV model** (2026+): Platform is the merchant of record; Checkout is L2. Platform handles all Platform merchant relationships.
2. **SMB model** (2027+, unconfirmed): Checkout contracts directly with SMB merchants, becoming L1. If this materialises, the support model changes significantly — Checkout takes on direct merchant responsibility for a segment it currently has no relationship with.

The strategic value: each ISV customer brings a portfolio of Platform merchants. As the segment grows, Checkout gains reach into merchant ecosystems without direct acquisition. Competitive context: both Stripe Connect and Adyen for Platforms operate the same tiered model (ISV is L1, payment processor is L2/L3). Checkout's differentiated opportunity is Platform merchant data quality and, from 2027, an embedded AI channel at the ISV layer.

Full segment detail: [`../products/platform-segment.md`](../products/platform-segment.md).

### 1. The Identification and Context Problem

When a Platform contacts Checkout, agents need to:
1. **Identify the contact as a Platform** (not a Direct Merchant) — required for every Platform contact
2. **Know which Platform merchant the issue relates to** — required for specific scenarios (e.g. failed KYC/KYB onboarding, funds holds, merchant-level payout queries); optional context for Platform-level issues

We have solutions in place for identifying these in Fin and Zendesk.

### 2. Platform Embedded AI — Future Channel *(2027)*

From 2027, the target channel for Platforms is a form of AI support embedded directly inside ISV portals. Platform support teams access Checkout knowledge and data through AI before escalating — contacts are resolved at the ISV layer, not the Checkout layer.

This extends the deflection model into the partner ecosystem. As the Platform segment grows, the embedded AI capability deflects a proportionally growing volume before it reaches Checkout agents — offloading the first line entirely, rather than just improving routing at Checkout.

Full vision: [`../products/platform-embedded-ai-support-vision.md`](../products/platform-embedded-ai-support-vision.md).

### 3. Flywheel Implications for Platforms

| Stage | What Platforms need |
|-------|-------------------|
| **Input** | Structured channel entry with Platform ID; Platform merchant field for applicable query types (onboarding failures, funds holds, payout queries); taxonomy coverage for Platform-specific query types |
| **Orchestration** | Routing rules that identify Platform contacts and direct to Platform-trained agents; Fin must identify Platform users at conversation start and understand L2 context |
| **Fuel** | Platform merchant data traversal for applicable queries (KYC/KYB status, transaction data, payout records); vertical-specific agent knowledge (Sunday, Guesty, Golfmanager have different urgency profiles and query types) |
| **Agent Experience** | Clear L1/L2 boundary guidance — what Checkout resolves vs. what the Platform resolves; Platform merchant lookup for applicable query types |
| **Insight & Prevention** | Platform contact reasons tracked separately from Direct Merchant contacts; root cause analysis distinguishes product/data bugs from upstream data surfacing failures at the ISV layer |
| **Governance** | SLA commitments calibrated to Platform urgency (e.g. active restaurant payment failure is critical; settlement query is standard); Platform-aware quality measurement |

### 4. The SMB Horizon *(2027+)*

The SMB model above (Checkout as L1 for SMB merchants) is a planning dependency for 2027 resource and roadmap decisions. It would add a large direct-merchant population Checkout has no relationship with today, requiring its own support model, taxonomy extensions, and agent capacity.

Unlike Enterprise and Platform, SMB cannot lean on developer-mediated self-service — research shows 69% of SMBs have no development resource, and PSP switching is rare except after a failure event (fund freeze, decline). This changes the flywheel's design assumptions materially:

| Stage | What SMB needs |
|-------|-----------------|
| **Input** | Dashboard-first entry, not API/docs-first — the self-serve leverage Enterprise and Platform docs provide (line 79 above) doesn't apply to a segment where most operators have no developer |
| **Orchestration** | "No monthly fee" pricing expectations mean thin margins per merchant — routing must favour cheap, high-volume Fin resolution over human escalation by default; escalation reserved for failure events, which are this segment's primary churn trigger |
| **Fuel** | Minimum viable data/content is narrow: live balance, expected settlement, invoice sending — the top two ranked SMB dashboard needs. Build this before broader taxonomy coverage |
| **Agent Experience** | Support response speed is a continuity requirement, not a service tier — a payment outage during live trading is unrecoverable revenue for an SMB with no reserve |
| **Governance** | FCA Consumer Duty's "retail customer" definition explicitly includes micro-enterprises — this extends the Consumer Duty obligations described under B2C above to SMB, independent of the B2C wallet launch. Automated account freezes need a human-in-the-loop review gate before this segment launches, not after |
| **Insight & Prevention** | Checkout.com has ~5% unprompted SMB brand awareness — direct-channel contact volume will be structurally low; most SMB volume will arrive through Platform-embedded or PayFac distribution, not direct acquisition |

**Strategic case for taking this on:** industry-wide SMB support research shows PSPs gate dedicated technical support behind $50M+ volume thresholds, leaving mid-market SMBs in a "Support Valley of Death." A Fin/Agent Consultant-driven model that resolves SMB queries cheaply at scale — without gating consultative support behind volume — is a genuine differentiation opportunity, not just a cost problem to solve.

Full research: [`../products/customer-segments.md`](../products/customer-segments.md) → SMB section.


## B2B Banking Evolution *(2027+)*

> Full business context: `../checkout-business-context.md` → Banking Evolution.

From 2027, Checkout.com will begin offering banking products to merchants — storing funds and paying interest on merchant balances. This is a meaningful evolution from the current PSP model and will require deliberate changes across the Care flywheel.

### Query taxonomy reset

The current B2B taxonomy is entirely payments-focused (payin, payout, settlement, disputes, integration, configuration). Banking products add entirely new first-level categories that don't exist today:

- Merchant balance management (depositing, withdrawing, viewing balance)
- Interest and yield queries (rate queries, interest calculation, accrual timing)
- Working capital / lending (if offered — cash advances, repayment, credit limits)
- Treasury and liquidity management (for larger merchants)

Every stage of the Care flywheel is affected: new query types for Input, new routing for Orchestration, new data and content for Fuel, new agent knowledge for Agent Experience, and new contact drivers for Insight & Prevention.

### AM/TAM role evolves

AMs and TAMs manage merchant relationships and currently escalate payments queries to Care. When merchants hold balances and earn interest, AMs and TAMs will start fielding banking questions — balance queries, yield comparisons, fund movements. This changes:
- What they need to know (banking product knowledge added to payments knowledge)
- What they escalate vs. self-serve (Sonar's knowledge base needs banking content)
- The nature of the structured intake form — banking query types need their own fields

### Competitive benchmarks shift for B2B

For B2B payments, the benchmark is Stripe and Adyen. For B2B banking, the relevant comparators become Revolut Business, Starling Business, and Tide — digital-first business banks. These have fundamentally different support models (and different regulatory floors) to PSP competitors.


## Now vs 2030 (segment deltas)

This table covers only what differs **by segment** between now and 2030. Stage-level detail that applies across segments (vision state, metrics, per-layer today/2030) is in the flywheel and stack tables above; this table is the B2B Direct / B2C / Platform view.

| Stage | Now (2026) | 2030 |
|---|---|---|
| **Customer Context** | **B2B Direct:** segment known, account configuration not systematically checked before routing. **Platform:** business model (Platform vs. Direct) not resolved — agents cannot distinguish a Platform contact from a Direct Merchant one. **B2C:** no context resolution exists (Remember Me webform only, no tiering). | **B2B Direct:** account configuration resolved before Orchestration, gating Fin eligibility. **Platform:** business model and Platform ID resolved at Input, read by Orchestration for L1/L2 routing. **B2C:** full context (tier, vulnerability signals) resolved before Fin responds. |
| **Input** | **B2B Direct:** email, Dashboard. **Platform:** untagged email/webform, no Platform ID. **B2C:** Remember Me webform only. | **B2B Direct:** adds live chat, IM/Slack, Phone. **B2C:** mobile app chat, Phone. **Platform:** structured entry with Platform ID; Fin identifies Platform users. |
| **Orchestration** | **B2B Direct:** new support model rolling out (merchant/channel eligibility). **Platform:** no Platform routing; agents cannot distinguish Platform from Direct. | **B2B Direct:** routing by support plan, taxonomy-mapped SLA/priority. **B2C:** AI-first, human escalation only when needed. **Platform:** auto-routed to Platform-trained agents; L1/L2 enforced; Fin in ISV portals (2027+). |
| **Fuel** | **B2B Direct:** Payin data only, high latency. **Platform:** no Platform merchant data access. | **B2B Direct:** joined-up low-latency data via MCPs. **Platform:** Platform merchant data traversal; vertical-specific agent knowledge. |
| **Agent Experience** | Single Zendesk instance; no B2B/B2C separation; no Platform tooling; L1/L2 unclear. | **B2B/B2C:** walled separation (B2C BPO cannot access B2B data). **Platform:** merchant lookup; Consultant understands Platform context; L1/L2 handoff supported. |
| **Insight & Prevention** | **Platform:** contacts mixed with Direct; root causes not separated. | **Platform:** contacts tracked separately; ISV-layer data failures distinguished from product bugs. |

