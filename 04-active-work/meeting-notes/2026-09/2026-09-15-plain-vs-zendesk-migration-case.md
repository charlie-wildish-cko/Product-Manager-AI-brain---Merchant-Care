# Plain vs Zendesk: The Migration Case

**Date:** 2026-09-15
**Attendees:** Karan Jagmohansing, Ashvin Pudaruth, Fraser Bryant, Ana Cachapa Cuomo, Joanie Vencatasamy, Charlie Wildish, Francisco Goncalves, Ling Wong, Harlie Patel, Joel Petrosino
**Drive source:** 1YWpSEfWrTYs7pLQHedHSpdps6a4nWE_19zB00rlkl-U

## Context

Introduces the 2027 Care team restructure alongside the Plain migration and sets out the case for leaving Zendesk. Precursor to a detailed session the following day. ~71 minutes.

## Key Points

**Team restructure**

- Diagnosis: Zendesk customisation and reduced dependencies did not deliver, because generalist agents handling everything cannot retain knowledge, be trained effectively, or hit SLAs.
- Proposal: move L1 from generalists to **product specialists in pods, mirroring L2**. Claimed benefits: narrower agent scope, L1/L2 parity, ticket swarming, better AHT, SLA, merchant experience, knowledge retention.
- Four complexity tiers: (1) dashboard inquiries and communications, low complexity, no resolver dependency; (2) transactions and refunds, cross-payment-method, log tracing, refund resolution; (3) financial, fee inquiries through reconciliation mismatches and invoices; (4) high-complexity platforms, APIs, plugins, e-commerce, tricky authentication, acceptance rates, also high volume.
- Agents keep a core specialisation plus secondary product attachments as backup, with fallback routing on queue imbalance. Everyone retains a generalist foundation: the minimum bar is that every agent can troubleshoot a transaction.
- Oliver's challenge: if Fin progressively absorbs simple queries, why the major structural change? Counter: Fin removes the easy wins and leaves residual cases needing deep product and API understanding. Resolution: an agent career journey through groups of increasing complexity, admin to transactions to coding-level.
- Oliver also pushed for a ranked skills matrix rather than knowledge silos, and a single source of truth on terminology, citing past settlement-vs-payout confusion.
- Follow-the-sun weekdays via Mauritius, AAC (5 people across L1/L2 covering 02:00-05:00 GMT) and Mexico, targeting 24/7. Weekends stay generalist: ~10 out-of-hours staff on rotation.
- Separate OKRs and scorecards per pod, because volumes, products and shift patterns are not comparable.
- **Headcount: started the year at 37, expected to close at 31 including Fin improvements. Conservative target set at 35** to absorb higher-than-expected volume and added scope (wallet, Remember Me). A properly staffed 24/7 operation would need closer to **48**.
- Quality reviews mapped per pod (transactions/refunds to gateway and fraud detection; payouts to financial; APIs/plugins to integrations). Complaints and IDV take precedence over pod assignment due to Salesforce limitations.
- Queue mechanics: specialised cases assigned by skill, with automated rules dropping the skill after N hours so the ticket falls through to the general queue before SLA breach.

**SMB and consumer**

- SMB merchants (~500k processing, free tier): a single support ticket can erase the margin and make the account loss-making. AI by default, human support by exception only, strict cost-benefit on escalation, dedicated UX designed by Milan's incoming team from Zil.
- Three customer categories going forward: existing merchants (human support retained, improving over time), SMB (AI default), consumer (AI default).
- SMB taxonomy expected to be broadly the same as today since the business model is not changing.

**Volume forecasting**

- Charlie's start-of-year forecast covers all customer and volume types over several years. B2B volume driven by TPV and customer segments. Ray (formerly Braavos) modelled with the same customer count assumptions. Consumer volume scales steeply with user growth.
- Current base ~2,300 merchants. At 100,000 merchants the volume picture changes fundamentally, which is why technology control, flexibility and velocity matter.
- A new data scientist joins next month.

**The case against Zendesk (six criteria)**

1. **AI.** Zendesk's April decision to cut off third-party AI integrations in favour of its own. Decision made not to use any Zendesk AI: it was duplicative (Procedures had to be authored separately from the Help Centre rather than reading from it). Pricing cited at roughly 2 to 3 per resolution, high for the market. A 20-year-old human-first platform being re-architected for AI is the wrong starting point.
2. **Channels.** Must support current and future channels: WeChat, phone, custom channels.
3. **Integration.** Accessible APIs, unopinionated data ingestion, integration marketplace, smooth work transfer between teams, freedom to plug in in-house or vendor AI agents.
4. **Architecture.** Core services (customer enrichment, taxonomy, product catalogue sync, custom channels, content sources) owned in-house and pushed to the vendor, making the vendor a recipient. Today Zendesk houses things like taxonomy. Jiro proposed forking the Tech Docs stack from GitHub to rebuild the support site, removing vendor dependency on the help centre.
5. **Deploy as code.** Zendesk work is all UI-based via STO, which is fragile, plus a paid third-party tool for what Zendesk does not support. Code deployment increases velocity and makes it easier for the team to use tools like Claude.
6. **Long-term partner.** A vendor that can grow with Checkout over several years.

- Also cited: poor analytics and data modelling, and an unresponsive account relationship (Checkout is not a big customer for them).
- Charlie's structural objection to Zendesk and Salesforce: platforms big enough to spawn a specialist labour market create expensive, niche, lock-in dependencies.
- Ashvin challenged: Care moved from Salesforce to Zendesk for specific reasons. Has the same due diligence been done this time?

**Other**

- Revolut as benchmark: in-house AI agent built from scratch with ~300 engineers, very sophisticated, handles most tasks, and deliberately makes reaching a human hard or paid. Only recently subject to FCA obligations. Max wants a concierge tier for a specific crypto club, implying basic and premium consumer segments.
- Translation: Arabic and Portuguese needed. Today translation is manually triggered by agents inbound and outbound. Option discussed: an AI skill preserving technical terminology, at a credit cost. Marketing is building a centralised terminology repository. Hardcoding terms by customer attribute taken away for review.
- Community: one-to-many webinars (David saw 30 attendees on an integrations webinar) as SMB ticket reduction. A self-owned site removes Zendesk's video-hosting restrictions.
- Telemetry: Heap tracks user metrics and can be searched by client/user logs if actions are defined. Dashboard user activity logs already track events like account admin changes.

## Decisions

- Reorganise L1 into specialised pods by issue complexity, timed with the Plain migration.
- Implement follow-the-sun weekday coverage.
- Use no Zendesk AI features.
- Own all core architecture services in-house; vendors become recipients.
- Build the support site by forking the Tech Docs stack and GitHub codebase.
- Open: hardcoded translation terms by customer attribute, marketing reviewing.

## Insights

- The restructure and the Plain migration are deliberately coupled. The pod model depends on Plain's API-first routing, programmatic skill management (training platform scores auto-assigning and removing skills) and override/fallback mechanisms. Zendesk's static groups cannot express it.
- The Fin-versus-specialisation tension now has an answer on the record: **AI raises the average complexity of what reaches humans**, so automation strengthens rather than weakens the case for deep specialisation.
- The headcount arithmetic is the commercial case: 35 instead of 48 is a ~13-person saving predicated on Fin delivering.
- SMB unit economics are a hard constraint driving AI-by-default, not a preference. One human ticket on a free-tier 500k-processing merchant is loss-making.
- The durable decision is the architecture principle: own enrichment, taxonomy, product catalogue and content, and treat the platform as a recipient. It survives any future vendor change and is the real answer to lock-in, independent of whether Plain wins.
