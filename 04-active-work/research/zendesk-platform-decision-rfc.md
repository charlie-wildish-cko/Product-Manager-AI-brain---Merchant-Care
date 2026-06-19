# RFC: Zendesk Platform Decision — Build / Buy / Keep

**Status**: Draft
**Created**: 2026-04-02
**Author**: Charlie Wildish
**Reviewers**: VP of Product · Director of Operations · Director of Operations Excellence · Engineering Manager
**Decision Deadline**: End of Q4 2026
**Contract Renewal Deadline**: June 2027

---

## Summary

Zendesk is the operational backbone of Checkout.com's Care function — the data source for Reflex, the agent workspace, the routing layer, and the integration hub for Fin, Jira, and Salesforce. The current contract renews June 2027. This RFC evaluates whether to renew (Keep), replace (Buy), or build a proprietary system, and produces a recommendation ahead of that decision.

**Strategic context**: All 2026 Care deliverables depend on Zendesk. Any replacement would disrupt the current roadmap. The evaluation must weigh the cost and risk of switching against the cost and risk of staying on a platform with known capability gaps.

---

## Background and Context

### Problem Statement

The Zendesk contract renews in June 2027. Before signing, we need a structured view of whether the platform can support the Care capability model through to 2030. Specific gaps have emerged:

- **AI workflow execution**: Zendesk supports AI suggestions (Copilot) but does not natively support agent-triggered, autonomous workflow execution — a core requirement for Agent Consultant phase 2+
- **Platform merchant data**: ISV/sub-merchant context is surfaced via custom integration, not native — fragile and limited
- **B2C compliance readiness**: Consumer Duty requires complaint handling, vulnerable customer detection, and phone channel from day one at wallet launch (2027); Zendesk supports this but requires configuration build-out
- **Pricing model shift**: Zendesk is moving to outcome-based pricing ($1.50–$2.00/Automated Resolution + add-ons of $50/agent Advanced AI, $35/agent QA, $25/agent WFM) — cost trajectory is unclear at scale
- **Vendor trust**: Systemic failures in Zendesk's own customer support, aggressive billing tactics, and non-auditable "Automated Resolution" charges represent tier-1 operational risk

### Current State

Zendesk is live for all B2B support handling. Key integrations in place or in delivery:

- Fin (Intercom) → Zendesk escalation
- Agent Toolkit (Customer 360 data panel in Zendesk sidebar)
- Agent Consultant (AI suggestions in Zendesk)
- Jira ↔ Zendesk bi-directional integration (in progress Q1/Q2)
- Salesforce → Zendesk case number sync (H2)
- Reflex data pipeline feeds from Zendesk tickets

The platform is not a simple tool — it is the data layer that every Care product depends on. Switching is a multi-quarter programme, not a lift-and-shift.

### Goals

- Produce a clear, defensible recommendation on platform direction before Q1 2027
- Identify what conditions would trigger a switch vs. a renewal negotiation
- Ensure 2026 roadmap delivery is not disrupted
- Anchor negotiation position if renewing
- Evaluate candidates against the desired platform architecture:**modular, flexible, and build-around** — the platform must allow us to plug in our own data sources, AI agents, and services without building for the platform's constraints

### Non-Goals

- This is not an evaluation of Fin (Intercom) — Fin is the AI layer and is evaluated separately
- This is not a case management redesign — the scope is the ticketing and agent platform only
- This does not commit to a migration timeline; it produces the decision and a path

---

## Candidate Evaluation

Candidates assessed: **Zendesk (Keep + Extend)**, **Intercom (Buy)**, **Plain / Pylon (Buy)**, **Build**.

Scored against the assessment requirements defined in the Appendix. Pricing is assessed separately below.

---

### 1. Multi-channel entry points

