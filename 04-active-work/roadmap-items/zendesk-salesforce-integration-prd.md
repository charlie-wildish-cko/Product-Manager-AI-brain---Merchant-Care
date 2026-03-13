# PRD: Zendesk–Salesforce Integration

**Author:** Charlie Wildish
**Date:** March 2026
**Approvers:** Director of Operations Excellence, Engineering Manager, Zendesk Admins
**Stage:** Discovery
**Status:** Draft
**Last Updated:** March 2026
**Stakeholders:** Care Operations, Operations Excellence, Zendesk Admins, Engineering, Data Engineering, Content Strategist


| Field                | Value                                                                                                                                                                                                           |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2026 deliverable** | Agent Productivity Tools (MCD-570)                                                                                                                                                                              |
| **Strategic goal**   | Reduce cost of support                                                                                                                                                                                          |
| **Flywheel domain**  | 4. Agent Experience                                                                                                                                                                                             |
| **How it fits**      | Removes manual Salesforce log-ins during active ticket handling and automates chaser messages to SF teams when cases stall, reducing agent time on escalation management and protecting Zendesk SLA compliance. |

---

## Executive Summary

Care agents escalate cases to internal Salesforce teams via Zendesk Side Conversations but have no visibility into whether SF has picked up the case without leaving Zendesk to check. This creates SLA breach risk on the Zendesk ticket while the merchant waits — particularly on Premium and Enterprise accounts where SLA breach has direct commercial consequences. This PRD defines two capabilities: surfacing SF case status directly in the Agent Toolkit sidebar (via case number extraction from SF's auto-reply and a BigQuery lookup), and automating a chaser to the SF case when the team has not progressed within the merchant's segment SLA threshold. Together, these remove the need for agents to monitor SF manually and reduce the risk of SLA breach on SF-dependent tickets. This is part of the Agent Productivity Tools deliverable (MCD-570, Q2–Q4 2026), applying the same extraction-and-query pattern already established in the Zendesk–Jira integration — lower technical risk, faster delivery. Approve to proceed to Phase 1 discovery sprint; estimated start TBC.

---

## Problem Space

**Problem statement:** When Care agents send a case to a Salesforce team via Side Conversation, they lose visibility. They cannot tell whether the SF team has opened the case, is working it, or has missed it — without logging into Salesforce to check. Meanwhile the Zendesk ticket SLA clock continues running.

**Who is affected:** All Care agents who escalate to internal SF-managed teams (e.g. Treasury, Billing, Risk, Disputes). Volume is approximately 5–10 tickets per week (TBC — establish at start of discovery). While low in volume, these tickets skew toward Premium and Enterprise merchants where SLA breach is a direct commercial and relationship risk.

**Evidence:** Manual process only; no integration between Zendesk Side Conversations and SF case status. Agents report checking Salesforce separately during active tickets. SLA breach risk on SF-dependent tickets is a known operational pain point flagged by Director of Operations Excellence.

**Competitive context:** Not applicable — this is internal tooling, not a merchant-facing product.

**Why now:** Delivering as part of Agent Productivity Tools (MCD-570) to support the 2026 SLA compliance goal. The Zendesk–Jira integration establishes the extraction-and-query pattern; applying it to Salesforce is lower-risk than a net-new approach and can be delivered in parallel.

---

## Goals and Success Metrics

**Business goals:** Reduce cost per contact by removing manual SF status checks during active ticket handling. Protect Zendesk SLA compliance on tickets escalated to SF by ensuring SF teams receive automated chasers when they have not responded in time. Meet 95% SLA Care goal for 2026.

**Merchant goals:** Faster resolution on cases that depend on an SF team's response, with fewer delays caused by agents not knowing a case has stalled.

**Non-goals (this release):**

- Full bi-directional Salesforce case management from Zendesk (create SF cases from ZD — agents already do this via Side Conversations)
- SF case comments syncing to Zendesk (v1: status display only)
- Merchant-visible notifications triggered by SF case events
- SF case creation or closing initiated from Zendesk

**Success metrics**


| Metric                                                                                                         | Why it matters                                                                    | Baseline                                    | Target                                                | Source              |
| -------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------- | ----------------------------------------------------- | ------------------- |
| SLA breach rate on Zendesk tickets with a linked SF case (% of SF-linked tickets that breach SLA)             | Direct measure of the problem this solves                                         | TBC — establish by end of discovery sprint  | Measurable reduction vs baseline, 90 days post-launch | Zendesk SLA reports |
| % of SF-escalated tickets (tickets with Side Conversation to known SF email domain) where case number extracted | Measures reliability of the extraction mechanic; denominator = SF-escalated tickets | TBC — establish in Phase 1 testing          | >95%                                                  | Integration logs    |
| Automated chasers sent per week (monitoring metric)                                                            | Confirms the mechanic fires; flags if chaser rate is unexpectedly high or zero    | 0 (feature not yet live)                    | Tracked from launch; no target — monitoring only      | Integration logs    |

---

## Customer Segments and Needs

**Customer segment(s):** Internal. Primary users are Care agents (L1/L2). Merchants benefit indirectly through faster resolution on cases that depend on SF teams.

**User stories**

- As a Care agent who has sent a case to an SF team via Side Conversation, I want to see the SF case status in my Zendesk sidebar, so that I know whether the case has been picked up without logging into Salesforce.
- As a Care agent managing a ticket close to SLA breach, I want to know that an automated chaser has been sent to the SF team if they haven't responded in time, so that I don't need to follow up manually to protect the SLA.
- As an SF team member who has not picked up a case in time, I receive an automated chaser on the case, so that urgent cases are flagged to me without depending on the Care agent to follow up manually.

---

## Proposed Solution and Scope

**Solution overview:** Extract the SF case number from the auto-reply SF sends when a side conversation email creates a case. Store this number on the Zendesk ticket. Use it to query BigQuery (which holds SF case data) and surface case status, assignee, and last-updated timestamp in the Agent Toolkit sidebar. Separately, run automated logic that fires a chaser via the side conversation when the SF case has not progressed within the merchant's segment threshold.

> Alternatives evaluated: see Appendix.

**In scope**

- Extraction of SF case number (8-digit format: `^[0-9]{8}$`) from SF's auto-reply to a Zendesk Side Conversation
- Storage of extracted case number as a custom field on the Zendesk ticket
- Agent Toolkit sidebar panel showing SF case status, assignee, and last-updated timestamp (sourced from BigQuery); displays "Data as of [timestamp]" to communicate data freshness
- Automated chaser message sent via the side conversation thread when the SF case status has not progressed beyond New/Open within the merchant's segment threshold
- Internal note posted on the Zendesk ticket when a chaser fires, confirming it was sent (timestamp + side conversation reference)

**Out of scope**

- SF case comments syncing to Zendesk (v1: status display only)
- Full bi-directional case management (agents cannot update SF case fields from Zendesk in v1)
- SF case creation from Zendesk (agents use Side Conversations for this today)
- Second or subsequent automated chasers (v1: one chaser per escalation; escalation ceiling to be defined in v2 scoping)
- Merchant-visible notifications from SF case events

---

## Requirements

**Requirements by audience / domain**


| Domain                          | Requirement IDs            | Purpose                                                                       |
| ------------------------------- | -------------------------- | ----------------------------------------------------------------------------- |
| **Care Ops / Agent Experience** | FR-1, FR-2, FR-3, FR-4     | Agents see SF case status in sidebar; receive internal note when chaser fires |
| **SF Teams**                    | FR-5                       | SF teams receive automated chaser on cases that stall                         |
| **Engineering / Product**       | FR-0, FR-6                 | Instrumentation; extraction and storage of SF case number                     |
| **Zendesk Admin**               | FR-7, FR-8                 | Custom field for SF case number; tag for SF-escalated tickets; Explore view   |
| **Security & Compliance**       | NFR-1                      | SF case data displayed as internal only; no merchant-visible auto-population  |

### Functional requirements


| ID       | Area                            | Requirement                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Priority |
| ---------- | --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **FR-0** | **Instrumentation**             | **Key events defined in the Instrumentation section must be implemented, validated in staging, and confirmed firing before Phase 2 go-live.** *AC: All listed events fire correctly in staging; validated by Engineering and Data Engineer before Phase 2 entry.*                                                                                                                                                                                                                                                                                                                 | **P0**   |
| FR-1     | Case number extraction          | When a Side Conversation receives a reply containing an 8-digit SF case number (`^[0-9]{8}$`), the case number is extracted and stored as a custom field on the Zendesk ticket. *AC: Given a Side Conversation reply containing a case number matching the pattern, when the reply is received, then the custom field on the Zendesk ticket is populated with the extracted case number within 5 minutes.*                                                                                                                                                                        | P0       |
| FR-2     | Agent Toolkit sidebar display   | The Agent Toolkit sidebar shows a Salesforce panel when an SF case number is present on the ticket. The panel displays: SF case status, SF case assignee (name), and last-updated timestamp from BigQuery. A "Data as of [timestamp]" label is shown to indicate data freshness.*AC: Given a Zendesk ticket with a linked SF case number, when an agent views the ticket, the sidebar panel shows current status, assignee, and last-updated timestamp from BigQuery. The timestamp reflects the most recent BigQuery sync, not real-time data.*                                  | P0       |
| FR-3     | Automated chaser                | When the elapsed time since the Side Conversation was sent exceeds the segment threshold AND the SF case status in BigQuery has not moved beyond New/Open, the system sends an automated chaser reply via the side conversation thread. Chaser evaluation runs on a scheduled cycle (cadence TBC — confirm with Engineering in Phase 1). After one chaser fires, no further automated action is taken in v1; the agent must review the ticket manually if SF still has not responded. *AC: Given a ticket where the segment threshold has elapsed and the SF case status remains New/Open in the most recent BigQuery sync, when the chaser condition is evaluated, then a chaser message is sent to the SF case via the side conversation within the next evaluation cycle. The chaser fires at most once per escalation (v1).* | P0       |
| FR-4     | Internal note on chaser         | When an automated chaser is sent (FR-3), an internal note is added to the Zendesk ticket confirming the chaser was sent, including the timestamp and side conversation reference. *AC: Given a chaser has fired, the Zendesk ticket shows an internal note with: "Automated chaser sent to SF case [case number] at [timestamp] via Side Conversation [reference]."* | P1       |
| FR-5     | Chaser message content          | The automated chaser message sent to the SF case is pre-agreed with Content Strategist and Operations. *AC: Chaser message text is approved before Phase 3 go-live. [Message copy TBC — see Open Questions.]* | P1       |
| FR-6     | Segment threshold configuration | Chaser thresholds are configurable per merchant segment (Standard / Enterprise / Premium) without a code deployment. *AC: Thresholds can be updated by Engineering or Zendesk Admins via configuration; no deployment required.* | P1       |
| FR-7     | Zendesk custom field            | A custom field named `sf_case_number` (text type) is created on Zendesk tickets to store the extracted SF case number. *AC: Field exists and is populated correctly by FR-1; visible in ticket sidebar for Zendesk Admins; not visible to merchants.* [Owner: Zendesk Admins — Phase 1 config] | P0       |
| FR-8     | Zendesk tag and Explore view    | All tickets with a linked SF case are tagged `sf_escalated`. An Explore view filters on this tag and surfaces SLA breach rate for SF-linked tickets. *AC: Tag is applied when SF case number is stored (FR-1); Explore view is available before Phase 4 go-live and used to track the primary success metric.* [Owner: Zendesk Admins — Phase 2] | P1       |

### Non-functional requirements

**NFR-1 — Security / Compliance:** SF case data surfaced in the Agent Toolkit is visible to agents only as an internal panel. SF case content must not be auto-populated into merchant-visible replies or public ticket fields.
*Acceptance criteria: No data path allows SF case fields to appear in public Zendesk replies or external-facing content. Verified in Phase 2 testing.*

**NFR-2 — Data freshness transparency:** The sidebar must always show the timestamp of the last BigQuery sync alongside SF case data. Stale data (>2 hours since last sync) should be visually flagged.
*Acceptance criteria: A "Data as of [timestamp]" label is present on every SF case panel. If last sync timestamp is >2 hours old, the panel shows a warning indicator.*

**NFR-3 — Chaser idempotency:** The automated chaser fires at most once per Zendesk ticket per escalation (v1). Duplicate chasers must not be sent due to retry logic or evaluation cycle overlaps.
*Acceptance criteria: Given a ticket where the chaser has already fired, when the chaser condition is re-evaluated, then no additional chaser is sent.*

**NFR-4 — Sidebar states:** The SF case panel must handle all key states gracefully. Required states: (1) loading — panel shows a loading indicator while querying BigQuery; (2) no case number — panel is hidden or shows "No SF case linked"; (3) data returned — status, assignee, last-updated shown with "Data as of [timestamp]"; (4) stale data (>2 hours) — warning indicator shown; (5) BigQuery query error — panel shows "Unable to load SF case data — try refreshing" (not a blank panel); (6) chaser already sent — panel or internal note indicates "Chaser sent [timestamp]".
*Acceptance criteria: All six states are defined in wireframes before Phase 2 build begins; each state is tested in Phase 2. [Copy ownership: Content Strategist.]*

**Constraints**

- BigQuery sync is batch/scheduled (hourly+); real-time SF case data is not available. All status display and chaser logic must account for up to ~1 hour of data lag.
- SF case number format is 8 digits (`^[0-9]{8}$`). Extraction logic is scoped to this pattern only.
- Agents cannot trigger, cancel, or resend chasers manually in v1.

---

## Design and User Experience

**Design & UX:** TBC — wireframes to be created with Engineering before Phase 2. **Copy ownership: Content Strategist** (all sidebar labels, state messages, and chaser message).

**Agent Toolkit sidebar — SF case panel**

Key flows:

1. Agent opens a Zendesk ticket that has a Side Conversation. SF has replied with an auto-reply containing the case number. The case number is extracted and stored automatically (no agent action required).
2. Agent sees an "SF Case" panel in the Agent Toolkit sidebar showing: case number, status, assignee, and last-updated timestamp. "Data as of [timestamp]" label is visible.
3. If the BigQuery data is stale (>2 hours), the panel shows a warning: "Data may be outdated — last synced [timestamp]."
4. If the chaser has fired, the internal note on the ticket reads: "Automated chaser sent to SF case [case number] at [timestamp]." The sidebar also shows "Chaser sent [timestamp]" so agents do not need to scroll the ticket to confirm.

**Required sidebar states (all must be specified in wireframes before Phase 2):** Loading; no SF case linked; data loaded (normal); stale data warning (>2 hours); BigQuery query error; chaser already sent. See NFR-4.

**Agent guidance on data staleness:** Agent runbook must include: "The SF case panel reflects data as of the last BigQuery sync (up to ~1 hour ago). If the panel still shows New/Open after a chaser has fired, this does not mean the chaser failed — the SF team may have responded but the data has not yet refreshed. Check the internal note timestamp and allow one sync cycle before escalating further."

**SF case fields to display (v1 — confirm with agents in Phase 1 discovery):** Status, assignee name, last updated timestamp. Additional fields (case priority, case subject, case age) to be agreed in agent discovery session.

**Chaser message copy:** TBC — to be agreed with Content Strategist and Director of Operations Excellence before Phase 3 entry.

---

## Instrumentation and Monitoring

**Key events to instrument**

- `sf_case_number_extracted`: Zendesk ticket ID, SF case number, timestamp, extraction source (side conversation reply)
- `sf_case_status_displayed`: Zendesk ticket ID, SF case number, SF case status shown, BigQuery sync timestamp, data age at display time (minutes)
- `sf_chaser_sent`: Zendesk ticket ID, SF case number, merchant segment, time since Side Conversation sent, SF case status at time of chaser, timestamp
- `sf_chaser_skipped`: Zendesk ticket ID, SF case number, reason (chaser already sent; SF case progressed; data too stale to evaluate), timestamp

**Internal dashboards and monitoring**

- SF Escalation Health dashboard: count of SF-linked tickets, breakdown by segment, SF case status distribution at time of chaser evaluation, chaser send rate per week
- Extraction reliability: % of Side Conversation replies where a case number was expected but not extracted (requires comparison against tickets sent to known SF teams)
- Data freshness monitor: daily alert if BigQuery SF sync has not run within expected cadence (owner: Data Engineering)

**Validation approach**

- All events validated in staging before Phase 2 entry (FR-0).
- Silent failure detection: daily row count alert on `sf_case_number_extracted` — if count drops to zero on a day with known SF escalation activity, alert fires. Owner: Data Engineer. Cadence: daily.
- Post-launch: compare `sf_chaser_sent` count against Zendesk SLA breach rate on SF-linked tickets to validate impact.

---

## Risks, Assumptions, and Open Questions

**Risks**


| Risk                                                                                                                     | Likelihood | Impact | Mitigation                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------ | ---------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Zendesk Side Conversations API does not support automated system replies (not from a named agent)                        | Medium     | High   | Validate in Phase 1 technical spike before any build begins. If not supported natively, evaluate webhook-based approach or Zendesk app; this is a hard dependency for the chaser mechanic.                        |
| SF auto-reply format is inconsistent; case number extraction fails for some emails                                       | Medium     | High   | Validate auto-reply format across SF teams in discovery; build monitoring for extraction failures; fallback: agent can manually enter case number in Phase 2                                                       |
| BigQuery data is stale at chaser evaluation time; chaser fires even though SF has already responded                      | Medium     | Medium | Surface "Data as of" timestamp prominently; build a buffer: do not evaluate chaser until at least 1 hour after Side Conversation sent AND at least 1 BigQuery sync has completed; NFR-3 ensures no duplicate fires |
| Chaser message is perceived as aggressive by SF teams; damages working relationship                                      | Medium     | Medium | Agree message copy with Operations before Phase 3; brief SF team leads before go-live (Phase 3 entry criterion)                                                                                                   |
| Extraction regex matches false positives (other 8-digit numbers in email)                                                | Low        | Medium | Scope extraction to Side Conversations from known SF email domains only; validate in Phase 1 testing                                                                                                               |
| Chaser automation misfires at scale (false positives sent to SF teams); no kill switch in place                          | Low        | High   | Rollback plan: chaser automation can be disabled by Engineering without a full deployment (configuration flag). Kill switch owner: Engineering Manager. Agent revert to manual process on rollback.               |

**Key assumptions**

- SF sends an auto-reply to every side conversation email that creates a case. Reliability of this must be confirmed in discovery. If SF does not auto-reply consistently, the extraction mechanic fails and the whole feature is blocked. [Validate: Phase 1 — test against known SF teams before build.]
- BigQuery contains SF case status, assignee, and last-updated fields, updated on a batch schedule. Exact sync cadence and field availability to be confirmed with Data Engineering.
- The Zendesk Side Conversations API supports sending an automated reply from the system (not from a named agent). This is a hard dependency for the chaser mechanic. [Validate: Phase 1 technical spike — must be confirmed before build begins.]

**Open questions**

1. **BigQuery sync frequency and field availability:** What is the exact sync cadence? Which SF case fields are available? [Owner: Data Engineering — Phase 1]
2. **Chaser thresholds per segment:** What is the correct threshold (in business hours) for Standard, Enterprise, and Premium? [Owner: Director of Operations Excellence — Phase 1]
3. **Chaser message copy:** What should the automated chaser say? [Owner: Content Strategist + Director of Operations Excellence — Phase 2, before Phase 3 entry]
4. **Escalation ceiling:** If SF has still not responded after the chaser, what happens? Does the agent get an alert? Does a second chaser fire? [Owner: Charlie + Director of Operations Excellence — scope for v2]
5. **Agent Toolkit SF case fields:** Beyond status, assignee, and last updated — what else do agents need from the SF case? [Owner: Charlie — agent discovery session, Phase 1]
6. **SF email domain whitelist:** Which SF team email addresses does Checkout use for Side Conversations? Required to scope extraction to the right emails. [Owner: Zendesk Admins — Phase 1]

---

## Rollout Plan

**Rollout approach:** Four phases — discovery and technical validation, build and internal testing, UAT, general availability. Rollback: chaser automation disabled via configuration flag (no deployment required); extraction trigger disabled by Zendesk Admin. Agents revert to manual SF checks. Existing tickets unchanged. Kill switch owner: Engineering Manager.

### Phase 1: Discovery and technical validation

**Purpose:** Validate assumptions before committing to build. Confirm SF auto-reply reliability, BigQuery field availability, Zendesk API support for automated side conversation replies, and SF email domain list.

**Entry criteria**

- Technical: Engineering and Data Engineering available for discovery
- Operational: Sample Side Conversation emails from known SF teams available for testing

**Success criteria**

- SF auto-reply format confirmed as consistent and parseable with 8-digit regex
- BigQuery SF case data fields and sync cadence confirmed
- Zendesk API capability for automated side conversation reply confirmed
- Chaser thresholds agreed per segment (Open Question 2 resolved)
- SF email domain whitelist confirmed (Open Question 6 resolved)

**Timeline:** TBC

### Phase 2: Build and internal testing

**Purpose:** Build extraction, BigQuery query, sidebar display, and chaser automation. Validate end-to-end against test tickets before agents see it.

**Entry criteria**

- Technical: Phase 1 success criteria met; all P1+ open questions resolved; test Zendesk environment available with test Side Conversations
- Operational: Zendesk Admins available for sidebar configuration

**Success criteria**

- Case number extraction works for >95% of test Side Conversation replies
- Sidebar displays correct SF case data with accurate "Data as of" timestamp
- Chaser fires correctly against segment thresholds on test tickets; does not fire twice
- Internal note appears on ZD ticket when chaser fires
- No SF case data visible in merchant-facing ticket fields (NFR-1 validated)
- All instrumentation events firing correctly in staging (FR-0)

**Timeline:** TBC

### Phase 3: UAT with Care Operations

**Purpose:** Validate with a small group of Care agents on live tickets before full rollout.

**Entry criteria**

- Technical: Phase 2 signed off; no P0 bugs outstanding
- Operational: Chaser message copy agreed (Open Question 3 resolved); SF team leads briefed on incoming automated chasers before Phase 3 begins (SF teams will receive chasers on live tickets during UAT); UAT agent group identified; agent guidance on BQ staleness prepared

**Success criteria**

- Agents confirm sidebar is useful and data freshness caveat is clear
- No false-positive chasers observed in UAT period
- SF team leads confirm chaser is received and understood correctly

**Timeline:** TBC

### Phase 4: General availability

**Purpose:** Enable for all Care agents.

**Entry criteria**

- Technical: All P0 requirements delivered and tested; monitoring in place
- Operational: Agent briefing and runbook published (including BQ staleness guidance and post-chaser behaviour); internal KB article published for agents; SF team leads notified of full rollout; escalation ceiling (Open Question 4) defined or deferred to v2 with documented scope
- Business: All P1 open questions resolved or accepted as deferred

**Success criteria:** All agents can see SF case status in sidebar; chaser automation live for all merchant segments; SLA breach rate on SF-linked tickets tracked from launch.

**Definition of Done**

- Technical: All P0 requirements delivered and tested; extraction, display, chaser, and internal note working; instrumentation validated
- Operational: Agent briefing complete; runbook published; SF team leads briefed; monitoring active
- Business: Success metric baselines established; post-launch review scheduled for 90 days

**Product dependencies**


| Dependency                                                          | Owner                             | Status          |
| --------------------------------------------------------------------- | ----------------------------------- | ----------------- |
| BigQuery SF case data fields and sync cadence confirmed                        | Data Engineering                  | Open — Phase 1 |
| Zendesk API support for automated side conversation reply confirmed            | Engineering                       | Open — Phase 1 |
| Chaser thresholds per segment agreed                                           | Director of Operations Excellence | Open — Phase 1 |
| SF email domain whitelist for extraction scoping                               | Zendesk Admins                    | Open — Phase 1 |
| `sf_case_number` custom field created in Zendesk                               | Zendesk Admins                    | Open — Phase 1 |
| `sf_escalated` tag and Explore view configured                                 | Zendesk Admins                    | Open — Phase 2 |
| Sidebar wireframes and state definitions complete (all 6 states per NFR-4)     | Engineering + Content Strategist  | Open — before Phase 2 |
| Chaser message copy approved                                                   | Content Strategist + Operations   | Open — Phase 2 |
| Internal KB article for agents published                                       | Content Strategist                | Open — Phase 4 |

**Go-to-market:** Internal only. Care Operations briefs agents and publishes updated runbook. SF team leads receive advance notice before Phase 4 go-live. No merchant-facing change.

---

## Appendix

**Strategy and research**

- `2026 deliverables.md` — Agent Productivity Tools (MCD-570)
- `01-knowledge-base/strategy/care-product-model.md` — Agent Experience domain

**Alternatives considered**

- **Option 1 — Manual agent process (status quo):** Agents log into Salesforce to check case status. Rejected: scales with agent effort, does not reduce cost, does not protect SLA.
- **Option 2 — Salesforce-native alerts:** SF sends email notifications to agents when case status changes. Rejected: requires SF team config changes across multiple internal teams; does not surface data inside Zendesk; does not automate the chaser.
- **Option 3 — Zendesk SLA escalation without SF status:** Use Zendesk's native SLA breach notification to alert agents when a ticket is at risk. Partially addresses the problem but does not tell agents whether SF has picked up the case; does not automate the chaser to SF. Considered as a fallback if Phase 1 validation fails.
- **Why we chose this approach:** The extraction + BigQuery query pattern is already established in the Jira integration and Agent Toolkit. Extending it to Salesforce is lower-risk than a net-new pattern. Automating the chaser via Side Conversations removes the need for any SF-side configuration.

**Technical and operational**

- `04-active-work/roadmap-items/zendesk-jira-integration-prd.md` — Reference PRD and pattern for Zendesk external system integration
- `01-knowledge-base/processes/agent-toolkit-zendesk.md` — Agent Toolkit product context
- `01-knowledge-base/processes/support-workflows.md` — Escalation workflow context
