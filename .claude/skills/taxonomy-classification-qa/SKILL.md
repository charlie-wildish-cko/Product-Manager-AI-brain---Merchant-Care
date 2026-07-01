---
name: taxonomy-classification-qa
description: QA Fin AI's contact classifications against the support taxonomy. Scores case type, issue type, and reason as a cascade (issue type only scored if case type is correct; reason only scored if issue type is correct), validates both parties' labels against the taxonomy, and identifies definition gaps and taxonomy gaps. Outputs a per-row TSV for Google Sheets plus a ranked fix hitlist (markdown) for triaging large batches. Invoke with /taxonomy-classification-qa <file-path>
tools: Read, Glob, Grep, Bash, Write, Agent
---

# Taxonomy Classification QA

QA Fin AI's contact classifications against the 3-level support taxonomy (Case Type → Issue Type → Reason). Case Type is the root branch of the taxonomy, so it is scored first and gates everything below it — a contact with the wrong Case Type cannot have a meaningful Issue Type or Reason verdict, since Fin was already on the wrong branch. Checks per contact:
1. **Fin vs agent, cascaded** — did Fin agree with the human label at each level? Case Type is always scored; Issue Type is only scored when Case Type is correct; Reason is only scored when Issue Type is correct (case_type_verdict, issue_type_verdict, reason_match, plus an overall verdict)
2. **Label validity** — did either party use a label that actually exists in the taxonomy? (fin_label_valid, agent_label_valid)
3. **Taxonomy coverage** — does the contact fit the taxonomy at all, or does it expose a gap? (taxonomy_gap_candidate)

Two outputs:
- **Per-row TSV** for Google Sheets — every contact, one row each, for spot-checking and filtering.
- **Fix hitlist (markdown)** — the per-row gap analysis clustered into the top 5-10 highest-impact patterns, ranked so you can work a backlog of 200+ rows without reading each one. This is the actionable output; the TSV is the audit trail behind it.

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

Verdicts cascade top-down through the taxonomy: **Case Type → Issue Type → Reason**. Each level is only scored if the level above it is `correct`. This reflects that Issue Type and Reason are sub-classifications within a Case Type branch — if Fin picked the wrong Case Type, its Issue Type pick was made on the wrong branch and isn't a meaningful signal about Issue Type definitions.

### Level 1 — `case_type_verdict` (always scored)

| Verdict | Condition |
|---------|-----------|
| `correct` | `fin_case_type` matches `correct_case_type` (after normalisation) |
| `wrong` | `fin_case_type` is present but doesn't match |
| `unclassified` | Fin left `fin_case_type` blank |
| `unverifiable` | `correct_case_type` is blank — cannot be scored |

Precedence: `unverifiable` > `unclassified` > `wrong` > `correct`.

### Level 2 — `issue_type_verdict` (scored only when `case_type_verdict = correct`)

| Verdict | Condition |
|---------|-----------|
| `n/a` | `case_type_verdict` is not `correct` — Issue Type is unscorable when Case Type already failed |
| `correct` | `fin_issue_type` matches `correct_issue_type` (after normalisation) |
| `wrong` | `fin_issue_type` is present but doesn't match |
| `unclassified` | Fin left `fin_issue_type` blank |
| `unverifiable` | `correct_issue_type` is blank — cannot be scored |

Precedence (when not `n/a`): `unverifiable` > `unclassified` > `wrong` > `correct`.

### Level 3 — `reason_match` (scored only when `issue_type_verdict = correct`)

`reason_match`: `yes` / `no` / `n/a`
- `n/a`: `issue_type_verdict` is not `correct` (cascade blocked above this level), OR either `fin_reason`/`correct_reason` is blank
- `yes`: `issue_type_verdict = correct` AND reasons match (after normalisation)
- `no`: `issue_type_verdict = correct` AND reasons do NOT match — flag for reason gap analysis

### Overall `verdict` (kept for backward-compatible top-line scoring)

`verdict = case_type_verdict` if `case_type_verdict != correct`, otherwise `verdict = issue_type_verdict`. In other words: the overall verdict is whichever level first fails in the cascade, or `correct` if both Case Type and Issue Type match.

Unverifiable rows (at any level) are excluded from that level's accuracy calculation. Include them in the TSV with the relevant verdict field = `unverifiable` and a note in `gap_description`.

---

## Output TSV columns

