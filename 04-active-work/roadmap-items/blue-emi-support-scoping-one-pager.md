---

## confluence_space_key: MTC

confluence_parent_page_id: "8041431176"
confluence_page_id: "8058863739"

# Blue EMI (Project Moon) — Merchant Care: Scoping Overview

**Owner**: Charlie Wildish  
**Last Updated**: February 2026  
**Status**: Scoping  
**Audiences**: Commercial, Engineering, Programme Management, Care Operations

---

## **Context**

**Blue EMI** (internal alias: **Project Moon**) is a new legal entity distinct from Checkout through which a subset of merchants will process payments. It operates as a white-label product on the Checkout platform but is fully separate in legal, regulatory, and brand terms.

- **March 2026**: First Blue EMI merchant goes live (1 merchant)
- **End H1 2026**: ~5 merchants expected
- Blue EMI merchants process under the same Checkout Client ID but under a distinct Blue EMI Entity with its own Entity ID and Processing Channels
- A merchant can be on **Checkout only**, **Blue EMI only**, or **both** at the same time — the same contact email does not uniquely identify which relationship a support request belongs to
- There is currently **no support infrastructure** for Blue EMI; without deliberate setup, tickets would land in Checkout queues with no entity context, causing misrouting and SLA failures

---

## **The Challenge**

The biggest areas we need to answer.


| Problem                                                                                                             | Impact                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Entity ID is the only way to attribute a ticket to Blue EMI, and it can only be captured via the Dashboard webform  | Email contacts carry no Entity ID; a merchant on both Checkout and Blue EMI cannot be automatically attributed to the correct entity from email alone                                     |
| What happens when a Blue EMI merchant contacts support via email is undecided                                       | Without a defined handling path, email contacts either land in the Checkout queue unattributed or go unrouted — and if entity-level reporting is required, all tickets must come via the webform |
| Zendesk configuration approach not confirmed                                                                        | Whether Blue EMI needs a separate Zendesk brand, email identity, and dedicated agent queue is an open decision; this blocks full scoping of the Zendesk build                             |
| Complaints must be handled under the Blue EMI entity, not Checkout                                                  | A separate complaints routing path to the correct Blue EMI org in Zendesk is required from go-live                                                                                        |


---

## **Phases**

### **Interim (March 2026, Commercial-owned)**

**Scale**: 1 merchant · ~<5 tickets/week *(assumption: 5 tickets per merchant per week)*

**What**: Managed Slack channel per merchant, with the Account Manager and merchant contact.

**Why**: Zendesk infrastructure is not ready; this covers the single March merchant without requiring engineering work.

**Effort to build from Product team:** n/a

**Merchant experience:** Raise issues with Account managers to resolve.

**Impact to agents:** Low volume; tickets reach Care only when the AM escalates. Agents create tickets manually and must associate them to the correct Blue EMI org if that data exists in Zendesk. No dedicated Blue EMI queue yet — risk of tickets landing in Checkout queue or catch-all. All replies are Checkout-themed. Training needed on when and how to attach Blue EMI client/org.

