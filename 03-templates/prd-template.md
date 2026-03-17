# `**PRD: [Product/Feature Name]**`

`**Author:**` `[Your name]`

`**Date:**` `[Date]`

`**Approvers:**` `[Who must approve this PRD]`

`**Stage:**` `[Ideation / Discovery / Solution Design / Planning / Build]`

`**Status:**` `[Draft / In Review / Approved / In Progress / Shipped]`

`**Last Updated:**` `[Date]`

`**Stakeholders:**` `[List key stakeholders and reviewers]`

> **TODO (delete on completion):** Fill the table below before writing any other section. Reference `2026 deliverables.md` and `01-knowledge-base/strategy/care-product-model.md`.

| Field | Value |
|-------|--------|
| **2026 deliverable** | [Name of the deliverable this PRD implements or supports] |
| **Strategic goal** | Reduce contact rate · Reduce cost of support (pick one) |
| **Flywheel domain** | 1. Input · 2. Orchestration · 3. Fuel · 4. Agent Experience · 5. Insight & Prevention · 6. Governance (pick one) |
| **How it fits** | [1–2 sentences: how this initiative supports the deliverable and goal] |

---

## `**Executive Summary**`

`*This is your elevator pitch. If an exec reads nothing else, they should understand what you're building and why it matters. Keep it to 3-4 sentences: the merchant problem, your solution, and the expected business impact. Include how this connects to our company strategy or pillar goals. For Care & Support work: state which 2026 deliverable and goal this supports.`*

## `**Problem Space*`*

`*Describe the problem you're solving. Include who experiences it, how it affects them, and data that validates it's worth solving (data points from merchant conversations, feature requests, support tickets, etc).`*

`**Problem statement:`** `Crisp 1-2 sentences describing the core merchant need/problem`

`**Who is affected:*`* `Merchant segments that show the most desire for this or feel this pain most acutely`

`**Evidence:**` `Real data that proves this matters. Merchant quotes, tickets, research links, etc. (Competitive context is captured separately below.)`

`**Competitive context:**` `How do others address this problem, and how do we compare? Use this to validate the problem, inform "why now", and shape the solution.`

- `**Who we compare to:**` `Direct competitors (e.g. other PSPs, support tools), adjacent players, or best-in-class in this capability`
- `**How they address this:**` `How they solve the same problem — channels, features, positioning`
- `**How we compare:**` `Gaps (where we lag), strengths (where we match or lead), differentiators we could lean on`
- `**Implications:**` `What this means for our solution (must-have vs nice-to-have), positioning, or "why now"`

`*Link to detailed competitive research in the Appendix if you have it.`*

`**Why now:**` `What makes this worth the investment now? Triggers, mandates, opportunity cost, risks, competitive moves, etc.`

`*(Avoid solution talk here. Focus on the pain and impact.)`*

## `**Goals and Success Metrics*`*

`*Define business goals (what Checkout.com achieves) and merchant goals (what merchants achieve). Use specific, measurable targets. List what you're deliberately not solving for.`*

`**Care & Support:** Link business goals and success metrics to the north star (contact rate, cost per contact) and/or the relevant flywheel domain metrics. State which strategic lever you're pulling (contact reduction, AI deflection, agent efficiency, self-service). See `01-knowledge-base/metrics/kpi-definitions.md` and `01-knowledge-base/strategy/care-product-model.md`.`

`**Business Goals:`** `What Checkout.com aims to achieve (e.g. increase revenue, gain SoW, OKR alignment; for Care: reduce contact rate or cost per contact via [lever])`

`**Merchant Goals:*`* `What our merchants want to accomplish (e.g. increase TAM, improve efficiency, etc.)`

`**Non-goals:**` `What you're explicitly not doing in this version`

`**Success metrics:**`

`*Include a mix of business outcomes, merchant adoption, and product health. For each metric, explain why it matters, provide a baseline if available, set a clear target, and identify the data source. For Care & Support, include at least one metric tied to north star or flywheel domain (see kpi-definitions and care-product-model).`*

> **Rule:** Every Baseline cell must contain a value or "TBC — establish by [date]". A bare TBC is not acceptable.

| `Metric`   | `Why it matters` | `Baseline` | `Target` | `Source` |
| ---------- | ---------------- | ---------- | -------- | -------- |
| `Metric 1` |                  |            |          |          |
| `Metric 2` |                  |            |          |          |
| `Metric 3` |                  |            |          |          |


## `**Customer Segments & Needs*`*

`*Identify your target merchant archetypes, along with their key needs, pain points, and motivations. Consider bringing these to life through customer persona artefacts that illustrate their goals and behaviors.`*

`**Customer segment(s):`** `Who needs this the most? Include business size, industry, geography, and any additional context that helps us understand the archetype better.`

`**User Stories/Jobs-To-Be-Done**: List the main jobs or problems the product helps them solve.`

