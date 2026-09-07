# Merchant Care Success Plans

> Original proposal (archived, superseded by this doc): `05-archive/2026/strategies/care-success-plans-proposal.md`
> Status: Being implemented in 2026
>
> **Stripe benchmark**: [stripe.com/support-plans](https://stripe.com/support-plans) — reviewed February 2026. Key gaps identified and mapped below.

## Why it matters

Checkout.com currently applies a one-size-fits-all support model to merchants with fundamentally different needs. A Tier 5 Growth merchant with one developer and low TPV gets the same support experience as a Premium strategic account processing billions annually. This misallocates agent time, frustrates high-value merchants with slow responses, and leaves Growth merchants with an experience that doesn't match their needs or expectations.

Without defined plans, support is reactive and inconsistent. Sales has no structured offering to present; merchants don't know what they're entitled to; agents have no framework for prioritisation. The result is poor CSAT at the top end (where expectations are highest and stakes are greatest) and unnecessary contact volume at the bottom end (where self-service and AI could resolve most queries).

Care Success Plans replace this with a model calibrated to merchant value and needs: highest-touch human support where it matters most commercially, AI and self-service for the long tail. The SLA differentiation also creates a commercial lever — Premium entitlements justify the pricing of Checkout.com's top-tier offering and provide a credible benchmark against Stripe.

## Overview

A support model with four Merchant segments (Essential, Growth, Enterprise, Premium) for B2B merchants, replacing the current one-size-fits-all approach. *("Growth" was previously named "Standard." "Essential" is new — split out from Growth to separate Tier 5+ (no Account Manager) merchants from Tier 3–4 (has an Account Manager), matching the White Glove / Not White Glove boundary defined in `customer-segments.md`.)* Merchant segment is determined by Salesforce CRM fields (Tier, Incentive Rating, SAT designation) and reflects a combination of current net revenue, revenue potential, and strategic brand value. See **Tier Assignment Logic** below for the exact rules.

**These four Care Plan tiers map onto the two primary segments in `customer-segments.md`**: Premium, Enterprise, and Growth are all **White Glove** (have an Account Manager); **Essential** is **Not White Glove** (no Account Manager). White Glove / Not White Glove is the primary segment; "Enterprise" and "SMB" are the commercial/Salesforce-facing names for those two primary segments in `customer-segments.md` — **not** the same thing as the "Enterprise" Care Plan tier below, which is one specific tier *within* White Glove, alongside Premium and Growth. Don't conflate the two uses of "Enterprise" in this document: (1) the commercial name for the whole White Glove segment, and (2) the specific mid tier between Growth and Premium.

This tiering applies uniformly across White Glove's business models — Large Direct merchants, Platforms, and Card Issuing customers are all assigned Essential, Growth, Enterprise, or Premium using the same Salesforce criteria (processing volume and revenue potential). Business model (see `01-knowledge-base/products/customer-segments.md`) determines the shape of the support relationship — direct, intermediated, or specialist-product; Merchant segment (tier) determines the level of service within it. A Platform or Card Issuing customer can sit at any tier, same as a Large Direct merchant — though per the working assumption in `customer-segments.md`, Platform/Card Issuing accounts are treated as White Glove (Premium/Enterprise/Growth) by default until AM-presence data exists for that population in Essential.

The goal is to match or exceed Stripe's support plan model — combining **context-aware resolution** (knowing the merchant's integration and history), **proactive health monitoring**, and a **named technical partner** in the top Merchant segments.

**Scope**: This model covers operational post-sales technical support and escalation handling for acquiring and issuing services. Technical Account Management (TAM), Account Management, and other Commercial teams are out of scope.

## Segment  definitions ( using Salesforce data)

Merchant segment (support plan) is determined by three fields in Salesforce CRM:


| Field                       | Values                   | Meaning                                                                                                                         |
| --------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| **Tier**                    | 1 (highest) → 5 (lowest); Tier 5+ reserved for any future lower tier (e.g. a dedicated SMB Tier 6, not yet defined) | Current net revenue contribution / TPV processed through Checkout. Tier 1–4 merchants have an Account Manager; Tier 5+ does not. |
| **Incentive Rating**        | Gold > Silver > Bronze   | Revenue potential — highest NR potential or best opportunity to increase share of wallet.                                       |
| **Account Owner Territory** | SAT                      | Strategic Account Treatment — brands with high strategic value regardless of current revenue (e.g. Sony, Netflix, Spotify).     |


