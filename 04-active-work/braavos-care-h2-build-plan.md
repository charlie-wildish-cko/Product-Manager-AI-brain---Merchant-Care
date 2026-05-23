# Braavos Consumer Care — H2 Build Plan
**Audience:** Engineering team, Zendesk admins
**Owner:** Charlie Wildish
**Date:** May 2026
**Status:** Draft

This document lists every Care-owned technical deliverable for Phase 2 (October 2026) and External Launch (H1 2027). It is the working build reference for the engineering team and Zendesk admins. For stakeholder context see `braavos-care-scoping.md`.

Each item is labelled: **[ZD]** = Zendesk admin task · **[ENG]** = engineering/integration task · **[FIN]** = Fin AI configuration · **[AC]** = Agent Consultant / Agent Consultant configuration

All analytics events are emitted to BigQuery. Looker dashboards are built on top. Neither Zendesk Explore nor Intercom Analytics are used for reporting.

---

## Phase 2 — October 2026 (1,000 internal employees)

### Zendesk

**Routing and queue setup**
- **[ZD]** Create Braavos group in Zendesk with dedicated agent queue
- **[ZD]** Create Braavos ticket form with the following custom fields:
  - `braavos_issue_category` (dropdown) — values aligned to consumer care taxonomy: Account Access, Card & Payment Instrument, Payments & Transactions, Fraud & Security, Account Management, Product & Features, Technical & App, Wellbeing
  - `braavos_user_type` (dropdown) — Internal Employee / External Consumer (set to Internal Employee for Phase 2; enables Phase 3 without schema change)
  - `vulnerability_indicator` (checkbox) — flags the ticket for specialist handling
  - `complaint_flag` (checkbox) — marks the contact as a formal complaint (not used in Phase 2 but field must exist so Phase 3 data is consistent from day one)
  - `root_cause_category` (dropdown) — FCA taxonomy codes (see External Launch for full list; Phase 2 uses simplified version)
- **[ZD]** Configure SLA policy for Braavos queue:
  - First reply time: 2 hours (working hours)
  - Next reply time: 8 hours (working hours)
  - Resolution: 48 hours
- **[ZD]** Configure views:
  - Braavos open tickets (sorted by created date)
  - Braavos tickets breaching SLA
  - Braavos vulnerability-flagged tickets
- **[ZD]** Configure triggers:
  - Auto-tag `braavos` on all tickets submitted via Braavos escalation channel
  - Notify assignee on new Braavos ticket
  - Escalation alert if ticket unassigned after 1 hour
- **[ZD]** Configure skill-based routing:
  - Define agent skills: `general-consumer`, `fraud-specialist`, `wellbeing-specialist`, `complaints-handler`
  - Assign skills to agents based on training and accreditation
  - Routing rules: tickets tagged `fraud` or `ato` → agents with `fraud-specialist` skill; tickets with `vulnerability_indicator` checked → agents with `wellbeing-specialist` skill; tickets with `complaint_flag` checked → agents with `complaints-handler` skill; all others → `general-consumer`
  - Overflow rule: if no skilled agent available within SLA threshold, escalate to team lead

**Ticket entry point**
- **[ENG]** Confirm mechanism for consumers to submit tickets into Zendesk — options are a simple web form or email proxy (e.g. support@braavos.example routes to Zendesk). Decision needed before build starts: form requires frontend work by Braavos app team; email proxy is faster to stand up but less structured.

**P1 volume alerting**
- **[ZD]** Configure Zendesk trigger to fire webhook when inbound ticket volume exceeds threshold within a 1-hour window (threshold set by Care Ops based on Phase 1 baseline)
- **[ENG]** Webhook receiver routes P1 alert to incident management tooling (confirm target system with Care Ops — likely PagerDuty or equivalent)

---

### Engineering / integrations

- **[ENG]** Instrumentation — the following events must be emitted to BigQuery for Phase 2 Looker dashboards:
  - `care.zendesk.ticket.created` (with `braavos_issue_category`, `braavos_user_type`)
  - `care.zendesk.ticket.first_reply` (with time-to-reply in seconds)
  - `care.zendesk.ticket.closed` (with resolution time, issue category)
  - `care.zendesk.sla.breach` (with ticket ID, SLA type)
  - `care.zendesk.vulnerability.flagged`
  - `care.p1_alert.triggered`

