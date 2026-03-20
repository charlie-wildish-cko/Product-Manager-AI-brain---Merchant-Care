# Merchant Care Success Plans

> Source document: `01-knowledge-base/strategy/care-success-plans-proposal.md`
> Status: Being implemented in 2026
>
> **Stripe benchmark**: [stripe.com/support-plans](https://stripe.com/support-plans) — reviewed February 2026. Key gaps identified and mapped below.

## Why it matters

Checkout.com currently applies a one-size-fits-all support model to merchants with fundamentally different needs. A Tier 5 Standard merchant with one developer and low TPV gets the same support experience as a Premium strategic account processing billions annually. This misallocates agent time, frustrates high-value merchants with slow responses, and leaves standard merchants with an experience that doesn't match their needs or expectations.

Without defined plans, support is reactive and inconsistent. Sales has no structured offering to present; merchants don't know what they're entitled to; agents have no framework for prioritisation. The result is poor CSAT at the top end (where expectations are highest and stakes are greatest) and unnecessary contact volume at the bottom end (where self-service and AI could resolve most queries).

Care Success Plans replace this with a model calibrated to merchant value and needs: highest-touch human support where it matters most commercially, AI and self-service for the long tail. The SLA differentiation also creates a commercial lever — Premium entitlements justify the pricing of Checkout.com's top-tier offering and provide a credible benchmark against Stripe.

## Overview

A support model with three Merchant segments (Standard, Enterprise, Premium) for B2B merchants, replacing the current one-size-fits-all approach. Merchant segment is determined by Salesforce CRM fields (Tier, Incentive Rating, SAT designation) and reflects a combination of current net revenue, revenue potential, and strategic brand value. See **Tier Assignment Logic** below for the exact rules.

The goal is to match or exceed Stripe's support plan model — combining **context-aware resolution** (knowing the merchant's integration and history), **proactive health monitoring**, and a **named technical partner** in the top Merchant segments.

## Segment  definitions ( using Salesforce data)

Merchant segment (support plan) is determined by three fields in Salesforce CRM:


| Field                       | Values                   | Meaning                                                                                                                         |
| --------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| **Tier**                    | 1 (highest) → 5 (lowest) | Current net revenue contribution / TPV processed through Checkout. Tier 1–4 merchants have an Account Manager; Tier 5 does not. |
| **Incentive Rating**        | Gold > Silver > Bronze   | Revenue potential — highest NR potential or best opportunity to increase share of wallet.                                       |
| **Account Owner Territory** | SAT                      | Strategic Account Treatment — brands with high strategic value regardless of current revenue (e.g. Sony, Netflix, Spotify).     |


### Assignment rules


| Support plan   | Salesforce criteria                                                                                                         |
| -------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **Premium**    | Account Owner Territory = `SAT` **or** (Tier = `1` **and** Incentive Rating = `Gold`)                                       |
| **Enterprise** | Tier = `1` (not Gold) **or** Incentive Rating = `Gold` (not Tier 1) **or** (Tier = `2` **and** Incentive Rating = `Silver`) |
| **Standard**   | All remaining merchants — typically Incentive Rating = `Bronze` and Tier = `3`, `4`, or `5`                                 |


> **Note**: SAT designation alone qualifies a merchant for Premium regardless of Tier or Incentive Rating, reflecting that strategic brand value is treated as equivalent to top-revenue performance for support purposes.

## Merchant segments

### Premium

**Salesforce criteria**: Account Owner Territory = `SAT` **or** (Tier = `1` and Incentive Rating = `Gold`)

**Merchant profile**: Highest-revenue merchants (Tier 1, Gold incentive rating) and strategic brands (SAT) regardless of current revenue. Two distinct sub-profiles:

- **High-revenue (Tier 1 / Gold)**: Mission-critical operations, high TPV, zero tolerance for downtime. Mature self-built tooling, heavy API/webhook usage, complex bespoke setups.
- **Strategic (SAT)**: Recognisable consumer brands (e.g. Netflix, Spotify) whose presence has commercial and reputational value beyond current NR. May have lower TPV today but have strong growth or partnership potential. Have a named Account Manager.

Both profiles warrant the highest-touch support model. All Premium merchants have an Account Manager.

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

### Enterprise

**Salesforce criteria**: Tier = `1` (not Gold) **or** Incentive Rating = `Gold` (not Tier 1) **or** (Tier = `2` and Incentive Rating = `Silver`)

**Merchant profile**: Three distinct sub-profiles, all with meaningful revenue or growth potential but below the Premium threshold:

- **Tier 1 / non-Gold**: Established high-TPV merchants who don't yet have Gold incentive rating — significant current revenue but lower growth potential or share-of-wallet opportunity than Gold.
- **Gold / non-Tier 1**: High revenue-potential merchants (Gold incentive rating) who are not yet Tier 1 — strong candidates for growing their Checkout share of wallet; may be earlier in their payments journey.
- **Tier 2 / Silver**: Mid-TPV merchants with moderate current revenue and meaningful upside. Growing operations, established payment flows. Have an Account Manager.

