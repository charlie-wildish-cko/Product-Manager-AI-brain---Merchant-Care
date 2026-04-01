# Target Operating Model — Merchant Care & Support (2026–2030)

**Document Purpose**: Defines how the Care and Support function must evolve to sustain service quality and economics at scale through 2030. Intended to align VP Product, Director of Operations, and Director of Operations Excellence on a five-year operating model.
**Audience**: VP Product · Director of Operations · Director of Operations Excellence
**Status**: Draft | **Last Updated**: March 2026 | **Owner**: Charlie Wildish

---

## 1. Strategic Context

### The Case for Change

Transaction volume is projected to grow 5–10x by 2030. At the current model — generalist agents handling all contact types at ~$40 per contact — support cost scales linearly with volume. That is not viable against revenue growth and competitive pressure. The only path to sustainable unit economics is an operating model where AI resolves the majority of contacts and human agents are reserved for complex, high-judgment cases.

### Strategic Goals

- Reduce contact rate (contacts per 1M transactions)
- Reduce cost of support (cost per contact)

### North Star and Guardrail Metrics

| Type | Metric | 2026 Baseline | 2030 Target |
|---|---|---|---|
| North Star | AI resolution rate | ~15–20% (to establish) | 80%+ |
| North Star | Cost per contact | ~$40 (to establish) | 40%+ below 2026 |
| North Star | Re-contact rate | Not tracked | <5% |
| Guardrail | Merchant CSAT | Current baseline | Must not decline |
| Guardrail | SLA adherence | Current baseline | Must not decline |

**Unit cost reference**: Fin costs $0.90 per resolution; human agent ~$40. Every point of AI resolution rate improvement compounds cost savings across the full volume base.

**The Klarna precedent**: Klarna's 2024 AI deployment achieved 66% resolution rate but optimised for speed over quality. Trust erosion drove a $152M net loss by H1 2025 and a quiet reversal to a hybrid model. The lesson: resolution rate is a vanity metric without re-contact rate. This TOM is designed to avoid that failure mode.

### 2026 Deliverable Anchor

This TOM spans the full 2026 roadmap and provides the operating model context for all Care Product deliverables, including: Improve Fin Resolution Through Procedures (Q2), Reflex Phases 1–3, Customer 360 / Merchant Context, Agent Consultant, Support Model Tiering, and B2C Support Launch (2027).

---

## 2. Current State (As-Is)

### What Works Today

The current model reliably handles contact volume through well-trained generalist agents. Zendesk routing is functional. Fin is deployed and resolving a minority of contacts. The team understands the merchant base and escalation paths are established.

### Where It Breaks Down

- **Fin is under-owned.** Responsibility is shared across Product, Content, and Zendesk Admins. No named owner means no accountability for resolution rate, accuracy, or Procedure quality.
- **Knowledge is reactive.** Articles are updated monthly at best. No freshness SLA. At scale, a single stale Procedure causes systematic resolution failures across hundreds of contacts before anyone notices.
- **QA is agent-focused, not AI-focused.** Sampling-based QA works when humans handle 100% of contacts. When AI handles 80%, cohort-level failure is invisible to the current QA model.
- **No contact prevention loop.** Support signals reach the Product team informally, if at all. There is no structured mechanism to convert contact drivers into Product team commitments.
- **Headcount scales with volume.** The team grows when contacts grow. This model becomes unsustainable at projected volume.

### Capability Gaps

Capabilities are organised across five industry-standard clusters (Deloitte / COPC / Gartner frameworks), adapted for an AI-first PSP support function.

**Cluster 1: Service Strategy & Governance**

