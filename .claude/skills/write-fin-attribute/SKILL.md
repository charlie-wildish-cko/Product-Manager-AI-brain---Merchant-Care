---
name: write-fin-attribute
description: Draft or update a single Fin Attribute value definition (Case Type, Issue Type, or Reason) in Intercom's Applies-if/Does-not-apply-if/Likely-keywords format, from a value name, its place in the taxonomy, a plain-English definition, and example queries. Writes the result into both fin-attributes-definitions.md (Intercom-ready) and support-taxonomy.md (the QA skill's parseable source), checking for boundary overlaps against sibling nodes and enforcing Intercom's 2500-character limit per value. Invoke with /write-fin-attribute, then supply the value name, taxonomy path, definition, and example queries (conversationally or all at once).
tools: Read, Glob, Grep, Bash, Edit, Write
---

# Write Fin Attribute Definition

Turns a rough attribute idea into a ready-to-paste Fin Attribute value definition, and keeps the two taxonomy files in sync while doing it. This is the authoring counterpart to `/taxonomy-classification-qa` — that skill finds gaps in existing definitions from real contact data; this skill writes (or rewrites) a definition from scratch when a human already knows what the value should cover.

---

## Inputs

Collect these four things from the user, in any order, in a single message or across a short back-and-forth:

| Input | Required | Notes |
|---|---|---|
| **Value name** | Required | The exact name of the Case Type, Issue Type, or Reason (e.g. "Refund proof", "Bank payouts", "Compliance and audit") |
| **Taxonomy path** | Required | Where it sits: which level (Case Type / Issue Type / Reason) and, for Issue Type or Reason, the parent chain (e.g. "Issue Type under Payouts", "Reason under Accepting payments → Refunds") |
| **Definition** | Required | A plain-English sentence or two describing what this value covers |
| **Example queries** | Recommended, not blocking | A few real or representative customer messages/questions this value should match. If none are given, proceed without an `Example:` line rather than inventing one — do not fabricate a customer quote |

If the value name or taxonomy path is missing or ambiguous (e.g. "put this under Payments" when no Case Type by that exact name exists), ask one clarifying question before drafting. Do not guess a parent that doesn't exist in the current taxonomy.

---

## Source files (read both before drafting)

| Purpose | File |
|---|---|
| Intercom-ready attribute definitions (Applies-if/Does-not-apply-if/Likely-keywords format) | `01-knowledge-base/processes/fin-attributes-definitions.md` |
| Canonical taxonomy tree — parsed directly by `/taxonomy-classification-qa` to build its valid-pairs set | `01-knowledge-base/processes/support-taxonomy.md` |

Both files must be updated together and must stay structurally consistent — a value that exists in one but not the other will silently break `/taxonomy-classification-qa`'s label-validity checks the next time it runs. Never update one without the other.

---

## Execution

### Step 1 — Determine level and parent chain

Parse the taxonomy path into:
- **Level**: `case_type`, `issue_type`, or `reason`
- **Parent Case Type** (required for issue_type and reason)
- **Parent Issue Type** (required for reason)

Read `support-taxonomy.md` and confirm every named parent actually exists (case-insensitive match against `### ` headings for Case Type, `**...**` headings for Issue Type). If a named parent doesn't exist:
- If it's a small variant (e.g. "Payout" vs "Payouts"), confirm the likely match with the user in one line rather than blocking.
- If no plausible match exists, stop and ask — do not invent a new parent node without the user explicitly confirming that's what they want (that would be a bigger structural change than "write one definition").

### Step 2 — Check for an existing node at this exact path

