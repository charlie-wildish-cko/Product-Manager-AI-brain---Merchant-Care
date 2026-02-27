# 2026 Product Roadmap — Care & Support

> Work in progress. Detail will be added per deliverable over time.
>
> **Strategic goals**: Reduce / maintain contact rate · Reduce cost of support
>
> **P&L context**: Both goals directly improve the 'L' column — contact rate reduction eliminates demand at source; cost reduction improves unit economics. See `01-knowledge-base/metrics/kpi-definitions.md` → P&L Reporting section.
>
> **Flywheel context**: Deliverables map to the Handle → Learn → Fix → Scale flywheel. See `01-knowledge-base/strategy/care-product-model.md`.


## Quick View by Quarter

| Q | Deliverable | Goal |
|---|---|---|
| Q1 | AI powered contextual answers on Dashboard | Reduce cost |
| Q1 | Merchant context for Fin and Agents (phase 1) | Reduce cost |
| Q1 | Platform support channels | Reduce cost |
| Q1 | AI Agent 'Consultant' (phase 1) | Reduce cost |
| Q1 | Contact reasons reporting — Reflex (phase 1) | Reduce contact rate |
| Q2 | Dashboard onboarding experience | Reduce contact rate |
| Q2 | Education Hub for merchants | Reduce contact rate |
| Q2 | Improve Fin resolution through Procedures | Reduce cost |
| Q2 | Merchant context for Fin and Agents (phase 2) | Reduce cost |
| Q2 | Support model — Standard merchants | Reduce cost |
| Q2 | Agent productivity tools (start) | Reduce cost |
| Q2 | AI Agent 'Consultant' (phase 2) | Reduce cost |
| Q2 | Contact reasons reporting — Reflex (phase 2) | Reduce contact rate |
| Q3 | Replace webform with Fin | Reduce cost |
| Q3 | Support model — Enterprise and Premium merchants | Reduce cost |
| Q3 | Contact reasons reporting — Reflex MCP | Reduce contact rate |
| Q2–Q4 | Agent productivity tools (ongoing) | Reduce cost |
| Continuous | AI first resolution using Fin | Reduce cost |
| Uncertain | Support-based proactive notifications | Reduce contact rate |
| TBC | Centralised merchant ticket submission and visibility | Reduce contact rate |


## Goal 1: Reduce / Maintain Contact Rate

### Dashboard Onboarding Experience
**Q2**

> As a new merchant, I want a clear and intuitive dashboard onboarding experience so that I can quickly and successfully set up my account and start processing payments.

- In-app onboarding checklist that tracks completion of key tasks (invite team members, check payments, check balance, check settlement…)
- Interactive product tours with tooltips for first-time users
- User-selected, role-based journeys for their necessary tasks in Dashboard
- Template merchant *Welcome* microsite, tailorable by Commercial with relevant content and links

**Flywheel**: Fix (reduces onboarding-related contacts at source)


### Education Hub for Merchants
**Q2**

> As a merchant, I want to easily find comprehensive resources and documentation to understand and manage my account, products, and processes.

