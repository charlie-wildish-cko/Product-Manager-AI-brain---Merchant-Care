# The Care flywheel and its stages

> Strategic principles for scaling the Care flywheel to 2030: [Support Scale Principles](support-scale-principles.md)
>
> **Capability model**: The full capability matrix per flywheel stage (year-by-year, 2026–2030) is in [care-capability-model.md](care-capability-model.md).
>
> **2026 delivery**: See `2026 deliverables.md` in the workspace root for the full roadmap mapped against these stages.
>
> **Taxonomy reference**: The current support query taxonomy (Case Type → Issue Type → Reason) is documented in [`../processes/support-taxonomy.md`](../processes/support-taxonomy.md) — 13 case types, 41 issue types, ~107 reasons. Gaps for B2C (2027) and B2B banking (2028+) are noted there.




| Stage | Components | Definition | Metrics | Product capabilities | Vision state |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **1\. Input** | **Query Taxonomy & Product mappings  Support Channels**  | What the customer is asking and the medium they are using to ask it. | Query mix % Channel mix % Self serve resolution potential % | Channels across B2B/B2C: Email Dashboard Webform Dashboard requests page Fin AI Agent IM/Slack Phone Taxonomy values & definitions. | We review our taxonomy bi-annually to ensure completeness and relevance We link tickets to Products in the Product Catalogue B2B channels: Email, AI Agent with escalation, live chat with human agent, IM, Phone B2C channels: Mobile app chat, Phone Fin AI Agent is majority channel for customer support; applied as triage on most channels before contacts reach a human agent Platform contacts arrive with Platform identification and Platform merchant context where needed; Fin AI Agent is configured for Platform users |
| **2\. Orchestration** | **Triage Logic Routing Rules** | Deciding where the contact goes and who is best suited to answer it. | % contacts resolved by AI Agent First assignment time Routed ticket acceptance/skip rate AHT/first solve times First contact resolution rate Reopen Rate | Auto-classification AI Classification logic Routing rules B2C team B2B team | Fin AI Agent is solving 80% of contacts Any contact escalated to a human agent is auto-classified to taxonomy before routing — no manually routed tickets Human Agents are specialists in product domains and offer fast, high quality technical support Routing gets tickets to right owners first time Platform contacts identified and routed; Fin operates with L2 context for Platform queries; Platform Embedded AI live from 2027 |
| **3\. Fuel** | **Data Knowledge Base** | The knowledge and contextual data provided to Agents and AI to enable efficient and accurate issue resolution. This is critical to any automation or AI solutions. | Data coverage vs taxonomy Customer facing  Internal facing Content coverage vs taxonomy Customer facing Internal facing AI Agent resolution rate % for Content | Data B2B: Payins, Payouts, Settlements, Balances, Integration,  Configuration… B2C: Consumer data, payments Knowledge Docs & SOPs Knowledge Product knowledge | Necessary Checkout data is easily available and joined up, we can leverage MCPs/AI Agents to query data from any source we need to solve queries Content reviews use AI to aggregate and provide updates to our Content team to improve Our content covers 90% of our taxonomy Our AI Agent and Agent tools access APIs which can solve 90% of our issue types/reasons Platform merchant data accessible to agents and Fin via MCP for applicable query types |
| **4\. Agent Experience** | **Agent tools (Support platform, Diagnostics, Agent Consultant)** | The interface the human agent uses and the actions they can perform. | Average Handle Time (AHT) Taxonomy automation % Agent tool adoption rate per ticket Issue type/reason automation % | Ticketing system (support platform) Agent tools [Agent AI Consultant](../products/agent-consultant.md) Diagnostic tooling Knowledge access | 90% of Agent tasks are automated/semi-automated using AI-assisted tools Agents get AI-suggested actions on every ticket The support platform operates a 7-step agent workflow: ticket creation and enrichment → auto-classification and routing → agent assignment with Consultant suggestion → agent approves and acts → reply to customer → cross-team escalation via Jira or custom API to other teams (Treasury, Engineering, other business teams) as needed → ticket close triggers Reflex data feed Support platform scales to ~500 agents across B2B and B2C with walled permissions — B2C agents (including any BPO) cannot access B2B customer data Platform architecture is modular and build-around: our AI agents, data sources, and integrations plug into the platform — we do not build for the platform's constraints |
| **5\. Insight and prevention** | **Support contact data sources Analytics on the sources** | The process and tooling used to translate individual customer issues into actionable product, process, or documentation improvements, and the measure of success in preventing future issues. | Quarterly top contact reasons per issue type % of top X contact reasons resolved by a product fix per quarter Contact Product tagging accuracy | Insights Support data product [Reflex](../products/reflex.md) | Automated outputs for Product/Engineering to prioritize and commit to fixing the top 5 contact drivers (B2B) Automated outputs for B2C contact drivers reviewed weekly to address Support data insights used across the Care flywheel (Input, Fuel, Governance, etc.) |
| **6\. Governance (this is more Ops, less Product)** | **Scheduling SLA Management** **Quality Assurance (QA)** | The operating principles, processes, and metrics (SLA, QA) that ensure consistent delivery of service speed and quality, and compliance with regulatory or internal standards. | CSAT (AI Agent and Agent) SLA adherence Internal QA scores | Zendesk SLAs Support CSAT survey QA in Zendesk | We have a 90%+ CSAT We meet 95% SLA Full automated, QA scores of 90%+ |


