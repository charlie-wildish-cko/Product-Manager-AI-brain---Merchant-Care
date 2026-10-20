# Support Platform Vendor Requirements (RFI)

**Purpose**: Requirements and questions issued to vendors evaluated to replace Zendesk. Vendor-agnostic. Send this to each vendor; capture their responses separately and score against `support-platform-vendor-scorecard.md`.
**Owner**: Charlie Wildish
**Related**: `support-platform-vendor-scorecard.md` · `support-platform-assessment-customer-references.md` · `vendor-poc-scope.md` · `05-archive/2026/investigations/zendesk-platform-decision-rfc.md` (archived RFC, decision record)

Instructions to vendors: for each requirement, state whether the capability is native, available via configuration, available via paid add-on, achievable only via custom build, or not supported. Provide documentation links and a reference customer where available. Answer every "Key question".

**Structure (revised 2026-09-18)**: Categories are organised around seven assessment principles, not the platform's own feature groupings:

1. Flexible channels, data model and routing — identify a customer on contact and route cleanly through their support channels; no lock-in to a vendor's data model
2. Integration ease — integrates well with other systems to receive and pass data
3. AI compatibility — can embed vendor and custom AI agents for both customers and Ops agents
4. Agent experience — the interface agents work in, and how they experience routing (queue views, capacity, handoff), not the routing rules themselves
5. Config as code — enhance our stack and deploy systematically at velocity
6. Partnership and reliability — strategic partner fit, plus operational/contractual reliability
7. Pricing — won't be a long-term cost burden, provides ROI

Customer-facing experience is kept as its own category (external-facing surface, distinct from the internal agent experience).

**Not a vendor requirement**: "Abstract our core services" — the principle that orchestration of customer enrichment/lookup, support channels, AI involvement, and content generation stays under our control, not the vendor's — is an internal engineering design constraint. It isn't scored directly; it governs how categories 2, 3, and 4 are read (e.g. a vendor's AI or app framework that can't be called from outside, or that requires our logic to live inside their platform, should score lower on those categories even if the feature nominally exists).

---

## 1. Flexible channels, data model and routing

**Channels**

- **Email ingestion** — native ticket creation from inbound email, with reply, reply all, threading, cc/bcc, and per-agent signatures. Example: a merchant replies to an existing ticket by email; the reply threads onto that ticket rather than creating a duplicate.
- **Email user enrichment** — identify the sender and match their email to the correct business/organisation record. We have trouble today matching emails to the right org: some addresses belong to multiple orgs, and we don't always know who the customer is when they reach our systems. How does the platform minimise contacts "falling through the cracks"? Example: an email from `jane@platformco.com`, not yet in our CRM, is still matched to "PlatformCo" by domain rather than creating an unassigned ticket.
- **Domain mapping** — link email domains to an organisation/business record in our data (e.g. `@checkout.com` maps to the Checkout.com organisation). Example: an email from `@checkout.com` is auto-tagged to the Checkout.com organisation record with no manual selection.
- **AI agent escalation path** — receive handoff from an external AI agent (Fin) with the full conversation transcript and metadata passed into the agent workspace. Example: Fin escalates a settlement query; the agent opens the ticket and sees the full chat transcript plus the tier and intent fields Fin already applied.
- **Live chat with human agent** — native or integrated chat for B2B, with conditional intake forms (bug reports, feature requests, general enquiries). Example: a merchant clicks "Report a bug" in the chat widget, which pre-fills a bug-report form before the conversation reaches an agent.
- **Instant messaging channels** — Slack and Microsoft Teams as B2B support channels (2028–2029 requirement). WeChat is a possible future requirement: is it supported? Example: a Platform partner messages support in a shared Slack Connect channel, and the message becomes a ticket in the queue.
- **Phone channel** — native or integrated IVR and call routing for B2C. If not native, describe the integration path with third-party telephony providers to create tickets from calls. Example: a consumer calls a support line, is routed by IVR based on account tier, and a ticket is created automatically with the call recording attached.
- **Mobile app chat** — B2C channel for the 2027 wallet launch; chat widget or API embeddable in a mobile app. Example: a consumer opens chat inside the wallet app without leaving it, and the conversation appears in the same ticket timeline as web chat.
- **Internal ticket submission** — account teams can raise tickets on behalf of customers without consuming a full agent seat. Example: an account manager raises a ticket from a meeting note on a merchant's behalf, without needing a full agent licence.
- **Multi-environment support at user and business level** — we support users from both sandbox and production environments. Can the platform determine which environment a user belongs to within an organisation? Example: a developer logging in with a sandbox-only account is distinguished from a merchant using the same email domain in production.
- **Contracting-entity / region enrichment** — match a merchant to its legal-entity region (or other contracting attribute) and write it to a field usable for routing, via API. Populated from an external source; the platform is not expected to derive it. Example: a merchant's contracting entity ("Checkout.com Ltd, UK") is written to a ticket field via API and used to route the ticket to the UK team.

