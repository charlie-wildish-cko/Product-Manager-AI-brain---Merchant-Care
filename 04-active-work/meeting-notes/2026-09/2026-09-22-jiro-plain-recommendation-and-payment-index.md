# Jiro / Charlie: Plain recommendation, payment index, email auth

**Date:** 2026-09-22  
**Attendees:** Charlie Wildish, Jiro Farah (Zendesk admin / engineer)  
**Drive source:** 1lbTf1K65R1z1syOh2ItEy-qxpx5gKGnBrngkE_ygMi0

## Context

About 60-minute working session covering the support platform recommendation, data access for Fin, and team and org changes. Gemini transcribes Plain as "Plane" and Meron (CPO) as "Moron".

## Key Points

**Recommendation timeline**
- Recommendation document goes out the following week. Decision session pencilled for 8 October with Meron (CPO) and Jenny.
- Zilch reference was very positive about Intercom, but in a pure B2C context.

**Plain vs Intercom**
- Core features (channels, agent experience, help desk) are about even. The decision comes down to AI:
  - Machine users, not seen at any other vendor.
  - Plain is unopinionated about integrations and supports bring-your-own-agent and Sidekick. Intercom makes BYO hard and requires marketplace approval.
  - Intercom Copilot has no custom API integrations and no timeline for them.
- Plain SLA policies have launched. Total resolution SLAs expected this month. Routing and API-based transfer workarounds still need defining.
- Plain references: largest is xAI (Grok team), 150+ members.
- Pylon only added BYO agent in July.

**Pricing**
- All vendors within about $10-15 per seat. Vendors earn on add-ons.
- Intercom basic plus Copilot: $150-160 per agent before discount (most expensive). Plain: $130 per agent plus Sidekick credits.
- Credits need estimating per ticket, assuming Sidekick or BYO agent runs on all non-Fin tickets. This is Plain's likely long-term revenue lever.
- Seat assumption about 100, based on current Zendesk seats. Could be lower.
- Plain has a rate limit but no API request cap. Zendesk's is about 2,000/hour and has caused problems (to double-check).
- Build in-house (raised by Meron) rejected: only worth it at hundreds of thousands of contacts a week with a dedicated team.

**Platform design points**
- Salesforce: case audit trails need bi-directional sync. Email-based sync is unreliable.
- Back-office tickets: Plain needs a dummy user so non-customer-initiated tickets do not notify customers. Jiro proposed one catch-all user.
- Help centre: excluded from vendor requirements to avoid lock-in. Build on the existing repo, like docs and API reference. Needed only when Zendesk migrates, not for Ray at first.
- Historical Zendesk tickets: options are migrate, keep view-only, or sync to BigQuery. Zendesk supports setting a starting ticket ID to avoid clashes.
- Plain feature needs: custom permissions and roles, workspace token split. Tracked in a Notion list.

**Payment index**
- Federico's team is building it. Accepts payment ID, ARN, RRN or reference. Returns payment type (card payout, bank payout, pay-in, unreferenced refund) and the BigQuery table/query.
- Schema clear enough for AI agents without complex prompts. InfoSec approved data sharing in principle.

**Email data sharing and auth**
- Jiro raised the Revolut incident (data sent to someone posing as an authority).
- Charlie: low-risk payment metadata (status, no identifiable person) is fine to share. Balances and settlements are more sensitive. Asking email users to log in is impractical.
- Needs delegated tokens or user validation before calling internal APIs. Jiro to consult Identity Services. Pragia is writing an authentication discovery doc.

**Fin goal**
- Target: Fin resolving 40% by end of year. Drivers: move web form volume to Fin (Pragia), then email integration, then chat buttons triggering payment ID lookups.
- Javad's customer bot performs better than expected but needs tuning and observability.

**Org changes**
- Former Zilch CPO joined Milan's team as senior director for Platforms and SMB experience.
- Fraser now reports to Helder. Andre moved into Adrian's role. Steven back in the pillar with 17 reports. Kunal leaving. Rumour that Retool is being phased out company-wide.
- Ray external launch still "sometime in Q1". Care milestones unchanged.

**ISV onboarding (from workshop)**
- Status not shown clearly, API cannot return what platforms need and does not match the Dashboard, too many manual checks.

**Internal support**
- Unmonitored tickets in the internal support channel. Jiro plans to move internal forms from Retool to Reflex.
- Help centre footer needs a new AML number by end of week (legal request).

## Insights

- Plain's differentiation is AI extensibility (machine users, BYO agent, open integrations). Seat price is not a differentiator. The cost risk is Sidekick credit consumption on non-Fin tickets.
- Decision session: 8 October.
- The 40% end-of-year Fin resolution target depends on web form migration and email integration.
- The payment index is the key enabler for Fin Procedures and Agent Consultant lookups.
- Email auth (delegated tokens) is the blocker for sharing payment data on the email channel.
- Help centre stays vendor-independent, built on the existing content repo.
