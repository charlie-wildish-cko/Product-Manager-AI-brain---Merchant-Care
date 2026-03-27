# Care Product Strategy 2026–2030

**Framework**: Rumelt's Strategy Kernel — Diagnosis → Guiding Policy → Coherent Actions
**Audience**: VP of Product, Director of Operations, Director of Operations Excellence
**Last Updated**: March 2026

---

## DIAGNOSIS: From Support Operation to AI-Powered System

### The Situation

Checkout.com's merchant support model was built for a different scale. Today, the Care team resolves contacts predominantly through human agents across email and webform channels, supported by Fin in partial deployment and a Zendesk environment configured for basic routing. At current contact volumes, this model is functional. It will not be functional at 2030 volumes.

Three structural forces are converging. First, volume will grow as Checkout expands into new segments — B2C consumer wallet in 2027, B2B banking in 2028, and the Platform/ISV channel scaling through 2026 and beyond. Each segment brings distinct contact drivers, regulatory requirements, and resolution complexity. The current model has no architecture for this differentiation. Second, the cost structure is unsustainable at scale. Human agent handling costs approximately $40 per contact; Fin costs $0.90 per resolution. The difference is 44x. As volume grows, a model that remains human-first compounds cost faster than revenue. Third, the intelligence loop is broken. Merchant contacts contain rich signal about product failures, documentation gaps, and UX friction. Today, that signal is lost. There is no reliable mechanism to convert contact volume into product priorities, and no accountability for contact reduction at the product team level. The flywheel is spinning, but it is not self-improving.

The 2026 starting conditions make this harder: Fin is partially deployed, with incomplete Procedures and no webform replacement; Customer 360 data is live but settlements and balances remain high-latency; Reflex exists as a dashboard but does not yet feed Product teams systematically; Agent Consultant is in its foundation phase; and Zendesk supports basic routing without skill-based or tier-based logic. The foundations are present but not load-bearing.

### The Crux

Checkout must transition from a human-first support operation to an AI-native support system before volume growth makes the human-first model prohibitively expensive — while simultaneously building the governance, knowledge infrastructure, and escalation design that makes the AI model trustworthy at scale.

---

## GUIDING POLICY: AI-Native Care, Built for Scale and Complexity

### Our Overall Approach

The Care team will build an AI-native support system on the Care flywheel: Input → Orchestration → Fuel → Agent Experience → Insight and Prevention → Governance. Every investment decision will be evaluated against its contribution to the flywheel, not against standalone productivity metrics.

The guiding principle is that AI handles volume; humans handle complexity. By 2030, Fin resolves 80%+ of B2B contacts autonomously and the majority of B2C contacts, with human agents reserved exclusively for Premium/Enterprise escalations, regulated contacts, and novel issue types. This is not a headcount reduction target — it is a service architecture. Agents become specialists, not generalists. The cost structure shifts from scaling-with-volume to fixed-at-complexity.

Reaching 80% AI resolution requires three things to be true simultaneously: Fin must be fully deployed as the primary channel with complete Procedures coverage; the knowledge base must function as infrastructure with systematic refresh cycles, not as documentation updated reactively; and Reflex must operate as an autonomous intelligence layer that converts contact signals into product priorities and, ultimately, product fixes. These three things are the flywheel. Progress on any one of them without the others does not achieve the strategic goal.

The operating model transformation is not a 2030 problem — it is a 2026 design problem. The governance structures, ownership models, and quality metrics that will be required at 80% AI resolution must be designed now, tested at lower AI resolution rates, and scaled incrementally. Building them at the end is not possible.

### Key Strategic Choices

**We will:**
- Make Fin the primary support channel for all B2B contacts by end of 2026, retiring the webform and treating email as a secondary channel
- Build Customer 360 data access as a platform product — not a one-off integration — so that every AI and agent tool draws from a single context layer
- Operate Reflex as the accountability mechanism for contact reduction: Product teams will receive quantified contact driver outputs and be expected to commit to fix targets
- Design B2C and B2B Banking support models before the products launch, not after — Consumer Duty, complaint handling, and vulnerable customer identification must be embedded from day one
- Invest in knowledge infrastructure as a strategic asset: content coverage targets, Reflex-driven gap identification, and weekly review cadences replace monthly reactive updates

