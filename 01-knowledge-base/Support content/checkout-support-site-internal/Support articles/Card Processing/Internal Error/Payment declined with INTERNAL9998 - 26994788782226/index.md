---
id: 26994788782226
section_id: 27060550224018
title: "Payment declined with INTERNAL9998"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/26994788782226-Payment-declined-with-INTERNAL9998"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-07-18T13:47:28Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JVS26PBA73NGJJETCPWS3SPE", "01JVS27ERFT6CA591PZY4AV4SZ", "01JW93XJA7VR2Z0SEQNRP45VPS", "01JW93XRA9V38PV0NS2PYF1NJW", "01JW93XWAFP95EEJWSZA0HST71"]
label_names: ["card_processing", "scheme_declines"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

This article explains the INTERNAL9998 response code, how to identify these internal declines in logs and outlines the process for diagnosis and escalation to the OC team.

 

## DESCRIBE THE ISSUE 💬

Merchants may encounter transactions failing due to a `**INTERNAL9998**` response code (20068). This indicates a **technical error** within our Card Processing (CP) application, such as a code crash or network disconnection. 

You can identify these by checking the CP response message to the Gateway (GW) for **"InternalDecline" in the **`**FreeText31**`** field**. This confirms the request was declined internally at the CP level, with no message sent to the scheme. This issue suggests a problem within our payment processing infrastructure, requiring an internal investigation
**PROCESS FOR INTERNAL9998 DECLINES**** **** 🖊️**

 **Step 1: Access and Analyze Transaction Logs**

 

- 
**Access logs **through ****[Data Dog](https://app.datadoghq.com/dashboard/j2p-zgh-7x5?fromUser=false&refresh_mode=sliding&from_ts=1747895167843&to_ts=1747898767843&live=true), ****[Traffic Insight](https://retoolprod.mgmt.ckotech.co/apps/a04c8c20-72cf-11eb-bea4-e7bba7ba05e6/payment-performance-shared-debug/Traffic%20Insights#payment_id=), or ****[Sherlock](https://retoolprod.mgmt.ckotech.co/apps/918d2a72-4c5a-11ec-88dc-53fd2c6a4170/gateway/Sherlock)

- 
**Confirm Internal Decline:**

  - Filter the logs to isolate the response from the **Card Processing (CP)** application to the **Gateway (GW)**.

  - Locate the `FreeText31` field in the response

  - Verify that the field contains the string "**InternalDecline**". This is the definitive confirmation of an `INTERNAL9998` issue.

- 
**Gather Context:** Review the surrounding log entries for any other errors, exceptions, or indications of network issues (HTTP 422, "Failed to process", "Error occurred while processing transaction", "AuthorizationTimedOut"). As observed in the provided screenshot, these indicate underlying technical problems.

**⚠️ Warning:** The presence of "InternalDecline" is a clear sign of an internal system failure. It is not a standard decline from a bank or card scheme. 

**Step 2: Check for Existing Incidents**

Before escalating, you must check for ongoing incidents to avoid duplicate reporting.

- Review the **Operations Command (OC) slack channel** to determine if an incident related to this error has already been reported and is under investigation.
 

**Step 3: Escalation ⏫**

This issue must be escalated to the **Operations/Engineering teams** under the following conditions:

- 
**New Incident:** An `INTERNAL9998` decline is identified, and there is **no existing incident** reported in the OC channel.

- 
**Systemic Issue:** A pattern of `INTERNAL9998` declines is observed across **multiple merchants or multiple transactions**, indicating a widespread, systemic problem.

 

**Step 4: Communicate with the Merchant**

When a merchant reports this issue, provide clear and concise information without causing unnecessary alarm or revealing sensitive technical details.

- 
**Inform:** "We are currently experiencing an internal technical issue that caused the transaction to fail. Our engineering teams are actively investigating the matter."

- 
**Provide RFO:** Once the OC team has investigated and shared a **Reason for Outage (RFO)** report, communicate this to the merchant.

- 
**Avoid:** Do not provide specific technical details about the error, such as "a server crashed" or "we have a network disconnection."

**RESOLUTION** 🛠️

- 
**Internal Action:** Resolution for `INTERNAL9998` errors is the responsibility of the **Operations and Engineering teams**. They will perform a root cause analysis and deploy a fix to the affected systems.

- 
**Merchant Action:** Advise the merchant to **retry the transaction** once you have confirmed that the underlying technical issue has been resolved.

 

## FAQs** ❓**

 What is the most reliable way to confirm a transaction failed with this specific error?

The most reliable way is to inspect the transaction logs. You must find the response message from the Card Processing (CP) application to the Gateway (GW). If the `FreeText31` field in that response contains the exact value "**InternalDecline**," it is definitively an `INTERNAL9998` issue.

 Does the customer's bank see or decline this transaction?

No. The error occurs before the transaction request is ever sent to the payment schemes (like Visa or Mastercard) and, therefore, never reaches the customer's bank. The failure is entirely contained within our infrastructure.

 The merchant wants to know if they can retry the transaction. What is the correct advice?Advise the merchant **not** to retry the transaction until they receive confirmation from you that the underlying issue has been resolved. Retrying before the fix is deployed will only result in more failed transactions. What happens after I escalate the issue?Once escalated, the Operations/Engineering teams will take ownership of the incident. They will begin their investigation, provide updates in the OC channel, and work on deploying a fix. Your role then shifts to monitoring the incident channel and managing communication with any affected merchants. What is a Reason for Outage (RFO) report and when do I share it?

The RFO is an official report prepared by the Operations/Engineering teams that explains the root cause of an incident. 

You should share this report with the affected merchant once the incident is fully resolved and the report has been made available to you.
