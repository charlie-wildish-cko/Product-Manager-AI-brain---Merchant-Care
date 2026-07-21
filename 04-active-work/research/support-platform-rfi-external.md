# Checkout.com — Support Platform RFI

## About this document

Checkout.com is evaluating platforms to run our merchant and consumer support operation. This document sets out our functional and commercial requirements. We ask each vendor to respond against every requirement and answer every "Key question".

**How to respond**: For each requirement, state whether the capability is:

- **Native** — out of the box, no configuration
- **Configuration** — available through standard configuration
- **Add-on** — available as a separately priced module
- **Custom build** — achievable only via API/custom development
- **Not supported**

Please include documentation links and a reference customer wherever possible. Where a capability is on your roadmap, give an expected availability date.

**Scale**: Responses should assume a projected requirement of up to 500 agents and a support operation spanning business (B2B) and consumer (B2C) customers.

**Confidentiality**: This document and your response are confidential and shared under the terms of our mutual NDA.

---

## 1. Multi-channel entry points

- **Email ingestion** — native ticket creation from inbound email, with reply, reply all, threading, cc/bcc, and per-agent signatures.
- **Email user enrichment** — identify the sender and match their email to the correct business/organisation record. Some addresses belong to multiple organisations, and the customer is not always known when they first reach us. Describe how the platform minimises contacts going unmatched or unrouted.
- **AI agent escalation** — receive handoff from an external AI agent (Intercom Fin) with the full conversation transcript and metadata passed into the agent workspace.
- **Live chat with human agent** — native or integrated chat for B2B, with conditional intake forms (bug reports, feature requests, general enquiries).
- **Instant messaging channels** — Slack and Microsoft Teams as B2B support channels (future requirement). WeChat is a possible future requirement: is it supported?
- **Phone channel** — native or integrated IVR and call routing for B2C. If not native, describe the integration path with third-party telephony providers to create tickets from calls.
- **Mobile app chat** — B2C channel; chat widget or API embeddable in a mobile app.
- **Internal ticket submission** — internal account teams can raise tickets on behalf of customers without consuming a full agent seat.
- **Domain mapping** — link email domains to an organisation/business record (e.g. `@example.com` maps to the Example organisation).
- **Multi-environment support at user and business level** — we support users from both sandbox and production environments. Can the platform determine which environment a user belongs to within an organisation? A user may have access to sandbox only (e.g. a developer), production only, or both.
- **Region / contracting-entity enrichment** — match a customer to a region or contracting-entity attribute and write it to a field usable for routing, via API. Populated from an external source; the platform is not expected to derive it. Supports region-based routing (see section 3).

**Key question**: Which channels are native vs. add-on, and what is the per-channel cost at 500-agent scale?

---

## 2. AI triage and classification

- **Auto-classification on escalation** — taxonomy tags applied automatically before human assignment, including urgency detection.
- **AI agent handoff with context** — transcript and metadata passed to the agent workspace on escalation from an external AI agent.
- **Pluggable AI layer** — must allow an external AI system of ours to operate without requiring the platform's native AI. We must be able to use our own AI, the platform's AI, or both, without lock-in.

**Key questions**:
- Can the platform accept AI classifications from an external system (apply labels/tags, set fields, set priority, route) via API or webhook, without using the platform's native AI?
- Intercom Fin classifies contacts using synced fields and passes the result back on handoff to a human. Do you support field syncing with Fin?

---

## 3. Routing and field logic

- **Support plan / tier routing** — route based on customer tier (P0–P3), with tier available as a condition in routing, SLA assignment, and prioritisation.
- **Skill-based routing** — match agent skill tags to ticket classification; teams configurable by skill, function, and region.
- **SLA per tier and taxonomy value** — different SLA clocks per priority and per contact type. Can SLA assignment be decoupled from tier and driven by workflow rules?
- **Customisable ticket and customer fields** — company/account-level and individual/ticket-level fields, both usable as conditions and actions in routing rules.
- **Flexible tagging/field system** — for taxonomy mapping and analytics; all fields and tags available for queue filtering and reporting.
- **Flexible routing system** — branching logic and fallbacks using any combination of tags, ticket fields, account fields, tier, and channel. Describe the level of programmatic control available via API.
- **Presence-aware ("follow-the-sun") routing** — route based on which agents and sites are currently online (login/presence state), automatically shifting distribution to active regions as other regions go offline, without manual queue switching.
- **Business-hours schedules per site/timezone** — multiple independent business-hours schedules; distinct in-hours vs out-of-hours routing; hold/pending queues that release to the next region's shift.
- **Geographic / entity-based routing** — route on a customer region or contracting-entity attribute held at account or ticket level, sending different regions to different sites or teams.
- **Queue-view scoping by attribute** — restrict which tickets an agent or site can see or pull, based on a region/segment attribute, to prevent cherry-picking and enforce workload segregation. This is distinct from the B2B/B2C data separation described in section 5.
- **Push and pull queue models** — support both automated push (capacity-based, no cherry-picking) and manual pull views, and freeze or lock views at shift boundaries.
- **Capacity controls and handoff mode** — per-agent concurrent-ticket caps, and the ability to block new assignments to agents or sites approaching end of shift ("handoff mode").
- **Conditional routing on computed thresholds** — redirect or cap volume automatically when a rolling operational metric (e.g. a volume-mix ratio by attribute over a rolling window) crosses configurable thresholds.
- **Automated ownership release on SLA-breach risk** — when the assigned agent is off-shift and the SLA will breach before their next shift, automatically un-assign the ticket and push it to an active queue/site. Predictive (time-to-breach) calculation, configurable per priority tier.

