# Blue EMI — Zendesk Support Infrastructure

**Status**: Draft  
**Owner**: Charlie Wildish  
**Last Updated**: February 2026  
**Stakeholders**: Zendesk Admins, Engineering, Care Operations, Operational Excellence, Blue EMI Programme, Merchant Experience


## Executive Summary

Blue EMI is a separate business entity through which a subset of Checkout.com merchants will process payments. These merchants have a Blue EMI Client ID distinct from their existing Checkout Client ID and must be handled as separate customers in Zendesk. This PRD covers the configuration and tooling required to route, triage, and manage Blue EMI support tickets correctly — including branded webforms, email identity, Zendesk organisation setup, and safeguards against routing failures.


## Problem

**What problem are we solving, and who has it?**  
Blue EMI merchants process payments under a different legal entity and hold a separate client ID. If support tickets from these merchants enter Zendesk without being associated to their Blue EMI identity, they will be miscategorised against their Checkout entity — causing routing errors, incorrect SLA application, and confused agent handling. We also cannot assume a merchant's email uniquely identifies their entity: the same contact may hold both a Checkout and a Blue EMI client relationship. This affects Blue EMI merchants (who need to raise support tickets for Blue EMI activity), CX agents (who need correct entity context to triage and respond), and CX Operations (who need clean reporting and queues for Blue EMI support volume).

**How are they solving it today?**  
There is no current solution. Blue EMI is a new entity. Without deliberate Zendesk configuration, inbound tickets would either fail to be submitted (no channel exists) or land in Checkout's existing support queue with no entity context.

**Why solve this now?**  
Blue EMI merchants will begin onboarding in 2026. Support infrastructure must be in place before the first merchant goes live to avoid unrouted tickets, manual triage, and SLA breaches from day one.


## Goals & Success Metrics

| Metric | Current State | Target | Timeline |
| --- | --- | --- | --- |
| % of Blue EMI tickets with a valid Blue EMI Client ID | N/A (no channel) | 100% | At launch |
| % of Blue EMI tickets correctly routed to Blue EMI queue | N/A | 100% | At launch |
| Direct-email-to-webform redirect bounce rate | N/A | <5% of inbound attempts (aim to eliminate via no-publish policy) | 3 months post-launch |
| Agent mislabelling of Blue EMI vs Checkout tickets | N/A | 0 | Ongoing |


## User Stories

### Merchant: Submitting a ticket (public webform)

**As a** Blue EMI merchant who is not logged into the Dashboard,  
**I want** to submit a support ticket via a public webform where I enter my Blue EMI Client ID,  
**So that** my ticket reaches the right support team with the correct entity context.

**Acceptance Criteria**:

- Webform is accessible without authentication
- Blue EMI Client ID is a mandatory field — form cannot be submitted without it
- Client ID is validated against known Blue EMI organisations before submission
- On submission, ticket is created in Zendesk with the correct Blue EMI org assigned
- Merchant receives a branded confirmation email from the Blue EMI support address


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
- Auto-reply clearly directs the merchant to the public webform URL and includes an emergency P0 escalation path
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
- Public-facing webform powered by this form, accessible without authentication
- Dashboard-embedded webform that pre-populates Blue EMI Client ID from session
- Zendesk Multibrand configuration for Blue EMI (separate brand, email identity, templates)
- Blue EMI support email address (e.g. `support@blueemi.com`) configured with correct DKIM/SPF
- Zendesk Organisation per Blue EMI client, with Blue EMI Client ID stored as org external ID or custom org field
- Trigger: on ticket creation via email channel with empty Blue EMI Client ID → auto-reply and close ticket
- Trigger: on ticket creation via Blue EMI form → auto-assign to correct Blue EMI organisation
- Dedicated agent view/queue for Blue EMI tickets (filtered by `blue_emi` tag or brand)
- Blue EMI Client ID field visible in ticket layout for agents

#### Should Have (P1)

- Client ID validation on public webform (live API call to confirm ID exists before form submits)
- Auto-reply for bounced email includes URL to public webform and emergency P0 escalation path
- Blue EMI branding applied to all outbound email notifications (confirmation, agent replies, CSAT)
- Alert/notification to CX Ops when a ticket arrives with an unrecognised Blue EMI Client ID
- Separate CSAT survey configuration for Blue EMI (distinct from Checkout CSAT)

#### Nice to Have (P2)