| Requirement                                    | Zendesk                                 | Intercom             | Plain / Pylon                          | Build |
| ---------------------------------------------- | --------------------------------------- | -------------------- | -------------------------------------- | ----- |
| Email ingestion                                | Native                                  | Native               | Plain: native; Pylon: limited          | Build |
| AI Agent escalation (Fin handoff with context) | Native via Intercom integration — live | Native (same vendor) | Plain: API only; Pylon: no             | Build |
| Live chat (B2B)                                | Via Sunshine Conversations (add-on TBC) | Native               | Pylon: native (Slack-first); Plain: no | Build |
| Instant messaging / Slack (2028–2029)         | Via Sunshine Conversations (add-on TBC) | Limited              | Pylon: native strength                 | Build |
| Phone / IVR (B2C, Consumer Duty)               | Zendesk Talk — native                  | No native phone      | No                                     | Build |
| Mobile app chat (B2C, 2027)                    | Via Sunshine Conversations              | Native               | No                                     | Build |
| Internal ticket submission (Account teams)     | Native                                  | Native               | Plain: yes; Pylon: limited             | Build |

**Assessment**: _TBD — to be completed after vendor research (Q3 2026)._

---

### 2. AI triage and classification

| Requirement                                    | Zendesk                                   | Intercom                                           | Plain / Pylon                  | Build        |
| ---------------------------------------------- | ----------------------------------------- | -------------------------------------------------- | ------------------------------ | ------------ |
| Auto-classification on escalation              | Via custom trigger / tag — not native    | Via Fin classifier — native                       | API-based only                 | Full control |
| AI agent handoff with context                  | Live via Intercom integration             | Native (same vendor)                               | API only                       | Build        |
| Pluggable external AI layer (Agent Consultant) | Supported via API + custom app — working | Supported but conflicts with native AI positioning | Plain: API yes; Pylon: limited | Full control |

**Assessment**: _TBD — to be completed after vendor research (Q3 2026)._

---

### 3. Routing logic

| Requirement                             | Zendesk                | Intercom          | Plain / Pylon              | Build        |
| --------------------------------------- | ---------------------- | ----------------- | -------------------------- | ------------ |
| Support plan / tier model (P0–P3)      | Native — configurable | Partial           | Plain: limited; Pylon: no  | Build        |
| Skill-based routing                     | Native — in delivery  | Basic             | No                         | Build        |
| SLA per tier and taxonomy value         | Native — configurable | Basic SLA support | No                         | Build        |
| Customisable ticket and customer fields | Native                 | Limited           | Plain: yes; Pylon: limited | Full control |
| Flexible tagging / taxonomy             | Native                 | Limited           | Plain: yes; Pylon: no      | Full control |

**Assessment**: _TBD — to be completed after vendor research (Q3 2026)._

---

### 4. Agent workspace

| Requirement                                                | Zendesk                                        | Intercom                     | Plain / Pylon              | Build        |
| ---------------------------------------------------------- | ---------------------------------------------- | ---------------------------- | -------------------------- | ------------ |
| Custom app embedding (Agent Consultant in sidebar)         | Native — live                                 | Supported                    | Plain: limited; Pylon: no  | Full control |
| Live customer data panel (CRM / Customer 360)              | Native sidebar app — live                     | Supported                    | Plain: limited             | Build        |
| Internal escalation (Jira, custom API)                     | Native Jira integration + custom apps          | API possible; no native Jira | Plain: API only            | Build        |
| Agent-triggered workflow execution                         | Not native; delivered via Agent Consultant     | Partial native AI actions    | No                         | Full control |
| Internal collaborator access (read/comment, no agent seat) | Via light agent seats — cost unclear at scale | Limited                      | Plain: yes; Pylon: limited | Build        |

**Assessment**: _TBD — to be completed after vendor research (Q3 2026)._

---

### 5. Data and permissions

| Requirement                         | Zendesk                                                 | Intercom                      | Plain / Pylon             | Build                      |
| ----------------------------------- | ------------------------------------------------------- | ----------------------------- | ------------------------- | -------------------------- |
| B2B / B2C data wall (BPO isolation) | Via brand separation + RBAC — configurable, not native | Workspace separation possible | Plain: limited; Pylon: no | Full control               |
| Role-based access control           | Native — granular                                      | Basic                         | Plain: basic; Pylon: no   | Full control               |
| 500-agent scale                     | Proven at enterprise scale                              | Unproven at this volume       | Not viable                | Dependent on build quality |

**Assessment**: _TBD — to be completed after vendor research (Q3 2026)._

---

### 6. Customer-facing experience

