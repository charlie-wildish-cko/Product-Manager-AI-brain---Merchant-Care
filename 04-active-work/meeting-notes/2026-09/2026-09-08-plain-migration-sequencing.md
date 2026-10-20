# Ajay / Charlie - Plain migration sequencing

**Date:** 2026-09-08
**Attendees:** Charlie Wildish, Ajay Paul
**Drive source:** 15U6A2sfkRbQQm7FLWDvEZYFoz7Lwnwy5p4lR6qEuFIE

## Context

Handover-driven session on how the Plain migration should be sequenced, plus the demo Charlie needs for Jenny. Ajay has resigned and is in a two-month handover.

## Key Points

**Ajay's departure**
- Joining Quanto, a French payment services company serving freelancers and small businesses (possibly a Checkout IDV client). Relocating to Paris or Barcelona. Two-month handover. Anna had not been told yet, being on holiday.

**Demo for Jenny**
- Charlie wants a short clipped demo video for the following Monday, reusing the existing 1.5-hour Ops session recording.
- Focus on the Plain ticketing UI, working a ticket, and how it handles described use cases including escalations. Not GitHub, not code.
- Ajay clips, Charlie does voiceover and edit.

**Migration approach**
- Both rejected lift-and-shift: much of the Zendesk build and config consists of workarounds for Zendesk's native limitations, plus SweetHawk dependencies that can be binned. Plain's native Jira integration helps.
- Sequencing: migrate API channels in Plain first, staff the team for those, then move email all in one go and reroute email forwarding away from Zendesk.
- Rationale for the single email cutover: the previous email setup required an allowlist of merchant email domains mapped to tiers, which was locked in and never updated, so tier changes or new users dropped into dispatch.

**Requirements ownership**
- Charlie does not want the Ops team dictating long-term requirements: they think well tactically but create bad downstream consequences and add edge cases. Joel is better placed to decide what is actually needed.
- Framing should be outcome-first ("what are you trying to achieve") rather than replicating existing flows. The same view exists in OE.

**Upcoming in-person week**
- Ops and technical teams visit next week while Ajay is on leave. Charlie wants conceptual migration discussion only, no locked dates, because nothing has been signed off.
- Wants James's and Eric's views on migration approach. Anna was going to pull James into a session.

**Open gaps**
- Ticket transfers remain unresolved. Charlie sent Plain a detailed document on ticket transfer options for James to review. Plain suggested other multi-team customers use Slack threads and swarming, which Charlie is wary of: it would require changing other teams' ways of working, and creating tickets from Slack threads via email produces unstructured, poorly transferred information.
- The Plain Slack app install is stalled with InfoSec on a Jira ticket. Production access is unnecessary; a QA Slack workspace would be enough for end-to-end testing.

**Decisions**
- Reject lift-and-shift. Migrate API channels first, then email in a single cutover rather than incrementally.

## Insights

- The migration sequencing rationale is documented here: API channels first, then a single email cutover. The reason is the failed tier-mapped email domain allowlist, which is the concrete evidence against incremental email migration.
- Requirements ownership is a live political question. Charlie's position: Joel, not the Ops team, defines future-state requirements, and outcomes rather than existing flows are the unit of requirement.
- Nothing is signed off as of 2026-09-08. Any downstream doc asserting Plain migration dates is ahead of reality.
- Ajay's departure removes the Zendesk admin depth ahead of the migration, with the two-month handover window starting now.
- Ticket transfer design is the biggest unresolved functional gap, and Plain's suggested Slack-swarming pattern has been implicitly rejected.
