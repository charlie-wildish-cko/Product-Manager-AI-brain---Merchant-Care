---
name: sync-meeting-notes
description: Scan the Google Drive meetings folder for new Gemini-generated meeting notes since the last sync, filter out recurring syncs without strategic content, and write structured notes files into 04-active-work/meeting-notes/. Invoke with /sync-meeting-notes [optional: YYYY-MM-DD cutoff].
tools: Read, Bash, Write, Agent, mcp__524a2989-6e89-4987-9cc4-c5ed852a61fb__search_files, mcp__524a2989-6e89-4987-9cc4-c5ed852a61fb__read_file_content
---

# Sync Meeting Notes

Pulls new "Notes by Gemini" documents from the Google Drive meetings folder and writes structured meeting notes files into `04-active-work/meeting-notes/YYYY-MM/`. Skips recurring syncs and meetings with no strategic content.

---

## Drive folder

**Folder ID:** `1Mnz7XMPGYaeZG0nHQ4_R9mYn06188zU8`

This folder contains all Gemini-generated Google Meet notes for Charlie Wildish's meetings.

---

## Exclusion rules

Skip any meeting where the title matches one of the following patterns. These are recurring syncs with no strategic content worth preserving:

| Pattern | Reason |
|---|---|
| Title contains "Tech Ops" OR "Tech<>Ops" OR "Tech & Ops" | Bi-weekly engineering sync — operational, not strategic |
| Title contains "Charlotte" (standalone meeting) | Fortnightly 1:1 without strategic content |
| Title starts with "Meeting started" or title is blank | Auto-generated label, no content |
| Title contains "Reflex Weekly" OR "Reflex sync" | Weekly team sync — covered by Reflex Q2/Q3 planning docs |
| Title contains "Reflex Stand" | Standup — no strategic content |
| Transcript duration < 60 seconds (inferred from "Transcription ended after 00:00:XX" where XX < 60) | Meeting did not happen or no usable content |
| Gemini summary says "not enough conversation in a supported language" AND no transcript content | Nothing to capture |

When in doubt, read the content snippet before deciding to skip. Include if there is at least one strategic insight, decision, or product finding.

---

## Meeting types

### Standard strategic meetings
Write to `04-active-work/meeting-notes/YYYY-MM/YYYY-MM-DD-[slug].md`

The slug is a short kebab-case description of the meeting subject: `joel-ops-ai-model`, `fin-procedure-prep-icx`, `mastercard-proof-of-payment`. Not participant names unless that is the only identifier.

### Merchant support needs interviews
If the meeting title contains "merchant support needs", "support needs", or is explicitly a merchant interview (title contains a merchant name like "Temu", "eBay", "Invygo", etc.):
- Write a merchant research file to `04-active-work/research/merchant-support-needs/[merchant-name].md`
- Check if a file already exists for that merchant — if so, append new insights rather than overwrite

---

## Phase 1 — Find the cutoff date

1. Find the most recently modified meeting notes file to auto-detect the last sync date:
```bash
find "04-active-work/meeting-notes" -name "*.md" | sort | tail -1
```

Extract the date from the filename (format: `YYYY-MM-DD-*`). Use this as the cutoff — search for meetings **after** this date.

2. If an argument was passed to the skill (e.g. `/sync-meeting-notes 2026-05-01`), use that date as the cutoff instead.

3. Print the cutoff date so the user can confirm before proceeding:
```
Scanning for meetings after [CUTOFF DATE].
Last notes file: [filename]
```

---

## Phase 2 — Search Drive for new meetings

Search the Drive folder for Gemini Notes docs created after the cutoff date:

```
mcp__524a2989-6e89-4987-9cc4-c5ed852a61fb__search_files:
  query: parentId = '1Mnz7XMPGYaeZG0nHQ4_R9mYn06188zU8' and createdTime > '[CUTOFF_DATE]T00:00:00Z' and title contains 'Notes by Gemini'
  pageSize: 50
```

If the result has a `nextPageToken`, paginate until all results are retrieved.

Build a list of candidate files: `{ id, title, createdTime }`.

Apply the exclusion rules from the section above to each title. For any uncertain cases, note them but don't skip them.

