# Consumer Care — Capabilities, Ownership & Delivery Plan

**Last updated**: April 2026
**Owner**: Charlie Wildish, Care Product
**Status**: Working draft

This document maps every capability required to support the Braavos consumer wallet to the team that must build it, with a description of what each team delivers and by when. Derived from the JTBD analysis and flow mapping in the consumer care requirements sheet.

**Support model by phase**: Braavos handles all consumer support in Phase 1 (50-consumer beta, Jun '26) and Phase 2 (1,000-consumer pilot, Oct '26). Care takes over support at External launch (H1 2027). Content and app capabilities are built ahead of Care's involvement so the self-serve layer is ready at each phase.

---

## Ownership model

| Team | What they own |
|---|---|
| **Braavos** | All app screens, flows, and self-serve features; all consumer data (source of truth — exposes to Care via API); handles all consumer support in Phase 1 and Phase 2 |
| **Care Product** | Fin configuration (Procedures, routing, escalation logic); agent-facing tooling in Zendesk; compliance guardrails in Fin/agent stack |
| **Content team** | Customer-facing support articles, FAQs, and product explainers (Braavos scopes topics; Content writes and publishes to help centre) |
| **Operations Excellence** | Agent-facing SOPs and internal process guides |
| **Risk / Legal** | Compliance tooling for PSR reimbursement, MLRO/OFSI notifications, and FOS case management (dependencies — not owned by Care or Braavos) |

---

## Braavos — App features

Screens, flows, and self-serve functions Braavos must build in the app. Care defines requirements and accepts each feature before phase completion; Care has no build ownership here.

| Ref | Capability | What Braavos must deliver | JTBDs | Phase |
|---|---|---|---|---|
| A1 | In-app fraud reporting entry point | Entry point accessible from the transaction detail screen and from the help menu. Tapping opens the fraud report initiation flow and triggers Fin Procedure FP3 (scam intake). Displays submission confirmation with reference number. | 38, 39 | Phase 1 |
| A2 | In-app card management self-serve | Card management screen showing current card status (active, frozen, blocked, lost). Actions: freeze/unfreeze card, order replacement, view troubleshooting guide for declined transactions. Replacement order flow confirms delivery ETA in-app. | 18–23 | Phase 1 |
| A3 | Web rescue page | Static page accessible outside the app without login. Contains: emergency card freeze instructions, alternative contact channel links, account access recovery steps. Reachable via direct URL; linked from consumer comms and from app error states. | 7 | Phase 1 |
| A4 | In-app contextual help entry point | Help surface visible on every main screen, showing contextual content based on the consumer's current screen. Connects to searchable knowledge base. Opens Fin chat on escalation. Required before C9 and FP2–FP6 can be surfaced in-context. | 58, 59 | Phase 2 |
| A5 | Account closure flow | Self-serve closure initiation. Must display: 90-day cooling-off information, remaining balance, fund nomination form (consumer nominates account for return). Sends closure confirmation and fund transfer confirmation on completion. | 50–53 | Phase 2 |
| A6 | SAR / data request form | In-app form for Subject Access Request, data export, and deletion requests. On submission: logs request with timestamp, displays acknowledgement with 30-day statutory timeline, triggers Fin confirmation. Audit trail required for ICO. | 54 | Phase 2 |
| A7 | Gambling block toggle | Toggle in account settings to activate/deactivate gambling transaction block. Activation immediate and confirmed in-app. Must be accessible without friction — FCA FG21/1 requirement. | 72 | Phase 2 |
| A8 | In-app case / dispute tracker | Real-time status tracker for open disputes and cases visible in-app. Shows: status, last updated, expected resolution date. Pulls from Care case management via D5 data feed. Sends push notifications on status change. | 32 | External launch |

---

## Braavos — Data provision to Care

Braavos is the source of truth for all consumer data. The feeds below must be exposed to Care systems before the Fin Procedures and agent tooling in sections 6 and 7 can be built. Braavos and Data Engineering are jointly responsible for exposure; Care Product owns the consumption layer.

