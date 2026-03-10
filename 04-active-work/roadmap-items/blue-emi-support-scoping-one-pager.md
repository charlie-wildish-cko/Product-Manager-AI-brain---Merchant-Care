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
- Blue EMI merchants have their own Client ID, Entity ID, and Processing Channels — separate from any Checkout identifiers they may also hold
- A merchant can be on **Checkout only**, **Blue EMI only**, or **both** at the same time — the same contact email does not uniquely identify which relationship a support request belongs to
- There is currently **no support infrastructure** for Blue EMI; without deliberate setup, tickets would land in Checkout queues with no entity context, causing misrouting and SLA failures

---

## **The Challenge**

The biggest areas we need to answer.


| Problem                                                                    | Impact                                                                                                                                                                                    |
| -------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| No Blue EMI support channel exists                                         | No route for merchants to raise tickets before March                                                                                                                                      |
| Unclear if Salesforce record for these merchants                           | No Tiering data to determine SLAs in Care/Zendesk                                                                                                                                         |
| Blue EMI and Checkout identifiers are different                            | Tickets cannot be automatically matched to the correct entity without the Blue EMI Client ID                                                                                              |
| Same merchant can hold both a Checkout and a Blue EMI relationship         | Email address alone cannot determine entity context, mandatory client-level identifier required on every ticket                                                                           |
| Zendesk org data and branded email are not yet configured                  | Full Zendesk solution is a Q2 build; cannot rely on it for March go-live                                                                                                                  |
| Complaints must be handled under the Blue EMI entity, not Checkout         | A separate complaints email and routing path is required for Blue EMI from the start                                                                                                      |
| Agent Toolkit (Zendesk) only works with Checkout client/payment data today | Agents cannot look up Blue EMI clients or query Blue EMI payment context using existing tooling — both the User Profile search and the Payment Tool need to support Blue EMI data sources |


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

**What**: Merchants submit tickets via a Dashboard webform; Blue EMI is a fully configured Zendesk brand.

**Effort to build from Product team:** X weeks ZD config, X weeks Eng

**Merchant experience:** Can use Dashboard webform to submit support requests to Care. AM still an option.

**Impact to agents:** Dedicated Blue EMI queue; every ticket shows Blue EMI Client ID, entity, and brand so agents always have the right context. Agent Toolkit (User Profile + Payment Tool) works for Blue EMI clients. Replies must go out from the Blue EMI identity. Wrong-channel emails are bounced before they reach the queue. Dual-entity merchants: ticket context (brand/org) makes it clear which relationship is in scope. New workflows and views to learn.

- Blue EMI Multibrand configured in Zendesk (separate brand, email identity, views/queues)
- Dashboard webform is the only submission channel — requires login; Blue EMI Client ID is pre-populated from session, removing manual entry and misrouting risk
- Direct email to support address auto-replies directing merchant to log in to the Blue EMI Dashboard; ticket is closed without entering the queue
- Zendesk organisation per Blue EMI client, matched on Client ID, one org regardless of whether that merchant also has a Checkout org
- Dedicated agent queue for Blue EMI tickets; Client ID, entity, and brand identity visible on every ticket
- Branded outbound emails (confirmation, agent replies, CSAT) from Blue EMI identity
- **Complaints**: Blue EMI complaints email mapped to the Blue EMI Zendesk brand; enriched only against Blue EMI client data
- **Agent Toolkit — User Profile**: search-by-client-ID must return Blue EMI clients and surface Blue EMI merchant context; agents handling dual-entity merchants must see the correct entity for the ticket in scope
- **Agent Toolkit — Payment Tool**: must accept Blue EMI Client IDs and query Blue EMI payment data; current tool queries Checkout data sources only

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

**Impact to agents (if we build in Care side):** Dedicated Blue EMI queue; every ticket shows Blue EMI Client ID, entity, and brand so agents always have the right context. Agent Toolkit (User Profile + Payment Tool) works for Blue EMI clients. Replies must go out from the Blue EMI identity. Wrong-channel emails are bounced before they reach the queue. Dual-entity merchants: ticket context (brand/org) makes it clear which relationship is in scope. New workflows and views to learn.

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
| **Blue EMI merchant** | Emails ++[support@checkout.com](mailto:support@checkout.com)++ or ++[complaints@checkout.com](mailto:complaints@checkout.com)++ | If sender is matched to a **Blue EMI client**, **reject**: auto-reply that this is not the right channel, with instructions to submit via the Blue EMI Dashboard (and escalation path if urgent). Ticket closed; does not enter Checkout queue. |
| **Blue EMI merchant** | Submits via Blue EMI Dashboard or emails ++[complaints@blueemi.com](mailto:complaints@blueemi.com)++                            | Ticket created in Zendesk linked to **Blue EMI client/org only**; Blue EMI queue and branding.                                                                                                                                                  |
| **Checkout merchant** | Submits via Checkout Dashboard                                                                                                  | Ticket created in Zendesk linked to **Checkout client/org only**; Checkout queue and branding.                                                                                                                                                  |
| **Checkout AM**       | Uses internal support form; picks Checkout or Blue client                                                                       | Ticket maps to the **relevant client/org in Zendesk** (Checkout or Blue EMI depending on selection).                                                                                                                                            |
| **Checkout AM**       | Emails ++[support@checkout.com](mailto:support@checkout.com)++ about a Blue client                                              | **Plan to block** AM email submissions for Blue clients from Q2/Q3 — AMs should use the internal form and select Blue client instead. Until then: treat as wrong channel or manual triage (TBC).                                                |


