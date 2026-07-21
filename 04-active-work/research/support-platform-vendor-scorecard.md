# Support Platform Decision — Vendor Scorecard

**Status**: Template — scores to be filled in during Q3 2026 POC and RFI (see `vendor-poc-scope.md`)
**Owner**: Charlie Wildish
**Related**: `support-platform-vendor-requirements.md` (defines the requirements this scorecard scores, one-to-one) · `zendesk-platform-decision-rfc.md` (decision context and options) · `vendor-poc-scope.md` (POC test flows that produce gate pass/fail and several requirement scores)

Purpose: turn the RFC's qualitative comparison into a weighted, numeric instrument that produces a defensible total per vendor for the Q4 2026 leadership decision. Fill in scores as POC results and RFI responses land; do not estimate scores from vendor marketing material alone — each score needs one line of evidence.

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

---

## Category weights

Weighted by how directly each category maps to a gap the RFC names as a decision driver (AI workflow execution, Platform merchant data, B2C readiness, pricing, vendor trust) versus categories that are lower-risk or further out on the roadmap.

| Tier | Weight | Categories |
|---|---|---|
| **High** | 14% each (70%) | 3. Routing & field logic · 4. Agent workspace · 5. Data and permissions · 10. Vendor reliability and operational trust · 11. Pricing |
| **Medium** | 7% each (21%) | 1. Multi-channel entry points · 7. Integrations · 8. Analytics and data extract |
| **Low** | 3% each (9%) | 2. AI triage and classification · 6. Customer-facing experience · 9. Environment and configuration deployment |

Rationale: routing, agent workspace, data/permissions, pricing and vendor trust carry the highest switching/renewal risk. Routing joins the High tier because presence-aware cross-region ("follow-the-sun") routing is the largest capability gap in the current Zendesk setup and a hard dependency for the EOY 2026 operating model. Integrations and analytics are core to today's operation but largely proven or in delivery. AI triage, customer-facing UX and environment tooling are lower risk: either already working via existing AI tooling or not yet load-bearing.

If Legal/Compliance input (Consumer Duty, Open Question 3) raises B2C readiness to a harder blocker, move Multi-channel entry points and Customer-facing experience into the High tier and rebalance.

---

## 1. Multi-channel entry points — weight 7%

| # | Requirement | Zendesk | Intercom | Plain | Pylon | Evidence |
|---|---|---|---|---|---|---|
| 1.1 | Email ingestion | | | | | |
| 1.2 | Email user enrichment (auto-match to org) | | | | | |
| 1.3 | Domain mapping | | | | | |
| 1.4 | AI Agent escalation path (Fin handoff w/ context) | | | | | |
| 1.5 | Live chat with human agent (B2B) | | | | | |
| 1.6 | Instant messaging channels (Slack/Teams, 2028–29) | | | | | |
| 1.7 | Phone channel (B2C IVR + routing) | | | | | |
| 1.8 | Mobile app chat (B2C, 2027) | | | | | |
| 1.9 | Internal ticket submission (Account teams) | | | | | |
| 1.10 | Multi-environment support (identify sandbox vs prod user/business) | | | | | |
| 1.11 | Region / contracting-entity enrichment (write routing attribute via API) | | | | | |
| | **Category score (avg)** | | | | | |

---

## 2. AI triage and classification — weight 3%

| # | Requirement | Zendesk | Intercom | Plain | Pylon | Evidence |
|---|---|---|---|---|---|---|
| 2.1 | Auto-classification on escalation | | | | | |
| 2.2 | AI agent handoff with context | | | | | |
| 2.3 | Pluggable external AI layer (Agent Consultant) | | | | | |
| | **Category score (avg)** | | | | | |

---

## 3. Routing & field logic — weight 14%

| # | Requirement | Zendesk | Intercom | Plain | Pylon | Evidence |
|---|---|---|---|---|---|---|
| 3.1 | Support plan / tier model (P0–P3) | | | | | |
| 3.2 | Skill-based routing | | | | | |
| 3.3 | SLA per tier and taxonomy value | | | | | |
| 3.4 | Customisable ticket and customer fields | | | | | |
| 3.5 | Flexible tagging / field system | | | | | |
| 3.6 | Flexible routing system (branching + fallbacks on any attribute) | | | | | |
| 3.7 | Presence-aware / follow-the-sun routing (real-time agent presence) | | | | | |
| 3.8 | Business-hours schedules per site/timezone (in/out-of-hours, hold queues) | | | | | |
| 3.9 | Geographic / entity-based routing (region → site/team) | | | | | |
| 3.10 | Queue-view scoping by attribute (prevent cherry-picking / segregation) | | | | | |
| 3.11 | Push and pull queue models (both supported; view lock at shift end) | | | | | |
| 3.12 | Capacity controls and handoff mode (concurrent caps, block near logoff) | | | | | |
| 3.13 | Conditional routing on computed thresholds (rolling-metric caps) | | | | | |
| 3.14 | Automated ownership release on SLA-breach risk (predictive reassignment) | | | | | |
| | **Category score (avg)** | | | | | |

