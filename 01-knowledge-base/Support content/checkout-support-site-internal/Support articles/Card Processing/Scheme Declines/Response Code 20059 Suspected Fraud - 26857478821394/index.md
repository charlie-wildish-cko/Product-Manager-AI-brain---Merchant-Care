---
id: 26857478821394
section_id: 26832912736274
title: "Response Code 20059 Suspected Fraud"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/26857478821394-Response-Code-20059-Suspected-Fraud"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-08-13T13:40:07Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRP1QGWAFPTEP0CSMC1WBV", "01JVS26PBA73NGJJETCPWS3SPE", "01JVS27ERFT6CA591PZY4AV4SZ", "01JVS37B77GAYYQJX3WQ88DPYV", "01JWGFBVDZS86TAMZG2K7PXG7X"]
label_names: ["scheme_declines"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article:**

Use this guide when a merchant reports a transaction has failed and you identify the response code **20059** (or **59**) in the transaction logs. 

This article will help you understand why the transaction was declined and provide clear steps to advise the merchant.**DESCRIBE THE ISSUE 💬**

When a transaction is declined with the response code 20059 (often seen as just `59` in logs), it means the issuing bank (the customer's bank) has refused the payment due to suspected fraud. Their internal security systems have flagged the transaction as potentially unauthorized, leading to the decline.

This is a common issue in payment processing related to card authentication and fraud prevention. It is not an error with our platform but a decision made by the cardholder's bank.

You can verify this response by checking the card processing logs (Visa, MasterCard etc.). If the **response value is **`**59**`, it confirms the decline originated from the issuing bank due to a suspected fraud flag.

## PROCESS FOR RESPONSE CODE 20059 DECLINES   🖊️

This process outlines the steps for diagnosing and responding to transactions declined with response code 20059 (suspected fraud). Both standard checks and contextual problem-solving based on 3DS usage are needed.

### Step 1: Verify the Response Code in Logs

- Open the transaction logs for the declined payment using [DataDog](https://app.datadoghq.com/account/login?next=%2Flogs%3Fquery%3Dsource%253Acard-processing%2520service%253A%2522Mpgs%2520Authorisation%2520API%2522%2520env%253Aprod%2520%2520%2540Properties.Request.MaskedTransactionId%253A%252AChargeID%252A%26cols%3Dpool%252Cservice%252C%2540error%252C%2540Properties.ActionType%252C%2540Properties.AcceptorName%252C%2540Properties.Response.ResponseDetails.AcquirerResponse%252C%2540Properties.Response.ResponseDetails.AcquirerResponseCode%252C%2540Properties.Request.RequestDetails.TransactionType%26index%3D%252A%26integration_id%3D%26integration_short_name%3D%26messageDisplay%3Dinline%26saved_view%3D749868%26stream_sort%3Dtime%252Cdesc%26viz%3Dstream%26from_ts%3D1648020996179%26to_ts%3D1648021896179%26live%3Dfalse), [Traffic Insight](https://retoolprod.mgmt.ckotech.co/apps/a04c8c20-72cf-11eb-bea4-e7bba7ba05e6/payment-performance-shared-debug/Traffic%20Insights#payment_id=), or [Sherlock](https://retoolprod.mgmt.ckotech.co/apps/918d2a72-4c5a-11ec-88dc-53fd2c6a4170/gateway/Sherlock).

_From the screenshot, we can see a CIT non-3DS transaction._

- Locate the response code. If the value is **59**, this confirms the issuing bank declined the transaction due to suspected fraud.

💡 **Tip:** In DataDog, you may need to inspect the specific service (Visa CP API) to find the detailed failure reason

 

### Step 2: Check for a Recommendation Code

- Within the logs, look for the ``[Recommendation Code](https://www.checkout.com/docs/developer-resources/codes/recommendation-codes), this code can provide more insight from the issuer.

- This may suggest specific actions like retrying with 3DS or provide further insight from the issuer (e.g., a recommendation code of `02` could indicate an issuer velocity rule decline

 

 

 

 

### Step 3: Determine if 3D Secure (3DS) Was Used

The next steps depend on whether the transaction was authenticated using 3D Secure (3DS), an extra layer of security for online payments.

**If 3DS was used:**

- 
**Inform the merchant** that because 3DS was used for authentication, the decline is definitively a result of the issuer's fraud systems

- Advise the merchant that the **cardholder must contact their issuing bank directly** to resolve the suspected fraud flag

**If 3DS was not used:**

- 
**Recommend** that the merchant asks the cardholder to try the transaction again, ensuring they complete the 3DS authentication step

- 
**Explain** that using 3DS provides an additional security layer that can satisfy the bank's fraud concerns and increase the chance of approval

✅ **Best Practice:** Where merchants use 3DS it can significantly reduce fraud-related declines and shift liability for fraudulent chargebacks

## RESOLUTION 🛠️

The issue is resolved if the cardholder successfully completes the transaction, either by contacting their bank (for 3DS transactions) or by re-attempting with 3DS (for non-3DS transactions).

## ESCALATION ⏫

While most 20059 declines are resolved by the cardholder, you should escalate the issue in the following scenarios:

- 
**Multiple Declines:** You observe a high number of '59' declines from the same Bank Identification Number (BIN) or issuer across different merchants.

- 
**Regional Spikes:** There is a sudden and unusual increase in '59' declines affecting a specific region or customer segment.

- 
**Persistent Failures:** A merchant reports that transactions are still failing even after the cardholder has contacted their bank and re-attempted with 3DS.

**How to Escalate:**

- For widespread issues or unusual spikes, notify the **Operations Team** via Slack for immediate awareness.

- For persistent, merchant-specific issues, raise a case with the **Outreach Team**.

 

## FAQs ❓

What does response code 20059 (or 59) mean?

It indicates that the cardholder's bank has declined the transaction because its fraud detection systems flagged it as suspicious.

 Is our platform causing this issue?

No, this is a decline from the issuing bank. It is based on their internal security rules and is not an error with our payment system.

 Will using 3DS guarantee the transaction goes through?

Not always, but using 3D Secure (3DS) provides stronger authentication and significantly reduces the perceived fraud risk. 

This substantially increases the likelihood of the transaction being approved by the bank.

 What should the cardholder do if they keep getting this decline?

If the transaction was attempted **with 3DS**, the cardholder needs to contact their bank to authorize the payment. 

If it was attempted **without 3DS**, they should try again and complete the 3DS verification process.