| Requirement                                    | Zendesk                 | Intercom             | Plain / Pylon           | Build |
| ---------------------------------------------- | ----------------------- | -------------------- | ----------------------- | ----- |
| Customer ticket portal                         | Zendesk Guide — native | Intercom portal      | Plain: basic; Pylon: no | Build |
| AI chat history alongside ticket history       | Requires configuration  | Native (same vendor) | No                      | Build |
| Account team thread visibility and email reply | Native                  | Native               | Plain: limited          | Build |

**Assessment**: _TBD — to be completed after vendor research (Q3 2026)._

---

### 7. Integrations & Knowledge (must-have)

| Integration                                  | Zendesk                           | Intercom                 | Plain / Pylon   | Build        |
| -------------------------------------------- | --------------------------------- | ------------------------ | --------------- | ------------ |
| Fin (Intercom) escalation with context       | Native — live                    | Native (same vendor)     | API only        | Build        |
| Jira bi-directional                          | Native integration — in delivery | API only                 | Plain: API only | Build        |
| Salesforce sync                              | Native integration                | API possible             | No              | Build        |
| Internal systems (Treasury, Card Processing) | Via Zendesk API + custom apps     | Via API                  | Plain: API only | Build        |
| Reflex data pipeline (outbound API)          | Live — working                   | Requires re-integration  | Requires build  | Full control |
| Knowledge sources                            | n/a                               | Synced with Intercom Fin |                 |              |

**Assessment**: _TBD — to be completed after vendor research (Q3 2026)._

---

### 8. Analytics and data extract

| Requirement                                        | Zendesk                                    | Intercom                        | Plain / Pylon | Build        |
| -------------------------------------------------- | ------------------------------------------ | ------------------------------- | ------------- | ------------ |
| Full ticket data extract via API (Reflex pipeline) | Live — working                            | Requires re-integration         | Limited       | Full control |
| Taxonomy-level reporting                           | Via Explore — native                      | Basic                           | No            | Build        |
| Billing auditability (AR charges per ticket)       | Non-auditable currently — a declared risk | $0.99/resolution — transparent | N/A           | Full control |

**Assessment**: _TBD — to be completed after vendor research (Q3 2026)._

---

### 9. Environment and configuration deployment

| Requirement                | Zendesk | Intercom | Plain / Pylon | Build        |
| -------------------------- | ------- | -------- | ------------- | ------------ |
| Sandbox / test environment | TBD     | TBD      | TBD           | Full control |
| Configuration as code      | TBD     | TBD      | TBD           | Full control |

**Assessment**: _TBD — to be completed after vendor research (Q3 2026)._

---

## Pricing Assessment

Pricing is assessed separately because it is a commercial question, not a capability question. The right platform at an unsustainable price is still the wrong choice.

### Zendesk (current)

Pricing model is shifting from per-seat to outcome-based:

- $1.50–$2.00 per Automated Resolution
- $50/agent/month Advanced AI add-on
- $35/agent/month QA add-on
- $25/agent/month WFM add-on
- Seat-based pricing for ~500 agents (current tier TBC)

At scale, the AR model could be materially more expensive than seat-based depending on Fin resolution rates. This must be modelled before renewal (see Open Questions). The AR billing mechanism is currently non-auditable — a contractual requirement, not a nice-to-have.

### Intercom (alternative)

- Fin: $0.99/Automated Resolution (vs. $1.50–$2.00 for Zendesk)
- Full platform pricing (ticketing, routing, agent workspace) not published at enterprise scale; requires RFI

The AI resolution cost is lower but the full platform cost comparison is unknown. Intercom consolidation would also require re-integrating Reflex, Jira, and Salesforce.

### Plain / Pylon

Lower headline cost but not viable at the required capability level. Not modelled.

### Build

Engineering cost is prohibitive. Not modelled.

---

## Options

### Option 1: Keep + Extend

Renew Zendesk at contract. Use the renewal as leverage to negotiate price, SLAs, and audit rights. Continue building the AI workflow layer (Agent Consultant) outside native Zendesk, and complete the B2C configuration build-out in 2026.

**What this means in practice:**

- Invest in Zendesk configuration for B2C: complaint handling, Consumer Duty flows, vulnerable customer flags, phone channel (Zendesk Talk)
- Negotiate on AR pricing, Advanced AI add-on costs, and response SLAs at enterprise scale
- Demand audit rights on "Automated Resolution" billing before signing
- Continue Agent Consultant as the AI workflow execution layer outside native Zendesk
- Accept that some capabilities (agent-triggered autonomous execution) require custom build

