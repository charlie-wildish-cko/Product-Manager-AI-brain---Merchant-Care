# Perrin / Charlie — Customer Data Fragmentation

**Date:** 2026-06-10  
**Attendees:** Charlie Wildish, Perrin Heyka (Account Manager)  
**Drive source:** 1qzhe2qvXKkUDZfbjwzW6wFXmq2aeDN7ez0H3Y9CQlmA

## Context

AM perspective on cross-team data fragmentation and customer communications for Charlie's proposal to product leadership on a unified customer layer.

## Key Points

- Biggest cross-team friction point: Care ↔ Disputes handoffs. Merchants (e.g. One Finance, Pay Near Me) get bounced between teams and lose track of which thread to follow.
- Technical issues escalate through AMs because merchants don't contact technical teams directly. Care's handling quality has improved 2022–2026, but cross-team handoffs remain fragmented.
- Internal periodic reviews are painful: compliance/financial review teams don't talk to each other; AMs act as bridges. Documents that already exist (e.g. Pay Near Me financials) get re-requested because there is no shared repository.
- Salesforce stores primary/secondary contacts but has no standardised "disputes manager" field. Contact knowledge lives in AMs' heads.
- ~50% of people contacting support have no dashboard account — blocks self-service and authentication.
- Dashboard user creation requires the merchant's account admin — AMs cannot add users themselves.

**Communication targeting fix**
- Decision: target account admins rather than individual users for dashboard adoption. Instead of emailing a repeat support sender, email the admin to get them provisioned. Charlie plans to adjust July comms using this approach.
- Long-term: merchant self-service notification preferences in the dashboard (only works once dashboard adoption is driven first).

**Perrin's proposal**
- Dashboard-based consent checklist: merchant opts in to comms types → auto-updates Salesforce. Elegant self-service model worth capturing.

## Insights

- The 50% no-dashboard-record figure is a live data point — directly impacts ability to authenticate and automate support.
- Support handoffs to AMs happen without context. Perrin's ask is for a Slack ping or ticket tag before the email lands, e.g. "this merchant may not have network tokens enabled." Low-cost product improvement.
- AM bandwidth is currently filling the gap between fragmented systems — this will not scale at SMB volumes.
- Charlie is building a pitch for product leadership to fund a solution for cross-team data fragmentation and unified communications. This session is part of that evidence gathering.
