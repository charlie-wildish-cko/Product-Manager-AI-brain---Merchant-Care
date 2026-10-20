# RFC: Zendesk Platform Decision — Build / Buy / Keep

**Status**: ARCHIVED 2026-09-22. Superseded. The recommendation it produced stands: replace Zendesk with Plain.

> **Archived because the decision is made and the live artefacts have taken over.** This RFC ran the Build / Buy / Keep evaluation from April to September 2026 and produced the recommendation to replace Zendesk with Plain. It is kept as the decision record, not as a working document. Do not update it, and do not cite it for current scores or dates.
>
> **Where the live versions are:**
> - Vendor scores and evidence: `04-active-work/research/support-platform-vendor-scorecard.md`
> - Requirement definitions: `04-active-work/research/support-platform-vendor-requirements.md`
> - Leadership recommendation and ask: `04-active-work/working-files/zendesk-decision-deck-content.md`
> - POC results and commercials: `04-active-work/research/plain-business-case-draft-v1.md`
> - Migration sequencing: `04-active-work/research/support-platform-migration-sequencing.md`
> - Roadmap anchor: `2026 deliverables.md`, Help Desk Platform Evaluation
>
> **Call notes extracted 2026-09-22.** The Vercel, Zilch and Intercom call notes in Options 2 and 3 below are kept here as the original record, but the live, maintained versions with evidence tiers are in `04-active-work/research/support-platform-assessment-customer-references.md`. Cite that file, not this one. Two figures were corrected during extraction: see its Provenance corrections section.
>
> **What this document is still the best source for**: the full Option 1 / Option 2 / Option 4 rejection reasoning, including the dated rebuttal of the original case for keeping Zendesk.

**Created**: 2026-04-02
**Author**: Charlie Wildish
**Reviewers**: VP of Product · Director of Operations · Director of Operations Excellence · Engineering Manager
**Decision Deadline**: End of Q4 2026 per `2026 deliverables.md`. Working target is end of September 2026 for the procurement gate.
**Contract Renewal Deadline**: June 2027
**Leadership deck**: `04-active-work/working-files/zendesk-decision-deck-content.md` is the compressed version of this RFC for the CPO/COO audience.

---

## Summary

Zendesk is the operational backbone of Checkout.com's Care function — the data source for Reflex, the agent workspace, the routing layer, and the integration hub for Fin, Jira, and Salesforce. The current contract renews June 2027. This RFC evaluates whether to renew (Keep), replace (Buy), or build a proprietary system, and produces a recommendation ahead of that decision.

**Strategic context**: All 2026 Care deliverables depend on Zendesk. Any replacement would disrupt the current roadmap. The evaluation must weigh the cost and risk of switching against the cost and risk of staying on a platform with known capability gaps.

---

## Background and Context

### Problem Statement

The Zendesk contract renews in June 2027. Before signing, we need a structured view of whether the platform can support the Care capability model through to 2030. Specific gaps have emerged:

- **AI workflow execution**: Zendesk supports AI suggestions (Copilot) but does not natively support agent-triggered, autonomous workflow execution — a core requirement for Agent Consultant phase 2+
- **Platform merchant data**: ISV/sub-merchant context is surfaced via custom integration, not native — fragile and limited
- **B2C compliance readiness**: as assessed in April 2026, Consumer Duty required complaint handling, vulnerable customer detection and a phone channel from day one at wallet launch. **Correction, 2026-09-22**: this no longer applies. Ray is not UK-launched and cards are issued via Checkout SAS, so Ray sits outside Consumer Duty and SCA, and phone is confirmed not required. Consumer Duty obligations return in 2027 through open banking payers and issuing cardholders, which is a separate requirement
- **Pricing model shift**: Zendesk is moving to outcome-based pricing ($1.50–$2.00/Automated Resolution + add-ons of $50/agent Advanced AI, $35/agent QA, $25/agent WFM) — cost trajectory is unclear at scale
- **Vendor trust**: Systemic failures in Zendesk's own customer support, aggressive billing tactics, and non-auditable "Automated Resolution" charges represent tier-1 operational risk

### Current State

Zendesk is live for all B2B support handling. Key integrations in place or in delivery:

- Fin (Intercom) → Zendesk escalation
- Agent Toolkit (Customer 360 data panel in Zendesk sidebar)
- Agent Consultant (AI suggestions in Zendesk)
- Jira ↔ Zendesk bi-directional integration (in progress Q1/Q2)
- Salesforce → Zendesk case number sync (H2)
- Reflex data pipeline feeds from Zendesk tickets

The platform is not a simple tool — it is the data layer that every Care product depends on. Switching is a multi-quarter programme, not a lift-and-shift.

### Goals

- Produce a clear, defensible recommendation on platform direction before Q1 2027
- Identify what conditions would trigger a switch vs. a renewal negotiation
- Ensure 2026 roadmap delivery is not disrupted
- Anchor negotiation position if renewing
- Evaluate candidates against the desired platform architecture:**modular, flexible, and build-around** — the platform must allow us to plug in our own data sources, AI agents, and services without building for the platform's constraints

### Non-Goals

- This is not an evaluation of Fin (Intercom) — Fin is the AI layer and is evaluated separately
- This is not a case management redesign — the scope is the ticketing and agent platform only
- This does not commit to a migration timeline; it produces the decision and a path

---

## Candidate Evaluation

Candidates assessed: **Zendesk** (Keep), **Intercom** (Buy), **Plain** (Buy), **Pylon** (Buy), **Build**.

Scored against the assessment requirements defined in the Appendix. Pricing is assessed separately below.

> **The tables in this section are the April 2026 baseline and are superseded for scoring purposes.** They record the desk-research view taken before any POC, RFI or reference call, and several Plain and Pylon cells below are now known to be wrong. The current instrument is `support-platform-vendor-scorecard.md`, which scores 60 requirements across 8 weighted categories for all four vendors at 100% coverage, with one line of evidence per cell and a named evidence tier. The Comparison Matrix and Recommendation below both draw on that scorecard, not on these tables. Two specific corrections worth naming, because they reverse an April conclusion: Plain's config-as-code, routing and AI-compatibility capability was proven in a four-week POC (27 July to end August 2026), and Plain committed workflows, custom dashboards, multiple business hours, merged tenants, in-product mass comms, improved importers and internal support tickets to ship by end of October 2026 at the 2026-08-05 workshop, with SLAs moving out of tiers into workflows. Source: [2026-08-05 notes](../../../04-active-work/meeting-notes/2026-08/2026-08-05-checkout-plain-workshop.md), `plain-business-case-draft-v1.md`.

---

### 1. Multi-channel entry points

| Requirement                                    | Zendesk                                 | Intercom             | Plain / Pylon                          | Build |
| ---------------------------------------------- | --------------------------------------- | -------------------- | -------------------------------------- | ----- |
| Email ingestion                                | Native                                  | Native               | Plain: native; Pylon: limited          | Build |
| AI Agent escalation (Fin handoff with context) | Native via Intercom integration — live | Native (same vendor) | Plain: API only; Pylon: no             | Build |
| Live chat (B2B)                                | Via Sunshine Conversations (add-on TBC) | Native               | Pylon: native (Slack-first); Plain: no | Build |
| Instant messaging / Slack (2028–2029)         | Via Sunshine Conversations (add-on TBC) | Limited              | Pylon: native strength                 | Build |
| Phone / IVR (B2C, Consumer Duty)               | Zendesk Talk — native                  | No native phone      | No                                     | Build |
| Mobile app chat (B2C, 2027)                    | Via Sunshine Conversations              | Native               | No                                     | Build |
| Internal ticket submission (Account teams)     | Native                                  | Native               | Plain: yes; Pylon: limited             | Build |

