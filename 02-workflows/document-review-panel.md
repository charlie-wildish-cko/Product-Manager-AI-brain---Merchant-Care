# Document Review Panel

> Use this workflow to refine PRDs, reports, memos, and other key documents by applying ten reviewer personas. Run the panel before sharing with real stakeholders or sending to leadership.

## When to Use This Workflow

- **PRDs and specs**: Before engineering kickoff or leadership review
- **Reports and status updates**: Before sending to CPO, COO, or broader stakeholders
- **C-suite memos**: Before sending to Chief of Product or Chief of Operations
- **Any document** where you want multiple perspectives to catch gaps, clarify ambiguity, or strengthen alignment

**Convention**: When running the panel, assume that any data in the document (metrics, numbers, baselines, tables, splits) originated from or was validated by the Product Data Scientist. The Data Scientist persona therefore reviews “their” output for clarity, correct definitions, and interpretability.

**Detailed personas**: For full backstory, goals, and typical questions (Sam, Jordan, Drew, Alex, Morgan, Casey, Riley, Quinn, Reese, Taylor), see [Review Panel Personas (Customer Support Angle)](../01-knowledge-base/processes/review-panel-personas.md). Use that doc when you want to inhabit a reviewer, brief someone else, or paste into AI for a simulated panel.

**Optional before the panel:** Run a quick self-check with 3–5 questions from [Socratic questioning for PRDs](../01-knowledge-base/processes/socratic-questioning-prds.md) to tighten problem, solution, and success criteria before reviewers see the doc.

## The Ten Review Panel Personas (Lens & Checklist)

The following sections are the concise “lens” and checklist for each role. Use the [detailed personas](../01-knowledge-base/processes/review-panel-personas.md) when you want to simulate or assign a specific reviewer. **All reviewers**: Flag verbosity — could any section be shortened without losing meaning?

### 1. Product Manager

**Lens**: Problem–solution fit, clarity, prioritisation, stakeholder alignment, and concision.

**What they look for**:
- Is the problem clearly stated and who has it?
- Are goals and success metrics specific and measurable?
- Are user stories and acceptance criteria complete and testable?
- Is scope (in/out) explicit?
- Are priorities (P0/P1/P2) defensible and consistent with goals?
- Would another PM understand the “why” and “so what” without you in the room?
- Could any section be shortened without losing meaning? (Flag verbosity or repetition.)

**Questions they ask**:
- Is anything unclear or ambiguous?
- Are we solving the right problem?
- Is anything missing that would block execution or decision-making?
- Are priorities correct given the goals?
- What are we not considering (edge cases, risks, dependencies)?

For more structured question prompts (problem clarity, solution validation, success criteria, scope, strategic fit), see [Socratic questioning for PRDs](../01-knowledge-base/processes/socratic-questioning-prds.md).

---

### 2. Software Engineering / Tech Lead

**Lens**: Feasibility, technical risk, implementation clarity, and operational reality (software build and runtime).

**What they look for**:
- Can we build this with the constraints and timeline stated?
- Are requirements specific enough to estimate and implement?
- What’s missing technically (APIs, data model, error handling, scale)?
- Security, compliance, and performance implications?
- Dependencies on other teams or systems?
- Edge cases and failure modes called out?
- Any ambiguity that would cause rework or mis-scoping?

**Questions they ask**:
- Is this feasible to build as written?
- What technical assumptions are we making that aren’t stated?
- What could go wrong in implementation or at runtime?
- Are there integration or dependency risks we haven’t addressed?
- Do acceptance criteria map to something we can actually test?

---

### 3. Product Designer

**Lens**: User experience, UX/UI of the product build, user flows, accessibility, and consistency with design and content.

**What they look for**:
- Are user flows and journeys clear and documented (merchant-facing and, where relevant, agent-facing)?
- Is the UX/UI specified enough to build from (key screens, states, hierarchy) or are we deferring design too late?
- Are edge states and empty states considered (errors, no data, loading, permissions)?
- Is accessibility and inclusive design called out (e.g. WCAG, keyboard, screen readers)?
- Does this align with our design system and brand (components, patterns, tone)?
- Is in-UI copy and microcopy in scope, and who owns it?
- Could the proposed flows create friction, confusion, or unnecessary steps for the user?

**Questions they ask**:
- Who is the primary user here, and what does “good” look like for them in the UI?
- What are the main user flows, and where could users get stuck or confused?
- Are we designing for all key states (happy path, errors, empty, loading) or only the happy path?
- Does this fit our design system, or do we need new components or patterns?
- Who owns copy and microcopy, and is it in the timeline?
- How does this behave across devices or contexts (e.g. dashboard vs mobile)?

