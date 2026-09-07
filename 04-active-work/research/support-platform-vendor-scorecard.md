# Support Platform Decision — Vendor Scorecard

**Status**: Template — scores to be filled in during Q3 2026 POC and RFI (see `vendor-poc-scope.md`)
**Owner**: Charlie Wildish
**Related**: `support-platform-vendor-requirements.md` (defines the requirements this scorecard scores, one-to-one) · `zendesk-platform-decision-rfc.md` (decision context and options) · `vendor-poc-scope.md` (POC test flows that produce gate pass/fail and several requirement scores)

Purpose: turn the RFC's qualitative comparison into a weighted, numeric instrument that produces a defensible total per vendor for the Q4 2026 leadership decision. Fill in scores as POC results and RFI responses land; do not estimate scores from vendor marketing material alone — each score needs one line of evidence.

---

## Strategic framing

The hypothesis behind replacing Zendesk: a new platform enables faster velocity through flexible deployment, better connectivity that improves SLA and resolution, unconstrained integration with our own AI/agentic tooling, and room to onboard teams beyond Care. That hypothesis resolves into four evaluation pillars. Each pillar is a capability/architecture question this scorecard can score directly — not a business-outcome claim, which cannot be proven pre-production (see RFC Recommendation section on POC scope limits).

| Pillar | Hypothesis | Maps to (category.requirement) | Gap not yet in scorecard |
|---|---|---|---|
| **Agentic compatibility** | Flexible integration for AI Agents, supporting agentic workflows and avoiding vendor lock-in | 2.3 (pluggable external AI layer) · 4.2 (app read+write+external API) · 4.6 (agent-triggered workflow execution) | POC gate tests read/write only — no flow yet tests an app *executing* an external action (e.g. mock refund call), which is what "agentic" actually requires |
| **API-first** | Increased flexibility using APIs for deployment, configuration, integrations, content, and data to accelerate development and support agentic flows | 4.1 (custom app framework) · 4.3 (deploy without vendor involvement) · 7.5 (custom API access) · 8.1 (full API export) · 9.1–9.2 (environment/config deployment) | Requirements test app deployment and data export via API, but not config-as-code coverage for routing/SLA rules or content/knowledge — deployment velocity is narrower than the full claim |
| **Omnichannel** | OOTB channels: email, forms, phone, IM, and a Community platform (SMB/Consumer) | Category 1 in full, esp. 1.5–1.9 | Community platform is not a row in Category 1 — needs adding before this pillar can be scored end-to-end |
| **Unified Operations platform** | Capable of serving all Operations teams, not just Care, consolidating fragmented tooling into one agentic-powered system | 5.1 (data wall/isolation) · 5.4 (flexible data model, no hardcoded schema) · 11.1, 11.4 (pricing/volume discount at scale) | No requirement row tests a second, non-Care team's data model against the platform — Category 5 currently only tests B2B/B2C isolation within Care |

Score the mapped requirements as the primary evidence for each pillar. Where a gap is flagged, the scorecard total will understate that pillar until the corresponding requirement/POC flow is added — call this out explicitly in the RFC recommendation rather than letting a partial score stand in for the full hypothesis.

---

## How to score

**Step 1 — Gates.** Each vendor must pass all 5 gate flows defined in `vendor-poc-scope.md`, scored pass/fail in the Gates table below:

1. Fin escalation handoff with context
2. Tier-based routing with SLA clocks
3. Custom sidebar app, read/write
4. Jira bi-directional
5. Email-to-org matching

A failed gate disqualifies the vendor regardless of weighted score below — record the fail and stop scoring that vendor.

**Step 2 — Requirement scores.** For every requirement in the 11 categories below (each maps one-to-one to a requirement in `support-platform-vendor-requirements.md`), score each vendor 0–3:

| Score | Meaning |
|---|---|
| 0 | Not supported — no credible path |
| 1 | Possible via custom build or heavy configuration — meaningful cost, time, or risk |
| 2 | Supported via configuration or paid add-on |
| 3 | Native, out-of-the-box |

**Step 3 — Category score.** Average the requirement scores within a category (0–3).

**Step 4 — Weighted total.** Multiply each category score by its weight (below) and sum. Maximum possible total is 3.0. Enter results in the Summary table at the end.

