# Braavos Consumer Care — Fin Configuration Plan
**Owner:** Charlie Wildish
**Date:** June 2026
**Status:** Draft — planning use only
**Scope:** External Launch only (Dec 2026–Jan 2027). Fin is not deployed in Phase 2.

This document lists every configuration item required to launch Fin for Braavos consumer care. It is structured by Fin's configuration layers (Personality → Content → Guidance → Attributes → Escalation → Procedures) followed by Analytics. Each item states what needs to be configured, who owns it, any prerequisites, and whether it is blocked.

**Owner labels:**
- **[FIN-ADMIN]** — Fin admin configuration (Care product / content team)
- **[ENG]** — Engineering build required (Data Connector, API integration)
- **[CONTENT]** — Content work required (KB articles, Guidance writing)
- **[LEGAL]** — Legal sign-off required before configuring (Nick Grafton-Green)
- **[OPS-EX]** — Operational Excellence input required before configuring

---

## 1. Personality and identity

| Item | What to configure | Owner | Blocker |
|---|---|---|---|
| Fin identity / name | Fin's display name in the Braavos app messenger. Options: "Braavos Support", "Braavos Assistant", or unnamed. Decision needed before install. | [FIN-ADMIN] | Decision required from Braavos product team |
| Tone of voice | Personality instructions in Fin's Guidance: register (formal / friendly / warm), response length preference, how to address the consumer ("you" / first name). Consumer product — warmer and shorter than merchant Fin. | [FIN-ADMIN] + [CONTENT] | None — draft and test pre-launch |
| Response length | Configure Fin for concise responses by default. Consumer queries are typically simpler than merchant queries; long answers increase abandonment. | [FIN-ADMIN] | None |
| Language | English at launch. Confirm whether multilingual support is required for Phase 2 or External Launch. If required, Intercom multilingual config + translated KB articles needed. | [FIN-ADMIN] | Decision required |
| Messenger appearance | Launcher logo, AI Agent logo, colour scheme — must match Braavos brand. Confirm design assets with Braavos product team. | [FIN-ADMIN] | Design assets from Braavos team |
| User identity / JWT verification | Consumers must be authenticated before Fin can surface account data. JWT-based user verification must be configured in Fin Messenger, passing user ID from the Braavos app session. Required for all data-connected Procedures. | [ENG] + [FIN-ADMIN] | Braavos app team to implement JWT token passing |

---

## 2. Content (Knowledge Base)

All KB articles must be tagged with `consumer_case_type` and `consumer_issue_type` before loading, so that BigQuery events carry full taxonomy metadata and retrieval accuracy can be measured at taxonomy level.

### 2.1 KB article set required at launch

| Topic area | Source | Status |
|---|---|---|
| Account access and recovery | To be written | Not started |
| Card management (block, unblock, replace, lost/stolen) | To be written | Not started |
| Payments — failure reasons, statuses, timelines | To be written | Not started |
| Fraud and security reporting (how to report, what happens next) | To be written | Not started |
| Technical issues and known fix library | To be written | Not started |
| Transaction recovery (CPR, ATM non-dispense, DD Guarantee) | To be written | Not started |
| Product and feature KB (FSCS, fees, cashback/rewards) | To be written | Not started |
| AML account restriction messaging | [LEGAL] sign-off required — POCA s.333A. Cannot load until approved. | Blocked |
| Dispute communications | To be written | Not started |
| Supporting content for each Procedure (see section 5) | Depends on Procedure specs being finalised | Blocked until Procedures defined |

### 2.2 KB tagging requirement

Every article must carry:
- `consumer_case_type` — top-level taxonomy category (8 values)
- `consumer_issue_type` — sub-issue level (conditional on case type; values from `consumer-app-care-taxonomy.md`)

Articles covering multiple issue types must be tagged to each applicable type. **No article may be loaded without both tags set.** Gate: FIN-ADMIN to verify all articles tagged before any KB load to production.

### 2.3 KB not to load

- Any content describing internal systems, agent-only processes, or internal complaint handling steps — these must not be surfaced to consumers
- AML restriction messaging: load only after Legal sign-off

