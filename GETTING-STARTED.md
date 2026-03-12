# Getting Started with Your PM Workspace

Welcome! This guide will help you start using your AI-enhanced PM workspace effectively.

**Principle:** All your work should relate back to strategy, goals and metrics at the top (strategic goals: reduce contact rate, reduce cost; north star metrics: contact rate, cost per contact; 2026 deliverables and flywheel domains). See `2026 deliverables.md` and `01-knowledge-base/metrics/kpi-definitions.md`. When drafting or reviewing anything, tie it to the relevant goal, deliverable, or metric.

## ⏱️ 5-Minute Quick Start

### 1. Understand What You Have (2 min)

Your workspace is organized into 5 main directories:

- **`.cursor/rules/`**: Context for Claude about your role and domain
- **`01-knowledge-base/`**: Reference information (products, processes, payment concepts)
- **`02-workflows/`**: Step-by-step guides for common PM tasks
- **`03-templates/`**: Document templates you'll use frequently
- **`04-active-work/`**: Your current projects and tasks
- **`05-archive/`**: Completed work

### 2. Try Your First Task (3 min)

**Pick one based on what you need right now**:

#### Option A: Analyze Some Support Tickets
1. Open `02-workflows/ticket-analysis.md`
2. Follow the workflow steps
3. Use `03-templates/ticket-analysis-template.md` for your report
4. Ask Claude: "Help me analyze these support tickets: [paste data or summary]"

#### Option B: Write a Stakeholder Update
1. Open `03-templates/stakeholder-update-template.md`
2. Copy it to `04-active-work/stakeholder-updates/`
3. Ask Claude: "Help me draft a weekly update for [project name]. Here's what happened this week: [summary]"

#### Option C: Start a Requirements Doc
1. Open `03-templates/prd-template.md`
2. Copy it to `04-active-work/roadmap-items/[your-feature]/`
3. Ask Claude: "Help me write requirements for [feature description]"


## 🎯 First Week Checklist

