# SMB Research Findings — How SMBs Define Themselves and Their Payment Needs

> Full findings and quotes underpinning the "Not White Glove (SMB)" segment in `customer-segments.md` and the Sam persona in `customer-personas.md`. AI-generated synthesis — review before citing externally.

**Sources**: 5 interview transcripts (In-Market Decision Makers series, 2023) + SMB Discovery Survey (Feb 2022, n=253) + internal strategy document (June 2026). Analysed 2026-06-17.

**Credibility: Medium-High.** Qual and quant triangulate on the core findings (self-serve preference, Stripe/PayPal dominance, live balance importance, invoice-first dashboard needs). Qual sample skews toward early-stage, tech-aware founders in UK, Germany, and Ukraine; quant survey adds geographic breadth (14 countries) but was fielded in 2022. Single-coder qual analysis, no triangulation beyond the survey cross-check. Unanswered by both sources: how SMBs self-categorise using the term "small business"; offline-first SMBs (card readers, SoftPOS); post-2022 PSP market shifts; what triggers an active PSP search.

## Interview sources

| # | Participant / company | Role |
|---|---|---|
| 1 | Offsetted | Founder |
| 2 | Myra (StylishAccessoriesShop context differs — see below) | Head of Operations (used Stripe and Tyl by Natwest) |
| 3 | Subjektiv | Head of Product Design |
| 4 | StylishAccessoriesShop | Contact Us Lead |
| 5 | Hafven (Lars) | Head of Product |
| 6 (quant) | SMB Discovery Survey, Feb 2022, n=253 (745 selections on multi-select questions) | — |
| 7 (internal context) | Checkout for SMB — Proposition & Launch Product (June 2026) | — |

Transcripts held in Checkout's Merchant Services research Drive (`Merchant Services/2022 - SMB/2023 - In-Market Decisions Makers/`) — not copied into this repo. Quotes below are the primary record available locally.

## Executive summary

SMBs do not self-identify as "SMB" — they describe themselves by business type, stage, and immediate problem. Payment needs are inseparable from broader operational jobs: invoicing, reconciliation, daily business visibility. The dominant PSP selection driver is self-serve activation with no monthly fee: 69% of the surveyed market has no dedicated development resource. Stripe and PayPal dominate awareness (79% and ~100%); Checkout.com is recognised by only 5.23% of respondents.

## Findings (ordered by certainty)

### 1. SMBs define themselves by business problem, not by payments — High certainty, 5/5 qual
Every participant described their product or service first; payments were an operational requirement to unlock something else.

> *"So our main product is carbon account and slash ESG reporting product... we need the payment provider."* — Offsetted, Founder

> *"So essentially what we do... is bring restaurant quality, award-winning food to people's kitchens... So we sell these cookery classes online and that's where we take payments."* — Myra, Head of Operations

Quant: Q3 role data confirms the "wearing many hats" profile — most respondents self-describe as Owner/Founder/Director handling finance, hiring, marketing, and payments simultaneously. Q66: 51% rank digital e-commerce services as their #1 adaptation priority (mean 2.07 of 7) — payments sit downstream of the e-commerce challenge, not separate from it.

### 2. Checkout.com has critically low brand awareness; Stripe/PayPal are the duopoly — High certainty
Q67 (n=745 selections): PayPal 100% aware, Stripe 79%, Worldpay 34%, Braintree 22%, **Checkout.com 5.23%** (39 of 745), Adyen 2.42%, Mollie 1.34%.

> *"Yeah, we looked at different payment providers. Honestly, I don't even remember its names because Stripe was typically a better choice from every perspective."* — Offsetted, Founder

The 5.23% figure likely overstates true unprompted awareness — this survey sample included participants recruited via Checkout.com contact channels. Cold acquisition on brand is not viable at current awareness; platform-native distribution (Wix, WooCommerce, GoDaddy) or co-marketing is the only scalable route until brand recognition improves.

### 3. Self-serve, zero-dev setup is non-negotiable — High certainty, 4/5 qual, corroborated quant
Q79 (n=253): 43% handle setup entirely themselves, 26% need only PSP technical support, 19% have in-house developers, 9% hire temporary developers. **69% have no development resource.**

> *"If you're telling me, OK, Alex, you can press one button, you are pre-approved already... one second passes, we are integrated and our commission is lower. I would switch instantly."* — Offsetted, Founder

> *"I know it integrates very easily. I don't need to understand coding and development to be able to integrate it. So that was important."* — Myra, Head of Operations

> *"Taking into account very short timeline, I think we'll be looking into solutions that can be integrated very fast."* — Subjektiv, Head of Product Design

Any PSP requiring API integration as the primary onboarding path loses 69% of the addressable SMB market before a transaction is processed.

### 4. No monthly platform fee is a hard filter — High certainty, 3/5 qual
> *"They were charging a monthly fee. Stripe don't charge the monthly fee, which is very important to keep our cost down as a startup."* — Myra, Head of Operations

> *"In the majority of cases, they are not earning any money in order to pay for this provider for a couple of months or maybe even longer. So the longer we can use the service free of charge, the more probabilities that we're gonna be paying for that."* — Offsetted, Founder

