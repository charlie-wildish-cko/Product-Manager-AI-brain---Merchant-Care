# **PRD: Blue EMI — Zendesk Support Infrastructure**

**Author:** Charlie Wildish

**Date:** February 2026

**Approvers:** TBC

**Stage:** Solution Design

**Status:** Draft

**Last Updated:** February 2026

**Stakeholders:** Zendesk Admins, Engineering, Care Operations, Operations Excellence, Blue EMI Programme, Merchant Experience

---

## **Executive Summary**

Blue EMI merchants process under the same Checkout Client ID as Checkout merchants, but under a distinct Blue EMI Entity with its own Entity ID. Because entity cannot be inferred from email alone, and the Blue EMI Dashboard (dashboard.blueemi.com) is the only place the Entity ID can be automatically captured and associated with a support ticket, the webform is the critical inbound channel for Blue EMI support. This PRD covers the Zendesk configuration needed to receive, route, and manage Blue EMI tickets: a Dashboard-embedded webform with Entity ID pre-populated from session, Zendesk org structure per Blue EMI entity, and the decisions still needed on whether Blue EMI requires separate Zendesk branding, a dedicated agent queue, or a separate email identity. Successful delivery enables Blue EMI merchants to get support from go-live and gives Care agents correctly attributed tickets.

## **Problem Space**

**Problem statement:** Blue EMI merchants have no dedicated support channel. Without it, tickets either go unrouted or land in the Checkout queue with no entity context — causing misrouting, wrong SLA application, and agent confusion. The same email address can belong to both a Checkout and a Blue EMI merchant; entity cannot be inferred from email alone.

**Who is affected:**
- Blue EMI merchants — need a structured, branded support path from go-live
- CX agents — need correct organisation and ticket context to triage and respond accurately
- Care Operations — need clean Blue EMI queues, accurate routing, and separate reporting

**Evidence:**
- Blue EMI is a new entity with onboarding commencing in 2026; there is no support channel today
- Without this configuration, tickets would either have no inbound path or land in the Checkout queue untagged
- The same email address can be associated with both a Checkout and a Blue EMI account — identity cannot be resolved from email alone; Entity ID is required
- Entity ID can only be automatically captured via the Blue EMI Dashboard webform (dashboard.blueemi.com); email contacts cannot be automatically attributed to a specific Blue EMI entity

**Why now:** Blue EMI merchant onboarding begins in 2026. Support infrastructure must be in place at first go-live to avoid unrouted tickets, manual triage, and SLA breaches from day one.

## **Goals and Success Metrics**

**Business Goals:** Ensure Blue EMI support is operationally ready at programme go-live; protect SLA performance for Blue EMI merchants; maintain clean separation between Blue EMI and Checkout ticket data for reporting and compliance.

**Merchant Goals:** Blue EMI merchants can submit support requests quickly and confidently via the Blue EMI Dashboard, without needing to supply their Entity ID manually or risk submitting under the wrong entity.

**Non-goals:**
- Blue EMI Live Chat or Fin AI on Blue EMI (v1 = human support via webform only)
- Consumer/B2C Blue EMI support (B2B only in this scope)
- Automated org creation at onboarding (deferred to P2)

**Success metrics:**

| Metric | Why it matters | Baseline | Target | Source |
| ----- | :---: | :---: | :---: | :---: |
| % of Blue EMI tickets with a valid Blue EMI Entity ID | Validates correct submission channel and enables accurate routing | N/A (no channel today) | 100% at launch | Zendesk ticket field |
| % of Blue EMI tickets correctly routed to Blue EMI queue | Measures routing accuracy; misroutes cause SLA breaches and agent confusion | N/A | 100% at launch | Zendesk views / reporting |
| % of Blue EMI ticket volume arriving via direct email (bypassing Dashboard) | Email bypass tickets require auto-reply and close; high rate signals channel adoption issue | N/A | <5% within 3 months of launch | Zendesk channel field |
| Agent mislabelling rate (Blue EMI ticket attributed to Checkout, or vice versa) | Mislabelling corrupts reporting and SLA calculations | N/A | 0 ongoing | Manual QA / Zendesk org field |

