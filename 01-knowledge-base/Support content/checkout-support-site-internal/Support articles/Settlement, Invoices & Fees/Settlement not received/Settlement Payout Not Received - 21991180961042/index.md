---
id: 21991180961042
section_id: 21991150886162
title: "Settlement Payout Not Received"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/21991180961042-Settlement-Payout-Not-Received"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:33:45Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHQKPVKA7XAZRYSRWE7JRH4", "01K44R8EENFFHF2FYFY7H371ZN"]
label_names: ["case_settlements", "case_settlements_issue_settlement_not_received", "issues_with_payouts_done_by_CKO"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

To diagnose a _payout not paid _issue, which is often caused by a high settlement threshold.

Problem/Symptom: Payout not paid, payout returned or payout pendingINTRODUCTION TO SETTLEMENT PAYOUTS NOT RECEIVED 💬

This article explains how to diagnose and resolve issues when a merchant has not received a settlement payout. 

This issue can be caused by a few different scenarios, including a high payout threshold, a returned payout, or a pending payout. A "payout" refers to the final step where funds from a customer's transaction are transferred from the acquiring bank to a merchant's business bank account.PROCESS STEPS TO DIAGNOSE & RESOLVE🖊️
 

## Scenario 1: Payout Not Paid Due to High Threshold

This often occurs when a merchant's settlement amount hasn't reached a specific threshold amount set in the system. If a high threshold is set, a payout will not be automatically triggered, even if a settlement is due. 

⚠️  For example, if the threshold is GBP 1000 and the settlement is GBP 950, the funds will not be paid out

- Log in to the Client Admin Tool (CAT) and search for the merchant by name:

- 
**Select the correct entity** for which the missing payout was reported

- In the left navigation panel, select Payout Schedules

- Choose the currency account that was reported as not paid:

- Check the **Threshold** **amount** field:

- If you see a high number (e.g 1,000,000,000), it means that an automatic payout will not be triggered until that amount is reached

**⚒️ Resolution**

If a payout threshold is present, you must determine why it was put in place before you can remove it.

- 
**For Tier 1, 2, 3, or 4 managed accounts: **Contact the Account Manager to understand the reason for the threshold

- 
**For Tier 4-unmanaged accounts: **Contact the Merchant Configuration team directly

- If the Risk team is responsible, use the Zendesk transfer macro to contact them and ask them to liaise with the merchant to get the issue resolved

 

## Scenario 2: Payout Returned

A payout is returned when the funds are sent back to Checkout.com, typically due to incorrect bank account details.

- Log in to the Merchant Portal and go to **Business** **account** > **Settlements**

- In the **Status** column, check if the payout is marked as Returned

**⚒️ Resolution**

- Use the transfer macro to contact the Treasury team to get more details on why the funds were returned

- If the return was due to incorrect details, the Treasury team will ask Merchant Care to update the account information

- The Treasury team will then force a new payout, and the funds will be settled on the merchant's next available settlement date

 

## Scenario 3: Payout Pending

A pending payout is a payout that has been initiated but has not yet been settled with the merchant's bank account. This status indicates that the funds are in transit and the payment process is still ongoing.

Follow these steps to identify a pending payout and check the payout frequency:

- Log in to the Merchant Portal and go to Business account > Settlements

- Check the Status column to see if the payout is marked as Pending

- To confirm the next scheduled payout date, go to the Merchant Portal Dashboard > Settings menu > Bank settlements

- The system will display the next scheduled payout day

**⚒️ Resolution **

- Inform the merchant that their payout is pending and is expected to be paid out on the next scheduled payment cycle

 

## Glossaries and Definitions:

For **Key Terms and Definitions** on Transactions as well as an **introduction into MENA Gateway and non-Gateway merchants**, please see ****[Settlements Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/21991207693458-Settlements-Glossary-Introduction)   

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Transactions articles, please see ****[Settlements Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/21991176789266-Settlements-Tools-Permissions)
