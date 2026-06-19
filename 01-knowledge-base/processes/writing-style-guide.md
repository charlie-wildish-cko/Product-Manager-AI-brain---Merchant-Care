# Writing Style Guide

## Leadership / C-suite
- 2-minute read max
- Recommendation first, then bullets with supporting evidence
- Clear business impact tied to metrics

## Slack updates
- Informal, concise (~10 lines max), emoji for scannability
- Conversational tone

## Engineering
- Formal and precise: exact endpoints, field names, Given/When/Then acceptance criteria

## Reports & readouts
- Narrative headers: "What we did / What we found / What this means / What we recommend"
- Bold-lead each finding with its key insight
- Evidence inline at point of claim, not in an appendix
- Numbered, actionable recommendations with bold titles

## Strategy & analysis documents
Cross-functional docs: problem statements, initiative strategies, segmentation analyses, competitive benchmarks.

**Structure**
- Every section leads with its conclusion, not context. If the section title is "Goal rationale", the first sentence states the goal — not the background.
- Executive summary = problem + data point, solution, deliverable. Three sentences max.
- Restate nothing from the exec summary in the body — go deeper or go further.

**Tables**
- Add a **TLDR:** line before any table longer than 5 rows. State the single most important takeaway.
- Bold-lead quantified findings within cells: "**Payment confirmation** 28%" not "Payment confirmation (28%)".
- Never use "TBC" in a table cell. Use "pending [named event or decision]" or leave blank with a footnote explaining what unblocks it.

**Inline callout patterns**
- **Note:** — a caveat, competitor comparison, or important constraint. One sentence.
- **TLDR:** — the point of a section or table, before the detail.
- **Ask:** — a request for input or a decision needed from a named person. Must include an owner and, where possible, a timeframe. "**Ask**: [Name] to confirm scope by end of Q3" not "**Ask**: someone to look into this".

**Hypothesis framing**
- When presenting analysis, state the hypothesis before the evidence: "Hypothesis: merchants in low-PSE segments drive disproportionate ticket volume. Finding: confirmed — Low TPV, Low PSE accounts for 49% of tickets from 57% of merchants."

**Hedging — never use**
- "we believe", "we could", "may not necessarily", "suggest a [timeframe]"
- State claims directly. If something is an estimate, say "estimate: X%" — don't hedge the estimate itself ("we estimate it could be around X%").

**Action items**
- Every recommendation must have: a named owner, a scope, and a timeframe or the named event that sets the timeframe.
- "For discussion with [Name]" is not an action item. Either assign it or remove it.
