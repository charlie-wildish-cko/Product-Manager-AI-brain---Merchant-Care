# Agent Consultant

> AI-powered application for Zendesk agents that helps with tasks today and, over time, acts as a semi-autonomous AI agent executing manual work to save agent time, using a human-in-the-loop model.

## What it is

The **Agent Consultant** is an AI-powered application for Care agents in Zendesk. It is designed to help agents with their tasks; the end goal is to act as a semi-autonomous AI agent that executes manual work on their behalf to save time, with humans remaining in the loop to review and approve.

## Why it matters

Human agents are Checkout.com's most expensive support resource at ~$40 per contact. Every minute an agent spends searching for information, manually retrieving payment data, or re-reading policy docs is cost with no customer value. At scale, that friction adds up across thousands of tickets per month.

The Agent Consultant attacks handle time directly. By surfacing the right knowledge, data, and suggested actions in the agent's workflow — without them leaving Zendesk — it reduces the cognitive load on agents and cuts the time to resolution. Over time, as the action-based capability matures, agents move from doing repetitive tasks manually to reviewing and approving AI-generated actions.

There is also a quality dimension. Inconsistent handling across agents is a persistent problem in support at scale. The QA capability creates a feedback loop — identifying gaps between how agents resolve tickets and what good looks like — that improves quality without requiring manual QA on every ticket.

The Agent Consultant is also a structural dependency for Reflex: ticket content summaries from the Consultant feed the Insight & Prevention engine, turning closed ticket data into prevention intelligence.

## Capabilities

| Capability | Description |
|------------|-------------|
| **Knowledge retrieval** | Retrieval from public and internal knowledge sources so agents get relevant answers and SOPs in context. |
| **Data retrieval** | Payments and other data. Currently live: posts internal notes in Zendesk when a payment ID is found in a ticket (see [agent-toolkit-zendesk.md](../processes/agent-toolkit-zendesk.md) Payment tool). |
| **Ticket content summary** | Summarises closed ticket content to identify root causes. Feeds into [Reflex](reflex.md) for contact driver analysis and insight. |
| **Internal QA** | QA on closed tickets based on QA definitions and a golden dataset of what qualifies as good tickets. |
| **Action-based** | Access to relevant APIs/MCP tools to perform agent tasks (e.g. refund reversals, querying 3rd party APIs), with human-in-the-loop approval. |

## Relationship to existing assets

- **Flywheel**: Agent Experience (reduces AHT; core driver of cost per contact for human-handled tickets).
- **Current toolkit**: Extends the agent toolkit (User Profile, Payment Tool). Data retrieval today is delivered via the Payment Tool behaviour; the Consultant adds the AI layer (suggestions, summarisation, QA, actions).
- **Reflex**: Ticket content summary from the Consultant is an input to Reflex for root cause and contact driver analysis (Insight & Prevention).

## Related

- [Care Product Model](../strategy/care-product-model.md) (Agent Experience domain)
- [Reflex](reflex.md) (receives ticket summary input from Consultant)
- [Agent toolkit (Zendesk)](../processes/agent-toolkit-zendesk.md) (User Profile, Payment Tool)
- `2026 deliverables.md` (AI Agent Consultant phased roadmap)
