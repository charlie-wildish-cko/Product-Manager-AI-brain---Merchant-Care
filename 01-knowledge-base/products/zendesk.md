# Zendesk

> **Purpose**: Reference document for Zendesk Support + Guide as used by Checkout.com. Covers ticket lifecycle, business rules, routing, knowledge base, AI tooling, and analytics. For internal agent tooling built on top of Zendesk, see [agent-toolkit-zendesk.md](../processes/agent-toolkit-zendesk.md).

---

## Why it matters

Zendesk is the operational backbone of Checkout.com's support function. Every contact that isn't resolved by Fin becomes a Zendesk ticket — it is where agents work, where SLAs are tracked, and where the data record of every merchant support interaction lives.

Its configuration directly determines support quality and efficiency. Routing rules control whether the right agent handles the right ticket at the right time. Business rules (triggers, automations, macros) determine how consistently tickets are processed. SLA policies set the expectations merchants are measured against. Poor Zendesk configuration means misrouted tickets, inconsistent handling, and avoidable SLA breaches.

Zendesk is also a primary data source for Reflex. Every ticket — its fields, tags, comments, resolution path, and CSAT — is raw material for contact driver analysis. The quality of that analysis depends on the quality of ticket data: accurate categorisation, consistent tagging, and structured fields. Investments in Zendesk configuration are therefore investments in the Reflex data foundation.

Finally, Zendesk Guide (support.checkout.com) is one of Fin's primary content sources. The quality of the knowledge base determines Fin's resolution accuracy. Keeping Guide current is a direct input to Fin performance.

## Checkout.com Setup

| Product | Use |
|---------|-----|
| **Zendesk Support** | Core ticketing platform — all inbound contacts (email, webform, Fin Messenger escalations) become tickets here |
| **Zendesk Guide / Knowledge** | Knowledge base at **support.checkout.com** — merchant-facing help centre; one of Fin's primary content sources |
| **Fin AI Agent** (Intercom) | AI resolution layer — integrated with Zendesk; handles tickets before human agents. Not Zendesk's native AI agents. |

---

## 1. Ticket Lifecycle

### Status progression

| Status | Colour | Meaning | Transitions |
|--------|--------|---------|------------|
| **New** | Orange | Created; no agent action taken. Cannot be reset once changed. | → Open, Pending, Solved |
| **Open** | Red | Assigned; awaiting agent action. | → Pending, On-hold, Solved |
| **Pending** | Blue | Agent waiting for requester response. Auto-reverts to Open when requester replies. | → Open, On-hold, Solved |
| **On-hold** | Dark grey | Waiting on a third party (not the requester). Requesters see this as Open. Must be activated by admin. | → Open, Pending, Solved |
| **Solved** | Light grey | Agent submitted resolution. | → Closed (by automation) |
| **Closed** | Light grey | Final status. Set by automations only — cannot be set manually. Requester reply creates a new follow-up ticket. | — |

Default: automations close Solved tickets after 4 days. Without any automation, the system closes them after 28 days (not configurable).

**Custom ticket statuses** (Professional+ plan): form-specific labels that sit within the standard status categories. Used to add detail without changing the underlying status model.

### Ticket types
Question · Incident · Problem · Task — set by agents; used in views, triggers, and reporting.

### Ticket fields and forms
- **Ticket fields**: custom data fields on tickets; can be agent-only or visible to end users
- **Ticket forms**: predefined sets of fields for specific request types (e.g. payment dispute vs. onboarding query)
- **Tags**: words/phrases added to tickets for categorisation, triggering rules, and searching

---

## 2. Agent Workspace

The unified agent interface for all support channels (email, chat, messaging, voice). Key components:

| Component | Description |
|-----------|------------|
| **Context panel** | Right-hand side: customer interaction history, knowledge panel (help centre content), side conversations, custom object records |
| **Auto Assist** | AI-suggested replies, macro recommendations, and agent instructions based on ticket content. Agents review before sending. Some admin-approved actions can execute automatically (with audit logging). |
| **Agent collision alerts** | Warns when two agents open the same ticket simultaneously |
| **Play mode** | Guides agents through tickets sequentially from a view — useful for high-volume queues |
| **Omnichannel status** | Single agent status across all channels (online, away, offline) |

---

## 3. Business Rules

Four types of automation, used to manage ticket workflow:

### Triggers
Event-driven rules that fire immediately when a ticket is **created or updated**, if conditions are met.

- **Conditions**: All (every condition must be true) + Any (at least one must be true)
- **Actions**: assign agent, set status, send notification, add tag, set priority, fire webhook
- **Cascade behaviour**: actions from one trigger can satisfy conditions in another, creating chains
- **Scope**: fire on New or Open tickets; do not fire on already-Closed tickets

12 standard triggers are pre-configured (notify requester, assign agent, notify group, etc.).

### Automations
Time-based rules that fire based on **elapsed time** after ticket properties are set. Used for:
- Auto-closing Solved tickets (default: 4 days after solved)
- Sending reminders on stale tickets
- Escalating tickets approaching SLA breach

### Macros
One-click prepared responses or action sets applied by agents to tickets. Can modify fields, add comments, set tags, change status. Admins create shared macros; agents can create personal macros. Generative AI can enhance macro content.

### Views
Filtered ticket lists based on defined criteria. Used for queue management. Agents self-assign tickets from views (pull model). Can be sorted by priority, SLA proximity, age.

---

## 4. Routing

### Two routing models

| Model | How it works | When to use |
|-------|-------------|------------|
| **Push** (system assigns) | System routes tickets to agents based on availability and rules | Consistent queue management, SLA-driven prioritisation |
| **Pull** (agents self-assign) | Agents choose tickets from views | Specialist teams, overflow, low-volume queues |

### Omnichannel routing (push model)

Supported channels: email tickets, messaging, calls.

**Assignment method**: highest spare capacity (default) or round-robin (idle-longest).

**Queue ordering** (escalates with plan tier):
- Team: oldest eligible-for-routing timestamp
- Growth: soonest SLA breach
- Professional+: highest priority

**Agent eligibility** requires: online status + spare capacity + matching skills (if skills routing enabled) + matching brand membership.

**Key configuration elements**:

| Element | Description |
|---------|------------|
| **Capacity rules** | Max concurrent work per agent per channel |
| **Skills-based routing** (Professional+) | Matches ticket skill requirements to agent skills; skills timeout prevents indefinite queuing |
| **Custom queues** (Professional+) | Define which agent groups are eligible for specific ticket sets; always prioritised over the standard queue |
| **Idle status threshold** | Auto-sets agents offline/away after inactivity |
| **Messaging reassignment** | If agent does not accept within 30 seconds (configurable on Enterprise), ticket reassigns |

**Key limitations**:
- Light agents cannot receive routed assignments
- Only New or Open tickets are routed; Pending/Solved/Closed are excluded
- Fin AI agent tickets are not omnichannel-routed until human escalation occurs
- Operating hours do not automatically change agent status

---

## 5. Zendesk Guide / Knowledge

### Structure

Content hierarchy: **Categories → Sections → Articles** (subsections add further levels).

Checkout.com's help centre: **support.checkout.com** — the merchant-facing knowledge base. Synced into Fin as one of its primary content sources.

### Key Guide features

| Feature | Description |
|---------|------------|
| **Semantic search** | Captures meaning, not just keyword matches; improves article relevance in search results |
| **Generative search** | AI-generated answers to help centre search queries (usage-limited) |
| **External content connections** | Confluence spaces or web-crawled external content surfaced in help centre search |
| **Team Publishing** (Enterprise) | Draft → Review → Approve → Publish workflow; staged edits don't affect live articles until approved |
| **Labels** | Words/phrases on articles that influence search ranking |
| **User segments** | Attribute-based groups controlling which end users can access which content |
| **Article summaries** | Short summaries attached to articles; used in search result snippets and AI-driven surfaces |

