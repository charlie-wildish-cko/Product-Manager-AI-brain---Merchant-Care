# Braavos Consumer Care — Care Scoping Document

**Author:** Charlie Wildish
**Date:** May 2026
**Status:** Draft

This document sets out Care's scope, build responsibilities, dependencies, risks, and assumptions across all three Braavos launch phases. It maps to the 2026 deliverable **Consumer Support — Braavos App (Q4)** and the pre-conditions required for External Launch (H1 2027).

---

## Phase 1 — Internal Beta (June 2026, 50 employees)

**Launch scope**
50 internal Checkout.com employees use Braavos accounts with real funds. No AI agent and no Zendesk — care is self-serve first (in-app features + FAQ content) with Jira as the escalation path. The primary goal is to validate the self-serve model and collect issue categorisation data to calibrate Phase 2.

**Question:** what level of support is Care providing in Phase 1?

**Needed for support launch**
- Four in-app features delivered by Consumer team: fraud reporting entry point (tap to report from transaction detail or Help & Support), card management self-serve (freeze/unfreeze, replacement, troubleshooting), web rescue page (accessible without app login for locked-out users), and transaction data display (status, failure reason, settlement ETA)
- Jira project (e.g. BCARE) configured with escalation workflow — delivered by Consumer team
- 4 FAQ content packages authored, Legal-reviewed, and published before launch: account access and recovery, card management, payments (failure reasons, status, timelines), fraud and security reporting
- Care instrumentation: FAQ view tracking, escalation form submission tracking, card freeze lifecycle events
- Emergency out-of-band security protocol documented

**What Care must build**
Assume none in this phase — insufficient time for tech and agent readiness.

**Interim support flow**
- Jira project for support issues, picked up by Consumer product team
- Triage SOP for Jira tickets (categories, response targets, routing, emergency protocol)
- Care team briefing pack (FAQ reference, triage process, emergency contact protocol)
- FAQ content (account access, card management, payments, fraud and security) — authored by Content/Technical Writing, Legal sign-off required

**Dependencies**

| Dependency | Owner | Required by |
|---|---|---|
| In-app fraud reporting, card management self-serve, web rescue page, transaction data display | Consumer team | June 2026 |
| Jira project setup (BCARE) | Consumer team | May 2026 |
| FAQ content drafting (account access, card management, payments, fraud and security) | Technical Writing / Content | May 2026 |
| Legal review of FAQ content (4 packages) | Nick Grafton-Green | Before June go-live |
| Consumer Duty applicability to internal accounts | Nick Grafton-Green | Before June go-live |

**Risks**

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| In-app features (fraud reporting, card management, web rescue page, transaction data display) not ready by June | Medium | High | Confirm sprint allocation by mid-May; descope web rescue page first if needed |
| Employees bypass in-app care via Slack or in person | High | Medium | Internal comms at launch; monitor Slack mentions as counter-signal |
| FAQ content not Legal-reviewed before go-live | Medium | Medium | Begin drafting May; prioritise account access and fraud/security content |
| Security incident with no fast resolution path | Low | High | Card freeze is self-serve (not dependent on Jira); document out-of-band protocol |

**Assumptions**
- Consumer Duty applies to internal employee accounts (Legal to confirm)
- 50 employees will use in-app channels, not ad hoc Slack/in-person routes
- Jira is a sufficient escalation mechanism at 50-user scale

---

## Phase 2 — Internal Scale (October 2026, 1,000 employees)

**Launch scope**
1,000 internal employees at approximately 20x Phase 1 volume. Zendesk replaces Jira as the care operations platform. Expanded self-serve: in-app contextual help entry point, account closure flow, and three new content packages (known fix library, transaction recovery, product and feature KB). Fin AI is not confirmed for Phase 2 — it is a Q4 deliverable for pre-External Launch preparation.

**Needed for support launch**
- An entry point to create tickets into Zendesk — simple form input or email proxy? (TBC)
- Consumer CRM integration for user data — needed for launch? (TBC)
- Zendesk routing configured for Braavos contacts (workflows, SLA tracking, issue categorisation aligned to care taxonomy)
- Three new content packages authored and Legal-reviewed: known fix library (ongoing maintenance of app issues with symptom, self-fix steps, escalation path), transaction recovery (CPR wrong-recipient payments, ATM non-dispense, Direct Debit Guarantee claims), and product and feature KB (FSCS protection, fee schedule, cashback/rewards)
- P1 volume alerting (contact spike detection integrated with incident management tooling)
- Two new in-app features delivered by Braavos app team: contextual help entry point (searchable KB) and account closure flow (self-serve, 90-day cooling-off, fund nomination)
- Agent staffing model confirmed for 1,000 employees

**What Care must build**
- Zendesk routing configuration: Braavos queue, issue categories, SLA rules (2–3 weeks lead time)
- Agent training on Zendesk workflows
- P1 volume alert thresholds (based on Phase 1 baseline)
- Fin AI knowledge base built from all Phase 1 and Phase 2 content — only if Fin is confirmed in scope