---

## 3. Guidance

Guidance is natural language standing instructions that shape how Fin responds, overriding defaults. Each item below is a discrete Guidance block.

| Guidance item | Instruction to write | Owner | Blocker |
|---|---|---|---|
| Scope definition | Define what Fin should and should not help with. Fin should not attempt to resolve complaints — escalate immediately. Fin should not provide legal advice, investment advice, or advice on AML investigations. | [CONTENT] + [FIN-ADMIN] | None |
| Wellbeing / vulnerable consumer escalation | If the consumer discloses distress, financial difficulty, mental health concerns, or uses language indicating vulnerability, escalate immediately to the wellbeing queue. Fin must not attempt to resolve or respond substantively. Fin must not draft a wellbeing response — the human agent owns this. | [CONTENT] + [FIN-ADMIN] | Signal list needs defining (see open question below) |
| Complaint identification | If the consumer expresses dissatisfaction with a product, service, or outcome — set `complaint_flag = true` and escalate to the complaints queue. Do not attempt to resolve a complaint as a standard query. | [CONTENT] + [LEGAL] | Legal must sign off on the definition of "expression of dissatisfaction" before this Guidance can be finalised |
| AML restriction | If the consumer asks why their account is restricted, apply the AML holding message only. Do not disclose whether an investigation is underway or any details of the restriction reason. | [CONTENT] + [LEGAL] | Legal sign-off required (POCA s.333A) |
| APP fraud / scam contacts | If the consumer reports sending money to a scammer or being deceived into a payment, do not advise them on likelihood of recovery or reimbursement. Capture the details and escalate to the fraud queue immediately. | [CONTENT] + [LEGAL] | Legal review recommended |
| Escalation default | If Fin cannot resolve a query with high confidence, escalate rather than speculate. Do not provide uncertain or hedged answers on financial matters. | [CONTENT] + [FIN-ADMIN] | None |
| Response on regulated products (BNPL, credit) | If the consumer's query concerns a credit product, note that Fin cannot provide advice on credit decisions and escalate to a specialist agent. | [CONTENT] + [LEGAL] | Confirm scope of regulated products at launch |

### Open question: wellbeing signal list

The wellbeing triage Procedure requires a defined list of signals that trigger escalation. This needs to be agreed before Guidance and the Procedure can be finalised:
- Explicit disclosures (e.g. "I'm struggling financially", "I'm having a hard time")
- Implicit signals (e.g. repeated failed transactions, pattern of contact type)
- Keywords / phrases that trigger immediate escalation (e.g. self-harm references, crisis language)

**Owner to define: [OPS-EX] + Legal. Blocking Guidance item 2 and Wellbeing Procedure.**

---

## 4. Attributes

Fin automatically assigns these to every conversation. Values must match Zendesk ticket field options exactly so the handoff carries consistent taxonomy metadata.

| Attribute | Type | Values | Owner | Notes |
|---|---|---|---|---|
| `consumer_case_type` | Dropdown | 8 values from consumer care taxonomy | [FIN-ADMIN] | Must match Zendesk `consumer_case_type` field values exactly |
| `consumer_issue_type` | Dropdown (conditional on case type) | Per-category sub-issues from consumer care taxonomy | [FIN-ADMIN] | Must match Zendesk `consumer_issue_type` values exactly; configure as conditional attribute |
| `complaint_flag` | Boolean | true / false | [FIN-ADMIN] | Drives complaint queue routing and SLA clock start |
| `resolution_status` | Dropdown | Resolved / Escalated / Abandoned | [FIN-ADMIN] | Standard Fin attribute |
| `csat` | CSAT | 1–5 star or emoji scale | [FIN-ADMIN] | Collected post-resolution only (not post-escalation); confirm scale with Braavos team |
| `escalation_reason` | Dropdown | Unresolved / Complaint / Wellbeing / Fraud / AML / Consumer request | [FIN-ADMIN] | Used in BigQuery for escalation driver analysis |

---

## 5. Escalation rules