## B2C — Current State and Launch Considerations

> Sourced from competitive analysis of Monzo, Revolut, Starling, Zilch, and Klarna. Full research: `B2C Fintech Support Competitive Analysis.md`.

**B2C support exists today in seed form.** Remember Me — Checkout.com's consumer card-saving product (via Flow) — is live. Consumers contact support via a webform on the Remember Me portal; tickets flow into the **Checkout Consumer** Zendesk brand. Volume is <10 tickets/week. There is no AI Agent, no formal SLA framework, and no tier structure for these contacts. The Checkout Consumer brand is the foundation for the Braavos support model, but requires significant configuration expansion before the 2027 launch.

Four considerations from the competitive landscape that are not yet captured in the 2030 model and should inform B2C product design decisions before the 2027 Braavos wallet launch.

### 1. Agentic Commerce Liability

By 2027, a meaningful share of B2C support contacts will involve disputes where an AI agent — not the human — made a purchase and something went wrong. This is a new category that existing support models (and consumer protection frameworks) don't cleanly address.

The support model needs to distinguish between:
- **Unauthorised transactions** (fraud — bank is liable under existing frameworks)
- **Unintended transactions** (AI agent error — liability depends on terms of service and what the user explicitly authorised)

This requires a product design decision (cryptographic or logged proof of user consent for AI-initiated purchases) and a policy decision (where Checkout's liability sits) before the wallet launches. Legal & Compliance should be involved early.

### 2. B2C Support Tiering

The 2030 model describes B2C channels but does not define a B2C care tier structure. Competitors (Revolut Standard/Premium/Ultra, Monzo, Starling) use tiered support as both a service model and a revenue lever:

| Tier | Channel | SLA | Model |
| --- | --- | --- | --- |
| Standard | AI Agent / self-service | Hours | 24/7 automated resolution |
| Premium | Priority in-app chat (human) | < 5 minutes | Dedicated human expert |
| VIP / Ultra | Priority voice + callback | Instant | Account management |

Checkout's B2C consumer wallet will need an equivalent structure defined before launch — both to set SLA commitments and to determine whether premium support access is a monetisable feature or a retention tool.

### 3. AI Resolution Rate — Ambition Check

The 2030 vision targets 80% AI resolution. The competitive analysis benchmarks the industry at 70–75% FCR today, with high performers already targeting >85% by 2027. This suggests:

- 80% may be the industry average at launch in 2027, not a differentiating target
- The 2030 B2C ambition should likely be **>85–90%** to be genuinely differentiated
- Intercom Fin (our current platform) benchmarks at 55–65% autonomous resolution — below specialist agentic platforms (Fini: 70–85%). Platform capability will be a constraint to track as B2C scales.

### 4. Embedded Support as a Product Feature

The most effective B2C support models (Klarna, Monzo, Starling) don't surface support as a separate flow — they embed it directly into the transaction and product experience:

- **Klarna**: dispute flow embedded in the transaction view; invoice auto-paused during investigation
- **Monzo**: "Report Missing Cashback" accessible from the specific transaction, not a generic help menu
- **Starling**: natural language spending queries eliminate an entire category of "where did my money go?" contacts

For the consumer wallet, this means the support model should be designed in conjunction with the product UX — not bolted on after. Key moments to embed support: missing cashback, disputed merchant transactions, rewards status tracking.

### 5. Banking Regulation Changes the B2C Support Floor *(2027 launch)*

The 2027 consumer wallet launches as a **banking product** — Checkout.com will hold consumer funds and earn interest on balances. This is not a future consideration; it applies at launch and raises the regulatory floor materially above what a PSP is required to provide:

| Obligation | PSP (current) | Bank (future) |
| --- | --- | --- |
| Complaint handling | Best practice | Mandatory — 8-week final response letters, FOS referral rights |
| Phone support | Optional | Typically required for accessibility compliance and Consumer Duty |
| Consumer Duty | Not applicable | Mandatory — requires demonstrable good outcomes for retail customers |
| Deposit protection communications | N/A | FSCS (or equivalent) disclosure obligations |
| Vulnerable customer identification | Best practice | Regulatory expectation (FCA Consumer Duty) |

**Support model implications:**
- Phone channel is likely to become a regulatory requirement at B2C launch (or shortly after), not just a feature decision — plan for it accordingly in the channel roadmap
- Complaint handling needs a formal process (distinct from support ticket handling) with tracked SLAs before any banking product goes live
- Vulnerable customer policy — including proactive identification in the AI Agent flow — needs to be designed in, not added later (Zilch's AI-driven vulnerability detection is a relevant reference in the B2C competitive analysis)
- New B2B query categories will emerge as merchants hold balances: interest and yield queries, balance statements, treasury-style questions. These aren't in the current support taxonomy and will need to be added before merchant banking products launch.

> Full banking direction context: `checkout-business-context.md` → Banking Evolution.


## Platforms — B2B Customer Segment

Platforms (ISVs) are a distinct B2B customer segment alongside Direct Merchants. A Platform is a vertical SaaS business that embeds Checkout payments into its product, acting as a PayFac for its own merchants (Platform merchants). The three-tier relationship:

```
Checkout.com → Platform (ISV) → Platform merchant
```

Checkout is L2 for Platform contacts; the Platform is L1 for its Platform merchants. Checkout has no direct relationship with Platform merchants — all contacts come from the Platform itself, either about their own account or on behalf of a Platform merchant. The US ISV launch is in active delivery in 2026.

There are two models within the Platforms initiative:
1. **ISV model** (2026+): Platform is the merchant of record; Checkout is L2. Platform handles all Platform merchant relationships.
2. **Checkout-as-PayFac model** (2028+, unconfirmed): Checkout contracts directly with Platform merchants, becoming L1. If this materialises, the support model changes significantly — Checkout takes on direct merchant responsibility for a segment it currently has no relationship with.

The strategic value: each ISV customer brings a portfolio of Platform merchants. As the segment grows, Checkout gains reach into merchant ecosystems without direct acquisition. Competitive context: both Stripe Connect and Adyen for Platforms operate the same tiered model (ISV is L1, payment processor is L2/L3). Checkout's differentiated opportunity is Platform merchant data quality and, from 2027, an embedded AI channel at the ISV layer.

Full segment detail: [`../products/platform-segment.md`](../products/platform-segment.md).

### 1. The Identification and Context Problem

When a Platform contacts Checkout, agents need to:
1. **Identify the contact as a Platform** (not a Direct Merchant) — required for every Platform contact
2. **Know which Platform merchant the issue relates to** — required for specific scenarios (e.g. failed KYC/KYB onboarding, funds holds, merchant-level payout queries); optional context for Platform-level issues

Currently neither is well supported:
- Tickets arrive via email or webform with no Platform tagging
- No structured Platform merchant field on tickets; Platform merchant context is not consistently captured
- Fin cannot distinguish between a Direct Merchant and a Platform user — meaning it cannot tailor content responses appropriately (e.g. a Platform user asking about a payment failure may need guidance on their Platform merchant's account, not their own; Fin currently has no way to know this)

Solving Platform identification is the foundational care requirement for the 2026 ISV launch.

### 2. Platform Embedded AI — Future Channel *(2027)*

From 2027, the target channel for Platforms is Fin embedded directly inside ISV portals. Platform support teams access Checkout knowledge and data through Fin before escalating — contacts are resolved at the ISV layer, not the Checkout layer.

This extends the deflection model into the partner ecosystem. As the Platform segment grows, the embedded AI capability deflects a proportionally growing volume before it reaches Checkout agents — offloading the first line entirely, rather than just improving routing at Checkout. The 2026 foundations (Platform identification, Fin Platform awareness) are prerequisites.

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

### 4. The Checkout-as-PayFac Horizon *(2028+, unconfirmed)*

If Checkout elects to act as a PayFac from 2028, it would contract directly with Platform merchants. Checkout becomes L1 for a large number of merchants it currently has no relationship with. This will require a new direct merchant support model for Platform merchants, taxonomy extensions, and significant agent and tooling capacity. This should be flagged as a planning dependency for 2027 resource and roadmap decisions.


## B2B Banking Evolution *(2028+)*

> Full business context: `checkout-business-context.md` → Banking Evolution.

From 2028, Checkout.com will begin offering banking products to merchants — storing funds and paying interest on merchant balances. This is a meaningful evolution from the current PSP model and will require deliberate changes across the Care flywheel.

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

### The 2030 Care flywheel assumptions need revisiting at 2028 transition

The 2030 model assumes the Care flywheel already spinning for B2B payments. Adding banking products will temporarily reset parts of it — new taxonomy to define, new Fuel (data + content) to build, new agent specialisms to develop. The transition should be planned as a discrete phase rather than assumed to be absorbed seamlessly.

### Competitive benchmarks shift for B2B

For B2B payments, the benchmark is Stripe and Adyen. For B2B banking, the relevant comparators become Revolut Business, Starling Business, and Tide — digital-first business banks. These have fundamentally different support models (and different regulatory floors) to PSP competitors.


## Now vs 2030

| Capability | What we have now (2026) | In 2030 |
|------------|-------------------------|---------|
| **Input** | **B2B (Direct):** Email and Dashboard channels. **Query taxonomy:** Refreshed every 6–12 months, with some LLM assistance. **Platform:** Email and webform, untagged; no Platform identification; Platform merchant context inconsistently captured. | **B2B (Direct):** Email, AI Agent with escalation, **live chat with human agent, IM/Slack, Phone**. **B2C:** **Mobile app chat, Phone**. **Platform:** Structured channel with Platform ID; Platform merchant field for applicable query types; Fin identifies Platform users. **Query taxonomy:** LLM-driven, refreshed **quarterly** based on contact reasons from Reflex. |
| **Orchestration** | **B2B (Direct):** New support model rolling out this year — merchant and channel eligibility, some AI involvement. AI currently limited to Dashboard and some emails. **Platform:** No Platform routing rules; agents cannot distinguish Platform contacts from Direct Merchants. | **B2B (Direct):** AI applied as triage on most channels; any escalated contact is auto-classified to taxonomy before routing — no manually routed tickets. Routing based on support plan (SLA and priority), with taxonomy-mapped SLA and priority rules. **B2C:** AI-first by default; human escalation only when needed. **Platform:** Platform contacts auto-routed to Platform-trained agents or Fin; L1/L2 boundary enforced; Fin embedded in ISV portals (2027+). |
| **Fuel** | **Data:** Primarily Payin data for payment queries in AI Agent & Agent tools, but high latency. Other data sources not yet suitable (standard/accuracy issues). No Platform merchant data access for agents or Fin. **Knowledge:** Reactive, manual monthly content reviews from AI Agent chats and Agent knowledge captures. Focus on building Tutorials & Video content. | **Data:** Accurate, joined-up, accessible data easily available to AI-powered tools (MCPs etc.) with **low latency**. Platform merchant data traversal via MCP for applicable queries. **Knowledge:** Proactive, **weekly** AI-assisted analysis of content gaps, reviewed and updated by Content teams. Public docs designed for customers with low payments knowledge; breadth of type (tailored guides/videos); surfaced by AI Agent. Vertical-specific knowledge available for Platform agents. |
| **Agent Experience** | **Ticketing:** Zendesk for handling and solving tickets. **Tooling:** Payment, User data, AI knowledge. Initial investment in Internal AI Agent to suggest and perform actions with human-in-the-loop. No Platform-specific tooling; L1/L2 boundary unclear for agents. | **Ticketing:** Support platform scaled for ~500 agents across B2B and B2C; B2B and B2C agents are virtually separated with walled permissions (BPO for B2C cannot access B2B data). Agent workflow: ticket enrichment → auto-classification and routing → Agent Consultant suggests action → agent approves and acts → reply → cross-team escalation via Jira or custom API integrations to other business and engineering teams → ticket close triggers Reflex data feed. **Tooling:** Agent Consultant suggests actions **proactively** on every ticket; agent approves before execution. Platform merchant lookup for applicable queries; AI Consultant understands Platform context; L1/L2 handoff supported. |
| **Insight & Prevention** | **Insights:** Building Reflex (AI insights) to analyze and synthesize contact root causes. **Prevention:** Planning governance model for contact reduction based on Reflex outputs. Platform contacts mixed with Direct Merchant contacts; root causes not separated. | **Insights:** **Weekly** contact reasons reported proactively using Reflex, shared with Product teams. Platform contact reasons tracked separately; data surfacing failures at ISV layer distinguished from product bugs. **Prevention:** Reflex generates AI **action plans** to resolve root causes for triage and escalation to Care & other Product teams to solve as BAU (like Stripe Minions). |

