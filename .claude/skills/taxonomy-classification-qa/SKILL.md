---
name: taxonomy-classification-qa
description: QA Fin AI's contact classifications against the support taxonomy. Compares Fin's assigned case type, issue type, and reason to human ground truth labels, generates a verdict per contact, validates both parties' labels against the taxonomy, and identifies definition gaps and taxonomy gaps. Output is TSV for Google Sheets. Invoke with /taxonomy-classification-qa <file-path>
tools: Read, Glob, Grep, Bash, Write, Agent
---

# Taxonomy Classification QA

QA Fin AI's contact classifications against the 3-level support taxonomy (Case Type → Issue Type → Reason). Three independent checks per contact:
1. **Fin vs agent** — did Fin agree with the human label? (verdict)
2. **Label validity** — did either party use a label that actually exists in the taxonomy? (fin_label_valid, agent_label_valid)
3. **Taxonomy coverage** — does the contact fit the taxonomy at all, or does it expose a gap? (taxonomy_gap_candidate)

Output is TSV for Google Sheets.

---

## Inputs

| Argument | Values | Notes |
|----------|--------|-------|
| `file-path` | Absolute or relative path to CSV or markdown file | Required |

Example:
- `/taxonomy-classification-qa 04-active-work/fin-qa-batch-2026-05.csv`
- `/taxonomy-classification-qa ~/Downloads/fin classification QA 18 May.md`

---

## Input file — accepted formats

Accepts **CSV** or **markdown table** (`.md`) files. Detect format by file extension.

### Canonical column names (used internally after normalisation)

| Canonical name | Required | Notes |
|----------------|----------|-------|
| `contact_id` | Required | Row identifier |
| `contact_text` | Required | Contact transcript or message body |
| `fin_case_type` | Required | Fin's assigned Case Type (blank = unclassified) |
| `fin_issue_type` | Required | Fin's assigned Issue Type (blank = unclassified) |
| `fin_reason` | Optional | Fin's assigned Reason (may be blank) |
| `correct_case_type` | Required | Human ground truth Case Type |
| `correct_issue_type` | Required | Human ground truth Issue Type |
| `correct_reason` | Optional | Human ground truth Reason |

### Column name mapping

When loading the file, apply this mapping using **contains-match** (case-insensitive, spaces/underscores interchangeable): if the canonical key appears anywhere within the column name, map it. Exact match takes priority; contains-match is the fallback.

| Canonical key (match anywhere in column name) | Canonical name |
|---|---|
| `Conversation ID` | `contact_id` |
| `Message Body (Plain)` | `contact_text` |
| `Case Type (Fin)` | `fin_case_type` |
| `Issue Type (Fin)` | `fin_issue_type` |
| `Reason (Fin)` | `fin_reason` |
| `Case Type (Zendesk)` | `correct_case_type` |
| `Issue Type (Zendesk)` | `correct_issue_type` |
| `Reason (Zendesk)` | `correct_reason` |

Any column not matched is carried through unchanged (e.g. `Ticket ID`, `Zendesk Ticket Channel`).

### Markdown table parsing

If the file extension is `.md`:
- Split lines on `|`, strip whitespace from each cell
- Skip the separator row (contains only `-`, `:`, `|`)
- Treat the first non-separator row as the header
- Parse all remaining rows as data rows

---

## Source files

| Purpose | File |
|---------|------|
| Taxonomy + classifier definitions | `01-knowledge-base/processes/support-taxonomy.md` |

---

## Label normalisation map

Before comparing any label, apply this canonical mapping (case-insensitive) to both Fin and ground truth values. This prevents false `wrong` verdicts caused by label formatting variants rather than genuine classification errors.

