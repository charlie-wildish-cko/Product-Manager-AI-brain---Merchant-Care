# Flows Brief — Intercom Demo Input

**Purpose**: Reference flows for Intercom to build a demo against, as part of the Q3/Q4 2026 support platform vendor evaluation. Scope matches what Plain received for its POC (`vendor-poc-scope.md`) — same three flows, vendor-neutral terms, no unresolved internal design questions.

**Status**: Ready to share
**Owner**: Charlie Wildish
**Related**: `04-active-work/research/vendor-poc-scope.md` · `04-active-work/research/support-platform-vendor-scorecard.md`

---

## Flow 1 — Merchant ticket creation and tier-based routing

**Input**: Fin (chat or email), web form, or direct email.

- **Path A — Fin resolves the request** (chat or email): no ticket created.
- **Path B — Fin escalates, or the request arrives without Fin**: a ticket is created with any context Fin already holds — conversation transcript, customer tier, intent/case type — attached automatically, no agent action required.

1. Channel-based intake rules apply on ticket creation:
   - Identity verification inbox: tag, set case type, add an internal note flagging the ticket type.
   - Escalations inbox: tag as escalation, notify team leads, add an internal note.
   - Secondary-tier support inbox: tag as routed-from-L2, send to L1 first.
   - Outage identified (via fields Fin has set): tag and add an internal note.
   - Urgent keyword detected: tag and set priority to High.
2. Two enrichment steps run in parallel: confirming ticket creation succeeded, and refreshing the requester's contact record. The ticket is tagged "enrichment complete" once both finish.
3. A separate rule copies account manager, technical account manager, sales engineer, and implementation engineer details from the organization record onto the ticket, falling back to whatever the merchant entered if no organization match exists.
4. The enrichment above also adds the merchant's tier and client ID/name to the ticket.
   - On the next hourly run, if the organization has a tier set and the ticket doesn't yet have one, the tier is copied over.
5. If no tier or client is identified, tag as unassigned and route to L1, visible in a shared L1 view.
6. The matching SLA policy (tier-based, or a specialized policy such as Outages or Escalations) sets first-reply and resolution targets.
7. Priority is set based on the selected case type/issue type, unless a rule above already set it (e.g. urgent keyword = High always takes precedence).
8. The ticket is assigned to L1, unless a specific skill is required (e.g. identity verification — routed to L1 agents with that skill; a Japanese-language thread — routed to JP speakers).
9. The requester receives a receipt notification, worded differently depending on channel and whether the request came directly from the merchant or on their behalf.
10. SLA-risk escalation: if unassigned and 8 hours from breach, priority moves to High. If unassigned and 2 hours from breach, priority moves to Critical/Urgent.

---

## Flow 2 — Complaints escalation

**Entry points**: a ticket can enter this flow two ways — direct intake via the complaints inbox (steps 1-10 below), or reclassification of an existing ticket already in progress on another queue, when an agent changes its case type to Complaints mid-thread. The reclassification path should re-trigger steps 2-10 (tag, schedule, routing, priority, SLA, assignment, notification) on the existing ticket rather than requiring a new one.

1. A ticket is identified as a complaint (dedicated complaints inbox, or case-type change on an existing ticket).
2. Tagged as a complaint.
3. A complaints-specific schedule is applied.
4. Routed to the Complaints team.
5. Priority set to High.
6. Ticket type set to Complaints.
7. SLA policy set by country if identifiable, otherwise a default complaints SLA policy applies.
8. Assigned to the Complaints team.
9. If unassigned and approaching or past SLA breach, a breach alert fires (e.g. via Slack).
10. The requester receives a receipt notification.

---

## Flow 3 — L1 to L2 escalation

**Scenario**: L1 agents escalate to L2 for help with a query. The correct L2 team depends on the specialization needed.

1. L1 adds an internal note using a pre-built template (with dynamic fields such as client name/ID) documenting the escalation reason.
2. L1 marks whether an L2 transfer is needed; if yes, selects the required specialization area.
3. Once both fields are set and the note is submitted, a transfer workflow triggers automatically.
4. The ticket routes to the matching L2 specialization team and is unassigned from the current L1 owner.

---

## Flow 4 — Ticket resolution and closure

**Scenario**: an agent marks a ticket solved. What happens next is time-based, not agent-triggered.

1. Ticket is set to solved.
2. An automated response is sent to the customer confirming resolution.
3. A CSAT survey is sent 24 hours after the ticket is marked solved.
4. The ticket remains reopenable for 7 days after being solved — a customer reply within that window reopens the same ticket.
5. After 7 days, the ticket is marked closed. A reply after that point creates a new ticket rather than reopening the original.

---

**Last updated**: 2026-08-24
