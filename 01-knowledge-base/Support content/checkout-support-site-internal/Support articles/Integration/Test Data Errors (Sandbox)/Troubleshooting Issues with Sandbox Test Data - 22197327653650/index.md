---
id: 22197327653650
section_id: 22188572850706
title: "Troubleshooting Issues with Sandbox Test Data"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22197327653650-Troubleshooting-Issues-with-Sandbox-Test-Data"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-15T16:41:35Z"
permission_group_id: 26838654181266
content_tag_ids: ["01H8EDHC0MTG4YFD7E4B42CE0V"]
label_names: ["global", "case_integration", "case_integration_issue_issues_with_test_data__sandbox_", "how_to_troubleshoot_issues_with_test_data"]
user_segment_ids: [11003606966930]
archive: false
---

**Use this article when**

A merchant is experiencing issues with their integration, particularly with payment methods or test transactions, and needs our assistance to diagnose and resolve the problem.

TOOLS & REOURCES 📍 

| Tools | Linked Articles |
| --- | --- |
| - Postman: To run API requests and test scenarios.N/A[Test Cards Documentation](https://www.google.com/search?q=https://www.cko.com/docs/test-cards)   - Datadog: To retrieve merchant API requests.N/A[API Reference Page](https://www.google.com/search?q=https://docs.cko.com/api-reference)   - CAT (Configuration Audit Tool): To verify merchant configurations  - Slack Channel: #ask-gateway | Merchant Facing articles:  - [Test Cards Documentation](https://www.checkout.com/docs/developer-resources/testing/test-cards) |

PROCESS FOR TROUBLESHOOTING TEST DATA ISSUES🖊️Step 1: Reproduce the Issue

The first step is to reproduce the issue on your own account to confirm the problem and understand the context.

- 
**Get the API request:** Use [Datadog](https://app.datadoghq.com/logs?query=%40Properties.CkoClientId%3Acli_izjltzbmrhkuxiemiox65bcdvu&cols=service%2Cenv%2C%40http.status_code%2C%40PaymentAction%2C%40Properties.Request.Source.type%2C%40Properties.Request.Source.Number%2C%40Properties.Request.MerchantInitiated%2C%40Properties.Request.Currency%2C%40Properties.Request.3ds.Enabled%2C%40Properties.MerchantId&index=processing&messageDisplay=inline&refresh_mode=sliding&saved-view-id=88535&stream_sort=time%2Cdesc&viz=stream&from_ts=1664101251355&to_ts=1666693251355&live=true) to search for the specific API request the merchant used. You can search by their Client ID

- 
**Verify configuration:** Use the CAT tool to ensure that the processor configured on your account is the same as the merchant's configuration ⚠️This is crucial for an accurate reproduction of the issue.

- 
**Run the request in Postman:**

  - Open Postman and create a new request

  - Choose the request type (e.g., `POST`, `GET`) based on the API reference [page](https://api-reference.checkout.com/#tag/Payments)

  - Copy the [request URL](https://api.sandbox.checkout.com/payments) from the API reference page

  - Set the `Authorization` header. This is typically a `Bearer` token with your API key. For example, `Key: Authorization`, `Value: Bearer + "Your API Key"`

- Copy the sample JSON body from the [API reference](https://api-reference.checkout.com/#tag/Payments) or the merchant's request and paste it into the body section of your Postman request

**⚠️ Warning:** If your Access/API key is configured with more than one processing channel, you must add the `"processing_channel_id"` parameter to the request body, along with your specific processing channel ID

- 
**Simulate the transaction:** Use the relevant test card details from the [Test Cards Documentation](https://www.google.com/search?q=https://www.cko.com/docs/test-cards) to run the same request using your own account's API key and processing channel

- 
**Verify the issue:** Click "Send" to run the API and wait for the response. Compare the response with the issue the merchant reported. You should see the same error or behavior

Step 2: Resolve the Issue

Based on the response you received in Postman, you can now advise the merchant on the resolution.

- 
**Error Code:** If you receive an error code in the response, refer to the API reference documentation. The error code will provide details on the reason for the failure.

- 
**Advise the merchant:** Based on the error code, you will be able to advise the merchant on how to correct their API request, configuration, or other related issues.

ESCALATION ⬆️

If you have followed the steps above and are unable to resolve the issue, or if the test cards themselves are not working as expected, it may require escalation:

**When to escalate:**

- Test cards are consistently failing across different scenarios for multiple users

- The error code is not documented or is unclear

- The issue seems to be with the gateway or backend system, not the merchant's integration

**How to escalate:**

- Escalate the issue to the **#ask-gateway** Slack channel

- Provide the following information in your message:

  - Client ID and relevant API requests

  - The specific test card used

  - The steps you took to reproduce the issue

  - The exact error code and response body received

  - A summary of your findings and why you believe it requires the gateway team's investigation

- Stay on the case and monitor the Slack channel for updates

- Notify the merchant that you have escalated the issue and will update them as soon as you have more information