| Capability | Current Maturity | Required Maturity | Gap |
|---|---|---|---|
| Channel architecture and prioritisation | L2 — email + webform + Fin deployed | L4 — Fin as primary; webform retired; channel mix optimised by segment | Fin not yet primary; webform still active |
| Service level design | L2 — SLA tiers exist; enforcement inconsistent | L4 — tier-aware SLAs automated; dynamic re-routing | Salesforce tier data not live in Zendesk |
| Regulatory and compliance management | L1 — B2B only; no Consumer Duty obligations | L4 — Consumer Duty live at B2C launch; complaint SLAs; FOS management | Entire consumer compliance function to build |
| AI governance and decision rights | L1 — no formal governance; ownership distributed | L4 — named AI owner; escalation policy; audit trail; opt-out mechanisms | No owner; no policy; no logging standard |
| Workforce and capacity planning | L1 — headcount scales with volume | L4 — skill-based, right-sized to AI resolution rate | No structured mechanism; headcount tracks volume |

**Cluster 2: Process & Operations**

| Capability | Current Maturity | Required Maturity | Gap |
|---|---|---|---|
| Case management and routing | L2 — Zendesk routing functional; tier rules partial | L4 — fully automated; tier-aware; AI confidence-scored routing | Routing not AI-aware; tier enforcement inconsistent |
| Escalation design and warm handoff | L1 — transcript-only handoff | L4 — full context assembled pre-read: transcript + Customer 360 + history + AI-suggested action | Agent Consultant not live; no context assembly |
| Quality assurance | L1 — sampling-based, agent-focused | L4 — 100% auto-scored; cohort anomaly detection; AI-specific QA | No AI QA process; systematic failures invisible |
| Complaint and dispute handling | L2 — basic dispute workflow; no Consumer Duty | L4 — regulated complaint workflow; 8-week SLA; FOS tracking | Consumer Duty process and tooling not built |
| Contact prevention and root cause | L1 — informal; no Product team accountability | L4 — structured weekly cycle; Product commit mechanism; volume reduction tracked | No governance loop; signals informal only |

**Cluster 3: Knowledge & Content**

| Capability | Current Maturity | Required Maturity | Gap |
|---|---|---|---|
| Knowledge base management | L1 — reactive updates; no freshness SLA | L4 — weekly AI-assisted review; zero articles >90 days; SLAs enforced | No SLA; no gap identification; monthly cadence at best |
| Content for AI consumption | L1 — content written for human agents | L4 — structured for AI parsing; Procedure-ready; coverage mapped to full taxonomy | Content not structured for Fin Procedures |
| Domain expertise and taxonomy | L2 — agent knowledge strong; not systematised | L4 — full taxonomy mapped; payment domain embedded in Fin knowledge | Taxonomy not fully mapped to AI coverage |

**Cluster 4: Technology & Automation**

| Capability | Current Maturity | Required Maturity | Gap |
|---|---|---|---|
| Conversational AI and self-service | L2 — Fin deployed; limited Procedures | L4 — 80%+ taxonomy covered by Procedures; version-controlled; Reflex-tuned | No Procedure library; no tuning cycle |
| Agent assist and augmentation | L1 — manual data retrieval | L4 — AI-suggested actions; NL data queries; 90%+ task automation | Agent Consultant not live |
| Customer data and context | L1 — basic entity data; >500ms latency | L4 — real-time context (<100ms): entity + balances + transactions + anomaly detection | Latency issue; Settlements/Balances incomplete |
| Analytics and reporting platform | L1 — manual dashboards; no automated insight | L4 — automated weekly digest; spike detection; Jira integration; content gap flagging | Reflex not yet operational |
| Platform integration and data pipeline | L2 — Zendesk + Intercom connected; Salesforce partial | L4 — Salesforce tier data live; Fin conversation ingestion; MCP layer operational | Salesforce → Zendesk pipeline; Fin API export issue |

**Cluster 5: People & Capability Development**

