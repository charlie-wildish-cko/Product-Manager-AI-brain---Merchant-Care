---
id: 21991162297234
section_id: 21991144652050
title: "Settlement is Suspended"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/21991162297234-Settlement-is-Suspended"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:33:45Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHQKPVKA7XAZRYSRWE7JRH4"]
label_names: ["case_settlements", "case_settlements_issue_have_i_been_settled_for_this_payment", "negative_balances", "settlement_suspended"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

To identify if settlement is temporarily suspended due to a negative balance. Although negative balances do not automatically block payouts, this can happen where they exceed a certain threshold.

Problem/Symptom: The merchant contacts us because settlement has been suspended

Solution: The negative balance must be cleared for settlements to resume

 This article applies to **NAS merchants only**INTRODUCTION TO NEGATIVE BALANCES 💬 

A negative balance occurs when the amount of money withdrawn or spent from an account exceeds the amount of money available in that account. This can happen due to various reasons such as fees, refunds, chargebacks or other transactions that exceed the available balance.

⚠️ For **MBC merchants, **you must contact the Payments team directly, who will perform the balance check and provide an update.PROCESS TO CHECK FOR A NEGATIVE BALANCE 🖊️

You can perform this check using either Retool or the Dashboard. Before you begin, review the ticket to find the correct currency, Currency ID or Entity ID. If this information is not available, you can ask the merchant to confirm which details to use for your search.

## **Check Negative Balance Using Retool**

- Navigate to **Currency Account Balances** in [Retool](https://retoolprod.mgmt.ckotech.co/apps/6840ab28-c4b7-11ec-909b-bf9c18a51b41/techfinance-finlab/Currency%20Account%20Balances)

- Follow the step that matches the information you have:

  - 
If you already have the Currency Account ID (e.g., ca_xxxxxxxxxxxxxxxx), enter it into the **Currency Account ID** field on the right-hand side and click Refresh:

- If you have the **Entity** **ID**, paste it into the **Entity ID** **field** and click **Refresh** to display all currency accounts associated with that entity:

- Click on the relevant account from the list to view the available balance on the right-hand side of the screen

- If multiple accounts appear and you are unsure which one to check, contact the Payments team for assistance

## **Check Negative Balance Using the Dashboard**

Both agents and merchants can use the Dashboard to check balances. You should educate the merchant on how to do this via self-serve:

- In the Dashboard, navigate to **Business** **Account** through the left panel and select **Balances**:

- The merchant’s balance is displayed under the **available** column, and if the balance is negative, it will be shown like so:
 RESOLUTION ✅To clear a negative balance and resume settlements, the merchant must add funds to their account through the Dashboard and clear the negative balance. See the external merchant-facing article [Add funds](https://www.checkout.com/docs/funds-management/move-funds/add-funds) to guide the merchant.After the merchant has completed the bank transfer, they should provide proof of payment to the Merchant Care team, who will forward this to the Treasury team. The Treasury team will then contact the Merchant Configuration team to remove the high threshold from the account, which will automatically resume settlements on the next scheduled settlement date.

| **Tools Needed** | **Related Articles** |
| --- | --- |
| [Retool](https://retoolprod.mgmt.ckotech.co/apps/6840ab28-c4b7-11ec-909b-bf9c18a51b41/techfinance-finlab/Currency%20Account%20Balances) | [Why is my available balance negative?](https://support.checkout.com/hc/en-us/articles/25574851882770-Why-is-my-Available-balance-negative) [Add funds](https://www.checkout.com/docs/funds-management/move-funds/add-funds) |

 

## Glossaries and Definitions:

For **Key Terms and Definitions** on Transactions as well as an **introduction into MENA Gateway and non-Gateway merchants**, please see ****[Settlements Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/21991207693458-Settlements-Glossary-Introduction)   For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Transactions articles, please see ****[Settlements Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/21991176789266-Settlements-Tools-Permissions)
