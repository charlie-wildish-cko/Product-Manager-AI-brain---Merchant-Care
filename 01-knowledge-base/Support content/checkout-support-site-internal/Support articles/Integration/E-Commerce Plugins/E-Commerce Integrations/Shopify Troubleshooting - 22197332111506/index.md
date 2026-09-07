---
id: 22197332111506
section_id: 22188499853714
title: "Shopify Troubleshooting"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22197332111506-Shopify-Troubleshooting"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-09-29T18:56:19Z"
permission_group_id: 26838654181266
content_tag_ids: ["01H8EDHC0MTG4YFD7E4B42CE0V"]
label_names: ["global", "ecommerce_plugins", "case_integration", "case_integration_issue_ecommerce_integration", "shopify"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

When a merchant is experiencing issues with their Shopify integration. 

## DESCRIBE THE ISSUE 💬

The merchant, who uses Checkout.com for payments, is experiencing a problem with their Shopify store integration. The merchant may see failed transactions, incorrect order statuses or other unexpected behavior. 

## KEY TAKEAWAYS 🔑

- Verify the merchant is using the most recent version of the Checkout.com Shopify plugin

- Check for common configuration issues within the Checkout.com merchant account and the Shopify admin panel

- Ensure webhooks are properly configured for order updates and fulfillment

- If initial checks are not enough, request temporary staff access to the merchant's Shopify store for in-depth troubleshooting

## RESOURCES 📍

| Tools | Related |
| --- | --- |
| Client Admin Tool CAT | - [Shopify Onsite](https://www.checkout.com/docs/payments/accept-payments/connect-to-an-ecommerce-platform/shopify)  - [Shopify Offsite (Shopify Payments App)](https://www.checkout.com/docs/payments/accept-payments/connect-to-an-ecommerce-platform/shopify-payments-app) |

## PROCESS FOR SHOPIFY INTEGRATION TROUBLESHOOTING 🖊️

### Step 1. Verify Plugin and Integration Setup

- Confirm the merchant is using the correct Checkout.com secret keys

- If using the Checkout.com Offsite App, check if the account is onboarded for HPP/PL

- Check Client Admin Tool for configuration issues, such as:

  -  Whether the Full Card API is enabled

  - If relevant currencies, schemes, or APMs are active

-  For Onsite integration ensure the secret key has `sessions:browser` scope enabled

### Step 2. Examine Merchant's Shopify Settings

- Verify the merchant has not enabled "Test Mode" in the Checkout Offsite App settings

- Confirm the merchant is using the correct test cards for their account's platform settings

- Check the "Billing Descriptor" and "Billing Descriptor City" values in the Checkout Offsite App settings for forbidden characters or character limit issues

### Step 3. Check Webhook Configuration

- Ensure the merchant has set up their webhook notifications as these are crucial for order updates

### Step 4. Request Temporary Staff Access for Deeper Investigation

- If the issue persists, request temporary staff access to the merchant's Shopify store. This allows for a more thorough check of their settings.

  - Instruct the merchant to log into their Shopify admin panel

  - Navigate to **Settings > Users and Permissions**

  - Click **Add Staff\**

- Ask them to enter `tech.support@checkout.com` as the email, and check the `Manage Settings` box

- They must also scroll down and check the `Checkout.com Payments App` box to grant access to adjust the app's settings

## RESOLUTION ⚒️

- Upon following the troubleshooting steps, the merchant should be able to resolve common integration issues. The problem is resolved when transactions are processing correctly and order statuses are updating as expected.

- **Remediation Steps:** Correct any misconfigurations found during the process, such as disabling test mode, updating secret keys, or reconfiguring webhooks.

- **Rollback/Recovery:** If a change causes an unexpected issue, simply revert the setting back to its original state.

## ESCALATION** ⏫**

- Escalate the case to the Partner Engineering or Tech Support team if:

  - The issue persists after completing all troubleshooting steps

  - The problem appears to be a bug or a complex technical issue not covered by this guide

  - The merchant's issue is related to the Checkout.com API itself, rather than the Shopify plugin

- Required information to include:

  - A detailed description of the issue

  - All steps taken so far, including the results of each check (e.g., "Confirmed secret keys are correct," "Test mode was disabled")

  - Merchant's account details and a link to the case

💡 For Shopify integration questions join the**#shopify** Slack channel

 

## FAQs** ****❓**

What is the difference between Shopify Onsite and Offsite?

Shopify Onsite allows customers to complete their payment directly on the Shopify store using Checkout.com's integration. Shopify Offsite redirects the customer to a secure hosted payment page (HPP) to complete their payment.How do I check for forbidden characters in the Billing Descriptor?

Check the merchant's Billing Descriptor in the Checkout Offsite App settings. Ensure it only contains standard alphanumeric characters and is within the specified character limit.Why are webhooks important for the Shopify integration?

Webhooks are automated messages sent from Shopify to Checkout.com. They are essential for communicating real-time updates on orders and payment statuses, ensuring data consistency between the two platforms.
