# Requirements Writing Workflow

> This workflow guides you through writing clear, actionable requirements for product features and improvements.

## When to Write Requirements

- Starting a new feature or product
- Making significant changes to existing functionality
- Responding to customer/support feedback that requires product work
- Planning a complex improvement or refactor
- Documenting a request before adding to roadmap


## Step 1: Understand the Problem

Before writing any requirements, deeply understand the problem you're solving.

### Gather Context

**Ask the "Five Ws"**:
- **Who** has this problem? (User persona, merchant segment)
- **What** problem are they facing? (Specific pain point)
- **When** does this problem occur? (User journey stage, frequency)
- **Where** does it happen? (Which part of product, which channel)
- **Why** is this a problem? (Business impact, user impact)

### Research Sources

- [ ] **Support tickets**: What are customers reporting?
- [ ] **User interviews**: Direct feedback from affected users
- [ ] **Analytics data**: Usage patterns and drop-off points
- [ ] **Competitive analysis**: How do others solve this?
- [ ] **Stakeholder input**: What do internal teams see?
- [ ] **Sales feedback**: What's blocking deals?
- [ ] **Technical constraints**: What's possible/practical?

### Validate the Problem

**Confirm**:
- This problem is real (not assumed)
- It's significant (worth solving)
- It's scoped appropriately (not too broad/narrow)
- You understand the root cause (not just symptoms)

**Red flags**:
- Only one person/merchant has mentioned it
- No clear business impact
- Solution looking for a problem
- Unclear who benefits

### Sharpen with Socratic questions

Use 3–5 questions from [Socratic questioning for PRDs](../01-knowledge-base/processes/socratic-questioning-prds.md) to validate problem, solution, success criteria, scope, and strategic fit before you lock the requirements. Pick the most relevant from each category (problem clarity, solution validation, success criteria, constraints & trade-offs, strategic fit). Quality over quantity.


## Step 2: Define Goals & Success

### Business Goals

**What are we trying to achieve?**
- Increase revenue/conversion
- Reduce churn or improve retention
- Decrease support costs
- Improve efficiency or scalability
- Meet compliance requirements
- Competitive differentiation
- Strategic capability building

**Be specific**:
- ❌ "Improve merchant experience"
- ✅ "Reduce merchant onboarding time from 5 days to 2 days"

### Success Metrics

**Define how you'll measure success**:

**Leading Indicators** (can measure during development):
- Feature adoption rate
- Usage frequency
- Completion rate
- Error rate

**Lagging Indicators** (measure after launch):
- Business metrics (revenue, retention, etc.)
- Support ticket reduction
- Customer satisfaction (CSAT, NPS)
- Operational efficiency gains

**Example**:
```
Goal: Reduce integration support burden
Metrics:
- Integration-related tickets decrease by 40% within 2 months
- New merchant time-to-first-transaction decreases by 30%
- Integration documentation NPS increases from 40 to 70
```

### Set Targets

For each metric:
- **Baseline**: Current state
- **Target**: Goal to hit
- **Timeline**: When to measure
- **Threshold**: Minimum acceptable improvement

