# Bug / enhancement reporting standardisation

**Date:** 2026-09-09
**Attendees:** Nicolas Maalouf (CPP), Philippe Leonhardt (CPP), Maris Kõllamets, Charlie Wildish, Harlie Patel
**Drive source:** 1z2FekSaTgDtboK0SShXZcBUDZmXvuSn3OzThzfoee3o

## Context

Commercial Product Partnership (CPP) wants a standard route for bugs and enhancement requests raised by commercial teams. Charlie demoed Reflex as the candidate aggregation layer.

## Key Points

**The problem**
- Bugs and enhancement requests are raised inconsistently. Some product teams use spreadsheets, others link directly to Jira. Maris confirmed there is no consistent method and no single list. Jira backlogs are probably not standardised across pillars either.
- Regional fragmentation example: MENA adopted Flow earliest, hit the most merchant issues, and built its own backlog. There are now three or four competing trackers and no clear source of truth.
- Charlie's view: issues should be logged against a merchant and tied to revenue or GPV at risk.

**Dashboard feedback feature**
- The closest thing that exists today. Hidden behind the help icon, merchant-facing, submissions land in a Google Sheet for the dashboard team rather than being collected holistically.
- Charlie noted it is impractical to tell enterprise tier-1 merchants to log issues in the dashboard when they have AMs and TAMs. It is also unclear whether internal users can submit, and the dashboard should not be an internal tool at all.

**Commercial intake scope**
- Deliberately high level, the smallest common denominator: who the merchant is, revenue at stake if unfixed, and a free-text description. No reproduction steps, no MCC, no entity or processing channel.
- Philippe flagged entity type and processing channel as metadata worth capturing.
- Primary submitters are solution engineers, almost exclusively.

**Incidents as an untapped source**
- SEV1s are visible to the whole business. Daily SEV3 and SEV4 incidents cause silent merchant impact, often skip postmortems, and produce no measurable improvement signal.
- Proposal: use AI to summarise postmortems or the Slack resolution thread, estimated to capture ~90% of those signals.
- Maris, recently in role and taking over some of Andy White's tasks, said she does not own incidents and could not see how this fits her goals. She agreed to find the right owner. Andy White still leads that team.

**Reflex demo (production)**
- Pulls both Fin AI conversations and Zendesk human tickets into one aggregated pipeline.
- Tags at the body level rather than relying on taxonomy ticket types, because taxonomy gives a category but not the actual problem.
- Supports drill-down from aggregate theme to individual tickets, with some overlap where a ticket contains two issues.
- Live example: Remittly went live with a large volume of card payouts, doubling weekly ticket volume. All manual review because there is no mechanism yet to answer their queries via AI in email. Reflex shows 22% of card payout issues came from Remittly, in the European region. Card payouts are ~9% of total volume, which Charlie said he would take to the card payouts team.
- Rollout: in beta with a group of PMs, launching to the rest of product by end of month. Company-wide access available. Data will also be pushed so teams can consume it in Looker, including via the Looker MCP, rather than being forced into the app.

**Architecture ask**
- The aggregation pipeline is solved. Adding commercial intake means conforming an external data model to the Reflex schema, which is engineering work.
- Reflex can consume raw text, so call transcripts work if transcribed. Type would become a filter dimension: bug, enhancement, incident, support contact.
- NPS data is also on the list of inputs to unify into Reflex.
- Charlie's repeated framing: solve the input processes first, then aggregation.

**Decisions**
- Aligned: aim to incorporate commercial bug and enhancement requests into the Reflex data pipeline for centralised product insights.

## Insights

- Reflex has a second demand source beyond Care: CPP wants it as the aggregation layer for commercial bug and enhancement intake, incidents and NPS. That expands Reflex from a support insights tool toward a merchant insights platform. The pipeline is reusable; the blocker is input standardisation and a data-model conformance exercise, not Reflex itself.
- The roadmap argument landed with CPP: unplanned work is only unplanned because teams lack this data. Reflex reframes it as roadmap shaping.
- Revenue or GPV at risk is the metadata CPP cares about and Care ticket data does not carry. Adding it would make Reflex themes prioritisable commercially, not just by volume.
- SEV3 and SEV4 incidents are an unowned, uninstrumented signal source with no clear owner. AI summarisation of postmortems or Slack threads is the proposed route.
- Remittly numbers for reuse: doubled weekly ticket volume, 22% of card payout issues, card payouts ~9% of total volume, all handled by manual review. The same Remittly spike appears in the Ling sync, where routing was excluded then reinstated.
- Reflex rollout to all of product is end of September 2026.
- Commercial intake data quality is low by design. Any Reflex integration must not assume reproduction steps or structured product tagging.
