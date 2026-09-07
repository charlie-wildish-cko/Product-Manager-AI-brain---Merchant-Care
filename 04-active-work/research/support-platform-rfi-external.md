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

- **Email ingestion** — native ticket creation from inbound email, with reply, reply all, threading, cc/bcc, and per-agent signatures. Example: a customer replies to an existing ticket by email; the reply threads onto that ticket rather than creating a duplicate.
- **Email user enrichment** — identify the sender and match their email to the correct business/organisation record. Some addresses belong to multiple organisations, and the customer is not always known when they first reach us. Describe how the platform minimises contacts going unmatched or unrouted. Example: an email from an address not yet in our CRM is still matched to the right organisation by domain rather than creating an unassigned ticket.
- **AI agent escalation** — receive handoff from an external AI agent (Intercom Fin) with the full conversation transcript and metadata passed into the agent workspace. Example: Fin escalates a query; the agent opens the ticket and sees the full chat transcript plus the tier and intent fields Fin already applied.
- **Live chat with human agent** — native or integrated chat for B2B, with conditional intake forms (bug reports, feature requests, general enquiries). Example: a customer clicks "Report a bug" in the chat widget, which pre-fills a bug-report form before the conversation reaches an agent.
- **Instant messaging channels** — Slack and Microsoft Teams as B2B support channels (future requirement). WeChat is a possible future requirement: is it supported? Example: a business customer messages support in a shared Slack Connect channel, and the message becomes a ticket in the queue.
- **Phone channel** — native or integrated IVR and call routing for B2C. If not native, describe the integration path with third-party telephony providers to create tickets from calls. Example: a consumer calls a support line, is routed by IVR based on account tier, and a ticket is created automatically with the call recording attached.
- **Mobile app chat** — B2C channel; chat widget or API embeddable in a mobile app. Example: a consumer opens chat inside a mobile app without leaving it, and the conversation appears in the same ticket timeline as web chat.
- **Internal ticket submission** — internal account teams can raise tickets on behalf of customers without consuming a full agent seat. Example: an account manager raises a ticket from a meeting note on a customer's behalf, without needing a full agent licence.
- **Domain mapping** — link email domains to an organisation/business record (e.g. `@example.com` maps to the Example organisation). Example: an email from a known domain is auto-tagged to the matching organisation record with no manual selection.
- **Multi-environment support at user and business level** — we support users from both sandbox and production environments. Can the platform determine which environment a user belongs to within an organisation? A user may have access to sandbox only (e.g. a developer), production only, or both. Example: a developer logging in with a sandbox-only account is distinguished from a customer using the same email domain in production.
- **Region / contracting-entity enrichment** — match a customer to a region or contracting-entity attribute and write it to a field usable for routing, via API. Populated from an external source; the platform is not expected to derive it. Supports region-based routing (see section 3). Example: a customer's contracting entity is written to a ticket field via API and used to route the ticket to the correct regional team.

**Key question**: Which channels are native vs. add-on, and what is the per-channel cost at 500-agent scale?

---

## 2. AI triage and classification

- **Auto-classification on escalation** — taxonomy tags applied automatically before human assignment, including urgency detection. Example: a ticket about a chargeback is auto-tagged "Disputes > Chargebacks" before it reaches an agent's queue.
- **AI agent handoff with context** — transcript and metadata passed to the agent workspace on escalation from an external AI agent. Example: Fin's classification of a query is passed to the ticket as a structured field, not just as free text in the transcript.
- **Pluggable AI layer** — must allow an external AI system of ours to operate without requiring the platform's native AI. We must be able to use our own AI, the platform's AI, or both, without lock-in. Example: our own AI system writes a suggested action to a ticket without the platform's native AI being enabled or paid for.

**Key questions**:
- Can the platform accept AI classifications from an external system (apply labels/tags, set fields, set priority, route) via API or webhook, without using the platform's native AI?
- Intercom Fin classifies contacts using synced fields and passes the result back on handoff to a human. Do you support field syncing with Fin?

---

## 3. Routing and field logic

