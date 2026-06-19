# Agent Consultant: Vision

**Deliverable**: AI Agent 'Consultant' · Q1–Q4 2026
**Flywheel domain**: Agent Experience
**Strategic goal**: Reduce cost per contact

---

## The cost problem

Human agents cost ~$40 per contact. Fin resolves contacts at $0.90. The 44x difference makes AI deflection the highest-leverage investment in support operations — but deflection has a ceiling. A significant share of contacts require a human: complex disputes, TPA payment investigations, account access issues, refund reversals. For those contacts, the unit cost is determined by how efficiently the agent works.

Most of that handle time is not skilled work. It is mechanical: navigating to an external system to check a payment status, re-reading an SOP to confirm the right procedure, manually drafting a response the agent has written dozens of times before. These steps absorb time without adding customer value. Agent Consultant is the product strategy for reducing that friction — for every contact that reaches a human.

---

## What Agent Consultant is

Agent Consultant is an AI assistant embedded in the Agent sidebar. It surfaces the right data, knowledge, and structured workflows in the agent's workspace at the moment they need them, without the agent leaving the ticket. The model is human-in-the-loop throughout: the AI retrieves information, prepares actions, and drafts responses; the agent reviews and approves.

This is distinct from what Intercom Copilot (Auto Assist) already provides. Copilot is the knowledge retrieval layer — it surfaces relevant articles and SOP suggestions as agents work a ticket. Agent Consultant builds on that foundation with three additional capabilities: data retrieval from external systems (Payments API, TPA systems, User Management API), structured action execution (refund reversals, account unlocks), and guided workflows that walk agents through repeatable tasks step by step. The two systems are complementary. Live today: User Profile (merchant context) and Payment Tool (payment data surfaced automatically when a payment ID appears in a ticket).

We would consolidate all Agent tools into the Consultant Toolkit UI as the single agent tool over time, removing need for manual checks or searches.

---

## Two interaction models

Not all agent tasks are the same. The right interaction model depends on a single question: **is the resolution path known before the agent starts?**

### Runbooks — when the path is defined

A Runbook is a named, step-by-step workflow written in natural language. Each Runbook maps to a specific, repeatable task. Variables are pulled automatically from ticket fields. The agent launches the Runbook from the sidebar and follows AI-guided steps — data is retrieved, API calls are made, responses are drafted. The agent approves each action before it executes.

Runbooks are the right tool when:

- The task has a defined resolution path (the steps are known before starting)
- Consistency matters (every agent should execute the task the same way)
- The action carries risk (refund reversals and account unlocks require an approval at each step)
- The task is high frequency (worth specifying once, reused across the team)

Checkout.com examples where Runbooks fit well: TPA payment status lookup (retrieve TPA reference from ticket, query TPA API, surface result, draft agent response); refund reversal (confirm payment eligibility, verify merchant intent, trigger reversal via API, post internal note); account unlock (verify identity, confirm request legitimacy, trigger unlock via User Management API, confirm to merchant).

The consistency argument is as important as the speed argument. A Runbook executes identically regardless of which agent runs it. Quality is built into the workflow, not dependent on individual experience or tenure. For a team handling hundreds of tickets per month, that structural consistency reduces both error rate and training cost.

### Contextual AI tools — when the path is unknown

Contextual tools are on-demand integrations the AI invokes in real time, either when the agent explicitly queries it or proactively when the AI infers that external data would help. There is no pre-defined path. The AI queries the relevant sources, synthesises results, and presents findings in the sidebar. Results are visible to the full team, building shared knowledge over time.

The interaction pattern is borrowed from how Plain's Cursor surfaces codebase knowledge inside a support workspace — applied here to Checkout.com's internal data systems rather than source code. The agent asks a question or the system detects relevance, and the AI retrieves from whichever combination of sources is needed: payment records, TPA data, prior ticket history, knowledge base articles, SOPs.

Contextual tools are the right tool when:

- The investigation path is not known in advance
- The agent needs to diagnose before they can prescribe
- Multiple data sources need to be synthesised
- The task is exploratory rather than procedural

Checkout.com examples: an agent investigating an unusual payment failure across multiple data points (payment record, TPA response, known error codes, prior similar tickets) before determining the resolution path; an agent pulling a merchant's full account context — open disputes, active configuration changes, recent tickets — before joining a call; an agent checking whether a specific Payouts edge case falls within documented SOP coverage.

### The mixed-mode pattern

