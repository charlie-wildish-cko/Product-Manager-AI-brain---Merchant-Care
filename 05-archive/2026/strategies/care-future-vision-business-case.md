# Care: Future Vision and Architecture (2026–2030)

**Audience**: VP of Product · VP of Engineering · Chief of Product · Chief of Operations
**Owner**: Charlie Wildish, Product Manager — Merchant Care
**Date**: March 2026
**Status**: Working draft

> This document is the investment framing of a detailed technical strategy. The full year-by-year capability model is in [`care-capability-model.md`](../01-knowledge-base/strategy/care-capability-model.md).

---

## Executive summary

Checkout's support model will not scale linearly from thousands to millions of contacts. The current architecture handles volume through human effort. The 2030 model handles it through AI, automation, and a flywheel that turns every contact into a signal that prevents the next one.

**The vision**: A Care flywheel where AI resolves 80%+ of contacts autonomously, Agent Consultant reduces human handling time by 90%, and Reflex operates as an autonomous insights agent — diagnosing contact drivers and generating fix recommendations directly for product teams.

**The economic case**: Fin (AI) costs $0.90 per resolution. Our human agent cost per contact is ~$40. Every contact shifted from human to AI reduces unit cost by ~44x. The flywheel compounds this: fewer contacts mean lower total cost regardless of resolution method.

**The investment ask**: The current team (4 engineers, 2 Zendesk admins, 1 PM) can deliver the 2026 B2B roadmap. It cannot simultaneously build the B2C foundation required for the 2027 wallet launch. The Braavos wallet launches as a banking product — Consumer Duty, complaint handling, and vulnerable customer identification are regulatory obligations from day one, not post-launch features. Investment in 2027 is a regulatory requirement, not a growth bet.

**Decision required**: Approval to hire into Care Engineering and Zendesk/Platform Admin in H1 2027, ahead of the B2C wallet launch. Detail in Section 4.

**If we don't act**: The 2027 B2C wallet goes live without Consumer Duty tooling in Fin, without a formal complaint handling process, and without B2C content in the knowledge base. Each is a regulatory obligation at launch. The legal and reputational risk of a non-compliant banking product launch is the cost of inaction.

**What success looks like**:
- 2026: Fin involvement rate >80%; webform retired; Reflex MCP live (Q3); Agent Consultant phase 2 in production
- 2027: B2C wallet launches with phone, complaint handling, and Consumer Duty tooling live on day one
- 2030: Contact rate declining year-on-year; cost per contact declining; Reflex generating action plan recommendations for Product teams; 90%+ CSAT; 80%+ AI resolution across B2B

---

## 1. The strategic case

### Care is a unit economics problem, not a headcount problem

Support sits on the Loss side of the Product P&L. The goal is not to reduce absolute spend — transaction volume will grow and some cost grows with it. The goal is to reduce unit cost: cost per contact and cost per $1M processed. These metrics must fall even as volume rises.

Two north star metrics define every investment decision:

| Metric | Definition | Direction |
|---|---|---|
| **Contact Rate** | Contacts per 1M transactions | Decreasing |
| **Cost per Contact** | Total support spend ÷ total contacts | Decreasing |

Both are moved by the same flywheel. The investments below are the mechanism.

### The Care flywheel

Care operates as a six-stage model. Each stage feeds the next, creating a compounding loop rather than a linear cost structure.

| Stage | What it does |
|---|---|
| **1. Input** | Captures every support contact with the right query classification and through the right channel — the accuracy of everything downstream depends on this. |
| **2. Orchestration** | Routes each contact to the right resolution method (AI, self-service, or human agent) based on query type, merchant level, and channel. |
| **3. Fuel** | Provides AI and human agents with the data and knowledge they need to resolve queries accurately — Customer 360 context, payments data, and content coverage across the taxonomy. |
| **4. Agent Experience** | Equips human agents with AI-suggested actions, natural language data queries, and automated workflows so they handle only what AI cannot. |
| **5. Insight and Prevention** | Analyses every contact to identify root causes, surfaces them to Product and Content teams, and tracks whether they get fixed — turning contact volume into a signal that reduces future volume. |
| **6. Governance** | Maintains consistent SLA adherence, CSAT, and QA as volume scales, and ensures regulatory compliance (Consumer Duty for B2C). |

The loop that makes this compound: better Fuel (data, content) → better AI resolution (Orchestration) → more contacts resolved without agents → better insight data (Insight and Prevention) → product fixes that prevent contacts → fewer contacts entering the system at Input. Each investment in the flywheel accelerates the stages that follow.

