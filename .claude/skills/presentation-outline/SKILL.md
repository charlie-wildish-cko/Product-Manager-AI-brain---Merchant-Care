---
name: presentation-outline
description: Build presentation outlines, storylines and ghost decks using the consulting method (Pyramid Principle, SCQA, action titles, MECE). Invoke with /presentation-outline [topic, file path or notes]. Use for deck structure, storyline, slide plan, exec update, strategy readout or recommendation deck, or to critique an existing outline. Output is the single working file that /slide-content later extends with Gemini prompts.
tools: Read, Glob, Grep, Write
---

# Presentation outline

Produce outlines where the answer comes first, every slide title is a full-sentence claim, and the deck can be understood by reading the titles alone. This skill decides the story. `/slide-content` then adds Gemini prompts to the same file.

## Step 1 - Pin down the brief

Read any file path or notes passed in, and check `04-active-work/` and `05-archive/` for an existing outline on the topic (update it rather than start a new one). Establish, inferring first and asking one question at most, and only if the answer would change the whole structure:

- Audience: who they are, what they know, what they care about (default VP/Director/C-suite; see audience profiles in `01-knowledge-base/processes/writing-style-guide.md`)
- Decision or action wanted from them
- Format: live, pre-read, or both
- Time or slide limit
- Source material

State assumptions in one line.

## Step 2 - Governing thought

One or two sentences that answer the audience's question and state the recommendation. If you cannot write it, the thinking is not finished: say so and help get there (suggest `/five-whys` if the problem is unclear).

Test: could the audience act on this sentence alone?

## Step 3 - SCQA

Four short lines: Situation (what the audience agrees is true), Complication (what changed or what problem exists), Question (what the complication raises), Answer (the governing thought). Keep Situation and Complication brief.

## Step 4 - Key line

Break the governing thought into 3 supporting arguments (2 to 4 acceptable). Each is a full-sentence claim, MECE with its siblings, and ordered by one clear logic: deductive, inductive, structural, time, or importance. Repeat one level down with 2 to 4 supporting points each. Never nest more than three levels.

## Step 5 - Logic tests

- Vertical: read any parent claim and ask "why?" or "how do we know?". The children must answer it.
- Horizontal: claims at one level read as a coherent argument.
- Title test: the slide titles alone are a complete, persuasive summary.

Fix failures before presenting.

## Step 6 - Ghost deck

For each slide: number, action title (full sentence with a verb and a "so what", two lines or fewer), evidence needed, suggested visual, status (data in hand / data to get / assumption).

Default structure unless the brief says otherwise:

1. Executive summary (whole story, answer first)
2. Context and complication (only as long as needed)
3. Body sections, one per key line argument
4. Recommendation, trade-offs and risks
5. Next steps and the specific decision or ask, with owners and dates
6. Appendix

## Slide rules

- One message per slide
- Title states the conclusion, body proves it
- Every number needs a comparison (vs target, last period, benchmark)
- Cut any slide that does not support a key line argument
- Recommendation early for senior audiences
- Numbers come from the source or `01-knowledge-base/` / `04-active-work/working-files/Contact breakdown since April 2026.md`. Never invent. Missing numbers are `[NEEDS DATA: description]` with status "data to get".
- Tie the deck to strategy: connect arguments to contact rate, cost per contact, Merchant CSAT, or a named deliverable in `2026 deliverables.md`. Flag slides that float.

## Output

Save to `04-active-work/working-files/presentation-<topic>-<YYYY-MM-DD>.md` with these sections in order:

1. Assumptions
2. Governing thought
3. SCQA
4. Key line (nested list)
5. Ghost deck (table: #, action title, evidence needed, visual, status)
6. Gaps and risks: weak arguments, missing data, likely pushback

Reply with the file link, the governing thought, the titles list, and the gaps. End with: "Run `/slide-content <file>` to add Gemini prompts to this file."

Follow the writing style in `CLAUDE.md`: no em dashes, no hedging, no flattery, flag weak logic honestly.

## Critiquing an existing deck

Extract the slide titles first and run the three logic tests. Report where the answer is buried or missing, titles that are topics not claims, MECE failures, slides to cut or merge, and a rewritten title list.

## Common failures to avoid

- Topic titles ("Q3 Results", "Next steps overview")
- Building up to the answer instead of leading with it
- Lists of facts with no synthesis
- An executive summary that restates the agenda
- A recommendation with no trade-offs
