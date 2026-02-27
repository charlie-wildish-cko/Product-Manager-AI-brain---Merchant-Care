# Incident Postmortem - [Incident Name/Description]

**Incident Date**: [Date of incident]  
**Postmortem Date**: [Date of this document]  
**Severity**: SEV 1 | SEV 2 | SEV 3  
**Incident Duration**: [X hours/days]  
**Status**: Draft | Under Review | Final

**Prepared By**: [Name]  
**Attendees**: [List of people who participated in postmortem]


## TL;DR

> 2-3 sentence summary of what happened, impact, and resolution

[Brief summary that anyone can understand]


## Incident Summary

### What Happened?
[Clear, concise description of the incident in simple language]

### When Did It Happen?
- **Incident Start**: [Date & Time with timezone]
- **Detected**: [Date & Time]
- **Resolved**: [Date & Time]
- **Total Duration**: [Hours/Minutes]

### Who Was Affected?
- **Merchants Impacted**: [Number or percentage]
- **Users Impacted**: [Number or description]
- **Regions/Segments**: [Which groups were affected]

### Impact
- **Business Impact**: [Revenue lost, transactions blocked, etc.]
- **Customer Impact**: [How merchants/users were affected]
- **Reputation Impact**: [Social media, press coverage, etc.]
- **SLA Breaches**: [Any SLA violations]


## Timeline of Events

> Detailed chronological timeline - all times in [timezone]

| Time | Event | Who |
|------|-------|-----|
| [HH:MM] | [What happened - be specific] | [Person/System] |
| [HH:MM] | [Next event] | [Person/System] |
| [HH:MM] | [Event] | [Person/System] |
| [HH:MM] | [Event] | [Person/System] |
| [HH:MM] | **Incident declared** | [Who] |
| [HH:MM] | [Response action] | [Who] |
| [HH:MM] | [Event] | [Person/System] |
| [HH:MM] | [Root cause identified] | [Who] |
| [HH:MM] | [Fix implemented] | [Who] |
| [HH:MM] | [Verification] | [Who] |
| [HH:MM] | **Incident resolved** | [Who] |
| [HH:MM] | [Post-incident monitoring] | [Who] |


## Root Cause Analysis

### What Was the Root Cause?

[Detailed technical explanation of what went wrong]

### Why Did It Happen?

**Immediate Cause**:
[Direct trigger - e.g., "Deployment of version X.Y.Z"]

**Contributing Factors**:
1. **[Factor 1]**: [e.g. No automated rollback]
2. **[Factor 2]**: [e.g. Insufficient load testing]
3. **[Factor 3]**: [e.g. Monitoring alert threshold too high]

### Five Whys Analysis

1. **Why did [incident] happen?**
   - [Answer]

2. **Why [answer from previous why]?**
   - [Answer]

3. **Why [answer from previous why]?**
   - [Answer]

4. **Why [answer from previous why]?**
   - [Answer]

5. **Why [answer from previous why]?**
   - [Root cause]


## Detection & Response

### How Was It Detected?

- [ ] Automated monitoring/alerting
- [ ] Customer report
- [ ] Internal team discovery
- [ ] Social media
- [ ] Other: [Specify]

**Details**: [How we found out about the issue]

### Detection Delay

- **Incident started**: [Time]
- **First detected**: [Time]
- **Detection delay**: [Minutes/Hours]

**Why the delay**: [Explanation if there was a gap]

### Response Effectiveness

**What Went Well**:
- ✅ [Thing that worked well in the response]
- ✅ [Another positive aspect]
- ✅ [Another positive]