| Ref | Data | What Braavos must expose | Consumed by | Phase |
|---|---|---|---|---|
| D1a | Transaction data — in-app display | Transaction records with status, failure reason, processing ETA, and merchant details surfaced natively in the app transaction detail view. | Braavos app (A2, JTBDs 24–26) | Phase 1 |
| D4 | P1 volume alerting | Contact volume monitoring detecting abnormal inbound spikes; triggers P1 alert to Care Ops before queue is overwhelmed. Owned by Data Engineering; Ops team defines thresholds. | Ops (JTBD 96) | Phase 2 |
| D6 | GDPR request tracking | System for tracking SAR and data deletion requests against the 30-day statutory deadline — logs submission date, owner, completion status. Audit trail for ICO. Owned jointly by Care Product and Legal. | Care Product / Legal (JTBD 92) | Phase 2 |
| D1b | Transaction data — Fin and agent access | API or data feed providing transaction records (status, failure reason, ETA, amount, merchant, timestamps) queryable by Fin Procedure and surfaced in agent Customer 360 view. Prerequisite for FP2 and HT2. | FP2, HT2 (JTBDs 24–26, 28, 30) | External launch |
| D2 | Account state — agent-facing | Read access to: restriction type, active sessions, closure status, account action history. Required before HT1 (account actions) and HT2 (Customer 360) can be built. | HT1, HT2 (JTBDs 15, 47–49, 57) | External launch |
| D3 | Vulnerability flag — read/write | Read/write access to a vulnerability flag on the consumer profile record. Care writes on identification; Braavos reads to inform future interactions. Schema must be agreed between teams before External launch. | CG2, HT2 (JTBDs 67–73, 94) | External launch |
| D5 | Case status — real-time | Real-time case status feed (status, last updated, ETA) for the in-app case tracker (A8). Status source is Care's case management system; Braavos consumes and displays it. | A8 (JTBD 32) | External launch |

---

## Content team — Customer-facing articles

Braavos scopes the topics and prioritises by flow. The Content team writes, reviews, and publishes to the help centre. Articles are surfaced in Fin's knowledge base and in the in-app contextual help layer (A4, live Phase 2).

| Ref | Content area | What to write | JTBDs | Phase |
|---|---|---|---|---|
| C1 | Account access & recovery | Articles covering: locked account recovery scenarios (forgotten PIN, biometric failure, lost phone), self-serve recovery steps by scenario, web rescue page instructions, magic link / email portal walkthrough, alternative channel options when app is unavailable. | 5–8, 10 | Phase 1 |
| C2 | Card management | Articles covering: how to freeze and unfreeze a card, how to order a replacement, what to do with a declined transaction, how to read card status in-app, damaged card replacement process, delivery timelines. | 18–23 | Phase 1 |
| C3 | Payments — failure reasons, status copy, ETA messaging | Articles and in-app microcopy covering: why payments fail and what happens next, how to read transaction status, expected resolution timelines for common failure types. Includes plain-language definitions for all payment status states used in-app (written to meet FCA Consumer Duty consumer understanding requirement). | 24–26 | Phase 1 |
| C4 | Fraud and security reporting | Articles covering: how to report a suspected fraud or scam, what channels are available, what to do when an unauthorised transaction appears, what happens after a report is submitted, provisional credit process and timeline. | 38–43 | Phase 1 |
| C5 | Technical issue / known fix library | Actively maintained library of known app issues with: symptom description, self-fix steps, escalation path if self-fix fails. Updated with each app release and when new issues are identified. Ongoing across all phases — Content team maintains with input from Braavos engineering. | 74–82 | Phase 1 onwards |
| C6 | Transaction recovery — CPR, ATM, DD Guarantee | Articles covering: how to report money sent to the wrong account (CPR process and timeline), how to report an ATM that did not dispense cash, consumer rights under the Direct Debit Guarantee and how to claim. Customer-facing only — internal agent steps for CPR and ATM investigation are owned by Operations Excellence. | 27–31 | Phase 2 |
| C8 | Account management & data rights | Articles covering: how to close an account, cooling-off period and fund return process, how to submit a SAR or data deletion request, how to update marketing preferences, data rights under UK GDPR. Must meet FCA Consumer Duty fair value and transparency obligations. | 50–57 | Phase 2 |
| C9 | Product & feature KB — FSCS, fees, rewards | Articles covering: FSCS protection status and limits, full fee schedule in plain language, how cashback and rewards work (rates, conditions, eligibility). Required under FCA Consumer Duty fair value disclosure. | 58–66 | Phase 2 |
| C11 | Disputes and complaints — process and rights | Articles covering: how to raise a dispute, what evidence to provide and why, dispute types and timelines, how to track a dispute, what outcomes mean, how to escalate if dissatisfied, FOS referral rights and process, FCA DISP timelines (what to expect and when). Published in help centre; also surfaced by automated comms at key DISP milestones. | 33–37, 83–87 | External launch |