**Data model**

- **Flexible data model** — custom objects and fields sufficient to model our org hierarchy and ISV/Platform data, including surfacing live external data without storing it in the platform. Example: a custom "Platform Parent Merchant" object models ISV/sub-merchant hierarchy without a vendor schema change.

**Routing rules**

- **Support plan / tier routing** — route based on customer tier (P0–P3), with tier available as a condition in routing, SLA assignment, and prioritisation. Example: a P0 ticket from an Enterprise merchant routes to a dedicated queue with a 1-hour SLA, distinct from a P3 Standard ticket's 24-hour SLA.
- **Skill-based routing** — match agent skill tags to ticket classification; teams configurable by skill, function, and region. Example: a ticket tagged "3DS authentication" only routes to agents holding the "Payments-3DS" skill tag.
- **SLA per tier and taxonomy value** — different SLA clocks per priority and per contact type. Can SLA assignment be decoupled from tier and driven by workflow rules? Example: a P1 dispute ticket gets a 4-hour SLA while a P1 general enquiry gets 8 hours, without changing the tier.
- **Customisable ticket and customer fields** — company/account-level and individual/ticket-level fields, both usable as conditions and actions in routing rules. Example: a custom account-level field "Platform ISV Parent" is added and used as a routing condition.
- **Flexible tagging/field system** — for taxonomy mapping and analytics; all fields and tags available for queue filtering and reporting. Example: every ticket carries case-type and issue-type tags that are filterable in reporting without a custom report build.
- **Flexible routing system** — branching logic and fallbacks using any combination of tags, ticket fields, account fields, tier, and channel. Describe the level of programmatic control available via API. Example: "Disputes" tickets from Enterprise accounts route to Team A, but the same case type from Standard accounts falls back to Team B when Team A is at capacity.
- **Presence-aware ("follow-the-sun") routing** — route based on which agents and sites are currently online (login/presence state), automatically shifting distribution to active regions as other regions go offline, without manual queue switching. Example: as the UK team logs off, new tickets start routing to the US night-shift team automatically, with no manual queue switch.
- **Business-hours schedules per site/timezone** — multiple independent business-hours schedules; distinct in-hours vs out-of-hours routing; hold/pending queues that release to the next region's shift. Example: a ticket raised at 2am UK time sits in a holding queue and releases to the Manila team when their shift starts.
- **Geographic / entity-based routing** — route on a merchant region or contracting-entity attribute held at account or ticket level, sending different regions to different sites or teams. Example: a merchant contracted with the EU entity routes to the EU team; the same case type from a US-contracted merchant routes to the US team.

**Target routing flow to support**:
1. Ticket arrives.
2. Enrich via email lookup to populate fields.
3. Fields determine SLA and route to specific agents via skill matching.
4. Priority ranking set from SLA timer, query type, etc.
5. Agent receives auto-routed ticket (no cherry-picking) and resolves.
6. Capacity controls on how many tickets each agent holds.

**Key questions**:
- Which channels are native vs. add-on, and what is the per-channel cost at 500-agent scale?
- Does the platform support custom object models, or are organisations and users a fixed schema? Which core objects are extensible via custom fields, and can external identifiers be associated with platform objects?
- How does the platform route across multiple regions/sites based on real-time agent presence, and can routing rules react to computed rolling metrics rather than only to static field values?

---

## 2. Integration ease

**Must-have integrations**

