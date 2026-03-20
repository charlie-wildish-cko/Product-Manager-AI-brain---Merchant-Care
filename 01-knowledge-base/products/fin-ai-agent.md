# Fin AI Agent

> **Purpose**: Reference document for how Fin AI Agent works as a product, scoped to the Checkout.com deployment context. Use this to ground PRDs, investigations, and stakeholder updates that involve Fin.

Fin is Intercom's AI customer service agent. It is resolution-first — designed to resolve customer queries end-to-end without human involvement, not just triage or deflect. It is built on a proprietary AI Engine optimised for customer service use cases.

---

## Why it matters

The unit economics of support are stark: a human agent contact costs ~$40; Fin costs $0.90 per resolution — a 44x difference. At Checkout.com's contact volumes, shifting resolution from agents to Fin is the single highest-leverage cost reduction available. Every percentage point improvement in Fin's involvement rate directly reduces cost per contact.

Beyond cost, Fin determines the merchant experience at first contact. Most merchants never speak to a human agent — Fin is the entire support interaction. If Fin resolves accurately and quickly, CSAT holds. If it deflects without resolving, merchants resubmit through email and the contact is counted twice. Getting Fin's resolution quality right is therefore both a cost lever and a guardrail.

Fin also creates the data layer that feeds the rest of the Care AI stack. Conversation metadata from Fin flows into Reflex for contact driver analysis. The Fin involvement rate metric is specifically designed to measure true deflection (not just first-touch), so improvements in Fin quality are reflected accurately in the north star metrics.

## Checkout.com Deployment

Checkout.com uses Fin across two surfaces:

| Surface | What it does |
|---------|-------------|
| **Fin Messenger** (Dashboard) | Merchant-facing live chat in the Checkout.com Dashboard. Fin attempts to resolve the query. If it cannot, it escalates by creating a Zendesk ticket. |
| **Fin for Zendesk** (email/tickets) | Handles inbound email tickets in Zendesk. Agents continue working in Zendesk; Fin adds AI resolution on top before a human agent is assigned. Requires trigger configuration; handoff settings control ticket assignment. |

**Copilot** (see section 7) is also connected to Zendesk for agent use.

---

## The Fin Flywheel

Intercom's continuous improvement framework governs how Fin is developed and optimised:

**Train → Test → Deploy → Analyze → (back to Train)**

Every improvement cycle follows this sequence. PRD work on Fin should identify which phase it primarily targets.

---

## 1. Training

Fin's behaviour is shaped by five distinct configuration layers:

### Content (Knowledge Sources)
The knowledge Fin draws on to answer queries. Supported sources:
- Websites (synced URLs)
- Documents (PDF, DOCX)
- Snippets (short-form content written directly in Intercom)
- Zendesk Help Center (synced)
- Confluence, Notion, Guru (internal knowledge import)
- Box, Document360, Salesforce Knowledge

Content can be tagged and targeted at specific audiences. Intercom surfaces **AI-powered content gap recommendations** — topics where Fin lacks sufficient training content.

### Guidance
Natural language instructions that shape how Fin responds — enforcing tone, policies, and escalation behaviour. Think of these as standing instructions that override Fin's default behaviour. Best practices for writing Guidance are documented separately in Intercom.

### Attributes
Structured classification fields that Fin automatically assigns to conversations. Attributes power routing rules, workflow logic, and reporting. Can be configured as conditional (shown only when relevant).

### Escalation
Rules that define when Fin hands off to a human agent. Rules can be based on conversation content, Fin Attributes, or explicit triggers. Configurable per channel.

### Tasks and Procedures
See dedicated section below — this is the most complex training layer.

---

## 2. Procedures and Tasks

The primary automation layer for Checkout.com's Q2 2026 deliverable ("Improve Fin Resolution Through Procedures").

### Procedures
Fin's equivalent of SOPs — they define the steps Fin follows to resolve a specific contact type, including API calls, data retrieval, and response logic. Key capabilities:

- **Natural language instructions**: written in plain English, not code
- **Code conditions**: advanced branching logic for edge cases
- **Sub-procedures**: reusable components that can be called from multiple parent Procedures
- **Simulations**: pre-deployment validation runs to test Procedure logic before it goes live
- **Data Connectors within Procedures**: Fin accesses external data (e.g. payment status, account info) directly within a Procedure step
- **Reporting**: full performance reporting per Procedure

Data integrations are accessed via Procedures, not ad hoc — this is the mechanism for connecting Fin to Checkout.com's internal systems.

### Tasks
Simpler automation for multi-step processes. Use Data Connectors to pull external data and return personalised answers. Less structured than Procedures; appropriate for lower-complexity retrieval flows.

### Data Connectors
API integrations that give Fin access to external systems — e.g. order management, account data, payment status. The mechanism by which Fin delivers data-driven responses rather than generic knowledge-base answers.

### MCP Connectors
Model Context Protocol connectors. Supported for popular third-party apps and custom integrations. Relevant to Checkout.com's **Reflex MCP (Q3 2026)** deliverable — Reflex insights could be made available to Fin via an MCP connector.

### When to use Procedures vs Tasks vs Workflows
Intercom documents this comparison explicitly. Rule of thumb:
- **Procedures** — complex, structured, multi-step flows that require data integration and pre-deployment testing
- **Tasks** — simpler retrieval flows without complex branching
- **Workflows** — conditional routing and handoff logic at the conversation level (not answer generation)

---

## 3. Testing

| Tool | What it tests | When to use |
|------|--------------|-------------|
| **Previews** | How Fin responds to a specific query, visually in the product UI | Quick spot-checks on content or Guidance changes |
| **Batch Testing** | Resolution rate across a set of common questions submitted in bulk | Measuring and improving overall resolution rate |
| **Simulations** | Procedure logic before deployment | Validating Procedure behaviour before going live |