Escalation rules define when Fin hands off to a human agent and which Zendesk queue the ticket lands in. Rules fire before the conversation ends — they can be triggered by Attribute value, conversation content, or explicit consumer request.

| Rule | Trigger | Destination queue | Owner |
|---|---|---|---|
| Complaint escalation | `complaint_flag = true` | Complaints queue | [FIN-ADMIN] |
| Wellbeing escalation | Wellbeing signal detected (via Guidance) | Wellbeing specialist queue | [FIN-ADMIN] |
| Fraud / ATO escalation | Procedure outputs fraud classification, OR consumer reports scam/ATO | Fraud specialist queue | [FIN-ADMIN] |
| AML escalation | AML restriction flag detected on account | AML specialist queue | [FIN-ADMIN] |
| Unresolved — standard | Fin cannot resolve after attempt | General Braavos queue | [FIN-ADMIN] |
| Consumer requests human | Consumer explicitly asks for a human agent | General Braavos queue | [FIN-ADMIN] |
| API failure fallback | Data Connector call fails (timeout or error) | General Braavos queue | [FIN-ADMIN] + [ENG] | Confirm fallback behaviour with engineering |

**Context handoff on escalation:** On every escalation, Fin must pass to the Zendesk ticket:
- Full conversation transcript
- Resolved Fin Attributes (`consumer_case_type`, `consumer_issue_type`, `complaint_flag`, `escalation_reason`)
- Procedure output summary (if a Procedure ran): signals detected, data retrieved, risk classification
- Consumer identity (user ID from JWT session)

This is configured in the Fin escalation workflow and the Zendesk ticket creation API integration. **[ENG]** to confirm the field mapping from Fin context to Zendesk ticket fields.

---

## 6. Procedures

Five Procedures are required for External Launch. All are blocked until Braavos Engineering confirms API availability (target: Q3 2026).

### Procedure 1 — ATO Triage

**What it does:** Identifies account takeover signals, classifies the contact, and escalates to the fraud queue with structured context. Fin does not freeze the account — that is a human agent action.

| Config item | Detail | Owner | Blocker |
|---|---|---|---|
| Procedure logic | Steps: (1) retrieve account status and recent login events via Data Connector; (2) retrieve device fingerprint data; (3) classify risk level (high / medium / uncertain); (4) generate structured summary for agent; (5) escalate to fraud queue | [FIN-ADMIN] | Braavos API availability |
| Data Connector — account status API | Connect to Braavos account status API; fields: account status, account freeze status, last login timestamp, login location | [ENG] | Braavos Engineering to confirm API spec |
| Data Connector — login events API | Recent login events: device ID, IP, timestamp, success/failure | [ENG] | Braavos Engineering to confirm API spec |
| Data Connector — device fingerprint | Device fingerprint data for mismatch detection | [ENG] | Braavos Engineering to confirm API spec |
| API failure fallback | If any Data Connector call fails: escalate to fraud queue immediately with partial context and flag `api_failure = true` on ticket | [FIN-ADMIN] + [ENG] | |
| Simulation | Run simulation suite before go-live: known ATO pattern, legitimate login, ambiguous case | [FIN-ADMIN] | Procedure must be built first |

### Procedure 2 — Transaction Lookup

**What it does:** Retrieves transaction status, failure reason, and resolution timeline for a specific transaction the consumer is querying.

| Config item | Detail | Owner | Blocker |
|---|---|---|---|
| Procedure logic | Steps: (1) consumer provides transaction reference or selects from recent transactions; (2) retrieve transaction detail via Data Connector; (3) return status, failure reason, and expected resolution timeline; (4) if unresolved failure: offer escalation | [FIN-ADMIN] | Braavos API availability |
| Data Connector — transaction API | Fields: transaction ID, amount, currency, merchant, status, failure reason code, failure reason text, resolution timeline | [ENG] | Braavos Engineering to confirm API spec |
| Failure reason mapping | Map API failure codes to consumer-facing explanations (e.g. "insufficient funds" → plain English). Must not expose internal system codes directly. | [CONTENT] + [FIN-ADMIN] | Need failure code list from Braavos Engineering |
| API failure fallback | If Data Connector fails: tell consumer the lookup is unavailable and offer to escalate | [FIN-ADMIN] | |
| Simulation | Test: successful lookup, failed transaction with clear reason, unknown transaction reference | [FIN-ADMIN] | |

