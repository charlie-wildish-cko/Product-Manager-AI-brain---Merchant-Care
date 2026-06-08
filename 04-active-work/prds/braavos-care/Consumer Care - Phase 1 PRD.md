**PRD: Consumer Care \- Phase 1**

| Author | Averof Stylianidis |
| :---- | :---- |
| **Date** | April 2026 |
| **Approvers** | Charlie Wildish, Oliver Westlake-Simm, Nick Grafton-Green |
| **Status** | Draft |

# **1.0 Executive Summary**

Phase 1 of Braavos Consumer Care launches the minimum viable care capability required to support 50 internal Checkout.com employees using real-money consumer accounts from June 2026\. Without a functioning care layer, employees who encounter card issues, payment failures, fraud, or account access problems will have no resolution path \- creating trapped funds, unresolved security incidents, and an inability to test the product under realistic conditions.

This PRD defines the capabilities required for Phase 1: three in-app features (fraud reporting, card management, web rescue page), one data dependency (transaction detail display), and four content packages (FAQs covering account access, cards, payments, and fraud). Escalation beyond self-serve is handled via an embedded Jira form \- Fin AI and the full Zendesk-based care stack are Phase 2 deliverables.

# **2.0 Problem Space**

**Problem statement:** Braavos Phase 1 puts real money into the hands of 50 employees with no care infrastructure. When something goes wrong \- a card is lost, a payment fails, a suspicious transaction appears \- there is currently no product surface for the consumer to self-serve, no escalation path to a human, and no content explaining what to do. This creates acute consumer harm risk from day one.

**Who is affected:** 50 internal Checkout.com employees using Braavos accounts with real funds. While this is an internal population, regulatory obligations (GDPR, Consumer Duty Outcome D, PSD2 SCA) apply from the first account opened. The employees are also our product testers \- their experience directly shapes the Phase 2 care stack that will serve 1,000 employees and eventually external consumers.

**Why now:** Phase 1 launches in June 2026\. Without a care layer in place before the first employee account is opened, any issue an employee encounters will have no resolution path. A card lost on day one with no freeze capability and no escalation form creates immediate, preventable consumer harm.

# **3.0 Goals and Success Metrics**

## **3.1 Goals**

* Ensure every employee has a functioning resolution path for the most common and most severe care issues from day one.

* Validate the self-serve-first care model (FAQ \+ in-app actions) before investing in Fin AI and Zendesk for Phase 2\.

* Collect structured data on issue types, frequency, and resolution quality to calibrate the Phase 2 care stack.

**Non-goals:**

* Fin AI agent \- no AI chat capability. Employees use FAQs and the embedded Jira escalation form only.

* Zendesk integration \- care tooling decisions (shared vs dedicated instance) are Phase 2\.

* Formal FCA DISP complaint process \- the formal complaint handling framework is an External launch requirement.

## **3.2 North Star Metric**

**Escalation rate per active user**: the number of Jira care tickets created per active Braavos user per month.

This measures the failure rate of self-serve \- lower means the product surfaces and content are resolving issues without human involvement.

We selected this metric as it is cleanly measurable (Jira ticket count/active user count), directly actionable (each ticket reveals what self-serve failed to resolve), and is the primary input for Phase 2 calibration (which issue categories generate the most tickets \= where Fin AI should focus first).

## **3.3 Success Metrics**

| Metric | Why it matters | Baseline | Target | Source |
| :---- | :---- | :---- | :---- | :---- |
| Escalation rate per active user (NSM) | Primary signal of whether self-serve is working \- each ticket is a self-serve failure | N/A (new) | \<0.5 tickets per user per month | Jira ticket count/active user count |
| Median time to first response on Jira tickets | Measures human responsiveness for escalated issues | N/A (new) | \<4 hours (working hours) | Jira SLA tracking |
| FAQ coverage rate | Measures whether content covers the issues employees actually encounter | N/A (new) | \>80% of ticket categories have a corresponding FAQ | Jira ticket categorisation vs FAQ inventory |
| Card freeze success rate | Core safety action must work reliably | N/A (new) | 100% within 10 seconds | App event logs |

## **3.4 Counter Metrics**

