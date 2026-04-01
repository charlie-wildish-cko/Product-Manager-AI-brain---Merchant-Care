---
confluence_space_key: MTC
confluence_parent_page_id: 8041431176
title: "PRD: Reflex (support contact reasons analytics)"
---

**Author:** Charlie Wildish
**Date:** 2026-04-01
**Stage:** Build
**Status:** Draft
**Last Updated:** 2026-04-01
**Stakeholders:** VP of Product, Director of Operations, Director of Operations Excellence, Engineering Manager, Product Data Scientist

| Field                      | Value                                                                                                                                                                                                            |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2026 deliverable** | Reflex                                                                                                                                                                                                           |
| **Strategic goal**   | Reduce contact rate                                                                                                                                                                                              |
| **Flywheel domain**  | Insight & Prevention                                                                                                                                                                                             |
| **Strategic lever**  | Contact reduction                                                                                                                                                                                                |
| **How it fits**      | Reflex attributes support contacts to products, surfaces ranked root cause drivers to Product teams, and tracks whether fixes reduce volume — closing the loop between contact data and product prioritisation. |

---

## Executive Summary

Checkout.com handles ~40k support contacts every year today. The issues driving the majority of that volume — failed payments, refund errors, login problems, settlement queries — recur quarter after quarter because the Product teams responsible for those areas have no systematic view of the contact data, no accountability for the volume they generate, and no mechanism to confirm that a fix reduced it. 

Reflex is the Insight & Prevention engine that closes this loop: it ingests Zendesk and Fin conversation data, uses LLM analysis to extract root causes, aggregates them into themes mapped to Product teams, and surfaces them through a self-serve query interface and regular reporting cadence. By 2026 Q4 it will automatically create Jira issues for the top contact drivers and track whether product fixes reduce volume. At $40 per human-handled contact, eliminating a recurring issue category compounds across every future transaction. 

End goal is to implement standing quarterly review with Product team leads and introduce Reflex to pillar owners at the start of Q2 — without that sponsorship, the insights will be generated but not acted on.

---

## Problem Space

**Problem statement:** The same product issues drive support contacts quarter after quarter because no system attributes contacts to root causes, surfaces them to the responsible Product team, or confirms that a shipped fix reduced volume.

We cannot scale with this support debt over the next few years, where we expect to handle 1-2m contacts per year.

**Who is affected:** Care Product team (Charlie), Product Managers across all pillars, Operations and Analytics teams, and ultimately every merchant whose recurring issue goes unfixed.

**Evidence:**

- 23,481 support contacts in the last 6 months. Top drivers: Refunds (4,114), Transaction status (3,679), Login & Access (2,228), Inquiries (1,802), Account changes (1,733), Card Payouts (1,707), Settlements (858). These are recurring, predictable categories — not one-off incidents.
- Payments (IN) alone accounts for 42.8% of all contacts (10,049). Within that, Refunds and Transaction status are 77% of the category — known, solvable problems that reappear because no product team is accountable for them.
- Account Management & Access (16.9%, 3,961 contacts) is the second largest category; Login & Access alone accounts for 2,228 contacts, the majority of which involve resolvable friction in the Dashboard authentication flow.

**Why now:** Q1 POC is complete — per-ticket summaries are in BigQuery and the data pipeline is stable. The foundation exists. Delaying Q2 theme aggregation means another quarter where the top 10 contact drivers are visible in raw data but not surfaced to anyone who can act. At 23,500 contacts per 6 months and $40/contact, the cost of inaction is approximately $940,000 in support costs per half-year, a material portion of which is attributable to issues a product fix could prevent.

---

## Goals and Success Metrics

**Business goals:**

- Reduce contact rate by attributing volume to products and driving product team accountability for fixes
- Create a compounding reduction in support costs as product fixes eliminate recurring contact categories
- Establish a quarterly cadence where Product teams receive, act on, and report back on Reflex-surfaced insights

**User goals:**