### The flywheel argument

Each investment compounds the next. To reach the 2030 state, the 2027 B2C foundations must be in place; to have those foundations ready for the wallet launch, the build must start in mid-2026.

```
Better data (Customer 360, MCPs)
  → Better AI resolution (Fin)
  → Fewer human-handled contacts
  → Better insight data (Reflex)
  → Product fixes contact root causes
  → Fewer contacts still
```

This is not a linear cost model. It is a compounding one. The first investments (data, Fin, Reflex) are the highest leverage because they accelerate everything downstream. Delaying them delays the entire compounding cycle.

### The cost of inaction

**Unit cost today**: Human agent at ~$40 per contact; Fin at $0.90 per resolution. At current Fin involvement rates, most contacts still reach a human agent. The gap between where we are and 80%+ AI resolution represents significant avoidable cost at scale.

**The 2027 constraint**: The Braavos consumer wallet launches as a banking product. From day one, Checkout holds consumer funds — Consumer Duty applies immediately. This mandates complaint handling processes, phone channel availability, and vulnerable customer identification in Fin. These cannot be added post-launch. The current team cannot deliver 2026 B2B commitments and build this foundation in parallel.

**The competitive context**: Best-in-class AI resolution rates are 70–85% today, targeting >85% by 2027. Our 2030 target of 80% will be industry average by that point, not a differentiator. Against Stripe (B2B benchmark) and Monzo/Revolut (B2C benchmark), delaying flywheel investment means higher cost-per-contact and slower resolution times — visible to merchants and consumers as a service quality gap.

---

## 2. The 2030 customer experience

Three journeys illustrate what Care delivers at full flywheel maturity. Each is grounded in the product architecture described in Section 3.

### Journey A: B2B merchant — Standard tier

**Today (2026)**

A merchant notices a settlement discrepancy. They navigate away from the Dashboard to email support, or ask their Account Manager to raise a ticket on their behalf. They wait hours for a human response. When the agent receives the ticket, they spend time locating the merchant's entity structure, processing profile, and settlement history before they can begin diagnosing the issue.

**2030**

The merchant finds the answer without contacting support. Education Hub content and in-Dashboard contextual guidance surface the explanation at the point of confusion. If they reach Fin, it queries Customer 360 in real-time, pulls the relevant settlement data, and resolves the query autonomously — within the Dashboard session, before the merchant leaves. If the contact escalates to a human agent, the agent receives full merchant context pre-loaded and an Agent Consultant action suggestion within seconds of opening the ticket.

The experience is tiered by merchant level. Standard merchants receive AI-first resolution with async human fallback. Enterprise merchants receive faster SLAs and dedicated channels. Premium merchants receive a Named Support Engineer and synchronous access. Channel entitlements and SLAs are governed by Success Plans.

### Journey B: Platform Operator

**Today (2026)**

A Platform Operator contacts Checkout by email on behalf of one of their sub-merchants. The agent must first establish which sub-merchant the query relates to — a step that adds friction, delays resolution, and produces no data about the Platform's wider merchant portfolio.

**2030**

The Platform Operator uses Platform Embedded AI in their own portal. Fin knows the Platform Operator and resolves the query within their workflow, with full sub-merchant context — processing profile, payment history, open disputes. Most queries resolve without Checkout involvement. Complex escalations that do reach Checkout arrive with sub-merchant context, prior resolution history, and Platform identity already pre-loaded in Zendesk.

### Journey C: B2C consumer (2027 forward)

B2C support is structurally different from B2B. The volume is higher, the per-contact value lower, the relationship is with a consumer not a merchant, and the regulatory obligations (Consumer Duty, FOS, complaint handling) are materially greater. The support model must be designed for this from the start — not adapted from B2B.

A Braavos wallet consumer disputes a merchant charge. They initiate the dispute from the transaction view in the app. Fin detects a vulnerability signal in the conversation and adapts its tone. The query is classified instantly against the B2C taxonomy. Fin gathers evidence autonomously — transaction metadata, merchant details, timestamps. The outcome is delivered within the Consumer Duty timeframe. A human agent is involved only if Fin cannot resolve, and receives full context, dispute evidence, and a suggested response on handoff. The entire interaction is logged for regulatory reporting.

---

## 3. The Care product architecture

