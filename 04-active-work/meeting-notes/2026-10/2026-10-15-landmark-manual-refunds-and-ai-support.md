# Andy / Charlie - Landmark and AI support

**Date:** 2026-10-15  
**Attendees:** Charlie Wildish, Andy Soh (merchant-facing, Dubai), Harlie Patel (Care, listener). Joel Petrosino invited, did not attend. Gemini misattributes some of Andy's lines to Harlie.  
**Drive source:** 1yWULuo0rFbdfpY9PLcps2-6LFvfACGnQBUu7fRZQHgI

## Context

Andy spoke to Landmark's contact the same day. Landmark wants written clarity on what changed with AI support. The meeting aligned the message and surfaced Landmark's wider product gaps.

## Key Points

**Manual refunds and routing**
- Most Landmark support requests are manual refund requests.
- Manual refund requests auto-escalate to the Care team on all channels (dashboard and email). The merchant gets a "we're passing this through" message, with no AI reply.
- Trigger: the merchant says "manual refund" or shares a CSV/spreadsheet of refunds. A generic "check refund status of X" is not escalated and Fin tries to answer it.
- No standardised manual refund template exists. Andy is collecting regional templates via Partnerships. This is why merchants, humans and AI all struggle.
- Harlie is optimising the manual refund process now. Care plans to automate it fully next year: the AI agent takes IDs/files, processes them and confirms completion, with humans in the loop where it cannot.

**Acceptance rate and dashboard gaps**
- Landmark has the performance tooling on. Andy sees uplift "close to zero".
- The dashboard analytics assistant is owned by other teams, not Care. Andy reproduced it breaking and replying that it cannot generate data. Feedback goes to the dashboard PM (Joseph El Choueiri).
- Biggest pain: no automated alert when acceptance rate drops below a threshold. Landmark uses cron jobs, and TAMs monitor manually (one TAM is 4 hours offset).
- The notification feature is a beta under Settings > Notifications, set per individual user only. Super merchants, Merchant Config and Care cannot set or see merchant notifications.
- Andy proposed an "impersonate" mode: read-only view of a merchant account, banner shown, sensitive data masked. Charlie has raised the same with the dashboard team. Care has "super user" with limited visibility.

**Escalation and channels**
- Charlie does not want to auto-escalate all acceptance rate issues, as that bypasses self-serve. Merchants reach a human by asking, or by answering "no" to "does this help?". Charlie asked to be told of cases where this fails.
- Once a human takes over a conversation it does not return to AI.
- Andy: email is too slow for enterprise incidents and wants live chat that creates tickets. Charlie: email cannot be switched off, so both run in parallel. Strategy: every contact passes through AI triage so it is classified and routed by urgency even when unsolved.
- Disabling AI for a merchant needs approval (usually declined). Charlie wants to understand the merchant's goal and confirm they know a human is reachable.

**SMB**
- SMB rollout expected next year, selective (Andy: 1 to 1.5 years).
- SMB will require dashboard login to raise any request, no email. Email persists for enterprise and may shrink.
- Charlie: "We can't afford support the way we do today." Human support must get harder to reach for SMB. Andy suggested paid tiers (SMB Light / Pro).

**AI quality**
- Andy: internal staff often copy-paste AI answers without validating, and the AI sometimes hallucinates. He frames it as a process problem, not a feature problem.

## Insights

- Landmark's real unmet need is proactive acceptance-rate-drop alerting, owned by dashboard/payments product, not Care.
- Notification gaps (user-level only, beta, invisible to Care) are a cross-team gap.
- Manual refunds are the dominant contact driver for this merchant. Full automation is targeted for 2027.
- Read-only impersonation for Care is a recurring ask.
- SMB direction is dashboard-only, AI-first, with harder access to humans and possible paid tiers.
- Risk: internal staff pass unvalidated AI output to merchants.
