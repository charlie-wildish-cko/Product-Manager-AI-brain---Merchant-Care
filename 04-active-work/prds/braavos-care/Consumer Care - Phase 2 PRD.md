**PRD: Consumer Care \- Phase 2**

| Author | Averof Stylianidis |
| :---- | :---- |
| **Date** | April 2026 |
| **Approvers** | Charlie Wildish, Oliver Westlake-Simm, Nick Grafton-Green |
| **Status** | Draft |

# **1.0 Executive Summary**

Phase 2 of Braavos Consumer Care scales the care capability from 50 internal employees to 1,000 Checkout.com employees, targeted for October 2026\. Phase 1 validated the self-serve-first model using FAQs, in-app features, and Jira-based escalation. Phase 2 introduces two foundational platform capabilities \- Fin AI agent and Zendesk CRM \- alongside new app features and expanded content covering product information and transaction recovery.

This PRD defines the capabilities required for Phase 2: two new app features, three content packages, one data dependency, and the introduction of Fin AI and Zendesk as the care platform stack. Phase 1 capabilities remain operational and are built upon, not replaced.

# **2.0 Problem Space**

**Problem statement:** Phase 1 validated that a self-serve care layer can resolve the most common employee issues. However, Phase 1 operates on a Jira-based escalation mechanism with no AI agent, no CRM, and no structured care operations. At 1,000 employees, this model breaks: Jira does not scale as a care platform, agents have no unified consumer context, and new care domains (account management, product information, transaction recovery) require content and tooling that does not exist today.

**Who is affected:** 1,000 internal Checkout.com employees using Braavos accounts with real funds. This population generates approximately 20x the care volume of Phase 1\. Additionally, the Phase 2 cohort is the final validation before external consumers \- any capability gaps discovered here must be resolved before the external launch in H1 2027\.

**Why now:** Phase 2 launches in October 2026\. Without Fin AI and Zendesk, the care team cannot handle 20x volume without linear headcount growth. Without expanded content covering new care domains, employees encountering account closure, payment recovery, or product questions will have no self-serve path. These are operational prerequisites for scale.

# **3.0 Goals and Success Metrics**

## **3.1 Goals**

* Scale care operations to support 1,000 employees without linear headcount growth by deploying Fin AI as the first-line resolution channel.

* Establish Zendesk as the care CRM, replacing Jira-based escalation with structured agent workflows, SLA tracking, and consumer interaction history.

* Expand self-serve coverage to include account closure and product information.

* Expand content to cover transaction recovery and product/feature information.

* Generate the operational data and platform foundations required for External Launch.

**Non-goals:**

* AML tipping-off scripts (CG1) and account restriction holding response scripts (C7) \- deferred to External Launch as no ongoing AML screening will be run on employee accounts.

* GDPR request tracking system (D6) \- deferred to External Launch as employees leaving the business lose app access, making formal deadline tracking unnecessary at this scale.

* Full Fin Procedure set (ATO triage, scam intake, transaction lookup, diagnostic capture, context handoff, wellbeing triage) \- External Launch.

* Full agent tooling stack (Customer 360, specialist queues, case management, out-of-band verification) \- External Launch.

* FCA DISP formal complaint handling process \- External Launch.

* In-app case/dispute tracker \- External Launch.

* PSR APP fraud reimbursement tooling \- External Launch.

## **3.2 North Star Metric**

**Fin AI resolution rate**: the percentage of consumer care contacts resolved by Fin AI without human agent involvement.

This measures the effectiveness of the AI-first care model. Higher means Fin is resolving issues independently, reducing agent load and enabling scale. We selected this metric because it is the primary validation of the Phase 2 investment thesis: that Fin AI can absorb the majority of volume growth without proportional agent headcount increase.

## **3.3 Success Metrics**

