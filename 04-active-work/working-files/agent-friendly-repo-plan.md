# Agent-friendly repo: plan for review

Status: Approved by Charlie. Scope approved: phases 1 and 2 only, then stop for review. This PR is phase 1.
Anchor: repo tooling, not a named deliverable in `2026 deliverables.md`. It supports the contact-rate goal only indirectly, by cutting rework in every Care Product session.

Security items found during the audit were raised with Charlie separately and are not tracked in this file.

## 1. Evidence

Sources: 127 past sessions (user messages mined by two independent readers over disjoint halves), 22 commits (66 across all branches), 20 memory files, and 7 prototypes. Commit messages carry little signal: 11 of 22 are "updates" or "many updates", and 4 are rename-only commits with 0 insertions.

| Mistake class | Sessions (half A / half B) | Hard number from the repo |
|---|---|---|
| Change not propagated to every doc that restates a fact | 14 / 9 | `$0.90 per resolution` is in 18 files. Ray timeline is in 9 live files. CLAUDE.md named a deliverable, "Improve Fin Resolution Through Procedures", that does not exist in `2026 deliverables.md` (the item is "AI First Resolution Using Fin"), and phase 1 fixed it. "Standard" tier: 19 live lines in 15 files after the rename to Growth. |
| Wrong or unlabelled source of truth | 0 / 11 | 214 of 711 active docs link an external authority (Google Doc, Confluence, Airtable, GitHub). 10 carry a sync date or source-of-truth note. |
| Moved or renamed a file, did not update referrers | seen in 5+ commits | 606 path refs checked, 46 distinct targets missing (71 refs). Live docs still cite `roadmap-items/`, renamed 21 weeks ago. |
| Domain facts wrong, current state not in the repo | 11 / 9 | No current-state fact sheet. Decisions live in Google Docs and chat. |
| Duplicate or misplaced files | 9 / 7 | The 2026-10-05 slide-content skill wrote a second file that repeated the story spine. Content overlap with the doc it repeated: 0.02. |
| Over-delivery, too long for the audience | 7 / 9 | PRDs of 327 to 408 lines against a stated 250 to 350. 50 files over 30 KB hold 74% of authored bytes. |
| Acts when asked to advise, overwrites user-owned text | 8 / 6 | No marker for human-owned sections. |
| Internal context leaks into shared artifacts | 8 / 5 | No audience flag and no export step. |
| Output needs a specific destination format (TSV, PDF, HTML) | 9 / 0 | TSV request repeated in 4 sessions. |
| Unsourced or inconsistent numbers | 6 / 6 | Product count: CSV 262 rows, definitions file 290 headings, MEMORY.md 258. |
| Skill config drift (hardcoded folder and field IDs) | 3 / 4 | Meeting-note sync broke when the Drive folder went quiet on 2026-08-07. |

Not real problems here, so the plan skips them:

- Finding existing files inside the repo. Benchmark, 10 queries, baseline versus a generated 180-line index: both 10 of 10 correct. Tool calls 54 versus 37 (-31%). Subagent tokens about 10% higher with the index. One query exposed a misleading filename, not a missing index.
- Duplicate content on disk. Only 2 pairs share over 50% of 4-grams across 149 authored docs.
- Braavos staleness. 48 files mention it, 2 lack ended or replaced context.
- Deliverable-quarter drift. 1 disagreement in 16 checked windows.
- Style rules. No session corrected em dashes, hedging, or flattery. The em-dash ban (stated in 8 places) is violated 5,232 times. Decision for you: drop the rule or ratchet it. This plan does neither.

## 2. What the prototypes settled

| Open question | Result | Decision |
|---|---|---|
| Does a topic index help agents find work? | Faster, not more correct | Do not build it. |
| Can a content-similarity lint catch the duplicate-file mistake? | No. 0.02 overlap on the real case | Fix the skill's save step and gate new files on a `deliverable:` match instead. |
| How often do agents create new docs? | 103 doc writes over 127 sessions, 54 are meeting notes (exempt). About 0.4 per session otherwise | A new-file prompt fires rarely. Use `ask`, not `deny`. |
| Is a banned-alias lint precise enough to block? | "Standard": about 3 of 19 hits are legitimate, roughly 16% false positives | Block, with an inline exemption marker. Under the 20% bar. |
| Is moving files into one folder per initiative safe? | 8 of 9 PRD folders map to line items, not deliverables, and file moves are already the top git-measured failure class | Defer. Not in this plan. |

## 3. Target architecture