**Assessment**: completed. Scored per requirement in `support-platform-vendor-scorecard.md`, 2026-09-22. See the Comparison Matrix below for the category result.

---

### 2. AI triage and classification

| Requirement                                    | Zendesk                                   | Intercom                                           | Plain / Pylon                  | Build        |
| ---------------------------------------------- | ----------------------------------------- | -------------------------------------------------- | ------------------------------ | ------------ |
| Auto-classification on escalation              | Via custom trigger / tag — not native    | Via Fin classifier — native                       | API-based only                 | Full control |
| AI agent handoff with context                  | Live via Intercom integration             | Native (same vendor)                               | API only                       | Build        |
| Pluggable external AI layer (Agent Consultant) | Supported via API + custom app — working | Supported but conflicts with native AI positioning | Plain: API yes; Pylon: limited | Full control |

**Assessment**: completed. Scored per requirement in `support-platform-vendor-scorecard.md`, 2026-09-22. See the Comparison Matrix below for the category result.

---

### 3. Routing logic

| Requirement                             | Zendesk                | Intercom          | Plain / Pylon              | Build        |
| --------------------------------------- | ---------------------- | ----------------- | -------------------------- | ------------ |
| Support plan / tier model (P0–P3)      | Native — configurable | Partial           | Plain: limited; Pylon: no  | Build        |
| Skill-based routing                     | Native — in delivery  | Basic             | No                         | Build        |
| SLA per tier and taxonomy value         | Native — configurable | Basic SLA support | No                         | Build        |
| Customisable ticket and customer fields | Native                 | Limited           | Plain: yes; Pylon: limited | Full control |
| Flexible tagging / taxonomy             | Native                 | Limited           | Plain: yes; Pylon: no      | Full control |

**Assessment**: completed. Scored per requirement in `support-platform-vendor-scorecard.md`, 2026-09-22. See the Comparison Matrix below for the category result.

---

### 4. Agent workspace

| Requirement                                                | Zendesk                                        | Intercom                     | Plain / Pylon              | Build        |
| ---------------------------------------------------------- | ---------------------------------------------- | ---------------------------- | -------------------------- | ------------ |
| Custom app embedding (Agent Consultant in sidebar)         | Native — live                                 | Supported                    | Plain: limited; Pylon: no  | Full control |
| Live customer data panel (CRM / Customer 360)              | Native sidebar app — live                     | Supported                    | Plain: limited             | Build        |
| Internal escalation (Jira, custom API)                     | Native Jira integration + custom apps          | API possible; no native Jira | Plain: API only            | Build        |
| Agent-triggered workflow execution                         | Not native; delivered via Agent Consultant     | Partial native AI actions    | No                         | Full control |
| Internal collaborator access (read/comment, no agent seat) | Via light agent seats — cost unclear at scale | Limited                      | Plain: yes; Pylon: limited | Build        |

**Assessment**: completed. Scored per requirement in `support-platform-vendor-scorecard.md`, 2026-09-22. See the Comparison Matrix below for the category result.

---

### 5. Data and permissions

| Requirement                         | Zendesk                                                 | Intercom                      | Plain / Pylon             | Build                      |
| ----------------------------------- | ------------------------------------------------------- | ----------------------------- | ------------------------- | -------------------------- |
| B2B / B2C data wall (BPO isolation) | Via brand separation + RBAC — configurable, not native | Workspace separation possible | Plain: limited; Pylon: no | Full control               |
| Role-based access control           | Native — granular                                      | Basic                         | Plain: basic; Pylon: no   | Full control               |
| 500-agent scale                     | Proven at enterprise scale                              | Unproven at this volume       | Not viable                | Dependent on build quality |

**Assessment**: completed. Scored per requirement in `support-platform-vendor-scorecard.md`, 2026-09-22. See the Comparison Matrix below for the category result.

---

### 6. Customer-facing experience

| Requirement                                    | Zendesk                 | Intercom             | Plain / Pylon           | Build |
| ---------------------------------------------- | ----------------------- | -------------------- | ----------------------- | ----- |
| Customer ticket portal                         | Zendesk Guide — native | Intercom portal      | Plain: basic; Pylon: no | Build |
| AI chat history alongside ticket history       | Requires configuration  | Native (same vendor) | No                      | Build |
| Account team thread visibility and email reply | Native                  | Native               | Plain: limited          | Build |

**Assessment**: completed. Scored per requirement in `support-platform-vendor-scorecard.md`, 2026-09-22. See the Comparison Matrix below for the category result.

---

### 7. Integrations & Knowledge (must-have)

| Integration                                  | Zendesk                           | Intercom                 | Plain / Pylon   | Build        |
| -------------------------------------------- | --------------------------------- | ------------------------ | --------------- | ------------ |
| Fin (Intercom) escalation with context       | Native — live                    | Native (same vendor)     | API only        | Build        |
| Jira bi-directional                          | Native integration — in delivery | API only                 | Plain: API only | Build        |
| Salesforce sync                              | Native integration                | API possible             | No              | Build        |
| Internal systems (Treasury, Card Processing) | Via Zendesk API + custom apps     | Via API                  | Plain: API only | Build        |
| Reflex data pipeline (outbound API)          | Live — working                   | Requires re-integration  | Requires build  | Full control |
| Knowledge sources                            | n/a                               | Synced with Intercom Fin |                 |              |

**Assessment**: completed. Scored per requirement in `support-platform-vendor-scorecard.md`, 2026-09-22. See the Comparison Matrix below for the category result.

---

### 8. Analytics and data extract

| Requirement                                        | Zendesk                                    | Intercom                        | Plain / Pylon | Build        |
| -------------------------------------------------- | ------------------------------------------ | ------------------------------- | ------------- | ------------ |
| Full ticket data extract via API (Reflex pipeline) | Live — working                            | Requires re-integration         | Limited       | Full control |
| Taxonomy-level reporting                           | Via Explore — native                      | Basic                           | No            | Build        |
| Billing auditability (AR charges per ticket)       | Non-auditable currently — a declared risk | $0.99/resolution — transparent | N/A           | Full control |

**Assessment**: completed. Scored per requirement in `support-platform-vendor-scorecard.md`, 2026-09-22. See the Comparison Matrix below for the category result.

---

### 9. Environment and configuration deployment

| Requirement                | Zendesk | Intercom | Plain / Pylon | Build        |
| -------------------------- | ------- | -------- | ------------- | ------------ |
| Sandbox / test environment | TBD     | TBD      | TBD           | Full control |
| Configuration as code      | TBD     | TBD      | TBD           | Full control |

**Assessment**: completed. Scored per requirement in `support-platform-vendor-scorecard.md`, 2026-09-22. See the Comparison Matrix below for the category result.