| Capability | Current Maturity | Required Maturity | Gap |
|---|---|---|---|
| Agent skills and domain expertise | L2 — generalist; strong payment knowledge | L4 — specialist by domain (disputes, Premium, regulatory); depth over breadth | Generalist model; no specialist tracks |
| AI operations roles and skills | L0 — roles do not exist | L4 — Fin Owner, QA Analyst (AI Audit), Conversation Designer, Automation Specialist | All AI ops roles to hire or develop |
| Performance management | L2 — agent metrics tracked; no AI-specific metrics | L4 — AI resolution rate, re-contact rate, accuracy rate tracked with owner accountability | No AI performance owner or OKRs |
| Change and adoption management | L1 — ad hoc | L3 — structured programme for agent role transition; AI tools adoption tracked | No structured change programme |

---

## 3. Target State (To-Be)

The 2030 model operates on inverted economics: AI resolves 80%+ of contacts; human agents are specialists handling the 20% that requires judgment. The work shifts from handling volume to governing the system that handles volume.

### 3a. Capabilities

The 2030 target state requires maturity across five clusters. Each capability is described as *what the function must be able to do*; the technology and roles that enable it are in Sections 3b and 3c.

**Cluster 1: Service Strategy & Governance**

| Capability | Target State | Why It Matters |
|---|---|---|
| Channel architecture and prioritisation | Fin is the primary contact channel across B2B, B2C, and Platform. Channel mix is actively managed by contact type and merchant segment. Webform retired. | Channel design determines where and how AI can be applied. A fragmented channel mix caps AI resolution rate. |
| Service level design | Tier-aware SLAs enforced automatically (Standard 24h / Enterprise 8h / Premium 2h). Escalation thresholds tuned by tier and confidence score. Tier data refreshed daily from Salesforce. | SLA adherence is a guardrail metric. Incorrect tier routing is the primary cause of Premium/Enterprise CSAT failure. |
| Regulatory and compliance management | Consumer Duty obligations live at B2C launch (2027): 8-week complaint SLA, FOS management, vulnerable customer identification, AI right-to-opt-out. Deterministic AI logging for all decisions. | A missed Consumer Duty obligation is a regulatory breach. Cannot be retrofitted post-launch. |
| AI governance and decision rights | Named AI owner with full decision authority. Escalation policy defines three action types for every Procedure: Autonomous, Recommend-and-Wait, Escalate. Audit trail on all AI decisions. | At 80%+ AI resolution, governance failure is systemic. Every unowned AI decision is a compliance and trust risk. |
| Workforce and capacity planning | Quarterly skill-based capacity reviews tied to AI resolution rate. Explicit right-sizing mechanism. Headcount grows with complexity, not volume. | The current model where headcount tracks volume becomes unsustainable at 5–10x transaction growth. |

**Cluster 2: Process & Operations**

| Capability | Target State | Why It Matters |
|---|---|---|
| Case management and routing | Fully automated routing: AI confidence score, merchant tier, and contact type determine routing before any human sees the ticket. AI handles 80%+ first-attempt; remainder routed to specialist by skill. | Routing is the first decision point. Errors here propagate to every downstream metric. |
| Escalation design and warm handoff | Before the agent reads the ticket, Agent Consultant assembles: Fin transcript, Customer 360 snapshot, ticket history, Reflex insight, and AI-suggested action. Re-contact rate is the primary quality metric. | Re-contact rate is the quality signal. A failed escalation — one that generates a second contact — costs $40 and erodes trust. |
| Quality assurance | 100% of contacts auto-scored. Cohort-level anomaly detection identifies systematic failures (e.g. all SEPA resolutions wrong) before customer impact. Human QA reserved for exception review. | When AI handles 80% of contacts, sampling-based QA cannot detect systematic failure. The model inverts: QA becomes data analysis, not coaching. |
| Complaint and dispute handling | Regulated complaint workflow: dedicated routing, specialist handlers, 8-week SLA enforced, FOS tracking. High-value dispute handling by domain specialists with full context assembly. | Complaints are a legal obligation and a CSAT risk. Complex disputes handled without context cause re-contacts and trust erosion. |
| Contact prevention and root cause | Weekly Reflex cycle: top contact drivers quantified and delivered to Product leads. Product teams commit to quarterly fixes. Volume reduction tracked post-fix. | The only lever that reduces contact rate rather than cost per contact. Prevention compounds — each fix reduces future demand permanently. |