`*If you have multiple customer segments, indicate which user stories apply to which segment for clearer milestone planning.`*

`Sample formats for user stories (use what works best for your product/feature):`

- `As a [merchant persona], I want to [do something], so that [benefit]`
- `When [situation], I want to [motivation], so I can [outcome]`

## `**Proposed Solution & Scope`**

*`Describe what you're building and why this approach solves the merchant problem. Focus on merchant value, not technical implementation. Define what's in scope and what's out of scope.`*

`**Solution overview:`** `2-3 sentences on what you're building`

> Alternatives evaluated: see Appendix.

`**What is in scope for this release and what is not.*`*

- `**In scope:**` `Bullets of capability slices, not tasks`
- `**Out of scope:**` `Bullets that might be assumed but are excluded`

## `**Requirements**`

`*Write requirements as testable behaviors. Each requirement should be verifiable. Include both merchant-facing and internal operational requirements.`*

`*Consider splitting into functional and non-functional sections, and provide relative prioritization within each section.`*

*`Prioritise: Must have (P0), Should have (P1), Nice to have (P2)`*

**Requirements by audience / domain**

`*Add a table that groups requirements by who benefits or which domain they serve (e.g. Merchant, Care Ops / CX, Analytics & Reporting, Security & Compliance, Product / Platform). Use requirement IDs (FR-X, NFR-X) so readers can map from domain to the detailed list below. One row per domain; Purpose column summarises what that audience gets.*`

| Domain | Requirement IDs | Purpose |
|--------|-----------------|---------|
| **Merchant** | [FR-X, NFR-X] | [Brief: what merchants get] |
| **Care Ops / CX** | [FR-X, NFR-X] | [Brief: what agents, team leaders, Zendesk admins get] |
| **Analytics & Reporting** | [FR-X, NFR-X] | [Brief: reporting, audit, dashboards] |
| **Security & Compliance** | [FR-X, NFR-X] | [Brief: policy, data protection, audit] |
| **Product / Platform** | [FR-X, NFR-X] | [Brief: engineering, config, tooling] |

`*Adjust row labels to match your initiative (e.g. add Treasury, Sales, Implementations). Omit domains that do not apply.*`

> **Gate vs requirement:** If a requirement depends on an open decision that has not been made, do not write it as a functional requirement. Capture it as an Open Question and reference it in the Rollout phase entry criteria. Promote it to the FR list only once the decision is made.

### Functional requirements

*`Include merchant-facing capabilities and internal operational needs (treasury reconciliation, support tooling, compliance reporting, etc.). Focus on what needs to happen, not how it will be built. Use clear acceptance criteria (Given [state], when [action], then [result]).`*

| ID | Requirement | Acceptance Criteria | Domain/s |
|----|-------------|---------------------|----------|
| **FR-0** | **Key events defined in the Instrumentation section must be implemented, validated in staging, and confirmed firing before Phase 1 go-live. (P0)** | All listed events fire correctly in staging; validated by [Data Scientist / Engineering] before Phase 1 entry. | Product / Platform |
| FR-1 | | | |

### Non-Functional Requirements

*`List only NFRs that will be tested. Use the same format: Given [state], when [action], then [result].`*

| ID | Requirement | Acceptance Criteria | Domain/s |
|----|-------------|---------------------|----------|
| NFR-1 | | | |

## `**Design and User Experience**`

**Design & UX:** `[Link to Figma]` — `[1-sentence description of key interaction or flow]`

## `**Instrumentation and Monitoring**`

`Define what data you'll collect and how. Focus on the events, properties, and validation needed to track your success metrics and maintain operational visibility.`

`**Key events to instrument**: List critical events with clear names and properties. For Care & Support PRDs, always include:`

- `contact_created: channel, case_type, issue_type, fin_involved (boolean), merchant_segment — use field names from` [support_contacts_flat_table_2025_metric_definitions.md](../01-knowledge-base/metrics/support_contacts_flat_table_2025_metric_definitions.md)
- `contact_resolved: resolved_by (fin / agent / merchant_self_serve), handle_time_seconds, fin_involved`
- `[Additional events specific to this initiative]`

`**Internal dashboards and monitoring**: What views you'll create for tracking`

- `[Dashboard 1]: [What it shows and who uses it]`
- `[Dashboard 2]: [What it shows and who uses it]`

`**Validation approach**: How you'll verify instrumentation works correctly before and after launch`

- `[Validation method, e.g., test contacts in staging, compare event counts to expected baseline]`
- `Silent failure detection: define how you will know if events stop firing or are malformed (e.g. daily row count alert, null-field threshold alert). Name the owner and cadence.`

## `**Risks, Assumptions, and Open Questions**`

`*List what could go wrong, what you're assuming, and what you don't know yet. Include potential mitigations for each risk.*`

