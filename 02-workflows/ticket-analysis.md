# Ticket Analysis Workflow

> This workflow guides you through analyzing support tickets to identify patterns, root causes, and product opportunities.

## When to Perform Ticket Analysis

### Regular Cadence
- **Weekly**: Quick review of trends and emerging issues
- **Monthly**: Comprehensive analysis for stakeholder updates and roadmap planning
- **Quarterly**: Deep dive for strategic planning and annual goals

### Ad-Hoc Triggers
- Noticeable spike in ticket volume
- New product launch or feature release
- Customer complaints about specific issue
- Leadership request for data
- Investigation of support cost trends


## Step 1: Data Collection

### Define Scope
- **Time Period**: [e.g., Past 7 days, Past month, Q1 2024]
- **Filters**: [All tickets, specific category, specific product, priority level]
- **Segments**: [All merchants, specific tier, region, industry]

### Export Data from Ticketing System

**Required Fields**:
- Ticket ID
- Creation date/time
- Category/Type
- Priority
- Status
- Resolution time
- Merchant ID
- Subject line
- Tags/Labels
- Assigned agent
- CSAT score (if available)

**Data Quality Check**:
- [ ] Verify date range is correct
- [ ] Check for missing or null values
- [ ] Confirm ticket counts match expectations
- [ ] Ensure all relevant fields exported

### Supplementary Data Sources
- CSAT survey responses and comments
- Merchant feedback from account teams
- Error logs or system metrics (if relevant)
- Previous analysis for comparison
- Product roadmap for context

### Canonical volume and taxonomy (Care)
- **Support taxonomy**: Use [support-taxonomy.md](../01-knowledge-base/processes/support-taxonomy.md) as the standard schema. When exporting or slicing Zendesk data, align categories to **Case Type → Issue Type → Reason**. Note any unmapped tags or "Other" so analysis uses consistent labels.
- **Last-6m flat table**: For volume, channel mix, segment, and Fin vs Zendesk splits, use [support_contacts_flat_table_2025_last_6m.csv](../01-knowledge-base/metrics/support_contacts_flat_table_2025_last_6m.csv) and [support_contacts_flat_table_2025_metric_definitions.md](../01-knowledge-base/metrics/support_contacts_flat_table_2025_metric_definitions.md) as the canonical source. Slice by case_type, issue_type, channel, support_segment, sales_territory, billing_region so frequency tables match how leadership already sees the data.


## Step 2: Quantitative Analysis

### Calculate Core Metrics

Use the template from `01-knowledge-base/metrics/kpi-definitions.md`

**Volume Metrics**:
- Total ticket count
- Average daily volume
- Tickets per agent
- Backlog size

**Performance Metrics**:
- First response time (median & average)
- Time to resolution (median & average)
- First contact resolution rate
- Reopen rate
- SLA compliance by priority

**Quality Metrics**:
- CSAT score
- Escalation rate
- Resolution rate (vs. escalated)

### Trend Analysis

**Compare to Previous Period**:
- Calculate % change in each metric
- Identify significant changes (>20% up or down)
- Look for patterns (day of week, time of day spikes)

**Visualization**:
- Create line chart of daily ticket volume
- Bar chart of top categories
- Trend line for key metrics over time


## Step 3: Categorization & Pattern Identification

### Category Breakdown

**Group tickets by** (align to support taxonomy where possible):
1. **Case Type** then **Issue Type** then **Reason** — use [support-taxonomy.md](../01-knowledge-base/processes/support-taxonomy.md) so every analysis uses the same labels (e.g. PAYMENTS (IN), Refunds, Refund status enquiry).
2. **Primary category** (integration, payment, account, billing, etc.) if your export uses legacy labels — map to taxonomy for reporting.
3. **Product area** (API, dashboard, specific feature).

**Baseline comparison**: Use the taxonomy’s summary counts and % of volume (from the last-6m flat table) as the baseline. Compare your analysis period to that mix (e.g. PAYMENTS 42.8%, AMA 16.9%) so you can state “PAYMENTS up 5% vs last-6m” or “Refunds within PAYMENTS driving the spike.”

