# Integrated Analysis Workflow

> How to combine data from multiple sources for comprehensive analysis and decision-making.

## Overview

This workflow helps you efficiently gather data from all your sources (BigQuery, Airtable, Confluence, GitHub, Google Drive) and synthesize it for PM decisions.


## Workflow 1: Weekly Ticket Analysis with Context

### Objective
Analyze support tickets with customer research and technical context to identify actionable opportunities.

### Steps

#### 1. Pull Ticket Data (BigQuery)
**Time: 10 minutes**

Run key queries:
- [ ] Weekly ticket volume and trends
- [ ] Top categories breakdown
- [ ] Channel distribution (email, webform, AI escalations)
- [ ] AI resolution rate
- [ ] Contact rate per 1M transactions

**Export**: Save results as CSV or copy to Google Sheets

#### 2. Gather Customer Context (Airtable)
**Time: 5 minutes**

For top ticket categories:
- [ ] Search for related feature requests
- [ ] Find relevant customer quotes
- [ ] Check research findings on those topics
- [ ] Note merchant segments affected

**Export**: Copy relevant records/quotes

#### 3. Check Technical Context (GitHub)
**Time: 5 minutes**

- [ ] Search for related bugs or issues
- [ ] Check recent fixes or PRs in those areas
- [ ] Note any known technical constraints
- [ ] Review issue comments for engineering perspective

**Document**: Key findings

#### 4. Review Past Work (Confluence)
**Time: 5 minutes**

- [ ] Search for previous analysis of similar issues
- [ ] Check documented known issues or workarounds
- [ ] Review meeting notes for related decisions

**Reference**: Links to relevant pages

#### 5. Synthesize with Claude
**Time: 15 minutes**

Bring all data to Claude:

```
"I'm doing weekly ticket analysis. Here's what I found:

TICKET DATA (from BigQuery):
- 450 tickets this week, up 15% from last week
- Top categories: [paste data]
- AI resolution rate: 62% (down from 68%)

CUSTOMER RESEARCH (from Airtable):
- [paste relevant feedback and quotes]

TECHNICAL CONTEXT (from GitHub):
- [paste related issues or constraints]

Help me:
1. Identify the top 3 patterns
2. Determine root causes
3. Prioritize opportunities for contact reduction
4. Draft recommendations with expected impact"
```

#### 6. Document Analysis
**Time: 10 minutes**

Use: `03-templates/ticket-analysis-template.md`

Save to: `04-active-work/investigations/weekly-analysis-[date].md`


## Workflow 2: Feature Prioritization with Data

### Objective
Make data-driven prioritization decisions using customer, support, and technical data.

### Steps

#### 1. List Candidates
**Time: 5 minutes**

From various sources:
- Feature requests from Airtable
- High-volume ticket categories from BigQuery
- Customer feedback themes
- Technical debt items from GitHub

**Create list**: Potential features/improvements

#### 2. Gather Impact Data
**Time: 20 minutes**

For each candidate:

**Support Impact (BigQuery)**:
- [ ] How many tickets per month?
- [ ] What % of total volume?
- [ ] Trending up or down?
- [ ] Cost per contact × volume = monthly cost

**Customer Demand (Airtable)**:
- [ ] How many merchants requested?
- [ ] Which segments?
- [ ] Business impact (revenue, transactions)?
- [ ] Urgency/sentiment?

**Technical Feasibility (GitHub)**:
- [ ] Similar past work (time/complexity)?
- [ ] Dependencies or blockers?
- [ ] Technical debt to address first?
- [ ] Engineering sentiment?

**Strategic Alignment (Confluence)**:
- [ ] Mentioned in roadmap or strategy docs?
- [ ] Related to company priorities?
- [ ] Stakeholder interest level?

#### 3. Calculate ROI
**Time: 10 minutes**

**For Contact Reduction**:
```
Monthly tickets saved × Cost per contact = Monthly savings
Monthly savings × 12 = Annual savings
Annual savings / Engineering months = ROI
```

**For AI Improvement**:
```
Current conversations × Improved AI resolution rate = Deflected tickets
Deflected tickets × (Human cost - AI cost) = Monthly savings
```

Ask Claude:
```
"Help me calculate ROI for these initiatives:
[paste data]

Consider:
- Engineering effort estimates
- Support cost savings
- Revenue impact if applicable
- Strategic value"
```

#### 4. Create Priority Matrix
**Time: 10 minutes**

