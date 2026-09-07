---
name: consolidation-review
description: Audit 01-knowledge-base/ and 04-active-work/ for content-level duplication across files (not file lifecycle), propose a canonical file per overlapping cluster, then merge and archive superseded files on confirmation. Invoke with /consolidation-review.
tools: Read, Bash, Write, Edit, Agent
---

# Consolidation Review

Finds files that say the same thing in more than one place — not stale or dead files (that's `workspace-review`'s job), but genuine content overlap: two docs covering the same topic, a fact duplicated and drifting apart, or a new doc that should have been a section in an existing one.

Scope: `01-knowledge-base/` and `04-active-work/`. Excludes bulk-imported reference dumps that are expected to have repetitive structure, not authored duplication: `01-knowledge-base/Support content/`, `01-knowledge-base/Tech Docs/`, `01-knowledge-base/Support content/API reference/`. Excludes `05-archive/` — frozen historical snapshots are not consolidation candidates.

---

## Verdicts (per cluster)

| Verdict | Rule |
|---|---|
| **Merge** | Two or more files substantively cover the same topic with overlapping content; one becomes canonical, the rest are folded in and archived |
| **Cross-reference only** | Files are related but each has a distinct primary purpose (e.g. a product reference doc and a phased delivery plan for that product) — add links between them instead of merging |
| **No action** | Topic proximity only; content does not actually overlap |

Only **Merge** clusters produce an execution step. **Cross-reference only** clusters produce a lightweight edit (add a "See also" link) rather than a full merge.

---

## Phase 1 — Inventory

1. List all files in scope:
```bash
find "01-knowledge-base" "04-active-work" -type f -name "*.md" \
  -not -path "*/Support content/*" -not -path "*/Tech Docs/*" \
  -not -path "*05-archive*"
```

2. For each file, capture path, title (first `#` heading), and first 40 lines:
```bash
for f in $(find "01-knowledge-base" "04-active-work" -type f -name "*.md" \
  -not -path "*/Support content/*" -not -path "*/Tech Docs/*" -not -path "*05-archive*"); do
  echo "=== $f ==="
  head -40 "$f"
  echo ""
done
```

Use Explore agents (parallel, "medium" breadth, split by top-level directory) if the combined output is too large for one context window.

---

## Phase 2 — Cluster candidates (Opus)

Spawn an Agent with `model: "opus"` and pass the file list with titles and excerpts from Phase 1.

Prompt:

> Below are files from a PM knowledge base, each with its path, title, and first 40 lines. Group files into clusters where two or more files appear to cover overlapping ground — the same topic, the same fact stated in more than one place, or content that reads as a duplicate/near-duplicate of another file.
>
> Do not cluster files just because they mention a shared keyword in passing (e.g. two files that both mention "Reflex" once are not a cluster). Cluster only when a file's *primary subject* overlaps with another file's *primary subject*.
>
> [FILE LIST WITH EXCERPTS]
>
> Return a JSON array. Each element: { "cluster_id": <int>, "files": ["<path>", ...], "shared_topic": "<one sentence>", "why_flagged": "<one sentence — what specifically overlaps>" }
>
> Only return clusters with 2+ files. Omit files with no overlap candidate — do not force singletons into a cluster.

Capture the JSON array. If empty, skip to Phase 5 and report "No consolidation candidates found."

---

## Phase 3 — Verify overlap (Opus)

For each cluster from Phase 2, read every listed file **in full** (not just the excerpt).

Spawn one Agent per cluster with `model: "opus"` (parallel across clusters), passing the full text of each file in the cluster.

Prompt:

> These files were flagged as a possible content-duplication cluster: [shared_topic]. Read them in full below.
>
> [FULL FILE CONTENTS, LABELLED BY PATH]
>
> Decide one of three verdicts:
> - **Merge**: the files substantively duplicate each other's content, or one is clearly a subset/superseded version of another. Identify which file should be canonical (most complete, most recently updated, or most authoritative per its directory — 01-knowledge-base/ docs outrank 04-active-work/ drafts for reference material) and what content from the others needs folding in before they're archived.
> - **Cross-reference only**: files are related but each serves a distinct purpose — recommend a specific "See also" link to add in each, pointing at the other(s).
> - **No action**: overlap was superficial; no change needed.
>
> Return JSON: { "cluster_id": <int>, "verdict": "Merge|Cross-reference only|No action", "canonical_file": "<path, if Merge>", "content_to_fold_in": "<bullet summary of what's in the non-canonical files that isn't already in the canonical one, if Merge>", "cross_ref_text": "<suggested link line, if Cross-reference only>", "rationale": "<one sentence>" }

Capture each cluster's verdict.

---

## Phase 4 — Report

Format a markdown report:

```markdown
# Consolidation Review — [DATE]

## Summary
X merge clusters · Y cross-reference clusters · Z no-action

## Merge candidates

### Cluster [N]: [shared_topic]
- Files: [list]
- Canonical: [path]
- Content to fold in: [bullets]
- Rationale: [sentence]

## Cross-reference candidates

### Cluster [N]: [shared_topic]
- Files: [list]
- Suggested links: [cross_ref_text per file]

## No action
[list clusters and why dismissed]
```

Save to `04-active-work/consolidation-review-[DATE].md`.

Print the summary and both tables to the terminal, then print:

```
---
Report saved to 04-active-work/consolidation-review-[DATE].md
Ready to execute: merge [X] clusters, add cross-references to [Y] clusters.
Confirm? Type yes to proceed, or no to stop here. You can also confirm subsets, e.g. "merges only" or "cross-references only".
```

---

## Phase 5 — Execute

Wait for user confirmation.

### Merges

For each Merge cluster:
1. Read the canonical file and each non-canonical file in full (if not already read this session).
2. Edit the canonical file to fold in `content_to_fold_in` — integrate into existing sections where topically relevant rather than appending an unstructured block. Preserve the canonical file's existing structure and heading conventions.
3. Archive each non-canonical file:
```bash
mkdir -p "05-archive/2026/<category>"
git mv "<source>" "05-archive/2026/<category>/<filename>"
```
Use the same category mapping as `workspace-review`: `*strategy*`/`*model*`/`*vision*` → `strategies/`, `*.tsv`/`*.csv` → `data-exports/`, `*-spec.*` → `specs/`, `*meeting*`/`*notes*` → `meeting-notes/`, else → `investigations/`.
4. If the canonical file lives in `01-knowledge-base/` and any archived file was linked from elsewhere (check with `grep -rl "<archived-filename>" 01-knowledge-base/ 04-active-work/ 03-templates/ CLAUDE.md README.md`), update those links to point at the canonical file.

### Cross-references

For each Cross-reference cluster, add the suggested link line to each listed file (typically under a "See also" heading near the top or bottom of the doc, matching the file's existing structure).

### Completion message

```
Done.
Merged [X] clusters into their canonical files. Archived [N] superseded files to 05-archive/2026/.
Added cross-references to [Y] clusters.

Review file kept at: 04-active-work/consolidation-review-[DATE].md
Changes are staged but not committed. Commit when ready.
```

Do NOT run `git commit`.

---

## Notes

- This skill does not overlap with `workspace-review`: that skill judges individual files against the roadmap (keep/update/archive/delete based on recency and relevance); this skill judges files against *each other* for content duplication. Run either independently.
- Never merge a file out of `04-active-work/roadmap-items/`, `04-active-work/merchant-interview-transcripts-2025/`, or `04-active-work/stakeholder-updates/` without flagging it explicitly in the report first — these are primary source or in-flight work, not reference docs, even if they look topically similar to something else.
- If a cluster's canonical-file choice is ambiguous (e.g. two files of similar completeness, both recently updated), surface both options in the report and ask Charlie to pick rather than guessing.
- `2026 deliverables.md`, `CLAUDE.md`, and template files in `03-templates/` are never merge targets or candidates — they are structural/reference files, not content that duplicates other content.