### Assignment rules


| Support plan   | Salesforce criteria                                                                                                         |
| -------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **Premium**    | Account Owner Territory = `SAT` **or** (Tier = `1` **and** Incentive Rating = `Gold`)                                       |
| **Enterprise** | Tier = `1` (not Gold) **or** Incentive Rating = `Gold` (not Tier 1) **or** (Tier = `2` **and** Incentive Rating = `Silver`) |
| **Growth**   | Incentive Rating = `Bronze` and Tier = `3` or `4` — has an Account Manager                                 |
| **Essential**   | Incentive Rating = `Bronze` and Tier = `5+` (Tier 5 or lower) — no Account Manager                                 |


> **Note**: SAT designation alone qualifies a merchant for Premium regardless of Tier or Incentive Rating, reflecting that strategic brand value is treated as equivalent to top-revenue performance for support purposes.

## Merchant segments

*Premium, Enterprise, and Growth (below) are all White Glove. Essential is Not White Glove. See the Overview above for how this maps to `customer-segments.md`'s primary segment split.*

### Premium

**Salesforce criteria**: Account Owner Territory = `SAT` **or** (Tier = `1` and Incentive Rating = `Gold`)

**Merchant profile**: Highest-revenue merchants (Tier 1, Gold incentive rating) and strategic brands (SAT) regardless of current revenue. Two distinct sub-profiles:

- **High-revenue (Tier 1 / Gold)**: Mission-critical operations, high TPV, zero tolerance for downtime. Mature self-built tooling, heavy API/webhook usage, complex bespoke setups.
- **Strategic (SAT)**: Recognisable consumer brands (e.g. Netflix, Spotify) whose presence has commercial and reputational value beyond current NR. May have lower TPV today but have strong growth or partnership potential. Have a named Account Manager.

Both profiles warrant the highest-touch support model. All Premium merchants have an Account Manager.

**Support needs** (AM/TAM research): Contact Care infrequently, but expect rapid, high-quality resolution when they do. High team churn means they rely on central support systems rather than individual relationships. Self-serve is not expected. Dashboard usage ranges from 5–10 logins/week (biggest TPV accounts) to 50–100/week (smaller Premium accounts, e.g. Careem).

**Examples**: Netflix, Uber, Spotify, eBay, Klarna, Temu, Shein, Ant Financial

**Key benefits**:

- Fastest SLAs
- Named Support Engineer (embedded technical partner)
- Monthly health reviews with optimisation recommendations
- 24×7 staffed coverage
- Dedicated Slack/IM (APAC), email, live chat, video callback
- Context-aware support — agents and AI familiar with integration history and account profile
- Developer-to-developer priority routing (4 developer profiles)
- Real-time merchant health alerts — API alerts + payments performance trends
- Proactive reporting, insights, and custom recommendations
- Critical support for flash sales and peak volume events (preparation, testing, observability, alerting)
- Platform-defined optimisations: connected account verifications, onboarding, payout optimisations (for ISV/Platform merchants)
- API availability reporting

**Channel validation (AM interviews, January 2026)**: Direct AM research on four Premium merchants confirmed the channel design:

| Merchant | Primary support channel | Dashboard? | Primary query types | Channel gap |
| --- | --- | --- | --- | --- |
| eBay | Multiple dedicated Slack channels (AR, dev, P0/P1). Almost never raises Zendesk tickets. | Minimal — deliberate policy | AR drops by BIN/market, invoice reconciliation, proof of settlement, 3DS/compliance | Phone for P1; AM CC on tickets; AI agent responses that avoid directing to dashboard |
| Temu | Proprietary in-house IM (not WeChat — no external integration possible). Support email for reconciliation/disputes. | None — internal compliance block | Webhook status mismatches, AR monitoring, out-of-hours coverage (APAC, after 8pm) | After-hours coverage; accurate webhook data would eliminate most contacts |
| Shein | Email/tickets | None — compliance block on holding cardholder data | APM status/disputes (~60%), Pay to Card RFI (~40%) | APM dispute API; clearing process visibility; no self-serve path |
| Ant Financial | DingTalk/InTalk (proprietary in-house IM, 150-person chat group; no external integration) | Partial — known bug in webhook subscription view | Payment confirmation, webhook misconfiguration, Payback sub-merchant auth failures | IM channel is untrackable; webhook dashboard bug needs fixing |

