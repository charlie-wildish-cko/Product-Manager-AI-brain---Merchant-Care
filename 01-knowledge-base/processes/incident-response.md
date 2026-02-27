# Incident Response Process

## Incident Severity Levels

### SEV 1 - Critical
**Definition**: Complete service outage or critical functionality unavailable

**Examples**:
- Payment processing is down
- Merchants cannot access dashboard
- Data breach or security incident
- Compliance violation

**Response**:
- Immediate response required
- All hands on deck
- Executive notification
- Regular status updates to affected merchants
- Post-incident review required

### SEV 2 - High
**Definition**: Major degradation of service affecting significant portion of users

**Examples**:
- Specific payment method failing
- Slow response times causing timeouts
- Regional outage
- High decline rates

**Response**:
- Response within 30 minutes
- Dedicated incident team
- Status page update
- Stakeholder notification
- Post-incident review recommended

### SEV 3 - Medium
**Definition**: Minor service degradation with workaround available

**Examples**:
- Dashboard feature not working
- Reporting delays
- Non-critical API endpoint errors
- Documentation issues

**Response**:
- Response within 2 hours
- Standard escalation process
- Internal notification
- Fix scheduled based on priority

## Incident Response Workflow

### 1. Detection & Alert
**How incidents are identified**:
- Automated monitoring alerts
- Merchant reports via support tickets
- Internal team discovery
- Social media mentions

**Initial Actions**:
- Acknowledge alert immediately
- Confirm incident is real (not false positive)
- Assess initial severity
- Page on-call engineer if SEV 1 or 2

### 2. Incident Declaration
**Who can declare**:
- Support team lead
- Engineering on-call
- Product management
- Operations team

**Declaration includes**:
- Severity level
- Brief description
- Estimated impact (number of merchants, transaction volume)
- Initial response team

### 3. Communication

**Internal Communication**:
- Create dedicated incident channel (e.g., Slack)
- Notify relevant stakeholders based on severity
- Assign incident commander (owns coordination)
- Designate communications lead

**External Communication**:
- Update status page with incident details
- Proactive outreach to affected merchants (if identifiable)
- Prepare merchant-facing messaging
- Social media response if needed

**Communication Cadence**:
- SEV 1: Every 30 minutes until resolved
- SEV 2: Every 1-2 hours
- SEV 3: At major milestones

### 4. Investigation & Resolution

**Incident Commander Responsibilities**:
- Coordinate response team
- Track investigation progress
- Make decisions on trade-offs
- Communicate status updates
- Document timeline of events

**Engineering Team**:
- Diagnose root cause
- Implement fix or workaround
- Test solution
- Deploy to production
- Monitor for stability

**Support Team**:
- Handle incoming merchant inquiries
- Provide consistent messaging
- Track affected merchants
- Escalate patterns or new information

### 5. Verification
- Confirm systems are fully operational
- Verify merchant transactions processing normally
- Check monitoring and alerting systems
- Test end-to-end flows

### 6. Stand Down
**When to close incident**:
- Root cause identified and fixed
- System stable for reasonable time (e.g., 1 hour for SEV 1)
- No recurring issues detected
- Monitoring shows normal behavior

**Close-out actions**:
- Final status page update
- Thank response team
- Schedule post-incident review
- Close incident channel (but preserve history)

### 7. Post-Incident Review

**Timing**: Within 48 hours for SEV 1, within 1 week for SEV 2

**Attendees**:
- Incident response team
- Product management
- Leadership (for SEV 1)
- Customer success (if merchant impact)

**Review Structure**:
1. **Timeline**: Detailed sequence of events
2. **Impact**: Merchants affected, duration, financial impact
3. **Root Cause**: Technical explanation of what went wrong
4. **Contributing Factors**: Why this wasn't caught earlier
5. **What Went Well**: Effective responses and processes
6. **What Could Improve**: Gaps and opportunities
7. **Action Items**: Preventive measures with owners and deadlines

**No Blame Culture**: Focus on systems and processes, not individuals

## Support Team's Role in Incidents

### During Active Incident

**Do**:
✅ Route new tickets related to incident to incident channel
✅ Use standardized response template
✅ Reassure merchants that team is actively working on it
✅ Provide realistic timelines based on commander's updates
✅ Track and report patterns or new symptoms
✅ Escalate VIP merchants or at-risk accounts

**Don't**:
❌ Speculate on root cause or timeline
❌ Provide contradictory information
❌ Promise specific resolution times
❌ Dismiss merchant concerns
❌ Share overly technical details publicly

### After Incident Resolution

**Immediate**:
- Respond to all pending related tickets with resolution
- Verify merchants are back to normal operation
- Monitor for any residual issues

**Follow-up**:
- Proactive outreach to significantly impacted merchants
- Offer account review or technical consultation if appropriate
- Document learnings in knowledge base
- Update documentation if process changed

## Response Templates

### Status Page Update Template
```
[TITLE]: [Brief description of issue]

We are currently investigating an issue affecting [specific functionality]. 

Impact: [Description of what's not working]

Affected services: [List]

We are actively working on a resolution and will provide updates every [timeframe].

Last updated: [Timestamp]
```

### Merchant Communication Template
```
Subject: [Update] Service Issue - [Date]

Dear [Merchant],

We're aware of an issue affecting [functionality] and are working on a resolution.

What's happening: [Simple explanation]

Impact to you: [Specific impact on their business]

What we're doing: [High-level action being taken]

Timeline: [Expected resolution or next update]

We apologize for any inconvenience. If you have urgent questions, please reply to this email or contact [support channel].

Thank you for your patience.

[Team/Name]
```


**Last Updated**: [Date]
**Owner**: Charlie Wildish
