# Zendesk–Jira Integration

**Status**: Draft — For Zendesk Admin Review  
**Owner**: Charlie Wildish  
**Last Updated**: February 2026  
**Stakeholders**: Care Operations, Operational Excellence, Zendesk Admins, L3 Engineering (Ramyaa), IT (Arnold S)


## Executive Summary

Agents today log into both Zendesk and Jira to escalate, track, and relay updates — manual overhead and incomplete handoffs. This PRD defines Zendesk–Jira Service Management (JSM) integration so agents create, link, and track Jira tickets from Zendesk; Engineering sees SLA urgency without logging into Zendesk.


## Problem

**What problem are we solving, and who has it?**  
Agents escalating to Engineering open Jira, create a ticket, copy context (Client ID, description), then return to Zendesk. Jira progress is invisible in Zendesk; agents re-check Jira and copy comments back. Result: delays, missed updates, incomplete context. Affects all agents who escalate.

**How are they solving it today?**  
Manual copy-paste; no integration. Agents duplicate info and chase updates via Slack instead of in Zendesk.

**Why solve this now?**  
Escalation is a known friction point. JSM is in place; integration reduces agent effort and improves handoff quality for faster merchant resolution.


## Goals & Success Metrics


| Metric                                                                                                         | Current State                                     | Target                                         | Timeline             |
| -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- | ---------------------------------------------- | -------------------- |
| Steps required to create an Engineering escalation from Zendesk                                                | Baseline TBC (currently requires leaving Zendesk) | Escalation completable without leaving Zendesk | At launch            |
| % of Jira escalation tickets with all required fields populated at creation (Client ID, Client Name, Priority) | Baseline TBC — estimated low due to manual entry  | >95%                                           | 3 months post-launch |
| Agent-reported frequency of checking Jira separately for escalation status                                     | Baseline TBC                                      | Measurable reduction vs baseline               | 3 months post-launch |
| Escalation volume to Engineering per week                                                                      | TBC — needed to baseline                          | Tracked                                        | At launch            |



## User Stories

### Care agent: escalating a ticket to Engineering

**As a** Care agent who has determined that a merchant issue requires Engineering investigation,  
**I want** to create a Jira ticket directly from the Zendesk ticket,  
**So that** I can hand off to Engineering without leaving Zendesk and without manually re-entering merchant context.

**Acceptance Criteria**:

- Agent can trigger Jira ticket creation from a button or panel within the Zendesk ticket
- The following fields are pre-populated from Zendesk data: Summary, Description, Client ID, Client Name, Priority
- The Zendesk SLA (time remaining / breach status) is passed to Jira as a read-only static field so Engineering can see urgency
- The Jira ticket ID is surfaced back in the Zendesk ticket immediately after creation
- Agent can confirm or edit pre-populated fields before submitting


### Care agent: linking to an existing Jira ticket

**As a** Care agent whose merchant issue is already covered by an open Jira ticket (e.g. a known bug affecting multiple merchants),  
**I want** to link my Zendesk ticket to that existing Jira ticket,  
**So that** I can track its progress without creating a duplicate.

**Acceptance Criteria**:

- Agent can search for and link to an existing Jira ticket from within Zendesk
- Multiple Zendesk tickets can be linked to the same Jira ticket (Many-to-One supported)
- The linked Jira ticket's status is visible in the Zendesk sidebar for each linked Zendesk ticket


### Care agent: tracking Engineering progress from Zendesk

**As a** Care agent managing an open escalation,  
**I want** to see the current status of the linked Jira ticket and any comments Engineering has added,  
**So that** I can update the merchant without logging into Jira.

**Acceptance Criteria**:

- Jira ticket status (e.g. Open, In Progress, Resolved) is visible in a Zendesk sidebar panel and updates in near real-time
- Comments added in Jira by Engineering sync to Zendesk as **internal notes** — visible to agents only, never to merchants
- Agent can manually copy an internal note to an external reply if the content is appropriate to share with the merchant
- The Jira panel clearly shows the linked ticket ID and a direct link to open the ticket in Jira when deeper context is needed


### Care agent: communicating with Engineering from Zendesk

**As a** Care agent who needs to provide additional context or ask a follow-up question to Engineering,  
**I want** to add a comment to the Jira ticket from within Zendesk,  
**So that** I don't have to switch to Jira to continue the conversation.

**Acceptance Criteria**:

- Agent can write and submit a comment to Jira directly from the Zendesk ticket
- Comment appears in Jira attributed to the agent
- Comment is also recorded in the Zendesk ticket as an internal note for audit purposes


### Engineering team member: receiving a well-structured escalation

