# Data Sources Reference

> This document catalogs all data sources used for PM work, including access patterns, key queries, and how to work with each system.

## Quick Reference

| Source | Purpose | Access | Best For |
|--------|---------|--------|----------|
| **Confluence** | Product documentation | [Add URL] | Feature specs, decisions, team docs |
| **Google Drive** | Documentation & files | [Add URL] | Presentations, spreadsheets, shared docs |
| **BigQuery** | Zendesk ticket data | SQL queries | Ticket analysis, trend identification |
| **Airtable** | Customer research | [Add URL] | Research notes, user interviews, feedback |
| **GitHub** | Team repository | [Add URL] | Code review, technical context, PRs |
| **support.checkout.com** | Customer support portal | Public | FAQs, help articles, self-service content |
| **checkout.com/docs** | Technical documentation | Public | Integration guides, API guides, best practices |
| **api-reference.checkout.com** | API reference | Public | Endpoint specs, request/response schemas |


## Confluence

### Purpose
Central repository for product documentation, technical specs, and team knowledge.

### Access
- **URL**: [Add your Confluence workspace URL]
- **Login**: [SSO/credentials info]
- **Permissions**: [Your access level]

### Key Spaces/Pages

**Product Documentation**:
- [Link to product specs]
- [Link to feature documentation]
- [Link to roadmap]

**Support Documentation**:
- [Link to support processes]
- [Link to escalation procedures]
- [Link to team runbooks]

**Meeting Notes**:
- [Link to PM sync notes]
- [Link to planning sessions]
- [Link to retrospectives]

### Search Tips
- Use Confluence search for: `space:SUPPORT type:page`
- Tag important pages for easy filtering
- Set up page watches for critical docs

### Workflow Integration

**When writing PRDs**:
1. Search Confluence for similar past features
2. Reference related technical specs
3. Link PRD to relevant Confluence pages
4. Export key information to this workspace for AI assistance

**When gathering context**:
1. Search for previous decisions
2. Review meeting notes for stakeholder input
3. Find related product specs

### Claude Assistance Pattern
```
"I found this information in Confluence: [paste relevant content]
Help me [analyze/summarize/draft based on] this information"
```


## Google Drive

### Purpose
Shared documentation, presentations, spreadsheets, and collaborative files.

### Access
- **URL**: [Add Drive folder URL]
- **Login**: [Google account]
- **Key Folders**:
  - [Link to PM folder]
  - [Link to Support team folder]
  - [Link to shared resources]

### Common File Types

**Presentations**:
- Stakeholder updates
- Roadmap reviews
- QBRs and planning decks

**Spreadsheets**:
- Ticket analysis data
- Metric tracking
- Prioritization frameworks
- Resource planning

**Documents**:
- Draft PRDs
- Research reports
- Meeting agendas

### Organization Best Practices
- Use consistent naming: `YYYY-MM-DD_Document-Name`
- Keep folder structure aligned with this workspace
- Download key docs to workspace for version control

### Claude Assistance Pattern
```
"I have this data from a Google Sheet: [paste data]
Help me analyze this and create visualizations/insights"

"Here's a draft presentation: [paste content]
Help me improve the messaging for [audience]"
```


## BigQuery - Zendesk Ticket Data

### Purpose
SQL database for analyzing support ticket data, trends, and metrics.

### Access
- **Project**: [Your GCP project]
- **Dataset**: [Zendesk data dataset name]
- **Access**: [BigQuery console URL]
- **Permissions**: [Your role]

### Key Tables

**Main Tables**:
- `zendesk_tickets`: All ticket data
- `zendesk_ticket_comments`: Ticket conversation history
- `zendesk_users`: Customer/agent information
- `zendesk_organizations`: Merchant account data
- `zendesk_ticket_metrics`: Performance metrics (response time, resolution time)

**Table Schemas**: [Link to data dictionary if you have one]

### Common Queries

