---
id: 29606868753810
section_id: 22188556181906
title: "Handling Redirection URL Issues"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/29606868753810-Handling-Redirection-URL-Issues"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-12-09T09:22:39Z"
permission_group_id: 26838654181266
content_tag_ids: []
label_names: []
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

This guide is for troubleshooting scenarios where a customer is not successfully redirected back to the merchant's website after completing a payment, especially after a 3D Secure (3DS) challenge, which may cause the payment status to remain "pending".

**Problem:** A customer completes a payment, but the transaction status remains "pending" in the merchant's system because the customer was not redirected to the specified success URL.

**Solution:** Investigate the redirection flow using logs, confirm the payment's actual status, and guide the merchant to use webhooks as the definitive method for payment confirmation.

## DESCRIBE THE ISSUE 💬

Merchants report that some transactions are stuck in a "pending" state within their system, even when the customer believes the payment was successful. This typically occurs after a payment flow involving a redirection, such as a 3D Secure authentication. The core issue is the customer's browser does not return to the merchant's designated `success_url`, preventing the merchant's frontend from receiving the final confirmation. This guide is for support agents assisting merchants in diagnosing this redirection failure and implementing a reliable solution.

## KEY TAKEAWAYS 🔑

- Browser-based redirection is not a guaranteed method for payment confirmation.

- The most common cause of failure is the customer closing their browser tab before the redirection completes.

- Webhooks provide a secure, server-to-server confirmation and are the recommended source of truth for payment status.

- Datadog logs can be used to verify if the redirection process was interrupted.  
 

## RESOURCES📍

| Tools | Documentation | Related Tickets |
| --- | --- | --- |
| [CAT (Client Admin Tool)](link-to-cat) [Datadog](link-to-datadog) [API Client (e.g., Postman)](link-to-postman) | [Redirect the customer](link-to-docs-redirect) [API Reference: Create Session](link-to-api-sessions) | [52476](link-to-webhooks-guide) [69216](https://checkout1360.zendesk.com/agent/tickets/69216) |

## PROCESS FOR TROUBLESHOOTING POST-PAYMENT REDIRECTION FAILURES 🖊️

This process involves standard checks of the payment session logs to determine the point of failure and advising the merchant on best practices for payment confirmation.

### Step 1. Understand the Common Causes of Incomplete Redirection

The issue almost always occurs when the customer is not successfully sent back to the merchant's `success_url` or `failure_url`. The primary reasons are:

- 
**Customer Action (Most Common):** The customer closes their browser tab or window too quickly after authenticating the payment but before the redirection process fully completes.

- 
**Incorrect URL:** The merchant's success or failure URL is misconfigured due to typos, incorrect protocols (HTTP vs. HTTPS), or an invalid path.

### Step 2. Review the Redirection Flow

Familiarise yourself with the standard process to identify the potential point of failure:

- When a merchant creates a payment session, they receive a `202 - Accepted` response containing a `_links.redirect` URL.

- The customer is sent to this URL to complete the payment or 3DS challenge.

- If this redirection process is interrupted (e.g., the browser is closed), the payment status in our system may not be updated from "Pending." It will remain in this state until it expires, even if the financial transaction was approved.

### Step 3. Confirm the Issue with Datadog Logs

1. 
**Find the Payment Session:** Use the transaction details to locate the payment session logs in Datadog.

2. 
**Check the Redirect URI:** Inside the logs, verify the `success_url` and `failure_url` that were provided during session creation.

3. 
**Look for Missing Confirmation:** Review the logs to see if the final confirmation step from the redirection is absent. If it is, this confirms that the redirection process was interrupted and is the likely cause of the "pending" status reported by the merchant.

### Step 4. Advise the Merchant on the Source of Truth (Webhooks)

While customer-facing redirects are important for user experience, they are not a reliable method for confirming payment success.

- 
**Recommend Webhooks:** Inform the merchant that the most reliable method to confirm a payment's final status is by listening for webhook notifications (e.g., `payment_approved`, `payment_captured`, `payment_declined`).

- 
**Explain the Benefit:** Webhooks provide a direct, secure server-to-server confirmation of the payment status, bypassing any potential interruptions or issues with the customer's browser.

## RESOLUTION ⚒️

Following these steps will allow the agent to identify the root cause of the "pending" payment status and guide the merchant toward a more robust payment confirmation solution.

- 
**Expected Result:** The merchant understands why redirection fails and acknowledges the need to implement webhooks for reliable payment status tracking.

- 
**Remediation Steps:**

  1. Advise the merchant to review and correct their `success_url` and `failure_url` configurations.

  2. Strongly recommend the implementation of webhook listeners to handle all final payment statuses.

- 
**Check for Resolution:** The problem is fully resolved when the merchant has successfully implemented webhooks to update order statuses in their system, eliminating their dependency on frontend redirection.  
 

## ESCALATION** ⏫**

- 
**When to Escalate:** If Datadog logs show that our system failed to send the customer to the correct redirection URL, or if there is evidence of a systemic issue beyond a single user's browser, escalation is required.

- 
**Required Information:** Include the payment session ID, relevant Datadog logs, and a clear description of the suspected issue.

- 
**Primary Channel:** For all redirection and authentication-related issues, use the **#ask-authentication** Slack channel.

- 
**Follow-up:** If you do not receive a response in the channel within 24 hours, follow up on the thread.

## FAQs ❓

Q. Why is the redirection page taking a long time to load or freezing?A. This issue typically occurs if the merchant's `success_url` or `failure_url` is slow to load. The delay is related to the performance of the merchant's own website and is outside of our control.Q. How can the merchant improve a slow redirection experience for their customers?A. The recommended solution is for the merchant to implement an interim loading page. This page can display a "Processing your order..." message immediately upon redirection, providing a better user experience while their back-end systems process the payment confirmation from a webhook and update the order status.