**See also:** For product or roadmap-level strategy (prioritisation, competitive response, executive narrative), use [Rumelt's Strategy Kernel](../01-knowledge-base/strategy/rumelt-strategy-kernel.md): Diagnosis → Guiding Policy → Coherent Actions.


## Step 3: Identify Users & Use Cases

### Define User Personas

**For each user type affected**:
- **Role**: Title/position (e.g., "Backend Developer", "Finance Manager")
- **Goals**: What they're trying to accomplish
- **Pain Points**: What frustrates them today
- **Technical Level**: Beginner/Intermediate/Expert
- **Context**: When/where they use the product

### Document Use Cases

**For each persona, describe**:
- Primary use case (most common scenario)
- Alternative use cases (less common but important)
- Edge cases (unusual but must be supported)
- Anti-use cases (what this is NOT for)

**Use Case Template**:
```
Actor: [User persona]
Goal: [What they want to accomplish]
Preconditions: [What must be true before starting]
Steps:
  1. User does [action]
  2. System responds with [result]
  3. User does [next action]
  4. ...
Success: [End state if everything works]
Failure: [What happens if something goes wrong]
```


## Step 4: Write User Stories

Use the template: `03-templates/user-story-template.md`

### Follow Standard Format

**As a** [type of user],  
**I want** [capability],  
**So that** [benefit].

### Make Stories Specific

**Bad examples**:
- ❌ "As a user, I want better performance, so it's faster"
- ❌ "As a merchant, I want the dashboard to be improved"

**Good examples**:
- ✅ "As a support agent, I want to search tickets by merchant ID, so I can quickly find all tickets for an account"
- ✅ "As a developer, I want clear error messages in API responses, so I can quickly identify and fix integration issues"

### Write Acceptance Criteria

**Use Given-When-Then format**:

```
Given [starting state/context]
When [action taken]
Then [expected outcome]
```

**Example**:
```
Given I'm a support agent viewing a ticket
When I click the merchant ID link
Then I'm taken to a search results page showing all tickets for that merchant
And the results are sorted by most recent first
And I can see ticket status, date created, and category
```

### Make Criteria Testable

Each acceptance criterion should be:
- **Specific**: No ambiguity about what's required
- **Testable**: Clear pass/fail condition
- **Achievable**: Technically possible
- **Relevant**: Tied to user value
- **Time-bound**: Part of this story, not future enhancement


## Step 5: Define Functional Requirements

### Organize by Priority

**P0 - Must Have**:
- Critical to core functionality
- Without it, feature doesn't work or provide value
- Blocking other work

**P1 - Should Have**:
- Important but not blocking
- Strong user need but workaround exists
- Significantly improves experience

**P2 - Nice to Have**:
- Enhancement or polish
- Benefits small subset of users
- Can be added later without major rework

### Be Precise & Unambiguous

**Bad requirements** (vague):
- "System should be fast"
- "UI should be intuitive"
- "Error handling should be robust"

**Good requirements** (specific):
- "API response time shall be < 500ms at p95 under normal load"
- "All form fields shall have visible labels and inline error messages"
- "System shall return a specific error code for each failure scenario (see error code table)"

### Cover the Essentials

**Inputs**:
- What data is provided?
- What format?
- What validations apply?
- What are valid/invalid examples?

**Processing**:
- What does the system do with inputs?
- What business logic applies?
- What calculations or transformations?
- What integrations are needed?

**Outputs**:
- What does the system return/display?
- What format?
- What happens on success?
- What happens on failure?

**State Changes**:
- What data is created/updated/deleted?
- What notifications are triggered?
- What audit logs are created?


## Step 6: Define Non-Functional Requirements

### Performance
- Response time targets
- Throughput (requests per second)
- Concurrent user capacity
- Data volume limits

**Example**: "Dashboard shall load within 2 seconds on 3G connection"

### Scalability
- Expected growth over time
- Peak load scenarios
- Capacity planning considerations

**Example**: "System shall support 10x current transaction volume without architectural changes"

### Reliability & Availability
- Uptime targets (e.g., 99.99%)
- Recovery time objectives (RTO)
- Recovery point objectives (RPO)
- Fault tolerance requirements

**Example**: "Payment processing shall have 99.99% uptime (max 52 minutes downtime/year)"

### Security & Compliance
- Authentication requirements
- Authorization/permissions model
- Data encryption (in transit, at rest)
- Audit logging requirements
- Regulatory compliance (PCI, GDPR, etc.)

**Example**: "All cardholder data shall be encrypted using AES-256 and never logged"

### Usability & Accessibility
- User experience standards
- Accessibility compliance (WCAG level)
- Supported browsers/devices
- Internationalization needs

**Example**: "Interface shall be WCAG 2.1 AA compliant"

### Data Integrity
- Data validation rules
- Referential integrity constraints
- Backup and retention requirements

**Example**: "All transactions shall be immutable after settlement"


## Step 7: Define What's Out of Scope

Explicitly state what you're NOT doing.

### Why This Matters
- Prevents scope creep
- Sets clear expectations
- Helps with future planning
- Avoids confusion

### What to Include

**Related features deferred**:
- "This version only supports card payments; alternative payment methods in v2"

**Edge cases not supported**:
- "Refunds for multi-currency transactions not supported in initial release"

**Integrations planned later**:
- "Integration with ERP systems is out of scope for MVP"

**Scale limitations**:
- "This solution works for up to 1M transactions/day; higher volumes need different architecture"


## Step 8: Address Dependencies & Constraints

### Technical Dependencies

**List what you depend on**:
- Other systems or services
- APIs or libraries
- Infrastructure or platform capabilities
- Data from other sources

**For each dependency**:
- What do you need?
- Who owns it?
- Is it available now or needs to be built?
- What's the risk if it's delayed?

### Business Constraints

**Factors that limit options**:
- Budget limitations
- Timeline constraints
- Resource availability (team capacity)
- Legal or compliance requirements
- Contractual obligations
- Technical debt or legacy system constraints

### Risks

**Identify risks early**:
| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| [Risk description] | High/Med/Low | High/Med/Low | [How to address] |


## Step 9: Collaborate & Refine

### Get Input from Key Stakeholders

**Engineering**:
- Technical feasibility
- Effort estimates
- Alternative approaches
- Platform constraints

**Design/UX**:
- User flows
- Interface requirements
- Accessibility considerations
- Interaction patterns

**Support**:
- Common customer issues
- Troubleshooting needs
- Documentation requirements
- Training implications

**Sales/Account Management**:
- Customer requests
- Competitive positioning
- Pricing implications
- Go-to-market considerations

### Review & Iterate

**Optional: Run the Document Review Panel**  
Before sharing, refine the doc using the five reviewer personas (PM, Engineering/Tech lead, Operations agent, CPO, COO). See [document-review-panel.md](document-review-panel.md) for persona lenses and questions. You can run the panel yourself (checklist), with AI (“apply the Review Panel to this PRD”), or with real reviewers assigned to personas.

**Questions to ask reviewers**:
- Is anything unclear or ambiguous?
- Are we solving the right problem?
- Is anything missing?
- Are priorities correct?
- Is this feasible to build?
- What are we not considering?

**Incorporate feedback**:
- Clarify ambiguous requirements
- Add missing details
- Adjust scope if needed
- Update priorities based on new information


## Step 10: Document & Communicate

### Create PRD (if comprehensive feature)

Use template: `03-templates/prd-template.md`

**Include**:
- Executive summary
- Problem statement
- Goals and metrics
- User stories
- Requirements (functional & non-functional)
- Design/UX approach
- Technical approach
- Out of scope
- Launch plan
- Dependencies and risks

### Or Write Concise Spec (if smaller change)

For smaller features, a lighter-weight doc:
- Problem & solution (1-2 paragraphs)
- User stories (2-5 stories)
- Key requirements (bullet list)
- Success metrics (2-3 metrics)
- Out of scope (if applicable)

### Share Widely

**Who needs to see it**:
- Engineering team (implementers)
- Design team (UX/UI)
- QA/Test team (acceptance testing)
- Support team (training and documentation)
- Product leadership (approval)
- Relevant cross-functional partners

**Communication channels**:
- Email stakeholders with link
- Present in team meetings
- Post in relevant Slack channels
- Add to project wiki/documentation
- Link from roadmap items


## Step 11: Maintain Requirements

Requirements are living documents.

### Update as You Learn

**During development**:
- Technical discoveries may require changes
- Design iterations may refine requirements
- Stakeholder feedback may adjust priorities

**Keep PRD current**:
- Mark sections as updated with dates
- Track decision history
- Document why requirements changed

### Handle Change Requests

**When someone proposes a change**:
1. Understand the rationale
2. Assess impact (scope, timeline, resources)
3. Evaluate against goals (still aligned?)
4. Decide: Accept, defer, or reject
5. Update documentation
6. Communicate decision to stakeholders

**Decision criteria**:
- Does it support original goals?
- Is it needed for MVP or can it wait?
- What's the cost/benefit?
- Does it introduce new risks?


## Requirements Quality Checklist

### ✅ Clear
- [ ] Anyone can understand what's being asked
- [ ] No ambiguous terms or jargon
- [ ] Includes examples where helpful

### ✅ Specific
- [ ] Precise, not vague
- [ ] Quantified where possible (numbers, limits, timing)
- [ ] Defines success criteria

### ✅ Testable
- [ ] Clear pass/fail condition
- [ ] Can be verified through testing
- [ ] Acceptance criteria defined

### ✅ Necessary
- [ ] Tied to user value or business goal
- [ ] Not "nice to have" masquerading as "must have"
- [ ] Can explain why it's needed

### ✅ Feasible
- [ ] Technically possible
- [ ] Achievable within timeline and budget
- [ ] Resources available

### ✅ Complete
- [ ] Covers all scenarios (happy path, errors, edge cases)
- [ ] Addresses functional and non-functional needs
- [ ] Includes all necessary details for implementation

### ✅ Consistent
- [ ] No contradictions with other requirements
- [ ] Uses consistent terminology
- [ ] Aligns with overall product strategy

### ✅ Traceable
- [ ] Linked to original problem/request
- [ ] Connected to goals and metrics
- [ ] Can track through to implementation


## Common Pitfalls to Avoid

### ❌ Solution Disguised as Requirement
**Problem**: Prescribing HOW instead of defining WHAT
- Bad: "Add a Redis cache to the API layer"
- Good: "API response time shall be < 200ms for read operations"

### ❌ Too Vague
**Problem**: Ambiguous language that could mean anything
- Bad: "System should be user-friendly"
- Good: "90% of users shall complete setup without contacting support"

### ❌ Too Prescriptive
**Problem**: Over-constraining implementation details
- Leave room for engineering judgment on implementation
- Focus on outcomes, not always on exact approach

### ❌ Missing Context
**Problem**: Requirements without explanation of why
- Always include rationale
- Help team understand problem, not just solution

### ❌ Kitchen Sink Requirements
**Problem**: Everything anyone ever mentioned
- Be ruthless about scope
- Separate must-have from nice-to-have
- Plan for iterations, not one giant release

### ❌ Writing Requirements in Isolation
**Problem**: Not involving key stakeholders
- Get input from engineering, design, support
- Validate with customers/users
- Review with leadership


## Quick Reference Template

```markdown
## Feature: [Name]

### Problem
[2-3 sentences describing the problem]

### Goals
- [Goal 1 with metric]
- [Goal 2 with metric]

### User Story
As a [user type],
I want [capability],
So that [benefit].

**Acceptance Criteria**:
- Given [context], when [action], then [outcome]
- Given [context], when [action], then [outcome]

### Requirements
**Must Have**:
- [ ] [Specific requirement]
- [ ] [Another requirement]

**Should Have**:
- [ ] [Important but not critical]

**Out of Scope**:
- [What we're not doing]

### Success Metrics
- [Metric]: [Current] → [Target] by [Date]

### Dependencies & Risks
- [Dependency or risk]
```


**Last Updated**: [Date]
**Owner**: Charlie Wildish
