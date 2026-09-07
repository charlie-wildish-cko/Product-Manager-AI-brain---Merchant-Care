---
id: 27359134991378
section_id: 22057285830034
title: "Response Code 20152 - 3DS Authentication Timeout"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/27359134991378-Response-Code-20152-3DS-Authentication-Timeout"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-09-19T11:34:18Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRP1QGWAFPTEP0CSMC1WBV", "01JXEYSCJTNWXDA5KB69ESKCVM"]
label_names: ["response_code_20152", "L2", "Trouble shooting guide", "Authentication failed", "3DS"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

To troubleshoot **20152 failures**, which indicates **authentication expiry** or **Transaction Timed Out at the Access Control Server (ACS)** during the 3D Secure (3DS) process

**Problem / Symptom**: 20152 3DS Authentication Expired / ACS Timeout

 

## DESCRIBE THE ISSUE 💬

Merchants report transactions failing with **response code 20152**. From their perspective, the 3DS authentication process was not completed within the allotted timeframe (typically 15 minutes).

 

## RESOURCES **📍**

| Tools | Case Examples | Related |
| --- | --- | --- |
| [Datadog Dashboard](https://app.datadoghq.com/logs?query=%403ds2.transaction_status_reason%3A14%20%403ds2.transaction_status%3AN%20%40Properties.Currency%3ASAR%20%40Properties.ClientId%3Acli_nilibeucitcu5c7ql3mnzxqoqm&agg_m=count&agg_m_source=base&agg_q=%40Properties.AcsUrl&agg_q_source=base&agg_t=count&analyticsOptions=%5B%22bars%22%2C%22dog_classic%22%2Cnull%2Cnull%2C%22value%22%5D&clustering_pattern_field_path=message&cols=source%2C%40ActionName%2C%40Properties.ApplicationName%2C%40duration%2C%40GatewayElapsed%2C%40HttpStatusCode%2C%403ds2.transaction_status_reason&event=AwAAAZdkH_o_gFLG7QAAABhBWmRrSF96ZUFBRFpuZUFMMDhQRXRBQWUAAAAkMDE5NzY0MmMtMGYzMC00ZDMzLTljYTgtZDlkYmY1YjE1NDU2AAtufQ&fromUser=true&messageDisplay=inline&panel=%7B%22queryString%22%3A%22%40Properties.AcsUrl%3Awww.securecode.tasheelfinance.com%22%2C%22filters%22%3A%5B%7B%22isClicked%22%3Atrue%2C%22source%22%3A%22log%22%2C%22path%22%3A%22Properties.AcsUrl%22%2C%22value%22%3A%22www.securecode.tasheelfinance.com%22%7D%5D%2C%22queryId%22%3A%22a%22%2C%22timeRange%22%3A%7B%22from%22%3A1748437774000%2C%22to%22%3A1749733774000%2C%22live%22%3Atrue%7D%7D&refresh_mode=sliding&storage=hot&stream_sort=desc&top_n=10&top_o=top&viz=sunburst&x_missing=true&from_ts=1739261883621&to_ts=1740557883621&live=true) | [Case Example - 61749](https://checkout1360.zendesk.com/agent/tickets/61749) | [Understand authentication failures](https://www.checkout.com/docs/payments/authenticate-payments/3d-secure/understand-authentication-failures) [Response code: 20152](https://checkoutint.zendesk.com/hc/en-us/articles/22059042697106) |

 

## PROCESS FOR 20152 FAILURE INVESTIGATION ** **** 🖊️**

The investigation process involves checking up to three platforms, depending on the age of the transaction and the level of detail required. Always start with the Dashboard for a quick diagnosis.

**Understand Authentication Timeframe:** Authentication must be completed within a 15-minute timeframe. If not, an expiry is generated. 

## Step 1: Initial Check on the Dashboard

- Take the **Payment ID** and locate the transaction on the Dashboard

- 
Confirm the transaction appears as **"Authentication failed"**
****

- Scroll down to the **"3DS Authentication" section **to find:

  - **Transaction Status**

  - **Transaction Status Reason**

  - **Status Reason**

- Confirm these fields show:

  - 
**Transaction Status = N** (Not Authenticated / Account Not Verified; Transaction denied)

  - 
**Transaction Status Reason = 14** (Transaction timed out at the ACS)

  - 
**Status Reason = RREQ status**
****

- Refer to the [external documentation](https://www.checkout.com/docs/payments/authenticate-payments/3d-secure/understand-authentication-failures) to confirm the meaning of these codes

**Tip:** The **Access Control Server (ACS)** is the service, typically run by the card issuer's bank, that is responsible for authenticating the cardholder during a 3DS transaction. A timeout here often means their system didn't respond in time.

## Step 2: In-Depth Investigation with Datadog

- 
**Access Datadog Logs: **on retool enter the **Payment ID**

- 
Under the **Associated IDs** tab, click the **Datadog link** associated with `ChargeAuthenticationFailed` to open the relevant logs

- 
Verify Redirection URL Generation - In Datadog, verify the response body to ensure that the redirection URL was successfully generated in the response body under the `**service:GatewayAPI**`

- You will find this in the response 

- This is the link the merchant's integration needs to pass to the cardholder for authentication

- 
Look for content Event **"AuthenticationExpired"**

- Click Open and you will see the Authentication **ResponseCode** and **ResponseReason** in the message

- 
**Root Cause Example:** In logs, if the Issuer's ACS was unable to communicate the 3DS information due to a timeout at the ACS this confirms an ACS timeout

- To conduct an analysis, you can make use of this [dashboard](https://app.datadoghq.com/logs?query=%403ds2.transaction_status_reason%3A14%20%403ds2.transaction_status%3AN%20%40Properties.Currency%3ASAR%20%40Properties.ClientId%3Acli_nilibeucitcu5c7ql3mnzxqoqm&agg_m=count&agg_m_source=base&agg_q=%40Properties.AcsUrl&agg_q_source=base&agg_t=count&analyticsOptions=%5B%22bars%22%2C%22dog_classic%22%2Cnull%2Cnull%2C%22value%22%5D&clustering_pattern_field_path=message&cols=source%2C%40ActionName%2C%40Properties.ApplicationName%2C%40duration%2C%40GatewayElapsed%2C%40HttpStatusCode%2C%403ds2.transaction_status_reason&fromUser=true&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=desc&top_n=10&top_o=top&viz=sunburst&x_missing=true&from_ts=1739261883621&to_ts=1740557883621&live=true) to view the ACS that has the most failures with the status code and reason

Note - Replace the Client ID and Status reason / code according to requirement

## Step 3: Investigation on Retool (for Transactions older than 14 Days)

For transactions older than 14 days, the necessary details are more easily found in Retool

- Open [Retool](https://www.google.com/search?q=link_to_retool)** **and **navigate to Authentication Tab:** Select the **"Authentication" tab** to view the authentication-related codes and details

- Input the relevant **Payment ID**

- Review the authentication details here, focusing on:

  - **Transaction Status**

  - **Transaction Status Reason**

  - 
**Challenge Cancel** (Note: This field may not always be available)

## 

## RESOLUTION **🛠️**

- 
**For One-off Cases (Redirection/Timeout):** Inform the merchant that the cardholder did not access the authentication page within the correct timeframe, possibly because they left the transaction screen.

  - 
**Action:** Advise the merchant to ask the cardholder to **try the transaction again**, ensuring they complete the pop-up or redirected authentication page.

- 
**For Multiple Scenarios (Redirection Issue):** If a single merchant sees this error repeatedly, they may not be correctly handling the redirection URL.

  - 
**Action:** Advise the merchant to **verify their integration** to ensure they are correctly passing on the redirection/interceptor link to the cardholders.

- 
**For ACS Timeouts (Intermittent):** These are often intermittent issues outside of our direct control.

  - 
**Action:** Inform the merchant that the failure was due to a temporary issue with the cardholder's bank's authentication service. Advise them to ask the cardholder to **retry the payment later**.

  - Check if multiple merchants are impacted by timeouts from the same ACS around the same time. This helps identify a wider, but temporary problem.

## ESCALATION** ⏫**

- A **significant and sustained increase** in 20152 failures, especially those definitively identified as ACS timeouts, across multiple merchants or a specific scheme type - which have to be raised with issuer outreach team through this [Form](https://checkout.atlassian.net/jira/core/projects/IO/form/46)

- If the issue cannot be resolved by advising the merchant/cardholder and the root cause points to a systemic platform or third-party service issue - which have to be raised with issuer outreach team through this [Form](https://checkout.atlassian.net/jira/core/projects/IO/form/46)

## FAQs** ❓**

What are the common reasons for a 20152 failure?The main reasons are:

- 
**Cardholder Inactivity/Abandonment:** The cardholder did not access or complete the 3DS authentication page within the 15-minute timeframe (often seen as a redirection error).

- 
**ACS Timeout:** The Access Control Server (ACS) responsible for the 3DS challenge did not respond in time, preventing the authentication from completing. This can be an intermittent technical issue on the ACS provider's side.

 Are ACS timeouts within our control to fix?ACS timeouts are typically **intermittent issues on the ACS provider's side** (e.g., `authentication.cardinalcommerce.com`). While we monitor these, they are generally outside of our direct control to "fix" immediately. Our internal outreach team may escalate persistent patterns with ACS providers to explore potential improvements.