### Content management
- Articles can be assigned to owners
- "Arrange Articles" view: visual management of the full content hierarchy
- Templates available for consistent article formatting

---

## 6. AI in Zendesk (Checkout.com context)

Zendesk has native AI agent capabilities — but **Checkout.com uses Fin (Intercom), not Zendesk's native AI agents**, layered via the Zendesk integration.

### Auto Assist (Copilot) — used at Checkout.com
Agent-facing AI assistant, connected to Zendesk. Maps to the [Agent Consultant](agent-consultant.md) product concept.

- **What it does**: reads the ticket and suggests replies, actions, and instructions to the agent
- **Suggestion sources**: admin-created Procedures, help centre articles, similar solved tickets, LLM training data
- **Agent review**: agents review and approve all suggestions before sending (some actions can be admin-approved for automatic execution)
- **Does not work on**: AI agent tickets, or content containing images/URLs/video

Auto Assist uses **Procedures** — step-by-step instructions written by admins — as a primary suggestion source. This is Zendesk's SOP layer for AI-assisted agents.

### Intelligent Triage — available (not confirmed in use at Checkout.com)
AI-powered analysis of incoming tickets predicting:
- **Intent**: what the ticket is about
- **Sentiment**: positive / neutral / negative
- **Language**: detected language

Predictions can drive triggers, routing rules, and deflection workflows without manual tagging.

### Zendesk native AI agents (not used at Checkout.com, documented for reference)
- **AI agents Essential**: generative answers from help centre content across messaging/email; replaced deprecated Autoreplies with articles (deprecated July 2025)
- **AI agents Advanced**: formerly Ultimate AI; multi-step flows, custom actions, CRM integrations
- **Automated resolutions**: billing unit for AI agent usage; counted only when issue fully resolved without human escalation

---

## 7. Analytics (Explore)

Zendesk's reporting tool, now called Analytics (formerly Explore).

### Real-time dashboards (three built-in)

| Dashboard | What it shows |
|-----------|-------------|
| **Incoming tickets** | Volume, channel mix, queue depth |
| **Ticket progress** | Status distribution, resolution rate |
| **Agent productivity** | Availability, assignments, handle time |

### Other built-in dashboards
- Agent productivity
- Copilot (Auto Assist) activity
- AI agents Essential activity (not currently used at Checkout.com)

### Custom dashboards
- New dashboard builder (legacy builder being migrated)
- External sharing without login required
- Scheduled automated delivery
- Filtered bookmark states for saving dashboard views
- Dynamically adapts data based on viewer permissions

---

## 8. Key Zendesk Terminology

