# Braavos Consumer Care — H2 Build Plan
**Audience:** Care Engineering, Zendesk admins, Braavos team, Data & Analytics, Operational Excellence
**Owner:** Charlie Wildish
**Date:** May 2026
**Status:** Draft

This document lists every technical deliverable required for Phase 2 (October 2026) and External Launch (H1 2027). Most items are Care-owned, but several depend on the Braavos app/engineering team, Data & Analytics, and Operational Excellence — these are tagged explicitly so cross-team owners can plan capacity. For stakeholder context see `./scoping.md`.

**Workstream labels** (owning team in brackets):
- **[ZD]** — Zendesk admin configuration (Care)
- **[CARE-ENG]** — Care engineering / integration build (Care)
- **[BRAAVOS]** — Braavos app or Braavos engineering team (non-Care dependency)
- **[DATA]** — Data & Analytics (BigQuery pipelines, Looker, FCA reporting exports)
- **[FIN]** — Fin AI configuration (Care)
- **[AC]** — Agent Consultant configuration (Care)
- **[OPS-EX]** — Operational Excellence (process design, SOPs, verification protocols)

All analytics events are emitted to BigQuery. Looker dashboards are built on top. Neither Zendesk Explore nor Intercom Analytics are used for reporting.

---

## Cross-team dependencies summary

| Team | Phase 2 dependencies | External Launch dependencies |
|---|---|---|
| Braavos team | Ticket entry point (if web form); decision on who builds it | Fin install into app; SAR/GDPR intake form; gambling block toggle |
| Braavos team | Confirm any backend changes needed for ticket intake | Braavos data APIs for all 6 Fin Procedures (critical path); MCC list for gambling block; data-store integration for GDPR deletion |
| Braavos team | CRM integration confirmed needed for Phase 2 — confirm data schema and API availability | CRM data schema + real-time data for Zendesk sidebar; vulnerability flag schema alignment |
| Data & Analytics | BigQuery instrumentation pipelines; Phase 2 Looker dashboards | Complaint/SAR/PSR/Agent Consultant event pipelines; FCA consolidated complaints return export; vulnerability data queryability; Agent Consultant (Toolkit) interaction events |
| Operational Excellence | P1 alert thresholds (with Care Ops); agent training material for Zendesk workflows | **Owns the complaints process flow and FCA regulatory requirements** (DISP, Consumer Duty Outcome D, PSR/EMR timelines, FCA Complaints Reporting Instrument 2026, vulnerability data mandate) — defines what Care configures in Zendesk. Also owns: out-of-band verification protocol; high-risk action approval flows; QA sampling process; SOPs for specialist queues |
| Care Ops | P1 alert tooling target decision | BPO confirmed (Oliver Westlake-Simm); phone channel decision; PSR reimbursement ownership decision. Do we need data controls over what BPO agents can/can't see? If so, what are these? (Joel Petrosino) |
| Legal / Compliance | FAQ content review (Phase 1 carry-over); Consumer Duty applicability ruling for internal accounts; content sign-off for new Phase 2 packages | **Sign-off required on:** vulnerability flag schema and definitions (FCA FG21/1); FCA root-cause taxonomy mapping; AML account restriction holding scripts (POCA s.333A tipping-off rules); Fin AI complaint identification logic (legal definition of "expression of dissatisfaction"); Final Response Letter template and FOS referral wording (DISP 1.6); PSR APP fraud reimbursement decision criteria and 50/50 liability rules; SAR/GDPR deletion process (UK GDPR Art. 12, 17); Agent Consultant AML/complaints guardrails; six-monthly FCA consolidated complaints return format. **Legal lead:** Nick Grafton-Green. |

---

## Phase 2 — October 2026 (1,000 internal employees)

### Zendesk

**Routing and queue setup**
- **[ZD]** Create Braavos BPO & internal group in Zendesk with dedicated agent queue
  - Different role for Consumer/Braavos to restrict access
  - All within consumer brand (Remember Me is staying)
- **[ZD]** Create Braavos ticket form with the following custom fields:
  - `consumer_case_type` (dropdown) — top-level category from consumer care taxonomy: Account Access, Card & Payment Instrument, Payments & Transactions, Fraud & Security, Account Management, Product & Features, Technical & App, Wellbeing
  - `consumer_issue_type` (dropdown, conditional on `consumer_case_type`) — sub-issue level from consumer care taxonomy; values per category defined in `consumer-app-care-taxonomy.md`. Must be set on every ticket — by Fin on escalation (from External Launch), by agent manually in Phase 2. Field must exist from Phase 2 so data is consistent from day one.
  - `vulnerability_indicator` (checkbox) — flags the ticket for specialist handling
  - `complaint_flag` (checkbox) — marks the contact as a formal complaint (not used in Phase 2 but field must exist so Phase 3 data is consistent from day one)
  - `fca_category` — mapped automatically from the taxonomy selection when `complaint_flag` is checked (see External Launch for full FCA code list; Phase 2 uses simplified version)