**Create frequency table**:
| Category | Count | % of Total | Change vs Previous |
|----------|-------|-----------|-------------------|
| [Category] | [#] | [%] | [↑↓ %] |

### Identify Top Issues

**For each major category, drill down**:
- What are the specific problems?
- Are there common keywords or phrases?
- Which error messages appear frequently?

**Example drill-down**:
```
Integration Issues (230 tickets, 25% of total)
  ├─ API authentication errors (95 tickets)
  │  ├─ Using wrong environment keys (47 tickets)
  │  └─ Signature validation failing (48 tickets)
  ├─ Webhook not receiving events (78 tickets)
  └─ SDK integration questions (57 tickets)
```

### Search for Patterns

**Segment by**:
- Merchant type (enterprise, SMB, startup)
- Industry vertical
- Integration method (API, SDK, platform)
- Geography/region
- Account age (new vs. established)

**Questions to ask**:
- Are certain merchant segments over-represented?
- Do issues cluster around specific times (releases, month-end)?
- Are there common merchants appearing repeatedly?
- Do similar issues share tags or keywords?


## Step 4: Qualitative Analysis

### Read Sample Tickets

**For each major category**:
- Read 5-10 representative tickets
- Note exact error messages
- Capture merchant's words describing the problem
- Understand their use case or context

### Analyze CSAT Comments

**Positive feedback**:
- What are merchants praising?
- What made their experience good?
- Which agents/responses work well?

**Negative feedback**:
- What frustrated merchants?
- Where did we fall short?
- What could have been clearer/faster?

### Extract Quotes

Capture specific merchant quotes that illustrate:
- Pain points
- Urgency or business impact
- Confusion or usability issues
- Feature requests
- Positive experiences


## Step 5: Root Cause Analysis

**Prioritisation lens**: Use the **Prioritisation implications** section in [support-taxonomy.md](../01-knowledge-base/processes/support-taxonomy.md) to decide where to dig. Focus root-cause work on high-leverage categories first (e.g. PAYMENTS (IN), ACCOUNT MANAGEMENT & ACCESS); treat TECHNICAL ISSUE as diagnostic/tooling, not content-only.

### For Each Top Issue, Ask

**Is this a...**
- [ ] **Bug/Technical Issue**: System not working as designed
- [ ] **Product Gap**: Feature doesn't exist or is limited
- [ ] **Documentation Gap**: Information missing or unclear
- [ ] **UX Problem**: Confusing interface or workflow
- [ ] **Education Gap**: Merchant doesn't understand how to use feature
- [ ] **Process Issue**: Internal support process inefficiency
- [ ] **Edge Case**: Unusual scenario we didn't account for

### Validate Root Cause

**Confirm your hypothesis**:
- Review product documentation
- Test the functionality yourself
- Consult with engineering or product team
- Check if this is a known issue
- Look at related tickets for additional evidence

### Assess Impact

**For each root cause**:
- How many tickets does this drive? (monthly rate)
- What's the business impact? (revenue at risk, churn risk)
- What's the support cost? (hours spent on these tickets)
- What's the merchant impact? (frustration, blocked workflows)
- Is this trending up or down?


## Step 6: Prioritization & Recommendations

### Prioritization Framework

Use 2x2 matrix: **Impact vs. Effort**

**High Impact, Low Effort** (Do First):
- Significant ticket volume or business impact
- Quick fix (documentation update, simple feature tweak)
- Examples: Fix broken link, clarify confusing error message

**High Impact, High Effort** (Plan for Roadmap):
- Major product gaps or architectural issues
- Requires substantial engineering work
- Examples: New payment method, major UX overhaul

**Low Impact, Low Effort** (Quick Wins):
- Nice-to-haves that are easy to do
- Small quality-of-life improvements
- Examples: Add tooltip, improve copy

**Low Impact, High Effort** (Defer):
- Edge cases affecting few merchants
- Large effort for small benefit
- Examples: Niche feature request

### Contact reduction programme — escalation to product

When escalating a contact driver to product or feeding the contact reduction programme:

- **Taxonomy**: Use [support-taxonomy.md](../01-knowledge-base/processes/support-taxonomy.md) to name the **Case Type** and **Issue Type** (and Reason if useful). Prioritise categories that the taxonomy flags as high-leverage (PAYMENTS, AMA, then PAYOUTS, FUNDS AND FEES). Escalation evidence should use the same labels so product and reporting stay aligned.
- **Evidence pack**: Use [support_contacts_flat_table_2025_last_6m.csv](../01-knowledge-base/metrics/support_contacts_flat_table_2025_last_6m.csv) (and [metric definitions](../01-knowledge-base/metrics/support_contacts_flat_table_2025_metric_definitions.md)) to build the evidence pack. Filter by case_type, issue_type, and optionally segment, channel, region. Include: contact count in period, trend, Fin vs Zendesk split. That gives product a reproducible, consistent basis for “how big is this?” and for tracking impact after fixes.

### Generate Recommendations

**For each high-priority issue**:
- **Problem**: Clear description of the issue
- **Root Cause**: What's actually wrong
- **Proposed Solution**: Specific action to take
- **Impact**: Expected improvement (ticket reduction, time saved, revenue protected)
- **Effort**: Rough estimate (hours/days/weeks)
- **Owner**: Who should take action (engineering, product, support, docs)
- **Timeline**: When should this be addressed


## Step 7: Create Analysis Report

Use the template: `03-templates/ticket-analysis-template.md`

### Key Sections

1. **Executive Summary**: Top 3 insights
2. **Volume Trends**: Charts and metrics
3. **Category Breakdown**: Top issues with details
4. **Root Cause Analysis**: What's driving tickets
5. **Recommendations**: Prioritized action items with owners

### Make it Actionable

- Specific recommendations, not vague observations
- Include owners and timelines
- Link to sample tickets as evidence
- Provide context on business impact
- Suggest success metrics to track


## Step 8: Socialize Findings

### Share with Stakeholders

**Product Team**:
- Product gaps and feature requests
- UX issues and usability concerns
- Merchant feedback and use cases

**Engineering Team**:
- Bugs and technical issues
- Performance or reliability concerns
- API/integration pain points

**Support Leadership**:
- Volume trends and resource needs
- Process improvements
- Training opportunities

**Leadership**:
- High-level trends and business impact
- Strategic recommendations
- Risk areas (churn, revenue)

### Present in Meetings

**Weekly support sync**:
- Quick highlights (5 minutes)
- Emerging issues to watch
- Wins (issues decreasing)

**Monthly business review**:
- Full report walkthrough
- Deep dive on top issues
- Roadmap discussion

**Quarterly planning**:
- Trends over quarter
- Strategic themes
- Investment priorities


## Step 9: Track Action Items

### Create Tasks

For each recommendation:
- [ ] File ticket/task in appropriate system (Jira, Linear, etc.)
- [ ] Assign owner
- [ ] Set due date
- [ ] Link to analysis report
- [ ] Tag with appropriate labels

### Follow Up

**Weekly**:
- Check progress on action items
- Unblock any issues
- Adjust priorities if needed

**Monthly**:
- Measure impact of completed actions
- Report back on improvements
- Celebrate wins

### Measure Success

**After implementing fixes**:
- Track ticket volume for that category
- Measure change in related metrics
- Gather qualitative feedback
- Calculate ROI (time/cost saved)


## Step 10: Continuous Improvement

### Update Documentation

- Add new patterns to `01-knowledge-base/payment-domain/common-issues.md`
- Update process docs if workflows changed
- Improve templates based on what worked

### Refine Analysis Process

**Reflect on**:
- What took too long?
- What data was hard to get?
- What insights were most valuable?
- What could be automated?

### Build Better Tools

**Invest in**:
- Automated dashboards for common metrics
- Tag taxonomy improvements in ticketing system
- Text analysis for pattern detection
- Integration between data sources


## Tips & Best Practices

### Be Consistent
- Use same time periods and definitions for trending
- Apply same categorization rules each time
- Track the same metrics regularly

### Be Curious
- Don't just count tickets, understand the "why"
- Read actual tickets, not just summaries
- Talk to support agents for their perspective
- Test the product yourself

### Be Objective
- Data may show unexpected results - report them honestly
- Not everything needs to be a crisis
- Acknowledge improvements and wins
- Provide context for changes

### Be Action-Oriented
- Every analysis should lead to decisions or actions
- Don't just report problems, propose solutions
- Make it easy for stakeholders to act on your findings
- Follow up to ensure recommendations are implemented

### Collaborate
- Involve support team in interpretation
- Partner with product/engineering on solutions
- Share drafts for feedback before finalizing
- Credit others' contributions


## Common Pitfalls to Avoid

❌ **Analysis paralysis**: Don't spend weeks perfecting the report
❌ **Data without insights**: Charts aren't useful without interpretation
❌ **No follow-through**: Recommendations without action waste time
❌ **Ignoring positives**: Don't only focus on problems
❌ **Too much detail**: Match depth to audience needs
❌ **Stale data**: Use recent data for current decisions


## Quick Reference Checklist

- [ ] Define scope and time period
- [ ] Export ticket data with all required fields; align categories to support taxonomy (Case Type / Issue Type / Reason)
- [ ] Use last-6m flat table and metric definitions for baseline volume and channel/segment splits
- [ ] Calculate core metrics (volume, performance, quality)
- [ ] Categorize tickets and identify top issues (compare to taxonomy baseline)
- [ ] Read sample tickets for qualitative insights
- [ ] Perform root cause analysis
- [ ] Prioritize using impact vs. effort framework
- [ ] Generate recommendations with owners and timelines
- [ ] Create analysis report using template
- [ ] Share with stakeholders
- [ ] Create and track action items
- [ ] Measure impact of implemented changes


**Last Updated**: [Date]
**Owner**: Charlie Wildish
