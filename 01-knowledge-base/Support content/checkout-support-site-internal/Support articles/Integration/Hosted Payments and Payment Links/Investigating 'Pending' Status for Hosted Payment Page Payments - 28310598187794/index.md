---
id: 28310598187794
section_id: 22188552840594
title: "Investigating 'Pending' Status for Hosted Payment Page Payments"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/28310598187794-Investigating-Pending-Status-for-Hosted-Payment-Page-Payments"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-08-06T13:56:36Z"
permission_group_id: 26838654181266
content_tag_ids: ["01K0YPEVRSXXEYB936K329TF6D", "01K0YPFBSHBA4R57ZGBPSED26T", "01K0YPFNT4QX4PX3Q34M6Z4789"]
label_names: ["hosted_payment_pages", "HPP", "payment_interfaces"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

If a merchant reports that a Hosted Payment Page (HPP) payment status is 'Pending', while the main Dashboard shows the same transaction as 'Captured'.

**Problem -**The merchant sees a payment is captured on the Dashboard, but the corresponding HPP status is stuck in a 'Pending' state.

**Solution - **Explain that this occurs when the customer closes their browser before the post-payment redirection completes and confirm that the main Dashboard is the correct source of truth for the payment status.

 

 

## KEY TAKEAWAYS 🔑

- When an HPP status is "pending" but the payment is "Captured" on the Dashboard, it's typically due to an incomplete browser redirection after the 3DS challenge

- In this scenario, the main Dashboard should always be used as the definitive source of truth for the payment status

- The HPP status cannot be changed from "pending" after the event, as the final update was missed

## RESOURCES 📍

| Tools | Case Examples | Related |
| --- | --- | --- |
| [Hosted Enablement Tool](https://retoolprod.mgmt.ckotech.co/apps/f67192a4-a90a-11ec-841c-938543b18be9/launchpad/Merchant%20Hosted%20Pages%20Enablement) | [Payment stuck on pending](https://checkout1360.zendesk.com/agent/tickets/48261) | [Confluence](https://checkout.atlassian.net/wiki/spaces/PI/pages/6092881943/Payment+Experience+FAQ+Document) |

## PROCESS FOR INVESTIGATING PENDING HPP STATUS 🖊️

## Step 1. Understand the Cause: Incomplete Redirection

- This issue almost always occurs when the customer is not successfully redirected back to the merchant's specified `success_url` after completing a 3D Secure (3DS) challenge

- The most common reason for this is the customer closing their browser tab or window too quickly after authenticating the payment but before the redirection completes

## Step 2. Review the HPP Status Flow

- The HPP system relies on the browser being successfully redirected to receive the final payment status update from the gateway

- If this redirection is interrupted, the HPP cannot update its status from "pending." It will remain in this state until it eventually expires, even though the underlying financial transaction was approved and captured

## Step 3. Confirm the Issue with Logs

- You can confirm this behaviour by comparing logs in [Datadog](https://app.datadoghq.com/logs?query=%40PaymentSessionId%3Aps_2VaI3uDP9R1GCp5ihMWRdThdHo4&agg_m=count&agg_m_source=base&agg_t=count&cols=host%2Cservice&fromUser=true&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=desc&viz=stream&from_ts=1694272949000&to_ts=1695136949000&live=true), see slack [chat](https://checkout.slack.com/archives/C0193U64C2E/p1695198918882239?thread_ts=1695132516.138819&cid=C0193U64C2E)

- Examine the logs of a successful HPP payment and look for a `hosted-payments/redirect-v2` scope or verify the `RedirectUri` in the 3DS log to confirm a completed redirection

- Next, review the logs for the transaction that is stuck in "pending." You will notice that this redirection confirmation is missing

## Step 4. Determine the Source of Truth

- It is crucial to understand that the HPP status is secondary to the actual payment status

- 
**Always use the main Dashboard as the definitive source of truth:** The Dashboard reflects the actual outcome of the financial transaction. If the Dashboard shows the payment as "Captured," the merchant has been paid successfully

- We recommend that Merchant listen for Payment Webhooks, as there is the possibility that end users close the asynchronous flow in the browser once they have complete the Payment

**💡 Best Practice:** Advise the merchant that while the HPP status may be "pending" in these cases, they should rely on the Dashboard status or webhook notifications for their order fulfilment and reconciliation processes.

## RESOLUTION ⚒️

**Expected Result**

- The support agent and merchant will understand that this is expected behavior when a user interrupts the payment flow and that the "Captured" status on the Dashboard confirms the payment was successful.

**Remediation Steps**

- This issue is resolved through clarification, not a technical fix. Advise the merchant to use the main Dashboard status or set up webhook notifications for payment events, as these provide a more reliable server-to-server confirmation than a client-side browser redirect.

**Check Problem is Resolved**

- Resolution is confirmed when the merchant acknowledges their understanding of the process.

- As a proactive measure, confirm that the merchant has webhooks configured for critical payment events (e.g `payment_captured`, `payment_approved`) to ensure they receive reliable notifications.

**Rollback/Recovery**

- Not applicable. No system changes are made; the resolution is informational

## ESCALATION** ⏫**

This behavior is an expected outcome of an interrupted user flow. However, if you suspect a technical issue beyond user action, you can raise it in the `**#payment-interfaces**` Slack channel for review.

 
 

## FAQs** ？**

A customer is being redirected to the wrong URL after a payment attempt. How can I fix this?A.This can occur if the default success and failure URLs are being used instead of the ones specified in the request.

1. 
**Verify URLs in CAT**: Log in to the Client Admin Tool (CAT) and check the configured success and failure URLs for the merchant's processing channel. Confirm with the merchant that these URLs are correct.

2. 
**Check 3DS Log**: Access the 3DS log for the transaction and find the `RedirectUri` parameter to confirm which URL was used for the redirection.

3. 
**Correct and Test**: If the URLs in CAT are incorrect, update them. Ensure the merchant is passing the correct URLs in the payment request if they are not relying on the defaults.

How can I omit the Apple Pay or Google Pay button from the Hosted Payment Page?A. You can hide these buttons by passing a specific parameter in your API request.

- 
**To hide Apple Pay**: Pass the parameter `"disabled_payment_methods":"applepay"`

- 
**To hide Google Pay**: Pass the parameter `"disabled_payment_methods":"googlepay"`

Are there specific instructions for Offsite Shopify merchants regarding Apple Pay and Google Pay on the Hosted Payment Page?A.Yes.

- 
**Shopify Onsite**: Merchants using the onsite integration do not need to register a separate account with Apple Pay. They should follow the
[Shopify onsite payments app guide](https://www.checkout.com/docs/payments/accept-payments/connect-to-an-ecommerce-platform/shopify) to activate Apple Pay and must adhere to Apple's Acceptable Use Guidelines. The same steps apply for Google Pay.

- 
**Shopify Offsite**: For merchants using the offsite plugin, Apple Pay and Google Pay will only be available for MENA customers.
