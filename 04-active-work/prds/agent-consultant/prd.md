# PRD: AI Agent Consultant

**Author:** Charlie Wildish

**Date:** 2026-04-09

**Approvers:** VP of Product · Director of Operations · Director of Operations Excellence

**Stage:** Solution Design

**Status:** Draft

**Last Updated:** 2026-04-09

**Stakeholders:** Engineering Manager · Knowledge Manager · Process Architect · Content Strategist

| Field | Value |
|-------|--------|
| **2026 deliverable** | AI Agent 'Consultant' · MCD-564 · Q1–Q4 2026 |
| **Strategic goal** | Reduce cost of support |
| **Flywheel domain** | 4. Agent Experience |
| **Strategic lever** | Agent efficiency |
| **How it fits** | 92.5% of contacts reach a human agent. Agent Consultant reduces cost per contact for those tickets by surfacing data, knowledge, and structured workflows in the Zendesk sidebar — cutting the mechanical effort on every human-handled ticket rather than diverting it. |

---

## Executive Summary

92.5% of contacts reach a human agent, and for the highest-volume types — Refunds (4,038 human-handled per 6m), Payouts (2,315), Login & Access (1,947) — Fin's resolution rate is below 5%, meaning handle time is the only remaining cost lever. Agent Consultant embeds an AI assistant in the Zendesk sidebar that surfaces SOP guidance, live payment data, and step-by-step Runbooks at the moment the agent needs them, removing the manual multi-system work that inflates handle time on every complex ticket. This PRD covers Q2–Q4 2026 (Q1 foundations already shipped), supporting the **AI Agent Consultant** deliverable (MCD-564) under the **Reduce cost of support** goal via the **agent efficiency** lever.

---

## Problem Space

**Problem statement:** Agents handling complex contacts — refunds, payout investigations, account access — spend significant time on mechanical work: navigating to external systems, re-reading SOPs, manually drafting responses they have written dozens of times. This friction inflates handle time without adding customer value.

**Who is affected:** All Care agents handling human-resolved tickets. The highest-impact contact types are those with both high volume and low Fin resolution rates — where AI deflection has already reached its ceiling and handle time is the primary cost driver.

**Evidence:**

Contact volumes (last 6 months, `support_contacts_flat_table_2025_last_6m.csv`):

| Issue Type | 6m Contacts | Fin Resolution Rate | Human-Handled |
|---|---|---|---|
| Refunds | 4,114 | 1.8% | 4,038 |
| Transaction Status | 3,679 | 5.8% | 3,465 |
| Login & Access | 2,228 | 12.6% | 1,947 |
| Card Payouts | 1,707 | 0.9% | 1,691 |
| Bank Payouts | 638 | 2.2% | 624 |
| **Q2 focus total** | **12,366** | — | **~11,765** |

Annualised, the Q2 focus contact types represent ~23,500 human-handled contacts. At ~$40 per contact, these five issue types represent approximately $940K of annual agent handling cost — before any efficiency gain. Even a 10% reduction in handle time across this volume is material.

The low Fin resolution rates on Refunds (1.8%) and Payouts (<3%) confirm these are structurally agent-resolved contacts: the task requires data access, policy confirmation, and action execution that Fin cannot perform. Agent Consultant is the correct lever — not more Fin content investment.

**Competitive context:**

- **Plain** (used as a reference model): surfaces codebase knowledge inside a support workspace via a Cursor-style AI assistant. The interaction pattern — contextual data retrieval into the sidebar based on ticket content — is the direct inspiration for the Consultant's contextual tool model.
- **Intercom Copilot (Auto Assist)**: already live for Checkout.com agents. Handles knowledge retrieval and SOP suggestions. Agent Consultant builds on this foundation; it does not replace it. The distinction: Copilot surfaces knowledge from the knowledge base; Consultant adds live data retrieval from payment systems, structured Runbook execution, and action capability.
- **Zendesk AI**: Checkout.com does not use Zendesk's native AI agents. Zendesk Copilot (Auto Assist) is connected via Intercom — this is the same Copilot layer already in use.

**Why now:**

Q1 foundations are shipped (Payins data surfacing, next-best-action prompts). Q2 builds on a working integration rather than starting from scratch. The automation backlog has been defined and prioritised. Refunds and TPA payouts are the two highest-volume, lowest-Fin-resolution contact types — the efficiency case is strongest here. Shipping Q2 before H2 lets the team measure AHT impact and use that data to prioritise the H2 automation backlog.

