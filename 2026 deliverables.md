# 2026 Product Roadmap — Care & Support

> Work in progress. Detail will be added per deliverable over time.
>
> **Strategic goals**: Reduce / maintain contact rate · Reduce cost of support
>
> **P&L context**: Both goals directly improve the 'L' column — contact rate reduction eliminates demand at source; cost reduction improves unit economics. See `01-knowledge-base/metrics/kpi-definitions.md` → P&L Reporting section.
>
> **Flywheel context**: Deliverables map to the Input → Orchestration → Fuel → Agent Experience → Insight & Prevention → Governance flywheel. See `01-knowledge-base/strategy/care-product-model.md`.

## Goal 1: Reduce / Maintain Contact Rate

### Dashboard Onboarding Experience

Guided in-app onboarding so new merchants set up successfully without contacting support.

**Deprioritised — not in 2026 scope**

> As a new merchant, I want a clear and intuitive dashboard onboarding experience so that I can quickly and successfully set up my account and start processing payments.

- In-app onboarding checklist that tracks completion of key tasks (invite team members, check payments, check balance, check settlement…)
- Interactive product tours with tooltips for first-time users
- User-selected, role-based journeys for their necessary tasks in Dashboard

**Flywheel**: Insight & Prevention (reduces onboarding-related contacts at source)

### Merchant Education Hub

20 tutorials and videos on support.checkout.com covering the top merchant how-to tasks, reducing inbound how-to contacts.

**Q1–Q4**

> As a merchant, I want to easily find comprehensive resources and documentation to understand and manage my account, products, and processes.

**Q1 ✓**

- Discovery on the 20 Tutorials for 2026 — Complete
- Design confirmed on how this exists on support.checkout.com — Complete
- Initial 5 tutorials scoped

**Q2**

- Add new Categories and Sections to support.checkout.com
- First 5 Tutorials and videos published

**Q3**

- Next 10 Tutorials and videos published

**Q4**

- Next 5 Tutorials and videos published

**Flywheel**: Insight & Prevention (self-service content reduces inbound contacts)

### Support-Based Proactive Notifications

Real-time alerts for critical payment events so merchants are informed before they need to contact support.

**2027** — deprioritised for 2026; dependency on notification data being available

> As a merchant, I want to receive proactive notifications so I am alerted to potential issues or actions required before they impact my business or require me to contact support.

- Real-time email / in-app notifications for critical events (payment failures, chargebacks, bank verification requests)
- Merchant-configurable notification preferences (in-app and email)
- Notification content includes ticket summary and self-serve resolution steps; explore using Fin for this

**Flywheel**: Insight & Prevention (proactive alerts prevent contacts before they happen)

### Merchant Ticket Submission and Visibility

A centralised place in Dashboard for merchants to submit and track all their support requests.

**Q4**

> As a merchant, I want a centralised place to submit new support requests and track the status of all my tickets in one place.

- List view in Dashboard ticket page pulling ticket data and statuses
- Admins in Dashboard can see all their business' support requests

**Flywheel**: Input + Orchestration (reduces friction in submission; improves routing accuracy)

### Reflex

AI-powered analysis of support tickets to surface the top contact drivers to Product teams for prioritisation and fix.

**Q1 → Q4**

> As a Support Leader, I want to understand the main drivers for merchants contacting support, identify areas for product improvement, and reduce unnecessary contacts.

**Q1 ✓ — Ticket Summaries POC**

- Dashboards surfacing quantified and costed recurring support issues and trends — Complete
- Reportable to Product for prioritisation and investment decisions — Complete
- POC feeds into Q2 Theme Aggregation and Product Mapping work

**Q2 — Theme Aggregation + Product Mapping + Query Interface**

- Aggregate per-ticket summaries into recurring theme clusters by product area and contact reason
- Map theme clusters to Product teams using the Product Catalogue data
- Build AI engine component 2: theme cluster aggregation + product team mapping
- Build Insights Query Interface (tool TBD): Product team views, self-serve querying, shareable insight links
- Establish quarterly reporting cadence to Product leads

**Done when**: Aggregated theme clusters live; top 10 contact drivers quantified and shared with VP Product and Director of Operations; at least one Product team using Reflex output for prioritisation

**Q3 — Reflex V2 (scope shaped by Q2 feedback)**

- Set up fix implementation measurement from Product teams
- NPS data merge into VoC view (Airtable source; joined via client ID)
- Spike detection and alert mechanism for recent contacts on specific themes/clusters
- Weekly Reflex digest to Product team leads

**Done when**: VoC dashboard live; spike detection running; Product teams on weekly digest; attribution model tracking contact rate reduction from Reflex-originated fixes

**Q4 — Jira Integration (TBC)**

