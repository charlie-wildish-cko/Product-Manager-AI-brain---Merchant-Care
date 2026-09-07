---
id: 21991193143314
section_id: 21991163883410
title: "Transaction Failures - 20030"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/21991193143314-Transaction-Failures-20030"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-12-09T12:56:55Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQT889RQXXSG27BB4ZJ0M", "01JVM5C9HVPQ6NTQTZA7FKEFT7", "01JVS26PBA73NGJJETCPWS3SPE", "01JYR94X1AAD1RXB70G1YJWXCT"]
label_names: ["case_transactions", "case_transactions_issue_transaction_declined_reason_response_codes_unclear", "MENA", "Transaction_Failures_20030", "card_processing", "internal_decline"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

For information on how to troubleshoot specific transaction failures in the Middle East and North Africa (MENA) region with the decline codes 20030, 20068 and 20091

## DESCRIBE THE ISSUE 💬

Merchants may contact support when they see unclear decline reasons or response codes. This article focuses on three common codes associated with transaction failures, particularly for refunds: 20030, 20068, and 20091.

The primary focus of this guide is to identify and resolve failures related to MADA card transactions, which are common in Saudi Arabia.

[This article](https://www.checkout.com/docs/developer-resources/codes/api-response-codes#20xxx_-_SOFT_DECLINE) covers decline response codes across all regions. 

## PROCESS FOR TRANSACTION FAILURES 20030, 20068 & 20091 🖊️

This process will help you determine if a failed transaction, especially a refund, is due to limitations on MADA cards.

### Step 1. Check if the transaction is a MADA transaction

MADA is a domestic payment network in Saudi Arabia. Transactions made with MADA cards have specific rules that can cause failures if not followed. The most common failure is a refund that has been attempted too late.**Method 1: Using Checkout Agent Toolkit**

- Open your ticket in Zendesk

- In the Apps section on the right, expand the Checkout Agent Toolkit

- Select the relevant Payment ID on display

- Click on the Timeline tab to see the **charge.requested** gateway event

- The Details tab will have the card and scheme details

**Method 2: Using the MADA BINs Sheet**

If you can't find the information in the Checkout Agent Toolkit, use this alternative method. A BIN (Bank Identification Number) is the first few digits of a card number.

- Go to the ****[MADA BINs Lookup Sheet](https://www.google.com/search?q=https://www.checkout.com/mada-bins) on the Checkout.com website

💡 **Tip:** This sheet is regularly updated by the Saudi network

- Find the BIN of the customer's card

- If the BIN is on this list, it confirms the transaction is a MADA transaction

### Step 2. Investigate the Cause of the Failure

The most common reason for a MADA refund to fail is the **30-day time limit**.

**For decline code **`**20030**`** on a refund:**

- Check the date of the original transaction (the authorisation date)

- Count the number of days that have passed since that date

- If more than 30 days have passed, the refund will fail, this is a hard rule for the MADA network.

**RESOLUTION** 🛠️

Once you've confirmed the refund failed because the 30-day MADA limit has passed, you have two options:

1. 
**Manual Refund (Internal Process):**

  - Process the refund manually by following the internal guide for [MADA 20030 refund failures](https://checkoutint.zendesk.com/hc/en-us/articles/21991182842386) follow the steps under 6.1.1.1

2. 
**Bank Transfer (Merchant Action):**

  - Advise the merchant that they can refund their customer directly via a bank transfer - this is often the quickest solution

✅ **Best Practice:** Clearly explain to the merchant _why_ the refund failed (the 30-day MADA limitation) and provide them with the two resolution options.

### Handling "Not a MADA Transaction" Errors

This process helps determine the source of the error and the next steps for resolution.
Step 1: Identify the Source of the Response Code

Determine whether the response code originated from the Issuing Bank, the Acquirer, or an Internal system.
Step 2: Action Based on Issuing Bank Error

If the response code is confirmed to be from the Issuing Bank:

- 
Recommended Action: Advise the merchant to instruct the cardholder/user to contact their Issuing Bank for clarification on why the transaction was declined or flagged as a format error.

  - _Note:_ Provide a standardized template for this communication to the merchant.

- Internal Investigation (If Cardholder Contact Fails): If the Issuing Bank's response suggests a systemic issue or the error is consistently reported, you may consider escalating to an L2 team for investigation into potential integration issues, or reaching out directly to the issuer for clarification on the specific format error.

Step 3: Action Based on Acquirer Error (Gateway-Only Checkout)

If the Checkout setup is Gateway (GW) only and the response code is from the Acquirer:

- Recommended Action: Advise the merchant to contact their Acquirer to resolve the issue.

- Regional Consideration: If the transaction is within MENA regions, verify the current policy. Sometimes, the internal team may initiate contact with the Acquirer directly to expedite resolution.

FAQs** ❓**

 What is MADA?

MADA is the domestic payment network for Saudi Arabia. It allows users to make payments with their local debit cards.

 Why do MADA refunds fail after 30 days?This is a specific rule set by the MADA network. All payment processors must adhere to this 30-day time limit for processing refunds on MADA card transactions.

 What should I tell the merchant if the 30-day limit has passed?

Inform them that the refund could not be processed through the original payment method due to the MADA network's 30-day policy. Advise them that the best way to refund their customer is through a direct bank transfer.

 Does this 30-day rule apply to all transactions?

No, this specific rule is for MADA transactions in the MENA region. Other card schemes and regions have different rules for refunds.
