---
name: strategic-review
description: Deep strategic review of any initiative, topic, or document. Opus analyses alignment, surfaces tensions, and asks hard questions. Sonnet writes the output. Invoke with /strategic-review [topic, file path, or initiative name]. Outputs a structured memo or strategy assessment saved to 04-active-work/.
tools: Read, Glob, Grep, Bash, Write, Agent
---

# Strategic Review

Two-phase workflow: **Opus analyses → Sonnet writes**.

## Model routing

| Phase | Model | Reason |
|-------|-------|--------|
| Phase 1 — Strategic analysis | Opus | Deep reasoning: diagnosis, tensions, strategic alignment, hard questions |
| Phase 2 — Written output | Sonnet | Structured memo or assessment against template |

---

## Phase 1 — Orient (current model, Sonnet)

Before calling Opus:

1. **Identify the subject.** If a file path was passed, read it. If a topic was passed, search `04-active-work/` for existing work on it.
2. **Read the strategy anchors:**
   - `2026 deliverables.md` — confirm whether the topic maps to a named deliverable
   - `01-knowledge-base/strategy/care-product-model.md` — flywheel domains
   - `01-knowledge-base/strategy/rumelt-strategy-kernel.md` — Diagnosis / Guiding Policy / Coherent Actions framework
3. **Assemble the brief** — gather enough context to give Opus a self-contained prompt (subject, any existing doc, relevant deliverable text, strategic goal).

---

## Phase 2 — Opus Strategic Analysis

Spawn an Agent with `model: "opus"`. Pass it everything assembled in Phase 1. Use this prompt structure:

> "You are doing a strategic review for a Product Manager at a global PSP (Checkout.com). The subject is: [topic or paste of document].
>
> The relevant 2026 deliverable is: [verbatim text from 2026 deliverables.md, or 'does not map to a named deliverable'].
>
> Strategic goals: reduce contact rate · reduce cost of support. North star metrics: contact rate (contacts per 1M transactions), cost per contact. Guardrail: merchant CSAT must not decline.
>
> Flywheel domains: Input → Orchestration → Fuel → Agent Experience → Insight & Prevention → Governance.
>
> Apply Rumelt's Strategy Kernel. Produce:
> 1. **Diagnosis** — What is the one pivotal difficulty or challenge this addresses? Name it precisely. If the subject fails to name a real challenge, say so.
> 2. **Strategic alignment** — Does this map clearly to a 2026 deliverable and strategic goal? If not, flag it as floating work.
> 3. **Flywheel domain** — Which domain does this sit in, and why?
> 4. **Tensions and risks** — What are the 2-3 sharpest tensions or risks in this initiative? (e.g. scope vs. team capacity, AI resolution vs. CSAT guardrail, short-term vs. long-term)
> 5. **Hard questions** — What are the 3 questions Charlie must be able to answer before this is ready to share with leadership? Be specific and demanding.
> 6. **Bad strategy check** — Apply Rumelt's four hallmarks of bad strategy (fluff, failure to face the challenge, goals mistaken for strategy, incoherent actions). Flag any that apply.
> 7. **Verdict** — One sentence: is this strategically sound, needs sharpening, or is it floating?"

Wait for the Opus agent output before proceeding.

---

## Phase 3 — Written Output (Sonnet)

Choose the output format based on the subject:

| Subject type | Output format |
|---|---|
| Initiative or roadmap item | Strategic assessment memo (`03-templates/c-suite-memo-template.md`) |
| Multi-year strategy document | Strategy review against `03-templates/product-strategy-template.md` |
| PRD or spec | Structured critique with verdict and required changes |
| Open question / exploration | Structured analysis: Diagnosis → Options → Recommendation |

Rules:
- Lead with the verdict from Opus
- Incorporate Opus's diagnosis, tensions, and hard questions directly — do not paraphrase them into mush
- Short paragraphs, active voice, specific numbers where available
- No em dashes, no hedging language
- End with a clear next step: what must happen before this is ready to progress

Save the output to `04-active-work/strategic-review-[kebab-case-topic]-[YYYY-MM-DD].md`.

Report to the user:
- File path saved
- The one-sentence verdict from Opus
- The top hard question that must be answered before sharing with leadership