| Metric | What it guards against | Threshold |
| :---- | :---- | :---- |
| Zero-ticket weeks | If we go a full week with zero Jira tickets, employees may not be using in-app care at all \- the form may be hard to find, or they are using Slack instead | Investigate if any full week passes with zero tickets |
| Repeat contact rate | Employees submitting multiple tickets for the same issue indicates poor resolution quality | \<15% of tickets are repeat contacts |
| Unresolved ticket age | Tickets open \>48 hours indicate operational capacity gaps or missing escalation paths | Zero tickets open \>48 hours |

# **4.0 Customer Segments & Opportunity Space**

Phase 1 serves a single consumer segment: 50 internal Checkout.com employees using Braavos accounts with real funds. While this is a constrained, known population, they use the product as real consumers \- making purchases, managing cards, and encountering the same issues external consumers will face. Their care needs are identical to external consumers; the difference is scale (50 vs 300K+) and the availability of compensating channels (Slack, in-person).

The Jobs-To-Be-Done addressed by Phase 1 capabilities are documented in the JTBD Register and summarised below by capability area.

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

**Solution overview:** A lightweight, self-serve-first care layer comprising three in-app features, one data surface, four content packages, and a universal embedded Jira form for escalation. No AI agent. No CRM. The entire stack is designed to be deliverable within the Phase 1 timeline (June 2026\) and to generate the data needed to calibrate the Phase 2 care stack (Fin AI, Zendesk, SOPs).

## **5.1 In scope**

* A1 \- In-app fraud reporting entry point

* A2 \- In-app card management self-serve (freeze, unfreeze, replacement, troubleshooting)

* ~~A3 \- Web rescue page (accessible without app login)~~ \[ Moved to Phase 2\]

* D1a \- Transaction data display in-app (status, failure reason, ETA)

* C1 \- FAQ content: account access and recovery

* C2 \- FAQ content: card management

* C3 \- FAQ content: payments (failure reasons, status, resolution timelines)

* C4 \- FAQ content: fraud and security reporting

* Embedded Jira escalation form accessible from every Help & Support surface

N.B.: For reference, the coding mechanism for the capabilities is derived from the JTBD sheet.

## **5.2 Out of scope**

* Fin AI agent (Phase 2\)

* Zendesk CRM integration (Phase 2\)

* FCA DISP formal complaint process (External launch)

* Wellbeing specialist protocols beyond basic signposting (Phase 2\)

# **6.0 Key Assumptions and Validation**

**1\. Assumption:** The 50-employee population will generate sufficient care interaction volume to validate the self-serve model.

**Validation:** Track weekly interaction volumes from week 1; if volume is too low to draw conclusions by week 4, consider expanding the Phase 1 cohort.

**2\. Assumption:** Employees will use the in-app Help & Support surface rather than Slack or in-person channels for care issues.

**Validation:** Monitor Jira ticket \+ FAQ view volume alongside any Slack mentions; if Slack becomes the de facto care channel, the in-app surface needs redesign before Phase 2\.

**3\. Assumption:** An embedded Jira form is a sufficient escalation mechanism for 50 users.

**Validation:** If median response time exceeds 4 hours or repeat contact rate exceeds 15%, the mechanism is insufficient and Phase 2 must accelerate Fin AI delivery.

# **7.0 Requirements**

## **7.1 App Feature Requirements**

### **7.1.1 A1 \- In-app fraud reporting entry point**

**Owner: Consumer app team**

**US-A1.1**  As a consumer, I want to find the fraud reporting option from a transaction detail screen, so that I can report a problem with a specific transaction without searching for the right place.

**Acceptance criteria:**

* Given a consumer is viewing a transaction detail, when they look for help options, then a 'Report a problem' action is visible on the screen.

* Given a consumer taps 'Report a problem', then they are taken to the fraud reporting flow with the transaction details pre-populated.

**US-A1.2**  As a consumer, I want to report a fraud or security incident from the Help & Support menu, so that I can report a general issue not tied to a specific transaction.

**Acceptance criteria:**

* Given a consumer opens Help & Support from any screen, when they look for fraud reporting, then a 'Report fraud or security issue' option is visible.

* Given a consumer taps 'Report fraud or security issue', then they are taken to the fraud reporting flow.

**US-A1.3**  As a consumer, I want to receive confirmation that my fraud report has been submitted, so that I know the report was received and what happens next.

**Acceptance criteria:**

* Given a consumer completes the fraud reporting form, when they submit it, then a confirmation screen is displayed with a reference number.

* Given a confirmation is displayed, then it includes a plain-language summary of what to expect next and an estimated response timeline.

### **7.1.2 A2 \- In-app card management self-serve**

