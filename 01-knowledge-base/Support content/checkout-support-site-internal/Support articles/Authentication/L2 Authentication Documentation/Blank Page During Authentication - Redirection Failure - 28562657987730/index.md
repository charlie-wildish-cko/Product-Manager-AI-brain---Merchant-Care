---
id: 28562657987730
section_id: 27822398640530
title: "Blank Page During Authentication / Redirection Failure"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/28562657987730-Blank-Page-During-Authentication-Redirection-Failure"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-09-19T12:10:43Z"
permission_group_id: 26838654181266
content_tag_ids: ["01K1ZNKGNFMDFZR9PD5RHV1K3P"]
label_names: ["L2", "Troubleshooting", "authentication", "blank_page"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

To investigate and resolve issues where a customer sees a blank page after entering their card details because the merchant failed to redirect them to the authentication page, leading to a session expiry.
DESCRIBE THE ISSUE 💬

When a customer sees a blank page after entering their card details, it's typically caused by the merchant's integration failing to redirect them to the 3D Secure authentication page. The payment session expires after 15 minutes, and the outdated link results in a blank screen instead of the expected authentication challenge.

From a customer's perspective, the page simply isn't loading, preventing the customer from completing the transaction. This issue is typically caused by the merchant's system is not sending GET requests or redirecting the cardholder to access the authentication page in 15 minutes after the session was created.

 
KEY TAKEAWAYS 🔑

**Blank Page = Redirection Failure:** A blank page after entering card details typically means the customer was never redirected to the 3DS authentication page.

**Root Cause: 15-Minute Timeout:** The payment session expired because the authentication was not started within 15 minutes of the session's creation.

**Diagnose in Datadog:** Check `Sessions.Interceptor` logs for the specific `SessionResourceId`. A lack of `GET` requests between the session's creation and its expiration confirms the redirection failure.

**Resolution:** The merchant must fix their integration to correctly and promptly redirect the customer. The customer must then start a new transaction.

**Escalate if Discrepancy:** Escalate if the merchant's claims of redirection do not align with the log evidence.

 

RESOURCES 📍

| Tools | Case Examples | Related |
| --- | --- | --- |
| [Traffic Insights](https://retoolprod.mgmt.ckotech.co/apps/a04c8c20-72cf-11eb-bea4-e7bba7ba05e6/payment-performance-shared-debug/Traffic%20Insights#payment_id=pay_rgyrv3davdzedkdpgpbuouhrde) | [Ticket 72507](https://checkout1360.zendesk.com/agent/tickets/72507) | [GET Payment Details](https://api-reference.checkout.com/#operation/getPaymentDetails) |
| [Datadog](https://www.google.com/search?q=link_to_datadog) | [Ticket 72084](https://checkout1360.zendesk.com/agent/tickets/72084) |  |

PROCESS FOR INVESTIGATING BLANK PAGE DURING AUTHENTICATION 🖊️

### Step 1. Access Logs via Traffic Insights (with Payment ID)

- On [Traffic Insights](https://www.google.com/search?q=link_to_traffic_insights), paste the **Payment ID** into the search bar

- Click on the **Associated Ids** tab to find and open the Datadog link associated with the transaction

### Step 2. Use Datadog (with Session ID)

If you do not have the Payment ID but have the **Session ID**, you can use the following filter directly in Datadog's search bar: `@Properties.SessionResourceId:********`

_Example Query:_ `@Properties.SessionResourceId:sid_xpdsgd5srjuufds6icktxd3xje` ([DD link](https://app.datadoghq.com/logs?query=%40Properties.SessionResourceId%3Asid_jf4e3diybiquxfvg7rxdt4xlna&agg_m=count&agg_m_source=base&agg_t=count&clustering_pattern_field_path=message&cols=source%2C%40ActionName%2C%40Properties.ApplicationName%2C%40duration%2C%40GatewayElapsed%2C%40HttpStatusCode%2C%40Properties.Action&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=desc&viz=stream&from_ts=1753171757506&to_ts=1754467757506&live=true))

### Step 3. Interpret Session Logs for Redirection Failure

- In the logs, observe the timing of the session

In the image above the authentication started at 23:00:28 and expired at 23:15:28 because the merchant did not redirect to authenticate the transaction.

This caused the customer to see a blank page after entering their card details.

**Ideal Scenario (Successful Redirection):** In contrast, an ideal scenario would show `GET` requests immediately following the session creation, indicating that the customer was successfully redirected to the authentication page.

 

In the screenshot above, after the session is created `GET` requests confirm the customer was redirected.

RESOLUTION 🛠️

**Expected Result:** Confirming that the blank page issue is due to a redirection failure and providing the correct guidance to the merchant.

**Remediation Steps:**

- 
**Explain Timeframe:** The cardholder has a **15-minute timeframe** to complete authentication after the session is created

- 
**Advise Merchant:** Advise the merchant to ensure their integration is correctly and promptly redirecting the customer to the authentication page - They should verify that no part of their system is sending outdated requests to an expired session

- 
**Advise Cardholder:** The cardholder will need to attempt the payment again in a new session

**Steps to Check Resolution:**

- The merchant confirms that their integration has been updated or verified

- A new transaction attempt is successful

ESCALATION** ⏫**

**Situations Requiring Escalation:**

- The merchant insists that they are redirecting the customer, but the Datadog logs show no record of these redirections - this suggests a more complex issue with the redirection mechanism itself

- A high volume of blank page issues are reported for a specific merchant, even after they claim to have checked their integration

FAQs** ****❓**

Why do payment sessions expire?Payment sessions have a limited lifespan for security reasons. For authentication, the session has a **15-minute timeframe** to be completed. If the cardholder does not access or complete the authentication page within this window, the session expires.
How can I confirm this is a redirection issue and not something else?You can confirm it in Datadog. By looking at the logs for the specific Session ID, you will see the session creation timestamp. If there are no GET requests to the Sessions.Interceptor service within the next 15 minutes, it confirms that the customer was never redirected.
