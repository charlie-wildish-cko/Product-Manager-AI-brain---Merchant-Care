# KPI Definitions & Metrics

> This document defines key performance indicators for customer support and product management. Use these definitions consistently across reports and stakeholder updates.

## The Care Flywheel — Metrics by Domain

Metrics are organised by the six domains of the Care Product capability model. Each domain has its own metrics that together describe the health of the full support system.

> Full model: `01-knowledge-base/strategy/care-product-model.md`

| Domain | Key Metrics |
|--------|------------|
| **1. Input** | Query mix %, channel mix %, self-serve resolution potential % |
| **2. Orchestration** | AI Agent resolution rate, first assignment time, routed ticket acceptance rate, AHT, FCR, reopen rate |
| **3. Fuel** | Data coverage vs taxonomy %, content coverage vs taxonomy %, AI Agent resolution rate by content |
| **4. Agent Experience** | Average Handle Time (AHT), taxonomy automation %, agent tool adoption rate, issue type automation % |
| **5. Insight & Prevention** | Top contact reasons per issue type (quarterly), % of top contact reasons resolved by a product fix per quarter, contact-product tagging accuracy |
| **6. Governance** | CSAT (AI Agent and human), SLA adherence %, internal QA scores |


## 🎯 North Star Metrics

These are the primary metrics that drive all product decisions for Customer Support:

### Contact Rate
- **Definition**: Number of support contacts per 1 million payment transactions
- **Calculation**: (Total support contacts / Total transactions) × 1,000,000
- **Target**: Continuously decreasing
- **Why It Matters**: 
  - Lower contact rate = better product quality and self-service
  - Indicates how often customers need help vs. self-serving
  - Scales with transaction volume growth
- **Measured**: Monthly and Quarterly
- **Influenced By**: 
  - Product quality and reliability
  - Documentation effectiveness
  - AI resolution rate
  - Proactive issue resolution

### Cost Per Contact
- **Definition**: Average cost to handle one support interaction
- **Calculation**: Total support costs / Total contacts handled
- **Target**: Continuously decreasing
- **Why It Matters**: 
  - Measures efficiency of support operations
  - Direct impact on business unit profitability
  - Enables comparison across channels and issue types
- **Measured**: Monthly and Quarterly
- **Influenced By**: 
  - Agent efficiency and productivity
  - Automation and tooling
  - Contact routing accuracy
  - Average handle time
  - Agent utilization rates

### Strategic Levers

To improve North Star Metrics, focus on:

1. **Contact Reduction**: Fix root causes → Lower contact rate
2. **AI Deflection**: Resolve with AI → Lower cost per contact
3. **Agent Efficiency**: Better tools → Lower cost per contact
4. **Self-Service**: Better docs → Lower contact rate

## Support Efficiency Metrics

### Ticket Volume
- **Definition**: Total number of support tickets created in a time period
- **Calculation**: Count of all tickets (excluding spam)
- **Target**: [Define based on team capacity]
- **Frequency**: Daily, Weekly, Monthly
- **Why It Matters**: Indicates support load and helps with resource planning

### First Response Time (FRT)
- **Definition**: Time from ticket creation to first agent response
- **Calculation**: Median or average time across all tickets
- **Target**: [e.g., < 4 hours for P2, < 24 hours for P3]
- **Frequency**: Daily, Weekly
- **Why It Matters**: Customer satisfaction heavily influenced by response speed

### Time to Resolution (TTR)
- **Definition**: Total time from ticket creation to resolution
- **Calculation**: Median or average time to close
- **Target**: [Define by priority level]
- **Frequency**: Weekly, Monthly
- **Why It Matters**: Measures efficiency and complexity of issues

### Backlog
- **Definition**: Number of open tickets awaiting agent action
- **Calculation**: Count of open tickets
- **Target**: [e.g., < 100 tickets]
- **Frequency**: Daily
- **Why It Matters**: Indicates whether team is keeping up with demand

### Tickets per Agent
- **Definition**: Average number of tickets handled per agent
- **Calculation**: Total tickets resolved / number of active agents
- **Target**: [Define based on ticket complexity]
- **Frequency**: Weekly, Monthly
- **Why It Matters**: Measures productivity and workload distribution

