# Agent toolkit (Zendesk)

Internal tooling available to Care agents inside Zendesk. Two functional areas:

---

## 1. User profile

Surfaces requester and merchant context so agents can triage and respond with the right identity in mind.

**What agents see:**
- **Requester information** — who the contact is
- **Dashboard role and permissions** — access level in the merchant dashboard
- **Dashboard SSO setup** — whether the organisation uses SSO
- **Merchant relationship** — e.g. *john@netflix.com* is part of the Netflix organisation

**Search by client name or ID**  
Used to associate **unknown requesters** with the correct organisation. Agents can search by client name or Client ID to find and attach the right client to the ticket. This supports the [Dispatch process](support-workflows.md#contact-creation) when the sender could not be auto-identified (email not found in Salesforce/Dashboard).

---

## 2. Payment tool

Speeds up payment-related triage by pulling payment context from the ticket.

**How it works:**
- **Input:** Payment ID (from the ticket body, e.g. text or pasted ID) and **Client ID** for the merchant on the ticket.
- **Query:** The tool calls payment data **outside Zendesk** (external system/API) using those identifiers.
- **Output:** Metadata about that payment is returned and shown in the agent view so they can see status, outcome, and relevant details without leaving Zendesk.

Useful for tickets that mention a specific payment or transaction; reduces context-switching to internal systems or dashboards.

---

## Related

- [support-workflows.md](support-workflows.md) — Dispatch queue, email identification, triage
- [known-challenges.md](known-challenges.md) — Why identification and Dispatch are hard
- [support-taxonomy.md](support-taxonomy.md) — Case type / issue type / reason applied to tickets