#### 1. Contact Rate per 1M Transactions
```sql
-- Contact Rate: Support contacts per 1M transactions
WITH ticket_counts AS (
  SELECT 
    DATE_TRUNC(created_at, MONTH) as month,
    COUNT(DISTINCT id) as ticket_count
  FROM `project.dataset.zendesk_tickets`
  WHERE created_at >= DATE_SUB(CURRENT_DATE(), INTERVAL 6 MONTH)
  GROUP BY month
),
transaction_counts AS (
  SELECT
    DATE_TRUNC(transaction_date, MONTH) as month,
    COUNT(*) as transaction_count
  FROM `project.dataset.transactions` -- Update with your transactions table
  WHERE transaction_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 6 MONTH)
  GROUP BY month
)
SELECT 
  t.month,
  t.ticket_count,
  tr.transaction_count,
  (t.ticket_count / tr.transaction_count) * 1000000 as contact_rate_per_1M
FROM ticket_counts t
JOIN transaction_counts tr ON t.month = tr.month
ORDER BY t.month DESC;
```

#### 2. Top Ticket Categories
```sql
-- Most common ticket categories (last 30 days)
SELECT 
  custom_field_topic as category,
  COUNT(*) as ticket_count,
  ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) as percentage
FROM `project.dataset.zendesk_tickets`
WHERE created_at >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
  AND status != 'deleted'
GROUP BY category
ORDER BY ticket_count DESC
LIMIT 20;
```

#### 3. AI Agent Containment Rate
```sql
-- Tickets escalated from Intercom Fin vs total conversations
SELECT 
  DATE_TRUNC(created_at, DAY) as date,
  COUNT(CASE WHEN via = 'intercom' THEN 1 END) as intercom_escalations,
  -- Add intercom_conversations from Intercom data if available
  ROUND(
    COUNT(CASE WHEN via = 'intercom' THEN 1 END) * 100.0 / 
    [total_intercom_conversations],
  2) as escalation_rate
FROM `project.dataset.zendesk_tickets`
WHERE created_at >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY)
GROUP BY date
ORDER BY date DESC;
```

#### 4. Tickets by Channel
```sql
-- Breakdown of tickets by support channel
SELECT 
  via as channel,
  COUNT(*) as ticket_count,
  ROUND(AVG(TIMESTAMP_DIFF(solved_at, created_at, HOUR)), 1) as avg_resolution_hours
FROM `project.dataset.zendesk_tickets`
WHERE created_at >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
  AND solved_at IS NOT NULL
GROUP BY channel
ORDER BY ticket_count DESC;
```

#### 5. Weekly Ticket Trends
```sql
-- Weekly ticket volume with YoY comparison
SELECT 
  EXTRACT(ISOWEEK FROM created_at) as week_number,
  EXTRACT(YEAR FROM created_at) as year,
  COUNT(*) as ticket_count,
  ROUND(AVG(COUNT(*)) OVER (
    PARTITION BY EXTRACT(YEAR FROM created_at)
    ORDER BY EXTRACT(ISOWEEK FROM created_at)
    ROWS BETWEEN 3 PRECEDING AND CURRENT ROW
  ), 0) as four_week_avg
FROM `project.dataset.zendesk_tickets`
WHERE created_at >= DATE_SUB(CURRENT_DATE(), INTERVAL 1 YEAR)
GROUP BY week_number, year
ORDER BY year DESC, week_number DESC;
```

### Query Best Practices

**Performance**:
- Always filter by date range to limit data scanned
- Use partitioned tables when available
- Test queries on small date ranges first

**Cost Management**:
- Preview query before running (shows data processed)
- Use `LIMIT` for exploratory queries
- Schedule recurring reports instead of running repeatedly

**Data Quality**:
- Check for null values in key fields
- Validate date ranges are reasonable
- Cross-reference totals with Zendesk UI

### Workflow Integration

**For Weekly Ticket Analysis**:
1. Run weekly trends query
2. Export results to Google Sheets or CSV
3. Copy data to this workspace: `04-active-work/current-sprint/ticket-data-[date].csv`
4. Ask Claude: "Analyze this ticket data and identify top patterns"

**For Monthly Reviews**:
1. Run comprehensive queries (categories, channels, metrics)
2. Combine with transaction data for contact rate
3. Use ticket-analysis-template.md
4. Ask Claude to help draft analysis report

**For Ad-Hoc Investigation**:
1. Write custom query for specific issue
2. Export results
3. Share with Claude for pattern analysis

### Claude Assistance Pattern
```
"Here's ticket data from BigQuery for the past month: [paste results]
Analyze the trends and identify the top 3 opportunities for reducing contact rate"

"I ran this SQL query: [paste query]
The results show: [paste data]
What insights can you extract? What should I investigate next?"
```