- New Education / Academy section on [support.checkout.com](http://support.checkout.com) with role-based guides for Dashboard tasks (linked to the onboarding journeys above)
- Videos for the top 5 "how to" tasks/pages in Dashboard

**Flywheel**: Fix (self-service content reduces inbound contacts)


### Support-Based Proactive Notifications
**Uncertain** — dependency on failure data being published

> As a merchant, I want to receive proactive notifications so I am alerted to potential issues or actions required before they impact my business or require me to contact support.

- Real-time email / in-app notifications for critical events (payment failures, chargebacks, bank verification requests)
- Merchant-configurable notification preferences (in-app and email)
- Notification content includes ticket summary and self-serve resolution steps; explore using Fin for this

**Flywheel**: Fix (proactive alerts prevent contacts before they happen)


### Centralised Merchant Ticket Submission and Visibility
**TBC**

> As a merchant, I want a centralised place to submit new support requests and track the status of all my tickets in one place.

- Unified ticket submission flow from Fin with auto-classification and routing to Zendesk and Salesforce
- List view in Dashboard ticket page pulling ticket data and statuses from multiple source systems (Zendesk, Salesforce) into a single interface

**Flywheel**: Handle + Orchestration (reduces friction in submission; improves routing accuracy)


### Contact Reasons Reporting — Reflex
**Q1 → Q2 → Q3**

> As a Support Leader, I want to understand the main drivers for merchants contacting support, identify areas for product improvement, and reduce unnecessary contacts.

**Q1 — AI-Powered Support Intelligence Hub**
- Dashboards surfacing quantified and costed recurring support issues and trends
- Reportable to Product for prioritisation and investment decisions

**Q2 — Voice of the Customer Intelligence**
- Merge support insights with NPS and other research into a full 360 view of merchant feedback
- Proactive ticket spike analysis dashboard — catch high volumes of inbound queries for triage and escalation to Product

**Q3 — Reflex MCP**
- Build Reflex as an MCP so support intelligence is queryable by AI tools and agents

**Flywheel**: Learn (the core insight and prevention engine — see `01-knowledge-base/products/reflex.md`)


## Goal 2: Reduce Cost of Support

### AI Powered Contextual Answers on Dashboard
**Q1**

> As a merchant, I want contextual answers on the Dashboard so I can get immediate, relevant support and information without leaving my workspace.

- Contextual buttons to launch Fin with pre-defined prompts for problem areas on Dashboard pages, providing answers from articles and docs
- Data lookups for specific pages (e.g. Payments, Settlements)
- *Note: access rights management currently has no practical solution — flagged as uncertain*

**Flywheel**: Handle (Fin deflects contacts before they become tickets)


### Merchant Context for Fin and Agents
**Q1 (phase 1) → Q2 (phase 2)**

> As an AI or human Agent, I want context so I can quickly understand the merchant's history, platform configuration, and previous interactions to provide fast and accurate resolution.

**Q1**
- Integration between Fin, Zendesk, and internal Entity / Merchant 360 data sources
- Identify "first-time contact" merchant users to offer a more guided support experience
- Agent Toolkit displays data from the Merchant 360 profile — entity structure, processing profile settings, merchant type, balances…

**Q2**
- Rules engine on Dashboard to define support channel eligibility (e.g. high-value customers see a "Phone" option; new customers guided to chatbot first)
- Show critical alerts in the Agent Toolkit (e.g. "Merchant live < 30 days", "High recent transaction failure rates")

**Flywheel**: Handle + Fuel (context powers both AI and human resolution quality)


### AI First Resolution Using Fin
**Continuous**

> As a merchant, I want rapid support resolution so I can get my common issues resolved instantly.

- Continuous improvement of content coverage through conversation analysis and gap-filling (persistent work)
- Provide Fin with APIs, MCPs, and other data to answer questions across: Outages, Clearing, TPA, APM, Settlements, Balances, Dashboard bugs/errors (using Datadog RUM API)

**Flywheel**: Handle (core AI deflection engine — primary driver of cost per contact reduction)


### Improve Fin Resolution Through Procedures
**Q2**

> As a merchant, I want Fin to handle my support request end-to-end, including following structured processes, so I get a consistent and accurate resolution without needing a human agent.

- Enable Fin to follow defined resolution procedures (SOPs) for known issue types — not just answer questions, but execute structured steps
- Detail to be added

**Flywheel**: Handle (increases AI resolution rate by expanding the types of contact Fin can fully own)


### Platform Support Channels
**Q1**

> As an ISV, I want access to raise support for my merchants.

- Identify which platform a sub-merchant belongs to when they seek support through Fin or Webform — surfaced in Zendesk
- ISV can link merchant to ticket raised through Fin and Webform

**Flywheel**: Handle + Orchestration (correct identification and routing for ISV contacts)
**Related context**: `01-knowledge-base/products/platform-segment.md`


### AI Agent 'Consultant'
**Q1 (phase 1) → Q2 (phase 2)**

> As an Agent, I want proactive, data-driven advice and recommendations to optimise my responses to the merchant.

**Q1**
- Auto-suggest data and answers for agents to review and send, based on SOPs
- Auto-suggested "next best action" prompts based on ticket content (e.g. "Suggest escalating to engineering team")

**Q2**
- Agents can view and use natural language to query production data securely across Payments, Settlements, Balances, Webhooks, and User Management
- AI to show recent tickets from the merchant in a short summary

**Flywheel**: Agent Experience (reduces AHT; core driver of cost per contact for human-handled tickets)


### Support Model
**Q2 → Q3**

> As a merchant, I want multiple support channels so I can contact support in my preferred way that is contextual for me.

- **Q2**: Enable support model for Standard level merchants
- **Q3**: Enable support model for Enterprise and Premium merchants

**Flywheel**: Orchestration (right channel for the right merchant at the right time)


### Replace Webform with Fin
**Q3**

> As a merchant, I want to contact support through a single, intelligent entry point so I get faster, more accurate help without navigating a static form.

- Retire the Dashboard webform as a standalone support entry point
- Fin becomes the primary support channel for ticket submission — capturing context, classifying intent, and routing to the right team where human handling is required
- Detail to be added

**Dependency**: Fin must be able to capture CC'd email addresses on handoff to Zendesk — this is a prerequisite before the webform can be retired, as CC functionality is currently a webform capability merchants rely on.

**Flywheel**: Handle + Orchestration (consolidates intake into AI-first channel; removes a low-intelligence entry point in favour of a higher-resolution one)


### Agent Productivity Tools
**Q2 → Q4 (ongoing)**

> As a Support Agent, I want tools so I can handle merchant inquiries more efficiently, reduce resolution time, and improve the quality of my support.

- Advanced data for L1 & L2 teams — Payments, Settlements, Balances
- Integration with workforce management tools for scheduling and capacity planning
- Routing rules based on agent skills
- SLAs based on issue type, per tier
- Bi-directional integration between Zendesk and Jira
- Bi-directional integration with Salesforce for tickets requiring SF team involvement

**Flywheel**: Agent Experience + Governance


## Flywheel Domain Summary

| Flywheel Domain | 2026 Deliverables |
|---|---|
| **Handle** | AI contextual answers, AI first resolution (Fin), Fin resolution through Procedures, Platform support channels |
| **Orchestration** | Merchant context (channel eligibility), Support model, Centralised ticket submission |
| **Fuel** | Merchant context for Fin & Agents, AI first resolution (data/MCPs) |
| **Agent Experience** | AI Consultant, Agent productivity tools |
| **Insight & Prevention (Learn)** | Reflex (all phases) |
| **Fix** | Dashboard onboarding, Education Hub, Proactive notifications |


**Last Updated**: February 2026
**Owner**: Charlie Wildish
**Status**: Work in progress — detail to be added per deliverable
