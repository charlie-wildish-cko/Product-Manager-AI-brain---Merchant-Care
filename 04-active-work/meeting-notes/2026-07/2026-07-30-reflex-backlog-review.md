# Reflex backlog review

**Date:** 2026-07-30
**Attendees:** Charlie Wildish (PM, Merchant Care), Lachie Fielding, Anish Mavadia, Imran Khan
**Drive source:** 17OnLJGYGQRoBDtwaUcq97VGHKLbPX0g5cQJrlWTLa_8

## Context

Backlog review timed to extract Imran's knowledge before he leaves in about a week. Anish Mavadia replaces Jurro on Reflex.

## Key Points

**Status**
- First UI batch is done. Backend topic-merging awaits approval to run in prod; output then goes to Charlie to confirm which merges to accept.

**Topic quality**
- Duplicate topics: the model produces "payouts pending" in about 10 variants. Imran's hypothesis is prompt divergence over time in the ticket summarization prompt, specifically after the channel mention was removed. Anish is closing this out.
- Catch-all buckets: clearly present in topic list V1 and V2 (visibly generic labels), ambiguous in V3. One "payment status" topic may be a genuine high-volume topic or a catch-all. Cannot be judged without contact-level data, which doesn't exist yet.

**Data quality**
- Missing taxonomy values in some tickets. Unclear whether a filter issue (ingesting ticket types that shouldn't be there, e.g. QA tickets) or an upstream problem needing backfill. Current dataset is a 3-month QA snapshot taken 2 months ago, so Lachie argued against investigating on it. Agreed to recheck against prod.
- Product team field is mapped to the wrong field. Two fields share the same name with different field IDs: one used for L1/L2 transfers, one mapped from product name. Reflex uses the transfer one, causing confusion with internal transfer categories. Fix is a query change in the engineering repo, not a change on the data side. Correct field is the granular team level (pillar "Merchant Services", team "Payment Processing").
- Contact ID drill-down shows the Zendesk ticket ID plus an internally generated UUID surrogate key that links nowhere. Acknowledged, deferred.

**Visualisation**
- Landing experience is topic-level, not taxonomy-level. Level 1 = aggregate topic visualisations (top topics, change over time, filters applying across all charts). Level 2 = drill through to the Insights tab for granular views and eventually the underlying contact data. Anish to check how front-end queries are built.
- Imran's QA UI used a time series across all topics with a product filter to cut noise for PMs. It surfaced distinct spikes tied to real events, e.g. the Frames-to-Flow migration. Split bar chart discussed as the app equivalent.
- Filters already exist; the work is reordering them to be product-driven with the rest behind a "more" menu. Filter chips minimise on scroll to recover screen space.
- Sentiment colour: down (good) = green, up = red. Date presets: 30 days, 90 days, previous quarter.
- Current bar chart implementation shelved pending the broader visualisation strategy.

**Cost metrics**
- The cost field already exists in the table, so this is a query change in the engineering repo, not new modelling.
- Lachie: cost metrics in the Looker Merchant Care Overview dashboard are the north stars, so cost is needed at topic level and that dashboard is the reference.
- Imran's coded UI keeps volume and cost side by side as two columns. Charlie wants that on the topic view, relabelled "contacts" not "tickets", plus cost per ticket in drill-down and cost visible at conversation level. Bubble chart (size = magnitude) noted as a future option.

**Fin conversation ingestion**
- Data is already in the source table. Jurro filtered to Zendesk only, so this is removing a filter. No prompt change needed.
- Charlie expects it to compound existing large topics and add a lot of "how do I" questions from the dashboard. Imran flagged Fin's standardised handoff messages as noise an LLM will ignore. Lachie curious how Fin shifts the topic distribution.

## Insights

- Sequencing is explicit: topic quality first, then data quality, then visualisation, then Fin ingestion. Charlie repeatedly refused to design visualisations before topics are trustworthy.
- Contact-level data requires a backfill and is the critical-path dependency. Anish would not estimate ("could take a day, could take two weeks"). It gates catch-all verification and topic drill-down.
- Topic quality has two defects with different resolution paths: duplicates (prompt divergence, fixable now) and catch-alls (blocked on contact-level data).
- Key person risk: Imran holds the topic-quality and QA-UI knowledge and leaves within about a week. Anish is new to the codebase and hasn't read the front-end repo. One more session with Imran planned the following week.
- Reflex's north-star framing inherits from the Looker Merchant Care Overview dashboard, so cost sits next to volume everywhere rather than in a separate view.