**As an** Engineering team member picking up a JSM ticket raised from Care,  
**I want** to see the merchant context and SLA urgency without having to look up the Zendesk ticket,  
**So that** I can prioritise and start investigating immediately.

**Acceptance Criteria**:

- JSM ticket contains: Summary, Description, Client ID, Client Name, Priority, Zendesk ticket ID, Zendesk SLA (read-only)
- A direct link back to the originating Zendesk ticket is visible on the JSM ticket
- If multiple Zendesk tickets are linked, all ticket IDs are listed

**Edge cases**:

- **Many-to-One (multiple Zendesk tickets linked to one Jira ticket)**: Each Zendesk ticket shows the shared Jira status independently. When a Zendesk ticket is closed, a comment is automatically added to the Jira ticket noting which Zendesk ticket closed and its resolution — the Jira ticket itself is **not** automatically closed.
- **Jira ticket promoted to a Jira Software bug**: If a JSM ticket is escalated to a Jira Software bug ticket, the linked Zendesk ticket(s) should surface the bug ticket status alongside the JSM ticket status.
- **Zendesk ticket closed before Jira ticket resolved**: Zendesk closure sends a comment to Jira with the Zendesk resolution. Engineering reviews and decides whether to close the Jira ticket. Auto-close is explicitly not implemented in v1 (see Out of Scope).
- **Agent links to wrong Jira ticket**: Agent must be able to remove a link and re-link to the correct ticket from within Zendesk.


## Requirements

#### Must Have (P0)

- Create a JSM ticket from Zendesk, pre-populated with: Summary, Description, Priority, Client ID, Client Name, Zendesk ticket ID, Zendesk SLA (read-only)
- Link a Zendesk ticket to an existing Jira ticket (search and link from within Zendesk)
- Many-to-One linking supported — multiple Zendesk tickets can link to a single Jira ticket
- Jira ticket status visible in a Zendesk sidebar panel
- Jira comments sync to Zendesk as internal notes (never as public replies)
- Agents can add a comment to Jira from within Zendesk
- Agent can remove or change a Jira link from within Zendesk

#### Should Have (P1)

- Zendesk SLA (time remaining / breach status) displayed as a read-only static field on the Jira ticket — updated when the Zendesk SLA changes
- When a Zendesk ticket is closed, an automatic comment is added to the linked Jira ticket noting the Zendesk ticket ID, resolution, and closure timestamp
- Bug ticket tracking: if a JSM ticket is promoted to a Jira Software bug, the Zendesk sidebar surfaces the bug ticket status in addition to the JSM status

#### Nice to Have (P2)

- Slack notifications when a Jira ticket is created from Zendesk — channel design and scope TBC (see Open Questions)
- Reporting view on Jira tickets created from Care — audience and metrics TBC

**Constraints**:

- **Security / Compliance**: Jira comments synced to Zendesk are internal notes only — merchant-visible content must never be auto-populated from Jira without agent review
- **Integrations**: Zendesk ↔ Jira Service Management (JSM); optionally Jira Software (bug tracking); Slack (P2 only). The relationship between Zendesk and JSM is Many-to-One from Zendesk's side.
- **Permissions**: Agents should not need direct Jira access to perform P0/P1 actions — all Jira interaction happens via the Zendesk integration layer


## Approach

**Implementation approach**: Start with the native Zendesk Marketplace Jira app (Zendesk/Atlassian) — it covers most P0/P1. Zendesk Admins configure app and field mappings; Engineering/IT configure JSM to receive tickets. Custom build only if the app can’t meet a requirement.

**Agent flow — creating a new escalation**:

```
1. Agent is on a Zendesk ticket and determines Engineering escalation is needed
2. Agent opens the Jira panel in the Zendesk sidebar
3. Agent selects "Create Jira ticket"
4. Pre-populated form appears: Summary (from ticket subject), Description (from ticket body),
   Client ID, Client Name (from org record), Priority, SLA status (from Zendesk SLA field)
5. Agent reviews, edits if needed, and submits
6. Jira ticket is created; ticket ID and status appear in the Zendesk sidebar
7. Agent can now track progress and add comments from the same panel
```

**Agent flow — linking to an existing Jira ticket**:

```
1. Agent opens the Jira panel in the Zendesk sidebar
2. Agent selects "Link to existing ticket" and searches by Jira ticket ID or keyword
3. Agent selects the correct ticket; link is created
4. Jira status and comments are now visible in the sidebar
```

**Key UX decisions**: Jira comments → internal notes only in Zendesk; agents choose what to share. No auto-close of Jira on Zendesk close in v1; closure sends a comment; Engineering owns Jira lifecycle.