---

## Goals and Success Metrics

**Business goals:**

- Reduce cost per contact for human-handled tickets by cutting agent handle time on mechanical tasks.
- Improve handling consistency across agents — Runbooks execute identically regardless of agent tenure.
- Generate ticket content summaries that feed Reflex with signal from agent-resolved contacts (structural dependency).

**Agent goals:**

- Resolve complex tickets without context-switching to external systems.
- Follow a clear, step-by-step path for high-risk actions (reversals, account unlocks) without relying on memory of the SOP.
- Access merchant payment data and account context the moment a ticket opens, not after manual retrieval.

**Non-goals:**

- Replacing Fin for deflectable contacts — this product operates on tickets that have already reached a human.
- Replacing Intercom Copilot's knowledge retrieval layer — Consultant augments, not duplicates.
- Full autonomous action without human approval — all action-based capabilities are human-in-the-loop in 2026.
- Consumer (B2C) contact handling — no consumer contacts in 2026 scope.

**Success metrics:**

> **Rule:** Every Baseline cell must contain a value or "TBC — establish by [date]". A bare TBC is not acceptable.

| Metric | Why it matters | Baseline | Target | Source |
|---|---|---|---|---|
| Cost per human-handled contact | North star for this lever | TBC — establish by Q2 2026 end using agent cost model Charlie will provide | 10% reduction on Q2 focus contact types by Q4 2026 | Agent cost model + Zendesk ticket data |
| Runbook adoption rate (eligible tickets) | Measures whether agents are using the tool; proxy for handle time impact | 0% (not yet launched) | 60% of eligible tickets use a Runbook by Q4 2026 | Consultant instrumentation |
| Contextual tool invocations per handled ticket | Measures active AI assistance beyond Runbooks | TBC — establish at Q2 launch | Upward trend quarter-on-quarter | Consultant instrumentation |
| Ticket content summary coverage | Structural dependency for Reflex; measures Consultant feeding the insight engine | TBC — establish at Q2 launch | 80% of agent-resolved tickets have a summary by Q4 2026 | Reflex pipeline |
| Merchant CSAT (guardrail) | Must not decline as automation increases | TBC — establish current baseline by Q2 2026 | No decline vs baseline | CSAT survey data (Zendesk) |

---

## Customer Segments and Needs

**Primary user:** Care agents (Zendesk). All agents handling B2B merchant contacts are in scope — Standard, Enterprise, and Premium segments.

**Secondary beneficiary:** Team Leaders and QA leads (via QA capability in H2 2026 and beyond).

**User stories:**

- As a Care agent handling a refund request, I want the Consultant to confirm payment eligibility and prepare the reversal action for my approval, so I can process the refund correctly without navigating three separate systems.
- As a Care agent investigating a payout failure, I want the Consultant to query the TPA system and surface the result in the sidebar, so I can respond to the merchant without leaving the ticket.
- As a Care agent resolving an account access issue, I want a step-by-step Runbook to guide me through identity verification and account unlock, so I follow the correct procedure every time regardless of how often I handle this ticket type.
- As a Care agent facing an unfamiliar error code, I want to ask the Consultant a question and receive a synthesised answer drawing on payment data, knowledge base articles, and prior ticket history, so I can diagnose the issue without manual multi-system searches.

---

## Proposed Solution and Scope

**Solution overview:**

Agent Consultant is an AI assistant embedded in the Zendesk sidebar. It operates in two complementary modes: Runbooks (step-by-step guided workflows for defined, repeatable tasks) and contextual AI tools (on-demand data and knowledge retrieval for open-ended investigations). Both modes surface in the same sidebar workspace; agents do not context-switch. All actions require agent approval before execution.

The content layer is distinct from Fin's. Fin uses public documentation only. Agent Consultant also uses internal agent SOPs and operational documentation — held in the git repository — giving agents access to guidance that Fin cannot surface.

> Alternatives evaluated: see Appendix.

**In scope — Q2 2026** (per MCD-564 Q2 deliverables):