### Saved Queries Location
Store your frequently-used queries in: `01-knowledge-base/bigquery-queries/`
- Keep a library of proven queries
- Version control query improvements
- Share with team members


## Airtable - Customer Research

### Purpose
Structured database for customer research, user interviews, feedback, and insights.

### Access
- **Workspace**: [Add Airtable workspace URL]
- **Login**: [SSO/credentials]
- **Key Bases**:
  - [Link to Customer Research base]
  - [Link to User Interviews base]
  - [Link to Feedback Tracking base]

### Common Tables/Views

**User Research**:
- Interview notes
- Research findings
- User personas
- Pain points catalog

**Feature Requests**:
- Request tracking
- Merchant information
- Priority/impact scoring
- Status tracking

**Customer Feedback**:
- CSAT responses
- Support ticket themes
- Merchant quotes
- Sentiment analysis

### Data Fields to Track

**For Each Research Session**:
- Date
- Merchant name/ID
- Merchant segment (enterprise, SMB, etc.)
- Interview type (discovery, usability, feedback)
- Key findings
- Quotes
- Related features/tickets
- Follow-up actions

**For Feature Requests**:
- Request description
- Number of merchants requesting
- Business impact (revenue, transactions affected)
- Effort estimate
- Status (backlog, planned, in-progress, shipped)
- Related support tickets

### Workflow Integration

**When Analyzing Support Patterns**:
1. Cross-reference top ticket categories with Airtable research
2. Look for existing merchant feedback on those topics
3. Identify gaps where more research is needed

**When Writing PRDs**:
1. Search Airtable for related feature requests
2. Pull merchant quotes and use cases
3. Reference customer pain points
4. Link research findings in PRD

**When Prioritizing Roadmap**:
1. Review feature request volume and impact
2. Check merchant segment distribution
3. Validate with research insights

### Claude Assistance Pattern
```
"Here's customer research data from Airtable: [paste relevant records]
Help me identify common themes and prioritize based on impact"

"I have these merchant quotes about [feature]: [paste quotes]
Help me synthesize this into a problem statement for a PRD"
```

### Export & Integration
- Export relevant views to CSV for analysis
- Copy key insights to `01-knowledge-base/customer-research/`
- Reference in PRDs and stakeholder updates


## Checkout.com Public Documentation

These are the three customer-facing documentation sites. As PM for Customer Support, these are critical sources for understanding what merchants can self-serve, identifying documentation gaps that drive tickets, and improving AI Agent knowledge.

### support.checkout.com — Support Portal & FAQs

**Purpose**: Customer-facing help articles and FAQs. Primary self-service resource and the main knowledge source powering the Intercom Fin AI Agent.

**URL**: https://support.checkout.com  
**Access**: Public  
**Login required**: No (viewing); yes for editing/management  
**Owned by**: Content team. Charlie's contact: Content Strategist.

**Content types**:
- Frequently asked questions by topic
- Step-by-step how-to guides
- Troubleshooting articles
- Account management guidance
- Billing and settlement help

**How to use as a PM**:

**Finding documentation gaps**:
1. Look up your top ticket categories in BigQuery
2. Search support.checkout.com for articles covering those topics
3. If article doesn't exist → documentation gap → create it
4. If article exists but tickets still come in → article is unclear/incomplete → improve it

**Assessing AI Agent performance**:
- The Fin AI Agent draws from this content
- If AI resolution rate is low on a topic, check if article exists and is clear
- Test the AI Agent yourself using the same questions merchants ask
- Compare AI answer to article content for accuracy

**Content audit**:
- Check for outdated articles after product changes
- Look for articles with no clear resolution path (→ higher ticket rate)
- Identify most-viewed articles (→ popular topics, potential contact reduction opportunities)

**Claude Assistance Pattern**:
```
"Here's an article from support.checkout.com: [paste article content]

We're getting [X] tickets/month on this topic despite the article existing.
Help me identify why merchants aren't self-serving and how to improve the article."

"Our AI Agent is failing to resolve questions about [topic].
Here's the current help article: [paste content]
How should we rewrite it to be more AI-friendly and easier to retrieve?"
```


### checkout.com/docs — Technical Documentation

**Purpose**: Developer-focused integration guides, implementation best practices, and technical references for merchants building on Checkout.com.

**URL**: https://checkout.com/docs  
**Access**: Public  
**Login required**: No  
**Owned by**: Content team. Charlie's contact: Content Strategist.

