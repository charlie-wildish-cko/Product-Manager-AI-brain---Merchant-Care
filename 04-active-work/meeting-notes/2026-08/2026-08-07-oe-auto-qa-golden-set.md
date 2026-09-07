# Using OE Auto QA for Care golden set of contacts

**Date:** 2026-08-07
**Attendees:** Charlie Wildish (PM, Merchant Care), Sreekanth Nair ("Sri", engineer), Joel Petrosino (Operations Excellence)
**Drive source:** 1GNRtFuu21ZBUXh1fVjKDY0vQt0x8fJjT9IMzfAX209I

## Context

Care wants to reuse Operations Excellence's QA output as a grounded golden set of reference tickets for its AI tools, so the AI evaluates against verified examples instead of heuristically.

## Key Points

**OE quality framework**

- Scores agents across weighted categories with pass/fail. A core resolution failure (wrong information given to the merchant) fails the whole ticket. A relationship-building failure does not fail the ticket, for example a missed opportunity to promote self-serve.
- Only tickets that are solved and tagged "QA eligible" are scored. Scoring happens at closing time, not on resolution or open state, because scores can still change while a ticket is open.
- Framework was written by Alex. Care will adopt it as the standard for AI scoring evaluation rather than build a parallel one.

**Auto QA tool state**

- Running since 29 June 2026. Pulls transcripts and side conversations from BigQuery matched per ticket ID, then runs scoring.
- Currently writes to Zendesk sandbox only. Production deployment (child tickets with internal notes carrying the pass/fail breakdown) is gated on calibration confidence.
- Scoring is broken down by case type and issue type. Charlie and Sri want coverage indexed by ticket volume across the taxonomy (payins and payouts are roughly 60% of volume) and ideally down to reason level.
- Calibration example: one ticket flagged as the most complex in the batch and highest quality in the run, with findings independently verified by Ling and Harshell reading the transcript.
- Joel raised that the agent-facing output must be coaching-toned, not harsh. Alex plus training and knowledge want it agent-friendly and not complex.
- Codebase lives in the AICOE GitHub org. Joel has to submit PRs there and AICOE resource is limited, so change requests should be batched rather than iterated.
- UI is a Google Sites mockup, access-locked because it contains individual agent scoring on production tickets. Joel wants a "flagged tickets" section (fails and non-compliance plus best practice) with a "submit to data set" button so the golden set grows continuously.

**Golden set design**

- Contains passes only.
- Source window: tickets from 29 June 2026 onwards, plus an earlier manual golden data set compiled by Ling (a care lead plus a care senior) listing ticket IDs against each scoring criterion with reasons, split pass / passive feedback / fail. Roughly 2-3 months of data.
- Joel can add a Zendesk tag when a ticket qualifies as a golden ticket, so Care can identify them from ticket data.
- Architecture: keep a repository layer plus a swappable mapping layer so the system can be repointed at Plain or Intercom without rebuilding the logic. Joel's framing: build anything here with next year in mind.
- First experiment: take a sample of passes, build a small knowledge base on the agent, and measure the impact on AI performance.

**Documentation parity gap**

- The Support Consultant does not yet consume agent SOPs. Charlie's line: without documentation parity you are giving the AI half the knowledge and expecting the same job. Documentation parity is a prerequisite before running this.
- Support Consultant update (with Looker) is queued after Sri's current project.
- Taxonomy definitions live in a markdown file in GitHub that Charlie updates whenever the taxonomy changes. New values are incoming from Jonathan on token integration.

## Insights

- The golden set is not a single-use asset. It is reusable for taxonomy quality grounding (which improves Fin definitions and supports future taxonomy add/remove decisions), content gap detection (answers present in golden tickets but missing from the KB), and per-category continuous agent learning.
- The Plain/Intercom migration is already shaping build decisions in adjacent OE tooling, not just the core platform. Anything QA-related built in 2026 needs a mapping layer.
- Documentation parity, not model quality, is the hard dependency on the Support Consultant roadmap.
- Adopting OE's existing framework rather than building a Care-specific one avoids two competing quality standards and means AI scoring is directly comparable to human agent scoring.
