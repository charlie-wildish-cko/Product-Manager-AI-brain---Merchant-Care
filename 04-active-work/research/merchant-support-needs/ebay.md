# eBay — Merchant Support Needs

**Meeting:** Melissa Pepperell / Charlie — 2026-01-13  
**AM:** Melissa Pepperell  
**Segment:** Tier 1, Global, API/report-first enterprise  
**Drive source:** 1U-gL7lQvcLBmwMeFWz1u6XwBU34usZBiliKmq5gglbI

---

## Merchant Profile

VIP strategic merchant. Global. Multi-PSP. Deliberately limits dashboard access — a small number of eBay staff have access by design; most data is pulled via reports and APIs into internal systems. Almost never raises Zendesk tickets; primary support happens through multiple dedicated Slack channels and weekly calls.

---

## Support Channels Used

- **Slack** — multiple dedicated channels: dev/integration, AR performance, general eBay-Checkout, P0/P1 emergency, sidebar channels
- **Weekly calls** — at least 3 per week with various eBay teams
- **Occasional email**
- Zendesk tickets: rare; most support is off-ticket and therefore invisible in care metrics

---

## Primary Support Needs and Pain Points

**Acceptance rate monitoring**
Primary ongoing concern. Constant questions about AR drops by payment method, geography, and BIN.
> "There's a lot of questions around AR and hey why are we seeing this on Google Pay in Australia and why are we seeing this here and what happened here. So that's an all the time question."

**Integration and technical queries**
Documentation gaps, unexpected response codes, integration questions as eBay adds new capabilities.
> "They are trying to integrate like at some point they're supposed to be doing authentication with us. So there'll be questions sometimes about our docs or the codes or hey we're suddenly seeing this response code."

**Invoice and report reconciliation mismatches**
eBay pulls Checkout reports into their own internal systems; contacts support when figures don't reconcile.
> "There are several questions about our invoices and then our reports and why are things not matching and then they're looking at what they're pulling in internally from our data sources and our reports."

**Proof of settlement**
Requests for remittance / proof of settlement require manual Treasury involvement.
> "What happened to this settlement? Can you... we have to go out to one of our treasury teams and say hey can you send me the remit... proof of payment basically proof of settlement."

**Compliance and scheme queries**
Recurring types: 3DS questions, chargebacks, AML/CTF compliance changes (e.g. Australia March 31 deadline), L2/L3 qualification calculations.

**Phone support gap**
eBay contacts have asked about phone support since the AM joined Checkout. Current phone line is not fit for purpose.
> "Since I started here I've been asked about our phone, which is quite normal with other PSPs."

**No dashboard self-service**
eBay deliberately limits dashboard access. AI agent responses that direct merchants to the dashboard are unhelpful and ignored.
> "Very few have access to dashboard on their side. That's purpose. That's something they they don't want."

---

## Key Insights

- eBay's true support volume is systematically undercounted — most interactions happen on Slack, not in Zendesk.
- Fin cannot reach eBay in its current dashboard-bound form. AI for eBay would need to work over email or Slack.
- eBay's AMs are spending significant time on queries that should route to a support channel — but eBay's expectation is white-glove, not ticketing.
- AM/TAM being CC'd on support tickets and AI responses is a practical request with low implementation effort. eBay needs to be able to interject if an AI response is wrong.
- Settlement and reconciliation queries require Treasury API access to automate — not achievable with current Fin scope.
- Phone support is a competitive gap vs other PSPs, particularly for P0/urgent scenarios.
- AI agent adoption is at 15–20% of ticket volume because it is entirely optional and not channelled by merchant tier.