Build is out of scope for this scorecard — see RFC Option 4 (not viable at current team capacity).

### Two scoring axes: Capability vs. Effort

A vendor question surfaced that not every requirement is truly binary — some ("supports Jira bi-directional?") have an obvious yes/no, but the real differentiator between two "yes" vendors is how much work it takes to stand up and run. The scorecard scores these as two separate axes rather than one blended number:

- **Capability (primary, all 60 requirements)** — the 0–3 Native/Config/Add-on/Custom-build/Not-supported score above. This is what feeds the weighted total. It's sourced from the RFI response and is comparable across every vendor and every requirement.
- **Effort — ease of use / setup time (secondary, POC-only)** — measured directly during the POC, not self-reported on the RFI. Concrete, not a rating: time to deploy (Flow 3: sidebar app in under 4 hours), click-count (Flow 4: Jira issue in under 3 clicks), extraction time (Flow 6: time to pull 20 tickets). Self-reported "ease of use" isn't used because it isn't verifiable or comparable across vendors — it's marketing-shaped, not evidence-shaped.

**These do not get averaged together.** Capability is the score that determines category and weighted totals. Effort is a tiebreaker: when two vendors score identically on Capability for a requirement, the POC's measured effort data decides which is preferred. Effort scores live in `vendor-poc-scope.md` alongside the gate/differentiator flows, not in the category tables below.

---

## Category weights

**Revised 2026-08-12.** Weights now reflect five named transformation drivers rather than pure switching/renewal risk: agentic compatibility, API-first, omnichannel, faster velocity via config-as-code, and a unified Operations platform (serving all Ops teams, not just Care).

| Category | Weight | Driver mapping |
|---|---|---|
| 4. Agent workspace | 16% | Agentic compatibility · API-first · Unified Operations platform — custom app framework, API access, single workspace for all Ops teams |
| 1. Multi-channel entry points | 13% | Omnichannel — OOTB channels including email, forms, phone, IM, Community |
| 5. Data and permissions | 13% | Unified Operations platform — flexible data model to serve non-Care teams · API-first |
| 2. AI triage and classification | 12% | Agentic compatibility — pluggable AI layer, avoiding vendor lock-in |
| 9. Environment and configuration deployment | 10% | Faster velocity via config-as-code deployment |
| 7. Integrations | 10% | Agentic compatibility · API-first — pluggable integrations, avoiding lock-in |
| 3. Routing & field logic | 10% | Unified Operations platform (cross-team routing); no longer the standalone top-tier gap it was under the switching-risk framing |
| 6. Customer-facing experience | 5% | Omnichannel (Community platform) — external-facing, not an internal velocity lever |
| 8. Analytics and data extract | 5% | API-first (partial) — not a standalone driver |
| 10. Vendor reliability and operational trust | 3% | Hygiene/gate, not a transformation driver |
| 11. Pricing | 3% | Commercial gate, not a transformation driver |

Total: 100%.

**Prior weighting (used through 2026-08-11, kept for reference)**: High 14% each — Routing, Agent workspace, Data/permissions, Vendor reliability, Pricing (70%); Medium 7% each — Multi-channel, Integrations, Analytics (21%); Low 3% each — AI triage, Customer-facing, Environment/config (9%). That framing weighted switching/renewal risk on the current operating model. The revision above weights readiness for the stated transformation drivers instead — Vendor reliability and Pricing drop to gating/hygiene status (3% each) since they aren't named drivers, while AI triage and Environment/config deployment rise sharply (3% → 12% and 3% → 10%) since they map directly to agentic compatibility and config-as-code velocity.

If Legal/Compliance input (Consumer Duty, Open Question 3) raises B2C readiness to a harder blocker, move Multi-channel entry points and Customer-facing experience weight up further and rebalance.

---

## 1. Multi-channel entry points — weight 13%