- **Central content source**: index public documentation and internal agent SOPs (from git repo) into a single retrieval layer — giving Consultant access to internal guidance that Fin cannot surface
- **Explain Payins using Agent SOPs**: when a ticket matches a Transaction Status or Refund issue type, surface the relevant agent SOP in the sidebar proactively
- **Explain Payouts using Agent SOPs**: when a ticket matches a Bank Payout or Card Payout issue type, surface the relevant agent SOP in the sidebar proactively
- **Automate TPA payment status lookups**: Runbook that retrieves the TPA reference from the ticket, queries the TPA API, surfaces the result, and drafts an agent response for approval
- **Automate Refund reversals**: Runbook that checks payment eligibility, confirms merchant intent, triggers the reversal via API (agent approval required), posts an internal note, and drafts the merchant response

**In scope — H2 2026** (per MCD-564 H2 deliverables):

- **Pick from the Agent automation backlog priorities**: following Q2 impact review, select and build the next highest-priority Runbooks from the automation backlog (Confluence page 7847149938) — exact items to be confirmed post-Q2
- **Analyse and flag potential content gaps**: Consultant analyses tickets solved by agents where it could not provide a useful answer and flags these to the Knowledge Manager as gaps in public or internal content

**In scope — H2 2026 (TBC, pending scoping and prioritisation):**

- **Context retrieval**: merchant data (entity structure, processing profile, account status), payment history, and prior ticket/contact history surfaced automatically on ticket open — requires a data layer not yet available; scoping needed before this can be scheduled
- **Response drafting**: Consultant drafts a reply to the merchant based on ticket context, knowledge retrieval results, or as the final step of a Runbook; agent reviews and sends
- **Conversation summary**: collapses the ticket thread into a summary on demand, for agents picking up a ticket mid-flight or reviewing a long exchange
- **Escalation summary**: generated at the point of escalation — states why the ticket is being escalated and the assessed complexity level, so the receiving agent has immediate context
- **Audit log**: records all Consultant actions (AI-generated and agent-approved) per ticket; accessible to Ops managers and the Product team only; prerequisite for any write-action capability

**In scope — 2027 horizon (not in this PRD, flagged for planning):**

- Autonomous task execution for approved action types (no human approval required for defined low-risk actions)
- QA on closed tickets — automated quality scoring against golden dataset
- Fin Procedures alignment: Consultant's data integrations and Fin's Procedures should share a common API access layer to avoid duplication

**Out of scope (2026):**

- Consumer (B2C) contact handling
- Replacing Intercom Copilot's knowledge retrieval layer
- Fully autonomous actions without human-in-the-loop approval
- External merchant-facing surface (Consultant is agent-only)

---

## Requirements

**Requirements by audience / domain**

| Domain | Requirement IDs | Purpose |
|---|---|---|
| **Care Ops / CX** | FR-0, FR-1, FR-2, FR-3, FR-4, FR-5, FR-6, FR-7, FR-8, FR-9, FR-10, FR-11 | Agent-facing Runbook and contextual tool capabilities; SOP content surfacing; summaries; response drafting; content gap flagging |
| **Analytics & Reporting** | FR-0, FR-7 | Runbook adoption, invocation rate, cost per contact tracking |
| **Security & Compliance** | NFR-1, NFR-2, FR-12 | Data access controls; human-in-the-loop enforcement; audit log for write actions |
| **Product / Platform** | FR-0, NFR-3, NFR-4 | Content source integration; API connections; performance |

### Functional requirements

Requirement IDs map to the MCD-564 deliverable line items.