All Enterprise merchants have an Account Manager.

**Examples**: eToro, Plus500

**Key benefits**:

- Faster SLAs than Standard
- Dedicated channels: live chat, email, video callback
- Named Support Engineer (Phase II)
- Quarterly health reviews — surfacing friction in payment flow with optimisation recommendations (Phase II)
- Context-aware support — agents and AI familiar with integration history and account profile
- Developer-to-developer priority routing (2 developer profiles)
- Real-time merchant health alerts — API alerts + payments performance trends
- Essential optimisations: fraud, disputes, and operational support
- Essential platform optimisations: risk, onboarding, and operational support (for ISV/Platform merchants)

### Standard

**Salesforce criteria**: Incentive Rating = `Bronze` and Tier = `3`, `4`, or `5` — all merchants not qualifying for Premium or Enterprise.

**Merchant profile**: Long-tail merchants with lower current revenue and limited growth potential in the near term. Tier 3–5, Bronze incentive rating. Tier 3–4 merchants have an Account Manager; Tier 5 merchants do not. Rely primarily on the Dashboard and self-service tooling. Lower payment flow complexity and API usage than higher Merchant segments.

**Key benefits**:

- Reliable baseline SLAs
- AI Agent, webform, live chat (business hours)
- 24×5 staffed coverage (P1 24×7)
- Self-service tools
- Developer-to-developer priority routing (1 developer profile)
- Real-time merchant health alerts — essential API alerts

### Checkout Payfac — Direct Sub-Merchant Support *(New, TBC)*

**Merchant profile**: Small merchants Checkout directly supports as primary Platform/PayFac, or SMB merchants onboarded via Tier 5 expansion. Same profile as Standard.

**Notes**:

- Timing TBC
- May offer premium add-ons (faster SLAs, live chat) for a fee
- Consumer Duty considerations may apply

### B2C Consumer

**Segments**: Remember Me (card-saving product, live today) + Braavos Neobank (2027+)

**Remember Me — live today**: Consumers contact support via a webform on the Remember Me portal (card saving feature within Flow). Tickets flow into the **Checkout Consumer** Zendesk brand. Volume is <10 tickets/week. No formal tier structure, AI Agent, or SLA framework yet — this is the seed of the B2C support model.

**Braavos and full B2C model — 2027+. Key differences from B2B**:

- AI Agent primary channel
- Phone mandatory (regulatory requirement for banking product)
- Business-hours human coverage
- Likely requires BPO for first-line contact handling
- SLA within hours
- Complaint handling as a distinct regulated function (Consumer Duty, 8-week FRL, FOS referral rights)

## Feature Comparison by Merchant segment


| Feature                                   | Standard             | Enterprise                      | Premium                         |
| ----------------------------------------- | -------------------- | ------------------------------- | ------------------------------- |
| **AI Agent**                              | 24×7                 | 24×7                            | 24×7                            |
| **Context-aware support**                 | —                    | ✅                               | ✅                               |
| **Developer profiles (priority routing)** | 1                    | 2                               | 4                               |
| **Real-time health alerts**               | Essential API alerts | API alerts + performance trends | API alerts + performance trends |
| **Named Support Engineer**                | —                    | Phase II                        | ✅                               |
| **Health reviews**                        | —                    | Quarterly (Phase II)            | Monthly                         |
| **Proactive reporting & custom insights** | —                    | —                               | ✅                               |
| **Flash sale / peak event support**       | —                    | —                               | ✅                               |
| **Platform optimisations**                | —                    | Essential                       | Custom-defined                  |
| **API availability reporting**            | —                    | —                               | ✅                               |
| **Dedicated Slack / IM**                  | —                    | —                               | 24×7                            |


## SLA Matrix


| Priority                            | Definition                                       | Standard                                  | Enterprise               | Premium                  |
| ----------------------------------- | ------------------------------------------------ | ----------------------------------------- | ------------------------ | ------------------------ |
| **P0** — Complete outage            | All payments failing                             | FR: 15 mins / Res: 4 hrs                  | FR: 15 mins / Res: 4 hrs | FR: 15 mins / Res: 4 hrs |
| **P1** — Major functional issue     | Sharp drop in approval rates, missing settlement | FR: 4 hrs / Res: 1 business day           | FR: 1 hr / Res: 12 hrs   | FR: 30 mins / Res: 8 hrs |
| **P2** — Limited operational impact | Refund failed, password reset                    | FR: 12 hrs / Res: 2 business days         | FR: 4 hrs / Res: 24 hrs  | FR: 2 hrs / Res: 12 hrs  |
| **P3** — Minimal impact             | Dashboard UI bug, docs question                  | FR: 1 business day / Res: 3 business days | FR: 12 hrs / Res: 48 hrs | FR: 4 hrs / Res: 24 hrs  |


*FR = First Response. All SLAs are first-response commitments.*