- Automated quarterly creation of top 5–10 stack-ranked Jira issues per product pillar
- Pre-populated with volume, cost, trend, example tickets, and recommended Product team (mapped via product catalogue)
- Issues routed to correct Jira project/board based on pillar → team mapping
- Human review step before issues publish

**Done when**: Quarterly Jira issues auto-created and reviewed by Product leads; Product team contact reduction targets tracked against Reflex-originated fixes

**TBC: Reflex MCP**

- Build and deploy Reflex MCP with read endpoints
- Enables Insights Query Interface and other internal teams to query Reflex insights programmatically

**Done when**: MCP live; Insights Query Interface connected; Product fix governance cycle started

**Flywheel**: Insight & Prevention (the core insight and prevention engine — see `01-knowledge-base/products/reflex.md`)

### Knowledge and Data Graph

Map the relationship between support taxonomy, products, content, and data to identify where coverage gaps exist and what is needed to close them.

**Q3** · Owned by Data Science

> As a Care Product team, I want to understand which contact types lack adequate content or data coverage so we can target improvements to Fin and agent knowledge.

- Map support taxonomy (contact reasons) to products and to existing content and data sources
- Identify gaps: where Fin lacks content, where agents lack SOPs, where data connectors are missing
- Output feeds directly into Fin Procedures roadmap and Knowledge Base prioritisation

**Flywheel**: Fuel + Insight & Prevention (informs content and data investment; connects taxonomy to resolution capability)

## Goal 2: Reduce Cost of Support

### AI Powered Contextual Answers on Dashboard

Contextual Fin buttons embedded on Dashboard pages so merchants get instant answers without leaving their workspace.

**Q3–Q4**

> As a merchant, I want contextual answers on the Dashboard so I can get immediate, relevant support and information without leaving my workspace.

**Q3**

- Re-usable contextual buttons to launch Fin with pre-defined prompts for problem areas on Dashboard pages, providing answers from articles and docs
- Put on Payments pages
- Assess impact

**Q4**

- Expand button to more pages - Settlements, Balances, Users etc

**Flywheel**: Input (Fin deflects contacts before they become tickets)

### Merchant Context for Fin and Agents

Merchant account data surfaced in Fin and the Agent Toolkit so AI and human agents can resolve queries faster with full context.

**Q1 (phase 1) → Q2 (phase 2)**

> As an AI or human Agent, I want context so I can quickly understand the merchant's history, platform configuration, and previous interactions to provide fast and accurate resolution.

**Q1 ✓**

- Integration between Fin, Zendesk, and internal Entity / Merchant 360 data sources — Complete
- Identify "first-time contact" merchant users to offer a more guided support experience — Complete
- Agent Toolkit displays data from the Merchant 360 profile — entity structure, processing profile settings, merchant type, balances… — Complete

**TBC**

- Rules engine on Dashboard to define support channel eligibility (e.g. high-value customers see a "Phone" option; new customers guided to chatbot first)
- Show critical alerts in the Agent Toolkit (e.g. "Merchant live < 30 days", "High recent transaction failure rates")

**Flywheel**: Fuel (context powers both AI and human resolution quality)

### AI First Resolution Using Fin

Expand Fin's data access and structured Procedures so it resolves more contact types autonomously, including over email.

**Q2 → Q3**

> As a merchant, I want rapid support resolution so I can get my common issues resolved instantly.

**Q2 — Data and Procedures**

- Continuous improvement of content coverage through conversation analysis and gap-filling
- Fin can query payments with Reference or ARN/RRN value
- Add Outages API to Fin so it can tell merchants about outages impacting them
- Create Fin Procedures for the top 5 query types

**Q2 — Discovery: Email Data Sharing**

- Design and get ARB sign-off for a solution enabling Fin to share data connector information over email, with an auth mechanism (Phase 1 of Fin data policy)

**Q3 — Expanded Data & Procedures**

- Connect bot gateway to Payin and Payout BQ data source (trade-off: available now vs. waiting on PLC dependency)
- Configure Fin for new PLC data source from Payments Search API
- Add User Management API to Fin so it can troubleshoot merchant account access issues
- Add Sub-merchant Onboarding API to Fin so it can explain onboarding status to Platform ops users in Dashboard and over email
- Add another 5 Procedures to Fin (covering top 10 query types) — Product and Ops scope

**Q3 — Email: Implement Fin Data Policy**

- Implement Phase 2 of Fin data policy — enable Fin to share data-driven resolutions over email (all available APIs)

**Flywheel**: Input + Fuel (core AI deflection engine — primary driver of cost per contact reduction)

### Platform Support Channels

Identify ISV contacts at point of entry and surface Platform merchant context in Zendesk for correct routing and resolution.

**Q1 ✓**