- **[ZD]** Configure SLA policy for Braavos queue:
  - First reply time: 2 hours (working hours)
  - Next reply time: 8 hours (working hours)
  - Resolution: 48 hours
- **[ZD]** Configure views (for Leads, Seniors and maybe open for Phase 2):
  - Braavos open tickets (sorted by created date)
  - Braavos tickets breaching SLA
  - Braavos vulnerability-flagged tickets
  - Complaint flagged
- **[ZD]** Configure triggers:
  - Auto-tag `braavos` on all tickets submitted via Braavos escalation channel
  - Auto replies to customer
  - Routing to the agent
  - Re-routing if not picked up in X time or no skill match
- **[ZD]** Configure skill-based routing using taxonomy:
  - Define agent skills: base this on the taxonomy list
  - Assign skills to agents based on training and accreditation
  - Priority based on taxonomy value
  - Routing rules: tickets tagged `fraud` or `ato` → agents with `fraud-specialist` skill; tickets with `vulnerability_indicator` checked → agents with `wellbeing-specialist` skill; tickets with `complaint_flag` checked → agents with `complaints-handler` skill; all others → `general-consumer`
- **[ZD]** Operations team transfers
  - Auto routing/transfer as needed based on taxonomy
  - Macros to send to other teams — TBC

**Ticket entry point**
- **[BRAAVOS] / [CARE-ENG]** Confirm mechanism for consumers to submit tickets into Zendesk — options are a simple web form or email proxy (e.g. support@braavos.example routes to Zendesk). Decision needed before build starts: form requires frontend work by Braavos app team; email proxy is faster to stand up but less structured.

**Phone IVR**
- **[CARE-ENG]** Integrate phone IVR to Zendesk for complaint calls — required for Phase 2 phone support. Confirm IVR provider and routing logic before build.

**P1 volume alerting**
- **[ZD]** Configure Zendesk trigger to fire webhook when inbound ticket volume exceeds threshold within a 1-hour window (threshold set by Care Ops + Ops Excellence based on Phase 1 baseline)
- **[CARE-ENG]** Webhook receiver routes P1 alert to incident management tooling (target system to be confirmed with Care Ops — likely PagerDuty or equivalent)

---

### Engineering / integrations

- **[DATA]** Instrumentation — the following events must be emitted to BigQuery for Phase 2 Looker dashboards (Care defines events; Data & Analytics owns pipeline build and dashboard delivery):
  - `care.zendesk.ticket.created` (with `consumer_case_type`, `consumer_issue_type`)
  - `care.zendesk.ticket.first_reply` (with time-to-reply in seconds)
  - `care.zendesk.ticket.closed` (with resolution time, issue category)
  - `care.zendesk.sla.breach` (with ticket ID, SLA type)
  - `care.zendesk.vulnerability.flagged`
  - `care.p1_alert.triggered`
- **[DATA]** Looker dashboards for Phase 2 go-live: ticket volume by issue category, SLA compliance rate, P1 alert frequency. Deliver before October go-live.
- **[BRAAVOS] / [CARE-ENG]** Status notification pipeline: emit alert event when the Braavos app is degraded or down; route to Zendesk trigger for proactive agent notification and ticket auto-tagging.

---

## External Launch — Dec 2026–Jan 2027

### Zendesk — base configuration updates

- **[ZD]** Add remaining custom fields to Braavos ticket form:
  - `fos_scope` (checkbox) — whether the complaint is in scope for FOS referral
  - `redress_claimed` (decimal) — financial loss or redress amount claimed
  - `vulnerability_flags` (multi-select) — four FCA-mandated data points (see Complaints section below)
  - `complainant_type` (dropdown) — Consumer / Third Party (CMC, solicitor, PoA, next of kin)
  - `root_cause_category` — expand to full FCA taxonomy (updated taxonomy effective January 2027; must be live in Zendesk before External Launch)
  - `psr_reimbursement_applicable` (checkbox) — flags APP fraud cases requiring PSR reimbursement processing
  - `aml_restriction_flag` (checkbox) — flags accounts subject to AML hold (restricts what agents can communicate per POCA)
