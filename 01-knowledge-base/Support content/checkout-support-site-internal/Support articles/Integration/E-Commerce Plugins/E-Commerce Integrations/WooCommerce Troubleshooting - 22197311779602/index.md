---
id: 22197311779602
section_id: 22188499853714
title: "WooCommerce Troubleshooting"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22197311779602-WooCommerce-Troubleshooting"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-09-30T12:28:09Z"
permission_group_id: 26838654181266
content_tag_ids: ["01H8EDHC0MTG4YFD7E4B42CE0V"]
label_names: ["global", "ecommerce_plugins", "case_integration", "case_integration_issue_ecommerce_integration", "woocommerce"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**   

For troubleshooting common issues with the Checkout.com WooCommerce plugin. To help users and support agents diagnose and resolve problems related to plugin configuration, compatibility, and third-party conflicts.   

## DESCRIBE THE ISSUE 💬

The merchant has reported an issue with their WooCommerce store's payment functionality, which uses the Checkout.com plugin. The problem could be a transaction not processing correctly, an order status not updating, or a conflict with other installed plugins. 

## KEY TAKEAWAYS 🔑

- Gather all relevant information upfront: plugin version, payment IDs, store URL and replication steps

- The first step in any troubleshooting is a hygiene check of the merchant's environment and Checkout.com account settings

- Issues can be caused by the plugin itself, a Checkout.com internal product, or third-party conflicts within the merchant's environment

- Replicating the issue in both the merchant's staging environment and a clean test environment is crucial for identifying the root cause

- If the issue is due to a third-party module or the merchant's hosting environment, the resolution must be handled by the merchant's technical team

PROCESS FOR WOOCOMMERCE PLUGIN ISSUE RESOLUTION 🖊️ 

**Step 1. Perform a hygiene check of the merchant's configuration**               

- 
**Check compatibility**: Verify that the merchant's WooCommerce and PHP versions meet the minimum requirements for the Checkout.com plugin.

  - WooCommerce: Check the plugin documentation for the minimum supported version

  - PHP: Confirm the version is 7.4 or higher                                

- 
**Review plugin version**: Ensure the merchant is using the latest released version of the plugin.

- 
**Code integrity**: Check with the merchant to confirm they have not made local changes to the plugin code.

- 
**Account configuration**: Use the CAT dashboard or ABC admin hub to check the merchant's Checkout.com account settings, including API keys, webhook settings, APMs, and redirection settings.

**Step 2. Replicate the merchant's issue and investigate**

- 
**Gather details**: Request the merchant's staging environment credentials and detailed, step-by-step instructions to replicate the issue.

- 
**Replicate on merchant's staging environment**: Follow the steps provided by the merchant to see if the issue can be reproduced on their staging site.

- 
**Replicate on CKO's test environment**: Attempt to reproduce the issue on a clean, controlled Checkout.com test environment with the same plugin version and configuration.

**Step 3. Identify the impact of third-party modules**

- If the issue only occurs on the **merchant's environment**, it is likely caused by a third-party module (e.g., another plugin) or their hosting setup (e.g., AWS, Linux).

- Engage with the merchant's technical team to investigate these external factors as they are outside of Checkout.com's control.

## RESOLUTION ⚒️

**If the issue is a Checkout.com product problem**: The issue was successfully replicated on both the merchant's and Checkout.com's test environments. This indicates a defect with a Checkout.com product (e.g., Gateway, Vault, a specific APM). Report the bug to the relevant product team. A good practice is to test the issue in isolation using a tool like Postman to confirm it is not plugin-related.

**If the issue is a plugin problem**: The issue was replicated on both environments and isolated to a plugin defect. Record the issue in the bug archive and proceed with the remediation steps.

**If the issue is a merchant environment problem**: The issue was only replicated on the merchant's environment. The resolution is for the merchant to work with their technical team or hosting provider to resolve the third-party conflict.

## ESCALATION** ⏫**

- Escalate the case when:

  - The issue is confirmed to be a **bug with a Checkout.com product**

  - You cannot replicate the issue and require assistance from a senior technical resource

  - The merchant's technical team requires direct support from our product engineering team

- 
**Required information to include**:

  - Detailed replication steps

  - All information gathered in the initial investigation (plugin versions, payment IDs, etc.)

  - Screenshots or screen-recordings of the issue

  - A summary of the troubleshooting steps you have already taken

 FAQs** ****❓**               

What are the minimum system requirements for the plugin?

The plugin requires a minimum PHP version of 7.4 and a compatible version of WooCommerce. Please refer to the official documentation for the latest compatibility information.My order status is not updating. What should I do?

This can be caused by webhook issues. First, ensure the webhooks are correctly configured in your Checkout.com account. Then, check your system logs for any failed webhook deliveries.A transaction failed with an error. Where can I find more information?

Check the detailed error messages in the Checkout.com hub by searching for the Payment ID. These messages often provide specific reasons for the decline or failure.How can I tell if another plugin is causing the conflict?

The most effective method is to temporarily deactivate all other plugins except for WooCommerce and the Checkout.com plugin. If the issue is resolved, reactivate other plugins one by one to identify the culprit. This should be done on a staging environment to avoid impacting the live site.
RESOURCES ⭐️

| Related Articles |
| --- |
| - External merchant facing article: [WooCommerce](https://www.checkout.com/docs/payments/accept-payments/connect-to-an-ecommerce-platform/woocommerce)   - [Payment methods](https://checkout.atlassian.net/wiki/spaces/CHEC/pages/5083139008/WooCommerce+Overview#Payment-methods) |