---

## Operations Excellence — Agent SOPs

Care Product defines requirements and regulatory constraints. Operations Excellence writes, owns, and maintains. These are internal documents — not published to the help centre.

Care agents are not live until External launch (H1 2027). Braavos handles all consumer support in Phase 1 and Phase 2. All SOPs must be complete and signed off before Care takes over at External launch.

Care human agents are not active in Phase 1 or Phase 2. All SOPs are required for External launch (H1 2027).

| Ref | SOP area | What to write | JTBDs | Phase |
|---|---|---|---|---|
| S1 | Account access & recovery — agent escalation | Agent process for when a consumer cannot complete self-serve account recovery. Covers: identity verification steps before restoring access, decision points for each locked-out scenario (forgotten PIN, biometric failure, lost phone), account restoration procedure, consumer communication at each step. | 5–8 | External launch |
| S2 | Card management — agent escalation | Agent process for card issues that cannot be resolved in-app. Covers: ordering a replacement on behalf of a consumer, handling a reported lost or stolen card, investigating a card that is declining incorrectly, confirming delivery status. | 18–23 | External launch |
| S3 | Payment issue handling | Agent process for payment queries escalated from Fin. Covers: how to look up transaction status and communicate failure reason in plain language, when and how to escalate internally, response process for payment delays and failed credits. | 24–26 | External launch |
| S4 | Fraud & security incident — agent handling | Agent process for fraud escalations received from Fin (FP3 output). Covers: how to review a submitted fraud report, provisional credit decision criteria and how to apply it, case logging and case ownership, consumer communication throughout investigation, closure and outcome steps. | 38–43 | External launch |
| S5 | Transaction recovery — CPR and ATM investigation | Agent process for transaction recovery cases. Covers: Credit Payment Recovery — how to initiate with the receiving bank, required information, timeline and consumer communication; ATM investigation — case logging steps, what information to record, escalation to scheme. Companion to customer-facing articles in C6. | 27–31 | External launch |
| C7 | Account restriction — holding response scripts | Scripted agent responses for contacts where an account action has been taken and specific reasons cannot be disclosed. Must comply with POCA s.333A tipping-off rules. Three scripts required: (1) initial holding response, (2) information request to consumer, (3) outcome notification within disclosure limits. Legal review required before activation. | 44–49 | External launch |
| S6 | Account management — verified account actions | Agent process for account management requests requiring identity verification. Covers: agent-assisted account closure (when self-serve not available), SAR and data deletion request handling, marketing preference updates requiring verification, complex profile changes. | 50–57 | External launch |
| S7 | Technical issue — engineering escalation | Agent process for technical issues that cannot be resolved in-app. Covers: how to review the Fin diagnostic payload (FP4 output), how to create an engineering ticket in Zendesk (HT6), consumer communication on escalation, how to notify the consumer when a fix is deployed. | 74–82 | External launch |
| C10 | Wellbeing — specialist support | SOPs for agents handling vulnerable consumers. Covers: how to identify vulnerability or distress, needs assessment process, active listening guidance, specialist routing decision points, external signposting list (Samaritans, StepChange, MIND), welfare check scheduling, emergency dispatch protocol for active self-harm risk. Must comply with FCA FG21/1. Specialist input required from welfare training provider before finalisation. | 67–73 | External launch |
| S8 | Dispute handling — agent process | Agent process for dispute escalations. Covers: reviewing submitted dispute evidence, case investigation steps, outcome decision process, how to communicate an upheld or rejected outcome clearly, how to handle a consumer who challenges a decision, internal escalation path for complex disputes. Companion to customer-facing articles in C11. | 33–37 | External launch |
| C12 | Account takeover (ATO) — specialist handling | Full specialist-grade SOPs for ATO cases: out-of-band identity verification steps (HT5), account lock and session termination procedure (HT1), credential reset with enhanced monitoring activation, consumer communication at each stage, evidence and case documentation requirements. Requires input from FinCrime and Security teams before finalisation. | 12–16 | External launch |
| S9 | Formal complaint handling — FCA DISP | T2/T3 agent process for formal complaint handling. Covers: how to assess whether a contact is a formal complaint or general feedback, complaint investigation steps, how to draft a Final Response Letter, FOS referral process and consumer rights communication, how to manage binding FOS decisions. Reviewed by Legal. Integrates with CG4 (DISP clock) and HT7 (T2/T3 routing). | 83–87, 97, 99 | External launch |

