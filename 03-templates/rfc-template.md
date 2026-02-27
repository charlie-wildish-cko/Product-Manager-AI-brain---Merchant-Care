# RFC: [Title] - Request for Comment

**Status**: Draft | Under Review | Approved | Rejected  
**Created**: [Date]  
**Author**: Charlie Wildish  
**Reviewers**: [List of people whose input you need]  
**Decision Deadline**: [Date: when decision is needed]


## Summary

> 2-3 sentences explaining what this RFC is about and what decision needs to be made

[Brief, clear explanation that anyone can understand]


## Background & Context

### Problem Statement
[What problem are we trying to solve? Why does it matter?]

### Current State
[How do things work today? What are the pain points?]

### Goals
- [Goal 1]
- [Goal 2]
- [Goal 3]

### Non-Goals
- [What we're explicitly NOT trying to solve]
- [Scope limitations]


## Proposal

### Recommended Approach

[Detailed explanation of the proposed solution]

**How it works**:
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Why this approach**:
- [Benefit 1]
- [Benefit 2]
- [Benefit 3]

### User Experience Changes

**For [User Type 1]**:
- [How their experience changes]

**For [User Type 2]**:
- [How their experience changes]

### Technical Approach

> High-level technical overview

**Architecture**:
[Description or diagram of how components interact]

**Key Components**:
- **[Component 1]**: [What it does]
- **[Component 2]**: [What it does]

**APIs/Interfaces**:
```
[Example API structure or interface definition]
```

**Data Model**:
[Any changes to data structures, databases, etc.]


## Alternative Approaches Considered

### Option 2: [Alternative Name]

**Description**: [How this approach would work]

**Pros**:
- [Advantage 1]
- [Advantage 2]

**Cons**:
- [Disadvantage 1]
- [Disadvantage 2]

**Why not chosen**: [Rationale for rejecting this option]


### Option 3: [Another Alternative]

**Description**: [How this would work]

**Pros**:
- [Advantage 1]
- [Advantage 2]

**Cons**:
- [Disadvantage 1]
- [Disadvantage 2]

**Why not chosen**: [Rationale]


### Option 4: Do Nothing

**Impact of not solving this**:
- [Consequence 1]
- [Consequence 2]
- [Opportunity cost]


## Comparison Matrix

| Criteria | Recommended | Option 2 | Option 3 | Do Nothing |
|----------|-------------|----------|----------|------------|
| **User Impact** | [Rating/Description] | [Rating] | [Rating] | [Rating] |
| **Effort** | [S/M/L or weeks] | [Effort] | [Effort] | [None] |
| **Risk** | [Low/Med/High] | [Risk] | [Risk] | [High] |
| **Scalability** | [Assessment] | [Assessment] | [Assessment] | [Assessment] |
| **Maintenance** | [Ongoing cost] | [Cost] | [Cost] | [Cost] |
| **Time to Value** | [How quickly benefits realized] | [Time] | [Time] | [N/A] |


## Trade-offs & Implications

### Technical Trade-offs
- [Trade-off description and why it's acceptable]
- [Another trade-off]

### Business Trade-offs
- [What we're giving up to get the benefit]
- [Another trade-off]

### User Experience Trade-offs
- [Any compromises to UX and justification]


## Impact Analysis

### Who is Impacted?

**Merchants**:
- [How merchants are affected]
- [Migration needed? Backwards compatible?]

**Internal Teams**:
- **Engineering**: [What changes for engineering]
- **Support**: [Training needed, process changes]
- **Operations**: [Operational impact]
- **Sales**: [How this affects sales process]

### Breaking Changes
- [ ] This is a breaking change requiring merchant updates
- [ ] This is backward compatible
- [ ] This requires data migration

**If breaking**:
- **Migration path**: [How existing users will transition]
- **Timeline**: [How much notice, deprecation schedule]
- **Communication plan**: [How we'll notify affected parties]


## Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation Strategy |
|------|-----------|--------|-------------------|
| [Risk description] | High/Med/Low | High/Med/Low | [How we'll reduce or address] |
| [Risk description] | High/Med/Low | High/Med/Low | [Mitigation] |
| [Risk description] | High/Med/Low | High/Med/Low | [Mitigation] |


## Success Metrics

### How We'll Know This Is Working

| Metric | Current | Target | Timeline |
|--------|---------|--------|----------|
| [Metric name] | [Baseline] | [Goal] | [When we expect to hit it] |
| [Metric name] | [Baseline] | [Goal] | [Timeline] |

### Leading Indicators
- [Early signs of success we can measure during implementation]


## Implementation Plan

### Phase 1: [Phase Name]
- **Scope**: [What's included]
- **Timeline**: [Duration]
- **Deliverables**: [What will be done]
- **Success Criteria**: [How we know it's complete]

### Phase 2: [Phase Name]
- **Scope**: [What's included]
- **Timeline**: [Duration]
- **Deliverables**: [What will be done]
- **Success Criteria**: [How we know it's complete]

### Phase 3: [Phase Name]
- **Scope**: [What's included]
- **Timeline**: [Duration]
- **Deliverables**: [What will be done]
- **Success Criteria**: [How we know it's complete]


## Dependencies

### Technical Dependencies
- [ ] [System or service we depend on]
- [ ] [Library or framework needed]
- [ ] [Infrastructure requirement]

### Team Dependencies
- [ ] [What we need from team X]
- [ ] [What we need from team Y]

### External Dependencies
- [ ] [Third-party vendor or service]
- [ ] [Legal or compliance review]


## Open Questions

> Questions that need answering before we can proceed

1. **Q**: [Question]
   - **Why it matters**: [Impact on decision]
   - **Who can answer**: [Person or team]
   - **Deadline**: [When we need the answer]

2. **Q**: [Another question]
   - **Why it matters**: [Impact]
   - **Who can answer**: [Person/team]
   - **Deadline**: [Date]


## Security & Compliance Considerations

### Security Review Needed?
- [ ] Yes - [What needs review]
- [ ] No - [Why not required]

### Compliance Impact
- **PCI-DSS**: [Impact or none]
- **GDPR/Privacy**: [Impact or none]
- **PSD2/SCA**: [Impact or none]
- **Other**: [Any other regulations affected]


## Rollout & Communication Plan

### Internal Communication
- [ ] Engineering team briefing
- [ ] Support team training
- [ ] Sales enablement materials
- [ ] Operations runbook updates

### External Communication
- [ ] Merchant notification (email, dashboard banner, etc.)
- [ ] Documentation updates
- [ ] API changelog entry
- [ ] Developer blog post

### Rollout Strategy
- [ ] **Dark launch**: Feature complete but not exposed
- [ ] **Internal beta**: Test with internal users
- [ ] **Limited beta**: [X]% of merchants or specific segment
- [ ] **Gradual rollout**: Increase to 25% → 50% → 100%
- [ ] **Full launch**: Available to all immediately

### Feature Flags
- [ ] [Flag name] - [Purpose]

### Rollback Plan
[How we can revert if things go wrong]


## Timeline & Milestones

| Milestone | Target Date | Owner | Status |
|-----------|-------------|-------|--------|
| RFC feedback period closes | [Date] | Charlie | ⏳ |
| Decision made | [Date] | [Decision maker] | ⏳ |
| Design complete | [Date] | [Designer] | ⏳ |
| Implementation starts | [Date] | [Eng lead] | ⏳ |
| Internal testing | [Date] | [QA] | ⏳ |
| Beta launch | [Date] | [PM] | ⏳ |
| GA launch | [Date] | [PM] | ⏳ |


## Feedback & Discussion

### Questions for Reviewers

1. [Specific question you want feedback on]
2. [Another area where you need input]
3. [Decision point where you want opinions]

### How to Provide Feedback

- **Deadline**: [Date]
- **Where**: [Comment on this doc, Slack channel, meeting, etc.]
- **What we need**: [Type of feedback - technical review, business input, user perspective, etc.]


## Decision

> This section completed after review period

**Date**: [Date]  
**Decision**: [Approved / Approved with modifications / Rejected / Deferred]  
**Decision Maker**: [Name]

**Rationale**: [Why this decision was made]

**Modifications** (if applicable):
- [Change to original proposal]
- [Another modification]

**Next Steps**:
- [ ] [Action item with owner and date]
- [ ] [Another action item]


## Appendix

### Related Documents
- [Link to related PRD]
- [Link to technical spec]
- [Link to research or data]

### Glossary
- **[Term]**: [Definition]
- **[Term]**: [Definition]

### References
- [Link to relevant documentation]
- [Link to competitive analysis]
- [Link to user research]