| ID | Priority | Deliverable | Requirement | Acceptance Criteria | Domain/s |
|---|---|---|---|---|---|
| **FR-0** | **P0** | All phases | **Instrumentation: key events defined in the Instrumentation section must be implemented, validated in staging, and confirmed firing before Q2 go-live.** | All listed events fire correctly in staging; validated by Data Scientist and Engineering before Q2 Phase 1 entry. | Product / Platform |
| FR-1 | P0 | Q2: Central content source | Public documentation and internal agent SOPs (from git repo) indexed into a single retrieval layer, accessible from the Consultant sidebar. | Given a query matching a public doc, the Consultant returns a relevant result with source. Given a query matching an internal SOP, the Consultant returns the SOP content. Both paths return results from the same interface. | Care Ops / CX · Product / Platform |
| FR-2 | P0 | Q2: Explain Payins using Agent SOPs | When a ticket is classified as Transaction Status or Refunds, the Consultant proactively surfaces the relevant agent SOP in the sidebar without agent prompting. | Given a ticket with issue_type = Transaction Status or Refunds, the Consultant surfaces the correct SOP within 5s of ticket open; tested against 5 representative ticket types. | Care Ops / CX |
| FR-3 | P0 | Q2: Explain Payouts using Agent SOPs | When a ticket is classified as Bank Payouts or Card Payouts, the Consultant proactively surfaces the relevant agent SOP in the sidebar. | Given a ticket with issue_type = Bank Payouts or Card Payouts, the Consultant surfaces the correct SOP within 5s of ticket open; tested against 5 representative ticket types. | Care Ops / CX |
| FR-4 | P0 | Q2: Automate TPA payment status lookups | TPA lookup Runbook: retrieves TPA reference from ticket, queries TPA API, surfaces result in sidebar, drafts agent response for approval. | Given a ticket containing a TPA reference, the Runbook completes all steps; agent approves the drafted response before it sends; result posted as internal note on approval; tested in staging against TPA sandbox. | Care Ops / CX · Security & Compliance |
| FR-5 | P0 | Q2: Automate Refund reversals | Refund reversal Runbook: payment eligibility check, merchant intent confirmation, API reversal trigger (agent approval required at this step), internal note, merchant response draft. | Given a refund request ticket, the Runbook completes all five steps in sequence; reversal API call does not execute without explicit agent approval at step 3; all reversal actions logged with agent ID and timestamp. | Care Ops / CX · Security & Compliance |
| FR-6 | P1 | H2: Agent automation backlog items | Following Q2 impact review, additional Runbooks built from the Agent automation backlog (Confluence 7847149938), prioritised by human-handled volume and estimated handle time saving. Exact items confirmed post-Q2. | Each selected Runbook follows the same approval-step model as FR-4 and FR-5; adoption instrumented from day 1. | Care Ops / CX |
| FR-7 | P1 | H2: Content gap flagging | When the Consultant cannot provide a useful answer on an agent-resolved ticket, the gap is flagged to the Knowledge Manager with the ticket reference, query text, and contact type. | Given a ticket where the Consultant returns no result or a low-confidence result, a gap event is logged and surfaced in the Knowledge Manager's gap report within 24h of ticket close. | Care Ops / CX · Analytics & Reporting |
| FR-8 | P1 | H2 TBC: Context retrieval | On ticket open, the Consultant automatically surfaces merchant context: entity structure, processing profile, account status, payment history, and prior tickets. Requires merchant data layer — scoping needed before scheduling. | Given a ticket open event, merchant context loads in the sidebar within 5s; data sourced from entity/merchant data layer (source TBC). Scope and timeline subject to data layer availability. | Care Ops / CX · Product / Platform |
| FR-9 | P1 | H2 TBC: Response drafting | Consultant drafts a reply to the merchant based on ticket context and knowledge retrieval results, or as the final step of a Runbook. Agent reviews, edits if needed, and sends. Consultant never sends without agent action. | Given a completed knowledge retrieval or Runbook, the Consultant presents a draft response in the sidebar; no send action is possible without agent confirmation; tested on 3 representative contact types. | Care Ops / CX |
| FR-10 | P1 | H2 TBC: Conversation summary | On demand, the Consultant summarises the ticket thread — collapsing context for agents picking up a ticket mid-flight or reviewing a long exchange. | Given a ticket with >5 messages, the agent can trigger a conversation summary; summary is generated within 10s and covers key exchanges and any resolution steps taken. | Care Ops / CX |
| FR-11 | P1 | H2 TBC: Escalation summary | At the point of escalation, the Consultant generates a summary stating why the ticket is being escalated and the assessed complexity level. | Given a ticket escalation event, an escalation summary is automatically generated and attached to the ticket before handoff; includes escalation reason and complexity rating; tested against 3 escalation scenarios. | Care Ops / CX |
| FR-12 | P1 | H2 TBC: Audit log | All Consultant actions per ticket — data retrievals, API calls, drafts generated, Runbook steps executed — are logged with timestamp and approving agent ID. Log is accessible to Ops managers and the Product team only; not visible to agents. | Given any Consultant action, a log entry is created within 1s; log queryable by ticket ID, agent ID, and action type; confirmed not surfaced in the agent-facing sidebar. | Security & Compliance · Analytics & Reporting |

### Non-functional requirements