**We will NOT:**
- Expand human agent headcount in proportion to volume growth — scale is absorbed by AI, not headcount
- Build point solutions for individual contact types without assessing flywheel contribution
- Launch B2C or B2B Banking support as adaptations of the B2B model — each segment requires distinct taxonomy, routing logic, regulatory treatment, and content coverage
- Treat the AI resolution rate in isolation — it will be read alongside re-contact rate, resolution accuracy, and content-type coverage

---

## COHERENT ACTIONS: 2026–2030 Build Sequence

The actions below map to the Care flywheel stages and build on each other in sequence. They are not independent workstreams.

---

### 2026 — Foundations

**Goal: Make the flywheel load-bearing for B2B at scale**

**Input**
- Deploy Fin as the primary B2B contact channel; retire webform Q3 2026
- Establish 13 case types / 41 issue types as the authoritative taxonomy; begin Reflex-driven quarterly reviews

**Orchestration**
- Roll out Success Plans tiering: Standard live Q2, Enterprise/Premium live Q3
- Configure Fin escalation criteria per reason type; structured context passed on handoff to Zendesk
- Activate Platform identification in routing; surface Platform merchant context in Zendesk

**Fuel**
- Deliver Customer 360 phase 1: entity, processing profile, balances in Agent Toolkit Q1; context in Fin Q2
- Resolve data latency for settlements/balances — this unblocks Agent Consultant phase 2
- Launch Merchant Education Hub Q2; reach 60% taxonomy content coverage by year-end

**Agent Experience**
- Agent Consultant phase 1: SOP-based next-best-action suggestions live Q1
- Agent Consultant phase 2: NL data queries across Payments, Settlements, Balances, User Management Q2
- Skill-based routing in Zendesk live Q2-Q4; bi-directional Jira integration live Q1/Q2

**Insight and Prevention**
- Reflex phase 1: AI-powered contact analysis dashboard live Q1
- Reflex phase 2: merged support + NPS + research view; proactive spike analysis Q2
- Reflex MCP: queryable by AI tools Q3 — this is the unlock for AI action plans to Product

**Governance**
- SLA rules per merchant level enforced in Zendesk from Q3
- Begin Consumer Duty and B2C support model design H2 — must be complete before 2027 build begins
- Formalise Fin ownership accountability: assign explicit owner for Fin resolution rate by Q2

---

### 2027 — B2C Launch and AI Majority

**Goal: Launch B2C at regulatory standard; reach AI majority on B2B**

**Input**
- B2C taxonomy defined and Fin configured before wallet launch; phone channel live from day one
- Fin becomes primary B2B channel across all merchant levels; webform fully retired

**Orchestration**
- B2C channel eligibility and routing rules live; B2C SLA model defined per tier
- Fin resolution rate target: >60% B2B autonomous resolution

**Fuel**
- B2C content and SOPs built and reviewed before launch (not after)
- Customer 360 extended to cover consumer data; B2C Fin content reviewed monthly

**Agent Experience**
- Agent Consultant two-mode operation live: autonomous for permitted actions, HITL for sensitive ones
- Zendesk B2C brand scaled; Consumer Duty complaint handling process live from day one
- QA: Agent Consultant scores tickets against defined criteria; QA results automated

**Insight and Prevention**
- Reflex produces AI action plans for top 5 B2B contact drivers; Product teams commit to quarterly fix targets
- Product fix governance cycle formalised: monthly review, contact driver ownership by domain

**Governance**
- Consumer Duty compliance live from wallet launch: 8-week final response letters, FOS referral rights, vulnerable customer identification in Fin
- B2C CSAT tracked separately from B2B; AI resolution CSAT tracked separately from human

---

### 2028 — B2B Banking Launch and Autonomous Intelligence

**Goal: Launch B2B Banking at standard; Reflex begins autonomous triage**

**Input**
- Banking taxonomy defined before product launch; banking channels and routing live
- Taxonomy automation: Reflex proposes new reason types; Content team approves

**Orchestration**
- Banking merchant routing and agent specialist queues live in Zendesk
- Platform Embedded AI: Fin component deployed in ISV portals; Platforms begin resolving sub-merchant contacts

**Fuel**
- Banking product docs and agent SOPs built before launch
- AM/TAM knowledge base updated for banking product scope

**Agent Experience**
- Agent Consultant banking-aware action suggestions live
- Zendesk handles B2B, B2C, and Banking routing from a unified platform