The Care flywheel runs across six operational domains. Each domain is delivered by named products that evolve year by year. The table below shows where each product stands today and where it needs to be.

| Product | What it does | 2026 | 2027 | 2028 | 2030 |
|---|---|---|---|---|---|
| **Fin** | Customer-facing AI Agent — first-line resolution via Dashboard, email, and mobile | Partially deployed; email + Dashboard contextual in progress | Primary B2B channel; webform retired; B2C deployed at wallet launch | Coverage extends to all B2B channels + B2C | 80%+ autonomous resolution across B2B, B2C, Platform |
| **Agent Toolkit** | Zendesk sidebar panel — surfaces Customer 360 data and context to agents | Merchant entity, processing profile, balances live Q1 | Full Customer 360 including B2C consumer data | Banking product data added | Real-time context; proactive anomaly alerts before agent reads ticket |
| **Agent Consultant** | AI layer in Zendesk — suggestions, NL data queries, QA, human-in-the-loop actions | SOP-based suggestions live; NL queries and QA in delivery | Two-mode operation: autonomous for permitted actions; HITL for confirmation-required actions | Banking-aware suggestions | 90%+ of agent tasks automated or AI-assisted |
| **Reflex** | Support insights engine — contact root cause analysis and automated outputs for Product and Content teams | On-demand insights dashboard live; MCP in development | Weekly automated contact reason reports + VoC integration | B2C and banking contact drivers included | AI-generated action plan recommendations and fix PRs for engineering review — not autonomous deployment |
| **Customer 360** | Centralised customer context across all Checkout sources | Merchant entity + processing profile live Q1; balances in progress | Full context including B2C consumer data | Banking product data (merchant balances, interest, yield) | Real-time, all customer types; low latency |
| **Docs and Education Hub** | Customer-facing and internal knowledge (support.checkout.com, technical docs, API reference, SOPs, agent knowledge base) | ~60% taxonomy coverage; monthly reactive updates | 80%+ coverage; quarterly AI-driven gap analysis; B2C content added | B2B expansion content added | 90%+ coverage; weekly AI-proposed updates; human approval cycle |
| **Platform Embedded AI** | Fin component embedded in Platform Operator portals — delivery model (API, widget, or SDK) to be defined | Vision only — depends on 2026 Platform identification foundations | Platform identification and context live in Fin and Zendesk | Platform Embedded AI deployed to first Platform Operators | Platforms self-serve the majority of sub-merchant queries |
| **Success Plans** | Merchant support tier model (Standard / Enterprise / Premium) | Phase I rolling out — Standard live Q2, Enterprise/Premium Q3 | Full B2B tiering live; B2C tier model defined | B2B expansion tiers extended | Stable; dynamic re-routing on tier change |
| **Zendesk** | Ticketing system — human handling, SLA, QA, routing | Live for B2B; basic routing; limited SLA differentiation | Skill-based routing, Jira integration, B2C brand; complaint handling live | Banking ticket categories; AM/TAM escalation flows | Automated classification, routing, SLA management |

### Critical blockers in 2026

Three dependencies gate significant downstream capability:

1. **Data latency fix** (Settlements, Balances via MCP) — gates Agent Consultant phase 2 and Fin autonomous resolution for balance and settlement queries. **Owner**: platform data team dependency; Care Engineering cannot resolve this unilaterally.
2. **Reflex MCP** (Q3 2026) — gates automated content gap identification, AI action plans for Product teams, and the product fix governance cycle. Owner: Care Engineering.
3. **B2C taxonomy definition** (required mid-2026) — gates all B2C content build, Fin B2C configuration, and Consumer Duty compliance readiness for the 2027 wallet launch. Owner: Care PM + Operations.

---

## 4. The team

### Today

| Domain | Roles | Headcount |
|---|---|---|
| Care Product | PM | 1 |
| Engineering | Engineers + Engineering Manager | 4 engineers + 1 EM |
| Zendesk / Platform Admin | Zendesk admins | 2 |
| Shared (limited allocation) | Product Data Scientist; part-time Data Engineer | Shared with wider teams |

Fin administration is a shared responsibility across Product and Content — there is no dedicated Fin owner. The Engineering Manager's current span approaches the limit with engineers and Zendesk admins combined. Data engineering capacity is constrained by shared allocation.

The team can deliver the 2026 B2B roadmap. It cannot simultaneously build the 2027 B2C foundation.

### How the team needs to evolve

Investment asks begin in 2027. Each phase is gated to a product launch or capability requirement.

