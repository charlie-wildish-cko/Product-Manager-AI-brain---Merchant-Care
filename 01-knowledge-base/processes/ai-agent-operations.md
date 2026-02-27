# AI Agent Operations - Intercom Fin

## AI Agent Landscape

There are two AI agents in the support ecosystem — they serve different audiences and are built by different teams:

| Agent | Audience | Channel | Built by | Status |
| --- | --- | --- | --- | --- |
| **Fin** (Intercom) | Merchants (external) | Dashboard, email (in development) | Charlie's team / Intercom platform | Live |
| **Sonar** | All Checkout staff (internal) | Slack | Central AI team | Planned for later 2026 |

This document covers Fin only. Sonar is tracked in [`teams.md`](../teams.md) and [`support-workflows.md`](support-workflows.md).


## Overview

The Intercom Fin AI Agent is our AI-first support channel, available in the merchant dashboard. It attempts to resolve merchant queries without human agent involvement, creating tickets in Zendesk only when escalation is necessary.

> **Key constraint**: Fin is in the authenticated Dashboard. The majority of merchant contacts arrive via email, which is unauthenticated. An approach to close this gap for Premium and Enterprise email is now defined and in development. See [`known-challenges.md`](known-challenges.md) for context and [`fin-email-auth-data-policy-prd.md`](../../04-active-work/roadmap-items/fin-email-auth-data-policy-prd.md) for the full solution design.

## How It Works

### 1. Merchant Initiates Contact
- **Location**: Merchant dashboard (Help/Support section)
- **Interface**: Chat-style conversation
- **Available**: 24/7 for all merchants

### 2. AI Resolution Attempt
**The AI Agent**:
- Understands merchant's question in natural language
- Searches its knowledge base — the three public documentation sites:
  - **support.checkout.com** (FAQs and help articles)
  - **checkout.com/docs** (technical and integration documentation)
  - **api-reference.checkout.com** (API reference)
- Provides answers with links to relevant documentation
- Can handle follow-up questions
- Confirms resolution with merchant

> **Key implication**: Fin can only answer questions that are covered by content on these three sites. If the answer doesn't exist there — or exists but is unclear — Fin will fail to contain the query and escalate to a human agent. Improving Fin's AI resolution rate is therefore directly tied to improving the quality and coverage of these sites.

**Common Successful Resolutions**:
- Account/password questions
- General product questions
- API documentation lookups
- Transaction status inquiries
- Integration guidance
- Billing/invoice questions

### 3. Escalation to Human Agent

**AI Agent escalates when**:
- Cannot find confident answer
- Issue requires transaction investigation
- Merchant explicitly requests human agent
- Issue flagged as requiring human judgment
- Multiple failed resolution attempts

**Escalation Process**:
1. AI asks merchant to describe issue for human agent
2. Collects any additional context
3. Creates Zendesk ticket with:
   - Full conversation transcript
   - Merchant information
   - AI confidence scores on attempted answers
   - Suggested routing category
4. Informs merchant of ticket number and expected response time

### 4. Handoff Context

**What Human Agents See**:
- Complete AI conversation history
- What the AI attempted to answer
- Why the AI escalated (confidence threshold, explicit request, etc.)
- Merchant sentiment/urgency indicators
- Suggested articles that were provided

**Benefits for Agents**:
- Don't repeat what AI already tried
- Understand merchant's journey
- Faster resolution with context


## Key Metrics

### AI Resolution Rate
- **Definition**: % of AI conversations resolved without reaching a human agent
- **Target**: Continuously increasing
- **Measured By**:
  - Overall AI resolution rate
  - Containment by topic/category
  - Containment by merchant segment
  - Containment by complexity

**Current Performance**: [Track actual numbers here]

### AI Escalation Reasons
Track why AI escalates to understand improvement opportunities:
- "No confident answer found" (knowledge gap)
- "Requires transaction investigation" (needs tools)
- "Merchant requested human" (trust/preference)
- "Multiple failed attempts" (AI ineffective)
- "Policy exception needed" (needs human judgment)

### Resolution Quality
- **CSAT for AI-resolved conversations**: [Track score]
- **Reopen rate**: How often AI resolutions lead to follow-up contacts
- **Accuracy**: Merchant validation of AI answers


## Improving AI Performance

### 1. Knowledge Base Expansion

Fin's knowledge base **is** the three public documentation sites. There is no separate internal knowledge base to maintain — improving Fin means improving content on these sites.