**Considerations:**

- Zero roadmap disruption — all 2026 deliverables are in flight on Zendesk
- Zendesk leads on routing depth, SLA management, compliance tooling, and must-have integrations across the current requirement set
- Migration to any alternative would consume 2+ engineers for 6–12 months
- Forethought acquisition (Resolution Learning Loop) indicates platform investment in AI workflow capability
- Zendesk's architecture is API-first and build-around — Agent Consultant, Agent Toolkit, and Reflex all follow this pattern today

**Risks and mitigations:**

| Risk                                                    | Likelihood | Impact | Mitigation                                                                                      |
| ------------------------------------------------------- | ---------- | ------ | ----------------------------------------------------------------------------------------------- |
| AR billing becomes unauditable/expensive at scale       | Medium     | High   | Demand audit rights and pricing caps in renewal contract; model volume scenarios before signing |
| Zendesk vendor support quality continues to deteriorate | Medium     | Medium | Escalate to enterprise account team; SLA for human support response times is contractual        |
| B2C configuration takes longer than expected            | Low        | High   | Begin Consumer Duty configuration design H2 2026; do not leave for 2027                         |
| Agent-triggered workflow execution gap widens           | Low        | Medium | Agent Consultant already fills this gap; watch Zendesk roadmap for native capability            |

---

### Option 2: Buy — Replace with Intercom

Migrate from Zendesk to Intercom as the primary platform before June 2027.

Intercom has meaningful advantages on AI chat history, Fin integration cost, and unified AI + ticketing UX. Known gaps against the requirement set include routing depth, SLA management, phone channel, and Consumer Duty compliance tooling. Migration cost would include Reflex re-integration, Jira re-integration, and team retraining (estimated 6–12 months engineering).

**Considerations**: Enterprise routing depth, SLA management, and phone channel maturity are the primary unknowns to assess. Full platform pricing at Checkout's scale is unpublished — requires RFI.

---

### Option 3: Buy — Replace with Plain or Pylon

Plain is API-first with a flexible data model and competitive pricing. Pylon is Slack-native and suited to B2B IM-first support. Neither has been assessed at 500-agent scale, and phone channel and Consumer Duty compliance tooling are not confirmed for either.

**Considerations**: Plain's routing configurability, custom object model, and API-first architecture warrant assessment. Pylon's native Slack/Teams channel support is relevant to the 2028–2029 IM requirement.

---

### Option 4: Build

Team capacity is 4 engineers + 1 EM. Building and maintaining enterprise-grade ticketing infrastructure would consume the team's full delivery capacity.

**Considerations**: Not viable as a primary path. Relevant only if no vendor meets requirements and a minimal custom layer is needed on top of an existing platform.

---

## Comparison Matrix

| Requirement area             | Zendesk                                                | Intercom                                                          | Plain / Pylon                 | Build                |
| ---------------------------- | ------------------------------------------------------ | ----------------------------------------------------------------- | ----------------------------- | -------------------- |
| Multi-channel entry points   | Strong — phone gap filled by Talk                     | Strong on chat/AI; no phone                                       | Pylon IM only; not full stack | Full control         |
| AI triage and classification | Working via Agent Consultant                           | Native advantage (same vendor as Fin)                             | API only                      | Full control         |
| Routing logic and SLA        | Native strength                                        | Insufficient at enterprise scale                                  | Not viable                    | Buildable            |
| Agent workspace              | Strong; agent-triggered execution via Agent Consultant | Supported; native AI conflicts with Agent Consultant              | Not viable                    | Full control         |
| Data and permissions         | Configurable; B2C wall requires design                 | Unproven at 500-agent scale                                       | Not viable                    | Full control         |
| Customer-facing experience   | Configurable                                           | Natural advantage (unified Fin history)                           | Not viable                    | Build                |
| Must-have integrations       | All live or in delivery                                | Requires full re-integration                                      | Not viable                    | Build                |
| Analytics and data extract   | Live; billing auditability is a gap                    | Requires Reflex re-integration                                    | Not viable                    | Full control         |
| Pricing                      | Unknown at scale; AR model needs modelling             | Lower AI cost ($0.99 vs $1.50–$2.00); full platform cost unknown | Lower but not viable          | Very high build cost |
| Migration risk               | None                                                   | High — 6–12 months                                              | Unknown at scale              | Highest              |

