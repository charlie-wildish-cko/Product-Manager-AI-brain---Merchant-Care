# Care Strategy 2026–2030

**Authors**: Charlie Wildish, Oliver Westlake-Simm
**Last Updated**: April 2026

---

## 1. The Situation

Between 2026 and 2030, Checkout grows from ~2,000 Enterprise merchants to Enterprise, Platforms (ISV, Marketplace, SMB), and Consumer segments — millions of customers across B2B and B2C.

**TPV growth and contact forecast**

| Segment | 2026 | 2027 | 2028 | 2029 | 2030 |
|---|---|---|---|---|---|
| **Enterprise** | | | | | |
| TPV ($M) | 455,244 | 617,277 | 846,048 | 1,163,781 | 1,596,139 |
| Support contacts | 60,014 | 111,188 | 150,455 | 200,180 | 260,316 |
| **Platforms — ISV/Marketplace** | | | | | |
| TPV ($M) | 300 | 10,400 | 17,100 | 31,600 | 50,250 |
| Merchants | 2,250 | 12,600 | 54,200 | 127,300 | 246,000 |
| Support contacts | 35 | 1,243 | 2,073 | 3,789 | 6,216 |
| **Platforms — SMB** | | | | | |
| TPV ($M) | 0 | 100 | 1,250 | 3,800 | 8,250 |
| Merchants | 0 | 8,000 | 129,000 | 524,000 | 1,284,000 |
| Support contacts | 0 | 1,948 | 26,149 | 79,739 | 179,467 |
| **Consumer** | | | | | |
| Customers | 0 | 319,000 | 1,400,000 | 4,400,000 | 8,900,000 |
| Support contacts | 0 | 45,936 | 229,600 | 844,800 | 1,708,800 |
| **Totals** | | | | | |
| B2B contacts | 60,049 | 114,379 | 178,677 | 283,708 | 445,999 |
| B2C contacts | 0 | 45,936 | 229,600 | 844,800 | 1,708,800 |
| **Total contacts** | **60,049** | **160,315** | **408,277** | **1,128,508** | **2,154,799** |

---

## 2. The Problem

We are running a support model built for today's scale. It will not hold at 2030 volumes. Four structural problems are driving this:

1. **Support debt is accumulating, not being fixed.** Known contact drivers — TPA status, payment failures, settlement delays — remain unresolved. Product teams are incentivised to ship new products, not reduce contact volume. There are no quality guardrails per pillar or team.

2. **Every customer receives the same level of support, regardless of ROI.** That model does not scale to SMB or Consumer. At 2030 volumes, a flat support model is cost-prohibitive.

3. **AI alone does not solve this.** Fin reduces cost per contact significantly, but it cannot compensate for product gaps. A share of today's contacts requires human involvement and always will.

4. **The operating model is not designed for this shift.** Moving into SMB, Consumer, and Platform segments requires a fundamentally different support architecture. The current model has no mechanism to differentiate by segment, value, or contact type.

---

## 3. Our Goals

| Goal | Measured by | By 2030 |
|---|---|---|
| Drive towards a no-contact support experience | Contact rate per customer / 1M transactions / product | B2B: <1 per 1M; B2C: 5% of total customers per year |
| When support is needed: fast and high quality | AI resolution rate · Re-contact rate · AI and human CSAT / SLA | 80% AI resolution, <1 re-contact rate; CSAT: >90%, SLA 95% |
| Sustainable cost structure at 2030 volumes | Support cost as % of NR · Cost per contact by segment | TBC |

*Cost target by 2030 to be confirmed — required before goals are finalised.*

---

## 4. Our Approach

Care will operate as an AI-native support function: AI handles volume, humans handle complexity.

Fin is the primary contact channel across all segments. The level of human support a customer receives is determined by their segment, value, and ROI. Enterprise and Premium merchants receive specialist escalation for complex issues. SMB and Consumer contacts are resolved by AI with minimal human touch, except where regulation requires it — for example Consumer Duty for B2C.

This model rests on two integrated shifts, which must happen together:

**The Agentic Support Stack.** A connected set of AI agents that automates across the full contact lifecycle — from intake and triage through resolution, escalation, QA, and insight generation. This replaces the point-solution approach of deploying one AI tool at a time. Each component feeds the next: context enables resolution, resolution quality drives QA, QA outputs feed knowledge, and knowledge closes the loop back to resolution.

**AI Operations.** The team's primary work shifts from handling contacts to operating and continuously improving the AI system. Agents become specialists. The new operational work is Fin performance, knowledge quality, and contact prevention — not ticket volume.

Operating at this scale requires managing a resolution engine, not a ticket queue — instrumenting, maintaining, and continuously optimising the system that handles contacts. Every resolution path must be mapped and standardised before volume arrives; retrofitting AI into broken processes creates a performance ceiling that cannot be engineered away. *[Fin Blueprint: Transform Your Business — Infrastructure Mindset]*

### Resolution Architecture

Contact resolution operates across four layers, each handling a distinct class of contact:

1. **Instant AI Resolution** — Fin resolves routine queries using knowledge base and Customer 360 data. Target: 60–80% of contacts.
2. **Actionable AI** — Fin executes multi-step workflows via Procedures: refund status, settlement queries, webhook diagnostics. Moves beyond Q&A to action via backend integrations.
3. **AI-Assisted Handoff** — Fin escalates with full context assembled: transcript, Customer 360, Reflex signal, and AI-suggested next action. The agent receives a prepared brief, not a cold transfer.
4. **Human-Led Expertise** — Complex or high-value issues routed to specialists. Premium and Enterprise escalations only.

The transition from layer 3 to layer 4 is a named design constraint. A customer who repeats themselves after being transferred from AI to a human agent is a system failure, not a normal handoff. Full context continuity is non-negotiable. *[Fin Blueprint: Customer Experience — 4-Layer Resolution Architecture and "The Void"]*

### What this looks like in practice

- **AI resolves** — Merchant asks about a failed transaction. Fin resolves in 15 seconds using Customer 360 data and a Procedure. Cost: ~$0.90.
- **AI escalates** — Merchant requests a refund reversal. Fin escalates with full context assembled. Agent resolves in 2 minutes. Reflex detects a systemic issue and flags it to Product.
- **AI failure caught** — Fin makes an error in SEPA interpretation. Anomaly detection flags a 4% accuracy drop across 47 contacts. Fix deployed in 1 hour before customer impact.
- **Prevention cycle** — Reflex identifies webhook onboarding as the top contact driver (1,200/month). Procedure tuned (40% reduction). Product ships UI fix (60% reduction). 172 fewer contacts per week, sustained.

---

## 5. What This Means for How We Operate

80% AI resolution does not mean 80% less operational work. The work shifts from handling contacts to maintaining the system.

The metrics shift accordingly: First Response Time gives way to Automated Resolution Rate; ticket-level CSAT gives way to AI-specific CSAT and handoff rate; Cost per Ticket gives way to Cost per Automated Resolution. *[Fin Blueprint: Transform Your Business — Leadership and Change Management]*

| Dimension | Now (2026) | 2030 |
|---|---|---|
| **Agent role** | Volume handler across all contact types | Complex-case specialist; Premium/Enterprise escalations and regulated contacts only |
| **Fin ownership** | Shared across Product and Content; no dedicated owner | Explicit owner accountable for Fin resolution rate — formalised by Q2 2026 |
| **Knowledge base** | Reactive, monthly updates | Infrastructure; Reflex-driven weekly gap detection; Content team approves, not creates |
| **QA** | Sampling-based, qualitative, agent-focused | AI-audit-focused, quantitative; Reflex monitors systematic Fin errors; human QA for exceptions |
| **Cost structure** | Scales with contact volume | Fixed around specialist core; volume growth absorbed by AI |
| **Key metric** | AI resolution rate | AI resolution rate + re-contact rate + resolution accuracy + content-type coverage |