---

## 4. Agent workspace — weight 14%

| # | Requirement | Zendesk | Intercom | Plain | Pylon | Evidence |
|---|---|---|---|---|---|---|
| 4.1 | Custom app framework (SDK/API, not marketplace-only) | | | | | |
| 4.2 | App capability scope (read + write + external API) | | | | | |
| 4.3 | App deployment/versioning without vendor involvement | | | | | |
| 4.4 | Live customer data panel (own sources) | | | | | |
| 4.5 | Internal escalation (Jira, custom API, read/write) | | | | | |
| 4.6 | Agent-triggered workflow execution | | | | | |
| 4.7 | Internal collaborator access (no full agent seat) | | | | | |
| | **Category score (avg)** | | | | | |

---

## 5. Data and permissions — weight 14%

| # | Requirement | Zendesk | Intercom | Plain | Pylon | Evidence |
|---|---|---|---|---|---|---|
| 5.1 | B2B/B2C data wall (BPO isolation) | | | | | |
| 5.2 | Role-based access control | | | | | |
| 5.3 | 500-agent scale | | | | | |
| 5.4 | Flexible data model (custom objects, no hardcoded schema) | | | | | |
| | **Category score (avg)** | | | | | |

---

## 6. Customer-facing experience — weight 3%

| # | Requirement | Zendesk | Intercom | Plain | Pylon | Evidence |
|---|---|---|---|---|---|---|
| 6.1 | Customer ticket portal | | | | | |
| 6.2 | AI chat history visibility | | | | | |
| 6.3 | Account team thread visibility/reply | | | | | |
| | **Category score (avg)** | | | | | |

---

## 7. Integrations (must-have) — weight 7%

| # | Requirement | Zendesk | Intercom | Plain | Pylon | Evidence |
|---|---|---|---|---|---|---|
| 7.1 | Fin (Intercom) escalation with context | | | | | |
| 7.2 | Jira bi-directional | | | | | |
| 7.3 | Salesforce sync | | | | | |
| 7.4 | Knowledge source sync (URL/GitHub, automated) | | | | | |
| 7.5 | Custom API access to internal systems | | | | | |
| | **Category score (avg)** | | | | | |

---

## 8. Analytics and data extract — weight 7%

| # | Requirement | Zendesk | Intercom | Plain | Pylon | Evidence |
|---|---|---|---|---|---|---|
| 8.1 | Full API export of ticket data (Reflex pipeline) | | | | | |
| 8.2 | Taxonomy-level reporting | | | | | |
| 8.3 | SLA breach alerting (configurable per tier) | | | | | |
| 8.4 | AHT / agent task time measurement | | | | | |
| | **Category score (avg)** | | | | | |

---

## 9. Environment and configuration deployment — weight 3%

| # | Requirement | Zendesk | Intercom | Plain | Pylon | Evidence |
|---|---|---|---|---|---|---|
| 9.1 | Sandbox/test environment mirroring production | | | | | |
| 9.2 | Configuration promotion path (test → prod) | | | | | |
| | **Category score (avg)** | | | | | |

---

## 10. Vendor reliability and operational trust — weight 14%

| # | Requirement | Zendesk | Intercom | Plain | Pylon | Evidence |
|---|---|---|---|---|---|---|
| 10.1 | Uptime SLA (core ticketing) | | | | | |
| 10.2 | Enterprise support SLA (human response, P1/P2) | | | | | |
| 10.3 | Named account team / escalation chain | | | | | |
| 10.4 | Billing dispute resolution process | | | | | |
| 10.5 | Auto-renewal protection (60-day notice) | | | | | |
| 10.6 | Vendor continuity risk (viable through 2030) | | | | | |
| | **Category score (avg)** | | | | | |

---

## 11. Pricing — weight 14%

| # | Requirement | Zendesk | Intercom | Plain | Pylon | Evidence |
|---|---|---|---|---|---|---|
| 11.1 | All-in cost at 500 agents (seats + required add-ons) | | | | | |
| 11.2 | Cost predictability (12-month model confidence) | | | | | |
| 11.3 | Add-on gating transparency (QA/WFM/Advanced AI) | | | | | |
| 11.4 | Volume discount terms at 2027–2030 projected contact volume | | | | | |
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
| 1. Multi-channel entry points | 7% | | | | |
| 2. AI triage and classification | 3% | | | | |
| 3. Routing & field logic | 14% | | | | |
| 4. Agent workspace | 14% | | | | |
| 5. Data and permissions | 14% | | | | |
| 6. Customer-facing experience | 3% | | | | |
| 7. Integrations | 7% | | | | |
| 8. Analytics and data extract | 7% | | | | |
| 9. Environment and configuration | 3% | | | | |
| 10. Vendor reliability and trust | 14% | | | | |
| 11. Pricing | 14% | | | | |
| **Weighted total (/3.0)** | 100% | | | | |
| **Gate status** | — | | | | |

Feed this table into the RFC's Comparison Matrix and Recommendation section once populated.

---

**Last updated**: 2026-07-17
**Owner**: Charlie Wildish