**Target routing flow to support**:
1. Ticket arrives.
2. Enrich via email lookup to populate fields.
3. Fields determine SLA and route to specific agents via skill matching.
4. Priority ranking set from SLA timer, query type, etc.
5. Agent receives an auto-routed ticket (no cherry-picking) and resolves.
6. Capacity controls on how many tickets each agent holds.

**Key question**: How does the platform route across multiple regions/sites based on real-time agent presence, and can routing rules react to computed rolling metrics rather than only to static field values?

---

## 4. Agent workspace

- **Custom app framework** — developer SDK/API for sidebar apps. We are building a custom AI assistant to run in the agent-workspace sidebar. Describe the framework: can a sidebar component render custom UI, fetch and display live data from our own systems, and write back to the ticket? How customisable is the content of a sidebar panel?
- **App capability scope** — custom apps can read ticket data, make external API calls, and write back to tickets.
- **App deployment and versioning** — deployable by our team without vendor involvement or marketplace approval.
- **Live customer data panel** — CRM and user data surfaced from our own sources in the ticket view.
- **Internal escalation** — native bi-directional Jira integration (create/update issues from tickets, sync status back), plus custom API integrations with read/write access.
- **Agent-triggered workflow execution** — an agent approves an AI-proposed action, and the platform passes an execution signal to an external system (via HTTP action or webhook).
- **Internal collaborator access** — read and comment access for non-agent staff without a full agent seat.

**Key questions**: What is the custom app development framework? Are there restrictions on what custom apps can read or write?

---

## 5. Data and permissions

- **B2B / B2C data wall** — two isolated environments; an outsourced (BPO) team handling B2C must never see B2B data. Describe the isolation mechanism (separate workspaces, RBAC, or both).
- **Role-based access control** — granular permissions per team and per brand, with custom roles for agents, leads, and admins.
- **500-agent scale** — support projected headcount without degraded performance or disproportionate cost.
- **Flexible data model** — custom objects and fields sufficient to model our organisation hierarchy and platform/reseller data, including surfacing live external data without storing it in the platform.

**Key question**: Does the platform support custom object models, or are organisations and users a fixed schema? Which core objects are extensible via custom fields, and can external identifiers be associated with platform objects?

---

## 6. Customer-facing experience

- **Customer ticket portal** — customers can view open tickets and conversation history. Describe both a hosted portal and any headless/API-driven option where we build the front-end.
- **AI chat history visibility** — previous AI agent conversations visible alongside ticket history, stored as part of the ticket timeline for both agents and customers.
- **Account team thread visibility** — account managers can view and reply into ticket threads over email, with internal notes for collaboration that are not visible to the customer.

---

## 7. Integrations (must-have)

- **Intercom Fin** — inbound escalation with full conversation context. Provide a reference customer running Fin escalation into your platform.
- **Jira** — bi-directional; create/update issues from tickets and sync status back.
- **Salesforce** — read and sync case numbers and customer data; state whether write-back is supported.
- **Knowledge sources** — inbound sync of content from an external source (URL, sitemap, or code repository). State which formats and connectors are supported.
- **Custom APIs** — pull data from internal systems (e.g. a cloud data warehouse); call external APIs from workflows; full read/write via API and webhooks.

**Key question**: What knowledge sync mechanisms are supported? Is sync automated on change, or manual?

---

## 8. Analytics and data extract

- **API access to ticket data** — full export for an analytics pipeline (API and CSV); state any native ELT connector and its availability date.
- **Taxonomy-level reporting** — filter and group by custom taxonomy tags and ticket fields.
- **SLA breach alerting** — automated alerts before and on breach, configurable per tier, surfaced in the agent workspace and via Slack/email.
- **AHT / agent task-time measurement** — do you have native average-handle-time or agent task-time measurement?

---

## 9. Environment and configuration deployment

- **Sandbox / test environment** — mirrors production configuration and keeps test data isolated from production.
- **Configuration promotion path** — a defined mechanism to promote configuration (workflows, fields, tags, tiers, SLAs) from test to production.

**Key question**: Is there a supported configuration promotion workflow between sandbox and production (e.g. push-button deploy), or must promotion be scripted via API?

---

## 10. Vendor reliability and operational trust

- **Uptime SLA** — contractual commitment for core ticketing.
- **Enterprise support SLA** — guaranteed human response time for P1/P2 issues; human-first, not bot-first deflection.
- **Named account team** — dedicated enterprise contact with a defined escalation chain.
- **Billing dispute resolution** — documented process with a defined resolution timeline.
- **Auto-renewal protection** — minimum 60-day written notice required before automatic renewal.
- **Vendor continuity** — evidence of operation and financial stability over a multi-year horizon.

**Key questions**: What are the contractual commitments for support response times? Is the company profitable or funded for the multi-year term? What financial-services domain experience do you have?

---

## 11. Pricing

- **All-in cost at 500 agents** — seats plus any required add-ons. State what is included in the seat price and what is billed separately.
- **Cost predictability** — 12-month cost modellable with reasonable confidence. State whether pricing is seat-based, usage-based, or per-ticket.
- **Add-on gating transparency** — required features documented as included or separately billed.
- **Volume discount terms** — enterprise pricing at projected multi-year contact volumes.

---

*Please return your completed response and any supporting documentation to your Checkout.com point of contact.*