| ID | Priority | Requirement | Acceptance Criteria | Domain/s |
|---|---|---|---|---|
| NFR-1 | P0 | All agent actions requiring API calls (reversals, account unlocks) require explicit agent approval before execution. No autonomous action on sensitive endpoints. | Given any Runbook step that triggers an API call, the step does not execute until the agent confirms; confirmed in staging test of each Runbook. | Security & Compliance |
| NFR-2 | P0 | Internal SOP documents are accessible to agents only — not surfaced to merchants via Fin or any external channel. | Content source separation validated in staging: internal SOP queries return no results when tested via the Fin (public-only) content path. | Security & Compliance |
| NFR-3 | P1 | Consultant sidebar loads and returns first result within 5 seconds of ticket open on supported ticket types. | P95 load time ≤ 5s measured over 7-day window post-launch; monitored via Consultant instrumentation. | Product / Platform |
| NFR-4 | P1 | Runbook step failure (API timeout or error) surfaces a clear error state to the agent with a manual fallback path. | Given a TPA or reversal API error, the Runbook displays an error message and offers the agent the manual SOP link; tested for each API integration. | Product / Platform |

---

## Design and User Experience

**Design & UX:** TBC — [Link to Figma to be added]

Key interaction principles:
- **Surfaced without asking.** Payment data, SOP suggestions, and Runbook prompts appear automatically when ticket content matches — agents do not need to know which tools exist.
- **Approve, don't configure.** Agents interact with outputs. Consultant proposes; agent approves or rejects. Effort is AI; decision is human.
- **No context switching.** Everything surfaces in the Zendesk sidebar. Agents do not leave the ticket.
- **Consistency by design.** Runbooks execute identically for all agents — correct execution from day one, not after months of experience.

---

## Instrumentation and Monitoring

**Key events to instrument:**

- `consultant_runbook_launched`: runbook_name, ticket_id, issue_type, agent_id
- `consultant_runbook_step_completed`: runbook_name, step_number, ticket_id, agent_id
- `consultant_runbook_step_rejected`: runbook_name, step_number, ticket_id, agent_id — captures where agents abandon or override
- `consultant_tool_invoked`: tool_name, ticket_id, issue_type, agent_id, query_type (proactive / agent-initiated)
- `consultant_tool_response_time_ms`: p50/p95 response time per tool
- `consultant_ticket_summary_generated`: ticket_id, case_type, issue_type — feeds Reflex pipeline
- `contact_resolved`: resolved_by (agent), handle_time_seconds, consultant_assisted (boolean), runbook_used (boolean), issue_type, merchant_segment

**Internal dashboards and monitoring:**

- Runbook adoption dashboard: adoption rate by issue type and Runbook, step rejection rate (where agents override), weekly trend. Owner: Charlie / Data Scientist.
- Consultant performance dashboard: tool invocations per handled ticket, response time p95, error rate per API integration. Owner: Engineering.
- Reflex summary coverage: % of agent-resolved tickets with a generated summary, daily. Owner: Charlie / Data Engineer.

**Validation approach:**

- Staging validation: all events fire on test tickets before Q2 launch; Data Scientist signs off.
- Silent failure detection: daily row count alert on `consultant_runbook_launched` and `consultant_ticket_summary_generated` — if count drops >50% vs prior 7-day average, alert to Engineering and Charlie. Owner: Data Engineer. Cadence: daily.

---

## Risks, Assumptions, and Dependencies

| Type | Description | Likelihood | Impact | Mitigation / Validation | Owner |
|---|---|---|---|---|---|
| Risk | TPA API availability or schema changes break the TPA lookup Runbook | Medium | High | API contract agreed with TPA team before Q2 build; versioned API calls; fallback to manual SOP link on error | Engineering Manager |
| Risk | Agent adoption is low — agents continue manual workflows out of habit | Medium | High | Runbooks are proactively suggested (not buried in a menu); measure adoption rate from day 1; review with Operations if <30% adoption at 4 weeks | Charlie / Director of Operations |
| Risk | Internal SOP content is out of date or inconsistently structured, reducing Consultant retrieval quality | Medium | Medium | Knowledge Manager audits internal SOPs before Q2 content indexing; flag gaps before launch | Knowledge Manager |
| Risk | Refund reversal Runbook triggers incorrect reversals due to eligibility logic errors | Low | High | Staged rollout — pilot with a small agent cohort before full rollout; manual override required at approval step; all reversals logged | Engineering Manager · Charlie |
| Assumption | AHT and cost per contact baseline will be established by end of Q2 2026 | — | High | Charlie to provide cost model data; baseline locked before Q3 metric review | Charlie |
| Assumption | Internal SOPs are maintained in a git repo accessible to the Consultant content pipeline | — | Medium | Validate repo access and format with Engineering Manager before Q2 build starts | Engineering Manager |
| Dependency | Refund reversal API access — requires approved API scope for reversal endpoint | High | High | Confirm API permissions with Engineering and Security before Q2 build; if not approved, Runbook ships as read-only (eligibility check + draft only, no execution) | Engineering Manager |
| Dependency | Ticket content summary pipeline for Reflex — Consultant must generate summaries in a format Reflex can consume | Medium | Medium | Format agreed with Reflex engineering workstream before Q3 build | Engineering Manager |

