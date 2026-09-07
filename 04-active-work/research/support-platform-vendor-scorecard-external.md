# Checkout.com — Support Platform Evaluation Criteria

Five requirements are treated as gating: a platform that cannot meet these is disqualified regardless of performance elsewhere.

**Gating requirements**:
1. Intercom Fin escalation handoff with full context
2. Tier-based routing with SLA clocks
3. Custom sidebar app, read/write
4. Jira bi-directional sync
5. Email-to-organisation matching

---

## How capability and effort are assessed

Each requirement below is assessed on two separate dimensions:

- **Capability** — whether and how the requirement is met: native, via configuration, via a paid add-on, via custom build, or not supported. This is what we ask you to answer in the RFI, with documentation links and a reference customer wherever possible.
- **Effort** — ease of use and setup time. We do not score this from self-reported ratings, since that isn't comparable across vendors. Instead we measure it directly during the POC (e.g. time to deploy a working integration, number of steps to configure a flow), where your team supports us in standing up the relevant flow. If your RFI response includes a concrete effort figure (e.g. "typical setup: 2 days," "no professional services required"), include it — this is a helpful complement to the POC, not a substitute for it.

---

## Evaluation criteria

### 1. Multi-channel entry points — weight 13%
- **1.1 Email ingestion** — e.g. a reply threads onto the existing ticket rather than creating a duplicate
- **1.2 Email user enrichment** (auto-match to organisation) — e.g. an unrecognised sender is still matched to the right org by domain
- **1.3 Domain mapping** — e.g. a known email domain auto-tags to its organisation record with no manual selection
- **1.4 AI agent escalation path** (Fin handoff with context) — e.g. the agent sees the full transcript plus tier/intent fields Fin already applied
- **1.5 Live chat with human agent** (B2B) — e.g. a "Report a bug" click pre-fills an intake form before reaching an agent
- **1.6 Instant messaging channels** (Slack/Teams) — e.g. a message in a shared Slack Connect channel becomes a ticket
- **1.7 Phone channel** (B2C IVR + routing) — e.g. IVR routes by tier and auto-creates a ticket with the call recording attached
- **1.8 Mobile app chat** (B2C) — e.g. in-app chat shares the same ticket timeline as web chat
- **1.9 Internal ticket submission** (account teams) — e.g. an account manager raises a ticket on a customer's behalf without a full seat
- **1.10 Multi-environment support** (sandbox vs. production user/business) — e.g. a sandbox-only login is distinguished from a production user on the same domain
- **1.11 Region / contracting-entity enrichment** (routing attribute via API) — e.g. a contracting-entity value is written to a field via API and drives regional routing

### 2. AI triage and classification — weight 12%
- **2.1 Auto-classification on escalation** — e.g. a chargeback ticket auto-tags "Disputes > Chargebacks" before reaching a queue
- **2.2 AI agent handoff with context** — e.g. a classification lands as a structured field, not just text in the transcript
- **2.3 Pluggable external AI layer** (no lock-in to native AI) — e.g. our own AI system writes to a ticket without the platform's native AI enabled

### 3. Routing and field logic — weight 10%
- **3.1 Support plan / tier model** — e.g. a P0 ticket routes to a dedicated 1-hour-SLA queue, distinct from a P3's 24 hours
- **3.2 Skill-based routing** — e.g. a ticket tagged with a specific skill only reaches agents holding that skill tag
- **3.3 SLA per tier and taxonomy value** — e.g. a P1 dispute gets a 4-hour SLA while a P1 general enquiry gets 8, same tier
- **3.4 Customisable ticket and customer fields** — e.g. a custom account-level field is used as a routing condition
- **3.5 Flexible tagging / field system** — e.g. case-type/issue-type tags are filterable in reporting with no custom build
- **3.6 Flexible routing system** (branching + fallbacks on any attribute) — e.g. overflow from one team falls back to another automatically at capacity
- **3.7 Presence-aware / follow-the-sun routing** — e.g. as one region logs off, new tickets auto-shift to the next active region
- **3.8 Business-hours schedules per site/timezone** — e.g. an out-of-hours ticket holds until the next region's shift starts
- **3.9 Geographic / entity-based routing** — e.g. a customer's contracting region determines which regional team it routes to
- **3.10 Queue-view scoping by attribute** — e.g. a B2C-only agent cannot see or pull B2B tickets from the queue
- **3.11 Push and pull queue models** — e.g. auto-push by capacity in-hours, a locked pull view near shift end
- **3.12 Capacity controls and handoff mode** — e.g. no new tickets route to an agent in the final minutes of their shift
- **3.13 Conditional routing on computed thresholds** — e.g. a contact type exceeding a volume share auto-redirects to a dedicated team
- **3.14 Automated ownership release on SLA-breach risk** — e.g. a ticket is reassigned before an agent's shift ends if it would otherwise breach overnight

