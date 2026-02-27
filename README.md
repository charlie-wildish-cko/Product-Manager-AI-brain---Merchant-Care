# Charlie PM Brain - Checkout.com Customer Support PM Workspace

Welcome to your AI-enhanced Product Management workspace! This directory is designed to help Claude assist you more effectively with your day-to-day PM work at Checkout.com.

## 🎯 What This Workspace Does

This workspace serves as:
- **Knowledge repository**: Domain knowledge about payments, PSPs, and customer support
- **Process documentation**: Your workflows and best practices
- **Template library**: Reusable formats for common deliverables
- **AI context**: Rules that help Claude understand your role and needs
- **Active workspace**: Where your current projects and work live

## 📁 Directory Structure

```
Charlie PM brain/
├── .cursor/rules/                        # AI context (role, domain, style, stakeholders)
│   ├── context.md                        # Role, team, goals, flywheel model, care tiers
│   ├── customer-support.md               # Support structure, channels, SLAs
│   ├── payment-domain.md                 # PSP fundamentals and terminology
│   └── communication-style.md            # Writing style by audience
│
├── 01-knowledge-base/                    # Domain knowledge and reference
│   ├── strategy/                         # Strategic frameworks and source docs
│   │   ├── care-product-model.md         # The Care Product flywheel (6-domain model)
│   │   ├── support-scale-principles.md   # Scaling principles to 2030
│   │   ├── competitive-support-audit-2026.md # Competitor support benchmarks (Stripe, Adyen, etc.)
│   │   └── care-success-plans-proposal.md# Source proposal for support tiers
│   ├── products/                         # Product reference docs
│   │   ├── merchant-segments.md          # All segments overview
│   │   ├── care-success-plans.md         # Tier model (Standard/Enterprise/Premium)
│   │   ├── platform-segment.md           # Platform/ISV deep-dive (primary 2026 focus)
│   │   ├── reflex.md                     # Reflex — AI contact insights product
│   │   └── checkout-products.md          # Checkout.com product overview
│   ├── processes/                        # Support process documentation
│   │   ├── support-workflows.md          # Ticket handling procedures
│   │   ├── ai-agent-operations.md        # Fin AI Agent operations
│   │   ├── incident-response.md          # Incident response process
│   │   └── known-challenges.md           # Known operational challenges
│   ├── payment-domain/                   # Payment industry knowledge
│   ├── metrics/                          # KPI definitions (flywheel-organised) + P&L reporting
│   ├── bigquery-queries/                 # Saved SQL query library
│   ├── checkout-business-context.md      # Company overview, product pillars, P&L context
│   ├── data-sources.md                   # All data source access and usage guide
│   └── teams.md                          # Internal team names and stakeholder groups
│
├── 02-workflows/                         # Step-by-step process guides
│   ├── ticket-analysis.md
│   ├── requirement-writing.md
│   ├── stakeholder-updates.md
│   └── integrated-analysis.md            # Multi-source analysis workflow
│
├── 03-templates/                         # Reusable document templates
│   ├── prd-template.md
│   ├── user-story-template.md
│   ├── stakeholder-update-template.md
│   ├── ticket-analysis-template.md
│   ├── rfc-template.md
│   └── postmortem-template.md
│
├── 04-active-work/                       # Current projects and work-in-progress
│   ├── roadmap-items/                    # PRDs and specs for features in flight
│   │   ├── fin-email-auth-data-policy-prd.md
│   │   ├── zendesk-org-domain-mapping-prd.md
│   │   └── blue-emi-zendesk-support-prd.md
│   └── fin-email-behaviour-spec.md
│
├── 05-archive/                           # Completed work
│
├── 2026 deliverables.md                  # 2026 product roadmap (goals, quarters, flywheel map)
└── README.md                             # You are here
```

## 🚀 Getting Started

### First Time Here?

1. **Review the Cursor rules** (`.cursor/rules/`) to see how Claude understands your role
2. **Browse the knowledge base** (`01-knowledge-base/`) to familiarize yourself with the structure
3. **Check out the templates** (`03-templates/`) for documents you'll create frequently
4. **Read the workflows** (`02-workflows/`) for process guidance