- **[ZD]** Extend skill-based routing for specialist queues (builds on Phase 2 skill config):
  - Add skills: `aml-specialist`, `psr-reimbursement`
  - Fraud queue — tickets tagged `fraud` or `ato` → agents with `fraud-specialist` skill
  - Wellbeing queue — tickets with `vulnerability_indicator` checked → agents with `wellbeing-specialist` skill
  - Formal complaints queue — tickets with `complaint_flag` checked → agents with `complaints-handler` skill
  - AML-restricted queue — tickets with `aml_restriction_flag` checked → agents with `aml-specialist` skill
  - Overflow and escalation rules per queue (define SLA thresholds per specialist type)
- **[ZD]** Configure agent workspace sidebar panels (dependent on Consumer CRM integration):
  - Consumer CRM panel: account status, account open date, balance (masked), linked cards, vulnerability flags, prior complaints
  - Transaction panel: last 30 transactions with status, amount, merchant name, failure reason
  - Interaction history panel: prior Zendesk tickets and Fin conversations for this consumer
  - Regulatory flags panel: AML restriction status, complaint open/closed history, PSR reimbursement status

---

### Zendesk — complaints case management

**Process and regulatory ownership: [OPS-EX]** — Operational Excellence owns the complaints process flow and the FCA regulatory requirements that drive it (DISP 1.3–1.6, Consumer Duty Outcome D, PSR/EMR 2011 timelines, FCA Complaints Reporting Instrument 2026, vulnerability data mandate from January 2027). Ops Excellence defines: what counts as a complaint, the handling stages, decision points, escalation criteria, FRL content standards, FOS referral process, root-cause taxonomy, QA sampling criteria, and FCA reporting field definitions. Care implements the Ops Excellence specification in Zendesk. All `[ZD]` items below are Care-owned configuration of an Ops Excellence-owned process.

**Legal sign-off required on (Nick Grafton-Green):** FRL template wording and FOS referral leaflet; AML holding message content (POCA s.333A — no disclosure of investigation); PSR reimbursement decision criteria and 50/50 liability split application; vulnerability flag definitions; "expression of dissatisfaction" definition that drives Fin AI complaint identification; six-monthly FCA consolidated complaints return format before first submission (July 2027).

