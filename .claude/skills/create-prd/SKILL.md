---
name: create-prd
description: Run the full PRD creation workflow (Draft → Review Panel Critique → Refine → Condense) for a Care Product initiative. Invoke with /create-prd [topic or deliverable name]. Outputs a finished PRD saved to 04-active-work/.
tools: Read, Glob, Grep, Bash, Write, Agent
---

# Create PRD

Run the full four-phase PRD workflow: **Draft → Critique → Refine → Condense**.

## Model routing

| Phase | Model | Reason |
|-------|-------|--------|
| Phase 1 — Orient | Opus | Strategic anchoring, roadmap alignment, problem framing |
| Phase 2 — Draft | Sonnet | Structured writing against template |
| Phase 3 — Critique | Opus | Deep multi-persona reasoning |
| Phase 4 — Refine & Condense | Sonnet | Editing, condensing, file output |

For Phase 1 and Phase 3, spawn an Agent with `model: "opus"`. Pass all relevant context (deliverable, reference files read, draft content) in the agent prompt. Use the agent's output as the input to the next phase — do not proceed until you have it.

---

## Phase 1 — Orient

Before writing anything:

1. **Check for existing work.** Search `04-active-work/` for any file related to the topic. If found, read it before proceeding — the PRD may already be partially done.

2. **Anchor to the roadmap.** Read `2026 deliverables.md`. Confirm the topic maps to a named 2026 deliverable. If it doesn't map clearly, flag this to the user before proceeding — floating work is not written.

3. **Gather context.** Read the following files to build background before drafting:
   - `03-templates/prd-template.md` — section-by-section guidance
   - `03-templates/prd-template-example.md` — annotated example with quality rules
   - `01-knowledge-base/strategy/care-product-model.md` — flywheel domain reference
   - `01-knowledge-base/products/customer-personas.md` — merchant and internal personas
   - `01-knowledge-base/products/customer-segments.md` — merchant segments

4. **Clarify if needed.** If the deliverable, strategic goal, or core problem is unclear, ask one question to fill the most important gap. Do not ask multiple questions.

5. **Spawn an Opus agent** with the following prompt structure:
   > "You are doing strategic analysis for a PRD on [topic]. The 2026 deliverable is [deliverable text verbatim]. Read the following context: [paste content from care-product-model.md, customer-personas.md, customer-segments.md]. Produce: (1) the correct flywheel domain and a 2-sentence explanation of fit, (2) the primary strategic goal (reduce contact rate / reduce cost of support), (3) the top 3 open strategic questions the PRD must answer, (4) any risks that could cause this initiative to float (not connect to strategy)."

   Wait for the Opus agent output before proceeding to Phase 2.

---

## Phase 2 — Draft

Fill in `03-templates/prd-template.md` with real content. Rules:

### Strategy block first (mandatory)
Fill the alignment table before any other section:

| Field | Value |
|-------|--------|
| **2026 deliverable** | Name from `2026 deliverables.md` |
| **Strategic goal** | Reduce contact rate · Reduce cost of support |
| **Flywheel domain** | Input · Orchestration · Fuel · Agent Experience · Insight & Prevention · Governance |
| **How it fits** | 1–2 sentences connecting the initiative to the deliverable and goal |

### Data — no placeholders
Pull real contact volume from the CSV data source:

```python
import pandas as pd
df = pd.read_csv('01-knowledge-base/metrics/support_contacts_flat_table_2025_last_6m.csv')
summary = df.groupby(['case_type', 'issue_type'])['support_contacts'].sum().sort_values(ascending=False)
print(summary.head(30))
```

Run this from the repo root. Use output for problem sizing in the Problem Space section.

Column definitions: `01-knowledge-base/metrics/support_contacts_flat_table_2025_metric_definitions.md`
Issue type structure: `01-knowledge-base/processes/support-taxonomy.md`

**Baseline rule**: Every success metric row must have a real number or `TBC — establish by [date]`. Bare "TBC" is not acceptable.

### Instrumentation field names
Field names in the Instrumentation section must match the column names in `support_contacts_flat_table_2025_metric_definitions.md` exactly.

### Writing style
- Lead with the point — conclusion first, evidence after
- Short paragraphs (2–3 sentences), active voice, specific numbers
- No em dashes as clause connectors
- No hedging language ("may", "could potentially", "somewhat")

---

## Phase 3 — Critique (Document Review Panel)

**Spawn an Opus agent** for this phase. Pass it: (1) the full PRD draft text, (2) the content of `01-knowledge-base/processes/review-panel-personas.md`. Instruct it to run all applicable personas and return structured critique output (see below). Wait for the result before proceeding to Phase 4.

Run the 5 core personas. Read `01-knowledge-base/processes/review-panel-personas.md` for full backstory, goals, and typical questions for each.

For each persona, produce:
- **Top 3 issues** with the current draft
- **One "approve if fixed" condition** — the single most important thing that must be resolved

### Core personas (always run)

| Persona | Name | Primary lens |
|---------|------|--------------|
| Operations Agent | Oliver | Frontline execution: can agents act on this? Are SLA impacts addressed? Is the runbook complete? |
| Chief of Operations | Casey | Capacity, training cost, operational risk, change management |
| Product Data Scientist | Imran | Metric definitions, baselines, data quality, instrumentation completeness |
| Content Strategist | Preethy | Content dependencies, knowledge article gaps, resolution rate implications |
| VP of Product | Taylor | Strategic alignment, exec pitch clarity, "why this, why now?" |

### Conditional personas
Check `01-knowledge-base/processes/review-panel-personas.md` for the rules on when to add:
- **Sam** (PM) — cross-team scope or dependency on another squad
- **Fraser** (Engineering/Tech Lead) — significant backend build or API work
- **Georgios** (Product Designer) — merchant-facing UI or self-service flow
- **Morgan** (Chief of Product) — C-suite or board-level strategic document
- **Ajana** (Zendesk Administrator) — routing, taxonomy, or Zendesk config changes

---

## Phase 4 — Refine & Condense

1. Address every "approve if fixed" condition from Phase 3.
2. Address the highest-severity issues from each persona.
3. Cut to ~250–350 lines. Remove scaffolding instructions, placeholder text, and redundant explanations.
4. Ensure all section headers match the template structure.
5. Save the final PRD to `04-active-work/[kebab-case-title].md`.

Report to the user:
- File path saved
- Which panel issues were resolved
- Any open questions that remain (flag for the user to answer, don't invent answers)
