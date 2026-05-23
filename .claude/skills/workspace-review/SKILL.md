---
name: workspace-review
description: Audit 04-active-work/, assign keep/update/archive/delete verdicts per file, then execute cleanup on confirmation. Invoke with /workspace-review.
tools: Read, Bash, Write, Edit, Agent
---

# Workspace Review

Scans `04-active-work/` (including subdirectories), assesses every file against the current roadmap and recency, assigns a verdict, produces a report, and on confirmation moves or deletes files.

---

## Verdicts

| Verdict | Rule |
|---|---|
| **Keep** | Tied to an active Q2/Q3/Q4 2026 deliverable; content is current |
| **Update** | Topic still active but content references past quarters as future, has stale dates, or has been partially superseded |
| **Archive** | Work complete, deliverable shipped, or file superseded by a newer doc — worth preserving as a historical record |
| **Delete** | Dated data export (`.tsv`, `.csv`) with a newer version in the same directory; scratch/duplicate content; safely regenerable |

---

## Phase 1 — Orient

1. Read `2026 deliverables.md` in full. Build a mental list of: active deliverable names, their quarters, and their status (complete / in-progress / deprioritised).

2. Run the following to get all files with modification dates:
```bash
ls -lA "04-active-work/" && echo "---" && ls -lA "04-active-work/roadmap-items/" && echo "---" && ls -lA "04-active-work/stakeholder-updates/" && echo "---" && ls -lA "04-active-work/merchant-interview-transcripts-2025/" 2>/dev/null || true
```

3. For each file in `04-active-work/` (root only — subdirs handled separately), read the first 40 lines:
```bash
for f in "04-active-work/"*.md "04-active-work/"*.csv "04-active-work/"*.tsv "04-active-work/"*.yaml "04-active-work/"*.yml; do
  [ -f "$f" ] || continue
  echo "=== $f ==="
  head -40 "$f"
  echo ""
done
```

4. Detect versioned duplicates: files sharing a base name with different date suffixes (e.g., `classification-qa-2026-05-18.tsv` vs `classification-qa-2026-05-22.tsv`). The older file is a Delete candidate; the newest is assessed on its own merits.

5. For `roadmap-items/`, read first 20 lines of each PRD to confirm which deliverable it maps to:
```bash
for f in "04-active-work/roadmap-items/"*.md; do
  [ -f "$f" ] || continue
  echo "=== $f ==="
  head -20 "$f"
  echo ""
done
```

---

## Phase 2 — Verdict (Opus)

Spawn an Agent with `model: "opus"` and pass:
- Today's date (use the `currentDate` from context, or `date +%Y-%m-%d` via Bash)
- The active deliverables list from Phase 1
- The file listing output (with modification dates) from Phase 1
- The first-40-line excerpts for all files from Phase 1
- The verdict criteria table above

Prompt the Opus agent:

> You are auditing the `04-active-work/` directory for a PM brain repository. Today's date is [DATE]. The active 2026 deliverables are:
>
> [DELIVERABLES LIST]
>
> Below are all files in 04-active-work/ with their modification dates and first 40 lines of content. Also below are the roadmap-items/ PRDs with their first 20 lines.
>
> [FILE EXCERPTS]
>
> For every file listed, assign one verdict: Keep, Update, Archive, or Delete.
>
> Rules:
> - Keep: file is tied to an active Q2/Q3/Q4 2026 deliverable and content is current
> - Update: topic is still active but content has stale quarter references (e.g., refers to Q1 2026 as future), outdated dates, or partial supersession
> - Archive: work is complete, deliverable shipped, or file is superseded by a clearly newer doc; worth keeping as historical record
> - Delete: dated data export (.tsv/.csv) with a newer dated version in the same directory; pure scratch; safely regenerable
>
> Additional rules:
> - Files in roadmap-items/ that map to active deliverables are always Keep
> - Merchant interview transcripts (merchant-interview-transcripts-2025/) are always Keep — primary research
> - stakeholder-updates/ files: Keep if referenced deliverable is still active, else Archive
> - The README.md in 04-active-work/ is always Keep
>
> Return a JSON array. Each element: { "file": "<relative path from repo root>", "verdict": "Keep|Update|Archive|Delete", "rationale": "<one sentence>" }
>
> Be decisive. If in doubt between Archive and Keep, prefer Archive. Do not return Update unless there is a specific named stale element.

Capture the JSON array output.

---

## Phase 3 — Report

Parse the JSON array and format a markdown report.

**Report structure:**

```markdown
# Workspace Review — [DATE]

## Summary
X keep · Y update · Z archive · N delete

## Verdicts

| File | Verdict | Rationale |
|---|---|---|
| 04-active-work/reflex-phased-plan.md | Keep | Active Q2–Q4 deliverable; content current |
| 04-active-work/classification-qa-2026-05-18.tsv | Delete | Superseded by classification-qa-2026-05-22.tsv |
| 04-active-work/care-product-strategy-inputs.md | Archive | Inputs doc superseded by final strategy files |
...

## Archive destinations
[list each Archive file and its target path in 05-archive/2026/<category>/]

## Files to delete
[list each Delete file]
```

Sort the table: Delete first, then Archive, then Update, then Keep.

Save to `04-active-work/workspace-review-[DATE].md`.

Print the summary line and the full table to the terminal, then print:

```
---
Report saved to 04-active-work/workspace-review-[DATE].md
Ready to execute: move [Z] files to archive, delete [N] files.
Confirm? Type yes to proceed, or no to stop here.
```

---

## Phase 4 — Execute

Wait for user confirmation.

If confirmed:

### Archive moves

Use this category mapping to determine the destination subfolder:

| File pattern | 05-archive/2026/ subfolder |
|---|---|
| `*strategy*.md`, `*model*.md`, `*vision*.md` | `strategies/` |
| `*-prd.md` in root (not roadmap-items/) | `investigations/` |
| `*.tsv`, `*.csv` | `data-exports/` |
| `*-spec.yaml`, `*-spec.md`, `*-spec.yml` | `specs/` |
| `*meeting*`, `*notes*` | `meeting-notes/` |
| Anything else | `investigations/` |

For each Archive file, create the destination directory if it doesn't exist, then move:
```bash
mkdir -p "05-archive/2026/<category>"
git mv "<source>" "05-archive/2026/<category>/<filename>"
```

### Deletions

For each Delete file:
```bash
git rm "<file>"
```

### Completion message

```
Done.
Moved [Z] files to 05-archive/2026/.
Deleted [N] files.

Review file kept at: 04-active-work/workspace-review-[DATE].md
Changes are staged but not committed. Commit when ready.
```

Do NOT run `git commit`.

---

## Notes

- Never delete files from `roadmap-items/`, `merchant-interview-transcripts-2025/`, or `stakeholder-updates/` without explicit instruction — these subdirs are always treated as Keep by default.
- If the JSON from Opus cannot be parsed, print the raw output and ask Charlie to confirm verdicts manually before executing.
- If `05-archive/2026/` does not exist, create it before running any moves.