- **[ZD]** Configure complaint SLA policy (separate from standard Braavos SLA):
  - Acknowledgement: by close of next business day after receipt
  - Summary Resolution Communication: day 3 (if resolved to customer's satisfaction — DISP 1.6.1AR)
  - Holding response: day 4 if unresolved, then every 10 business days (automated)
  - Final Response Letter: 8-week clock with escalation alert at week 6
  - Payment services complaints (PSR/EMR): 15-business-day clock, extendable to 35
- **[ZD]** Configure complaint acknowledgement trigger: on ticket creation with `complaint_flag` checked, send acknowledgement macro (case reference, named handler, indicative timeline, FOS rights) by close of next business day
- **[ZD]** Configure holding response automation: if complaint ticket unresolved after 3 business days, trigger holding response macro and repeat every 10 business days
- **[ZD]** Configure Final Response Letter macro: template with FOS leaflet attachment, 6-month FOS referral window, FOS contact details
- **[ZD]** Configure systemic issue trigger: when 5 or more complaint tickets share the same `root_cause_category` value within a 30-day window, fire webhook alerting Complaints Manager — implement via Zendesk webhook + BigQuery query on `care.complaint.opened` events (confirm approach with engineering)
- **[ZD]** Configure internal review workflow: complaint tickets escalated for internal review are reassigned to a separate Zendesk group (Senior Review), preventing reassignment to original handler
- **[ZD]** Configure QA sampling:
  - Auto-tag `qa_required` on 10% of closed complaint tickets (random sample via Zendesk trigger with modulo condition on ticket ID)
  - Auto-tag `qa_required` on 100% of tickets with `vulnerability_indicator` checked
  - Auto-tag `qa_required` on 100% of tickets with `redress_claimed` > 500
- **[ZD]** Build macros for standard regulated responses:
  - Complaint acknowledgement (pre-populated with case reference, handler name, FOS rights)
  - Summary Resolution Communication
  - Holding response (day 4 and 10-day repeat)
  - Final Response Letter (with FOS leaflet placeholder)
  - AML holding message (restricted per POCA — no disclosure of investigation)
  - PSR reimbursement acknowledgement
- **[AC]** High-risk actions (refund, account reinstatement, card block override) are initiated via Toolkit UI, not Zendesk macros — supervisor approval step built into the Toolkit action flow; Zendesk ticket updated with outcome via API
- **[ZD]** Configure FCA data export:
  - All complaint tickets with `complaint_flag` checked, exportable with full field set for FCA consolidated complaints return (six-monthly, first period January–June 2027) — available in Looker
  - Vulnerability data points: four FCA fields queryable from Looker via `care.complaint.*` events

**Vulnerability data fields (mandatory from January 2027)**

Four fields must be present on every complaint ticket and reportable to FCA:

| Field | Type | Description |
|---|---|---|
| `vuln_opened_vulnerable_consumer` | Boolean | Complaint opened by a consumer identified as in vulnerable circumstances |
| `vuln_closed_vulnerable_consumer` | Boolean | Complaint closed by a consumer identified as in vulnerable circumstances |
| `vuln_opened_failure_to_consider` | Boolean | Complaint opened relating to Checkout's failure to consider or respond to vulnerability |
| `vuln_closed_failure_to_consider` | Boolean | Complaint closed relating to Checkout's failure to consider or respond to vulnerability |

Note: where the complainant is a third party (next of kin, PoA), `complainant_type` distinguishes between vulnerability of the consumer and vulnerability of the complainant. Both data points must be separately capturable.

---

### Fin AI — Procedures

Five Fin Procedures are required for External Launch. Each Procedure requires a data connector to a Braavos API. **These are blocked until Braavos Engineering confirms API availability — earliest Q3 2026 for scoping.**

| Procedure | What it does | Data connector required |
|---|---|---|
| ATO triage | Identifies account takeover signals, classifies the contact, and escalates to the fraud queue with structured context (signals, risk indicators, timeline) — account freeze and resolution are human-agent actions, not Fin actions | Account status API, recent login events, device fingerprint |
| Transaction lookup | Retrieves transaction status, failure reason, and resolution timeline for a specific transaction | Transaction API |
| Scam intake | Structured intake for APP fraud and scam reports; captures transaction references, scam type, timeline; routes to fraud queue | Transaction API, account API |
| Context handoff | Passes full conversation context, issue category, and customer data to Zendesk on escalation | Zendesk ticket creation API |
| Wellbeing triage | Identifies wellbeing disclosure signals, escalates immediately to wellbeing queue with classification — Fin does not respond to the consumer; all messaging and signposting is handled by the human agent | None (response logic only) |

**Knowledge base**
- **[FIN]** Load full consumer care knowledge base into Fin:
  - Account access and recovery
  - Card management
  - Payments (failure reasons, status, timelines)
  - Fraud and security reporting
  - Technical issue / known fix library
  - Transaction recovery (CPR, ATM non-dispense, DD Guarantee)
  - Product and feature KB (FSCS, fees, cashback/rewards)
  - AML account restriction messaging (response-limited per POCA)
  - Dispute communications
  - Supporting content for each of the 6 Procedures above
- **[FIN]** Tag all KB articles to the consumer care taxonomy before loading: each article must carry `consumer_case_type` and `consumer_issue_type` metadata. This enables taxonomy-level retrieval accuracy measurement in BigQuery and ensures Fin surfaces the correct content per classification. Articles covering multiple issue types must be tagged to each applicable type.

**Escalation and classification**
- **[FIN]** Configure Fin escalation routing: unresolved conversations create a Zendesk ticket in the Braavos queue with full conversation transcript attached — open question: do we need to route to other Checkout teams, e.g. Fraud?
- **[FIN]** Configure Fin attributes for automatic classification on every conversation: `consumer_case_type` and `consumer_issue_type` (mapped to Zendesk dropdown values), resolution status, CSAT. Both taxonomy attributes must be passed to the Zendesk ticket on escalation so BigQuery events carry full taxonomy metadata from External Launch go-live.
- **[FIN]** Configure Fin complaint identification: if a conversation contains an expression of dissatisfaction, Fin must set `complaint_flag = true` on the resulting Zendesk ticket and route to the complaints queue — Fin must not attempt to resolve a complaint as a standard query

**Analytics**
- **[FIN]** Ensure all Fin conversation events are emitted to BigQuery (not Intercom Analytics): `care.fin.conversation.started`, `care.fin.conversation.resolved`, `care.fin.escalation.triggered`, `care.fin.procedure.started`, `care.fin.procedure.completed`, `care.fin.complaint_identified`, `care.fin.csat.submitted`

---

### Engineering / integrations

- **[BRAAVOS] / [CARE-ENG]** Install Fin into Braavos app — TBC whether this requires mobile engineering support from the Braavos app team or can be handled by Care. Confirm ownership and dependency before Q4 2026 build starts.
- **[CARE-ENG] / [BRAAVOS]** Consumer CRM data integration into Zendesk agent workspace:
  - Surface in Zendesk sidebar: account status, account open date, balance (masked), transaction history (last 30 transactions), prior care contacts, vulnerability flags from CRM
  - Must update in real time or near-real time (not batch)
  - Confirm data schema with Consumer CRM team (non-Care dependency); vulnerability flag schema must match Zendesk fields
  - **Confirmed needed for Phase 2.** Pull Consumer CRM integration into Phase 2 build — confirm data schema and API availability with Consumer CRM team before August 2026.
- **[CARE-ENG] / [BRAAVOS]** SAR and GDPR deletion request handling:
  - Intake form (in-app or web) — Braavos app team builds the in-app form; Care builds Zendesk intake processing
  - Generates Zendesk ticket tagged `sar` or `gdpr_deletion`; Zendesk trigger routes to dedicated queue with 30-day SLA clock (GDPR Art. 12)
  - On deletion request: integration with Consumer CRM and Braavos data store to action erasure (requires Braavos engineering); audit log retained separately per legal hold requirements
- **[CARE-ENG]** PSR APP fraud reimbursement workflow:
  - Zendesk ticket tagged `psr_reimbursement` triggers notification to reimbursement owner (Finance/Care/Fraud — ownership TBC, Care Ops decision required)
  - 5-business-day SLA clock configured in Zendesk
  - Outcome (reimbursed / not reimbursed / partial) recorded on ticket for regulatory reporting
- **[BRAAVOS] / [CARE-ENG]** Gambling block:
  - In-app toggle (Braavos app team delivery) sends block/unblock instruction to card processor via Braavos API
  - Zendesk trigger: if consumer contacts Care about gambling block, auto-tag `gambling_block` and route to standard queue (not specialist — no FCA obligation to delay or question)
  - Agreed list of blockable MCCs required from Braavos engineering before build
- **[OPS-EX]** Tag all consumer care SOPs to the consumer care taxonomy: each SOP must carry `consumer_case_type` and `consumer_issue_type` metadata before External Launch agent training. This enables the Agent Consultant to surface the correct SOP per ticket classification and enables Reflex to link contact volume to specific process steps. Ops Excellence owns the tagging; Care Product to provide taxonomy reference (`consumer-app-care-taxonomy.md`).
- **[OPS-EX] / [CARE-ENG]** Out-of-band verification protocol for high-risk agent actions (refunds, reversals, account reinstatement):
  - Ops Excellence designs verification steps (challenge questions, identity confirmation, audit log); Care builds into Zendesk macro
  - High-risk action macro requires supervisor approval field before submission
- **[DATA] / [CARE-ENG]** Reflex — Consumer Fin and Zendesk ticket ingestion:
  - Reflex must ingest Consumer Fin conversation events and Zendesk ticket events for the Braavos queue, with full taxonomy metadata (`consumer_case_type`, `consumer_issue_type`) on every record
  - This enables Reflex to attribute contact volume to taxonomy-level issue types, identify high-volume drivers, and surface them to engineering and product for root-cause investigation
  - Dependency: taxonomy fields must be populated on all tickets (Fin-originated and agent-created) before Reflex ingestion is meaningful — enforce non-null policy on `consumer_issue_type` from External Launch go-live
  - Confirm with Data & Analytics whether Braavos Fin/Zendesk events flow through the same Reflex pipeline as merchant tickets or require a separate consumer segment feed
- **[DATA]** FCA regulatory reporting export:
  - Automated six-monthly data export from Zendesk in FCA consolidated complaints return format (Complaints Reporting Instrument 2026 / FCA 2026/12)
  - Fields: complaint volume by product/channel/root-cause, uphold rate, time-to-resolve, redress paid, four vulnerability data points
  - First reporting period: January–June 2027 (export required by July 2027)
  - Must be able to purge personal data on user request from tickets, Fin and analytics
  - 5 year retention rules across support data
- **[DATA]** Instrumentation — additional events to emit to BigQuery for External Launch (Fin events covered separately in Fin section above):
  - `care.complaint.opened` (with `consumer_case_type`, `consumer_issue_type`, channel, `vulnerability_indicator`, `complainant_type`)
  - `care.complaint.sla.acknowledgement_sent`
  - `care.complaint.sla.src_issued`
  - `care.complaint.sla.holding_response_sent`
  - `care.complaint.frl_issued`
  - `care.complaint.fos_referred`
  - `care.complaint.closed` (with uphold status, redress amount)
  - `care.sar.request.opened`
  - `care.sar.request.closed`
  - `care.psr.reimbursement.opened`
  - `care.psr.reimbursement.closed` (with outcome)
  - `care.agent_consultant.suggestion_shown` (with suggestion type, ticket ID)
  - `care.agent_consultant.suggestion_accepted`
  - `care.agent_consultant.lookup_triggered` (with lookup type)

---

### Agent Consultant and human agent actions (External Launch)

The Agent Consultant is the AI assistance layer for Braavos care agents. The Agent Toolkit is its UI surface — a Zendesk side panel through which all data queries, data changes, and Consultant suggestions are delivered. All agent actions that query or change data must be executed through the Toolkit UI. Both depend on the Consumer CRM integration being live.

**Toolkit — context panels** (read-only; agent-initiated)

Build: **[AC]** side panel configuration (requires Consumer CRM integration)

The Toolkit is a Zendesk side panel that loads alongside the open ticket. Context panels are read-only — no agent action required to populate them. They load automatically when a ticket is opened, pulling live data from the Consumer CRM and Zendesk history.

- **Consumer CRM panel**: shows account status (active/frozen/closed), account open date, masked balance, linked cards, vulnerability flags from CRM, and prior complaints. This is the primary context panel — always visible.
- **Transaction panel**: last 30 transactions listed with status, amount, merchant name, and failure reason where applicable. Agent can scroll the list; no interaction beyond browsing.
- **Interaction history panel**: prior Zendesk tickets and Fin conversation summaries for this consumer, sorted by recency. Gives the agent full prior contact history without leaving the ticket.
- **Regulatory flags panel**: surfaces AML restriction status (flagged / not flagged), complaint open/closed history, and PSR reimbursement status if applicable. Read-only; agent cannot change flags here — changes happen via data change actions.
- **Idea**: app impersonation feature so the agent can log in as the customer via web interface — to help diagnose UX issues. To be assessed.

---

**Toolkit — data queries** (agent-initiated; results displayed in panel)

Build: **[AC]** lookup actions within Toolkit UI

Data queries are agent-initiated lookups triggered by clicking an action in the Toolkit panel. Results appear inline in the panel, replacing the prompt. The agent enters a reference (e.g. transaction ID) and the Toolkit fetches and displays the result.

- **Transaction lookup**: agent enters a transaction ID or selects from the transaction panel; Toolkit returns detailed status, failure reason, and resolution timeline. Designed for cases where the consumer queries a specific transaction and the panel summary is insufficient.
- **Consumer data lookup**: agent triggers a fresh pull of account status, balance, and recent transactions from the Consumer CRM — for cases where the auto-loaded context panel data may be stale or incomplete.

---

**Toolkit — data changes** (agent-initiated; all require supervisor approval before execution)

Build: **[AC]** action flows within Toolkit UI; **[OPS-EX]** defines verification steps; **[AC]** builds them into the flow

Data changes are destructive or sensitive actions that modify the consumer's account or data. Every action follows a gated flow: agent initiates → identity verification step (challenge questions per OPS-EX protocol) → supervisor approval field (supervisor name or ID required) → confirmation screen → execution. The Zendesk ticket is updated automatically with the action outcome. No data change can be executed without completing all steps.

*High-risk actions* (out-of-band verification + supervisor approval)
- **Account freeze or unfreeze**: agent-initiated; triggers verification flow. Freeze is immediate on approval; unfreeze requires same steps.
- **Refund or reversal**: agent enters transaction reference and refund amount; verification and approval flow before execution. Outcome (approved / rejected / partial) written back to app view.
- **Account reinstatement**: restores a closed or restricted account; highest-risk action, same approval flow. Legal or compliance review may be required upstream before agent can initiate.
- **Card block override**: overrides an active card block placed by the system or a prior agent. Requires justification field in addition to standard approval.

*Regulated process actions* (SLA-clocked; process-gated)
- **GDPR deletion**: agent initiates a right-to-erasure request from the Toolkit. Deletion is executed by Braavos engineering against the data store; the Toolkit action triggers the request and tracks status.

*Standard agent actions* (agent-initiated; identity verification only; no supervisor approval required)
- **Gambling block toggle**: agent blocks or unblocks gambling merchant transactions on behalf of the consumer, where the consumer has contacted Care rather than using the in-app toggle. No specialist queue; no FCA obligation to delay or question the request. Toolkit action calls Braavos API, which sends block/unblock instruction to the card processor. Agreed MCC list required from Braavos Engineering before build.

---

**Consultant-assisted actions** (Consultant proactively prompts; agent confirms and executes via Toolkit)

Build: **[AC]** prompt configuration and Toolkit action binding

Consultant-assisted actions are surfaced by the AI as suggestions in the Toolkit panel — the agent does not need to find or initiate them. The Consultant analyses the ticket context (Fin escalation notes, conversation transcript, ticket fields) and surfaces a prompt such as "This looks like an ATO — consider freezing the account." The agent reads the suggestion, decides whether to act, and confirms or dismisses it. Execution happens via the Toolkit action flow, not via the suggestion itself.

- **ATO (Account Takeover)**: Consultant surfaces account takeover signals and risk classification from the Fin escalation (suspicious login events, device mismatch, etc.). Agent reviews and initiates account freeze via the Toolkit high-risk action flow. Consultant does not take any account action.
- **Wellbeing**: Consultant surfaces a wellbeing signal identified during the Fin conversation (consumer disclosed distress, safeguarding indicator, etc.) with a prompt to handle carefully. Agent authors and sends the response directly. Consultant must not draft the consumer-facing message for wellbeing contacts — human authorship is required.
- **Refund or reversal**: Consultant identifies a refund signal from ticket context (e.g. transaction failure with consumer detriment). Agent reviews the suggestion, confirms the transaction reference, and executes via the Toolkit refund action flow.
- **Card freeze or unfreeze**: Consultant identifies a card action signal (consumer reported lost/stolen, or block incorrectly applied). Agent confirms and executes via Toolkit.
- **Complaint flagging**: Consultant identifies an expression of dissatisfaction in the ticket or escalation transcript and prompts the agent to set `complaint_flag = true`. Agent confirms; flag is applied to the ticket and SLA clock starts.
- **Escalation routing**: Consultant detects a specialist signal (fraud indicators, vulnerability disclosure, AML flags) and prompts the agent to reroute to the appropriate specialist queue. Agent confirms; ticket is reassigned.
- **Suggested reply**: Consultant drafts a response from the knowledge base based on the ticket context and issue category. Agent reviews, edits as needed, and sends. Agent must always review before sending — the Toolkit does not send automatically.

---

**Standard Zendesk actions** (no data query or change; ZD macros appropriate)

Build: **[ZD]** macros (already listed in complaints case management section above)

These actions do not require Toolkit integration — they are standard Zendesk macros that agents apply from the ticket view. No data is queried or changed in external systems.

- **AML holding message**: POCA-compliant holding script the agent applies when the account is under AML restriction. Pre-written; agent selects the macro and sends. Content is legally reviewed and fixed — agents cannot edit.
- **Complaint acknowledgement, holding response, Final Response Letter**: regulated response templates applied at each stage of the complaint lifecycle. Pre-populated with case reference and handler name where available.
- **PSR reimbursement**: macro to initiate the reimbursement decision workflow and set the 5-business-day SLA clock. Ownership of the reimbursement decision is TBC (Finance/Care/Fraud).
- **SAR processing**: macro to log a Subject Access Request and trigger the 30-day GDPR Art. 12 SLA clock.

---

**Consultant configuration**

Build: **[AC]**

- **[AC]** Knowledge base access: all Fin KB content available for Consultant suggestions (same content, agent-facing surface)
- **[AC]** QA on closed tickets: autonomous review against defined quality criteria; results flagged for agent or team lead review — no agent action required

**Guardrails**
- **[AC]** Responses must not disclose AML investigation status
- **[AC]** Complaint responses must not offer or imply settlement without agent review
- **[AC]** Wellbeing disclosures must surface to the agent immediately; Consultant must not respond to the consumer

**Analytics**
- **[AC]** All Consultant interaction events emitted to BigQuery (see instrumentation section)

---

## Sequencing and dependencies

```
PHASE 2 (by October 2026)
│
├── Ticket entry point decision (web form vs email proxy)              ← Must resolve before ZD config
│
├── Zendesk base config (queue, form, fields, SLA, views, triggers)   ← Week 1–2 after green light
│   ├── Requires: Zendesk routing decision confirmed (end Q2 2026)
│   └── Includes: skill-based routing (general-consumer, fraud, wellbeing, complaints)
│
├── P1 alerting webhook                                                ← Parallel with ZD config
│   └── Requires: incident management tooling target confirmed
│
└── BigQuery instrumentation                                           ← Final, before go-live

EXTERNAL LAUNCH PREP (Q3 2026 – Q1 2027)
│
├── Q3 2026: Consumer care taxonomy finalised (all categories + sub-issues) ← Gates Zendesk issue_type field values, Fin attribute config, KB tagging, SOP tagging
│
├── Q3 2026: Braavos API scoping with Engineering                     ← Gates all Fin Procedures
│
├── Q3 2026: Consumer CRM data schema agreed                          ← Gates ZD sidebar + Agent Consultant lookups
│
├── Q3 2026: Vulnerability flag schema agreed (Legal + Care Ops)      ← Gates ZD fields + Fin config
│
├── Q3–Q4 2026: Zendesk External Launch config                        ← Builds on Phase 2 ZD config
│   ├── Extend skill routing (add aml-specialist, psr-reimbursement)
│   ├── Specialist queues (fraud, wellbeing, complaints, AML)
│   ├── Complaint SLA clocks (acknowledgement, SRC, holding, FRL, PSR)
│   ├── QA sampling automation
│   ├── Vulnerability data fields (4 FCA data points)
│   ├── FCA taxonomy codes updated (December 2026 deadline)
│   └── Zendesk macros (acknowledgement, SRC, holding, FRL, AML, PSR)
│
├── Q4 2026: Consumer CRM → Zendesk sidebar integration               ← Gates Agent Consultant (Toolkit UI + data lookups)
│
├── Q4 2026: Agent Consultant configuration (incl. Toolkit UI)        ← Requires CRM integration
│   └── Autonomous: suggested reply, KB retrieval, transaction lookup, data lookup, QA
│       Human-in-the-loop: ATO freeze, wellbeing response, refund/reversal, card freeze, complaint flag, escalation routing
│
├── Q4 2026: Fin install into Braavos app                             ← Ownership TBC (Care vs Braavos mobile eng)
│
├── Q4 2026: Fin knowledge base + Procedures build + simulation       ← Requires Braavos APIs live + Fin installed
│   └── ATO → Transaction lookup → Scam intake → Diagnostic →
│       Context handoff → Wellbeing triage (in priority order)
│
├── Q4 2026: SAR/GDPR intake + deletion workflow
│
├── Q4 2026: PSR reimbursement workflow                               ← Requires ownership decision
│
├── Q1 2027: FCA reporting export (test with FCA ahead of Jan 2027)
│
└── Q1 2027: UAT + agent training before External Launch go-live
```

---

## Open questions for engineering

| Question | Impact | Owner |
|---|---|---|
| What is the ticket entry point for Phase 2 — web form or email proxy? If form, does Braavos app team build it or Care? | Phase 2 ticket submission | Charlie Wildish + Braavos app team |
| Is Consumer CRM integration needed for Phase 2 launch? Confirmed needed for Phase 2 — confirm data schema with Consumer CRM team | Phase 2 scope + Agent Toolkit timing | Charlie Wildish + Consumer CRM team |
| Who owns installing Fin into the Braavos app — Care or Braavos mobile engineering? | External Launch Fin deployment | Charlie Wildish + Braavos Engineering |
| Which incident management tool does P1 alerting fire to? | P1 alerting build | Care Ops |
| What APIs does Braavos expose for Fin Procedures — and when? | All 6 Fin Procedures blocked without this | Braavos Engineering |
| What is the Consumer CRM data schema? Which fields are available for Zendesk sidebar? | Consumer CRM integration | Consumer CRM team |
| What vulnerability flag fields exist in the Consumer CRM? Do they match the 4 FCA data points? | Vulnerability reporting | Legal + Consumer CRM team |
| What is the agreed MCC list for gambling block? | Gambling block build | Braavos Engineering / Compliance |
| Is call recording needed? If yes, which system — and how does it link to Zendesk cases? | Investigation tooling, FCA DISP compliance | Charlie Wildish / Oliver |
| Who owns PSR reimbursement processing — Finance, Care, or Fraud? | PSR reimbursement workflow | TBD |
| Which Braavos actions should Agent Consultant be permitted to execute human-in-the-loop — and what approvals are required? | Agent Consultant scope and guardrails | Charlie Wildish + Engineering |
| Does Agent Consultant have access to the Consumer CRM API directly, or via the Zendesk sidebar integration? | Agent Consultant data lookup architecture | Engineering |