**Cluster 3: Knowledge & Content**

| Capability | Target State | Why It Matters |
|---|---|---|
| Knowledge base management | Weekly AI-assisted review cycle. Zero articles older than 90 days. Freshness SLAs enforced, not aspirational. Reflex identifies gaps; Knowledge Manager approves all changes. | Knowledge quality is the ceiling on AI resolution accuracy. A single stale Procedure causes systematic failures at scale before anyone notices. |
| Content for AI consumption | All knowledge structured for AI parsing, not just human browsing. Fin Procedures cover 90%+ of contact taxonomy. Content mapped to contact types with coverage tracked. | An AI that cannot find or parse relevant content will hallucinate or escalate. Coverage gaps directly cap resolution rate. |
| Payment domain expertise | Full payment taxonomy embedded: failed payments, settlements, disputes, 3DS, FX, webhooks, onboarding. Knowledge current against product changes and regulatory updates. | PSP support requires deep domain specificity. Generic knowledge bases fail on payment-specific queries. Domain gaps are the primary driver of escalation in this sector. |

**Cluster 4: Technology & Automation**

| Capability | Target State | Why It Matters |
|---|---|---|
| Conversational AI and self-service | Fin resolves 80%+ of contacts via Procedures covering the full taxonomy. Procedures version-controlled, accuracy-tested, Reflex-tuned. Confidence scoring drives autonomous vs. escalation decisions. | This is the primary cost lever. Every 10-point gain in AI resolution rate reduces cost-per-contact by ~$3.90 at current unit costs. |
| Agent assist and augmentation | AI-suggested actions, NL data queries, and task automation surface before agent reads ticket. 90%+ of routine agent tasks automated. Agents focus on judgment, not data retrieval. | Reduces handle time on the 20% of contacts that reach humans. Agent Consultant determines whether human handling is a cost or an investment. |
| Real-time customer context | Merchant context available to Fin and agents in <100ms: entity data, processing profile, balances, transaction history, anomaly alerts. | Without real-time context, Fin cannot accurately diagnose payment and settlement queries. Data latency is the most common cause of AI resolution failure in PSP support. |
| Analytics and insight delivery | Automated weekly digest of top contact drivers to Product leads. Spike detection, Jira integration, content gap flagging. Predictive contact detection in later phases. | Without systematic insight delivery, support signals do not reach Product teams. Contact prevention is impossible without this loop. |
| Platform integration | Zendesk + Intercom as the platform layer. MCP as the integration standard. Salesforce tier data live. Fin conversation content ingested for analytics. BigQuery as centralised data store. | Integration gaps are the primary execution risk. Latency issues, missing data pipelines, and API blockers are the most common failure modes in this build. |

**Cluster 5: People & Capability Development**

| Capability | Target State | Why It Matters |
|---|---|---|
| Specialist agent model | Agents hired and trained for domain depth, not breadth: disputes, Premium relationships, regulatory complaints, payment operations. Contact mix is 70%+ complex by 2030. | Generalists are optimised for routine volume. When AI handles routine volume, the remaining 20% requires a different hiring and training profile entirely. |
| AI operations roles | Dedicated AI ops team operational: Fin Owner, QA Analyst (AI Audit), Knowledge Manager, Conversation Designer. These roles do not exist in the current model. | An AI-first support function requires a new operating team. The current shared-responsibility model cannot govern a primary resolution product at scale. |
| Performance management | AI resolution rate, re-contact rate, and resolution accuracy are owned metrics with named owners and quarterly OKRs. Not shared KPIs — individual accountability. | Shared ownership of AI quality is a predictable failure mode (Klarna precedent). Clear ownership with OKRs is the governance mechanism. |
| Change and adoption | Structured programme for agent role transition to specialist model. AI tool adoption tracked. Role changes framed as career advancement, not narrowing. | The transition from generalist to specialist is the highest-risk org change. Unmanaged, it drives attrition of experienced agents at the point they are most needed. |

