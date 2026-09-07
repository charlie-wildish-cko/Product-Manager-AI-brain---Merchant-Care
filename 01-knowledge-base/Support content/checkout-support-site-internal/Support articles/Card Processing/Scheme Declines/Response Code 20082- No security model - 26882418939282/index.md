---
id: 26882418939282
section_id: 26832912736274
title: "Response Code 20082- No security model"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/26882418939282-Response-Code-20082-No-security-model"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-07-18T13:47:32Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JVS26PBA73NGJJETCPWS3SPE", "01JVS7Q4N2D9E599M0J2P62MYP", "01JVVWSBQHBJ3T5YTHAY8YJF54", "01JWGDT2GVZDC77V6NTVP368S0"]
label_names: ["card_processing", "scheme_declines"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

For information on how to handle transactions that fail with the response code **20082**.

## DESCRIBE THE ISSUE 💬

This error indicates that the cardholder's issuing bank has declined the transaction due to a problem with the card's security information. This is a direct decline from the issuer and not an error with our platform. The most common reasons include:

- 
**No security model found** or **PIN cryptographic error** (an error detected by the VIC security module during PIN decryption).

- 
**Negative Card Authentication Method (CAM), dCVV, iCVV, or CVV results**. This means the card's security code (like CVV2/CVC2) provided was incorrect or did not match the issuer's records.

In all instances, this is a **decline from the cardholder's issuing bank**. The bank has rejected the transaction based on internal security checks related to the card data provided.

You can confirm this by checking the card processing logs. If the response value is `82`, it confirms the decline originated from the issuing bank due to one of these security-related reasons. In these situations, the cardholder should be advised to contact their issuing bank directly for further support and to understand the specific reason for the decline

## PROCESS FOR RESPONSE CODE 20082  🖊️

This process outlines the steps to diagnose and advise on transactions declined with response code 20082. Standard log checks are crucial.

### Step 1: Confirm the Response Code in Logs

- 
Navigate to the card processing logs for the declined transaction using ****[Data Dog](https://app.datadoghq.com/dashboard/j2p-zgh-7x5?fromUser=false&refresh_mode=sliding&from_ts=1747895167843&to_ts=1747898767843&live=true), ****[Traffic Insight](https://retoolprod.mgmt.ckotech.co/apps/a04c8c20-72cf-11eb-bea4-e7bba7ba05e6/payment-performance-shared-debug/Traffic%20Insights#payment_id=), or ****[Sherlock](https://retoolprod.mgmt.ckotech.co/apps/918d2a72-4c5a-11ec-88dc-53fd2c6a4170/gateway/Sherlock).
_**Screenshot demonstrating how to find a transaction by ID and identify Last Response Code_

- 
**Identify the Response Code: **From the card processing logs, Look for **response code **`**82**`

- This confirms the decline is due to a security model, PIN cryptographic, or CVV/CVM mismatch issue from the issuer, also the [recommendation code](https://www.checkout.com/docs/developer-resources/codes/recommendation-codes).

__ _Table explaining _`_Recommendation code_`_ values (01, 02, 03) and their summaries/possible decline reasons:_ 

### Step 2. Investigate for Wider Impact

Check if the issue is isolated to a single cardholder or part of a larger trend.If you notice a **significant number of declined transactions with code 20082 coming from the same issuer bank and most impacted BIN(s)**, this indicates a potential systemic issue beyond an isolated cardholder error._Example screenshot showing how to check for impact for a mentioned period, indicating no significant impact found (using Datadog query with BIN and Issuername counts):_ ✅ **Best Practice:** If you only see a single decline or a few unrelated instances, the issue is with the individual cardholders, not a systemic problem. 

## RESOLUTION 🛠️

## Step 3. Advise the Merchant

Based on your findings, provide clear guidance to the merchant.**For a single decline:**

1. Inform the merchant that the error code `20082` is a security-related decline from the cardholder's bank

2. Explain that the bank has rejected the transaction because the security information provided (like the CVV) was incorrect or did not pass their security checks

3. Advise the merchant to ask the cardholder to contact their bank directly to find out the specific reason for the decline and resolve it

**If you identified a wider impact:**

1. Follow the escalation path outlined below

2. Inform the merchant that you have identified a potential issue with the issuing bank and that your team is investigating it

## ESCALATION ⏫

Escalate the issue if you identify a pattern of declines from the same source.⚠️ **When to Escalate:**You should escalate if you notice a significant number of transactions with response code `20082` coming from the **same issuer bank** and affecting the **same BIN(s)**.**How to Escalate:**

1. Create a ticket and assign it to the ****[Outreach Team](https://checkout.atlassian.net/jira/core/projects/IO/form/46)

2. Include the following information in the ticket:

  - A summary of the issue.

  - A link to the report or query showing the high number of declines  in the ****[looker report](https://checkoutinternal.eu.looker.com/looks/11623?toggle=fil)

  - The name of the affected issuer bank and the impacted BIN(s).

 

## FAQs ❓

 What does response code 20082 mean?It means the transaction was declined by the issuing bank due to a security-related issue, such as an incorrect CVV/PIN, or a problem with the card's security model. Is this a platform issue?No, this is an issuer-side decline. Our platform simply relays the bank's rejection based on their security checks. What should the cardholder do if their transaction is declined with 20082?The cardholder should contact their issuing bank directly to understand the specific reason for the decline and resolve any potential security issues or incorrect card data on file.
