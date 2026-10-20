# Fin renewal: sign 24 months, with the commit resized to our usage

**To**: VP of Product
**From**: Charlie Wildish
**Date**: 2026-10-12
**Topic**: Fin's Fin renewal quote expires 23 Oct 2026. We need a position on term, commit size and price lock before then.

**Strategy link**: Reduce cost of support (north star: cost per contact). Guardrail: Merchant CSAT. 2026 deliverable: AI First Resolution Using Fin. Flywheel domain: Orchestration.

---

## Summary

Our current Fin contract ($0.93 per resolution) runs to the start of July, but Salesforce's acquisition of Fin makes a price rise likely from Nov, and we assume $1.50 per outcome if we do not take Fin's renewal quote, which expires 23 Oct 2026. Over 24 months we expect ~359k outcomes, and the 24-month quote costs ~$378k all-in against ~$539k if we do not renew, but it commits us to 150k outcomes a year when we expect to use ~83k in year 1, so ~$57k pays for outcomes we never use. 

**We recommend signing the 24-month term with the commit resized to ~60k outcomes in year 1 and ~190k in year 2 (base case ~$321k all-in), auto-renewal removed, and an exit clause if the Zendesk integration stops working.**

---

## 1. The problem

- **Context: current contract and the Salesforce acquisition.** We pay $0.93 per resolution today, and the current contract runs to the start of July. Salesforce has acquired Fin, and Fin has flagged a price increase. The quote locks a lower price for the term. After it, we are exposed to whatever pricing Salesforce sets.
- **Fin is billed per outcome.** An outcome is a Fin resolution, or a procedure-based escalation where Fin hands off cleanly. The quote is for the renewal of the existing Fin contract.
- **Fin's quote.** 12 or 24 months, each committing 150k outcomes a year, at $0.89 (12 months) or $0.84 (24 months) per outcome, plus a fixed Pro (Conversations) add-on. Costs per option are in section 2. Order form detail is in Supporting data.
- **The commit is flat and annual.** 12,500 outcomes a month (150k a year) in both years. Unused outcomes do not carry forward at the end of the year. Outcomes above the commit bill at the unit price.
- **Our usage is back-loaded.** Year 1 usage is ~83k against a 150k commit. Year 2 is ~277k against 150k. Paying for outcomes we do not use in year 1 is where the cost risk sits.
- **The price risk is on the other side.** If we do not renew, we assume $1.50 per outcome. Any discount in the order form applies only for the term, and Fin can reprice at renewal.
- **A credit offsets the new contract.** Fin confirms a credit note of ~$37k on the current contract, which runs to the start of July. It can be offset against the new contract, so it applies to a renewal and not to walking away.
- **Fin stays either way.** A Fin resolution costs about $1 against $20-40 for a human contact, so the decision is how much volume we commit to and what price we lock in.

---

## 2. The options and what each costs

**Every cost in this section is all-in for 24 months (Nov 2026 to Oct 2028):** outcomes, plus the Pro add-on, minus the ~$37k credit on the three renewal options.

**Options at a glance (base case: ~359k outcomes)**

| Option                                                       | What we commit to             | Price per outcome                        | Pro add-on (fixed) | Credit | **All-in cost, base case** | All-in range across scenarios | Main risk                                                         |
| ------------------------------------------------------------ | ----------------------------- | ---------------------------------------- | ------------------ | ------ | -------------------------- | ----------------------------- | ----------------------------------------------------------------- |
| **A. Don't renew**                                           | Nothing                       | $1.50 (assumed)                          | Not quoted         | None   | **$539k**                  | $377k - $539k                 | Highest price, no lock. Any platform fee is unknown and excluded. |
| **B. 12 months, then renegotiate**                           | 150k outcomes in year 1       | $0.89 in year 1, $1.50 assumed in year 2 | $62k ($31k a year) | -$37k  | **$573k**                  | $449k - $573k                 | Year 2 reprices after the Salesforce change.                      |
| **C. 24 months as quoted**                                   | 150k outcomes a year          | $0.84                                    | $56k               | -$37k  | **$378k**                  | $308k - $378k                 | $57k-$78k of year-1 commit paid for but unused.                   |
| **D. 24 months, lower commit** (our counter, not yet agreed) | 60k in year 1, 190k in year 2 | $0.84, if Fin keeps the discount    | $56k               | -$37k  | **$321k**                  | $232k - $321k                 | Fin may reduce the discount for a smaller commit.            |