> As an ISV, I want access to raise support for my merchants.

- Identify which platform a sub-merchant belongs to when they seek support through Fin or Webform — surfaced in Zendesk — Complete
- ISV can link merchant to ticket raised through Fin and Webform — Complete
- Agents can identify Platform-type queries; Fin has Platform flag for context and content use

**Flywheel**: Input + Orchestration (correct identification and routing for ISV contacts)
**Related context**: `01-knowledge-base/products/platform-segment.md`

**Future direction**: Embed the Fin AI Agent in the Platform's portal so they resolve merchant queries with Fin first and escalate to us only when needed. Vision: `01-knowledge-base/products/platform-embedded-ai-support-vision.md`.

### AI Agent 'Consultant'

An AI assistant in Zendesk that proactively suggests data, answers, and actions for agents to review and send, reducing AHT.

**Q1–Q4**

Product context and capability set: `01-knowledge-base/products/agent-consultant.md`

> As an Agent, I want proactive, data-driven advice and actions to optimise my responses to the merchant.

**Q1 ✓**

- Auto-suggest data and answers for agents to review and send, based on SOPs — Complete
- Auto-suggested "next best action" prompts based on ticket content (e.g. "Suggest escalating to engineering team") — Complete
- Payins status and response code explanations posted as internal notes

**Q2**

- Add central content source - Public content & Agent content (from git repo)
- Explain Payins using Agent SOPs
- Explain Payouts using Agent SOPs
- Automate TPA payment status lookups
- Automate Refund reversals

**Q3**

- New version of Agent Toolkit incorporating runbook solution — refund reversals is the first runbook
- Agents can trigger automated task: Refund reversals
- Consultant QA judge: nightly batch job that scores every AC-fired ticket against a four-dimension rubric (Relevance, Accuracy, Completeness, Actionability — each 1–3) plus a binary quality signal (would this response reduce AHT or improve reply quality?). Judge runs on a stronger model than the AC (Opus if AC runs on Sonnet) with an independent prompt and rubric. Requires the AC to surface which KB articles it drew from — this is a prerequisite; without it the judge cannot assess accuracy. Scores stored against ticket ID; weekly aggregates surfaced in analytics to identify retrieval degradation, stale KB content, and actionability gaps. Low-scoring examples become the primary input for AC prompt and retrieval improvements. Before shipping as a metric: calibrate against 50–100 human-QA-scored tickets and refine the judge prompt where scores diverge.

**Q4**

- Additional automated tasks (from backlog priorities)
- Analyse and flag potential content gaps in public and internal content using tickets solved by Agents

**Flywheel**: Agent Experience (reduces AHT; core driver of cost per contact for human-handled tickets)

### Support Model

A tiered support model that matches each merchant segment to the right channels and SLAs.

**Q2 → Q3**

> As a merchant, I want multiple support channels so I can contact support in my preferred way that is contextual for me.

* **Q2**: Add relevant merchant attributes to determine support tier — not yet enforced
* **Q3**: Enable support model for Enterprise and Premium merchants; enforce tier routing for Standard

**Dependency**: Ops decision on support model tiers and SLA rules — TBC.

**Flywheel**: Orchestration (right channel for the right merchant at the right time)

### Replace Webform with Fin

Retire the static Dashboard webform and make Fin the primary support entry point for ticket submission.

**Q3**

> As a merchant, I want to contact support through a single, intelligent entry point so I get faster, more accurate help without navigating a static form.

- Retire the Dashboard webform as a standalone support entry point, bar exceptions like for: MCR requests and for fallback if Fin is down
- Fin becomes the primary support channel for ticket submission — capturing context, classifying intent, and routing to the right team where human handling is required

**Dependency**: Fin must be able to capture CC'd email addresses on handoff to Zendesk — this is a prerequisite before the webform can be retired, as CC functionality is currently a webform capability merchants rely on.

**Flywheel**: Input + Orchestration (consolidates intake into AI-first channel; removes a low-intelligence entry point in favour of a higher-resolution one)

### Reduce Agent Effort on Dispatch and Email Clean Up Rules

Zendesk configuration and routing improvements to reduce manual triage work and noise in the agent queue.

**Q2**

* Pilot domain mapping for big merchants with missing users: Exness/Danibrook, Bytedance, MAF Holding, Yango - Eng needed
* Set Closed rules on non business emails - e.g. gmail/hotmail etc - ZD Config
* Close internal ticket creation bar exceptions & enforce internal form adoption for Commercial - ZD config
* Enable internally created tickets to enrich using client id
* Trigger weekly sync for AM/TAM records from SF accounts - Eng needed

**Flywheel**: Agent Experience

### Agent Productivity Tools (toolkit and routing)

