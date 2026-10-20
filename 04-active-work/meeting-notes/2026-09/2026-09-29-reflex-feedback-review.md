# Reflex Feedback Review

**Date:** 2026-09-29  
**Attendees:** Charlie Wildish, Anish Mavadia, Harlie Patel (speakers anonymised, individual attribution not possible)  
**Drive source:** 1g5g_kBTsJK6OLyk4Y16RVjkxDgY3oUt85zzfsnVIyM8

## Context

First feedback review after Reflex launched to a restricted Slack group of PMs and designers. Goal: triage feedback and reach a stable point before opening to all users.

## Key Points

**Feedback process**
- New feedback items are added to the tracking list by an automated workflow (verified live on the call).
- The small audience repeats the same feedback, so rollout to everyone follows once core fixes land.

**AI chat ignores filters (top priority)**
- Root cause: the knowledge base is a large unstructured blob with no topic metadata or source mapping, so the AI cannot filter by topic. Two feedback items are the same issue. A fix is started.

**Ticket export**
- All contact data (metadata, description, summaries, full comments) is already in Looker and downloadable as CSV or MD. Decision: use Looker (link per topic or Looker MCP) instead of a custom export (about an hour to build, but needs contact table fields that may not exist in Reflex).
- Wanted fields, identical for every topic: subject, summaries, full comments, client name, client ID, ticket ID, cost, product, merchant, tier, resolution.

**Reflex vs Looker discrepancies**
- A topic shows about 5% of volume in Reflex and 7% in Looker. Cause: Reflex is built on AI summaries indexed every few days or weekly, then joined to the table Looker reads directly.
- Reflex holds no data older than 6 months. The backfill missed under 5% of tickets (a couple of hundred at most) to AI processing failures. Accepted as an initial loss.
- Reflex percentages are percentages of the filtered opportunity, not total volume.

**Metrics and cost**
- Added SLA attainment and L2 dependency percentage per topic from the existing support contact table. Low SLA means the topic hurts SLA performance. High L2 or non-Care team share means higher cost.
- Topic cost is the sum of weighted ticket costs, not average or median. A low-volume, high-cost topic still spikes. Confirmed as intended.

**Other items**
- Client name in the contacts table filter: blocked on add-the-field vs join decision.
- Product name fixes on hold: names come from the product catalogue and cannot change at Reflex level. Attribution is acknowledged as weak.
- Chat history: persists within the session only, plus a "new chat" button. Full history is a much larger build.
- UI: SLA, escalated, L2 and defence-team pills on the main page and topic drill-down. Idea: left-to-right routing flow chart (L1 to L2 to other teams). Bug: long topic text cut off.
- Semantic search for low-level feature issues in ticket content is feasible but not fully precise.

**Root cause and upstream**
- Tickets are a lagging indicator. Example: a client launched card payouts in August, transactions rose about 10,000% and about 1,000 tickets arrived in week one. Reflex shows tickets, not cause. Product release data and external sources are the planned input once a data scientist joins.
- Product catalogue team errors must be fixed upstream. Reflex only consumes the data.
- Reflex source fields (catalogue, taxonomy) are tightly coupled to Zendesk fields with no abstraction. Plan: remodel under a "support_content" naming schema so a platform change does not break it.

## Insights

- Reflex quality is capped by upstream Zendesk and catalogue fields. Product attribution is a known weak spot.
- Expect small Reflex vs Looker mismatches from indexing lag and the 6-month window.
- Topic cost ranks by total cost, not per-ticket cost.
- Zendesk field coupling is a migration risk for the Plain move. The support_content schema is the mitigation.
- Decisions: fix AI filtering first, Looker for exports, session-only chat history, roll out to all users after core fixes.
