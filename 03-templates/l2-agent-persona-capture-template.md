# L2 Agent Persona Capture — Interview Template

**Agent name:**
**Focus area (self-described):**
**Date:**
**Interviewer:**

---

## 1. Domain Coverage

*Goal: map to taxonomy nodes*

- Which case types do you handle most? Which do you almost never touch?
- Within those, which issue types do you consider yourself the go-to for?
- Are there any issue types you share with another agent, and if so, how do you decide who picks it up?

---

## 2. Product Depth

*Goal: map to product catalogue*

- Which Checkout products do you know best — well enough to resolve without escalating or checking docs?
- Which products do you handle but typically need to reference documentation or ask someone?
- Which products do you actively avoid or always hand off?

---

## 3. Triage Heuristics

*Goal: decision logic for sub-agent routing*

- When a ticket lands with you, what's the first thing you look at to decide whether you can resolve it?
- What signals tell you immediately that a ticket needs escalating, regardless of topic?
- What's an example of a ticket that looks straightforward but isn't? What's the trap?

---

## 4. Resolution Patterns

*Goal: capture known playbooks and edge cases*

- For your most common ticket type, walk me through your typical resolution steps.
- What information do you almost always need that isn't in the original ticket?
- What's the most common mistake a junior agent makes on your ticket types?

---

## 5. Escalation Behaviour

*Goal: define sub-agent handoff conditions*

- What do you escalate, and to whom? (Engineering / Fin team / Compliance / External)
- What does an escalation-ready ticket look like — what do you include before handing off?
- Is there anything you would never try to resolve in Zendesk alone (requires a tool, portal, or call)?

---

## 6. Edge Cases and Tribal Knowledge

*Goal: capture tacit knowledge not in SOPs*

- What's something you know that isn't written down anywhere?
- What's a situation where following the SOP exactly would give the wrong outcome?
- What should a new agent never do on your ticket types?

---

## Interviewer Notes

*Fill in after session:*

- Taxonomy nodes confirmed: `[ ]`
- Products confirmed: `[ ]`
- Escalation paths confirmed: `[ ]`
- Gaps / follow-up needed: `[ ]`

---

## Processing Instructions (for Claude)

When given a transcript of this interview, produce a structured persona by matching the agent's answers to canonical values — do not alter what the agent said, only normalise the output fields.

**Taxonomy matching** — cross-reference `01-knowledge-base/processes/support-taxonomy.md`:
- Map the agent's described case types and issue types to the exact taxonomy labels in that file
- Where the agent's language doesn't match a taxonomy label exactly, pick the closest match and note the discrepancy
- Flag any case types or issue types the agent mentions that don't exist in the taxonomy

**Product matching** — cross-reference `01-knowledge-base/products/product-definitions.md` and `01-knowledge-base/Checkout Products and teams.csv`:
- Map product names to exact names in the product catalogue
- Where the agent uses informal names or abbreviations, resolve to the canonical product name and note the alias used
- Flag any products mentioned that don't appear in either reference file

**Preserve verbatim**: keep the agent's own words for triage heuristics, resolution patterns, escalation behaviour, and tribal knowledge — these are prompt-ready and must not be paraphrased.

**Output format**: produce a markdown persona file with sections:
1. Identity (name, focus area, date)
2. Taxonomy coverage (canonical labels, with confidence: primary / secondary / handles-sometimes)
3. Product depth (canonical names, with confidence: expert / familiar / avoid)
4. Triage heuristics (verbatim)
5. Resolution patterns (verbatim)
6. Escalation rules (verbatim + escalation targets)
7. Tribal knowledge (verbatim)
8. Matching notes (discrepancies, unresolved names, taxonomy gaps)