---

## External Launch — H1 2027

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
- **[ZD]** Build internal note templates for high-risk actions (refund, account reinstatement, card block override) — requires supervisor approval field before submission
- **[ZD]** Configure FCA data export views:
  - All complaint tickets with `complaint_flag` checked, exportable with full field set for FCA consolidated complaints return (six-monthly, first period January–June 2027) — exported from Zendesk via API; final return formatted in BigQuery
  - Vulnerability data points: four FCA fields queryable from BigQuery via `care.complaint.*` events

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

Six Fin Procedures are required for External Launch. Each Procedure requires a data connector to a Braavos API. **These are blocked until Braavos Engineering confirms API availability — earliest Q3 2026 for scoping.**

| Procedure | What it does | Data connector required |
|---|---|---|
| ATO triage | Identifies account takeover signals, freezes account, routes to fraud queue | Account status API, recent login events, device fingerprint |
| Transaction lookup | Retrieves transaction status, failure reason, and resolution timeline for a specific transaction | Transaction API |
| Scam intake | Structured intake for APP fraud and scam reports; captures transaction references, scam type, timeline; routes to fraud queue | Transaction API, account API |
| Diagnostic capture | Captures structured data for technical issues (error codes, device, OS, app version) before escalation | None (structured form) |
| Context handoff | Passes full conversation context, issue category, and customer data to Zendesk on escalation | Zendesk ticket creation API |
| Wellbeing triage | Identifies wellbeing disclosure signals, responds with appropriate signposting, routes to wellbeing queue | None (response logic only) |

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

**Escalation and classification**
- **[FIN]** Configure Fin escalation routing: unresolved conversations create a Zendesk ticket in the Braavos queue with full conversation transcript attached
- **[FIN]** Configure Fin attributes for automatic classification on every conversation: `braavos_issue_category` (mapped to Zendesk dropdown values), resolution status, CSAT
- **[FIN]** Configure Fin complaint identification: if a conversation contains an expression of dissatisfaction, Fin must set `complaint_flag = true` on the resulting Zendesk ticket and route to the complaints queue — Fin must not attempt to resolve a complaint as a standard query

**Analytics**
- **[FIN]** Ensure all Fin conversation events are emitted to BigQuery (not Intercom Analytics): `care.fin.conversation.started`, `care.fin.conversation.resolved`, `care.fin.escalation.triggered`, `care.fin.procedure.started`, `care.fin.procedure.completed`, `care.fin.complaint_identified`, `care.fin.csat.submitted`

---

### Engineering / integrations

- **[ENG]** Install Fin into Braavos app — TBC whether this requires mobile engineering support from the Braavos app team or can be handled by Care. Confirm ownership and dependency before Q4 2026 build starts.
- **[ENG]** Consumer CRM data integration into Zendesk agent workspace:
  - Surface in Zendesk sidebar: account status, account open date, balance (masked), transaction history (last 30 transactions), prior care contacts, vulnerability flags from CRM
  - Must update in real time or near-real time (not batch)
  - Confirm data schema with Consumer CRM team; vulnerability flag schema must match Zendesk fields
  - **Open question:** is Consumer CRM integration also needed for Phase 2 launch (not just External Launch)? If yes, pull this forward into the Phase 2 build.
- **[ENG]** SAR and GDPR deletion request handling:
  - Intake form (in-app or web) generates Zendesk ticket tagged `sar` or `gdpr_deletion`
  - Zendesk trigger routes to dedicated queue with 30-day SLA clock (GDPR Art. 12)
  - On deletion request: integration with Consumer CRM and Braavos data store to action erasure; audit log retained separately per legal hold requirements
- **[ENG]** PSR APP fraud reimbursement workflow:
  - Zendesk ticket tagged `psr_reimbursement` triggers notification to reimbursement owner (Finance/Care/Fraud — ownership TBC)
  - 5-business-day SLA clock configured in Zendesk
  - Outcome (reimbursed / not reimbursed / partial) recorded on ticket for regulatory reporting
