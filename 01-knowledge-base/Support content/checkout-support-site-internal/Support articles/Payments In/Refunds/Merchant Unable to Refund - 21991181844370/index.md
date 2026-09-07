---
id: 21991181844370
section_id: 21991163953810
title: "Merchant Unable to Refund"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/21991181844370-Merchant-Unable-to-Refund"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-03-18T14:20:28Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQT889RQXXSG27BB4ZJ0M"]
label_names: ["case_transactions", "ROW", "case_transactions_issue_unable_to_refund", "unable_to_refund"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

When a merchant is unable to successfully **refund** a transaction and contacts us for support.

**Case type: **Payments in

**Issue Type: **Transaction status (Non 3DS & Refunds)

**Reason: **Refund failed / manual refund

## INTRODUCTION TO THE ISSUE 💬

This article provides a troubleshooting guide for cases where a merchant is unable to successfully **refund** a transaction. This issue typically occurs when a payment is in a "captured" or "partially captured" state but cannot be refunded via the merchant's dashboard or API.

Understanding why a refund fails requires us to investigate the root cause, which can be related to the merchant's setup, a bug in our system, or an external factor like a scheme or bank issue. This guide will walk you through the diagnostic process.

The most common reasons for refund fails are:

- The merchant is sending incorrect or invalid data in their API request

- Refunds are disabled in the merchant's configuration

- A bug in our API or dashboard is preventing the refund

- An external incident or outage occurred (e.g., at a scheme or bank)

- Transaction already disputed; refund attempts return HTTP 403

## PROCESS STEPS 🖊️

### Step 1: Identify the Payment and Check Traffic Insights

First, get the **Payment ID** from the merchant's information. Then, use this ID to search in Traffic Insights.

- If you see a `chargeRefunded` event, the refund was successful, and no further action is required

- If you see a `chargeRefundDeclined` event, the refund was requested but declined by the issuing bank or scheme

💡 Refer to the **Response Code Unclear** SOPs for more information (link under resources below)

- If you don't see any refund-related events, proceed to the next step

### Step 2: Check Logs in Datadog

Search for the Payment ID in [Datadog](https://app.datadoghq.com/logs?query=%40PaymentId%3Apay_wykl5vo2mdb23fk6v7bae4cg3m&ag[%E2%80%A6]z=stream&from_ts=1649747918643&to_ts=1651043918643&live=true) logs by using `@PaymentId`

- 
**HTTP Status Code 422:** If the  [logs](https://api.checkout.com/payments/pay_xxx/refunds) show a `422` status code, the merchant sent invalid data in their request. Refer to the common 422 [error codes documentation](https://checkout.atlassian.net/wiki/spaces/GW/pages/5624430773/Investigating+payment+errors#Common-422-Validation-Errors-and-Investigating) for the likely cause

- 
**Other 4XX or 5XX Status Codes:** If you see any other `4XX` or `5XX` code (e.g., `401`, `403`, `404`, `502`), consult the [common reasons for these status codes](https://checkout.atlassian.net/wiki/spaces/GW/pages/5624430773/How+to+Investigate+payment+errors#Other-Common-HTTP-Codes)

⚠️ **Warning:** A `403` status code often indicates that the transaction is already **disputed** and cannot be refunded

### Step 3: Verify Rate Limits

A failed refund can sometimes be due to the merchant hitting a **rate limit**. Check this in Slack:

- Go to Slack 

- Type `/rate-limit <Client ID>/refunds POST` (ensure there is a space before `/refunds`)

- If the rate limit needs to be increased, post in the `#rate_limiting` Slack channel

### Step 4: Check for Outages or Incidents

Check the **OC (Outage Communications)** Slack channel to see if any recent incidents or outages align with the time the refund failed. This can confirm if the issue was part of a wider system problem.

## ESCALATIONS ⬆️

If you've completed all the steps above and the root cause for the failed refund is still not clear, you should **escalate** the case.

- 
**Escalate to L2:** This is the appropriate escalation path when the issue appears to be a bug or the reason for the failure cannot be identified through standard troubleshooting, use the Macro:

| Macro: L1>L2 |
| --- |

**RESOURCES ⭐️**

| Related Articles |
| --- |
| - [Response Code Unclear](https://checkoutint.zendesk.com/hc/en-us/sections/21991160409234-Response-code-unclear)  - [Response Code Unclear - MENA](https://checkoutint.zendesk.com/hc/en-us/sections/21991145657362-Response-code-unclear)  - [422 Error Codes](https://checkout.atlassian.net/wiki/spaces/GW/pages/5624430773/Investigating+payment+errors#Common-422-Validation-Errors-and-Investigating)  - [Common HTTP Error Codes](https://checkout.atlassian.net/wiki/spaces/GW/pages/5624430773/Investigating+payment+errors#Other-Common-HTTP-Codes) |