## **Customer Segments & Needs**

**Customer segment(s):** Blue EMI merchants — B2B merchants onboarded to the Blue EMI entity, initially a small cohort (~5 at Zendesk Build, ~20 by end of 2026). These merchants use the Blue EMI Merchant Dashboard (dashboard.blueemi.com) and process under the same Checkout Client ID but under a distinct Blue EMI Entity and Entity ID.

**User Stories / Jobs-To-Be-Done**

*Merchant: submitting a ticket via Dashboard*

As a Blue EMI merchant logged into the Merchant Dashboard, I want to submit a support ticket without manually entering my Blue EMI Entity ID, so that the process is fast and I cannot accidentally submit under the wrong entity.

- Dashboard webform pre-populates the Blue EMI Entity ID from the merchant's session
- Merchant can confirm but cannot clear the Entity ID field
- Ticket is created in Zendesk with the correct Blue EMI org on submission
- Merchant receives a confirmation email on submission

*Merchant: replying to a ticket via email*

As a Blue EMI merchant with an open ticket, I want to reply to email notifications to continue the conversation, so that I do not have to return to the webform for every exchange.

- Reply-to email threads correctly back to the existing ticket in Zendesk via ticket ID in headers
- No re-entry of Blue EMI Entity ID is required (already on the ticket)
- Reply is attributed to the correct requester

*CX Agent: handling a Blue EMI ticket*

As a CX agent, I want Blue EMI tickets to have the Blue EMI org and Entity ID clearly visible, so that I can triage and respond in the right context without confusion with Checkout tickets.

- Blue EMI Entity ID field is prominently displayed on the ticket
- Organisation panel shows the Blue EMI org

**Edge cases:**
- **Invalid Entity ID on submission:** Webform validation rejects the submission and surfaces an inline error asking the merchant to check their Entity ID
- **Blue EMI org not yet created in Zendesk:** Ticket creation fails gracefully, falls to a catch-all queue, and triggers an alert to Care Operations for manual triage
- **Same email exists under Checkout and Blue EMI:** User is a member of both orgs (Zendesk Enterprise); ticket org is set by trigger based on Entity ID field, not user's default org
- **Merchant replies from a different email address:** Standard Zendesk behaviour — reply is associated with the ticket via ticket ID in headers; agent is notified of the email mismatch

## **Proposed Solution & Scope**

**Solution overview:** Embed a webform in the Blue EMI Merchant Dashboard (dashboard.blueemi.com) as the primary contact channel, with the Blue EMI Entity ID pre-populated from the merchant's session. Zendesk org structure is built per Blue EMI entity for correct ticket attribution and routing. Several decisions on Zendesk configuration (separate brand, email identity, agent queue) remain open and are listed in the Open Questions section.

**Confirmed in scope:**
- `blue_emi_entity_id` custom ticket field and matching org field; one Zendesk org per Blue EMI entity
- Dashboard-embedded webform (dashboard.blueemi.com) with Blue EMI Entity ID pre-populated from session (read-only)
- Trigger: form submission → auto-assign correct Blue EMI org based on Entity ID
- Agent Toolkit (User Profile search and Payment Tool) support for Blue EMI Entity IDs and data sources
- Blue EMI complaints routed to the correct Blue EMI org in Zendesk
- Alert to Care Operations when a ticket arrives with an unrecognised Blue EMI Entity ID

**Pending decisions (see Open Questions):**
- Whether a separate Blue EMI brand is required in Zendesk (determines Multibrand configuration, separate email identity, separate ticket form)
- Whether a dedicated agent queue/view for Blue EMI tickets is required
- What happens when a Blue EMI merchant contacts support via direct email (no Entity ID available)