---

## Pricing Assessment

Pricing is assessed separately because it is a commercial question, not a capability question. The right platform at an unsustainable price is still the wrong choice.

### Zendesk (current)

Pricing model is shifting from per-seat to outcome-based:

- $1.50–$2.00 per Automated Resolution
- $50/agent/month Advanced AI add-on
- $35/agent/month QA add-on
- $25/agent/month WFM add-on
- Seat-based pricing for ~500 agents (current tier TBC)

At scale, the AR model could be materially more expensive than seat-based depending on Fin resolution rates. This must be modelled before renewal (see Open Questions). The AR billing mechanism is currently non-auditable — a contractual requirement, not a nice-to-have.

### Intercom (alternative)

- Fin: $0.99/Automated Resolution (vs. $1.50–$2.00 for Zendesk)
- Full platform pricing (ticketing, routing, agent workspace) not published at enterprise scale; requires RFI

The AI resolution cost is lower but the full platform cost comparison is unknown. Intercom consolidation would also require re-integrating Reflex, Jira, and Salesforce.

### Plain

Frontier plan at $139 per seat per month at 100 seats, all channels, AI features, API access and CSM support included, no per-channel or per-feature add-ons, unlimited free viewer seats. Includes 600k Sidekick credits a year, with discounted top-up rates beyond that. Quote received August 2026.

### Pylon