Search `support-taxonomy.md` and `fin-attributes-definitions.md` for a node with this exact name at this exact path.
- **If found**: this is an update, not a new addition. Report this to the user before proceeding ("X already exists under Y with this definition: ... — replacing it, correct?") and treat the rest of this skill as a rewrite of that block, not an insert.
- **If not found**: this is a new node. Confirm which position it should slot into (end of the parent's list is the default — do not silently reorder existing siblings).

### Step 3 — Gather sibling and cross-taxonomy context

This is the step that catches ambiguous boundaries before they ship — do not skip it even for a "simple" definition.

1. List every sibling at the same level under the same immediate parent (e.g. every other Issue Type under the same Case Type). Read their full definitions.
2. Extract the likely keywords/signals implied by the new value's definition and example queries.
3. Grep `support-taxonomy.md` for any of those keywords/signals appearing in a *different* branch of the taxonomy (different Case Type, or different Issue Type under the same Case Type). A hit here means there's a real risk Fin will confuse the new value with an existing one.
4. For every genuine overlap found, note the specific colliding node and the distinguishing signal that separates them — this becomes a `Does not apply if` bullet, not a vague "may overlap with X" caveat.

If no overlaps are found, say so explicitly in the final report rather than silently omitting the `Does not apply if` section — a value with truly no boundary risk is rare enough that it's worth flagging so the user can sanity-check the search was thorough.

### Step 4 — Draft the block

Use this exact structure, matching `fin-attributes-definitions.md`'s existing style:

```
<one-sentence definition, tightened from the user's input>

**Applies if the customer:**
- <specific signal 1, generalised from the definition and example queries — not a copy-paste of the example itself>
- <specific signal 2>
- [more as needed, but prefer 2-4 tight bullets over 6+ vague ones]

**Does not apply if the customer:**
- <the specific colliding node from Step 3, and where to route instead>
- [one bullet per genuine overlap found — omit this section only if Step 3 found zero overlaps, and say so in the report]

**Example:** "<one representative customer query, verbatim from the user's input if given>"

**Likely keywords:** <5-8 comma-separated phrases customers would actually use, drawn from the definition and examples — not generic taxonomy jargon>
```

Rules:
- `Applies if` bullets describe *signals in the contact*, not restatements of the definition. "Reports a refund stuck in Pending" is a signal; "is about refund status" is a restatement — avoid the latter.
- Every `Does not apply if` bullet must name where the excluded case actually routes (a specific sibling or Case Type), never just "elsewhere."
- Only include `Example:` if the user supplied at least one query, or if you're directly quoting from the taxonomy source with attribution — never fabricate a customer quote to fill the section.
- If this is a Case Type-level block and it will have child Issue Types (existing or about to be added in the same session), do not duplicate their content into an `Includes:` list at the Case Type level — that's redundant with the child blocks and burns the character budget for no reason (this exact mistake was found and fixed in this file on 2026-07-07 — see the file's own history if unsure).

### Step 5 — Enforce the 2500-character limit

Intercom's Fin Attribute value description field has a **2500-character hard limit, including whitespace**.

1. Count the full character length of the drafted block (definition + Applies if + Does not apply if + Example + Likely keywords — everything that would be pasted into the one Attribute value field, not counting the markdown heading itself).
2. If over 2500: trim in this order — (a) tighten wording without losing distinct signals, (b) drop the `Example:` line before dropping any `Does not apply if` bullet (boundary-safety content is higher value than one illustrative quote), (c) merge near-duplicate `Applies if` bullets. Never trim by silently deleting a `Does not apply if` bullet that resolves a real overlap found in Step 3 — if it's still over budget after (a)-(c), say so in the report rather than quietly dropping disambiguation.
3. Re-count after trimming and confirm it's under 2500 before writing.

Run this check with a quick Python one-liner (`len(block_text)`) rather than eyeballing it — character counts are not reliably estimable by inspection at this length.

### Step 6 — Write to `fin-attributes-definitions.md`

- New Case Type: insert as a new `## Case Type: <name>` section, in the position confirmed in Step 2, with the standard `---` divider before/after matching surrounding sections.
- New Issue Type: insert as a new `### Issue Type: <name>` section under the correct `## Case Type:` block, after its existing sibling Issue Types.
- New Reason: insert as a new `#### Reason: <name>` section under the correct `### Issue Type:` block, after its existing sibling Reasons.
- Update (existing node): replace the full existing block in place — do not leave the old text alongside the new.
- If Step 3 found overlaps with nodes in *other* Case Types/Issue Types, add a reciprocal one-line cross-reference to those other nodes' `Does not apply if` sections too, the same way the Card issuing ↔ Technical issue and IDV ↔ Technical issue boundaries were cross-referenced on 2026-07-07. A one-directional exclusion is half-finished.

