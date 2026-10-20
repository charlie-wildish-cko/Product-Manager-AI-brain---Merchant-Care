# Plain × Checkout.com; Business Case (Draft v1)

## 🎯 What this is about

The operations team evaluated Plain as the replacement for Zendesk across Checkout.com's support operation, following a four week proof of concept in July and August 2026 run by engineering, product and support ops.

This document supports the recommendation to adopt Plain as the support platform for Merchant Care, migrating in H1 2027 ahead of the June 2027 Zendesk renewal, with a path to extend across the wider operations organisation (300+ users across merchant care, risk ops, compliance ops, and finance ops).

---

## ❓ Why change

[Checkout.com](http://Checkout.com) moved to Zendesk in 2023, before the AI landscape matured. Three years on, the operation has outgrown it in specific ways:

- **All administration is manual, through the UI.** A recent taxonomy change took weeks of admin time. Zendesk configuration cannot be version controlled natively, so Checkout pays for Salto as a bolt-on to get an audit trail and rollback. Even then, Zendesk's API was never designed for managing configuration changes.
    - **Impact:** the support org can only adapt as fast as two admins can safely click. Change velocity is capped, and audit compliance depends on a third party layer.
- **Config sprawl nobody can safely touch.** 318 triggers (23 of 47 trigger categories unused), 171 distinct tags, roughly 200 macros carrying dead weight, and a 105 field form with 108 conditional show/hide rules built around Zendesk's limitations.
    - **Impact:** operational logic is opaque, fragile, and expensive to change. New requirements from ops leadership queue behind admin capacity.
- **No conditional logic where the business needs it.** Zendesk dictates what can be done rather than letting the team supply the conditions within workflows.
    - **Impact:** follow the sun routing, regional SLAs, capacity caps, and shift handoffs (the operating model ops leadership wants) cannot be expressed in Zendesk without workarounds or more vendors.
- **Vendor responsiveness.** Feature requests to Zendesk disappear into a product backlog with no visibility or timeline.
    - **Impact:** the gap between what the operation needs and what the platform provides widens every quarter.
- **A growing add-on stack.** Zendesk seats, a sandbox fee, Salto for config as code, SweetHawk for approval flows, plus enrichment automations built and maintained in house.
    - **Impact:** four contracts, four security reviews, and four renewal cycles to approximate what a modern platform does natively.
- **[Charlie to add: operational metrics that show the cost of the current setup. SLA misses, uneven thread pickup, wait times, reopen rates.]**
    - **Impact:** leadership decisions on staffing and quality are made on metrics the team itself considers flawed. For example, the AHT clock starts at assignment while agents hold multiple tickets.

---

## ✅ What the POC proved

The POC ran from 27 July to the end of August across two tracks: engineering (config as code, API, data model) and support ops (workflows, routing, day to day operation).

**Engineering track**

- **Full config as code, working.** Taxonomy, thread fields, field dependencies, labels, and workflows deployed from a GitHub repo as source of truth via GraphQL and GitHub Actions, with working drift detection: changes made outside the repo are reverted on the next run. 11 test cases passed in week one. This replaces the Salto layer natively, with version control, peer review, and rollback through Checkout's standard engineering pipeline.
- **AI assisted administration works in practice.** Admins used Claude against Plain's API and docs to draft and deploy workflows from business descriptions. This upskills admins to do more technical work without engineering dependency.
- **Data model fits.** Client maps to Tenant. Entities are served via customer cards from Checkout's own APIs. Sandbox to production promotion flows tested across workspaces.
- **Agent tooling path validated.** Customer cards render payment context from Checkout systems inside the thread view. Engineering's assessment is that this is a better agent experience than the current iframe approach.
- **Vendor responsiveness, measured.** Documentation gaps raised on a Monday were fixed in a PR the same morning. A workflow feature request (user status conditions) was designed, built, and shipped within one week of being raised.

**Support ops track**

- End to end flows working: multi channel intake, AI language detection, auto labelling, prioritisation, tier based and regional routing with capacity caps, and priority first auto assignment (urgent tickets jump the queue natively, removing cherry picking).
- **Complaints chase sequences and SLA breach Slack digests.** Automated internal and external follow up chases for active complaints. The admin team identified this as a standout capability that Zendesk cannot match without add-ons.
- Two workspace architecture validated for the Merchant (B2B) and Consumer (B2C) data wall.

**Reference checks**

- Tines runs Fin to Plain escalation in production today and validated the integration architecture directly with Checkout.
- Vercel operates Plain with a comparable engineering led model: custom agents built on the API for retro analysis, escalation summaries, and AI triage, sustaining a 19% efficiency gain while redeploying 20% of support headcount to other roles.

---

## 📋 Coverage against the evaluation criteria

Mapped to the 11 sections of the evaluation criteria document.

| Criteria section | POC outcome | Status |
| --- | --- | --- |
| 1. Multi-channel entry points | Email, live chat, Slack/Teams, internal submission all native and tested. Enrichment and domain mapping land with the tenant model update (end of August). Phone is not native; integration architecture via API with a telephony provider. | Proven, except phone (integration path) and enrichment (end of August) |
| 2. AI triage and classification | Auto labelling, language detection, urgency detection, and external classification via API all tested. No lock-in to native AI; Checkout's own agent connects as a machine user. | Proven |
| 3. Routing and field logic | Tier, skill, regional, and capacity based routing tested. Priority first assignment is native. SLA per taxonomy and business hours per site ship in September (dates below). | Proven, except SLA and business hours items (September product commitment from Plain) |
| 4. Agent workspace | Customer cards for live data, full API read/write, deployment without vendor involvement, Jira escalation, free viewer seats. No embedded iframe SDK; customer cards plus headless auth are the recommended replacement, per engineering's own assessment. | Proven via customer cards |
| 5. Data and permissions | Separate workspaces give the B2B/B2C wall. Custom roles for RBAC. Seat based scaling to 500+. | Proven |
| 6. Customer-facing experience | Help center with customer inbox, or headless portal on the API. AI transcripts stored on the thread timeline. | Validated, not yet built in POC |
| 7. Integrations | Jira and Salesforce native. Fin escalation validated via the Tines reference. Knowledge sources sync automatically. Custom API access unrestricted. | Proven or referenced |
| 8. Analytics and data extract | Full GraphQL export today; Fivetran connector committed in writing by end of 2026, with a Plain funded Polytomic connector as interim option. AHT measurement is a gap; metric definition to be co-designed against the events API. | Partial; Fivetran end of 2026, AHT open |
| 9. Environment and configuration deployment | Sandbox workspace mirrors production. Promotion via the same config as code pipeline, tested cross workspace with drift detection. | Proven |
| 10. Vendor reliability | Uptime SLA in enterprise contracts, named CSM and solutions engineering on Frontier. Funding and runway session with Plain's CEO and CPO to be scheduled as part of due diligence. | Session pending |
| 11. Pricing | Seat based + platform fee, all features included, no add-on gating, unlimited free viewer seats. Quote received; detail below. | Received |

---

## ⚠️ Known gaps, all dated

The three must-haves flagged at POC close, each with a committed mitigation:

| Gap | Status | Date |
| --- | --- | --- |
| SLA model: per taxonomy and per country SLAs, resolution time with and without customer wait time, including FCA complaints requirements | Rebuilt as workflow blocks; committed in writing | First week of September 2026 |
| Multiple business hours: follow the sun across London, Mauritius, Dubai, and Mexico | In build; Checkout is a design partner on requirements | By 14 September 2026 |
| Fivetran integration: metrics export to BigQuery | Committed in writing; interim is a Plain funded Polytomic connector plus full API access today | By end of 2026 |

Both September items land inside the extended evaluation window and will be verified before the final recommendation.

---

## 📊 Business impact

Mapped to the metrics Operations reports on today (tickets received and solved, first contact resolution, dependency rate, L1 to L2 transfers, reopens, CSAT):

1. **SLA integrity as a compliance asset.** Regulatory SLAs (the FCA 15 day complaints clock, 10 day exceptional circumstance extensions, per country calculations) expressed natively in workflows, with breach alerting and after the fact reporting, rather than held together by custom fields and manual vigilance. [Charlie to add: current breach or miss rate]
2. **Change velocity.** Taxonomy or routing changes move from weeks of manual admin work to reviewed, auditable deploys. Admin capacity shifts from clicking to designing. [Baseline: recent taxonomy change duration vs the POC equivalent]
3. **Dependency and transfer friction.** Automated chase sequences, structured escalation, and close the loop flows directly target the dependency and L2 transfer lines in the MBR. Today's manual email handoffs (hours for treasury, days to weeks for engineering) become tracked, automated threads.
4. **Honest metrics, no cherry picking.** Priority first, capacity based assignment removes manual ticket grabbing, and measurement resets on metrics the team trusts.
5. **Stack consolidation.** Zendesk, the sandbox fee, Salto, and SweetHawk consolidate into one platform, one contract, one security review. [Insert current combined annual cost]
6. **Scale without proportional headcount.** Unlimited free viewer seats give account managers, engineering, and adjacent teams visibility without licence cost. AI triage plus Checkout's own agent as a first class citizen (alongside Fin) lifts per agent throughput as volume grows toward the 2027 B2C launch.

---

## 🚀 Scaling beyond Merchant Care

- **The expansion model.** Every additional team onboarded is a set of workflows, fields, and routing rules deployed from the same repo. The marginal effort of onboarding the next team is a code review rather than a re-implementation. Migration effort per team can be forecast with a repeatable audit (channels, workflows, integrations) that engineering has now done once.
- **Support as an insights engine.** With all support data structured, API accessible, and flowing to BigQuery, support becomes a source of product and merchant intelligence rather than a cost centre reporting lagging indicators.
- **Strategic alignment.** A platform whose operating model (follow the sun, per region SLAs, entity aware routing) lives in configuration supports US and APAC expansion and enterprise merchant growth without re-platforming. Scaling from 100 to 300+ to 900 users by 2030 is a licensing change, not a technology decision.

---

## 💰 Commercials

- Frontier plan at roughly $139 per seat per month at 100 seats. All channels, AI features, API access, and CSM support included. No per channel or per feature add-ons. Unlimited free viewer seats.
- Includes 600k Sidekick credits per year. A right sized credit pool for an AI heavy operation (around 30k contacts) is available with discounted top up rates.
- Incentives available for a multi year term (procurement's stated preference for business critical systems), growth commitments, and case study rights.
- Cost is predictable (seat based, no usage or per ticket fees) and should be assessed against the total current stack: Zendesk, sandbox fee, Salto, SweetHawk, and integration maintenance.

---

## 🗓️ Path forward

| Phase | Window | Activity |
| --- | --- | --- |
| Internal approval | Late August to September | Leadership demo (week of 24 August); this business case plus evaluation scoring; verification of the September feature ships; vendor viability session with Plain's founders |
| Procurement and security (parallel) | September to end of October | InfoSec review; DORA Art. 30, PCI DSS 12.8 and 12.9, GDPR Art. 28 assessment; MSA and DPA; commercial close. Build continues in the existing workspaces throughout, on verbal approval |
| Build | November 2026 to Q1 2027 | Production configuration via config as code; integrations (Fin, Jira, Salesforce, BigQuery); agent tooling; training |
| Migration | H1 2027 | Merchant Care first; parallel run against Zendesk; cutover well ahead of the June 2027 renewal; subsequent teams phased |

---

## Partnership

Plain's engagement through the POC included same day fixes, weekly embedded sessions, features shipped against Checkout requirements inside the evaluation window, and design partner status on routing and business hours. This is the working relationship on offer through implementation, with a named CSM and dedicated support on the Frontier plan. Vendor viability (funding, runway, continuity through 2030) will be covered directly with Plain's CEO and CPO as part of due diligence.

---

[Checkout.com Proof Points](https://app.notion.com/p/Checkout-com-Proof-Points-3d4810036f9d80a28421f37360233436?pvs=21)