---

## Recommendation



## Implementation Plan

### Phase 1 — Capability gap analysis, cost modelling, and vendor evaluation (Q3 2026)

- Map full B2C configuration requirements to Consumer Duty obligations
- Model AR billing scenarios at Checkout's 2027 projected contact volume (use contact forecasting data)
- Identify Advanced AI add-on requirements — which features are mandatory vs. optional
- Request Zendesk enterprise roadmap briefing: what is on the roadmap for agent-triggered workflow execution, Platform multi-tenancy, and B2C tooling?
- RFI from Intercom on full platform capability (as a data point for negotiation leverage, not as a serious replacement candidate at this stage)
- Draft renewal terms and non-negotiables

### Phase 2 — Decision and contract (Q4 2026)

- Present RFC + recommendation to VP of Product, Director of Operations, Director of Operations Excellence
- Decision approved
- Begin contract negotiation with Zendesk account team using Q3 findings as leverage

### Phase 4 — B2C configuration build (H2 2026 → Q1 2027)

- Consumer Duty complaint handling flows configured in Zendesk
- Vulnerable customer flag designed and integrated with Fin and Agent Toolkit
- Phone channel (Zendesk Talk) enabled and IVR designed
- B2C SLAs defined and configured
- Must be complete before wallet launch — not added after

---

## Success Metrics

| Metric                               | Current | Target                                   | Timeline                  |
| ------------------------------------ | ------- | ---------------------------------------- | ------------------------- |
| Decision made and approved           | —      | ✓                                       | End Q4 2026               |
| Renewal terms agreed                 | —      | Audit rights + price protections secured | Q1 2027                   |
| B2C Zendesk configuration live       | L0      | L2 (Consumer Duty compliant)             | Before wallet launch 2027 |
| AR billing cost per resolved contact | Unknown | Modelled and capped contractually        | Q3 2026                   |

---

## Open Questions

1. **Q**: What is Checkout.com's current Zendesk tier and seat count?

   - **Why it matters**: Determines which add-ons are included vs. billed separately; sets the negotiation baseline
   - **Who can answer**: Engineering Manager / Finance
   - **Deadline**: Q3 2026
2. **Q**: What is the projected AR volume at 2027 and 2030 Fin resolution rates?

   - **Why it matters**: Determines whether outcome-based pricing is cheaper or more expensive than seat-based at scale
   - **Who can answer**: Charlie (contact forecasting + Fin involvement rate data)
   - **Deadline**: Q3 2026 (Phase 1)
3. **Q**: Does Zendesk's consumer complaint handling configuration satisfy Consumer Duty requirements in its current form?

   - **Why it matters**: If not, the configuration work required may change the cost/benefit calculation
   - **Who can answer**: Legal/Compliance + Director of Operations Excellence
   - **Deadline**: Q3 2026
4. **Q**: What is Zendesk's enterprise roadmap for agent-triggered workflow execution (beyond Copilot suggestions)?

   - **Why it matters**: If Zendesk builds this natively in 2026–2027, the Agent Consultant architecture may change
   - **Who can answer**: Zendesk enterprise account team (roadmap briefing, Q3 2026)
   - **Deadline**: Q3 2026
5. **Q**: Is Zendesk Sunshine Conversations included in our current enterprise tier, or is it a separate add-on?

   - **Why it matters**: Sunshine Conversations is the Zendesk mechanism for IM/Slack B2B support channels, which are required by 2028–2029. If it is billed separately at 500-agent scale, the cost must be factored into the renewal negotiation.
   - **Who can answer**: Engineering Manager / Zendesk account team
   - **Deadline**: Q3 2026

---

## Dependencies

- [ ] Legal/Compliance input on Consumer Duty configuration requirements (Q3 2026)
- [ ] Finance input on current Zendesk contract value and renewal timeline (Q2 2026)
- [ ] VP of Product and Directors alignment on renewal vs. replacement framing before vendor engagement
- [ ] Contact volume forecast + Fin resolution rate projections to model AR pricing (Charlie — Q2 2026)

---

## Related Documents