Plot on Impact vs. Effort:
- High Impact, Low Effort → Do Now
- High Impact, High Effort → Plan & Resource
- Low Impact, Low Effort → Quick Wins
- Low Impact, High Effort → Don't Do

Ask Claude to help visualize and recommend order.

#### 5. Document Decision
**Time: 10 minutes**

Create: `04-active-work/roadmap-items/prioritization-[date].md`

Include:
- Ranking with rationale
- Data supporting each decision
- Expected impact on North Star Metrics
- Resource requirements
- Recommended timeline


## Workflow 3: PRD with Full Context

### Objective
Write comprehensive PRD backed by data from all sources.

### Steps

#### 1. Problem Validation (30 minutes)

**Support Data (BigQuery)**:
```sql
-- Tickets related to this problem area
SELECT 
  created_at,
  subject,
  custom_field_topic,
  tags
FROM zendesk_tickets
WHERE [filter for relevant tickets]
  AND created_at >= DATE_SUB(CURRENT_DATE(), INTERVAL 3 MONTH)
ORDER BY created_at DESC;
```
→ Export: Volume, frequency, cost

**Customer Voice (Airtable)**:
- [ ] Search for feature requests
- [ ] Find merchant quotes
- [ ] Check research findings
- [ ] Note use cases
→ Export: Quotes, use cases, segmentation

**Past Attempts (Confluence)**:
- [ ] Search for previous RFCs or PRDs
- [ ] Check why not done before
- [ ] Review technical decisions
→ Document: History, constraints

#### 2. Solution Research (30 minutes)

**Technical Approach (GitHub)**:
- [ ] Review similar features
- [ ] Check architecture patterns
- [ ] Identify constraints
- [ ] Get engineering input
→ Document: Feasibility, approach

**Competitive Intel (Google Drive/Confluence)**:
- [ ] Check competitive analysis docs
- [ ] Review market research
- [ ] Find best practice examples
→ Reference: Industry standards

#### 3. Draft with Claude (45 minutes)

```
"Help me write a PRD for [feature]. Here's my research:

PROBLEM (from Support Data):
- [paste ticket volumes and costs]
- [paste common issues]

CUSTOMER VOICE (from Airtable):
"[paste quotes]"
- Use cases: [paste use cases]
- Segment: [affected customers]

TECHNICAL CONTEXT (from GitHub):
- [paste constraints or patterns]

PAST WORK (from Confluence):
- [paste relevant context]

Use our PRD template and help me draft:
1. Problem statement
2. User stories
3. Requirements
4. Success metrics"
```

#### 4. Validate & Refine (30 minutes)

**Technical Review**:
- Share with engineering
- Link to relevant GitHub issues
- Get effort estimates

**Business Review**:
- Share with stakeholders
- Reference Confluence strategy docs
- Validate ROI calculations

**Customer Validation**:
- Optional: Share concept with select merchants from Airtable research

#### 5. Finalize & Link

Save: `04-active-work/roadmap-items/[feature-name]/prd.md`

**Include links to**:
- BigQuery queries used
- Airtable feature request
- GitHub issues/discussions
- Confluence related docs
- Google Drive research materials


## Workflow 4: Root Cause Investigation

### Objective
Deep dive on support issue spike using all available data.

### Trigger
- Ticket volume spike detected
- AI resolution rate drop
- Customer complaints
- Leadership inquiry

### Steps

#### 1. Quantify the Issue (15 minutes)

**BigQuery Queries**:
```sql
-- Spike analysis
WITH daily_counts AS (
  SELECT 
    DATE(created_at) as date,
    COUNT(*) as ticket_count
  FROM zendesk_tickets
  WHERE created_at >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
  GROUP BY date
)
SELECT 
  date,
  ticket_count,
  AVG(ticket_count) OVER (
    ORDER BY date
    ROWS BETWEEN 6 PRECEDING AND 1 PRECEDING
  ) as seven_day_avg,
  ticket_count - AVG(ticket_count) OVER (
    ORDER BY date
    ROWS BETWEEN 6 PRECEDING AND 1 PRECEDING
  ) as variance
FROM daily_counts
ORDER BY date DESC;
```

Answer:
- When did it start?
- How big is the increase?
- Which categories affected?
- Which channels?

#### 2. Sample Ticket Review (20 minutes)

**In Zendesk**:
- Pull 10-15 representative tickets
- Read actual merchant descriptions
- Look for common patterns
- Note error messages or specific issues

**Document**: Specific examples with ticket IDs

#### 3. Check for Changes (15 minutes)

