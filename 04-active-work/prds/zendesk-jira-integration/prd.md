# PRD: Zendesk–Jira Integration

**Author:** Charlie Wildish  
**Date:** February 2026  
**Approvers:** Zendesk Admins, Director of Operations Excellence, Engineering/IT (JSM config)  
**Stage:** Solution Design  
**Status:** Draft — For Zendesk Admin Review  
**Last Updated:** March 2026  
**Stakeholders:** Care Operations, Operations Excellence, Zendesk Admins, L3 Engineering (Ramyaa), IT (Arnold S)

**Roadmap alignment (Care & Support)**


| Field                | Value                                                                                                                                                                                                                                     |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2026 deliverable** | Agent Productivity Tools                                                                                                                                                                                                                  |
| **Strategic goal**   | Reduce cost of support                                                                                                                                                                                                                    |
| **Flywheel stage**   | 4. Agent Experience                                                                                                                                                                                                                       |
| **How it fits**      | Bi-directional Zendesk–Jira integration (listed under Agent Productivity Tools in 2026 deliverables) reduces agent effort and handoff friction when escalating to Engineering, improving AHT and resolution time without leaving Zendesk. |


## Executive Summary

Care agents today log into both Zendesk and Jira to escalate, track, and relay updates. Manual copy-paste and context switching create delays, missed updates, and incomplete handoffs. This PRD defines Zendesk–Jira Service Management (JSM) integration so agents create, link, and track Jira tickets from Zendesk, and Engineering sees merchant context and SLA urgency without logging into Zendesk. The outcome is fewer steps per escalation, better field completion, and measurable reduction in agents checking Jira separately. This supports the 2026 goal to reduce cost of support via Agent Experience tooling.

---

## Problem Space

**Problem statement:** Agents escalating to Engineering leave Zendesk, create a Jira ticket manually, copy context (Client ID, description), then return. Jira progress is invisible in Zendesk; agents re-check Jira and copy comments back. Result: delays, missed updates, incomplete context.

**Who is affected:** All Care agents who escalate to Engineering (L1/L2). Escalation volume is approximately 5–10% of support volume. Engineering receives tickets with inconsistent or missing fields and must sometimes open Zendesk to get full context.

**Evidence:** Manual process only; no integration. Agents duplicate info and chase updates via Slack. Escalation is a known friction point in support workflows. JSM is in place; integration reduces agent effort and improves handoff quality for faster merchant resolution.

**Why now:** Escalation friction is documented; JSM is available. Delivering as part of Agent Productivity Tools in 2026 aligns with cost reduction and Agent Experience priorities.

*(Avoid solution talk here. Focus on the pain and impact.)*

---

## Goals and Success Metrics

**Business goals:** Reduce cost per contact by cutting agent time on escalation (create, link, track, comment) and improving handoff quality so Engineering can act without extra lookups.

**Merchant goals:** Faster resolution on issues that require Engineering investigation, via fewer back-and-forth and less agent context-switching.

**Non-goals (this release):** Auto-close Jira on Zendesk close; Slack notifications; reporting on Care-originated Jira tickets; automated merchant updates from Jira comments; Jira-native SLA (we only surface Zendesk SLA in Jira as read-only).

**Success metrics**


| Metric                                                                                           | Why it matters              | Baseline                                 | Target                                         | Source                                       |
| ------------------------------------------------------------------------------------------------ | --------------------------- | ---------------------------------------- | ---------------------------------------------- | -------------------------------------------- |
| Steps to create an Engineering escalation from Zendesk                                           | Proxy for agent effort      | TBC (currently requires leaving Zendesk) | Escalation completable without leaving Zendesk | At launch                                    |
| % of Jira escalation tickets with required fields (Client ID, Client Name, Priority) at creation | Handoff quality             | TBC, estimated low                       | >95%                                           | JSM / integration logs, 3 months post-launch |
| Agent-reported frequency of checking Jira separately for escalation status                       | Proxy for context-switching | TBC                                      | Measurable reduction vs baseline               | Survey / ops feedback, 3 months post-launch  |
| Escalation volume to Engineering per week                                                        | Operational visibility      | TBC                                      | Tracked                                        | At launch                                    |


---

## Customer Segments and Needs

**Customer segment(s):** Internal. Primary users are Care agents (L1/L2) and Engineering (JSM users). Success is measured via agent efficiency and handoff quality; merchants benefit indirectly through faster resolution.

**User stories / jobs to be done**