- `01-knowledge-base/products/zendesk.md` — Checkout.com Zendesk setup and capabilities
- `04-active-work/Zendesk Viability_ AI, Pricing, Market.md` — External market research on Zendesk strategic position
- `01-knowledge-base/strategy/care-capability-model.md` — Year-by-year capability requirements 2026–2030
- `01-knowledge-base/metrics/contact forecasting.md` — Volume projections for AR pricing model
- `01-knowledge-base/strategy/operating-model-at-scale.md` — 2030 vision implications
- `2026 deliverables.md` — Current roadmap dependencies on Zendesk

---

## Appendix: Vendor Assessment Requirements

Derived from [support platform flows](support%20platform%20flows.md). Use as a scorecard when evaluating any platform candidate — including Zendesk in renewal negotiation.

### 1. Multi-channel entry points

| Requirement                | Detail                                                                          |
| -------------------------- | ------------------------------------------------------------------------------- |
| Email ingestion            | Native ticket creation from inbound email                                       |
| Email user enrichment      | Auto-match inbound email to the correct org record; handle emails that belong to multiple orgs or have no match |
| Domain mapping             | Link email domains to org records (e.g. @checkout.com → Checkout.com org) so unrecognised senders can be resolved |
| AI Agent escalation path   | Receive handoff from AI Agent (Fin for now) with full conversation context      |
| Live chat with human agent | Native or integrated chat for B2B                                               |
| Instant messaging channels | Slack/Teams/WeChat/custom integrations for B2B support (2028–2029 requirement) |
| Phone channel              | Native or integrated IVR + call routing for B2C                                 |
| Mobile app chat            | B2C channel (2027 wallet launch)                                                |
| Internal ticket submission | Account teams can raise tickets on behalf of customers                          |

**Assessment question**: Which channels are native vs. add-on, and what is the per-channel cost at 500-agent scale? How is email-to-org matching configured — domain rules, manual mapping, or API enrichment?

---

### 2. AI triage and classification

| Requirement                       | Detail                                                                                                                 |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Auto-classification on escalation | Taxonomy tags applied to any ticket escalated from AI, before human assignment                                         |
| AI agent handoff with context     | Conversation transcript and metadata passed to human agent workspace                                                   |
| Pluggable AI layer                | Must allow external AI (Agent Consultant) to operate in the agent workspace without requiring the platform's native AI |

**Assessment question**: Can the platform accept AI classifications from an external system, or does classification require the platform's native AI?

---

### 3. Routing & field logic

| Requirement                             | Detail                                             |
| --------------------------------------- | -------------------------------------------------- |
| Support plan / tier model               | Routing based on customer tier (P0–P3)            |
| Skill-based routing                     | Agent skill tags matched to ticket classification  |
| SLA per tier and taxonomy value         | Different SLA clocks per priority and contact type |
| Customisable ticket and customer fields | Company-level and individual-level custom fields   |
| Flexible tagging/field system           | Taxonomy mapping and analytics use cases           |

Ultimately, we need a flexible routing system where we can use attributes in branches and fallbacks.

**Required routing flow**: Ticket arrives → email enrichment populates org/tier fields → fields determine SLA and routing to correct team via skill matching → priority ranking applied (SLA timer, contact type) → auto-assignment to agent with capacity controls; no cherry-picking.

---

### 4. Agent workspace

| Requirement                        | Detail                                                                                                                             |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Custom app framework               | Platform provides a developer SDK or API for building and deploying custom sidebar apps — not restricted to marketplace apps only |
| App capability scope               | Custom apps can read ticket data, make external API calls, and write back to the ticket — not read-only                           |
| App deployment and versioning      | Custom apps can be deployed and updated without requiring vendor involvement or marketplace approval                               |
| Live customer data panel           | CRM and user data surfaced from our own sources in the agent UI                                                                    |
| Internal escalation to other teams | Jira integration and custom API integrations with read/write access                                                                |
| Agent-triggered workflow execution | Agent approves AI action; platform passes execution signal, or allows external system to do this                                   |
| Internal collaborator access       | Account teams and non-agent staff can view threads and leave internal comments without a full agent seat                           |

**Assessment questions**: What is the custom app development framework (SDK, API, tooling)? Are there restrictions on what custom apps can read/write, or requirements to publish via a vendor marketplace?

---

### 5. Data and permissions