Simulations are specific to Procedures. Batch Testing measures aggregate resolution rate. Previews are for individual query inspection.

---

## 4. Deployment Channels

| Channel | Status |
|---------|--------|
| Fin Messenger (live chat) | Live — deployed in Checkout.com Dashboard |
| Email / tickets (Zendesk) | Live — Checkout.com deployment |
| **Fin Voice** (phone) | Live product — relevant for B2C wallet launch (2027); Consumer Duty obligations require phone channel from day one |

---

## 5. Analytics and Reporting

### Primary metrics

| Metric | Definition |
|--------|-----------|
| **Automation Rate** (AI Resolution Rate) | % of conversations resolved by Fin without human involvement. Equivalent to "AI resolution rate" in Checkout.com's KPI framework. |
| **Fin Involvement Rate** | Checkout.com's specific metric: contacts where Fin was the first point of contact and the merchant did not subsequently submit a separate channel contact for the same issue. Measures true deflection, not just first-touch. |
| **CSAT** | Customer satisfaction, measurable and reportable within Fin |
| **CX Score** | Intercom's composite metric spanning both AI and human interactions |

### AI-powered analysis tools

| Tool | What it does |
|------|-------------|
| **Topics Explorer** | AI-generated topic clustering showing what is driving contact volume — without manual tagging. Useful for taxonomy alignment and content gap identification. |
| **Unresolved Questions Analysis** | Surfaces queries Fin failed to answer. Primary input for content improvement cycles. |
| **Fin AI Agent Monitors** (beta) | Large-scale automated QA across conversations |
| **Optimization Recommendations Dashboard** | AI-generated suggestions for improving Fin performance |
| **Debug Fin answers** | Inspect which content source Fin drew on for a specific response. Used when investigating inaccurate or inconsistent answers. |

### Reporting tools
- **Custom Reports**: build tailored dashboards; can be shared externally without login or scheduled for automated distribution
- **Chart Drill-in**: interactive exploration from charts into underlying conversations
- **Reporting Datasets**: structured data layer with documented column definitions

---

## 6. Copilot (agent-facing, distinct from Fin)

Copilot is Intercom's AI assistant for **human agents** — not for customers. It is a separate product from Fin.

**Checkout.com**: Copilot is connected to Zendesk for agent use. Maps to the [Agent Consultant](agent-consultant.md) product concept in the Care Product roadmap.

| Capability | Notes |
|------------|-------|
| Knowledge retrieval | Surfaces internal articles in agent context |
| Multilingual support | Translates conversations for agents |
| Performance reporting | Own reporting separate from Fin analytics |

---

## 7. Key Settings

| Setting | What it controls |
|---------|-----------------|
| **Personality customisation** | Fin's identity, tone of voice, and response length |
| **Topic curation** | Rename, merge, create, or delete AI-generated Topics (relevant for aligning with `support-taxonomy.md`) |
| **Multilingual support** | Deploy Fin in multiple languages |
| **Multi-brand (Zendesk)** | Brand-specific experiences for different Zendesk brands |
| **JWT-based user verification** | Authenticate users in Fin Messenger |
| **Fin Messenger appearance** | Launcher logo, AI Agent logo, visual customisation |
| **Teammate permissions** | View-only vs full access per teammate |
| **Data sync** | Import ticket/case history, Zendesk user/org data |

---

## Terminology Reference

| Term | Definition |
|------|-----------|
| **Fin AI Engine** | Intercom's proprietary AI model, optimised for customer service |
| **Fin Flywheel** | Train → Test → Deploy → Analyze continuous improvement cycle |
| **Procedures** | Structured automation: natural language instructions, code conditions, sub-procedures, simulations, Data Connector access, and per-Procedure reporting |
| **Tasks** | Simpler automation for multi-step retrieval flows; use Data Connectors |
| **Data Connectors** | API integrations giving Fin access to external systems |
| **MCP Connectors** | Model Context Protocol connectors for popular apps or custom integrations |
| **Fin Attributes** | Structured classification fields Fin applies automatically to conversations |
| **Guidance** | Natural language standing instructions shaping Fin's responses and policies |
| **Automation Rate** | % of conversations resolved without human involvement (same as AI Resolution Rate) |
| **Fin Involvement Rate** | Contacts where Fin was first point of contact and no separate follow-up contact was submitted |
| **CX Score** | Intercom's composite customer experience metric across AI and human interactions |
| **Topics Explorer** | AI-generated volume clustering without manual tagging |
| **Copilot** | AI assistant for human agents (not customers) — distinct from Fin |
| **Fin Voice** | Fin deployed on the phone channel |
| **Simulations** | Pre-deployment validation runs for Procedures |
| **Batch Testing** | Bulk question testing to measure and improve resolution rate |
| **Content gap recommendations** | AI-generated suggestions for missing training content |

---

## Related

- [Agent Consultant](agent-consultant.md) — Copilot analogue in Checkout.com's roadmap
- [Platform Embedded AI Support Vision](platform-embedded-ai-support-vision.md) — Fin in Platform portals (2027)
- [KPI Definitions](../metrics/kpi-definitions.md) — AI Agent resolution rate, Fin Involvement Rate, CSAT
- `04-active-work/fin-involvement-rate-prd.md` — PRD for increasing Fin Involvement Rate
- `04-active-work/fin-email-behaviour-spec.md` — email channel behaviour specification
- `2026 deliverables.md` — "Improve Fin Resolution Through Procedures" (Q2 2026)