- As a Care agent who has determined that a merchant issue requires Engineering investigation, I want to create a Jira ticket directly from the Zendesk ticket, so that I can hand off without leaving Zendesk and without manually re-entering merchant context.
- As a Care agent whose merchant issue is already covered by an open Jira ticket (e.g. known bug affecting multiple merchants), I want to link my Zendesk ticket to that existing Jira ticket, so that I can track progress without creating a duplicate.
- As a Care agent managing an open escalation, I want to see the current status of the linked Jira ticket and any comments Engineering has added, so that I can update the merchant without logging into Jira.
- As a Care agent who needs to provide additional context or ask a follow-up to Engineering, I want to add a comment to the Jira ticket from within Zendesk, so that I don't have to switch to Jira.
- As an Engineering team member picking up a JSM ticket raised from Care, I want to see merchant context and SLA urgency without looking up the Zendesk ticket, so that I can prioritise and start investigating immediately.

---

## Proposed Solution and Scope

**Solution overview:** Integrate Zendesk with Jira Service Management (JSM) via the native Zendesk Marketplace Jira app (preferred). Agents create and link Jira tickets from a Zendesk sidebar panel; Jira status and comments sync into Zendesk as internal notes; agents can comment to Jira from Zendesk. Engineering sees pre-populated fields plus Zendesk SLA and ticket link on the JSM ticket.

**In scope**

- Create JSM ticket from Zendesk with pre-populated fields (Summary, Description, Priority, Client ID, Client Name, Zendesk ticket ID, Zendesk SLA read-only).
- Link Zendesk ticket to existing Jira ticket (search and link from Zendesk); support Many-to-One (multiple Zendesk tickets to one Jira ticket).
- Jira ticket status visible in Zendesk sidebar; Jira comments sync to Zendesk as internal notes only.
- Agents add comments to Jira from Zendesk; agents can remove or change Jira link.
- (P1) Zendesk SLA on Jira ticket; auto-comment on Jira when Zendesk ticket closes; surface Jira Software bug status when JSM ticket is promoted to a bug.

**Out of scope**

- Auto-close Jira when Zendesk closes (v1: comment on closure only; Engineering owns Jira closure).
- Slack notifications; reporting on Care-originated Jira tickets (until scope defined).
- Automated merchant updates from Jira comments (agent-controlled only).
- Jira-native SLA (this PRD only surfaces Zendesk SLA in Jira as read-only).

---

## Alternatives Considered

**Option 1 — Native Zendesk Jira app:** Covers most P0/P1. Zendesk Admins configure app and field mappings; Engineering/IT configure JSM. **Chosen as default:** fastest path, lower build cost.

**Option 2 — Custom integration (Zendesk APIs + Jira/JSM APIs):** Full control over fields and flows. **Rejected for v1:** higher build and maintenance cost; only pursue if native app cannot meet a requirement.

**Why we chose this approach:** Start with native app; custom build only if the app cannot meet a must-have or should-have requirement.

---

## Key Assumptions and Validation

**Critical assumptions**

- Zendesk Marketplace Jira app supports create, link, comment sync, and field mapping (Summary, Description, Client ID, Client Name, Priority, Zendesk ticket ID, Zendesk SLA). **Validate:** Phase 1 configuration and Phase 2 internal testing.
- Zendesk org fields for Client ID and Client Name exist and are populated for tickets we escalate. **Validate:** Field mapping and pre-population checks in Phase 2.
- JSM project is (or will be) set up to receive Care escalations; ownership (IT vs Engineering) is clear. **Validate:** Open questions with IT/Engineering (Ramyaa, Arnold S).
- Jira comments synced to Zendesk will be internal notes only; agents will not auto-promote them to merchant-visible replies. **Validate:** Training and rollout briefing; product constraint (no auto-promotion).

---

## Requirements

**Requirements by audience / domain**


| Domain                          | Requirement IDs  | Purpose                                                                                                              |
| ------------------------------- | ---------------- | -------------------------------------------------------------------------------------------------------------------- |
| **Care Ops / Agent Experience** | FR-1–FR-7, NFR-1 | Create/link Jira tickets from Zendesk; see status and comments; add comments; remove/change link; internal-only sync |
| **Engineering (JSM)**           | FR-8             | Receive well-structured tickets with merchant context and SLA                                                        |
| **Security & Compliance**       | NFR-1            | Jira content in Zendesk is internal only; no merchant-visible auto-population                                        |


### Functional requirements

