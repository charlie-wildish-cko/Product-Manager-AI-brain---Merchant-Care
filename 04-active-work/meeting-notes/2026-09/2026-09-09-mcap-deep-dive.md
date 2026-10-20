# MCAP Deep Dive - Emerging Products

**Date:** 2026-09-09
**Attendees:** Orrin Ward (presenting), Jamie Sims, Inge Mutsaers, Antoine Keriven, Charlie Wildish, Annaelle Poisson, Stephanie Teo, Richard Ding, Gabriele Usonyte, Arthur Magnes, Madhur Khedekar, Davine Ittoo, Emily Geffen, Ellie Conheady, Julie Chalumeau, Gilles Beausseron
**Drive source:** 1J5_2dqbqRNakwy57TDT7PDNI5Uz6SCiAWeRDSQe-9Yc

## Context

Walkthrough of MCAP (Major Change Approval Process), which replaces the fragmented legacy launch-readiness framework, and what it requires of product teams.

## Key Points

**Why MCAP exists**
- Three stated problems with the old process: stakeholders engaged too late causing last-minute blocks, inconsistent cross-functional collaboration raising cognitive load for legal and compliance, and no tracking data to find bottlenecks.

**Process shape**
- Standardised PDLC stages: Ideation, Scoping, Planning, Execution, Launch (beta and GA).
- Mandatory artifacts: scoping brief (scope-approval gate), PRD (planning gate), solution design, integrated execution plan.
- Solution design is expected to be multiple connected sections, not one monolithic doc. The execution plan is a cohesive cross-domain deliverable map (marketing, commercial, legal, product, tech, finance) spanning up to 24 Jira spaces for large initiatives.
- Qualification criteria: greenfield launches, material product changes, material technology changes, regulatory or scheme events, strategic merchant events, plus 13 broader live event types.
- Scoping is opt-out, not opt-in. The brief goes via Hive to 45 Domain Points of Contact. Reg and Legal demanded that all product work route through them, so every scoping doc gets reviewed.

**Volume**
- The broadest 2026 Jira product-discovery view projected 860 initiatives, meaning 860 scoping docs reviewed by 45 people plus ~800 PRDs. After driver-versus-supporter triage the refined estimate is 150-200 initiatives.
- The 2027 planning process injected 150 initiatives into the older Hive instance. Orrin plans to merge the two Hive instances.

**PRD bloat**
- Jamie Sims reported reading PRDs up to 36 pages for minor updates, and argued length discourages both reading and authorship.
- Charlie and Jamie both flagged that AI-assisted writing tools generate massive unreadable documents, increasing the cognitive-transfer burden on readers.
- Orrin acknowledged the problem and asked the group for exemplar PRDs to base guidance on.

**Friction raised**
- Jamie Sims reported real friction on the Platforms-in-EA initiative: it moved to Planning prematurely before documents were submitted, and he has had to use Slack channels and Claude to drive stakeholder engagement because MCAP is not securing timely responses.
- Inge Mutsaers flagged the bottleneck risk of a 45-person stakeholder list and proposed an opt-out deadline so non-response implies no impact, avoiding month-long reviews. Orrin conceded Reg and Legal queues could stall initiatives ranked around tenth on their priority list.
- Emily Geffen voiced adoption scepticism: why will MCAP succeed where past processes failed. Orrin's answer: Strategy and Operations owns MCAP long term, with nurture programmes, tooling accountability, and empirical tracking of micro-process failures.
- Inge Mutsaers presented Product Registry (internal service determining merchant eligibility and product enablement across the dashboard, Salesforce, Airtable), assessed as a major change, currently between Scoping and Planning with a completed PRD.
- Feedback channels: `#ask-mcap` (public) and `#MCAP-pilot`.

**Decisions**
- Conservative entry policy: almost all product initiatives go through MCAP initially, with filtering and qualification refined over time.
- Work contributing to a larger parent initiative does not need its own MCAP. It rolls up into the parent's documentation.
- Unresolved: how to handle subsequent MCAPs spawned by scope negotiations and iterative add-ons, pending a verified lightweight approval path. Orrin's position is that repeat MCAPs are acceptable if approval triage stays fast.

## Insights

- Every Care initiative that counts as a material product change now needs a scoping brief through Hive to 45 domain contacts, then a PRD, solution design and execution plan. The organisation is deliberately over-inclusive at the start, so expect Care PRDs to be pulled into MCAP.
- The PRD-bloat thread is directly relevant to the PM brain's condense rule (~250-350 lines). 36-page AI-generated PRDs are now an explicitly named org problem, and Orrin is collecting exemplars: an opening to submit Care's template as a reference.
- The real risk to Care delivery is queue position, not process: Reg and Legal review every scoping doc, and Orrin conceded initiatives low on their priority list can stall.
- The parent-initiative rollup rule is useful for Care: bundling related deliverables under one parent avoids repeat MCAPs per sub-component.
