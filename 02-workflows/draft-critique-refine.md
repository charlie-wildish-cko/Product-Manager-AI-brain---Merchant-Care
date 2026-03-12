# Draft → Critique → Refine → Condense Workflow

> Use this workflow when you want a polished, reviewed document produced automatically before you look at it. AI drafts, applies the Document Review Panel, refines, and (for PRDs) condenses to the template — you only step in at the end.

## When to use this workflow

- You have a brief and want a finished document to review, not a raw first draft
- You want the Review Panel applied before you share with stakeholders
- You're under time pressure and want to compress the write → review → revise cycle
- You want to sanity-check a document against multiple perspectives without running the panel manually

**This workflow is not a substitute for stakeholder review.** It gives you a structurally sound, well-argued draft ready for that review — it does not replace it.

---

## How it works

Four phases run automatically in a single AI response (for PRDs; three phases for other doc types):

```
Brief + context
      ↓
[Phase 1] DRAFT     — AI writes first draft from the relevant template; for Care & Support PRDs, anchor in strategy first (deliverable, goal, flywheel domain, north star/domain metrics) per [requirement-writing.md](requirement-writing.md) Step 0
      ↓
[Phase 2] CRITIQUE  — AI applies Review Panel personas relevant to the doc type; for PRDs, also applies Socratic question categories (problem clarity, solution fit, success criteria, scope) from [socratic-questioning-prds.md](../01-knowledge-base/processes/socratic-questioning-prds.md)
      ↓
[Phase 3] REFINE    — AI rewrites to address the critique
      ↓
[Phase 4] CONDENSE  — (PRDs only) AI shortens the PRD to match [prd-template.md](../03-templates/prd-template.md): section order, one table per section where specified, detail moved to Appendix; target body ~250–350 lines; decisions and gates preserved
      ↓
Handoff to you      — Refined doc + summary of what changed + unresolved items
```

You provide the brief. You review the finished output.

---

## How to trigger it

Tell the AI what you want to produce and provide your brief. The skill picks the right template and persona set automatically.

```
"Draft and refine a PRD for [feature]. Here's the brief: [paste]"

"Draft and refine a C-suite memo on [topic] for CPO/COO. Context: [paste]"

"Run draft-critique-refine on a stakeholder update. Here's what happened: [summary]"

"Draft and refine a scoping one-pager on [topic]"
```

The more context you give upfront, the less the AI needs to ask and the stronger the draft. A thin brief produces a generic draft that requires heavy rework; a sufficient brief produces a document that needs only light editing.

**Brief quality check — does yours include all five elements?**

| Element | Thin brief (will produce a weak draft) | Sufficient brief |
|---------|---------------------------------------|-----------------|
| **Problem** | "Need a PRD for Blue EMI support" | "Blue EMI merchants have no support channel; entity ID can't be inferred from email alone; need Zendesk config + webform routing" |
| **Metrics** | *(missing)* | "No baseline exists; success = 100% correct routing at launch; track by support volume to correct queue" |
| **Strategic anchor** | *(missing)* | "2026 deliverable: Agent Productivity Tools; goal: reduce cost of support; flywheel: Agent Experience" |
| **Constraints** | *(missing)* | "Brand decision pending (blocks entity naming); B2C out of scope; ~5 merchants at launch, ~20 by EOY" |
| **Audience** | *(missing)* | "Zendesk Admins, Care Ops, Engineering counterpart; VP of Product for approval" |

**For Care & Support PRDs**, include in the brief (or the AI will infer from context): which **2026 deliverable** this supports, which **strategic goal** (reduce contact rate / reduce cost), and which **flywheel domain**. That anchors the draft in the strategy-first flow (requirement-writing Step 0).

---

## Persona sets by document type

The AI selects a subset of the nine Document Review Panel personas depending on what's being written. It applies their lenses from [document-review-panel.md](document-review-panel.md) to find gaps before rewriting.

| Doc type | Personas applied |
|----------|-----------------|
| **PRD — merchant-facing** (feature or product that changes what a merchant sees, does, or receives) | PM, Designer, Operations Agent, Data Scientist, Chief of Operations, VP of Product; critique also uses [Socratic question categories](../01-knowledge-base/processes/socratic-questioning-prds.md) |
| **PRD — internal** (config, tooling, policy, or process with no direct merchant impact) | PM, Tech Lead, Operations Agent, Zendesk Administrator, VP of Product; critique also uses [Socratic question categories](../01-knowledge-base/processes/socratic-questioning-prds.md) |
| C-suite memo | PM, Chief of Product, Chief of Operations, Product Data Scientist, VP of Product; critique can draw on [Rumelt's Strategy Kernel](../01-knowledge-base/strategy/rumelt-strategy-kernel.md) for diagnosis/policy/actions coherence |
| Stakeholder update | PM, Operations Agent, VP of Product |
| One-pager / scoping doc | PM, Chief of Product, Product Data Scientist |
| Other | PM, Chief of Product, VP of Product |

*Operations Agent is present in both PRD tiers — they bridge product decisions and merchant-facing execution regardless of scope.*

For full persona backstories and detailed lenses, see [review-panel-personas.md](../01-knowledge-base/processes/review-panel-personas.md).

---

## What you receive at handoff

1. **Refined document** — the complete, ready-to-review document
2. **What changed** — 3–6 bullets summarising the main improvements made in Phase 3
3. **Unresolved items** — critique points that need your input to close (e.g. missing data, unknown stakeholder names); omitted if there are none

---

## Iterating after review

If you want to revise after reading the output:

- **Small edits**: Make them directly in the document, then ask the AI to "do a final pass" or address a specific point
- **Major revision**: Give the AI your edits or new context and ask it to "re-run the critique and refine" on the updated draft
- **Re-run the panel only**: Use [document-review-panel.md](document-review-panel.md) Option B for a targeted simulated panel without a full redraft

---

## Where this fits in your other workflows

| Workflow | Relationship |
|----------|-------------|
| [requirement-writing.md](requirement-writing.md) | Run draft-critique-refine after Step 8 (dependencies & constraints) instead of running the panel manually in Step 9 |
| [document-review-panel.md](document-review-panel.md) | This workflow automates Option B (simulated panel). Use document-review-panel.md directly for Option A (manual checklist) or Option C (real reviewers) |
| [stakeholder-updates.md](stakeholder-updates.md) | Use draft-critique-refine instead of writing the update manually, then follow stakeholder-updates.md for distribution |

---

**Owner**: Charlie Wildish
**Last updated**: March 2026