- **Fin (Intercom)** — inbound escalation with full conversation context. Provide a reference customer running Fin → your platform. Example: a live Fin escalation creates a ticket with transcript and metadata already attached.
- **Jira** — bi-directional; create/update issues from tickets and sync status back. Example: updating a Jira issue's status to "Done" automatically updates the linked support ticket without an agent touching it.
- **Salesforce** — read and sync case numbers and customer data; state whether write-back is supported. Example: a ticket displays the merchant's current Salesforce case number and account owner without manual lookup.
- **Knowledge sources** — inbound sync of content from an external source (URL, sitemap, or GitHub repo). State which formats and connectors are supported. Example: our support site's GitHub repo is connected once, and new articles re-sync into the agent's knowledge base automatically after each merge.
- **Custom APIs** — pull data from systems such as BigQuery; call external APIs from workflows; full read/write via API and webhooks. Example: a workflow calls an internal API to pull a merchant's live transaction volume into a ticket field.

**Analytics and data extract**

- **API access to ticket data** — full export for an analytics pipeline (API and CSV); state any native ELT connector and its availability date. Example: all fields, including custom fields and comment history, for every ticket created can be extracted daily via API to feed our Reflex pipeline.
- **Taxonomy-level reporting** — filter and group by custom taxonomy tags and ticket fields. Example: a report filters tickets by "Case Type = Disputes AND Issue Type = Pre-Arbitration" without a custom report build.
- **SLA breach alerting** — automated alerts before and on breach, configurable per tier, surfaced in the agent workspace and via Slack/email. Example: a Slack alert fires 30 minutes before a P0 ticket breaches SLA, and again if it actually breaches.
- **AHT / agent task-time measurement** — do you have native average-handle-time or agent task-time measurement? Example: a dashboard shows average handle time per agent per case type without a separate time-tracking app.

**Key question**: What knowledge sync mechanisms are supported? Is sync automated on change, or manual?

---

## 3. AI compatibility

- **Auto-classification on escalation** — taxonomy tags applied automatically before human assignment, including urgency detection. Example: a ticket about a chargeback is auto-tagged "Disputes > Chargebacks" before it reaches an agent's queue.
- **AI agent handoff with context** — transcript and metadata passed to the agent workspace on escalation from an external AI agent. Example: Fin's classification of "Settlement — Payout Delay" is passed to the ticket as a structured field, not just as free text in the transcript.
- **Pluggable AI layer** — must allow an external AI (our Agent Consultant) to operate without requiring the platform's native AI. We must be able to use our own AI, the platform's AI, or both, without lock-in. Example: Agent Consultant writes a suggested action to a ticket without the platform's native AI being enabled or paid for.
- **Agent-triggered workflow execution** — agent approves an AI action; the platform passes an execution signal to an external system (via HTTP action or webhook). Example: an agent clicks "Approve refund" on an AI-suggested action, and the platform fires a webhook that triggers the actual refund in the payments system.
- **Dedicated AI-agent actor identity ("bring your own agent")** — a first-class, dedicated identity type for an external AI agent, distinct from both a human agent seat and a generic shared API/service-account token: it can be assigned threads with full context, reply to customers under its own name, update status, and hand off to a human via a logged transition, without consuming a paid human seat and without being tied to the platform's own native AI. Example: our AI layer (Fin, or a future replacement) operates under its own identity in the platform, visible in its own activity view, swappable without rebuilding routing/queues/escalation paths. Distinct from "pluggable external AI layer" above, which asks whether an external AI can write to a ticket at all — this asks whether it can do so as a durable, first-class actor rather than by borrowing a human's seat or a shared system credential.

**Key questions**:
- Can the platform accept AI classifications from an external system (apply labels/tags, set fields, set priority, route) via API or webhook, without using the platform's native AI?
- Fin classifies contacts using synced fields and passes the result back on handoff to a human. Do you support field syncing with Fin?
- Is the platform's own agent-AI layer (e.g. a Copilot equivalent) customisable and callable from outside, or is it a closed system with fixed skills?

---

## 4. Agent experience

**Interface**

