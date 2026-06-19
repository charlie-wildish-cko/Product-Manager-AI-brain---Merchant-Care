# Dashboard Account Coverage — Problem & Tactics

## Problem

50% of inbound email contacts (Zendesk) have no dashboard account. A dashboard account is a prerequisite for Fin to share account-specific data in email responses, as mandated by Infosec. Merchant admins are the only party who can create accounts — Checkout cannot provision them unilaterally.

The result: half of all email contacts cannot receive AI-assisted, data-informed responses. They either wait for a human agent or receive generic answers.

See also: [customer-comms-identity-problem-statement.md](customer-comms-identity-problem-statement.md) — broader identity and comms fragmentation context.

---

## Selected tactics

| # | Tactic | Mechanism |
|---|---|---|
| 1 | Auto-response to requester | Fin detects no account, sends immediate reply with instructions to get their admin to create one. Ticket held pending. |
| 4 | Weekly admin digest of unmatched contacts | Batch email to merchant admins listing contacts who emailed without accounts that week. |
| 5 | Proactive bulk provisioning campaign | Outreach to admins with low user coverage, ahead of contacts hitting support. |

Tactic 1 is the reactive in-thread layer. Tactics 4 and 5 are the proactive layers. This doc focuses on implementing tactic 1 via Fin.

---

## Implementing tactic 1 with Fin

### How it works

Fin receives every inbound Zendesk email ticket. Before attempting to resolve the query, it runs an identity check via Procedure: look up the requester's email against the dashboard User Management API.

- **Match found** — Fin proceeds with normal resolution flow, with access to account data.
- **No match found** — Fin sends an immediate templated response, sets the ticket to Pending, and does not route to the human queue.

### Fin Procedure design

**Procedure name**: Verify Dashboard Identity

**Trigger**: All inbound email tickets, before any resolution step.

**Steps**:
1. Extract requester email from ticket.
2. Call User Management API: look up user by email address.
3. If user found with active dashboard account: set ticket tag `dashboard-verified`, continue to resolution flow.
4. If no user found: set tag `no-dashboard-account`, send auto-response (see below), set ticket status to Pending.

**API dependency**: User Management API must be configured as a Fin data source. The check is a binary existence lookup only — no account data is returned or exposed. Requires Infosec sign-off on that scope.

### Auto-response template (draft)

> Hi [first name],
>
> To protect your account security, we can only share account-specific information with verified dashboard users. We couldn't find a dashboard account linked to this email address.
>
> To continue, please ask your organisation's dashboard admin to add you as a user. Once they've done this, reply to this email and we'll pick up your query straight away.
>
> [How to add users to your Checkout.com dashboard →]
>
> Checkout.com Support

### Ticket handling

- Status: **Pending** (not Open)
- Tag: `no-dashboard-account`
- SLA clock: paused while Pending
- Re-open trigger: when requester replies, Fin re-checks identity. If verified, resumes normal flow. If still unverified, re-sends response once, then escalates to human queue on a second reply.

### Dependencies

| Dependency | Owner | Status |
|---|---|---|
| User Management API lookup by email | Engineering | TBC |
| Fin Procedure authoring + testing | Product + Content | TBC |
| Infosec sign-off on existence check (no data exposure) | Infosec | TBC |
| Zendesk Pending automation rules | ZD Admin | TBC |
| Help article: how to add dashboard users | Knowledge | TBC |

### Open questions

1. Does the User Management API support lookup by email? Check `04-active-work/user-management-api-endpoints.csv`.
2. When no match is found, can we identify the merchant admin to notify in the same Procedure? Requires a company→admin mapping — overlaps with tactic 4.
3. What's the right escalation threshold before routing to human (one re-send? two)?
4. How do we handle contacts from external parties (agencies, accountants) who will never have dashboard accounts? May need a separate routing path.