**How each base-case number is built**

| Base case (359k outcomes used) | A. Don't renew | B. 12 months | C. 24 months as quoted | D. 24 months, lower commit |
|---|---|---|---|---|
| Committed outcomes (paid upfront) | None | $134k (150k outcomes) | $252k (300k outcomes) | $210k (250k outcomes) |
| Outcomes above the commit (billed as used) | $539k (359k at $1.50) | $415k (year 2: 277k at $1.50) | $106k (127k at $0.84) | $92k (109k at $0.84) |
| Pro add-on | Not quoted | $62k | $56k | $56k |
| Credit | None | -$37k | -$37k | -$37k |
| **All-in total** | **$539k** | **$573k** | **$378k** | **$321k** |
| *Paid for but unused (already inside the committed cost)* | *None* | *$60k (67k outcomes)* | *$57k (67k outcomes)* | *None* |

**What "commit" means.** The commit is the number of outcomes we pay for upfront each year, whether we use them or not. Unused outcomes are lost at the end of the year. Outcomes above the commit bill at the same price per outcome. So a lower commit does not lower the price of the outcomes we use. It stops us paying for ones we do not use, and that is the whole $57k gap between C and D in the base case.

**All-in cost by scenario**

| Scenario                                                                  | B2B contacts | Ray contacts | Fin outcomes | A. Don't renew | B. 12 months | C. 24 months as quoted | D. 24 months, lower commit |
| ------------------------------------------------------------------------- | ------------ | ------------ | ------------ | -------------- | ------------ | ---------------------- | -------------------------- |
| **1. Base case:** forecast contacts, Fin at 60% end 2027 and 70% Oct 2028 | 270k         | 237k         | 359k         | $539k          | $573k        | $378k                  | **$321k**                  |
| **2. Fin plateaus:** Fin stays at 60% after end 2027                      | 270k         | 237k         | 340k         | $510k          | $545k        | $362k                  | **$305k**                  |
| **3. Ray late:** Ray starts 6 months later (Oct 2027)                     | 270k         | 122k         | 279k         | $418k          | $481k        | $326k                  | **$253k**                  |
| **4. Volume low:** B2B and Ray contacts 30% below forecast                | 189k         | 166k         | 251k         | $377k          | $449k        | $308k                  | **$232k**                  |
| **5. Fin plateaus and Ray late**                                          | 270k         | 122k         | 263k         | $394k          | $457k        | $312k                  | **$240k**                  |

Volume assumptions: contacts from the contact volume forecast, with Ray contacts starting Apr 2027. Fin resolves 40% of all contacts by end 2026, 60% by end 2027 and 70% by Oct 2028. Procedure-based escalations are 10% of contacts. Outcomes = resolutions + escalations.

**What this shows**
- **24 months is cheapest in every scenario.** C beats not renewing (A) by $69k to $161k, and beats 12 months (B) by $141k to $195k.
- **C pays for unused outcomes in every scenario.** We use 64k-83k of the 150k committed in year 1, so $57k-$78k is paid for and not used.
- **D removes that cost.** It saves $57k-$76k against C, provided Fin keeps the 15% discount on the smaller commit.

**Read with care**
- **Ray is a placeholder.** It is 48% of the 24-month outcomes and rests on a forecast built for Braavos with no real Ray data.
- **70% by Oct 2028 is the weakest input.** It means Fin resolves ~90% of the conversations it handles. The 40% start is below the leadership plan of ~50% in Q4 2026.
- **Replace the forecast with Fin's billed monthly outcomes before signing.** August shows ~5,000 Fin-handled tickets, which does not fit the forecast.
- **A excludes any platform fee.** If not renewing also carries a Pro-style fee, A costs more than shown.

---

## 3. When is this a good decision, and when is it bad

A good decision holds up across the futures we could land in, not only the base case. Judge it on three things: what it costs if we are wrong, what stays open, and what we will know later.

**Good decision if all of these hold**