```
contact_id	contact_text_truncated	fin_case_type	fin_issue_type	fin_reason	correct_case_type	correct_issue_type	correct_reason	case_type_verdict	issue_type_verdict	verdict	reason_match	fin_label_valid	agent_label_valid	taxonomy_gap_candidate	gap_type	gap_description	recommended_fix
```

| Column | Content |
|--------|---------|
| `contact_id` | From input |
| `contact_text_truncated` | First 200 chars of contact text |
| `fin_case_type` … `correct_reason` | Pass-through from input (raw, un-normalised) |
| `case_type_verdict` | `correct` · `wrong` · `unclassified` · `unverifiable` — always scored |
| `issue_type_verdict` | `correct` · `wrong` · `unclassified` · `unverifiable` · `n/a` (n/a when `case_type_verdict` isn't `correct`) |
| `verdict` | Overall verdict: `case_type_verdict` if not `correct`, else `issue_type_verdict`. `correct` · `wrong` · `unclassified` · `unverifiable` |
| `reason_match` | `yes` · `no` · `n/a` (n/a when `issue_type_verdict` isn't `correct`, or either reason field is blank) |
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

Rows are triaged into tiers by which cascade level first failed. A row gets gap analysis from exactly one tier (whichever level failed first), plus a separate invalid-label note if applicable:

- **Tier 1 — Case Type** (`case_type_verdict` = `wrong` or `unclassified`): classification gap populated by Opus, scoped to Case Type only. Issue Type and Reason are not analysed for these rows — they're `n/a`/unscored, and any gap there would just be an artefact of the wrong branch.
- **Tier 2 — Issue Type** (`case_type_verdict=correct` AND `issue_type_verdict` = `wrong` or `unclassified`): classification gap populated by Opus, scoped to Issue Type within the (correctly identified) Case Type.
- **Tier 3 — Reason** (`case_type_verdict=correct` AND `issue_type_verdict=correct` AND `reason_match=no`): `gap_type=reason_mismatch`, reason gap populated by Opus.
- **No gap** (`case_type_verdict=correct` AND `issue_type_verdict=correct` AND `reason_match=yes`, or `reason_match=n/a` because reasons weren't populated) + both labels valid: `gap_type=none`, blank description and fix, `taxonomy_gap_candidate=no`.
- `fin_label_valid=no` or `agent_label_valid=no`: `gap_type=invalid_label` (combined with the tier's gap_type if the row also failed a cascade level), description names the invalid value and correct path.
- `unverifiable` (at whichever level `verdict` reports): `gap_type=n/a`, `gap_description` = "Human ground truth not populated in Zendesk — unable to verify Fin classification.", `recommended_fix` = "Ensure Zendesk agents classify all tickets; untagged rows cannot contribute to QA."

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

**2b — Compute verdicts (cascading)**

1. Apply the label normalisation map to all four classification fields before comparing
2. Strip and lowercase all label values (case-insensitive)
3. Assign `case_type_verdict` per the Level 1 logic above (precedence: unverifiable > unclassified > wrong > correct) — always scored
4. Assign `issue_type_verdict` per the Level 2 logic — `n/a` if `case_type_verdict != correct`, otherwise scored with the same precedence
5. Assign `reason_match` per the Level 3 logic — `n/a` if `issue_type_verdict != correct` or either reason field is blank, otherwise `yes`/`no`
6. Derive the overall `verdict`: `case_type_verdict` if not `correct`, else `issue_type_verdict`

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

Assign each row to at most one tier, by which cascade level first failed:
- **Tier 1 (case_type)**: `case_type_verdict` is `wrong` or `unclassified`
- **Tier 2 (issue_type)**: `case_type_verdict=correct` AND `issue_type_verdict` is `wrong` or `unclassified`
- **Tier 3 (reason)**: `case_type_verdict=correct` AND `issue_type_verdict=correct` AND `reason_match=no`

Separately, flag rows where `fin_label_valid=no` or `agent_label_valid=no` (invalid label — can co-occur with any tier, or occur alone if verdict is otherwise correct).

Spawn an Opus agent for the union of: all Tier 1/2/3 rows, plus any invalid-label rows not already included.

Pass to the agent:
- The full content of `support-taxonomy.md`
- All qualifying rows, each tagged with its tier (1/2/3/invalid_label_only), plus contact_id, contact_text, fin values, correct values, case_type_verdict, issue_type_verdict, reason_match, fin_label_valid, agent_label_valid
- The verdict and validity summary

Opus agent instruction:

> "You are auditing AI classification errors against a support taxonomy. Each contact is tagged with a tier — the tier tells you which taxonomy level to analyse. Do not analyse or comment on levels below the tagged tier: a Tier 1 (case_type) row failed at the root of the taxonomy, so its Issue Type and Reason fields are not meaningful signal and must not be used to justify a fix.
>
> - Tier 1 rows: diagnose the Case Type error only. Ignore fin_issue_type / correct_issue_type content when reasoning about the fix — the fix must be a Case Type definition change.
> - Tier 2 rows: diagnose the Issue Type error only, within the (correctly matched) Case Type branch.
> - Tier 3 rows: diagnose the Reason mismatch only, within the (correctly matched) Case Type and Issue Type.
> - invalid_label_only rows (no tier, or already covered above): diagnose the invalid label.
>
> For each contact, identify (1) the gap in the classifier definitions or taxonomy that caused the error and (2) a specific recommended fix.
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
> gap_description: 1–2 sentences describing what caused the error, scoped to the row's tier. For invalid_label rows: name the invalid value and the correct canonical path.
>
> recommended_fix: A specific, actionable change, scoped to the row's tier. For classifier definition gaps: name the field (include_when, exclude_when, disambiguation, scope) and target class at the tier's level (Case Type for Tier 1, Issue Type for Tier 2, Reason for Tier 3). For taxonomy gaps (missing_coverage): name the missing node and where to add it. For invalid labels: state the correct canonical label to use and whether Zendesk field config or the classifier output needs updating.
>
> Output format: one JSON object per contact, with keys: contact_id, tier, gap_type, gap_description, recommended_fix. Return a JSON array. No prose, no explanation outside the JSON."

Wait for the Opus agent to return the JSON array before proceeding.

### Step 4 — Cluster gap analysis into a fix hitlist (Opus agent)

The per-row output from Step 3 is one fix per contact — at 200+ rows this is not something a human can work through one by one. This step clusters those rows into a small number of shared root causes and ranks them by impact, so the output is a prioritized backlog rather than a list of symptoms.

Spawn a second Opus agent. Pass it:
- The full JSON array returned by Step 3 (contact_id, tier, gap_type, gap_description, recommended_fix)
- The total row count and case_type/issue_type/reason verdict breakdown from Step 2, for computing "% of batch" per cluster

Opus agent instruction:

> "You are clustering AI classification errors into a prioritized fix backlog. You've been given per-contact gap analysis (tier, gap_type, gap_description, recommended_fix) for a batch of contacts.
>
> Group contacts into clusters by shared root cause — not just by matching gap_type, but by whether the underlying definition gap is actually the same one. Two `ambiguous_boundary` rows are only the same cluster if the same two classes are being confused for the same reason.
>
> For each cluster, produce: a short cluster name, the tier (1/2/3) and gap_type, the count and list of contact_ids affected, a single merged recommended_fix that would resolve all contacts in the cluster, and 1-2 sentences on the shared pattern.
>
> Rank clusters by impact: Tier 1 (case type) clusters first — a case type fix also recovers Issue Type and Reason scoring for every contact in it, since those levels were unscored (n/a) while case type was wrong. Within a tier, rank by number of contacts affected, descending.
>
> Return the top 10 clusters, or fewer if there are fewer than 10 distinct clusters. If more than 10 distinct clusters exist, cap at 10 and separately report the count of remaining smaller clusters and total contacts they cover — do not silently drop them.
>
> Output format: a single JSON object with keys: clusters (array of {rank, tier, gap_type, cluster_name, pattern_description, recommended_fix, affected_count, affected_contact_ids}), and overflow ({cluster_count, contact_count} for clusters beyond the top 10, or null if none). No prose outside the JSON."

Wait for the Opus agent to return this JSON object before proceeding.

### Step 5 — Merge, output, and save (per-row TSV)

1. Merge gap analysis into the full row set using `contact_id` as key
2. Apply row rules from the Output TSV columns section above
3. For rows with no gap analysis entry (correct + reason_match=yes + both labels valid): set `gap_type=none`, leave description and fix blank
4. Truncate `contact_text` to first 200 chars for the `contact_text_truncated` column
5. Produce the TSV: tab-separated, replace any embedded tabs with a space
6. Save to: `04-active-work/classification-qa-<YYYY-MM-DD>.tsv`

### Step 6 — Save the fix hitlist (markdown)

Write the Step 4 output to `04-active-work/classification-qa-fixes-<YYYY-MM-DD>.md` in this format:

```
# Classification QA — Fix Hitlist — YYYY-MM-DD

Source: classification-qa-YYYY-MM-DD.tsv (N rows, N verifiable)
Ranked by impact — Tier 1 (case type) first, since a case type fix also recovers Issue Type and Reason accuracy for every affected contact. Within a tier, ranked by contacts affected.

## 1. [Tier N] Cluster name — N contacts (X% of batch)
**Gap type:** gap_type
**Pattern:** pattern_description
**Recommended fix:** recommended_fix
**Example contacts:** contact_id, contact_id, contact_id — (full text and raw labels in the TSV)

## 2. ...

---
[If overflow is non-null:] N additional smaller clusters not listed above, covering N contacts. See the TSV (gap_type, taxonomy_gap_candidate columns) for the long tail.
```

### Step 7 — Report to user

Print the following in this exact format:

```
Saved to: 04-active-work/classification-qa-YYYY-MM-DD.tsv (per-row detail)
Saved to: 04-active-work/classification-qa-fixes-YYYY-MM-DD.md (ranked fix hitlist)

=== ACCURACY SUMMARY — YYYY-MM-DD (cascade: Case Type → Issue Type → Reason) ===
Case type accuracy:     N/N = XX%   (case_type_verdict:correct ÷ case-type-verifiable)
Issue type accuracy:    N/N = XX%   (issue_type_verdict:correct ÷ rows with correct case type, excl. unverifiable)
Reason accuracy:        N/N = XX%   (reason_match:yes ÷ rows with correct case type AND issue type, both reasons populated)
Overall accuracy:       N/N = XX%   (verdict:correct ÷ verifiable)

Case type verdicts:   correct: N | wrong: N | unclassified: N | unverifiable: N (excluded)
Issue type verdicts:  correct: N | wrong: N | unclassified: N | unverifiable: N | n/a (case type already wrong): N
Reason match:         yes: N | no: N | n/a: N

Gap types:  ambiguous_boundary: N | missing_coverage: N | wrong_scope: N | reason_mismatch: N | invalid_label: N
By tier:    Tier 1 (case type): N | Tier 2 (issue type): N | Tier 3 (reason): N

=== TAXONOMY HEALTH ===
Invalid Fin labels:       N rows — labels Fin output that don't exist in the taxonomy
Invalid agent labels:     N rows — Zendesk labels that don't match the canonical taxonomy
Taxonomy gap candidates:  N contacts — may need new case type, issue type, or reason added

INVALID LABEL DETAILS (if any):
  Fin:   "[raw value]" → correct path: [Case Type / Issue Type] (N occurrences)
  Agent: "[raw value]" → correct path: [Case Type / Issue Type] (N occurrences)

TOP 5 FIXES (Tier 1 case type fixes first — highest leverage, since a case type gap suppresses issue type and reason accuracy for every affected contact. Full ranked list of up to 10 clusters in classification-qa-fixes-YYYY-MM-DD.md):
1. [Tier N] Cluster name — N contacts (X% of batch) — recommended_fix
2. ...
[If overflow: "+ N more smaller clusters covering N contacts — see the fix hitlist file."]
```

Definitions:
- **Case-type-verifiable** = total − (case_type_verdict:unverifiable)
- **Case type accuracy** = case_type_verdict:correct ÷ case-type-verifiable
- **Issue-type-eligible** = rows where `case_type_verdict=correct`, minus `issue_type_verdict:unverifiable`
- **Issue type accuracy** = issue_type_verdict:correct ÷ issue-type-eligible
- **Reason-eligible** = rows where `issue_type_verdict=correct` AND both `fin_reason` and `correct_reason` are non-blank
- **Reason accuracy** = reason_match:yes ÷ reason-eligible
- **Verifiable** (for overall accuracy) = total − (verdict:unverifiable)
- **Overall accuracy** = verdict:correct ÷ verifiable
- **Invalid label details**: group by raw value, show the closest valid taxonomy path and occurrence count
- **Top 5 fixes**: the first 5 entries from the Step 4 cluster ranking (which already covers ordering, tier weighting, and the overflow note) — the console shows 5 for a quick read, the markdown file has the full ranked list of up to 10
