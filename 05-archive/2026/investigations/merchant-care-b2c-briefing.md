# Merchant Care — Context Briefing for the Consumer PM

**From**: Charlie Wildish, Care Product  
**Date**: March 2026  
**For**: Consumer PM — Support requirements, experience definition, Consumer Duty

---

**This document answers one question**: how does Merchant Care work, and what does it mean for your work on B2C consumer support?

Checkout.com's support model is built primarily around B2B merchants. There is a live B2C touchpoint, Remember Me, Checkout.com's card saving product for consumers, already has a support channel and a Zendesk brand  but it's early stage (<10 tickets/week) and is not a full support model. You're stepping into a domain where the B2C support model exists in seed form and needs to be defined and scaled: the channel strategy, the regulatory approach, the competitive benchmarks, and the gap between what's in place for Remember Me and what Braavos will require. This document gives you the context to do that: how Merchant Care works, what I'm building on the B2B side, where our work intersects, and what the open questions are that we need to resolve together.

---

## What Merchant Care Owns

Care Product is the PM function for Checkout.com's support infrastructure. The domain covers everything that happens from the moment a merchant contacts support to the moment that contact drives a product improvement or is deflected entirely.

We think about the domain as a six-stage flywheel:


| Stage                    | What it covers                                                                                       |
| ------------------------ | ---------------------------------------------------------------------------------------------------- |
| **Input**                | The channels merchants use to contact us, and the query taxonomy that classifies what they're asking |
| **Orchestration**        | Triage logic and routing rules — where the contact goes and who is best placed to answer it          |
| **Fuel**                 | The data and knowledge content that powers both AI and human agents to resolve issues accurately     |
| **Agent Experience**     | The tooling human agents use inside Zendesk to investigate and resolve tickets                       |
| **Insight & Prevention** | Translating support contact data into product and content fixes that prevent future contacts         |
| **Governance**           | SLA management, QA, and operational standards — the baseline below which we don't go                 |


The strategic direction is for the flywheel to spin faster over time: better AI resolution reduces volume, better insights fix root causes, better data quality improves AI accuracy, which reduces volume further. The target by 2030 is AI handling 80%+ of contacts, with human agents reserved for complex issues and VIP merchants.

**P&L context**: Care sits on the Loss side of the Product P&L. Support is not revenue-generating, but it is revenue-protecting — and for B2C at scale, it becomes a direct churn driver. The goal is for unit costs (cost per contact, cost per £1M processed) to decline as scale grows, even if absolute spend rises. Investment in AI deflection, agent tooling, and contact reduction compounds over time. For B2C specifically, the link between support quality and churn is more direct than in B2B — there's no account management layer to buffer it.

---

## How Support Works Today

Every aspect of the current support model is built for B2B merchants. Understanding it tells you both what infrastructure you can potentially build on top of, and what will need to be rebuilt or extended for B2C.

### The channels

Merchants contact us through four routes:

- **Fin AI Agent** (Dashboard chat) — Intercom Fin runs inside the merchant Dashboard. It attempts to resolve the query before creating a Zendesk ticket. Today this is the only channel where AI is involved.
- **Email** (`support@checkout.com`) — routes directly into Zendesk. Fin is not deployed here today.
- **Dashboard Webform** — a structured form inside the Dashboard. Authenticated at submission, so identity is confirmed. Fin is not deployed here today either.
- **AM/TAM internal form** — Account Managers raise tickets on behalf of merchants via a Retool form that maps to the merchant's Zendesk organisation. ~8–10% of annual contact volume comes through this channel.

The critical operational reality: **Fin involvement is 9.2% today**. That means 90.8% of contacts arrive via channels where AI is not deployed. Email alone is 45% of all contacts. The plan to reach 80% involvement by end-2026 requires deploying Fin on email and webform, and redirecting Standard merchants who currently use email to Dashboard chat.

### Zendesk and the agent toolkit

Zendesk is the backbone. When AI cannot resolve a contact, or when a merchant goes direct, a ticket is created in Zendesk and routed to a human agent. Agents use two internal tools:

- **User Profile** — surfaces requester identity, Dashboard role, and merchant organisation context. Agents also use it to manually search for and attach an unknown sender to the correct merchant organisation (the "Dispatch" process — more below).
- **Payment Tool** — takes a Payment ID and Client ID from the ticket, queries external payment systems, and returns payment metadata so agents don't have to leave Zendesk to investigate.

