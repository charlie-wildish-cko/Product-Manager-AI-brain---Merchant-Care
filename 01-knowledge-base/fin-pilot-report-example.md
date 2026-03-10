# Fin AI Agent – lean in Pilot group report

**Example report** illustrating the style in `.cursor/rules/report-writing-style.mdc`. Originally in `.cursor/rules/`; moved here so rules only contain instructions, not sample content.

---

## Summary

We ran a pilot with six Tier 1 merchants in Q4 2025 to test whether Fin could replace email as their primary support channel. 

**Hypothesis**: These Merchants will prefer using Fin in Dashboard instead of email for support.

**Answer**: email entrenchment at this level is structural, not behavioural; these merchants will not move off email organically even if Fin is great. 

Based on this, the right response is not to keep pushing them toward Dashboard chat for now, but to bring Fin to where they already are. Long term we should look to shift this behaviour. This report says what we learned and the recommended actions.

## What we did

Six Tier 1 merchants participated in Q4 2025, selected because they had a representative email sample support volume (5-10% of contacts in the prior 6 months) and issue types where ≥60% of queries were assessed as Fin solvable. Account Managers supported the pilot and briefed the merchants directly. 

Participating merchants: ***eToro, Plus500, Sibilla, Wise, Bytedance, Vinted***.

## What we found

* **Scale & systems:** Larger merchants run distributed operations teams of 50+ people, use multiple PSPs, and manage support through centralised ticketing systems (Zendesk, Freshdesk etc). Corroborated through interviews with AMs from top merchants outside this pilot, from the top 20 who submit support tickets to us.  
* **Email is wired into their internal processes**: Changing that requires them to change across their whole operation not just for Checkout, and not without significant overhead.  
* **Dashboard access is a barrier**: Merchants with large, high-churn ops teams find the burden of managing individual Dashboard accounts and MFA significant. Shared email inboxes are simpler for them to operate. This is not a preference, it is a structural friction point. Dashboard is used by most merchants, but lessens for Operational teams and their work (managing payments/Settlements etc) as you go up in merchant profile.  
* **Low awareness about Dashboard features/Fin availability:** Theme that merchants don't know what Dashboard can do and self serve available there.  
* **Fin works well when it can answer the question**: eToro and Plus500, who had the simplest (payment-related) queries, gave strong positive feedback:  
  * *"The AI Agent has been very helpful in understanding codes" eToro*  
  * *"I've used the AI several times over the last few weeks and found it to be very helpful. It clearly has the potential to save time by cutting down on lengthy emails"* *Plus500*  
* **Current feature gaps limit adoption**: eToro couldn't access scheme dispute outcome letters, and they defaulted to emailing us. Fin needs to be capable of resolving the full query before merchants will trust it as a replacement.   
* **Channel shift was limited despite AM engagement**: Even with active Account Manager support and briefing sessions, email to Fin channel shift was modest (2.2% to 9.6%).   
* **Internal communications on the merchant side are a bottleneck**: Ops teams don't always receive or act on messages from their own AMs.

## What this means

* Tier 1/large merchants will not move to Dashboard chat without enforcement – enforcement at this size of merchant carries satisfaction/quality of service risk vs other PSPs.   
* The recommended compromise is to meet these merchants on email, not to push them off it (Fin's resolution cost is also the same on email as on chat).   
* We highlight Dashboard self serve in these emails to help awareness and drive usage  
* Deploying Fin on email for this segment is not a compromise, it is the right mix of our solutions and where they are working in our channel strategy.  
* For smaller merchants (Tier 3 / Bronze), the picture is different: smaller teams, less operational complexity/tooling, and less dedicated AM support mean enforcement toward Dashboard is feasible and appropriate.

## Recommendation:

1. **Deploy Fin on email for Premium and Enterprise merchants (meet in middle):** Deploy widely on email (with some edge case exceptions) and enable Fin to address payment queries securely over email with authentication. It is the only lever that reaches the majority of contacts (70%+ email mix) from this segment where they actually are. We then pass more volume through Fin and get more insights on what needs to be done to increase its resolution rate.  
2. **Enforce Dashboard / Fin chat for Standard merchants (Tier 3–5 / Bronze):** These merchants do not have the traits that make email entrenchment inevitable, with smaller teams to manage and better ROI from us to streamline support. Routing them to Fin chat is feasible and directly improves our overall Fin involvement rate. This does not mean a drop in quality of support, but drives more efficiency here which allows us to scale these types of merchants in future.  
3. **Address the gaps that blocked Fin adoption in the pilot:** Scheme dispute letter access was a specific gap mentioned. We will be reporting on contact reasons and build a feedback mechanism to push these to product teams to solve.  
4. **Work with Dashboard team on increasing Awareness & self serve:** Working on Projects in H1 such as Welcome Pack for new merchants, Tutorials and Video content and resources for Commercial teams about Dashboard functionality.

These Insights/Recommendations are informing the [Involvement rate plan.](?tab=t.covb64tt2z67)

## Results with Fin – pre/post pilot

| Merchant | Fin channel uplift % since pilot | Fin conversations | Fin resolution rates | Escalated issue types |
| :---- | ----- | ----- | ----- | :---- |
| eToro | 0.0% → 21.2% | 7 | 100% |  |
| Plus500 | 0.0% → 36.6% | 34 | 91% | Bank Payouts, Card Payouts |
| Sibilla | 0.0 → 4.8% | 6 | 83% | Transaction Status |
| Wise | 13.3% → 2.1%  (Pre-pilot: 2 fin ÷ 15 total = 13.3%  Pilot: 1 fin ÷ 48 total = 2.1%) | 1 | 100% |  |
| Bytedance | 0.0% → 1% | 1 | 100% |  |
| Vinted | 0.0% → 0.8% | 1 | 100% |  |
| **Overall** | 2.2% → 9.6% | 50 | 92% | Bank Payouts, Card Payouts, Transaction Status |