- Blue EMI merchant-facing ticket inbox (analogous to the Checkout Dashboard ticket view)
- Automated org creation in Zendesk when a new Blue EMI client is onboarded (webhook from internal onboarding system)
- Reporting dashboard separating Blue EMI ticket volume, SLA performance, and CSAT from Checkout

**Constraints**:
- **Security**: Blue EMI Client ID validation must not expose the existence or non-existence of other client IDs to unauthenticated users — return a generic validation error on failure
- **Compliance**: Ticket data for Blue EMI merchants must be handled in line with applicable data residency and retention requirements for the Blue EMI entity
- **Availability**: Webform must be available 24×7; form submission failures must degrade gracefully with a clear error message and fallback contact path
- **Performance**: Client ID validation on public webform should return within 2 seconds
- **Integrations**: Zendesk Multibrand enabled; internal Blue EMI Client ID validation API; email DNS configuration (DKIM/SPF); Dashboard webform session integration; Zendesk trigger and webhook configuration for org auto-assignment


## Approach

### Merchant Flow — Public Webform

```
1. Merchant navigates to Blue EMI public support webform URL
2. Merchant enters: Blue EMI Client ID (validated), topic, subject, description
3. On submit: Client ID validated against known orgs
   - Invalid ID → inline error, form not submitted
   - Valid ID → ticket created in Zendesk
4. Merchant receives branded confirmation email from support@blueemi.com
5. Merchant can reply to that email to continue the thread
```

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
   "To submit a support request please use our form at [URL] and include your 
    Blue EMI Client ID. For urgent payment issues (P0), contact us via [escalation path]."