**Implications**: Dashboard-based self-serve is not viable for this segment — these merchants deliberately bypass it, confirming the dedicated email/Slack/IM/phone channel set. Slack/IM is the primary contact channel for APAC accounts (Temu, Ant) — without it, support effort is invisible and absorbed by AMs. Phone for P1 is validated (eBay's AM reports merchants requesting phone support since she joined; the current line isn't fit for purpose). AM/TAM auto-CC on tickets is confirmed as important — eBay specifically asked for the ability to interject if an AI response is incorrect.

### Enterprise

**Salesforce criteria**: Tier = `1` (not Gold) **or** Incentive Rating = `Gold` (not Tier 1) **or** (Tier = `2` and Incentive Rating = `Silver`)

**Merchant profile**: Three distinct sub-profiles, all with meaningful revenue or growth potential but below the Premium threshold:

- **Tier 1 / non-Gold**: Established high-TPV merchants who don't yet have Gold incentive rating — significant current revenue but lower growth potential or share-of-wallet opportunity than Gold.
- **Gold / non-Tier 1**: High revenue-potential merchants (Gold incentive rating) who are not yet Tier 1 — strong candidates for growing their Checkout share of wallet; may be earlier in their payments journey.
- **Tier 2 / Silver**: Mid-TPV merchants with moderate current revenue and meaningful upside. Growing operations, established payment flows. Have an Account Manager.

All Enterprise merchants have an Account Manager.

**Support needs** (AM/TAM research): Ask repeat, simple support issues, usually about several payments at once. Willing to self-serve in most cases. Dashboard usage: 50–200 logins/week. Low/medium tooling maturity — some in-house tools, but rely on the Dashboard to fill gaps; use Checkout's APIs/webhooks.

**Examples**: eToro, Plus500, Delivery Hero

**Key benefits**:

- Faster SLAs than Growth
- Dedicated channels: live chat, email, video callback
- Named Support Engineer (Phase II)
- Quarterly health reviews — surfacing friction in payment flow with optimisation recommendations (Phase II)
- Context-aware support — agents and AI familiar with integration history and account profile
- Developer-to-developer priority routing (2 developer profiles)
- Real-time merchant health alerts — API alerts + payments performance trends
- Essential optimisations: fraud, disputes, and operational support
- Essential platform optimisations: risk, onboarding, and operational support (for ISV/Platform merchants)

### Growth

**Salesforce criteria**: Incentive Rating = `Bronze` and Tier = `3` or `4`.

**Merchant profile**: Long-tail merchants with lower current revenue and limited growth potential in the near term. Tier 3–4, Bronze incentive rating. Have an Account Manager — White Glove side of the boundary defined in `customer-segments.md` (Not White Glove is Essential, below), despite the baseline entitlement level. Rely primarily on the Dashboard and self-service tooling, with AM support for escalations. Lower payment flow complexity and API usage than higher Merchant segments.

**Support needs** (AM/TAM research, pre-split Standard tier — applies to Growth and Essential alike): Ask a range of simple support issues across the payment lifecycle and Dashboard usage/functionality. Tries to self-serve first. Dashboard usage: 25–50 logins/week. Low tooling maturity — usually no in-house tools, so relies on the Dashboard; API usage is low.

**Key benefits**:

- Reliable baseline SLAs
- AI Agent, webform, live chat (business hours)
- 24×5 staffed coverage (P1 24×7)
- Self-service tools
- Developer-to-developer priority routing (1 developer profile)
- Real-time merchant health alerts — essential API alerts
- Account Manager relationship

### Essential

**Salesforce criteria**: Incentive Rating = `Bronze` and Tier = `5+` (Tier 5 or any lower tier).

**Merchant profile**: Long-tail merchants with the lowest current revenue and limited near-term growth potential. No Account Manager — Not White Glove side of the boundary defined in `customer-segments.md` (commercial name: SMB); support relationship is AI-first and self-service by design, not AM-mediated. Includes small merchants Checkout directly supports as primary Platform/PayFac, and SMB merchants onboarded via a future Tier 5 expansion programme (that acquisition programme is still TBC; Tier 5 merchants already in the book today sit on this plan now). Rely primarily on the Dashboard and self-service tooling. Lower payment flow complexity and API usage than higher Merchant segments.

