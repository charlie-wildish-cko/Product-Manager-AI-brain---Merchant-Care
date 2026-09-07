---
id: 27670854734610
section_id: 21991120809362
title: "Response code 20012/ 20030"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/27670854734610-Response-code-20012-20030"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-03-18T13:33:09Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JYR94X1AAD1RXB70G1YJWXCT"]
label_names: ["ROW", "response_code_20012/20030", "card_processing", "scheme_declines"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

When a merchant reports that they are unable to void a transaction, follow these steps to diagnose and resolve the issue.

This guide will help you determine if a failed void is due to an expired authorization and provides the correct steps to inform the merchant.

**Case Type: **Payments In

**Issue Type: **Transaction Status (non 3DS & Refunds)

**Reason:** Declined/Failed Action

## DESCRIBE THE ISSUE 💬

This article addresses the issue of a transaction failing to be voided. This can occur when the authorization hold, placed on a customer's card at the time of purchase, has already been released by the card issuer (the customer's bank). 

This automatic release happens after a set period known as the authorization validity period. 

## PROCESS FOR RESPONSE CODE 20012, 20030 🖊️

### Step 1: Check the Authorization Validity Period

The first step is to determine if the void attempt is happening after the allowed timeframe.

- Open the ****[Authorization Validity Period](https://www.checkout.com/docs/payments/manage-payments/authorize-a-payment#Authorization_validity_period) documentation

- Review the tables provided to find the validity period for the specific card scheme used in the transaction

- Compare the date of the original authorization with the date of the void attempt

**RESOLUTION** 🛠️

### Step 2: Analyze Your Findings and Respond

Based on whether the void attempt is within the validity period, follow the appropriate path below.**If the void period HAS expired:**

This is the most common reason for a failed void. The issuing bank has automatically released the hold on the funds.

- Inform the merchant that the void failed because the authorization validity period has expired.

- Explain that the hold on the funds has likely been released automatically by the customer's bank.

- Advise the merchant to confirm with their customer if the funds are now available in their account.

- Provide the merchant with the **Retrieval Reference Number (RRN)** of the transaction.

💡 **Tip:** The RRN is a unique 12-digit code that helps the customer's bank trace the specific transaction if they have trouble locating the released funds.**If the void period HAS NOT expired:**

If the void attempt is still within the valid timeframe for the card scheme, the issue requires further technical investigation.

- Using the Zendesk Macro: Transfer the case to **L2 - Card Processing** for further investigation. [The L2 team will then use the transaction failures 20030 article](https://checkoutint.zendesk.com/hc/en-us/articles/21991193143314) to investigate 

**FAQs ❓**

 What is an authorization hold?

An authorization hold (or pre-authorization) is a temporary hold placed on a customer's funds when they make a purchase. It ensures the customer has sufficient funds to complete the transaction, which are then captured later.

 What is a Retrieval Reference Number (RRN)?

A Retrieval Reference Number (RRN) is a unique identifier assigned to a card transaction. It allows the merchant and the customer's bank to locate and track a specific transaction throughout its lifecycle.

 Why can't a transaction be voided after the authorization expires?

A void cancels an authorization _before_ the funds are captured. Once the authorization hold expires, the issuing bank automatically releases the funds back to the customer. 

At this point, there is no active authorization to void. If the merchant still needs to return funds after this period, they will need to perform a refund instead of a void.

 

**RESOURCES**

For **Key Terms and Definitions** on Transactions as well as an **introduction into MENA Gateway and non-Gateway merchants**, please see ****[Transactions Glossary](https://checkoutint.zendesk.com/hc/en-us/articles/21991201065106-Transactions-Glossary-Introduction)**.  **
 
 
 
 
 
 
 
 
 

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Transactions articles, please see ****[Transactions Tools & Permissions](https://checkoutint.zendesk.com/hc/en-us/articles/21991176883474-Transactions-Tools-Permissions)**.**
