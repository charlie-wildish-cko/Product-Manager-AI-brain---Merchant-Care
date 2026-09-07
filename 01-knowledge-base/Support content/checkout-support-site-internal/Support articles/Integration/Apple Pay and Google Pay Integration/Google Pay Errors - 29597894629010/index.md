---
id: 29597894629010
section_id: 22188546107666
title: "Google Pay Errors"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/29597894629010-Google-Pay-Errors"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-09-29T12:13:54Z"
permission_group_id: 26838654181266
content_tag_ids: ["01K5GZBB1WTESD7J7JK1VGJ33V", "01K5GZBKSD264XY7TGY0RWRAN8", "01K5GZBVVHSYX8VK3HAV0WER5N"]
label_names: ["google_pay", "apple_pay_and_google_pay_integration", "google_pay_errors"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

To troubleshoot common errors that can occur during and after the integration of Google Pay.

**Problem:** Issues such as the Google Pay button not appearing or specific error messages during payment processing can disrupt the customer experience.

**Solution:** This guide provides solutions for common problems like invalid tokens, registration errors, and display issues to ensure a smooth Google Pay experience.

## DESCRIBE THE ISSUE 💬

After setting up Google Pay, a merchant might encounter issues like the payment button not displaying, or receiving specific error codes (e.g., `token_data_invalid`, `OR_BIBED_11`) during a transaction. This guide is for anyone troubleshooting these post-integration problems to identify the root cause and apply the correct fix.

 
 

## KEY TAKEAWAYS 🔑

- Always gather initial information first: integration method and relevant IDs

- 
`token_data_invalid` errors are often caused by an incorrect request format or a public key mismatch

- The `OR_BIBED_11` error means domain registration in the Google Pay & Wallet Console is incomplete

- If the Google Pay button is missing, check for a conflicting Content Security Policy (CSP) or a duplicate Google Pay SDK script loading on the page

- Use Datadog and the Integrations website to investigate and replicate errors

## RESOURCES 📍

| Tools | Case Examples | Related |
| --- | --- | --- |
| [Datadog](https://app.datadoghq.com/) [Integrations Website](https://example.com/integrations-site) | [Example 1](https://checkout1360.zendesk.com/agent/tickets/51581) [Example 2](https://checkout1360.zendesk.com/agent/tickets/73188) [Example 3](https://checkout1360.zendesk.com/agent/tickets/68135) | [Google Pay & Wallet Console](https://pay.google.com/business/console) |

## PROCESS FOR TROUBLESHOOTING GOOGLE PAY ERRORS 🖊️

This process involves standard checks using logs and console settings to diagnose and resolve common Google Pay integration issues.
**Step 1. Gather Initial Information**

Before troubleshooting, collect the following key details from the merchant:

- The integration method being used (API Only or Flow)

- The name of the account on NAS

- Any relevant payment or request IDs associated with the error

**Step 2. Troubleshoot Common Errors**

**Error: **`**token_data_invalid**`** when converting a Google Pay token to a Checkout card token**

**Cause:** This can be due to an incorrect format in the token data request or a mismatch of the public key.

**Solution:**

- Confirm that the token data in the request is in the correct format and contains all required fields.

- If the format is correct, verify that the public key being used as the `gatewayMerchantId` is the same key used in the token's header request.

**Error: **`**OR_BIBED_11**`** displays when the Google Pay button is clicked**

**Cause:** This error indicates that the registration to use the Google Pay API has not been completed.

**Solution:**

- Navigate to the [Google Pay & Wallet Console](https://pay.google.com/business/console)

- Complete the required steps to verify the domain

**Error: The Google Pay button is not showing on the website**

**Cause 1:** A Content Security Policy (CSP) configuration is blocking Google Pay domains.

**Cause 2:** A previous Google Pay integration is already loading the Google Pay SDK on the web page, causing a conflict with the Flow integration.

**Solution:**

- Check the browser's developer console for CSP errors related to Google domains and adjust the policy if necessary.

- If you are loading the Google Pay SDK script yourself and using Flow, it will prevent Flow from loading the SDK correctly. Remove the script loading from your website and allow Flow to handle it.

## RESOLUTION ⚒️

- 
**Expected Result:** By following these troubleshooting steps, the identified Google Pay error will be resolved. The Google Pay button will display correctly, and transactions will process without error messages, leading to a seamless payment experience.

- 
**Remediation Steps:** After applying a fix, perform a test transaction to confirm the error is gone. For display issues, clear the browser cache and reload the page to ensure the button appears as expected. Check Datadog logs for the absence of previous error messages on new transaction attempts.

- 
**Rollback/Recovery:** Most fixes involve configuration changes. If a change introduces a new problem, revert the configuration (e.g., remove CSP rule) and re-evaluate the root cause.

 
 

## FAQs** ****❓**

How can I replicate Google Pay errors?

You can use the Integrations website to replicate errors. You can also search the `/tokens` endpoint logs in Datadog using your vault account ID and filter by the Correlation ID to see the Google API logs for any errors.