Enterprise tier at $139 per seat per month, annual billing only, 7-seat minimum, which is identical to Plain's Frontier price. Only Enterprise carries the features our scale needs (data warehouse integrations, RBAC, customer portal, dedicated CSM). Add $50 per seat per month for AI Assistants. Pylon's own AI Agents product is priced from $100 a month with undisclosed usage-based scaling, so any figure for it is a floor rather than a cost. Source: [featurebase.app/blog/pylon-pricing](https://www.featurebase.app/blog/pylon-pricing).

### Modelled comparison, 2026 to 2030

Seat trajectory 100, 130, 200, 320, 400. Figures exclude discounting.

| Year | Zendesk seats | Zendesk add-ons (unconfirmed) | **Plain** | Intercom | Pylon |
|---|---|---|---|---|---|
| 2026 | $278,640 | $40,000 | **$166,800** | $193,200 | $228,000 |
| 2027 | $346,194 | $52,000 | **$216,840** | $251,160 | $296,040 |
| 2028 | $503,820 | $80,000 | **$333,972** | $386,400 | $454,800 |
| 2029 | $774,036 | $128,000 | **$549,615** | $618,240 | $726,960 |
| 2030 | $954,180 | $160,000 | **$713,844** | $772,800 | $908,400 |

Zendesk seat costs come from the signed 24-month order form (100 agent seats, GBP, signed 27 June 2025): `04-active-work/research/evidence/2025-06-27-zendesk-signed-contract-Q-540753.pdf`. On top of seats, Zendesk carries roughly $130,000 a year of third-party bolt-ons that Plain replaces natively: Salto for config-as-code and audit trail, SweetHawk for approvals, and a sandbox fee.

Cumulative 2026 to 2030, Plain is about $876,000 cheaper on seats and about $650,000 cheaper on the bolt-on stack, roughly **$1.5M** in total. Pricing is a 3% hygiene gate in the scorecard and is not the deciding factor between vendors: seat prices are close and the material difference is what each price includes.

**The AR fee remains the largest unresolved number.** If Zendesk's $1.50 to $2.00 per Automated Resolution applies to Fin-driven resolutions passing through Zendesk, at 2030 volume (1.72m AI-resolved contacts) that is a $2.6M to $3.4M annual exposure, larger than the entire seat comparison above. A written answer has been requested from the Zendesk account team (Open Question 2).

### Build

Engineering cost is prohibitive. Not modelled.

---

## Options

### Option 1: Keep + Extend

Renew Zendesk at contract. Use the renewal as leverage to negotiate price, SLAs, and audit rights. Continue building the AI workflow layer (Agent Consultant) outside native Zendesk, and complete the B2C configuration build-out in 2026.

**What this means in practice:**

- Invest in Zendesk configuration for B2C: complaint handling, Consumer Duty flows, vulnerable customer flags, phone channel (Zendesk Talk)
- Negotiate on AR pricing, Advanced AI add-on costs, and response SLAs at enterprise scale
- Demand audit rights on "Automated Resolution" billing before signing
- Continue Agent Consultant as the AI workflow execution layer outside native Zendesk
- Accept that some capabilities (agent-triggered autonomous execution) require custom build

**Considerations:**

- Zero roadmap disruption — all 2026 deliverables are in flight on Zendesk
- Zendesk leads on routing depth, SLA management, compliance tooling, and must-have integrations across the current requirement set
- Migration to any alternative would consume 2+ engineers for 6–12 months
- Forethought acquisition (Resolution Learning Loop) indicates platform investment in AI workflow capability
- Zendesk's architecture is API-first and build-around — Agent Consultant, Agent Toolkit, and Reflex all follow this pattern today

**Why these considerations no longer hold (2026-09-22).** Option 1 is rejected. Three of the five points above were the strongest case for keeping Zendesk in April 2026, and each has since been contradicted by evidence:

- "Zendesk leads on must-have integrations" is wrong on our own experience. It scores lowest of four on integration ease (1.50): the Jira app was deprecated and never implemented with no replacement available, Salesforce needed a custom BigQuery build, and knowledge content cannot sync in from an external source.
- "Forethought acquisition indicates platform investment in AI workflow capability" reads the opposite way now. That acquisition is why Zendesk is consolidating on its own AI stack, terminating legacy AI Agents in December 2026, and why it ended the Intercom partnership in April 2026.
- "Zendesk's architecture is API-first and build-around" holds for reading ticket data, not for configuration. Config-as-code scores 1.00 and only reaches that by buying Salto. All administration is manual UI work.

The remaining two points are real and stand as the cost of switching: zero roadmap disruption, and a migration that consumes engineering capacity for multiple quarters. They are priced into the Track C build rather than argued away.

**Risks and mitigations:**

| Risk                                                    | Likelihood | Impact | Mitigation                                                                                      |
| ------------------------------------------------------- | ---------- | ------ | ----------------------------------------------------------------------------------------------- |
| AR billing becomes unauditable/expensive at scale       | Medium     | High   | Demand audit rights and pricing caps in renewal contract; model volume scenarios before signing |
| Zendesk vendor support quality continues to deteriorate | Medium     | Medium | Escalate to enterprise account team; SLA for human support response times is contractual        |
| B2C configuration takes longer than expected            | Low        | High   | Begin Consumer Duty configuration design H2 2026; do not leave for 2027                         |
| Agent-triggered workflow execution gap widens           | Low        | Medium | Agent Consultant already fills this gap; watch Zendesk roadmap for native capability            |

---

### Option 2: Buy — Replace with Intercom

Migrate from Zendesk to Intercom as the primary platform before June 2027.

Intercom has meaningful advantages on AI chat history, Fin integration cost, and unified AI + ticketing UX. Known gaps against the requirement set include routing depth, SLA management, phone channel, and Consumer Duty compliance tooling. Migration cost would include Reflex re-integration, Jira re-integration, and team retraining (estimated 6–12 months engineering).

**Considerations**: Enterprise routing depth, SLA management, and phone channel maturity are the primary unknowns to assess. Full platform pricing at Checkout's scale is unpublished — requires RFI.

**Vendor call notes (2026-09, Intercom)** — qualitative, not RFI/POC evidence; does not feed the scorecard's numeric scores:

- Strong as a ticketing system: native Fin, Copilot for agent AI, workflow builder as a UI layer (vs. Zendesk Triggers config)
- All standard channels supported natively
- Operator AI tool (comparable to Zendesk's Sidekick) for internal diagnosis on tickets and metrics
- Back-office (non-customer-facing) ticket model is simple: create a ticket, assign to type or team
- Native Jira and Salesforce connectors
- Simple UI; separate test and prod environments for deploying config changes
- Good API endpoint coverage
- **Gap — AI compatibility (scorecard 3.3, "abstract our core services" principle)**: Copilot has no custom integrations and limited skill customisation — described as a black box. This weakens the case for Copilot as the Agent Consultant equivalent inside Intercom.
- **Gap — Config as code (scorecard 5.3)**: configuration is done mostly via UI, not config-as-code; vendor says this may improve long-term but nothing committed
- **Gap — Agent experience / data model (scorecard 1.21, 4.11–4.12)**: object model is restrictive — mandates certain data points, and nested logic would need custom API calls to link field IDs rather than native support
- **Gap — Agent experience / Ops-wide fit (scorecard category 4, "abstract our core services" principle)**: not convinced Intercom fits Ops teams beyond Care. It's built for customer-facing work, not internal enabling work with AI workflows across teams.

**Reference customer call notes (2026-09, Zilch)** — reference customer, ~250 BPO agents + 40 internal staff, migrated off Zendesk to Fin + Intercom. This is genuine reference-customer evidence (scorecard category 6a asks for exactly this), not vendor marketing — usable as supporting evidence for scorecard scoring, though still short of our own POC:

- **Partnership fit (scorecard 6.2)**: chose Intercom to be "a bigger fish in a smaller pond" — wanted to be a material customer where scale matters to the vendor (Zilch is Intercom's No. 2 account). Cited better responsiveness and consultancy than they got from Zendesk/Salesforce, who they felt didn't guide them on how to use the tech. Now locked in and the relationship is strong, despite Intercom's Salesforce acquisition.
- **Partnership fit (scorecard 6.2, negative)**: "the person you get for help is key" — support quality is described as individual-dependent, not a consistent guarantee
- **Partnership fit / AI compatibility (scorecard 6.1)**: growing pains with change control on Fin, and a black box on which features are coming next — corroborates our own vendor call's "black box" finding on Copilot
- **Channels (scorecard 1.4/1.5)**: live chat + email with Fin integration called out as a standout strength — "seamless"
- **AI compatibility (scorecard 3.1/3.3)**: uses Fin's attribute detection to control conversation flow — matches our pluggable-AI requirement in spirit, though this is Intercom's own AI, not an external one
- **Integration ease (scorecard 2.7/2.9)**: uses the "Pro" analytics tier — flags this is a paid add-on, not included in base
- **Agent experience (scorecard 4.6/4.7, with a specific limitation)**: multi-agent/location/BPO setup via separate Inboxes per line of business (e.g. Chargebacks, Collections, Refunds), each assigned to a specific BPO — but **cannot segment team members into organisations**; team members are assigned to an Inbox individually, not grouped by org. This is a materially different model from a true B2B/B2C data wall (4.11) and worth testing directly in POC.
- **Agent experience (scorecard 4.12)**: custom roles available to restrict conversation/report visibility
- **Config as code / AI compatibility (scorecard 3.4/5.3)**: workflow automation "helpful" for both AI flow control and SLA management — SLAs are managed via workflows rather than a native SLA policy engine, which is a mechanism difference worth noting even where the outcome (SLA enforcement) is achieved
- **Channels (scorecard 1.9)**: second- and third-line tech teams work from back-office tickets only — consistent with our own vendor call's description of the back-office ticket model

---

### Option 3: Buy — Replace with Plain (recommended)

**This is the recommended option.** Plain is headless, API-first and config-as-code, with a flexible custom object model. It scores 2.46 of 3.0 on the weighted scorecard, the highest of the four candidates.

**Assessed, not assumed.** A four-week POC ran 27 July to end August 2026 across engineering, product and support ops. Config-as-code was proven end to end (taxonomy, thread fields, field dependencies, labels and workflows deployed from a GitHub repo via GraphQL and GitHub Actions, with drift detection, 11 test cases passed in week one). Tier, skill, regional and capacity-based routing were tested, as was external AI classification via API. Two-workspace B2B/B2C isolation and seat-based scaling to 500+ were validated. Three gaps were committed in writing with dates: SLA model (first week of September 2026), multiple business hours (by 14 September 2026), Fivetran export to BigQuery (by end of 2026). Full results in `plain-business-case-draft-v1.md`.

**Open caveats.** Plain has not been run at 500-agent scale by any customer we have spoken to (Vercel operates ~60 agents). Phone is not native and needs a telephony integration, which is acceptable because phone is confirmed not required for Ray. Handle-time measurement scores 1.00 against Intercom's 3.00 and is a feature request, not a shipped capability. Consumer Duty tooling is not a requirement: Ray is not UK-launched and cards are issued via Checkout SAS, so Ray sits outside Consumer Duty and SCA.

**Reference customer call notes (2026-09-18, Vercel — Will Viles)** — reference customer, migrated from Salesforce Service Cloud. **Scale caveat**: Vercel runs ~60 support agents on Plain, handling ~1,200 cases/week, with a single system operator (Will) owning all admin, configuration, and integration work. Still materially smaller than Checkout's 500-agent target, and their multi-workspace/RBAC gap below has not been stress-tested at our scale. Treat scale-dependent findings (data segregation, config-as-code operating model) as directionally useful, not scale-validated:

- **Partnership fit (scorecard 6.1)**: chose Plain over the incumbent for its "vision of headless support" and because Vercel didn't want off-the-shelf agents — wanted to build every agent (help box, triage, retro) themselves. Was "customer zero" for a lot of functionality, i.e. a heavy co-build relationship, not a configure-and-go one.
- **Partnership fit (scorecard 6.1, negative)**: roadmap delivery has slipped materially — functionality quoted at "4 months" 12 months ago took 8 months to ship. Direct quote: "they haven't exceeded expectations... but they do get round to it." Consistent with "not the fastest" vendor, compensated for by API-level flexibility to build around gaps yourself.
- **Reliability (scorecard 6.4)**: "absolutely zero downtime" reported (informal, not a contractual SLA data point).
- **Partnership fit / Implementation weight (scorecard 6.3)**: Plain's entire admin, requirements gathering, and the original Salesforce migration are run by one system operator, supporting a ~60-agent team. Strong evidence that Plain's day-to-day operating and configuration overhead is genuinely light for a single admin to own — though this is also a single point of failure at Vercel's scale, not evidence the same 1-operator model holds at 500 agents.
- **AI compatibility (scorecard 3.3)**: full custom multi-agent architecture built on Plain's API — a "Sel[ect]" first-contact agent creates the case, a fast triage agent runs on creation (posts a note, doesn't investigate deeply), and enterprise/notable accounts get a retro afterward. Entirely Vercel's own logic; Plain provides the substrate only. Direct quote: "everything is easy, and you're completely in control" — this is close to a working example of Checkout's "abstract our core services" principle in production.
- **AI compatibility (scorecard 3.1, mixed)**: tried Plain's native knowledge-base/documentation agent approach — "didn't feel like the right approach," implying dissatisfaction, though the detail didn't come through clearly on the call.
- **Integration ease (scorecard 2.2/2.5, gap)**: native Linear/Jira-equivalent ticket linking is "very basic" — CS/engineering had to build the entire flow (custom app, prefilled form, mutating the thread via API) themselves, describing it as a 6-month effort. Matches the general pattern that anything not core to Plain's own product must be self-built on the GraphQL API. Confirmed the same is true for Jira specifically when asked directly.
- **Integration ease (scorecard 2.5, strength)**: Plain exposes its full GraphQL SDK — "you can do anything that they do inside their UI," entirely webhook-driven, integration logic written in TypeScript. This is the strongest API-completeness signal gathered from any reference call so far.
- **Config as code (scorecard 5.3)**: configuration managed primarily through code/API ("edge config" for dynamic settings), not the UI — consistent with the API-first framing. Exception: the labelling/tagging model (hierarchical, e.g. product > sub-label, used for analytics) is managed more directly/transiently, not fully as code.
- **Agent experience / data and permissions (scorecard 4.11/4.12, significant gap)**: Plain requires **separate workspaces ("spaces")** for privacy/security/trust segregation rather than granular RBAC within one workspace — Vercel called this out as a real limitation ("one area I think they're lacking in") that Plain "hasn't really wanted to work on" resolving. Practical effect: cross-workspace visibility needs an API call even within the same company, which Will agreed "doesn't really make sense." Plain added basic cross-workspace thread-state API support only **this week** (2026-09), and Will believes a label-based approach is in progress but couldn't confirm details. **This is the same class of gap flagged for Intercom** (Zilch: can't segment team members into orgs) — both vendors handle multi-team/BPO data segregation more coarsely than a native, granular data wall. Note: Vercel split workspaces for their own privacy/security/trust reasons, not a B2B/B2C-style split — we don't yet know whether Checkout's data-wall requirement actually needs multiple workspaces in the way Vercel does, or whether RBAC within a single workspace would suffice. Don't assume the requirement maps 1:1; confirm our own need first, then test the relevant vendor mechanism (workspace split vs. RBAC) directly in POC rather than taking either vendor's description at face value.
- **Channels (scorecard 1.6)**: native Slack support is in progress; previously required a custom-built agent to ingest Slack threads. Support currently centres on Slack as the primary customer-conversation surface (a deliberate design choice, not a Zendesk-style ticket-first model), which may not map directly onto Checkout's channel mix.
- **Migration precedent**: Vercel did not migrate historical case/thread data from Salesforce — decided it wasn't worth the effort given the data models didn't match cleanly. Matches Checkout's own prior Salesforce-to-Zendesk migration approach; useful precedent if a Zendesk migration proceeds.

---

### Option 4: Build

Team capacity is 5 engineers + 1 EM, + 2 Support Admins. Building and maintaining enterprise-grade ticketing infrastructure would consume the team's full delivery capacity.

**Considerations**: Not viable as a primary path. Relevant only if no vendor meets requirements and a minimal custom layer is needed on top of an existing platform.

---

## Comparison Matrix

Superseded as of 2026-09-22 by the weighted scorecard. This is the summary view. Per-requirement scores, evidence and evidence tiers are in `support-platform-vendor-scorecard.md`.

Scale: 0 not supported, 1 custom build required, 2 supported via configuration or paid add-on, 3 native. All four vendors are scored at 100% weight coverage.

| Category | Weight | **Plain** | Intercom | Pylon | Zendesk |
|---|---|---|---|---|---|
| Flexible channels, data model and routing | 20% | **2.62** | 2.24 | 2.45 | 2.05 |
| Agent experience | 20% | **2.14** | 1.89 | 1.69 | 1.58 |
| Integration ease | 15% | 2.25 | **2.50** | 2.00 | 1.50 |
| AI compatibility | 15% | **2.60** | 1.60 | 1.80 | 1.20 |
| Config as code | 10% | **3.00** | 1.50 | 0.50 | 1.00 |
| Partnership and reliability | 10% | **2.67** | 1.83 | 1.67 | 1.38 |
| Customer-facing experience | 7% | **2.00** | 1.50 | **2.00** | 1.50 |
| Pricing | 3% | **2.33** | 2.00 | 2.00 | 1.67 |
| **Weighted total (of 3.0)** | 100% | **2.46** | 1.94 | 1.82 | 1.52 |

**Ranking: Plain (2.46) > Intercom (1.94) > Pylon (1.82) > Zendesk (1.52).**

Plain leads six of eight categories, ties customer-facing experience with Pylon, and loses integration ease to Intercom on native Jira and native handle-time reporting. Zendesk scores lowest overall and lowest on integration ease, the category where an incumbent with live integrations should win: the Jira app was deprecated and never implemented with no replacement available, the Salesforce link required a custom BigQuery build, and knowledge content cannot sync in from an external source.

**Read this alongside the earlier ranking.** Until 2026-09-21 Zendesk showed 2.06 and read as a close second to Plain. That figure was a coverage-adjusted partial over 70% of the weighting, with categories 4 and 6 unscored. The 2026-09-22 pass filled every remaining Zendesk cell and rescored six cells carried forward from this RFC's own April read (2.1, 2.2, 2.3, 4.4, 7.1, 8.4 all dropped once checked against how they work day to day). Zendesk's full-coverage total is 1.52. In the same pass Intercom rose from 1.83 to 1.94 on confirmed native Jira and Salesforce apps, and Pylon rose from 1.77 to 1.82 after its "Bring Your Own Agent" capability was verified.

**Build is out of scope for the scorecard.** See Option 4: not viable at current team capacity.

---

## Recommendation

**Replace Zendesk with Plain.** Migrate Ray (consumer) first in Q1 2027, then Merchant Care in H1 2027, ahead of the June 2027 renewal. Option 3.

### Why

1. **Zendesk has closed off third-party AI, and Fin is the casualty.** Zendesk's Chief Customer Officer confirmed in writing on 1 April 2026 that Zendesk "made the decision to stop partnering with Intercom / Fin going forward." New integrations are blocked and ours survives only as a discretionary exemption. Intercom confirmed the same from its side on 11 June 2026, with engineering in "lights on" mode on the Zendesk integration. Fin is our AI resolution layer, and on Zendesk its continued improvement depends on a vendor building a competing product. Sources: `04-active-work/research/evidence/2026-04-01-zendesk-notice-intercom-integration-partnership-ended.pdf`, `04-active-work/meeting-notes/2026-06/2026-06-11-intercom-renewal.md`.
2. **The volume we are scaling into makes manual configuration untenable.** Contact volume grows 36x by 2030 (60,049 to 2,154,799), one customer segment becomes four, and 79% of 2030 volume is a consumer business with no platform today. Zendesk holds 500+ configuration items maintained entirely through the UI, with high-complexity changes taking 2+ weeks. Config-as-code is the only route to that scale without growing admin headcount linearly. Source: `01-knowledge-base/metrics/contact forecasting.md`.
3. **Plain scores highest on our own published criteria, on our own evidence.** 2.46 against 1.52 for the incumbent, on full coverage, with weights set before scoring and one line of evidence per cell. Plain's strongest cells are POC-verified rather than vendor-claimed.
4. **It is the only candidate that supports the target architecture.** Plain is headless and API-first with a seat-free machine-user identity for AI agents, so the abstraction layer stays ours and any vendor in the stack, including Fin, stays swappable without another migration. Intercom requires a third-party AI agent to run as a paid human seat. Zendesk blocks the concept outright.
5. **The commercial case holds independently.** Plain is roughly $242,000 a year cheaper all-in in 2026 and about $1.5M cheaper cumulatively to 2030, before any AR-fee exposure, while replacing three bolt-on contracts with one platform and one security review.
6. **The 2027 operating model depends on it.** The specialist pod model delivers 24/7 coverage at 35 agents instead of the 48 a generalist model needs. It requires API-first routing with programmatic skill assignment and fallback, which Zendesk's static groups cannot express. Source: `04-active-work/meeting-notes/2026-09/2026-09-15-plain-vs-zendesk-migration-case.md`.

### Why not the alternatives

- **Keep and extend Zendesk (Option 1)**: rejected. It scores lowest of four on full coverage, and the AI-partnership risk is the specific thing the platform has to carry through 2030. Keeping it also leaves the $2.6M to $3.4M AR exposure unresolved and the $130,000-a-year bolt-on stack permanent.
- **Intercom (Option 2)**: rejected on architecture and on ownership. No config-as-code (confirmed negative in Intercom's own scoring pass), no swappable AI agent identity, and a data model that cannot represent a user belonging to more than one company. Salesforce signed a definitive agreement to acquire Intercom on 15 June 2026 for $3.6bn, expected to close October 2026 to January 2027, which triggers our standing rule on conglomerate acquisition. Fin is retained as the AI layer either way: this is a judgement about Intercom as the case platform.
- **Pylon**: rejected. Lowest config-as-code score of the four (0.50), UI-only configuration, no sandbox, and Slack-first by design. Cost was never the reason, since its Enterprise seat price matches Plain's. Note that Pylon's whole column is desk research against public documentation with no RFI or POC, so it carries a lower evidence tier than Plain's or Intercom's.
- **Build (Option 4)**: rejected on capacity. 5 engineers, 1 EM and 2 support admins cannot build and maintain enterprise-grade ticketing at 500-agent scale without consuming the team's entire delivery capacity. The recommendation is hybrid: buy the case-management core, build only the abstraction and orchestration layer.

### Conditions on this recommendation

Three items must close before contract signature. None of them changes the direction, and each has a named gate.

| Condition | Why it matters | Gate |
|---|---|---|
| Plain funding and runway evidence | Scorecard row 6.9 is deliberately blank rather than guessed. Plain is a materially smaller company than the incumbent, and continuity is the one dimension where Zendesk scores best (2.00 against 1.00 for Intercom and Pylon) | Session with Plain's CEO and CPO, 23 September 2026. Continuity and data-export protections to be contractual |
| Written answer on Zendesk's AR fee | $2.6M to $3.4M annual swing at 2030 volume, larger than the entire seat comparison | Zendesk account team, before the renewal negotiation closes |
| Jira integration and data-wall evidence conflict | The POC reads "native" where the Vercel and Fyxer reference calls both describe self-built. Scorecard categories 2 and 4c | Resolve before contract. Effort sized into the Track C build either way |

### Decision and owners

Consultative consensus across VP of Product, Director of Operations, Director of Operations Excellence and Product, with CPO and COO confirming the architecture direction and the procurement go-ahead. Working target for the procurement gate is 30 September 2026.

---

## Implementation Plan

Rewritten 2026-09-22. The prior plan assumed a Zendesk renewal and a Consumer Duty configuration build inside Zendesk. Both assumptions are dead: the recommendation is replacement, and Ray sits outside Consumer Duty because it is not UK-launched and cards are issued via Checkout SAS.

### Track A: Selection and procurement (September to early November 2026)

- Internal approval: leadership demo (held week of 24 August), this RFC and the leadership deck, verification of Plain's September feature ships, vendor viability session with Plain's founders (23 September)
- Parallel procurement and security: budget, InfoSec, DORA Art. 30, PCI DSS 12.8 and 12.9, GDPR Art. 28 assessment, MSA and DPA, commercial close
- Negotiate the three conditions above into the contract, plus auto-renewal notice (Plain's standard is 30 days, not 60) and a handle-time measurement commitment
- Procurement is the critical path for Track B

### Track B: Ray (B2C) validation (December 2026 to Q1 2027)

- December 2026 internal alpha: 50 to 100 friends-and-family users, deliberately not the full architecture, a pass-through web form with taxonomy and a few fields. Not on Zendesk
- Q1 2027 external beta: Ray on Plain with the full architecture
- Ray is the first Care deployment with no Zendesk and the validation ground for Plain at real, if small, volume

### Track C: Merchant Care (B2B) build and migration (November 2026 to H1 2027)

- Production configuration via config-as-code, integrations (Fin, Jira, Salesforce, BigQuery), agent tooling, training
- No lift-and-shift: much of the Zendesk build is workarounds for Zendesk and is not carried across
- Migrate API channels first, staff for those, then move email in a single cutover and reroute forwarding away from Zendesk
- Parallel run against Zendesk, then cutover well ahead of the June 2027 renewal
- Gate: engineering estimates for this track cannot be produced until the Fin and Plain target architecture is signed off

### Track D: Wider Operations (2027 onward)

- Risk ops, compliance ops and finance ops onboard as workflow deployments from the same repo, 300+ users
- Merchant onboarding moves from Salesforce to threads
- Marginal effort per additional team is a code review, not a re-implementation

---

## Success Metrics

| Metric | Current | Target | Timeline |
|---|---|---|---|
| Recommendation made | Done, 2026-09-22 | Plain | Complete |
| Procurement and security approval | Not started | Cleared, contract signed | Early November 2026 |
| Ray internal alpha live on Plain | Not started | 50 to 100 users supported, no Zendesk | December 2026 |
| Ray external beta on Plain | Not started | Full architecture live | Q1 2027 |
| Merchant Care migrated off Zendesk | Not started | Cutover complete, parallel run closed | Before June 2027 renewal |
| Pick-up to deployment for a config change | 1 to 2 days low complexity, 2+ weeks high | Reviewed deploy, same working day | H1 2027 |
| Third-party bolt-on contracts | 3 (Salto, SweetHawk, sandbox) | 0 | At cutover |
| Handle-time measurement on the new platform | Not available in Plain | Native or co-designed metric live | Before Merchant Care cutover |

---

## Open Questions

Statuses updated 2026-09-22. Questions 3, 4 and 5 are closed by the recommendation itself.

### Live

1. **Q**: Is Plain funded and viable through 2030?

   - **Why it matters**: The only condition on the recommendation that could change its direction. Scorecard row 6.9 is deliberately blank rather than guessed
   - **Who can answer**: Plain's CEO and CPO
   - **Deadline**: 23 September 2026
2. **Q**: Does Zendesk's $1.50 to $2.00 Automated Resolution fee apply to Fin-driven resolutions passing through Zendesk?

   - **Why it matters**: A $2.6M to $3.4M annual swing at 2030 volume, larger than the entire seat comparison. It is also the single strongest commercial argument against renewal if the answer is yes
   - **Who can answer**: Zendesk enterprise account team, in writing
   - **Deadline**: Before the renewal position is finalised
3. **Q**: Is Plain's Jira integration native or self-built, and does our B2B/B2C data wall need separate workspaces or RBAC within one?

   - **Why it matters**: The POC and two independent reference calls (Vercel, Fyxer) disagree. Affects scorecard categories 2 and 4c and the Track C build estimate
   - **Who can answer**: Plain solutions engineering plus our own test, against our own requirement rather than Vercel's
   - **Deadline**: Before contract signature
4. **Q**: What does the modelled Zendesk add-on line ($40,000 in 2026 rising to $160,000 by 2030) actually cover?

   - **Why it matters**: It is excluded from the headline cost comparison until confirmed, which understates the incumbent's cost
   - **Who can answer**: Engineering Manager / Zendesk account team
   - **Deadline**: Before the cost slide is presented as final
5. **Q**: Should the Zendesk contract be extended by six months to buy migration time?

   - **Why it matters**: It would be useful cover for unknowns, but formally notifying Zendesk generates noise, degrades the support we get in the meantime, and drags spend across the year boundary
   - **Who can answer**: Procurement, with Charlie and the Engineering Manager
   - **Deadline**: Open. Source: `04-active-work/meeting-notes/2026-09/2026-09-04-charlie-fraser-platform-assessment.md`

### Closed

6. **Current Zendesk tier and seat count**: answered. Signed 24-month order form, 100 agent seats, GBP, signed 27 June 2025, renewing June 2027. Source: `04-active-work/research/evidence/2025-06-27-zendesk-signed-contract-Q-540753.pdf`
7. **Projected AR volume at 2027 and 2030 resolution rates**: modelled. 1.72m AI-resolved contacts at 2030. What remains open is whether the fee applies, which is question 2 above
8. **Does Zendesk's configuration satisfy Consumer Duty?**: no longer applicable. Ray is not UK-launched and cards are issued via Checkout SAS, so Ray sits outside Consumer Duty and SCA. Phone support is confirmed not required for Ray
9. **Zendesk's roadmap for agent-triggered workflow execution**: moot. Zendesk is not the platform, and its April 2026 decision to close off third-party AI is the reason
10. **Is Sunshine Conversations included in our tier?**: moot for the same reason. Channel breadth is now assessed against Plain

---

## Dependencies

- [x] Finance input on current Zendesk contract value and renewal timeline: signed order form obtained
- [x] Contact volume forecast and Fin resolution rate projections to model AR pricing: modelled, `contact forecasting.md`
- [x] VP of Product and Directors alignment on renewal versus replacement framing: replacement, per this recommendation
- [ ] Legal/Compliance input on Consumer Duty configuration requirements: no longer required for Ray. Still required for open banking payers and issuing cardholders in 2027, where the FCA obliges us to support end users we have no account relationship with
- [ ] Sign-off on the Fin and Plain target architecture. Blocks Track C estimates
- [ ] Procurement advice on when to formally notify Zendesk, and whether to extend by six months

---

## Related Documents

**Note on weights (current as of 2026-09-18)**: category weights were restructured around the seven assessment principles, superseding the 2026-08-12 driver-based weighting. Current weights: agent experience 20%, flexible channels/data model/routing 20%, integration ease 15%, AI compatibility 15%, config as code 10%, partnership and reliability 10%, customer-facing experience 7%, pricing 3%. Partnership and reliability rose from 3% to 10% because strategic vendor fit is a named principle rather than a renewal-risk check. Pricing stays a 3% hygiene gate. Weights were fixed before the 2026-09-21 and 2026-09-22 scoring passes. See `support-platform-vendor-scorecard.md` for the full rationale.

- `04-active-work/working-files/zendesk-decision-deck-content.md` — leadership deck content for the CPO/COO audience, the compressed version of this RFC
- `04-active-work/research/support-platform-vendor-scorecard.md` — weighted, numeric scorecard; the current scoring instrument, superseding the candidate tables above
- `04-active-work/research/support-platform-vendor-requirements.md` — the 60 requirement definitions the scorecard scores, one to one
- `04-active-work/research/plain-business-case-draft-v1.md` — Operations business case with full four-week POC results
- `04-active-work/research/multi-team-routing-overview-plain-intercom.md` — routing requirements shared with both vendors as design input
- `04-active-work/research/vendor-poc-scope.md` — POC gate and differentiator test flows that feed the scorecard
- `04-active-work/research/zendesk-current-config-flow-map.md` — conceptual map of current Zendesk config (routing, SLA, automations, triggers), sourced from the Salto IaC repo, for walking vendors through existing flows
- `01-knowledge-base/products/zendesk.md` — Checkout.com Zendesk setup and capabilities
- `05-archive/2026/investigations/Zendesk Viability_ AI, Pricing, Market.md` — External market research on Zendesk strategic position
- `04-active-work/strategy/care-strategy-2026-2030.md` — Care strategy, segment scenarios and resolution-rate targets
- `01-knowledge-base/strategy/care-product-model.md` — Care Product flywheel model
- `01-knowledge-base/metrics/contact forecasting.md` — Volume projections 2026 to 2030 by segment
- `2026 deliverables.md` — Current roadmap dependencies on Zendesk

---

## Appendix: Vendor Assessment Requirements

Derived from [support platform flows](../strategies/support%20platform%20flows.md). This is the original 11-section requirement set from April 2026. It was restructured on 2026-09-18 into the 8 weighted assessment categories now used for scoring, and the canonical requirement definitions live in `support-platform-vendor-requirements.md` (60 requirements, one to one with the scorecard). Both views are kept: the four-week Plain POC was run against the 11 sections below, so this is the framing those results report under.

### 1. Multi-channel entry points

| Requirement                | Detail                                                                          |
| -------------------------- | ------------------------------------------------------------------------------- |
| Email ingestion            | Native ticket creation from inbound email                                       |
| Email user enrichment      | Auto-match inbound email to the correct org record; handle emails that belong to multiple orgs or have no match |
| Domain mapping             | Link email domains to org records (e.g. @checkout.com → Checkout.com org) so unrecognised senders can be resolved |
| AI Agent escalation path   | Receive handoff from AI Agent (Fin for now) with full conversation context      |
| Live chat with human agent | Native or integrated chat for B2B                                               |
| Instant messaging channels | Slack/Teams/WeChat/custom integrations for B2B support (2028–2029 requirement) |
| Phone channel              | Native or integrated IVR + call routing for B2C                                 |
| Mobile app chat            | B2C channel (2027 wallet launch)                                                |
| Internal ticket submission | Account teams can raise tickets on behalf of customers                          |

**Assessment question**: Which channels are native vs. add-on, and what is the per-channel cost at 500-agent scale? How is email-to-org matching configured — domain rules, manual mapping, or API enrichment?

---

### 2. AI triage and classification

| Requirement                       | Detail                                                                                                                 |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Auto-classification on escalation | Taxonomy tags applied to any ticket escalated from AI, before human assignment                                         |
| AI agent handoff with context     | Conversation transcript and metadata passed to human agent workspace                                                   |
| Pluggable AI layer                | Must allow external AI (Agent Consultant) to operate in the agent workspace without requiring the platform's native AI |

**Assessment question**: Can the platform accept AI classifications from an external system, or does classification require the platform's native AI?

---

### 3. Routing & field logic

| Requirement                             | Detail                                             |
| --------------------------------------- | -------------------------------------------------- |
| Support plan / tier model               | Routing based on customer tier (P0–P3)            |
| Skill-based routing                     | Agent skill tags matched to ticket classification  |
| SLA per tier and taxonomy value         | Different SLA clocks per priority and contact type |
| Customisable ticket and customer fields | Company-level and individual-level custom fields   |
| Flexible tagging/field system           | Taxonomy mapping and analytics use cases           |

Ultimately, we need a flexible routing system where we can use attributes in branches and fallbacks.

**Required routing flow**: Ticket arrives → email enrichment populates org/tier fields → fields determine SLA and routing to correct team via skill matching → priority ranking applied (SLA timer, contact type) → auto-assignment to agent with capacity controls; no cherry-picking.

---

### 4. Agent workspace

| Requirement                        | Detail                                                                                                                             |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Custom app framework               | Platform provides a developer SDK or API for building and deploying custom sidebar apps — not restricted to marketplace apps only |
| App capability scope               | Custom apps can read ticket data, make external API calls, and write back to the ticket — not read-only                           |
| App deployment and versioning      | Custom apps can be deployed and updated without requiring vendor involvement or marketplace approval                               |
| Live customer data panel           | CRM and user data surfaced from our own sources in the agent UI                                                                    |
| Internal escalation to other teams | Jira integration and custom API integrations with read/write access                                                                |
| Agent-triggered workflow execution | Agent approves AI action; platform passes execution signal, or allows external system to do this                                   |
| Internal collaborator access       | Account teams and non-agent staff can view threads and leave internal comments without a full agent seat                           |

**Assessment questions**: What is the custom app development framework (SDK, API, tooling)? Are there restrictions on what custom apps can read/write, or requirements to publish via a vendor marketplace?

---

### 5. Data and permissions

| Requirement               | Detail                                                                                                                                   |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| B2B / B2C data wall       | Two isolated environments — BPO handling B2C must never see B2B data                                                                    |
| Role-based access control | Granular permissions per team and per brand                                                                                              |
| 500-agent scale           | Must support projected 2030 headcount without degraded performance or disproportionate per-seat cost                                     |
| Flexible data model       | Custom objects and fields sufficient to model our org hierarchy and ISV data via our own integrations — no hardcoded schema assumptions |

**Assessment question**: Does the platform support custom object models, or are organisations and users a fixed schema?

---

### 6. Customer-facing experience

| Requirement                    | Detail                                                   |
| ------------------------------ | -------------------------------------------------------- |
| Customer ticket portal         | Merchants can view open tickets and conversation history |
| AI chat history visibility     | Previous AI Agent conversations visible                  |
| Account team thread visibility | AMs can view and reply into ticket threads over email    |

---

### 7. Integrations (must-have)

| System                  | Direction      | Requirement                                                                                                                                         |
| ----------------------- | -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Fin (Intercom)          | Inbound        | Escalation with full conversation context                                                                                                           |
| Jira                    | Bi-directional | Create/update Jira issues from tickets; sync status back                                                                                            |
| Salesforce              | Read           | Sync case numbers and customer data                                                                                                                 |
| Knowledge sources       | Inbound        | Sync knowledge content from an external source (website URL or GitHub repo) for use by the AI agent layer — no manual article duplication required |
| Custom APIs             | Read           | Pull data from internal systems (e.g. BigQuery)                                                                                                     |

**Assessment question**: What knowledge sync mechanisms are supported (URL crawl, GitHub, API push)? Is sync automated on change, or manual?

---

### 8. Analytics and data extract

| Requirement               | Detail                                                                                                       |
| ------------------------- | ------------------------------------------------------------------------------------------------------------ |
| API access to ticket data | Full export of ticket data fields for Analytics pipeline                                                     |
| Taxonomy-level reporting  | Filter and group by custom taxonomy tags                                                                     |
| SLA breach alerting       | Automated in-platform alerts before and on SLA breach, configurable per tier — for agent and supervisor use |
| AHT / agent task time     | Native measurement of handle time per ticket and per agent; required for cost-per-contact modelling         |


---

### 9. Environment and configuration deployment

| Requirement                  | Detail                                                                                                                                        |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Sandbox / test environment   | A test environment that mirrors production configuration — routing rules, SLAs, integrations — so changes can be validated before promotion |
| Configuration promotion path | A defined mechanism to promote configuration from test to production — not manual recreation                                                 |

**Assessment question**: Is there a supported configuration promotion workflow between sandbox and production?

---

### 10. Vendor reliability and operational trust

| Requirement                | Detail                                                                                              |
| -------------------------- | --------------------------------------------------------------------------------------------------- |
| Uptime SLA                 | Contractual uptime commitment for core ticketing; messaging components (if used) covered separately |
| Enterprise support SLA     | Guaranteed human response time for P1/P2 platform issues — not bot-first deflection                |
| Named account team         | Dedicated enterprise contact with defined escalation chain contractually named                      |
| Billing dispute resolution | Documented process for disputing AR charges with a defined resolution timeline                      |
| Auto-renewal protection    | Minimum 60-day written notice required before automatic contract renewal                            |
| Vendor continuity risk     | Evidence of operation in substantially the same form through 2030                                                                                                                                                                       |

**Assessment questions**: What contractual commitments exist for vendor support response times and escalation? Is the vendor profitable or funded beyond 2028? Financial services domain customers and experience?

---

### 11. Pricing scorecard

| Requirement                | Detail                                                                             |
| -------------------------- | ---------------------------------------------------------------------------------- |
| All-in cost at 500 agents  | Total monthly cost modelled: seats + required add-ons                              |
| Cost predictability        | 12-month cost can be modelled with reasonable confidence                           |
| Add-on gating transparency | Required features (QA, WFM, Advanced AI) documented as included or separately billed |
| Volume discount terms      | Enterprise pricing at projected 2027–2030 contact volumes available on request    |

---

**Last Updated**: 2026-09-22 (Comparison Matrix replaced with the weighted scorecard result, Recommendation written, Pricing Assessment updated with real Plain and Pylon quotes and the five-year model, Implementation Plan rewritten from a Zendesk-renewal plan to the four-track Plain migration, Success Metrics and Open Questions restated, April 2026 candidate tables marked as superseded baseline)
**Owner**: Charlie Wildish
**Status**: Recommendation made. Plain, pending the three conditions named in the Recommendation
