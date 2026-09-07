---
id: 30550800650130
section_id: 26817954592018
title: "APM \u2013 Payment failed with 422 \u201capm_service_unavailable\u201d"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/30550800650130-APM-Payment-failed-with-422-apm-service-unavailable"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-12-04T12:38:52Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JVW5V7B7TZ05VVPPCG5ZEHCF"]
label_names: ["422 error"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

When a merchant reports that they are receiving the error response 422 “apm_service_unavailable”.

**Problem/Symptom**

Merchant cannot initiate payments, API returns 'service_unavailable_error'.

## DESCRIBE THE ISSUE 💬

The merchant attempts to initiate a payment but fails immediately. Instead of a successful transaction, they receive a specific JSON error indicating that the Alternative Payment Method (APM) service is unavailable.

This issue typically halts the payment flow before it reaches the Gateway, meaning standard payment ID searches will not yield results. The error usually stems from either a configuration mismatch in the Client Admin Tool (CAT) or a downtime incident with the third-party APM provider.

```{
    "request_id": "aa446813-f4bd-4f86-8a07-0db5ace000ba",
    "error_type": "service_unavailable_error",
    "error_codes": ["apm_service_unavailable"]
}
```

 

## TOOLING**📍**

| Tool | Access |
| --- | --- |
| [DataDog](https://app.datadoghq.eu/dashboard/cya-7rs-8v3?fromUser=false&refresh_mode=sliding&from_ts=1764841936612&to_ts=1764845536612&live=true)   [Client Admin Tool(CAT)](https://client-admin.cko-prod.ckotech.co/web/nas/) | Access granted via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274) |

## PROCESS FOR ANALYZING ERROR 422 🖊️

Step 1. Gather Error Details

Request the specific error response from the merchant. Confirm that the `error_code` matches `apm_service_unavailable` and ask for the `request_id`.

💡 Tip: You cannot search for logs using a Payment ID for this error, as the failure occurs before the request hits the Gateway. You must use the `request_id` provided in the error response.
Step 2. Analyze Logs in DataDog

- Open DataDog and use [these filters](https://app.datadoghq.com/logs?query=%28service%3AMerchant.Api%20OR%20service%3A%22Gateway%20API%22%29%20%40Properties.Response.RequestId%3Aaa446813-f4bd-4f86-8a07-0db5ace000ba&agg_m=count&agg_m_source=base&agg_t=count&cols=service%2Cenv%2C%40http.status_code%2C%40PaymentAction%2C%40Properties.Request.Source.type%2C%40Properties.Request.Source.Number%2C%40Properties.Request.MerchantInitiated%2C%40Properties.Request.Currency%2C%40Properties.Request.3ds.Enabled%2C%40Properties.MerchantId&fromUser=true&index=processing&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=time%2Cdesc&viz=stream&from_ts=1664101251355&to_ts=1666693251355&live=true) 

- Filter logs using the `request_id` (e.g., `aa446813-f4bd-4f86-8a07-0db5ace000ba`).

- 
Analyze the logs for specific error patterns:

  - **Scenario A (Timeouts/Internal Errors):** If you see `504 Gateway Timeout` or internal server errors, the issue is likely with the APM provider itself (downtime or intermittent failure).

  - **Scenario B (Configuration Error):** If logs suggest validation failures, proceed to Step 3.

Step 3. Verify Configuration in CAT

Incorrect configurations are a common cause for this error

- Access the ****[Client Admin Tool (CAT)](https://client-admin.cko-prod.ckotech.co/web/nas/)

- Verify the Merchant ID (MID), Country and Currency settings

- Compare these settings against the specific **APM Onboarding Page** in Confluence to ensure all mandatory fields are correct.

⚠️ Note: If the merchant is in Production, cross-reference findings with the Merchant Configuration Team. If in Sandbox, consult with Level 2 support.

## RESOLUTION ⚒️

Once the issue is diagnosed, follow the appropriate remediation path.

### Remediation Steps

- **Validate Request Parameters:** Ask the merchant for the full raw request they are sending. Verify that **all** mandatory parameters (as defined in the developer docs) are present. Missing parameters often trigger this 422 error.

- **Correct CAT Configurations:** If a mismatch was found in Step 3, update the settings in CAT to match the required APM specifications.

- 
**Test Internal Setup:** Attempt to create a payment using the internal test setup.

  - **If the internal test fails:** This confirms a wider issue. Contact the respective third-party APM support team via email.

  - **If the internal test passes:** The issue is isolated to the merchant's specific integration or configuration.

### Expected Result

The merchant is able to initiate the payment successfully without receiving the `apm_service_unavailable` error.

## ESCALATION** ⏫**

If the issue persists after verifying configurations, testing internally, and checking for valid request parameters, escalate the case.

- **Who to escalate to:** APM Engineering L3 Team

- **How to escalate:** Use the [L3 Escalation Form here](https://www.google.com/search?q=%23)

- 
**Required Information:**

  - `request_id`

  - Screenshots of the error

  - Confirmation that CAT config and mandatory parameters have been validated

  - Results of your internal testing

## RESOURCES** ⭐**

| Case Examples | Related Links |
| --- | --- |
| - [Case 8873](https://checkout1360.zendesk.com/agent/tickets/8873)  - [Case 63754](https://checkout1360.zendesk.com/agent/tickets/63754)  - [Case 86109](https://checkout1360.zendesk.com/agent/tickets/86109) | [Internal APM knowledge space](https://checkout.atlassian.net/wiki/spaces/APM/overview?homepageId=279478468) |
