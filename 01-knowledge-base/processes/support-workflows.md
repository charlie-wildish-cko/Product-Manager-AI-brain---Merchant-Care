# Customer Support Workflows

## Standard Ticket Handling Process

### 1. Contact Creation

**Support Channels**:

**AI-First (Intercom Fin AI Agent)**:
- Contact initiated in merchant dashboard
- AI Agent attempts resolution first
- Only creates Zendesk ticket if:
  - AI cannot resolve
  - Merchant explicitly requests human agent
  - Issue requires technical investigation
- **Goal**: Maximize AI resolution rate

**Direct to Zendesk**:
1. **Email** (support@checkout.com):
   - Routes directly to Zendesk
   - Ticket created immediately
   - Goes through merchant identification before routing (see below)
   
2. **Dashboard Webform**:
   - Structured form with: Topic, Subject, Payment ID, Description
   - Routes directly to Zendesk
   - Merchant is authenticated (Dashboard login) — no identity check required
   - Provides better context for triage

3. **AM/TAM on behalf of merchant** (~8–10% of annual contact volume):
   - Account Managers (AMs) and Technical Account Managers (TAMs) raise tickets to Care on behalf of their merchants
   - **Current state**: Submitted via email — unstructured; requires manual identification and context extraction
   - **In progress**: A structured AM/TAM submission form is being built (replaces email)
   - **Later 2026**: **Sonar** — internal AI agent in Slack available to all Checkout staff (built by central AI team); will interact with the support intake process and can escalate to Zendesk if needed. Internal-facing only, distinct from Fin (customer-facing)
   - Tickets must be attributed to the merchant represented, not to the AM/TAM themselves — SLA, routing, and org reporting are all based on the merchant identity

**Email Merchant Identification**:

When an email arrives, Zendesk checks the sender's email address against two source systems:

```
Email received in Zendesk
        ↓
Email address checked in Salesforce (CRM) + Dashboard user management
        ↓
        ├── FOUND → Ticket matched to organisation record
        │            → Enriched automatically with merchant data (tier, AM, etc.)
        │            → SLA set based on merchant tier
        │            → Routed to Level 1 queue
        │
        └── NOT FOUND → Ticket drops into Dispatch queue
                         → Manual review by agent to identify merchant
                         → Matched manually before SLA clock starts
```

**The Dispatch queue** handles unidentified email contacts. This is a direct cost driver — agent time is spent on identification before resolution even begins. See [`known-challenges.md`](known-challenges.md) for full detail on why this is hard to solve.

**Auto-routing Logic (identified tickets)**:
- Based on topic/category selection (webform) or parsing (email)
- Priority assignment based on keywords and payment ID
- Merchant tier (Enterprise/Premium/Standard)
- Previous ticket history

**SLA Tracking**:
- Clock starts at Zendesk ticket creation for webform and identified email tickets
- Dispatch queue tickets: SLA clock may not start until merchant is identified
- AI conversations don't count toward SLA until escalated to Zendesk

### 2. Initial Triage

**For Dashboard Webform Tickets**:
- Merchant is already authenticated — identity confirmed
- Topic and payment ID already provided
- Faster context gathering
- Pre-categorized for routing

**For Email Tickets (identified)**:
- Merchant data already enriched from Salesforce/Dashboard lookup
- Parse subject and body for key info
- Look for transaction/payment IDs

**For Dispatch Queue Tickets**:
- Agent must attempt to identify merchant from email content, domain, or referenced payment IDs
- Once identified, match to org record and set SLA/routing manually
- If cannot identify: request merchant confirms identity before proceeding

**Agent Actions**:
- Review ticket details and merchant history
- Verify categorization (integration, payment issue, account, etc.)
- Assign priority based on impact
- Tag with relevant labels
- Check if AI Agent already attempted resolution (for escalations)

**Key Questions**:
- Is this a known issue?
- Does this affect multiple merchants?
- Is there an existing solution in knowledge base?
- Did AI Agent already provide partial resolution?
- Should this go to help docs instead? (deflection opportunity)
- Does this require escalation?

**Root Cause Flagging**:
- If ticket is part of a pattern, flag for product team
- Tag systemic issues for quarterly root cause elimination review

