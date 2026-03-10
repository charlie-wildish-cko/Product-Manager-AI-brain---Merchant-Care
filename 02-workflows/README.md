# Workflows

Process documentation for repeatable PM tasks and best practices.

## Available Workflows

### 🔍 **ticket-analysis.md** - Support Ticket Analysis

Complete workflow for analyzing support ticket data to identify patterns and opportunities.

**When to use**: Weekly/monthly ticket reviews, investigation of support trends

**Key steps**:
- Data collection and quality checks
- Quantitative analysis (metrics, trends)
- Pattern identification and categorization
- Root cause analysis
- Prioritization and recommendations
- Stakeholder communication

**Time**: 2-4 hours for comprehensive monthly analysis


### 📝 **requirement-writing.md** - Requirements Writing

Step-by-step guide for writing clear, actionable product requirements.

**When to use**: Starting new features, documenting product changes

**Key steps**:
- Understanding the problem deeply
- Defining goals and success metrics
- Identifying users and use cases
- Writing user stories with acceptance criteria
- Defining functional and non-functional requirements
- Collaboration and refinement

**Output**: PRD, user stories, or concise specs depending on scope


### 👥 **document-review-panel.md** - Document Review Panel

Structured multi-perspective review using nine personas (PM, Engineering/Tech lead, Operations agent, CPO, COO, Product Data Scientist, Zendesk Administrator, Content Strategist, VP of Product). Persona definitions: `01-knowledge-base/processes/review-panel-personas.md`. Use to refine PRDs, reports, and memos before sharing.

**When to use**: Before finalising PRDs, status reports, or c-suite memos

**Key steps**: Apply each persona’s lens and questions; note gaps and edits; revise. Can be run solo (checklist), with AI (simulated panel), or with real reviewers.


### 📢 **stakeholder-updates.md** - Stakeholder Communication

Framework for creating effective regular updates for stakeholders.

**When to use**: Weekly, bi-weekly, or monthly project updates

**Key steps**:
- Defining audience and cadence
- Gathering information and metrics
- Structuring content (TL;DR, progress, blockers, asks)
- Adapting for different stakeholder groups
- Distribution and follow-up
- Tracking action items

**Output**: Written updates, presentations, or status reports


## How to Use These Workflows

### For New PM Tasks

1. **Identify which workflow applies** to your current task
2. **Read through the workflow** to understand the full process
3. **Follow the steps** sequentially
4. **Use the checklists** to ensure you don't miss anything
5. **Reference templates** linked in each workflow

### For Recurring Tasks

Once familiar with a workflow:
- Use the **Quick Reference Checklist** at the end
- Skip to relevant sections as needed
- Customize the process to fit your needs

### For Training

These workflows are useful for:
- Onboarding new PMs
- Training cross-functional team members
- Standardizing processes across teams
- Creating shared understanding of best practices

## Workflow Principles

All workflows in this directory follow these principles:

### 1. Start with Why
Every workflow explains when and why to use it

### 2. Be Comprehensive but Flexible
Cover all important steps, but allow for adaptation

### 3. Include Examples
Show good and bad examples to illustrate points

### 4. Be Action-Oriented
Focus on what to do, not just theory

### 5. Link to Resources
Connect to templates, tools, and related documentation

### 6. Continuous Improvement
Workflows evolve based on what works and what doesn't

## Creating Your Own Workflows

As you develop reliable processes, document them here:

### Structure to Follow

```markdown
# [Workflow Name]

## When to Use This Workflow
[Describe triggers and scenarios]

## Step 1: [Step Name]
[What to do]
[Why it matters]
[Tips and examples]

## Step 2: [Next Step]
...

## Quick Reference Checklist
- [ ] Key step 1
- [ ] Key step 2
...

## Tips & Best Practices
[Dos and don'ts]

## Common Pitfalls
[What to avoid]
```

## Complementary Resources

### Frameworks
- **Rumelt Strategy Kernel** (`01-knowledge-base/strategy/rumelt-strategy-kernel.md`) — for product/roadmap strategy, prioritisation, and executive narrative (Diagnosis → Guiding Policy → Coherent Actions).
- **Socratic questioning for PRDs** (`01-knowledge-base/processes/socratic-questioning-prds.md`) — for sharpening requirements and PRD review (problem clarity, solution validation, success criteria, scope, strategic fit).

### Templates
See `03-templates/` for document templates referenced in workflows

### Knowledge Base
See `01-knowledge-base/` for domain knowledge supporting these workflows

### Context Rules
See `.cursor/rules/` for AI assistant context on your role and domain

## Feedback & Improvement

Workflows should evolve based on experience:

**After using a workflow**:
- What worked well?
- What was confusing?
- What was missing?
- What could be streamlined?

**Update workflows when**:
- You discover a better approach
- Tools or processes change
- Team provides feedback
- Repeated issues arise


**Owner**: Charlie Wildish  
**Last Updated**: [Date]