**Dependencies**

| Dependency | Owner | Required by |
|---|---|---|
| Transaction recovery and product/feature KB content drafting | Technical Writing / Content | August 2026 |
| Legal review of transaction recovery and product/feature KB content | Nick Grafton-Green | Before October go-live |
| In-app contextual help entry point and account closure flow | Braavos app team | September 2026 |

**Risks**

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Agent staffing model not confirmed before scale-up | Low | Medium | Volume at 1,000 employees remains low; risk manageable without model, but confirm before go-live |
| Transaction recovery and product KB content not Legal-reviewed before October | Medium | Medium | Begin drafting August; identify Legal lead by end of Q2 |

**Assumptions**
- Staffing model accounts for no-AI scenario (all escalations handled by agents)

---

## Phase 3 — External Launch (H1 2027, consumer-facing)

**Launch scope**
Full public consumer launch. Target 300K–500K users in Year 1. Care moves from internal operations to a regulated consumer support function. Consumer Duty Outcomes A–D, PSRs (APP fraud reimbursement), FCA DISP (formal complaints), and AML MLRs apply from day one. This phase requires the largest Care build: 6 Fin Procedures, Consumer CRM data integration, specialist queues, full SOP library, and 6 compliance configurations.

**Needed for support launch**
- Fin AI Procedures (6): ATO triage, transaction lookup, scam intake, diagnostic capture, context handoff, wellbeing triage — all require data connectors to Braavos APIs
- Consumer data from Consumer CRM surfaced in Zendesk (account history, interaction history, vulnerability flags)
- Specialist queues in Zendesk: fraud, wellbeing/vulnerability, formal complaints, AML-restricted accounts
- FCA DISP complaint handling process (intake, 8-week clock, FOS referral)
- PSR APP fraud reimbursement tooling and processing workflow (100% within 5 business days)
- SAR and GDPR deletion request handling (Subject Access Requests + right-to-erasure)
- Gambling block functionality and blockable MCC list agreed
- Full SOP library (9 SOPs: ATO, scam intake, dispute, complaint, account restriction, wellbeing, verification, DD Guarantee, ATM non-dispense)
- 6 compliance configurations: Consumer Duty, AML tipping-off restrictions (account restriction holding messaging; no-disclosure scripts where POCA applies), PSR reimbursement, FCA DISP, GDPR, vulnerability flagging
- BPO strategy confirmed (in-house vs outsourced agents)
- Phone channel decision confirmed (FCA accessibility requirements)

**What Care must build**
- Install Fin into app — TBC whether mobile engineering support is required
- All 6 Fin Procedures with data connectors (dependent on Braavos APIs)
- Consumer CRM data integration into Zendesk agent workspace
- Escalation and routing rules in Fin and Zendesk (fraud queue, wellbeing queue, complaints queue, AML queue)
- Full SOP library (9 SOPs)
- Compliance configurations: AML hold messaging, PSR reimbursement workflow, FCA DISP intake and clock management, GDPR SAR tracking, vulnerability flag schema
- Content packages: AML account restriction holding messaging and POCA tipping-off restriction scripts, dispute communications, and supporting content for each Fin Procedure
- Out-of-band verification protocol for high-risk agent actions (refunds, reversals)

**Dependencies**

| Dependency | Owner | Required by |
|---|---|---|
| Braavos data APIs for Fin Procedures (critical path) | Braavos Engineering | Q3 2026 for scoping; Q4 for build |
| BPO strategy decision | Oliver Westlake-Simm | Q3 2026 (onboarding lead time) |
| Phone channel decision | Charlie Wildish / Oliver | Q3 2026 |
| PSR reimbursement ownership (Finance vs Care vs Fraud) | TBD | Q3 2026 |
| Vulnerability flag process | Legal + Ops Excellence | Q3 2026 |
| Legal/Compliance sign-off on AML, PSR, FCA DISP configs | Nick Grafton-Green | Before go-live |
| Gambling block implementation (MCC list) | Braavos Engineering | Q4 2026 |

**Risks**

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Braavos data API delays block all Fin Procedures | Medium | High | Identify API requirements and owners by Q3 2026; escalate if not scoped by then |
| BPO / staffing model undefined at launch | Medium | High | Decision required Q3 2026; if BPO route, 3–4 month onboarding lead time |
| PSR reimbursement ownership unresolved | Medium | High | Force decision Q3 2026; PSR 5-day SLA applies from first external account |
| Specialist capability not ready (fraud, wellbeing) | Medium | High | Define training requirements Q3 2026; vulnerability/wellbeing requires specialist-level handling from day one |
| FCA DISP process not ready at launch | Low | High | Complaint handling is a legal obligation, not a stretch goal; must be live before first external account |

