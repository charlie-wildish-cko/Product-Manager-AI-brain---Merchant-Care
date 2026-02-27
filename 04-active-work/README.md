# Active Work

This directory contains your current projects and work-in-progress.

## Subdirectories

### `current-sprint/`
Work planned for this sprint or week. Organize by priority or project.

**Example structure**:
```
current-sprint/
├── high-priority-bug-investigation.md
├── q2-roadmap-planning.md
└── merchant-feedback-review.md
```

### `roadmap-items/`
Features and initiatives being planned or actively developed.

**Example structure**:
```
roadmap-items/
├── self-service-password-reset/
│   ├── prd.md
│   ├── user-stories.md
│   └── design-mockups/
└── multi-currency-refunds/
    ├── rfc.md
    └── research-notes.md
```

### `investigations/`
Deep dives on support issues, performance problems, or opportunities.

**Example structure**:
```
investigations/
├── webhook-delivery-failures-feb-2024.md
├── high-decline-rates-analysis.md
└── onboarding-friction-research.md
```

### `stakeholder-updates/`
Draft and sent status updates to stakeholders.

**Example structure**:
```
stakeholder-updates/
├── 2024-02-weekly/
│   ├── week-of-feb-12.md
│   ├── week-of-feb-19.md
│   └── week-of-feb-26.md
└── 2024-monthly/
    ├── january-update.md
    └── february-update.md
```

## Organization Tips

### Keep It Focused
- Only active work belongs here
- Archive completed items regularly
- Delete outdated drafts

### Create Structure That Works for You
- By project
- By sprint/week
- By type (bugs, features, investigations)
- By team or stakeholder

### Link to Related Documents
- PRDs link to user stories
- Updates link to PRDs
- Investigations link to source tickets

### Regular Cleanup
- **Weekly**: Review and update current sprint items
- **Monthly**: Archive completed work to `05-archive/`
- **Quarterly**: Assess overall organization

## Quick Start

### Starting a New Project

1. Create subdirectory: `roadmap-items/[project-name]/`
2. Copy relevant template from `03-templates/`
3. Fill in initial details
4. Link from sprint planning or roadmap

### Starting a New Investigation

1. Create file: `investigations/[issue-description-date].md`
2. Document:
   - What triggered investigation
   - Initial observations
   - Questions to answer
   - Data sources
3. Update as you learn
4. Summarize findings and recommendations

### Creating a Status Update

1. Copy template: `03-templates/stakeholder-update-template.md`
2. Save to: `stakeholder-updates/[period]/[date].md`
3. Fill in sections
4. Review and send
5. Track action items

## Example Active Work Structure

```
04-active-work/
├── current-sprint/
│   ├── ticket-analysis-week-7.md
│   ├── q2-planning-prep.md
│   └── prd-review-sessions.md
├── roadmap-items/
│   ├── improved-error-messages/
│   │   ├── prd.md
│   │   ├── error-catalog.md
│   │   └── merchant-feedback.md
│   └── dashboard-redesign/
│       ├── user-research-notes.md
│       ├── design-feedback.md
│       └── requirements-draft.md
├── investigations/
│   ├── settlement-delay-spike-feb-2024.md
│   ├── new-merchant-onboarding-friction.md
│   └── api-timeout-pattern-analysis.md
└── stakeholder-updates/
    ├── 2024-02-weekly/
    │   └── week-of-feb-12.md
    └── monthly/
        └── february-2024.md
```


**Pro tip**: Create a "parking lot" document for ideas and tasks that aren't yet prioritized but you don't want to forget.

**Example**: `active-work/parking-lot.md`
```markdown
# Ideas & Future Work

## Product Improvements
- [ ] Add bulk refund capability
- [ ] Improve webhook retry logic visibility

## Process Improvements
- [ ] Automate weekly ticket reports
- [ ] Create support agent training program

## Investigations Needed
- [ ] Why do enterprise merchants open fewer tickets?
- [ ] What's driving weekend ticket spikes?
```