---

## Care Product — Fin Procedures

Configured by Care Product in Intercom. Each Procedure defines: the trigger (how Fin detects the contact type), any data calls to Braavos systems, resolution logic or routing action, and consumer-facing output. All Procedures target External launch — Braavos data APIs (D1b, D2) must be live first.

| Ref | Procedure | What Care configures in Fin | JTBDs | Phase |
|---|---|---|---|---|
| FP1 | ATO triage and route | Detects ATO signals (consumer reports unauthorised access or account compromise). Fin does not attempt resolution. Immediately routes to ATO specialist queue (HT3), passing conversation context and consumer ID. Fin does not ask diagnostic questions that could reveal to an attacker that an investigation is active. | 12 | External launch |
| FP2 | Transaction lookup | On contact about a payment issue, Fin calls Braavos transaction API (D1b) using consumer ID to retrieve status, failure reason, and expected resolution ETA. Surfaces result in plain language. If resolved: closes conversation. If unresolved or data unavailable: escalates to agent with transaction context pre-populated (via FP5). | 24–26 | External launch |
| FP3 | Scam intake — structured capture | Structured intake triggered from in-app fraud report (A1) or direct Fin contact. Captures: scam type, contact method used by fraudster, amount, timeline. Submits structured report to case management. Confirms receipt to consumer with reference number. Escalates immediately if consumer requests human contact. Outputs structured payload for PSR reimbursement assessment (D7). | 41 | External launch |
| FP4 | Technical diagnostic capture | On contact about an app or technical issue, Fin collects: device type, OS version, app version, issue description, screenshots. Checks known issue library (C5) for a matching fix. If match found: provides fix steps. If no match: packages diagnostics and escalates to agent for engineering ticket creation (HT6). | 78 | External launch |
| FP5 | Context handoff on escalation | On any Fin-to-agent escalation, generates a structured handoff summary: consumer ID, query topic, conversation summary, data retrieved, resolution steps attempted. Passed to agent on connection — consumer does not need to repeat their query. Required by all other Procedures that escalate. | 62 | External launch |
| FP6 | Wellbeing triage and route | Detects vulnerability or distress signals in conversation (explicit disclosure, language indicators). Fin does not attempt to resolve or assess the situation. Routes immediately to wellbeing specialist queue (HT3) with conversation context. Fin does not ask clinical or diagnostic questions. | 67 | External launch |

---

## Care Product — Agent Tooling

Built within Zendesk and integrated systems. Engineering resource required for all HT items. Braavos data provision (D1b, D2, D3) is a hard prerequisite for HT1 and HT2. All agent tooling targets External launch.

| Ref | Tool | What Care builds | Braavos data dependency | JTBDs | Phase |
|---|---|---|---|---|---|
| HT1 | Account actions — session termination, lock, credential reset | Agent-accessible actions in Zendesk: terminate all active sessions, lock consumer account, initiate credential reset, activate enhanced monitoring. Requires agent authentication before each action. Every action auto-logged to case history with timestamp and agent ID. | D2 (account state write access) | 15, 16 | External launch |
| HT2 | Customer 360 — unified consumer context view | Single agent-facing panel in Zendesk showing: account state (status, restrictions, active sessions), transaction history (recent 30 days), full interaction history across all channels, open cases, vulnerability flag status. Replaces manual multi-system lookups. | D1b (transactions), D2 (account state), D3 (vulnerability flag) | 13–16, 28, 30, 47–49, 57, 67–73 | External launch |
| HT3 | Specialist queue routing — ATO and wellbeing | Two specialist queues in Zendesk: ATO specialist queue (receives cases routed by FP1) and wellbeing specialist queue (receives cases routed by FP6). Routing logic ensures only agents with the relevant specialist training can receive these cases. Queue SLA tracking configured separately from standard queue. | None | 12–16, 67–73 | External launch |
| HT4 | Case management — CPR, ATM investigation, welfare check | Structured case workflows for: Credit Payment Recovery initiation with receiving bank, ATM investigation logging, welfare check scheduling with follow-on reminder. Each workflow captures required fields, assigns ownership, and triggers automated consumer notification on status update. | D1b (transaction details for CPR / ATM cases) | 28, 30, 73 | External launch |
| HT5 | Out-of-band identity verification | Mechanism for agents to confirm consumer identity through a channel not compromised in the incident (e.g. email magic link, document verification). Used for ATO cases and any complex account action requiring verified consent. Must meet AML/KYC standards. Reviewed by Legal and Security before activation. | None | 14, 81 | External launch |
| HT6 | Engineering escalation — ticket creation with diagnostics | One-action creation in Zendesk of an engineering ticket pre-populated with Fin's FP4 diagnostic payload: device, OS, app version, issue description, screenshots. Routes to Braavos engineering triage queue. Agent notified of ticket ID; consumer notified escalation is raised. | None | 79 | External launch |
| HT7 | T2/T3 complaint routing — DISP clock and FOS management | Complaint workflow in Zendesk: routes formal complaints to T2/T3 agents, starts DISP clock at intake (5-day acknowledgement, 8-week resolution), triggers automated acknowledgement to consumer, tracks FOS referral eligibility at 8 weeks, manages binding FOS decisions. Integrates with CG4. Configured with Legal. | None | 86, 97, 99 | External launch |