When AI absorbs 80%+ of contact volume, agent capacity does not simply reduce — it unlocks. That unlocked time is reinvested into proactive customer success (outreach to at-risk merchants before they contact), revenue influence (passing high-value expansion signals to account management), and structured product intelligence (human-resolved contacts feeding Reflex). This is how Care shifts from cost centre to value driver — and why headcount reduction is not the goal. *[Fin Blueprint: Economics — Capacity as Currency]*

---

## 6. What We Need to Build

### Technology: The Agentic Support Stack

*Owner: Charlie Wildish*

The Agentic Support Stack is the connected set of AI agents that automates across the full contact lifecycle. Each component is a discrete capability; together they form a self-improving system. Components map to the Care flywheel stages (Input → Orchestration → Fuel → Agent Experience → Insight and Prevention → Governance) and to the 2026–2030 delivery timeline.

*[Map components to flywheel stages and delivery timeline — see care-product-strategy-2026-2030.md for 2026–2030 build sequence]*

### People & Process: AI Operations

*Owner: Oliver Westlake-Simm*

AI Operations is the operating model for a team whose primary responsibility is the performance of the AI system, not the volume of contacts handled. It defines the roles, processes, and governance cadence needed to run Fin, maintain knowledge quality, detect failures, and convert contact signals into product action.

#### Essential Roles

Scaling to an AI-native support model requires three roles that do not exist in a human-first operation: *[Fin Blueprint: Org and System Design — Essential Scaling Roles]*

| Role | Responsibility | Checkout mapping |
|---|---|---|
| **AI Ops Lead** | Strategic owner of the resolution engine. Analyses resolution trends, identifies coverage gaps, manages the AI technical roadmap. Accountable for Fin resolution rate. | Named owner required by Q2 2026 — currently unassigned (see Open Decisions) |
| **Conversation Designer** | Owns tone, logic, and Fin personality. Designs Procedure flows and escalation logic. Ensures AI responses are accurate, on-brand, and efficient. | Maps to Fin Procedures authorship; currently split across Content and Product with no single owner |
| **Knowledge Manager** | Shifts from managing help articles for humans to managing structured data for LLMs. Owns content coverage targets, gap detection cycles, and Reflex-driven refresh cadence. | Existing role; scope expands significantly as Fin knowledge becomes load-bearing infrastructure |

#### Governance and Quality Loops

Fast and safe iteration requires three operational practices: *[Fin Blueprint: Org and System Design — Governance and Quality Loops]*

- **Continuous feedback**: Every human handoff is flagged as a knowledge gap. The AI Ops Lead reviews handoff patterns weekly to identify Procedure failures and content gaps.
- **Simulation testing**: Automated tests run against new Procedure deployments before go-live, covering edge cases and known failure modes. Changes are not deployed without passing simulation.
- **Shadow mode**: New Fin behaviours are monitored passively on live queries before being given response authority. Performance is validated at scale before full activation.

---

## 7. Plan to 2030

*[One row per year. Columns: Technology milestones (Agentic Stack), People and Process milestones (AI Operations), contact volumes, target AI resolution rate.]*

---

## 8. Open Decisions

- **Cost target**: Total support cost threshold by 2030 — required to finalise the goals table.
- **AI-first scope**: AI first for all segments is the stated approach — confirm this is agreed before committing.
- **Fin ownership**: Who owns the Fin resolution rate? Must be named before AI resolution becomes load-bearing. The AI Ops Lead role (see Section 6) defines what this person does — the decision is who.
- **Consumer Duty**: Design and build must start H2 2026. Sign-off process and delivery owner needed.

---

## Appendix: How Others Have Done This

- Fin AI Blueprint — Scaling AI Agents: https://fin.ai/blueprint/scaling-ai-agents/transform-your-business
- Klarna AI reversal (Forbes, 2025): https://www.forbes.com/sites/quickerbettertech/2025/05/18/business-tech-news-klarna-reverses-on-ai-says-customers-like-talking-to-people/
- What Klarna learned from its AI rollout (Time/Charter, 2025): https://time.com/charter/7378651/what-klarna-learned-from-its-ambitious-ai-rollout/
