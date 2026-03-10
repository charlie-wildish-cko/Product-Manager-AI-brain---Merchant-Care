# Blue EMI — Zendesk Support Infrastructure

**Status**: Draft  
**Owner**: Charlie Wildish  
**Last Updated**: February 2026  
**Stakeholders**: Zendesk Admins, Engineering, Care Operations, Operational Excellence, Blue EMI Programme, Merchant Experience


## Executive Summary

Blue EMI is a separate entity; its merchants have a distinct Client ID and must be handled as separate customers in Zendesk. This PRD covers the Zendesk configuration and tooling to route, triage, and manage Blue EMI tickets: Dashboard webform, email identity, org setup, and safeguards against misrouting. For programme context (Interim vs Zendesk Build vs End State), see the [scoping one-pager](blue-emi-support-scoping-one-pager.md).


## Problem

**What problem are we solving, and who has it?**  
Tickets from Blue EMI merchants that aren’t tied to their Blue EMI identity get miscategorised as Checkout — wrong routing, SLA, and agent context. The same email can be both Checkout and Blue EMI; we can’t infer entity from email alone. Affected: Blue EMI merchants (need a support path), CX agents (need correct org to triage), CX Ops (need clean Blue EMI queues and reporting).

**How are they solving it today?**  
None. Blue EMI is new. Without this config, tickets would either have no channel or land in the Checkout queue with no entity.

**Why solve this now?**  
Blue EMI onboarding starts in 2026. Support must be ready at first go-live to avoid unrouted tickets, manual triage, and SLA breaches.


## Goals & Success Metrics

| Metric | Current State | Target | Timeline |
| --- | --- | --- | --- |
| % of Blue EMI tickets with a valid Blue EMI Client ID | N/A (no channel) | 100% | At launch |
| % of Blue EMI tickets correctly routed to Blue EMI queue | N/A | 100% | At launch |
| % of new-ticket attempts that arrive via direct email and receive auto-reply (no manual triage) | N/A | Aim to minimise via no-publish policy; target &lt;5% of Blue EMI ticket volume created via direct email (rest via Dashboard) | 3 months post-launch |
| Agent mislabelling of Blue EMI vs Checkout tickets | N/A | 0 | Ongoing |


## User Stories

### Merchant: Submitting a ticket (Dashboard webform)

**As a** Blue EMI merchant logged into the Merchant Dashboard,  
**I want** to submit a support ticket without needing to manually enter my Blue EMI Client ID,  
**So that** the process is fast and I cannot accidentally submit under the wrong entity.

**Acceptance Criteria**:

- Dashboard webform pre-populates the Blue EMI Client ID from the merchant's session
- Merchant can confirm but cannot clear the Client ID field
- Ticket is created in Zendesk with the correct org on submission
- Merchant receives a branded confirmation email from the Blue EMI support address


### Merchant: Replying to a ticket via email

**As a** Blue EMI merchant who has an open ticket,  
**I want** to be able to reply to email notifications to continue the conversation,  
**So that** I don't have to return to the webform for every exchange.

**Acceptance Criteria**:

- Reply-to email threads correctly back to the existing ticket in Zendesk
- No re-entry of Blue EMI Client ID is required (it is already on the ticket)
- Reply is attributed to the correct requester


### Merchant: Attempting to open a new ticket via direct email

**As a** Blue EMI merchant who tries to email the support address directly to open a new ticket,  
**I want** to receive a clear response directing me to the correct channel,  
**So that** I can still get help even if I used the wrong contact method.

**Acceptance Criteria**:

- Inbound email without a Blue EMI Client ID triggers an auto-reply within seconds
- Auto-reply clearly directs the merchant to log in to the Blue EMI Dashboard to submit a ticket, and includes an emergency P0 escalation path
- The ticket is automatically closed/suspended and does not enter the active queue


### Agent: Handling a Blue EMI ticket

**As a** CX agent,  
**I want** Blue EMI tickets to appear in a dedicated queue with the Blue EMI org and Client ID clearly visible,  
**So that** I can triage and respond in the right context without confusion with Checkout tickets.