**FR-1:** Create a JSM ticket from Zendesk, pre-populated with Summary, Description, Priority, Client ID, Client Name, Zendesk ticket ID, Zendesk SLA (read-only).  
**Acceptance criteria:** Given an open Zendesk ticket, when the agent triggers "Create Jira ticket" from the sidebar, then a form appears with these fields pre-populated from Zendesk/org data; agent can edit and submit; Jira ticket is created and its ID is shown in the Zendesk sidebar.

**FR-2:** Link a Zendesk ticket to an existing Jira ticket (search and link from within Zendesk).  
**Acceptance criteria:** Given an open Zendesk ticket, when the agent searches by Jira ticket ID or keyword and selects a ticket, then the link is created and the Jira ticket status is visible in the sidebar.

**FR-3:** Many-to-One linking: multiple Zendesk tickets can link to a single Jira ticket.  
**Acceptance criteria:** Given multiple Zendesk tickets for the same issue, when each is linked to the same Jira ticket, then each Zendesk ticket shows the shared Jira status independently.

**FR-4:** Jira ticket status visible in a Zendesk sidebar panel.  
**Acceptance criteria:** Given a linked Jira ticket, when status changes in Jira, then the sidebar shows current status (e.g. Open, In Progress, Resolved) in near real-time; panel shows ticket ID and direct link to open in Jira.

**FR-5:** Jira comments sync to Zendesk as internal notes (never as public replies).  
**Acceptance criteria:** Given a comment added in Jira by Engineering, when sync runs, then the comment appears in the Zendesk ticket as an internal note only; agent can manually copy to an external reply if appropriate.

**FR-6:** Agents can add a comment to Jira from within Zendesk.  
**Acceptance criteria:** Given a linked Jira ticket, when the agent writes and submits a comment from the Zendesk panel, then the comment appears in Jira attributed to the agent and is also recorded in Zendesk as an internal note.

**FR-7:** Agent can remove or change a Jira link from within Zendesk.  
**Acceptance criteria:** Given a linked Zendesk ticket, when the agent removes or re-links to another Jira ticket, then the sidebar reflects the new link (or no link).

**FR-8 (Engineering):** JSM ticket contains Summary, Description, Client ID, Client Name, Priority, Zendesk ticket ID, Zendesk SLA (read-only), and a direct link to the originating Zendesk ticket; if multiple Zendesk tickets are linked, all ticket IDs are listed.  
**Acceptance criteria:** Given a ticket created from Zendesk, when an Engineering user opens it in JSM, then all listed fields and the link(s) to Zendesk are present and correct.

**P1 (Should Have)**

- Zendesk SLA (time remaining / breach status) displayed as a read-only static field on the Jira ticket, updated when the Zendesk SLA changes.
- When a Zendesk ticket is closed, an automatic comment is added to the linked Jira ticket with Zendesk ticket ID, resolution, and closure timestamp.
- If a JSM ticket is promoted to a Jira Software bug, the Zendesk sidebar surfaces the bug ticket status in addition to the JSM status.

**P2 (Nice to Have)**

- Slack notifications when a Jira ticket is created from Zendesk (channel and scope TBC).
- Reporting view on Jira tickets created from Care (audience and metrics TBC).

### Edge cases

- **Many-to-One:** When a Zendesk ticket is closed, a comment is added to the Jira ticket noting which Zendesk ticket closed and its resolution; the Jira ticket is not auto-closed.
- **Jira ticket promoted to Jira Software bug:** Linked Zendesk ticket(s) surface the bug ticket status alongside the JSM ticket status (P1).
- **Zendesk ticket closed before Jira resolved:** Zendesk closure sends a comment to Jira; Engineering decides whether to close the Jira ticket. Auto-close is out of scope for v1.
- **Agent links wrong Jira ticket:** Agent can remove the link and re-link to the correct ticket from within Zendesk.

### Non-functional requirements

**NFR-1 — Security / Compliance:** Jira content synced to Zendesk is internal notes only. Merchant-visible content must never be auto-populated from Jira without agent review.  
**Acceptance criteria:** No sync path allows Jira comments or fields to appear as public replies or merchant-visible content; configuration and behaviour verified in testing.

**Constraints**

- **Integrations:** Zendesk ↔ Jira Service Management (JSM); optionally Jira Software (bug tracking); Slack (P2 only). Relationship: Many-to-One from Zendesk to Jira.
- **Permissions:** Agents should not need direct Jira access to perform P0/P1 actions; all Jira interaction happens via the Zendesk integration layer.

---

## Design and User Experience