---

### 4. Operations Agent

**Lens**: Day-to-day execution, support, training, and process impact.

**What they look for**:
- How does this change how agents (or ops) work?
- What training, playbooks, or documentation will be needed?
- What new questions or issues might customers raise?
- Are handoffs, escalation paths, and SLAs clear?
- Is the doc written so an ops person can explain the change to a merchant?
- Any impact on tools (Zendesk, Jira, etc.) or workflows?

**Questions they ask**:
- What will agents need to know or do differently?
- What could confuse or frustrate customers when this ships?
- What support volume or ticket types might change?
- Are there process or tool changes we need to plan for?
- Is the language clear enough for frontline teams to use?

---

### 5. Chief of Product

**Lens**: Strategy, portfolio fit, resource trade-offs, and executive narrative.

**What they look for**:
- How does this fit the product and company strategy?
- Is the “so what” and business impact clear in 30 seconds?
- Are we making the right trade-offs vs other initiatives?
- Is the narrative crisp for board/exec conversations?
- Are risks and dependencies surfaced so decisions can be made?
- Would this hold up under “why this, why now?”

**Questions they ask**:
- Why this over other things we could do?
- What’s the one thing we want everyone to remember?
- Are we being honest about risks and what we don’t know?
- Is the recommendation (or ask) explicit and actionable?
- What would we say if asked to cut scope or timeline?