- **Custom app framework** — developer SDK/API for sidebar apps. We are building a custom AI agent app to run in the agent-workspace sidebar. Describe the framework: can a sidebar component render custom UI, fetch and display live data from our own systems, and write back to the ticket? How customisable is the content of a sidebar panel? Example: a sidebar panel calls our internal API to show a merchant's recent transaction history live, without that data being stored in the platform.
- **App capability scope** — custom apps can read ticket data, make external API calls, and write back to tickets. Example: an app reads a ticket's account ID, calls an external fraud-check API, and writes the result to a custom field the agent can see.
- **App deployment and versioning** — deployable by our team without vendor involvement or marketplace approval. Example: engineering pushes an updated sidebar app version directly from CI, with no vendor marketplace review step.
- **Live customer data panel** — CRM and user data surfaced from our own sources in the ticket view. Example: an agent sees a merchant's current processing volume and recent settlement status pulled live from our data warehouse in the ticket sidebar.
- **Internal collaborator access** — read and comment access for non-agent staff without a full agent seat. Example: a Knowledge Manager can read and comment on a ticket to suggest a fix, without being issued a full agent seat.

**Agent-facing routing** (how the agent experiences the queue, distinct from the routing rules in category 1)

- **Queue-view scoping by attribute** — restrict which tickets an agent or site can see or pull, based on a region/segment attribute, to prevent cherry-picking and enforce workload segregation. Distinct from the B2B/B2C data wall below. Example: a BPO agent handling B2C tickets cannot see or pull B2B tickets from the queue view, even if idle.
- **Push and pull queue models** — support both automated push (capacity-based, no cherry-picking) and manual pull views, and freeze or lock views at shift boundaries. Example: tickets auto-assign by capacity during business hours but shift to a locked pull view for agents to self-select from in the last 30 minutes of a shift.
- **Capacity controls and handoff mode** — per-agent concurrent-ticket caps, and the ability to block new assignments to agents or sites approaching end of shift ("handoff mode"). Example: an agent holding 8 concurrent tickets stops receiving new assignments, and no new tickets route to them at all in the final 15 minutes of their shift.
- **Conditional routing on computed thresholds** — redirect or cap volume automatically when a rolling operational metric (e.g. a 30-day volume-mix ratio by attribute) crosses configurable thresholds. Example: if refund-related contacts exceed 20% of daily volume, new refund tickets automatically cap or redirect to a dedicated team.
- **Automated ownership release on SLA-breach risk** — when the assigned agent is off-shift and the SLA will breach before their next shift, automatically un-assign the ticket and push it to an active queue/site. Predictive (time-to-breach) calculation, configurable per priority tier. Example: an agent's shift ends at 6pm; if their assigned ticket will breach SLA before 9am the next day, it's automatically reassigned to the active night team at 5:45pm.

**Data and permissions**

- **B2B / B2C data wall** — two isolated environments; a BPO handling B2C must never see B2B data. Describe the isolation mechanism (separate workspaces, RBAC, or both). Example: a BPO agent logged into the B2C workspace cannot search for or view any B2B merchant ticket, even by ticket ID.
- **Role-based access control** — granular permissions per team and per brand, with custom roles for agents, leads, and admins. Example: a team lead can see and reassign all tickets in their team's queue, while an agent can only see and act on their own assigned tickets.

**Key questions**: What is the custom app development framework? Are there restrictions on what custom apps can read or write? How does queue-view scoping interact with the B2B/B2C data wall — are they the same mechanism or two separate controls?

---

## 5. Config as code

- **Sandbox / test environment** — mirrors production configuration and keeps test data isolated from production. Example: a routing rule change can be built and tested against realistic ticket data in sandbox before it touches a live customer ticket.
- **Configuration promotion path** — a defined mechanism to promote configuration (workflows, fields, tags, tiers, SLAs) from test to production. Example: a "promote to production" action (button or API call) moves an approved SLA policy from sandbox to live without re-building it by hand.
- **Config as code** — configuration (routing, fields, tags, tiers, SLAs) expressible as version-controlled files, deployable via CI/CD, diffable and reviewable like application code, rather than only editable through a UI or ad hoc API scripts. Example: a new ticket field or routing rule is defined in a YAML/Terraform file, reviewed via pull request, and applied through a pipeline — with a visible diff of what changed and a rollback path if the deploy is wrong.