More data in the Agent Toolkit and smarter routing rules so agents spend less time on admin and more time resolving.

**Q1 → Q4**

> As a Support Agent, I want tools so I can handle merchant inquiries more efficiently, reduce resolution time, and improve the quality of my support.

**Q1 🔄**

- Bi-directional integration between Zendesk and Jira — In progress

**Q2**

- Add Fraud Detection data to the Agent Toolkit
- Payouts and Processing Profile (TBC)
- Routing rules based on agent skills

**Q3**

- Routing by taxonomy Reason (route tickets based on contact reason classification) — ZD config
- SLAs based on issue type, per Segment (Standard/Enterprise/Premium) — ZD config

**Q4**

- Get case numbers from Salesforce and show case status in Agent toolkit

**Flywheel**: Agent Experience + Governance

## Other Goals / Asks

> Other asks or areas which don't contribute to our 2026 goals

### Blue EMI support

Enable merchant support through Zendesk for merchants with Blue EMI entity

H2

* Build Zendesk brand and configuration; user identification from Dashboard webform and link to Blue EMI entity for reporting

### Consumer Support — Braavos App

Establish the support infrastructure for Checkout.com's first B2C product: the Braavos consumer wallet app. This is a new customer segment requiring a distinct support channel, contact taxonomy, agent content, and AI resolution layer — separate from the existing B2B merchant support model.

Consumer Duty obligations apply from day one of launch. Complaint handling and vulnerable customer identification must be live at launch, not added post-launch.

**Q3–Q4** · PRDs to be added per phase

> As a Braavos consumer, I want fast, accessible support so I can resolve payment and account issues without friction, through the app I'm already using.

**Q3**

- Define consumer care taxonomy (contact types, issue types, reasons) for the Braavos wallet
- Set up Zendesk brand, forms, triggers, automations, and routing for B2C contacts
- Author agent content and macros for launch contact types

**Q4**

- Install Fin mobile into the Braavos app as the primary support entry point
- Configure Fin for B2C: content, Guidance, escalation rules, and Procedures for top consumer contact types
- Validate support model against Consumer Duty obligations before launch

**Future phases (2027)**

- Complaint handling workflow (Consumer Duty compliant)
- Vulnerable customer identification in Fin

**Flywheel**: Input + Orchestration (establishes AI-first entry point and correct routing for a net-new B2C segment)

### Help Desk Platform Evaluation

Evaluate whether Zendesk remains the right long-term platform for Care, ahead of contract renewal in June 2027.

**Q3 → Q4** · Strategic decision piece

- **Q3**: Analysis of current capability gaps; light spikes and trials of alternative platforms (e.g. Plain, Pylon, Intercom)
- **Q4**: Decision made; recommendation approved; contract negotiation or replacement programme initiated by Q1 2027

**Trigger**: Contract renewal June 2027; known capability gaps (Platform merchant data, AI workflow execution, B2C readiness)

**Flywheel**: Governance (underpins all flywheel stages — ticketing, routing, SLA, QA, data pipeline)

Reference: `04-active-work/research/zendesk-platform-decision-rfc.md`

---

### Contact Volume Forecast 2026–2030

Long-range demand forecast across all segments (Enterprise, Platforms ISV, Platforms SMB, Consumer) to anchor investment decisions and B2C readiness planning.

**Q1 ✓**

- Segment-level contact projections from 2026 to 2030 — Complete
- B2B and B2C split quantified — Complete
- Underpins AI investment case and Consumer Duty planning horizon

Reference: `01-knowledge-base/metrics/contact forecasting.md`

## Flywheel Domain Summary

| Flywheel Domain                | 2026 Deliverables                                                                                                  |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| **Input**                | AI contextual answers on Dashboard, AI first resolution (Fin), Platform support channels, Replace webform with Fin |
| **Orchestration**        | Support model, Merchant context (channel eligibility), Merchant ticket submission and visibility                   |
| **Fuel**                 | Merchant context for Fin & Agents, AI first resolution (data/procedures)                                           |
| **Agent Experience**     | AI Consultant, Agent productivity tools, Reduce agent effort on dispatch                                           |
| **Insight & Prevention** | Reflex (all phases), Education Hub, Knowledge and Data Graph                                                       |
| **Governance**           | Agent productivity tools (SLAs, routing), Support model (SLA framework)                                            |

**Last Updated**: 2026-05-18
**Owner**: Charlie Wildish
**Status**: Q1 complete / in-flight. Detail to be added per deliverable.

---

## Q1 Summary

✓ Complete (6): Merchant Education Hub · Reflex POC · Merchant Context Phase 1 · Platform Support Channels · AI Consultant (Payins) · Contact Volume Forecast
🔄 In Progress (1): Agent Productivity Tools (Zendesk/Jira integration)