- Commercial / AM owns the channel and first-line triage
- If the issue requires a Zendesk ticket, the AM must escalate to Care and Care agent creates it manually, only possible if Blue EMI client data is available to associate it with the correct organisation in Zendesk
- No self-serve or webform for the merchant; all contact is through the AM
- **Complaints**: Separate Blue EMI complaints email address must be set up and forwarded/handled manually during this phase
- **Email replies**: No Blue EMI brand yet, any ticket replies or confirmations are Checkout-themed (same as today's support)

**Exits when**: Zendesk build is ready and the merchant migrates to the webform channel.

---

### **Zendesk Build (Q2 2026)**

**Scale**: 5 merchants · ~10-15 tickets/week *(assumption: 5 tickets per merchant per week)*

**What**: Merchants submit tickets via a Dashboard webform (dashboard.blueemi.com); Zendesk configured with Blue EMI org structure and Entity ID field. Whether Blue EMI also requires a separate Zendesk brand, email identity, and dedicated agent queue is an open decision.

**Effort to build from Product team:** X weeks ZD config, X weeks Eng

**Merchant experience:** Can use Blue EMI Dashboard webform to submit support requests to Care. AM still an option.

**Impact to agents:** Every ticket shows Blue EMI Entity ID and org so agents have the right context. Agent Toolkit (User Profile + Payment Tool) works for Blue EMI Entity IDs. Dual-entity merchants: ticket org makes it clear which entity is in scope. Whether a dedicated Blue EMI queue and branded outbound email are required is a pending decision.

- Dashboard webform (dashboard.blueemi.com) is the primary submission channel — requires login; Blue EMI Entity ID is pre-populated from session, removing manual entry and misrouting risk
- `blue_emi_entity_id` custom ticket field; Zendesk organisation per Blue EMI entity, matched on Entity ID
- Trigger: form submission → auto-assign correct Blue EMI org based on Entity ID
- What happens when a merchant emails a support address directly: **open question** (Entity ID not available from email)
- Whether a dedicated Blue EMI agent queue and branded outbound emails are needed: **open question** (depends on branding decision)
- **Complaints**: Blue EMI complaints routed to the correct Blue EMI org in Zendesk
- **Agent Toolkit — User Profile**: search-by-entity-ID must return Blue EMI entities and surface Blue EMI merchant context
- **Agent Toolkit — Payment Tool**: must accept Blue EMI Entity IDs and query Blue EMI payment data; current tool queries Checkout data sources only

---

### **End State (end of 2026, target)**

**Scale**: ~20 merchants · ~40-50 tickets/week *(assumption: ~2 tickets per merchant per week)*

**Effort to build from Product team:** X weeks ZD config, X weeks Eng

**What**: Two possible directions not yet decided:


| Option                | Description                                                                                                                                                |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Full Care support** | Checkout/Care continues to support Blue EMI merchants in Zendesk (current Phase 3 plan). This is intended to be **temporary** until Blue EMI takes over.   |
| **Blue EMI support**  | Blue EMI eventually takes on full support for Blue EMI merchants in **another system** (TBC). Checkout would no longer handle Blue EMI tickets in Zendesk. |


*Open question for Phase 3:* Will Checkout still be supporting Blue EMI in Zendesk, or will Blue EMI have moved to their own support system by then?

**Merchant experience:** Can use Dashboard AI Agent or webform to submit support requests to Care. AM still an option.

**Impact to agents (if we build in Care side):** Every ticket shows Blue EMI Entity ID, entity, and org so agents have the right context. Agent Toolkit (User Profile + Payment Tool) works for Blue EMI Entity IDs. Dual-entity merchants: ticket org makes it clear which entity is in scope.

**If Full Care support (current plan):**

- Fin AI agent handling first-line Blue EMI queries in Dashboard
- Automated Zendesk org creation triggered at merchant onboarding (no manual step)
- Separate Blue EMI reporting: ticket volume, SLA performance, CSAT, distinct from Checkout reporting
- Automated onboarding-to-Zendesk sync for client/entity data
- Internal support form can search for Blue EMI clients, AMs can raise tickets on behalf of merchants directly

---

## **Merchant contact scenarios**

How inbound contact is routed and which identity is used in Zendesk:


| Who                   | Channel                                                                                                                         | Behaviour                                                                                                                                                                                                                                       |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Checkout merchant** | Emails ++[support@checkout.com](mailto:support@checkout.com)++ or ++[complaints@checkout.com](mailto:complaints@checkout.com)++ | Zendesk links to Checkout client/org as today; ticket handled in Checkout queue.                                                                                                                                                                |
| **Blue EMI merchant** | Emails ++[support@checkout.com](mailto:support@checkout.com)++ or ++[complaints@checkout.com](mailto:complaints@checkout.com)++ | Entity ID not available from email — handling **TBC** (open question: treat as standard contact with no entity attribution, or redirect to Dashboard webform).                                                                                  |
| **Blue EMI merchant** | Submits via Blue EMI Dashboard (dashboard.blueemi.com) or emails ++[complaints@blueemi.com](mailto:complaints@blueemi.com)++   | Ticket created in Zendesk linked to **Blue EMI entity/org**; Entity ID pre-populated from session.                                                                                                                                              |
| **Checkout merchant** | Submits via Checkout Dashboard                                                                                                  | Ticket created in Zendesk linked to **Checkout client/org**; Checkout queue.                                                                                                                                                                    |
| **Checkout AM**       | Uses internal support form; picks Checkout or Blue entity                                                                       | Ticket maps to the **relevant entity/org in Zendesk** (Checkout or Blue EMI depending on selection).                                                                                                                                            |
| **Checkout AM**       | Emails ++[support@checkout.com](mailto:support@checkout.com)++ about a Blue entity                                              | **Plan to block** AM email submissions for Blue entities from Q2/Q3 — AMs should use the internal form and select Blue entity instead. Until then: handling TBC.                                                                               |


*Dual-entity merchants:* The channel and submission path determine which entity is in scope. Webform submissions carry the Entity ID from session. Email contacts have no Entity ID — handling for dual-entity merchants arriving via email is TBC (see Open Questions).

---

## **Assumptions & Dependencies**


| Item                                                                                                                                                          | Owner                            | Required for                                                                 | Status                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- | ---------------------------------------------------------------------------- | ------------------------------------------- |
| Blue EMI brand / Zendesk configuration decision — **BLOCKER**                                                                                                 | Care Operations / Blue EMI Programme | Zendesk build: determines scope of brand, email identity, queue, and email path requirements | Open                                        |
| Blue EMI Entity ID available in merchant session at dashboard.blueemi.com — **CRITICAL**                                                                      | Dashboard Engineering            | Zendesk build: Dashboard webform pre-population                              | TBC                                         |
| Blue EMI Entity ID and org data available in a queryable source — **CRITICAL**                                                                               | Engineering / Blue EMI Programme | Zendesk build: org matching; Agent Toolkit                                   | TBC                                         |
| Internal Blue EMI Entity ID validation API                                                                                                                    | Engineering                      | Zendesk build: org-matching on ticket creation                               | TBC — confirm if exists or needs building   |
| Zendesk orgs created per Blue EMI entity (manual or bulk import for v1)                                                                                       | Zendesk Admins                   | Zendesk build: org-based routing                                             | TBC                                         |
| Blue EMI complaints email address defined                                                                                                                     | Blue EMI Programme               | Zendesk build (complaints routing)                                           | TBC                                         |
| Blue and Checkout Entity IDs are always distinct and cannot collide                                                                                           | Blue EMI Programme / Engineering | All phases                                                                   | Assumed — must be confirmed                 |
| SLA tiers for Blue EMI merchants: confirmed same as Checkout (derived from Checkout Client ID)                                                                | Care Leadership                  | Zendesk build: SLA policies                                                  | Assumed — confirm with Care Operations      |
| Ticket volume: 5 tickets per merchant per week (used for scale)                                                                                               | Care Ops / Programme             | Resourcing and queue sizing                                                  | Working assumption — revisit with real data |
| Agent Toolkit updated to support Blue EMI Entity ID search and payment data                                                                                   | Engineering                      | Zendesk build: agent triage                                                  | TBC — scope not yet assessed                |
| Block AM email to ++[support@checkout.com](mailto:support@checkout.com)++ for Blue entities (use internal form instead)                                       | Care Ops / Zendesk Admins        | Target Q2/Q3; behaviour until then TBC                                       | TBC                                         |


---

## **Open Questions**

- **Blue EMI brand in Zendesk**: Is a separate Blue EMI brand required? This determines whether Multibrand, a separate email identity, a separate ticket form, and a dedicated agent queue are in scope. Highest-priority decision — blocks Zendesk Build planning. *(Owner: Care Operations / Blue EMI Programme)*
- **Direct email handling**: What happens when a Blue EMI merchant emails a support address directly? Entity ID cannot be captured from email. Options: treat as a standard Checkout contact (no entity attribution) or redirect to Dashboard webform (requires auto-reply). *(Owner: Care Operations)*
- **Reporting requirement for email contacts**: If entity-level reporting is required for all contacts, the webform must be the mandatory channel. *(Owner: Care Operations / Blue EMI Programme)*
- **Entity ID in session**: How is the Blue EMI Entity ID surfaced in the merchant session at dashboard.blueemi.com? Is it available in the session token/context for webform pre-population? *(Owner: Dashboard Engineering)*
- **Entity ID validation API**: Does an internal API exist to validate Blue EMI Entity IDs, or does one need to be built? *(Owner: Engineering)*
- **Complaints email**: What address is being used? Who is operationally responsible? *(Owner: Blue EMI Programme)*
- **SLA tiers**: Assumed same as Checkout (derived from Checkout Client ID). Confirm no separate tier definition is needed. *(Owner: Care Leadership)*
- **Agent Toolkit scope**: Which parts need updating — User Profile (entity search) and Payment Tool (payment data query)? What data sources does each need, and does Blue EMI have those APIs available? *(Owner: Engineering)*

---