| # | Requirement | Zendesk | Intercom | Plain | Pylon | Evidence |
|---|---|---|---|---|---|---|
| 1.1 | Email ingestion (e.g. email reply threads onto the existing ticket, no duplicate) | | | | | |
| 1.2 | Email user enrichment (auto-match to org) (e.g. unrecognised sender still matched to org by domain) | | | | | |
| 1.3 | Domain mapping (e.g. `@checkout.com` auto-tags to the Checkout.com org record) | | | | | |
| 1.4 | AI Agent escalation path (Fin handoff w/ context) (e.g. agent sees full transcript + tier/intent Fin already applied) | | | | | |
| 1.5 | Live chat with human agent (B2B) (e.g. "Report a bug" click pre-fills an intake form before reaching an agent) | | | | | |
| 1.6 | Instant messaging channels (Slack/Teams, 2028–29) (e.g. a Slack Connect message becomes a ticket) | | | | | |
| 1.7 | Phone channel (B2C IVR + routing) (e.g. IVR routes by tier and auto-creates a ticket with the call recording) | | | | | |
| 1.8 | Mobile app chat (B2C, 2027) (e.g. in-app chat shares the same ticket timeline as web chat) | | | | | |
| 1.9 | Internal ticket submission (Account teams) (e.g. AM raises a ticket on a merchant's behalf, no full seat needed) | | | | | |
| 1.10 | Multi-environment support (identify sandbox vs prod user/business) (e.g. sandbox-only dev login distinguished from prod merchant on same domain) | | | | | |
| 1.11 | Region / contracting-entity enrichment (write routing attribute via API) (e.g. contracting entity written to a field via API, drives regional routing) | | | | | |
| | **Category score (avg)** | | | | | |

---

## 2. AI triage and classification — weight 12%

| # | Requirement | Zendesk | Intercom | Plain | Pylon | Evidence |
|---|---|---|---|---|---|---|
| 2.1 | Auto-classification on escalation (e.g. a chargeback ticket auto-tags "Disputes > Chargebacks" before reaching a queue) | | | | | |
| 2.2 | AI agent handoff with context (e.g. Fin's classification lands as a structured field, not just transcript text) | | | | | |
| 2.3 | Pluggable external AI layer (Agent Consultant) (e.g. Agent Consultant writes to a ticket without the platform's native AI enabled) | | | | | |
| | **Category score (avg)** | | | | | |

---

## 3. Routing & field logic — weight 10%

| # | Requirement | Zendesk | Intercom | Plain | Pylon | Evidence |
|---|---|---|---|---|---|---|
| 3.1 | Support plan / tier model (P0–P3) (e.g. P0 Enterprise ticket to a dedicated 1-hour-SLA queue vs. P3 Standard's 24 hours) | | | | | |
| 3.2 | Skill-based routing (e.g. a "3DS authentication" ticket only reaches agents with that skill tag) | | | | | |
| 3.3 | SLA per tier and taxonomy value (e.g. P1 dispute gets a 4-hour SLA, P1 general enquiry gets 8, same tier) | | | | | |
| 3.4 | Customisable ticket and customer fields (e.g. "Platform ISV Parent" account field used as a routing condition) | | | | | |
| 3.5 | Flexible tagging / field system (e.g. case-type/issue-type tags filterable in reporting with no custom build) | | | | | |
| 3.6 | Flexible routing system (branching + fallbacks on any attribute) (e.g. overflow from Team A falls back to Team B at capacity) | | | | | |
| 3.7 | Presence-aware / follow-the-sun routing (real-time agent presence) (e.g. UK team logs off, tickets auto-shift to US night shift) | | | | | |
| 3.8 | Business-hours schedules per site/timezone (in/out-of-hours, hold queues) (e.g. a 2am ticket holds until the next region's shift starts) | | | | | |
| 3.9 | Geographic / entity-based routing (region → site/team) (e.g. EU-contracted merchant routes to the EU team) | | | | | |
| 3.10 | Queue-view scoping by attribute (prevent cherry-picking / segregation) (e.g. B2C-only agent can't see or pull B2B tickets) | | | | | |
| 3.11 | Push and pull queue models (both supported; view lock at shift end) (e.g. auto-push by capacity in-hours, locked pull view near shift end) | | | | | |
| 3.12 | Capacity controls and handoff mode (concurrent caps, block near logoff) (e.g. no new tickets route to an agent in the last 15 minutes of shift) | | | | | |
| 3.13 | Conditional routing on computed thresholds (rolling-metric caps) (e.g. refund tickets >20% of daily volume auto-redirect to a dedicated team) | | | | | |
| 3.14 | Automated ownership release on SLA-breach risk (predictive reassignment) (e.g. ticket reassigned before agent's shift end if it would breach overnight) | | | | | |
| | **Category score (avg)** | | | | | |

---

## 4. Agent workspace — weight 16%

| # | Requirement | Zendesk | Intercom | Plain | Pylon | Evidence |
|---|---|---|---|---|---|---|
| 4.1 | Custom app framework (SDK/API, not marketplace-only) (e.g. sidebar shows live internal data without storing it in the platform) | | | | | |
| 4.2 | App capability scope (read + write + external API) (e.g. app reads account ID, calls a fraud-check API, writes result to a field) | | | | | |
| 4.3 | App deployment/versioning without vendor involvement (e.g. engineering deploys an updated sidebar app from CI, no marketplace review) | | | | | |
| 4.4 | Live customer data panel (own sources) (e.g. agent sees live processing volume/settlement status pulled from our warehouse) | | | | | |
| 4.5 | Internal escalation (Jira, custom API, read/write) (e.g. one-click Jira bug creation; ticket status updates when Jira closes) | | | | | |
| 4.6 | Agent-triggered workflow execution (e.g. agent approves an action, platform fires a webhook that triggers it externally) | | | | | |
| 4.7 | Internal collaborator access (no full agent seat) (e.g. Knowledge Manager comments on a ticket without a full agent licence) | | | | | |
| | **Category score (avg)** | | | | | |

---

## 5. Data and permissions — weight 13%

| # | Requirement | Zendesk | Intercom | Plain | Pylon | Evidence |
|---|---|---|---|---|---|---|
| 5.1 | B2B/B2C data wall (BPO isolation) (e.g. B2C agent can't see or search any B2B ticket, even by ID) | | | | | |
| 5.2 | Role-based access control (e.g. team lead sees/reassigns the whole queue, agent only sees their own tickets) | | | | | |
| 5.3 | 500-agent scale (e.g. dashboard/search performance holds from 50 to 500 concurrent users) | | | | | |
| 5.4 | Flexible data model (custom objects, no hardcoded schema) (e.g. custom "Platform Parent Merchant" object with no vendor schema change) | | | | | |
| | **Category score (avg)** | | | | | |

---

## 6. Customer-facing experience — weight 5%

| # | Requirement | Zendesk | Intercom | Plain | Pylon | Evidence |
|---|---|---|---|---|---|---|
| 6.1 | Customer ticket portal (e.g. merchant logs in and sees open tickets, or same data via API for our own front-end) | | | | | |
| 6.2 | AI chat history visibility (e.g. earlier Fin conversation visible in the same ticket timeline, not a separate log) | | | | | |
| 6.3 | Account team thread visibility/reply (e.g. AM replies via email with an internal note not visible to the merchant) | | | | | |
| | **Category score (avg)** | | | | | |

---

## 7. Integrations (must-have) — weight 10%

| # | Requirement | Zendesk | Intercom | Plain | Pylon | Evidence |
|---|---|---|---|---|---|---|
| 7.1 | Fin (Intercom) escalation with context (e.g. escalation creates a ticket with transcript + metadata pre-attached) | | | | | |
| 7.2 | Jira bi-directional (e.g. Jira status change to "Done" auto-updates the linked ticket) | | | | | |
| 7.3 | Salesforce sync (e.g. ticket shows current SF case number and account owner with no manual lookup) | | | | | |
| 7.4 | Knowledge source sync (URL/GitHub, automated) (e.g. GitHub repo connected once, new articles re-sync after each merge) | | | | | |
| 7.5 | Custom API access to internal systems (e.g. workflow pulls live transaction volume from BigQuery into a ticket field) | | | | | |
| | **Category score (avg)** | | | | | |

---

## 8. Analytics and data extract — weight 5%

| # | Requirement | Zendesk | Intercom | Plain | Pylon | Evidence |
|---|---|---|---|---|---|---|
| 8.1 | Full API export of ticket data (Reflex pipeline) (e.g. all fields incl. custom fields/comments extractable daily via API) | | | | | |
| 8.2 | Taxonomy-level reporting (e.g. filter by "Case Type = Disputes AND Issue Type = Pre-Arbitration" with no custom build) | | | | | |
| 8.3 | SLA breach alerting (configurable per tier) (e.g. Slack alert 30 min before a P0 breach, and again on breach) | | | | | |
| 8.4 | AHT / agent task time measurement (e.g. avg handle time per agent per case type with no separate time-tracking app) | | | | | |
| | **Category score (avg)** | | | | | |

---

## 9. Environment and configuration deployment — weight 10%

| # | Requirement | Zendesk | Intercom | Plain | Pylon | Evidence |
|---|---|---|---|---|---|---|
| 9.1 | Sandbox/test environment mirroring production (e.g. test a routing change against realistic data before it hits a live ticket) | | | | | |
| 9.2 | Configuration promotion path (test → prod) (e.g. "promote to production" action moves an approved SLA policy live, no manual rebuild) | | | | | |
| 9.3 | Config as code (version-controlled, CI/CD-deployable configuration) (e.g. routing rule defined in YAML/Terraform, reviewed via PR, deployed via pipeline, with diff + rollback) | | | | | |
| | **Category score (avg)** | | | | | |

---

## 10. Vendor reliability and operational trust — weight 3%

| # | Requirement | Zendesk | Intercom | Plain | Pylon | Evidence |
|---|---|---|---|---|---|---|
| 10.1 | Uptime SLA (core ticketing) (e.g. contractual 99.9% with defined service credits on breach) | | | | | |
| 10.2 | Enterprise support SLA (human response, P1/P2) (e.g. guaranteed 1-hour human response on a P1, not a bot-first reply) | | | | | |
| 10.3 | Named account team / escalation chain (e.g. a named TAM, not a rotating support queue, as first point of contact) | | | | | |
| 10.4 | Billing dispute resolution process (e.g. documented process with a committed resolution timeframe, e.g. 30 days) | | | | | |
| 10.5 | Auto-renewal protection (60-day notice) (e.g. contract requires 60 days' notice before auto-renewal) | | | | | |
| 10.6 | Vendor continuity risk (viable through 2030) (e.g. evidence of profitability/funding runway supporting operation through 2030) | | | | | |
| | **Category score (avg)** | | | | | |

---

## 11. Pricing — weight 3%

| # | Requirement | Zendesk | Intercom | Plain | Pylon | Evidence |
|---|---|---|---|---|---|---|
| 11.1 | All-in cost at 500 agents (seats + required add-ons) (e.g. one quote covering seats + QA/WFM/Advanced AI needed to match today's functionality) | | | | | |
| 11.2 | Cost predictability (12-month model confidence) (e.g. next year's cost modellable in a narrow range from our volume forecast) | | | | | |
| 11.3 | Add-on gating transparency (QA/WFM/Advanced AI) (e.g. a comparison sheet states plainly what's in-seat vs. a separate SKU) | | | | | |
| 11.4 | Volume discount terms at 2027–2030 projected contact volume (e.g. discount tier applies automatically at agreed volume thresholds) | | | | | |
| | **Category score (avg)** | | | | | |

---

## Gates (pass/fail — disqualifying)

| Gate flow | Zendesk | Intercom | Plain | Pylon |
|---|---|---|---|---|
| Fin escalation handoff with context | | | | |
| Tier-based routing with SLA clocks | | | | |
| Custom sidebar app, read/write | | | | |
| Jira bi-directional | | | | |
| Email-to-org matching | | | | |

Any fail = disqualified. Record fail reason; do not proceed to weighted scoring for that vendor.

---

## Summary — weighted totals

| Category | Weight | Zendesk | Intercom | Plain | Pylon |
|---|---|---|---|---|---|
| 1. Multi-channel entry points | 13% | | | | |
| 2. AI triage and classification | 12% | | | | |
| 3. Routing & field logic | 10% | | | | |
| 4. Agent workspace | 16% | | | | |
| 5. Data and permissions | 13% | | | | |
| 6. Customer-facing experience | 5% | | | | |
| 7. Integrations | 10% | | | | |
| 8. Analytics and data extract | 5% | | | | |
| 9. Environment and configuration | 10% | | | | |
| 10. Vendor reliability and trust | 3% | | | | |
| 11. Pricing | 3% | | | | |
| **Weighted total (/3.0)** | 100% | | | | |
| **Gate status** | — | | | | |

Feed this table into the RFC's Comparison Matrix and Recommendation section once populated.

---

**Last updated**: 2026-08-12
**Owner**: Charlie Wildish