**Owner: Consumer App team**

**US-A2.1**  As a consumer, I want to see the current status of my card on the card management screen, so that I know at a glance whether my card is usable.

**Acceptance criteria:**

* Given a consumer has a card issued, when they open the card management screen, then the current card status is displayed (active/frozen/blocked/lost).

* Given a card status changes, when the action completes, then the status updates without requiring a page refresh.

**US-A2.2**  As a consumer, I want to freeze my card instantly from the card management screen, so that I can prevent unauthorised use the moment I suspect a problem.

**Acceptance criteria:**

* Given a consumer's card is active, when they tap 'Freeze card', then the card is frozen within 10 seconds and a confirmation is displayed.

* Given a consumer's card is frozen, when they tap 'Unfreeze card', then the card is reactivated and a confirmation is displayed.

* Given a card is frozen, when any transaction is attempted on that card, then it is declined.

**US-A2.3**  As a consumer, I want to order a replacement card without calling anyone, so that I can get a new card when mine is lost, stolen, or damaged.

**Acceptance criteria:**

* Given a consumer needs a replacement, when they tap 'Order replacement', then a replacement order is submitted and a delivery ETA is displayed.

* Given a replacement is ordered, when the consumer returns to the card management screen, then the pending replacement is visible with its expected delivery date.

**US-A2.4**  As a consumer, I want to view a troubleshooting guide for common card issues, so that I can try to resolve the problem myself before escalating.

**Acceptance criteria:**

* Given a consumer is on the card management screen, when they tap 'Troubleshooting', then a contextual guide is displayed with steps for common card issues (chip, contactless, mobile wallet).

* Given the troubleshooting guide is displayed, when the consumer cannot resolve their issue, then they are offered a link to the Help & Support section.

### **7.1.3 A3 \- Web rescue page \[ Moved to Phase 2\]**

**Owner: Consumer App team**

**US-A3.1**  As a consumer, I want to access critical account functions when I do not have my phone or the app is broken, so that I can secure my account and get help through an alternative channel.

**Acceptance criteria:**

* Given a consumer cannot access the Braavos app, when they navigate to the web rescue page URL, then they can access the page without logging into the app.

* Given the web rescue page is loaded, then it displays: emergency card freeze instructions, alternative contact channel links, and account recovery steps.

* Given the web rescue page is loaded, then all content meets Consumer Duty Outcome plain language standards.

### **7.1.4 D1a \- Transaction data \- in-app display**

**Owner: Consumer App team/Data Engineering**

**US-D1a.1**  As a consumer, I want to see full details of any transaction including its status, failure reason, and expected resolution time, so that I can understand what happened with my payment without contacting support.

**Acceptance criteria:**

* Given a consumer opens a transaction detail view, then the following fields are displayed: amount, merchant name, date and time, transaction status, and payment method.

* Given a transaction has failed, then a plain-language failure reason is displayed alongside an expected resolution time where applicable.

* Given a transaction is pending, then the expected settlement time is displayed.

## **7.2 Universal Escalation Mechanism**

### **7.2.1 Embedded Jira escalation form**

**Owner: Consumer App team**

**US-ESC.1**  As a consumer, I want to escalate my issue to a human when self-serve options cannot help me, so that I know my problem is being looked at by a person.

**Acceptance criteria:**

* Given a consumer is on any Help & Support screen or FAQ article, then an 'I still need help' button is visible.

* Given a consumer taps 'I still need help', then an embedded form opens capturing: issue category, description, and relevant transaction reference (optional).

* Given a consumer submits the form, then a Jira ticket is created automatically and the consumer sees a confirmation with a reference number and expected response timeline.

**US-ESC.2**  As a consumer who has reported a fraud or security incident, I want my escalation to be routed to the same channel as all other escalations at Phase 1, so that the process is consistent.

**Acceptance criteria:**

* Given a consumer submits a fraud report (A1), then the submission creates a Jira ticket in the same project as general escalations.

* Given a Jira ticket is created from a fraud report, then it is tagged with the category 'Fraud/Security' for triage purposes.

## **7.3 Content Requirements**

### **7.3.1 Content quality standards (apply to all content capabilities)**

* All articles are published natively in the Braavos app knowledge base before the first employee account is opened.

* All articles are written in plain English per FCA Consumer Duty Outcome C (clear, fair, not misleading).

* All articles are reviewed and approved by Legal (Nick Grafton-Green) before publication.