Many contacts involve both. The agent investigates first (contextual tools to retrieve and synthesise data) and then executes a defined action (Runbook for the delivery step). This handoff from open-ended investigation to structured execution is a first-class pattern, not an edge case.

| Task type                                    | Interaction model                   |
| -------------------------------------------- | ----------------------------------- |
| Defined path, high frequency, carries risk   | Runbook                             |
| Open-ended, multi-source, unpredictable path | Contextual AI tools                 |
| Starts open, ends with a defined action      | Contextual tools → Runbook handoff |

One important clarification on how this works in practice: the selection of interaction model is a product and operations configuration decision, not an agent runtime choice. For each task type in the automation backlog, the team determines whether it warrants a Runbook (defined path) or contextual tooling (exploratory). Agents follow the interface the system presents. They do not need to choose which mode to invoke.

---

## Customer Agent: the data and reasoning layer for Fin

The Consultant serves two audiences: human agents in Zendesk, and Fin (and future AI agents) handling merchant conversations. **Customer Agent** is the Care-owned product that serves the second audience.

Today, Fin calls other teams' APIs directly to retrieve merchant data. This creates external dependencies and limits what data Fin can access — large volumes of relevant data sit in BigQuery with no path to Fin. Customer Agent removes that constraint.

**How it works.** Fin calls Customer Agent for any data-dependent query — payment status, settlement reconciliation, balance, dispute outcome. Customer Agent queries BigQuery and internal systems it already has access to, reasons over the results, and returns a structured explanation to Fin. Fin's role is the conversation layer: it translates the Customer Agent output into a clear merchant-facing response. Sensitive raw data never leaves Care's systems.

**Why this matters.**

- **No new cross-team dependencies.** Customer Agent already has BigQuery access. Any BQ table in the business is reachable without a new API agreement with another team.
- **Reasoning, not just retrieval.** Payment queries require explanation, not just data. A decline reason code, a settlement discrepancy, a dispute timeline — these need context to be useful to a merchant. Customer Agent reasons over the data before returning it; Fin does not need to.
- **Portable.** Fin is the current AI agent. If Checkout.com moves to an in-house AI agent in future, the Customer Agent interface is unchanged — only the caller changes. The interface must be designed as agent-agnostic from the start: clean request/response contracts that do not assume Fin's specific API conventions.
- **Data boundary.** Fin (Intercom) is a third-party system. Keeping raw merchant data inside Care's systems and passing only the explanation to Fin is a clean data governance boundary.

**Design constraint.** Customer Agent's reasoning must operate on deterministic data as input — BQ queries return facts; Customer Agent reasons on top of them. It should not infer what data probably says. Clear logging at each hop (Fin → Customer Agent → BQ → Customer Agent → Fin) is required so that when an explanation is wrong, the failure point is identifiable.

---

## Supporting capabilities

Beyond the two core interaction modes, the Consultant provides four capabilities that apply across all ticket types.

**Context retrieval.** When a ticket opens, the Consultant loads merchant context automatically: entity structure, processing profile, account status, payment history, and prior tickets and contacts. The agent has a complete picture of who they are dealing with before reading the merchant's first message. This is the data layer the Consultant provides — distinct from the existing Agent Toolkit (User Profile, Payment Tool), which surfaces structured data fields. Context retrieval synthesises across sources into a single sidebar view.

**Response drafting.** The Consultant drafts a reply to the merchant based on the current ticket context. For Runbook tasks, response drafting is the final step — the Runbook prepares the response after completing the resolution steps. For knowledge-based queries, the Consultant can draft a response based on the SOP or article it retrieved. In both cases the agent reviews, edits if needed, and sends. The Consultant never sends on the agent's behalf.

**Conversation summary and escalation summary.** When a ticket is escalated — to a specialist team, a technical account manager, or a senior agent — the receiving agent needs immediate context without reading the full thread. The Consultant generates two distinct summaries at escalation: a conversation summary (what has been discussed and attempted) and an escalation summary (why it is being escalated and the assessed complexity level). Both are available on demand for any long or complex thread, not only at escalation.

**Audit log.** Every action the Consultant performs — data retrievals, API calls, response drafts generated, Runbook steps executed — is logged per ticket with a timestamp and the agent who approved it. The audit log is not visible to agents; it is accessible to Ops managers and the Product team for quality review, incident investigation, and governance. This is a prerequisite for any write-action capability (reversals, account unlocks).

---

## Example workflows

### Pattern 1: Runbook — Refund reversal

A merchant submits a ticket requesting a refund on a payment processed three days ago. The agent opens the ticket.