**Dispatch** is the queue for unidentified email contacts — tickets where the sender's email didn't match a Salesforce or Dashboard record. Agents spend time identifying the merchant before they can even start resolving the issue. This is a direct operational cost and a known challenge. It's worth understanding because any B2C implementation will face the same identity problem at much higher volume.

### The three merchant support tiers

Merchants are segmented into three tiers based on Salesforce CRM data (current revenue contribution, growth potential, and strategic brand value):


| Tier           | Profile                                                                            | Key benefits                                                                                          |
| -------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Premium**    | Highest-revenue (Tier 1 / Gold) and strategic brands (SAT: Netflix, Spotify, Uber) | Named Support Engineer, monthly health reviews, dedicated Slack/IM, fastest SLAs, 24×7 staffed        |
| **Enterprise** | Tier 1 (non-Gold), Gold incentive rating, or Tier 2 / Silver                       | Live chat 24×5, quarterly health reviews (Phase II), context-aware support, faster SLAs than Standard |
| **Standard**   | All remaining merchants — Bronze / Tier 3–5                                        | AI Agent 24×7, webform and live chat during business hours, reliable baseline SLAs                    |


The SLA structure escalates with priority and tier. At P0 (complete outage), all tiers get a 15-minute first response. At P1 (major functional issue), Standard gets 4 hours; Premium gets 30 minutes. Standard merchants are not entitled to email as a contact channel — though 26.6% still use it today, which is part of the enforcement problem we're solving in 2026.

**This tier model is B2B only.** It is not designed for consumer support and cannot be applied directly. B2C requires a different framework — addressed in Section 4.

---

## The Strategy and Where We're Heading

### The flywheel in practice

The operating principle behind the strategy is: Handle → Learn → Fix → Scale.

- **Handle**: AI Agent takes the volume first. Humans focus on complex issues and the highest-value merchants. Good data powers both.
- **Learn**: Support contact data flows automatically into root cause analysis and outputs for Product and Content teams. We're building Reflex — an AI-powered insights product — to do this at scale.
- **Fix**: Product and content teams act on those outputs to close the gaps that generated the contacts. Every ticket that gets prevented saves cost and improves merchant experience.
- **Scale**: Fewer contacts, higher quality remaining volume, more capacity for the next cycle.

### 2026 priorities

Three things are driving this year's roadmap:

1. **Fin involvement rate** — getting from 9.2% to 80% by deploying Fin on email and webform, and enforcing channel eligibility. This is the single biggest lever for cost reduction and AI quality improvement.
2. **Merchant success plans** — rolling out the Standard / Enterprise / Premium tier model with defined SLAs, channel entitlements, and (Phase II) named support engineers and health reviews. Replacing the previous one-size-fits-all approach.
3. **Reflex insights** — building the automated contact driver analysis that feeds product and content improvements. The "Learn" stage of the flywheel.

### Blue EMI as a live case study

One active workstream that's worth understanding for context: Blue EMI (Project Moon) is a new legal entity running on Checkout's platform, launching its first merchant in March 2026. There is currently no support infrastructure for it — no Zendesk brand, no channel, no agent tooling.

I'm scoping that now: an interim Slack-managed model through Q1, then a full Zendesk Multibrand build in Q2. The challenge it surfaces is directly analogous to challenges you'll face for B2C: identity disambiguation at submission (a Blue EMI merchant and a Checkout merchant can share an email address), branded channel separation, complaints routing, and agent tooling that works for the right entity.

Blue EMI is B2B only — it's not in scope for your work. But the infrastructure patterns we're solving for it will be relevant precedents for any multi-brand or multi-entity B2C build.

---

## The B2C Landscape — What Exists and What's Coming

### What already exists: Remember Me

**Remember Me** is a live B2C product today — a card saving feature for cardholders who transact via Flow. Cardholders contact support through a webform on the Remember Me portal; those tickets flow into a dedicated Zendesk brand called **Checkout Consumer**. Volume is under 10 tickets per week at this stage, so the query mix and patterns aren't yet statistically meaningful, but the infrastructure seed is real: there is a live B2C channel, a live Zendesk brand, and real consumer contacts coming in.

