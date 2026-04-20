---
name: classify-definitions
description: Generate AI-readable classification definitions from the support taxonomy or product catalogue. Output is TSV (tab-separated) for direct paste into Google Sheets — one row per class, multi-value fields pipe-separated. Invoke with /classify-definitions [taxonomy|products|both] [optional: case_type or product_category filter]
tools: Read, Glob, Grep, Bash, Write, Agent
---

# Classify Definitions

Generate machine-optimised classification definitions. Output is TSV — one row per class, designed for direct paste into Google Sheets. Definitions are precise and unambiguous, written for AI consumption not human reading.

---

## Inputs

| Argument | Values | Default |
|----------|--------|---------|
| `scope` | `taxonomy` · `products` · `both` | required |
| `filter` | case type name, issue type name, or product category | none (generate all) |

Examples:
- `/classify-definitions taxonomy` — all case types and issue types
- `/classify-definitions products "Payment Methods"` — one product category
- `/classify-definitions both` — full combined output

---

## Source Files

| Scope | File |
|-------|------|
| Taxonomy | `01-knowledge-base/processes/support-taxonomy.md` |
| Products | `01-knowledge-base/products/product-definitions.md` |
| Product catalogue (names/categories) | `01-knowledge-base/Checkout Products and teams.csv` |

Read all relevant source files before spawning the agent.

---

## Output Format

Output is a TSV file. Print the full TSV content in a code block in the response (so the user can copy it), and also save it to disk.

Multi-value fields (include_when, exclude_when, disambiguation, keywords, phrases, entities, examples) use ` | ` (space-pipe-space) as the separator within a single cell.

No quotes around cell values unless the value itself contains a tab character (which should never occur).

### Taxonomy columns

```
id	parent_case_type	label	scope	include_when	exclude_when	disambiguation	keywords	phrases	entities	examples	reasons
```

| Column | Content |
|--------|---------|
| `id` | `snake_case_case_type.snake_case_issue_type` |
| `parent_case_type` | e.g. `payments_in` |
| `label` | Issue Type label as written in taxonomy |
| `scope` | One sentence: what this class covers, in active classifier terms |
| `include_when` | Pipe-separated conditions that should route here |
| `exclude_when` | Pipe-separated conditions that should NOT route here — each entry names the redirect target in parentheses, e.g. `merchant asks about enabling a payment method (→ account_management.payment_method_setup)` |
| `disambiguation` | Pipe-separated edge cases with explicit routing rules, e.g. `If merchant references 3DS → payments_in.authentication_3ds` |
| `keywords` | Pipe-separated single words that are strong classifiers |
| `phrases` | Pipe-separated multi-word patterns |
| `entities` | Pipe-separated named things: API field names, product names, error codes, UI labels |
| `examples` | Pipe-separated raw merchant query strings (2–3 per class) |
| `reasons` | Pipe-separated Reason labels for this Issue Type |

### Product columns

```
id	category	label	contact_risk	risk_reasons	description	include_when	exclude_when	disambiguation	keywords	phrases	entities	examples
```

| Column | Content |
|--------|---------|
| `id` | `snake_case_product_name` |
| `category` | Product category from catalogue |
| `label` | Product name as written in catalogue |
| `contact_risk` | `high` · `medium` · `low` · `unknown` |
| `risk_reasons` | Pipe-separated tags: `dispute-prone` · `mandate-management` · `setup-complexity` · `redirect-failure` · `auth-friction` · `account-management` |
| `description` | One sentence: what this product does, written as a classifier instruction |
| `include_when` | Pipe-separated conditions that should classify as this product |
| `exclude_when` | Pipe-separated conditions that should NOT classify here — each names the redirect target |
| `disambiguation` | Pipe-separated edge cases with explicit routing rules |
| `keywords` | Pipe-separated single words |
| `phrases` | Pipe-separated multi-word patterns |
| `entities` | Pipe-separated named things: API names, field names, error codes, UI labels |
| `examples` | Pipe-separated raw merchant query strings (2–3 per class) |

---

## Generation Rules

### Precision over coverage
- `include_when` and `exclude_when` conditions are mutually exclusive. If a signal appears in both, `exclude_when` wins.
- Every `exclude_when` entry must name the correct redirect target.

### Disambiguation is mandatory for adjacent classes
Any two classes sharing overlapping keywords must have explicit `disambiguation` entries pointing at each other.

### Signal types
- **keywords**: single words an AI would extract from a raw message (e.g. `chargeback`, `3DS`, `webhook`)
- **phrases**: multi-word patterns (e.g. `transaction stuck in pending`, `settlement delay`)
- **entities**: named things that uniquely identify the class — API field names, product names, error codes, UI labels

### No prose
- `scope` and `description` are single sentences only.
- `examples` are raw merchant query strings — no annotation, no explanation.
- No rationale, footnotes, or comments in any cell.

### Completeness
- Every issue type in the taxonomy must appear as a row.
- Every product in the product definitions file must appear as a row.
- Do not skip `unknown` contact risk products.

---

## Execution

### Step 1 — Read sources
Read the relevant source files based on scope and filter.

### Step 2 — Spawn Opus agent
Pass the source content to an Opus agent with this instruction:

> "You are generating machine-readable TSV classification definitions for an AI classifier. Output will be consumed directly by an AI model and pasted into a spreadsheet — optimise for precision and unambiguity, not human readability. Follow the column schema exactly. Use ` | ` (space-pipe-space) to separate multiple values within a single cell. For each row: write `include_when` and `exclude_when` as specific boolean conditions, not vague descriptions. Write `keywords` as exact strings an AI would extract from a merchant's message. Write `phrases` as exact multi-word patterns. Write `disambiguation` for every pair of adjacent classes that share overlapping keywords. Write 2–3 `examples` as realistic raw merchant query strings. Do not use hedging language. Do not add prose. Output the header row first, then one data row per class."
>
> Pass: the column schema, the source file content, and any filter.

Wait for the Opus agent output before proceeding.

### Step 3 — Validate, output, and save

Check output against:
- Every row has at least 2 pipe-separated values in `include_when`
- Every row has at least 1 pipe-separated value in `exclude_when`
- Every row has at least 2 values in `keywords`
- No `disambiguation` cell is empty where adjacent classes share keywords

Then:
1. Print the full TSV in a code block labelled with the scope and date, so the user can copy-paste directly into Google Sheets
2. Save to: `04-active-work/classifier-definitions-<scope>-<YYYY-MM-DD>.tsv`

Report: file path, row count, any classes skipped or flagged.
