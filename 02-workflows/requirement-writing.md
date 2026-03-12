# Requirements Writing Workflow

> This workflow guides you through writing clear, actionable requirements for product features and improvements.

## When to Write Requirements

- Starting a new feature or product
- Making significant changes to existing functionality
- Responding to customer/support feedback that requires product work
- Planning a complex improvement or refactor
- Documenting a request before adding to roadmap

**PRD writing flow (Care & Support):** Anchor in strategy and goals first (which goal, which deliverable, which flywheel domain, which metrics). Then understand the problem, define goals and success metrics tied to north star and flywheel, then complete the rest of the PRD. See Step 0 and Step 2.


## Step 0: Anchor in strategy and goals (Care & Support PRDs)

Before writing a Care & Support PRD, fix the strategic context. This ensures the PRD supports the roadmap and uses the right success metrics.

**Decide and document:**

1. **Strategic goal** — Which of the two 2026 goals does this initiative support?
   - **Reduce / maintain contact rate** (fewer contacts per 1M transactions)
   - **Reduce cost of support** (lower cost per contact)

2. **2026 deliverable** — Which deliverable in `2026 deliverables.md` does this PRD implement or support? Name it explicitly.

3. **Flywheel domain** — Which of the six Care Product domains does this work sit in? (Defines which domain-level metrics apply.)
   - 1. Input | 2. Orchestration | 3. Fuel | 4. Agent Experience | 5. Insight & Prevention | 6. Governance  
   See `01-knowledge-base/strategy/care-product-model.md`.

4. **North star and domain metrics** — Which north star metric (contact rate, cost per contact) and/or which flywheel domain metrics will this initiative move? Use these when you define success metrics in the PRD.  
   See `01-knowledge-base/metrics/kpi-definitions.md` for north star definitions and strategic levers; care-product-model for metrics by domain.

