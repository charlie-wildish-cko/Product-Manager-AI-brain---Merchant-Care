# Operations Platform: Definition and Story Spine

Status: draft for XFN group (Support, Risk, Compliance; product and operations). Deliverable: Operations Platform Design (Q4 2026, product discovery / strategy) in `2026 deliverables.md`.

How this doc works: Part 1 holds every fact once. Part 2, the story spine, only says which facts go on which slide and how each slide is laid out. Each slide has a "Draws from" line pointing to its Part 1 section. If the two disagree, Part 1 wins, and changes flow from Part 1 to Part 2.

## Part 1: Definition

### 1. Problem today

Our operations tooling model is designed around products, not customers. Each product team ships its own tools, queues and processes, so humans absorb the fragmentation. Customers repeat themselves, are bounced between teams, hear conflicting messages from different teams, cannot see where their request is, and wait on slow decisions. CSAT drops 20% when work moves from Care to another Ops team. Agents switch between about 5 tools on one ticket, create and copy cases by hand, and redo checks already done by another team. Account managers mask this for white-glove customers. At Platforms, Consumer and SMB scale it gets worse. The consequence is churn risk, and an inability to produce transparent regulatory reporting, with fine and breach exposure.


**Data gathering - need Ops/OE support across Ops teams:**

- Team sizes
- Volumes of cases 
- Cost per case?
- a work 'inventory' per team in each area - to see what work looks like across, what is similar what is different
- Factor the volumes x the work types to analyse what is simple vs complex
- What are the top 3 problems per Ops team?

**Per-team data card** (one per team in the section 3 list, also the input to the prioritisation model in section 9a): headcount (in-house and BPO) and cost; cases a month by work type; share Checkout-initiated; handle time and cycle time against SLA; backlog age; case system or inbox used; tools per case; share of cases created by hand; cross-team handoffs (share of cases touching 2 or more teams, owner changes per case); regulatory deadlines; 12-month growth driver. Where a team has no data, a 2-week sample gives a labelled estimate. Request workbook: `04-active-work/working-files/ops-data-request/ops-data-request.xlsx` (tabs: field guide, team data card, tool inventory).

| Evidence                                                                                                                                                                                                        | Source                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| 2 primary case management systems: Salesforce (several teams), Zendesk (Care only). Some teams work from email inboxes with no case system                                                                      | Steerco draft, Charlie (2026-10-07) |
| Multiple tools used to complete work (RA tool, CAT, Fircosoft, Genesis, Sardine, Looker, Datadog and others)                                                                                                    | Steerco draft              |
| At least 20 Retool apps used in Care alone                                                                                                                                                                      | Steerco draft              |
| CSAT drops 20% when work moves from Care to another Ops team                                                                                                                                                    | Steerco draft              |
| Complaints reports take hours to collate end to end                                                                                                                                                             | Steerco draft              |
| Periodic reviews ask merchants for data already provided, because it sits in another system                                                                                                                     | Steerco draft              |
| Account managers intervene heavily to align cross-team work                                                                                                                                                     | Steerco draft              |
| Teams cannot see the same customer data and communications history, so customers get different answers                                                                                                          | Steerco draft              |
| Channels are unstructured (email, webform, chat, social) and internal requests move by email and Slack                                                                                                          | Steerco draft              |
| Knowledge sits in 8 places (Google Docs, Zendesk, Salesforce, Confluence, Slack, Figma, Gemini notebook, Guidde) across 21 sub-functions. Federated search masks it but does not embed guidance in the workflow | Knowledge Manager comments |
| About 5 tools used on a single Care L1 ticket                                                                                                                                                                   | Mauritius site visit       |
| IP onboarding runs on a spreadsheet tracker, manual MCC checks and Gmail approvals after documents move from Salesforce to Drive, with one reviewer approving every case                                        | Mauritius site visit       |
| Cases are created by hand in Salesforce or by email-to-case, then assigned by hand. Slack conversations run on the side and are not linked to any case. The configuration team copies Salesforce cases into CAT by hand | Ops review, 2026-10-07 |
| Most Risk Operations teams work from a basic Salesforce setup that limits queueing and reporting. Cases close without a recorded outcome (approved, declined or escalated), only as closed | Head of Risk Operations, 2026-10-13 |
| Information is requested by email, from Salesforce or straight from an inbox, and received as email attachments to download. Very little arrives through the Dashboard | Head of Risk Operations, 2026-10-13 |
| There is no single secure place for merchants to upload documents, no scanning for sensitive content, and no company-approved way to ask for sensitive information. Secure upload exists for some Dashboard flows (for example bank account) and not others. It has been flagged several times and not prioritised | Head of Risk Operations, 2026-10-13 |
| Platform sub-merchants are asked for information through the platform by webhook. Risk Operations cannot see when a request was sent or whether chasers ran | Head of Risk Operations, 2026-10-13 |
| A merchant's Dashboard shows Care's replies to a request but not a reply from another team such as Disputes, so the Care request looks unanswered after the other team has replied by email | Charlie, Ops review 2026-10-13 |
| Transaction Monitoring cases open in Salesforce, are worked in Retool, sync back only on close, and return to a queue for manual reassignment after an information request is answered                          | Mauritius site visit       |
| Manual QA reviews are under 1% of Care volume                                                                                                                                                                   | Mauritius site visit       |
| An underwriting review flagged in May 2024 was still pending while the merchant kept processing                                                                                                                 | Mauritius site visit       |
| Commercial and account managers talk to merchants in Slack, WhatsApp and email, so Ops cannot see what was said. Example: Care messaged a merchant about goodwill remediation after commercial had already given a fee reduction | Ops review, 2026-10-07 (Joel) |
Treat sources as verified here, not gaps.

**Impact**

Basis uses the same status key as the evidence table. *Inferred* means the impact follows from the pattern and has no evidence yet.

| From     | Impact                        | What it means                                                                                            | Basis                                 | Addressed by |
| -------- | ----------------------------- | -------------------------------------------------------------------------------------------------------- | ------------------------------------- | --- |
| Customer | Repeat themselves             | Teams can't see the same customer data, and periodic reviews re-ask data already provided                | Needs source                          | Customer context |
| Customer | Mixed answers                 | Answers differ by team                                                                                   | Needs source                          | Customer context, AI agents and knowledge |
| Customer | Bounced between teams         | CSAT drops 20% when work moves from Care to another Ops team                                             | Care CSAT data                          | Case system, Care experience |
| Customer | No visibility of status       | Status sits in whichever system holds the work, and Care cannot see Checkout-initiated work              | Inferred                              | Care experience |
| Customer | Slow decisions                | Manual handoffs and single-approver bottlenecks lengthen onboarding and reviews                          | Single observation                    | Case system |
| Customer | No one to rescue the case     | Consumer and SMB customers have no account manager to absorb the fragmentation                           | Needs source                          | Care experience, AI agents and knowledge |
| Agent    | Swivel chair between tools    | About 5 tools on one Care L1 ticket, and a periodic review moves through CAT, Genesis, RA Tool and Looker to decide if it is needed | Single observation | Portal for people, Shared services, AI agents and knowledge |
| Agent    | Manual case handling          | Cases created and assigned by hand, and the configuration team copies Salesforce cases into CAT                                          | Ops review, 2026-10-07 | One front door, Case system |
| Agent    | Repeated checks               | A risk alert already reviewed by another team is checked again, because nothing links the earlier outcome                                | Single observation (Risk) | Orchestration layer, AI agents and knowledge |
| Agent    | Cannot find the answer        | Knowledge in 8 places across 21 sub-functions, and search does not put guidance in the workflow                                           | Knowledge Manager comments | AI agents and knowledge |
| Checkout | Cost does not fall with scale | Can be 5 tools per ticket, manual reassignment and knowledge in 8 places, while volume grows 36x by 2030 | Single observation, stated in session | Case system, AI agents and knowledge |
| Checkout | Regulatory exposure           | Missed SLAs, and complaints reports that take hours to compile                                           | Needs source                          | Reporting and insight, Control and quality |
| Checkout | Risk exposure                 | Decision latency, such as a flagged review pending while the merchant kept processing                    | Single observation, verify with Risk  | Case system, Control and quality |
| Checkout | Quality blind spots           | QA is not being performed or is at very low levels which means hard to spot problems early.              | Single observation                    | Control and quality |


Not yet quantified: the AI-assisted vs human-only split of work, agent time lost to tool-switching and rework, the cost of a cross-team handoff, effort to produce a regulatory report, and onboarding and review cycle times against target.

### 1a. Vision: what good looks like

Before the solution: the outcome we want for each group the problem hits. Each vision answers the matching "poor" in section 1, and none describes how it is delivered.

| Who          | Vision                                                                        | What good looks like                                                                                                                                                                                                                             | How we know                                                                                                                                                                  |
| ------------ | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Customers    | Ask once, hear one voice, see where it is                                     | They never repeat themselves, whoever they deal with. They are never bounced between teams. They hear one consistent message and know a request from us is genuine. They can see where their request is, and decisions do not wait on one person | Merchant CSAT by segment (guardrail). CSAT at cross-team handoff (20% drop today). Contact rate. [NEEDS DATA: repeat-request rate]                                           |
| Human agents | Work in one place, with the context to decide                                 | They see the customer's history and what other teams did. They never create, copy or chase cases by hand. They do not redo checks another team has done. Guidance is in the workflow                                                             | Tools per ticket (about 5 today). Share of cases created by hand [NEEDS DATA]. Agent time lost to tool-switching (not yet quantified)                                        |
| Checkout     | Operations that scale with volume, not headcount, and can prove what happened | Cost per contact falls as volume grows. Every piece of work is measured, so we know what to fix. Regulatory reports come from the record, not from hours of stitching. Risk decisions land on time and quality is checked on all work            | Cost per contact (north star). Time to compile a complaints report (hours today). Cycle time for Risk and Compliance work. QA coverage (under 1% in Care today, target 100%) |

Customers and agents are both users of the platform: the customer vision is the front stage, and the agent vision is the back stage (section 5).

### 2. Why now

Three things land at once: volume, consumers and a platform decision.