### Day 1: Setup & Familiarization
- [ ] Read through `README.md` (you're almost done!)
- [ ] Browse the `01-knowledge-base/` to see what's available
- [ ] Review `.cursor/rules/context.mdc` - does it accurately describe your role?
- [ ] Skim through available templates in `03-templates/`

### Day 2: Add Your Context
- [ ] Update `.cursor/rules/context.mdc` with specific stakeholders and team details
- [ ] Add any existing product docs to `01-knowledge-base/products/`
- [ ] Document any custom processes in `01-knowledge-base/processes/`
- [ ] Create a list of key metrics you track in `01-knowledge-base/metrics/`

### Day 3: Use Your First Template
- [ ] Pick a template you use often (PRD, user story, update)
- [ ] Create a real document using it
- [ ] Ask Claude to help you draft or review it
- [ ] Note what works and what needs customization

### Day 4: Follow Your First Workflow
- [ ] Choose a workflow that matches your current work
- [ ] Follow it step-by-step for a real task
- [ ] Use the checklist at the end
- [ ] Adjust the workflow if needed for your situation

### Day 5: Organize Your Active Work
- [ ] Create folders in `04-active-work/` for current projects
- [ ] Move or create documents for things you're working on
- [ ] Set up a structure that makes sense for your workflow
- [ ] Archive any old documents to `05-archive/`


## 💬 Working with Claude

### Essential Commands

**Get Help with a Process**:
> "Walk me through analyzing support tickets"
> 
> "What's the workflow for writing requirements?"

**Draft Documents**:
> "Draft a PRD for [feature] using the template"
> 
> "Help me write a stakeholder update. Here's what happened this week: [summary]"

**Understand Concepts**:
> "Explain how payment authorization and capture work"
> 
> "What's the difference between a chargeback and a refund?"

**Review Your Work**:
> "Review this PRD and tell me what's missing"
> 
> "Is this user story well-written? How can I improve it?"

**Analyze Data**:
> "Here's our ticket data for the past month [data]. What patterns do you see?"
> 
> "These metrics changed this week [data]. What should I investigate?"

### Tips for Better Results

**✅ Be Specific**:
- ❌ "Help with this"
- ✅ "Review this PRD for a password reset feature and check if the security requirements are complete"

**✅ Provide Context**:
- Mention which template or workflow you're using
- Share relevant data or examples
- Explain constraints or requirements

**✅ Reference the Knowledge Base**:
- "Using the ticket analysis workflow, help me understand these trends..."
- "Based on our PSP fundamentals doc, explain this to a non-technical stakeholder"

**✅ Iterate**:
- Start with a draft
- Ask for specific improvements
- Request alternatives if the first attempt isn't quite right


## 🛠️ Customization Guide

### Week 1-2: Use as-is
Don't customize yet—use the default structure to understand what works for you.

### Week 3-4: Light Customization
- Add your specific product information to knowledge base
- Update context rules with real stakeholders and processes
- Adjust templates to match your preferred format
- Create shortcuts or bookmarks to frequently used files

### Month 2+: Deep Customization
- Add new workflows for your specific needs
- Create custom templates for unique deliverables
- Reorganize directories to match your mental model
- Build out knowledge base with team-specific information

### What to Customize

**Definitely Customize**:
- `.cursor/rules/context.mdc` - Make it specific to you
- `01-knowledge-base/products/` - Add your actual products
- `01-knowledge-base/processes/` - Document your real processes
- Template headers and sections - Match your org's style

**Probably Customize**:
- Workflow steps - Adjust for your team's process
- Directory structure in `04-active-work/` - Organize how you think
- Knowledge base categories - Add sections for your domain

**Maybe Don't Customize** (at least not yet):
- Core workflow principles - They're based on best practices
- Template structure - Standard sections exist for good reasons
- Overall directory organization - Works for most PM workflows


## 📚 Learning Resources

### Included in This Workspace

**Understanding Payments**:
- `01-knowledge-base/payment-domain/psp-fundamentals.md`
- `01-knowledge-base/payment-domain/common-issues.md`

**Support Processes**:
- `01-knowledge-base/processes/support-workflows.md`
- `01-knowledge-base/processes/incident-response.md`

**PM Best Practices**:
- `02-workflows/requirement-writing.md`
- `02-workflows/stakeholder-updates.md`

### How to Learn Each Area

**For Payment Domain Knowledge**:
1. Read `psp-fundamentals.md` cover-to-cover
2. Ask Claude to quiz you on key concepts
3. Apply it: Explain a payment flow in your next stakeholder update
4. Add new learnings as you discover them

**For PM Workflows**:
1. Skim workflow to understand overall process
2. Use it for a real task
3. Reference detailed steps as needed
4. Refine based on what works

**For Templates**:
1. Read through template once
2. Fill in for real project
3. Delete sections you don't need
4. Add sections you do need
5. Update master template with improvements


## 🚀 Success Milestones

### Week 1 ✅
- [ ] Used first template successfully
- [ ] Asked Claude for help on real work
- [ ] Started organizing active work directory

### Month 1 ✅
- [ ] Followed complete workflow end-to-end
- [ ] Created multiple documents using templates
- [ ] Added team-specific info to knowledge base
- [ ] Customized at least one template or workflow

### Month 3 ✅
- [ ] Using workspace as default for all PM docs
- [ ] Claude helps are significantly speeding up your work
- [ ] Knowledge base is growing with your learnings
- [ ] Shared workspace structure with team member

### Month 6 ✅
- [ ] Workspace is fully customized to your needs
- [ ] Created new workflows for your unique processes
- [ ] Archive has meaningful completed work
- [ ] Helped someone else set up their workspace


## ❓ FAQ

### "Where should I put [type of document]?"

**PRDs, specs, requirements** → `04-active-work/roadmap-items/[project-name]/`

**Status updates** → `04-active-work/stakeholder-updates/`

**Analysis reports** → `04-active-work/investigations/` or `current-sprint/`

**Reference docs** → `01-knowledge-base/[relevant-category]/`

**Completed work** → `05-archive/[year]/[quarter]/`

### "Do I need to use every template/workflow?"

No! Use what's helpful. If a template doesn't fit your needs, don't use it. If a workflow is overkill for a simple task, skip it.

### "Can I change the directory structure?"

Yes! This structure is a starting point. After using it for a few weeks, reorganize it to match how your brain works.

### "What if my company has different processes?"

Update the workflows and knowledge base to reflect your actual processes. The goal is to document how YOU work, not follow a rigid system.

### "How much should I document?"

Document things you'll reference again:
- Processes you repeat frequently
- Decisions that need context later
- Knowledge you had to learn the hard way

Don't document:
- One-off tasks
- Obvious information
- Things that change constantly

### "Should this be in version control (git)?"

**Good for git**:
- Templates (version them)
- Workflows (track improvements)
- Knowledge base (history of learnings)

**Maybe not for git**:
- Active work (changes too frequently)
- Personal notes
- Sensitive information

**Decision**: Start without git. Add it later if you need versioning, collaboration, or backup.


## 🆘 Troubleshooting

### "I can't find anything!"

**Solutions**:
- Use Cursor's file search (Cmd/Ctrl + P)
- Check the README in each directory
- Search for keywords across all files
- Create an index file in `04-active-work/` with links to current projects

### "It's taking too long to document everything"

**Remember**:
- Don't document everything—just what's useful
- Start with templates and fill them in as you work
- Use Claude to speed up documentation
- It's okay to have incomplete docs initially

### "My org's processes are different"

**That's expected!** 
- Update workflows to match reality
- Keep what works, delete what doesn't
- This is YOUR workspace—customize it

### "Claude doesn't understand my context"

**Check**:
- Have you updated `.cursor/rules/context.mdc`?
- Are you providing enough context in your questions?
- Have you added relevant domain knowledge to knowledge base?
- Try being more specific in your requests


## 🎉 You're Ready!

You now have everything you need to:
- ✅ Use templates to create documents faster
- ✅ Follow workflows for complex tasks
- ✅ Work with Claude as your AI PM assistant
- ✅ Build up your knowledge base over time
- ✅ Keep your active work organized

**Next step**: Pick one thing you're working on right now and try using this workspace for it!


**Questions?** Ask Claude! 
> "I'm new to this workspace. How should I get started with [specific task]?"

**Need help?** Check the main `README.md` or the README in each directory.

**Ready to dive in?** Start with whatever you're working on today! 🚀