**Capability Maturity Roadmap**

| Cluster | Capability | 2026 | 2027 | 2028 | 2029 | 2030 |
|---|---|---|---|---|---|---|
| **Strategy & Governance** | Channel architecture | L2 | L3 | L4 | L4 | L4 |
| | Service level design | L2 | L3 | L4 | L4 | L4 |
| | Regulatory and compliance | L0 | L2 | L3 | L4 | L4 |
| | AI governance and decision rights | L1 | L3 | L4 | L4 | L4 |
| | Workforce and capacity planning | L1 | L2 | L3 | L4 | L4 |
| **Process & Operations** | Case management and routing | L2 | L3 | L4 | L4 | L4 |
| | Escalation and warm handoff | L1 | L2 | L3 | L4 | L4 |
| | Quality assurance | L1 | L2 | L3 | L4 | L4 |
| | Complaint and dispute handling | L2 | L3 | L4 | L4 | L4 |
| | Contact prevention and root cause | L1 | L2 | L3 | L4 | L4 |
| **Knowledge & Content** | Knowledge base management | L1 | L2 | L3 | L4 | L4 |
| | Content for AI consumption | L1 | L2 | L3 | L4 | L4 |
| | Payment domain expertise | L2 | L3 | L3 | L4 | L4 |
| **Technology & Automation** | Conversational AI and self-service | L2 | L3 | L4 | L4 | L4 |
| | Agent assist and augmentation | L1 | L2 | L3 | L4 | L4 |
| | Real-time customer context | L1 | L2 | L3 | L4 | L4 |
| | Analytics and insight delivery | L1 | L2 | L3 | L4 | L4 |
| | Platform integration | L2 | L3 | L4 | L4 | L4 |
| **People & Capability** | Specialist agent model | L1 | L2 | L3 | L4 | L4 |
| | AI operations roles | L0 | L2 | L3 | L4 | L4 |
| | Performance management | L1 | L2 | L3 | L4 | L4 |
| | Change and adoption | L1 | L2 | L3 | L3 | L4 |

_L1 = ad hoc · L2 = defined, basic measurement · L3 = owned, OKRs, tooling live · L4 = optimised, self-correcting_

---

### 3b. Organisation

**Structure**

The 2030 structure organises around two distinct functions that did not exist in the 2026 model: an AI Operations function (owning Fin, QA, and Knowledge) and a Specialist Escalation function (owning human-handled contacts, Consumer Duty, and Premium relationships). Product and Data functions remain consistent with the 2026 team; their work increasingly shifts toward system quality and insight delivery.

**Roles and Accountabilities**

| Role | Accountability | Decision Authority |
|---|---|---|
| Fin Owner | AI resolution rate; Procedure library; escalation thresholds; QA | Full authority on Fin config, Procedures, routing logic |
| Knowledge Manager | Content coverage; freshness SLAs; AI-assisted review cycle | Approve/reject all knowledge base changes |
| QA Lead (AI Audit) | 100% auto-scoring; cohort anomaly detection; accuracy reporting | Define QA scoring model; flag systematic failures |
| Specialist Agents | Complex escalations; Premium/Enterprise relationships; regulatory complaints | Resolution decisions within policy |
| Consumer Duty Lead | Complaint handling; 8-week SLA; FOS management; vulnerable customer ID | Complaint routing and escalation decisions |
| Reflex Owner (PM) | Weekly insight delivery; Product team engagement; Jira governance cycle | Contact driver prioritisation |
| Agent Consultant Owner (EM) | Context assembly; task automation; NL query infrastructure | Automation scope and deployment |

**Governance**

