---
name: taxonomy-classification-qa
description: QA Fin AI's contact classifications against the support taxonomy. Pulls the current QA batch directly from Looker Look 18808 by default (no export step needed) — or accepts a CSV/markdown file if given one. Runs incrementally — appends to the same persistent log files every time rather than creating a new dated file per run, and skips any ticket already reviewed in a prior run. Scores case type, issue type, and reason as a cascade (issue type only scored if case type is correct; reason only scored if issue type is correct), validates both parties' labels against the taxonomy, adjudicates genuine Fin-vs-agent mismatches instead of assuming the Zendesk label is correct, and identifies definition gaps and taxonomy gaps. Outputs a cumulative per-row TSV for Google Sheets plus a ranked fix hitlist (markdown) for triaging large batches. Invoke with /taxonomy-classification-qa [file-path | look:<id>] — defaults to look:18808 if no argument given.
tools: Read, Glob, Grep, Bash, Write, Agent, mcp__looker-toolbox__run_look
---

# Taxonomy Classification QA

QA Fin AI's contact classifications against the 3-level support taxonomy (Case Type → Issue Type → Reason). Case Type is the root branch of the taxonomy, so it is scored first and gates everything below it — a contact with the wrong Case Type cannot have a meaningful Issue Type or Reason verdict, since Fin was already on the wrong branch. Checks per contact:
1. **Fin vs agent, cascaded** — did Fin agree with the human label at each level? Case Type is always scored; Issue Type is only scored when Case Type is correct; Reason is only scored when Issue Type is correct (case_type_verdict, issue_type_verdict, reason_match, plus an overall verdict)
2. **Label validity** — did either party use a label that actually exists in the taxonomy? (fin_label_valid, agent_label_valid)
3. **Adjudication** — when Fin and the agent disagree using two otherwise-valid labels, which one (if either) was actually right for this contact? The Zendesk `correct_*` fields are the human agent's pick, not verified ground truth — a disagreement is not automatically a Fin error (see "Adjudication" below).
4. **Taxonomy coverage** — does the contact fit the taxonomy at all, or does it expose a gap? (taxonomy_gap_candidate)

**Fin is classifying against `fin-attributes-definitions.md`, not `support-taxonomy.md`.** The taxonomy doc is the internal reference for what the tree *should* be; the Intercom Attribute value descriptions in `fin-attributes-definitions.md` are what actually drives Fin's output. Gap diagnosis (Step 3) treats the Attributes file as the primary reference — the taxonomy doc is secondary, used for tree structure and boundary context.

Two outputs, both **persistent and cumulative** — the same two files are appended to on every run, not recreated per run:
- **Per-row TSV** for Google Sheets — every contact ever reviewed, one row each, tagged with the `run_date` it was reviewed on, for spot-checking and filtering.
- **Fix hitlist (markdown)** — a running log of dated sections, each holding that run's cluster analysis for the top 5-10 highest-impact patterns found in the rows new to that run. This is the actionable output; the TSV is the audit trail behind it.

