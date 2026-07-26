# Vendor POC — Test Scope

**Candidates**: Zendesk · Intercom · Plain · Pylon

**Gate tests** — fail any and the vendor is out. **Differentiators** — scored 0–3, feed into RFC comparison matrix.

---

## Gates

**Flow 1: Fin escalation handoff with context**

Simulate a Fin conversation escalating to a ticket. Ticket must arrive with full conversation transcript and at least two metadata fields (customer tier, intent/topic) pre-populated.

_Pass_: Ticket created with transcript, tier field and intent tag applied — no agent action required.

---

**Flow 2: Tier-based routing with SLA clocks**

Create four test tickets, one per tier (P0–P3). Configure routing to separate queues with separate SLA policies. Verify SLA clocks start on creation and that a P0 breach alert fires before a P3 ticket would breach.

_Pass_: All four tickets in correct queue. SLA clock running per tier. Breach alert fires in test. Routing rules editable without vendor involvement.

---

**Flow 3: Custom sidebar app with read/write**

Build a minimal app: read a ticket field, make a mock external API call, write a result back to a custom ticket field. Deploy without marketplace approval.

_Pass_: App deployed in under 4 hours. Read/write confirmed. No marketplace submission required.

---

**Flow 4: Jira bi-directional**

Create a Jira issue from a test ticket. Update the Jira status. Verify the status syncs back to the ticket without agent action.

_Pass_: Issue created in under 3 clicks. Status sync confirmed. Integration configurable without vendor involvement.

---

**Flow 5: Email-to-org matching**

Send test emails from three addresses: one clean domain match, one personal domain with no mapping, one domain shared across two orgs. Check auto-association and how the ambiguous case is handled.

_Pass_: Domain mapping configurable without vendor involvement. Ambiguous case surfaces a resolution path (manual assignment, fallback queue, or duplicate flag) — does not silently drop or misassign.

---

## Differentiators

**Flow 6: Ticket data extract via API**

Create 20 test tickets across three types. Extract all fields (custom fields, tags, status history, comments) via API.

_Scoring_: Field parity vs. Zendesk baseline; time to extract 20 tickets; webhook support (real-time vs. polling-only).

---

**Flow 7: B2B/B2C data wall**

Create two brands/workspaces. Confirm an agent with brand B access only cannot see brand A tickets or customer records.

_Scoring_: Native isolation = full marks. Achievable via config = partial. Requires separate instance = risk flag.

---

## Summary

| Flow | Type |
|---|---|
| Fin escalation handoff | Gate |
| Tier routing + SLA | Gate |
| Custom sidebar app | Gate |
| Jira bi-directional | Gate |
| Email-to-org matching | Gate |
| Ticket data extract | Differentiator |
| B2B/B2C data wall | Differentiator |

---

## Plain-Specific POC Scope (Q3 2026)

Agreed scope for the Plain assessment. Overlaps with the gates/differentiators above where the underlying flow is the same (taxonomy, routing, SLA, tenancy); listed separately because this is the scope agreed specifically for Plain, not the general vendor comparison.

- Three-layered taxonomy matching ours (case type / issue type / reason)
- Ticket routing to queues
- Ticket routing to queues with SLAs based on taxonomy — **note**: our SLA model is changing to use Workflows; assess Plain against the Workflows-based model, not the current one
- Routing on dynamic fields (e.g. location — route North American client tickets to Mexico-based agents)
- Modelling of users and organisations (tenants)
- Separation of Merchant vs. Consumer tickets — proposed approach: separate Workspaces
- Robust, reliable deployment via IaC and pipelines
- Plan for integrating our existing apps — Plain does not currently support iframes, so existing sidebar apps (e.g. Agent Consultant, Customer 360) need an alternative integration path

---

**Owner**: Charlie Wildish
**Created**: 2026-06-11
**Related**: `04-active-work/research/zendesk-platform-decision-rfc.md`
