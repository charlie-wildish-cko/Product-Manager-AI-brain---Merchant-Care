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

---

## AI Writing Tropes to Avoid (applies to all output)
Source: [tropes.fyi](https://tropes.fyi) by [ossama.is](https://ossama.is). Any one of these used once might be fine — the problem is repetition, or several appearing together.

**Word choice**
- Magic adverbs: "quietly", "deeply", "fundamentally", "remarkably", "arguably"
- "Delve" and its family: "certainly", "utilize", "leverage" (as a verb), "robust", "streamline", "harness"
- Grandiose nouns: "tapestry", "landscape", "paradigm", "synergy", "ecosystem", "framework" (unless literally a technical framework)
- The "serves as" dodge — replacing "is"/"are" with "serves as", "stands as", "marks", "represents"

**Sentence structure**
- Negative parallelism: "It's not X — it's Y" and "not because X, but because Y"
- Dramatic countdown: "Not X. Not Y. Just Z."
- Self-posed rhetorical Q&A: "The result? Devastating."
- Anaphora abuse: repeating the same sentence opener three-plus times in a row
- Tricolon abuse: stacked rule-of-three constructions back to back
- Empty transitions: "it's worth noting", "it bears mentioning", "importantly", "interestingly", "notably"
- Superficial -ing tacked on for fake significance: "...highlighting its importance", "...reflecting broader trends"
- False ranges: "from X to Y" where X and Y aren't on a real scale

**Paragraph structure**
- Short punchy fragments as standalone paragraphs for manufactured emphasis
- Listicle in a trench coat: "The first wall is... The second wall is..." dressed as prose

**Tone**
- False suspense: "here's the kicker", "here's the thing", "here's where it gets interesting"
- Patronizing analogy: "think of it as...", "it's like a..."
- "Imagine a world where..."
- False vulnerability / performative self-awareness: "and yes, I'm openly..."
- Asserting simplicity instead of proving it: "the truth is simple", "history is unambiguous"
- Stakes inflation: "this will fundamentally reshape everything"
- Hand-holding pedagogy: "let's break this down", "let's unpack this"
- Vague attribution: "experts argue", "industry reports suggest", "observers have cited" — name the source or cut the claim
- Invented compound labels used as if established: "the supervision paradox", "workload creep"

**Formatting**
- Em-dash overuse for dramatic pauses (2-3 per document max; already banned in this guide — see top)
- Bold-first bullets where every single item opens with a bolded phrase
- Unicode decoration: `->` arrows, curly/smart quotes — type straight quotes and plain ASCII

**Composition**
- Fractal summaries: summarizing at every level (subsection, section, and document)
- Dead metaphor beaten across the whole document
- Historical analogy stacking: rapid-fire "Apple didn't build Uber. Facebook didn't build Spotify..."
- One-point dilution: restating a single thesis many ways to look comprehensive
- Content duplication: repeating a section or paragraph verbatim
- Signposted conclusions: "in conclusion", "to sum up", "in summary"
- "Despite its challenges..." formula: acknowledge a problem only to wave it away