**Optional strategy check:** For "why this, why now" and exec narrative, use [Rumelt's Strategy Kernel](../01-knowledge-base/strategy/rumelt-strategy-kernel.md): ensure the initiative is a coherent action under the guiding policy, with a clear link to diagnosis.


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

- [ ] **Support tickets**: What are customers reporting? When the problem is support-driven, name the **Case Type** and **Issue Type** (and Reason if useful) from [support-taxonomy.md](../01-knowledge-base/processes/support-taxonomy.md) (e.g. PAYMENTS (IN) → Refunds → Refund status enquiry). Use [support_contacts_flat_table_2025_last_6m.csv](../01-knowledge-base/metrics/support_contacts_flat_table_2025_last_6m.csv) and [support_contacts_flat_table_2025_metric_definitions.md](../01-knowledge-base/metrics/support_contacts_flat_table_2025_metric_definitions.md) to size the problem (e.g. “X contacts in last 6m in this case_type/issue_type, by segment/channel if relevant”).
- [ ] **User interviews**: Direct feedback from affected users
- [ ] **Analytics data**: Usage patterns and drop-off points
- [ ] **Competitive analysis**: How do others solve this? (See Competitive analysis below.)
- [ ] **Stakeholder input**: What do internal teams see?
- [ ] **Sales feedback**: What's blocking deals?
- [ ] **Technical constraints**: What's possible/practical?

### Competitive analysis

Use competitive context to validate the problem, inform "why now", and shape the solution. Capture:

- **Who we compare to** — Direct competitors (other PSPs, support tools), adjacent players, or best-in-class in the capability (e.g. how leading B2C fintechs handle support if relevant).
- **How they address this** — How do they solve the same problem or serve the same need? Channels, features, positioning, pricing if relevant.
- **How we compare** — Gaps (where we lag), strengths (where we match or lead), and differentiators we could lean on.
- **Implications** — What does this mean for our solution (must-have vs nice-to-have), positioning, or "why now" (e.g. competitors are investing here, or we have a window to differentiate).

Document this in the PRD under **Competitive context** (Problem Space) and link to any detailed competitive research in the Appendix. Competitive context can also strengthen the strategy anchor (Step 0) and Alternatives Considered.

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
- **Baseline**: Current state. For contact volume or involvement, use [support_contacts_flat_table_2025_last_6m.csv](../01-knowledge-base/metrics/support_contacts_flat_table_2025_last_6m.csv) and [support_contacts_flat_table_2025_metric_definitions.md](../01-knowledge-base/metrics/support_contacts_flat_table_2025_metric_definitions.md) so baselines match the canonical dataset (support_contacts, fin_only_resolved, channel, case_type, issue_type).
- **Target**: Goal to hit
- **Timeline**: When to measure
- **Threshold**: Minimum acceptable improvement

### Care & Support: tie to north star and flywheel metrics

For Care & Support PRDs, business goals and success metrics should link explicitly to strategy:

- **North star metrics** (from `01-knowledge-base/metrics/kpi-definitions.md`): **Contact rate** (contacts per 1M transactions) and **Cost per contact**. Every Care initiative should move one or both.
- **Strategic levers** that move those north stars: Contact reduction, AI deflection, agent efficiency, self-service. State which lever this initiative pulls.
- **Flywheel domain metrics**: Use the metrics for your initiative's domain (Input, Orchestration, Fuel, Agent Experience, Insight & Prevention, Governance) from `01-knowledge-base/strategy/care-product-model.md`. Include baseline and target for the domain metrics you can influence (e.g. AI resolution rate, AHT, content coverage).

Avoid generic goals like "improve support". Use specific, measurable outcomes tied to north star or domain metrics (e.g. "Reduce cost per contact via agent efficiency by lowering AHT for Blue EMI tickets by 15%").

### Optional: Strategy check (Rumelt)

For exec summary and "why now", check that the initiative reads as a **coherent action** under the guiding policy (e.g. "we reduce cost by shifting volume to Fin and improving agent tools") and links to a clear **diagnosis** (e.g. "cost per contact is under pressure as volume grows"). See [Rumelt's Strategy Kernel](../01-knowledge-base/strategy/rumelt-strategy-kernel.md).


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

**Care & Support — new query types**: If the feature introduces support contacts that don’t map to existing taxonomy, call out that new **Case Types / Issue Types / Reasons** may be needed (routing and reporting depend on them). See [support-taxonomy.md](../01-knowledge-base/processes/support-taxonomy.md) and “Known gaps” (B2C, B2B banking, PLATFORMS) for the checklist when new products or flows launch.

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
Before sharing, refine the doc using the reviewer personas (PM, Engineering/Tech lead, Operations agent, CPO, COO, and others). See [document-review-panel.md](document-review-panel.md) for persona lenses and questions. You can run the panel yourself (checklist), with AI (“apply the Review Panel to this PRD”), or with real reviewers assigned to personas.

**After first draft and review panel: Condense (PRDs only)**  
After incorporating panel feedback, run a **condense** pass so the PRD matches the template length and structure. Shorten to match [03-templates/prd-template.md](../03-templates/prd-template.md): section order, one success metrics table, one evidence/channel table in Problem Space, requirements by domain + FR/NFR, phased rollout with entry/success criteria; move detailed volume model, scenario tables, and full risk/dependency tables to the Appendix. Preserve all decisions, gates, and links. Target: body ~250–350 lines. The [draft-critique-refine](../.cursor/skills/draft-critique-refine/SKILL.md) skill does this automatically for PRDs (Draft → Critique → Refine → Condense).

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

**Care & Support PRDs — strategy alignment checklist:**
- [ ] **Roadmap alignment** block completed: 2026 deliverable, strategic goal (contact rate / cost), flywheel domain, how it fits
- [ ] **Executive summary** ties to 2026 deliverable and goal
- [ ] **Goals and success metrics** reference north star (contact rate, cost per contact) and/or flywheel domain metrics; baseline and target set; strategic lever stated

**Include**:
- Executive summary
- Problem statement
- Goals and metrics (north star / flywheel for Care & Support)
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
