**PRD: Consumer Care \- External Launch**

| Author | Averof Stylianidis |
| :---- | :---- |
| **Date** | April 2026 |
| **Approvers** | Charlie Wildish, Oliver Westlake-Simm, Nick Grafton-Green |
| **Status** | Draft |

# **1.0 Executive Summary**

The External Launch PRD defines the full care capability required to serve external consumers when Braavos opens to the public in H1 2027\. Phase 1 (50 employees, June 2026\) validated the self-serve model. Phase 2 (1,000 employees, October 2026\) introduces Fin AI and Zendesk. External Launch completes the care stack: full Fin Procedures for automated case handling, the complete agent tooling suite (Customer 360, specialist queues, case management), FCA DISP-compliant complaint handling, PSR APP fraud reimbursement tooling, and all operational SOPs.

This is the largest and most compliance-critical phase. It delivers 40+ capabilities across seven categories: three app features, five content packages, six data dependencies, six Fin Procedures, seven agent tooling modules, nine SOPs, and six compliance configurations. Every capability in this PRD is either a regulatory obligation or a prerequisite for safe, scalable consumer care at public launch volumes.

# **2.0 Problem Space**

**Problem statement:** Braavos is targeting 300K-500K external consumers in Year 1\. At this scale, care operations require: automated case handling (Fin Procedures) for fraud, ATO, and technical issues; a unified agent workspace (Customer 360\) for complex escalations; specialist routing for ATO and vulnerability cases; FCA-compliant complaint handling with DISP clock management; PSR APP fraud reimbursement processing; and formal SOPs for every care flow. None of these exist today. Without them, Braavos cannot launch to external consumers without creating regulatory risk, consumer harm, and operational failure.

**Who is affected:** External consumers \- UK retail customers using Braavos accounts for everyday transactions, card payments, and financial services. Unlike the internal cohorts in Phase 1 and Phase 2, these consumers have no compensating channels (no Slack, no in-person access to Checkout.com staff). The care experience IS the safety net.

**Why now:** External launch is targeted for H1 2027\. FCA notification requires demonstration of care readiness as part of the regulatory approval process. Complaint handling must comply with FCA DISP from day one. PSR APP fraud reimbursement obligations apply from the first consumer transaction. There is no grace period \- these capabilities must be live at launch, not retrofitted.

# **3.0 Goals and Success Metrics**

## **3.1 Goals**

* Deliver the complete care stack required for FCA notification and external consumer launch.

* Enable Fin AI to handle the full breadth of care flows through six dedicated Fin Procedures (ATO triage, transaction lookup, scam intake, diagnostic capture, context handoff, wellbeing triage).

* Equip agents with a unified workspace (Customer 360\) and specialist routing for ATO and vulnerability cases.

* Implement FCA DISP-compliant complaint handling with automated clock management and FOS referral.

* Deliver PSR APP fraud reimbursement eligibility assessment and 50/50 liability split tooling.

* Publish all operational SOPs and train Care team to full operational readiness.

**Non-goals:**

* Omnichannel care (social media, community) \- focus is in-app and phone/email for launch.

## **3.2 North Star Metric**

**Consumer resolution satisfaction (CSAT)**: the percentage of consumers rating their care experience positively after issue resolution.

At External Launch, the metric shifts from internal operational efficiency (Fin resolution rate) to external consumer outcome quality. CSAT measures whether the complete care stack \- Fin AI, agent tooling, SOPs, compliance controls \- actually delivers good outcomes for real consumers. This aligns directly with FCA Consumer Duty Outcome D (consumer support).

## **3.3 Success Metrics**

| Metric | Why it matters | Baseline | Target | Source |
| :---- | :---- | :---- | :---- | :---- |
| Consumer resolution CSAT (NSM) | Direct measure of consumer outcome quality per Consumer Duty Outcome D | Phase 2 CSAT | \>80% positive | Post-resolution survey |
| Fin AI resolution rate | Continuity from Phase 2 \- must sustain at higher volume | Phase 2 actual | \>50% of contacts resolved without human | Fin analytics |
| FCA DISP SLA compliance | Regulatory obligation: 5-day acknowledgement, 8-week resolution | N/A (new) | 100% compliance | DISP clock tracking (CG4) |
| Complaint-to-FOS escalation rate | Lower \= better complaint resolution; high rate signals systemic issues | N/A (new) | \<5% of formal complaints escalated to FOS | Complaint tracking |
| Mean time to resolve fraud case | Consumer experience of fraud response speed | N/A (new) | \<5 business days | Case management (HT4) |
| PSR reimbursement processing time | Regulatory: reimbursement within 5 business days of decision | N/A (new) | 100% within 5 business days | PSR tooling (CG6) |

