---
id: 26958171063826
section_id: 26832912736274
title: "Response code 20057-Transaction not permitted to cardholder"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/26958171063826-Response-code-20057-Transaction-not-permitted-to-cardholder"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-07-18T13:47:32Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JVS26PBA73NGJJETCPWS3SPE", "01JVS27ERFT6CA591PZY4AV4SZ", "01JW5VVF5AVK1PT33CHX741DHR", "01JWG4DMWCF44JCTX1F5HXERC4"]
label_names: ["card_payout", "scheme_declines"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

For transactions declined with response code **20057**. This error means the customer's bank has blocked the payment because that type of transaction is not permitted on the cardholder's account.

This article shows you how to confirm this issue in the logs and what advice to give the merchant.

 

## DESCRIBE THE ISSUE 💬

Payment declines that have the response code **20057: Transaction not permitted to cardholder** indicates that the customer's issuing bank has blocked the transaction due to a specific restriction on their card or account. This is a direct decline from the bank, not an error with our platform.

- 
**Problem/Symptom:** A merchant reports that a customer's payment has failed. Transaction logs show response code 20057.

This issue directly impacts payment processing and affects both the cardholder and the merchant.

 

## PROCESS FOR RESPONSE CODE 20057 DECLINE  🖊️

This process outlines the steps to diagnose and inform the merchant about a transaction declined with response code 20057.

### Step 1: Access Transaction Logs

- Using the `correlationID` for the failed payment, access the transaction logs in one of the available tools (****[Data Dog](https://app.datadoghq.com/dashboard/j2p-zgh-7x5?fromUser=false&refresh_mode=sliding&from_ts=1747895167843&to_ts=1747898767843&live=true) is recommended). You can also use ****[Traffic Insight](https://retoolprod.mgmt.ckotech.co/apps/a04c8c20-72cf-11eb-bea4-e7bba7ba05e6/payment-performance-shared-debug/Traffic%20Insights#payment_id=), or ****[Sherlock](https://retoolprod.mgmt.ckotech.co/apps/918d2a72-4c5a-11ec-88dc-53fd2c6a4170/gateway/Sherlock) to access the logs for the declined transaction.

  - 
**Filter:** `correlationID` 

  - 
**Source:** `card-processing`

  

### Step 2: Identify the Response Code

- In the card processing logs, locate **data element 38**

- 
This element will contain the response code. Confirm that the code is **57**. This verifies the decline reason is "Transaction not permitted to cardholder."
  
  

- Review the **Recommendation Code** as well. This provides more detail from the issuing bank. Common reasons include:

  - The account is closed

  - There is a suspected fraud alert

  - 
A recurring payment agreement was cancelled
 

## RESOLUTION 🛠️

### Step 3: Advise the Merchant

Communicate your findings clearly to the merchant

- Inform them that the decline (response code 20057) is from the customer's bank and not a platform error

- Explain that this means the transaction type is not allowed for that specific card or account

- Share the **Recommendation Code** and its meaning to provide more context

- Advise the merchant to ask their customer to either:

  - Contact their bank for more details about the restriction

  - Use an alternative payment card

✅ **Best Practice:** Frame your explanation clearly to help the merchant understand that you have investigated the issue and confirmed the source of the decline. This builds trust and helps them communicate effectively with their customer. 

## ESCALATION ⏫

In most cases, this issue is resolved by the cardholder contacting their bank or using a different card. An escalation is not typically needed.However, if the merchant has strong reason to believe the issue is on our end despite your findings, you can escalate the case.

- 
**When to Escalate:** The merchant continues to believe there is a platform error after you have presented the evidence from the transaction logs.

- 
**Who to Escalate to:** Support L3

- 
**Information to Include:** Provide the `correlationID`, your findings from the logs, and a summary of your communication with the merchant.

## FAQs ❓

What is response code 20057?It is a decline code from a customer's issuing bank that means the attempted transaction is not allowed for that specific card or account. Is this an error with our platform?No, this is a direct decline from the customer's bank. Our systems have successfully sent the payment request, but the bank has rejected it. What is the difference between a "decline" and an "error"?A decline is a deliberate rejection of a transaction by the customer's bank or the payment processor. An error typically refers to a technical issue (a system timeout or misconfiguration) that prevents the transaction request from being processed at all. Can the customer try the same card again?While they can try again, it will likely fail for the same reason. The underlying restriction on their account must be addressed by contacting their bank. Using a different card is the quickest solution.