**Content types**:
- Integration guides (API, SDK, hosted pages)
- Payment method setup guides
- Fraud and risk configuration
- Webhooks and event handling
- Testing and sandbox guides
- Migration guides
- Compliance and security guidance

**How to use as a PM**:

**Understanding integration pain points**:
- Cross-reference integration-related support tickets with relevant doc pages
- Identify steps in guides that correlate with common errors
- Check if error codes returned by APIs are explained in docs

**Evaluating documentation quality**:
- Follow a guide from start to finish as a developer would
- Note any ambiguous steps, missing code examples, or broken links
- Check if guides cover edge cases that generate support tickets

**When investigating technical support issues**:
- Find the relevant guide to understand expected behaviour
- Compare documented behaviour with what merchants are experiencing
- Identify gaps between documentation and actual product behaviour

**When writing PRDs**:
- Link to relevant docs sections as context
- Note if new features require new documentation
- Flag if existing docs will need updating post-launch

**Claude Assistance Pattern**:
```
"Here's the integration guide for [feature] from checkout.com/docs: [paste content]

We're receiving [X] tickets/month from merchants struggling with this step.
Help me identify which parts are unclear and suggest specific improvements."

"A merchant is getting this error: [error message]
The docs say: [paste relevant section]
Help me identify if this is a documentation gap or a product bug."
```


### api-reference.checkout.com — API Reference

**Purpose**: Complete technical reference for all Checkout.com API endpoints — request parameters, response schemas, error codes, and authentication.

**URL**: https://api-reference.checkout.com  
**Access**: Public  
**Login required**: No  
**Owned by**: Content team. Charlie's contact: Content Strategist.

**Content types**:
- Endpoint documentation (method, path, parameters)
- Request and response body schemas
- Error codes and descriptions
- Authentication requirements
- Code examples by language
- Changelog / API versioning

**How to use as a PM**:

**Diagnosing API-related support tickets**:
- Look up the endpoint the merchant is calling
- Check required vs. optional parameters
- Review error code definitions to validate error messages
- Compare merchant's request to expected schema

**Identifying documentation quality issues**:
- Check if error codes have clear, actionable descriptions
- Look for endpoints with missing examples or incomplete schemas
- Identify deprecated endpoints that merchants may still be using

**When writing API-related requirements**:
- Reference specific endpoints to scope the work
- Use existing schema conventions for consistency
- Document any new error codes required
- Link PRDs to relevant API reference pages

**API versioning awareness**:
- Track which API versions are still in use (via support tickets)
- Identify merchants on deprecated versions causing ticket spikes
- Flag upcoming deprecations as potential support volume drivers

**Claude Assistance Pattern**:
```
"Here's the API reference for the [endpoint] endpoint: [paste spec]

A merchant is seeing this error response: [paste error]
Help me explain what's likely wrong and what they should do."

"I need to spec a new feature that adds [capability] to the [endpoint] endpoint.
Here's the current endpoint spec: [paste]
Help me draft the API changes needed in our PRD."
```


## How to Use All Three Together

These three sites serve two purposes simultaneously:

1. **Customer self-service** — merchants find answers without contacting support
2. **Fin AI Agent knowledge base** — Fin draws exclusively from these three sites to answer merchant queries in Intercom

```
support.checkout.com        →  Non-technical merchants, general users
checkout.com/docs           →  Developers integrating the product
api-reference.checkout.com  →  Developers writing API calls
```

> **Critical implication for AI resolution rate**: If a question isn't answered in these three sites — or is answered poorly — Fin will escalate to a human agent. Every content gap is both a self-service gap and a Fin AI gap. Improving content on these sites improves both simultaneously.

### Finding Documentation Gaps

When a ticket category is high:
1. **Search all three sites** for related content
2. **Map the user journey**: Which site should have the answer?
3. **Identify the gap**: Missing article, unclear content, wrong location?
4. **Measure potential impact**: Tickets × resolution rate = deflection opportunity

### Before and After Product Changes

**Before launch**:
- [ ] Is the new feature documented on the right site(s)?
- [ ] Are error messages explained in API reference?
- [ ] Is the help article written and ready?
- [ ] Has the AI Agent been tested with new content?

**After launch**:
- [ ] Monitor tickets for documentation-related questions
- [ ] Update articles based on real merchant questions
- [ ] Check AI resolution rate on new topic