| Condition | Why it matters |
|---|---|
| **Commit is sized to the downside, ~250k total** | Outcomes above the commit bill at the same price, so a lower commit costs nothing extra and removes $57k-$76k of unused commit. |
| **Auto-renewal is removed** | Agreed with Procurement in May and June. The draft order form has it back as "Yes". |
| **An exit clause covers the Zendesk integration** | Fin has put the Zendesk integration in "lights on" mode and has not confirmed its future. We should not owe unused fees if it stops working. Not in the draft. |
| **Overage rate is confirmed as the discounted ~$0.84** | The form says "subject to any applicable discounts" and gives no rate. |
| **We use the term to prepare for Oct 2028** | By Oct 2028 we run at ~29k outcomes a month, ~350k a year. At $1.50 that is ~$520k a year, against ~$295k at $0.84. |

**Bad decision if any of these happen**

| Trigger | Cost |
|---|---|
| **We sign as drafted:** 150k a year, auto-renewal on, no exit clause | $57k-$78k paid for unused year-1 outcomes, locked in again in Oct 2028, tied to the vendor if the integration breaks. |
| **We sign to meet the deadline without resizing the commit** | Same waste. The quote is better than not renewing, but the waste is avoidable. |
| **We take 12 months and year 2 reprices to $1.50** | $141k-$195k more than option C over two years. |
| **We do not reduce dependence on Fin before Oct 2028** | We face the same price cliff on ~350k outcomes a year instead of ~83k. |

**What would change the answer**
- If Fin will not keep the 15% discount on a smaller commit, the quote as written is still better than not renewing in every scenario. The waste is the price of the discount.
- If Ray is cancelled, year-2 volume falls to ~135k outcomes and the quote's commit is too high. Offer Ray's growth as the trade for a lower commit.
- If Fin plateaus below 50% through 2027, review at Jun 2027 whether Fin is still worth scaling.

**How to judge it later**: if volume falls short, the decision is not bad as long as the price lock, the resized commit and the exit clause were in. It is bad if we signed without them.

**Reviews after signing**: Mar 2027 (did Ray's beta start on time?), Jun 2027 (is Fin at 50% or above?), Jun 2028 (start the next renewal and have a fallback ready).

---

## Recommendation and ask

1. **Sign the 24-month term**, not the 12-month. Approve an all-in ceiling of ~$378k, which is option C in the base case. Walk-away is above that.
2. **Resize the commit** to ~60k outcomes in year 1 and ~190k in year 2 at the same discount. Fall back to the quote as written if Fin refuses.
3. **Make three conditions firm:** remove auto-renewal, add the Zendesk exit clause, and confirm the discounted overage rate in writing.
4. **Hold back the customer advocacy clause** (name, logo, case study, 4 reference calls) as something to trade for the commit resize.

---

## Open items before signing

- **Fin actuals.** Billed monthly outcomes and the handoff share, to replace the 10% escalation assumption and the forecast baseline.
- **The ~$37k credit.** Confirm in writing that it offsets either term, when it applies (year-1 invoice), and the exact amount. Ask what happens to it if we do not renew.
- **Pro (Conversations) definition.** 25,000 a month. Our contacts pass 25k a month in Q1 2028. Confirm overage rules.
- **Exit clause.** Page 6 of the draft is blank. Ask Procurement whether the clause sits in the master agreement.
- **Legal.** Review the advocacy clause before signing.
- **Ray.** Replace the Braavos-era forecast when Ray's own volume plan exists.

---

**Owner**: Charlie Wildish
**Next update**: After Fin responds to the counter-proposal, before 23 Oct 2026
**Questions to**: Charlie Wildish

## Supporting data: draft order form (Q-196698, dated 2026-10-09, expires 2026-10-23)

| | 12 months | 24 months |
|---|---|---|
| Outcomes, monthly quantity | 12,500 | 12,500 |
| Outcomes list price per outcome | $0.99 ($12,374.50 per month) | $0.99 |
| Outcomes discount | 10% | 15% |
| Outcomes total | $133,644.60 | $252,439.80 |
| Pro (Conversations), 25,000 a month | $30,948.00 (no discount) | $55,706.40 (10% discount) |
| Operator credits, 25,000 a month | Included | Included |
| **Grand total** (list: $182,442 / $364,884) | **$164,592.60** | **$308,146.20** |
| Billing | Annual in advance, wire, net 30 | Same |
| Auto-renewal | Yes (12-month periods, 30 days' notice) | Yes. To be removed. |
