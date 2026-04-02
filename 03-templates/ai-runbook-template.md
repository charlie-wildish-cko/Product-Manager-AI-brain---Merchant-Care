# AI Runbook Template

Use this template to define a runbook for the Agent Consultant (Zendesk sidebar, human-in-the-loop) or a Fin Procedure (autonomous AI execution). Complete all sections before marking a runbook Active.

---

## Metadata

| Field | Value |
|---|---|
| **Runbook ID** | RB-[NNN] |
| **Version** | 1.0 |
| **Status** | Draft / Review / Active / Deprecated |
| **Owner** | [PM or Care Ops lead] |
| **Last updated** | [Date] |
| **Target surface** | Agent Consultant · Fin Procedure · Both |
| **Source SOP** | [Filename or link to originating human SOP] |
| **Contact type** | [Case type → Issue type → Reason — from support-taxonomy.md] |
| **Est. frequency** | [Contacts/month] |
| **Reflex tag** | [Zendesk tag applied on runbook completion, e.g. `rb_refund_reversal_complete`] |

---

## Trigger Conditions

When should this runbook be surfaced automatically? The system uses these signals to suggest the runbook without the agent asking.

**Ticket signals:**
- [e.g. Case type = PAYMENTS (IN) AND issue type = Refunds AND ticket body contains a payment ID]

**Exclusion signals (do not trigger if):**
- [e.g. Ticket already tagged `escalated_to_engineering`]
- [e.g. Dispute already in progress]

> For Fin Procedures: describe the conversation signal that triggers this Procedure (e.g. merchant says "refund was processed in error" or "reverse this refund").

---

## Pre-Conditions

All of the following must be true before the runbook proceeds. Verify programmatically where possible; surface to agent for manual confirmation where not.

| # | Pre-condition | How to verify | If not met |
|---|---|---|---|
| 1 | [e.g. Payment ID present in ticket] | Auto: extracted from ticket body | Prompt agent to request payment ID from merchant |
| 2 | [e.g. Merchant identity confirmed] | Auto: org match in Zendesk | Exit: escalate to Dispatch queue |
| 3 | [e.g. Payment age ≤ 90 days] | Data: `GET /payments/{id}` → `created_on` | Agent decision: escalate to L2 |
| 4 | [e.g. Agent has required permission] | Auto: check agent role in Zendesk | Exit: escalate to senior agent |

---

## Data Inputs

All data the runbook requires and where it comes from. Specify the exact API call or data source so engineers can configure Data Connectors.

| Input | Source | API / query | Required? |
|---|---|---|---|
| [e.g. Payment ID] | Ticket body (extracted) | — | Required |
| [e.g. Client ID] | Zendesk org record | Zendesk org metadata | Required |
| [e.g. Payment status] | Payments API | `GET /payments/{payment_id}` | Required |
| [e.g. Account status] | User Management API | `GET /accounts/{client_id}/status` | Required |

---

## Steps

### Step types

| Type | What it does | Auto-execute? | Approval gate? |
|---|---|---|---|
| `retrieve` | Read data from an external system. No side-effects. | Yes | No |
| `decide` | Apply logic to data. Surface result to agent for review. | Yes | Yes — agent confirms before proceeding |
| `act` | Execute a write operation (API call, system update). Irreversible or risky. | No | Yes — always, before execution |
| `communicate` | Draft a message (internal note or merchant response). Agent reviews before send. | No | Yes — agent approves text |

---

### Step 1: [Step name]

**Type:** `retrieve`

**What happens:** [Plain English description — e.g. Retrieve payment record for the payment ID found in the ticket.]

**API call:**
```
GET /payments/{payment_id}
```

**Output surfaced to agent:** [What the agent sees — e.g. Payment status, amount, created date, refund eligibility flag.]

**If data not found:** [What happens — e.g. Surface message: "Payment ID not found. Ask merchant to confirm payment reference." Exit runbook.]

---

### Step 2: [Step name]

**Type:** `decide`

**What happens:** [e.g. Evaluate whether the payment is eligible based on status, age, and account standing.]

**Logic:**
```
IF payment.status == "Captured"
AND payment.created_on >= [today - 90 days]
AND account.status == "Active"
THEN eligible = true
ELSE eligible = false
```

**Output surfaced to agent:** [What the agent sees — e.g. "Payment [ID] is eligible: Amount [X], Captured [date], Account active."]

**Approval gate:** Agent confirms before proceeding to next step.

**If not eligible:** [e.g. Surface reason. Offer exit paths: (a) escalate to L2 for exception, (b) close with merchant explanation.]

---

### Step 3: [Step name]

