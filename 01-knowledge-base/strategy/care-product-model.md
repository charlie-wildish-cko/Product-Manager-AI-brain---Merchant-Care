# Mental model for how we talk about Care Product

> Strategic principles for scaling these domains to 2030: [Support Scale Principles](support-scale-principles.md)
>
> **2026 delivery**: See `2026 deliverables.md` in the workspace root for the full roadmap mapped against these domains.
>
> **Taxonomy reference**: The current support query taxonomy (Case Type → Issue Type → Reason) is documented in [`../processes/support-taxonomy.md`](../processes/support-taxonomy.md) — 13 case types, 41 issue types, ~107 reasons. Gaps for B2C (2027) and B2B banking (2028+) are noted there.




| Domain ‘flywheel’ | Components | Definition | Metrics | Product capabilities | Vision state |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **1\. Input** | **Query Taxonomy & Product mappings  Support Channels**  | What the customer is asking and the medium they are using to ask it. | Query mix % Channel mix % Self serve resolution potential % | Channels across B2B/B2C: Email Dashboard Webform Dashboard requests page Fin AI Agent IM/Slack Phone Taxonomy values & definitions. | We review our taxonomy bi-annually to ensure completeness and relevance We link tickets to Products in the Product Catalogue We offer synchronous and priority channels (chat and phone), email reserved for VIP only Fin AI Agent is majority channel for customer support |
| **2\. Orchestration** | **Triage Logic Routing Rules** | Deciding where the contact goes and who is best suited to answer it. | % contacts resolved by AI Agent First assignment time Routed ticket acceptance/skip rate AHT/first solve times First contact resolution rate Reopen Rate Zendesk complexity? | Intent classification AI Classification logic Routing rules B2C team B2B team | Fin AI Agent is solving 80% of contacts Human Agents are specialists in product domains and offer fast, high quality technical support Routing gets tickets to right owners first time |
| **3\. Fuel** | **Data Knowledge Base** | The knowledge and contextual data provided to Agents and AI to enable efficient and accurate issue resolution. This is critical to any automation or AI solutions. | Data coverage vs taxonomy Customer facing  Internal facing Content coverage vs taxonomy Customer facing Internal facing AI Agent resolution rate % for Content | Data B2B: Payins, Payouts, Settlements, Balances, Integration,  Configuration… B2C: Consumer data, payments Knowledge Docs & SOPs Knowledge Product knowledge | Necessary Checkout data is easily available and joined up, we can leverage MCPs/AI Agents to query data from any source we need to solve queries Content reviews use AI to aggregate and provide updates to our Content team to improve Our content covers 90% of our taxonomy Our AI Agent and Agent tools access APIs which can solve 90% of our issue types/reasons |
| **4\. Agent Experience** | **Agent tools (Zendesk, Diagnostics, Copilot, Consultant)** | The interface the human agent uses and the actions they can perform. | Average Handle Time (AHT) Taxonomy automation % Agent tool adoption rate per ticket Issue type/reason automation % | Ticketing system Zendesk Agent tools Agent AI Consultant Diagnostic tooling Knowledge access | 90% of Agent tasks are automated/semi automated using AI assisted tools Agents get AI suggested actions on every ticket |
| **5\. Insight and prevention** | **Support contact data sources Analytics on the sources** | The process and tooling used to translate individual customer issues into actionable product, process, or documentation improvements, and the measure of success in preventing future issues. | Quarterly top contact reasons per issue type % of top X contact reasons resolved by a product fix per quarter Contact Product tagging accuracy | Insights Support data product [Reflex](../products/reflex.md) | Automated outputs for Product/Engineering to prioritize and commit to fixing the top 5 contact drivers (B2B) Automated outputs for B2C contact drivers reviewed weekly to address Support data insights used across ‘flywheel’ (Demand, Fuel, Governance etc) |
| **6\. Governance (this is more Ops, less Product)** | **Scheduling SLA Management** **Quality Assurance (QA)** | The operating principles, processes, and metrics (SLA, QA) that ensure consistent delivery of service speed and quality, and compliance with regulatory or internal standards. | CSAT (AI Agent and Agent) SLA adherence Internal QA scores | Zendesk SLAs Support CSAT survey QA in Zendesk | We have a 90%+ CSAT We meet 95% SLA Full automated, QA scores of 90%+ |


## B2C Launch Considerations (2027+)

> Sourced from competitive analysis of Monzo, Revolut, Starling, Zilch, and Klarna. Full research: `B2C Fintech Support Competitive Analysis.md`.

