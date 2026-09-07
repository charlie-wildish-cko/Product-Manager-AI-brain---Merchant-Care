---
id: 30478859398290
section_id: 26817954592018
title: "APM - Refund stuck in Deferred status"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/30478859398290-APM-Refund-stuck-in-Deferred-status"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-12-05T11:29:39Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JVW5V7B7TZ05VVPPCG5ZEHCF"]
label_names: ["APM"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

If the merchant reports that payments are stuck in the RefundDeferred status. 

**Problem**

This indicates that a refund has been initiated but has not yet been fully reconciled or processed by the Alternative Payment Method (APM) provider.

## DESCRIBE THE ISSUE 💬

This article outlines the process for investigating and resolving payments that remain in the `RefundDeferred` status.

Typically, an automatic reconciliation process runs for **7 days** after a refund is created. If the refund status does not update within this window, or if the merchant requires immediate assistance, a manual reconciliation may be required.

TOOLING**📍**

| Tool | Access |
| --- | --- |
| [DataDog](https://app.datadoghq.eu/dashboard/cya-7rs-8v3?fromUser=false&refresh_mode=sliding&from_ts=1764841936612&to_ts=1764845536612&live=true)   [Okta - Postman](https://checkout.okta.com/app/getpostman/exk7urhx4g76Lyjmo357/sso/saml?fromHome=true)   [Retool - Traffic Insights](https://retoolprod.mgmt.ckotech.co/apps/a04c8c20-72cf-11eb-bea4-e7bba7ba05e6/payment-performance-shared-debug/Traffic%20Insights#payment_id=)   [Okta - Guacamole](https://guacamole.mgmt.checkout.internal:8080/guacamole/#/)   [Retool - Sherlock](https://retoolprod.mgmt.ckotech.co/apps/918d2a72-4c5a-11ec-88dc-53fd2c6a4170/gateway/Sherlock) | Access granted via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274) |

PROCESS TO ANALYSE PAYMENT STUCK IN REFUND DEFERRED STATUS🖊️

Follow these steps to diagnose the root cause before attempting a fix.

### Step 1. Verify Payment Status

- Navigate to ****[retool](https://retoolprod.mgmt.ckotech.co/apps/a04c8c20-72cf-11eb-bea4-e7bba7ba05e6/payment-performance-shared-debug/Traffic%20Insights#payment_id=pay_juxjr3remwbefpotxlzablq6wa)** **Traffic Insights or [sherlock](https://retoolprod.mgmt.ckotech.co/apps/918d2a72-4c5a-11ec-88dc-53fd2c6a4170/gateway/Sherlock)

- Replace the `payment_id` with the relevant `payment_id` 

- Confirm the current status is indeed `RefundDeferred`

### Step 2. Analyze Logs in Datadog

- In Retool or Sherlock, locate the **RefundDeclined** event

- Copy the `correlation_id` associated with that event

- 
Open [Datadog](https://app.datadoghq.com/logs?query=%40CorrelationId%3A4f6a166d-6a70-4080-8d83-a375a8310ce7&agg_m=count&agg_m_source=base&agg_t=count&clustering_pattern_field_path=message&cols=service&fromUser=true&messageDisplay=inline&refresh_mode=sliding&saved-view-id=348561&storage=hot&stream_sort=desc&viz=stream&from_ts=1692692637230&to_ts=1695284637230&live=true)  replace the `correlation_id` with the one you copied to check for errors

  - _Alternative:_ Click [here](https://app.datadoghq.com/logs?query=%40PaymentId%3Apay_juxjr3remwbefpotxlzablq6wa&agg_m=count&agg_m_source=base&agg_t=count&clustering_pattern_field_path=message&cols=service&fromUser=true&messageDisplay=inline&refresh_mode=sliding&saved-view-id=348561&storage=hot&stream_sort=desc&viz=stream&from_ts=1692692637230&to_ts=1695284637230&live=true) and replace the `payment_id` with the one you want to use to filter the logs

- 
**Check for Webhooks:** Look for a "Refund successful" webhook

  - If no errors are found and no webhook is present, the refund may simply be delayed

**💡 Tip:** For certain APMs like **iDeal** or **ACH**, the refund webhook is not immediate. It may take **2-3 days** to arrive.

### Step 3. Check APM Portal (Optional)

If the APM uses a collecting model:

- Log in to the specific APM portal using credentials from the [LastPass](https://lastpass.com/vault/?nk=1)** **vault

- Verify the status of the transaction on the provider's side

## RESOLUTION ⚒️

If the payment has exceeded the standard processing time or the 7-day auto-reconciliation window, follow these steps to manually reconcile the refund.

### Step 1. Retrieve and Convert IDs

- In **Retool**, locate the transaction currently in `RefundDeferred` status

- Copy the **Transaction ID** (starts with `ref_`)

- Convert the Transaction ID to an Act ID using the internal ID conversion [tool](https://devapi.ckotech.co/webhooktester/events/encode/fd3391ba-28bb-494e-914e-e97a4529915d)

- 
Add the prefix `act_` to the converted ID

  - _Example:_ `act_xkith7n3fbheteko5f5ekkmrlu`

As an example, let's review a Qpay payment with the ID: `pay_wlatcc3j267e7nywhrkl4buaxy` as payment is stuck in RefundDeferred, we need to perform a manual reconciliation. To do this, we first need to retrieve the act ID for the payment.

In Retool, open the RefundDeferred status to locate the Transaction ID (as shown in the screenshot below).

Copy this Transaction ID and convert it from ref to act ID using the provided [link](https://devapi.ckotech.co/webhooktester/events/encode/fd3391ba-28bb-494e-914e-e97a4529915d).

Once converted, prefix the result with “act_”, and then log in to Jumpbox to run the manual reconciliation. For this payment its: act_ xkith7n3fbheteko5f5ekkmrlu

Similarly the act ID can also be obtained from Sherlock.

### Step 2. Access Jumpbox

- Log in to **Okta**

- Navigate to **Guacamole**

- Enter your credentials to access the Jumpbox environment

### Step 3. Run Manual Reconciliation via Postman

- Inside Jumpbox, open **Postman**

- Navigate to **Workspaces** > **App.Postman.APM.**

- Select **Alternative Payment Method (APM)** > **Internal** > **[Specific APM Name, e.g., Qpay APM]**.

- Select the request: **Post Refund reconciliation**

- 
Enter the following details in the request params:

  - **Payment ID**

  - **Account ID (**`**act_...**`**)** obtained in Step 1.

  - **Environment:** Select `PROD`.

- Click **Send**.

**Expected Result:** You should receive a `200 OK` response with the body:

JSON
 

```
"reason_text": "Refund successfully reconciled"

```

### Step 4. Confirm Resolution

- Wait approximately **5 minutes**

- Check **Retool** or the Dashboard

- Confirm the payment status has updated to **Refunded**

 

Please note that an automatic reconciliation process runs for 7 days after the refund creation date. If the refund status does not update within those 7 days, the payment will remain in __RefundDeferred__ status. In such cases, we need to follow the process outlined above to update the status manually.

💡 RetryDuration = TimeSpan.FromDays(7) // Arbitrary value which is high enough to retry the reconciliation several times 

## ESCALATION** ⏫**

If the manual reconciliation fails or is not possible:

- 
**Endpoint Unavailable:** Not all APMs have a manual reconciliation endpoint in Postman. If the endpoint is missing for the specific APM, you must contact the **APM Support Team (Third-party)** via email to resolve the issue.
You can also escalate to the **L3 Engineering Team** with the Datadog logs and the Postman response through this** ******[form](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277)**.**

## RESOURCES** ⭐**

| Case Examples |
| --- |
| - [Case 49202](https://checkout1360.zendesk.com/agent/tickets/49202)  - [Case 48384](https://checkout1360.zendesk.com/agent/tickets/48384)  - [Case 65445](https://checkout1360.zendesk.com/agent/tickets/65445) |
