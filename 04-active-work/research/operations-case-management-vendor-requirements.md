# Operations Case Management Requirements (Vendor-Agnostic)

## Context

We're evaluating vendors as a unified case management layer across three operations functions: Support, Risk Operations (disputes, underwriting, fraud), and Compliance (transaction monitoring). The intent is not to replicate specialist tooling (e.g. Sardine) inside the case management platform, but to use it as the single intake point, queue, and system of record for work, with specialist analysis happening in external tools and results linked back.

Below is a high-level target architecture and the requirement areas we need any vendor to answer against.

This is currently the view of [Charlie Wildish](mailto:charlie.wildish@checkout.com) and not complete or final.

## Target model

- Cases can be created either by a customer (email, chat, form) or by an internal system (fraud alert, transaction monitoring rule, underwriting trigger); both land as the same kind of object in the same queue.
- Every case links to a customer or business entity as the minimum requirement, not necessarily an individual email or contact. For merchants the minimum is the business; for consumers it's the customer ID.
- Cases are typed by team/work category (e.g. Support, Dispute, Underwriting, Fraud, TM Alert), each with its own relevant data fields, while still being one underlying object any agent can pick up.
- Agents can see and pick up work they are permission-scoped to, and cases can be reassigned across teams as needed.
- External specialist tools (e.g. Sardine) do the actual analysis. Their case reference is linked back to the case in the platform, and their output is surfaced there for an agent to review and approve.
- Agent approval is the "work done" event, and should be able to trigger downstream workflows outside the platform.
- Agent status, work output, etc. can be tracked to measure productivity, occupancy, etc.

## Terminology

- **Case management** - manages the full lifecycle of a piece of work: intake, investigation, collaboration, approvals, evidence, resolution and audit trail. Work assignment and distribution decides where work goes: which queue, team or person should handle it, based on skills, capacity, priority, jurisdiction, shift and SLA risk. Key capabilities:
  - Routes work intelligently across teams.
  - Gives agents the context and tools needed to resolve it.
  - Tracks status, ownership, ageing, next actions and SLA risk.
  - Supports internal collaboration as tracked work, not informal conversations lost in Slack or email.
  - Allows conversations, internal requests, approvals and escalations to remain linked to the main case.
  - Captures the full audit trail, including decisions, evidence and handoffs.
  - Integrates with specialist systems while presenting one operational workspace.
  - Provides automation and AI assistance to summarise cases, fetch information, recommend actions and reduce manual work.
- **Specialist tools** - tools which cover specific domains and help complete the actual work. Examples: Care Agent toolkit, Sphinx, Sardine, RA Tool, Retool, Fircosoft/TM tools, Genesis.
- **Case / ticket** - the core unit of work in the platform: a single intake object that carries conversation, data, and status through its lifecycle, regardless of what the vendor calls it internally.
- **Work type** - the data needed for a case for a specific domain or team, for reporting, routing or AI involvement. Affects downstream automation, reporting, audit, so needs to be quality controlled.

## Questions by requirement area

### 1. Case intake & creation

| Requirement | What we need from the vendor |
| :-- | :-- |
| Business-initiated (system-triggered) case creation with no inbound customer message | Confirm the platform supports creating a case with no real conversation cleanly today, and whether there are any UI or reporting side effects of a case with no message content. |
| Idempotent creation from upstream retries | Confirm the platform supports idempotent case creation keyed on an external ID we supply, distinct from any bulk/historical import mechanism. |
| Pre-sorted routing at creation and using AI to classify | Confirm labels/fields can be set at creation time to route directly into a team queue without manual triage. |

### 2. Entity linking

| Requirement | What we need from the vendor |
| :-- | :-- |
| Case must link to a customer entity as the minimum, and sometimes independent of any individual contact (e.g. email address) | Confirm a case can be created and scoped to an account/tenant with no customer/contact attached, or what the minimum viable customer record looks like in that scenario. |
| Some cases may need to reference two business entities (e.g. a dispute involving payer and payee) | Confirm whether the platform's data model supports more than one account/entity link per case, or how you'd recommend handling this. |

### 3. Per-team case typing

| Requirement | What we need from the vendor |
| :-- | :-- |
| Different field sets per work type (Support vs Dispute vs Underwriting vs Fraud vs TM Alert) — equivalent of a Salesforce record type or Zendesk ticket form | Confirm whether case fields can be scoped to a case type/label so only relevant fields appear and are required per type, versus being global across all cases. |
| Enforced data quality per work type | Confirm whether "required field" logic can be conditional (only required when a given label/type is present) or is only settable globally. |

### 4. Cross-team routing, handoff & access control

| Requirement | What we need from the vendor |
| :-- | :-- |
| Any agent can see the shared queue, but sensitive case types (e.g. compliance) may need restricted visibility even within the same workspace | Confirm the actual granularity of role-based access control: can a role be scoped to specific labels/case types, or only at team/workspace level? |
| Reassignment across teams may need to change access, not just ownership | Confirm whether reassigning a case to a different team can also apply a different visibility/permission set automatically. |
| Segregation of duties for regulated casework (compliance, fraud) | This is our highest-priority open question — please confirm what the platform currently supports here and what your customers in regulated industries typically do. |

### 5. External tool integration (e.g. Sardine)

| Requirement | What we need from the vendor |
| :-- | :-- |
| AI agent integration with relevant knowledge, data and tools | Confirm the platform's AI/assistant layer can connect to any AI agent, API, or data source we specify, not just pre-built integrations. |
| Bi-directional link between a case and an external system's case ID | Confirm the platform has a fully general-purpose way to link a case to an external record (not limited to specific pre-built integrations) and that it can be called entirely via API. |
| Surfacing an external tool's output in a case for agent review | Confirm the best-practice pattern: internal note, case field, or another mechanism — and whether there's a review-and-approve pattern that could be generalised to non-reply content (i.e. not just for approving a customer-facing message). |
| Agent approval as a distinct, auditable action | Confirm whether an approval action can be captured as its own event (not just "case marked Done"), including who approved and when. |

### 6. Downstream workflow triggers

| Requirement | What we need from the vendor |
| :-- | :-- |
| Approval of a case should be able to trigger workflows outside the platform (e.g. refund, notification, ledger update) | Confirm which webhook events fire on note creation, field updates, and case resolution, and what payload each carries. |
| A single approval may need to trigger more than one downstream action | Confirm whether multiple systems can subscribe to the same webhook event, or whether we should plan for an intermediary event bus. |

### 7. Audit & compliance trail

| Requirement | What we need from the vendor |
| :-- | :-- |
| Immutable or fully versioned history for regulated casework | Confirm whether notes/fields can be edited or deleted post-creation, and if so, whether changes are logged anywhere accessible to us. |
| Configurable retention per case type | Confirm whether retention policy can be set per case type/label, or is workspace-wide only. |
| Full case export for audit/regulator review | Confirm what a complete export of a case (conversation, notes, field history, links) looks like and in what format. |

### 8. Reporting segmentation

| Requirement | What we need from the vendor |
| :-- | :-- |
| Support SLA-style metrics don't apply to compliance/risk casework | Confirm whether reporting can be filtered or built separately per case type/label from the outset. |
| Leadership may want a single cross-team throughput view | Confirm whether this is achievable natively or would need to be built via export into a BI tool. |

### 9. Roles

| Requirement | What we need from the vendor |
| :-- | :-- |
| Distinct roles for support agents, risk analysts, and compliance officers | Confirm how granular the platform's role model is today, and whether it maps to functionally distinct teams with different permissions, not just different inboxes. |
