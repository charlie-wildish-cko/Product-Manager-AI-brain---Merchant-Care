---
id: 30191736717458
section_id: 21991135458066
title: "Understanding Tiered Pricing"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/30191736717458-Understanding-Tiered-Pricing"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-16T13:38:27Z"
permission_group_id: 26838654181266
content_tag_ids: []
label_names: []
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

To understand how Checkout.com's tiered pricing works, including how fees are calculated, applied, and adjusted.

## INTRODUCTION TO TIERED PRICING💬

Checkout.com’s tiered pricing model is a volume-based system designed to provide better rates to merchants as their processing volume increases. The model is applied to various fees, including those for card processing, authentication, and fraud detection. It operates on a **prospective** and **retrospective** basis, calculated on a UTC calendar month.

- 
**Prospective Application:** At the beginning of the month, the tier achieved in the _previous_ month is used to calculate fees on all new transactions.

- 
**Retrospective Adjustment:** At the end of the month, the total processing volume is reviewed. If the merchant's volume qualifies them for a different tier, a retrospective adjustment (a debit or credit) is applied to their account.

Related article: [Tiered Pricing Fee Calculation](https://checkoutint.zendesk.com/hc/en-us/articles/29392710165010-Tiered-Pricing-Fee-Calculation)

 

## KEY TAKEAWAYS 🔑

**It's dynamic:** Tiered pricing is not static; it adjusts retrospectively based on the merchant's actual monthly processing volume.

**Adjustments are calculated retroactively:** The system applies a rate prospectively, but then calculates a final adjustment (a credit or debit) at the end of the month based on the total volume for that period.

**Net volume matters:** For variable fees, processing volume is measured **net of refunds and chargebacks**, which encourages "good" volume.

**FX rates are specific:** When currency conversion is needed, a specific, non-marked-up midnight FX rate is used for the calculation.

**Manual solutions are an exception:** The automated tiered pricing solution is the default, and keeping a merchant on a manual solution requires a thorough justification and senior leadership approval.

 

## HOW TIERED PRICING ADJUSTMENTS WORK 🖊️

**Prospective Rate Application:** All transactions at the start of a billing period (a calendar month) are charged at the rate corresponding to the tier the merchant achieved in the prior month.

**Volume Measurement:** Throughout the month, the system measures the merchant's processing volume. This is based on either the number of transactions (for fixed fees) or the total transaction value **net of refunds and chargebacks** (for variable fees).

**Retrospective Tiering:** On the first day of the new month, the total volume is evaluated to determine the tier the merchant actually achieved for the previous month.

**Adjustment Calculation:** A tiered pricing adjustment is calculated as the difference between the total fees initially charged at the prospective rate and what should have been charged at the final, achieved tier rate.

**Rebate or Charge Application:** This adjustment is applied as a credit (rebate) if the merchant's volume moved them to a lower fee tier, or as a debit (charge) if they moved to a higher fee tier. **Crucially, the new tier applies to all processing for the entire billing period, not just the volume that tipped them into the new tier.**

 
 

## FAQs** ****❓**

Where can I see the tiered pricing adjustments?They appear as a credit or debit in Financial Action Reports and are shown as a single line item on the merchant's invoice under "Previous Period Tiered Pricing Adjustments."How do I find a merchant's current tier?You can find the current tier by checking the fee being applied in CAT. For a precise check, go to the pricing page in CAT and view the fee in the Card Scheme section.Can different entities under the same client have different fees?Yes, the client-level volume determines the overall tier, but the rebate or charge is applied to each individual entity based on its own volume and fee structure.

## 

Are tiered pricing adjustments taxed?Yes, adjustments are subject to local tax rates if the entity operates in a jurisdiction where this is applicable.How are FX rates handled in the calculation?If transactions are in a different currency than the tiered pricing ranges, they are converted using a **midnight rate** from a source like OpenExchange on the first day of the month when the calculation is run. No markup is applied.