- **Support plan / tier routing** — route based on customer tier (P0–P3), with tier available as a condition in routing, SLA assignment, and prioritisation. Example: a P0 ticket from an enterprise customer routes to a dedicated queue with a 1-hour SLA, distinct from a P3 customer's 24-hour SLA.
- **Skill-based routing** — match agent skill tags to ticket classification; teams configurable by skill, function, and region. Example: a ticket tagged "payments authentication" only routes to agents holding the matching skill tag.
- **SLA per tier and taxonomy value** — different SLA clocks per priority and per contact type. Can SLA assignment be decoupled from tier and driven by workflow rules? Example: a P1 dispute ticket gets a 4-hour SLA while a P1 general enquiry gets 8 hours, without changing the tier.
- **Customisable ticket and customer fields** — company/account-level and individual/ticket-level fields, both usable as conditions and actions in routing rules. Example: a custom account-level field is added and used as a routing condition.
- **Flexible tagging/field system** — for taxonomy mapping and analytics; all fields and tags available for queue filtering and reporting. Example: every ticket carries case-type and issue-type tags that are filterable in reporting without a custom report build.
- **Flexible routing system** — branching logic and fallbacks using any combination of tags, ticket fields, account fields, tier, and channel. Describe the level of programmatic control available via API. Example: tickets from a named account tier route to Team A, but fall back to Team B automatically when Team A is at capacity.
- **Presence-aware ("follow-the-sun") routing** — route based on which agents and sites are currently online (login/presence state), automatically shifting distribution to active regions as other regions go offline, without manual queue switching. Example: as one team logs off, new tickets start routing to the next active regional team automatically, with no manual queue switch.
- **Business-hours schedules per site/timezone** — multiple independent business-hours schedules; distinct in-hours vs out-of-hours routing; hold/pending queues that release to the next region's shift. Example: a ticket raised outside business hours sits in a holding queue and releases to the next region's team when their shift starts.
- **Geographic / entity-based routing** — route on a customer region or contracting-entity attribute held at account or ticket level, sending different regions to different sites or teams. Example: a customer contracted with a regional entity routes to that region's team; the same case type from a different-region customer routes elsewhere.
- **Queue-view scoping by attribute** — restrict which tickets an agent or site can see or pull, based on a region/segment attribute, to prevent cherry-picking and enforce workload segregation. This is distinct from the B2B/B2C data separation described in section 5. Example: an outsourced agent handling B2C tickets cannot see or pull B2B tickets from the queue view, even if idle.
- **Push and pull queue models** — support both automated push (capacity-based, no cherry-picking) and manual pull views, and freeze or lock views at shift boundaries. Example: tickets auto-assign by capacity during business hours but shift to a locked pull view for agents to self-select from near shift end.
- **Capacity controls and handoff mode** — per-agent concurrent-ticket caps, and the ability to block new assignments to agents or sites approaching end of shift ("handoff mode"). Example: an agent at their concurrent-ticket cap stops receiving new assignments, and no new tickets route to them at all in the final minutes of their shift.
- **Conditional routing on computed thresholds** — redirect or cap volume automatically when a rolling operational metric (e.g. a volume-mix ratio by attribute over a rolling window) crosses configurable thresholds. Example: if a contact type exceeds a defined share of daily volume, new tickets of that type automatically cap or redirect to a dedicated team.
- **Automated ownership release on SLA-breach risk** — when the assigned agent is off-shift and the SLA will breach before their next shift, automatically un-assign the ticket and push it to an active queue/site. Predictive (time-to-breach) calculation, configurable per priority tier. Example: if an assigned ticket will breach SLA before the agent's next shift starts, it's automatically reassigned to an active team shortly before their shift ends.

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

