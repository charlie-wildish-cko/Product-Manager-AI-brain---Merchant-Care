# Care AI agent monthly reviews (Fin QA onboarding)

**Date:** 2026-07-08
**Attendees:** Charlie Wildish, Preethy Sundaresan, Sebastian Garcia Cardona, Janny Chow (new Fin QA reviewer), Ling Wong, Joel Petrosino
**Drive source:** 16fHCEX2swE3FOCjNlIVRms1TLAdSUHPrgSpke8NXFko

## Context

Onboarding Janny Chow as QA reviewer for Fin, walking through the June review process. Linked artifact: "Chatbot Escalation Analysis" doc.

## Key Points

**Targets and volumes**
- Fin has run ~1 year. Currently involved in ~15% of tickets.
- 2026 goal: push Fin involvement to ~80% (all easy, repetitive volume) and resolution to 40–50% by year-end.
- Janny's review workload: escalated + negative conversations, last 7 days, ~30–50 items/week (an 8-week view showed 325, hence narrowing to 1 week).

**QA framework — three failure categories**
1. Product gap — missing feature or broken product behaviour driving the contact/escalation.
2. Missing content — the human agent knew the answer but it isn't documented, so Fin couldn't use it.
3. Bot issue — Fin misbehaved (wrong action, wrong answer, looping).
Reviewer cross-checks the Zendesk ticket to see the human agent's actual resolution.

**June examples**
- Missing content: merchant couldn't generate reports; human fix was "clear cache and retry" — undocumented. Tech writing to evaluate adding it.
- Bot issue — payment lookup misfire: merchant asked for a bank statement/transfer receipt/proof of payment for a payment ID; Fin wrongly triggered a payment lookup and returned irrelevant metadata. Root cause: still on the old "task," not the new "procedure." Possibly also a content gap (proof-of-payment is available from the Dashboard). 2–3 similar cases exist.
- Product gap — business details: merchant sees "outstanding items" notification but the product UI doesn't show what's outstanding (already filled in). Wrong error surfaced, referred to product team.
- Bot issue — reference not accepted: merchant supplied a payment reference; Fin only validates ARN or payment ID and kept asking for 5 payment IDs. This is an API limitation, not a Fin issue — reference is free text (up to ~180 chars); API needs logic to try it as a reference if not a payment ID or ARN. Known gap, not yet built.
- Human-preference escalations: many merchants bypass Fin to reach a human even when Fin worked well. Hard to solve short-term; confidence-building before engagement may matter more than having the right answer.
- Escalation loop (bot issue): Fin asked for more info before escalating, merchant repeated the same message, Fin tried to answer again instead of escalating. Legacy config required asking 3 times before escalating (since reduced to 2). Once a user provides requested info, Fin should escalate, not re-answer.
- Fee queries (bot issue): Fin falsely offers to look up fees if given a payment ID, but fee data isn't in the payment payload. A detailed fee-lookup guide exists in a Zendesk ticket — candidate for documentation.
- Pricing/fees: agreed to add to the list of issue types Fin escalates directly to a human. Underlying issue is a product gap that should eventually be self-serve.
- Apple Pay domain enrollment / MCRs: routing depends on whether merchant is managed (→ account manager) or unmanaged tier 5 (→ K/support). Fully automating MCR routing is hard (broad use cases, false-positive risk). Fin already prompts users to identify whether they have an account manager before escalating.

**Review mechanics**
- Scorecard: most fields pre-filled up to customer sentiment; reviewer completes accuracy + improvement requirement (mapped to the 3 categories, plus a content-accuracy/outdated option), which auto-generates a score.
- Customer sentiment is Fin-determined and treated as non-absolute.
- The reviewer's written note is the most important output — it carries the actionable fix.
- Submitted reviews move to a "completed/reviews received" queue for Charlie/Preethy to action.
- Access via Intercom → Analyze → Monitors (two monitors: email and chat escalated conversations); Janny logs in via SSO.

## Insights

- The 15% → 80% involvement / 40–50% resolution target is the headline Fin metric for 2026; the QA loop (categorize failure → fix content/config/API/product) is the mechanism to get there. Ties directly to the reduce-contact-rate / AI-deflection strategy.
- Recurring distinction: task (legacy) vs procedure (new SOP-style) — several June failures trace to conversations still on the old task. Migrating lookups to procedures is a live improvement lever.
- Concrete backlog generated: (1) API accepts payment reference strings; (2) suppress payment lookup for proof-of-payment/report requests; (3) fix escalation loop so info-provision triggers escalation; (4) stop Fin offering fee lookups; (5) add pricing/fees to direct-escalate list; (6) document "clear cache" fix and the fee-lookup guide.
- Guardrail insight: a meaningful share of escalations are pure AI-aversion, not Fin failures — resolution rate alone won't capture this, and it caps deflection regardless of content quality.