### Step 7 — Fold back into `support-taxonomy.md`

Convert the same content into `support-taxonomy.md`'s native structure — do not just paste the Fin Attributes markdown in:

- Case Type: `### <Name>` heading, followed by an italic one-paragraph definition (fold `Applies if`/`Does not apply if` prose into it), then a `**Key distinctions:**` bulleted list for anything that needs explicit disambiguation.
- Issue Type: `**<Name>** — <short description>` line.
- Reason: `- *<Name>* — IF <condition, in the same "IF...THEN select this" style as neighboring reasons> THEN select this.`

Add the same reciprocal cross-references identified in Step 6 as new `**Key distinctions:**` bullets on the colliding Case Type(s).

### Step 8 — Verify no structural regression

Run the taxonomy parser check (the same regex logic `/taxonomy-classification-qa` uses to build its valid-pairs set) before and after the edit, and confirm:
- Case type count is unchanged unless a new Case Type was intentionally added
- Issue type / reason pair and triple counts increased by exactly the number of new nodes added (0 for a pure update)

```python
import re
def count_taxonomy(path):
    with open(path) as f:
        content = f.read()
    tree = content.split("## Taxonomy Tree")[1].split("## Summary Counts")[0]
    case_type = issue_type = None
    pairs, triples = set(), set()
    for line in tree.split("\n"):
        s = line.strip()
        if m := re.match(r'^### (.+)$', s):
            case_type, issue_type = m.group(1).strip().lower(), None; continue
        if m := re.match(r'^\*\*(.+?)\*\*\s*[—-]', s):
            if case_type:
                issue_type = m.group(1).strip().lower(); pairs.add((case_type, issue_type)); continue
        if m := re.match(r'^- \*(.+?)\*', s):
            if case_type and issue_type:
                triples.add((case_type, issue_type, m.group(1).strip().lower())); continue
        if m := re.match(r'^- \*\*(.+?)\*\*$', s):
            if case_type and not issue_type:
                pairs.add((case_type, m.group(1).strip().lower()))
    return len(set(p[0] for p in pairs)), len(pairs), len(triples)
```

If the counts don't move as expected, the markdown structure was broken during the edit — fix it before reporting success.

### Step 9 — Verify the 2500-character limit across the whole file

Re-run the block-length check across the entire `fin-attributes-definitions.md` file, not just the new/edited block — an edit to a Case Type-level description can push its own block over budget even if the new child Issue Type/Reason is fine. Report any block still over 2500 chars.

```python
import re
def find_oversized_blocks(path, limit=2500):
    with open(path) as f:
        content = f.read()
    lines = content.split("\n")
    blocks, heading, level, buf = [], None, None, []
    for line in lines:
        m = re.match(r'^(#{2,4})\s+(.*)$', line)
        if m:
            if heading:
                blocks.append((level, heading, "\n".join(buf)))
            level, heading, buf = len(m.group(1)), m.group(2), []
        else:
            buf.append(line)
    if heading:
        blocks.append((level, heading, "\n".join(buf)))
    return [(l, h, len(b)) for l, h, b in blocks if len(b) > limit]
```

### Step 10 — Report to the user

```
Added/Updated: [Case Type / Issue Type / Reason] "<name>" under <parent chain>

Character count: N / 2500

Overlap check: [N overlaps found and cross-referenced | none found — see note] 
  - <colliding node> → distinguished by <signal>  (if any)

Files updated:
- fin-attributes-definitions.md (new/updated block, plus N reciprocal cross-reference(s) on other nodes)
- support-taxonomy.md (same content in native structure, plus N Key distinctions bullet(s) added)

Taxonomy parser check: case types N→N, issue-type pairs N→N, reason triples N→N (expected: +1 <level> only)
```

If anything from Steps 3, 5, or 8 surfaced a problem that wasn't fully resolved (an overlap that couldn't be cleanly distinguished, a block still over budget, or a parser count that didn't move as expected), lead the report with that — don't bury a real issue under a routine summary.