**Key flows**

**Creating a new escalation**

1. Agent is on a Zendesk ticket and determines Engineering escalation is needed.
2. Agent opens the Jira panel in the Zendesk sidebar.
3. Agent selects "Create Jira ticket".
4. Pre-populated form appears: Summary (from ticket subject), Description (from ticket body), Client ID, Client Name (from org record), Priority, SLA status (from Zendesk SLA field).
5. Agent reviews, edits if needed, and submits.
6. Jira ticket is created; ticket ID and status appear in the Zendesk sidebar.
7. Agent can track progress and add comments from the same panel.

**Design note — Zendesk Macros:** To be validated with Zendesk Admins in Phase 1: whether Zendesk Macros can be used to streamline the flow (e.g. one-click to open the Jira panel or apply a standard escalation template). If supported, document in runbook and agent guidance.

**Linking to an existing Jira ticket**

1. Agent opens the Jira panel in the Zendesk sidebar.
2. Agent selects "Link to existing ticket" and searches by Jira ticket ID or keyword.
3. Agent selects the correct ticket; link is created.
4. Jira status and comments are visible in the sidebar.

**Key UX decisions:** Jira comments become internal notes only in Zendesk; agents choose what to share with the merchant. No auto-close of Jira on Zendesk close in v1; closure sends a comment; Engineering owns Jira lifecycle. Clear UI labelling when multiple Zendesk tickets share one Jira ticket.

**Designs:** TBD (native app UI; Zendesk Admins to confirm panel placement and field mapping).

**Technical notes:** Zendesk Admins install Jira app, map Client ID/Client Name from org fields, configure comment sync. Engineering/IT confirm JSM structure and Jira Software vs JSM instance; confirm which Zendesk SLA field is passed (breach time, time-remaining, or status label).

---

## Instrumentation and Monitoring

**Key events to instrument**

- Jira ticket created from Zendesk: ticket ID, Zendesk ticket ID, timestamp, pre-populated fields present/absent.
- Zendesk ticket linked to existing Jira ticket: Zendesk ticket ID, Jira ticket ID, timestamp.
- Comment sent from Zendesk to Jira: Zendesk ticket ID, Jira ticket ID, timestamp.
- Zendesk ticket closed with linked Jira ticket: Zendesk ticket ID, Jira ticket ID, resolution, timestamp (for auto-comment verification).

**Internal dashboards and monitoring**

- Count of Jira tickets created from Zendesk per week (escalation volume).
- % of created Jira tickets with required fields populated (Client ID, Client Name, Priority) — for success metric.

**Validation approach:** Verify events in Phase 2 internal testing; compare counts to JSM and Zendesk data post-launch.

---

## Risks and Open Questions

**Risks**


| Risk                                                                       | Likelihood | Impact          | Mitigation                                                                                         |
| -------------------------------------------------------------------------- | ---------- | --------------- | -------------------------------------------------------------------------------------------------- |
| Agent accidentally shares an internal Jira comment with merchant           | Medium     | Medium          | Jira comments are internal notes only; training on promotion policy; no auto-promotion.            |
| Field mapping incorrect at launch (wrong Client ID, missing org data)      | Medium     | High            | Field mapping validated in Phase 2; pre-population tested against real org records before go-live. |
| Jira Software bug tracking out of scope for native app                     | Medium     | Low for v1 (P1) | Confirm instance structure in Phase 1; if not supported natively, defer to v2.                     |
| Many-to-One creates agent confusion (whose ticket is the Jira ticket for?) | Low        | Medium          | Clear UI labelling in sidebar; agent guidance on when to create vs link.                           |


**Dependencies**


| Dependency                                                               | Owner                                                | Status | Risk if delayed                 |
| ------------------------------------------------------------------------ | ---------------------------------------------------- | ------ | ------------------------------- |
| JSM project set up to receive Care escalations                           | Engineering / IT (Gareth Thomas, Marianne Vanlaecke) | TBC    | Blocks all phases               |
| Zendesk Jira app procured / available on account                         | Zendesk Admins                                       | TBC    | Blocks configuration            |
| Zendesk org fields for Client ID and Client Name confirmed and populated | Zendesk Admins / Care Operations                     | TBC    | Blocks field pre-population     |
| Jira Software instance relationship to JSM confirmed                     | Engineering / IT                                     | TBC    | Blocks bug ticket tracking (P1) |


**Open questions (resolved where noted)**