### Average Handle Time (AHT)
- **Definition**: Average active time an agent spends working on a single ticket
- **Calculation**: Total active handle time / tickets resolved
- **Target**: Decreasing over time (via automation and better tooling)
- **Flywheel domain**: Agent Experience (Domain 4)
- **Frequency**: Weekly, Monthly
- **Why It Matters**: Key lever for reducing cost per contact; reflects agent efficiency and tool effectiveness

### Taxonomy Automation Rate
- **Definition**: Percentage of ticket fields (category, topic, reason) auto-populated without agent input
- **Calculation**: (Auto-tagged fields / Total fields) × 100
- **Target**: High — reduces agent admin, speeds up routing
- **Flywheel domain**: Agent Experience (Domain 4)
- **Frequency**: Monthly
- **Why It Matters**: Manual tagging is slow and inconsistent; automation improves both AHT and data quality

### Contact-Product Tagging Accuracy
- **Definition**: How accurately tickets are linked to the product/feature that caused the contact
- **Calculation**: % of tickets with a valid product tag (validated by sampling)
- **Target**: High — poor tagging undermines the entire Insight & Prevention domain
- **Flywheel domain**: Insight & Prevention (Domain 5)
- **Frequency**: Monthly
- **Why It Matters**: If tickets aren't tagged to products accurately, the contact reduction programme cannot function

### Top Contact Reasons Fixed by Product (Quarterly)
- **Definition**: Of the top X contact drivers identified each quarter, what % had a product fix committed and delivered
- **Calculation**: (Contact drivers with confirmed fix / Top X drivers identified) × 100
- **Target**: Increasing over time
- **Flywheel domain**: Insight & Prevention (Domain 5)
- **Frequency**: Quarterly
- **Why It Matters**: Measures the effectiveness of the contact reduction programme end-to-end — not just identification, but actual resolution

## Support Quality Metrics

### First Contact Resolution (FCR)
- **Definition**: Percentage of tickets resolved in first interaction
- **Calculation**: (Tickets resolved in 1 interaction / Total tickets) × 100
- **Target**: [e.g., > 70%]
- **Frequency**: Weekly, Monthly
- **Why It Matters**: Higher FCR = better efficiency and customer experience

### Reopen Rate
- **Definition**: Percentage of tickets reopened after closure
- **Calculation**: (Reopened tickets / Total closed tickets) × 100
- **Target**: [e.g., < 10%]
- **Frequency**: Weekly, Monthly
- **Why It Matters**: High reopen rate indicates quality issues with initial resolution

### Customer Satisfaction (CSAT)
- **Definition**: Percentage of satisfied customers based on post-ticket survey
- **Calculation**: (Positive responses / Total responses) × 100
- **Target**: [e.g., > 90%]
- **Frequency**: Weekly, Monthly
- **Why It Matters**: Direct measure of customer happiness with support

### Escalation Rate
- **Definition**: Percentage of tickets requiring escalation to L2/L3 or engineering
- **Calculation**: (Escalated tickets / Total tickets) × 100
- **Target**: [e.g., < 15%]
- **Frequency**: Weekly, Monthly
- **Why It Matters**: Indicates knowledge gaps, training needs, or product complexity

### SLA Compliance
- **Definition**: Percentage of tickets meeting SLA targets
- **Calculation**: (Tickets meeting SLA / Total tickets) × 100
- **Target**: > 95%
- **Frequency**: Daily, Weekly
- **Why It Matters**: Contractual commitment and customer trust

## Product Impact Metrics

### AI Resolution Rate
- **Definition**: Percentage of AI Agent conversations resolved without reaching a human agent
- **Calculation**: (Conversations resolved by AI without human involvement / Total AI conversations) × 100
- **Target**: Continuously increasing (track by topic/category)
- **Frequency**: Daily, Weekly, Monthly
- **Why It Matters**: 
  - Higher AI resolution rate = lower cost per contact
  - Indicates AI Agent effectiveness
  - Key driver of support scalability
- **Breakdown By**:
  - Topic/category (which types of issues AI handles well)
  - Customer segment
  - Time of day / day of week