- Care Product, Ops & Ops Excellence teams: understand which products are generating the most contact volume and surface that data to the right Product team without manual analysis
- Product Managers: see the contact drivers attributable to their product area in a self-serve interface, with volume, cost, and trend data
- Care Analytics teams: access to structured contact trend data, VoC view, and reporting without relying on ad-hoc data pulls

**Non-goals:**

- Autonomous deployment of product fixes (Reflex generates action plan recommendations and Jira issues; humans ship)
- B2C consumer taxonomy (2027 scope)
- Real-time alerting below 24-hour SLA (spike detection is daily cadence)
- Content gap identification in this PRD scope (TBC if in Reflex or Agent Consultant).

**Success metrics:**

> Every baseline must have a real value or `TBC — establish by [date]`. The Q1 POC is live; attribution rate and adoption baselines need to be established once Phase 2 ships.

| Metric                                                              | Why it matters                                                                                            | Baseline                                                                                                                                              | Target                                                                          | Source                                     |
| ------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------ |
| % contact volume reduction post-fix                                 | North star — measures whether Reflex actually reduces contact rate, not just whether it produces reports | TBC — establish by end of Q2 2026 once attribution model live; target: measurable reduction in at least 2 of the top 10 driver categories by Q4 2026 | Measurable YoY reduction in contact rate for Reflex-identified issue categories | BQ enrichment table + contact volume delta |
| % of top 10 contact drivers with a committed or delivered fix       | Leading indicator — measures Product team uptake, not just insight generation                            | 0% (no current mechanism)                                                                                                                             | ≥50% of top 10 drivers with committed fix by Q4 2026                           | Quarterly review with VP Product           |
| # PMs actively querying Reflex per quarter                          | Adoption — if PMs aren't using it, it won't reduce contacts                                              | 0 (query interface not yet live)                                                                                                                      | ≥5 PMs per quarter by end of Q3 2026                                           | Query interface usage logs                 |
| Data attribution rate (% of tickets mapped to a product/issue type) | Health — if tickets aren't attributed, the ranked driver list is incomplete                              | TBC — establish by end of Q1 2026 from POC data (Data Scientist to confirm)                                                                          | ≥95%                                                                           | BQ enrichment table audit                  |
| Merchant CSAT                                                       | Guardrail — must not decline as product fixes ship                                                       | TBC — confirm with Data Scientist                                                                                                                    | Must not decline QoQ                                                            | Zendesk reporting                          |

---

## Customer Segments & Needs

**Primary users (internal):**

- **Care Product team:** Needs a systematic, automated view of contact root causes mapped to Product teams. Today this is a manual, periodic exercise. Reflex makes it continuous and self-serve.
- **Product Managers (all pillars):** Need contact-to-product attribution to prioritise fixes. Today they have no systematic access to support data. Reflex gives them a product team view showing the contact drivers attributable to their area, with volume, cost, and trend.
- **Operations and Analytics teams:** Need structured contact trend data for reporting and planning. Reflex provides the weekly digest and VoC view (merged support + NPS) once Q3 ships.
- **Content/Knowledge team:** Uses contact theme data and the VoC view to prioritise knowledge article and help centre content. Should be an explicit user of the Insights Query Interface with access to theme clusters and content gap indicators.

**User stories:**

- As a Care PM, I want to see the top 10 contact drivers mapped to product teams so that I can run a quarterly prioritisation review without manually querying BigQuery.
- As a Product Manager, I want a self-serve view of contact drivers attributable to my products so that I can include support volume in my prioritisation decisions without relying on Care to generate a report.
- As a Director of Operations, I want a weekly digest of the top contact themes and any volume spikes so that I can identify emerging issues before they become operational problems.
- As a Product Data Scientist, I want the contact attribution model to be auditable and versioned so that I can validate accuracy and explain changes in the ranked driver list to stakeholders.

---

## Proposed Solution & Scope

**Solution overview:** Reflex is a five-component system built on top of BigQuery. The AI engine ("the whale") runs LLM enrichment on raw ticket data to produce per-ticket root cause summaries, aggregate them into theme clusters, and map those clusters to Product teams via the Product Catalogue. The Insights Query Interface makes that output self-serve. Spike detection and NPS correlation (Q3) broaden the signal. Jira integration (Q4 TBC) closes the governance loop by auto-creating Product backlog issues from the top ranked drivers.