**Ownership**: Content team. Charlie's contact: Content Strategist. The content team's 2026 roadmap is documented in [`content-strategy-2026.md`](../strategy/content-strategy-2026.md) — it covers the proactive guide programme, reactive content improvements, the agent/customer feedback loop, and a target Fin resolution rate of ~70%.

**When to request new or updated content**:
- Repeated questions Fin cannot answer (escalation pattern in Zendesk)
- High-volume ticket categories with no corresponding help article
- New features or product changes launching — content must be live before launch
- Outdated articles that no longer reflect current product behaviour

**How to make content more effective for Fin**:
- Clear, direct answers near the top of articles (Fin retrieves by relevance)
- Use the language merchants actually use in their questions
- Avoid vague or overly generic articles — specificity helps Fin match queries
- Include examples, error codes, and step-by-step guidance
- Link related articles so Fin can surface connected content

**Process for requesting content changes**:
1. Identify gap from Zendesk escalation data or Fin conversation analysis
2. Quantify impact (tickets/month on this topic)
3. Raise with Content Strategist — frame as "X tickets/month on this topic, no article covering it"
4. Track article publication and monitor AI resolution rate improvement

### 2. Training Data & Conversation Analysis

The **Content team** runs a **monthly Fin AI conversation analysis** to identify where the AI is underperforming. Charlie's direct contact for this is the **Content Strategist**.

**The monthly analysis covers**:
- Questions AI should have answered but didn't
- Incorrect or low-confidence answers
- Missing or outdated knowledge base content
- Topics with high escalation rates

**Charlie's role in this process**:
- Review analysis findings with Content Strategist
- Prioritise content gaps by ticket volume and contact rate impact
- Identify gaps that require product fixes (not just content updates)
- Feed findings into roadmap and sprint planning

**Feedback Loop**:
- Monthly: Content team conversation analysis → review with Content Strategist
- Ongoing: Escalation pattern monitoring in Zendesk
- Quarterly: Knowledge base content audit

### 3. Conversation Design

**Optimize for**:
- Clear intent identification
- Effective follow-up questions
- Appropriate escalation timing (not too early, not too late)
- Smooth handoff to human agents

### 4. Topic Coverage Strategy

**Prioritize topics by**:
- Volume (most frequent questions)
- Containment rate (where AI struggles)
- Impact (high-value use cases)
- Effort (low-hanging fruit first)


## Success Patterns

### What Works Well for AI

**Factual Questions**:
- API endpoint specifications
- Account settings/configuration
- Product capabilities and features
- Pricing and billing information
- Integration steps and requirements

**Navigational Help**:
- "Where do I find X?"
- "How do I access Y?"
- Dashboard guidance

**Status Inquiries**:
- Transaction status (if API lookup enabled)
- Settlement schedules
- Account verification status

### What Requires Human Agents

**Investigation Required**:
- Specific transaction failures needing logs
- Account-specific configuration issues
- Discrepancies needing reconciliation

**Judgment Calls**:
- Policy exceptions
- Escalations or complaints
- Relationship management
- Custom solutions or workarounds

**Sensitive Issues**:
- Fraud or security concerns
- Compliance questions
- Legal or regulatory inquiries


## Monitoring & Alerting

### Daily Monitoring
- [ ] AI AI resolution rate vs. baseline
- [ ] Escalation volume and reasons
- [ ] CSAT for AI conversations
- [ ] Response time for AI answers

### Weekly Analysis
- [ ] Containment rate by category
- [ ] Top escalation reasons
- [ ] Knowledge gaps identified
- [ ] Merchant feedback themes

### Monthly Deep Dive
- [ ] Trend analysis (AI resolution rate improving?)
- [ ] ROI calculation (contacts deflected × cost per contact)
- [ ] Knowledge base effectiveness
- [ ] Feature requests for AI capabilities


## Impact on North Star Metrics

### Contact Rate Reduction
**AI Agent impact**:
- Each AI-resolved conversation = avoided Zendesk ticket
- Directly reduces contacts per 1M transactions
- Scales automatically with transaction volume

**Measurement**:
- Track: AI conversations per 1M transactions
- Compare: AI AI resolution rate × conversations = deflected tickets

### Cost Per Contact Reduction
**Cost comparison**:
- AI resolution: ~$0.25 per conversation
- Human agent email: ~$10 per ticket
- Savings: ~$9.75 per AI-contained conversation

**ROI Calculation**:
- Monthly AI resolutions × Cost savings = Monthly savings
- Justify investment in AI improvements


## 2027 B2C Considerations

### Scaling for Consumer Volume

**Differences from B2B**:
- Much higher volume (consumers vs. merchants)
- Simpler questions (typically)
- Lower average transaction value
- Higher expectations for instant resolution