## GitHub - Team Repository

### Purpose
Code repository for viewing technical implementation, understanding constraints, and reviewing changes.

### Access
- **Repository**: [Add your repo URL]
- **Login**: [GitHub account]
- **Your Role**: [Permissions level]

### What to Look For

**When Reviewing Technical Feasibility**:
- Browse existing code structure
- Check similar implementations
- Identify technical constraints
- Review API patterns used

**When Understanding Issues**:
- Look at recent commits related to problem area
- Check pull request discussions
- Review issue comments and decisions
- Find related bug reports

**When Writing Requirements**:
- Understand existing architecture
- Check API endpoints and data models
- Review similar features for patterns
- Validate technical approach with code

### Key Areas to Monitor

**Pull Requests**:
- Support-related bug fixes
- New features in development
- API changes affecting integrations
- Performance improvements

**Issues**:
- Support-escalated bugs
- Feature requests from engineering perspective
- Technical debt items

**Documentation**:
- README files
- API documentation
- Architecture decisions (ADRs)
- Setup and deployment guides

### Workflow Integration

**When Gathering Context for PRD**:
1. Search repo for related code/features
2. Review past PRs for similar work
3. Check for technical constraints in issues
4. Document findings in PRD technical section

**When Investigating Support Issues**:
1. Search for related bug reports
2. Check recent commits to affected areas
3. Review PR discussions for context
4. Share findings with engineering team

**When Estimating Effort**:
1. Look at similar past features
2. Check complexity of affected code
3. Review team's development patterns
4. Factor in technical debt

### Claude Assistance Pattern
```
"I found this code in our repo: [paste relevant code snippet]
Help me understand how this works and what constraints it creates for [feature]"

"Here's a GitHub issue discussion: [paste comments]
Summarize the technical decision and implications for support"
```

### Setup for Easy Access
- Bookmark frequently-visited repo sections
- Set up GitHub notifications for support-related labels
- Use GitHub search syntax for efficient searching:
  - `label:support` - Support-related issues
  - `is:pr is:merged label:bug` - Merged bug fixes
  - `path:api/` - API-specific code


## Workflow: Bringing It All Together

### For Ticket Analysis
1. **BigQuery**: Pull ticket data and metrics
2. **Airtable**: Cross-reference with customer research
3. **Confluence**: Review any documented known issues
4. **GitHub**: Check for related bugs or fixes
5. **This Workspace**: Create analysis using template + Claude

### For Writing PRDs
1. **Confluence**: Search for related past work
2. **Airtable**: Find customer research and quotes
3. **GitHub**: Understand technical constraints
4. **Google Drive**: Review any related presentations/data
5. **This Workspace**: Draft PRD using template + Claude

### For Stakeholder Updates
1. **BigQuery**: Pull latest metrics
2. **GitHub**: Check feature development progress
3. **Confluence**: Review recent decisions
4. **Google Drive**: Update presentation/report
5. **This Workspace**: Draft update using template + Claude


## Best Practices

### Data Management
- **Don't store raw data in this workspace**: Link to sources instead
- **Do extract insights**: Document findings, not full datasets
- **Use Claude for analysis**: Paste data into Claude for interpretation
- **Version control insights**: Keep analyzed data with timestamps

### Access Patterns
- **Bookmark frequently-used URLs**: Quick access to common queries/pages
- **Save common queries**: Template queries in this knowledge base
- **Set up alerts**: Get notified of important changes
- **Document access issues**: Note who to contact for permissions

### Integration Hygiene
- **Cite your sources**: Always note where data came from
- **Check timestamps**: Ensure data is current
- **Cross-validate**: Confirm findings across multiple sources
- **Update regularly**: Keep links and access info current


## Quick Access Checklist

For your next analysis session, ensure you have:
- [ ] BigQuery bookmarked and access confirmed
- [ ] Airtable bases open and filtered
- [ ] Confluence search ready
- [ ] GitHub repo open to relevant section
- [ ] Google Drive folders accessible
- [ ] support.checkout.com open in browser
- [ ] checkout.com/docs open in browser
- [ ] api-reference.checkout.com open in browser
- [ ] This workspace ready for documentation


**Last Updated**: [Date]  
**Owner**: Charlie Wildish

**Note**: Update URLs and access information as you add them. This document should be a living reference that evolves with your workflow.