* All content topics are included in the Care team briefing pack so that agents responding to Jira tickets can reference the same information.

* Each article ends with a clear call-to-action: either a self-serve action (e.g., 'Go to card management') or the escalation form ('I still need help').

### **7.3.2 C1 \- Account access and recovery**

**Owner: Technical Writing and Content teams**

**Topics to cover:**

* Locked account recovery by scenario: forgotten PIN, biometric failure, failed login attempts

* Lost phone: how to access the web rescue page and secure the account

* Magic link recovery: step-by-step walkthrough

* Alternative contact channels when the app is unavailable

* What to do if you suspect your account has been compromised (with link to fraud reporting)

### **7.3.3 C2 \- Card management**

**Owner: Technical Writing and Content teams**

**Topics to cover:**

* How to freeze and unfreeze your card

* How to order a replacement card and expected delivery timelines

* Troubleshooting: card declined at POS, contactless not working, chip issues

* How to read your card status in the app

* What to do if your card is lost or stolen (with link to card management screen)

### **7.3.4 C3 \- Payments: failure reasons, status, and resolution timelines**

**Owner: Technical Writing and Content teams**

**Topics to cover:**

* Why payments fail: common reasons in plain language

* How to read transaction status in the app (pending, completed, failed, refunded)

* Expected resolution timelines by failure type

* What to do if a payment was sent to the wrong account

* What to do if an ATM did not dispense cash

### **7.3.5 C4 \- Fraud and security reporting**

**Owner: Technical Writing and Content teams**

**Topics to cover:**

* How to report fraud or a scam (with link to in-app fraud reporting)

* What to do with an unauthorised transaction

* Types of scams: impersonation, investment, romance, recruitment \- what to watch for

* What happens after you report fraud: investigation process and timeline

* When and how provisional credit may be applied

# **8.0 Design and User Experience**

## **8.1 Key UX principles**

* Help & Support entry point visible on every main screen \- employees should never be more than one tap away from help.

* Self-serve first: the app should guide towards FAQ content and in-app actions before surfacing the escalation form.

* Plain language throughout \- no internal jargon, no technical payment terminology without explanation.

* Contextual help: the Help & Support surface on the card management screen should show card-related content first; on the transaction screen, payment-related content first.

* The escalation form should pre-populate context (current screen, transaction reference if applicable) to reduce employee effort. \[stretch goal\]

# **9.0 Instrumentation and Monitoring**

## **9.1 Key events to instrument**

| Event | Description | Properties |
| :---- | :---- | :---- |
| care.faq.viewed | Tracks which FAQ article was viewed, from which screen, and for how long | article\_id, source\_screen, view\_duration\_seconds |
| care.escalation.submitted | Tracks Jira escalation form submissions | issue\_category, source\_screen, transaction\_ref (if applicable) |
| care.card.freeze.initiated/completed/failed | Tracks card freeze lifecycle | card\_id, time\_to\_complete\_ms, outcome (success/failure), failure\_reason |
| care.card.replacement.ordered | Tracks replacement card orders | card\_id, reason (lost/stolen/damaged) |
| care.fraud\_report.submitted | Tracks fraud report form submissions | transaction\_ref, report\_type |
| care.help\_support.opened | Tracks Help & Support section opens | source\_screen, user\_action (faq\_browse/escalation\_form) |

## **9.2 Monitoring Dashboards**

* Care Phase 1 Overview \- weekly: FAQ views by article, escalation volume by category, card freeze success rate, median response time on Jira tickets.

* Escalation Triage Board \- Jira board filtered by Phase 1 care tickets, sorted by age.

# **10.0 Risks and Open Questions**

## **10.1 Risks**

| Risk | Likelihood | Impact | Mitigation |
| :---- | :---- | :---- | :---- |
| Employees bypass in-app care and use Slack/in-person channels, making the self-serve model unvalidatable | High | Medium | Clear comms at launch that in-app care is the primary channel. Track Slack mentions as a counter-signal. Consider making in-app the only supported channel for non-urgent issues. |
| Braavos app team cannot deliver A1, A2, A3, D1a by June 2026 due to competing priorities | Medium | High | Confirm sprint allocation by mid May. If at risk, descope A3 (web rescue page) first \- it is the lowest-frequency need at 50-employee scale, and push further items into next iteration as needed. |
| A security incident (ATO, fraud) occurs at Phase 1 and the manual Jira-based response is too slow | Low | High | Define an out-of-band emergency protocol (e.g., dedicated Slack channel for security incidents) alongside the Jira process. Card freeze is self-serve and does not depend on Jira response time. |
| FAQ content is not ready by June launch due to creation/review delays | Medium | Medium | Begin content drafting in May. Prioritise C1 (account access) and C4 (fraud) as highest-severity topics. Legal review can be parallelised across content packages. |