For "why this, why now" and strategic narrative, see [Rumelt's Strategy Kernel](../01-knowledge-base/strategy/rumelt-strategy-kernel.md) (diagnosis, guiding policy, coherent actions).

---

### 6. Chief of Operations

**Lens**: Operational impact, scalability, cost, and run-the-business readiness.

**What they look for**:
- What does this mean for capacity, headcount, or process?
- Are support, compliance, and training implications clear?
- What could break or get worse when we scale?
- Are we accounting for run-the-business cost (not just build)?
- Is the document clear enough for ops leadership to plan and communicate?

**Questions they ask**:
- What’s the impact on ops when this goes live?
- What do we need to have in place before launch (training, playbooks, tools)?
- What could increase cost or risk in ongoing operations?
- Is the timeline realistic for ops readiness, not just engineering?
- Would our teams know what “good” looks like after launch?

---

### 7. Product Data Scientist

**Lens**: Measurability, metric definitions, instrumentation, baselines, and reporting feasibility. *Assume data in the doc (metrics, numbers, tables) originated from the data scientist; this persona is reviewing that output for correctness and interpretability.*

**What they look for**:
- Are success metrics and targets defined with a clear numerator, denominator, and dimensions?
- Can we measure this with existing or planned data sources?
- Are baselines established so we can track progress?
- What could confound or break the measurement (definition drift, channel changes, missing instrumentation)?
- Is reporting feasible (cadence, ownership, tooling) and usable by support/ops?

**Questions they ask**:
- Can we actually measure this? What’s the source of truth?
- Are we comparing apples to apples over time (consistent definitions)?
- What’s the baseline today, and how do we know when we’ve hit the target?
- What could make this metric misleading or uninterpretable?
- Who owns the report, how often do we refresh it, and can the right people use it to decide?

---

### 8. Zendesk Administrator

**Lens**: Configuration, tagging, routing, reporting, and agent tooling in Zendesk; taxonomy and config readiness before launch.

**What they look for**:
- Do we need new tags, fields, or ticket types? What’s the taxonomy?
- What triggers, routing, or views need to change before go-live?
- How will we report on this in Zendesk (Explore, dashboards)—and is that in scope?
- What internal KB articles or macros do agents need, and who’s writing them?
- When do config changes need to be done so we’re ready when this ships?
- Does this align with existing tagging and reporting strategy?

**Questions they ask**:
- Do we need new tags, fields, or ticket types for this?
- What triggers, routing, or views need to change before launch?
- How will we report on this in Zendesk—and is that in scope for this launch?
- What KB articles or macros do agents need, and who’s responsible?
- When do config changes need to be done for support readiness?
- Does this fit our existing taxonomy and reporting conventions, or do we need to adjust?

---

### 9. Content Strategist

**Lens**: Content dependencies, ownership, and alignment with the content strategy; resolution rate, deflection, and self-serve; what must be written or updated for launch.

**What they look for**:
- What content does this depend on—and does it exist? Who owns it?
- Does this create or change anything that needs a help article, guide, or Fin KB update?
- How does this align with the content strategy (guide programme, resolution rate target)?
- What do we need to write or update so agents, Fin, and customers have the right answers?
- Is the timeline realistic for content work, not just engineering and ops?
- If we're tracking resolution or deflection, is content explicitly in the dependency list?

**Questions they ask**:
- What content does this depend on, and who owns it?
- Does this need new or updated help articles, guides, or Fin KB content?
- How does this fit our content strategy and resolution/deflection targets?
- What content work needs to happen before or alongside launch?
- Is content called out in dependencies and timeline?

---

### 10. VP of Product

**Lens**: Clarity and defensibility for leadership; alignment between problem, goals, scope, and recommendation; explicit ask so they can advocate upward; support/ops impact surfaced so they can represent it to the CPO.

**What they look for**:
- Would the CPO understand this and the ask in 2 minutes?
- Are problem, goals, scope, and recommendation aligned?
- Are trade-offs and support impact stated honestly?
- What would we cut or delay if we had to—and is it said?
- Is the recommendation clear enough to advocate for with leadership?
- What's the one thing we want everyone to remember, and is it stated?

**Questions they ask**:
- Would my CPO understand this and the ask in 2 minutes?
- Are we being honest about trade-offs and support impact so I can represent it accurately?
- What would we cut or delay if we had to?
- Is the recommendation clear enough that I can advocate for it with leadership?
- What's the one thing we want everyone to remember?

---

## How to Run the Panel

### Option A: Checklist pass (solo or with AI)

1. **Open your document** (PRD, report, memo).
2. **For each persona**, work down their “What they look for” and “Questions they ask.”
3. **Note gaps and edits**: Add comments or a short “Panel feedback” section.
4. **Revise the document** to address the feedback.
5. **Optional**: Tick off personas once you’ve explicitly considered their view (see template below).

### Option B: Simulated panel (with AI)

Use a prompt like:

- *“Apply the Document Review Panel to this [PRD/report]. For each persona (PM, Software Engineering/Tech lead, Product Designer, Operations agent, CPO, COO, Product Data Scientist, Zendesk Administrator, Content Strategist, VP of Product), list 2–3 concerns or suggested edits, with a customer support angle where relevant. Then suggest concrete changes to the doc.”*

Reference: [Review Panel Personas](../01-knowledge-base/processes/review-panel-personas.md) (Sam, Jordan, Drew, Alex, Morgan, Casey, Riley, Quinn, Reese, Taylor) when you want the AI to reason from concrete, support-aware reviewer perspectives.

### Option C: Live panel (with real people)

- Share the doc and the [persona definitions](../01-knowledge-base/processes/review-panel-personas.md).
- Assign each reviewer one persona (or rotate).
- Collect feedback in one place, then refine the doc and close the loop.

---

## Quick Reference: Panel Checklist

Use this when refining a document. Consider each persona and note any actions.

| Persona              | Considered? | Actions / notes |
|----------------------|------------|-----------------|
| Product Manager (Sam)     | ☐          |                 |
| Software Engineering/Tech lead (Jordan) | ☐ |                 |
| Product Designer (Drew)   | ☐          |                 |
| Operations agent (Alex)   | ☐          |                 |
| Chief of Product (Morgan) | ☐          |                 |
| Chief of Operations (Casey) | ☐         |                 |
| Product Data Scientist (Riley) | ☐      |                 |
| Zendesk Administrator (Quinn) | ☐      |                 |
| Content Strategist (Reese) | ☐      |                 |
| VP of Product (Taylor) | ☐      |                 |

---

## Where This Fits in Your Workflows

- **PRDs**: Run the panel after drafting (e.g. after [requirement-writing.md](requirement-writing.md) Step 9) and before “Document & Communicate” and stakeholder share.
- **Reports and status updates**: Run before sending; especially useful for CPO/COO-facing updates (see [stakeholder-updates.md](stakeholder-updates.md)).
- **C-suite memos**: Run before sending to CPO or COO (see `03-templates/c-suite-memo-template.md`).
- **Ad hoc**: Use whenever you want a structured multi-perspective pass on any important doc.

---

## Tips & Best Practices

- **Order**: Running PM → Software Engineering → Product Designer → Ops → Zendesk Administrator → Content Strategist → Product Data Scientist → VP of Product → CPO → COO often works well (detail first, then UX and measurability, then strategy and ops leadership).
- **Don’t over-edit**: Use the panel to find gaps and sharpen clarity; you don’t need to satisfy every hypothetical concern, only the ones that matter for this doc.
- **Reuse**: Once you’ve run the panel on a doc type (e.g. PRDs), you’ll internalise many of the questions and can do a lighter pass next time.
- **AI assist**: When using AI to “simulate” the panel, paste the persona section from [review-panel-personas.md](../01-knowledge-base/processes/review-panel-personas.md) so the model stays aligned with your definitions.

---

**Owner**: Charlie Wildish  
**Last Updated**: Feb 2026