**Out of scope:**
- Public unauthenticated webform for Blue EMI
- Blue EMI ticket inbox in the Merchant Dashboard
- Automated org creation on merchant onboarding
- Blue EMI Live Chat or Fin AI Agent on Blue EMI
- Consumer/B2C Blue EMI support
- Separate CSAT survey configuration for Blue EMI

## **Alternatives Considered**

**Option 1 — Manual triage via Checkout queue:** Blue EMI tickets land in the Checkout queue and agents manually reassign. Viable for very low volumes but does not scale, produces dirty reporting, and risks SLA misapplication.

**Option 2 — Zendesk Multibrand with separate Blue EMI brand:** Gives Blue EMI its own Zendesk brand, email identity, ticket form, and agent queue. Provides the cleanest separation and branded experience but requires additional Zendesk configuration and a decision on whether a Blue EMI brand is needed at all. Currently an open question.

**Option 3 — Shared Zendesk brand, separate org and field only:** Blue EMI tickets route through the same Checkout Zendesk brand but with a dedicated `blue_emi_entity_id` field and org structure for attribution and routing. Simpler to configure; relies on agents correctly filtering and handling Blue EMI tickets. Viable if a separate brand is not required.

The recommended approach and which option it maps to is pending the branding decision (see Open Questions).

## **Key Assumptions and Validation**

**Critical assumptions:**

* Blue EMI Entity IDs and org records will be available in a location accessible to the Zendesk webhook and internal validation API in time for Zendesk Build. Validate by: confirming data availability and API spec with Engineering before Zendesk configuration begins.

* The Blue EMI Merchant Dashboard (dashboard.blueemi.com) can surface a pre-populated, read-only Entity ID field in the embedded webform, sourced from the merchant session. Validate by: confirming how the Entity ID is exposed in the session token/context with Dashboard Engineering.

* SLA tier is derived from the Checkout Client ID, same as today — existing Salesforce-linked tier logic applies to Blue EMI merchants without change. Validate by: confirming with Care Operations that no separate SLA tier definition is needed for Blue EMI.

## **Requirements**

### Functional Requirements

***FR-1:** Zendesk Multibrand configuration for Blue EMI.*
*Status: Pending decision — see Open Questions. Whether a separate Blue EMI brand in Zendesk is required determines whether this requirement is in scope.*

***FR-2:** Dashboard webform pre-populates Blue EMI Entity ID from merchant session.*
*Acceptance criteria: Given a merchant is logged in to the Blue EMI Dashboard (dashboard.blueemi.com), when they open the support form, then the Blue EMI Entity ID field is pre-populated and cannot be cleared; merchant can confirm and submit.*

***FR-3:** Ticket creation via form assigns correct Blue EMI org.*
*Acceptance criteria: Given a form submission includes a valid Blue EMI Entity ID, when the ticket is created, then Zendesk automatically assigns the corresponding Blue EMI organisation to the ticket.*

***FR-4:** Direct email handling.*
*Status: Pending decision — see Open Questions. What happens when a Blue EMI merchant emails a support address directly (no Entity ID available) is not yet decided.*

***FR-5:** Blue EMI sender to support@checkout.com — wrong-channel handling.*
*Status: Pending decision — see Open Questions. Depends on branding decision.*

***FR-6:** Dedicated Blue EMI agent view.*
*Status: Pending decision — see Open Questions. Whether a dedicated Zendesk view is required depends on branding and queue separation decisions.*

***FR-7:** Outbound replies use Blue EMI email identity.*
*Status: Pending decision — see Open Questions. Depends on whether a separate Blue EMI email identity is required.*

***FR-8:** Agent Toolkit supports Blue EMI Entity IDs.*
*Acceptance criteria: Given an agent enters a Blue EMI Entity ID in the Agent Toolkit (User Profile or Payment Tool), when the lookup is performed, then Blue EMI entity and payment data is returned from the appropriate Blue EMI data source.*