Note: this table covers the product and engineering team. Ops agent headcount (support agents, QA, scheduling) is owned by Care Operations and is not in scope here — but B2C will require separate ops capacity planning as volume scales, including potential BPO for first-line phone and chat. That workstream should be owned by the Director of Operations in parallel to this engineering investment.

| Domain | 2026 (now) | 2027 — B2C launch + B2B scaling | 2028 — B2B and B2C expansion | 2030 — steady state |
|---|---|---|---|---|
| **Care Product** | 1 PM | 1 PM | 1–2 PM — B2C product scope expands the PM surface area materially | TBC |
| **Engineering** | 4 engineers + 1 EM | +1–2 engineers — B2C Fin configuration, Consumer Duty tooling, data pipeline capacity; at or near EM span limit | +1 engineer if not already at span limit — B2B and B2C expansion, data infrastructure | Stabilises; AI tooling absorbs volume growth without linear headcount increase |
| **Zendesk / Platform Admin** | 2 admins | +1 admin — B2C Zendesk brand, complaint handling workflow configuration, Consumer Duty escalation flows | Stable unless banking adds significant new configuration scope | Stabilises |

**Note on operational process design**: Engineering build cannot begin before the underlying processes are designed. Consumer Duty complaint handling SLAs, vulnerable customer policy, and phone channel SLA framework must be defined by Operations and Legal before the engineering work is scoped. This is a parallel workstream that needs to start in Q2 2026.

### What the investment enables

**2027 B2C launch, without additional resource**: Fin deployed to B2C without vulnerability detection. Zendesk not configured for Consumer Duty complaint handling. No formal complaint process at wallet launch. Each is a regulatory obligation — not a feature decision.

**2027 B2C launch, with investment**: Consumer Duty and complaint handling built into the product from day one. Phone channel live at launch. B2C taxonomy defined and content in Docs and Education Hub before launch. Fin B2C configured and tested before go-live. Regulatory risk mitigated at launch.

**2030**: As AI capability matures and Reflex takes on autonomous diagnosis, the engineering maintenance burden per product stabilises. Team growth flattens. The compounding flywheel means the same engineering headcount handles significantly higher contact volume at lower unit cost.

---

## 5. What success looks like

Baselines for current Fin involvement rate, AI resolution rate, and blended cost per contact are owned by the Product Data Scientist and are flagged as open items to be confirmed before this document is finalised.

| Milestone | Target | Metric | Baseline (open) |
|---|---|---|---|
| **2026** | Fin involvement rate >80% | Contacts where Fin was first point of contact and the merchant did not subsequently submit a separate channel contact for the same issue | TBC — confirm with Product Data Scientist |
| **2026** | Fin resolution rate improving toward 70% | Contacts fully resolved by Fin without human handoff | TBC |
| **2026** | Reflex MCP live (Q3); Agent Consultant phase 2 in production; webform retired | Delivery milestones | N/A |
| **2027** | B2C wallet live with Consumer Duty compliance from day one | Regulatory requirement | N/A |
| **2027** | B2B AI resolution rate >75% | AI resolution rate | TBC |
| **2028** | B2B and B2C expansion milestones — confirmed once banking product scope is defined (decision gate: Q4 2027) | TBC | N/A |
| **2030** | Contact rate declining year-on-year | Contacts per 1M transactions | TBC |
| **2030** | Cost per contact declining year-on-year | Total support spend ÷ total contacts | TBC — blended cost per contact (weighted AI + human) to be confirmed |
| **2030** | 90%+ CSAT; 80%+ AI resolution across B2B | Customer satisfaction; AI resolution rate | TBC |
| **2030** | Reflex generating action plan recommendations for Product teams | Action plans generated; fix PRs raised for engineering review | N/A |

---

## Appendix

| Reference | File |
|---|---|
| Full capability model (year-by-year per flywheel stage) | [`care-capability-model.md`](../01-knowledge-base/strategy/care-capability-model.md) |
| Care flywheel stages and 2030 vision | [`care-product-model.md`](../01-knowledge-base/strategy/care-product-model.md) |
| Support scale principles | [`support-scale-principles.md`](../01-knowledge-base/strategy/support-scale-principles.md) |
| 2026 deliverables | [`2026 deliverables.md`](../2026%20deliverables.md) |
| KPI definitions and P&L framework | [`kpi-definitions.md`](../01-knowledge-base/metrics/kpi-definitions.md) |