This matters for your work because the Checkout Consumer brand is the foundation to build on. The question for Braavos is not whether to stand up B2C support in Zendesk — it's already there — but what configuration expansion is needed to cover a consumer banking product at materially higher volumes and under a materially higher regulatory bar.

### Project Braavos

The B2C product is **Project Braavos** — a consumer wallet and neobank. Launch is planned for **2027**. When it launches, Checkout.com will hold consumer funds and earn interest on balances. This is not a future consideration to be designed later; it applies from day one and raises the regulatory floor materially.

The current Remember Me / Checkout Consumer setup is not a support model for a banking product. It handles a simple card-saving use case at low volume with no regulatory obligations beyond basic consumer protection. Braavos requires complaint handling, Consumer Duty compliance, phone, BPO capacity, and an AI Agent configured for consumer banking queries. The Checkout Consumer brand is the right starting point — it just needs to be significantly expanded before 2027.

### Why B2C is structurally different from B2B

Five structural differences that govern how the support model must be designed:

**1. Volume and complexity are inverted.** B2B contacts are lower volume, higher complexity — integration issues, settlement disputes, API debugging. B2C contacts will be high volume, lower average complexity — "why did my payment fail?", "where is my cashback?", "my card won't save". This inverts the economics: the AI resolution rate needs to be very high to keep costs manageable, and the human agent tier is reserved for exceptions, not the norm.

**2. Phone is likely a regulatory requirement, not a feature decision.** As a banking product holding consumer funds, Checkout.com will be subject to FCA Consumer Duty and accessibility requirements that typically mandate a phone channel. This is not a post-launch enhancement — it needs to be in the plan before the wallet goes live.

**3. Consumer Duty changes the floor for every interaction.** FCA Consumer Duty requires demonstrable good outcomes for retail customers — the support model needs to be designed with that in mind from day one. This includes complaint handling with tracked SLAs, vulnerable customer identification in the AI Agent flow, and 8-week Final Response Letters with FOS referral rights for unresolved complaints.

**4. Complaint handling is a distinct function from ticket handling.** In B2B, complaints are edge cases handled as tickets. In banking, complaints handling is a regulated function — separate process, tracked SLAs, documented outcomes. This needs to exist before any banking product goes live.

**5. BPO is likely for first-line volume.** B2C contact volumes at scale are incompatible with the staffing model used for B2B merchant support. A BPO partner for first-line handling is the standard model across the competitive set. The timing and procurement of that needs to be in your roadmap.

### The regulatory step-change

The difference between supporting merchants as a PSP (current) and supporting consumers as a bank (Braavos) is significant:


| Obligation                         | PSP today      | Banking product (Braavos)                                     |
| ---------------------------------- | -------------- | ------------------------------------------------------------- |
| Complaint handling                 | Best practice  | Mandatory — 8-week Final Response Letter, FOS referral rights |
| Phone support                      | Optional       | Typically required for accessibility / Consumer Duty          |
| Consumer Duty                      | Not applicable | Mandatory — demonstrable good outcomes for retail customers   |
| FSCS disclosure                    | N/A            | Required if deposits are protected                            |
| Vulnerable customer identification | Best practice  | Regulatory expectation                                        |


The support model for Braavos is not a lighter version of the B2B model. It's a different regulatory category.

---

## Competitive Benchmarks for B2C Support

The relevant competitive set for Braavos is Monzo, Revolut, Starling, Klarna, and Zilch. Four patterns from this analysis are most relevant for forming your strategy.

### 1. Embedded support beats standalone support

The most effective B2C support models don't surface support as a separate help flow — they embed it directly into the product at the point of friction. Klarna's dispute flow is embedded in the transaction view; the invoice is automatically paused during investigation, so the customer isn't chasing while they wait. Monzo's "Report Missing Cashback" is accessible from the specific transaction, not a generic help menu. Starling's natural language spending queries eliminate an entire category of "where did my money go?" contacts.

For Braavos, this means the support model should be designed alongside the product UX, not separately. The highest-friction moments — missing cashback, disputed transactions, failed payments — are where embedded support prevents contacts, not just resolves them.

### 2. The industry is already at 70–75% FCR — the bar is higher than it looks