**Key question**: Is there a supported configuration promotion workflow between sandbox and production (e.g. push-button deploy), or must promotion be scripted via API? Does a native or supported config-as-code tool exist (e.g. Terraform provider, CLI, or vendor-native IaC), and what proportion of configuration does it cover?

---

## 6. Partnership and reliability

**Partnership fit** (draft — qualitative, gathered via reference calls and account team engagement, not a standard RFI field)

- **Roadmap alignment / co-investment** — evidence the vendor is investing in the capability areas that matter to us (agentic workflows, config-as-code, AI compatibility), not treating our requests as one-off custom work. Example: a named roadmap item exists for agent-triggered workflow execution, not just a "we'll consider it" response.
- **Account treatment at our scale** — a strategic account team and pricing/support model appropriate to a 500-agent enterprise deployment, not a self-serve or SMB-first motion. Example: a dedicated solutions engineer is assigned during evaluation, not a shared success-team queue.
- **Implementation weight required** — how much professional services / implementation partner spend is required to reach production readiness. Example: go-live is achievable with our own engineering team plus vendor documentation, without a mandatory paid implementation package.

**Reliability**

- **Uptime SLA** — contractual commitment for core ticketing. Example: a contractual 99.9% uptime commitment with defined service credits if breached.
- **Enterprise support SLA** — guaranteed human response time for P1/P2 issues; human-first, not bot-first deflection. Example: a P1 outage from us gets a guaranteed 1-hour human response, not a bot-first auto-reply.
- **Named account team** — dedicated enterprise contact with a defined escalation chain. Example: a named technical account manager, not a rotating support queue, is our first point of contact for escalations.
- **Billing dispute resolution** — documented process with a defined resolution timeline. Example: a disputed charge has a documented process with a committed resolution timeframe, such as 30 days.
- **Auto-renewal protection** — minimum 60-day written notice required before automatic renewal. Example: the contract requires the vendor to notify us at least 60 days before auto-renewing.
- **Vendor continuity** — evidence of operation through 2030. Example: evidence such as funding runway, profitability, or customer base size supporting continued operation and support through 2030.
- **500-agent scale** — support projected 2030 headcount without degraded performance or disproportionate cost. Example: dashboard and search performance doesn't degrade as the agent roster grows from 50 to 500 concurrent users.

**Key questions**: What are the contractual commitments for support response times? Is the company profitable or funded beyond 2028? What financial-services domain experience do you have? What roadmap investment is planned in agentic/AI workflow capability over the next 12 months?

---

## 7. Customer-facing experience

- **Customer ticket portal** — merchants can view open tickets and conversation history. Describe both a hosted portal and any headless/API-driven option where we build the front-end. Example: a merchant logs into a portal and sees their open tickets, or the same data is exposed via API for us to build our own view.
- **AI chat history visibility** — previous AI agent conversations visible alongside ticket history, stored as part of the ticket timeline for both agents and customers. Example: an agent opens a ticket and sees the merchant's earlier Fin conversation about the same issue in the same timeline, not a separate log.
- **Account team thread visibility** — account managers can view and reply into ticket threads over email, with internal notes for collaboration not visible to the customer. Example: an account manager replies to a ticket thread by email and adds an internal note visible to staff but not the merchant.

---

## 8. Pricing

- **All-in cost at 500 agents** — seats plus any required add-ons. State what is included in the seat price and what is billed separately. Example: a single quote shows seat cost plus every add-on (QA, WFM, Advanced AI) required to match our current functionality at 500 agents.
- **Cost predictability** — 12-month cost modellable with reasonable confidence. State whether pricing is seat-based, usage-based, or per-ticket. Example: next year's cost can be modelled within a narrow range from our contact volume forecast, rather than being exposed to usage-based charges that spike unpredictably.
- **Add-on gating transparency** — required features documented as included or separately billed. Example: a feature comparison sheet states plainly which capabilities are included in the seat price vs. billed as a separate SKU.
- **Volume discount terms** — enterprise pricing at projected 2027–2030 contact volumes. Example: a defined discount tier applies automatically once contact volume crosses an agreed threshold, rather than requiring a fresh negotiation each time.

---

**Last updated**: 2026-09-18
**Owner**: Charlie Wildish
