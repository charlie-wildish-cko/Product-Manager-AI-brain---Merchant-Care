---
id: 21991138241682
section_id: 21991144652050
title: "How to Check Why a Payment Hasn't Settled"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/21991138241682-How-to-Check-Why-a-Payment-Hasn-t-Settled"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-09-18T18:14:54Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHQKPVKA7XAZRYSRWE7JRH4"]
label_names: ["case_settlements", "case_settlements_issue_have_i_been_settled_for_this_payment", "card_schemes", "payment_not_settled"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

To investigate why a payment has not been settled and determine the correct course of action, including when to contact the Payments team.

**Problem:** A payment has not been settled

**Solution:** Investigate the payment status and troubleshoot based on the findings

 

## DESCRIBE THE ISSUE 💬

Merchants may contact support because a payment they expected to be settled has not appeared in their bank account. They need to understand why the settlement has not occurred and what steps they can take to resolve the issue. 

Settlement is the final stage of a payment transaction. It occurs when funds from a captured payment are successfully transferred from the customer's bank to the merchant's bank account. This process confirms that the merchant has received and can access the funds.

Settlement typically follows a **T+X** schedule, where **T** is the transaction's capture date and **X** is a specific number of business days. If the settlement day falls on a weekend or bank holiday, it is postponed to the next available business day.

 

You can check the risk level-captured arrears on the Client Admin Tool under the ‘Arrears configuration’ section

 

## KEY TAKEAWAYS 🔑

- 
The settlement process follows a T+X schedule, where "T" is the capture date and "X" is the number of business days
⚠️ A "Gateway only" processor means the merchant must contact their acquirer directly for settlement issues
 

## PROCESS FOR INVESTIGATING UNSETTLED PAYMENTS 🖊️

Step 1. Investigating using the Agent Toolkit or Looker

**Method 1. Check Settlement Status using the Checkout Agent Toolkit (Visa and Mastercard)**

1. In Zendesk, open the **Checkout Agent Toolkit** under `Apps`

2. 
Enter the `Payment ID` and click on it to open the payment details

3. 
Click on `Clearing events`

4. Scroll down to the `Clearing` section. If the event type `PresentmentSettled` is visible, the payment has been settled

**Method 2. Check Settlement Status using Looker**

1. Go to the [FTS folder in Looker](https://checkoutinternal.eu.looker.com/folders/2347)

2. Select the ``[NAS Transaction Details by Payment ID dashboard](https://checkoutinternal.eu.looker.com/dashboards/7480?Payment%20ID=&Processed%20on%20Date=&Client%20Name=&Client%20ID=&Entity%20ID=&Entity%20Name=)

3. 
Enter the `Payment ID` in the designated field and click `load`

4. 
In the results, a settled payment will have a `Payout Reference` and settlement date - If these are blank, the payment has not been settled

 
Merchant Self-Serve Access to Settlement Statement
💡 The merchant can use the **Payout Reference** to find the settlement statement in their Merchant Portal by navigating to **Business account > Settlements**, entering the reference in the search bar and clicking **Search**.

**Step 2. Check for a Negative Account Balance or High Threshold**
A negative balance on the merchant's account or a high threshold on their payout schedule may prevent settlement. See the articles below for information on how to check this:

- [How to Identify and Reconcile a Negative Balance](https://checkoutint.zendesk.com/hc/en-us/articles/29350197272466-How-to-Identify-and-Reconcile-a-Negative-Balance)

- [How to check for a high threshold](https://checkoutint.zendesk.com/hc/en-us/articles/21991189393042-How-to-Check-for-a-High-Threshold)

- If there is no negative balance or a high threshold, proceed to step 3

**Step 3. Contact the Payments Team**
If there is no negative balance and the standard settlement timeframe has passed, contact the Payments team.

- Use the relevant regional **Treasury Payments** macro to create a side conversation in Zendesk from the merchant’s ticket

 

## ESCALATION** ⏫**

 
**Situations requiring escalation:**

- The standard settlement timeframe has passed, the payment is still not settled, and there is no negative balance or high threshold on the merchant's account

- You have confirmed that a payment is not settled and need assistance from the Payments team

**Required information to include:**

- Create a side conversation in Zendesk from the merchant's ticket using the relevant regional **Treasury Payments** macro

- Provide the Payment ID(s) and any relevant transaction details

**Instructions for the agent:**

- Stay on the case and monitor the side conversation for updates from the Payments team

- Notify the merchant of the escalation and provide a timeline for a response

 
 

## FAQs** ****❓**

What is settlement?Settlement is the final step in a payment transaction where the captured funds are successfully transferred from the customer's bank to the merchant's bank account.What does a T+X schedule mean?A T+X schedule means that settlement happens "X" business days after the transaction's capture date, which is "T". If a settlement day falls on a weekend or bank holiday, it's moved to the next business day.What should I do if the processor is "Gateway only"?If the processor is "Gateway only," advise the merchant to contact their acquirer directly. In this case, the acquirer is responsible for managing their settlements.