**Acceptance Criteria**:

- Blue EMI tickets appear in a dedicated Zendesk view/queue
- Blue EMI Client ID field is prominently displayed on the ticket
- Organisation panel shows the Blue EMI org (not the Checkout org)
- Outbound replies are sent from the Blue EMI branded email address automatically

**Edge cases**:

- **Invalid Client ID on submission**: Webform validation rejects the submission and surfaces an inline error asking the merchant to check their Client ID
- **Blue EMI org not yet created in Zendesk**: Ticket creation fails gracefully, falls to a catch-all queue, and triggers an alert to CX Ops for manual triage
- **Same email exists under Checkout and Blue EMI**: User is a member of both orgs (Zendesk Enterprise); ticket org is set by trigger based on Client ID field, not user's default org
- **Merchant replies to a ticket from a different email address**: Standard Zendesk behaviour — reply is associated with the ticket via ticket ID in headers; agent is notified of the email mismatch
- **Merchant submits a P0 issue via direct email**: Auto-reply includes emergency contact path so critical issues are not lost in the redirect


## Requirements

#### Must Have (P0)

- Dedicated Blue EMI ticket form in Zendesk with Blue EMI Client ID as a mandatory custom field
- Dashboard-embedded webform that pre-populates Blue EMI Client ID from session
- Zendesk Multibrand configuration for Blue EMI (separate brand, email identity, templates)
- Blue EMI support email address (e.g. `support@blueemi.com`) configured with correct DKIM/SPF
- Zendesk Organisation per Blue EMI client, with Blue EMI Client ID stored as org external ID or custom org field
- Trigger: on ticket creation via email channel with empty Blue EMI Client ID → auto-reply and close ticket
- Trigger: on ticket creation via Blue EMI form → auto-assign to correct Blue EMI organisation
- **Checkout brand**: Trigger on inbound email to support@checkout.com — if requester email matches a Blue EMI client, auto-reply (wrong channel; use Blue EMI Dashboard) and close ticket; do not create Checkout ticket
- Dedicated agent view/queue for Blue EMI tickets (filtered by `blue_emi` tag or brand)
- Blue EMI Client ID field visible in ticket layout for agents
- **Agent Toolkit** (User Profile search and Payment Tool) must support Blue EMI Client IDs and Blue EMI data sources so agents can look up Blue EMI clients and query Blue EMI payment context
- Blue EMI complaints received and routed under the Blue EMI entity (dedicated complaints address and/or routing to Blue EMI brand in Zendesk)

#### Should Have (P1)

- Auto-reply for bounced email includes link to Blue EMI Dashboard login and emergency P0 escalation path
- Blue EMI branding applied to all outbound email notifications (confirmation, agent replies, CSAT)
- Alert/notification to CX Ops when a ticket arrives with an unrecognised Blue EMI Client ID
- Separate CSAT survey configuration for Blue EMI (distinct from Checkout CSAT)

#### Nice to Have (P2)

- Blue EMI merchant-facing ticket inbox (analogous to the Checkout Dashboard ticket view)
- Automated org creation in Zendesk when a new Blue EMI client is onboarded (webhook from internal onboarding system)
- Reporting dashboard separating Blue EMI ticket volume, SLA performance, and CSAT from Checkout

**Constraints**:
- **Compliance**: Ticket data for Blue EMI merchants must be handled in line with applicable data residency and retention requirements for the Blue EMI entity
- **Availability**: Dashboard webform must be available 24×7; form submission failures must degrade gracefully with a clear error message and fallback contact path
- **Integrations**: Zendesk Multibrand enabled; email DNS configuration (DKIM/SPF); Dashboard webform session integration; Zendesk trigger and webhook configuration for org auto-assignment


## Approach

### Merchant Flow — Dashboard Webform

```
1. Merchant opens support form within the Blue EMI Merchant Dashboard
2. Blue EMI Client ID is pre-populated from session (read-only or confirmed)
3. Merchant fills topic, subject, description
4. On submit → ticket created in Zendesk with correct org
5. Merchant receives branded confirmation email
```