- **JSM project configuration ownership:** Arnold (IT) supports Jira config; Ramyaa supports Engineering project fields in Jira. Both are contacts for Phase 1.
- **Current escalation volume from Care to Engineering:** Confirmed in the 5–10% ballpark. Baseline formally at launch.
- **Slack notifications (P2):** New channel can be set up if needed. Owner: Care Ops. Channel design and criteria (product, priority, team) TBC when P2 is scoped.

---

## Rollout Plan

**Rollout approach:** Four phases — configuration, internal testing, UAT with Care Operations, full rollout. Rollback: remove Jira app and revert to manual process; existing tickets unchanged.

### Phase 1: Configuration and field mapping

**Purpose:** Install app, agree field mappings with Engineering/IT, configure JSM to receive Care escalations.

**Entry criteria**

- Technical: Zendesk Jira app available; JSM project identified.
- Operational: Zendesk Admins and Engineering/IT available for mapping session.

**Success criteria:** App installed; field mappings agreed (Summary, Description, Priority, Client ID, Client Name, Zendesk ticket ID, Zendesk SLA); JSM project ready; Jira Software vs JSM relationship confirmed.

**Timeline:** TBC

### Phase 2: Internal testing

**Purpose:** End-to-end validation of create, link, comment, and closure notification against a test JSM project.

**Entry criteria**

- Technical: Phase 1 complete; test JSM project available.
- Operational: Zendesk Admins and small group of Care agents available.

**Success criteria:** Create, link, comment, and closure comment work as specified; pre-population accurate; no P0 bugs; agents can complete escalation without leaving Zendesk.

**Timeline:** TBC

### Phase 3: UAT with Care Operations

**Purpose:** Broader agent group tests against live JSM project; validate field pre-population and SLA display.

**Entry criteria**

- Technical: Phase 2 signed off; live JSM project configured.
- Operational: Care Operations briefed; UAT group identified.

**Success criteria:** Field pre-population accurate against real org records; SLA field displays correctly in Jira; agents confirm workflow is acceptable.

**Timeline:** TBC

### Phase 4: General availability

**Purpose:** Enable for all Care agents; new workflow (including internal note policy for Jira comments) in use.

**Entry criteria**

- Technical: All P0 requirements delivered and tested; instrumentation in place.
- Operational: Briefing and guidance on create vs link and internal note policy; runbook or help article available.
- Business: Open questions resolved or accepted as deferred.

**Success criteria:** All agents can create and link Jira tickets from Zendesk; escalation volume and field completion tracked; no critical incidents from misconfiguration or misuse.

**Timeline:** TBC

**Definition of done**

- **Technical:** All P0 requirements delivered and tested; Jira app configured; field mapping and comment sync validated.
- **Operational:** Care agents briefed; internal note policy and create-vs-link guidance published; Zendesk Admins and Engineering/IT know escalation path.
- **Business:** Success metrics baselined where possible; monitoring in place for escalation volume and field completion.

**Product dependencies:** JSM project setup (Engineering/IT); Zendesk app and org fields (Zendesk Admins / Care Operations). See Dependencies table above.

**Go-to-market:** Internal only. Care Operations and Zendesk Admins own agent briefing and rollout comms; no merchant-facing change.

---

## Timeline


| Milestone                                   | Date | Owner                            | Status  |
| ------------------------------------------- | ---- | -------------------------------- | ------- |
| PRD reviewed and approved                   | TBC  | Charlie Wildish / Zendesk Admins | Draft   |
| Open questions resolved                     | TBC  | Multiple                         | Pending |
| Zendesk Jira app installed and configured   | TBC  | Zendesk Admins                   | Pending |
| Field mappings agreed with Engineering / IT | TBC  | Zendesk Admins + Engineering     | Pending |
| Internal testing complete                   | TBC  | Zendesk Admins + Care Operations | Pending |
| UAT with Care agents                        | TBC  | Care Operations                  | Pending |
| Rollout to all agents                       | TBC  | Care Operations / Zendesk Admins | Pending |


---

## Appendix

**Strategy and research**

- `2026 deliverables.md` — Agent Productivity Tools (Zendesk–Jira bi-directional integration)
- `01-knowledge-base/strategy/care-product-model.md` — Agent Experience domain

**Technical and operational**

- `04-active-work/roadmap-items/Copy of JIRA Merchant Care Requirement Document.md` — source discovery workshop requirements (March 2025)
- `01-knowledge-base/processes/support-workflows.md` — escalation to Engineering workflow context
- `01-knowledge-base/teams.md` — team naming reference