- **Custom app framework** — developer SDK/API for sidebar apps. We are building a custom AI assistant to run in the agent-workspace sidebar. Describe the framework: can a sidebar component render custom UI, fetch and display live data from our own systems, and write back to the ticket? How customisable is the content of a sidebar panel? Example: a sidebar panel calls our internal API to show a customer's recent activity live, without that data being stored in the platform.
- **App capability scope** — custom apps can read ticket data, make external API calls, and write back to tickets. Example: an app reads a ticket's account ID, calls an external verification API, and writes the result to a custom field the agent can see.
- **App deployment and versioning** — deployable by our team without vendor involvement or marketplace approval. Example: our team pushes an updated sidebar app version directly from CI, with no vendor marketplace review step.
- **Live customer data panel** — CRM and user data surfaced from our own sources in the ticket view. Example: an agent sees a customer's account status and recent activity pulled live from our own systems in the ticket sidebar.
- **Internal escalation** — native bi-directional Jira integration (create/update issues from tickets, sync status back), plus custom API integrations with read/write access. Example: an agent creates a Jira issue from a ticket in one click; when the linked issue closes, the ticket status updates automatically.
- **Agent-triggered workflow execution** — an agent approves an AI-proposed action, and the platform passes an execution signal to an external system (via HTTP action or webhook). Example: an agent approves an AI-suggested action, and the platform fires a webhook that triggers the actual action in an external system.
- **Internal collaborator access** — read and comment access for non-agent staff without a full agent seat. Example: a subject-matter expert can read and comment on a ticket to suggest a fix, without being issued a full agent seat.

**Key questions**: What is the custom app development framework? Are there restrictions on what custom apps can read or write?

---

## 5. Data and permissions

- **B2B / B2C data wall** — two isolated environments; an outsourced (BPO) team handling B2C must never see B2B data. Describe the isolation mechanism (separate workspaces, RBAC, or both). Example: a BPO agent logged into the B2C workspace cannot search for or view any B2B customer ticket, even by ticket ID.
- **Role-based access control** — granular permissions per team and per brand, with custom roles for agents, leads, and admins. Example: a team lead can see and reassign all tickets in their team's queue, while an agent can only see and act on their own assigned tickets.
- **500-agent scale** — support projected headcount without degraded performance or disproportionate cost. Example: dashboard and search performance doesn't degrade as the agent roster grows from 50 to 500 concurrent users.
- **Flexible data model** — custom objects and fields sufficient to model our organisation hierarchy and platform/reseller data, including surfacing live external data without storing it in the platform. Example: a custom object models a reseller/platform hierarchy without a vendor schema change.

**Key question**: Does the platform support custom object models, or are organisations and users a fixed schema? Which core objects are extensible via custom fields, and can external identifiers be associated with platform objects?

---

## 6. Customer-facing experience

- **Customer ticket portal** — customers can view open tickets and conversation history. Describe both a hosted portal and any headless/API-driven option where we build the front-end. Example: a customer logs into a portal and sees their open tickets, or the same data is exposed via API for us to build our own view.
- **AI chat history visibility** — previous AI agent conversations visible alongside ticket history, stored as part of the ticket timeline for both agents and customers. Example: an agent opens a ticket and sees the customer's earlier AI-agent conversation about the same issue in the same timeline, not a separate log.
- **Account team thread visibility** — account managers can view and reply into ticket threads over email, with internal notes for collaboration that are not visible to the customer. Example: an account manager replies to a ticket thread by email and adds an internal note visible to staff but not the customer.

---

## 7. Integrations (must-have)

- **Intercom Fin** — inbound escalation with full conversation context. Provide a reference customer running Fin escalation into your platform. Example: a live Fin escalation creates a ticket with transcript and metadata already attached.
- **Jira** — bi-directional; create/update issues from tickets and sync status back. Example: updating a Jira issue's status to "Done" automatically updates the linked support ticket without an agent touching it.
- **Salesforce** — read and sync case numbers and customer data; state whether write-back is supported. Example: a ticket displays the customer's current Salesforce case number and account owner without manual lookup.
- **Knowledge sources** — inbound sync of content from an external source (URL, sitemap, or code repository). State which formats and connectors are supported. Example: a support site's source repository is connected once, and new articles re-sync into the agent's knowledge base automatically after each update.
- **Custom APIs** — pull data from internal systems (e.g. a cloud data warehouse); call external APIs from workflows; full read/write via API and webhooks. Example: a workflow calls an internal API to pull a customer's live account data into a ticket field.

**Key question**: What knowledge sync mechanisms are supported? Is sync automated on change, or manual?