### 4. Agent workspace — weight 16%
- **4.1 Custom app framework** (SDK/API) — e.g. a sidebar panel shows live internal data without storing it in the platform
- **4.2 App capability scope** (read + write + external API) — e.g. an app reads a ticket field, calls an external API, and writes the result back
- **4.3 App deployment/versioning without vendor involvement** — e.g. our team deploys an updated app from CI with no marketplace review step
- **4.4 Live customer data panel** (own sources) — e.g. an agent sees live account data pulled from our own systems in the ticket sidebar
- **4.5 Internal escalation** (Jira, custom API, read/write) — e.g. a one-click Jira issue creation, with ticket status updating when the issue closes
- **4.6 Agent-triggered workflow execution** — e.g. an agent approves an action, and the platform fires a webhook that triggers it externally
- **4.7 Internal collaborator access** (no full agent seat) — e.g. a subject-matter expert comments on a ticket without a full agent licence

### 5. Data and permissions — weight 13%
- **5.1 B2B/B2C data wall** (isolation mechanism) — e.g. a B2C-only agent cannot see or search any B2B ticket, even by ID
- **5.2 Role-based access control** — e.g. a team lead sees and reassigns the whole team queue; an agent sees only their own tickets
- **5.3 500-agent scale** — e.g. dashboard and search performance holds as concurrent users scale from 50 to 500
- **5.4 Flexible data model** (custom objects, no hardcoded schema) — e.g. a custom object models a reseller/platform hierarchy with no vendor schema change

### 6. Customer-facing experience — weight 5%
- **6.1 Customer ticket portal** — e.g. a customer logs in and sees open tickets, or the same data is available via API for our own front-end
- **6.2 AI chat history visibility** — e.g. an earlier AI-agent conversation is visible in the same ticket timeline, not a separate log
- **6.3 Account team thread visibility/reply** — e.g. an account manager replies via email and adds an internal note not visible to the customer

### 7. Integrations (must-have) — weight 10%
- **7.1 Intercom Fin escalation with context** — e.g. an escalation creates a ticket with transcript and metadata already attached
- **7.2 Jira bi-directional** — e.g. a Jira status change to "Done" auto-updates the linked ticket
- **7.3 Salesforce sync** — e.g. a ticket shows the current Salesforce case number and account owner with no manual lookup
- **7.4 Knowledge source sync** (URL/GitHub, automated) — e.g. a source repo is connected once and new articles re-sync after each update
- **7.5 Custom API access to internal systems** — e.g. a workflow pulls live account data from an internal system into a ticket field

### 8. Analytics and data extract — weight 5%
- **8.1 Full API export of ticket data** — e.g. all fields, including custom fields and comment history, are extractable daily via API
- **8.2 Taxonomy-level reporting** — e.g. a report filters by case type and issue type with no custom report build
- **8.3 SLA breach alerting** — e.g. an alert fires 30 minutes before a P0 ticket breaches SLA, and again on breach
- **8.4 AHT / agent task-time measurement** — e.g. average handle time per agent per case type, no separate time-tracking app

### 9. Environment and configuration deployment — weight 10%
- **9.1 Sandbox/test environment mirroring production** — e.g. test a routing change against realistic data before it hits a live ticket
- **9.2 Configuration promotion path** (test to production) — e.g. a "promote to production" action moves an approved SLA policy live without a manual rebuild
- **9.3 Config as code** (version-controlled, CI/CD-deployable configuration) — e.g. a routing rule defined in YAML/Terraform, reviewed via pull request, deployed through a pipeline, with a visible diff and rollback path

### 10. Vendor reliability and operational trust — weight 3%
- **10.1 Uptime SLA** (core ticketing) — e.g. a contractual 99.9% commitment with defined service credits on breach
- **10.2 Enterprise support SLA** (human response, P1/P2) — e.g. a guaranteed 1-hour human response on a P1, not a bot-first reply
- **10.3 Named account team / escalation chain** — e.g. a named account manager, not a rotating queue, as first point of contact
- **10.4 Billing dispute resolution process** — e.g. a documented process with a committed resolution timeframe, such as 30 days
- **10.5 Auto-renewal protection** (60-day notice) — e.g. the contract requires 60 days' notice before auto-renewal
- **10.6 Vendor continuity risk** — e.g. evidence of profitability or funding runway supporting continued operation over the contract term

### 11. Pricing — weight 3%
- **11.1 All-in cost at 500 agents** — e.g. one quote covering seats plus every add-on required to match current functionality
- **11.2 Cost predictability** — e.g. next year's cost can be modelled within a narrow range from a contact-volume forecast
- **11.3 Add-on gating transparency** — e.g. a comparison sheet states plainly what's included in the seat price vs. a separate SKU
- **11.4 Volume discount terms** — e.g. a discount tier applies automatically once contact volume crosses an agreed threshold
