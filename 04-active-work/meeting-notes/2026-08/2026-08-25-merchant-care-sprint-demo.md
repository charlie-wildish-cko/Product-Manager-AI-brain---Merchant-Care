# Merchant Care sprint demo

**Date:** 2026-08-25
**Attendees:** Fraser Bryant (organiser), Charlie Wildish, Joel Petrosino, Imran Khan, Lachie Fielding, Preethy Sundaresan, Oliver Westlake-Simm, Alcinda Lee, Ana Cachapa Cuomo, Ajay Paul, Ignas Sakalauskas, Kunal Patel, Stephen Adams, Sravanthi Vattikuti, Cain Voong, Mark Gossa, Philip Mueller, Bernard Ryan, Pao Igarteburu, plus care-experience group
**Drive source:** 1vxWsD2Llh7AxXvXU-tAM_nv3V1_CFpFrhfCIGa0-0y4

## Context

End-August sprint demo covering delivery status, the new target AI architecture, agent tooling consolidation, and the first hard performance numbers for the consultant bot.

## Key Points

**Sprint status**
- Moved from "concerningly orange" two weeks prior to mostly green. Deliverables close to completion and on schedule.

**Target architecture**
- Engineering is drawing a new target architecture covering enrichment, AI thread interactions, the customer bot (Javed's), the consultant bot, and Fin.
- Core shift in framing: AI should engage across the entire ticket lifecycle, not only react at ticket creation. Joel's operations-demo feedback drove this. Example: refund reversals waiting on third-party integrations.
- Concept of "machine users" in Plain, working alongside bots to assist agents.
- Engineering goals stated: automated ticket handling by default with human fallback; simplified architecture eliminating race conditions in enrichment; a single centralised configuration source of truth (owned by Ana and AJ) for taxonomy and similar, removing the need for Jira microservice tickets to change config; faster delivery; measuring tool usage efficiency via Plain and Sidekick.

**Agent tooling consolidation**
- The user profile Zendesk app and the payments-focused agent toolkit have merged into one app. Reads emails, searches client access and entities, adds tickets to fields via a single button, checks user permissions.
- All backend endpoints are reusable for Plain integration.

**Consultant bot performance (Shri)**
- 1,738 records to 24 August. ~1,800 ratings on a 1-5 scale.
- Average rating 3.05. 37.4% rated 4 or 5. 276 ratings of 5 against 680 ratings of 1 or 2.
- Gaps identified in 84% of tickets, by comparing agent closure comments against support consultant data.
- Chart dips are attributed to historical data backfill, not real degradation.
- Named gap example: the consultant bot has no access to settlement data.

**Decisions**
- Golden Signals project approved as a new initiative: 50 high-quality tickets as training and reference material for agents. Originated from a Shri and Charlie discussion with Joy. Proposed as a two-week project for the graduate team.

## Insights

- The consultant bot is underperforming on quality: 3.05/5 average and gaps in 84% of tickets. This is the hard baseline number for any Agent Consultant PRD or roadmap conversation.
- Root causes are partly data access, not model quality. Missing settlement data is a named example, which connects directly to the settlements data work with Joe Graves.
- Architectural direction is moving from event-triggered AI to lifecycle-resident AI. That changes how Agent Consultant and Fin Procedures should be scoped: the trigger set widens beyond ticket creation.
- Centralised config ownership removes a standing operational tax. Taxonomy changes currently require a Jira ticket per microservice, which is exactly the config-maintenance-at-scale argument being used in the platform assessment.