**Incremental behaviour**: each run only analyses tickets not already present in the log from a prior run (see "Incremental runs & dedup" below). This means re-running the skill regularly (e.g. weekly, as Look 18808's batch rolls over) never re-scores or re-clusters the same ticket twice.

---

## Inputs

| Argument | Values | Notes |
|----------|--------|-------|
| *(none)* | — | Defaults to `look:18808` — pulls the current QA batch straight from Looker |
| `look:<id>` | Looker Look ID | Pulls directly via `mcp__looker-toolbox__run_look`, no export step |
| `file-path` | Absolute or relative path to CSV or markdown file | Use when someone hands you an export instead of a live Look |

Example:
- `/taxonomy-classification-qa` (defaults to Look 18808)
- `/taxonomy-classification-qa look:19042`
- `/taxonomy-classification-qa 04-active-work/fin-qa-batch-2026-05.csv`
- `/taxonomy-classification-qa ~/Downloads/fin classification QA 18 May.md`

---

## Canonical fields (used internally after normalisation, regardless of source)

| Canonical name | Required | Notes |
|----------------|----------|-------|
| `contact_id` | Required | Row identifier |
| `ticket_id` | Optional | Zendesk ticket ID — used as the dedup key across runs when present (see "Incremental runs & dedup"); falls back to `contact_id` if absent |
| `contact_text` | Required | Contact transcript or message body |
| `fin_case_type` | Required | Fin's assigned Case Type (blank = unclassified) |
| `fin_issue_type` | Required | Fin's assigned Issue Type (blank = unclassified) |
| `fin_reason` | Optional | Fin's assigned Reason (may be blank) |
| `correct_case_type` | Required | Zendesk agent's assigned Case Type — the human's pick, not verified ground truth. Field name kept for backward compatibility with existing logs. |
| `correct_issue_type` | Required | Zendesk agent's assigned Issue Type — same caveat |
| `correct_reason` | Optional | Zendesk agent's assigned Reason — same caveat |

---

## Incremental runs & dedup

The skill maintains two persistent files across runs (see "Output files" below) instead of writing a new dated file per invocation. Every run:

1. Fetches the current source batch (Look or file) in full, same as before.
2. Loads the existing `04-active-work/classification-qa-log.tsv` if it exists, and builds a set of already-reviewed keys from its `ticket_id` column (falling back to `contact_id` for any historical rows that predate the `ticket_id` column).
3. Filters the freshly-fetched batch down to rows whose dedup key (`ticket_id`, or `contact_id` if `ticket_id` is blank) is **not** already in that set.
4. Runs Steps 2-6 only on this new subset. Already-reviewed tickets are never re-scored, re-sent to the Opus gap-analysis agent, or re-counted in this run's cluster stats — this keeps repeat runs cheap and keeps the log free of duplicate rows.
5. If a Look batch happens to include a ticket that changed classification since it was last reviewed (e.g. a Zendesk agent re-tagged it), that ticket is still skipped — the dedup key match is on identity, not on content. If the user wants a re-review of specific tickets, they should say so explicitly rather than relying on a normal run to catch it.

If zero new rows remain after filtering, skip Steps 2-6 entirely and report: "N rows fetched, all N already reviewed. Nothing new to QA this run."

---

## Source: Looker Look (default)

Look 18808 is a live Fin-vs-Zendesk classification comparison — no CSV export needed. Fetch it directly and work from the JSON rows in memory; do not write an intermediate CSV to disk.

### Fetch procedure

1. Call `mcp__looker-toolbox__run_look` with `look_id` and an explicit `limit` of at least **1000**. Always pass this explicitly — the tool's own schema default (500) can silently truncate a saved Look's row limit below its true current size, and this batch's size **changes week to week** as the underlying QA sample rolls over. Passing a generous explicit limit ensures the full current batch comes back rather than a stale or arbitrary cutoff.
2. The result is large (typically 200K+ characters) and will be saved to a file rather than returned inline — expect a message like "result exceeds maximum allowed tokens... saved to [path]". Do not try to read that file directly with `Read`; it's a JSON array of `{type, text}` objects where each `text` is itself a JSON string.
3. Extract rows with `jq -r '.[].text' <file> > rows.jsonl`, giving one JSON object per line.
4. If the returned row count exactly equals the limit you passed, the batch may still be truncated — retry with a higher limit (e.g. 5000) and warn the user.
5. Print the row count fetched before proceeding.

### Field mapping (Looker column name → canonical name)

| Looker field | Canonical name |
|---|---|
| `fct_support_contact.conversation_id` | `contact_id` |
| `fct_support_contact_thread.plain_body` | `contact_text` |
| `fct_support_contact.fin_case_type` | `fin_case_type` |
| `fct_support_contact.fin_issue_type` | `fin_issue_type` |
| `fct_support_contact.fin_reason` | `fin_reason` |
| `fct_support_contact.zendesk_case_type` | `correct_case_type` |
| `fct_support_contact.zendesk_issue_type` | `correct_issue_type` |
| `fct_support_contact.zendesk_reason` | `correct_reason` |
| `fct_support_contact.ticket_id` | `ticket_id` |

Carry through unchanged for context (not scored, but useful in the TSV or gap analysis): `fct_support_contact.zendesk_company_tier`, `fct_support_contact.zendesk_ticket_channel`, `fct_support_contact.zendesk_ticket_sub_channel`.

Treat `null` values as blank (equivalent to an empty string) for all verdict logic.

### Thread rows

The Look includes `fct_support_contact_thread.message_order`. If a conversation has multiple rows (multiple thread messages), keep only `message_order = 1` (the initial contact) as `contact_text` — QA is scored at the contact level, not the thread-message level. Deduplicate on `contact_id` after filtering.

---

## Source: file (CSV or markdown)

Accepts **CSV** or **markdown table** (`.md`) files, for when someone hands you an export instead of pulling live. Detect format by file extension.

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
| `Ticket ID` | `ticket_id` |

Any other column not matched is carried through unchanged (e.g. `Zendesk Ticket Channel`).

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
| Taxonomy tree (secondary reference — structure, boundaries) | `01-knowledge-base/processes/support-taxonomy.md` |
| Fin Attributes (primary reference — what actually drives Fin's classification) | `01-knowledge-base/processes/fin-attributes-definitions.md` |

---

## Fin Attributes reference

Fin's classification behaviour is configured via **Fin Attributes** (Intercom) — the actual live text is `01-knowledge-base/processes/fin-attributes-definitions.md`, not `support-taxonomy.md`. The taxonomy doc is our internal reference for what the correct tree *should* be; `fin-attributes-definitions.md` is what Fin is actually reading when it classifies. Gap diagnosis (Step 3) must treat `fin-attributes-definitions.md` as the primary reference for "why did Fin pick this" — reading `support-taxonomy.md` alone can misdiagnose a gap that the Attributes file already covers correctly, or miss one that the taxonomy doc's prose doesn't surface. The actual fix for most classifier errors is a change to an Attribute value's description in that file. Every `recommended_fix` this skill outputs for a classifier-definition gap (not a pure taxonomy-tree gap) must be written as a ready-to-paste Attribute value update in this format, per Intercom's own best practice:

```
<Attribute value name>
<One-sentence description of what this value covers>

Applies if the customer:
- <specific signal 1>
- <specific signal 2>

Does not apply if the customer:
- <closely related case that should route elsewhere, and where>

Likely keywords: <comma-separated phrases customers actually use>
```

Key implications for gap analysis and recommended fixes:
- **Fin abstains (leaves a field blank) when attribute value descriptions are underspecified, overlapping, or there's no safe "Other/Uncategorized" catch-all** — not because of a confidence-threshold setting. When a row shows Fin leaving a field blank despite the level above being correctly classified and a valid answer existing in the taxonomy, the fix is a better/more complete Attribute description (or adding a documented default / "Other" value), never "lower Fin's confidence" or "require non-null output."
- **Abstention is a distinct defect from a wrong or invalid label.** A row where Fin left a field blank is not the same defect as a row where Fin confidently picked a label that doesn't exist or is a genuine mismatch — use `gap_type=fin_abstention` for the former (see gap_type list below) and keep `invalid_label` / `ambiguous_boundary` / `wrong_scope` for the latter.
- Genuine ambiguous-boundary or missing-coverage fixes should still be phrased as an Attribute value update (Applies if / Does not apply if / Likely keywords) at the specific level that failed (Case Type, Issue Type, or Reason), not as vague prose like "add a disambiguation note."

---

## Adjudication

The Zendesk `correct_*` fields are the human agent's classification pick, not verified ground truth. Treating every Fin-vs-agent mismatch as a Fin error is wrong: the agent can just as easily have mistagged a ticket using a label that's perfectly valid in the taxonomy but simply the wrong one for that contact. Without adjudication, this skill would generate Fin Attribute "fixes" for cases where Fin was actually right and the human wasn't — a real defect found in earlier runs.

**Adjudication is only needed for genuinely ambiguous disagreements — most mismatches don't require it:**
- If either party's label is *invalid* (`fin_label_valid=no` or `agent_label_valid=no`), don't adjudicate — that party is deterministically wrong (the label doesn't exist in the taxonomy at all). Handled by the existing `invalid_label` path.
- If Fin abstained (`case_type_verdict=unclassified`, or `issue_type_verdict=unclassified` with Case Type correct, or `fin_reason` blank with `correct_reason` populated), don't adjudicate — Fin gave no answer to compare, so there's nothing to weigh against the agent's pick. Handled by the existing `fin_abstention` path.
- Adjudicate **only** rows where both Fin and the agent used a fully valid, populated (case_type, issue_type) pair that disagrees at the first-failing cascade level — i.e. `fin_label_valid=yes` AND `agent_label_valid=yes` AND (`case_type_verdict=wrong` OR (`case_type_verdict=correct` AND `issue_type_verdict=wrong`) OR (`case_type_verdict=correct` AND `issue_type_verdict=correct` AND `reason_match=no`)). This is the only case where "who's actually right" is a real open question — both parties named something real, and they disagree.

For each qualifying row, a default-model agent (see Step 2.5) reads `contact_text` against the relevant excerpt of `fin-attributes-definitions.md` and returns one `adjudication_verdict`:

| Verdict | Meaning | Consequence |
|---|---|---|
| `fin_correct` | Fin's label is the right one for this contact; the agent mistagged it | `gap_type=agent_mistag`. No Fin Attribute change — skip Step 3's Opus diagnosis entirely and write a templated fix (see Row rules below). |
| `agent_correct` | The agent's label is the right one; Fin genuinely erred | Proceed to Step 3 (Opus) for full diagnosis — this is a real classifier-definition gap. |
| `both_wrong` | Neither label is the right one for this contact | Proceed to Step 3 (Opus) — likely `missing_coverage` or a definition that needs rescoping. |
| `ambiguous` | The contact genuinely could support either label; no clean right answer | Proceed to Step 3 (Opus) — likely `ambiguous_boundary`. |

**New gap type: `agent_mistag`.** Distinct from `invalid_label` (agent used a non-existent value) — here the agent's value exists in the taxonomy but was the wrong pick for this specific contact. Always `taxonomy_gap_candidate=no` (same reasoning as `fin_abstention`: a valid answer existed, an assessable error was made by the human side, not the taxonomy). Owner: Zendesk agent QA/coaching, not Fin Attributes and not the taxonomy doc.

**Reliability check**: adjudication is itself a judgment call by a smaller model and can be wrong. Step 4's clustering pass checks for a warning sign — many `agent_mistag` verdicts clustering around the same Fin-side label — and flags it rather than accepting it at face value (see Step 4).

---

## Label normalisation map

Before comparing any label, apply this canonical mapping (case-insensitive) to both Fin and agent values. This prevents false `wrong` verdicts caused by label formatting variants rather than genuine classification errors.

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

**These verdicts measure Fin-vs-agent agreement, not verified accuracy.** `correct` means "Fin matched the Zendesk label," not "Fin was right" — the Zendesk label is the agent's pick, not ground truth. For rows where the two disagree using otherwise-valid labels, the Adjudication section above determines which party (if either) was actually correct before any fix gets written; don't read `wrong` as "Fin's fault" on its own.

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

**Abstention blind spot**: `reason_match=n/a` because `fin_reason` is blank looks identical, in the accuracy math, to a row where `correct_reason` is also blank (nothing to check against) — but these are not the same signal. If `issue_type_verdict=correct` AND `fin_reason` is blank AND `correct_reason` is populated, Fin was on the exact right branch and simply stopped short of committing to a Reason. This is a real defect (Fin abstention) and must be surfaced in gap analysis (see Step 3's "reason abstention" candidate) even though `reason_match` itself stays `n/a` for accuracy-math purposes. Do not let this case silently fall into `gap_type=none`.

### Overall `verdict` (kept for backward-compatible top-line scoring)

`verdict = case_type_verdict` if `case_type_verdict != correct`, otherwise `verdict = issue_type_verdict`. In other words: the overall verdict is whichever level first fails in the cascade, or `correct` if both Case Type and Issue Type match.

Unverifiable rows (at any level) are excluded from that level's accuracy calculation. Include them in the TSV with the relevant verdict field = `unverifiable` and a note in `gap_description`.

---

## Output TSV columns

```
run_date	contact_id	ticket_id	contact_text_truncated	fin_case_type	fin_issue_type	fin_reason	correct_case_type	correct_issue_type	correct_reason	case_type_verdict	issue_type_verdict	verdict	reason_match	fin_label_valid	agent_label_valid	adjudication_verdict	taxonomy_gap_candidate	gap_type	gap_description	recommended_fix
```

| Column | Content |
|--------|---------|
| `run_date` | The date (YYYY-MM-DD) this row was reviewed — the run that first processed it, never changed on later runs |
| `contact_id` | From input |
| `ticket_id` | From input, or blank if the source had none. This plus `contact_id` form the dedup key for future runs. |
| `contact_text_truncated` | First 200 chars of contact text |
| `fin_case_type` … `correct_reason` | Pass-through from input (raw, un-normalised) |
| `case_type_verdict` | `correct` · `wrong` · `unclassified` · `unverifiable` — always scored |
| `issue_type_verdict` | `correct` · `wrong` · `unclassified` · `unverifiable` · `n/a` (n/a when `case_type_verdict` isn't `correct`) |
| `verdict` | Overall verdict: `case_type_verdict` if not `correct`, else `issue_type_verdict`. `correct` · `wrong` · `unclassified` · `unverifiable` |
| `reason_match` | `yes` · `no` · `n/a` (n/a when `issue_type_verdict` isn't `correct`, or either reason field is blank) |
| `fin_label_valid` | `yes` if Fin's (case_type, issue_type) pair is fully populated and a valid path in the taxonomy; `no` only if both levels are non-blank but the pair doesn't exist (a genuinely wrong label); `n/a` if either field is blank (abstention — see Label validity rules) |
| `agent_label_valid` | `yes` if the agent's (case_type, issue_type) pair is fully populated and a valid path in the taxonomy; `no` only if both levels are non-blank but the pair doesn't exist; `n/a` if either field is blank |
| `adjudication_verdict` | `fin_correct` · `agent_correct` · `both_wrong` · `ambiguous` · `n/a` — only populated for rows that passed the adjudication gate (see "Adjudication" above); `n/a` for abstentions, invalid labels, and rows where both parties already agreed |
| `taxonomy_gap_candidate` | `yes` if the contact likely exposes a gap in the taxonomy itself (see rules below); `no` otherwise |
| `gap_type` | `ambiguous_boundary` · `missing_coverage` · `wrong_scope` · `reason_mismatch` · `invalid_label` · `fin_abstention` · `agent_mistag` · `none` · `n/a` |
| `gap_description` | 1–2 sentences: what signal led Fin astray, or what is absent from the definitions. For `agent_mistag`: the adjudication agent's one-line rationale for why Fin's label was actually correct. |
| `recommended_fix` | For `ambiguous_boundary` / `wrong_scope` / `missing_coverage` / `invalid_label`: a ready-to-paste Fin Attribute value update (Applies if / Does not apply if / Likely keywords — see "Fin Attributes reference" above), naming the exact level (Case Type/Issue Type/Reason). For `fin_abstention`: point at strengthening that Attribute value's description or adding a safe default/"Other" value — never "lower confidence" or "require non-null output," and never a `support-taxonomy.md` edit. For `reason_mismatch`: the Reason-level Attribute update. For `agent_mistag`: a one-line note that Fin's label was correct and the Zendesk tag should be corrected — flag for agent QA/coaching, never a Fin Attribute or taxonomy edit. |

### Label validity rules

Extract the full set of valid (case_type, issue_type) pairs from `support-taxonomy.md` as a Python set. Use normalised lowercase for comparison.

**Important distinction**: a blank field is not the same thing as an invalid label. Leaving a field blank is Fin (or the agent) declining to classify — that's abstention. Populating a field with a value that doesn't exist in the taxonomy is a genuinely wrong label. Conflating the two (treating "blank issue_type" as "invalid label") was a bug found in production use — it misdirected fix recommendations toward taxonomy/definition edits when the real fix was a Fin Attributes completion problem. The rules below fix this: `no` only fires when a non-blank value was given that doesn't exist in the taxonomy; any blank field (whole pair, or just one level) is `n/a`.

`fin_label_valid`:
- `yes` — Fin's normalised (case_type, issue_type) pair is fully populated (both non-blank) and exists in the valid-pairs set
- `no` — both case_type and issue_type are non-blank, but the pair does not exist in the taxonomy (a genuinely wrong/non-canonical label was used — e.g. a non-existent Case Type, or an Issue Type that doesn't belong under that Case Type)
- `n/a` — Fin left case_type blank, OR left issue_type blank while case_type is populated (incomplete classification / abstention, not an invalid label call)

`agent_label_valid`:
- `yes` — agent's normalised (case_type, issue_type) pair is fully populated and exists in the valid-pairs set
- `no` — both levels are non-blank, but the pair does not exist in the taxonomy
- `n/a` — agent left case_type blank, OR left issue_type blank while case_type is populated

When `fin_label_valid=no` or `agent_label_valid=no`, set `gap_type=invalid_label` and populate `gap_description` with the invalid value and the closest valid taxonomy path. Do not change the verdict — label validity is independent of the Fin-vs-agent comparison. When a field is blank (fin_label_valid or agent_label_valid = `n/a`) and the level above was correctly classified with a valid answer existing on the other side, that is a `fin_abstention` (or, for the agent's own blank field, a Zendesk-tagging gap — see Row rules below), not `invalid_label`.

If a row already has a gap_type from the Fin-vs-agent analysis (ambiguous_boundary, missing_coverage, etc.) AND also has an invalid label, report both: set gap_type to the Fin-vs-agent type and note the invalid label issue in gap_description.

### Taxonomy gap candidate rules

Set `taxonomy_gap_candidate=yes` when ANY of the following are true:
- `fin_label_valid=no` AND `agent_label_valid=no` — neither party could find a valid taxonomy path
- `gap_type=missing_coverage` — Opus identified the contact as genuinely uncovered by the taxonomy
- `agent_label_valid=no` AND verdict=`correct` — agent used an invalid label and Fin matched it (both wrong against the taxonomy, but agreeing with each other)

`taxonomy_gap_candidate=no` in all other cases. **`gap_type=fin_abstention` and `gap_type=agent_mistag` are always `taxonomy_gap_candidate=no`** — abstention means a valid answer exists and Fin failed to commit to it, and a mistag means a valid answer exists and the agent picked the wrong one; neither is evidence that the taxonomy itself is missing something.

### Row rules for gap columns

Rows are triaged into tiers by which cascade level first failed, and — within Tier 1/2 — by whether Fin left the field blank (abstention) or populated it with a wrong/non-existent value. For Tier 1/2-wrong and Tier 3-mismatch rows where **both** labels are valid, the adjudication gate applies first (see "Adjudication" above) — it decides whether the row is a genuine Fin gap or an agent mistag before any Opus diagnosis runs. A row gets gap analysis from exactly one tier, plus a separate note if the *agent's* label was also invalid:

- **Tier 1 — Case Type, wrong, both labels valid**: run adjudication first. If `adjudication_verdict=fin_correct`: `gap_type=agent_mistag`, no Opus, templated fix (see below) — skip straight to Step 5. If `adjudication_verdict=agent_correct` / `both_wrong` / `ambiguous`: classification gap populated by Opus, scoped to Case Type only — `gap_type` is `ambiguous_boundary` / `wrong_scope` / `missing_coverage`.
- **Tier 1 — Case Type, wrong, either label invalid**: skip adjudication (deterministic) — `gap_type=invalid_label` if the value Fin used doesn't exist in the taxonomy at all (e.g. a non-canonical Case Type name); populated by Opus as before.
- **Tier 1 — Case Type, abstention** (`case_type_verdict=unclassified`, i.e. Fin left Case Type blank entirely): `gap_type=fin_abstention`. This should be rare in practice (Fin generally always assigns some Case Type) — if it occurs, the fix is a Fin Attributes completeness/default fix at the Case Type level, not a taxonomy edit.
- **Tier 2 — Issue Type, wrong, both labels valid**: run adjudication first, same logic as Tier 1. `adjudication_verdict=fin_correct` → `gap_type=agent_mistag`, no Opus. Otherwise → classification gap populated by Opus, scoped to Issue Type within the (correctly identified) Case Type — `gap_type` is `ambiguous_boundary` / `wrong_scope` / `missing_coverage`.
- **Tier 2 — Issue Type, wrong, either label invalid**: skip adjudication — `gap_type=invalid_label` if Fin's Issue Type value doesn't exist under that Case Type (e.g. an Issue Type borrowed from a different Case Type's list); populated by Opus.
- **Tier 2 — Issue Type, abstention** (`case_type_verdict=correct` AND `issue_type_verdict=unclassified`, i.e. Fin left Issue Type blank while Case Type was correct): `gap_type=fin_abstention`. This is the most common abstention pattern — Fin found the right branch and stopped. `recommended_fix` must target the Fin Attributes Issue Type value description (Applies if / Does not apply if / Likely keywords, or a documented safe default), never a taxonomy-doc edit.
- **Tier 3 — Reason, mismatch, both reasons valid**: run adjudication first. `adjudication_verdict=fin_correct` → `gap_type=agent_mistag`, no Opus. Otherwise → `gap_type=reason_mismatch`, reason gap populated by Opus.
- **Tier 3 — Reason, abstention** (`case_type_verdict=correct` AND `issue_type_verdict=correct` AND `fin_reason` is blank AND `correct_reason` is non-blank): `gap_type=fin_abstention`, even though `reason_match` itself is `n/a` for accuracy-math purposes (see the "Abstention blind spot" callout under Verdict logic). Do not let this fall through to `gap_type=none` — it must be surfaced.
- **No gap** (`case_type_verdict=correct` AND `issue_type_verdict=correct` AND `reason_match=yes`, or `reason_match=n/a` because **both** reason fields were blank) + both labels valid: `gap_type=none`, blank description and fix, `taxonomy_gap_candidate=no`.
- `agent_label_valid=no` (agent populated a non-blank, non-canonical Zendesk label): note this alongside whatever `gap_type` the row already has from the tiers above, or set `gap_type=invalid_label` on its own if the row is otherwise `correct`.
- Agent left a field blank while Fin's classification at that level is `unverifiable`: this is a Zendesk agent-tagging gap, not a Fin defect — `gap_type=n/a`, `gap_description` = "Zendesk agent did not populate this field — unable to verify Fin's classification against a human pick at this level.", `recommended_fix` = "Enforce that Zendesk agents populate this field before closing a ticket; untagged rows cannot contribute to QA or serve as Fin training signal."
- `unverifiable` (at whichever level `verdict` reports, driven by a blank `correct_*` field): same as above.
- **`agent_mistag` templated fix** (no Opus call): `gap_description` = the adjudication agent's one-line rationale for why Fin's label was correct; `recommended_fix` = "Fin's classification is correct; the Zendesk agent's label does not match this contact. Flag ticket [ticket_id] for agent QA/coaching — no Fin Attribute or taxonomy change needed."

---

## Execution

### Step 1 — Read inputs

Read `01-knowledge-base/processes/support-taxonomy.md`.

Note: `01-knowledge-base/processes/fin-attributes-definitions.md` is read in Step 1.6, once the relevant Case Types for this run are known — not here in full, to avoid loading its ~1,435 lines into every run regardless of relevance.

Determine the source from the argument:
- No argument, or `look:<id>` → **Looker Look source**. Default to look ID `18808` if none given. Follow the "Source: Looker Look" fetch procedure above: call `run_look` with an explicit high limit, extract rows with `jq`, apply the field mapping, dedupe thread rows to `message_order = 1`. Print the row count fetched.
- A file path → **file source**. Load with a Python script:
  - Detect format by file extension: `.md` = markdown table, anything else = CSV
  - For markdown: split on `|`, strip cells, skip separator rows, use first row as header
  - Apply the column name mapping using contains-match (see above)
  - Fall back: map the first column to `contact_id` if no match is found
  - Print: row count and column names found (after mapping)

Either way, the result of this step is the same shape: a list of dicts keyed by the canonical field names, held in memory (or a scratch JSON/JSONL file) — no intermediate CSV needs to be written to `04-active-work/`.

### Step 1.5 — Filter out already-reviewed tickets

1. Check whether `04-active-work/classification-qa-log.tsv` exists.
2. If it exists, read it and build a `seen` set from its `ticket_id` column values (using `contact_id` for any row where `ticket_id` is blank — this covers rows logged before the `ticket_id` column existed).
3. Filter the batch from Step 1: keep only rows whose dedup key (`ticket_id` if non-blank, else `contact_id`) is not in `seen`.
4. Print: `Fetched N rows. M already reviewed (skipped). K new rows to process this run.`
5. If `K == 0`: skip Steps 2-6, report `"N rows fetched, all N already reviewed. Nothing new to QA this run."`, and stop.
6. If `04-active-work/classification-qa-log.tsv` does not exist yet (first-ever run), treat all fetched rows as new.

All subsequent steps operate only on the K new rows.

### Step 1.6 — Extract the relevant Fin Attributes excerpt

`fin-attributes-definitions.md` is ~1,435 lines (roughly 4x `support-taxonomy.md`) and is the primary reference for Step 2.5 and Step 3. Sending it in full on every run wastes tokens proportional to how many of the 14 Case Types this run doesn't even touch — extract only what's needed:

1. From the K new rows, collect the distinct set of Case Type values across `fin_case_type` and `correct_case_type` (after normalisation) — this is the set of Case Types actually implicated by this run's batch.
2. `fin-attributes-definitions.md` is structured with `## Case Type: <name>` headings, each followed by its Issue Type and Reason sub-sections until the next `## Case Type:` heading. Extract the full block for each Case Type in the implicated set.
3. Concatenate the extracted blocks into a single excerpt, held in memory (or a scratch file) — this excerpt, not the full file, is what gets passed to Step 2.5 and Step 3.
4. Print: `Fin Attributes excerpt: N of 14 Case Types extracted (X of ~1,435 lines) — <list of Case Type names>`.
5. If a row's Case Type isn't found as a heading in `fin-attributes-definitions.md` (e.g. it's only in `support-taxonomy.md` so far), fall back to passing that row's `support-taxonomy.md` section instead and note the gap — this itself is worth surfacing, since it means the two files have drifted out of sync.

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

### Step 2.5 — Adjudicate ambiguous mismatches (default-model agent)

Gate rows per the "Adjudication" section above: `fin_label_valid=yes` AND `agent_label_valid=yes` AND (`case_type_verdict=wrong` OR (`case_type_verdict=correct` AND `issue_type_verdict=wrong`) OR (`case_type_verdict=correct` AND `issue_type_verdict=correct` AND `reason_match=no`)).

If zero rows pass the gate, skip this step and set `adjudication_verdict=n/a` for all rows.

Otherwise, spawn **one** `Agent` call (no model override — this deliberately stays on the cheaper default model, not Opus) for the full set of qualifying rows in this run, batched:

Pass to the agent:
- The Step 1.6 Fin Attributes excerpt (only the implicated Case Types, not the full file)
- Each qualifying row: `contact_id`, `contact_text`, `fin_case_type`/`fin_issue_type`/`fin_reason`, `correct_case_type`/`correct_issue_type`/`correct_reason`, and which cascade level first mismatched

Agent instruction:

> "For each contact, you're given Fin's classification and the Zendesk agent's classification — both are valid taxonomy labels, but they disagree at one level. The Zendesk label is a human agent's pick, not verified ground truth. Read the contact text against the attached Fin Attributes definitions and decide which label (if either) actually fits this contact best.
>
> Return exactly one `adjudication_verdict` per contact:
> - `fin_correct`: Fin's label fits; the agent's does not
> - `agent_correct`: the agent's label fits; Fin's does not
> - `both_wrong`: neither label fits this contact well
> - `ambiguous`: the contact text genuinely supports either label — no clean answer
>
> Also return a one-sentence `rationale` citing the specific signal in the contact text that drove your call.
>
> Output format: one JSON object per contact, with keys: contact_id, adjudication_verdict, rationale. Return a JSON array. No prose, no explanation outside the JSON."

Wait for the agent to return the JSON array before proceeding. Merge `adjudication_verdict` and `rationale` onto the corresponding rows.

Rows with `adjudication_verdict=fin_correct` are done: set `gap_type=agent_mistag`, `gap_description` = the returned rationale, `recommended_fix` per the templated `agent_mistag` fix (see Row rules), `taxonomy_gap_candidate=no` — and **exclude them from Step 3's Opus input**, since no classifier-definition diagnosis is needed.

Rows with `agent_correct` / `both_wrong` / `ambiguous` carry their `adjudication_verdict` forward as context into Step 3.

Print: `N rows passed the adjudication gate. Verdicts — fin_correct: N | agent_correct: N | both_wrong: N | ambiguous: N. N rows routed to Opus diagnosis, N resolved as agent_mistag without Opus.`

### Step 3 — Gap analysis (Opus agent)

Assign each row to at most one tier, by which cascade level first failed and whether it was a wrong value or a blank (abstention):
- **Tier 1, wrong**: `case_type_verdict=wrong`
- **Tier 1, abstention**: `case_type_verdict=unclassified`
- **Tier 2, wrong**: `case_type_verdict=correct` AND `issue_type_verdict=wrong`
- **Tier 2, abstention**: `case_type_verdict=correct` AND `issue_type_verdict=unclassified`
- **Tier 3, mismatch**: `case_type_verdict=correct` AND `issue_type_verdict=correct` AND `reason_match=no`
- **Tier 3, abstention**: `case_type_verdict=correct` AND `issue_type_verdict=correct` AND `fin_reason` is blank AND `correct_reason` is non-blank (include this even though `reason_match=n/a` — see the abstention blind-spot note)

Separately, flag rows where `agent_label_valid=no` (agent used a non-blank, non-canonical label — can co-occur with any tier, or occur alone if Fin's side is otherwise correct).

**Exclude rows resolved as `agent_mistag` in Step 2.5** — those already have their gap analysis (no Opus needed). Tier 1/2-wrong and Tier 3-mismatch rows only reach this step if either label was invalid (adjudication was skipped, deterministic `invalid_label` case) or adjudication returned `agent_correct` / `both_wrong` / `ambiguous`.

Spawn an Opus agent for the union of: all remaining Tier 1/2/3 rows (wrong-and-not-agent_mistag, or abstention), plus any agent-invalid-label rows not already included.

Pass to the agent:
- The Step 1.6 Fin Attributes excerpt (the implicated Case Types only) — this is the **primary reference**, since it's what actually drove Fin's output, not `support-taxonomy.md`'s prose
- `support-taxonomy.md`'s relevant sections as secondary context, for tree structure and cross-branch boundary notes the Attributes file may not spell out
- The "Fin Attributes reference" section from this skill file (Applies-if/Does-not-apply-if/Likely-keywords template and the abstention-vs-invalid-label distinction)
- All qualifying rows, each tagged with its tier+mode (e.g. `1-wrong`, `2-abstention`, `3-mismatch`, `3-abstention`, `agent_invalid_label_only`), plus contact_id, contact_text, fin values, correct values, case_type_verdict, issue_type_verdict, reason_match, fin_label_valid, agent_label_valid, and `adjudication_verdict`/`rationale` where Step 2.5 populated one
- The verdict and validity summary

Opus agent instruction:

> "You are auditing AI classification errors against Fin Attributes — the actual Intercom configuration that drives Fin's classification output. You've been given the relevant excerpt of `fin-attributes-definitions.md` (primary reference) and `support-taxonomy.md` (secondary, for tree structure). Each contact is tagged with a tier+mode — the tier tells you which level to analyse, and the mode tells you whether Fin used a wrong value or abstained (left the field blank). Do not analyse or comment on levels below the tagged tier: a Tier 1 (case_type) row failed at the root of the taxonomy, so its Issue Type and Reason fields are not meaningful signal and must not be used to justify a fix.
>
> Some rows carry an `adjudication_verdict` — this means a separate pass already confirmed the Zendesk label is NOT reliable ground truth for this contact, and determined:
> - `agent_correct`: the agent's label was right, Fin's is genuinely wrong — diagnose Fin's classifier-definition gap as normal.
> - `both_wrong`: neither party's label fits — lean toward `missing_coverage` unless the contact text clearly fits an existing definition that both parties missed (then it's `ambiguous_boundary` or `wrong_scope`).
> - `ambiguous`: the contact text could genuinely support either label — this is `ambiguous_boundary` almost by definition; focus the fix on sharpening the Does-not-apply-if boundary between the two values.
> Rows without an `adjudication_verdict` either have an invalid label (deterministic) or are abstentions — treat as before.
>
> - `1-wrong` / `2-wrong` rows: Fin populated a non-blank value that doesn't match. Diagnose why the wrong class was chosen — this is a classifier-definition gap (ambiguous_boundary, wrong_scope, missing_coverage) or an invalid_label if the value doesn't exist in the taxonomy at all.
> - `1-abstention` / `2-abstention` rows: Fin left the field blank despite the level(s) above it being correctly resolved. This is NEVER a taxonomy or definition gap — a valid answer existed and Fin declined to commit to it. Diagnose what in the contact text should have driven Fin to the correct value (or to a documented default, if one exists), and set gap_type=fin_abstention.
> - `3-mismatch` rows: diagnose the Reason mismatch only, within the (correctly matched) Case Type and Issue Type — gap_type=reason_mismatch.
> - `3-abstention` rows: Fin left Reason blank despite Case Type and Issue Type both being correct and a ground-truth Reason existing. Same logic as 2-abstention, scoped to Reason. gap_type=fin_abstention.
> - `agent_invalid_label_only` rows: diagnose the agent's invalid label only (their Zendesk tag doesn't exist in the taxonomy).
>
> For each contact, identify (1) the gap that caused the error and (2) a specific recommended fix.
>
> gap_type must be exactly one of:
> - ambiguous_boundary: the contact could fit multiple classes and the definitions don't clearly disambiguate
> - missing_coverage: no existing definition covers this contact type
> - wrong_scope: the definition's scope is too broad and incorrectly captures this contact
> - reason_mismatch: case type and issue type are correct but the reason label is wrong or inconsistently defined
> - invalid_label: Fin or the agent populated a field with a non-blank value that does not exist in the canonical taxonomy (wrong spelling, deprecated name, borrowed from another branch, or non-existent path)
> - fin_abstention: Fin left a field blank despite the level(s) above being correctly resolved and a valid taxonomy answer existing. This is a Fin Attributes completeness problem (an underspecified attribute description, missing keywords, or no safe default/"Other" value), never a taxonomy-tree or classifier-definition gap.
>
> If a row has both a classification error AND an invalid agent label, use the classification gap_type and mention the invalid label in gap_description.
>
> gap_description: 1–2 sentences describing what caused the error, scoped to the row's tier+mode. For invalid_label rows: name the invalid value and the correct canonical path. For fin_abstention rows: name the specific signal in the contact text that should have driven Fin to commit to the correct value.
>
> recommended_fix: For ambiguous_boundary / wrong_scope / missing_coverage / reason_mismatch / invalid_label: a ready-to-paste Fin Attribute value update in the Applies-if / Does-not-apply-if / Likely-keywords format (see the Fin Attributes reference), written as an edit to the *actual current wording* in the Fin Attributes excerpt you were given — not a fix invented from scratch — naming the exact level (Case Type, Issue Type, or Reason) and the correct value name. For fin_abstention: the same format, but framed as strengthening the target Attribute value's existing description (tighter Applies-if/Does-not-apply-if, more Likely Keywords) or adding/clarifying a safe default/'Other' value at that level — never propose lowering a confidence threshold or a support-taxonomy.md edit, since the taxonomy already has a correct answer that Fin failed to select.
>
> Output format: one JSON object per contact, with keys: contact_id, tier, gap_type, gap_description, recommended_fix. Return a JSON array. No prose, no explanation outside the JSON."

Wait for the Opus agent to return the JSON array before proceeding.

### Step 4 — Cluster gap analysis into a fix hitlist (Opus agent)

The per-row output from Step 3 is one fix per contact — at 200+ rows this is not something a human can work through one by one. This step clusters those rows into a small number of shared root causes and ranks them by impact, so the output is a prioritized backlog rather than a list of symptoms.

Spawn a second Opus agent. Pass it:
- The full JSON array returned by Step 3, **plus** the `agent_mistag` rows resolved without Opus in Step 2.5 (contact_id, tier, gap_type=agent_mistag, gap_description, recommended_fix, and the raw `fin_case_type`/`fin_issue_type`/`fin_reason` values so the reliability check below has something to compare)
- The total row count and case_type/issue_type/reason verdict breakdown from Step 2, for computing "% of batch" per cluster

Opus agent instruction:

> "You are clustering AI classification errors into a prioritized fix backlog. You've been given per-contact gap analysis (tier, gap_type, gap_description, recommended_fix) for a batch of contacts, including `agent_mistag` rows where a separate adjudication pass concluded Fin was actually right and the Zendesk agent mistagged the ticket.
>
> Group contacts into clusters by shared root cause — not just by matching gap_type, but by whether the underlying gap is actually the same one. Two `ambiguous_boundary` rows are only the same cluster if the same two classes are being confused for the same reason. Two `fin_abstention` rows are only the same cluster if they'd be fixed by the same Attribute value description update (e.g. multiple contacts abstaining on the same Issue Type for the same missing-default reason). Two `agent_mistag` rows are only the same cluster if the agent is confusing the same two classes for the same reason (e.g. repeatedly tagging a specific Issue Type when the contact is actually a different, adjacent one).
>
> **Never merge an `agent_mistag` or `fin_abstention` cluster with an `ambiguous_boundary` / `wrong_scope` / `missing_coverage` / `invalid_label` / `reason_mismatch` cluster, even if they land at the same tier and level.** These are different defects with different owners and different fixes — `fin_abstention` fixes go to whoever owns Fin Attributes config, `agent_mistag` fixes go to Zendesk agent QA/coaching (not Fin, not the taxonomy), classification-error fixes go to the taxonomy/classifier-definitions owner. Prefix abstention cluster names with '[Fin abstention]' and mistag cluster names with '[Agent mistag]' so this is unambiguous downstream.
>
> **Reliability check on `agent_mistag` clusters**: adjudication is a judgment call by a smaller model and can be wrong. If an `agent_mistag` cluster has 3+ contacts all citing the *same* Fin-side label as "correct," treat this as a signal worth flagging rather than accepting outright — it's equally consistent with "the agent really does keep mistagging this" and "adjudication is systematically over-crediting Fin on this specific label." Add a `reliability_flag: true` and a one-sentence caveat to any such cluster recommending a manual spot-check of a few contact_ids before acting on it.
>
> For each cluster, produce: a short cluster name, the tier (1/2/3) and gap_type, the count and list of contact_ids affected, a single merged recommended_fix (in the Fin Attribute Applies-if/Does-not-apply-if/Likely-keywords format from the gap analysis for classifier-definition/abstention clusters, or the plain coaching note for agent_mistag clusters, merged/generalized where the same fix covers multiple contacts) that would resolve all contacts in the cluster, and 1-2 sentences on the shared pattern.
>
> Rank clusters by impact: Tier 1 (case type) clusters first — a case type fix also recovers Issue Type and Reason scoring for every contact in it, since those levels were unscored (n/a) while case type was wrong. Within a tier, rank by number of contacts affected, descending.
>
> Return the top 10 clusters, or fewer if there are fewer than 10 distinct clusters. If more than 10 distinct clusters exist, cap at 10 and separately report the count of remaining smaller clusters and total contacts they cover — do not silently drop them.
>
> Finally, produce a `root_cause_summary`: exactly three buckets — 'fin_abstention' (contacts needing a Fin Attributes config/description fix, owner: whoever administers Fin's classification prompt/attributes), 'taxonomy_definition' (contacts needing a `support-taxonomy.md` / classifier-definition edit — ambiguous_boundary, wrong_scope, missing_coverage, reason_mismatch, and invalid_label rows where Fin used the bad value), and 'zendesk_tagging' (contacts where the agent's own label was invalid, blank, or — per adjudication — simply the wrong pick for this contact (`agent_mistag`); none of these are fixable by Fin or taxonomy changes — invalid/blank labels need ticket-closing enforcement, `agent_mistag` needs agent QA/coaching). For each bucket report the contact count and one sentence on what needs to happen, and for 'zendesk_tagging' break the count down as invalid/blank vs. mistag.
>
> Output format: a single JSON object with keys: clusters (array of {rank, tier, gap_type, cluster_name, pattern_description, recommended_fix, affected_count, affected_contact_ids, reliability_flag}), overflow ({cluster_count, contact_count} for clusters beyond the top 10, or null if none), and root_cause_summary (array of exactly 3 objects: {bucket, contact_count, note}). No prose outside the JSON."

Wait for the Opus agent to return this JSON object before proceeding.

### Step 5 — Merge, output, and append (per-row TSV)

This step operates only on the K new rows identified in Step 1.5 — never rewrites or reprocesses rows already in the log.

1. Merge gap analysis into the new row set using `contact_id` as key — this includes both the Step 3 Opus output and the Step 2.5 adjudication output (`adjudication_verdict`, and for `fin_correct` rows, the already-populated `gap_type=agent_mistag`/`gap_description`/`recommended_fix`)
2. Apply row rules from the Output TSV columns section above
3. For rows with no gap analysis entry (correct + reason_match=yes + both labels valid): set `gap_type=none`, leave description and fix blank
4. For rows that never passed the adjudication gate (abstentions, invalid labels, or agreements): set `adjudication_verdict=n/a`
5. Truncate `contact_text` to first 200 chars for the `contact_text_truncated` column
6. Stamp every new row's `run_date` with today's date
7. Produce TSV lines: tab-separated, replace any embedded tabs with a space
8. Append to `04-active-work/classification-qa-log.tsv` — write the header row only if the file doesn't already exist; otherwise open in append mode and write only the new data rows. Never overwrite existing rows.

### Step 6 — Append the fix hitlist section (markdown)

`04-active-work/classification-qa-fixes.md` is a running log — each run prepends a new dated section rather than replacing the file's contents. If the file doesn't exist yet, create it with just the header line below and this run's section.

Prepend (directly under the top-level `# Classification QA — Fix Hitlist` header, above all prior dated sections) a new section built from the Step 4 output for this run's new rows only:

```
# Classification QA — Fix Hitlist

## Run: YYYY-MM-DD

Source: classification-qa-log.tsv — N new rows this run (N verifiable), M total rows in log to date
Ranked by impact — Tier 1 (case type) first, since a case type fix also recovers Issue Type and Reason accuracy for every affected contact. Within a tier, ranked by contacts affected.

### 1. [Tier N] Cluster name — N contacts (X% of this run's batch)
**Gap type:** gap_type
**Pattern:** pattern_description
**Recommended fix:** recommended_fix
**Example contacts:** contact_id, contact_id, contact_id — (full text and raw labels in the TSV)
[If reliability_flag=true:] **⚠ Reliability check:** spot-check a few example contacts before acting — adjudication for this cluster leans heavily on one Fin-side label and could be systematically over-crediting Fin rather than genuinely catching repeated agent mistags.

### 2. ...

[If overflow is non-null:] N additional smaller clusters not listed above, covering N contacts. See the TSV (gap_type, taxonomy_gap_candidate columns) for the long tail.

**What to fix, this run — three separate root causes, not one:**

1. **Fin abstention (N contacts)**: <note from root_cause_summary>. Not fixable via taxonomy edits — flag to whoever owns Fin's Attributes/classification config.
2. **Taxonomy definition gaps (N contacts)**: <note from root_cause_summary>. These need `support-taxonomy.md` / classifier-definition edits — see the fin_abstention-excluded clusters above.
3. **Zendesk agent tagging gaps (N contacts, of which N are agent_mistag)**: <note from root_cause_summary>. Not fixable via Fin or taxonomy changes — invalid/blank labels need Zendesk ticket-closing enforcement; `agent_mistag` rows (Fin was right, the agent's valid-but-wrong label was adjudicated against it) need agent QA/coaching, not a system change. See any `⚠ Reliability check` notes above before treating agent_mistag counts as settled.

---

[...prior dated sections follow unchanged below...]
```

Compute "M total rows in log to date" by counting data rows in `classification-qa-log.tsv` after Step 5's append. Populate the "What to fix" block directly from Step 4's `root_cause_summary` — do not paraphrase away the fin_abstention / taxonomy_definition / zendesk_tagging distinction, since collapsing it back into one undifferentiated list re-introduces the original bug.

### Step 7 — Report to user

Print the following in this exact format:

```
Fetched N rows from source. M already reviewed (skipped). K new rows QA'd this run.

Appended to: 04-active-work/classification-qa-log.tsv (per-row detail, M+K total rows to date)
Updated: 04-active-work/classification-qa-fixes.md (new dated section prepended, ranked fix hitlist for this run)

=== ACCURACY SUMMARY — YYYY-MM-DD, this run's K new rows only (cascade: Case Type → Issue Type → Reason) ===
Case type accuracy:     N/N = XX%   (case_type_verdict:correct ÷ case-type-verifiable)
Issue type accuracy:    N/N = XX%   (issue_type_verdict:correct ÷ rows with correct case type, excl. unverifiable)
Reason accuracy:        N/N = XX%   (reason_match:yes ÷ rows with correct case type AND issue type, both reasons populated)
Overall accuracy:       N/N = XX%   (verdict:correct ÷ verifiable)

Case type verdicts:   correct: N | wrong: N | unclassified: N | unverifiable: N (excluded)
Issue type verdicts:  correct: N | wrong: N | unclassified: N | unverifiable: N | n/a (case type already wrong): N
Reason match:         yes: N | no: N | n/a: N

Gap types:  ambiguous_boundary: N | missing_coverage: N | wrong_scope: N | reason_mismatch: N | invalid_label: N | fin_abstention: N | agent_mistag: N
By tier:    Tier 1 (case type): N | Tier 2 (issue type): N | Tier 3 (reason): N

=== ADJUDICATION (Fin-vs-agent mismatches with two otherwise-valid labels) ===
Rows adjudicated:    N   (fin_label_valid=yes AND agent_label_valid=yes AND a mismatch — see "Adjudication" section)
  fin_correct:       N   (Zendesk agent mistagged; Fin was right — resolved as agent_mistag, no Opus/Fin-fix generated)
  agent_correct:     N   (Fin genuinely wrong — routed to Opus diagnosis as a real classifier-definition gap)
  both_wrong:        N   (neither label fit — routed to Opus, likely missing_coverage)
  ambiguous:         N   (contact could support either label — routed to Opus, likely ambiguous_boundary)
Opus calls avoided this run: N rows resolved without diagnosis (fin_correct) — this is the batch that would previously have been misdiagnosed as a Fin defect.

=== TAXONOMY HEALTH ===
Invalid Fin labels:       N rows — non-blank Fin values that don't exist in the taxonomy (excludes abstentions — see below)
Invalid agent labels:     N rows — non-blank Zendesk labels that don't match the canonical taxonomy
Fin abstentions:          N rows — Fin left a field blank despite a valid answer existing (Fin Attributes config issue, not a taxonomy gap)
Agent mistags:            N rows — Fin's label was adjudicated correct; the agent's valid-but-wrong pick is a Zendesk QA issue, not a Fin or taxonomy gap
Taxonomy gap candidates:  N contacts — may need new case type, issue type, or reason added

INVALID LABEL DETAILS (if any):
  Fin:   "[raw value]" → correct path: [Case Type / Issue Type] (N occurrences)
  Agent: "[raw value]" → correct path: [Case Type / Issue Type] (N occurrences)

=== WHAT TO FIX (three separate owners — do not collapse) ===
1. Fin abstention:        N contacts — <root_cause_summary note> — owner: Fin Attributes/classification config
2. Taxonomy definition:   N contacts — <root_cause_summary note> — owner: support-taxonomy.md / classifier definitions
3. Zendesk tagging:       N contacts (N invalid/blank + N agent_mistag) — <root_cause_summary note> — owner: Zendesk ticket-closing enforcement (invalid/blank) / agent QA & coaching (agent_mistag)

TOP 5 FIXES (Tier 1 case type fixes first — highest leverage, since a case type gap suppresses issue type and reason accuracy for every affected contact. Full ranked list of up to 10 clusters in classification-qa-fixes.md, under today's date section):
1. [Tier N] Cluster name — N contacts (X% of batch) — recommended_fix
2. ...
[If overflow: "+ N more smaller clusters covering N contacts — see the fix hitlist file."]
[If any cluster has reliability_flag=true: "⚠ N cluster(s) flagged for manual spot-check — see classification-qa-fixes.md."]
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