### Self-Service Deflection Rate
- **Definition**: Percentage of users finding answers via help docs (vs. creating contact)
- **Calculation**: (Help article views by unique users / (Help views + New contacts)) × 100
- **Target**: Continuously increasing
- **Frequency**: Monthly
- **Why It Matters**: 
  - Indicates effectiveness of documentation
  - Lower cost than AI or human agent
  - Reduces contact rate directly
- **Resources**:
  - support.checkout.com (FAQs and help articles)
  - checkout.com/docs (integration docs)
  - api-reference.checkout.com (API reference)

### Feature-Related Tickets
- **Definition**: Number of tickets related to specific feature or product area
- **Calculation**: Count of tickets tagged with feature
- **Target**: Trending down after feature improvements
- **Frequency**: Weekly, Monthly
- **Why It Matters**: 
  - Identifies problem areas needing product attention
  - Quantifies impact of product quality issues on contact rate
  - Helps prioritize root cause elimination efforts

### Root Cause Elimination Impact
- **Definition**: Reduction in contacts after fixing underlying product issue
- **Calculation**: (Tickets before fix - Tickets after fix) / Tickets before fix × 100
- **Target**: Varies by issue (aim for 50%+ reduction)
- **Frequency**: Tracked per fix, aggregated quarterly
- **Why It Matters**: 
  - Demonstrates ROI of product improvements
  - Validates prioritization decisions
  - Shows compounding benefit over time

### Time Saved by Tools
- **Definition**: Estimated hours saved by support tools and automation
- **Calculation**: (Automated resolutions × avg. handle time) / 60
- **Target**: Increasing over time
- **Frequency**: Monthly, Quarterly
- **Why It Matters**: Quantifies ROI of product improvements

### Documentation Usage
- **Definition**: Views of help articles and documentation
- **Calculation**: Page views, unique visitors, time on page
- **Target**: High traffic on key articles
- **Frequency**: Weekly, Monthly
- **Why It Matters**: Shows what information merchants need most

## Business Impact Metrics

### Support Cost Breakdown by Channel
- **Definition**: Cost per contact by support channel
- **Calculation**: Channel costs / Contacts handled in that channel
- **Benchmarks** (typical industry ranges):
  - AI Agent: $0.10 - $0.50 per resolution
  - Self-service (docs): $0.05 - $0.10 per view
  - Email support: $5 - $15 per ticket
  - Chat support: $3 - $10 per conversation
  - Phone support: $15 - $40 per call (future)
- **Target**: Shift volume to lower-cost channels while maintaining quality
- **Frequency**: Monthly, Quarterly
- **Why It Matters**: 
  - Identifies opportunities for channel optimization
  - Drives investment in automation and AI
  - Informs pricing and capacity planning

### Revenue at Risk
- **Definition**: Transaction volume from merchants with open critical issues
- **Calculation**: Sum of monthly volume for affected merchants
- **Target**: Minimize through quick resolution
- **Frequency**: Weekly (for active incidents)
- **Why It Matters**: Quantifies business impact of support issues

### Churn Influenced by Support
- **Definition**: Merchants who churned citing support issues
- **Calculation**: Count and revenue from churned merchants
- **Target**: < [Define threshold]
- **Frequency**: Monthly, Quarterly
- **Why It Matters**: Support quality impacts retention

### Merchant NPS (Net Promoter Score)
- **Definition**: Likelihood of merchant to recommend Checkout.com
- **Calculation**: % Promoters - % Detractors
- **Target**: [e.g., > 50]
- **Frequency**: Quarterly
- **Why It Matters**: Overall satisfaction and loyalty metric

## Operational Metrics

### Agent Utilization
- **Definition**: Percentage of agent time actively working on tickets
- **Calculation**: (Active ticket time / Total work time) × 100
- **Target**: [e.g., 70-80%]
- **Frequency**: Weekly
- **Why It Matters**: Balance productivity with avoiding burnout

### Knowledge Base Health
- **Definition**: Percentage of articles reviewed and updated recently
- **Calculation**: (Articles updated in last 90 days / Total articles) × 100
- **Target**: > 80%
- **Frequency**: Monthly
- **Why It Matters**: Outdated documentation creates support burden