`**Risks:**`

- `Risk 1 and potential mitigation`
- `Risk 2 and potential mitigation`

`**Key assumptions:**`

- `[Assumption 1 — and how you'll validate or monitor it]`
- `[Assumption 2 — and how you'll validate or monitor it]`

`**Open questions:**`

- `Question 1 that needs answering [owner]`
- `Question 2 that needs answering [owner]`

## `**Rollout Plan**`

`*Define your phased rollout approach. For each phase, specify entry criteria (what must be ready), success criteria (what must be true to move forward), and timeline.`*

`***Rollout approach:*`* `[High-level strategy - why this phased approach, risk mitigation plan, rollback triggers]*`

### `***Phase 1: [Pilot/Beta]**`*

`***Purpose:**` `[What you're trying to validate in this phase]*`

`***Entry criteria:**` `What must be ready to start this phase*`

- `***Technical:**` `[e.g., Feature complete in sandbox, certifications received]*`
- `***Operational:**` `[e.g., Support trained on beta process, escalation path defined]*`
- `***Merchant:**` `[e.g., beta merchants identified and onboarded]*`
- `*etc.`*

`***Success criteria:*`* `What must be true to move to next phase*`

- `*[e.g., Process X transactions with >Y% success rate]`*
- `*[e.g., <N P1 incidents, all resolved within SLA]`*
- *`[e.g., Beta merchants confirm production readiness]`*

*`**Timeline:`** `[Phase start date] - [Phase end / decision point]`*

### `***Phase 2: [Gradual Expansion]**`*

`*Optional phase. Include if you have gradual expansion between beta and GA.`*

`***Purpose:*`* `[What you're trying to validate in this phase]*`

`***Entry criteria:**` `What must be ready to start this phase*`

- `***Technical:**` `[e.g., Beta issues resolved, monitoring validated]*`
- `***Operational:**` `[e.g., Extended support coverage in place]*`
- `***Merchant:**` `[e.g., Next cohort of merchants ready]*`

`***Success criteria:**` `What must be true to move to GA*`

- `*[e.g., X merchants live processing Y volume]`*
- `*[e.g., Maintain success rate and stability targets]`*

*`**Timeline:`** `[Phase start date] - [Phase end / GA decision point]`*

### `***Phase 3: General Availability**`*

`***Purpose:*`* `[e.g., Launch to all eligible merchants]*`

`***Entry criteria:**` `What must be ready for GA*`

- `***Technical:**` `[e.g., All P0 requirements met, performance meets NFRs]*`
- `***Operational:**` `[e.g., Runbooks published, 24/7 on-call staffed, treasury reconciliation tested]*`
- `***Business:**` `[e.g., Legal/compliance approvals complete, contracts signed]*`
- `***Merchant:**` `[e.g., Documentation published, communications ready]*`

`***Success criteria:**` `[e.g., X merchants live within 30 days, maintain >Y% uptime]*`

`**Definition of Done:**`

`*What must be true to consider this launch-ready? Define technical, operational, merchant, and business criteria that must be met.`*

- `**Technical:`** `[e.g., All P0 requirements delivered and tested, performance meets NFR targets]`
- `**Operational:*`* `[e.g., support trained with runbooks published, monitoring and alerting configured]`
- `**Merchant:**` `[e.g., beta merchants processing successfully, documentation published]`
- `**Business:**` `[e.g., Legal/compliance approvals complete, go-to-market materials ready]`

`**Timeline:**` `List target dates for the different phases.`

`**Product Dependencies:**` `List what must be completed before launch. Cover cross-pillar product build dependencies including central teams such as One Finance, CoS Ops, legal/compliance activities (licensing, approvals, T&C changes), and external dependencies (scheme certification and approvals, third-party integrations). Include owners`

`**Go-to-market:**` `Define how we'll take this to market and how our merchants will learn about this. Cover operational enablement (merchant care briefings and training, knowledge hub enhancements, runbooks, SoPs, etc.), sales enablement (sales briefing and training, collateral, etc.), merchant communications (email, dashboard prompts, documentation, etc.), marketing (blogs, press, case studies, etc.), and developer materials (API docs, SDK guides). Include owners for each activity`

## `**Appendix**`

`*Include supporting materials that provide context but aren't essential to the core PRD.`*

`**Strategy and Research:`**

- `Links to market sizing and opportunity analysis`
- `Links to competitive analysis`
- `Links to user research findings`

`**Alternatives Considered:**`

- `Option 1: Brief description and why rejected or deferred`
- `Option 2: Brief description and why rejected or deferred`
- `Why we chose this approach: Clear rationale for the proposed solution`

`**Technical and Commercial:*`*

- `Links to solution design documents`
- `Links to commercial modeling and projections`

`**Detailed Requirements:**`

- `Links to granular user stories`
- `Links to technical specifications`