## **10.2 Open Questions**

| Question | Proposal | Owner |
| :---- | :---- | :---- |
| What Jira project and workflow should care tickets use? | Dedicated Jira project (e.g., BCARE) with a simple Kanban workflow: Open \> In Progress \> Resolved. Categories matching the care taxonomy. | Braavos app team |
| Who triages and responds to Phase 1 Jira tickets? | TBD | Oliver Westlake-Simm |
| Does Consumer Duty formally apply to internal employee accounts? | We should design as if it does \- the same product will serve external consumers. Legal to confirm. | Nick Grafton-Green |

# **11.0 Rollout Plan**

Phase 1 is itself the first phase of the broader Braavos Consumer Care rollout. Within Phase 1, delivery is sequential: content and Jira setup first (can begin immediately), then app features (dependent on Braavos sprint capacity).

## **11.1 Delivery sequence**

| When | What | Owner | Dependency |
| :---- | :---- | :---- | :---- |
| May 2026 | Jira project created, workflow configured, triage process documented | Consumer team/IT | Jira project setup and access for Care Ops |
| May 2026 | C1-C4 content drafted | Technical Writing and Content teams | None |
| May 2026 | Care Product team confirms Jira workflow alignment with existing care processes | Care Product team (Charlie Wildish) | None |
| May-June 2026 | Legal review of C1-C4 content (Consumer Duty Outcome C and vulnerability standards) | Nick Grafton-Green | C1-C4 drafts complete |
| May-June 2026 | A1, A2, D1a built and tested | Braavos app team | Sprint allocation confirmed |
| May-June 2026 | A3 (web rescue page) built | Braavos app team | Sprint allocation confirmed |
| June 2026 | C1-C4 content published in-app | Technical Writing and Content teams | Legal sign-off |
| June 2026 | Care team briefing: Jira triage, FAQ reference, emergency protocol | Consumer team/Oliver Westlake-Simm | All above complete |

## **11.2 Success criteria to proceed to Phase 2**

* All 8 capabilities operational for at least 4 weeks.

* Escalation rate per active user trackable for at least 4 consecutive weeks with sufficient volume to identify category-level patterns.

* Zero unresolved Jira tickets open \>48 hours at the time of Phase 2 gate review.

* Issue categorisation data sufficient to calibrate Fin AI knowledge base for Phase 2\.

## **11.3 Definition of Done**

* **Technical:** All P0 app features (A1, A2, D1a) delivered, tested, and accessible in the production app. A3 delivered or explicitly descoped with documented rationale.

* **Content:** All FAQ articles (C1-C4) published, Legal-approved, and accessible in-app.

* **Operational:** Jira triage process live. Care team briefed. Emergency security protocol documented.

* **Instrumentation:** All care events instrumented and visible in the Phase 1 Overview dashboard.

# **12.0 Dependencies**

| Dependency | Owner | Required by |
| :---- | :---- | :---- |
| Technical Writing and Content teams to draft C1-C4 FAQ content | Technical Writing and Content teams | May 2026 |
| Legal review of consumer-facing content (Consumer Duty Outcome C, vulnerability standards) | Nick Grafton-Green | Before Phase 1 go-live (June 2026\) |
| Jira project setup and access for Care Ops | Consumer team | May 2026 |
| Care Product team to confirm Jira workflow alignment with existing care processes | Charlie Wildish | May 2026 |

# **13.0 Go-to-Market**

Phase 1 is an internal launch to 50 employees. Go-to-market is limited to internal enablement.

| Activity | Type | Owner | Timeline |
| :---- | :---- | :---- | :---- |
| Care team briefing: Jira triage, FAQ content, escalation paths, emergency protocol | Operational enablement | Consumer team/Oliver Westlake-Simm | June 2026 |
| Employee onboarding comms: 'How to get help' guide included in Braavos onboarding email | Consumer comms | Consumer team | June 2026 |
| Internal Slack announcement: Phase 1 launch, what to expect, how to report issues | Consumer comms | Consumer team | June 2026 |