### 3. Investigation & Resolution
**Troubleshooting Steps**:
- [ ] Review merchant account configuration
- [ ] Check transaction logs and error messages
- [ ] Search knowledge base for similar issues
- [ ] Test reproduction steps if applicable
- [ ] Identify root cause

**Resolution Options**:
- Provide solution from knowledge base
- Guide merchant through configuration fix
- Escalate to engineering for bug fix
- Escalate to product for feature request
- Work with account team for commercial issues

### 4. Response to Merchant
**Best Practices**:
- Acknowledge receipt promptly
- Set expectations on resolution timeline
- Explain root cause in merchant-friendly language
- Provide clear next steps
- Include relevant documentation links
- Offer to follow up if needed

### 5. Verification & Closure
- Confirm with merchant that issue is resolved
- Document resolution in ticket for future reference
- Close ticket with appropriate resolution code
- Add to knowledge base if new issue/solution

## Escalation Workflows

### When to Escalate to Engineering

**Criteria**:
- Bug in payment processing or core functionality
- System error or outage
- Issue requires code change or investigation of logs
- Pattern of similar issues indicating systemic problem

**How to Escalate**:
1. Gather complete information (steps to reproduce, error messages, merchant IDs, transaction IDs)
2. File bug report in engineering system (e.g., Jira)
3. Include business impact and priority justification
4. Link related support tickets
5. Set appropriate SLA expectations with merchant

### When to Escalate to Product

**Criteria**:
- Feature request from merchant
- Product limitation blocking merchant use case
- Usability issue with merchant dashboard
- Documentation gap or confusion
- Competitive feature gap

**How to Escalate**:
1. Document merchant's use case and pain point
2. Assess impact (how many merchants affected, revenue at risk)
3. File feature request in product backlog
4. Provide context and merchant feedback
5. Set expectation with merchant that this is a roadmap consideration

### When to Escalate to Leadership

**Criteria**:
- Critical outage affecting multiple merchants
- High-value merchant at risk of churn
- Compliance or security incident
- Reputation risk (social media, press)
- SLA breach with significant impact

**How to Escalate**:
1. Brief summary of situation and impact
2. Steps already taken
3. Specific ask (resources, authority, decision needed)
4. Timeline and urgency

## Specialized Workflows

### Payment Dispute Investigation
1. Review transaction details and merchant evidence
2. Check for fraud indicators
3. Verify merchant followed best practices
4. Compile evidence for dispute response
5. Submit dispute response within deadline
6. Follow up on outcome

### Settlement Inquiry
1. Verify expected settlement date based on terms
2. Check for holds or reserves on account
3. Review recent chargebacks or risk flags
4. Confirm bank details are correct
5. Escalate to finance team if discrepancy found

### Integration Support
1. Review merchant's API requests and responses
2. Check authentication and permissions
3. Verify API version and endpoints used
4. Review webhook configuration
5. Test in sandbox environment
6. Provide code examples or documentation

### Account Access Issues
1. Verify merchant identity and authorization
2. Check user roles and permissions
3. Review recent access logs
4. Reset credentials if appropriate
5. Enable MFA if not already active
6. Document security verification steps

## Quality Assurance

### Ticket Quality Checklist
- [ ] Issue is clearly understood
- [ ] Root cause identified
- [ ] Solution is accurate and complete
- [ ] Response is professional and clear
- [ ] Relevant documentation linked
- [ ] Resolution is documented for future reference
- [ ] Merchant confirmed satisfaction (when possible)

### Common Pitfalls to Avoid
- ❌ Closing ticket without merchant confirmation
- ❌ Providing generic response without understanding issue
- ❌ Missing escalation when issue is beyond support scope
- ❌ Not documenting resolution for future agents
- ❌ Forgetting to follow up on promised timeline
- ❌ Using technical jargon without explanation

## Knowledge Management

### When to Add to Knowledge Base
- New type of issue encountered
- Non-obvious solution discovered
- Common question asked repeatedly
- Complex issue with clear resolution path

### How to Document
- **Title**: Clear, searchable description of issue
- **Symptoms**: How merchant experiences the problem
- **Cause**: Root cause or technical explanation
- **Solution**: Step-by-step resolution
- **Related**: Links to similar issues or documentation


**See also**: [`known-challenges.md`](known-challenges.md) — documents the email authentication gap, Dispatch queue cost, and AI adoption blockers in detail.


**Last Updated**: February 2026  
**Owner**: Charlie Wildish
