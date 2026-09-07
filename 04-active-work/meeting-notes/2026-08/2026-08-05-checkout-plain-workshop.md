# Checkout / Plain workshop

**Date:** 2026-08-05
**Attendees:** Ana Cachapa Cuomo, Fraser Bryant, Ajay Paul, Charlie Wildish, Joel Petrosino (Checkout); Eric Weiss, James Amey (Plain)
**Drive source:** 1hTeMPrndkKgF-0arWzGciJMb1AmV6qYodfxvlJe2SfA

## Context

Regular working session with Plain covering feature gaps against Checkout's current Zendesk workflows, Plain's roadmap, and SLA mechanics. Relevant to the Zendesk platform decision RFC.

## Key Points

**Side conversations and snippets**

- Checkout's current Zendesk pattern pre-populates the recipient email and a template (e.g. contacting PSPs, transfer-external). Sandbox templates omit real addresses so tests do not fire real emails.
- Checkout wants the equivalent in Plain: easy target selection, pre-filled email, template with variables such as transaction ID. Confirmed third-party replies land back in the same side conversation and reopen it.
- Plain's read: extending snippets into discussions is easy. The hard part is making a snippet populate the recipient email field. Workaround: put the address as the first line of the snippet body for copy-paste, since an agent cannot send a discussion without filling the field anyway.

**Plain roadmap, all shipping by end of October**

- Merging companies and tenants
- Bringing the standalone Slack broadcast app into Plain with Slack and email support (enables mass comms and audience building from within Plain)
- Workflows
- Custom dashboards
- Multiple business hours
- Improved importers
- Better support for internal support tickets
- External reporting integration
- Custom thread statuses scoped for Q4, described as a very common request

**Plain product philosophy shift**

Build primitives, stop having product opinions. Consequences: SLAs are being pulled out of tiers and moved into workflows; custom statuses arrive; tenants become the single organisational object; every primitive gets simplified so customers decide usage.

**SLA timer mechanics as they stand today**

| Status | Effect on SLA timer |
|---|---|
| Done | Fulfils the SLA |
| Waiting for customer | Fulfils / stops the SLA |
| Pause for later | Does NOT stop the timer, it keeps ticking |
| Any to-do status (needs first response, next response, investigating, close the loop) | Timer keeps running |

- Icons for these statuses are visually very close, which caused confusion in the meeting.
- With "only applies during business hours" enabled, the timer stops at business-hours close and resumes at open. SLA settings stay the same after the tier removal, they just will not live inside tiers.
- Checkout confirmed its SLAs are a mixture of business-hours and calendar-hours, with complaints a likely calendar-hours case. Nobody could recall the exact split.

**Slack discussions**

New to Checkout. "Ask your team" creates a discussion in Slack or email from the thread and maps it onto the ticket timeline. Pre-existing Slack escalations can be pulled in by pasting the Slack URL. Flagged as relevant to QA.

**Working relationship**

- Checkout is happy with cadence, organisation, and Plain's responsiveness, and does not feel context-overloaded. Both sides want the workshops made more regular.
- Checkout expects a high volume of operations and access questions from ops, and will design internally how to funnel them.
- A Checkout team lead in Mauritius signed up for his own Plain workspace via the free-trial flow after hearing about it internally. Plain flagged it and offered to pull him into the main workspace.

## Insights

- Plain's Q4 roadmap resolves several likely blockers for a Zendesk replacement in one release window: custom statuses, SLAs in workflows, multiple business hours, mass comms, external reporting. Any Plain feature-gap assessment against Zendesk should re-baseline after end of October rather than on current state.
- Current SLA behaviour has a trap worth documenting: "pause for later" does not pause the SLA timer, and the status icons are near-identical. That is an agent-error and SLA-breach risk on any Plain pilot.
- Slack discussions plus URL-pasting gives timeline capture of escalations that currently happen off-ticket in Slack. Directly useful for QA completeness, where BigQuery transcripts plus side conversations are the scoring input.
- Staff are finding and signing up for Plain independently. That is both an access-governance issue and evidence of pull from ops.
