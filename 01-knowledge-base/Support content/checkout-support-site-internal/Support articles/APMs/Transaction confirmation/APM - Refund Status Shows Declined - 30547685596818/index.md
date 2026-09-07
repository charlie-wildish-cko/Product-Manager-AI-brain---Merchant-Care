---
id: 30547685596818
section_id: 26817978758418
title: "APM - Refund Status Shows Declined"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/30547685596818-APM-Refund-Status-Shows-Declined"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-12-04T15:42:03Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JVW5V7B7TZ05VVPPCG5ZEHCF"]
label_names: ["APM"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

When a merchant reports that a refund attempt has returned a **Declined** status. This article outlines how to investigate the root cause using Retool, Datadog, and internal logs to determine if the issue lies with the customer's card, the APM (Alternative Payment Method) provider, or a system sync error.

## DESCRIBE THE ISSUE 💬

The merchant has attempted to refund a transaction, but the status is updating to **Declined** in the dashboard. This prevents the funds from returning to the customer. This issue often requires investigating specific error logs to determine if the decline is coming from the payment provider (APM) or an internal validation error.

TOOLING**📍**

| Tool | Access |
| --- | --- |
| [DataDog](https://app.datadoghq.eu/dashboard/cya-7rs-8v3?fromUser=false&refresh_mode=sliding&from_ts=1764841936612&to_ts=1764845536612&live=true)   [Retool - Traffic Insights](https://retoolprod.mgmt.ckotech.co/apps/a04c8c20-72cf-11eb-bea4-e7bba7ba05e6/payment-performance-shared-debug/Traffic%20Insights#payment_id=)   [Okta - Guacamole](https://guacamole.mgmt.checkout.internal:8080/guacamole/#/) | Access granted via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274) |

PROCESS FOR TROUBLESHOOTING DECLINED REFUNDS 🖊️

Follow these steps to diagnose the cause of the decline.
Step 1: Confirm Payment Status

- Navigate to ** ******[retool](https://retoolprod.mgmt.ckotech.co/apps/a04c8c20-72cf-11eb-bea4-e7bba7ba05e6/payment-performance-shared-debug/Traffic%20Insights#payment_id=pay_juxjr3remwbefpotxlzablq6wa)** (Traffic Insights)** or ****[sherlock](https://retoolprod.mgmt.ckotech.co/apps/918d2a72-4c5a-11ec-88dc-53fd2c6a4170/gateway/Sherlock)

- Replace the `payment_id` with the one provided by the merchant

- Confirm that the specific refund action shows a status of **RefundDeclined**

Step 2: Locate the Correlation ID

To filter logs effectively, you need the unique identifier for the event.

- In Retool or Sherlock, locate the **RefundDeclined** event

- 
Copy the `correlation_id` associated with that specific event

  - Alternatively, you can use the `payment_id` directly

Step 3: Analyze Logs in Datadog

- Open **Datadog**

- Click [here](https://app.datadoghq.com/logs?query=%40CorrelationId%3A4f6a166d-6a70-4080-8d83-a375a8310ce7&agg_m=count&agg_m_source=base&agg_t=count&clustering_pattern_field_path=message&cols=service&fromUser=true&messageDisplay=inline&refresh_mode=sliding&saved-view-id=348561&storage=hot&stream_sort=desc&viz=stream&from_ts=1692692637230&to_ts=1695284637230&live=true) and replace the `correlation_id` with the one you copied

- Look for errors in the "APM Consumer" service logs or responses received from the APM

- Identify the specific error message (See _Common Error Examples_ below)

Step 4: Check Internal Event Store (Optional)

💡 **Tip:** Perform this step only if the decline reason is **not** found in Datadog.

- Log in to the **Jumpbox** using Okta and navigate to **Guacamole**

- Open the Google Chrome browser within the remote session

- Navigate to the internal Event Store URL : [http://eventstore-apm.prod.internal:2113/web/index.html#/streams/KNet.Payment-17dbbae2-f28b-48a6-a203-](http://eventstore-apm.prod.internal:2113/web/index.html#/streams/KNet.Payment-17dbbae2-f28b-48a6-a203-392d011cc408)

- Search for the payment stream to find raw error data

Example Case

As an example, let's review a MBway payment with the ID: `pay_iw2bl5crs7vezokfkkgaiu6f4q`  
As an example, let's review a Tamara payment with the ID: `pay_uundmlprtnvuncytj56rl7j4h4`
Scenario A. MBway payment details 

As payment is in a RefundDeclined status, and upon reviewing the logs, we found the following error from MBway: "MB WAY purchase with an invalid card." This indicates that the customer’s card has either been expired or deactivated, which caused the refund to fail.

We can see the below mentioned error in logs from Mbway.  
_Error while calling MBWay refund: com.checkout.mbway.exception.ServerError: Received error response from inbound server: 400 BAD_REQUEST { "merchant":{ "terminalId":"1598774", "merchantTransactionId":"w2bl5crs7vezokfkkgaiu6f4q", "merchantTransactionTimestamp":"2025-09-12T07:50:33.050874763Z" }, "transactionRecipientId":"S13073800474198S", "transactionTimestamp":"2025-09-12T08:50:33.284+01:00", "amount":{ "value":"12.99", "currency":"EUR" }, "transactionID":"s2Z3WvHj6FUQ73pvRQTf", "execution":{ "startTime":"2025-09-12T07:50:33.235Z", "endTime":"2025-09-12T07:50:34.010Z" }, "paymentStatus":"Declined", "returnStatus":{ "statusCode":"E0531", "statusMsg":"Error", "statusDescription":"MB WAY purchase with an invalid card" } }_
Scenario B. Tamara payment details

As payment is in a RefundDeclined status, and upon reviewing the logs, we found the following error from Tamara:

_Partner error has occurred. Partner API responded with HTTP status: 422 to "POST" request on path ___[https://api-cko.tamara.co/tamara/payments/5d2f7c73-cdc0-41dc-a631-1e6425c4fa36/refunds.](https://api-cko.tamara.co/tamara/payments/5d2f7c73-cdc0-41dc-a631-1e6425c4fa36/refunds.)_ RequestId: "d221318b-8cca-479a-a80b-113e226b9419", ErrorType: "entity_error", ErrorCodes: "payment_state_not_refundable"._

### COMMON ERROR EXAMPLES 🔎

**Scenario A: MBWay - "Invalid Card"**

- **Log Error:** `MB WAY purchase with an invalid card` or `400 BAD_REQUEST`.

- **Meaning:** The customer’s card/account is expired, deactivated, or invalid. The refund cannot be processed to this source.

**Scenario B: Tamara - "Payment State Not Refundable"**

- **Log Error:** `HTTP status: 422 ... ErrorCodes: "payment_state_not_refundable"`.

- **Meaning:** There is a status mismatch. The payment might be 'Pending' on the provider's side but 'Captured' on ours, or vice versa.

## RESOLUTION ⚒️

Once you have identified the error from the logs above, follow the appropriate resolution path:

**If the error indicates an Invalid Card (e.g., MBWay case):**

- **Action:** Inform the merchant that the refund cannot be processed through the gateway because the customer's card/account is invalid.

- **Fix:** The merchant must arrange an alternative refund method (e.g., manual bank transfer) directly with the customer.

**If the error indicates a Provider Sync Issue (e.g., Tamara case):**

- **Action:** The status needs to be corrected on the provider's side.

- **Fix:** Contact the specific APM team (e.g., Tamara) via their Tech Slack channel (e.g., `#tamar_cko_tech`) or email using the contact details listed [in Confluence](https://checkout.atlassian.net/wiki/spaces/APM/pages/6262259713/Tamara+Direct+Home). Request them to check the transaction status and update it to 'Captured' manually. Once updated, the merchant can retry the refund.

## ESCALATION** ⏫**

If you cannot identify the error in Datadog/EVS, or if the Resolution steps above do not solve the issue:

- Gather the **Payment ID**, **Correlation ID**, and screenshots of the logs.

- Raise a request with the **APM Engineering L3 team**

- Use the standard escalation ****[here](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277)

 

## RESOURCES** ⭐**

| Case Examples |
| --- |
| - [Case 77266](https://checkout1360.zendesk.com/agent/tickets/77266)  - [Case 79268](https://checkout1360.zendesk.com/agent/tickets/79268)  - [Case 84124](https://checkout1360.zendesk.com/agent/tickets/84124) |