- **[ENG]** Gambling block:
  - In-app toggle (Braavos app team delivery) sends block/unblock instruction to card processor via Braavos API
  - Zendesk trigger: if consumer contacts Care about gambling block, auto-tag `gambling_block` and route to standard queue (not specialist — no FCA obligation to delay or question)
  - Agreed list of blockable MCCs required from Braavos Engineering before build
- **[ENG]** Out-of-band verification protocol for high-risk agent actions (refunds, reversals, account reinstatement):
  - Define verification steps and build into Zendesk macro (challenge questions, identity confirmation, audit log)
  - High-risk action macro requires supervisor approval field before submission
- **[ENG]** FCA regulatory reporting export:
  - Automated six-monthly data export from Zendesk in FCA consolidated complaints return format (Complaints Reporting Instrument 2026 / FCA 2026/12)
  - Fields: complaint volume by product/channel/root-cause, uphold rate, time-to-resolve, redress paid, four vulnerability data points
  - First reporting period: January–June 2027 (export required by July 2027)
- **[ENG]** Instrumentation — additional events to emit to BigQuery for External Launch (Fin events covered separately in Fin section above):
  - `care.complaint.opened` (with `braavos_issue_category`, channel, `vulnerability_indicator`, `complainant_type`)
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

### Agent Toolkit (External Launch)

The Agent Toolkit is the Zendesk side panel app surfacing consumer context to agents. It depends on the Consumer CRM integration being live.

- **[ZD]** Configure Agent Toolkit side panel with the following panels:
  - Consumer CRM panel: account status, account open date, balance (masked), linked cards, vulnerability flags, prior complaints
  - Transaction panel: last 30 transactions with status, amount, merchant name, failure reason
  - Interaction history panel: prior Zendesk tickets and Fin conversations for this consumer
  - Regulatory flags panel: AML restriction status, complaint open/closed history, PSR reimbursement status

---

### Agent Consultant (External Launch)

The Agent Consultant assists Braavos care agents in real time within the Zendesk workspace. It operates in two modes: autonomous (no agent approval needed) and human-in-the-loop (agent must confirm before execution).

- **[AC]** Configure Agent Consultant knowledge base access: all Fin KB content available for agent-facing suggestions (same content as Fin, different surface)
- **[AC]** Configure autonomous skills:
  - Suggested reply: draft response based on ticket content and KB, surfaced as editable suggestion in agent workspace
  - Knowledge retrieval: surface relevant KB articles as agent types or updates a ticket
  - Transaction lookup: retrieve transaction details for a referenced transaction ID and inject into ticket context
  - Consumer data lookup: retrieve account status, balance, and recent transactions from Consumer CRM
  - QA on closed tickets: autonomous review of closed tickets against defined quality criteria, results flagged for agent or team lead review
- **[AC]** Configure human-in-the-loop skills (agent must confirm before execution):
  - Refund or reversal initiation: Agent Consultant drafts the action, agent reviews and approves
  - Card freeze or unfreeze: Agent Consultant proposes action based on ticket context, agent confirms
  - Complaint flag: if Agent Consultant identifies an expression of dissatisfaction not already flagged, it prompts agent to confirm complaint status
  - Escalation routing: if Agent Consultant detects specialist signals (fraud, vulnerability, AML), it prompts agent to reroute to the appropriate queue
- **[AC]** Configure guardrails:
  - Responses must not disclose AML investigation status
  - Complaint responses must not offer or imply settlement without agent review
  - Wellbeing disclosures must be surfaced to the agent immediately, not handled autonomously
- **[AC]** Confirm all Agent Consultant interaction events are emitted to BigQuery (see instrumentation above)

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
├── Q4 2026: Consumer CRM → Zendesk sidebar integration               ← Gates Agent Toolkit + Agent Consultant data lookups
│
├── Q4 2026: Agent Toolkit side panel build                           ← Requires CRM integration
│
├── Q4 2026: Agent Consultant configuration                           ← Requires Agent Toolkit + CRM integration
│   └── Autonomous: suggested reply, KB retrieval, transaction lookup, data lookup, QA
│       Human-in-the-loop: refund/reversal, card freeze, complaint flag, escalation routing
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
| Is Consumer CRM integration needed for Phase 2 launch, or can it wait until External Launch? | Phase 2 scope + Agent Toolkit timing | Charlie Wildish |
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