**Support needs**: See Growth's Support needs above — the underlying AM/TAM research predates the Growth/Essential split and characterised this population (then combined as "Standard") together.

**Why "Tier 5+" and not "Tier 5"**: Tier 5 is the lowest tier Salesforce currently defines. If a dedicated SMB motion gets its own tier (e.g. a future Tier 6, not yet defined), Essential's criteria is written to include it automatically rather than needing another Assignment rules update.

**Key benefits** *(currently identical to Growth — see open question below)*:

- Reliable baseline SLAs
- AI Agent, webform, live chat (business hours)
- 24×5 staffed coverage (P1 24×7)
- Self-service tools
- Developer-to-developer priority routing (1 developer profile)
- Real-time merchant health alerts — essential API alerts

**Notes**:

- Tier 5 expansion / Payfac acquisition programme timing TBC
- May offer premium add-ons (faster SLAs, live chat) for a fee
- Consumer Duty considerations may apply

**Open question — should Essential's entitlements differ from Growth's?** The split from Growth was made on the White Glove / Not White Glove boundary (AM presence), not on SLA/channel need — Essential's Feature Comparison, SLA Matrix, and Channel Entitlement values below are currently carried over unchanged from the pre-split Growth/Standard tier. Not yet decided whether Growth (has an AM) should get materially better SLA/channel entitlements than Essential (no AM), or whether they stay pooled at the same entitlement level with AM being the only differentiator between them.

### B2C Consumer

**Segments**: Remember Me (card-saving product, live today) + Ray (non-custodial stablecoin wallet + USD Visa card; internal launch end Dec 2026, external beta end Q1 2027)

**Remember Me — live today**: Consumers contact support via a webform on the Remember Me portal (card saving feature within Flow). Tickets flow into the **Checkout Consumer** Zendesk brand. Volume is <10 tickets/week. No formal tier structure, AI Agent, or SLA framework yet — this is the seed of the B2C support model.

**Ray and full B2C model — internal Dec 2026 / external beta Q1 2027. Key differences from B2B**:

- AI L1 primary channel (per the Ray Ops & Care manual), escalating to a human L2 queue (KYC, deposit recovery, disputes, account ops, complaints, data rights) and/or BPO overflow
- No phone-channel regulatory mandate — Ray is not a UK-launched banking product and carries no Consumer Duty obligation
- 24/7 follow-the-sun L2 coverage targeted for Public Beta
- Likely requires BPO for first-line contact handling
- SLA within hours: L2 first-response target 24h; complaint ack 24h / resolution 15 calendar days (per the Ray Ops manual, not a statutory FCA DISP requirement since Ray is not UK-launched)
- Complaint handling still exists as a distinct function, but without Consumer Duty/FOS referral rights — the manual's complaint SLAs are operational commitments, not regulatory ones

## Feature Comparison by Merchant segment


| Feature                                   | Essential | Growth             | Enterprise                      | Premium                         |
| ----------------------------------------- | --------- | -------------------- | ------------------------------- | ------------------------------- |
| **AI Agent**                              | 24×7 | 24×7                 | 24×7                            | 24×7                            |
| **Context-aware support**                 | — | —                    | ✅                               | ✅                               |
| **Developer profiles (priority routing)** | 1 | 1                    | 2                               | 4                               |
| **Real-time health alerts**               | Essential API alerts | Essential API alerts | API alerts + performance trends | API alerts + performance trends |
| **Named Support Engineer**                | — | —                    | Phase II                        | ✅                               |
| **Health reviews**                        | — | —                    | Quarterly (Phase II)            | Monthly                         |
| **Proactive reporting & custom insights** | — | —                    | —                               | ✅                               |
| **Flash sale / peak event support**       | — | —                    | —                               | ✅                               |
| **Platform optimisations**                | — | —                    | Essential                       | Custom-defined                  |
| **API availability reporting**            | — | —                    | —                               | ✅                               |
| **Dedicated Slack / IM**                  | — | —                    | —                               | 24×7                            |

*Essential and Growth columns are identical pending the entitlement-differentiation decision flagged above.*


## SLA Matrix