| Requirement               | Detail                                                                                                                                   |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| B2B / B2C data wall       | Two isolated environments — BPO handling B2C must never see B2B data                                                                    |
| Role-based access control | Granular permissions per team and per brand                                                                                              |
| 500-agent scale           | Must support projected 2030 headcount without degraded performance or disproportionate per-seat cost                                     |
| Flexible data model       | Custom objects and fields sufficient to model our org hierarchy and ISV data via our own integrations — no hardcoded schema assumptions |

**Assessment question**: Does the platform support custom object models, or are organisations and users a fixed schema?

---

### 6. Customer-facing experience

| Requirement                    | Detail                                                   |
| ------------------------------ | -------------------------------------------------------- |
| Customer ticket portal         | Merchants can view open tickets and conversation history |
| AI chat history visibility     | Previous AI Agent conversations visible                  |
| Account team thread visibility | AMs can view and reply into ticket threads over email    |

---

### 7. Integrations (must-have)

| System                  | Direction      | Requirement                                                                                                                                         |
| ----------------------- | -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Fin (Intercom)          | Inbound        | Escalation with full conversation context                                                                                                           |
| Jira                    | Bi-directional | Create/update Jira issues from tickets; sync status back                                                                                            |
| Salesforce              | Read           | Sync case numbers and customer data                                                                                                                 |
| Knowledge sources       | Inbound        | Sync knowledge content from an external source (website URL or GitHub repo) for use by the AI agent layer — no manual article duplication required |
| Custom APIs             | Read           | Pull data from internal systems (e.g. BigQuery)                                                                                                     |

**Assessment question**: What knowledge sync mechanisms are supported (URL crawl, GitHub, API push)? Is sync automated on change, or manual?

---

### 8. Analytics and data extract

| Requirement               | Detail                                                                                                       |
| ------------------------- | ------------------------------------------------------------------------------------------------------------ |
| API access to ticket data | Full export of ticket data fields for Analytics pipeline                                                     |
| Taxonomy-level reporting  | Filter and group by custom taxonomy tags                                                                     |
| SLA breach alerting       | Automated in-platform alerts before and on SLA breach, configurable per tier — for agent and supervisor use |
| AHT / agent task time     | Native measurement of handle time per ticket and per agent; required for cost-per-contact modelling         |


---

### 9. Environment and configuration deployment

| Requirement                  | Detail                                                                                                                                        |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Sandbox / test environment   | A test environment that mirrors production configuration — routing rules, SLAs, integrations — so changes can be validated before promotion |
| Configuration promotion path | A defined mechanism to promote configuration from test to production — not manual recreation                                                 |

**Assessment question**: Is there a supported configuration promotion workflow between sandbox and production?

---

### 10. Vendor reliability and operational trust

| Requirement                | Detail                                                                                              |
| -------------------------- | --------------------------------------------------------------------------------------------------- |
| Uptime SLA                 | Contractual uptime commitment for core ticketing; messaging components (if used) covered separately |
| Enterprise support SLA     | Guaranteed human response time for P1/P2 platform issues — not bot-first deflection                |
| Named account team         | Dedicated enterprise contact with defined escalation chain contractually named                      |
| Billing dispute resolution | Documented process for disputing AR charges with a defined resolution timeline                      |
| Auto-renewal protection    | Minimum 60-day written notice required before automatic contract renewal                            |
| Vendor continuity risk     | Evidence of operation in substantially the same form through 2030                                                                                                                                                                       |

**Assessment questions**: What contractual commitments exist for vendor support response times and escalation? Is the vendor profitable or funded beyond 2028? Financial services domain customers and experience?

---

### 11. Pricing scorecard

| Requirement                | Detail                                                                             |
| -------------------------- | ---------------------------------------------------------------------------------- |
| All-in cost at 500 agents  | Total monthly cost modelled: seats + required add-ons                              |
| Cost predictability        | 12-month cost can be modelled with reasonable confidence                           |
| Add-on gating transparency | Required features (QA, WFM, Advanced AI) documented as included or separately billed |
| Volume discount terms      | Enterprise pricing at projected 2027–2030 contact volumes available on request    |

---

**Last Updated**: 2026-04-15
**Owner**: Charlie Wildish
**Status**: Draft — work begins Q3 2026