| Metric | Why it matters | Baseline | Target | Source |
| :---- | :---- | :---- | :---- | :---- |
| Fin AI resolution rate (NSM) | Primary signal of AI care effectiveness \- each unresolved contact is a Fin capability gap | N/A (new) | \>40% of contacts resolved without human | Fin analytics/Zendesk |
| Escalation rate per active user | Continuity from Phase 1 \- measures self-serve failure rate at 20x scale | Phase 1 actual | \<0.3 tickets per user per month | Zendesk ticket count/active users |
| Median time to first response (agent) | Measures human responsiveness now via Zendesk | Phase 1 Jira baseline | \<2 hours (working hours) | Zendesk SLA tracking |
| CSAT on Fin interactions | Measures quality of AI-resolved contacts | N/A (new) | \>75% positive | Fin post-interaction survey |

## **3.4 Counter Metrics**

| Metric | What it guards against | Threshold |
| :---- | :---- | :---- |
| Fin false resolution rate | Fin marks a contact as resolved but the consumer re-contacts within 24 hours for the same issue | \<10% of Fin-resolved contacts result in re-contact |
| Agent handle time increase | Fin escalating only the hardest cases could artificially inflate agent AHT | Monitor trend \- investigate if AHT increases \>25% vs Phase 1 |

# **4.0 Customer Segments & Opportunity Space**

Phase 2 serves 1,000 internal Checkout.com employees using Braavos accounts with real funds. This population is 20x Phase 1 scale and represents the final internal validation before external consumers. The JTBD addressed by Phase 2 capabilities are documented in the JTBD Register and cover new territory beyond Phase 1: account management (closure), product information (FSCS, fees, rewards), and transaction recovery (CPR, ATM, DD Guarantee).

## **4.1 Methodology**