| Variant(s) | Canonical label |
|---|---|
| `Disputes/Chargebacks`, `Disputes / Chargebacks`, `Chargebacks` | `Disputes` |
| `Account management and access`, `Account Management & Access` | `Account management and access` |
| `Accepting payments`, `Payments (in)`, `PAYMENTS (IN)` | `Accepting payments` |
| `Compliance and audit`, `Compliance & Audit` | `Compliance and audit` |
| `Card issuing`, `Issuing` | `Card issuing` |
| `Non-merchant requests`, `Non Merchant Requests` | `Non-merchant requests` |
| `Integration methods`, `Integration Methods` | `Integration methods` |
| `Sub-Merchant onboarding`, `Sub-merchant onboarding` | `Sub-Merchant onboarding` |

Apply this map before the case-insensitive string comparison in Step 2. If a value is not in the map, use it as-is (lowercased).

---

## Verdict logic

| Verdict | Condition |
|---------|-----------|
| `correct` | `fin_case_type` + `fin_issue_type` match ground truth (after normalisation) |
| `wrong` | Fin assigned values that don't match ground truth |
| `unclassified` | Fin left `fin_case_type` or `fin_issue_type` blank |
| `unverifiable` | Human ground truth (`correct_case_type` AND `correct_issue_type`) is blank — Fin may or may not be right, but cannot be scored |

Precedence: `unverifiable` > `unclassified` > `wrong` > `correct`.

Unverifiable rows are excluded from all accuracy calculations. Include them in the TSV with verdict = `unverifiable` and a note in `gap_description`.

`reason_match`: `yes` / `no` / `n/a`
- `yes`: verdict = correct AND reasons match (after normalisation)
- `no`: verdict = correct AND reasons do NOT match — flag for reason gap analysis
- `n/a`: verdict is wrong / unclassified / unverifiable, or either reason field is blank

---

## Output TSV columns

```
contact_id	contact_text_truncated	fin_case_type	fin_issue_type	fin_reason	correct_case_type	correct_issue_type	correct_reason	verdict	reason_match	fin_label_valid	agent_label_valid	taxonomy_gap_candidate	gap_type	gap_description	recommended_fix
```

| Column | Content |
|--------|---------|
| `contact_id` | From input |
| `contact_text_truncated` | First 200 chars of contact text |
| `fin_case_type` … `correct_reason` | Pass-through from input (raw, un-normalised) |
| `verdict` | `correct` · `wrong` · `unclassified` · `unverifiable` |
| `reason_match` | `yes` · `no` · `n/a` |
| `fin_label_valid` | `yes` if Fin's (case_type, issue_type) pair is a valid path in the taxonomy; `no` if either level doesn't exist; `n/a` if Fin left both blank |
| `agent_label_valid` | `yes` if the agent's (case_type, issue_type) pair is a valid path in the taxonomy; `no` if either level doesn't exist; `n/a` if agent left both blank |
| `taxonomy_gap_candidate` | `yes` if the contact likely exposes a gap in the taxonomy itself (see rules below); `no` otherwise |
| `gap_type` | `ambiguous_boundary` · `missing_coverage` · `wrong_scope` · `reason_mismatch` · `invalid_label` · `none` · `n/a` |
| `gap_description` | 1–2 sentences: what signal led Fin astray, or what is absent from the definitions |
| `recommended_fix` | Specific, actionable change — for classifier definition gaps: name the field and class; for taxonomy gaps: name the missing node and where to add it; for invalid labels: the correct canonical label to use |

### Label validity rules

Extract the full set of valid (case_type, issue_type) pairs from `support-taxonomy.md` as a Python set. Use normalised lowercase for comparison.