### Daily Usage

**When you need to...**

📝 **Write requirements** → Use `02-workflows/requirement-writing.md` + `03-templates/prd-template.md`

📊 **Analyze support tickets** → Follow `02-workflows/ticket-analysis.md` + use `03-templates/ticket-analysis-template.md`

📢 **Update stakeholders** → Follow `02-workflows/stakeholder-updates.md` + use `03-templates/stakeholder-update-template.md`

❓ **Understand payment concepts** → Reference `01-knowledge-base/payment-domain/`

🔧 **Handle support processes** → Check `01-knowledge-base/processes/`

📈 **Define or track metrics** → See `01-knowledge-base/metrics/kpi-definitions.md`

🔗 **Work with data sources** → See `01-knowledge-base/data-sources.md`

🔄 **Do integrated analysis** → Follow `02-workflows/integrated-analysis.md`

### Working with Claude

Claude has context about:
- Your role as Customer Support PM at Checkout.com
- Payment industry fundamentals and PSP concepts
- Common support workflows and processes
- Your communication style preferences

**Ask Claude to**:
- Draft documents using your templates
- Analyze ticket data you provide
- Answer questions about payment concepts
- Suggest approaches to PM challenges
- Review and improve your drafts
- Explain complex technical topics in simple terms

**Examples**:
> "Help me draft a PRD for a self-service password reset feature"

> "Analyze these ticket trends and identify the top 3 product opportunities"

> "Explain how 3D Secure works in simple terms for a stakeholder update"

> "Review this requirements doc and flag anything unclear or missing"

## 📂 Directory Details

### `.cursor/rules/` - AI Context

Rules that give Claude context about your work:

- **context.md**: Your role, responsibilities, stakeholders
- **payment-domain.md**: PSP and payment processing fundamentals
- **customer-support.md**: Support processes, escalations, metrics
- **communication-style.md**: How to communicate with different audiences

**When to update**: When your role changes, new processes are added, or you join new teams


### `2026 deliverables.md` - Active Roadmap

The 2026 product roadmap organised by goal (reduce contact rate / reduce cost of support), with quarterly delivery targets, flywheel domain mapping, and roadmap dependencies. Update as quarters progress and deliverables are refined.


### `01-knowledge-base/` - Domain Knowledge

Centralized reference information organized by topic:

**products/** - Checkout.com products and features
- Starter doc for product info (add your specific product details)
- Subdirectories for feature specs and integration guides

**processes/** - Internal workflows and procedures
- Support ticket handling workflows
- Incident response processes
- Release and deployment procedures

**payment-domain/** - Payment industry knowledge
- PSP fundamentals and payment flows
- Common payment issues and solutions
- Compliance and regulations

**metrics/** - KPIs and measurement
- Standard metric definitions
- Dashboard locations and links

**When to update**: As you learn new information, document it here for future reference


### `02-workflows/` - Process Documentation

Step-by-step guides for repeatable PM tasks:

- **ticket-analysis.md**: How to analyze support data
- **requirement-writing.md**: Writing clear, actionable requirements
- **stakeholder-updates.md**: Creating effective status updates

**When to add new workflows**: When you develop a reliable process you use repeatedly


### `03-templates/` - Document Templates

Reusable formats for common PM deliverables:

- **prd-template.md**: Product Requirements Document
- **user-story-template.md**: User story with acceptance criteria
- **stakeholder-update-template.md**: Regular status update
- **ticket-analysis-template.md**: Support data analysis
- **rfc-template.md**: Request for Comment
- **postmortem-template.md**: Incident postmortem

**How to use**: Copy template to your working directory, rename, and fill in


### `04-active-work/` - Current Projects

Your work-in-progress organized by type:

**current-sprint/** - Work for this sprint/week

**roadmap-items/** - Features being planned or built

**investigations/** - Deep dives on support issues or opportunities

**stakeholder-updates/** - Draft and sent updates

**How to organize**:
- Create subdirectory per major project/initiative
- Move to `05-archive/` when complete
- Keep this directory focused on active work only


### `05-archive/` - Completed Work

Historical projects and documentation:

- Completed PRDs and feature specs
- Past analysis reports
- Finished projects
- Deprecated documentation

**When to archive**: Once work is complete and no longer actively referenced


## 🛠️ Best Practices

### Keep It Current

This workspace is most valuable when it's up-to-date:
- Document new processes as you develop them
- Add learnings to knowledge base as you discover them
- Update metrics and definitions as they change
- Archive completed work regularly

### Link Liberally

Connect related documents:
- Link from PRDs to related user stories
- Reference knowledge base articles in updates
- Connect analysis reports to resulting features
- Cross-link workflows and templates

### Use Consistent Naming

Makes it easier to find things:
- Use date prefixes for time-based docs: `2024-02-18-weekly-update.md`
- Use descriptive names: `password-reset-prd.md` not `feature-doc.md`
- Keep naming conventions consistent across similar documents

### Customize for Your Needs

This structure is a starting point:
- Add directories for your specific needs
- Modify templates to match your style
- Adjust workflows based on what works
- Remove sections you don't use

### Review Periodically

**Monthly**: 
- Clean up `04-active-work/`
- Archive completed projects
- Update knowledge base with new learnings

**Quarterly**:
- Review and update templates
- Refresh workflows based on experience
- Update Cursor rules if role changes
- Audit metrics definitions for accuracy

## 💡 Tips for Success

### For Better AI Assistance

**Be specific in your requests**:
- ❌ "Help me with this feature"
- ✅ "Draft a PRD for multi-currency refunds using our template"

**Provide context**:
- Reference relevant knowledge base articles
- Share data or examples
- Explain constraints or requirements

**Iterate together**:
- Start with a draft and refine
- Ask for specific improvements
- Request alternative approaches

### For Better Documentation

**Write for your future self**:
- Will you understand this in 6 months?
- Is the rationale clear?
- Are decisions documented?

**Include examples**:
- Real ticket IDs
- Actual error messages
- Specific merchant scenarios

**Update timestamps**:
- Mark "Last Updated" dates
- Note when information may be stale

### For Better Collaboration

**Make it accessible**:
- Clear headers and structure
- Concise language
- Links to source materials

**Share appropriately**:
- Not everything needs wide distribution
- Sensitive info stays internal
- Public-facing docs in separate location

## 📚 Additional Resources

### Checkout.com Resources
- [Add links to internal wiki, docs, dashboards]
- [Ticketing system]
- [Analytics platform]
- [Product roadmap]

### External Learning
- [Payment industry resources]
- [Product management communities]
- [Support best practices]

## 🤝 Feedback & Improvements

This workspace should evolve based on your needs:

**What's working?** Keep doing it!

**What's not working?** Change it!

**What's missing?** Add it!

The goal is to make your PM work more efficient and effective. Customize this structure to match your workflow and preferences.


## Quick Reference

### Most Used Commands

**Ask Claude**:
- "Walk me through the ticket analysis workflow"
- "Draft a stakeholder update for [project]"
- "Help me write requirements for [feature]"
- "Explain [payment concept] in simple terms"

**Common Files**:
- Payment fundamentals: `01-knowledge-base/payment-domain/psp-fundamentals.md`
- Support workflows: `01-knowledge-base/processes/support-workflows.md`
- Metric definitions: `01-knowledge-base/metrics/kpi-definitions.md`
- PRD template: `03-templates/prd-template.md`

### Next Steps

1. ✅ Workspace structure created
2. 📝 Start adding your existing documentation to knowledge base
3. 🎯 Use templates for your next deliverable
4. 🔄 Follow workflows for your next analysis or requirement
5. 🚀 Iterate and improve based on what works!


**Workspace Owner**: Charlie Wildish  
**Role**: Product Manager, Customer Support  
**Company**: Checkout.com  
**Last Updated**: February 18, 2026

**Questions or suggestions?** Update this README or the relevant section directly!