> **Stripe comparison**: Stripe's Growth tier has a 6-hour priority email SLA; Premium and Enterprise have 4-hour. Their business-critical response SLA is 15 minutes across all paid tiers. Checkout's SLAs are broadly comparable or stronger.

## Channel Entitlements


| Channel              | Standard       | Enterprise | Premium   |
| -------------------- | -------------- | ---------- | --------- |
| AI Agent             | 24×7           | 24×7       | 24×7      |
| Dashboard Webform    | Business hours | 24×5       | 24×7      |
| Dedicated Email      | —              | —          | 24×7      |
| Live Chat            | Business hours | 24×5       | 24×7      |
| Telephone            | P1 only        | P1 only    | P1 only   |
| Video Callback       | —              | Scheduled  | Scheduled |
| Dedicated Slack / IM | —              | —          | 24×7      |


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
| Developer-to-developer routing      | Support model enablement              | Q2 (Standard), Q3 (Enterprise/Premium) |
| Flash sale / peak event support     | Support model + Named Engineer        | Q3+                                    |
| Platform optimisations              | Platform support channels             | Q1                                     |


## Ticket Distribution (2025 baseline)


| Merchant segment | % of tickets | % of merchants |
| ---------------- | ------------ | -------------- |
| Premium          | 31%          | 5%             |
| Enterprise       | 33%          | 20%            |
| Standard         | 36%          | 75%            |


## Problem This Solves

- No defined support plans → inconsistent, ad hoc service experience
- Different merchants offered different channels without a strategic framework
- Merchants unaware of what they're entitled to → misaligned expectations
- One-size-fits-all SLO applied uniformly regardless of Merchant segment or issue priority

## Key Risks


| Risk                                        | Mitigation                                                                                    |
| ------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Internal misalignment on entitlements       | Cross-functional enablement pack + mandatory training for frontline teams                     |
| Merchant perception as a downgrade          | Proactive comms emphasising enhancements; grandfather existing expectations where appropriate |
| SKU/catalogue friction for Sales            | Include plans in all commercial proposals with pricing logic                                  |
| Standard Merchant segment feels underserved | Continue self-service and AI investment; monitor CSAT/NPS across all Merchant segments        |


## Competitor Benchmark


| Feature                       | Stripe                                                  | Adyen                                                               | Worldpay                   | Checkout.com (target)                                        |
| ----------------------------- | ------------------------------------------------------- | ------------------------------------------------------------------- | -------------------------- | ------------------------------------------------------------ |
| **Support tiers**             | 4 (Standard + Growth + Premium + Enterprise)            | Account-led; platform merchants have mandated 3-tier internal model | Merchant-type segmentation | 3 Merchant segments (Standard / Enterprise / Premium)        |
| **Named TAM / Engineer**      | Scaled TAM (Premium), embedded TAM (Enterprise)         | Account Manager for escalations                                     | Account Manager            | Named Support Engineer (Phase II, Enterprise+)               |
| **Context-aware support**     | ✅ Growth+ — agents know your integration history        | —                                                                   | —                          | ✅ Q1 via Merchant 360 context                                |
| **Developer routing**         | 1–4 developer profiles by tier                          | —                                                                   | —                          | 1–4 developer profiles by Merchant segment (target)          |
| **Health alerts**             | API alerts (all tiers); + performance trends (Premium+) | Webhooks (merchant-managed)                                         | —                          | Proactive notifications (roadmap)                            |
| **Health reviews**            | Continuous (Premium+), custom (Enterprise)              | —                                                                   | —                          | Quarterly (Enterprise) / Monthly (Premium)                   |
| **Flash sale / peak support** | ✅ Enterprise only                                       | —                                                                   | ✅ High-TPS gaming vertical | ✅ Premium (target)                                           |
| **Dedicated Slack**           | ✅ Enterprise only                                       | —                                                                   | —                          | ✅ Premium                                                    |
| **Live Chat**                 | ✅ All customers 24/7                                    | —                                                                   | —                          | Business hours (Standard); 24×5 (Enterprise); 24×7 (Premium) |
| **Phone**                     | ✅ All customers 24/7                                    | Critical only                                                       | ✅ 24/7 multiple lines      | P1 all Merchant segments                                     |
| **Platform optimisations**    | ✅ Premium+                                              | Mandated on platform                                                | —                          | Q1 (ISV identification); full optimisations Phase II         |
| **Monetised premium tier**    | ✅ (subscription / contract)                             | Contract-based                                                      | Bespoke                    | Bespoke / minimum billing                                    |


**Target**: Match Stripe's Growth tier at our Enterprise level; match Stripe's Premium/Enterprise at our Premium level. Key Checkout differentiators to maintain: video callback, stronger SLAs at Premium, and proactive health reviews at Enterprise (Stripe only offers this at Premium+).

**Last Updated**: February 2026
**Owner**: Charlie Wildish
**Source**: `Merchant Care Success Plans Proposal.md` + [stripe.com/support-plans](https://stripe.com/support-plans)