| Term | Definition |
|------|-----------|
| **Agent Workspace** | Unified interface for managing all support channels in a single ticket view |
| **AI agent** | Automated persona interacting with customers via messaging or email; Essential or Advanced tiers (not used at Checkout.com — Fin is used instead) |
| **Assignee** | Agent currently assigned to a ticket |
| **Automated resolutions** | Billing unit for Zendesk AI agent usage; counted only on fully resolved requests without human escalation |
| **Automations** | Time-based business rules; fire when elapsed time conditions are met after ticket update |
| **Auto Assist** | Zendesk's agent-facing AI assistant (part of Copilot suite); used at Checkout.com |
| **Brand** | Customer-facing identity with its own contact points (email address, help centre, widget) |
| **Business hours** | Configurable schedule for SLA measurement; excludes holidays |
| **Business rules** | Umbrella term for automations, macros, SLA targets, triggers, and views |
| **Capacity rules** | Max concurrent work per agent per channel for omnichannel routing |
| **Channel** | Method customers use to submit requests (email, chat, messaging, voice, social) |
| **Closed** | Final ticket status; set by system automations only; cannot be reopened manually |
| **Context panel** | Agent Workspace component showing customer history and knowledge content |
| **Copilot** | Zendesk's suite of agent-facing AI tools, including Auto Assist |
| **CSAT** | Customer satisfaction rating — post-resolution feedback from end users |
| **Custom fields** | Additional data fields on tickets, users, or organisations |
| **Custom objects** | Custom data structures for business-specific entities (orders, contracts, products) |
| **Custom queues** | (Professional+) Fine-grained routing queues by eligibility group, priority, and SLA proximity |
| **Dynamic content** | Multi-language placeholders used in automations, macros, triggers, and system messages |
| **End user** | Person submitting support requests; no admin/agent access |
| **First reply time (FRT)** | Minutes between ticket creation and first public agent comment; standard SLA metric |
| **Group** | Collection of agents; tickets can be assigned to groups |
| **Help centre** | Customer-facing portal with knowledge base, community, and request portal |
| **Intent** | AI prediction of what a customer request is about (Intelligent Triage) |
| **Labels** | Words/phrases on articles that influence search relevance |
| **Light agent** | Limited role; can view tickets and add private comments within groups; cannot receive routed assignments |
| **Liquid markup** | Zendesk's templating language for placeholders in notifications and macros |
| **Macro** | One-click prepared response or action set applied to tickets by agents |
| **Messaging** | Persistent channel for customer conversations with full history (web, mobile, social) |
| **Omnichannel routing** | System-directed routing of email, calls, and messaging based on agent availability and capacity |
| **On-hold** | Ticket status for waiting on a third party (not the requester); requesters see this as Open |
| **Organization** | Collection of users; used to define views, assignment, and access rules |
| **Pending** | Ticket status — waiting for requester response; reverts to Open on reply |
| **Play mode** | Feature guiding agents through tickets sequentially from a view |
| **Priority** | Ticket classification: Low, Normal, High, Urgent |
| **Procedures** | Admin-written step-by-step instructions used as Auto Assist suggestion source |
| **Requester** | Person who submitted the ticket |
| **Satisfaction Prediction Score** | AI-predicted likelihood of a positive CSAT rating |
| **Side conversations** | Private threads within a ticket for collaborating with specific groups or third parties |
| **SLA** | Service Level Agreement — policy monitoring response/resolution time targets |
| **Tag** | Word or phrase added to a ticket for categorisation, triggering rules, or searching |
| **Ticket form** | Set of predefined ticket fields for a specific request type |
| **Trigger** | Event-based business rule; fires immediately on ticket creation or update |
| **Type** | Ticket classification: Question, Incident, Problem, Task |
| **User segment** | Attribute-based grouping of users determining help centre content access |
| **View** | Filtered list of tickets based on defined criteria; used for queue management |
| **Voice** | Integrated phone channel (formerly Talk) with recording, transcription, voicemail-to-ticket |
| **Web Widget** | Channel embedding Zendesk messaging or support on websites |
| **Webhook** | HTTP request sent to a URL when a trigger or automation fires |

---

## Related

- [Agent toolkit (Zendesk)](../processes/agent-toolkit-zendesk.md) — internal tooling built on top of Zendesk (User Profile, Payment Tool)
- [Fin AI Agent](fin-ai-agent.md) — AI resolution layer integrated with Zendesk
- [Agent Consultant](agent-consultant.md) — AI agent product; Auto Assist is the current Zendesk Copilot instantiation
- [Support workflows](../processes/support-workflows.md) — Dispatch queue, email identification, triage
- [KPI definitions](../metrics/kpi-definitions.md) — FRT, CSAT, resolution rate, AHT
- `04-active-work/roadmap-items/zendesk-org-domain-mapping-prd.md`
- `04-active-work/roadmap-items/zendesk-jira-integration-prd.md`
- `04-active-work/roadmap-items/zendesk-salesforce-integration-prd.md`