Before the agent takes any action, the Consultant detects the payment ID in the ticket body and retrieves the payment record automatically. The sidebar surfaces the payment status, amount, processing date, and refund eligibility. The agent has the context they need before reading the first line of the merchant's message.

The Consultant identifies the contact type as a refund request and suggests the Refund Reversal Runbook. The agent launches it. The Runbook walks through each step in sequence:

1. Payment eligibility confirmed — amount, age, and merchant account status all checked against reversal policy. The Consultant surfaces the result; the agent reviews and proceeds.
2. Merchant intent verified — the Runbook prompts the agent to confirm the reversal is authorised by the merchant. The agent confirms.
3. Reversal triggered — the Consultant prepares the API call to initiate the reversal. The agent reviews the parameters (amount, payment reference, destination) and approves. The call executes.
4. Internal note posted — the Consultant drafts a note summarising the action taken (amount reversed, timestamp, authorisation confirmed). The agent approves and it posts to the ticket.
5. Merchant response drafted — the Consultant generates a response confirming the reversal and the expected settlement timeframe. The agent reviews, edits if needed, and sends.

The agent has processed a refund reversal — correctly, consistently, and without leaving the ticket — in a fraction of the time it would take to navigate three separate systems manually.

### Pattern 2: Contextual tools — Unusual payment failure investigation

A merchant reports that several payments over the past 24 hours have failed with an error code they have not seen before. The agent opens the ticket. There is no obvious resolution path yet — the agent needs to investigate before they can respond.

The agent asks the Consultant: "What is error code 20153 and why are these payments failing?" The Consultant queries the Payments API for the affected payment records, cross-references the error code against the internal knowledge base, and checks whether any similar tickets have been resolved in the past 30 days.

The Consultant returns a synthesised summary in the sidebar: the error code indicates a decline at the acquirer level due to a velocity rule trigger; three prior tickets with the same pattern were resolved by advising the merchant to contact their acquiring bank, and one was escalated to the technical account team when the volume exceeded a threshold. No active outage or known platform issue is linked to this code.

The agent now has a diagnosis. They ask a follow-up: "How many payments has this merchant had with this error code in the past 7 days?" The Consultant queries the Payments API for the merchant's recent transaction history and returns a count with a breakdown by date.

With the investigation complete, the agent has a clear picture: isolated acquirer-side velocity limit, no platform fault, resolved through standard merchant guidance. They draft a response. The Consultant suggests the relevant SOP text; the agent adapts and sends.

The investigation took minutes, not the 15–20 minutes it would take an agent to manually query multiple systems and search prior ticket history. Crucially, the Consultant's output is visible to the full team — the next agent to encounter this error code has the precedent immediately available.

---

## Agent experience principles

**Surfaced without asking.** The Consultant does not wait for the agent to query it. When a ticket opens, merchant context is loaded automatically: entity structure, account status, payment history, and prior tickets. When a payment ID appears in the thread, live payment data is retrieved. When the ticket content matches a Runbook, the Runbook is suggested. Agents do not need to know what tools exist — the system presents what is relevant.

**Approve, don't configure.** Agents interact with outputs. The Consultant proposes actions; the agent approves or rejects. The decision to act remains human. The effort to prepare the action is AI.

**No context switching.** Everything happens in the Zendesk sidebar. Data from the Payments API, TPA systems, User Management API, and the knowledge base all surface in the same workspace. Agents do not leave the ticket.

**Consistency by design, not by training.** A Runbook executes the same way regardless of which agent runs it. This matters most for high-risk actions (reversals, account unlocks) and for newer agents — correct execution from day one, not after months of accumulated experience.

**The system learns from use.** Queries the Consultant cannot answer are flagged to the Knowledge Manager as content gaps. Closed ticket summaries feed Reflex, the Insight and Prevention engine, turning agent-resolved contacts into contact driver intelligence. The longer the system runs, the more signal it generates.

---

## What success looks like

The primary metrics are AHT reduction per handled ticket and cost per contact for human-handled contacts. Supporting measures: Runbook adoption rate per eligible task type; contextual tool invocations per handled ticket. The guardrail is Merchant CSAT — which must not decline as automation increases.

There is a structural dependency worth naming. Ticket content summaries generated by the Consultant feed Reflex for root cause analysis. If Consultant adoption grows, Reflex gains signal from agent-resolved contacts — not just AI-resolved ones. The value of building the Consultant well compounds through the Insight and Prevention domain, not just the Agent Experience domain.
