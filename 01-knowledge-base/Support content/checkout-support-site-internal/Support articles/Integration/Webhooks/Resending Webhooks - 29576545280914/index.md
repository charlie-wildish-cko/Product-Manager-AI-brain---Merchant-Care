---
id: 29576545280914
section_id: 22188517144978
title: "Resending Webhooks"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/29576545280914-Resending-Webhooks"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-31T16:47:11Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JVM5TPJQV63X1YGHPGKWQTJN", "01K5EQ850SJ5QGG7AW2HYQ6PHP", "01K5EQ8AZP5GQ1CKBD4S0SE83T"]
label_names: ["webhook_troubleshooting", "webhook_resending", "reflow_webhook"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

Use this guide when you need to manually resend webhook notifications for specific events or all events related to a particular payment or dispute.

**Problem:** The merchant sometimes misses webhook notifications due to temporary issues with their server endpoint or other system problems, leading to out-of-sync order statuses.

**Solution:** This article provides the step-by-step process for manually retriggering webhooks using our API to ensure the system receives the missed information.

## DESCRIBE THE ISSUE 💬

The merchant's system has missed one or more webhook notifications, possibly due to a temporary server outage or an internal processing error. This has caused a discrepancy in their records (e.g. order statuses are not updated). 

The merchant now needs to manually trigger a resend of these specific webhooks to synchronize the system. 

 

## KEY TAKEAWAYS 🔑

- Webhooks can be resent either individually using an `eventId` or in bulk for a specific subject (like a payment) using a `subjectId`

- API requests must be authenticated with an OAuth 2.0 Bearer Token

- The API key used must have the `flow:events` scope enabled

- Both API methods are `POST` requests and have an empty body

- Use the sandbox API endpoint for testing purposes

## RESOURCES 📍

| Tools | Related |
| --- | --- |
| API Client (Postman) | [Official Documentation: Retrigger events](https://example.com/docs/retrigger-events) [Automatic retries](https://www.checkout.com/docs/developer-resources/webhooks/manage-webhooks/set-up-your-webhook-receiver#Automatic_retries) |

## PROCESS FOR RESENDING WEBHOOKS 🖊️

This process outlines two API-based methods for retriggering webhook notifications. You will need an API client like Postman to execute these requests.

**Method 1: Resend a Single Webhook Notification (by **`**eventId**`**)**

This method is ideal for resending a single, specific event notification that was missed.

- 
**Obtain the Event ID:** You need the unique `eventId` for the webhook you want to resend. This can be found in the original webhook notification or by retrieving events via the API.

- 
**Prepare the API Request:**

  - 
**Method:** `POST`

  - 
**Endpoint:** `https://api.checkout.com/workflows/events/{eventId}/reflow`  
_(Replace _`_{eventId}_`_ with the actual ID from step 1)_

  - 
**Authorization:** The request must be authenticated using an OAuth 2.0 Bearer Token. Ensure the API key has the `flow:events` scope enabled.

  - 
**Body:** This request has an empty body.

- 
**Execute the Request:** Send the request using your API client. A successful response indicates the webhook has been resent.

**Method 2: Resend All Webhooks for a Specific Subject (by **`**subjectId**`**)**

This method is useful when you need to resynchronize your system by receiving all events related to a specific subject, such as a payment or dispute.

- 
**Obtain the Subject ID:** You need the `subjectId`, which is typically the `payment_id` or `dispute_id`.

- 
**Prepare the API Request:**

  - 
**Method:** `POST`

  - 
**Endpoint:** `https://api.checkout.com/workflows/subjects/{subjectId}/reflow`  
_(Replace _`_{subjectId}_`_ with the actual ID, e.g., _`_pay_xxxxxxxx_`_)_

  - 
**Authorization:** The request must be authenticated using an OAuth 2.0 Bearer Token. Ensure the API key has the `flow:events` scope enabled.

  - 
**Body:** This request has an empty body.

- 
**Execute the Request:** Send the request using your API client. A successful response indicates that all webhooks associated with that subject have been resent.

**💡 Note:** For sandbox testing, use the endpoint: `https://api.sandbox.checkout.com/...`

## RESOLUTION ⚒️

- 
**Expected Result:** Upon successful execution of the API request, the specified webhook(s) will be re-sent to the configured endpoint. The merchant's system will receive the missed notifications, allowing it to update its status and synchronize with our records.

- 
**Remediation Steps:** After sending the API request, monitor the server logs to confirm that the resent webhook(s) have been received and processed successfully. You can also check the webhook delivery status in Datadog to see a new delivery attempt with a `200` status code.

- 
**Rollback/Recovery:** This is a one-time action and does not have a direct rollback. If a webhook is resent in error, your system should be idempotent, meaning it can handle duplicate notifications without causing issues (e.g., by checking the `eventId` to see if it has already been processed).

 

## ESCALATION** ⏫**

- If you continue to have issues with the API call or if webhooks are still not being received after a successful "reflow" request, please consult the #ask-notifications Slack channel.

- For persistent issues, raise a detailed support ticket in [Jira.](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277)

 

## FAQs** ****❓**

When should I manually resend webhooks?This process is useful if your endpoint was temporarily down, you had a bug that prevented you from processing incoming webhooks correctly, or you need to sync your system after missing notifications for any other reason.Are failed webhooks retried automatically?Yes, our system automatically attempts to resend webhooks that fail to deliver. This manual process is for exceptional cases where a full replay is needed, not for routine delivery failures.What is the difference between an eventId and a subjectId?An `eventId` refers to a single, specific webhook notification (e.g., `payment_approved`). A `subjectId` refers to the object the events are related to, which is typically the `payment_id`. Retriggering by `subjectId` will resend all events associated with that payment (e.g., `payment_pending`, `payment_approved`, `payment_captured`).What API scope is needed to perform this action?Your API keys must have the `flow:events` scope enabled to use these endpoints.