**Insight and Prevention**
- Reflex: autonomous triage scoped and initial actions identified; targeted fix PRs generated for human review
- B2C and Banking action plans added to weekly Product briefing

---

### 2029 — System Maturity

**Goal: Stable, managed flywheel across all segments; weekly intelligence cycle**

- Reflex: automated weekly action plans; Product teams triage and commit on defined cadence
- Content coverage: 80%+ across B2B and B2C taxonomy; weekly gap analysis cycle
- Agent Consultant: high suggestion acceptance rate; autonomous actions cover majority of routine tasks
- Platform Embedded AI: reduces direct Checkout contact volume from Platform sources
- QA: AI-focused, quantitative sampling; automated CSAT reporting with Reflex-identified low-CSAT patterns

---

### 2030 — Optimised

**Goal: 80%+ AI resolution; agents as premium product; Reflex fully autonomous**

- **Fin**: resolves 80%+ of B2B contacts autonomously; AI-first across B2B, B2C, and Platform
- **Reflex**: fully autonomous insights agent — triages contact drivers, generates weekly action plans, executes targeted fix PRs in product team codebases; human team approves
- **Agent Consultant**: every ticket gets AI-suggested action; 90%+ acceptance rate; autonomous for permitted actions, HITL for sensitive ones
- **Docs and Education Hub**: 90%+ taxonomy coverage; Reflex-proposed updates on weekly human-approval cycle
- **Platform Embedded AI**: resolves majority of sub-merchant queries; Checkout handles complex escalations only
- **Governance**: SLA adherence and CSAT automated and self-reported; Consumer Duty and complaint handling auditable without manual effort

---

## Operating Model Implications

80% AI resolution does not mean 80% less operational work. The work shifts from handling contacts to maintaining the system.

| Dimension | Now (2026) | 2030 |
|---|---|---|
| **Agent role** | Volume handler across all contact types | Complex-case specialist; Premium/Enterprise escalations and regulated contacts only |
| **Fin ownership** | Shared across Product and Content; no dedicated owner | Explicit owner accountable for Fin resolution rate — formalised by Q2 2026 |
| **Knowledge base** | Reactive, monthly updates; ~60% coverage | Infrastructure; Reflex-driven weekly gap detection; Content team approves, not creates |
| **QA** | Sampling-based, agent-focused, qualitative | AI-audit-focused, quantitative; Reflex monitors systematic Fin errors; human QA for exceptions |
| **Cost structure** | Scales with contact volume | Fixed around specialist core; volume growth absorbed by AI |
| **Key metric** | AI resolution rate | AI resolution rate + re-contact rate + resolution accuracy + content-type coverage |

---

## Resource Allocation

**2026**: Full team capacity on B2B flywheel foundations — Fin deployment, Customer 360, Reflex, Agent Consultant, Success Plans. Consumer Duty design in H2.

**2027**: Split capacity — B2C launch preparation (H1) runs in parallel with B2B AI maturity improvements (ongoing). B2C requires taxonomy, content, Zendesk brand, regulatory compliance, and Fin configuration before launch.

**2028**: Banking product preparation mirrors B2C approach — taxonomy, content, routing before launch.

**2027 onwards**: Team growth investment required to deliver B2C foundations alongside B2B roadmap. Current team (4 engineers + EM) can deliver 2026 B2B roadmap; cannot simultaneously build B2C and Banking foundations without growth.

---

## Critical Assumptions

| Assumption | Risk if false |
|---|---|
| Data latency fix for settlements/balances is resolved in 2026 | Agent Consultant phase 2 and Fin settlement resolution blocked; AHT does not improve |
| Fin Procedures coverage reaches sufficient depth to retire webform Q3 2026 | Webform retirement delayed; Fin resolution rate plateaus |
| B2C wallet product scope defined mid-2026 | Taxonomy design, content build, and Fin configuration all delayed; B2C support not ready at launch |
| Product teams engage with Reflex outputs and commit to contact reduction targets | Insight and Prevention flywheel stage produces signal with no action; contact rate does not fall |
| Fin ownership is formalised before AI resolution rates become load-bearing | No accountable owner for Fin quality at scale; systematic errors go undetected |
| Consumer Duty process is designed in 2026 and embedded before B2C launch | Regulatory non-compliance from day one; cannot be remediated retrospectively |