| Priority                            | Definition                                       | Essential | Growth                                  | Enterprise               | Premium                  |
| ----------------------------------- | ------------------------------------------------ | --------- | ----------------------------------------- | ------------------------ | ------------------------ |
| **P0** — Complete outage            | All payments failing                             | FR: 15 mins / Res: 4 hrs | FR: 15 mins / Res: 4 hrs                  | FR: 15 mins / Res: 4 hrs | FR: 15 mins / Res: 4 hrs |
| **P1** — Major functional issue     | Sharp drop in approval rates, missing settlement | FR: 4 hrs / Res: 1 business day | FR: 4 hrs / Res: 1 business day           | FR: 1 hr / Res: 12 hrs   | FR: 30 mins / Res: 8 hrs |
| **P2** — Limited operational impact | Refund failed, password reset                    | FR: 12 hrs / Res: 2 business days | FR: 12 hrs / Res: 2 business days         | FR: 4 hrs / Res: 24 hrs  | FR: 2 hrs / Res: 12 hrs  |
| **P3** — Minimal impact             | Dashboard UI bug, docs question                  | FR: 1 business day / Res: 3 business days | FR: 1 business day / Res: 3 business days | FR: 12 hrs / Res: 48 hrs | FR: 4 hrs / Res: 24 hrs  |


*FR = First Response. All SLAs are first-response commitments.*

> **Stripe comparison**: Stripe's Growth tier has a 6-hour priority email SLA; Premium and Enterprise have 4-hour. Their business-critical response SLA is 15 minutes across all paid tiers. Checkout's SLAs are broadly comparable or stronger.

## Channel Entitlements


| Channel              | Essential | Growth       | Enterprise | Premium   |
| -------------------- | --------- | -------------- | ---------- | --------- |
| AI Agent             | 24×7 | 24×7           | 24×7       | 24×7      |
| Dashboard Webform    | Business hours | Business hours | 24×5       | 24×7      |
| Dedicated Email      | — | —              | —          | 24×7      |
| Live Chat            | Business hours | Business hours | 24×5       | 24×7      |
| Telephone            | P1 only | P1 only        | P1 only    | P1 only   |
| Video Callback       | — | —              | Scheduled  | Scheduled |
| Dedicated Slack / IM | — | —              | —          | 24×7      |


## Phase II Features (FY26)


| Feature                  | Enterprise | Premium |
| ------------------------ | ---------- | ------- |
| Named Support Engineer   | ✅          | ✅       |
| Proactive health reviews | Quarterly  | Monthly |


**Named Support Engineer**: Dedicated technical partner for complex issues and proactive monitoring. Owns high-impact cases — day-to-day tickets handled by pooled support. Equivalent to Stripe's "Technical Account Manager" (TAM).

**Health Reviews**: Data-led reviews surfacing friction in a merchant's payment flow, with optimisation recommendations and optional deep-dive sessions. Stripe offers this at Premium and Enterprise with continuous optimisation and proactive insights.

## Roadmap Dependencies

Several features in the plan depend on 2026 deliverables being live. See `2026 deliverables.md` for full detail.


| Plan Feature                        | Depends On                            | Expected                               |
| ----------------------------------- | ------------------------------------- | -------------------------------------- |
| Context-aware support (agents + AI) | Merchant context for Fin and Agents   | Q1–Q2                                  |
| Real-time health alerts             | Support-based proactive notifications | Uncertain                              |
| Developer-to-developer routing      | Support model enablement              | Q2 (Essential/Growth), Q3 (Enterprise/Premium) |
| Flash sale / peak event support     | Support model + Named Engineer        | Q3+                                    |
| Platform optimisations              | Platform support channels             | Q1                                     |


## Ticket Distribution (2025 baseline)


| Merchant segment | % of tickets | % of merchants |
| ---------------- | ------------ | -------------- |
| Premium          | 31%          | 5%             |
| Enterprise       | 33%          | 20%            |
| Growth + Essential (combined)        | 36%          | 75%            |

*Growth and Essential are shown combined — the 2025 baseline predates the split, so ticket/merchant share isn't yet broken out by AM presence within this population.*


## Problem This Solves

- No defined support plans → inconsistent, ad hoc service experience
- Different merchants offered different channels without a strategic framework
- Merchants unaware of what they're entitled to → misaligned expectations
- One-size-fits-all SLO applied uniformly regardless of Merchant segment or issue priority