---

## 8. Analytics and data extract

- **API access to ticket data** — full export for an analytics pipeline (API and CSV); state any native ELT connector and its availability date. Example: all fields, including custom fields and comment history, for every ticket created can be extracted daily via API to feed an internal analytics pipeline.
- **Taxonomy-level reporting** — filter and group by custom taxonomy tags and ticket fields. Example: a report filters tickets by case type and issue type without a custom report build.
- **SLA breach alerting** — automated alerts before and on breach, configurable per tier, surfaced in the agent workspace and via Slack/email. Example: a Slack alert fires 30 minutes before a P0 ticket breaches SLA, and again if it actually breaches.
- **AHT / agent task-time measurement** — do you have native average-handle-time or agent task-time measurement? Example: a dashboard shows average handle time per agent per case type without a separate time-tracking app.

---

## 9. Environment and configuration deployment

- **Sandbox / test environment** — mirrors production configuration and keeps test data isolated from production. Example: a routing rule change can be built and tested against realistic ticket data in sandbox before it touches a live customer ticket.
- **Configuration promotion path** — a defined mechanism to promote configuration (workflows, fields, tags, tiers, SLAs) from test to production. Example: a "promote to production" action (button or API call) moves an approved SLA policy from sandbox to live without re-building it by hand.
- **Config as code** — configuration (routing, fields, tags, tiers, SLAs) expressible as version-controlled files, deployable via CI/CD, diffable and reviewable like application code, rather than only editable through a UI or ad hoc API scripts. Example: a new ticket field or routing rule is defined in a YAML/Terraform file, reviewed via pull request, and applied through a pipeline — with a visible diff of what changed and a rollback path if the deploy is wrong.

**Key question**: Is there a supported configuration promotion workflow between sandbox and production (e.g. push-button deploy), or must promotion be scripted via API? Does a native or supported config-as-code tool exist (e.g. Terraform provider, CLI, or vendor-native IaC), and what proportion of configuration does it cover?

---

## 10. Vendor reliability and operational trust

- **Uptime SLA** — contractual commitment for core ticketing. Example: a contractual 99.9% uptime commitment with defined service credits if breached.
- **Enterprise support SLA** — guaranteed human response time for P1/P2 issues; human-first, not bot-first deflection. Example: a P1 outage gets a guaranteed 1-hour human response, not a bot-first auto-reply.
- **Named account team** — dedicated enterprise contact with a defined escalation chain. Example: a named account manager, not a rotating support queue, is our first point of contact for escalations.
- **Billing dispute resolution** — documented process with a defined resolution timeline. Example: a disputed charge has a documented process with a committed resolution timeframe, such as 30 days.
- **Auto-renewal protection** — minimum 60-day written notice required before automatic renewal. Example: the contract requires the vendor to notify us at least 60 days before auto-renewing.
- **Vendor continuity** — evidence of operation and financial stability over a multi-year horizon. Example: evidence such as funding runway, profitability, or customer base size supporting continued operation and support over the contract term.

**Key questions**: What are the contractual commitments for support response times? Is the company profitable or funded for the multi-year term? What financial-services domain experience do you have?

---

## 11. Pricing

- **All-in cost at 500 agents** — seats plus any required add-ons. State what is included in the seat price and what is billed separately. Example: a single quote shows seat cost plus every add-on (QA, WFM, Advanced AI) required to match our current functionality at 500 agents.
- **Cost predictability** — 12-month cost modellable with reasonable confidence. State whether pricing is seat-based, usage-based, or per-ticket. Example: next year's cost can be modelled within a narrow range from our contact volume forecast, rather than being exposed to usage-based charges that spike unpredictably.
- **Add-on gating transparency** — required features documented as included or separately billed. Example: a feature comparison sheet states plainly which capabilities are included in the seat price vs. billed as a separate SKU.
- **Volume discount terms** — enterprise pricing at projected multi-year contact volumes. Example: a defined discount tier applies automatically once contact volume crosses an agreed threshold, rather than requiring a fresh negotiation each time.

---

*Please return your completed response and any supporting documentation to your Checkout.com point of contact.*