---

## Rollout Plan

Phased by capability risk: read-only first, write actions on a pilot cohort second, full rollout third. Rollback trigger: >3 incorrect reversals or >2 P0 incidents in any phase.

| | Phase 1 | Phase 2 | Phase 3 |
|---|---|---|---|
| **Name** | Content and read-only | Action Runbooks (pilot) | Full rollout + H2 backlog |
| **Timeline** | Q2 2026 | Q3 2026 | Q4 2026 |
| **In scope** | FR-1 (content source), FR-2/FR-3 (SOP explanations), FR-4 (TPA lookup — read only) | FR-5 (refund reversal Runbook, pilot cohort of 3–5 agents), account unlock Runbook (pilot), ticket content summaries | Full rollout of Phase 2 Runbooks, FR-6 (backlog Runbooks), FR-7 (content gap flagging) |
| **Entry criteria** | FR-0 instrumentation live in staging; public + SOP content indexed; agents briefed; cost per contact baseline methodology agreed | Reversal API permissions confirmed; approval flow tested in staging; Phase 1 TPA adoption >40%; no open P0s | Phase 2 pilot complete; zero incorrect reversals; all agents trained; monitoring configured |
| **Success criteria** | >80% agent "helpful" rating on SOP suggestions; TPA Runbook used on >40% eligible tickets; zero P0s | Zero incorrect reversals over 4-week pilot window; >70% ticket summary coverage on pilot cohort | >60% Runbook adoption on eligible tickets; >80% ticket summary coverage; CSAT no worse than baseline |

**Definition of Done:**
- Technical: all P0 FRs and NFRs delivered and tested; instrumentation validated; API integrations stable
- Operational: all agents trained; Runbook documentation published; content gap alert workflow live
- Data: cost per contact delta measurable; Reflex receiving ticket summaries from Consultant
- Business: Q4 adoption and cost metrics reviewed with Director of Operations and VP of Product

**Product dependencies:**

| Dependency | Owner | Required by |
|---|---|---|
| TPA API access (read) | Engineering Manager | Phase 1 |
| Internal SOP git repo access | Engineering Manager | Phase 1 |
| Refund reversal API permissions (write) | Engineering Manager + Security | Phase 2 |
| User Management API access (account unlock) | Engineering Manager | Phase 2 |
| Reflex summary ingestion format agreed | Reflex / Engineering Manager | Phase 2 |

**Go-to-market:**
- Agent briefing and training before each phase — Director of Operations Excellence
- Runbook documentation in knowledge base before each Runbook goes live — Knowledge Manager
- No external merchant communication required (agent-internal tool)
- Quarterly adoption and cost impact review with VP of Product and Director of Operations — Charlie

---

## Appendix

**Strategy and research:**

- Agent Consultant vision and interaction model: `./vision.md`
- Agent Consultant product reference: `01-knowledge-base/products/agent-consultant.md`
- Agent automation backlog: Confluence page 7847149938
- Contact volume actuals: `01-knowledge-base/metrics/support_contacts_flat_table_2025_last_6m.csv`
- Support taxonomy: `01-knowledge-base/processes/support-taxonomy.md`
- Care product flywheel model: `01-knowledge-base/strategy/care-product-model.md`

**Alternatives considered:**

- **Extend Fin to cover refund reversals and TPA lookups**: Fin's strength is deflecting contacts before they reach agents. Refund reversals and complex payout investigations require multi-step approval, human judgement, and write-API access — not a natural fit for an AI deflection layer. Extending Fin here would conflate two distinct products with different risk profiles. Rejected.
- **Build standalone tooling outside Zendesk**: Requires agents to context-switch. The core value proposition of Consultant is zero context-switching. Rejected.
- **Generic AI assistant (e.g. ChatGPT-style interface)**: No proactive surfacing, no Zendesk integration, no structured Runbook model. Does not meet the "surfaced without asking" principle. Rejected.