### Email Bypass Flow

```
1. Merchant emails support@blueemi.com directly (new ticket attempt)
2. Zendesk trigger fires: channel = email, Blue EMI Client ID field = empty
3. Auto-reply sent within seconds:
   "To submit a support request please log in to the Blue EMI Dashboard at [URL].
    For urgent payment issues (P0), contact us via [escalation path]."
4. Ticket status set to Closed
5. Ticket does not appear in active agent queue
```

### Merchant contact scenarios

| Who | Channel | Behaviour |
|-----|---------|-----------|
| **Checkout merchant** | Emails support@checkout.com | Zendesk links to Checkout client/org as today; ticket handled in Checkout queue. |
| **Blue EMI merchant** | Emails support@checkout.com | If sender is matched to a **Blue EMI client**, **reject**: auto-reply that this is not the right channel, with instructions to submit via the Blue EMI Dashboard (and escalation path if urgent). Ticket closed; does not enter Checkout queue. |
| **Blue EMI merchant** | Submits via Blue EMI Dashboard | Ticket created in Zendesk linked to **Blue EMI client/org only**; Blue EMI queue and branding. |
| **Checkout merchant** | Submits via Checkout Dashboard | Ticket created in Zendesk linked to **Checkout client/org only**; Checkout queue and branding. |
| **Checkout AM** | Uses internal support form; picks Checkout or Blue client | Ticket maps to the **relevant client/org in Zendesk** (Checkout or Blue EMI depending on selection). |
| **Checkout AM** | Emails support@checkout.com about a Blue client | **Plan to block** AM email submissions for Blue clients from Q2/Q3 — AMs must use the internal form and select Blue client. Until block is in place: wrong-channel handling or manual triage (TBC). |

*Dual-entity merchants:* Channel and submission path set identity. Email to support@checkout.com from a known Blue EMI client → wrong-channel reply and close (Checkout-side trigger), not a Checkout ticket.

### Key UX Decisions

- **Dashboard webform only** — submission requires Blue EMI Dashboard login; Client ID always pre-populated from session.
- **Client ID pre-populated, not editable** — prevents wrong-entity submissions.
- **Direct email → auto-reply to use Dashboard** — no manual triage of email without Client ID.
- **Blue EMI sender to support@checkout.com → rejected** — wrong-channel reply and close so Checkout queue stays clean.
- **AM email for Blue clients → block from Q2/Q3** — AMs must use internal form and select Blue client; behaviour until block TBC.
- **Complaints** — Blue EMI complaints must be received and routed under the Blue EMI entity (e.g. dedicated complaints address and routing to Blue EMI brand in Zendesk, not Checkout).

### Zendesk Configuration

| Element | Detail |
|--------|--------|
| Multibrand | Blue EMI brand: help centre, ticket form, email identity |
| Ticket field | `blue_emi_client_id` — required on Blue EMI form |
| Org field | `blue_emi_client_id` on Organisation (matching) |
| Orgs | One org per Blue EMI client; Client ID = org external ID or custom field |
| Triggers | Set org from Client ID (form → webhook); Bounce direct email (empty Client ID → auto-reply → close) |
| Views | Blue EMI — Open, Pending, Recently Solved |
| Email | `Blue EMI Support <support@blueemi.com>` — DKIM/SPF |

**Technical**: `GET /internal/blue-emi/clients/{client_id}` for validation; Zendesk `PUT /tickets/{id}` for org; Multibrand enabled; Blue EMI domain DNS for DKIM/SPF.


## End State options

*Aligned with the [scoping one-pager](blue-emi-support-scoping-one-pager.md) phase **End State** (end of 2026, ~20 merchants).*

End State may go in one of two directions:

