---
id: 28249126965778
section_id: 22188546107666
title: "Apple Pay Common Errors"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/28249126965778-Apple-Pay-Common-Errors"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-09-29T12:14:21Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JVM5WYPR2CFA1MQCGT9B790K", "01K5E45R7D7E6MP9X4VJBNNN6P", "01K5E46QDZ9376VGM50A15Q8Q6"]
label_names: ["apple_pay", "apple_pay_and_google_pay_integration", "apple_pay_common_errors"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

To diagnose and resolve common errors merchants may experience with an Apple Pay integration, including missing payment buttons, specific error codes and platform-related issues.

**Problem:** Merchants experiencing technical issues causing Apple Pay transactions to fail or the payment option to not display correctly.

## DESCRIBE THE ISSUE 💬

When using an Apple Pay integration, merchants might encounter issues that prevent it from working correctly. These problems can range from the Apple Pay button not appearing on the checkout page, to specific error messages like "Payment not completed," or transaction failures that can be identified by error codes in logs. This guide is designed to help you methodically identify the root cause of the issue and apply the correct fix.

## KEY TAKEAWAYS 🔑

- Before troubleshooting, always gather key information like the integration type, affected Payment IDs, and a screenshot of your Apple Developer account's Merchant ID (MID) configuration

- A missing Apple Pay button is often due to environmental factors: the user must be on an Apple device using Safari with a card saved in their Wallet

- Error code `400` typically points to an incorrect file path for your `.pem` or `.key` certificate files

- Error code `417` indicates a mismatch between the Merchant ID (MID) in your configuration and the one in your Apple Developer account

- Apple Pay payment processing certificates expire every 25 months and must be renewed correctly to prevent transaction failures

 

## PROCESS FOR TROUBLESHOOTING APPLE PAY ERRORS 🖊️

Follow this process to diagnose and resolve the issue a merchant is facing.
**Step 1. Information Gathering**

Before troubleshooting, it is important to gather as much information as possible. Create a checklist with the following items:

- The integration the merchant is are using (e.g., Shopify, SDK)

- The name of the account on NAS

- Any affected Payment IDs

- A screenshot of the Apple Developer account showing the specific Merchant ID configuration

**Step 2. Triage Common Issues**

Based on the problem the merchant is experiencing, use the following sections to diagnose the cause:

**Issue: The Apple Pay Button is Missing**  
If the Apple Pay button has disappeared, verify the following:

- 
**Device and Browser:** Confirm the merchant is testing on an Apple device using the Safari browser, as Apple Pay only works in this environment

- 
**Device Wallet:** The device must have a payment card saved in the Wallet app

- 
**Site/Plugin Settings:** Ensure Apple Pay is enabled on the site or within the e-commerce plugin's settings

- 
**Developer Account:** The business account must be correctly set up in the Apple Developer portal, and all necessary certificates must be uploaded to the Checkout.com account

**Issue: “Payment not completed” Error on UI**  
This error message on the Apple Pay interface can be resolved with the following steps:

- Restart the Apple Pay setup process from the beginning

- Check that the domain is verified in the Apple Developer portal

- Verify that the merchant is sending the correct `supportedNetworks`, `currencyCode`, and `merchantCapabilities`

**Issue: Expired Payment Processing Certificate**  
⚠️ Apple Pay payment processing certificates are valid for 25 months - an expired certificate will cause all Apple Pay transactions to fail.

- 
**Renewal Process:** To avoid transaction downtime, the merchant must follow a specific renewal process. They must upload the new certificate files to their server and update the file paths **before** activating the new certificate in the Apple Developer account.

**Issue: Specific Error Codes in Logs**

- 
**Error: **`**statusCode: '400'**`

  - 
**Cause:** This error indicates that a merchant does not have the correct file path to the `.pem` and/or `.key` files on the server

  - 
**Solution:** Check that the path configured for the certificate files is correct and accessible from the server

- 
**Error: **`**statusCode: '417'**`

  - 
**Cause:** This error means the merchant identifier (MID) is not the same as the one saved in the Apple Pay developer account

  - 
**Solution:** Compare the MID from the Apple Developer account with the one configured  to ensure they match exactly

**Issue: Shopify Specific Problems**  
If merchants are using the Shopify Onsite plugin, ensure they have followed the setup guide to activate Apple Pay.

- When creating a Shopify API Key, ensure the merchant has **not** selected the 'Allow any processing channel' option, as this will cause payments to fail.

- Shopify determines if Apple Pay is available on the merchants store, it is based on various factors but most common ones are location, MCC and products the store sells. 

## RESOLUTION ⚒️

Following these steps should resolve the specific Apple Pay error, resulting in the payment option being displayed correctly and transactions processing successfully.

- 
**Remediation Steps:**

  - For a `400` error, correct the certificate file path on your server

  - For a `417` error, ensure the Merchant ID in your code matches the one in your Apple Developer account.

  - For a missing button, verify all device, browser, and configuration requirements are met.

- 
**How to Verify Resolution:** Once a fix is applied, confirm that the Apple Pay button appears on a compatible device and that you can successfully complete a test transaction.

 

## ESCALATION** ⏫**

- If you are unable to resolve the issue using this guide, escalate to the appropriate support channel based on your integration:

  - 
**General Gateway Issues:** Use the `#ask-gateway` Slack channel.

  - 
**Platform-Specific Issues:** Use the dedicated Slack channel for the platform (e.g., `#shopify`).

## FAQs** ****❓**

The card number in the dashboard looks different from my customer's real card. Is this an error?

No, this is expected behavior. Apple Pay uses a secure token called a DPAN (Device Account Number) instead of the real card number, which is never exposed during the transaction.What are the specific settings for MADA Apple Pay for MENA users?

The configuration depends on the transaction location:

- 
**Outside Saudi Arabia:** Ensure the `countryCode` is not 'SA' and that "mada" is not included in `SupportedNetworks`.

- 
**Inside Saudi Arabia:** The `countryCode` must be 'SA' and `SupportedNetworks` must include "mada".

Can I have more than one active payment processing certificate?

No. While you can create more than one certificate in your Apple Pay MID account, only one can be active at any given time.
