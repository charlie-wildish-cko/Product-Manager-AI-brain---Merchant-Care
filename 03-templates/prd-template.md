# [Feature Name] - Product Requirements Document

**Status**: Draft | In Review | Approved  
**Owner**: [Your Name]  
**Last Updated**: [Date]  
**Stakeholders**: [List key stakeholders; see `01-knowledge-base/teams.md` for correct team names]


## Executive Summary

> 2-3 sentences: What are we building and why? What's the expected impact? If there's one thing you want everyone (including support/ops) to remember, state it. Keep sections as short as clarity allows; prefer bullets and tables over long prose.

[Brief description that anyone can understand]


## Problem

**What problem are we solving, and who has it?**  
[Describe the customer or business problem and the specific users/segments affected]

**How are they solving it today?**  
[Current workarounds, manual processes, or gaps]

**Why solve this now?**  
[Urgency, business impact, strategic importance]

**One sentence support can use** (optional): [e.g. for playbooks/macros: "We're doing X so that [outcome]."]


## Goals & Success Metrics

> For each metric: define numerator/denominator and source of truth so we can compare over time. Who owns reporting and at what cadence? Can support/ops use it to make decisions? If any metric maps to what support will see (e.g. ticket volume, resolution rate), note it.

| Metric | Current State | Target | Timeline |
|--------|--------------|--------|----------|
| [Metric name] | [Baseline] | [Goal] | [When] |
| [Metric name] | [Baseline] | [Goal] | [When] |


## User Stories

**As a** [type of user],  
**I want** [capability],  
**So that** [benefit].

**Acceptance Criteria**:
- [ ] [Specific, testable condition]
- [ ] [Another condition]


**As a** [another user type],  
**I want** [another capability],  
**So that** [another benefit].

**Acceptance Criteria**:
- [ ] [Condition]
- [ ] [Condition]

**Edge cases**:
- [ ] What happens when [edge case]?
- [ ] How do we handle [error condition]?


## Requirements

#### Must Have (P0)
- [ ] [Critical requirement]
- [ ] [Another critical requirement]

#### Should Have (P1)
- [ ] [Important but not blocking]

#### Nice to Have (P2)
- [ ] [Enhancement for future consideration]

**Constraints**:
- **Performance / Scalability**: [e.g. response time, concurrent user targets]
- **Security / Compliance**: [e.g. PCI, GDPR, encryption requirements]
- **Integrations**: [Systems, APIs, or webhooks this must interact with]


## Approach

**User flow**:
```
1. User starts at [location]
2. User does [action]
3. System responds with [result]
```

[Link to design files / mockups if available]

**Key UX decisions**:
- **[Decision]**: [Brief rationale]

**Technical notes**:
- **[Components/systems]**: [What is affected]
- **[Scoping]**: [Anything engineering should know before scoping]

**Error states & support** (if relevant): What messages or states will the customer (and support agent) see when something fails? Runbook or escalation path needed? What should go in the support KB or internal docs so agents can troubleshoot?


## Out of Scope

> Explicitly state what we're NOT doing in this version

- [ ] [Feature we considered but excluded]
- [ ] [Related problem we'll address later]

**Why**: [Brief explanation]


## Support & operations impact

> What do agents need to know or do differently? What training, playbooks, or tool changes before go-live? Likely customer questions and suggested answers? Handoffs/escalation path? Impact on Zendesk, macros, or internal KB? (Omit if not relevant.)

- **Agent impact**: [What changes for frontline]
- **Training / playbooks / tools**: [What's needed before launch]
- **Customer-facing**: [Likely questions, suggested answers, or comms]
- **Handoffs / escalation**: [Who, when, what to include]
- **Tools**: [Zendesk, Jira, KB, macros — any changes]


## Launch Plan

- [ ] **Phase 1**: [e.g., Internal testing, Week 1]
- [ ] **Phase 2**: [e.g., Beta with select merchants, Week 2-3]
- [ ] **Phase 3**: [e.g., GA, Week 4]

**Support/ops readiness**: What needs to be in place before go-live (training, playbooks, tools, comms)? When is ops ready?

**Rollback**: [How we revert if things go wrong]


## Risks, Dependencies & Open Questions

**Risks**:

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| [Risk description] | High/Med/Low | High/Med/Low | [How we'll address] |

**Dependencies**:

| Dependency | Owner | Status | Risk if Delayed |
|------------|-------|--------|-----------------|
| [What we need] | [Who] | [Status] | [Impact] |

**Open questions**:
- [ ] [Question] *(Owner: [Name])*
- [ ] [Question] *(Owner: [Name])*

*Optional*: What would we cut or delay if we had to protect support capacity or customer trust?

**Review panel** (optional before share): See `02-workflows/document-review-panel.md`. Run through PM, Engineering, Ops, CPO, COO, Product Data Scientist, Zendesk Administrator, Content Strategist, and VP of Product lenses and note any changes made.


## Timeline

| Milestone | Date | Owner | Status |
|-----------|------|-------|--------|
| PRD Complete | [Date] | [Name] | ✅ / 🔄 / ⏳ |
| Design Complete | [Date] | [Name] | ⏳ |
| Engineering Kickoff | [Date] | [Name] | ⏳ |
| Dev Complete | [Date] | [Name] | ⏳ |
| Support/ops ready | [Date] | [Name] | ⏳ |
| Launch | [Date] | [Name] | ⏳ |


## Appendix

- [Links to research, design files, related PRDs, meeting notes]