***FR-9:** Alert to Care Operations on unrecognised Entity ID.*
*Acceptance criteria: Given a ticket arrives with a Blue EMI Entity ID that does not match any Zendesk org, when the trigger fires, then Care Operations receives an alert (Slack notification or Zendesk internal note) to perform manual triage.*

***FR-10:** Blue EMI complaints routed to Blue EMI org.*
*Acceptance criteria: Given a complaint is received for a Blue EMI merchant (via complaints address or dashboard route), when the ticket is created, then it is assigned to the correct Blue EMI org in Zendesk — not a Checkout org.*

### Non-Functional Requirements

***NFR-1:** Webform availability.*
*Acceptance criteria: Given a Blue EMI merchant attempts to submit a ticket, when the Dashboard webform is accessed, then the form is available 24×7; form submission failures degrade gracefully with a clear error message and fallback contact path.*

***NFR-2:** Data handling.*
*Acceptance criteria: Given a Blue EMI ticket is stored in Zendesk, when accessed or exported, then ticket data is handled in line with applicable data residency and retention requirements for the Blue EMI entity (separate from Checkout data).*

## **Design and User Experience**

**Designs:** No Figma designs at this stage; the primary interface is the Blue EMI Merchant Dashboard webform. Dashboard Engineering to provide wireframes for the embedded form.

**Key UX principles:**

- **Dashboard webform as primary channel** — submission via the Blue EMI Dashboard (dashboard.blueemi.com); Entity ID is pre-populated from session and cannot be cleared
- **Entity ID pre-populated, not editable** — prevents wrong-entity submissions; merchant confirms but cannot clear
- **Direct email path** — what happens when a merchant emails a support address directly is an open question (see Open Questions); Entity ID cannot be automatically captured from email
- **Complaints** — Blue EMI complaints must be routed to the correct Blue EMI org in Zendesk

**Merchant contact scenario reference:**

| Who | Channel | Behaviour |
|-----|---------|-----------|
| Checkout merchant | Emails support@checkout.com | Linked to Checkout client/org as today; handled in Checkout queue |
| Blue EMI merchant | Emails support@checkout.com | Entity ID not available from email — handling TBC (see Open Questions) |
| Blue EMI merchant | Submits via Blue EMI Dashboard (dashboard.blueemi.com) | Entity ID pre-populated from session; ticket created linked to Blue EMI entity/org |
| Checkout merchant | Submits via Checkout Dashboard | Ticket created linked to Checkout client/org; Checkout queue |
| Checkout AM | Uses internal support form, selects Blue entity | Ticket maps to Blue EMI entity/org |
| Checkout AM | Emails support@checkout.com about a Blue entity | Block planned for Q2/Q3; AMs must use internal form. Until block: handling TBC |

## **Instrumentation and Monitoring**

**Key events to instrument:**

* Ticket created via Blue EMI Dashboard form: ticket ID, Blue EMI Entity ID, org matched (true/false), timestamp
* Ticket created via direct email (no Entity ID): ticket ID, channel, handling outcome, timestamp
* Unrecognised Entity ID alert: Entity ID submitted, alert sent (true/false), manual triage outcome

**Event properties:** blue_emi_entity_id, submission_channel (form / email), org_matched, alert_triggered

**Internal dashboards and monitoring:**

* Blue EMI ticket volume dashboard: weekly ticket count by submission channel; routing accuracy rate; unrecognised Entity ID alerts — used by Care Operations and Charlie
* SLA performance view: first response time and resolution time against SLA targets — used by Care Operations Lead
* Misrouting log: any tickets landing in a Checkout org with a Blue EMI Entity ID — used by Zendesk Admins for trigger validation

**Validation approach:**