**Type:** `act`

**What happens:** [e.g. Execute the reversal via the Payments API.]

**APPROVAL GATE — agent must confirm before this step executes.**

**Agent sees before approving:**
- Action: [e.g. Reverse refund]
- Payment ID: {payment_id}
- Amount: {payment.amount} {payment.currency}
- [Any other parameters relevant to the action]

**API call:**
```
POST /payments/{payment_id}/reversals
Body: { "amount": {payment.amount} }
```

**Output:** [e.g. Reversal confirmation with reversal ID and expected settlement date.]

**If API call fails:** [e.g. Surface error code to agent. Do not retry automatically. Agent decides: retry, escalate, or close.]

---

### Step 4: [Step name]

**Type:** `communicate`

**What happens:** [e.g. Draft an internal note confirming the action for the ticket record.]

**APPROVAL GATE — agent reviews and approves before posting.**

**Draft template:**
```
[Insert draft internal note here. Use {placeholders} for dynamic values.]
```

**Agent action:** Review, edit if needed, approve to post.

---

### Step 5: [Step name]

**Type:** `communicate`

**What happens:** [e.g. Draft a merchant-facing response confirming the outcome.]

**APPROVAL GATE — agent reviews and approves before sending.**

**Draft template:**
```
Hi {merchant.contact_name},

[Insert draft merchant response here. Use {placeholders} for dynamic values.]

[Agent name]
Checkout.com Merchant Care
```

**Agent action:** Review, personalise if needed, approve to send.

---

## Approval Gate Summary

| Step | Gate type | What agent approves | If rejected |
|---|---|---|---|
| [2] | Eligibility review | Confirm payment is eligible to proceed | Exit to escalation or close |
| [3] | Action authorisation | Confirm API call parameters before execution | Do not execute; agent decides next step |
| [4] | Internal note | Review and approve drafted note | Agent edits and re-approves |
| [5] | Merchant response | Review and approve drafted response | Agent edits and re-approves |

---

## Exit Conditions

Every way this runbook can end. Every exit must have a defined outcome.

| Exit condition | Trigger | Outcome |
|---|---|---|
| Successful completion | All steps completed, API call succeeded, response sent | Tag ticket `runbook_complete` + `{reflex_tag}`; close or pending-close |
| Pre-condition not met: [specify] | Step [N] — [condition fails] | [Agent action or escalation path] |
| API failure | Step [N] — API returns error | Surface error to agent; agent decides: retry, escalate, or close |
| Agent rejects at approval gate | Any `act` step | Step does not execute; agent decides next action manually |
| Escalation required | Agent determines case needs L2 or engineering | Tag ticket `escalated`; escalation note drafted |

---

## Success Criteria

What does a successful runbook execution look like?

- [ ] [e.g. Eligibility confirmed and logged]
- [ ] [e.g. API call returned 2xx response]
- [ ] [e.g. Internal note posted to ticket]
- [ ] [e.g. Merchant response sent]
- [ ] Ticket tagged `runbook_complete` + `{reflex_tag}`

---

## Escalation Paths

| Scenario | Escalate to | How |
|---|---|---|
| [e.g. Payment ineligible — exception requested] | L2 / Senior Agent | Tag ticket `l2_review_required`; brief internal note added |
| [e.g. API error persists] | Engineering | Raise Jira with error code and payload |
| [e.g. Suspected fraud] | Risk team | Tag `risk_review` + internal note |
| [e.g. Merchant dispute about outcome] | Account Manager / TAM | Internal note drafted; agent notified |

---

## Reflex Tag

Tag applied to the Zendesk ticket on runbook completion. Feeds Reflex contact driver intelligence via the existing ticket tagging pipeline.

- **Completion tag:** `rb_[runbook_name]_complete` (e.g. `rb_refund_reversal_complete`)
- **Escalation tag:** `rb_[runbook_name]_escalated`
- **Exit tag (pre-condition failed):** `rb_[runbook_name]_ineligible`

---

## Notes and Edge Cases

Known exceptions, special cases, or behaviours that do not fit cleanly into the main flow.

- [e.g. Partial reversals are not supported by the current API. If merchant requests partial, exit and escalate to L2.]
- [e.g. If merchant is on a custom settlement schedule, the expected settlement date in the response draft will be incorrect. Flag to agent.]

---

## Related

- Source SOP: [link]
- Data Connector spec: [link to fin-data-access-backlog or Jira ticket]
- Taxonomy reference: [support-taxonomy.md entry]
- Related runbooks: [RB-IDs that may be invoked before/after or in similar contexts]
- Fin Procedure counterpart: [link if a Fin-facing version also exists]