---

## Care Product — Compliance configuration

Guardrails, routing rules, and logging hooks configured by Care Product within Fin and Zendesk. Legal review required before CG1 and CG4 are activated.

| Ref | Capability | What Care configures | JTBDs | Phase |
|---|---|---|---|---|
| CG1 | AML tipping-off scripts | Constrains Fin and agent responses in account restriction contacts (Flow 8) to comply with POCA s.333A. Fin uses only Legal-reviewed holding response scripts (C7) and cannot deviate to explain the underlying action. Agents presented with compliant response options only — free-text restricted for disclosure-sensitive contacts. | 46, 89 | External launch |
| CG2 | Vulnerability flagging — profile write on identification | When an agent or Fin identifies a vulnerable consumer, a vulnerability flag is written to the consumer's profile via D3. Flag is visible in Customer 360 (HT2) on all future contacts. Activation criteria and flag categories defined per FCA FG21/1 — agreed with Legal before launch. | 94 | External launch |
| CG3 | Complaint root cause logging — Consumer Duty feedback loop | At complaint closure, agent is required to log a root cause category before the case can be closed. Aggregated root cause data surfaced to Care Product monthly. Required under Consumer Duty Outcome D (obligation to identify and act on recurring product and service issues). | 98 | External launch |
| CG4 | DISP clock management — 5-day acknowledgement, 8-week resolution | Automated deadline tracking in Zendesk (integrated with HT7): triggers automated acknowledgement at Day 1 if not already sent, alerts T2/T3 agent at Day 4 if acknowledgement outstanding, escalates to complaint lead at Week 7 if unresolved, generates FOS referral prompt at Day 56. Configuration reviewed by Legal. | 97 | External launch |

---

## Risk / Legal dependencies

Not owned by Care or Braavos. These capabilities must be delivered by Risk and Legal before External launch. Care Product is the internal customer for D7 and CG6; both Braavos and Care are stakeholders for CG5.

| Ref | Item | What Care / Braavos need from Risk / Legal | Required by |
|---|---|---|---|
| D7 | PSR eligibility data | A data service or decision model determining PSR APP fraud reimbursement eligibility and calculating the 50/50 liability split per PSR October 2024 rules. Required before CG6 and FP3 outputs can trigger reimbursement. | External launch |
| CG5 | MLRO / OFSI notification workflows | Automated workflows to: (1) notify the MLRO of SAR-eligible cases and obtain DAML consent where required per AML MLRs; (2) notify OFSI of asset freezes within SAMLA-required timeframes. Checkout's regulatory obligation — must be operational at External launch, not post-launch. | External launch |
| CG6 | PSR reimbursement tooling | End-to-end tooling to determine reimbursement eligibility, calculate the 50/50 liability split, and process reimbursement per PSR October 2024 rules. Dependent on D7. | External launch |

---

## Phase delivery summary

| Phase | Target | Braavos | Care Product | Content team | Ops Excellence | Risk / Legal (deps) |
|---|---|---|---|---|---|---|
| **Phase 1** | Jun '26 | A1, A2, A3, D1a | — | C1, C2, C3, C4, C5 (start) | — | — |
| **Phase 2** | Oct '26 | A4, A5, A6, A7, D4, D6 | — | C5 (ongoing), C6, C8, C9 | — | — |
| **External launch** | H1 '27 | A8, D1b, D2, D3, D5 | FP1–FP6, HT1–HT7, CG1–CG4 | C11 | S1–S9, C7, C10, C12 | D7, CG5, CG6 |