* Pre-launch: end-to-end test with test Blue EMI org and test merchant session in staging; verify Entity ID pre-population, org assignment, and agent view filtering
* Post-launch: compare ticket count to expected volume from Blue EMI programme; validate 100% org match rate for first week; review unrecognised Entity ID alert frequency

## **Risks and Open Questions**

**Risks:**

| Risk | Likelihood | Impact | Mitigation |
| --- | --- | --- | --- |
| Merchant submits with wrong Entity ID pre-populated (session error) | Low | High — ticket misrouted | Session integrity in Dashboard; agent alert on unmatched org; merchant can confirm before submit |
| Blue EMI org not yet created in Zendesk when ticket arrives | Medium | High — ticket lands in catch-all | Alert to Care Operations on unmatched Entity ID; documented manual triage SLA |
| Same email exists under Checkout and Blue EMI orgs | High (expected) | Medium | Trigger explicitly sets org from Entity ID field, overriding user default; Zendesk Enterprise multi-org membership |
| Zendesk configuration scope not confirmed | High | High — blocks build planning | Branding decision (open question) must be resolved before Zendesk Build begins; track as blocker |
| Blue EMI Entity ID format not validated (e.g. typo) | Medium | Medium | Regex/format validation on form field + API existence check |

**Open questions:**

* **Is a separate Blue EMI brand required in Zendesk?** Determines whether Zendesk Multibrand configuration, a separate email identity, a separate ticket form, and a dedicated agent queue/view are in scope. This is the highest-priority decision — it blocks Zendesk Build planning. *(Owner: Care Operations / Blue EMI Programme)*
* **What happens when a Blue EMI merchant emails a support address directly?** Entity ID cannot be automatically captured from email — options include: treat as a standard Checkout contact with no entity attribution, or redirect to the Dashboard webform (requires auto-reply trigger). *(Owner: Care Operations)*
* **Is there a reporting requirement for Blue EMI contacts that arrive via direct email?** If entity-level reporting is required for all contacts, the webform must be the mandatory channel. *(Owner: Care Operations / Blue EMI Programme)*
* **How is the Blue EMI Entity ID surfaced in the merchant session at dashboard.blueemi.com?** Is it available in the session token/context for webform pre-population, and in what format? *(Owner: Dashboard Engineering — needed before webform build begins)*
* **Does an internal API exist to validate Blue EMI Entity IDs, or does one need to be built?** Needed for Zendesk org-matching webhook on ticket creation. *(Owner: Engineering)*
* **How are new Blue EMI entities onboarded into Zendesk as organisations?** Manual, bulk import, or automated? *(Owner: Zendesk Admins — determines org creation process)*
* **Block AM email to support@checkout.com for Blue entities: target Q2 or Q3?** How to detect AM vs merchant? Behaviour until block is in place? *(Owner: Care Operations / Zendesk Admins)*

## **Rollout Plan**

***Rollout approach:** Single phase (Zendesk Build), conditional on the branding decision being made (see Open Questions). Rollback: documented fallback is agent manually sets org from blue_emi_entity_id field.*

### ***Phase: Zendesk Build (Q2 2026)***

***Purpose:** Deliver Zendesk configuration and Dashboard webform; give Blue EMI merchants a structured support channel from go-live.*

***Entry criteria:***

* ***Business:** Blue EMI brand / Zendesk configuration approach confirmed (scope of FR-1, FR-4–FR-7 depends on this)*
* ***Technical:** Blue EMI entity data available and accessible; Blue EMI Entity ID validation API confirmed or scoped; Blue EMI Entity ID available in merchant session at dashboard.blueemi.com*
* ***Operational:** Care Operations briefed; agent training material and runbook drafted; Care Operations lead has signed off queue and views*
* ***Merchant:** First cohort of ~5 Blue EMI merchants identified*

***Success criteria:***

* *100% of Blue EMI tickets created via Dashboard webform with valid Entity ID and correct org assigned*
* *0 Blue EMI tickets misattributed to a Checkout org*
* *No P1 routing incidents in first 2 weeks*