| Option | Description |
|--------|-------------|
| **Full Care support** | Checkout/Care continues to support Blue EMI merchants in Zendesk (current plan). This is intended to be **temporary** until Blue EMI takes over. |
| **Blue EMI support** | Blue EMI eventually takes on full support for Blue EMI merchants in **another system** (TBC). Checkout would no longer handle Blue EMI tickets in Zendesk. |

*Open question:* Will Checkout still be supporting Blue EMI in Zendesk at End State, or will Blue EMI have moved to their own support system by then? This PRD describes the **Full Care support** path; the Blue EMI-owned support path is TBC and would be a separate scope.


## Out of Scope

- Public unauthenticated webform; Blue EMI ticket inbox in Dashboard; automated org creation at onboarding (P2)
- Blue EMI Live Chat; Fin on Blue EMI (v1 = human support via webform only)
- Consumer/B2C Blue EMI support (B2B only)


## Launch Plan

*Phases align with the [scoping one-pager](blue-emi-support-scoping-one-pager.md): **Interim** → **Zendesk Build** → **End State**.*

### Interim (March 2026)

**Scale (from one-pager):** 1 merchant · ~5 tickets/week

No Zendesk build in this phase; support is Commercial-owned (Slack channel, AM escalation). This PRD’s work prepares for Zendesk Build: Zendesk configuration and Dashboard webform development can run in parallel so they are ready when the first merchant migrates off Interim.

### Zendesk Build (Q2 2026)

**Scale (from one-pager):** 5 merchants · ~10–15 tickets/week

- **Zendesk configuration**: Multibrand, email identity, org structure, ticket form, triggers, views (internal only)
- **Dashboard webform & integration**: Embed pre-populated form in Blue EMI Merchant Dashboard; test session handoff and Client ID pre-population; test trigger logic end-to-end with test organisations; UAT with CX Ops
- **Soft launch**: First Blue EMI merchants migrate to webform; CX agents briefed (training, runbook for unrecognised Client IDs, Blue EMI queue and views signed off by CX Ops lead, escalation path for P0/P1 documented); monitor queue and routing

### End State (end of 2026, target)

**Scale (from one-pager):** ~20 merchants · ~40–50 tickets/week