**Preparation Needed**:
- Expand knowledge base for consumer scenarios
- Optimize for common consumer payment issues
- Multi-language support
- Integration with mobile app
- Phone channel AI (voice bot)

### Consumer-Specific Topics
- Payment method questions
- Order/transaction disputes
- Refund status
- Account access issues
- Basic troubleshooting


## Best Practices

### For Product Managers

**When building new features**:
- [ ] Update knowledge base BEFORE launch
- [ ] Test AI Agent can answer common questions
- [ ] Create help articles for anticipated questions
- [ ] Monitor AI performance post-launch

**When seeing escalation spikes**:
- [ ] Review escalation reasons
- [ ] Identify knowledge gaps
- [ ] Create/update relevant articles
- [ ] Re-test AI performance

### For Support Team

**Leveraging AI insights**:
- Review AI conversation transcripts for patterns
- Identify confusing product areas
- Suggest knowledge base improvements
- Provide feedback on AI accuracy

**When handling escalations**:
- Don't repeat what AI already tried
- Build on AI-provided context
- Flag cases where AI should have succeeded


## Channel Constraints & Adoption Challenges

### Authentication Gap — Approach Defined, In Development

Fin lives in the authenticated Dashboard. Premium and Enterprise merchant ops teams predominantly contact us via **email**. The approach to closing the authentication gap on email is now defined and in development. Email is a dedicated channel entitlement for Premium and Enterprise only; Standard merchants are directed to Dashboard and AI Agent.

| Channel | Authentication | Fin Available | Payment Data Returnable |
|---------|---------------|--------------|------------------------|
| Dashboard (Fin) | ✅ Yes | ✅ Yes | ✅ Yes |
| Email | ❌ No | ❌ Not deployed | ❌ No |
| Dashboard Webform | ✅ Yes | ❌ Not currently | ✅ Possible |

**Chosen approach (in development)**: Org identification (Salesforce/Dashboard match, or domain mapping as fallback) acts as the data gate — consistent with what agents already do today. OTP email verification is available as optional step-up. CC-based exclusion rules apply (no Fin involvement if @checkout.com is CC'd, or >2 people CC'd). Standard response = payment summary + Dashboard deep link. PANs and consumer PII are never returned over email.

> Full detail: [`fin-email-auth-data-policy-prd.md`](../../04-active-work/roadmap-items/fin-email-auth-data-policy-prd.md)

**Background**: A pilot on Tier 3 (Standard) email found that generic/FAQ answers could be automated, but payment-specific responses could not be returned safely. The majority of merchant queries are payment-specific. Standard email is being deprecated — email AI work is scoped to Premium and Enterprise only.

See [`known-challenges.md`](known-challenges.md) for context on how this challenge was framed.


## Future Enhancements Roadmap

**In progress**:
- [ ] **Fin involvement rate programme — 80% by end 2026** — orchestrates all channel levers (email, Webform, chat adoption) to hit the 80% involvement rate target — see [`fin-involvement-rate-prd.md`](../../04-active-work/roadmap-items/fin-involvement-rate-prd.md)
- [ ] Fin on email (Premium/Enterprise) — authentication gap solution, org identification + data policy — see [`fin-email-auth-data-policy-prd.md`](../../04-active-work/roadmap-items/fin-email-auth-data-policy-prd.md)
- [ ] Zendesk org domain mapping — fallback identification for email — see [`zendesk-org-domain-mapping-prd.md`](../../04-active-work/roadmap-items/zendesk-org-domain-mapping-prd.md)

**Near-term (Next 6 months)**:
- [ ] **Sonar** (central AI team) — internal Slack AI agent available to all Checkout staff; answers queries and escalates to Zendesk where needed. Relevant to Care because it will interact with the support intake process and will affect internal contact volume (including AM/TAM submissions). Not a Fin dependency. See [`support-workflows.md`](support-workflows.md).
- [ ] Expand topic coverage for top escalation categories
- [ ] Improve transaction lookup capabilities
- [ ] Better sentiment detection for urgent issues
- [ ] Enhanced handoff experience

**Medium-term (6-12 months)**:
- [ ] Proactive outreach for known issues
- [ ] Predictive routing to specialists
- [ ] Multi-language support
- [ ] Voice AI integration

**Long-term (2027+)**:
- [ ] Full B2C consumer support
- [ ] Mobile-optimized AI experience
- [ ] Advanced personalization
- [ ] Automated issue resolution (beyond answers)


**Last Updated**: February 2026  
**Owner**: Charlie Wildish  
**System**: Intercom Fin AI Agent