**In scope — 2026:**

- Phase 2 (Q2): Theme cluster aggregation, Product team mapping, Insights Query Interface, quarterly reporting cadence
- Phase 3 (Q3): NPS data merge (VoC view), contact spike detection, fix implementation measurement, weekly digest
- Phase 4 (Q4 TBC): Jira integration — automated quarterly Jira issue creation per product pillar
- TBC: Reflex MCP — programmatic read endpoints for query interface and other internal teams

**Out of scope:**

- Autonomous deployment of code fixes or PRs to production
- B2C consumer ticket taxonomy and analysis (2027)
- Real-time push notifications (spike detection is daily cadence)
- Fin conversation content ingestion is confirmed available (not in scope for this PRD to specify the mechanism — engineering to confirm data pipeline)

---

## Requirements

**Requirements by domain:**

| Domain                          | Requirement IDs                      | Purpose                                                          |
| ------------------------------- | ------------------------------------ | ---------------------------------------------------------------- |
| **Product / Platform**    | FR-0, FR-1, FR-2, FR-3, NFR-1, NFR-2 | Data pipeline, AI enrichment, theme aggregation, product mapping |
| **Analytics & Reporting** | FR-4, FR-5, FR-6, FR-7, NFR-3        | Insights Query Interface, dashboards, weekly digest, VoC view    |
| **Care Ops / CX**         | FR-8, NFR-4                          | Spike alerts, operational visibility                             |
| **Engineering**           | FR-9                                 | MCP read endpoints (TBC)                                         |

### Functional requirements

| ID             | Priority     | Requirement                                                                                                                                                                                                                  | Acceptance Criteria                                                                                                                                                     | Domain/s              |
| -------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| **FR-0** | **P0** | **Instrumentation events defined in the Instrumentation section must be implemented, validated in staging, and confirmed firing before Phase 2 go-live.**                                                              | All listed events fire correctly in staging; validated by Data Scientist before Phase 2 entry.                                                                          | Product / Platform    |
| FR-1           | P0           | Theme cluster aggregation: the AI engine groups per-ticket root cause summaries into recurring theme clusters by product_area, root_cause_category, and issue_type                                                           | Theme clusters are present in BQ enrichment table; clusters are interpretable by a non-technical reviewer; top 20 themes are rankable by volume and cost                | Product / Platform    |
| FR-2           | P0           | Product team mapping: each theme cluster is mapped to one or more Product teams using the Product Catalogue (product → pillar → team)                                                                                      | ≥95% of theme clusters have a mapped Product team; unmapped clusters are flagged for manual review                                                                     | Product / Platform    |
| FR-3           | P0           | Quarterly reporting: top 10 contact drivers are produced as a structured report and shared with VP Product and Director of Operations each quarter                                                                           | Report exists; VP Product and Director of Operations confirm receipt by end of Q2 2026                                                                                  | Analytics & Reporting |
| FR-4           | P0           | Insights Query Interface: a self-serve interface allows Product Managers and Care PM to view contact drivers filtered by product, segment, and territory without BQ access                                                   | At least one PM outside the Care team can self-serve a contact driver view without support from Charlie or the Data Scientist                                           | Analytics & Reporting |
| FR-5           | P1           | Product team view: the query interface includes a per-team view showing top contact drivers scoped to that team's product area, with quarter-on-quarter trend                                                                | Product team views are available; at least one PM confirms the view matches their product area                                                                          | Analytics & Reporting |
| FR-6           | P1           | NPS data merge (Q3): Merchant NPS scores from Airtable are joined to Zendesk organisations via client ID and surfaced in a VoC view combining contact themes with NPS movement                                               | VoC view is live; correlation between contact theme clusters and NPS movement is visible in the interface                                                               | Analytics & Reporting |
| FR-7           | P1           | Fix implementation measurement (Q3): when a Product team ships a fix for a Reflex-identified contact driver, the system tracks whether contact volume for that driver declines in the subsequent period                      | Attribution model is live; at least one shipped fix has volume delta measured and reported                                                                              | Analytics & Reporting |
| FR-8           | P1           | Spike detection (Q3): the system monitors inbound contact volume by issue type and triggers an alert when volume exceeds a defined threshold for a specific theme or cluster                                                 | Spike detection runs daily; at least one test spike is detected and alerted correctly in staging before go-live                                                         | Care Ops / CX         |
| FR-9           | P2           | Reflex MCP (TBC): programmatic read endpoints (`GET /top-contact-drivers`, `GET /issue-detail/:issue_type`, `GET /product-insights/:product_id`, `GET /spike-alerts`) are live and accessible to internal teams      | MCP endpoints return correct data; Insights Query Interface can query via MCP; at least one other internal team (e.g. Agent Consultant) confirms the endpoint is usable | Engineering           |
| FR-10          | P1 (Q4 TBC)  | Jira integration: top 5–10 contact drivers per product pillar are auto-created as Jira issues quarterly, pre-populated with volume, cost, trend, example tickets, and recommended Product team; human review before publish | Quarterly Jira issues are created; at least one Product team lead confirms the issue format is actionable; human review step is enforced                                | Product / Platform    |

