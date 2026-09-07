---
id: 21991163520914
section_id: 21991120367762
title: "How to Check for a Transaction Mismatch on MPGS"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/21991163520914-How-to-Check-for-a-Transaction-Mismatch-on-MPGS"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-09-24T09:50:40Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHQKPVKA7XAZRYSRWE7JRH4"]
label_names: ["case_settlements_issue_general_adjustments", "case_settlements", "mena", "transaction_mismatch_between_mpgs_and_dashboard"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

To check the true status of a payment for a MENA merchant who uses **Mastercard Payment Gateway Services (MPGS)** to process transactions. You should use this procedure when a transaction is marked as **Failed** in the Dashboard, but the customer's card was charged.INTRODUCTION 💬 

Sometimes, a merchant may report that a transaction appears as **Failed** on their Dashboard, but the customer confirms their card was charged. This can happen with gateway merchants who use Mastercard Payment Gateway Services (MPGS) to process payments. 

In these cases, it's crucial to check the true status of the transaction on MPGS, as the merchant may have already received the settlement from their bank. 

⚠️You cannot change the transaction status in the Dashboard, but you can advise the merchant on the correct next steps once you have the true status.PROCESS TO CHECK THE STATUS OF A PAYMENT ON MPGS🖊️
Step 1: Gather Necessary Credentials

- In Retool, go to Traffic Insights and search for the Payment ID provided by the merchant

- Scroll down to the Associated IDs section

- In the ChargeRequested row, click the second link to open the logs in Datadog.

- In Datadog, click on card-processing > Mpgs Authorisation API

- On the new screen, scroll down to find the Merchant ID, Token and Order ID

Step 2: Check the Transaction Status in Postman

- Open Postman and insert the **Merchant ID**, **Token**, and **Order ID** under the **Authorization** tab

- In the **Get API URL**, replace the placeholder values with the relevant **Merchant ID** and **Root Transaction ID** from the Datadog logs

- 
Under the **User details**, fill in the following:
**Username:** `merchant.[your Merchant ID]`
**Password:** `[your Token]`

- Click **Send**

Step 3: Interpret the Result

- Scroll down to the **Status** section of the response to see the true status of the transaction

- If the status is **Captured: **This means the customer was charged, despite the Dashboard showing the transaction as Failed.

  - You don't need to make any adjustments

  - Advise the merchant to either refund the customer or take no action if the service was delivered, and direct them to their acquirer

- If the status is **Failed**: This confirms that the customer was not charged. Inform the merchant that no action is required

## 

FAQs**❓**

 Why would the Dashboard show a transaction as 'Failed' if it was successful on MPGS?

This can happen when there's a disconnect or delay in the data feed between the payment gateway (MPGS) and the Dashboard. 

The true status is always reflected by the payment gateway itself, as that's where the actual charge occurs.

 

 Can I change the transaction status in the Dashboard?No, you cannot change transaction statuses on the Dashboard. The purpose of this procedure is to determine the true status and then advise the merchant accordingly.

 Do I need to make an adjustment or refund the customer if the transaction status is 'Captured'?No, you do not need to make an adjustment. If the service was delivered, the merchant should take no action. If the service was not delivered, the merchant should process a refund through their acquiring bank.

## 

##
