---
id: 27324189050898
section_id: 27822398640530
title: "Response code 20151 -  Cardholder 3DS Authentication Failed"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/27324189050898-Response-code-20151-Cardholder-3DS-Authentication-Failed"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-09-19T12:12:29Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JXEYRHXZ1CJ9A5371EDR7F0R", "01JXEYSCJTNWXDA5KB69ESKCVM"]
label_names: ["L2", "SOP", "Trouble shooting guide", "Authentication failed"]
user_segment_ids: []
archive: false
---

**When to use this article**

To troubleshoot **20151 failures**, which occur when a cardholder fails or does not complete the 3D Secure (3DS) authentication process.DESCRIBE THE ISSUE** 💬**

Merchants report transactions failing with **response code 20151 (Authentication Failed on the dashboard) and c**ustomers report seeing the payment failed after attempting 3D Secure verification. KEY TAKEAWAYS 🔑

- 20151 failure indicates an issue with 3D Secure (3DS) authentication

- Use Dashboard, Datadog, and Retool to investigate the failure

- The investigation aims to pinpoint the exact reason for the failure, such as cardholder abandonment or issuer decline

- The resolution involves communicating the reason to the merchant and suggesting actionable steps for the cardholder.

PROCESS FOR 20151 FAILURE INVESTIGATION  🖊️

This process outlines how to investigate 20151 failures using the Dashboard, Datadog, and Retool to understand why the 3DS authentication failed.Step 1. Dashboard Investigation

- 
**Locate the Transaction:** Find the specific transaction on the Dashboard using its Payment ID or other relevant filters

- 
**Access Authentication Section:** Scroll down on the transaction details page until you locate the **"Authentication"** section

- 
**Review Authentication Details:** In this section, observe the following key fields:

  - **Transaction Status**

  - **Transaction Status Reason**

  - 
**Challenge Cancel** (Note: This field may not always be available)

_Example:_

- See the external documentation: [Track authentication events](https://www.checkout.com/docs/business-operations/use-the-dashboard/payment-activity/track-authentication-events) for details on transaction statuses and reason codes.
Step 2. Investigation on Datadog (transaction less than 14 days ago) or Retool (transactions older than 14 days**Data Dog Investigation Steps**

- 
**Access Datadog Logs:** on retool and enter the **Payment ID**

- 
Under the **Associated IDs** tab, click the **Datadog link** associated with `ChargeAuthenticationFailed` This will open the relevant logs:

- 
**Locate 3DS Session Log:** In Datadog, find the **last **`**ThreeSD2.Sessions.API**` log entry

- 
**Examine Response Body:** Open this log entry and scroll down to the **response body**. Locate the `response_code` to confirm the specific reason for the 3DS authentication failure.
 

- 
**When merchants are complaining about a particular trend or drop in authentication performance: **Use this [looker](https://checkoutinternal.eu.looker.com/explore/sessions/session_authentication_report?qid=swabTKoCWbi2AO8rGr6d4A&origin_space=2958&toggle=fil) to spot transaction trends and all types of authentication failures

⚠️ Note - Change the date, entity / client details as required** Retool Investigation Steps**

- 
**Access Retool:** Open [Retool](https://www.google.com/search?q=link_to_retool)** **

- 
**Navigate to Authentication Tab:** Select the **"Authentication" tab** to view the authentication-related codes and details, which is especially helpful for transactions older than 15 days

- 
**Enter Payment ID:** Input the relevant **Payment ID**

- Select the **"Authentication" tab** to view the authentication-related codes and details, which is especially helpful for transactions older than 15 days.

- 
**Review Authentication Details:** In this section, observe the following key fields:

  - **Transaction Status**

  - **Transaction Status Reason**

  - 
**Challenge Cancel** (Note: This field may not always be available)

RESOLUTION 🛠️

- 
**Expected Result:** Identifying the precise reason for the 3DS authentication failure (e.g., cardholder abandonment, incorrect input, issuer decline) and providing the appropriate guidance

- 
**Communicate Reason:** Clearly inform the customer/merchant that the transaction failed because the cardholder did not complete or pass the 3D Secure verification

- 
**Advise Retry:** Recommend the customer **re-attempt the transaction**, ensuring they complete all steps of the 3D Secure challenge

- 
**Check for Issuer Issues:** If the authentication decline code points to an issuer-specific issue (e.g., `decline code 08 - No card record`) advise the cardholder to **contact their issuing bank**

- 
**Alternative Payment Method:** Suggest trying a different 3DS-enabled card if repeated attempts with the same card consistently fail 3DS

ESCALATION ⏫

- 
**Merchant-Specific Trend:** A high volume of 20151 failures for a specific merchant that cannot be attributed to cardholder error after investigation. This should be raised with the Issuer Outreach team using the specified [Form](https://checkout.atlassian.net/jira/core/projects/IO/form/46)

- 
**Systemic Issue:** A sudden increase in 20151 failures across multiple merchants, potentially indicating a systemic issue with an ACS provider or our platform. This also needs to be raised with the Issuer Outreach team using the specified [Form](https://checkout.atlassian.net/jira/core/projects/IO/form/46)

FAQs ❓**Q: What does response code 20150 mean?**Response code 20151 indicates that the cardholder did not successfully complete or pass the 3D Secure (3DS) authentication process. **Q: Why would a cardholder fail 3DS authentication?**Common reasons for a cardholder failing 3DS authentication include:

- Incorrectly entering their 3DS password or one-time passcode (OTP)

- Closing the authentication pop-up/page before completing the process

- Their device or browser having compatibility issues with the 3DS challenge

- A technical issue on the issuing bank's Access Control Server (ACS) preventing the challenge from being delivered or completed

- The cardholder abandoning the process

## RESOURCES 📍

| Tools | Case Examples | Related Article |
| --- | --- | --- |
| [Dashboard](https://dashboard.checkout.com/) [](https://checkout.atlassian.net/wiki/spaces/LL/database/6990364784?atl_f=PAGETREE) | [Case 21200](https://checkout1360.zendesk.com/agent/tickets/21200) | [Understand authentication failures](https://www.checkout.com/docs/payments/authenticate-payments/3d-secure/understand-authentication-failures) |
| [Traffic Insights](https://retoolprod.mgmt.ckotech.co/apps/a04c8c20-72cf-11eb-bea4-e7bba7ba05e6/payment-performance-shared-debug/Traffic%20Insights#payment_id=pay_pk4tedtjwlbudnbk3yfpkgsvoe) | [Case 45413](https://checkout1360.zendesk.com/agent/tickets/45413) |  |
| [Datadog](https://app.datadoghq.com/logs?query=&agg_m=count&agg_m_source=base&agg_t=count&cols=host%2Cservice%2C%40Properties.EventType&fromUser=true&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=time%2Cdesc&viz=stream&from_ts=1666681487938&to_ts=1666940687938&live=true) | [Case 24940](https://checkout1360.zendesk.com/agent/tickets/24940) |  |