### Procedure 3 — Scam Intake

**What it does:** Structured intake for APP fraud and scam reports. Captures transaction references, scam type, and timeline. Routes to fraud queue with structured context. Fin does not advise on reimbursement likelihood.

| Config item | Detail | Owner | Blocker |
|---|---|---|---|
| Procedure logic | Steps: (1) identify scam report signal; (2) collect: transaction reference(s), scam type (authorised push payment / invoice fraud / romance scam / impersonation / other), date, amount, payee details; (3) retrieve transaction data via Data Connector to confirm transaction exists; (4) generate structured intake summary; (5) escalate to fraud queue | [FIN-ADMIN] + [LEGAL] | Braavos API availability; Legal review of intake flow |
| Data Connector — transaction API | Same connector as Procedure 2 | [ENG] | |
| Data Connector — account API | Account status for context on escalation | [ENG] | |
| Guidance override | Fin must not state or imply whether the consumer will be reimbursed under PSR. Legal-reviewed Guidance required. | [LEGAL] | Legal sign-off |
| API failure fallback | If transaction lookup fails: proceed with intake using consumer-provided data; flag `api_failure = true` on ticket | [FIN-ADMIN] | |
| Simulation | Test: APP fraud, invoice fraud, impersonation scam, consumer unsure of scam type | [FIN-ADMIN] | |

### Procedure 4 — Context Handoff

**What it does:** Passes full conversation context, Fin Attributes, and consumer data to the Zendesk ticket on escalation. Used on every escalation regardless of which other Procedure ran (or if none did).

| Config item | Detail | Owner | Blocker |
|---|---|---|---|
| Procedure logic | Steps: (1) compile Fin Attributes (`consumer_case_type`, `consumer_issue_type`, `complaint_flag`, `escalation_reason`); (2) compile Procedure output summary if applicable; (3) compile consumer identity (user ID from JWT); (4) create Zendesk ticket via API with full field set | [FIN-ADMIN] + [ENG] | Zendesk ticket creation API integration |
| Zendesk ticket creation API | Integration to create Braavos queue tickets from Fin with full field mapping. Must pre-populate: `consumer_case_type`, `consumer_issue_type`, `complaint_flag`, conversation transcript, Procedure summary, consumer user ID | [ENG] | Engineering to confirm field mapping |
| Ticket deduplication | If a Zendesk ticket already exists for this consumer (same session), update rather than create a new ticket | [ENG] | Confirm deduplication logic with engineering |
| Simulation | Test: standard escalation, complaint escalation, wellbeing escalation, Procedure-preceded escalation | [FIN-ADMIN] | |

### Procedure 5 — Wellbeing Triage

**What it does:** Identifies wellbeing disclosure signals and escalates immediately to the wellbeing specialist queue. Fin does not respond to the consumer after the signal is detected — all messaging is handled by the human agent.

| Config item | Detail | Owner | Blocker |
|---|---|---|---|
| Procedure logic | Steps: (1) detect wellbeing signal (from agreed signal list — see open question in section 3); (2) immediately route to wellbeing specialist queue; (3) generate agent context note: signal type, exact consumer phrasing that triggered escalation; (4) Fin sends holding message only — no substantive response | [FIN-ADMIN] + [OPS-EX] | Signal list not yet defined — **blocking** |
| Holding message text | Short message Fin sends while handing off: must not attempt to help or diagnose. E.g. "I'm going to connect you with a specialist member of our team right now." Legal/OPS-EX review recommended. | [CONTENT] + [OPS-EX] | |
| No agent draft rule | Fin must not draft a consumer-facing response for this type. Guidance must explicitly block Fin from generating a reply. | [FIN-ADMIN] | |
| Signal list definition | Agreed list of keywords, phrases, and patterns that trigger the Procedure. Input from OPS-EX + Legal. | [OPS-EX] + [LEGAL] | **Not yet defined — critical path** |
| Simulation | Test: explicit financial distress disclosure, crisis language, implicit signal (ambiguous phrasing) | [FIN-ADMIN] | Signal list required first |