**GitHub**:
- [ ] Recent deploys or releases?
- [ ] New features launched?
- [ ] Bug fixes that might have broken something?
- [ ] Infrastructure changes?

**Confluence**:
- [ ] Planned releases or migrations?
- [ ] Known issues documented?
- [ ] Incident reports?

**Google Drive**:
- [ ] Recent merchant communications?
- [ ] Marketing campaigns?

#### 4. Correlate with External Factors (10 minutes)

Consider:
- Transaction volume changes (BigQuery)
- Merchant growth (new signups)
- Seasonal patterns
- Industry events
- Competitor issues

#### 5. Customer Impact Assessment (10 minutes)

**Airtable**:
- [ ] Check if affected merchants are in research database
- [ ] Review their past feedback
- [ ] Note segment and size

**BigQuery**:
- [ ] Transaction volume at risk
- [ ] Number of unique merchants affected
- [ ] Revenue impact

#### 6. Synthesize Findings with Claude (20 minutes)

```
"Help me investigate this support ticket spike:

QUANTITATIVE DATA:
- Tickets increased from [X] to [Y] starting [date]
- Primary categories: [data]
- Channels affected: [data]

TICKET SAMPLES:
[paste examples with ticket IDs]

RECENT CHANGES:
- GitHub: [deployments or changes]
- Product: [new features or changes]

CUSTOMER IMPACT:
- Merchants affected: [segment info]
- Transaction volume: [data]

Help me:
1. Identify the most likely root cause
2. Determine if this is product, process, or external
3. Recommend immediate mitigation
4. Suggest long-term fix"
```

#### 7. Create Action Plan (15 minutes)

Use: `03-templates/rfc-template.md` or investigation doc

**Include**:
- Root cause analysis
- Impact quantification  
- Immediate actions
- Long-term solution
- Owner and timeline
- How to prevent recurrence

**Share**:
- Confluence (document findings)
- GitHub (file issue if technical)
- Stakeholders (update via email/Slack)


## Tips for Efficient Multi-Source Analysis

### Before You Start
- [ ] Bookmark all data source URLs
- [ ] Have login credentials ready
- [ ] Open all tools in separate browser tabs/windows
- [ ] Set up screen layout for easy switching

### During Analysis
- [ ] Keep running notes document open
- [ ] Copy data with source attribution
- [ ] Take screenshots of key findings
- [ ] Note any access issues or broken links

### Using Claude Effectively
- [ ] Paste data in chunks (not all at once)
- [ ] Provide context for each data source
- [ ] Ask for synthesis, not just summary
- [ ] Request actionable recommendations
- [ ] Iterate on initial output

### After Analysis
- [ ] Save all source queries/filters used
- [ ] Document data source links
- [ ] Archive raw data if needed
- [ ] Update this workflow with learnings


## Common Pitfalls to Avoid

❌ **Analysis paralysis**: Don't try to gather ALL data—start with most important sources

❌ **Stale data**: Always check data timestamps and refresh if needed

❌ **Missing context**: Always cross-reference—BigQuery data alone doesn't tell the story

❌ **No documentation**: Don't just analyze—document findings for future reference

❌ **Working in silos**: Share queries, findings, and methods with team

❌ **Ignoring outliers**: Investigate anomalies—they often reveal important issues


## Quick Reference: When to Use Which Source

| Need | Primary Source | Supporting Sources |
|------|---------------|-------------------|
| Ticket volume trends | BigQuery | - |
| Contact rate calculation | BigQuery + Transactions | - |
| Customer pain points | Airtable | BigQuery (for volume) |
| Technical feasibility | GitHub | Confluence (for past decisions) |
| Feature prioritization | All sources | - |
| Root cause analysis | BigQuery | GitHub, Confluence, Airtable |
| Market/competitive intel | Google Drive, Confluence | Airtable (customer requests) |
| Engineering estimates | GitHub | Confluence (past projects) |
| Strategic alignment | Confluence | Google Drive (strategy docs) |
| Documentation gaps | support.checkout.com | BigQuery (ticket volume to quantify) |
| Integration issues | checkout.com/docs | api-reference.checkout.com, BigQuery |
| API-related tickets | api-reference.checkout.com | checkout.com/docs, GitHub |
| AI Agent improvement | support.checkout.com | Intercom analytics |
| Self-service content audit | All three doc sites | BigQuery (which topics drive tickets) |


**Last Updated**: [Date]  
**Owner**: Charlie Wildish