Full Blue EMI merchant base supported via Zendesk (if **Full Care support**); reporting baseline established. See [End State options](#end-state-options) for Full Care vs Blue EMI-owned support.

**Rollback**: Documented fallback: agents set org from `blue_emi_client_id`. If webform is down, auto-reply points merchants to P0 escalation path.


## Risks, Dependencies & Open Questions

**Dependencies**:

*Critical for any Zendesk work:*

| Dependency | Owner | Status | Risk if Delayed |
| --- | --- | --- | --- |
| Merchant data available for Blue EMI merchants, in same location as Checkout merchant data | Engineering / Data | TBC | Blocks org matching, Agent Toolkit, support@checkout.com rejection logic; no reliable Zendesk build without it |
| Clear flag that a merchant is Blue EMI vs Checkout (e.g. in merchant/org data or identity store) | Engineering / Data | TBC | Cannot route, triage, or report correctly; blocks triggers and views |
| Zendesk Multibrand enabled on account | Zendesk Admins | Confirmed ✓ | N/A |
| Blue EMI email domain and DNS setup | Blue EMI Programme / IT | TBC | Blocks branded email sending |
| Internal Blue EMI Client ID validation API | Engineering | TBC | May block org-matching on ticket creation; workaround: manual org assignment by agent |
| Zendesk org creation for all Blue EMI clients | Zendesk Admins | TBC | Blocks org auto-assignment; tickets land in catch-all |
| Dashboard webform session integration | Dashboard Engineering | TBC | Blocks pre-populated form; no merchant-facing ticket channel until resolved |
| Checkout-side: match requester email to Blue EMI client (for support@checkout.com rejection) | Engineering / Zendesk Admins | TBC | Blocks wrong-channel rejection; Blue EMI merchants could land in Checkout queue |

**Risks**:

| Risk | Likelihood | Impact | Mitigation |
| --- | --- | --- | --- |
| Merchant submits with wrong Client ID pre-populated (e.g. session error) | Low | High — ticket misrouted | Session integrity in Dashboard; merchant can confirm Client ID before submit; agent alert on unmatched org |
| Blue EMI org not yet created in Zendesk when ticket arrives | Medium | High — ticket lands in catch-all | Alert to Care Operations on unmatched ID; documented manual triage SLA |
| Same email exists under Checkout and Blue EMI orgs | High — expected | Medium | Trigger explicitly sets org from Client ID field, overriding user default; Zendesk Enterprise multi-org membership |
| Merchant discovers and uses support email directly for new requests | Medium | Low-Medium | Auto-reply redirect; no-publish policy for email address; P0 path included in bounce message |
| Agent accidentally replies from Checkout identity on a Blue EMI ticket | Low | Medium — brand confusion | Multibrand auto-assigns outbound identity; agent training |
| Blue EMI Client ID format not validated (e.g. typo) | Medium | Medium | Regex/format validation on form field + API existence check |

**Open questions**:

- [ ] What is the Blue EMI support email domain? (e.g. `support@blueemi.com`) *(Owner: Blue EMI Programme — blocks email identity and DNS setup)*
- [ ] Does an internal API exist to validate Blue EMI Client IDs, or does one need to be built? *(Owner: Engineering — needed for Zendesk org-matching webhook on ticket creation)*
- [ ] Will Blue EMI use the same SLA tiers as Checkout (Standard / Enterprise / Premium), or have separate SLA definitions? *(Owner: Care Leadership — determines whether existing Zendesk SLA policies apply or new ones are needed)*
- [ ] Is there an emergency/P0 contact channel for Blue EMI merchants (phone, dedicated email)? *(Owner: Blue EMI Programme / Care Operations — needed for the email bounce auto-reply and merchant help article)*
- [ ] How are new Blue EMI clients onboarded into Zendesk as organisations — manual, bulk import, or automated? *(Owner: Zendesk Admins — determines org creation process and whether automation is needed sooner)*
- [ ] Will End State be Full Care support (Checkout in Zendesk, temporary) or will Blue EMI have taken over support in another system by then? *(Owner: Blue EMI Programme / Care Leadership — affects long-term scope and reporting)*
- [ ] Block AM email to support@checkout.com for Blue clients: target Q2 or Q3? How to detect AM vs merchant (e.g. internal domain)? Behaviour until block is in place — wrong-channel auto-reply or manual triage? *(Owner: Care Ops / Zendesk Admins)*
- [ ] Do Blue EMI merchants have (or will they have) Salesforce records used for tiering? If not, how will SLA tier be determined in Zendesk? *(Owner: Commercial / Care Ops — affects SLA policies and reporting; see scoping one-pager challenge “No Tiering data”)*


## Timeline

| Milestone | Date | Owner | Status |
| --- | --- | --- | --- |
| PRD Complete | Feb 2026 | Charlie Wildish | 🔄 Draft |
| Open questions resolved | TBC | Multiple | ⏳ |
| Zendesk configuration complete | Q2 2026 (target) | Zendesk Admins | ⏳ |
| UAT with Care Operations | Q2 2026 (target) | Care Operations | ⏳ |
| Dashboard webform integration | Q2 2026 (target) | Dashboard Engineering | ⏳ |
| Agent training | Before first merchant | Care Operations Lead | ⏳ |
| First merchant go-live | March 2026 | Blue EMI Programme | ⏳ |


## Appendix

- [Scoping one-pager](blue-emi-support-scoping-one-pager.md) — Programme phases (Interim, Zendesk Build, End State), scale, agent impact, merchant scenarios
- [How Blue EMI differs from Checkout (Project Moon context)](../01-knowledge-base/payment-domain/How Blue EMI differs from Checkout (Project Moon context).md) — Blue EMI vs Checkout entity and identifiers
- `01-knowledge-base/products/checkout-products.md` — Support Ticket Inbox and Zendesk channel overview
- `01-knowledge-base/products/care-success-plans.md` — SLA tiers and channel entitlements