### Non-functional requirements

| ID    | Priority | Requirement                                                                                                                                               | Acceptance Criteria                                                                                            | Domain/s              |
| ----- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | --------------------- |
| NFR-1 | P0       | Data attribution rate: ≥95% of closed Zendesk tickets in the enrichment table have a mapped product_area and issue_type                                  | Daily audit query in BQ shows ≥95% attribution rate; gaps are flagged automatically                           | Product / Platform    |
| NFR-2 | P0       | Daily pipeline SLA: the AI enrichment pipeline runs and completes within 24 hours of ticket close                                                         | Pipeline run logs confirm daily completion; alerting fires if a run fails or exceeds 24-hour window            | Product / Platform    |
| NFR-3 | P1       | Model versioning: LLM model versions used for summarisation and aggregation are tracked and logged in Bedrock or equivalent; prompt changes are versioned | Model version is queryable from enrichment table metadata; Data Scientist can audit changes to model or prompt | Analytics & Reporting |
| NFR-4 | P1       | Spike alert latency: spike detection alerts are delivered within 24 hours of threshold breach                                                             | Test breach triggers alert within 24 hours in staging                                                          | Care Ops / CX         |

---

## Design and User Experience

**Design & UX:** Tool TBD (Looker, Retool, or equivalent). 

Core requirements: filterable contact driver dashboard; per Product or Product team views; self-serve query capability without BQ access; shareable insight links.

---

## Instrumentation and Monitoring

**Key events to instrument:**

> Note: event names below are suggested. Owner for validation: Data Scientist + Engineering, before Phase 2 go-live (end of Q2 2026).

| Event                              | Properties                                                              | Why                                                                             |
| ---------------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `reflex_summary_generated`       | ticket_id, model_version, root_cause_category, product_area, issue_type | Confirms per-ticket enrichment is running; enables attribution rate calculation |
| `reflex_theme_cluster_created`   | cluster_id, product_area, issue_type, ticket_count, cost_estimate       | Tracks aggregation output; enables ranked driver reporting                      |
| `reflex_insight_queried`         | user_id, query_type, product_team_filter, timestamp                     | Adoption tracking for Insights Query Interface                                  |
| `reflex_jira_issue_created` (Q4) | cluster_id, product_team, volume, cost_estimate, review_status          | Governance tracking for Jira integration                                        |
| `reflex_fix_measured` (Q3)       | cluster_id, fix_shipped_date, volume_before, volume_after, delta_pct    | Attribution model — north star metric input                                    |

**Internal dashboards and monitoring:**