| Forum | Attendees | Frequency | Purpose |
|---|---|---|---|
| Fin Ops Review | Fin Owner, EM, QA Lead | Weekly | Procedure quality, top failures, escalation thresholds |
| Knowledge Review | Knowledge Manager, Fin Owner, Content | Weekly | Freshness SLAs, gap candidates, draft approvals |
| Reflex Digest | PM, Product Leads, Ops Director | Weekly | Top contact drivers, spike alerts, fix commitments |
| Capacity Review | Ops Director, PM, EM | Quarterly | Headcount vs AI performance; right-sizing decisions |
| Consumer Duty Review | Consumer Duty Lead, Compliance, PM | Monthly | SLA adherence, complaint queue, FOS status |
| Operating Model Review | VP Product, Ops Director, Ops Excellence Director, PM | Quarterly | North star metrics, maturity progression, investment |

---

### 3c. Technology

The technology stack maps directly to the Care flywheel (Input → Orchestration → Fuel → Agent Experience → Insight & Prevention → Governance).

| Capability | Technology Required | Current State | Gap |
|---|---|---|---|
| AI Resolution | Fin Procedures library; Customer 360 MCP | Fin deployed; no Procedure library | Procedure authoring workflow; latency fix for Settlements/Balances |
| AI Quality Assurance | Auto-scoring in Zendesk; cohort anomaly detection dashboard | Manual sampling only | QA tooling build required |
| Knowledge Lifecycle | CMS with SLA enforcement; Reflex gap flagging; version control | Basic Zendesk Guide | SLA automation; Reflex integration |
| Escalation and Handoff | Agent Consultant: context assembly, AI-suggested actions, NL query | Not live | Agent Consultant build (Q2–Q3 2026) |
| Support Tiering | Zendesk routing rules; Salesforce tier data feed (daily) | Partial; enforcement inconsistent | Salesforce → Zendesk data pipeline |
| Contact Prevention | Reflex MCP; Jira integration; weekly digest automation | Manual dashboards | Reflex Phase 1–3 build (2026) |
| Customer 360 | MCP with <100ms lookup; entity + balances + transactions | Basic entity data; >500ms latency | Latency fix; Settlements MCP (Q1 2026) |
| Consumer Duty | Zendesk complaint workflows; phone channel; FOS tracking; deterministic AI logging | Does not exist | Full build before B2C launch 2027 |
| Capacity Planning | Ops dashboard: AI resolution rate vs headcount vs cost | Not tracked | Dashboard build (2027) |

**Design principle**: technology enables the operating model — the model is designed first, then technology is selected or configured to fit. Zendesk and Intercom remain the platform foundation; MCP is the integration layer; Reflex is the insights engine.

---

## 4. Implementation Roadmap

### Sequencing Principles

Data and knowledge foundations must be in place before AI resolution can scale. AI resolution must reach a meaningful baseline before QA and governance tooling delivers return. Org changes (Fin ownership, specialist agents, Consumer Duty) are sequenced to match the point at which AI resolution rate makes them operationally critical.

### Phases

| Phase | Period | Key Changes | Success Criteria |
|---|---|---|---|
| 1 — Foundation | Q1–Q2 2026 | Reflex Phase 1 (data foundation); Customer 360 Settlements MCP; Support model tiering defined and signed off; Fin Procedures pilot | Reflex reporting to Product leads; Settlements latency fix live; tier enforcement in Zendesk; 3+ Procedures in production |
| 2 — Build | Q3–Q4 2026 | Fin as majority entry channel; webform retired; Agent Consultant live; Reflex MCP; Reflex Phase 2 (AI root cause); Fin Procedures expanding | AI resolution rate >20%; Agent Consultant on >50% of tickets; Reflex weekly digest running |
| 3 — AI-First | 2027 | B2C support launch; Fin ownership formalised; Consumer Duty tooling live; Platform Embedded AI; first Reflex-originated Product fixes | AI resolution rate 30%+; Consumer Duty SLA 100%; Fin Owner named with OKRs |
| 4 — Scale | 2028 | B2B Banking taxonomy; QA transition to AI audit; Reflex autonomous phase; Agent Consultant 60%+ task automation | AI resolution rate 50–60%; re-contact rate <10% |
| 5 — Target State | 2029–2030 | Capacity right-sizing; AI resolution rate managed to target; Reflex generates action plans | AI resolution rate 80%+; cost per contact 40%+ below 2026; CSAT maintained |

