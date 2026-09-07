# Improving incident comms for merchants

**Date:** 2026-07-29
**Attendees:** Charlie Wildish (PM, Merchant Care), Sebastian Garcia Cardona, Thomas Martindell, Alex Jordan
**Drive source:** 18FllA7h5_4avzmyNNfar2qfGE3iZsRQ3S06OIF3ty0Y

## Context

Fin has no incident documentation, so every incident-related contact goes to a human who checks the incident manually. The meeting scoped a content workflow to fix the post-incident half of the problem.

## Key Points

**Current state**
- No content articulates what happened, who was impacted, or what a merchant should do. Handling is ad hoc: a few one-offs from Alex, something Preethy put into Fin, agent macros Alex built from Tom's comms plus one article and CAM responses. Alex was only recently added to PagerDuty notifications.
- Competitor AI assistants proactively flag that an incident may be relevant to the query.

**Source content**
- Post-incident reports (PIRs) on Confluence, collected in a single repo page. Well curated and usable as-is or via a modified template. They publish only after the PIR completes, not mid-incident.
- MI / NMI in the incident string distinguishes Merchant Impacting from Not Merchant Impacting. Critical filter: NMI items are internal (BigQuery, Snowflake) and publishing them would generate bad Fin answers.

**Proposed workflow (Seb)**
- Atlassian MCP automation triggered on new additions to the Confluence PIR section: strip internal information, run content review agents, raise a PR, produce a draft for human review before publishing.
- Seb prefers a published-then-unpublished support article over Fin content guidance because it is easier to automate.

**Live incident vs post-incident**
- Tom's position, firmly held: live comms are general holding statements ("we're experiencing a problem with X service, investigating, will update shortly"), not granular detail. Attribution or blame during a live incident creates exposure. He never lets AI send merchant communication unsupervised. His current method: give Glean a previously written talking-points doc plus the incident channel, ask for the same format, then edit and post. Much faster than before. Alex accepted access to that doc.
- Alex's timing objection: PIRs lag, but merchants contact Care during the incident. Charlie's counter: Care already has automated feeds showing whether an incident is live and affecting a given merchant. What's missing is accompanying content, which may not exist that early.
- Charlie's structural objection: the burden always lands on a human. Within 10 minutes of an incident there should be automated triage and a merchant-communicable statement. The OC team is building an agent for automated triage from their data sources.

**Destination**
- The incident description, not an article, is the right target for live comms. It is what merchants see in the dashboard, and the dashboard API is already connected to Fin, so Fin can look up incidents. It only surfaces what the description contains. Articles carry the later, more detailed post-report view.
- Any article published internally or externally becomes available to all AI knowledge surfaces, so the internal/external split is a content-format decision for Alex, not an availability one.

**Content lifecycle**
- Contacts drop off after roughly two weeks: a spike the following week, then decline. Unpublish incident content after no more than 3-4 weeks, otherwise Fin surfaces a year-old incident as relevant.
- Sync frequency is unclear. Charlie believed support content re-syncs to Fin weekly, then found the setting says hourly, but the UI shows last sync today. He will investigate. Seb's fallback: tag these articles with special taxonomy so the workflow can force a re-sync via the Fin API.

**Measurement**
- No clean baseline. Identifying incident contacts is a semantic trawl through tickets, though the signals are consistent ("all my payments failed between these dates", "is there an outage?") and an existing Fin workflow detects those intents.
- Recent SEV1 produced no clear incident-related spike. Ticket volume was up by over 100 versus the prior week, but those tickets were not incident-related. Charlie's hypothesis: comms, account management and commercial teams curated it well. He had expected a large spike.

## Insights

- Charlie explicitly rejects framing outages as an AI deflection opportunity. The goal is handling them properly and efficiently, with reassurance and a path to resolution. Deflection may follow but is the wrong target metric.
- Two-layer model: holding statement in the incident description within minutes (upstream, OC-owned, largely outside Care's control), then a detailed article from the PIR days later (Care-owned, automatable now). Charlie accepted OC owns tightening the upstream half and chose to control the downstream half.
- Contact pattern has a meaningful slow tail: a merchant's own customer complains days later about a missing refund, the merchant investigates and finds an incident three days prior. That tail is what content solves.
- Scale concern stated directly: current standards depend on account managers manually handling comms for roughly 2,000 merchants. That does not survive next year's expansion. Tom's counterpoint: scale will force the fix.
- Long-term target is platform-based automatic triage that drafts responses from content, removing per-incident macro building.
- Not urgent, since incidents are not a daily occurrence. Framed as an addition to automated content workflows. Seb committed to a proof of concept by end of week: V1 drafts content from an existing PIR without publishing, purely to test the workflow.