To derive the JTBD for this project, we first identified a high level list of taxonomy categories for Care Issues, alongside their sub-issues (e.g., Account creation & Verification, Product information, etc.). We then mapped a relevant, holistic [user journey](https://www.figma.com/board/DFRv2J31Rj6WgVzqson0sG/Braavos-%E2%80%94-Consumer-Care-User-Journey-Flows?node-id=48-16222&t=W0d72sWZCBvbUGXX-4) to represent each of the [12 Taxonomy](https://docs.google.com/spreadsheets/d/1Hpll3V9FvhxYYlIarE3M32zdJjekqjon/edit?gid=980169016#gid=980169016) Categories we have, and then mapped out from the various user journeys step-by-step which needs/desires/pain points make up the [total opportunity space](https://docs.google.com/spreadsheets/d/1_BZ8Kd4O9wCd8iBj_3KztRk2WJbtarWu/edit?gid=2120581180#gid=2120581180) for Consumer Care. These were translated into JTBD, that were then categorised in different "Capabilities" (given the broad nature of the types of x-functional features that comprise a Care flow). These are:

* Braavos app features

* Content

* Data

* Fin procedures

* Agent tooling

* Compliance

For each phase of the project, some (if not all) categories represent items we need to deliver in order to have fully functional Care flows that adhere to our regulatory requirements and level of Customer Experience we wish to offer.

# **5.0 Proposed Scope**

**Solution overview:** Phase 2 introduces the full care platform (Fin AI \+ Zendesk), two new self-serve app features, three content packages covering new care domains, and one data capability. All Phase 1 capabilities remain operational. The Jira escalation mechanism is replaced by Zendesk with structured agent workflows.

## **5.1 In scope**

**App features:**

* A4 \- In-app contextual help entry point (connects to Fin AI and searchable KB)

* A5 \- Account closure flow (self-serve, 90-day cooling-off, fund nomination)

**Content:**

* C5 \- Technical issue/known fix library (ongoing maintenance from Phase 1\)

* C6 \- Transaction recovery: CPR, ATM, DD Guarantee

* C9 \- Product and feature KB: FSCS, fees, rewards

**Data:**

* D4 \- P1 volume alerting (contact spike detection)

**Platform:**

* Fin AI agent \- first-line AI resolution for care contacts

* Zendesk CRM \- replaces Jira as the care operations platform

# **6.0 Key Assumptions and Validation**

**1\. Assumption:** Fin AI can resolve \>40% of care contacts without human intervention at 1,000-employee scale.

**Validation:** Monitor Fin resolution rate weekly from launch. If below 25% after 4 weeks, review Fin knowledge base coverage and escalation thresholds before External Launch.

**2\. Assumption:** Zendesk can be configured and operational by October 2026 (shared or dedicated instance decision pending).

**Validation:** Zendesk instance decision must be made by June 2026\. Configuration and testing require minimum 8 weeks. If decision is delayed past June, October launch is at risk.

**3\. Assumption:** Phase 1 learnings (ticket categorisation data, FAQ coverage gaps, escalation patterns) are sufficient to calibrate Fin AI knowledge base.

**Validation:** Review Phase 1 data quality by end of August. If category-level patterns are insufficient, supplement with synthetic training data from known care scenarios.

# **7.0 Requirements**

## **7.1 App Feature Requirements**

### **7.1.1 A4 \- In-app contextual help entry point**

**Owner: Braavos app team**

**US-A4.1**  As a consumer, I want to find answers and access help contextually without leaving the app, so that I can resolve my issue in the moment.

**Acceptance criteria:**

* Given a consumer is on any main screen, when they tap the help icon, then a Help & Support surface opens showing content relevant to the current screen context.

* Given the help surface is open, then the consumer can search the knowledge base using free-text search.

* Given the help surface is open, then a 'Chat with us' option opens a Fin AI conversation.

**US-A4.2**  As a consumer, I want to search for answers using my own words, so that I do not have to navigate a category tree to find what I need.

**Acceptance criteria:**

* Given a consumer enters a search query, then results are ranked by relevance and displayed within 2 seconds.

* Given search results are displayed, then each result shows a title, a preview snippet, and a link to the full article.

### **7.1.2 A5 \- Account closure flow**

**Owner: Braavos app team**

**US-A5.1**  As a consumer, I want to close my account without friction when I choose to leave, so that the process is straightforward and does not feel like a retention trap.

**Acceptance criteria:**

* Given a consumer navigates to account settings, then an 'Close account' option is visible without requiring contact with an agent.

* Given a consumer initiates closure, then the app displays the 90-day cooling-off period, the current account balance, and any pending transactions.

**US-A5.2**  As a consumer, I want to choose where my remaining money goes, so that I am confident my funds will be returned.

**Acceptance criteria:**

* Given a consumer proceeds with closure, then they are prompted to nominate a bank account for the fund return.

* Given closure is confirmed, then the consumer receives a confirmation screen and an email with the closure timeline, nominated account, and expected fund transfer date.

## **7.2 Content Requirements**

All content must meet the quality standards established in Phase 1: plain English per FCA Consumer Duty Outcome C, Legal review before publication, and a clear call-to-action at the end of each article.

### **7.2.1 C5 \- Technical issue/known fix library (ongoing)**

**Owner: Technical Writing and Content teams**

Maintained library of known app issues with symptom, self-fix steps, and escalation path. Updated each app release and when new issues are identified. Carried forward from Phase 1\. Fin AI must be trained on this content.

### **7.2.2 C6 \- Transaction recovery: CPR, ATM, DD Guarantee**

**Owner: Technical Writing and Content teams**

**Topics to cover:**

* How to report money sent to the wrong account (Credit Payment Recovery process and timeline)

* How to report an ATM non-dispense incident

* Consumer rights under the Direct Debit Guarantee and how to claim

* Expected timelines for each recovery type

### **7.2.3 C9 \- Product and feature KB: FSCS, fees, rewards**

**Owner: Technical Writing and Content teams**

**Topics to cover:**

* FSCS protection status and limits (required under FCA disclosure requirements)

* Full fee schedule in plain language (required under FCA Consumer Duty fair value)

* Cashback rates, conditions, and eligibility (required under FCA Consumer Duty)

* Product features and how to use them

## **7.3 Data Requirements**

### **7.3.1 D4 \- P1 volume alerting**

**Owner: Data Engineering/Ops**

Contact volume monitoring detecting abnormal inbound spikes. Triggers P1 alert to Care Ops before the queue is overwhelmed. Ops team defines alert thresholds based on Phase 1 baseline data. Must integrate with existing incident management tooling.

## **7.4 Platform Requirements**

### **7.4.1 Fin AI agent**

**Owner: Care Product team (Charlie Wildish)**

First-line AI resolution channel for consumer care contacts. Fin must be trained on all Phase 1 and Phase 2 content (C1-C6, C9). At Phase 2, Fin operates in a basic capacity: knowledge base retrieval, FAQ answers, and routing to human agents when confidence is low. Full Fin Procedures (FP1-FP6) are External Launch items.

**Phase 2 Fin capabilities:**

* Answer consumer queries from the knowledge base (C1-C6, C9)

* Route contacts to Zendesk agent queue when unable to resolve

* Capture consumer satisfaction after interaction

* Log interaction data for Phase 2 analytics and External Launch calibration

### **7.4.2 Zendesk CRM**

**Owner: Care Product team (Charlie Wildish)**

Replaces the Phase 1 Jira escalation mechanism. Zendesk becomes the single care operations platform for agent workflows, SLA tracking, ticket management, and reporting. Instance decision (shared vs dedicated) is pending.

**Phase 2 Zendesk requirements:**

* Ticket creation from Fin escalation with conversation context

* Issue categorisation aligned with the care taxonomy

* SLA tracking with configurable response and resolution targets

* Reporting dashboard: volume by category, SLA compliance, agent performance

* Integration with Fin for escalation routing

# **8.0 Design and User Experience**

## **8.1 Key UX principles**

* Continuity from Phase 1: Help & Support entry point remains visible on every main screen. Phase 2 adds the contextual help surface (A4) as the primary entry to Fin AI.

* AI-first, not AI-only: Fin is the first contact, but the path to a human must be visible and accessible at all times. No dead-end AI loops.

* Account closure must be frictionless: FCA Consumer Duty requires that exit journeys are free from unreasonable barriers. The closure flow (A5) must not use design complexity as a retention tool.

* Plain language throughout \- consistent with Phase 1 standards.

# **9.0 Instrumentation and Monitoring**

## **9.1 Key events to instrument**

| Event | Description | Properties |
| :---- | :---- | :---- |
| care.fin.conversation.started | Tracks Fin AI conversation initiation | source\_screen, consumer\_id, entry\_type (search/chat/contextual) |
| care.fin.conversation.resolved | Tracks Fin-resolved contacts (no human escalation) | resolution\_type, topic, duration\_seconds |
| care.fin.escalation.triggered | Tracks Fin-to-agent escalation | escalation\_reason, topic, conversation\_summary\_length |
| care.zendesk.ticket.created | Tracks Zendesk ticket creation | source (fin\_escalation/direct), category, priority |
| care.account\_closure.initiated | Tracks account closure flow starts | consumer\_id, balance\_at\_initiation |
| care.account\_closure.completed | Tracks completed closures | consumer\_id, days\_to\_completion, fund\_return\_method |
| care.p1\_alert.triggered | Tracks P1 volume alerts | threshold\_breached, contact\_volume, alert\_time |

## **9.2 Monitoring Dashboards**

* Care Phase 2 Overview \- weekly: Fin resolution rate, Fin CSAT, escalation volume by category, agent SLA compliance.

* Fin Performance Dashboard \- daily: resolution rate by topic, false resolution rate, escalation reasons, conversation duration.

* Zendesk Operations Dashboard \- daily: open tickets by category, SLA compliance, agent workload distribution.

# **10.0 Risks and Open Questions**

## **10.1 Risks**

| Risk | Likelihood | Impact | Mitigation |
| :---- | :---- | :---- | :---- |
| Zendesk instance decision delayed past June 2026, compressing configuration timeline | Medium | High | Escalate decision to Consumer Pillar Lead by end of May. If undecided by June, proceed with dedicated instance as default. |
| Fin AI resolution rate below target (\<40%), creating unexpected agent load | Medium | Medium | Weekly Fin performance review. If below 25% after 4 weeks, prioritise knowledge base gap analysis and retraining. Accept higher agent load for Phase 2 if needed. |
| Phase 1 data insufficient to calibrate Fin AI knowledge base | Medium | Medium | Supplement with synthetic training data from known care scenarios. Use Phase 1 FAQ view data and ticket categorisation as primary inputs. |

## **10.2 Open Questions**

| Question | Proposal | Owner |
| :---- | :---- | :---- |
| Shared or dedicated Zendesk instance? | Dedicated instance preferred for consumer care data separation and compliance. Decision required by June 2026\. | Charlie Wildish |
| Who is the named Fin AI owner responsible for knowledge base accuracy and ongoing tuning? | Care Product team should own Fin configuration. Propose a named owner by May 2026\. | Charlie Wildish |
| What is the agent staffing model for 1,000 employees? | Model based on Phase 1 escalation rate \+ Fin deflection target. Consumer team to produce staffing model by July. | Oliver Westlake-Simm |

# **11.0 Rollout Plan**

Phase 2 delivery is sequenced to ensure platform foundations (Fin AI, Zendesk) are in place before new consumer-facing features go live.

## **11.1 Delivery sequence**

| When | What | Owner | Dependency |
| :---- | :---- | :---- | :---- |
| June 2026 | Zendesk instance decision finalised | Charlie Wildish | None |
| June-Aug 2026 | Zendesk configured: workflows, categories, SLA rules, Fin integration | Care Product team | Instance decision |
| June-Aug 2026 | Fin AI knowledge base built from Phase 1 data \+ C1-C6, C9 content | Care Product team | Phase 1 data, content drafts |
| July-Aug 2026 | C6, C9 content drafted | Technical Writing and Content teams | None |
| Aug 2026 | Legal review of C6, C9 content | Nick Grafton-Green | Content drafts complete |
| Aug-Sep 2026 | A4, A5 built and tested | Braavos app team | Sprint allocation confirmed |
| Aug-Sep 2026 | D4 (P1 alerting) built | Data Engineering | Requirements finalised |
| Sep 2026 | Fin AI and Zendesk UAT | Care Product team | All above complete |
| Oct 2026 | Agent training: Zendesk workflows | Consumer team/Oliver Westlake-Simm | Zendesk configured |
| Oct 2026 | Phase 2 go-live | Consumer team | All above complete |

## **11.2 Success criteria to proceed to External Launch**

* Fin AI resolution rate tracked for at least 6 weeks with consistent measurement.

* Zendesk operational for at least 6 weeks with SLA tracking active.

* Issue categorisation data from Zendesk sufficient to scope External Launch agent tooling requirements.

## **11.3 Definition of Done**

* **Technical:** All Phase 2 app features (A4, A5) delivered and tested. D4 operational. Fin AI and Zendesk live.

* **Content:** All content packages (C5, C6, C9) published, Legal-approved, and loaded into Fin AI knowledge base.

* **Operational:** Agents trained on Zendesk. P1 alerting thresholds configured.

* **Instrumentation:** All Phase 2 events instrumented. Fin Performance Dashboard and Zendesk Operations Dashboard live.

# **12.0 Dependencies**

| Dependency | Owner | Required by |
| :---- | :---- | :---- |
| Technical Writing and Content teams to draft C6, C9 content | Technical Writing and Content teams | August 2026 |
| Legal review of all consumer-facing content | Nick Grafton-Green | Before Phase 2 go-live (October 2026\) |
| Care Product team to configure Fin AI and Zendesk | Charlie Wildish | September 2026 |
| Zendesk instance decision | Charlie Wildish | June 2026 |

# **13.0 Go-to-Market**

Phase 2 is an internal launch to 1,000 employees. Go-to-market is internal enablement at larger scale.

| Activity | Type | Owner | Timeline |
| :---- | :---- | :---- | :---- |
| Agent training: Zendesk workflows, Fin escalation handling | Operational enablement | Consumer team/Oliver Westlake-Simm | October 2026 |
| Employee onboarding comms: updated 'How to get help' guide for Phase 2 features | Consumer comms | Consumer team | October 2026 |
| Internal Slack announcement: Phase 2 launch, Fin AI introduction, new self-serve features | Consumer comms | Consumer team | October 2026 |
| Fin AI knowledge base review and sign-off with Care Product team | Technical enablement | Care Product team | September 2026 |