4. Ticket status set to Closed
5. Ticket does not appear in active agent queue
```

### Key UX Decisions

- **Blue EMI Client ID is mandatory and validated on the public webform, not optional** — without it, tickets cannot be routed correctly; a soft field would inevitably produce unrouted tickets. (Alternative considered: optional field with agent follow-up — rejected due to SLA risk and agent overhead.)
- **Dashboard webform pre-populates Client ID from session** — eliminates entry errors for logged-in merchants; improves submission speed. (Alternative: manual entry even in dashboard — rejected as unnecessary friction.)
- **Direct email bounced to webform, not manually triaged** — manual triage of email tickets without Client ID is unsustainable; auto-reply gives merchant immediate path forward.

### Zendesk Configuration

- **Multibrand**: New Blue EMI brand with dedicated help centre, ticket form, and email identity
- **Custom Ticket Field**: `blue_emi_client_id` — text field, required on the Blue EMI form
- **Custom Org Field**: `blue_emi_client_id` on Organisation records (used for matching)
- **Organisations**: One Zendesk org per Blue EMI client; Blue EMI Client ID stored as org external ID or custom field
- **Triggers**:
  - `[Blue EMI] Set org from Client ID`: fires on new ticket from Blue EMI form → webhook to match org → update ticket org
  - `[Blue EMI] Bounce direct email`: fires on new ticket via email channel with empty `blue_emi_client_id` → auto-reply → close
- **Views**: `Blue EMI — Open`, `Blue EMI — Pending`, `Blue EMI — Recently Solved`
- **Email identity**: `Blue EMI Support <support@blueemi.com>` — DKIM/SPF configured

### Technical Notes

- `GET /internal/blue-emi/clients/{client_id}` — validates a Blue EMI Client ID exists; used by public webform before submission
- Zendesk API `PUT /tickets/{id}` — used by webhook/trigger to set organisation on ticket creation
- Zendesk Suite (Multibrand capability) must be confirmed as enabled on account
- Blue EMI email domain DNS management required for DKIM/SPF setup


## Out of Scope

- **Blue EMI ticket inbox in the Merchant Dashboard** — desirable but a separate piece of work
- **Automated Zendesk org creation at Blue EMI onboarding** — v1 assumes orgs are manually created or bulk-imported; automation is a P2 improvement
- **Blue EMI Live Chat channel** — not part of v1 support channel strategy
- **Blue EMI AI Agent (Fin)** — not in scope; human support via webform only for v1
- **Consumer/B2C Blue EMI support** — this PRD covers B2B merchants only


## Launch Plan

- **Phase 1 — Zendesk Configuration**: Set up Multibrand, email identity, org structure, ticket form, triggers, views (internal only)
- **Phase 2 — Integration & Validation**: Connect webform Client ID validation API; test trigger logic end-to-end with test organisations; UAT with CX Ops
- **Phase 3 — Dashboard Webform**: Embed pre-populated form in Blue EMI Merchant Dashboard; test session handoff
- **Phase 4 — Soft Launch**: First Blue EMI merchants onboarded; CX agents briefed (training session, runbook for unrecognised Client IDs, Blue EMI queue and views signed off by CX Ops lead, escalation path for P0/P1 issues documented); monitor queue and routing
- **Phase 5 — GA**: Full Blue EMI merchant base supported; reporting baseline established

**Rollback**: If routing triggers malfunction at launch, a manual fallback process is documented for CX Ops: agents check the `blue_emi_client_id` field and manually set the organisation. Public webform can be taken offline temporarily with a maintenance message if the Client ID validation API is unavailable.


## Risks, Dependencies & Open Questions

**Dependencies**:

| Dependency | Owner | Status | Risk if Delayed |
| --- | --- | --- | --- |
| Zendesk Multibrand enabled on account | Zendesk Admins | TBC | Blocks all brand separation |
| Blue EMI email domain and DNS setup | Blue EMI Programme / IT | TBC | Blocks branded email sending |
| Internal Blue EMI Client ID validation API | Engineering | TBC | Blocks public webform validation; workaround: accept unvalidated ID + trigger fallback queue |
| Zendesk org creation for all Blue EMI clients | Zendesk Admins | TBC | Blocks org auto-assignment; tickets land in catch-all |
| Dashboard webform session integration | Dashboard Engineering | TBC | Blocks pre-populated form; merchants use public form as fallback |

**Risks**:

| Risk | Likelihood | Impact | Mitigation |
| --- | --- | --- | --- |
| Merchant submits incorrect Client ID | Medium | High — ticket misrouted or unrouted | Client ID validation on public webform; clear field label and helper text |
| Blue EMI org not yet created in Zendesk when ticket arrives | Medium | High — ticket lands in catch-all | Alert to Care Operations on unmatched ID; documented manual triage SLA |
| Same email exists under Checkout and Blue EMI orgs | High — expected | Medium | Trigger explicitly sets org from Client ID field, overriding user default; Zendesk Enterprise multi-org membership |
| Merchant discovers and uses support email directly for new requests | Medium | Low-Medium | Auto-reply redirect; no-publish policy for email address; P0 path included in bounce message |
| Agent accidentally replies from Checkout identity on a Blue EMI ticket | Low | Medium — brand confusion | Multibrand auto-assigns outbound identity; agent training |
| Blue EMI Client ID format not validated (e.g. typo) | Medium | Medium | Regex/format validation on form field + API existence check |

**Open questions**:

- [ ] What is the Blue EMI support email domain? (e.g. `support@blueemi.com`) *(Owner: Blue EMI Programme — blocks email identity and DNS setup)*
- [ ] Does an internal API exist to validate Blue EMI Client IDs, or does one need to be built? *(Owner: Engineering — determines whether public webform validation is available at launch or deferred)*
- [ ] Will Blue EMI use the same SLA tiers as Checkout (Standard / Enterprise / Premium), or have separate SLA definitions? *(Owner: Care Leadership — determines whether existing Zendesk SLA policies apply or new ones are needed)*
- [ ] Is there an emergency/P0 contact channel for Blue EMI merchants (phone, dedicated email)? *(Owner: Blue EMI Programme / Care Operations — needed for the email bounce auto-reply and merchant help article)*
- [ ] How are new Blue EMI clients onboarded into Zendesk as organisations — manual, bulk import, or automated? *(Owner: Zendesk Admins — determines org creation process and whether automation is needed sooner)*


## Timeline

| Milestone | Date | Owner | Status |
| --- | --- | --- | --- |
| PRD Complete | Feb 2026 | Charlie Wildish | 🔄 Draft |
| Open questions resolved | TBC | Multiple | ⏳ |
| Zendesk configuration complete | TBC | Zendesk Admins | ⏳ |
| Client ID validation API ready | TBC | Engineering | ⏳ |
| UAT with Care Operations | TBC | Care Operations | ⏳ |
| Dashboard webform integration | TBC | Dashboard Engineering | ⏳ |
| Agent training | TBC | Care Operations Lead | ⏳ |
| First merchant go-live | TBC | Blue EMI Programme | ⏳ |


## Appendix

- `01-knowledge-base/products/checkout-products.md` — Support Ticket Inbox and Zendesk channel overview
- `01-knowledge-base/products/care-success-plans.md` — SLA tiers and channel entitlements