*Dual-entity/client merchants:* The channel and submission path determine which identity is used; email to ++[support@checkout.com](mailto:support@checkout.com)++ from a known Blue EMI client must be redirected to Blue, not handled as Checkout. Same for Complaints emails.

---

## **Assumptions & Dependencies**


| Item | Owner | Required for | Status |
| ---- | ----- | ------------ | ------ |



| Item                                                                                                                                                          | Owner                            | Required for                                                                 | Status                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- | ---------------------------------------------------------------------------- | ------------------------------------------- |
| Blue EMI Client ID, Entity ID, and Processing Channel data available in a queryable source, flag to determine it is Blue EMI vs Checkout - **CRITICAL**       | Engineering / Blue EMI Programme | Zendesk build: Dashboard session pre-population; org matching; Agent Toolkit | TBC                                         |
| Blue EMI Dashboard user management data accessible - **CRITICAL**                                                                                             | Dashboard Engineering            | Zendesk build: Dashboard webform                                             | TBC                                         |
| Internal Blue EMI Client ID validation                                                                                                                        | Engineering                      | Zendesk build: org-matching on ticket creation                               | TBC — confirm if exists or needs building   |
| Zendesk orgs created per Blue EMI client (manual or bulk import for v1)                                                                                       | Zendesk Admins                   | Zendesk build: org-based routing                                             | TBC                                         |
| Blue EMI complaints email address defined                                                                                                                     | Blue EMI Programme               | Interim (complaints) + Zendesk build                                         | TBC                                         |
| Blue and Checkout client/entity identifiers are always distinct and cannot collide                                                                            | Blue EMI Programme / Engineering | All phases                                                                   | Assumed — must be confirmed                 |
| Ticket volume: 5 tickets per merchant per week (used for scale in each phase)                                                                                 | Care Ops / Programme             | Resourcing and queue sizing                                                  | Working assumption — revisit with real data |
| SLA tiers for Blue EMI merchants defined                                                                                                                      | Care Leadership                  | Zendesk build: SLA policies                                                  | TBC                                         |
| Emergency escalation path for Blue EMI merchants defined                                                                                                      | Blue EMI Programme / Care Ops    | Interim + Zendesk build (bounce auto-reply)                                  | TBC                                         |
| Agent Toolkit updated to support Blue EMI client search and payment data                                                                                      | Engineering                      | Zendesk build: agent triage                                                  | TBC — scope not yet assessed                |
| Checkout-side: match requester email to Blue EMI client (++[support@checkout.com](mailto:support@checkout.com)++ rejection); same logic for complaints emails | Engineering / Zendesk Admins     | Zendesk build: wrong-channel redirect                                        | TBC                                         |
| Block AM email to ++[support@checkout.com](mailto:support@checkout.com)++ for Blue clients (use internal form instead)                                        | Care Ops / Zendesk Admins        | Target Q2/Q3; behaviour until then TBC                                       | TBC                                         |


---

## **Open Questions**

- Is Blue EMI merchant and user data available in source systems? Is there a flag to identify a Blue EMI client vs a Checkout one?
- **Interim manual ticket creation**: When an AM escalates an issue to Care during the interim phase, is Blue EMI client data available in Zendesk to associate the ticket to the correct org? If not, are agents expected to create orphan tickets and reconcile later?
- **Complaints email**: What address is being used? Who is operationally responsible during the interim phase? If ++[complaints@blueemi.com](mailto:complaints@blueemi.com)++ is pointed at ++[complaints@checkout.com](mailto:complaints@checkout.com)++, we need a way to know whether the merchant contacted Checkout vs Blue directly so the ticket can be assigned the correct client ID (Checkout vs Blue EMI).
- **SLA tiers**: Does Blue EMI inherit Checkout's Standard / Enterprise / Premium tiers, or are new tiers needed?
- **Interim exit criteria**: What triggers the decision to move from Slack to Zendesk webform for the March merchant?
- **Agent Toolkit scope**: Which parts need updating for Blue EMI — both User Profile (client search) and Payment Tool (payment data query)? What data sources does each component need to connect to, and does Blue EMI have those APIs available?
- **End State**: Will Phase 3 be Full Care support (Checkout in Zendesk, temporary) or will Blue EMI have taken over support in another system (TBC) by then?

---