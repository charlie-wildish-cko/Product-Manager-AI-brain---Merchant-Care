---
id: 26906931802642
section_id: 26832912736274
title: "Response code 20014_Invalid card number"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/26906931802642-Response-code-20014-Invalid-card-number"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-07-18T13:46:03Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JVS26PBA73NGJJETCPWS3SPE", "01JVY5HRRSM5W25W9PRP9EKN3H", "01JVY5J3FB1JFFCWYS3PQHSBMT"]
label_names: ["card_processing", "scheme_declines"]
user_segment_ids: [11003606966930]
archive: false
---

**This article explains what response code 20014 means and outlines the process for diagnosing this issue.**

 

## DESCRIBE THE ISSUE** 💬**

Sometimes, merchants reach out to us when a customer's payment doesn't go through. If the transaction shows a response code of **20014**, it means there's an **"Invalid account number (no such number)"** decline. Essentially, this indicates that the cardholder's bank has turned down the transaction due to incorrect card information.

This is a **decline from the cardholder's issuing bank**.** **

The cardholder should get in touch with their bank for more help and to find out the specific reason behind the decline. This situation relates to payment processing and affects both the cardholder and the merchant. 

 

## **PROCESS FOR RESPONSE CODE 20014 DECLINES**** **** 🖊️**

This process outlines the steps to diagnose and advise on transactions that have been declined with a response code 20014. Standard checks are typically sufficient for individual cases.

1. 
**Check Transaction Logs:**

  - Use ****[Sherlock](https://retoolprod.mgmt.ckotech.co/apps/918d2a72-4c5a-11ec-88dc-53fd2c6a4170/gateway/Sherlock)** / ******[Traffic Insight](https://retoolprod.mgmt.ckotech.co/apps/a04c8c20-72cf-11eb-bea4-e7bba7ba05e6/payment-performance-shared-debug/Traffic%20Insights#payment_id=) or ****[DataDog](https://app.datadoghq.com/dashboard/j2p-zgh-7x5?fromUser=false&refresh_mode=sliding&from_ts=1747895167843&to_ts=1747898767843&live=true)  to access the logs for the declined transaction.

_**From Traffic insight, within the _`_ChargeDeclined_`_ event, the _`_AcquirerResponseCode_`_ will be _`_14_`

1. 
**Identify the Response Code from Datadog:**

  - In Datadog, look for the response code **14** within the card processing log. This confirms it is an "invalid account number" decline from the issuing bank.

_**In the card processing log, the **Data Element is returned as 14, **which confirms the decline is from the issuer bank_

1. 
**Advise the Merchant:**

  - This is a **bank-issued decline** and not a checkout.com error

  - Explain that, in line with the scheme (MasterCard/VISA etc) error message, either this PAN is no longer in use or a new one has been issued

  - The merchant should advise the cardholder to contact their issuing bank for further support

 

## **RESOLUTION 🛠️**

- The cardholder may need to use a different card or obtain a new one from their bank if the existing one is no longer valid.

## **ESCALATION ⏫**

- If the merchant still thinks there’s an issue on our side, then you can escalate to **Support L3: the card processing team.**

 

## **FAQs ❓**

 What does response code 20014 mean?

It means the transaction was declined by the issuing bank because the account number (card number) is invalid or no longer recognized by the bank.

 What should the cardholder do if their transaction is declined with 20014?

- Suggest they carefully re-enter their card details to correct any potential typos.

- If the payment fails again, they should contact their bank directly to resolve the issue or try a different payment method.
