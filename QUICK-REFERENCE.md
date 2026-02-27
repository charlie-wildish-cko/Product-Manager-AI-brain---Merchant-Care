# Quick Reference Card

## 📂 Where to Find Things

| I Need... | Location |
|-----------|----------|
| **2026 roadmap** | `2026 deliverables.md` |
| Care product flywheel model | `01-knowledge-base/strategy/care-product-model.md` |
| Scaling principles to 2030 | `01-knowledge-base/strategy/support-scale-principles.md` |
| Competitor support benchmarks | `01-knowledge-base/strategy/competitive-support-audit-2026.md` |
| Support tier model (SLAs, channels) | `01-knowledge-base/products/care-success-plans.md` |
| All merchant segments | `01-knowledge-base/products/merchant-segments.md` |
| Platform / ISV segment detail | `01-knowledge-base/products/platform-segment.md` |
| Reflex — contact insights product | `01-knowledge-base/products/reflex.md` |
| Checkout.com company overview + P&L context | `01-knowledge-base/checkout-business-context.md` |
| Metric definitions + P&L reporting | `01-knowledge-base/metrics/kpi-definitions.md` |
| Data sources & access | `01-knowledge-base/data-sources.md` |
| Team names (for PRDs / docs) | `01-knowledge-base/teams.md` |
| Support process docs | `01-knowledge-base/processes/` |
| Fin AI Agent operations | `01-knowledge-base/processes/ai-agent-operations.md` |
| Payment concepts explained | `01-knowledge-base/payment-domain/` |
| How to analyze tickets | `02-workflows/ticket-analysis.md` |
| How to do integrated analysis | `02-workflows/integrated-analysis.md` |
| How to write requirements | `02-workflows/requirement-writing.md` |
| How to update stakeholders | `02-workflows/stakeholder-updates.md` |
| PRD template | `03-templates/prd-template.md` |
| User story template | `03-templates/user-story-template.md` |
| Update template | `03-templates/stakeholder-update-template.md` |
| Analysis template | `03-templates/ticket-analysis-template.md` |
| Active PRDs | `04-active-work/roadmap-items/` |
| Past projects | `05-archive/` |

## 🤖 Claude Quick Commands

```
"Help me draft a PRD for [feature]"

"Walk me through the ticket analysis workflow"

"Explain [payment concept] in simple terms"

"Review this requirements doc - what's missing?"

"Draft a stakeholder update. Here's what happened: [summary]"

"Analyze these ticket trends: [data or description]"

"Write user stories for [feature description]"

"What questions should I ask about [topic]?"

"Analyze this BigQuery data: [paste results]"

"Help me synthesize insights from these sources: [paste data]"
```

## 📝 Common Tasks

### Working with Data Sources
1. Check `01-knowledge-base/data-sources.md` for access info
2. Pull data from BigQuery, Airtable, etc.
3. Follow `02-workflows/integrated-analysis.md`
4. Paste data into Claude for analysis

### Analyzing Support Tickets
1. Follow `02-workflows/ticket-analysis.md`
2. Use template: `03-templates/ticket-analysis-template.md`
3. Save to: `04-active-work/investigations/` or `current-sprint/`

### Writing Requirements
1. Follow `02-workflows/requirement-writing.md`
2. Use template: `03-templates/prd-template.md`
3. Save to: `04-active-work/roadmap-items/[project]/`

### Sending Status Update
1. Follow `02-workflows/stakeholder-updates.md`
2. Use template: `03-templates/stakeholder-update-template.md`
3. Save to: `04-active-work/stakeholder-updates/`

### Starting New Project
1. Create folder: `04-active-work/roadmap-items/[project-name]/`
2. Copy relevant templates
3. Update `.cursor/rules/` if needed (new processes, stakeholders)

### Archiving Completed Work
1. Add completion metadata to documents
2. Move to: `05-archive/[year]/[quarter]/`
3. Update any links in active documents

### Sharing PRDs, reports & notes (preferred channels)
- **Google Doc** – collaborative docs, live editing
- **Slack** – quick shares, threads, channels
- **Gmail** – formal or external, email updates
- **Confluence** – durable docs, status reports, team knowledge

## 🎯 Workflow Checklists

### Quick Ticket Analysis
- [ ] Define time period and scope
- [ ] Export data from ticketing system
- [ ] Calculate core metrics (volume, response time, etc.)
- [ ] Categorize and identify patterns
- [ ] Perform root cause analysis
- [ ] Generate prioritized recommendations
- [ ] Share with stakeholders

### Quick Requirements Doc
- [ ] Understand the problem (who, what, when, where, why)
- [ ] Define goals and success metrics
- [ ] Write user stories with acceptance criteria
- [ ] List functional requirements (P0, P1, P2)
- [ ] Define non-functional requirements
- [ ] State what's out of scope
- [ ] Get stakeholder review
- [ ] Maintain and update as you learn

### Quick Stakeholder Update
- [ ] Gather progress and metrics
- [ ] Draft TL;DR (top 3 things)
- [ ] List completed items
- [ ] List in-progress work
- [ ] Call out blockers and help needed
- [ ] Review and edit
- [ ] Distribute and track action items

## 💡 Tips

### For Better AI Help
- Be specific in requests
- Provide context and examples
- Reference relevant knowledge base docs
- Iterate on drafts together

### For Better Documentation
- Write for your future self
- Include examples and links
- Update timestamps
- Keep it concise

### For Better Organization
- Use consistent naming
- Clean up weekly
- Archive monthly
- Link related docs

## ⚡ Keyboard Shortcuts (Cursor)

```
Cmd/Ctrl + P       → Quick file search
Cmd/Ctrl + Shift + F → Search across all files
Cmd/Ctrl + Click   → Follow links
Cmd/Ctrl + K       → Open AI chat
```

## 📞 Key Stakeholders

> Update this section in `.cursor/rules/context.md` with your actual stakeholders

- **Support Leadership**: [Names]
- **Engineering Leads**: [Names]
- **Product Leadership**: [Names]
- **Design/UX**: [Names]
- **Operations**: [Names]

## 📊 Key Metrics to Track

> See full definitions in `01-knowledge-base/metrics/kpi-definitions.md`

**Support Efficiency**:
- Ticket volume
- First response time
- Time to resolution
- Backlog size

**Support Quality**:
- First contact resolution
- Reopen rate
- CSAT score
- Escalation rate

**Product Impact**:
- Feature-related tickets
- Ticket deflection rate
- Documentation usage

## 🔗 Important Links

> Add your actual links here

**Support Systems**:
- **Zendesk**: [URL]
- **Intercom Fin AI**: [URL]
- **Support Portal**: support.checkout.com
- **Technical Docs**: checkout.com/docs
- **API Reference**: api-reference.checkout.com

**Data & Analysis**:
- **BigQuery Console**: [URL]
- **Analytics Dashboard**: [URL]
- **Metrics Dashboard**: [URL]

**Documentation**:
- **Confluence**: [URL]
- **Google Drive**: [URL]
- **GitHub Repo**: [URL]

**Research & Planning**:
- **Airtable (Research)**: [URL]
- **Product Roadmap**: [URL]
- **Team Wiki**: [URL]


**💾 Bookmark this file for quick access!**

For detailed information, see `README.md` or `GETTING-STARTED.md`