First Contact Resolution at 70–75% is the **industry average** in 2026. High performers are targeting >85% by 2027. The 2030 vision for Checkout's B2C support targets 80% AI resolution — but at 2027 launch, 80% may already be table stakes, not differentiation. The ambition should be >85–90% to be genuinely competitive. Note that Intercom Fin (our current platform) benchmarks at 55–65% autonomous resolution — below specialist agentic platforms (Fini: 70–85%). Platform capability will need to be tracked as a constraint.

### 3. Tiered support is both a service model and a revenue lever

Revolut (Standard / Premium / Metal / Ultra), Monzo, and Starling all use tiered support as a product feature. Standard users get AI and self-service; Premium users get priority human chat within 5 minutes; Ultra/VIP users get priority voice and callback. For a consumer wallet, tiered support access is potentially a monetisable feature, not just an operational decision. This is a strategic choice to make early: is premium support access a retention tool bundled with the product tier, or a standalone subscription?

### 4. Agentic commerce creates a new dispute category

By 2027, a meaningful share of B2C support contacts will involve disputes where an AI agent — not the human — made a purchase. This requires a new support category that doesn't map to the existing fraud / chargeback framework: the difference between an **unauthorised transaction** (fraud — bank is liable under existing frameworks) and an **unintended transaction** (AI agent error — liability depends on what the user explicitly authorised). This needs both a product design decision (cryptographic or logged proof of user consent for AI-initiated purchases) and a policy decision before launch. Legal and Compliance should be involved early.

---

## Where Our Domains Connect

The B2B support infrastructure I own and the B2C consumer support model you're defining are largely parallel — distinct user bases, distinct channels, distinct regulatory contexts. There are two points where they genuinely intersect.

### Project Braavos — the infrastructure / requirements split

For the 2027 consumer wallet, the split in ownership is:

- **Care Product (me)**: The support infrastructure — which channels, which AI Agent configuration, how Zendesk is set up for B2C, what tooling agents use, how the flywheel runs for consumer contacts
- **Consumer PM (you)**: The consumer experience and requirements — what the support flow looks and feels like for users, what Consumer Duty compliance looks like end to end, how complaints are handled, what the vulnerable customer policy requires, what SLAs are committed to

Neither of us can define our piece without the other. The infrastructure I build needs to be shaped by your requirements — channel mix, complaint handling flow, regulatory constraints, tiering logic. Your requirements need to be grounded in what's feasible to build on the infrastructure side. We need an early alignment conversation on scope and timing before either of us goes deep into design.

### Shared infrastructure dependencies

The B2B tooling that exists today — Fin AI Agent, Zendesk, Agent Toolkit — is all configured for B2B merchants. B2C will require:

- **A new Fin configuration** with consumer-oriented content, B2C query taxonomy, and consumer data access (not merchant/payment data)
- **A new Zendesk brand / instance** — whether this sits in the same Zendesk account as B2B or a separate one is an open question; the answer affects cost, complexity, and governance
- **New agent specialisms** — human agents handling Braavos contacts need different knowledge and tooling than those handling merchant contacts; likely a separate team, potentially a BPO for first-line

---

## Open Questions to Resolve Together

These are the questions we need to align on before either of us can go deep into planning:

1. **Checkout Consumer brand scope** — the Zendesk brand already exists, seeded by Remember Me (<10 tickets/week). The question is what configuration expansion it needs to support Braavos at launch: new SLA policies, complaint handling workflows, a phone channel, Consumer Duty-driven routing, BPO integration. What does the gap look like between what's configured now and what Braavos needs?
2. **Phone channel timing** — phone is likely a regulatory requirement for a banking product, not an optional feature. When does it need to be in the roadmap for it to be live at or shortly after the Braavos launch? This needs input from Legal/Compliance and needs to drive a procurement decision for BPO or in-house staffing.
3. **BPO vs in-house for first-line** — the consumer volume model doesn't work with Checkout's current B2B support staffing. A BPO partner for first-line volume is the standard across the competitive set. What's the timing, procurement lead time, and budget path for that decision?
4. **Consumer Duty sign-off** — Consumer Duty requires demonstrable evidence of good outcomes. Who is responsible for that sign-off in the product org? Is it the Consumer PM, Legal/Compliance, or shared? The answer determines what gets built into the support model vs. what sits in a separate compliance function.

---

**Owner**: Charlie Wildish  
**For**: Consumer PM (Checkout Consumer team)  
**Last Updated**: March 2026