## **3.4 Counter Metrics**

| Metric | What it guards against | Threshold |
| :---- | :---- | :---- |
| Complaint volume per 1,000 consumers | High complaint rate signals systemic product or care issues | Track from launch \- investigate if \>5 per 1,000 in any month |
| FOS upheld rate | FOS decisions upheld against Checkout.com indicate poor complaint handling quality | \<30% of FOS decisions upheld |
| Specialist queue wait time |  ATO and vulnerability cases waiting too long for specialist response | \<15 minutes average for ATO queue; \<10 minutes for wellbeing queue |
| Agent error rate on compliance-sensitive contacts | AML tipping-off, PSR reimbursement, or DISP process errors | Zero tolerance \- every instance investigated |

# **4.0 Customer Segments & Opportunity Space**

External Launch serves UK retail consumers: individuals using Braavos accounts. Year 1 target is 300K-500K users. This is the first time Checkout.com has a direct consumer relationship at scale. The care experience must meet FCA Consumer Duty standards from day one \- there is no beta buffer.

## **4.1 Methodology**

To derive the JTBD for this project, we first identified a high level list of taxonomy categories for Care Issues, alongside their sub-issues (e.g., Account creation & Verification, Product information, etc.). We then mapped a relevant, holistic [user journey](https://www.figma.com/board/DFRv2J31Rj6WgVzqson0sG/Braavos-%E2%80%94-Consumer-Care-User-Journey-Flows?node-id=48-16222&t=W0d72sWZCBvbUGXX-4) to represent each of the [12 Taxonomy](https://docs.google.com/spreadsheets/d/1Hpll3V9FvhxYYlIarE3M32zdJjekqjon/edit?gid=980169016#gid=980169016) Categories we have, and then mapped out from the various user journeys step-by-step which needs/desires/pain points make up the [total opportunity space](https://docs.google.com/spreadsheets/d/1_BZ8Kd4O9wCd8iBj_3KztRk2WJbtarWu/edit?gid=2120581180#gid=2120581180) for Consumer Care. These were translated into JTBD, that were then categorised in different "Capabilities" (given the broad nature of the types of x-functional features that comprise a Care flow). These are:

* Braavos app features

* Content

* Data

* Fin procedures

* Agent tooling

* Compliance

For each phase of the project, some (if not all) categories represent items we need to deliver in order to have fully functional Care flows that adhere to our regulatory requirements and level of Customer Experience we wish to offer.

**The JTBD addressed by External Launch capabilities complete the full care opportunity space. New categories introduced at External Launch:**

* Formal complaints ([Flow 13](https://www.figma.com/board/DFRv2J31Rj6WgVzqson0sG/Braavos-%E2%80%94-Consumer-Care-User-Journey-Flows?node-id=39-13069&t=W0d72sWZCBvbUGXX-4)): FCA DISP-compliant complaint initiation, investigation, resolution, and FOS referral

* Dispute management ([Flow 6](https://www.figma.com/board/DFRv2J31Rj6WgVzqson0sG/Braavos-%E2%80%94-Consumer-Care-User-Journey-Flows?node-id=39-12603&t=W0d72sWZCBvbUGXX-4)): guided evidence capture, reference tracking, outcome communication, and escalation

* Full ATO specialist handling ([Flow 3](https://www.figma.com/board/DFRv2J31Rj6WgVzqson0sG/Braavos-%E2%80%94-Consumer-Care-User-Journey-Flows?node-id=39-12390&t=W0d72sWZCBvbUGXX-4)): out-of-band verification, session termination, credential reset, enhanced monitoring

* Full agent tooling: Customer 360, specialist queues, case management, engineering escalation, complaint routing

* Full Fin Procedures: automated handling for ATO, transactions, scams, diagnostics, wellbeing, and context handoff

# **5.0 Proposed Scope**

**Solution overview:** External Launch delivers the complete care stack. It adds the in-app case tracker, full Fin Procedure set, complete agent tooling suite, all SOPs, and all remaining compliance controls. Combined with Phase 1 and Phase 2 capabilities, this constitutes the full care product for external consumers.

## **5.1 In scope**

**App features:**

* A6 \- SAR/data request form (moved from Phase 2 \- employees leaving lose app access)

* A7 \- Gambling block toggle (moved from Phase 2 \- vulnerability/wellbeing tooling is a regulatory requirement for external consumers)

* A8 \- In-app case/dispute tracker (real-time status, push notifications on status change)

**Content:**

* C11 \- Disputes and complaints: process, evidence requirements, FOS rights, DISP timelines

* C12 \- ATO agent SOPs: full specialist handling procedures

* C7 \- Account restriction holding response scripts (moved from Phase 2 \- no AML screening on employee accounts)

* C8 \- Account management and data rights: closure, SAR, GDPR, preferences (moved from Phase 2\)

* C10 \- Wellbeing SOPs: vulnerability identification, specialist support, signposting (moved from Phase 2\)

**Data:**

* D1b \- Transaction data: Fin and agent access (API for Fin Procedures and Customer 360\)

* D2 \- Account state: agent-facing (restrictions, sessions, closure status)

* D3 \- Vulnerability flag: read/write on consumer profile

* D5 \- Case status: real-time feed for in-app tracker (A8)

* D6 \- GDPR request tracking: SAR and deletion deadline management (moved from Phase 2 \- employees leaving lose app access)

* D7 \- PSR eligibility data: APP fraud reimbursement and 50/50 liability split

**Fin Procedures:**

* FP1 \- ATO triage and route

* FP2 \- Transaction lookup

* FP3 \- Scam intake: structured capture

* FP4 \- Technical diagnostic capture

* FP5 \- Context handoff on escalation

* FP6 \- Wellbeing triage and route

**Agent tooling:**

* HT1 \- Account actions: session termination, lock, credential reset

* HT2 \- Customer 360: unified consumer context view

* HT3 \- Specialist queue routing: ATO and wellbeing

* HT4 \- Case management: CPR, ATM investigation, welfare check

* HT5 \- Out-of-band identity verification

* HT6 \- Engineering escalation: ticket creation with diagnostics

* HT7 \- T2/T3 complaint routing: DISP clock and FOS management

**SOPs:**

* S1-S9 \- Full operational SOPs for all care flows (see section 7.6)

**Compliance:**

* CG2 \- Vulnerability flagging tooling

* CG3 \- Complaint root cause logging (Consumer Duty feedback loop)

* CG4 \- DISP clock management: 5-day acknowledgement, 8-week resolution

* CG5 \- MLRO/OFSI notification workflows

* CG6 \- PSR reimbursement tooling

## **5.2 Out of scope**

* Omnichannel care (social media, community) \- post-launch

# **6.0 Key Assumptions and Validation**

**1\. Assumption:** Phase 2 Fin AI and Zendesk are stable and performant before External Launch scope is built on top of them.

**Validation:** Phase 2 must run for at least 6 weeks with stable metrics before External Launch features are deployed to production.

**2\. Assumption:** FCA notification will be submitted and accepted before external consumer onboarding begins.

**Validation:** Legal to confirm notification timeline. If notification is delayed, external launch date moves \- Care readiness cannot be the bottleneck.

**3\. Assumption:** Care operations headcount is sufficient for external launch volumes (300K-500K consumers Year 1).

**Validation:** Staffing model based on Phase 2 escalation rate \+ Fin deflection \+ external volume projection. Model must be validated and hiring approved by Q4 2026\.

# **7.0 Requirements**

## **7.1 App Feature Requirements**

### **7.1.1 A6 \- SAR/data request form**

**Owner: Braavos app team**

**US-A6.1**  As a consumer, I want to request my personal data or deletion easily, so that I can exercise my data rights without calling anyone.

**Acceptance criteria:**

* Given a consumer navigates to account settings or Help & Support, then a 'Data rights' option is visible.

* Given a consumer opens the data rights form, then they can select: Subject Access Request, Data Export, or Data Deletion.

* Given a consumer submits a request, then the app confirms receipt and displays the 30-day statutory timeline.

* Given a request is submitted, then it is logged with timestamp, request type, and consumer ID for ICO audit trail.

### **7.1.2 A7 \- Gambling block toggle**

**Owner: Braavos app team**

**US-A7.1**  As a consumer, I want to block gambling transactions immediately to protect myself, so that I can take control of my spending without delay.

**Acceptance criteria:**

* Given a consumer navigates to account controls, then a 'Block gambling transactions' toggle is visible.

* Given a consumer activates the gambling block, then it takes effect immediately and a confirmation is displayed.

* Given the gambling block is active, then all transactions with gambling MCCs are declined.

* Given the toggle is accessible, then it does not require contacting an agent or completing additional verification steps per FCA FG21/1.

### **7.1.3 A8 \- In-app case/dispute tracker \[stretch goal \- could be realigned to reduce effort if necessary\]**

**Owner: Braavos app team**

**US-A8.1**  As a consumer, I want to track the progress of my case or dispute in-app without contacting support again, so that I stay informed without effort.

**Acceptance criteria:**

* Given a consumer has an open case or dispute, when they open the case tracker, then the current status, last update date, and expected resolution date are displayed.

* Given a case status changes, then the consumer receives a push notification with the updated status.

* Given the tracker is open, then all open and recently closed cases are visible in a single list view.

**US-A8.2**  As a consumer, I want to be guided step-by-step to describe what happened and know exactly what evidence to provide, so that my dispute is handled efficiently.

**Acceptance criteria:**

* Given a consumer initiates a dispute, then a guided flow collects the incident description, dispute type, and required evidence based on the dispute category.

* Given evidence is required, then the flow clearly states what documents or information are needed and allows file upload.

* Given the dispute is submitted, then a reference number is issued and the expected timeline is communicated.

## **7.2 Content Requirements**

### **7.2.1 C11 \- Disputes and complaints: process and rights**

**Owner: Technical Writing and Content teams/Legal**

**Topics to cover:**

* How to raise a dispute (step-by-step)

* Evidence requirements by dispute type

* Dispute types and expected timelines

* How to track dispute progress in-app (A8)

* Understanding outcomes: upheld, rejected, partial

* How to escalate or challenge a decision

* FOS referral rights: when, how, and what to expect

* FCA DISP timelines: 5-day acknowledgement, 8-week resolution

### **7.2.2 C12 \- ATO agent SOPs: specialist handling**

**Owner: Technical Writing and Content teams/Specialist**

**Topics to cover:**

* Out-of-band identity verification process (integrates with HT5)

* Account lock and session termination procedure (integrates with HT1)

* Credential reset with enhanced monitoring

* Consumer communication at each stage

* Evidence and documentation requirements

* Handoff from Fin ATO triage (FP1) to specialist agent

### **7.2.3 C7 \- Account restriction holding response scripts**

**Owner: Technical Writing and Content teams/Legal**

**Three Legal-reviewed scripts for contacts where account action has been taken and reasons cannot be disclosed:**

* Script 1: Initial holding response (acknowledges restriction, does not disclose reason)

* Script 2: Information request (requests updated KYC/AML information from consumer)

* Script 3: Outcome notification (communicates outcome within POCA s.333A disclosure limits)

All scripts must be approved by Legal before integration into Fin or agent workflows. Scripts must comply with POCA s.333A \- no disclosure of AML investigation existence. Deferred from Phase 2 as no ongoing AML screening is run on employee accounts.

### **7.2.4 C8 \- Account management and data rights**

**Owner: Technical Writing and Content teams**

**Topics to cover:**

* How to close an account (process, 90-day cooling-off, fund return)

* SAR and data deletion requests (rights, process, 30-day timeline)

* Marketing preferences (how to manage)

* UK GDPR data rights in plain language

Deferred from Phase 2\. At Phase 2, closure is explained inline in the A5 flow. Full content including SAR/GDPR articles published at External Launch alongside A6 and D6.

## **7.3 Data Requirements**

| Ref | Capability | Description | Owner |
| :---- | :---- | :---- | :---- |
| D1b | Transaction data: Fin and agent access | API providing transaction records (status, failure reason, ETA, amount, merchant, timestamps) queryable by Fin Procedures (FP2) and surfaced in Customer 360 (HT2). Prerequisite for FP2 and HT2. | Braavos/Data Engineering |
| D2 | Account state: agent-facing | Read access to restriction type, active sessions, closure status, account action history. Required before HT1 and HT2 can be built. | Braavos/Data Engineering |
| D3 | Vulnerability flag: read/write | Read/write access to a vulnerability flag on the consumer profile. Care writes on identification (CG2); Braavos reads to inform future interactions. Schema to be agreed before launch. | Braavos/Data Engineering |
| D5 | Case status: real-time | Real-time case status feed (status, last updated, ETA) for the in-app case tracker (A8). Status source is Care case management (HT4); Braavos consumes and displays. | Braavos/Data Engineering |
| D6 | GDPR request tracking | System tracking SAR and data deletion requests against the 30-day statutory deadline. Logs submission date, request type, assigned owner, and completion status. Must provide an auditable trail for ICO. Integrates with SAR/data request form (A6). Deferred from Phase 2 as employees leaving lose app access. | Consumer team/Legal |
| D7 | PSR eligibility data | Data service determining PSR APP fraud reimbursement eligibility and 50/50 liability split per PSR October 2024 rules. Required before CG6 can process reimbursements. | Risk |

## **7.4 Fin Procedure Requirements**

All Fin Procedures are owned by the Care Product team (Charlie Wildish). Each procedure operates within Fin AI and handles a specific care scenario with structured inputs, logic, and outputs.

| Ref | Procedure | Behaviour | Escalation |
| :---- | :---- | :---- | :---- |
| FP1 | ATO triage and route | Detects ATO signals in conversation. Routes immediately to ATO specialist queue (HT3) with context. No resolution attempt. Does not ask questions that could alert an attacker. | Immediate to HT3 ATO queue |
| FP2 | Transaction lookup | Calls Braavos transaction API (D1b) on payment contact. Retrieves status, failure reason, ETA. Surfaces in plain language. Escalates with context (FP5) if unresolved. | Via FP5 to agent |
| FP3 | Scam intake: structured capture | Structured intake from in-app fraud report (A1) or direct contact. Captures scam type, contact method, amount, timeline. Submits to case management with reference number. Outputs payload for PSR assessment (D7). | To agent with structured payload |
| FP4 | Technical diagnostic capture | Collects device, OS, app version, issue description, screenshots. Checks known fix library (C5). Provides fix if match found; packages diagnostics and escalates to agent (HT6) if no match. | Via HT6 to engineering |
| FP5 | Context handoff on escalation | On any Fin-to-agent escalation, generates structured summary: consumer ID, query, conversation summary, data retrieved, steps attempted. Passed to agent so consumer does not repeat their query. | N/A (handoff mechanism) |
| FP6 | Wellbeing triage and route | Detects vulnerability or distress signals. Routes immediately to wellbeing specialist queue (HT3) with context. No resolution attempt. No clinical or diagnostic questions. | Immediate to HT3 wellbeing queue |

## **7.5 Agent Tooling Requirements**

All agent tooling is built in Zendesk and owned by the Care Product team. Each module serves a specific operational function in the agent workflow.

| Ref | Module | Capabilities | Dependencies |
| :---- | :---- | :---- | :---- |
| HT1 | Account actions | Agent-accessible actions: terminate sessions, lock account, initiate credential reset, activate enhanced monitoring. Requires agent authentication. All actions logged with timestamp and agent ID. | D2 (account state) |
| HT2 | Customer 360 | Single Zendesk panel showing: account state, transaction history (30 days), full interaction history, open cases, vulnerability flag. The unified context view for every agent interaction. | D1b, D2, D3 |
| HT3 | Specialist queue routing | Two specialist queues: ATO (fed by FP1) and wellbeing (fed by FP6). Routing restricted to trained specialists only. Separate SLA tracking from standard queue. | FP1, FP6 |
| HT4 | Case management | Structured case workflows for CPR initiation, ATM investigation logging, and welfare check scheduling. Captures required fields, assigns ownership, triggers consumer status notifications via D5. | D5 (case status feed) |
| HT5 | Out-of-band identity verification | Mechanism for agents to verify consumer identity via uncompromised channel (e.g. email magic link, document verification). Used for ATO and verified account actions. Meets AML/KYC standards. | IDV team (Antoine Keriven) |
| HT6 | Engineering escalation | One-action Zendesk ticket creation pre-populated with FP4 diagnostic payload. Routes to Braavos engineering triage. Agent and consumer both notified of ticket creation. | FP4 (diagnostic payload) |
| HT7 | T2/T3 complaint routing | Routes complaints to T2/T3 agents. Starts DISP clock (CG4). Triggers automated 5-day acknowledgement. Tracks 8-week deadline. Manages FOS referral eligibility and binding decisions. | CG4 (DISP clock) |

## **7.6 SOP Requirements**

All SOPs are owned by Operations Excellence and must be reviewed by Legal where compliance-sensitive. SOPs must be published and agents trained before External Launch.

| Ref | SOP | Scope |
| :---- | :---- | :---- |
| S1 | Account access and recovery: agent escalation | Agent process when consumer cannot complete self-serve recovery. Covers: identity verification, decision points by locked-out scenario, account restoration, consumer communication at each step. |
| S2 | Card management: agent escalation | Agent process for card issues beyond self-serve. Covers: ordering replacement on behalf of consumer, lost/stolen card handling, investigating incorrect declines, confirming delivery status. |
| S3 | Payment issue handling | Agent process for payment queries escalated from Fin. Covers: transaction status lookup, communicating failure reason in plain language, internal escalation decision points, response for delays and failed credits. |
| S4 | Fraud and security incident: agent handling | Agent process for fraud escalations from Fin (FP3 output). Covers: reviewing submitted fraud report, provisional credit decision criteria and application, case logging, consumer communication, closure and outcome. |
| S5 | Transaction recovery: CPR and ATM investigation | Agent process for CPR (initiation with receiving bank, required info, timeline, consumer comms) and ATM investigation (case logging, information to record, scheme escalation). |
| S6 | Account management: verified account actions | Agent process for requests requiring identity verification. Covers: agent-assisted account closure, SAR and data deletion handling, preference updates requiring verification, complex profile changes. |
| S7 | Technical issue: engineering escalation | Agent process for technical issues not resolved in-app. Covers: reviewing Fin diagnostic payload (FP4), creating engineering ticket (HT6), consumer communication on escalation, notifying consumer when fix is deployed. |
| S8 | Dispute handling: agent process | Agent process for dispute escalations. Covers: evidence review, case investigation, outcome decisions, communicating upheld/rejected outcomes, handling challenges, internal escalation for complex disputes. |
| S9 | Formal complaint handling: FCA DISP | T2/T3 process: assessing formal vs informal complaints, investigation steps, drafting Final Response Letter, FOS referral process, managing binding FOS decisions. Reviewed by Legal. Integrates with CG4 and HT7. |

Additionally, C7 (account restriction holding response scripts), C8 (account management and data rights), and C10 (wellbeing SOPs) are External Launch content items. C12 (ATO specialist handling) is an External Launch content item (see 7.2.2).

## **7.7 Compliance Requirements**

| Ref | Capability | Requirement | Owner |
| :---- | :---- | :---- | :---- |
| CG2 | Vulnerability flagging tooling | Writes vulnerability flag to consumer profile (D3) when identified. Visible in Customer 360 (HT2) on future contacts. Flag categories defined per FCA FG21/1. Agreed with Legal before launch. | Consumer team/Risk |
| CG3 | Complaint root cause logging | Agent required to log root cause category at complaint closure. Aggregated data surfaced to Consumer team monthly. Required under Consumer Duty Outcome D. | Consumer team |
| CG4 | DISP clock management | Automated DISP deadline tracking in Zendesk (integrated with HT7): Day 1 acknowledgement trigger, Day 4 alert if outstanding, Week 7 escalation, Day 56 FOS referral prompt. | Care Product team/Care Ops |
| CG5 | MLRO/OFSI notification workflows | Automated workflows to notify MLRO of SAR-eligible cases and obtain DAML consent; notify OFSI of asset freezes within SAMLA timeframes. Regulatory obligation. | Care Product/Care Ops/Compliance 1st line |
| CG6 | PSR reimbursement tooling | End-to-end tooling for reimbursement eligibility, 50/50 split calculation, and processing per PSR October 2024\. 5-day contribution deadline for receiving PSP. Dependent on D7. | RiskOps/Open Banking product team |

# **8.0 Design and User Experience**

## **8.1 Key UX principles**

* Consumer Duty by design: every consumer-facing surface must meet FCA Consumer Duty standards for clarity, fairness, and accessibility.

* Case transparency: the in-app tracker (A8) must give consumers full visibility into their case status without needing to contact support.

* No dead ends: every Fin AI flow must have a clear path to a human agent. Specialist cases (ATO, wellbeing) must route immediately without intermediate steps.

* Context preservation: FP5 ensures consumers never repeat their issue when escalated from Fin to an agent.

* Complaint accessibility: per FCA DISP, the complaint option must be prominent and easy to find \- not buried in settings.

* Gambling block must be immediate: per FCA FG21/1, the toggle must be accessible without friction, delay, or agent contact.

* Frictionless exit: dispute outcomes, complaint decisions, and FOS referral rights must be communicated proactively and clearly.

# **9.0 Instrumentation and Monitoring**

## **9.1 Key events to instrument**

| Event | Description | Properties |
| :---- | :---- | :---- |
| care.dispute.initiated | Tracks dispute flow starts | dispute\_type, transaction\_ref, consumer\_id |
| care.dispute.evidence\_submitted | Tracks evidence uploads in dispute flow | dispute\_ref, evidence\_type, file\_count |
| care.dispute.outcome\_communicated | Tracks outcome delivery to consumer | dispute\_ref, outcome (upheld/rejected/partial), amount |
| care.complaint.formal\_filed | Tracks formal complaint submissions | complaint\_ref, consumer\_id, category |
| care.complaint.disp\_clock\_started | Tracks DISP clock initiation | complaint\_ref, start\_date, 8\_week\_deadline |
| care.complaint.fos\_referral | Tracks FOS referral communications | complaint\_ref, referral\_date |
| care.fin.procedure.executed | Tracks Fin Procedure executions | procedure\_id (FP1-FP6), outcome, duration\_seconds |
| care.specialist.queue.assigned | Tracks specialist queue assignments | queue\_type (ATO/wellbeing), wait\_time\_seconds, agent\_id |
| care.psr.reimbursement.processed | Tracks PSR reimbursement decisions | case\_ref, eligibility, amount, split\_ratio |
| care.vulnerability.flag.written | Tracks vulnerability flag writes | consumer\_id, flag\_category, identified\_by |
| care.gambling\_block.toggled | Tracks gambling block activations/deactivations | action (activate/deactivate), consumer\_id |

## **9.2 Monitoring Dashboards**

* Consumer Care Command Centre \- real-time: all queues, SLA status, specialist queue wait times, P1 alerts, DISP clock status across all open complaints.

* Complaint and Dispute Dashboard \- weekly: formal complaint volume, resolution rate, FOS referral rate, root cause distribution, DISP compliance rate.

* Fin Procedure Performance \- daily: execution count by procedure, resolution rate, escalation rate, average duration.

* Regulatory Compliance Dashboard \- weekly: PSR reimbursement processing time, GDPR request SLA, DISP SLA, AML script compliance audit results.

# **10.0 Risks and Open Questions**

## **10.1 Risks**

| Risk | Likelihood | Impact | Mitigation |
| :---- | :---- | :---- | :---- |
| Data API delivery (D1b, D2, D3, D5) delayed, blocking Customer 360 and Fin Procedures | Medium | High | Engineering scoping by Q3 2026\. If APIs are at risk, define minimum viable data access for HT2 and FP2 as a fallback. |
| FCA notification delayed, pushing external launch date | Low | High | Legal to own notification timeline. Care readiness must not be the bottleneck \- deliver all capabilities to schedule regardless. |
| Agent staffing insufficient for external launch volumes | Medium | High | Staffing model validated by Q3 2026\. BPO contract decision for supplementary capacity must be made by Q1 2027\. |
| PSR reimbursement tooling not ready at launch, creating regulatory exposure | Low | High | Risk team owns D7 and CG6 delivery. If tooling is delayed, manual reimbursement process with Legal oversight as interim. |
| Specialist agent training (ATO, wellbeing, DISP) insufficient for live consumer cases | Medium | Medium | Training programme starts Q4 2026\. Include scenario-based exercises with escalation. Named senior contact for first 4 weeks of live operation. |

## **10.2 Open Questions**

| Question | Proposal | Owner |
| :---- | :---- | :---- |
| What is the BPO strategy for external launch agent capacity? | Decision required by Q1 2027\. Proposal: hybrid model with in-house specialists (ATO, wellbeing, DISP) and BPO for T1 volume. | Oliver Westlake-Simm |
| Who owns PSR reimbursement processing operationally? | Risk team for eligibility assessment; Care Ops for consumer communication and fund disbursement. Needs RACI. | RiskOps/Open Banking |
| What is the phone channel strategy for external consumers? | In-app and email at launch. Phone for specialist flows (ATO, wellbeing) only. Full phone channel is post-launch. | Charlie Wildish/Oliver Westlake-Simm |
| How are FOS binding decisions operationally managed? | S9 SOP must include FOS decision processing. Legal must review all FOS binding decisions before execution. Process to be agreed with Legal by Q1 2027\. | RiskOps |
| What is the vulnerability flag schema? | Schema must be agreed between Care, Risk, and Legal per FCA FG21/1. Propose: four vulnerability drivers (health, life events, resilience, capability) with free-text note field. | Consumer team/Risk Product/Care Product |
| How is the gambling block technically implemented at the MCC level? | Issuing team to confirm MCC-based blocking capability. If not available, interim solution via manual transaction monitoring. | Issuing team (Joe Foulds) |
| Are there more MCCs that may need to be blocked/blockable by the user? | Clarification needed at policy level for Consumer duty by Legal | Nick Grafton-Green/Kristina Lajara |

# **11.0 Rollout Plan**

External Launch delivery is phased to ensure platform dependencies (data APIs) are in place before agent tooling and Fin Procedures are built on top of them.

## **11.1 Delivery sequence**

| When | What | Owner | Dependency |
| :---- | :---- | :---- | :---- |
| Q3 2026 | Engineering scoping for D1b, D2, D3, D5 data APIs | Braavos engineering | None |
| Q4 2026 | C7, C8, C10, C11, C12 content drafted | Technical Writing and Content teams |  |
| Q4 2026 | S1-S9 SOPs drafted by Operations Excellence | Operations Excellence | Consumer Duty/Vulnerability policies ready |
| Q4 2026-Q1 2027 | D1b, D2, D3, D5, D6, D7 data APIs and tracking systems built and tested | Braavos/Data Engineering/Risk/Consumer team | Eng. scoping complete |
| Q1 2027 | FP1-FP6 Fin Procedures built and tested | Care Product team | D1b (for FP2), C5 (for FP4) |
| Q1 2027 | HT1-HT7 agent tooling built in Zendesk | Care Product team | D1b, D2, D3 (for HT2), D5 (for HT4) |
| Q1 2027 | CG2-CG6 compliance configs built and tested | Consumer team/Risk/Legal | D3 (for CG2), D7 (for CG6), HT7 (for CG4) |
| Q1 2027 | A6 (SAR/data request form), A7 (gambling block), and A8 (in-app case tracker) built | Braavos app team | D5 (for A8), D6 (for A6), Issuing team MCC confirmation (for A7) |
| Q1 2027 | Legal review of C7, C8, C10, C11, C12, S9, and all compliance configs | Nick Grafton-Green | Content and SOPs drafted |
| Q1 2027 | Agent training programme: all SOPs, specialist flows, compliance | Consumer team/Oliver Westlake-Simm | SOPs approved, tooling configured |
| Q1 2027 | UAT: full care stack end-to-end testing | Consumer team | All above complete |
| Q2 2027 | External Launch go-live | Consumer team | FCA notification accepted, all above complete |

## **11.2 Success criteria for External Launch readiness**

* All Fin Procedures (FP1-FP6) tested against scenario bank with \>95% correct routing and resolution.

* All agent tooling modules (HT1-HT7) operational in Zendesk with UAT sign-off.

* All SOPs (S1-S9, C10, C12) published, Legal/Risk/Compliance policy owners approved where required, and agents trained.

* DISP clock management (CG4) tested with simulated complaints through full 8-week cycle.

* PSR reimbursement tooling (CG6) tested with simulated cases through full eligibility and processing flow.

* FCA notification accepted and closed.

## **11.3 Definition of Done**

* **Technical:** All data APIs (D1b, D2, D3, D5, D6, D7) live. A6, A7, and A8 delivered. All Fin Procedures and agent tooling operational.

* **Content:** C7, C8, C10, C11, C12 published and Legal-approved. All SOPs published.

* **Compliance:** CG2-CG6 all operational and tested. DISP clock management and PSR reimbursement processing validated.

* **Operational:** Agents trained on all SOPs and specialist flows. Staffing model confirmed. BPO contract in place if required.

* **Regulatory:** FCA notification accepted and closed. All Consumer Duty evidence documented per compliance questionnaire.

* **Instrumentation:** All events instrumented. Command Centre, Complaint Dashboard, Fin Performance, and Regulatory Compliance dashboards live.

# **12.0 Dependencies**

| Dependency | Owner | Required by |
| :---- | :---- | :---- |
| Braavos engineering to deliver D1b, D2, D3, D5 data APIs | Joe Foulds | Q1 2027 |
| Care/Legal to deliver D6 GDPR request tracking system | Consumer team/Legal | Q1 2027 |
| Risk team to deliver D7 PSR eligibility data service | Risk | Q1 2027 |
| Care Product team to build FP1-FP6 and HT1-HT7 | Charlie Wildish | Q1 2027 |
| Technical Writing and Content teams to draft C7, C8, C10, C11, C12, and support SOP drafting | Technical Writing and Content teams | Q4 2026 |
| Operations Excellence to draft S1-S9 SOPs | Operations Excellence | Q4 2026 |
| Legal review of C7, C8, C10, C11, C12, S9, CG2-CG6 | Nick Grafton-Green | Q1 2027 |
| IDV/Consumer Product team to support out-of-band verification mechanism (HT5) | Antoine Keriven/Umang Sota | Q4 2026 |
| Issuing team to confirm MCC-based gambling block capability (A7) | Issuing team (Joe Foulds) | Q4 2026 |
| FCA notification accepted | Legal | Before external go-live |

# **13.0 Go-to-Market**

External Launch is the first consumer-facing release. Go-to-market covers operational readiness, consumer communications, and regulatory compliance.

| Activity | Type | Owner | Timeline |
| :---- | :---- | :---- | :---- |
| Agent training programme: all SOPs, specialist flows, Zendesk tooling, compliance procedures | Operational enablement | Consumer team/Oliver Westlake-Simm | Q1 2027 |
| Consumer-facing help centre: all content (C1-C12) published and accessible | Consumer experience | Technical Writing and Content teams | Before go-live |
| Consumer onboarding comms: 'How to get help' integrated into Braavos onboarding journey | Consumer comms | Consumer team/Technical writing & Content team | Before go-live |
| FCA Consumer Duty compliance questionnaire signed off | Compliance | Legal/Compliance | Before go-live |
| Hypercare period: first 4 weeks post-launch with named senior escalation contacts | Operational enablement | Consumer team/Oliver Westlake-Simm | First 4 weeks post-launch |

