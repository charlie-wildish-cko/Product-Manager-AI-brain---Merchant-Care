# Charlie / Ling - monthly sync

**Date:** 2026-09-08
**Attendees:** Charlie Wildish, Ling Wong
**Drive source:** 13TI9S5KkSVgGhdraM3liO4HwbHRlPUpCX0nhPjvIDGo

## Context

Monthly sync on the WeCom/Slack channel expansion, and on why Mauritius is breaching SLA despite having capacity.

## Key Points

**WeCom / WeChat**
- Integrating WeCom requires a user identification workflow agreed with the commercial team to satisfy InfoSec requirements. Epha (Charlie's team, with prior implementation experience) previously evaluated options including one-to-one conversations with sync back to groups.
- Charlie argued against agent participation in group chats: it creates endless, never-closing tickets. Preferred model is one-to-one, with each new request starting a new ticket lifecycle. Ling agreed commercial has to decide whether to accept that limitation.
- Security driver: InfoSec requirements forced WeChat prioritisation. Named trigger: Christos applying for a phone plus a Telegram data breach was the tipping point for Ashin to push the changes.
- WeChat integration is officially scheduled for next year.

**Slack**
- Would be enterprise-only. Technically simpler than WeChat because Slack exposes email addresses that can be matched to dashboard accounts, whereas WeChat requires mapping IDs to merchant accounts in Salesforce.
- Charlie questioned whether Care needs Slack at all, since tier-1 merchants go via TAMs and AMs. Ling pushed back: in Asian markets AMs lean heavily on Care for accounts with no dedicated TAM.
- Still under evaluation.

**Mauritius backlog**
- Janie and the Mauritius team were bogged down by queues driven by a Remittly volume spike. Remittly routing was temporarily excluded, then reinstated once volume subsided.
- Tickets still breach SLA because of slow pickup, not slow handling.
- Shift patterns are heavily staggered, bulk starting 07:00-09:00, leaving thin cover when UK volume is still high. Excessive shift patterns complicate training and create messy multi-agent handoffs where no one owns a ticket end to end.
- Night shift staff get three consecutive days off, cutting monthly working days from the standard 20-22 to ~16-17.
- Capacity maths: 53-55% of contacts arrive 08:00-16:00 local (06:00-14:00 UTC). At 30 minute AHT, roughly 12 agents are needed at peak. Weekday data shows overstaffing in some hours; weekends match the 12-agent requirement.
- Carolina's report from a Mauritius trip criticised unsustainable reliance on a few "hero" agents rescuing breaching SLAs.

**Efficiency**
- 30 minute median AHT is judged too high and varies widely by individual. Target is 20 minutes.
- During the payout spike Ling worked payout tickets without Alfred or Retool and cleared 5-8 per hour, against standard analysts at 2-3 per hour. Diagnosis: overthinking and tool proliferation, not workload.
- MCP for Looker is intended to auto-aggregate payout and pay-in data so agents stop searching multiple tools.
- Oliver is building basic tooling to match ticket volume against headcount.

**Decisions**
- Aligned: force stricter Mauritius shift patterns and reduce the number of varied shift start times.
- Proposed, not decided: backfill headcount in Mexico to absorb Mauritius night shifts, freeing Mauritius staff onto day shifts. Also move some staff to a Wednesday-Sunday week for weekend cover.

## Insights

- The Mauritius SLA problem is a scheduling and pickup problem, not a capacity problem. Volume is concentrated 06:00-14:00 UTC (53-55%) while headcount is spread across too many start times.
- AHT is the lever with the clearest evidence: the same tickets took 5-8 per hour with fewer tools versus 2-3 per hour with the full toolset. That is an observed data point, not a projection, and a direct argument for Agent Consultant and MCP-for-Looker consolidation.
- Channel strategy has a hard security gate: no WeCom or WeChat without a user identification workflow. Group chat is being deliberately rejected on ticket-lifecycle grounds.
- Slack-versus-WeChat priority is contested by region. Asian AM behaviour means Care demand does not disappear just because merchants are tier 1.