| Fact                                                                                                                                  | Source                                             |
| ------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| Care contacts grow from about 60k in 2026 to 1.5m-2m in 2030, up to 36x. Care contacts only, not total Ops volume (but assume same levels) | `01-knowledge-base/metrics/contact forecasting.md` |
| 70-80% of 2030 Care contacts are consumer                                                                                             | `01-knowledge-base/metrics/contact forecasting.md` |
| Ray internal launch end Dec 2026, external beta end Q1 2027                                                                           | `01-knowledge-base/products/ray.md`                |
| Platforms & SMB - Platforms scale and SMB starts in 2027                                                                              |                                                    |
| Zendesk renewal (June 2027): the move to Plain is the single case system of record for Ops                                                  |                                                    |
| Periodic review intake rises from 100-150 cases a month to about 450 a month next year, as the first sub-merchant cohort from the IP full platform product comes due. Cases take one to two days each to close. The RA Tool has not yet delivered straight-through automation for them | Head of Risk Operations, 2026-10-13 (single source) |

### 3. Definition

**Defining thread:** Care is the customer experience of Checkout.com's operations. Whichever team is doing the work, the customer has one place to ask, to see what we know and what we are doing, and to hear from us first. Care the team is one operator behind that experience, not the whole of it.

The operations platform is where Checkout.com's operational work is received, routed, decided and actioned, around one view of the customer it concerns, with a shared record of what was done and communicated that internal teams and customers can see.

Care is the customer-facing layer of the platform (see section 6). Care the team is one operator on the platform. Not all work routes through the Care team.

"Customer" means anyone the work concerns: direct merchants, platforms, platform merchants, consumers, and end users with no account relationship (open banking payers, issuing cardholders).

The teams involved: 3 areas and 16 teams. This is the unit for the data card (section 1) and the prioritisation model (section 9a).

| Area | Team | Lead | Tools known today (from evidence) |
|---|---|---|---|
| Merchant Operations (Ashvin) | Care | [NEEDS DATA: lead] | Zendesk, Fin, 20+ Retool apps |
| | Config | [NEEDS DATA: lead] | Salesforce (cases copied into CAT by hand), CAT |
| Risk Operations (Luca) | Underwriting | Ali, Jarrett | Salesforce, CAT. To confirm: others |
| | Due diligence | Mirabel | To confirm |
| | Consumer fraud | Fabio | To confirm |
| | Disputes | Akshav | To confirm. Replies to Care by email, outside the Dashboard |
| | Scheme compliance | Jaysen | To confirm |
| | AML periodic reviews | Ian | CAT, Genesis, RA Tool, Looker, basic Salesforce. Information requested by email |
| | Risk monitoring | Cayne | To confirm |
| | IDV/Fraud | Nathan | To confirm |
| Compliance (John) | Transaction screening | Pooja | To confirm |
| | Transaction monitoring | Pooja | Salesforce, Retool (syncs back only on close) |
| | Merchant screening | Pooja | To confirm |
| | Line of Defence / FCIU | MLROs | To confirm |

Tools named in evidence but not yet mapped to a team: Sardine, Fircosoft, Datadog. Most Risk Operations teams work from a basic Salesforce setup (head of Risk Operations, 2026-10-13). The tool column is completed from the data card, one team at a time.

Operations as a whole is about 300? agents across many teams such as above. Operators include in-house and BPO agents, and multiple BPOs may work different volumes.

### 4. Terms

| Term                    | Definition                                                                                                                                                                  | Today                                                                         | Vision                                                                                                                                                                                                                       |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Channels                | How a request reaches us: email, form, Dashboard, chat, social, internal request, system trigger                                                                            | Many, mostly unstructured, internal work by email and Slack                   | Internal work and system triggers create cases through structured channels, not email. Customer channels (email forms, Dashboard, chat, social) enter as structured requests. Pre-filled intake, one front door per audience. Team inboxes are retired. Customers who need email use one unified address, and the work is triaged and routed behind it. Account managers submit work through a dedicated structured channel, or are empowered to resolve it themselves |
| Case management         | The case system of record: where work is created and distributed. Where it arrives, who owns it, who it is assigned to (human or AI), status, SLA clock, full audit trail. It does not complete the work                                | Salesforce (several teams), Zendesk (Care only), and email inboxes for some teams. Separate queues | One case system of record across teams, for assignment, SLAs and audit                                                                                                                                                   |
| Tooling                 | The screens and systems people use to look things up and take action. Used by AI and human agents.                                                                          | 30+ tools, at least 20 Retool apps in Care alone                              | One back office portal for human agents (UI), with role-based permissions. AI agents read the same data through interfaces (APIs and MCPs). Domain teams own the UI and interface layers for their domain                                                                                                                                                    |
| AI agents               | Software that does work in place of a person: triage, analysis, routine actions, with human approval where needed                                                           | Fin for Care support only (the customer agent today).                                                    | The customer agent is the second point of call for customer queries, after self-serve. It solves them through the orchestration layer with no human involved, a case is still created for audit, and anything it cannot solve falls back to a human agent. Internal and customer escalations assigned to a domain agent by task type and risk, using the same data and sources as human agents                                           |
| Care team               | The people in Merchant Care who handle support contacts and own those SLAs                                                                                                  | One team among many Ops agents                                                | Unchanged: one operator on the platform, owns its case types                                                                                                                                                                 |
| Care experience         | What the customer sees their side when they need help from us, across all teams: status, communications, proactive contact                                                  | Only exists for Support, not other work done by Checkout.                     | The customer-facing layer of the platform, whichever team does the work and enables visibility to customers on getting help and any information they need.                                                                   |
| Customer-initiated work | Work that starts because a customer asks (for example a support contact or dispute query)                                                                                   | Mostly Care, in Zendesk and Salesforce                                        | Enters through designated channels, fully visible to the customer within rules                                                                                                                                               |
| Checkout-initiated work | Work that starts because a rule, schedule or event creates it (for example onboarding checks, fraud and transaction alerts, periodic reviews) or because we reach out first | Spread across Salesforce, Retool and specialist tools, often hidden from Care | Structured intake into a case object from automated and Checkout team origins, visibility to the customer set by the owning function.                                                                                        |