**What Could Be Improved**:
- ⚠️ [Thing that didn't go well]
- ⚠️ [Another area for improvement]
- ⚠️ [Another gap]


## Impact Details

### Merchant Impact

**Number of Merchants Affected**: [#] ([%] of total)

**Merchant Segments**:
- [Segment name]: [# affected]
- [Segment name]: [# affected]

**Top Affected Merchants**:
| Merchant | Monthly Volume | Impact Description |
|----------|---------------|-------------------|
| [Name/ID] | [Amount] | [How they were affected] |
| [Name/ID] | [Amount] | [Impact] |

### Transaction Impact

- **Failed Transactions**: [#]
- **Transaction Volume Lost**: [Amount]
- **Estimated Revenue Impact**: [Currency amount]
- **Transaction Types Affected**: [Which types - authorizations, captures, refunds, etc.]

### Support Impact

- **Tickets Created**: [#]
- **Peak Ticket Rate**: [# per hour]
- **Support Team Hours**: [Hours spent responding]

### System Impact

- **Systems Affected**: [List]
- **Error Rate**: [%]
- **Uptime**: [% during incident]


## Resolution

### How Was It Fixed?

[Detailed explanation of the fix applied]

### Why Did the Fix Work?

[Technical explanation]

### Temporary vs. Permanent Fix

- **Immediate mitigation**: [What we did to stop the bleeding]
- **Permanent solution**: [What we are doing to truly fix it]

### Verification

[How we confirmed the issue was resolved]


## Action Items

> Concrete, actionable items with owners and deadlines - tracked in [system]

### Prevent Recurrence (P0 - Critical)

- [ ] **[Action item]**
  - **Owner**: [Name]
  - **Deadline**: [Date]
  - **Status**: Not Started | In Progress | Complete
  - **Tracking**: [Link to ticket/task]

- [ ] **[Action item]**
  - **Owner**: [Name]
  - **Deadline**: [Date]
  - **Status**: [Status]
  - **Tracking**: [Link]

### Improve Detection (P1 - High Priority)

- [ ] **[Action item]**
  - **Owner**: [Name]
  - **Deadline**: [Date]
  - **Status**: [Status]
  - **Tracking**: [Link]

### Improve Response (P1 - High Priority)

- [ ] **[Action item]**
  - **Owner**: [Name]
  - **Deadline**: [Date]
  - **Status**: [Status]
  - **Tracking**: [Link]

### Process Improvements (P2 - Medium Priority)

- [ ] **[Action item]**
  - **Owner**: [Name]
  - **Deadline**: [Date]
  - **Status**: [Status]
  - **Tracking**: [Link]

### Documentation Updates (P2)

- [ ] **[Action item]**
  - **Owner**: [Name]
  - **Deadline**: [Date]
  - **Status**: [Status]
  - **Tracking**: [Link]


## Lessons Learned

### Technical Lessons

1. **[Lesson]**
   - **What we learned**: [Description]
   - **How we will apply it**: [Action]

2. **[Lesson]**
   - **What we learned**: [Description]
   - **How we will apply it**: [Action]

### Process Lessons

1. **[Lesson]**
   - **What we learned**: [Description]
   - **How we will apply it**: [Action]

### Operational Lessons

1. **[Lesson]**
   - **What we learned**: [Description]
   - **How we will apply it**: [Action]


## Communication

### Internal Communication

**During Incident**:
- **[Internal comms]**: [How we communicated internally]
- **[Frequency]**: [How often we updated]
- **[Channels]**: [Where we communicated]

**What worked**: [Effective aspects]
**What did not**: [Gaps or issues]

### External Communication

**During Incident**:
- **Status page updated**: [Yes/No, when]
- **Proactive outreach**: [Which merchants contacted]
- **Public communication**: [Social media, blog, etc.]

**Post-Incident**:
- [ ] Affected merchants notified
- [ ] Public postmortem published
- [ ] Support team briefed
- [ ] Leadership updated

**Merchant Communication Sample**:
[Include copy of communication sent to merchants]


## Preventive Measures

### Short-term (Within 1 Month)

1. [Specific measure to prevent recurrence]
2. [Another preventive measure]
3. [Another measure]

### Long-term (Within Quarter)

1. [Larger architectural or process change]
2. [Another long-term improvement]

### Monitoring & Alerting Improvements

- [New alert to add]
- [Threshold to adjust]
- [Dashboard to create]

### Testing Improvements

- [Test case to add]
- [Testing process to implement]
- [Load testing enhancement]


## What Went Well

> It's important to recognize things that worked! No blame culture.

1. **[Thing that went well]**
   - **Why it worked**: [Explanation]
   - **How to reinforce**: [Action]

2. **[Another positive]**
   - **Why it worked**: [Explanation]
   - **How to reinforce**: [Action]

3. **[Team member recognition]**
   - **What they did well**: [Description]


## Related Incidents

### Similar Past Incidents
- **[Date]**: [Brief description and link]
- **[Date]**: [Brief description and link]

**Pattern**: [Are these related? Do we see a trend?]


## Appendix

### Technical Details

[Detailed technical information - logs, stack traces, system architecture diagrams, etc.]

### Metrics & Graphs

[Charts showing system behavior during incident]

### Links

- **Incident Channel**: [Slack channel link]
- **Status Page Updates**: [Link]
- **Engineering Ticket**: [Link to bug/issue]
- **Action Item Tracking**: [Link to project board]
- **Recorded Meeting**: [Link if postmortem was recorded]

### Glossary

[Define any technical terms used in this document]


**Questions or corrections?** Please comment or reach out to [owner]


## Sign-off

This postmortem has been reviewed and approved by:

- [ ] Incident Commander: [Name] - [Date]
- [ ] Engineering Lead: [Name] - [Date]
- [ ] Product Manager: [Name] - [Date]
- [ ] Leadership: [Name] - [Date]
