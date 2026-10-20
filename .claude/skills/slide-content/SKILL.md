---
name: slide-content
description: Turn notes, a document, or a deck outline into layout-enforced, density-constrained slide prompts for Gemini in Google Slides. Invoke with /slide-content [topic, file path, or pasted notes]. Outputs paste-ready Gemini prompts, one per slide. If given a /presentation-outline file, appends the prompts to that same file; otherwise saves to 04-active-work/working-files/.
tools: Read, Glob, Grep, Write
---

# Slide Content (Gemini prompt architect)

Convert raw content into prompts Gemini can render without inventing text. Gemini follows explicit layout keywords and hard word limits far better than free-form requests, so every prompt names the layout, states the exact text, and forbids extras.

## Step 1 - Gather inputs

Read any file path or pasted notes passed in. If the input is a `/presentation-outline` file (`presentation-<topic>-<date>.md`), use its ghost deck as the slide plan: keep its slide order and statuses, reuse its audience and assumptions, and carry its `[NEEDS DATA]` gaps through. Derive each fragment title (max 10 words) from the action title; the full-sentence action title stays in the outline. Establish (infer first, ask one question at most):

- **Audience and tone** (default: VP/C-suite, direct, minimal; see audience profiles in `01-knowledge-base/processes/writing-style-guide.md`)
- **Slide count** (default: one slide per distinct point, no more than 1 message per slide)
- **Grounding**: numbers must come from the source or `01-knowledge-base/` / `04-active-work/working-files/Contact breakdown since April 2026.md`. Never invent or round-up figures. If a number is missing, write `[NEEDS DATA: description]` in the slide and list it in the notes.
- **Strategy tie-in**: each slide's message should connect to contact rate, cost per contact, or Merchant CSAT, or a named deliverable in `2026 deliverables.md`. Flag slides that float.

## Step 2 - Plan the deck

List slides as: number | one-sentence takeaway | layout. Show this plan to the user only if the deck is 5+ slides; otherwise proceed.

Rules:
- Open with the answer, not the context (conclusion first, evidence after).
- Last slide is the ask, decision, or next step.
- Deck of 1 slide uses the Single Slide schema; 2+ uses the Multi-Slide schema for the overview, then a Single Slide prompt per slide (Gemini renders detail better one slide at a time).

## Step 3 - Map content to a layout keyword

Pick exactly one per slide. Never use "bullet list" as a layout.

| Content | Layout keyword | Spec |
|---|---|---|
| One headline metric | Big Number Hero | Dominant stat, one-line subtitle, optional 3-column sub-stat row |
| 3 pillars / features / options | 3-Card Grid | Equal cards, bold header, 1-3 fragments each |
| 4 categories | 4-Tile Matrix | 2x2, header + 1-2 fragments per tile |
| Sequence / roadmap / phases | Horizontal Linear Timeline | 3-5 steps, label above, fragment below |
| Two states / options | 2-Column Split | Left vs right, parallel structure, equal item count |
| Before vs after | Before vs After Grid | Rows aligned across both columns |
| Trend or comparison of numbers | Single Chart + Callout | State chart type, axes, exact data points, one takeaway line |
| Title / section break | Minimal Title | Title + optional one-line subtitle, no bullets |

If content fits none, split it across two slides instead of crowding one.

## Step 4 - Apply density rules

Inject these into every prompt:

- **Fragments only.** No full sentences, no trailing periods, no transitions.
- **Max 3-4 items** per card/column/tile; **max 8 words per item**, not counting the lead-in.
- **2-3 word bold lead-in** on every list item and card header.
- **Title is the takeaway as a fragment**, max 10 words, containing the number where one exists ("Contact rate down 12% since April"), not a topic label ("Contact Rate Update").
- **Numbers**: exact, with unit and period. One stat per Big Number Hero.
- **Style**: straight quotes, plain ASCII, no em dashes, no hedging words, no AI-trope vocabulary (see writing style guide).
- **No invented content**: Gemini may not add statistics, icons-as-text, taglines, or filler.
- **Visuals**: describe at most one supporting visual per slide, and only when the layout needs it (Chart, Timeline). Otherwise "no imagery".

## Step 5 - Output

Write each prompt in a fenced `text` block so it copies cleanly. Use these schemas.

**Single slide**

```text
Role: Expert Google Slides designer.
Task: Create one slide for [TOPIC].
Audience: [AUDIENCE] | Tone: [TONE]
Slide title: "[EXACT TITLE FRAGMENT]"
Layout: [LAYOUT KEYWORD + spec from table]

Content:
- [Lead-in]: [fragment]
- [Lead-in]: [fragment]
- [Lead-in]: [fragment]

Constraints: Use only the text above, verbatim. Fragment grammar, no full sentences, no periods. Max 8 words per item excluding lead-in. Bold lead-ins. No added statistics, taglines, or intro/outro text. Clean, minimal, consistent spacing. [Visual: none | describe]
```

**Multi-slide overview** (use first, to set deck-level context)

```text
Role: Expert Google Slides designer.
Task: Create a [N]-slide presentation on [TOPIC].
Audience: [AUDIENCE] | Tone: [TONE]
Grounding: [@Doc/@Sheet or "text below only"]

Slide breakdown:
- Slide 1: "[TITLE]" | Layout: [keyword]
- Slide 2: "[TITLE]" | Layout: [keyword]
...

Global constraints: Headline fragments only. Max 3-4 items per card/column. Max 8 words per item. Bold 2-3 word lead-ins. No paragraphs, no filler, no added statistics. Same fonts, colours and spacing on every slide.
```

If the input was a `/presentation-outline` file, append a `## Gemini prompts` section to that same file (replace it if one exists) and do not create a second file. Otherwise save to `04-active-work/working-files/slide-content-<topic>-<YYYY-MM-DD>.md` (check for an existing file on the topic first and update it instead). Format: overview prompt first, then one section per slide with its prompt block.

## Step 6 - Self-check before replying

For each slide confirm: one message, layout keyword from the table, title carries the takeaway, every item within word limits, every number sourced, no `[NEEDS DATA]` left unmentioned. Fix failures silently.

Reply with the file link, the slide plan (number, title, layout) and any `[NEEDS DATA]` gaps. No other summary.