### Blocking Dependencies

1. **Merchant Context data latency fix (Q1 2026)** — blocks Fin from reliably resolving payment and settlement queries; blocks Phase 1 completion.
2. **Fin conversation content ingestion (H2 2026)** — Intercom API export issue blocks Reflex AI root cause analysis on Fin conversations; blocks Phase 2 insight quality.
3. **Reflex MCP deployment (Q3 2026)** — required before Agent Consultant can query Reflex insights; blocks autonomous insight cycle.
4. **Support model commercial sign-off (Q1 2026)** — leadership decision on tier definitions blocks Q2 routing rollout.
5. **Consumer Duty tooling (2026 H2)** — must be built and tested before B2C launch 2027; cannot be retrofitted post-launch.

---

## 5. Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Volume Trap — high resolution rate, rising re-contact rate | High | High | Track re-contact rate as a first-class metric from Phase 1; do not report resolution rate without it |
| Knowledge Debt — stale articles cause systematic failures at scale | High | High | Audit knowledge base before expanding Procedure coverage; weekly refresh cycle live before AI resolution rate exceeds 50% |
| Unmanaged Delegation — AI takes financial actions without designed handoff | Medium | High | Every Procedure explicitly categorises each action: Autonomous, Recommend-and-Wait, or Escalate. No exceptions. |
| Multiplicative Error — multi-step Procedures succeed 60% of the time at 95% per-step accuracy | High | Medium | Bound Procedure complexity; validate accuracy at each step before deployment; complex types directed to humans until accuracy confirmed |
| Fin Ownership Gap — shared ownership stagnates quality as AI resolution rate climbs | High | High | Define owner role in H1 2026; budget for 3–4 person team; OKRs before Phase 3 |
| Agent Role Resistance — generalists resist narrowing to specialist escalations | Medium | Medium | Frame specialisation as career advancement; invest in domain training; establish specialist career path before transition |
| Consumer Duty Launch Miss — capabilities not ready at B2C launch | Medium | High | Build and test in 2026; hire specialist staff before launch; run tabletop exercises on complaint scenarios |
| Capacity Right-Sizing Inertia — headcount accumulates as AI improves | Medium | Medium | Define right-sizing policy in 2028 before need is acute; prioritise voluntary attrition and internal moves |

---

## 6. Success Criteria

**Phase 1 complete when**: Reflex reporting to Product leads. Merchant Context latency fix live. Tier enforcement in Zendesk. AI resolution rate baseline established.

**Phase 2 complete when**: AI resolution rate >20%. Agent Consultant live on >50% of tickets. Reflex weekly digest operational. Webform retired.

**Phase 3 complete when**: AI resolution rate 30%+. B2C support live with Consumer Duty obligations met. Fin Owner named with quarterly OKRs tracking.

**Phase 4 complete when**: AI resolution rate 50–60%. Re-contact rate <10% and tracked. QA transition to AI audit complete.

**Target state achieved when**: AI resolution rate 80%+. Cost per contact 40%+ below 2026 baseline. Re-contact rate <5%. CSAT maintained at or above 2026 baseline. Headcount stable or declining despite volume growth.

---

## Appendix: Glossary

