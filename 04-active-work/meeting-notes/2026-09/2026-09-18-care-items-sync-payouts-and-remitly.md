# Care items sync: payout terminology, Remitly spike, FI data

**Date:** 2026-09-18  
**Attendees:** Charlie Wildish, Joe Graves, Jason Dantzer, Joshua Bedeau  
**Drive source:** 1u2iQ5qaRSoY14zZX9RGekKcyySJCjjKcjOS_g3Xn2nU

## Context

Cross-team sync on payments and payouts items driving Care contacts. Most speech is attributed to room mic "LON-03-02" (almost certainly Charlie, with Jason and Josh merged in). Gemini's summary misstates the volume figures. The figures below come from the transcript.

## Key Points

**New payout terminology**
- Henry introduced "pay to self" (client settlements, replacing "settlement") and "pay to third party" (bank payouts and card payouts), with little process.
- Charlie: the terms scale better and are clearer for AI, because merchants use "payout" for three different things. Joe is unsure "pay to self" works as a public term.

**Record contact volume**
- Normal year: about 40,000 contacts (about 4,000/month). This year has passed 50,000, forecast 50,000-60,000.
- August 2026: about 9,500 contacts total, of which about 4,000 from Remitly alone.
- Remitly moved its TPV to Checkout in about 2 days at its pay-to-card launch, with its AM and TAM both on holiday. Payouts onboarding checks were incomplete, regions and routes not configured. Transactions hit the sanctions flow and returned declined, failed or pending. Remitly was not onboarded to the Dashboard or trained, and 4 regional support teams shared one inbox.
- Charlie framed it as a merchant-readiness problem: nothing stops a merchant sending volume before it is ready.
- Jenny (Ops) raised a possible agent headcount increase this year, citing volume and a slower-than-hoped AI resolution ramp.

**FI clearing and settlement status (Jason)**
- Still waiting on FI to expose source data. It gives settlement status, not true clearing status, but shows failures.
- Originally expected H1/Q2. Paul (FI) now expected to define event outputs before end of Q4. At risk, dependent on the source team.
- Coverage: Visa, Mastercard, AMEX, DCI (about 98% of volume). Jason logged a request with Hamish to flow it into pay-in. Payment ops agreed to create the new status that also fixes scheme rejections.

**MPG/APG migration impact (Josh)**
- Charlie to work with Raina to test whether migration reduces support issues (for example, a 50% migration threshold). No data scientist on the team yet. Charlie may get one next month.

**Refund error 2030 (format error)**
- Generic error. The real reason sits in the data log. Common causes: refund past the 30-day window, payload validation failure.
- Agreed with Jason: deterministic logic returning clearer internal messages. Jason said it is easy. Manual refunds out of scope.

**Pay-to-self documentation (Joe Graves)**
- Public docs can be clearer, but Joe expects the contact reduction to be "pretty low". Seb (content) can help.
- The Financial Actions API is the source for linking a payment ID to a settlement or payout ID. Dashboard integration status unknown. Charlie to check with Alexa.

## Insights

- August 2026 is an outlier (about 4,000 Remitly contacts). Annotate or exclude it in contact-rate trend analysis.
- Merchant-readiness gating before go-live is a contact-prevention lever for Insight & Prevention and Reflex.
- Headcount pressure plus a slow AI ramp strengthens the cost-per-contact case for Fin investment.
- FI clearing-status data has slipped from Q2 to end of Q4 and is at risk.
- "Pay to self" / "pay to third party" affects the support taxonomy and Fin attribute definitions once adopted.
- Financial Actions API is the confirmed source for payment-to-settlement linkage.
