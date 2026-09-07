---
id: 30549693756946
section_id: 26817954592018
title: "APM - Payments stuck in Deferred status"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/30549693756946-APM-Payments-stuck-in-Deferred-status"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-12-05T09:47:17Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JVW5V7B7TZ05VVPPCG5ZEHCF"]
label_names: ["APM"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

**When to use this article:** Use this guide when a merchant reports that payments are stalled in a "Deferred" status. This typically occurs when the backend automatic reconciliation process encounters a problem.

**Problem / Symptom:** Payments fail to transition to "Captured" or "Failed" and remain "Deferred" indefinitely.

## DESCRIBE THE ISSUE 💬

The merchant reports that one or more customer transactions are stuck in a Deferred status for an extended period. The payments are not transitioning to Captured, Failed, or Expired as expected, causing confusion regarding whether the funds were actually received.

TOOLING**📍**

| Tool | Access |
| --- | --- |
| [DataDog](https://app.datadoghq.eu/dashboard/cya-7rs-8v3?fromUser=false&refresh_mode=sliding&from_ts=1764841936612&to_ts=1764845536612&live=true)   [Okta - Postman](https://checkout.okta.com/app/getpostman/exk7urhx4g76Lyjmo357/sso/saml?fromHome=true)   [Retool - Traffic Insights](https://retoolprod.mgmt.ckotech.co/apps/a04c8c20-72cf-11eb-bea4-e7bba7ba05e6/payment-performance-shared-debug/Traffic%20Insights#payment_id=)   [Okta - Guacamole](https://guacamole.mgmt.checkout.internal:8080/guacamole/#/)   [Retool - Sherlock](https://retoolprod.mgmt.ckotech.co/apps/918d2a72-4c5a-11ec-88dc-53fd2c6a4170/gateway/Sherlock) | Access granted via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274) |

PROCESS TO ANALYSE PAYMENT STUCK IN DEFERRED STATUS🖊️

## 🔎 Phase 1: Investigation & Diagnosis

Follow these steps to confirm the issue and identify the root cause.
Step 1: Verify Payment Status

- Open  [Retool](https://retoolprod.mgmt.ckotech.co/apps/a04c8c20-72cf-11eb-bea4-e7bba7ba05e6/payment-performance-shared-debug/Traffic%20Insights#payment_id=pay_juxjr3remwbefpotxlzablq6wa)  and navigate to **Traffic Insights** or [Sherlock](https://retoolprod.mgmt.ckotech.co/apps/918d2a72-4c5a-11ec-88dc-53fd2c6a4170/gateway/Sherlock) 

- Locate the payment by replacing the payment ID with the one provided by the merchant 

- Confirm the status is indeed **Deferred**

Step 2: Analyze Logs (DataDog)

- Copy the `correlation_id` from the Deferred event in Retool/Sherlock

- Open [Datadog](https://app.datadoghq.com/logs?query=%40CorrelationId%3A4f6a166d-6a70-4080-8d83-a375a8310ce7&agg_m=count&agg_m_source=base&agg_t=count&clustering_pattern_field_path=message&cols=service&fromUser=true&messageDisplay=inline&refresh_mode=sliding&saved-view-id=348561&storage=hot&stream_sort=desc&viz=stream&from_ts=1692692637230&to_ts=1695284637230&live=true) and replace `correlation_id` with the one you just copied(or filter directly using the `payment_id` [here](https://app.datadoghq.com/logs?query=%40PaymentId%3Apay_juxjr3remwbefpotxlzablq6wa&agg_m=count&agg_m_source=base&agg_t=count&clustering_pattern_field_path=message&cols=service&fromUser=true&messageDisplay=inline&refresh_mode=sliding&saved-view-id=348561&storage=hot&stream_sort=desc&viz=stream&from_ts=1692692637230&to_ts=1695284637230&live=true)).

**Check for the following:**

- Are there specific error logs?

- Is the _Payment Captured_ or _Successful_ webhook missing?

If no obvious errors or webhooks are found, proceed to Step 3
Step 3: Check Private Events (Sherlock)

Sometimes, public events (like "Refunded" or "Captured") are not generated, but private events indicate a rejection.

- In **Sherlock**, look for "Private Events"

- 
**Scenario A: Capture Rejected**

  - If you see `CaptureRejected` events, the Gateway has refused to update the payment status

  - **Action:** Raise an L3 ticket to the Gateway Team to re-trigger the Capture status: Sample [ticket](https://checkout.atlassian.net/browse/GTW-12926)

- 
**Scenario B: No Rejection Events**

  - If the payment is simply stuck without rejection, proceed to Phase 2 for Manual Reconciliation

**💡 Pro Tip:** You can also verify private events via the Event Store (EVS) in Guacamole. Login to Jumpbox → Open Chrome → Navigate to the APM URL: [http://eventstore-apm.prod.internal:2113/web/index.html#/streams/KNet.Payment-17dbbae2-f28b-48a6-a203-392d011cc408](http://eventstore-apm.prod.internal:2113/web/index.html#/streams/KNet.Payment-17dbbae2-f28b-48a6-a203-392d011cc408) and search the Stream ID.

## ⚒️ Phase 2: Resolution & Remediation

Choose the resolution path based on the Payment Method (APM) identified in Phase 1.

### Path A: EPS Payments (Specific Workflow)

**⚠️ Note:** EPS payments generally do not require deep investigation. An internal reconciliation call is usually sufficient.

- Log in to the **Jumpbox** using Okta → Guacamole

- Open **Postman** and select the Workspace `App.Postman.APM`

- Navigate to: `Alternative Payment Method(APM)` → `Internal` → `EPS APM`

- Select **Post reconciliation**

- Enter the `payment_id` in the URL parameters and ensure the environment is set to **PROD**

- 
Click **Send**

  - **Expected Result:** Response should be `200 OK`

- Wait a few minutes; the payment status should update to **Expired**

### Path B: General Manual Reconciliation (e.g., Multibanco)

Use this step for Multibanco and other APMs where the automatic backend reconciliation failed.

- Log in to the **Jumpbox** using Okta → Guacamole

- Open **Postman** and select the Workspace `App.Postman.APM`

- Navigate to: `Alternative Payment Method(APM)` → `Internal` → `[Specific APM Name]`

- Select **Post Reconcile Payment**

- Enter the `payment_id` in the URL and set the environment to **PROD**

- 
Click **Send**

  - **Expected Result:** Status `200 OK` and body text `"reason_text": "Payment successfully reconciled"`.

- 
Wait approximately 5 minutes

  - Check Retool/Dashboard. The status should update to **Captured** or **Expired** depending on the 3rd party status.

**✅ Best Practice:** If the APM operates on a "Collecting Model," you can verify the status directly in the 3rd party APM portal. Access credentials can be found in the [LastPass](https://lastpass.com/vault/?nk=1) Vault.
Example Case

As an example, review the Multibanco payment with the ID: `pay_cjc4mjoehwdevafautipp6kldu`

Since the payment is currently stuck in a Deferred status, a manual reconciliation needs to be performed by the L2 team.

💡 An automatic reconciliation process runs in the backend, and this issue typically occurs when that process encounters a problem. 

The payment status been updated as “Captured/Expired” as per the status that’s been received from Multibanco. Later the same will be updated in Retool and Dashboard.

## ESCALATION** ⏫**

If the standard reconciliation steps fail or are unavailable:

- **Missing Endpoint:** If the specific APM does not have a reconciliation endpoint in Postman, contact the **3rd Party APM Support Team** via email.

- **Engineering Support:** If deep technical assistance is required, raise a ticket with the **APM Engineering L3 Team** using the standard escalation ****[form](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277)**.**

## RESOURCES** ⭐**

| Case Examples |
| --- |
| - ****[Case 73429](https://checkout1360.zendesk.com/agent/tickets/73429)  - ****[Case 74216](https://checkout1360.zendesk.com/agent/tickets/74216)  - ****[Case 72661](https://checkout1360.zendesk.com/agent/tickets/72661) |