- **Contact driver dashboard**: Top contact drivers by volume and cost, filterable by product, segment, territory. Owner: Data Scientist. Updated: daily.
- **Attribution rate monitor**: Daily audit of % tickets with mapped product_area and issue_type. Alerts if drops below 95%. Owner: Data Scientist.
- **Fix attribution tracking view** (Q3): Contact volume delta pre/post fix for each Reflex-identified driver where a fix has been shipped. Owner: Care PM.

**Validation approach:**

- Run pipeline against a known set of closed tickets before Phase 2 go-live; Data Scientist confirms ≥95% attribution on the validation set.
- Silent failure detection: daily row count alert on BQ enrichment table — if enriched ticket count drops >20% below 7-day average, alert fires to Data Scientist and Care PM. Owner: Data Scientist. Cadence: daily.

---

## Risks, Assumptions, and Dependencies

| Type       | Description                                                                                                     | Likelihood | Impact | Mitigation / Validation                                                                                                                | Owner                |
| ---------- | --------------------------------------------------------------------------------------------------------------- | ---------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| Risk       | Product teams don't act on surfaced insights — Reflex generates reports that sit unread                        | Medium     | High   | VP Product buy-in required before Q2 launch; at least one PM should be identified as a design partner before the query interface ships | Care PM + VP Product |
| Assumption | Product Catalogue (Airtable) mapping of product → pillar → team is accurate and maintained                    | Medium     | High   | Validate Airtable currency with Analytics team before Phase 2 build; agree owner for ongoing maintenance                               | Analytics team       |
| Dependency | MCP hosting model not yet decided — standalone service or shared with Agent Consultant                         | Low        | Medium | Engineering to decide hosting model before TBC MCP phase starts; does not block Phases 2–4                                            | Engineering Manager  |
| Assumption | LLM summarisation quality is sufficient for production-grade attribution at ≥95%                               | Medium     | High   | Q1 POC provides baseline — Data Scientist to run quality assurance review of a sample before Phase 2 aggregation build                | Data Scientist       |
| Dependency | Jira project/board mapping per product pillar must be agreed with Product team leads before Q4 Jira integration | Low        | Medium | Confirm pillar → Jira project mapping by end of Q3 2026                                                                               | Care PM + VP Product |

---

## Rollout Plan

**Rollout approach:** Phased by capability. Each phase has a clear "done when" condition that gates progression. Phases 2–4 build on each other sequentially; Reflex MCP is independent and can be sequenced around engineering capacity.

### Phase 1 (complete): Q1 2026 — Data Foundation + Per-Ticket Summaries

Done. Per-ticket LLM root cause summaries live in BigQuery. Basic contact driver dashboard shipped.

### Phase 2: Q2 2026 — Theme Aggregation + Product Mapping + Query Interface

**Purpose:** Aggregate per-ticket summaries into actionable theme clusters; make insights self-serve for Product teams.

**Entry criteria:**

- Technical: Q1 BQ enrichment table stable and running daily; Data Scientist confirms ≥95% attribution rate on Q1 output
- Operational: Insights Query Interface tool confirmed; at least one Product team PM identified as design partner
- Instrumentation: FR-0 events validated in staging

**Success criteria (done when):**

- Aggregated theme clusters live in BQ
- Top 10 contact drivers quantified and shared with VP Product and Director of Operations
- At least one Product team PM using Reflex output for prioritisation

**Timeline:** Q2 2026

### Phase 3: Q3 2026 — NPS Data, Spike Detection, Fix Measurement

**Purpose:** Broaden the signal; automate the governance loop; begin measuring whether product fixes reduce contact volume.

**Entry criteria:**

- Technical: Phase 2 query interface live and in use; NPS Airtable join via client ID confirmed with Analytics team
- Operational: Weekly digest format agreed with Director of Operations

**Success criteria (done when):**

- VoC dashboard live (support + NPS merged view)
- Spike detection running and tested
- Product teams receiving weekly digest
- Attribution model tracking contact rate reduction from at least one Reflex-identified fix

**Timeline:** Q3 2026

### Phase 4: Q4 2026 — Jira Integration (TBC)

**Purpose:** Automate the quarterly Product fix backlog from Reflex.

