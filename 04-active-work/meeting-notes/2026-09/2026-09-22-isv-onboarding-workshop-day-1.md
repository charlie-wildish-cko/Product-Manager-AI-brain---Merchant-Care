# ISV integration and onboarding workshop, day 1

**Date:** 2026-09-22  
**Attendees:** Milan Jani (likely facilitator), Antonio Vasilev, Arthur Magnes, Brendan Cain, Charlie Wildish, Dasha Rodionova, Georgios Maninis, Gilles Beausseron, Helder Goncalves, Ignas Sakalauskas, Jamie Sims, Joe Zender, Kunal Patel, Mirabel Tay, Stephen Adams, Daria Biryukova, Paula Caicedo, Ayesha Ghoshal, Mark Gossa, Davine Ittoo, Inge Mutsaers, Richard Ding  
**Drive source:** 171rAgNFbBnmCTQEZrqmGz4AOCpnIeNQEmP32VuuWjhM

## Context

First of two 3-hour workshops to build a RICE-scored list of ISV onboarding improvements for Gilles's Q4 planning. Most speakers sit under room LON-06-11, so attribution is limited.

## Key Points

**Baseline**
- Onboarding without human intervention: "1 in 16,000". Gemini's notes give three conflicting figures for the improved state (1 in 4,000, 1 in 14,000, and 1 in 6,000 on day 2). Verify before citing.
- 17 Trouvo applications triggered 85 manual checks (about 5 each, more with multiple UBOs). 13 rejected at source, 5 approved, 3 of those terminated within two weeks for transaction laundering. Mirabel: the platform's referrals were poor, not the system.
- Top risk-team messages to Trouvo: expired driver's licence (14), wrong bank document format (8), missing website disclosures (8, agent policy error now fixed), wrong MCC (6), representative address failure (5).
- 50% of submitted bank statements fail quality checks.
- Sunday benchmark: over 80% success across most buckets (single line of business, single MCC, business model checks waived, years of education).
- A 90% zero-touch pass rate needs about 99% pass rates across all nine check families.
- No system event distinguishes instant onboarding (5-7 minutes) from manual review (24 hours).

**Customer principles (facilitator)**
- Instant, clear feedback. Fast go-live or a clean no with reasons. Clear statuses beyond onboarding. Enough information to run the business without escalations about blocked settlements.
- Internal: cost to serve must not rise with seller accounts.
- "We were solving most things over Slack and our APIs and webhooks didn't have enough fidelity for the customer to have a clue what was going on."

**Dashboard and API gaps**
- New platform dashboard: "action required" entities not surfacing (entity status sync broken). Dashboard statuses differ from API statuses.
- Agent messages to merchants use free-text templates from two years ago that do not match webhook messages. Dropdowns to replace them.
- Three different webhooks for "requirements due", without reason detail. Sunday scrapes the dashboard instead.
- APIs return empty responses or no reason codes for draft entities. Customers fall back to Slack.
- Platforms care most about payment splits and fee breakdowns. Platform fees not fully populated (being fixed with Jason).
- Integration docs: missing headers, no packaged sandbox scenarios, schemas not public.
- Risk assessment checks run async, stateless, no state machine, so merchants get piecemeal requirements.

**Risk architecture**
- Flow: Salesforce opportunity creates entity and invite, onboarding API renders forms, submission goes to RA tool and Galactus, policy engine picks checks, checks pass or return "inconclusive" (no auto-decline), CRA score of 80+ passes, below 80 goes to manual review via Salesforce case.
- Enhanced due diligence is fully manual. Merchant-declared MCCs are often wrong. Declared volumes often annual instead of monthly.
- Mexico team does manual shadow underwriting after go-live, with offboarding 2-4 weeks later if alerts trigger.
- Scale target: 50,000 platform merchants next year.

**Pipeline**
- About 20 platforms to onboard before Easter. By Christmas: Finalsite, Checkout Champ, Zender, Toa Pay.

**Decisions**
- Consumer use cases for the platform for the next six months. Rejections stay manual at first. In-house MCC tool is the source of truth. Enhanced fraud checks move to phase two. Default low-risk MCC list for all customers from the following week.

## Insights

- Platform onboarding support runs over Slack because APIs, webhooks and dashboard lack fidelity. That volume is invisible to Care taxonomy and metrics.
- Inconsistent status language across API, dashboard, webhooks and agent templates drives L2 contacts from platforms. Care content, Fin Procedures and taxonomy need the canonical status names once standardised.
- Sunday vs Trouvo shows platform quality and education drive contact load. The 20 platforms due by Easter will test this.
- No instant-vs-manual review signal feeds "where is my onboarding" contacts.
- Post-go-live offboarding (2-4 weeks) is a Care load that is communicated manually today.