Also used:
- **Work type**: the category of case (for example Support, Dispute, Underwriting, Fraud, Transaction monitoring alert) and the data it requires. Work type drives routing, reporting, AI involvement and audit, so its fields are quality controlled.
- **Portal**: the one back office UI where human agents complete work, opened from a case. The case system creates and distributes work, the portal is where humans complete it as needed, and AI agents complete work through interfaces. Every action in the portal writes back to the case. Why one portal: it gives control of permissions, traceability and audit of work, and removes the swivel chair between tools, which lifts human agent productivity. Test: if it describes the work item (owner, status, SLA, communications, audit), it lives on the case. If it reads or changes customer data or takes an action, it happens in the portal or an interface and is recorded on the case.
- **Product onboarding**: Stage 0. The step that runs once per product launch or change and configures the ops stack (work types, workflows, orchestration rules, portal modules, permissions, knowledge, reporting tags) before the first case. Gated by MCAP, with rejection rights for incomplete submissions. Measure: % of launches fully onboarded before first case. Today the stack finds out from live work: 150+ initiatives were reviewed at 2027 planning, and several (BlueEMI, Ray, eFX, Interest) shipped with no Care assessment.
- **Reflex**: the insight and prevention data product (Care's Insight & Prevention domain, `01-knowledge-base/products/reflex.md`). It reads work data, clusters root causes and routes fixes to owners. Where a work type relates to a product it attributes the work to the product catalogue entry. Where it does not (for example a process, policy, knowledge or tooling problem) it reports against the work area instead. Today it ingests Care data (Zendesk, Fin, NPS). On the platform it reads the one case record for every work type, so Support, Risk and Compliance issues are analysed together. It stays a separate data product: the platform supplies the record and the tagging, Reflex does the analysis.
- **Customer agent**: the customer-facing AI and the second point of call, after self-serve, when a customer gets in touch with us. It solves queries by accessing the orchestration layer, using the same interfaces and data as human agents, with no human interaction. A case is still created for every query, so the audit trail and reporting are complete. Anything it cannot solve falls back to the human side: a human agent picks up the same case, within escalation controls set by customer segment. Human support is viable for Enterprise, but not for SMB or Consumer at high volumes, so escalation to a human is limited by policy for those segments. Today: Fin, Care support only. A domain agent is different: it does back office work assigned from the case system. This is the platform-wide term and does not change the Care product model's naming.
- **Specialist tools**: tools that do the domain analysis and work (for example Care Agent toolkit, Sardine, Sphinx, RA Tool, Retool, Fircosoft, Genesis). They do not necessarily stay. Their functionality is consolidated into the unified portal where possible, so people stop moving between tools, and their output is surfaced on the case. Where a tool is not consolidated, it is linked to the case.
- **Shared services**: the interfaces (APIs and MCPs), owned by domain teams, that give the portal and AI agents the same customer, transaction, funds, communications, KYC and action-history data (candidate design, see open points).
- **Case system of record**: the single place where work is created, assigned, tracked and audited. It is not the system of record for data (ledgers, payments, customer data stay where they are). Work does not have to be performed in the case system: a task may run in the portal, through an interface or in a specialist tool, and the outcome is always written back to the case. It is not the tool that does the work for everyone.
- **Orchestration layer**: connects cases, tools and AI agents so a task can be assigned to AI or a human by task type, and so work done in a tool links back to its case.
- **Linked case**: a case raised for an owning team from a customer contact, linked to the customer thread that stays with Care.

### 5. Solution: capabilities and the stack

The platform needs eleven capabilities in six groups. Each answers a failure in section 1 and a vision line in section 1a. The owner column says who builds and runs it: **Platform** (the operations platform team), **Care** (the customer-facing layer), or **Domain teams** (the teams that own a domain's data, tools and interfaces). The last column places each capability in a stack tile (below), which are what slides 4 and 5 show.

| # | Capability | What it does | Owner | Moves | Stack tile |
|---|---|---|---|---|---|
| | **Front door** | | | | |
| 1 | One front door | Structured intake for all work, whoever starts it. Customer-initiated: self-serve in the Dashboard first, then structured requests from email forms, Dashboard, chat and social. Team inboxes are retired, customers who need email use one unified address, and account managers submit work through a dedicated channel. Checkout-initiated: triggers, schedules and internal requests (fraud alerts, monitoring rules, underwriting triggers, commercial requests) create cases through structured channels, not email. Both land as the same kind of case in the same queue, and retried creation does not duplicate | Platform | Contact rate, cost per contact | Channels |
| 2 | Care experience (communications and visibility) | The customer-facing layer, and where every message to and from the customer sits, whichever team does the work. Two-way: one thread per case, linked to the customer, whatever the channel or team, and a customer reply returns to the owning case automatically. Two modes: a conversation hosted by Care for anything that needs a reply, and a visible automated notification for status, requests and outcomes. Proactive: notifications and outreach before the customer asks, including requests for information on Checkout-initiated work. The owning function approves the wording and sets visibility, and everything sent or received is logged on the case. A self-serve view of status, actions taken and next steps, within those visibility rules. Requests for information are automated: the first request, scheduled chasers, a secure way to upload documents instead of email (to be defined), and the response ingested onto the case | Care | Contact rate, Merchant CSAT | Channels |
| | **Work** | | | | |
| 3 | Case system of record | Where work is created and distributed. One case object and lifecycle for all work (open, assign, act, decide, close). Each case has a work type with its own required fields. Work is pushed to the right person, queue or AI by skills, capacity, priority, jurisdiction, shift and SLA risk. Cases reassign across teams, and a customer reply returns the case to the right queue. Internal requests, approvals and escalations are tracked work linked to the case, and approvals route to available approvers, not one named person or email. Case age, touches and SLA risk are visible, and repeated touches trigger review. Every case closes with a recorded outcome (for example approved, declined or escalated), not just closed | Platform | Cost per contact, cycle time, Merchant CSAT | Case management |
| 4 | Customer context | One view of the customer, with a timeline of everything done and said. A case links to a customer as the minimum (business for merchants, customer ID for consumers), can reference more than one (payer and payee), or can be unlinked (unidentified contacts, spam). Related recently closed cases for the customer are visible, along with what was asked of the customer, when, and whether they responded | Platform (Care owns the presentation) | Contact rate, Merchant CSAT | Case management |
| 5 | Portal for people | One back office portal for human agents, with controlled permissions, full audit and no swivel chair between tools. Specialist tool functionality is consolidated into the portal where possible, and where it is not, the tool is linked to the case. Opened from a case, and every action writes back to it. Domain teams contribute and own their UI modules to one standard. The minimum is one case system and one tool for actions. A headless portal on the case system's API is possible but not assumed. A different UI per use case (for example an AI-powered credit review form) can sit on the same backend, with outcomes in one format | Platform (portal shell), Domain teams (UI modules) | Cost per contact, agent productivity | Tooling and AI |
| | **Data and interfaces** | | | | |
| 6 | Orchestration layer | Connects cases, specialist tools and AI agents with one standard pattern for every team: call, enrich and complete work items. Work done in a tool links to the originating case, which keeps the audit trail whole and measures handle time. Each task goes to AI or a human by task type and risk, and both use the same data and sources. Agent approval is a distinct, auditable event that can trigger downstream workflows (refund, notification, ledger update). Tool output is surfaced on the case. The case record is the source of truth: based on rules for its type it creates the downstream work item in the tool where the work is done, and the outcome is registered back on the case | Platform | Cost per contact, cycle time | Tooling and AI |
| 7 | Shared services | One set of interfaces (APIs and MCPs) behind the portal, the orchestration layer and every AI agent, so humans and AI use the same data: customer records, communications, transactions, funds, KYC/KYB status, merchant risk level (the RA Tool merchant risk 360 vision), periodic reviews and action history. Domain teams own the interfaces for their domain, built to one standard. Permissions apply at user level across portal and agents, so nobody can use an agent to reach data they cannot see. The platform does not become a system of record for data. Candidate design and an open point (section 12) | Domain teams (platform sets the standard) | Cost per contact, regulatory confidence | Data and reporting |
| | **AI and knowledge** | | | | |
| 8 | AI agents and knowledge | The customer agent is the second point of call for customer queries, after self-serve. It solves them through the orchestration layer with no human involved, a case is still created for audit, and anything it cannot solve falls back to a human agent, within escalation controls set by customer segment. Domain agents retrieve, analyse or draft for humans and take Checkout-initiated tasks. Agents prefill from related recently closed cases, so a check already done by another team is not redone. Knowledge and saved responses surface in the case by work type, as guided flows and decision trees, not a separate search | Platform (customer agent: Care) | Cost per contact | Tooling and AI, Data and reporting |
| | **Control and insight** | | | | |
| 9 | Control and quality | Role- and partner-scoped permissions (including BPO), visibility rules set by owning functions, immutable or versioned history, redaction of sensitive data (cards, IBANs, API keys), retention per work type, and full case export for regulators. Quality control checks work before it is actioned (four-eyes review for configuration changes and regulated work). Quality assurance reviews completed work: AI scoring of all cases, human review of a sample to check the checker, and targeted review of high-touch cases. Findings feed coaching, knowledge updates and reporting | Platform (rules set by Risk, Compliance and owning functions) | Regulatory confidence, QA coverage, Merchant CSAT | Case management, Tooling and AI |
| 10 | Reporting and insight | Three outputs from the one case record, plus a feed to Reflex. Regulatory: reports and evidence from the audit trail, owned by Compliance. Efficiency: agent status, occupancy, productivity, handling time, SLA performance, AI resolution, cost per case, quality scores and review coverage. Volumes: work in, work out and backlog by work type, team, partner and segment, with a cross-team throughput view. Insight and prevention: Reflex reads the case record to surface the biggest problems and work areas, find root causes and route fixes to the owning team. Some relate to a product and some do not. It starts with Care and extends to every work type | Platform (Reflex: Care) | Cost per contact, regulatory exposure | Data and reporting |
| | **Launch** | | | | |
| 11 | Product onboarding | Runs once per product launch or change, before the first case. It is Stage 0 of the Care flywheel (`01-knowledge-base/strategy/care-product-model.md`) extended across Operations. The launching product team registers the product through MCAP and Hive, and each domain's documented inputs say what it needs. A readiness check (the Support Readiness Agent concept) derives what the stack needs. The output configures work types and required fields, workflows, routing and SLAs, orchestration rules, the interfaces and portal modules domain teams own, permissions, knowledge, and reporting and attribution tags. Incomplete submissions can be rejected with reasons, which leaves an audit trail. Changes, deprecations and regulatory changes follow the same path in tiers (proposed: essentials, standard, full service) | Platform, with product teams (MCAP, EP governance) | Contact rate, cost per contact | All four tiles (configures them before launch) |

**The stack: today and vision**

| Tile | Today | Vision |
|---|---|---|
| Channels | Email, webform, Dashboard chat, social. Internal requests by email and Slack. Unstructured | Internal requests and system triggers (alerts, checks, reviews) create cases through structured channels, not email. Customer channels (email forms, Dashboard, chat, social) enter as structured requests. Pre-filled intake. One front door: team inboxes retired, one unified customer email for those who need it, and a dedicated channel for account managers to submit work. The Care experience band spans channels and the customer view of status |
| Case management | Salesforce for several teams, Zendesk for Care only, and email inboxes for some teams. Separate queues, no shared view. Care appears as a team here and in tooling only | One case system of record for Support, Risk and Compliance: assignment to humans and AI, SLA timestamps and the audit log of record |
| Tooling and AI | 30+ tools, 20+ Retool apps in Care, about 5 tools on one ticket. | One back office portal for human agents and interfaces for AI agents, over the same data, with role permissions. Domain teams own the UI and interface layers. An orchestration layer assigns each task to AI or a human by type and risk, and work done in tools links back to the case. AI and humans use the same data. Humans handle judgment and approve. Quality control and 100% quality assurance coverage |
| Data and reporting | Customer data in separate systems. Knowledge in 8 places. Complaints reports take hours to collate. Access set per tool | One set of APIs behind tools and agents. Knowledge in one source, embedded in the workflow. Regulatory, efficiency and volume reporting from one record. Permissions and visibility set by the owning function |

The stack shows capabilities, not systems. Case management is the case system of record. How Salesforce and Zendesk work moves into it is an open decision (migration path).

**What the platform does not own**

- Systems of record for data: such as ledgers, payments data, customer data
- Decision engines and the analysis they do: screening, fraud scoring, KYC verification. The portal consolidates the screens people use to work with them where possible, and the platform receives their alerts
- Commercial's customer and contract records: commercial keeps Salesforce as its record of truth (CRM, quote to cash, which is moving out of Salesforce). Work that commercial initiates (MCRs, net new onboarding, underwriting, configuration) creates cases through structured intake. The boundary is an open point
- Reflex and its analysis: Reflex stays a separate data product. The platform supplies the case record and required tags, and Reflex produces the root causes
- Regulatory judgments: these stay with Compliance and Risk
- Regulatory submissions: Compliance owns what is filed and when. The platform supplies the data and evidence.

Test: work belongs on the platform if a person or AI must receive it, review context, decide and act. A system that decides alone stays outside, and the platform receives its alerts.

### 6. Customer experience and Care

**The customer journey.** Six steps, covering work the customer starts and work we start.

| Step | What the customer experiences | What the platform does | Area |
|---|---|---|---|
| Ask or be told | Asks in the channel they choose, or hears from us first when we start the work (a check, a request for information, a notice). No need to know which team to contact. | Structured intake from any channel and from system triggers, plus proactive contact | Care experience, Work |
| Be known | Does not repeat themselves. Whoever helps knows who they are and what has happened. | One view of the customer and their history | Customer |
| Get picked up | Fast response, no bouncing between teams | Routes to the right person or AI by skill, capacity and priority | Work |
| Get it handled | A quick answer for routine requests, an expert for complex ones | AI agents do routine work, specialists and humans handle judgment, checks run before action | AI and knowledge, Control and quality |
| Stay informed | Sees status, what was done and what is needed from them, in one place, whichever team is working | Shared record of communications and status, within visibility rules set by the owning function | Care experience |
| Resolved and prevented | Gets the outcome, and the same problem does not come back | Quality review, reporting, and root causes fed back to product | Reporting and analytics |

**Care as the customer experience**

Care has two meanings. Care the team is one operator on the platform. Care the customer experience is the merchant-facing layer: proactive and reactive, covering all communication from Checkout regardless of which team sent it. Work does not have to route through the Care team.

**Care owns:** the customer's view of status, actions and communications, all customer conversations on any case (including Checkout-initiated work), proactive and automated notifications, and the customer channels.

**Care owns as a team:** the SLAs for support contacts, like any other function owns its case types.

**Care does not own:** customer data (stays in systems of record), other functions' cases or SLAs, or visibility decisions.

**Rules**

1. **Everything is logged.** All customer communication is written to the shared record, whatever channel or team. Care can only show what the record holds.
2. **The owning function sets visibility.** Each case type has a setting: visible, status only, or hidden. Risk, Compliance or the case owner decides. The default is hidden. Care applies the setting and does not judge sensitivity. The same test applies to frontline and BPO agents: what an agent sees on screen is what could be said to the customer, so they see limited information and approved responses, not internal reasons.
3. **Care shows status, the owner owns the SLA.** The function that owns a case type, including the Care team for support contacts, is accountable for its response and resolution SLA. The case management layer tracks all of them. Care the experience is accountable for accuracy and timeliness of what customers see, on all work.
4. **Customers hear from Care.** Care owns customer communication on every case, whichever team's it is. There are two modes: a conversation hosted by Care for anything that needs a reply, and a visible automated notification for status, requests and outcomes. The owning function approves the wording and visibility and keeps the decision. Customer replies return to the owning case automatically.

**Illustrative visibility settings** (owners to confirm)

| Case type | Customer sees | Decided by |
|---|---|---|
| Support contact | Full thread and status | Care |
| Onboarding | Status and requests for information | Onboarding / Compliance |
| Fraud or screening review | Hidden, or "under review" only | Risk / Compliance |
| Dispute | Full thread and status | Disputes owner |

### 7. Customer-initiated and Checkout-initiated work

Both are the same case object on the same platform. They differ on dials that each work type sets.

| Dial | Customer-initiated (for example support) | Checkout-initiated (for example onboarding checks, fraud and transaction alerts, periodic reviews) |
|---|---|---|
| Trigger | The customer asks | A rule, schedule or event creates the case, or we reach out first |
| Starting point | Free text to classify and link to a customer, sometimes unlinked | Structured data and evidence, always linked to a customer, sometimes two |
| Customer awareness | The customer knows it exists | Varies: hidden, status only, or visible with requests for information |
| Outcome | An answer or resolution | A decision or approval, which may trigger an action |
| SLA driver | Customer expectation | Regulatory deadline or internal risk window |
| Volume driver | Customer behaviour | Rules and thresholds we set |
| Specialist tools | Some | Heavy |

**How the split is reconciled**

1. **One intake, one case object.** Origin is an attribute set at creation, not a separate system or queue model.
2. **Work type sets the dials.** Each work type declares who can start it, how much the customer sees, and what outcome it produces. The owning function decides, consistent with the visibility rule.
3. **Linked cases cross the boundary.** When Checkout-initiated work needs the customer (a request for information in onboarding or a periodic review), it opens a customer-facing thread linked to the case, which Care hosts, or sends a visible automated notification when no reply is needed. The owning function keeps the decision and approves the wording. When a customer-initiated contact needs another team (an engineering bug to log, a funds delivery issue from Treasury to the merchant's bank account, a reported fraud), Care raises a linked case for the owning function. The customer thread stays with Care. The linked case's visibility is set by its type: status updates to the customer for most, hidden (silent handoff) for sensitive ones such as fraud or screening. When the linked case resolves, the customer thread updates automatically.
4. **The Care experience covers both, to different depths.** Customer-initiated work is visible by default within the rules. Checkout-initiated work is hidden by default and surfaces only what its owner approves: status, requests, outcomes. Proactive contact is itself Checkout-initiated work with a customer-facing outcome.
5. **Reporting is by work type and origin.** Volumes and efficiency are comparable, and a rule change that floods alerts shows up as volume.

### 8. Design principles

1. **Organise around the customer, not the ticket.** One view across all functions.
2. **One case object, typed work types.** Support, risk and compliance work share one lifecycle. Each work type enforces its own required data.
3. **Work finds the person.** Work is pushed by skills, capacity, priority and SLA risk. Queues do not rely on agents pulling.
4. **Enforce access in the platform.** Permissions and visibility are built in, scoped by role and partner, and set by the owning function.
5. **Every action is auditable.** Who, what, why, for humans and AI alike. Approval is its own recorded event.
6. **One record, whatever the channel.** All customer communication is logged. Internal teams and customers see the same history at the level their role allows.
7. **Keep regulatory choices reversible.** Rules are still changing, so no rebuilds.
8. **Own the work, integrate the data.** The platform is the case system of record. Ledgers, payments and customer data stay in their systems of record.
9. **AI first, humans for judgment.** Tasks are assigned to AI or a human by type and risk: data retrieval and light analysis can go to AI, human judgement or human-in-the-loop for complex or high-risk work. AI and human agents use the same data and sources.
10. **Every action links to its case.** Work is done in the right tool, and each action links to the originating case, which keeps the audit trail whole and measures handle time. Approval is recorded on the case and fires downstream workflows (refund, notification, ledger update).
11. **Design beyond the vendor.** The design is written as capabilities, so it holds whichever platform runs it. Plain is the chosen platform.
12. **Prove it on the hardest case.** Ray L2, ISV onboarding, fraud alert.
13. **Measure every function.** Contact rate and cost per contact, plus cycle time for risk and compliance.
14. **Report from the record.** Regulatory, efficiency and volume reporting all come from the same case record. No parallel spreadsheets, and a work type's required fields are what make its reporting reliable.
15. **Standard before bespoke.** Operations deploys one standard pattern for every team: an orchestration layer to call, enrich and complete work items. A team-specific problem is solved by configuring the standard (work types, tools, rules), not by building in silo. This gives every team operating parity.
16. **One portal for people, interfaces for AI.** Human agents work in one back office portal (UI), which gives control of permissions, traceability and audit, and fewer tool switches. AI agents read the same data and take the same actions through interfaces (APIs and MCPs). Specialist tools do not necessarily stay: their functionality is consolidated into the portal where possible, and where it is not, the tool is linked to the case. Domain teams contribute and own their relevant parts of the tooling stack and interfaces under a contribution model: the platform sets the standard (permissions, audit, case linking, design) and owns the portal shell, the orchestration layer and the case.
17. **Launch with operations built in.** Every product launch or change is onboarded into the ops stack before its first case, not discovered from live work. Product onboarding configures the work types, workflows, orchestration rules and portal for the product, so the stack stays current as products ship. See the Product onboarding capability in section 5.

### 9. Plan

Operations Platform Design is scoped to Q4 2026 in `2026 deliverables.md`. The milestones below are proposed, and the Ray external launch date is an unconfirmed decision point. Ray is greenfield, so there is no migration. Plain is the platform for these milestones. The vendor decision is made before this plan is presented.

| Milestone | Timing | What happens |
|---|---|---|
| Discover and design | Q4 2026 | Work types from SOPs. Vision and system design signed off by Support, Risk and Compliance. Sequence of teams moving to Plain for Acquiring support drafted and shared by end Q4 2026 |
| Ray friends and family | Dec 2026 | Care team handles Consumer support on Plain |
| Ray external launch | Q1 or Q2 2027 (date unconfirmed) | Care team plus Fraud and Disputes Ops on Plain |
| Acquiring support | By end H1 2027 | Care team handles Acquiring support on Plain |
| Other teams, tools and AI agents | From H2 2027 | Teams move to Plain for Acquiring support in the agreed sequence. Tools, shared services and AI agent build across teams: TBC in H2 2027 scoping |

### 9a. Prioritising teams

Section 9 fixes the sequence to the end of H1 2027: design, Ray, then Care for Acquiring support. Beyond that, the order teams move is set by applying the model below to the data cards from section 1, not decided in advance.

**Score.** Each team is scored 1 to 5 on five criteria. The weights are proposed and need agreement from Support, Risk and Compliance.

| Criterion | Weight | Measured by |
|---|---|---|
| Value | 30% | Monthly cases x handle time x share that can be automated or AI-assisted |
| Pain and exposure | 20% | Handoff rate, CSAT at handoff, regulatory deadlines, cases closed without a recorded outcome |
| Growth pressure | 20% | Volume growth over the next 12 to 24 months, and its driver |
| Readiness | 15% | Case system today, work types defined, named sponsor, data access |
| Complexity (inverse) | 15% | Tools to consolidate, Salesforce coupling, regulated work |

**Handoff pairs.** CSAT drops when work moves from Care to another team, so a team that receives many Care handoffs moves in the same wave as the Care flow into it.

**Gates.** A team moves only when its work types are defined, a sponsor is named and the previous team's guardrails hold (section 10).

**Build order, for every wave.**
1. Case system, work types, intake and permissions.
2. Shared services and customer context, built once and reused by each team.
3. Per team: the minimum is one case system plus one tool. Then the orchestration connector for the team's top one or two tools, then portal modules ranked by tool usage and tools per ticket.
4. AI automation, only on simple, high-volume work types that have an interface.

**Teams to score** (not ranked): the 16 teams in section 3. Care is already sequenced in section 9. AML periodic reviews is the team the head of Risk Operations proposes first (intake 100-150 rising to about 450 a month).

### 10. Measures

- North stars: contact rate and cost per contact. Guardrail: Merchant CSAT.
- Added for operations: cycle time for Risk and Compliance work, work volumes and handling time by function.
- Work mix: % of completed work by who did it, by work type and function. Read from the case record (assignment and action log). Three categories: **automated** (AI completed every step with no human touch, the same as AI resolution rate, and a case is still created for audit), **AI-assisted** (AI retrieved, analysed or drafted and a human approved or decided), **human only**. Drives cost per contact: Fin costs $0.90 per resolution against about $40 per human contact. Today, Care only: Fin handles about 25% of volume with an overall resolution rate of 16-18% (2026-09-08, `01-knowledge-base/products/fin-ai-agent.md`). The split between AI-assisted and human only is not measured, and Risk and Compliance work has no baseline because Fin covers Care support only. Targets are set per work type by risk and by customer segment, not as one company-wide percentage: high-risk and regulated work stays human-in-the-loop. Paired with a quality guardrail so the mix cannot improve at the cost of service: QA score on AI-handled work, reopen rate, human override rate and escalation rate.
- Impact to metric: customer impacts (repeat themselves, mixed answers, bounced between teams, slow decisions) map to Merchant CSAT and contact rate. Cost does not fall with scale maps to cost per contact. Regulatory and risk exposure map to SLA performance and cycle time for Risk and Compliance work. Quality blind spots map to QA coverage.
- Quality: QA coverage. Target 100% of cases. Care today under 1% (single observation, see section 1). The 100% is a target: AI scoring is near go live per the Knowledge Manager.
- Insight and prevention (Reflex, extended beyond Care, proposed): at least 95% of cases attributed to a work type and root-cause area, and to a product where one applies (Reflex health metric today), % of top work drivers with a fix delivered, and work volume reduction after a fix (Reflex north star), reported for Risk and Compliance work as well as Care.

**Phase measures (proposed).** The outcome measures above only move once teams are on the platform. Each phase of the plan in section 9 has its own measures. Targets for all of them are set from the Q4 baselines, which are the first measure.

| Phase | Measures |
|---|---|
| Baseline (Q4 2026, Discover and design) | Work types inventoried: % of SOP work types. Baselines captured: cost per case, handle time, cycle time, CSAT by team. Executive sponsor named and XFN group released |
| Build (Dec 2026, Ray friends and family) | Work types live vs plan. Cases created through structured intake, not email: %. Actions linked to a case: % (audit completeness). Fin involvement rate and AI resolution rate. Work mix (automated, AI-assisted, human only) reported for every live work type. Launches onboarded into the ops stack before first case: % |
| Migrate (H1 2027, Acquiring support) | Care volume on the platform vs legacy: %. Tools per ticket (about 5 today). QA coverage (under 1% today, target 100%). Active agents working in the platform: %. Work mix for Care vs the Q4 baseline (16-18% automated today) |
| Migrate and retire (from H2 2027, other teams) | Teams on the platform: n of total. Case systems and email inboxes: 2 plus inboxes to one case system. Retool apps retired (20+ in Care alone). CSAT drop on cross-team handoff (20% today). Time to compile a complaints report (hours today) |

**Migration guardrails, checked at every cutover:** Merchant CSAT (reported by segment), SLA attainment, backlog age and handle time stay at or better than the team's Q4 baseline. The next team moves only when the previous team's guardrails hold.

Open: baselines do not exist yet for agent time lost to tool-switching, cost of a cross-team handoff, effort to produce a regulatory report, onboarding and review cycle times against target, or the AI-assisted vs human-only split of work (see "Not yet quantified" in section 1). Capturing them is a Design-phase task.

### 11. The ask

1. **Executive sponsor:** one accountable executive named.
2. **XFN group:** Support, Risk and Compliance leads released, each with a product and an operations lead.
3. **Care scope:** Care owns the customer-facing layer. This absorbs the Merchant Ticket Submission and Visibility and Support-Based Proactive Notifications deliverables. Confirm with the VP of Product and Director of Operations.

Vision, design and the team sequence due by end of Q4 2026 (see section 9).

### 12. Open points for the group

- Naming: platform is "operations platform" (15 Sep vision meeting), the customer-facing layer is "Care".
- Boundary cases: onboarding (Salesforce today) and transaction monitoring.
- Salesforce and commercial: commercial initiates much risk and configuration work from Salesforce (MCRs, net new onboarding, underwriting, then configuration in CAT) and treats it as its record of truth. Open: which records stay in Salesforce and which work items move to the case system, how commercial-initiated work creates a case, and how onboarding is redesigned (merchants receive a 46-page spreadsheet today, and quote to cash is being built outside Salesforce). Discovery needs the Salesforce owners and their plans. Raised in the Ops review, 2026-10-07.
- Visibility of risk and compliance cases to customers: Compliance decision.
- Principle 1 versus 4: who sees what across a single customer view.
- Scope of Care: the proactive and reactive customer experience absorbs the Merchant Ticket Submission and Visibility and Support-Based Proactive Notifications deliverables. Confirm with VP of Product and Director of Operations.
- Care accountability: is Care also accountable for the customer's overall experience of other functions' work (for example a slow onboarding), beyond status accuracy and timeliness?
- Care owns the presentation of Customer 360, not the underlying data.
- Workspaces: one permissioned workspace for all work, or separate workspaces for sensitive work types.
- Unlinked contacts: how cases with no identifiable customer (consumer chargeback complaints, spam) are created and handled.
- Regulatory reporting: which reports and evidence each regulator requires, by work type (Compliance to list), and the retention and format each needs.
- Metric definitions: one definition of work volume, handling time and SLA performance that holds across Support, Risk and Compliance, so teams are comparable. Queue SLA performance is a staffing and planning measure, so agent metrics use individual speed and quality, not queue SLO.
- Reporting data home: reports built inside the platform or from the data warehouse, and which is the source of truth for regulatory submissions.
- Migration path to one case system of record: how Salesforce and Zendesk work moves into it, in what order and at what cost. Teams on email inboxes have no case record to migrate, so they start from intake and need work types defined first. Options from the back office steerco draft include Care as the first triage point with downstream routing and sync-back as a bridge, and starting greenfield with Ray. Principle 8 now fixes the destination as one system.
- Inbound customer email: team inboxes are retired and customers who need email use one unified address, which enters as a structured request (email forms). Top-tier merchants who email their account manager are served by a dedicated account manager channel for submitting work, or by account managers resolving it themselves. Open: how an email sent outside the form is handled (redirect to the form or Dashboard, or convert into a structured request).
- Commercial and account manager communication: visibility is needed both ways. Ops needs to see what commercial told the merchant (fee reductions, goodwill), and commercial needs to see what Ops communicated. Part of it is a process and accountability gap (commercial sign-offs and processes), not only tooling. Open: how account manager conversations in Slack, WhatsApp and email are logged to the case, and how sign-offs are built into the work type.
- Portal and shared service layer: the direction is one back office portal for human agents (UI) and interfaces for AI agents, over the same data (customer data, transactions, funds, communications record, KYC/KYB status, periodic reviews, action history), with domain teams owning the UI and interface layers. Direction: the functionality of specialist tools (Sardine, Fircosoft, RA Tool, Retool apps) is consolidated into the unified portal where possible. Open: the contribution model (what domain teams own, the UI contract, interface contract and permissions they build to), and for each specialist tool whether its functionality is rebuilt in the portal, surfaced through an interface, or the tool is retained and linked to the case. This sets how far tools per ticket and the 20+ Retool apps can fall.
- Human escalation by customer segment: the customer agent escalates to a human only within controls set per segment. Direction: human support is viable for Enterprise (which has a white-glove route through account managers today), but not for SMB or Consumer at high volumes (70-80% of 2030 Care contacts are consumer). Open: the policy for each segment, the exceptions (for example regulated work, high-risk work and vulnerable customers, and Consumer Duty obligations through open banking in 2027), what the customer sees when a human is not available, and the capacity sized for the humans that remain. Also decide how Merchant CSAT and the work mix targets are reported by segment so a high automation rate does not hide a poor SMB or Consumer experience. Raised in design review, 2026-10-08.
- Outbound requests to platform merchants: requests for information to sub-merchants go through the platform by webhook, with no visibility of when they were sent or whether chasers ran. Open: the responsibilities platforms take on for relaying and chasing, how platforms are given an incentive to comply, and how the case system sees the request and the response. At 20 ISVs with 100,000 merchants each, the inbound path is better thought through than the outbound one. Raised by the head of Risk Operations, 2026-10-13.
- Secure information requests: there is no company-approved way to ask a merchant for sensitive information, no single secure upload place, and no scanning of what is sent. Open: who owns the secure upload route, which document types it covers first, and the rule for what may still arrive by email.
- Sequence after Care: Care moves to Plain by end H1 2027 and other teams from H2 2027. The head of Risk Operations proposes starting team by team with periodic reviews, because intake rises from 100-150 to about 450 cases a month and the work touches every part of the cycle (high reward, high complexity). The method is in section 9a. Open: agreeing the weights, the case volume and handle time data it needs, and whether Ray and other teams join the same wave.
- Capacity and ownership: the work needs configuration built for every team to operate its workflows, more engineers than are in the team today (hiring lags), and investment from Operations as well as Product. It is an EP-level project, not a Care one. The head of Risk Operations asks for someone from Product to spend time with each team end to end, because assumptions about what other teams do are a common gap.
- Product onboarding and operational maturity: product teams onboard onto the platform with operational requirements as standard (self-serve, APIs), so Ops owns orchestration and the resolution path, not the means to resolve. MCAP with Hive is agreed (2026-08-19) as the mandatory product-to-ops intake with domain-specific documentation and formal rejection rights, in pilot now. Open: getting each ops domain's required inputs embedded in MCAP while the pilot is open (Charlie to brief the MCAP owner), a readiness check that derives stack configuration from the product information, the V1 scope (new products, changes, deprecations, regulatory changes), tiering so a minor change does not get heavyweight intake, advance notice and sandbox access for training, who owns the governance (EP), and Ray as the worst case for impact assessment. Needs product team commitment.
- Reflex across Operations: Reflex is positioned as the company-wide customer insight layer and merges sources by a data contract (merchant ID plus the product catalogue entry). Open: (1) required fields on every work type must include customer ID, work area and cross-team involvement (which Reflex lists as a missing cost dimension), plus a root-cause category such as product, process, policy, knowledge, tooling or rule. Product catalogue ID is required only where the work type relates to a product, because some work types do not, so the model needs flexibility. Fields are set at work type design, and for product-related work at product onboarding. (2) Reflex engineering was scoped for deployment and maintenance, not for onboarding new sources, so each new work type's clustering and evals need separate funding. (3) What a root cause means for Risk and Compliance work (for example alert rule tuning) and who acts on it. (4) The 2026 Reflex deliverable scopes Care contact data, so extending it to all Operations work is not a named deliverable yet. Confirm against `2026 deliverables.md` before presenting.
- Standard vs bespoke: who approves an exception when a team needs a team-specific build, and how existing team-specific tools (20+ Retool apps in Care alone) move onto the standard pattern. Raised by an Ops leader in review.
- Quality standards: one definition of quality control versus quality assurance across teams (not clearly delineated today), who owns standards and calibration, and the sampling approach for human review.
- Exceptions to Care-owned communication: whether any regulated notices must come directly from Compliance or Risk, and how Care is resourced (staff, AI, BPO) for the extra conversations that Checkout-initiated work creates.
- Escalation rules: which contact types open a linked case, and who decides. Proposed: the owning function defines the trigger and required fields for its destination (Engineering, Treasury, Risk, Compliance, Disputes and others), Care (agent or AI) raises the case, and the owner accepts, reroutes or rejects it. Needs the list of destinations, their triggers, and which are silent handoffs.
- Checkout-initiated volume: how much of this work exists today by work type, since the Care experience, routing and reporting are sized on it. No figure yet. Head of Risk Operations: the vast majority of their teams' work is Checkout-initiated, not customer-initiated.
- Frontline visibility: which limited information and approved responses frontline and BPO agents see for sensitive work types.

## Part 2: Story spine (COO and C-suite)

**Governing thought.** Operations cannot absorb up to 36x more Care contacts, a consumer business and regulator scrutiny on tooling built around products. Sponsor one operations platform, designed jointly by Support, Risk and Compliance with Care as the customer layer, and prove it on Ray from December 2026.

**SCQA**
- Situation: Operations is Support, Risk and Compliance teams, about 300 agents [NEEDS DATA: confirm headcount, section 3 has "300?"], each working in its own tools. Account managers hold the experience together for white-glove customers.
- Complication: Care contacts grow up to 36x by 2030, 79% consumer. Ray launches in Dec 2026 and Zendesk renews in June 2027. The same fragmentation at that volume means more customers repeating themselves, bouncing between teams and waiting, plus regulatory exposure.
- Question: How does Operations run at that scale without per-product tooling?
- Answer: One operations platform. A case system creates and distributes work, one portal and interfaces complete it, and Care is the customer layer.

**Key line** (why, then what, then how)
1. Tooling built around products already fails customers and Checkout, and volume multiplies the cost (slides 2 to 4)
   - Customers repeat themselves, are bounced between teams, and CSAT drops 20% at handoff
   - Checkout cost does not fall with scale and regulatory exposure rises
   - Care contacts grow up to 36x by 2030, with Ray and the Zendesk renewal as the near-term windows
   - The cause is 30+ tools, two case systems and team email inboxes with no shared view
2. One platform with one standard pattern for every team fixes the cause (slides 5 to 8)
   - Work enters through one front door, team inboxes are retired, and every product launch configures the ops stack before its first case
   - The case system creates and distributes work. The portal and interfaces complete it. Work can be done in any tool, and every outcome writes back to the case
   - Customers ask once and see every step, because Care is the layer on top
   - Quality and regulatory evidence come from one record, at 100% coverage
   - Reflex reads the same record to find root causes across all work and route fixes to owners, which feeds the next product launch
   - Domain teams build to the standard (principles 15 and 16), not in silo
3. Ray proves the design, Acquiring support proves the migration, and measures with guardrails govern each step (slides 9 to 11)
   - Sequence from Dec 2026 to H2 2027
   - Phase measures, with Merchant CSAT guarding every cutover
   - Three trade-offs, each with a mitigation
4. Ask: three decisions today (slide 12)

**Title test.** The titles alone read as the story:

| # | Title |
|---|---|
| 1 | Sponsor one operations platform with Care as the customer experience |
| 2 | Tooling built around products fails customers and drives Checkout cost and risk |
| 3 | Care contacts grow 36x by 2030, multiplying every fragmentation cost |
| 4 | Work runs across 30+ tools, two case systems and email inboxes with no shared view of the customer |
| 5 | One case system, one portal and a Care layer replace per-product tooling |
| 6 | Every request becomes one case, goes to AI or a human, and every action is written back |
| 7 | The customer asks once and sees every step |
| 8 | Quality review covers 100% of cases, up from under 1% in Care today |
| 9 | Ray proves the design, Acquiring support proves the migration, other teams follow |
| 10 | Phase measures prove progress, and Merchant CSAT guards every cutover |
| 11 | Three trade-offs come with the platform, each with a named mitigation |
| 12 | Approve three decisions today so design starts in Q4 2026 |

**New slides 4b, 10, 11, A12, A13 and A14 (ghost, to be defined in the slide format by `/slide-content`).**

| # | Evidence needed | Visual | Status |
|---|---|---|---|
| 10 | Phase measures and work mix from section 10: baseline, build, migrate, migrate and retire. Guardrails: Merchant CSAT, SLA attainment, backlog age, handle time at or better than Q4 baseline. North stars: contact rate, cost per contact. Current Care work mix: Fin about 25% of volume, 16-18% resolved | 4-column phase table with a guardrail strip beneath | Measures in hand. Baselines: [NEEDS DATA: Q4 baselines for cost per case, handle time, cycle time, CSAT by team] |
| 4b | Title: Good means customers ask once, agents work in one place, and Checkout scales without headcount. Evidence: the vision table in section 1a, each line answering a "poor" from slide 2. Content: three columns (Customers, Human agents, Checkout) with the vision line and three outcomes each. Sits between slide 4 (today) and slide 5 (the platform) so the solution answers a stated outcome | 3-column card layout, one vision line per column | Direction in hand. [NEEDS DATA: repeat-request rate, share of cases created by hand, agent time lost to tool-switching] |
| A14 | Title: Human escalation is set by customer segment, so Enterprise keeps human support and SMB and Consumer scale on the customer agent. Evidence: 70-80% of 2030 Care contacts are consumer (`01-knowledge-base/metrics/contact forecasting.md`), Enterprise has a white-glove route through account managers today, Fin handles about 25% of Care volume with 16-18% resolved (2026-09-08), the segment policy is the open point in section 12. Content: the path (self-serve, customer agent, human) with the escalation rule per segment, and what the customer gets when no human is available | 3-column segment table: Enterprise, SMB, Consumer, with human support, escalation rule and fallback experience | Direction in hand. [NEEDS DATA: policy and exceptions per segment, CSAT by segment baseline, capacity for the humans that remain, what SMB and Consumer customers see when no human is available] |
| A13 | Reflex across all Operations work: one case record lets Reflex find root causes for Support, Risk and Compliance together. Evidence: Reflex scope beyond Care (2026-08-20), the product catalogue plus merchant ID as the join key for product-related work (other work reports by work area and root-cause category), metrics (95% attribution, fix coverage, volume reduction after fix). Loop: product onboarding configures tags, work generates records, Reflex returns root causes to product and process owners | Closed loop: launch, work, record, Reflex, fix, next launch | Reflex facts in hand. [NEEDS DATA: Risk and Compliance root-cause use cases, funding for new sources, deliverable mapping] |
| A12 | Product onboarding: why every launch must configure the ops stack before its first case. Stage 0 from `01-knowledge-base/strategy/care-product-model.md` extended to Operations. Evidence: 150+ initiatives at 2027 planning, several shipped with no Care assessment (BlueEMI, Ray, eFX, Interest). Mechanism: MCAP and Hive gate with rejection rights, readiness check, configures work types, workflows, orchestration rules, portal modules, permissions, knowledge, reporting tags. Measure: % of launches onboarded before first case | Horizontal flow: launch registered, readiness check, stack configured, first case | Evidence in hand. [NEEDS DATA: Ops domain required inputs, V1 scope] |
| 11 | Trade-offs: (1) migration effort and cost: two case systems and team email inboxes move, commercial keeps Salesforce as its record of truth and the boundary is open (A11). (2) Domain teams must own UI and interface layers, take on the standard and meet operational requirements at product launch (principle 17), which needs product team and EP commitment, with an exception process still to design. (3) Care takes on extra conversations from Checkout-initiated work, resourcing open | 3-card grid: trade-off, mitigation, owner | Assumption. [NEEDS DATA: migration cost and sequence, product team commitment] |

Structure: 12 core slides, an appendix divider and 11 appendix slides. Ask first, then the impact on customers and Checkout, then urgency, then the before and after stacks as the centrepiece, then how work flows through the platform, then the customer journey, the control story, the plan, the measures, the trade-offs and the decisions. Send a one-page pre-read (ask, the customer and Checkout impact lines, three decisions) ahead of the meeting. Every slide from 2 onwards carries a one-line "What the customer sees" footer strip so the Care experience runs through the story.

Each slide is defined once: title, layout, exact on-slide content, and notes. "Draws from" names the Part 1 section that holds the facts. Notes are for the presenter and are not rendered. Slide content follows the rules for Gemini rendering: layout keyword, fragments only, max 3-4 items per card or tile, max 8 words per item, bold lead-ins, numbers sourced.

### Gemini prompt template

Use once per slide. Paste the slide's title, layout and content from below. For the overview, list all slides' titles and layouts with the global constraints.

```text
Role: Expert Google Slides designer.
Task: Create one slide for the Operations Platform vision.
Audience: COO and C-suite | Tone: direct, minimal
Slide title: "[TITLE]"
Layout: [LAYOUT]
Content:
[CONTENT]

Constraints: Use only the text above, verbatim. Fragment grammar, no full sentences, no periods. Max 8 words per item excluding lead-in. Bold lead-ins. No added statistics, taglines, or intro/outro text. Clean, minimal, consistent spacing. Same fonts, colours and spacing as every other slide in the deck. [Visual: as stated, otherwise none]
```

### Core slides

**Slide 1. Sponsor one operations platform with Care as the customer experience**
Draws from: sections 3 (defining thread), 9, 11.
Layout: 3-Card Grid. Three equal cards, bold header, 1-3 fragments each.

Content:
- Card 1, The problem
  - Built for products: not customers
  - Volume: Care contacts up to 36x by 2030
  - Customers: bounced between teams, CSAT down 20%
- Card 2, The platform
  - One case system: Support, Risk, Compliance
  - One portal for people, interfaces for AI
  - Care: one place to ask and track
  - Proven first: Ray, Dec 2026
- Card 3, The ask
  - Executive sponsor: one accountable owner
  - XFN group: released, design by end Q4 2026
  - Care scope: owns customer-facing layer

Notes: Open by reading the defining thread from section 3 aloud. The cards read problem, answer, ask, so this slide is also the executive summary.

**Slide 2. Tooling built around products fails customers and drives Checkout cost and risk**
Draws from: section 1 (problem statement and Impact).
Layout: 2-Column Split. Left vs right, parallel structure, equal item count.

Content:
- Left header, Customers
  - Repeat themselves: teams can't see the same data
  - Mixed answers: differs by team
  - Bounced between teams: CSAT down 20%
- Right header, Checkout
  - Cost: does not fall with scale
  - Regulatory exposure: missed SLAs, slow reports
  - Quality blind spots: QA at very low levels
- Footer strip: Customer sees: repeated questions, mixed answers

Notes: Lead with the hero finding in section 1: operations is built around products, not customers. This slide is the "so what"; the cause (tools, systems) comes on slide 4. If the other customer impacts cannot be sourced, lead with the Checkout column. Ties to Merchant CSAT and cost per contact. If asked for a story: Care messaged a merchant about goodwill remediation after commercial had already given a fee reduction, because commercial and account manager conversations sit in Slack, WhatsApp and email out of view (Ops review, 2026-10-07). [NEEDS DATA: add the period and method for the 20% (Care CSAT data). "QA at very low levels" is a single observation, Care only (under 1% per section 1).]

**Slide 3. Care contacts grow 36x by 2030, multiplying every fragmentation cost**
Draws from: section 2.
Layout: Big Number Hero. Dominant stat, one-line subtitle, 3-column sub-stat row.

Content:
- Hero stat: 36x
- Subtitle: Same fragmentation at 36x volume: 60,049 to 2,154,799 Care contacts
- Sub-stat 1: 79% | of 2030 contacts are consumer
- Sub-stat 2: End Dec 2026 | Ray internal launch
- Sub-stat 3: Jun 2027 | Zendesk contract renewal
- Footer strip: Customer sees: a consumer base that will not wait

Notes: Say that the impacts on slide 2 multiply with volume, and that figures are Care contacts only, not total Ops volume. State the renewal as the window that the Plain decision uses. Plain is named on slide 9 as already decided. Ties to contact rate. Risk Operations has its own growth point: periodic review intake rises from 100-150 to about 450 cases a month next year, at one to two days a case (head of Risk Operations, single source).

**Slide 4. Work runs across 30+ tools, two case systems and email inboxes with no shared view of the customer**
Draws from: section 5 (stack, Today column), section 4.
Layout: 4-Tile Matrix. 2x2, header plus 1-2 fragments per tile. Small muted label "Today" above the title. Tile order: top-left Channels, top-right Case management, bottom-left Tooling and AI, bottom-right Data and reporting. Same positions as slide 5.

Content:
- Tile 1, Channels
  - Unstructured: email, webform, chat, social
  - Team inboxes: each team has its own
  - Internal work: email and Slack
- Tile 2, Case management
  - Salesforce: several teams
  - Zendesk: Care only
  - Email inboxes: some teams, no case system
- Tile 3, Tooling and AI
  - 30+ tools: 20+ Retool apps in Care
  - About 5 tools: on one Care ticket
- Tile 4, Data and reporting
  - Knowledge: 8 places
  - Complaints reports: hours to collate
- Callout (small, under the matrix): Care is a team inside two tiles
- Footer strip: Customer sees: repeated questions, mixed answers

Notes: This is the cause behind the slide 2 impacts. Key line to say: channels are how requests arrive, case management is the record of work, tooling is the screens people use, AI agents do work for people (section 4). Arrows between teams in the case management tile are email and Slack, labelled "CSAT drops 20% on cross-team handoff". An email to a team inbox may land in Salesforce or a Gmail account. Care is the only team with an alternative to email. Validate with Ops leads (tools per team, which systems hold which work, which teams use inboxes and at what volume).

**Slide 5. One case system, one portal and a Care layer replace per-product tooling**
Draws from: section 5 (stack, Vision column and the capabilities table).
Layout: 4-Tile Matrix. 2x2, header plus 1-2 fragments per tile, identical tile positions and order to slide 4. Small muted label "Vision" above the title.

Content:
- Tile 1, Channels
  - Customers: one front door, inboxes retired
  - Account managers: dedicated channel to submit work
  - Internal work: forms and triggers, not email
- Tile 2, Case management
  - One system: Support, Risk, Compliance
  - Full audit: who did what, SLAs
  - Work done elsewhere: outcome written back
- Tile 3, Tooling and AI
  - One portal for people, interfaces for AI
  - Domain teams own UI and interfaces
  - AI or human: assigned by task and risk
  - AI prefills: from related closed cases
- Tile 4, Data and reporting
  - Shared services: one data layer
  - Reporting: regulatory, efficiency, volume
  - Reflex: root causes across all work
- Callout (small, under the matrix): Product onboarding configures all four tiles before launch
- Visual: one vertical band labelled "Care experience" along the left edge, spanning the Channels tile and the customer view of status. No other imagery.
- Footer strip: Customer sees: one place for every step

Notes: Same layout as slide 4 so the audience can flip between them. Each slide 2 impact has a named fix in the "Addressed by" column of section 1. The eleven capabilities map onto the tiles through the capabilities table in section 5. Slide 6 shows how work moves through it. The diagram shows capabilities, not systems: the migration path to one case system of record is an open point (appendix slide A11). Commercial keeps Salesforce as its record of truth, and commercial-initiated work creates cases through structured intake (section 12). Top-tier merchants will keep emailing their account manager, so the account manager channel is part of the front door. Product onboarding (Stage 0, principle 17) is what keeps the stack current: each launch configures work types, workflows, orchestration rules and portal modules before the first case, gated by MCAP.

**Slide 6. Every request becomes one case, goes to AI or a human, and every action is written back**
Draws from: section 5 (One front door, Case system of record, Orchestration layer), section 8 (principles 9 and 10).
Layout: Horizontal Linear Timeline. 4 steps, label above, fragment below.

Content:
- Step 1, One front door: Requests, triggers and launches create cases
- Step 2, Case system of record: Creates, distributes and tracks work
- Step 3, AI or human: Assigned by task type and risk
- Step 4, Portal and interfaces: Work completed, written back to case
- Footer strip: Customer sees: status drawn from one record
- Visual: simple connected steps, no icons

Notes: This is the operating mechanism behind the customer journey on the next slide. Example for step 3: data retrieval and light analysis can go to AI, while human judgement or human-in-the-loop handles complex or high-risk work. AI and human agents use the same data and sources. Step 4: humans complete work in one portal opened from the case, AI agents through interfaces. Domain teams own the UI and interface layers to one standard pattern (principles 15 and 16). Work need not happen in the case system: a task can run in a specialist tool and the outcome is always written back. AI prefills from related recently closed cases so a check already done by another team is not repeated (a Risk example from the Ops review). Every action written back keeps the audit trail whole and lets handle time and work mix be measured on the case. Self-serve is the customer's own step, not back stage. Where it is not available, the customer agent acts first for customer-initiated work (Fin today). It solves queries through the orchestration layer with no human involved, a case is still created for audit, and anything it cannot solve escalates to a human agent, within controls set by customer segment (Enterprise open, SMB and Consumer limited by policy). Domain agents take Checkout-initiated and escalated tasks. Inbound customer email is an open point (section 12).

**Slide 7. The customer asks once and sees every step**
Draws from: section 6 (customer journey).
Layout: Horizontal Linear Timeline. 5 steps, label above, fragment below.

Content:
- Step 1, Ask or be told: Any channel, or we reach out first
- Step 2, Be known: No repeating themselves
- Step 3, Get handled: Customer agent for routine, experts for complex
- Step 4, Stay informed: Status in one place, any team
- Step 5, Resolved: Problem does not come back
- Footer strip: Customer sees: one experience, whichever team works
- Visual: simple connected steps, no icons

Notes: Section 6 has six steps. "Get picked up" and "Get it handled" are merged here to meet the 5-step limit. Show the customer's view above the line and the platform below it when presenting.

**Slide 8. Quality review covers 100% of cases, up from under 1% in Care today**
Draws from: sections 1 (Impact), 5 (Control and quality, Reporting and analytics), 6 (Care rules 1 and 2), 10.
Layout: Big Number Hero. Dominant stat, one-line subtitle, 3-column sub-stat row.

Content:
- Hero stat: 100%
- Subtitle: Case quality review coverage target, Care today under 1%
- Sub-stat 1: Owner sets | visibility, default hidden
- Sub-stat 2: One record | one evidence set for regulators
- Sub-stat 3: Measured | contact rate, cost per contact, CSAT
- Footer strip: Customer sees: consistent, checked answers

Notes: Risk and Compliance set the rules and the platform enforces them. This closes the regulatory exposure, risk exposure and quality blind spots from slide 2. Handle time is measured because work done in tools links to its case (slide 6). Needs Risk and Compliance leadership pre-wired. [NEEDS DATA: "under 1%" is a single observation, Care only. The 100% is a target.]

**Slide 9. Ray proves the design, Acquiring support proves the migration, other teams follow**
Draws from: section 9.
Layout: Horizontal Linear Timeline. 4 steps, label above, fragment below. Connected chevrons, not a Gantt chart.

Content:
- Step 1, Dec 2026: Care Consumer support on Plain for Ray friends and family
- Step 2, Q1 or Q2 2027: Care plus Fraud and Disputes Ops on Plain for Ray external launch
- Step 3, End H1 2027: Care Acquiring support on Plain
- Step 4, H2 2027 onwards: Other teams move, tools and AI agents scoped
- Footer strip: Customer sees: Ray launches on the new model

Notes: Vision and design are signed off in Q4 2026, and the team sequence for Acquiring support is shared by end Q4 2026. The Ray external launch date is unconfirmed (Q1 or Q2 2027). Tools, shared services and AI agent build are TBC as part of H2 2027 scoping. Dates are proposed (section 9). Ties to the Zendesk renewal (June 2027) on slide 3. Ray is greenfield, so it proves the design, not the migration. Acquiring support is the migration proof, and the migration path is still open (A11). Say this before the audience asks.

**Slide 12. Approve three decisions today so design starts in Q4 2026**
Draws from: section 11.
Layout: 3-Card Grid. Three equal cards, bold header, 1-3 fragments each.

Content:
- Card 1, Executive sponsor: One accountable executive named
- Card 2, XFN group: Support, Risk, Compliance leads released
- Card 3, Care scope: Care owns customer-facing layer
- Footer strip: Customer sees: one experience, owned end to end

Notes: Confirm Care scope with the VP of Product and Director of Operations before the meeting.

### Appendix slides

**Appendix divider. Appendix**
Layout: Minimal Title. Title only, no bullets, no subtitle.

**Slide A1. Terms: how work arrives, is recorded and is done**
Draws from: section 4.
Layout: Before vs After Grid. Rows aligned across three columns: term with plain definition, today, vision. Column headers: Term, Today, Vision.

Content:
- Channels (how requests reach us) | Unstructured: email, webform, chat, Slack | Structured requests from every channel, internal work not by email
- Case management (case system of record) | Salesforce and Zendesk, separate queues | One case system of record
- Tooling (screens people act in) | 30+ tools, 20+ Retool apps in Care | One tool set, work links to the case
- AI agents (software that does work) | TBC | Assigned by task type, same data as humans

**Slide A2. Terms: who does the work and where it starts**
Draws from: section 4.
Layout: Before vs After Grid. Rows aligned across three columns: term with plain definition, today, vision. Column headers: Term, Today, Vision.

Content:
- Care team (Merchant Care, owns support SLAs) | One operator among many | Unchanged, one operator on the platform
- Care experience (what customers see, any team) | Does not exist as a layer | Customer-facing layer, whichever team works
- Customer-initiated work (customer asks) | Mostly Care, in two systems | Structured channels, visible within rules
- Checkout-initiated work (rule, event or outreach) | Spread across tools, often hidden | Same intake, owner sets visibility

**Slide A3. Capabilities: what they do (1 of 2)**
Draws from: section 5 (capabilities 1 to 8).
Layout: 3-Card Grid. Three equal cards, bold header, 2 fragments each.

Content:
- Card 1, Front door and Care
  - What: structured intake, one thread, status
  - Outcome: lower contact rate
- Card 2, Work, data and interfaces
  - What: case system, portal, orchestration, shared services
  - Outcome: faster handling, fewer handoffs
- Card 3, AI agents and knowledge
  - What: customer agent, domain agents, knowledge
  - Outcome: lower cost per contact

**Slide A4. Capabilities: what they do (2 of 2)**
Draws from: section 5 (capabilities 9 to 11).
Layout: 3-Card Grid. Three equal cards, bold header, 2 fragments each.

Content:
- Card 1, Control and quality
  - What: permissions, audit, QC, QA
  - Outcome: regulatory confidence, consistent quality
- Card 2, Reporting and insight
  - What: regulatory, efficiency, volume, Reflex
  - Outcome: regulatory confidence, root causes fixed
- Card 3, Product onboarding
  - What: stack configured before launch
  - Outcome: no launch surprises

**Slide A5. One case system of record gives four things**
Draws from: section 5 (Case system of record, Orchestration layer), section 8 (principles 5 and 10).
Layout: 4-Tile Matrix. 2x2, header plus 1-2 fragments per tile.

Content:
- Tile 1, Traceability
  - Every task: assigned and recorded
  - Tool work: links back to the case
- Tile 2, SLAs
  - One clock: across teams
  - Ageing and breach risk: visible
- Tile 3, Consistent experience
  - Same agent experience: any team
  - Humans and AI: one queue
- Tile 4, Audit
  - Who did what: and why
  - Handle time: measured per case

Notes: Case management is the case system of record, not a system of record for data. Ledgers, payments and customer data stay in their systems of record.

**Slide A6. Tasks go to AI or a human by type and risk**
Draws from: section 5 (Orchestration layer), section 8 (principle 9).
Layout: 2-Column Split. Left vs right, parallel structure, equal item count.

Content:
- Left header, AI agent
  - Data retrieval: lookups across sources
  - Light analysis: summaries and diagnosis
  - Routine actions: approved, low risk
  - Knowledge: answers from verified content
- Right header, Human
  - Judgement: complex scenarios
  - High risk: human in the loop
  - Approvals: refunds and reversals
  - Exceptions: anything AI cannot resolve
- Footer strip: Same data and sources for both

Notes: Examples, not a final split. Autonomy is set per task type by the owning function. The orchestration layer assigns the task and records who did it. Autonomous versus human-in-the-loop modes follow the Agent Consultant model (`01-knowledge-base/products/agent-consultant.md`).

**Slide A7. 30+ tools, 8 knowledge sources, unstructured channels**
Draws from: section 1.
Layout: 4-Tile Matrix. 2x2, header plus 1-2 fragments per tile.

Content:
- Tile 1, Case systems
  - Salesforce: several teams
  - Zendesk: Care only
  - Email inboxes: some teams, no case system
- Tile 2, Tools
  - 30+ tools: RA tool, CAT, Genesis, Sardine
  - About 5 tools: on one Care ticket
- Tile 3, Knowledge
  - 8 places: across 21 sub-functions
  - Search masks it: not in the workflow
- Tile 4, Channels
  - Unstructured: email, webform, chat, social
  - Internal requests: email and Slack

Notes: "About 5 tools" is a single shadowing observation. [NEEDS DATA: 30+ tools, see section 1.]

**Slide A8. 20% CSAT drop at handoffs, with no shared data**
Draws from: section 1.
Layout: 4-Tile Matrix. 2x2, header plus 1-2 fragments per tile.

Content:
- Tile 1, Handoffs
  - CSAT: down 20% Care to other Ops
  - Account managers: step in on cross-team work
- Tile 2, Visibility
  - Customer data: not shared across teams
  - Answers: differ by team
- Tile 3, Reporting
  - Complaints reports: hours to collate
  - Periodic reviews: re-ask data merchants gave
- Tile 4, Workarounds
  - IP onboarding: spreadsheet tracker, Gmail approvals
  - Transaction Monitoring: worked in Retool, synced on close

Notes: Proof behind the slide 2 impacts. Do not use the May 2024 underwriting case on a slide (section 1, verify with Risk). [NEEDS DATA: the 20% CSAT figure is Care CSAT data (add period and method); visibility and reporting rows are "Needs source"; workarounds are single observations.]

**Slide A9. Two origins, one case object**
Draws from: section 7.
Layout: 2-Column Split. Left vs right, parallel structure, equal item count.

Content:
- Left header, Customer-initiated (support)
  - Trigger: customer asks
  - Starts as: free text, to link
  - Awareness: customer knows it exists
  - Outcome: answer or resolution
- Right header, Checkout-initiated (checks, alerts)
  - Trigger: rule, schedule, event or outreach
  - Starts as: structured data, always linked
  - Awareness: hidden, status only or visible
  - Outcome: decision, may trigger action

Notes: SLA driver and volume driver also differ (section 7).

**Slide A10. Linked cases connect customers to owning teams**
Draws from: sections 7 (reconciliation rules 1 to 3), 6 (Care rule 4).
Layout: 4-Tile Matrix. 2x2, header plus 1-2 fragments per tile.

Content:
- Tile 1, One intake
  - One case object: origin set at creation
  - One queue model: no separate systems
- Tile 2, Work type sets dials
  - Owner decides: visibility and outcome
  - Default: hidden
- Tile 3, Linked cases
  - Care raises: case for owning team
  - Examples: engineering bug, Treasury funds delivery
- Tile 4, Care owns comms
  - Two modes: conversation or automated notification
  - Owner approves: wording and visibility

Notes: Care resourcing for the extra conversations is an open point.

**Slide A11. Four decisions still open**
Draws from: section 12.
Layout: 4-Tile Matrix. 2x2, header plus 1-2 fragments per tile.

Content:
- Tile 1, Migration path
  - To one system: from Salesforce, Zendesk, inboxes
  - Open: order, cost, Salesforce boundary, Ray first
- Tile 2, Escalation rules
  - Which contacts: open a linked case
  - Who decides: owner defines, Care raises
- Tile 3, Care resourcing
  - Extra conversations: staff, AI or BPO
  - Regulated notices: from Compliance or Risk
- Tile 4, Checkout-initiated volume
  - Size by work type: no figure yet
  - Drives: routing, reporting, Care capacity

Notes: Other open points stay in section 12 only.

### Gaps to fill before presenting

- Source and validate the section 1 items marked "Needs source": hours to collate complaints reports and the 30+ tool count lead the list. Add the period and method for the 20% CSAT figure (Care CSAT data). Still missing: handoffs per case, time lost to rework, cost of the agent base. The SOP breakdown can produce tool and handoff counts.
- Cost of the status quo and a sized benefit range (productivity per agent, BPO leverage). No verified figure exists yet.
- How regulatory and management reporting is produced today.
- Validate the today's-stack slide with Ops leads (tools per team, which systems hold which work).
- Pre-wire Risk and Compliance leadership on slide 8, and confirm the regulatory outputs with Compliance.
- Size Checkout-initiated work by work type. No figure yet. The head of Risk Operations says it is the vast majority of their teams' work. One data point exists: periodic review intake, 100-150 to about 450 cases a month.
- [NEEDS DATA] Ops domain required inputs for product onboarding. Each Ops domain (Merchant Care, Merchant Configuration, Risk Ops, Compliance) documents the specific inputs it needs from a product's scope or PRD, so everything downstream is derivable: work types and required fields, workflows and SLAs, orchestration rules (AI or human), portal modules and interfaces, permissions, knowledge, and reporting tags. Source: the ask from the 2026-08-19 product introduction session. Owners: the domain leads. Care's inputs exist in `01-knowledge-base/strategy/care-product-model.md` (Stage 0). Needed for slide A12, and to be fed into MCAP and Hive while the pilot is open. Also decide the V1 scope (new products, changes, deprecations, regulatory changes).

### Story review gaps (presentation-outline pass)

- No sized business case beyond the periodic review growth point (100-150 to about 450 cases a month). The ask has no cost of the status quo, no benefit range and no build cost, which is the first thing a COO tests. Slides 10 and 11 give measures and trade-offs, but a number is still missing.
- Ray is greenfield, so it does not prove migration. Slide 9 now says so. The migration path (Salesforce and Zendesk into the case system) is an open point and needs an answer before the meeting.
- Contact forecast mismatch: section 2 says "1.5m-2m in 2030", while `01-knowledge-base/metrics/contact forecasting.md` and slide 3 use 2,154,799 (35.9x of 60,049). Part 1 should be corrected to the forecast file.
- Headcount "about 300?" is unverified and sits in the situation line. Confirm or remove.
- Slide 8 leans on "under 1%" QA coverage, a single observation in Care only. A COO will ask about Risk and Compliance.
- Product onboarding is only specified for Care. The other Ops domains' required inputs are not yet documented (see Gaps to fill). Expect Risk and Compliance to ask why their launches follow the same path.
- Salesforce boundary is unresolved. Commercial treats Salesforce as its record of truth for MCRs, onboarding and underwriting, and quote to cash is moving out of it. Expect commercial and the Salesforce owners to challenge "one case system". Needs discovery before the meeting (section 12).
- Commercial and account manager communication sits outside Care's scope as written. Expect the question of whether Care owns it, and a gap in visibility both ways.
- The front door needs an account manager channel design, because top-tier merchants will keep emailing their account manager.
- Product launch governance (principle 17) needs product team and EP commitment. Slide 11 carries it as a trade-off. No owner is named.
- Segment escalation is the question a COO will ask: what does an SMB or Consumer customer get when the customer agent cannot solve it and a human is not available? The direction is set (Enterprise open, SMB and Consumer limited by policy) but the policy, exceptions and fallback experience are not defined. Ghost slide A14 holds it.
- Twelve core slides is long for a C-suite meeting. If time is short, use the 10-minute path below.
- Likely pushback: why one platform instead of fixing each team's tooling (answer: principle 15, operating parity); who pays for domain teams to build UI and interfaces; what happens to Sardine, Fircosoft, RA Tool and the 20+ Retool apps (answer: their functionality is consolidated into the portal where possible, and the tool-by-tool decision is an open point in section 12).

### Framing choices

- Ask first (writing guide: recommendation first). If the audience is unfamiliar with the work, swap slides 1 and 2.
- Headline "operations platform" for the bigger, more fundable idea. Care appears as the customer layer on slides 1, 5 and 7.
- The Plain decision is made before the meeting, so it is not an ask. Plain is named only in the plan (slide 9). The vision stack shows capabilities, not systems.
- If the meeting is 10 minutes, present slides 1, 4, 5, 6, 7 and 12.