## Options Considered

| Option | Pros | Cons | Decision |
| --- | --- | --- | --- |
| 2 tiers (Standard vs Enterprise) | Simple, fewer SKUs | No mid-price step | Rejected — doesn't meet mid-market needs; delta between Enterprise and Standard too large |
| Baseline + à la carte add-ons | Flexible | SKU sprawl, quote fatigue, routing complexity | Rejected — Ops & Commercial overhead |
| Bespoke SOW per large client | Tailored | Legal overhead, no economies of scale | Rejected — not scalable |
| Tiered ladder (current model) | Smooth upgrade path, matches competitors | Adds SKUs to catalogue | Recommended and adopted |

## Key Risks


| Risk                                        | Mitigation                                                                                    |
| ------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Internal misalignment on entitlements       | Cross-functional enablement pack + mandatory training for frontline teams                     |
| Merchant perception as a downgrade          | Proactive comms emphasising enhancements; grandfather existing expectations where appropriate |
| SKU/catalogue friction for Sales            | Include plans in all commercial proposals with pricing logic                                  |
| Essential (Not White Glove) Merchant segment feels underserved | Continue self-service and AI investment; monitor CSAT/NPS across all Merchant segments        |


## Competitor Benchmark


| Feature                       | Stripe                                                  | Adyen                                                               | Worldpay                   | Checkout.com (target)                                        |
| ----------------------------- | ------------------------------------------------------- | ------------------------------------------------------------------- | -------------------------- | ------------------------------------------------------------ |
| **Support tiers**             | 4 (Standard + Growth + Premium + Enterprise)            | Account-led; platform merchants have mandated 3-tier internal model | Merchant-type segmentation | 4 Merchant segments (Essential / Growth / Enterprise / Premium) — note: Stripe's own "Growth" tier (left) is a different tier from Checkout's Growth (formerly Standard); naming overlap is coincidental        |
| **Named TAM / Engineer**      | Scaled TAM (Premium), embedded TAM (Enterprise)         | Account Manager for escalations                                     | Account Manager            | Named Support Engineer (Phase II, Enterprise+)               |
| **Context-aware support**     | ✅ Growth+ — agents know your integration history        | —                                                                   | —                          | ✅ Q1 via Merchant 360 context                                |
| **Developer routing**         | 1–4 developer profiles by tier                          | —                                                                   | —                          | 1–4 developer profiles by Merchant segment (target)          |
| **Health alerts**             | API alerts (all tiers); + performance trends (Premium+) | Webhooks (merchant-managed)                                         | —                          | Proactive notifications (roadmap)                            |
| **Health reviews**            | Continuous (Premium+), custom (Enterprise)              | —                                                                   | —                          | Quarterly (Enterprise) / Monthly (Premium)                   |
| **Flash sale / peak support** | ✅ Enterprise only                                       | —                                                                   | ✅ High-TPS gaming vertical | ✅ Premium (target)                                           |
| **Dedicated Slack**           | ✅ Enterprise only                                       | —                                                                   | —                          | ✅ Premium                                                    |
| **Live Chat**                 | ✅ All customers 24/7                                    | —                                                                   | —                          | Business hours (Essential/Growth); 24×5 (Enterprise); 24×7 (Premium) |
| **Phone**                     | ✅ All customers 24/7                                    | Critical only                                                       | ✅ 24/7 multiple lines      | P1 all Merchant segments                                     |
| **Platform optimisations**    | ✅ Premium+                                              | Mandated on platform                                                | —                          | Q1 (ISV identification); full optimisations Phase II         |
| **Monetised premium tier**    | ✅ (subscription / contract)                             | Contract-based                                                      | Bespoke                    | Bespoke / minimum billing                                    |


**Target**: Match Stripe's Growth tier at our Enterprise level; match Stripe's Premium/Enterprise at our Premium level. Key Checkout differentiators to maintain: video callback, stronger SLAs at Premium, and proactive health reviews at Enterprise (Stripe only offers this at Premium+).

**Last Updated**: February 2026
**Owner**: Charlie Wildish
**Source**: `05-archive/2026/strategies/care-success-plans-proposal.md` (original proposal, archived) + [stripe.com/support-plans](https://stripe.com/support-plans)