Four considerations from the competitive landscape that are not yet captured in the 2030 model and should inform B2C product design decisions before the 2027 wallet launch.

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


## B2B Banking Evolution *(2028+)*

> Full business context: `checkout-business-context.md` → Banking Evolution.

From 2028, Checkout.com will begin offering banking products to merchants — storing funds and paying interest on merchant balances. This is a meaningful evolution from the current PSP model and will require deliberate changes across the care flywheel.

### Query taxonomy reset

The current B2B taxonomy is entirely payments-focused (payin, payout, settlement, disputes, integration, configuration). Banking products add entirely new first-level categories that don't exist today:

- Merchant balance management (depositing, withdrawing, viewing balance)
- Interest and yield queries (rate queries, interest calculation, accrual timing)
- Working capital / lending (if offered — cash advances, repayment, credit limits)
- Treasury and liquidity management (for larger merchants)

Every domain of the flywheel is affected: new query types for Input, new routing for Orchestration, new data and content for Fuel, new agent knowledge for Agent Experience, and new contact drivers for Insight & Prevention.

### AM/TAM role evolves

AMs and TAMs manage merchant relationships and currently escalate payments queries to Care. When merchants hold balances and earn interest, AMs and TAMs will start fielding banking questions — balance queries, yield comparisons, fund movements. This changes:
- What they need to know (banking product knowledge added to payments knowledge)
- What they escalate vs. self-serve (Sonar's knowledge base needs banking content)
- The nature of the structured intake form — banking query types need their own fields

### The 2030 flywheel assumptions need revisiting at 2028 transition

The 2030 model assumes a flywheel already spinning for B2B payments. Adding banking products will temporarily reset parts of it — new taxonomy to define, new Fuel (data + content) to build, new agent specialisms to develop. The transition should be planned as a discrete phase rather than assumed to be absorbed seamlessly.

### Competitive benchmarks shift for B2B

For B2B payments, the benchmark is Stripe and Adyen. For B2B banking, the relevant comparators become Revolut Business, Starling Business, and Tide — digital-first business banks. These have fundamentally different support models (and different regulatory floors) to PSP competitors.


## Now vs 2030

| Capability | What we have now (2026) | In 2030 |
|------------|-------------------------|---------|
| **Input** | **B2B:** Email and Dashboard channels. **Query taxonomy:** Refreshed every 6–12 months, with some LLM assistance. | **B2B:** Email, Dashboard, **Phone, IM/Slack** channels. **B2C:** **Mobile app, Phone, IM** channels. **Query taxonomy:** LLM-driven, refreshed **quarterly** based on contact reasons from Reflex. |
| **Orchestration** | **B2B:** New support model rolling out this year — merchant and channel eligibility, some AI involvement. AI currently limited to Dashboard and some emails. | **B2B:** AI applied across all channels, based on support level (e.g. Premium/Standard), with rules for human escalation. **B2C:** Action-enabled AI by default on all channels, human escalation only when needed. |
| **Fuel** | **Data:** Primarily Payin data for payment queries in AI Agent & Agent tools, but high latency. Other data sources not yet suitable (standard/accuracy issues). **Knowledge:** Reactive, manual monthly content reviews from AI Agent chats and Agent knowledge captures. Focus on building Tutorials & Video content. | **Data:** Accurate, joined-up, accessible data easily available to AI-powered tools (MCPs etc.) with **low latency**. **Knowledge:** Proactive, **weekly** AI-assisted analysis of content gaps, reviewed and updated by Content teams. Public docs designed for customers with low payments knowledge; breadth of type (tailored guides/videos); surfaced by AI Agent. |
| **Agent Experience** | **Ticketing:** Zendesk for handling and solving tickets. **Tooling:** Payment, User data, AI knowledge. Initial investment in Internal AI Agent to suggest and perform actions with human-in-the-loop. | **Ticketing:** Zendesk scaled for B2B and B2C; relevant Agent teams receive AI-escalated contacts. **Tooling:** Action & Knowledge Internal AI Agent suggests tasks **proactively** based on query context and gets Agent approval for actions. |
| **Insight & Prevention** | **Insights:** Building Reflex (AI insights) to analyze and synthesize contact root causes. **Prevention:** Planning governance model for contact reduction based on Reflex outputs. | **Insights:** **Weekly** contact reasons reported proactively using Reflex, shared with Product teams. **Prevention:** Reflex generates AI **action plans** to resolve root causes for triage and escalation to Care & other Product teams to solve as BAU (like Stripe Minions). |

