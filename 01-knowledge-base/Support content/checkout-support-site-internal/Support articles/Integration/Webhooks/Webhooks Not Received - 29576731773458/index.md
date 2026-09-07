---
id: 29576731773458
section_id: 22188517144978
title: "Webhooks Not Received"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/29576731773458-Webhooks-Not-Received"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-31T16:48:23Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JVM5TPJQV63X1YGHPGKWQTJN", "01JWRC46WWC378V6E80MQ1J31Q", "01K5EQEA0XWX44PMGF84GWVYTM"]
label_names: ["webhook_troubleshooting", "webhook_troubleshooting_steps", "webhook_not_received"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

Use this guide to troubleshoot and resolve issues when a merchant is not receiving webhooks, which can result in their system's orders not being updated or dispatched correctly.

**Problem:** Webhooks are essential for receiving real-time notifications about events like payments and refunds. When these notifications fail, it can disrupt automated workflows.

**Solution:** This article provides a systematic process to diagnose and fix webhook delivery failures by verifying delivery status, checking configurations, and authenticating keys.

## DESCRIBE THE ISSUE 💬

The merchant has configured webhooks to receive real-time notifications for events like payments or refunds, but they are not arriving at the endpoint. This failure disrupts automated processes, such as order fulfillment or system updates. 

 
 

## KEY TAKEAWAYS 🔑

- Start by verifying webhook delivery status in Datadog using the Payment ID

- A `200` status code means successful delivery; other codes indicate a problem

- Ensure all required Checkout.com IP addresses are allowlisted on your server

- Authentication keys (Authorization Header and Signature Key) must match exactly between the system and the Dashboard

- Check that the Endpoint URL, event types, and processing channels are correctly configured in the Dashboard

## RESOURCES 📍

| Tools | Case Examples | Related |
| --- | --- | --- |
| [Datadog](https://app.datadoghq.com/) [Checkout.com Dashboard](https://dashboard.checkout.com/) [Client Admin Tool (CAT)](https://example.com/cat-login) | [Example 1](https://checkout1360.zendesk.com/agent/tickets/48285) [Example 2](https://checkout1360.zendesk.com/agent/tickets/5778) | [Checkout.com IP Addresses](https://example.com/ip-addresses) [Automatic Retries Guide](https://example.com/docs/retries) [Retrigger Events Guide](https://example.com/docs/retrigger) |

## PROCESS FOR TROUBLESHOOTING WEBHOOKS NOT RECEIVED 🖊️

This process uses standard checks in Datadog, the Dashboard, and server configuration to diagnose why webhooks are not being received.
**Step 1. Verify Webhook Delivery in Datadog**

Confirm if the webhook was sent successfully from our system.

- 
**Search Datadog:** Use the [Datadog](https://app.datadoghq.eu/logs?query=%40Properties.ApplicationName%3AFlow.Actions.Webhook%20%40Properties.EventSubjectId%3Apay_sivnl2qaefgu5oh46a2tab77ku%20&cols=service%2Cenv%2C%40http.status_code%2C%40Properties.EventType%2C%40Properties.WebhookUrl%2C%40Properties.ProcessingChannelId%2C%40Properties.AccountName&fromUser=true&index=&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=%40Properties.Request.Source.type%2Casc&view=spans&viz=stream&from_ts=1698759430161&to_ts=1700055430161&live=true) Webhook search by Payment ID to check the delivery status for a specific transaction.

- 
**Check Status Codes:**

  - 
**Status **`**200**`**:** The webhook was sent and processed correctly by the server.

  - 
**Status **`**202**`**:** The webhook was skipped. This is often expected (e.g., if a transaction does not belong to a specific workflow).
**⚠️ ****Any other status code:** Indicates a delivery failure that needs investigation

**Step 2. Check for IP Address Allowlisting Issues**

If webhooks are failing, the server might be blocking traffic from our IP addresses.

- 
**Check Your Server:** Confirm if the server restricts incoming traffic to a specific set of IP addresses

- 
**Verify Allowlist:** If it does, ensure all relevant [Checkout.com IP addresses](https://example.com/ip-addresses) are on the allowlist

- 
**Test After Update:** After updating the allowlist, test the webhook delivery again to confirm the issue is resolved

**Step 3. Verify Webhook Authentication**

Incorrect authentication keys are a common cause of webhook failures.

- 
**Match the Keys:** Ensure that the Webhook Authorization Header Key and Signature Key match exactly on both system (e.g., SDK, e-commerce site) and in the Checkout.com Dashboard.

- 
**Resolve Mismatches:**

  - If the merchant has the correct keys saved, they can update them in the setup

  - If they do not have the keys saved, they must create a new webhook, generate a new set of keys, and then delete the old webhook configuration

**Step 4. Check Dashboard and CAT Settings**

Incorrect configuration in the Dashboard or CAT can prevent webhooks from being created or sent.

1. 
**Verify Dashboard Settings:**

  - Log in to the Checkout.com Dashboard and navigate to the **Webhooks** section.

  - Check that the **Endpoint URL** is correct and begins with either `https://` or `http://`.

  - Ensure the correct event types are selected for the webhook.

  - Verify that the transaction occurred on one of the processing channels selected for the webhook.

2. 
**Check User Permissions (If unable to create webhooks):**

  - In the Dashboard, go to **Settings User permissions** and select the user.

  - Under the **Notifications** section, ensure the user has the rights to manage webhooks.

3. 
**Check CAT Configuration:**

  - Verify that **Flow** is enabled in CAT under **Services**.

  - 
Check that Access Keys and API Keys have the `flow`, `flow:events`, and `flow:workflows` scopes enabled.
**⚠️ Warning:** For Live accounts, changes to API and Access keys must be handled by your Config team. For Sandbox accounts, the Merchant Care team can perform these changes.

## RESOLUTION ⚒️

- 
**Expected Result:** After following these steps, the root cause of the webhook failure will be identified and corrected. The endpoint will begin receiving webhook notifications successfully, allowing automated workflows to function as expected.

- 
**Remediation Steps:** After applying a fix (e.g., updating an allowlist, correcting a key), trigger a new event (like a test payment) that should generate a webhook. Verify in Datadog that the new webhook delivery shows a `200` status code. You should also confirm that your system has received and processed the notification correctly.

- 
**Rollback/Recovery:** Configuration changes can be easily reverted. If an updated key or URL causes new issues, revert to the previous setting in the Dashboard. If an IP allowlist change causes problems, remove the newly added IPs to restore the previous state while you investigate further.

 

## ESCALATION** ⏫**

- 
**Raise a Support Ticket:** If the issue persists, submit a detailed ticket through the Jira support portal.

- 
**Consult the Team:** For additional assistance, use the #ask-notifications Slack channel to consult with the notifications team.

 
 

## FAQs** ****❓**

How should I handle automated retries and manually resend webhooks?Our system automatically retries failed webhooks. If you need to manually replay failed events or retrigger them for any reason, refer to the following documentation:

- [Automatic retries](https://example.com/docs/retries)

- [Retrigger events](https://example.com/docs/retrigger)

How can I be notified of chargebacks?You can use our Dispute API or enroll for Webhook Chargeback Notifications. Otherwise, you will need to monitor chargebacks manually on the Dashboard or by retrieving chargeback reports.Does this SOP apply to Order issues on e-commerce plugins ?Yes, our e-commerce plugins rely on webhooks to update Order statuses based on the payment outcome. Each e-commerce plugin will have their own specific order management settings that can apply to the different types of webhooks received e.g Capture Order Status - Processing in Magento