### Bug Fix Cycle Time
- **Definition**: Time from bug reported to fix deployed
- **Calculation**: Median time across all bugs
- **Target**: [e.g., < 2 weeks for P1/P2]
- **Frequency**: Monthly
- **Why It Matters**: Speed of resolving recurring support issues

## P&L Reporting for Care/Support Product

### Context

Across the Product department, each team is required to justify investment through a P&L lens. Care/Support sits firmly on the **Loss (L)** side — it is a cost centre that does not directly generate revenue. However, it **protects revenue** by retaining merchants, resolving issues that would otherwise cause churn, and preventing compliance failures.

The goal is to:
1. Report the 'L' transparently with the right unit economics, not just absolute spend
2. Demonstrate a clear reduction trajectory — showing that investment in product, AI, and automation is bending the cost curve down
3. Provide the narrative for *why* the L is worth it (revenue protection, not just cost)


### What Belongs Under 'L' for Care/Support

| Cost Category | Examples | Notes |
|---|---|---|
| **Headcount** | Human agents, support ops, PM/PD/DS in Care Product | Largest L item; track as $/contact and $/transaction |
| **Tooling & Platforms** | Zendesk, Fin AI agent, diagnostic tools, internal dashboards | Fixed cost; amortise over contact volume |
| **AI & Infrastructure** | LLM API costs, Reflex compute, MCP/data infra | Variable with volume; cost/contact is a fraction of human handling |
| **Knowledge & Content** | Content team time, doc production | Preventive investment — deflects future human-handled contacts |


### How to Report Under 'L': Unit Economics, Not Absolute Spend

Reporting raw headcount cost alone will always grow with transaction volume unless normalised. The right lens is **unit cost decreasing over time**, even if absolute cost holds steady or grows slightly as Checkout.com scales.

#### Primary P&L Metric: Support Cost per $1M Processed

> **Formula**: Total support spend (headcount + tooling + AI) ÷ Total payment volume ($) × 1,000,000

This is the most defensible 'L' metric for a payments business because:
- It normalises against business growth — more transactions mean more revenue, so measuring cost against volume is fair
- A declining number proves efficiency gains even as the business scales
- Directly ties the cost of support to the company's core output ($300B+ processed in 2025)

#### Supporting P&L Metrics

| Metric | Why it matters for P&L | Direction |
|---|---|---|
| **Cost per contact** | Per-unit efficiency; the clearest signal of operational improvement | ↓ Target decreasing |
| **Contact rate (per 1M txns)** | Demand-side reduction via product quality and self-service; measures how much of the 'L' can be structurally eliminated | ↓ Target decreasing |
| **AI vs human cost split** | Demonstrates channel shift toward lower-cost resolution (AI: ~$0.10–0.50 vs human email: ~$5–15) | AI % ↑ |
| **Human-handled contacts as % of total** | Shows automation absorbing incremental volume without headcount growth | ↓ Target decreasing |
| **Estimated cost avoidance ($, quarterly)** | Contacts *not raised* due to product fixes; quantifies ROI of Reflex and contact reduction programme | ↑ Increasing |


### Suggested Quarterly P&L Reporting Format

| Metric | Q-2 Actual | Q-1 Actual | This Q Actual | Target / Trend |
|---|---|---|---|---|
| Total support cost ($) | | | | Tracked; absolute may grow |
| Support cost per $1M processed | | | | ↓ Decreasing |
| Cost per contact | | | | ↓ Decreasing |
| AI resolution rate % | | | | ↑ Increasing |
| Contact rate (contacts per 1M txns) | | | | ↓ Decreasing |
| Human-handled contacts % of total | | | | ↓ Decreasing |
| Estimated cost avoidance ($) | | | | ↑ Increasing |
| Headcount (agents + product) | | | | Flat or sub-linear vs volume growth |


### The Reduction Story: Narrative for Leadership

The framing when presenting the 'L' to senior stakeholders:

1. **Absolute cost may grow** as we scale (more merchants onboarding, B2C expansion in 2027) — this is expected and acceptable
2. **Unit cost must fall** — cost per contact and cost per $1M processed should decrease quarter-on-quarter; this is the headline
3. **Levers already in flight to drive that reduction**:
   - **AI deflection (Fin)**: Absorbing volume at <$0.50/contact vs $5–15 for human-handled; AI resolution rate is a leading indicator
   - **Reflex (contact reduction)**: Root cause fixes reduce contact rate at source — each fix has a lasting, compounding cost reduction
   - **Agent tooling**: Reducing AHT means fewer minutes of human cost per ticket
   - **Self-service docs**: Pre-contact resolution absorbs demand before it enters the cost base
4. **Long-term: support scales non-linearly** — as the flywheel matures, contact volume grows materially slower than transaction volume because of compounding product quality improvements


### Reframing the 'L': Support as Revenue Protection

When presenting to leadership, layer in the revenue-protection argument alongside the cost narrative:

| Mechanism | Revenue impact | Segment relevance |
|---|---|---|
| **Churn prevention** | Merchants with unresolved issues churn; fast, high-quality support retains transaction volume | **Most relevant for SMB B2B and B2C** — see note below |
| **NPS → expansion** | Satisfied merchants expand payment volume and refer other enterprise accounts | Enterprise and mid-market |
| **Compliance risk mitigation** | Support prevents regulatory failures (SCA, PSD3, KYC) that could cause merchant offboarding or fines | All segments |
| **Incident response** | Rapid support during outages protects the revenue at risk metric for affected merchants | All segments, highest $ impact for enterprise |

This does not move support out of the L column, but it justifies the level of investment and explains why cutting the L too aggressively has revenue-side consequences.

#### Note: Churn Prevention by Segment

The churn prevention argument strengthens materially as Checkout.com moves into SMB B2B and B2C:

- **Enterprise (current primary focus)**: Churn is rarely caused by support quality alone. Long contracts, high switching costs, dedicated account managers, and commercial relationships act as retention buffers. Support quality matters but is one factor among many.
- **SMB/Mid-market B2B**: Smaller merchants have lower switching costs, no dedicated account management layer, and are more likely to leave if they hit a wall on support. Support experience becomes a more direct churn signal.
- **B2C (personal.checkout.com — 2027 expansion)**: Consumers have near-zero switching costs and no commercial relationship. A single bad support interaction can cause immediate churn with no recovery opportunity. At consumer scale, even small churn rates represent significant volume loss.

**Implication for P&L reporting**: The churn prevention revenue argument should be weighted carefully today (enterprise-heavy book), but should be built into the investment case for SMB and B2C from the outset — both to justify support investment in those segments and to establish the measurement baseline (churn rate correlated with support experience) before they scale.


## How to Use These Metrics

### Daily/Weekly Reviews
Focus on:
- **Contact rate trends**: Spikes or unusual patterns
- **AI resolution rate**: Daily performance by category
- **Response times and SLA compliance**
- **Top contact drivers**: What's generating volume
- **Urgent escalations**: Issues needing immediate attention

### Monthly Reviews
Focus on:
- **North Star Metrics**: Contact rate & cost per contact trends
- **Channel performance**: AI vs. human-handled breakdown
- **Quality metrics**: FCR, CSAT, reopen rate
- **Efficiency metrics**: Handle time, agent productivity
- **Root cause analysis**: Top drivers of contact rate
- **Self-service performance**: Documentation usage and effectiveness

### Quarterly Business Reviews
Focus on:
- **North Star Metrics YoY/QoQ**: Progress toward targets
- **ROI of initiatives**: 
  - Contact reduction from product fixes
  - AI deflection improvements
  - Cost savings from automation
- **Strategic roadmap impact**: Feature improvements driving metric changes
- **Channel strategy**: Shift to lower-cost channels
- **Future planning**: 2027 B2C preparation
- **Capacity and budget planning**

### 2027 Transition Planning
Track additional metrics for B2C readiness:
- Mobile support readiness
- Phone channel cost modeling
- Consumer vs. merchant contact patterns
- Scale requirements and infrastructure needs

### Dashboards
Create different views for:
- **Support Team**: Real-time operational metrics
- **Product Management**: Feature and quality trends
- **Leadership**: Business impact and strategic metrics


**Last Updated**: [Date]
**Owner**: Charlie Wildish

**Note**: Targets should be reviewed quarterly and adjusted based on team maturity, product changes, and business priorities.