**Assumptions**
- Consumer Duty, PSRs, FCA DISP, and AML MLRs all apply from the first external account opened
- Complaint handling and vulnerable customer identification are live at launch
- External Launch date is H1 2027 (specific month TBC)
- BPO decision is made by Q3 2026 to allow adequate onboarding and training time
- Fin Procedures require working Braavos data APIs — Care cannot build Procedures without them

---

## Open Decisions

| Decision | Owner | Required by |
|---|---|---|
| Does Consumer Duty apply to internal Phase 1/2 accounts? | Nick Grafton-Green | May 2026 |
| BPO vs in-house agent model for External Launch? | Oliver Westlake-Simm | Q3 2026 |
| Phone channel for External Launch? | Charlie Wildish / Oliver | Q3 2026 |
| PSR reimbursement ownership? | To be agreed | Q3 2026 |

---

## Complaints Handling

Formal FCA DISP complaints handling is out of scope for Phase 1 and Phase 2 — internal employees are not eligible complainants under DISP. It is a hard requirement for External Launch, where Consumer Duty, DISP, PSRs, and AML MLRs apply from the first account opened. The build is larger than a single workflow: it spans automated SLA clocks, root-cause taxonomy, vulnerability data reporting, QA sampling, regulatory exports, and systemic issue detection.

### Phase 2 — Foundations (October 2026)

Phase 2 must lay the groundwork so that External Launch data is clean and the Zendesk configuration does not need to be rebuilt.

**Zendesk configuration**
- Complaint identification flag: any expression of dissatisfaction must be loggable as a complaint regardless of channel or wording — the field must exist in Zendesk before External Launch, and agents must be trained to use it
- Vulnerability indicator fields added to Zendesk ticket schema — easier to build into initial config than retrofit; needed for External Launch reporting from day one
- FCA root-cause taxonomy codes mapped to Zendesk ticket categorisation — the updated taxonomy takes effect January 2027; Phase 2 data must be coded consistently so Phase 3 reporting starts clean
- Complaint outcome field on ticket — possible additional field (TBC)

Zendesk is the complaints case management system for External Launch. The complaints-specific configuration (mandatory field sets, SLA clocks, QA workflows, FCA export) must be explicitly scoped as part of the Phase 2 Zendesk build — not assumed to be covered by standard routing config.

### External Launch — Full Build (H1 2027)

**Case management**
- Unique complaint reference number generated automatically at logging
- Mandatory fields on every case: customer ID, contact details, communication preference, vulnerability flags (4 FCA data points), date/channel/colleague, root-cause category (FCA taxonomy), FOS scope indicator, redress claimed
- Case allocation and routing by complexity and case value
- Independent reallocation workflow for internal review (different handler, different team from original investigator)
- Systemic issue trigger: automated alert when 5 or more complaints share the same root cause within a 30-day window, routed to Complaints Manager

**SLA automation**
- Acknowledgement workflow: triggered by close of next business day after receipt
- Summary Resolution Communication at day 3 if resolved
- Holding response automation: day 4 if unresolved, then every 10 business days
- Final Response Letter 8-week clock with escalation alerts
- Separate 15-business-day clock for payment services complaints (PSRs/EMRs 2011), extendable to 35

**Vulnerability data (mandatory from January 2027)**
- Four FCA-mandated fields: complaints opened by vulnerable consumers; complaints closed by vulnerable consumers; complaints opened relating to a failure to consider vulnerability; complaints closed relating to a failure to consider vulnerability
- Vulnerability flags must travel with the case through every workflow stage
- Schema must distinguish vulnerable consumer from vulnerable complainant (e.g. next of kin, PoA)
- Same flag definitions used for operational case handling and FCA reporting — no divergent schemas

**Regulatory reporting**
- Consolidated complaints return: six-monthly FCA export, first period January–June 2027
- FCA taxonomy codes on every case (taxonomy updated December 2026)
- Consumer Duty board report data feed (annual)
- Website publication trigger if 500 or more complaints in a six-month reporting period

**QA sampling**
- 10% of closed complaints independently quality-assured
- 100% QA on cases involving a vulnerable customer
- 100% QA on cases with redress above £500
- Monthly calibration against published FOS decisions

**Channel intake**
- In-app chat as primary channel — Fin AI must identify and route complaints, not attempt to resolve them as standard queries
- UK freephone number with Relay UK and BSL video interpretation (if phone channel confirmed)
- Dedicated complaints email address
- Third-party authority handling in Zendesk (CMC, solicitor, Power of Attorney) — requires a verification workflow

**Investigation tooling**
- Full account history, transaction history, and prior contact records accessible within the Zendesk agent workspace (covered by Consumer CRM integration, but must explicitly include complaint investigation use cases)
- Chat transcript linkage from Fin AI escalations to the complaint case record
- Call recording access from within the case (if phone channel confirmed)