Print a summary:
```
Found [N] new meeting notes. [X] excluded by filter rules. [Y] to process.
Excluded: [list of skipped titles]
```

---

## Phase 3 — Read and summarise

Process candidates in batches of 3–4, using parallel Agent calls. For each batch, spawn an Agent with this prompt:

> Read these Google Docs using the Drive MCP tool `mcp__524a2989-6e89-4987-9cc4-c5ed852a61fb__read_file_content` (fileId parameter). For each document, return a structured summary:
>
> - File ID and meeting title/date
> - Attendees (if listed in the document)
> - Key discussion points (bullet list — facts, findings, decisions discussed)
> - Decisions or conclusions reached
> - Strategic insights worth preserving (what would a PM want to remember in 3 months?)
>
> If a document has no substantive content (< 60 second transcript, Gemini summary failure, meeting did not happen), say so explicitly and note the file ID to skip.
>
> File IDs to read: [list]
>
> Return raw structured text. Be thorough — capture specific numbers, product decisions, named people, and concrete findings.

Collect all summaries. Flag any files that agents report as empty/no-content.

---

## Phase 4 — Write notes files

For each meeting with substantive content, write a notes file.

**File format:**

```markdown
# [Meeting Title]

**Date:** YYYY-MM-DD  
**Attendees:** [names and roles]  
**Drive source:** [file ID]

## Context

[1–2 sentences: why this meeting happened, what it was trying to resolve]

## Key Points

[Structured bullets — grouped by topic if the meeting covered multiple subjects. Use bold sub-headings for distinct topics. Include specific numbers, names, and concrete details.]

## Insights

[Bullet list of the most important things to remember — strategic decisions, architectural choices, product gaps confirmed, risks surfaced, or findings that should influence future work. These are the things a PM would want when they open this file cold in 3 months.]
```

**Rules:**
- No "Actions" or "Next steps" sections — insights only
- No hedging language ("may", "could potentially")
- No padding or filler sentences
- Include specific numbers where they exist (volumes, costs, percentages, dates)
- If a meeting covers the same topic as an existing notes file, write the new file independently (do not merge)
- The Drive source ID allows future re-reading if needed

**Filename:** `YYYY-MM-DD-[slug].md` where the date matches the meeting date (from the doc title or createdTime), not today's date.

Create the monthly subfolder if it doesn't exist:
```bash
mkdir -p "04-active-work/meeting-notes/YYYY-MM"
```

---

## Phase 5 — Knowledge base insertions (optional)

After writing notes files, scan the new content for insights that belong in existing knowledge base files. Apply the same judgment used when you insert findings from research into strategy or product docs.

Candidates for insertion:
- `01-knowledge-base/strategy/care-product-model.md` — new structural gaps, confirmed volume patterns
- `01-knowledge-base/products/agent-consultant.md` — new use cases, capability confirmations, limitations found
- `01-knowledge-base/products/reflex.md` — new architecture decisions, data source additions
- `01-knowledge-base/products/fin-ai-agent.md` — Fin capability findings, deployment decisions, bugs
- `01-knowledge-base/products/zendesk.md` — integration findings, platform decisions
- `04-active-work/research/merchant-support-needs/[merchant].md` — new merchant-specific findings

For each candidate insertion, show what you intend to add and where, then make the edit. Keep edits minimal — add a callout block or a bullet under the relevant section. Do not rewrite existing content.

If no insertions are warranted, skip this phase silently.

---

## Phase 6 — Report

Print a completion summary:

```
Sync complete — [DATE]

New notes files written: [N]
  [list of filenames]

Skipped (no content): [list of file IDs / titles]
Skipped (filter rules): [list of titles]

Knowledge base updates: [list of files updated, or "none"]
```

Do not commit. Leave changes staged for the user to review.

---

## Notes

- The Drive MCP returns file content for Google Docs. If a file returns an error, note it in the skipped list and continue.
- If a meeting is ambiguous (unclear whether it has strategic content), read the first few paragraphs of the content snippet from the search result before deciding.
- Paginate the Drive search if there are more than 50 results — use `nextPageToken` from the search response.
- If the cutoff auto-detection finds no existing notes files, default to `2026-01-01` and warn the user.
- Monthly folders already exist for 2026-01 through 2026-06. Create new ones as needed.
