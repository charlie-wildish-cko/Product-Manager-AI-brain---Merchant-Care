---
id: 29566262103442
section_id: 22188572850706
title: "How to Replicate and Resolve Merchant Issues in Sandbox"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/29566262103442-How-to-Replicate-and-Resolve-Merchant-Issues-in-Sandbox"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-09-29T11:01:43Z"
permission_group_id: 26838654181266
content_tag_ids: ["01K5E54S1SVT0CH56GGKATNQBZ", "01K5E556304P9E6AAM865CS50T"]
label_names: ["sandbox", "reproducing"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**  

To reproduce a merchant's reported issue in a sandbox environment to diagnose the root cause of an error.  

**Problem - **A merchant is experiencing a failing API request or payment flow, and the issue needs to be replicated in a controlled test environment to find a solution.  

**Solution - **Configure a sandbox environment to mirror the merchant's setup, use Postman and test data to reproduce the error, identify the failing component, and provide a fix.  

## DESCRIBE THE ISSUE 💬

This Standard Operating Procedure (SOP) outlines how to reproduce a merchant's reported issue within a sandbox environment. The primary goal is to replicate the exact conditions of a problem to diagnose the root cause accurately.

This process is used for a variety of debugging scenarios, including:

- Reproducing a merchant's API request to understand why it's failing (e.g., receiving a `422` error)

- Testing different request payloads to see how specific fields change the payment outcome

- Confirming the correct workflow for Alternative Payment Methods (APMs), including redirects to success or failure URLs

- Verifying system limitations and behaviors with specific test data

 
 

## KEY TAKEAWAYS 🔑

- Always mirror the merchant's configuration in your sandbox using the Client Admin Tool (CAT) before running any tests

- If the merchant's request payload is missing, retrieve it from Datadog using their Client ID

- Use Postman for API-level debugging and a test website for APMs that require redirection

- If you cannot find a solution after reproducing the error, escalate to the appropriate team's Slack channel (e.g., #ask-apms, #ask-gateway)

 

## RESOURCES 📍

| Tools | Related Articles |
| --- | --- |
| -  **Postman**: For sending API requests to the sandbox environment  -  **A sandbox or test integration website**: Required for testing APMs that involve website redirection  -  **Client Admin Tool (CAT)**: To configure the test environment  -  **Datadog**: To retrieve merchant API requests if not provided | -  ****[Test Cards](https://www.checkout.com/docs/developer-resources/testing/test-cards): For simulating various card payment scenarios  -  ****[API Reference](https://api-reference.checkout.com/): To check required fields, scopes, and endpoints for specific API calls  -  ****[Product Documentation:](https://www.checkout.com/docs) To find example payment requests for specific products or payment methods |

 

## PROCESS FOR SANDBOX DEBUGGING 🖊️

**Step 1. Obtain the Merchant's API Request**

If the merchant has not included the failing API request payload in their support ticket, you must retrieve it from Datadog.

- Navigate to Datadog logs

- Search using the merchant's **Client ID**

- Filter the results by the specific response code or error code mentioned by the merchant to locate the exact failed request

**Step 2. Configure Your Sandbox Environment**

To ensure an accurate test, your sandbox account must mirror the merchant's environment configuration.

- Log in to the **Client Admin Tool (CAT)**

- Review the merchant's configuration and replicate the following settings on your own sandbox processor:

  - Merchant Category Code (MCC)

  - Entity location

  - BAI (Billing Account Information) value

  - AFT (Account Funding Transaction) processing value

  - Enabled currencies

**Step 3. Replicate the Request in Postman**

- 
**URL**: Set the request URL in Postman to the same API endpoint the merchant is using, but ensure it points to the sandbox environment (e.g., `https://api.sandbox.checkout.com/payments`)

- 
**Headers**: Add an `Authorization` header. Check the API Reference page for the specific endpoint to determine if you need to use a Secret Key, Public Key, or Access Key

- 
**Body**: Copy the merchant's request payload into the request body - to isolate the problem it is best practice to only include the relevant fields for the test

- Click **Send** to run the request and reproduce the error

**Step 4. Diagnose and Resolve the Issue**

Once you have successfully reproduced the error in Postman, follow this debugging process:

- Analyze the error response to understand the cause of failure.

- Modify the values of different fields in the request body one at a time and resend the request after each change.

- When a change successfully resolves the error, document exactly which field and value provided the fix.

- Clearly communicate the solution to the merchant.

**⚠️ Testing Alternative Payment Methods (APMs)**  
For APMs that require an SDK or involve redirection (e.g., Sofort, iDEAL), you must use a test integration website instead of Postman to complete the flow. 

Refer to the [official Checkout.com documentation](https://www.checkout.com/docs) for the specific test values and credentials needed for each APM.

## RESOLUTION ⚒️

The expected outcome is a clear identification of the problem's root cause and a documented solution that can be provided to the merchant. The agent should be able to confirm the fix works in the sandbox environment before communicating the steps for resolution.

## ESCALATION** ⏫**

If you successfully reproduce an issue but cannot find a solution, the escalation path depends on the nature of the problem. Identify the team that supports the failing component and reach out in their dedicated Slack channel for assistance:

- For issues with **Alternative Payment Methods**, use the `#ask-apms` channel

- For **403 errors** or other gateway-related problems, use the `#ask-gateway` channel

## FAQs** ****❓**

What is a common mistake when trying to reproduce an error?

A common mistake is using the incorrect API endpoint in Postman. To find the correct endpoint, you should always check the Datadog logs for the merchant's original failed request. The path that comes after the base URL (e.g., `/payments` or `/tokens`) is the endpoint you must use. Verify this path matches an official endpoint on our API Reference page.
