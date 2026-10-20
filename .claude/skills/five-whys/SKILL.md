---
name: five-whys
description: Use the 5 Whys to find the real question behind a request, problem or idea, then assess who the outcome affects and how. Invoke with /five-whys [problem, request or idea]. Use when a problem statement is vague, or is really a solution in disguise (e.g. "we need a chatbot for X"), before writing a PRD, deck or recommendation. Also use for "what is the real problem", "root cause", "why is this happening", "should we build X".
tools: Read, Glob, Grep, Write
---

# Five Whys: find the right question, then size the impact

The goal is not a root cause for its own sake. The goal is to end with a better question than the one the user started with, and a clear view of who is affected and how. Do not assume who is affected or which metrics matter: the chain should surface them.

## Step 0 - Orient

Check `04-active-work/` (and `05-archive/`) for existing work on the topic. Read it before starting. Use real data from `01-knowledge-base/` and `04-active-work/working-files/` when sizing. Never invent numbers; mark gaps `[NEEDS DATA]`.

## Step 1 - Capture the starting statement

Write the user's statement exactly as given. Classify it:

- Symptom: something observed ("CSAT dropped")
- Solution: a proposed fix ("we need a chatbot for refunds")
- Request: something someone asked for ("the COO wants a dashboard")
- Idea: something vague ("we should improve knowledge")

If it is a solution or request, the first "why" is: what problem is this meant to solve?

## Step 2 - Ask why, up to five times

Draft the whole chain yourself from the material available, then ask the user only about the weakest link. Do not interview one why at a time (ask one clarifying question at most).

- Each answer is a fact or a clearly labelled hypothesis, never a guess presented as fact.
- Ask "why does that happen?" for causes and "why does that matter?" for importance. Use both. Causes find the problem, importance finds what is worth solving.
- Branch when an answer has more than one cause. Follow the branch with the most evidence or impact first, and list the others as parked.
- Stop early when you hit something the team can act on, or something outside its control. Five is a guide, not a target.
- If an answer assigns blame to a person, turn it into a process or system cause.

Show the chain as a numbered list. Each line: answer, then evidence status (known, hypothesis, or needs data).

## Step 3 - Check the chain

- Does each step follow from the one before? Read it backwards with "therefore".
- Which steps are unverified? List what data would confirm each.
- Does the chain point at a cause the team can change?
- Was a simpler or cheaper explanation skipped?

## Step 4 - Reframe as the right question

- Original question or ask, as stated
- The real question, one sentence, open (starts with "how", "what" or "why"), containing no solution
- What would be different if the real question were answered

Example of the shift: "Can we add a refund bot?" becomes "Why do customers contact us about refunds at all, and which of those contacts are avoidable?"

## Step 5 - Assess impact of the outcome

Identify every group the real question affects. Derive the groups from the chain rather than from a fixed list. Include groups the user did not mention, especially ones that bear the cost but do not appear in the ask.

For each group:

- What changes for them if the outcome is good
- What changes if it is bad or the issue is left alone
- Rough size: how many people, how often, how much (state the basis, mark estimates as "estimate")
- Confidence: high, medium or low

Then:

- Second-order effects: what else moves (workload shifts, new failure modes, incentives)
- Cost of being wrong: what happens if the root cause is misidentified
- Reversibility: easy to undo, or not
- A leading and a lagging measure, chosen because they would show whether the real problem is fixed, not because they are the usual ones

## Step 6 - Recommend the next move

End with one of:

- Enough evidence: proceed to solution options on the reframed question
- Needs data: list 1 to 3 specific checks, who could run them, and what result would change the answer
- Wrong problem: explain why the original ask should be dropped or deferred

## Output format

1. Starting statement and its type
2. The why chain, with evidence status per step
3. Parked branches
4. The real question
5. Impact table: group, if good, if bad, size, confidence
6. Second-order effects, cost of being wrong, reversibility
7. Next move

Save to `04-active-work/research/five-whys-<topic>-<YYYY-MM-DD>.md` (check for an existing file on the topic first and update it instead). Reply with the file link, the real question, and the next move. No other summary.

Be direct. Challenge weak links in the user's reasoning. Keep each section short. Follow the writing style in `CLAUDE.md` (no em dashes, no hedging).

## Common failures to avoid

- Stopping at the first plausible cause
- Whys that drift into blame
- Treating a hypothesis as a finding
- A reframed question that still hides a solution
- Impact described only for the company and not for the people who bear the cost
- Precise-looking numbers with no stated basis
