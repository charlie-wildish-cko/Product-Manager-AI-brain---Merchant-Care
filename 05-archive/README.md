# Archive

This directory contains completed projects, historical documentation, and deprecated materials.

## Purpose

The archive serves as:
- **Historical record**: Reference past projects and decisions
- **Learning resource**: See what worked and what didn't
- **Audit trail**: Document evolution of products and processes
- **Declutter active workspace**: Keep current work focused

## What to Archive

### Completed Projects
- Shipped features (PRDs, specs, user stories)
- Finished investigations
- Resolved initiatives

### Historical Documents
- Past quarterly plans
- Old process documentation (when superseded)
- Previous versions of templates
- Outdated product specs

### Campaign/Time-Bound Work
- Past stakeholder updates
- Specific event responses (incidents, launches)
- Seasonal initiatives

## What NOT to Archive

### Keep in Knowledge Base Instead
- Current process documentation
- Active product specs
- Valid metric definitions
- Useful reference material

## Organization

### Organize by Year and Quarter

```
05-archive/
├── 2024/
│   ├── Q1/
│   │   ├── projects/
│   │   ├── updates/
│   │   └── investigations/
│   └── Q2/
│       └── ...
├── 2025/
│   └── Q1/
│       └── ...
└── README.md
```

### Or by Project

```
05-archive/
├── password-reset-feature/
│   ├── prd.md
│   ├── user-stories.md
│   ├── launch-retrospective.md
│   └── final-metrics.md
├── dashboard-redesign-2024/
│   └── ...
└── README.md
```

### Or by Type

```
05-archive/
├── completed-features/
├── investigations/
├── stakeholder-updates/
└── deprecated-docs/
```

**Choose what works for you!** Consistency matters more than the specific structure.

## When to Archive

### Regular Schedule
- **Weekly**: Old drafts and superseded documents
- **Monthly**: Completed sprint work
- **Quarterly**: Finished projects and initiatives

### Triggers
- Feature launched and stable (30+ days)
- Investigation completed and recommendations implemented
- Document replaced by newer version
- Project cancelled or deprioritized indefinitely

## How to Archive

### Before Moving

**Add closing metadata**:
```markdown

Status: Completed / Cancelled / Superseded
Completion Date: 2024-02-15
Outcome: [Brief summary of result]
Lessons Learned: [Key takeaways]
Related Documents: [Links to relevant files]

```

### Moving Process

1. **Create archive structure** (if doesn't exist)
2. **Add completion metadata** to documents
3. **Move files** to appropriate archive location
4. **Update any links** in active documents
5. **Note in archive index** (optional)

### Archive Index

For large archives, maintain an index:

```markdown
# Archive Index - 2024 Q1

## Completed Projects
- **Password Reset Feature**: Self-service password reset for merchants
  - Location: `2024/Q1/projects/password-reset/`
  - Outcome: Reduced password reset tickets by 85%
  - Shipped: March 2024

## Key Investigations
- **Settlement Delays**: Root cause analysis of payment settlement issues
  - Location: `2024/Q1/investigations/settlement-delays.md`
  - Outcome: Identified and fixed configuration issue

## Major Updates
- Weekly updates: `2024/Q1/updates/weekly/`
- Monthly summaries: `2024/Q1/updates/monthly/`
```

## Accessing Archive

### When to Reference

**Review archives when**:
- Planning similar projects
- Need context on past decisions
- Writing retrospectives
- Onboarding new team members
- Preparing performance reviews
- Conducting postmortems

### Search Tips

**Use Cursor/IDE search** across archive:
- Search for similar problems: "authentication error"
- Find past decisions: "decision" or "we chose"
- Locate metrics: "baseline" or "target"
- Review outcomes: "lessons learned" or "retrospective"

## Cleanup & Maintenance

### Periodic Review

**Annually**:
- Remove very old drafts (> 3 years)
- Consolidate redundant documents
- Extract valuable learnings into knowledge base
- Update archive index

### What to Keep Forever

- **Completed feature PRDs**: Historical record
- **Major incident postmortems**: Lessons learned
- **Strategic decisions**: Context for future
- **Successful investigations**: Methodology reference

### What to Delete

- **Abandoned drafts**: Never completed, no value
- **Duplicate copies**: Keep only final version
- **Superseded processes**: If no historical value
- **Very old meeting notes**: Unless decisions recorded

## Tips for Useful Archives

### ✅ Do's

**Document outcomes**: Why archive if you don't record the result?

**Keep related items together**: PRD + user stories + launch retro in same folder

**Add searchable metadata**: Tags, dates, outcomes make it findable

**Extract learnings**: Move reusable insights to knowledge base

**Maintain some structure**: Don't just dump everything in one folder

### ❌ Don'ts

**Don't archive too early**: Feature isn't "done" until it's stable

**Don't delete too quickly**: If uncertain, keep it

**Don't break links**: Update references in active docs

**Don't archive active reference material**: Belongs in knowledge base

## Example Archive Structure

```
05-archive/
├── 2024/
│   ├── Q1-completed-projects/
│   │   ├── self-service-password-reset/
│   │   │   ├── prd-v1.md
│   │   │   ├── prd-v2-final.md
│   │   │   ├── user-stories.md
│   │   │   ├── launch-plan.md
│   │   │   ├── launch-retrospective.md
│   │   │   └── 90-day-metrics-review.md
│   │   └── webhook-retry-improvements/
│   │       └── ...
│   ├── Q1-investigations/
│   │   ├── settlement-delay-analysis.md
│   │   └── decline-rate-spike-investigation.md
│   └── Q1-updates/
│       ├── weekly/
│       │   └── [weekly updates from Q1]
│       └── monthly/
│           ├── january-2024.md
│           ├── february-2024.md
│           └── march-2024.md
└── 2023/
    └── [previous year archives]
```


**Remember**: Archive is not a graveyard—it's a library. Organize it for future reference, not just to get files out of the way.

**Last Updated**: February 18, 2026
