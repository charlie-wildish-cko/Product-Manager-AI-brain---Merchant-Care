---
id: 29346766886162
section_id: 26817954592018
title: "APM Payments Declined"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/29346766886162-APM-Payments-Declined"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-12-04T15:15:33Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JVW5V7B7TZ05VVPPCG5ZEHCF"]
label_names: ["APM"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

when a merchant reports that payments are being declined or failing. This article outlines how to investigate Alternate Payment Method (APM) logs to distinguish between user errors, external provider issues, and internal system faults.

**Problem / Symptom:** Merchant reports higher than usual decline rates or specific failed transactions.

## DESCRIBE THE ISSUE 💬

The merchant reports that payments are failing or returning a "Declined" status. This often requires investigation into the specific error codes returned by the APM (Alternative Payment Method) provider to determine the root cause.

TOOLING**📍**

| Tool | Access |
| --- | --- |
| [DataDog](https://app.datadoghq.eu/dashboard/cya-7rs-8v3?fromUser=false&refresh_mode=sliding&from_ts=1764841936612&to_ts=1764845536612&live=true)   [Client Admin Tool(CAT)](https://client-admin.cko-prod.ckotech.co/web/nas/)   [Retool - Traffic Insights](https://retoolprod.mgmt.ckotech.co/apps/a04c8c20-72cf-11eb-bea4-e7bba7ba05e6/payment-performance-shared-debug/Traffic%20Insights#payment_id=)   [Okta - Guacamole](https://guacamole.mgmt.checkout.internal:8080/guacamole/#/) | Access granted via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274) |

## PROCESS TO ANALYSE PAYMENT DECLINES🖊️

Follow these steps to diagnose the source of the decline. This process moves from standard checks to in-depth log analysis.
Step 1. Verify Payment Status

First, confirm the current status of the payment to ensure it was actually attempted and declined.

- Open ****[Retool](https://retoolprod.mgmt.ckotech.co/apps/a04c8c20-72cf-11eb-bea4-e7bba7ba05e6/payment-performance-shared-debug/Traffic%20Insights#payment_id=pay_juxjr3remwbefpotxlzablq6wa)** (Traffic Insights)** or ****[Sherlock](https://retoolprod.mgmt.ckotech.co/apps/918d2a72-4c5a-11ec-88dc-53fd2c6a4170/gateway/Sherlock)

- Replace the the `payment_ID` with the one provided by the merchant

- Confirm the status is listed as **Declined** or **Failed**

Step 2. Analyze Logs in Datadog

Once the decline is confirmed, you need to find the specific error message.

- Copy the `correlation_id` associated with the Declined event in Retool/Sherlock

- Open [Datadog](https://app.datadoghq.com/logs?query=%40CorrelationId%3A4f6a166d-6a70-4080-8d83-a375a8310ce7&agg_m=count&agg_m_source=base&agg_t=count&clustering_pattern_field_path=message&cols=service&fromUser=true&messageDisplay=inline&refresh_mode=sliding&saved-view-id=348561&storage=hot&stream_sort=desc&viz=stream&from_ts=1692692637230&to_ts=1695284637230&live=true) and replace the `correlation_id` with the one you copied above

- You can also use the payment ID to directly view the errors in the logs

- Look for errors in the **"APM Consumer"** service logs or responses from the APM

- Click [here](https://app.datadoghq.com/logs?query=%40PaymentId%3Apay_juxjr3remwbefpotxlzablq6wa&agg_m=count&agg_m_source=base&agg_t=count&clustering_pattern_field_path=message&cols=service&fromUser=true&messageDisplay=inline&refresh_mode=sliding&saved-view-id=348561&storage=hot&stream_sort=desc&viz=stream&from_ts=1692692637230&to_ts=1695284637230&live=true) and replace the `payment_id` with the one you want to use to filter the logs.

 
Step 3. Deep Dive (Internal Event Store)

If Datadog does not show a clear decline reason, you must check the internal Event Store (EVS).

- Log in to the **Jumpbox** via **Okta** > **Guacamole**

- Open the Chrome browser within the Jumpbox

- Navigate to the Event Store URL: [http://eventstore-apm.prod.internal:2113/web/index.html#/streams/KNet.Payment-9b9e4db4-e3ab-44fe-b38d-0775dec40d20](http://eventstore-apm.prod.internal:2113/web/index.html#/streams/KNet.Payment-9b9e4db4-e3ab-44fe-b38d-0775dec40d20)

- Search for the stream using the Payment ID format (e.g., `KNet.Payment-[UUID]`)

Example Case

  
  

- As an example, let's review a Knet payment with the ID: `pay_juxjr3remwbefpotxlzablq6wa`

- As an example, let's review a Qpay payment with the ID: `pay_nectkkkxgbcebpve2rufyprvse`

For knet payment `pay_juxjr3remwbefpotxlzablq6wa` as observed in the logs, the error is from Knet “_Error notification with Trandata: null due to "IPAY01000305 - Duplicate Merchant Track Id"_”.

 

Follow the steps above to extract the logs for the Qpay payment

  
For Qpay payment `pay_nectkkkxgbcebpve2rufyprvse` - As observed we do not see any errors but we can see that the payment is Declined and response in the log says - "_payment_rejected_".

 

## RESOLUTION ⚒️

Use the error messages found in Step 2 or 3 to determine the resolution. Below are common scenarios.
Scenario A: Duplicate Merchant Track Id (Knet)

**Error:** `Error notification with Trandata: null due to "IPAY01000305 - Duplicate Merchant Track Id"`

- **Root Cause:** The customer clicked the payment redirection link, started the process, and then clicked the link a second time to restart the session. This triggers a duplicate security error.

- **Remediation:** Advise the merchant to instruct their customers to click the redirection link **only once** and complete the payment within that single session.

Scenario B: Payment Rejected (Qpay/General)

**Error:** `payment_rejected` (No specific error code)

- **Root Cause:** The customer was successfully redirected to the payment page but did not complete the transaction (abandonment).

- **Remediation:** If the APM (e.g., Qpay) does not provide a specific error code, assume customer abandonment.

- **Next Step:** If the merchant insists the customer completed it, contact the APM Support (Acquirer bank) for further investigation.

General Resolution Logic

- **Internal Service Error:** If the logs show an internal system fault, escalate to Engineering.

- **Third-Party APM Error:** If the warning/error comes from the external provider, contact them via email or support portal.

## ESCALATION ⏫

If the issue cannot be resolved via the steps above or indicates an internal platform bug:

- **Who to contact:** APM Engineering L3 Team

- **How to contact:** Use the escalation [form](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277)

- **Required Info:** Include the `payment_id`, `correlation_id`, and a screenshot of the logs from Datadog/Guacamole

Determining the Root Cause (Internal vs. External)

Because APM providers vary significantly, they do not always return standardized decline reasons. You must analyze the **Log Source** in Datadog/Splunk to determine the next step.

| **If the error source is...** | **Then...** |
| --- | --- |
| **An Internal Service**      _(e.g., timeouts in our own API, internal server errors)_ | **Escalate to Engineering**      Use the L3 Escalation Form. Include the Payment ID and exact timestamp. |
| **A Third-Party APM**      _(e.g., "Gateway Rejected," "Provider Unavailable," or external timeouts)_ | **Contact the APM Provider**      Reach out to the provider directly via their support email or portal to confirm if they are experiencing an outage or blocking the specific transaction. |

**💡 Best Practice:** Always check the **"APM Consumer"** service logs first. If the error originates there, it is likely an internal issue. If the error is simply a relayed message from the provider (e.g., `400 Bad Request` from Knet), it is an external issue.

## RESOURCES** ⭐**

| Case Examples |
| --- |
| - [Case 70605](https://checkout1360.zendesk.com/agent/tickets/70605)  - [Case 73197](https://checkout1360.zendesk.com/agent/tickets/73197)  - [Case 43585](https://checkout1360.zendesk.com/agent/tickets/43585) |