---

## 7. Analytics — BigQuery events

All Fin conversation events must emit to BigQuery, not Intercom Analytics. These are the required events for External Launch:

| Event | Payload fields | Owner |
|---|---|---|
| `care.fin.conversation.started` | consumer_user_id, channel, timestamp | [ENG] |
| `care.fin.conversation.resolved` | consumer_user_id, consumer_case_type, consumer_issue_type, resolution_time_seconds, csat | [ENG] |
| `care.fin.escalation.triggered` | consumer_user_id, escalation_reason, consumer_case_type, consumer_issue_type, complaint_flag | [ENG] |
| `care.fin.procedure.started` | procedure_name, consumer_user_id | [ENG] |
| `care.fin.procedure.completed` | procedure_name, consumer_user_id, outcome (resolved / escalated / api_failure) | [ENG] |
| `care.fin.complaint_identified` | consumer_user_id, ticket_id | [ENG] |
| `care.fin.csat.submitted` | consumer_user_id, csat_score, conversation_id | [ENG] |

All events must carry `consumer_case_type` and `consumer_issue_type` where they have been assigned by Fin Attributes. If not yet assigned at event time (e.g. `conversation.started`), fields may be null — but must be populated on all post-classification events.

---

## 8. Pre-launch gates

Before Fin goes live for External Launch, the following gates must be cleared:

| Gate | Owner | Status |
|---|---|---|
| All 5 Procedures simulated and signed off | [FIN-ADMIN] | Blocked — APIs needed |
| Braavos API Data Connectors live and tested in staging | [ENG] | Blocked — Braavos Engineering |
| Full KB loaded and tagged (all articles carry case_type + issue_type) | [FIN-ADMIN] + [CONTENT] | Not started |
| Legal sign-off on: complaint definition, AML messaging, scam intake flow, PSR reimbursement Guidance | [LEGAL] | Not started |
| Wellbeing signal list agreed | [OPS-EX] + [LEGAL] | Not started |
| JWT user verification live in Braavos app and Fin | [ENG] + Braavos app team | Not started |
| BigQuery event pipeline confirmed working in staging | [ENG] | Not started |
| Fin Attributes mapped exactly to Zendesk ticket fields | [FIN-ADMIN] + [ENG] | Not started |
| Batch testing run: resolution rate baseline established | [FIN-ADMIN] | Not started |
| UAT completed with internal agents before external go-live | [FIN-ADMIN] + Care Ops | Not started |

---

## 9. Phase 2 scope note

Fin is not deployed in Phase 2 (October 2026). Everything in this document is scoped to External Launch (Dec 2026–Jan 2027). Phase 2 runs on Zendesk direct ticket submission only — no AI resolution layer.

---

## 10. Open questions

| Question | Impact | Owner |
|---|---|---|
| What is the agreed definition of "expression of dissatisfaction" for complaint identification? | Blocks complaint Guidance and `complaint_flag` Attribute config | Charlie Wildish + Nick Grafton-Green (Legal) |
| What is the wellbeing signal list — keywords, phrases, patterns? | Blocks Wellbeing Triage Procedure and Guidance item 2 | OPS-EX + Legal |
| Which Braavos APIs will be available, in what format, and by when? | Blocks all 5 Procedures | Braavos Engineering |
| Who owns installing Fin into the Braavos app — Care or Braavos mobile engineering? | Phase 2 Fin deployment | Charlie Wildish + Braavos Engineering |
| What is Fin's display name / identity in the Braavos app? | Personality config | Braavos product team |
| Is multilingual support required at Phase 2 or External Launch? | KB translation + Fin multilingual config | Braavos product team |
| What scale / wording for CSAT collection? | Attribute config | Braavos product team |
| Does JWT user verification exist in the Braavos app today, or is it a new build? | Blocks all data-connected Procedures | Braavos Engineering |