Design run twice by independent runners (opus, fable) with different constraints. Base: the front-matter design. Grafts: skill output contracts and skill config from the folder design. Rejected: the folder-per-initiative move (about 95 file moves, unproven grain) and the index.

- 00-facts/facts.yaml. One entry per current-state fact, decision, or assumption: product count (derived from the CSV), unit costs, Ray timeline, team composition, current-state facts. Docs link or restate, and a check lists every stale restatement.
- 00-facts/glossary.yaml. Only terms with banned aliases (Standard to Growth, Moron to Meron, entity to customer). The 200-term payment glossary stays where it is.
- 00-facts/sources.yaml. Every external authority and every external ID the skills hardcode (Drive folder, Airtable IDs, Look 18808, Confluence parents, the Plain deck).
- Front matter on about 156 authored docs: `status`, `owner` (charlie or shared), `audience`, `deliverable`, `verified_on`, optional `canonical_source` plus `synced_on`, `superseded_by`. Imported content (3,872 files), the archive, transcripts, and old meeting notes get a path class and no front matter.
- `scripts/repo_check.py`, one script, one error format: `path:line: problem. Fix: action`. It runs as a Claude Code hook on write, as a pre-commit hook for your Obsidian edits, and in CI.
- Skill contract: no skill chooses a save path. Each updates the named doc in place or replies in chat. IDs come from `sources.yaml`.
- CLAUDE.md shrinks last, from 26 KB to about 12 KB (estimate), because the checks replace the prose rules.

How each class is handled, highest level that works:

| Class | Eliminate | Enforce | Docs only |
|---|---|---|---|
| Propagation, numbers, terminology | facts and glossary entries | stale-value and banned-alias checks | |
| Wrong source | `canonical_source` plus `sources.yaml` | reference check | |
| Moved file, dead referrer | | broken-path check in CI | |
| Duplicate or misplaced file | skill save contract | new-file gate | |
| Overwrites your text | `owner: charlie` | edit gate | "suggest" means chat |
| Internal context in shared docs | `audience`, export step | internal-marker scan on exports | |
| Over-delivery | | length warning by doc type | default depth per type |
| Destination format | | | five-row table |
| Skill config drift | `sources.yaml` | raw-ID check in skills | |

## 4. Phases, each one PR with a proof

Each check is proven by making it fail on a real past mistake before it ships.

1. **Subtract.** Untrack the 4 dead worktree gitlinks and `.obsidian/`. Delete the older `payment search API schema.md` and its stale PDF (the kept `payment-search-api-schema.md` holds all its fields). Delete `workspace-review-2026-07-10.md` (29 dead refs). Fix the phantom deliverable name. Add `.obsidian/` and `.claude/worktrees/` to `.gitignore`. The collapse of the 3,829 per-file ignore lines to directory rules is deferred, because directory rules change new-file behaviour and the decision on which SOPs copy is canonical is pending. Proof: git status clean, `git ls-files` count drops.
2. **repo-check v0.** Broken-path check plus tests. Fixes the 46 dead targets. Proof: it fails on the `roadmap-items/` refs on the pre-fix commit.
3. **Facts, glossary, sources.** The stale-value, banned-alias, and quarter checks. Fixes the Standard, 258/262/290, and $0.90 sites. Proof: it fails on the "Standard" and phantom-deliverable lines at HEAD today.
4. **Front matter and gates.** Codemod defaults onto about 156 docs. You set about 20 values by hand (owner, copies, superseded PRDs). Add the new-file and owner gates. Proof: replay the slide-content duplicate and the "suggest, don't edit" case.
5. **Skill contracts.** 13 skills. Save steps become update-in-place. IDs move to `sources.yaml`. Dry-run checks for the sync skills (rows in equals rows out). Proof: rerun `/slide-content` on the 2026-10-05 brief and count new files written (target 0).
6. **Shrink docs.** CLAUDE.md, README generated skills table, memory entries now enforced by checks. Proof: a fresh session answers the 10 benchmark queries with no loss.

Cost estimate (guess): about 10 new files, about 210 file edits (160 via codemod), one 450-line script, 6 PRs.

## 5. Decisions only you can make

- `Care Agent SOPs/` (untracked, 527 files) duplicates the tracked `checkout-support-site-internal/` (529 files, 511 shared article IDs). CLAUDE.md pointed agents at the untracked copy. Resolved: `checkout-support-site-internal/` is canonical (decided 2026-10-21). The old folder stays on disk, deprecated. Deleting it is Charlie's call.
- Em-dash rule: drop it or ratchet it.
- Execution mode: Autopilot-stack or Autopilot-full.