`fin_label_valid`:
- `yes` — Fin's normalised (case_type, issue_type) pair exists in the valid-pairs set
- `no` — one or both levels do not exist in the taxonomy (even if Fin's intent is clear)
- `n/a` — Fin left case_type AND issue_type both blank (unclassified rows)

`agent_label_valid`:
- `yes` — agent's normalised (case_type, issue_type) pair exists in the valid-pairs set
- `no` — one or both levels do not exist in the taxonomy
- `n/a` — agent left case_type AND issue_type both blank (unverifiable rows)

When `fin_label_valid=no` or `agent_label_valid=no`, set `gap_type=invalid_label` and populate `gap_description` with the invalid value and the closest valid taxonomy path. Do not change the verdict — label validity is independent of the Fin-vs-agent comparison.

If a row already has a gap_type from the Fin-vs-agent analysis (ambiguous_boundary, missing_coverage, etc.) AND also has an invalid label, report both: set gap_type to the Fin-vs-agent type and note the invalid label issue in gap_description.

### Taxonomy gap candidate rules

Set `taxonomy_gap_candidate=yes` when ANY of the following are true:
- `fin_label_valid=no` AND `agent_label_valid=no` — neither party could find a valid taxonomy path
- `gap_type=missing_coverage` — Opus identified the contact as genuinely uncovered by the taxonomy
- `agent_label_valid=no` AND verdict=`correct` — agent used an invalid label and Fin matched it (both wrong against the taxonomy, but agreeing with each other)

`taxonomy_gap_candidate=no` in all other cases.

### Row rules for gap columns

- `correct` + `reason_match=yes` + both labels valid: `gap_type=none`, blank description and fix, `taxonomy_gap_candidate=no`
- `correct` + `reason_match=no`: `gap_type=reason_mismatch`, reason gap populated by Opus
- `wrong` / `unclassified`: classification gap populated by Opus
- `fin_label_valid=no` or `agent_label_valid=no`: `gap_type=invalid_label` (or combined with classification gap type), description names the invalid value and correct path
- `unverifiable`: `gap_type=n/a`, `gap_description` = "Human ground truth not populated in Zendesk — unable to verify Fin classification.", `recommended_fix` = "Ensure Zendesk agents classify all tickets; untagged rows cannot contribute to QA."

---

## Execution

### Step 1 — Read inputs

Read `01-knowledge-base/processes/support-taxonomy.md`.

Read the input file. Use a Python script to load it:
- Detect format by file extension: `.md` = markdown table, anything else = CSV
- For markdown: split on `|`, strip cells, skip separator rows, use first row as header
- Apply the column name mapping using contains-match (see above)
- Fall back: map the first column to `contact_id` if no match is found
- Print: row count and column names found (after mapping)

### Step 2 — Compute verdicts and label validity (Python)

Run a Python script that does all of the following:

**2a — Build the valid-pairs set from the taxonomy**

Parse `support-taxonomy.md` to extract every valid (case_type, issue_type) combination. Store as a set of normalised lowercase tuples. Also extract every valid (case_type, issue_type, reason) triple for reason validation. Print the count of valid pairs found.

Example valid pairs (normalised): `{("accepting payments", "transaction status"), ("funds and fees", "settlements"), ...}`

**2b — Compute verdicts**

1. Apply the label normalisation map to all four classification fields before comparing
2. Strip and lowercase all label values (case-insensitive)
3. Assign `verdict` per the logic above (precedence: unverifiable > unclassified > wrong > correct)
4. Assign `reason_match` for correct rows

**2c — Compute label validity**

For each row, check Fin's (case_type, issue_type) pair and the agent's (case_type, issue_type) pair against the valid-pairs set:
- Apply the same normalisation map before checking
- Set `fin_label_valid` and `agent_label_valid` per the rules above
- Track which specific invalid labels appear (raw value → closest valid path) for the summary report

**2d — Compute taxonomy gap candidates**

Apply the taxonomy_gap_candidate rules above. Set `yes` or `no` per row.

**2e — Print summary counts**

Print: total rows, verdict breakdown, invalid label counts (Fin and agent separately), taxonomy gap candidate count.

### Step 3 — Gap analysis (Opus agent)

Spawn an Opus agent for rows where:
- verdict is `wrong` or `unclassified`, OR
- verdict is `correct` with `reason_match=no`, OR
- `fin_label_valid=no` or `agent_label_valid=no` (even if verdict is correct)

Pass to the agent:
- The full content of `support-taxonomy.md`
- All qualifying rows (contact_id, contact_text, fin values, correct values, verdict, reason_match, fin_label_valid, agent_label_valid)
- The verdict and validity summary

Opus agent instruction:

> "You are auditing AI classification errors against a support taxonomy. For each contact, identify (1) the gap in the classifier definitions or taxonomy that caused the error and (2) a specific recommended fix.
>
> gap_type must be exactly one of:
> - ambiguous_boundary: the contact could fit multiple classes and the definitions don't clearly disambiguate
> - missing_coverage: no existing definition covers this contact type
> - wrong_scope: the definition's scope is too broad and incorrectly captures this contact
> - reason_mismatch: case type and issue type are correct but the reason label is wrong or inconsistently defined
> - invalid_label: Fin or the agent used a label that does not exist in the canonical taxonomy (wrong spelling, deprecated name, or non-existent path)
>
> If a row has both a classification error AND an invalid label, use the classification gap_type and mention the invalid label in gap_description.
>
> gap_description: 1–2 sentences describing what caused the error. For invalid_label rows: name the invalid value and the correct canonical path.
>
> recommended_fix: A specific, actionable change. For classifier definition gaps: name the field (include_when, exclude_when, disambiguation, scope) and target class. For taxonomy gaps (missing_coverage): name the missing node and where to add it. For invalid labels: state the correct canonical label to use and whether Zendesk field config or the classifier output needs updating.
>
> Output format: one JSON object per contact, with keys: contact_id, gap_type, gap_description, recommended_fix. Return a JSON array. No prose, no explanation outside the JSON."

Wait for the Opus agent to return the JSON array before proceeding.

### Step 4 — Merge, output, and save

1. Merge gap analysis into the full row set using `contact_id` as key
2. Apply row rules from the Output TSV columns section above
3. For rows with no gap analysis entry (correct + reason_match=yes + both labels valid): set `gap_type=none`, leave description and fix blank
4. Truncate `contact_text` to first 200 chars for the `contact_text_truncated` column
5. Produce the TSV: tab-separated, replace any embedded tabs with a space
6. Save to: `04-active-work/classification-qa-<YYYY-MM-DD>.tsv`

### Step 5 — Report to user

Print the following in this exact format:

```
Saved to: 04-active-work/classification-qa-YYYY-MM-DD.tsv

=== ACCURACY SUMMARY — YYYY-MM-DD (n=N verifiable) ===
Overall accuracy:       N/N = XX%   (correct ÷ verifiable)
Case type accuracy:     N/N = XX%   (rows where L1 matches ÷ verifiable)
Issue type accuracy:    N/N = XX%   (rows where L1+L2 both match ÷ verifiable)
Reason accuracy:        N/N = XX%   (reason_match:yes ÷ correct rows with both reasons populated)

Verdicts:  correct: N | wrong: N | unclassified: N | unverifiable: N (excluded from scores)
Gap types: ambiguous_boundary: N | missing_coverage: N | wrong_scope: N | reason_mismatch: N | invalid_label: N

=== TAXONOMY HEALTH ===
Invalid Fin labels:       N rows — labels Fin output that don't exist in the taxonomy
Invalid agent labels:     N rows — Zendesk labels that don't match the canonical taxonomy
Taxonomy gap candidates:  N contacts — may need new case type, issue type, or reason added

INVALID LABEL DETAILS (if any):
  Fin:   "[raw value]" → correct path: [Case Type / Issue Type] (N occurrences)
  Agent: "[raw value]" → correct path: [Case Type / Issue Type] (N occurrences)

TOP FIXES (by frequency):
1. [gap_type] — [one-line description of the pattern, N occurrences]
2. ...
```

Definitions:
- **Verifiable** = total − unverifiable
- **Case type accuracy** = rows where `normalize(fin_case_type) == normalize(correct_case_type)` ÷ verifiable
- **Issue type accuracy** = rows where both L1 and L2 match ÷ verifiable (same as overall accuracy)
- **Reason accuracy** = reason_match:yes ÷ (correct rows where both `fin_reason` and `correct_reason` are non-blank)
- **Invalid label details**: group by raw value, show the closest valid taxonomy path and occurrence count
- **Top fixes**: synthesise the gap analysis into the 3–5 most frequent patterns; name the definition change needed, not just the symptom