| Term | Definition |
|---|---|
| AI Resolution Rate | % of contacts resolved by Fin without human agent involvement |
| Re-contact Rate | % of resolved contacts where the merchant contacts again within N days — the primary quality signal |
| Fin Procedures | AI agent playbooks combining NL instructions with data queries and API calls |
| Customer 360 | Real-time merchant context: entity data, processing profile, balances, transaction history |
| Agent Consultant | AI augmentation layer in Zendesk: context assembly, AI-suggested actions, NL data queries |
| Reflex | Support insights engine: identifies contact drivers and converts them into Product team actions |
| MCP | Programmatic API interface for querying support data and insights |
| Consumer Duty | UK FCA regulatory framework for consumer financial services; applies to B2C support from day one |
| Warm Handoff | Pre-assembled context package (transcript + Customer 360 + history + AI-suggested action) delivered to the agent before they read the ticket |
| L1–L4 Maturity | L1 ad hoc · L2 defined, basic measurement · L3 owned, OKRs, tooling · L4 optimised, self-correcting |
| CSAT | Merchant Customer Satisfaction score — guardrail metric |
| FOS | Financial Ombudsman Service — UK consumer complaints escalation body |
| Flywheel | Input → Orchestration → Fuel → Agent Experience → Insight & Prevention → Governance |

---

## Appendix: Reference Sources

Capability framework research drawn from the following industry sources:

| Source | Relevance |
|---|---|
| [Deloitte: Customer Support Operating Models](https://www.deloitte.com/ch/en/services/consulting/perspectives/customer-support-operating-models-organisation-location-people-technology-data-iii-iii.html) | 9-layer operating model framework; capability cluster structure |
| [Deloitte: Target Operating Model Design](https://www.deloitte.com/us/en/services/consulting/services/target-operating-model-design.html) | Capability-based TOM: Strategy → Capabilities → Organisation → Technology |
| [McKinsey: How the operating model can unlock CX](https://www.mckinsey.com/capabilities/growth-marketing-and-sales/our-insights/how-the-operating-model-can-unlock-the-full-power-of-customer-experience) | Integrated CX operating model; performance management framework |
| [McKinsey: The contact center crossroads — humans and AI](https://www.mckinsey.com/capabilities/operations/our-insights/the-contact-center-crossroads-finding-the-right-mix-of-humans-and-ai) | Human/AI balance; workforce and capability transitions |
| [Gartner: Agentic AI will resolve 80% of customer service issues by 2029](https://www.gartner.com/en/newsroom/press-releases/2025-03-05-gartner-predicts-agentic-ai-will-autonomously-resolve-80-percent-of-common-customer-service-issues-without-human-intervention-by-20290) | AI resolution rate trajectory; capability requirements for agentic AI era |
| [Gartner: Customer Service Maturity Model](https://www.gartner.com/en/documents/3645319/use-gartner-s-maturity-model-to-improve-customer-service) | Maturity model structure; CX management capability dimensions |
| [Forrester: Best Practice Framework for Customer Service](https://www.forrester.com/blogs/forresters-best-practice-framework-for-customer-service/) | 8-category framework across Strategy, Process, Technology, People dimensions |
| [COPC Standards Release 8.0](https://www.copc.com/copc-standards/) | Operational process and metrics standards; AI governance additions; QA framework |
| [HDI Support Center Standard](https://www.thinkhdi.com/services/support-center-standard) | 5-dimension support centre standard: Processes, Integration, Technology, Staff, Information |
| [BCG: Agentic AI in Customer Service Transformation](https://www.bcg.com/publications/2025/new-frontier-customer-service-transformation) | Agentic AI operating model shifts; lean human operations model |
| [Cisco: Agentic AI to handle 68% of interactions by 2028](https://newsroom.cisco.com/c/r/newsroom/en/us/a/y2025/m05/agentic-ai-poised-to-handle-68-of-customer-service-and-support-interactions-by-2028.html) | AI adoption benchmarks and timeline validation |

---

**Document History**

| Version | Date | Changes |
|---|---|---|
| 0.1 | March 2026 | Initial draft |
| 0.2 | March 2026 | Condensed; duplicate capability definitions removed |
| 0.3 | March 2026 | Reworked to Deloitte capability-based TOM template |
| 0.4 | March 2026 | Capabilities reworked to industry-standard clusters (Deloitte, Gartner, COPC, Forrester, HDI); reference sources added to appendix |