***Timeline:** Q2 2026*

**Definition of Done:**

* **Technical:** All confirmed P0 requirements delivered and tested end-to-end; Entity ID pre-population, org assignment, and unrecognised Entity ID alert verified in production
* **Operational:** Agent training complete; runbook for unrecognised Entity IDs published; Care Operations lead sign-off on views and queue
* **Merchant:** First Blue EMI merchant cohort submitting via Dashboard successfully
* **Business:** Open questions on branding, email path, and Entity ID session availability resolved

**Timeline:**

| Milestone | Date | Owner | Status |
| --- | --- | --- | --- |
| PRD updated | March 2026 | Charlie Wildish | In progress |
| Branding / Zendesk scope decision | TBC | Care Operations / Blue EMI Programme | Pending |
| Entity ID session availability confirmed | TBC | Dashboard Engineering | Pending |
| Open questions resolved | TBC | Multiple | Pending |
| Zendesk configuration complete | Q2 2026 | Zendesk Admins | Pending |
| Dashboard webform integration | Q2 2026 | Dashboard Engineering | Pending |
| UAT with Care Operations | Q2 2026 | Care Operations | Pending |
| Agent training | Before first merchant go-live | Care Operations Lead | Pending |
| First merchant go-live | Q2 2026 | Blue EMI Programme | Pending |

**Product Dependencies:**

| Dependency | Owner | Status | Risk if Delayed |
| --- | --- | --- | --- |
| Blue EMI brand / Zendesk configuration decision | Care Operations / Blue EMI Programme | Open | Blocks scoping of FR-1, FR-4–FR-7; Zendesk Build cannot be fully planned until resolved |
| Blue EMI entity data available and accessible for org matching and Agent Toolkit | Engineering / Data | TBC | Blocks org assignment and Agent Toolkit; no reliable Zendesk build without it |
| Blue EMI Entity ID available in merchant session at dashboard.blueemi.com | Dashboard Engineering | TBC | Blocks webform pre-population; Entity ID must be in session context |
| Internal Blue EMI Entity ID validation API | Engineering | TBC | May block org-matching on ticket creation; workaround: manual org assignment |
| Blue EMI Zendesk orgs created for all entities | Zendesk Admins | TBC | Blocks org auto-assignment; tickets fall to catch-all |
| Zendesk Multibrand enabled on account (conditional) | Zendesk Admins | Confirmed | Only required if separate Blue EMI brand is confirmed |

**Go-to-market:**

- **Operational enablement:** Care Operations agent training on Blue EMI ticket handling and escalation paths (Owner: Care Operations Lead); runbook for unrecognised Entity IDs (Owner: Operations Excellence); Blue EMI queue and views signed off by Care Operations (Owner: Zendesk Admins)
- **Merchant communications:** Blue EMI merchants informed of support channel (Dashboard webform URL, what to expect) as part of onboarding (Owner: Blue EMI Programme / Merchant Experience)
- **Internal tooling:** Agent Toolkit updated with Blue EMI data sources before first merchant go-live (Owner: Engineering)
- **Developer materials:** N/A — no external API or developer-facing integration in this scope

## **Appendix**

**Strategy and Research:**

* [Scoping one-pager](blue-emi-support-scoping-one-pager.md) — programme phases (Interim, Zendesk Build, End State), scale projections, agent impact, merchant scenarios
* [How Blue EMI differs from Checkout (Project Moon context)](../../01-knowledge-base/payment-domain/How%20Blue%20EMI%20differs%20from%20Checkout%20(Project%20Moon%20context).md) — Blue EMI vs Checkout entity and identifiers

**Technical and Commercial:**

* `01-knowledge-base/products/checkout-products.md` — Support Ticket Inbox and Zendesk channel overview
* `01-knowledge-base/products/care-success-plans.md` — SLA tiers and channel entitlements