**Why TBC:** This phase is dependent on Phase 3 attribution model stability. If the fix measurement model is not reliable by end of Q3, auto-creating Jira issues from it will create noise rather than value. Decision point: end of Q3 2026 — Care PM and VP Product confirm go/no-go based on Phase 3 stability.

**Entry criteria:**

- Technical: Phase 3 theme clustering and attribution model stable; ≥95% attribution rate sustained for one full quarter
- Operational: Jira project/board mapping confirmed for each product pillar; human review process agreed with VP Product

**Success criteria (done when):**

- Quarterly Jira issues auto-created and reviewed by Product team leads
- Product team contact reduction targets tracked against Reflex-originated fixes

**Timeline:** Q4 2026 — go/no-go decision at end of Q3

### TBC: Reflex MCP

**Purpose:** Make Reflex programmatically queryable by AI tools and internal teams (Agent Consultant, query interface backend).

**Entry criteria:**

- Technical: Phase 2 query interface live; hosting model decided
- Operational: At least one downstream consumer (Agent Consultant or query interface) ready to integrate

**Success criteria (done when):**

- MCP endpoints live and returning correct data
- Query interface connected via MCP
- At least one other internal team queries Reflex via MCP

**Definition of Done (Phase 4 / end of 2026):**

- Technical: All P0 and P1 FRs delivered; ≥95% attribution rate sustained; daily pipeline SLA met
- Operational: VP Product and Director of Operations receiving quarterly Reflex report; at least 5 PMs using query interface; weekly digest running
- Business: At least one contact driver with a shipped product fix and measured volume delta

**Product dependencies:**

- Product Catalogue (Airtable) maintained and accurate — Analytics team
- Zendesk ticket data in BigQuery — already live
- Fin conversation data pipeline — Engineering to confirm mechanism and timeline
- NPS Airtable source — Analytics team to confirm join via client ID before Phase 3

**Go-to-market:**

- Internal comms: VP Product introduces Reflex to Product team leads at start of Q2; quarterly review meeting cadence established with a named Product lead per pillar
- Accountability: VP Product owns the quarterly review; Product team leads are expected to respond to surfaced drivers within the same quarter. Teams that consistently don't act will be flagged to VP Product for follow-up — this is the accountability mechanism that makes Reflex a prevention engine, not a reporting tool.
- Enablement: Data Scientist publishes guide to reading and querying the interface; Care PM delivers walkthrough session with Product team leads and Content/Knowledge team
- Reporting: Quarterly Reflex report format agreed and templated before first send; weekly digest format agreed with Director of Operations before Q3 go-live
- Operational briefing: Before Q3 weekly digest launch, Director of Operations briefs team leads on how to read spike alerts and what action is expected when a spike fires — escalation path is: spike alert fires to Operations team lead and Care PM; Care PM confirms root cause with Data Scientist; Director of Operations decides whether to escalate to Product or manage within Ops. Agents do not receive spike alerts directly; team leads relay context on known recurring drivers in team briefings.

---

## Appendix

**Strategy and research:**

- Reflex product reference:`01-knowledge-base/products/reflex.md`
- Phased build sequence:`04-active-work/reflex-phased-plan.md`
- Care flywheel model:`01-knowledge-base/strategy/care-product-model.md`
- Care capability model (year-by-year to 2030):`01-knowledge-base/strategy/care-capability-model.md`
- Contact volume data source:`01-knowledge-base/metrics/support_contacts_flat_table_2025_last_6m.csv`
- Support taxonomy:`01-knowledge-base/processes/support-taxonomy.md`

**Alternatives considered:**

- Manual quarterly analysis by Care PM: rejected — not scalable, not systematic, no attribution model
- Off-the-shelf support analytics tool: rejected — requires custom Product Catalogue mapping and LLM enrichment that generic tools don't provide; BQ foundation already exists
- Combine Reflex with Agent Consultant as one product: rejected — different users, different flywheel domains (Insight & Prevention vs Agent Experience); share data layer but separate build tracks