Quant free-text (Q52/Q68): *"Stripe, because my business is seasonal, so I don't want to pay for a monthly fee when I don't use the service for 6 months."* Fixed monthly costs disproportionately punish seasonal/variable-revenue SMBs.

### 5. The dashboard is a daily business-ops tool, not an exception console — High certainty
Q74 (n=252): 79% rate live balance visibility extremely/very important (52% extremely, 27% very). Q78: "Send single invoices to customers" ranked #1 dashboard capability by 45.2% (mean rank 1.95), ahead of custom transaction alerts (20.4%), customised transaction views (22%), and double approval for refunds (12.4%).

> *"What Natwest do a bit better is when you log in it first straightaway shows you your sales for today, if it's up or down from yesterday, and if you're expecting any settlements. That's quite good to see just on a front page."* — Myra, Head of Operations

> *"Is there a way to automate reporting? Can I schedule a report to run at the end of the week and come straight into my inbox... that'll be important for weekly reconciliations, monthly reconciliations, understanding the tax side of things."* — Myra, Head of Operations

> *"The first thing I would check out is how do I get my data into my accounting software? That's always one of the first things I check out."* — Hafven (Lars), Head of Product

Minimum viable SMB dashboard: today's sales → expected settlement → send an invoice. Everything else is secondary.

### 6. Settlement accounts are sticky; PSP switching cost is perceived as near-zero but rarely acted on — Medium-High
Q76 (n=253): 72% never change settlement bank account; 19% once a year; 8% once every 6 months.

> *"If you offer me a better deal and my switching cost is zero, I would consider changing. I would change the next day. No problem."* — Offsetted, Founder

Quant free-text: *"I've used PayPal and Stripe for a very long time, over 10 years... other payment providers need to offer something noticeably better to encourage me to spend time switching over my systems."* The tension resolves as: low psychological switching cost, high behavioural inertia — SMBs don't evaluate PSPs on an ongoing basis; the trigger is a failure event (fund hold, account freeze) or a frictionless, materially better offer.

### 7. PSP brand/logo is a conversion signal SMBs pass to their own customers — Medium, 2/5 qual
> *"Selling to the United States is very hard because people want to see the safe payment gateway... we show our payment gateways, we are using American Express, Checkout.com, Mastercard, Visa. After that first step, people believed us — they say, OK, it's safe."* — StylishAccessoriesShop, Contact Us Lead

> *"If it looks like a scam — the graphics not as good, like someone is trying to steal your credit card — I'm not gonna switch, it will be reducing my conversion right now for sure."* — Offsetted, Founder

Checkout.com's low brand awareness compounds here: a low-recognition badge is a weaker trust signal at the SMB's own checkout — a circular disadvantage against Stripe/PayPal.

### 8. Responsive support is a continuity requirement, not a premium tier — Medium, 2/5 qual
> *"If there's a problem with the payment system, I would like to write immediately to you... some customer comes and wants to buy, if he or she cannot, it will be very different to bring them back again."* — StylishAccessoriesShop, Contact Us Lead

Quant open-text (Q80): *"Real time support from the PSP regarding any transaction or feature we want to custom access, will be of great help while choosing PSP"*; *"be fast and able to handle all transactions and be safe... support should be available at all times, active system monitoring."* Real-time support was the third most common unprompted theme when respondents described a PSP being "relevant, adaptive and a partner." This is a baseline expectation, not a differentiator — framing fast support as a paid upsell misreads the segment.

### 9. Payment method defaults are market-specific — Low certainty, 1/5 qual, unquantified
> *"The German consumer is the master of SEPA direct debit... if you would try to offer a service here where you can only pay via credit card, I think you would need to think twice."* — Hafven (Lars), Head of Product

The 2022 survey's card-centric framing didn't capture geography-specific payment method preferences. Treat as a material unvalidated risk for any EEA go-to-market.

## Pricing considerations

1. **Fee structure matters more than fee rate.** A monthly platform fee is a hard disqualifier for early-stage SMBs, corroborated by both qual and the seasonal-business quant quote above.
2. **Price is evaluated as a bundle**, not in isolation — settlement speed, integration ease, and support are weighed alongside cost. *"How quickly we can get money to our bank account"* matters as much as the commission rate (Offsetted).
3. **Free-to-start drives long-term retention** — removing the cost barrier pre-revenue creates stickiness once the product proves out (Offsetted).
4. **The switching threshold is "noticeably better," not "marginally cheaper."** Price alone rarely triggers switching because SMBs aren't actively monitoring the market; the incumbent holds structural advantage absent a failure event or a frictionless, materially better offer.
5. **High price is tolerated when it solves a non-substitutable problem.** Hafven pays €700/month to Stripe and calls it "damn expensive" but stays because no cheaper alternative offers the same invoicing/accounting compliance required by German law — most acute in regulated European markets.

## Divergences and gaps

- Checkout.com brand recognition in the qual sample is likely inflated by prior exposure (recruited via Checkout.com contacts); the 5.23% survey figure is the more reliable read of unprompted awareness.
- Geographic payment method preferences (SEPA in Germany, etc.) are invisible in the quant instrument — unresolved.
- No data on how SMBs self-categorise as "small business," offline-first SMBs, post-2022 PSP share shifts, or what triggers an active PSP search vs. defaulting to a bundled option.
