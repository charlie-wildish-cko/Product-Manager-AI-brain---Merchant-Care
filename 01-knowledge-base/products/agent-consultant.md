# Agent Consultant

> AI-powered application for Zendesk agents that helps with tasks today and, over time, acts as a semi-autonomous AI agent executing manual work to save agent time, using a human-in-the-loop model.

## What it is

The **Agent Consultant** is an AI-powered application for Care agents in Zendesk. It is designed to help agents with their tasks; the end goal is to act as a semi-autonomous AI agent that executes manual work on their behalf to save time, with humans remaining in the loop to review and approve.

The Consultant also functions as the **data and reasoning layer for Fin**. Rather than Fin calling other teams' APIs directly, Fin calls Care-owned Consultant endpoints for any merchant data query (payment status, settlement, balance, dispute). The Consultant retrieves data from BigQuery and internal systems, reasons over it, and returns a structured explanation. Fin converts that explanation into merchant-facing language. Sensitive data never leaves Care's systems; Fin receives only the output. This architecture removes cross-team API dependencies, uses BigQuery access the Consultant already holds, and is portable — any future AI agent can replace Fin without changing the Consultant interface.

## Why it matters

Human agents are Checkout.com's most expensive support resource at ~$40 per contact. Every minute an agent spends searching for information, manually retrieving payment data, or re-reading policy docs is cost with no customer value. At scale, that friction adds up across thousands of tickets per month.

The Agent Consultant attacks handle time directly. By surfacing the right knowledge, data, and suggested actions in the agent's workflow — without them leaving Zendesk — it reduces the cognitive load on agents and cuts the time to resolution. Over time, as the action-based capability matures, agents move from doing repetitive tasks manually to reviewing and approving AI-generated actions.

There is also a quality dimension. Inconsistent handling across agents is a persistent problem in support at scale. The QA capability creates a feedback loop — identifying gaps between how agents resolve tickets and what good looks like — that improves quality without requiring manual QA on every ticket.

The Agent Consultant is also a structural dependency for Reflex: ticket content summaries from the Consultant feed the Insight & Prevention engine, turning closed ticket data into prevention intelligence.

## Capabilities

| Capability | Description |
|------------|-------------|
| **Context retrieval** | Surfaces merchant data (entity structure, processing profile, account status), payment history, and prior ticket/contact history in the sidebar when a ticket opens — giving the agent full context before they read the first line of the merchant's message. |
| **Knowledge retrieval** | Retrieval from public documentation and internal agent SOPs so agents get relevant answers and procedures in context. Fin uses public content only; Consultant also retrieves from internal operational documents held in the git repo. |
| **Data retrieval** | Live payment and third-party data surfaced from internal APIs. Currently live: payment status and response code explanations posted as internal notes when a payment ID is found in a ticket (see [agent-toolkit-zendesk.md](../processes/agent-toolkit-zendesk.md) Payment tool). |
| **Action execution** | Access to relevant APIs to perform agent tasks (e.g. refund reversals, TPA status lookups, account unlocks) via step-by-step Runbooks. Human-in-the-loop: agent approves each action before it executes. |
| **Response drafting** | Drafts a response to the merchant based on ticket context, knowledge retrieval results, or as the final step of a Runbook. Agent reviews, edits if needed, and sends. |
| **Conversation summary** | Summarises the ticket thread on demand — collapses context for agents picking up a ticket mid-flight or reviewing a long exchange quickly. |
| **Escalation summary** | Generated at the point of escalation: states why the ticket is being escalated and the complexity level, so the receiving agent or team has immediate context without reading the full thread. |
| **Ticket content summary** | Summarises closed ticket content to identify root causes. Feeds into [Reflex](reflex.md) for contact driver analysis and insight. Distinct from conversation summary — this is a post-resolution output for the insight pipeline, not an agent-facing view. |
| **Content gap flagging** | When the Consultant cannot answer a query on an agent-resolved ticket, the gap is flagged to the Knowledge Manager with the ticket reference, query, and contact type — creating a feedback loop between agent usage and content investment. |
| **Fin data layer** | Care-owned endpoints that Fin calls to retrieve and reason over merchant data (payments, settlements, balances, disputes). Consultant queries BigQuery and internal systems, reasons over results, and returns a structured explanation. Fin converts the explanation to merchant-facing language. Data does not leave Care's systems. |
| **Audit log** | Records all Consultant actions — AI-generated and agent-approved — per ticket. Accessible to Ops managers and the Product team only (not surfaced to agents). Supports quality review, incident investigation, and governance. |
| **Internal QA** | QA on closed tickets based on QA definitions and a golden dataset of what qualifies as good tickets. 2027 horizon. |

## Relationship to existing assets

- **Flywheel**: Agent Experience (reduces AHT; core driver of cost per contact for human-handled tickets).
- **Current toolkit**: Extends the agent toolkit (User Profile, Payment Tool). Data retrieval today is delivered via the Payment Tool behaviour; the Consultant adds the AI layer (suggestions, summarisation, QA, actions).
- **Reflex**: Ticket content summary from the Consultant is an input to Reflex for root cause and contact driver analysis (Insight & Prevention).

## Related

- [Care Product Model](../strategy/care-product-model.md) (Agent Experience domain)
- [Reflex](reflex.md) (receives ticket summary input from Consultant)
- [Agent toolkit (Zendesk)](../processes/agent-toolkit-zendesk.md) (User Profile, Payment Tool)
- `2026 deliverables.md` (AI Agent Consultant phased roadmap)
