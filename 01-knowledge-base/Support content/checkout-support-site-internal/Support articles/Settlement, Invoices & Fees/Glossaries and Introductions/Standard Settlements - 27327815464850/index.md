---
id: 27327815464850
section_id: 21991151260690
title: "Standard Settlements"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/27327815464850-Standard-Settlements"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-07-18T13:47:36Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHQKPVKA7XAZRYSRWE7JRH4"]
label_names: []
user_segment_ids: [11003606966930]
archive: false
---

Use this article to understand the upcoming changes to how merchant balances and financial reports display funds, these take effect from 01/09/2025.

 

## INTRODUCTION TO STANDARD SETTLEMENTS 💬

Currently, all funds land in the 'Available' balance right away, which makes it difficult for merchants to know what their incoming settlements will be without building reconciliation logic. To improve the Merchant experience we're making some changes! 

Funds and fees related to transactions will now show as 'Pending' in balances during the period between a sale and settlement. They'll only switch to 'Available' when they're truly ready for settlement.  

Our financial reports are also getting an update to reflect these Pending and Available balance movements, and some might even have new fields! We've got all the details for the Merchants, including how rolling reserves and funds pooling are affected, on our [support site.](https://support.checkout.com/hc/en-us)

 

_**Note: **While the settlement batch will continue to be made up of captures from Day 0, we may apply fees, reserves, and other adjustments to the Available balance that will affect the final settlement amount._

 
 
**KEY TAKEAWAYS 🔑**

 
 

- 
**Clearer View of Funds**: This change means merchants will have a much clearer picture of the funds that are genuinely ready to hit their bank accounts. Only funds that are ready for payout will appear in the 'Available' balance.

- 
**Introducing 'Pending' Balance**: Funds and fees from transactions will initially appear in a 'Pending' balance. They'll only move to 'Available' once they're ready to be settled.

- 
**Report Updates**: Financial reports will now show movements in both 'Pending' and 'Available' balances. Keep an eye out for new report fields!

- 
**Impact on Chargebacks and Refunds**: Good news! Chargebacks and refunds will now be funded from the 'Pending' balance instead of 'Available', so it won't mess with a merchant's ability to handle these.

- 
**No Change to Settlement Times**: The timing of when merchants receive funds in their bank accounts won't change.

- 
**Who's Affected**: This first phase applies to all entities _not_ based in APAC and those _not_ using Bank Payouts, Card Payouts, or Issuing solutions. These specific groups will transition later in the year.

- 
**Prepare for Report Changes**: Merchants might need to update any automatic reconciliation processes if they're based on our current report format. We've got examples of the old and new reports on our support site to help them out!

 

## RESOURCES **📍**

 

| Related Links |
| --- |
| [Merchant Comms & Support Material](https://docs.google.com/document/d/1nuRbJfeIwd14J8cEq7HqtIz-3R_SsPni/edit?usp=sharing&ouid=116646008491128357680&rtpof=true&sd=true) |
| SOP links here |
| Training Links here |

 

## ESCALATION** ⏫**

If you encounter any questions or issues that aren't covered here, or if a merchant needs more in-depth assistance, please:

 
 

## FAQs** ****❓**

 
Why are we making these changes?We're doing this to give our merchants a clearer view of the funds that are truly ready to arrive in their bank accounts. Only funds that are ready for payout will show in their 'Available' balance, making it much easier for them to predict what they'll receive from us!

 

 
What exactly is the 'Pending' balance?

Think of the 'Pending' balance as all the incoming funds that haven't quite cleared yet, minus any refunds, chargebacks, and fees. 

Once those funds clear, they'll smoothly move into the 'Available' balance after a short, fixed delay.

 

 

 
How is 'Pending' different from 'Available'?Great question! The 'Pending' balance is the total sum of incoming funds that are still clearing, after we've taken out any refunds, chargebacks, and fees. Once they're cleared, they shift into the 'Available' balance. The 'Available' balance, is the money that's ready to roll for outgoing transactions, like payouts, transfers, or settlements to their bank account. This balance is always changing as funds clear from 'Pending'. 
Will this affect how we fund chargebacks and refunds?Instead of taking funds for chargebacks and refunds from the 'Available' balance, we'll now fund them from the 'Pending' balance. This won't impact a merchant's ability to fund those or make refunds to customers. 
Can merchants see how their reports are changing?

They can head over to our support site to check out examples of both the old and new reports. We've put them there to help them understand what's coming!

 

 
What do merchants need to do to get ready?We recommend they take a look at the materials on our support site to understand how these changes will affect their reports, balances, and reserves. Since we're tweaking the report structure, they might need to update any automated reconciliation processes they have set up.

 
Will the time they receive funds in their bank account change?

No, good news here! There won't be any change to the time when we make settlements to them.

 
When do these changes begin?These changes will start from September 1, 2025. The merchant's Account Manager will reach out to confirm the exact date for them. 
Who is affected by these changes?

In the first phase of the project, we will be making these changes for all Entities that are **not**:

- Based in APAC. This is because downstream changes to our settlement model are planned during later phases. These changes will require merchants to update their settlement time zone to align with local banking cut-off times, and we are releasing an enhancement in Q3 allowing these merchants to decouple their settlement time zone from their reporting time zone, where required for reconciliation processes

- Using Bank Payouts, Card Payouts, or Issuing. As we are going to be showing funds and fees related to transactions as Pending in balances, instead of Available, we are going to implement funding from the Pending balance for Issuing and Card Payouts merchants, and reaching out to merchants to configure a minimum balance for Bank Payouts

- Set up with early payment cutoff times where same-day execution of settlements is not possible 

__Note: To prepare for these changes, we’re making an update from August to move transactions to the available balance shortly after midnight, instead of throughout the day. This will only affect merchants with a settlement speed greater than T+0.__ 
What are the impacts on merchants?

- 
**Balances: **Funds will now only transition to Available when they are ready for settlement. During the period between a sale and transactions being ready for settlement, we’ll show the funds and fees applicable to transactions as Pending in our [balances](https://www.checkout.com/docs/funds-management/manage-funds/balances/fixed-and-rolling-reserves).

- 
**Reports: **Our financial reports will now show funds movements in the Pending balance and the Available balance, in some cases this may mean the reports include new report fields.

We’ve published a full list of the changes on our support site. These include an overview of how balances will change, samples of new reports, and the impacts on rolling reserves and funds pooling, where applicable.