**Technical notes**: Zendesk Admins: install Jira app, map Client ID/Client Name from org fields, configure comment sync. Engineering/IT: confirm JSM structure and Jira Software vs JSM instance. Confirm which Zendesk SLA field is passed (breach time, time-remaining, or status label).


## Out of Scope

- Auto-close Jira on Zendesk close (v1: comment on closure only; Engineering owns Jira closure)
- Slack notifications; reporting on Care-originated Jira tickets (until scope defined)
- Automated merchant updates from Jira comments (agent-controlled only)
- Jira-native SLA (this PRD only surfaces Zendesk SLA in Jira as read-only)


## Launch Plan

- **Phase 1 — Configuration & field mapping**: Install Zendesk Jira app; agree field mappings with Engineering/IT; configure JSM project to receive Care escalations. Confirm Jira Software / bug ticket relationship.
- **Phase 2 — Internal testing**: Zendesk Admins and a small group of Care agents test end-to-end (create, link, comment, closure notification) against a test JSM project.
- **Phase 3 — UAT with Care Operations**: Broader agent group tests against live JSM project; validate that field pre-population is accurate and SLA field is displaying correctly.
- **Phase 4 — Rollout**: Enable for all Care agents; brief on new workflow (particularly internal note policy for Jira comments).

**Rollback**: Remove Jira app → back to manual process; existing tickets unchanged.


## Risks, Dependencies & Open Questions

**Risks**:


| Risk                                                                       | Likelihood | Impact                                         | Mitigation                                                                                                |
| -------------------------------------------------------------------------- | ---------- | ---------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| Agent accidentally shares an internal Jira comment with merchant           | Medium     | Medium — internal Engineering detail exposed   | Jira comments are internal notes only; agent training on promotion policy; cannot be auto-promoted        |
| Field mapping incorrect at launch (wrong Client ID, missing org data)      | Medium     | High — Engineering receives incomplete tickets | Field mapping validated in Phase 2 testing before go-live; pre-population tested against real org records |
| Jira Software bug tracking out of scope for native app                     | Medium     | Low for v1 — it's P1 not P0                    | Confirm instance structure in Phase 1; if not supported natively, defer to v2                             |
| Many-to-One creates agent confusion (whose ticket is the Jira ticket for?) | Low        | Medium                                         | Clear UI labelling in sidebar; agent guidance on when to create vs link                                   |


**Dependencies**:


| Dependency                                                               | Owner                                                | Status | Risk if Delayed                 |
| ------------------------------------------------------------------------ | ---------------------------------------------------- | ------ | ------------------------------- |
| JSM project set up and ready to receive Care escalations                 | Engineering / IT (Gareth Thomas, Marianne Vanlaecke) | TBC    | Blocks all phases               |
| Zendesk Jira app procured / available on account                         | Zendesk Admins                                       | TBC    | Blocks configuration            |
| Zendesk org fields for Client ID and Client Name confirmed and populated | Zendesk Admins / Care Operations                     | TBC    | Blocks field pre-population     |
| Jira Software instance relationship to JSM confirmed                     | Engineering / IT                                     | TBC    | Blocks bug ticket tracking (P1) |


**Open questions**:

- Who owns the JSM project configuration — IT or Engineering? *IT - Ramyaa and Arnold S as contacts to support*
- What is the current escalation volume from Care to Engineering per week? *its about 5-10% volume*
- For Slack notifications (P2): which channels should receive notifications, split by which criteria (product, priority, team)? *(Owner: Care Operations / Engineering to agree)*


## Timeline


| Milestone                                   | Date | Owner                            | Status   |
| ------------------------------------------- | ---- | -------------------------------- | -------- |
| PRD reviewed and approved                   | TBC  | Charlie Wildish / Zendesk Admins | 🔄 Draft |
| Open questions resolved                     | TBC  | Multiple                         | ⏳        |
| Zendesk Jira app installed and configured   | TBC  | Zendesk Admins                   | ⏳        |
| Field mappings agreed with Engineering / IT | TBC  | Zendesk Admins + Engineering     | ⏳        |
| Internal testing complete                   | TBC  | Zendesk Admins + Care Operations | ⏳        |
| UAT with Care agents                        | TBC  | Care Operations                  | ⏳        |
| Rollout to all agents                       | TBC  | Care Operations / Zendesk Admins | ⏳        |



## Appendix

- `04-active-work/roadmap-items/Copy of JIRA Merchant Care Requirement Document.md` — source discovery workshop requirements (March 2025)
- `01-knowledge-base/processes/support-workflows.md` — escalation to Engineering workflow context
- `01-knowledge-base/teams.md` — team naming reference

