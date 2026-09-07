---
id: 22197296034066
section_id: 22188499853714
title: "Magento Troubleshooting"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22197296034066-Magento-Troubleshooting"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-04T07:02:29Z"
permission_group_id: 26838654181266
content_tag_ids: ["01H8EDHC0MTG4YFD7E4B42CE0V"]
label_names: ["global", "ecommerce_plugins", "magento", "case_integration", "case_integration_issue_ecommerce_integration", "plugin", "ecommerce", "integration"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

For troubleshooting common issues related to the Checkout.com Magento plugin.

Slack channel: _#magento_

## DESCRIBE THE ISSUE 💬

A merchant using the **Checkout.com Magento plugin** is reporting a problem with their payment processing. The issue could be related to an older plugin version, configuration errors or a specific transaction. 

 

## KEY TAKEAWAYS 🔑

- Always check the merchant's current Magento plugin version against the latest version on GitHub

- Gather specific details like Payment ID, Request ID and store URLs for efficient troubleshooting

- Use Datadog logs to find the Magento and plugin versions if a Payment ID is available

- Document replication steps, screenshots or screen recordings to provide a clear context for the issue

## PROCESS FOR MAGENTO PLUGIN TROUBLESHOOTING 🖊️

**Step 1. Gather Initial Information**

- Begin by requesting the following information from the merchant. This data is essential for diagnosing the issue and should be a standard part of any Magento-related inquiry.

  - 
**Checkout for Magento plugin version:** Ask the merchant which version they are currently using- Plugin versions can be verified against the [GitHub repository](https://github.com/checkout/checkout-magento2-plugin/releases).

  - 
**Payment ID/Request ID:** If the issue is transactional, obtain a Payment ID or Request ID - this allows you to check logs for specific errors.

  - 
**Store URL:** Get the URLs for both the Sandbox and Production environments to replicate the issue.

  - 
**Replication steps:** Request a detailed, step-by-step account of how the issue occurred (e.g., "add Item X to cart, proceed to checkout, and the payment fails when using an American Express card").

  - 
**Screen-recording/screenshots:** Ask the merchant for visual evidence of the problem, especially if you are unable to replicate it.

**Step 2. Utilize Internal Tools**

- Once you have the Payment ID, you can use **Datadog** to find the Magento and plugin versions in the logs- this can confirm the information provided by the merchant or provide it if they don't have it.

**Step 3. Check Configurations **

- Check the public-facing [merchant documentation](https://github.com/checkout/checkout-magento2-plugin#documentation) to see if the merchant may be missing a key configuration step.

## RESOLUTION ⚒️

Following these steps should provide enough information to either identify the problem or prepare the case for escalation.

- 
**Remediation Steps:** If the issue is caused by an outdated plugin version, advise the merchant to update to the latest version. If it's a configuration issue, guide them through the correct settings as outlined in the merchant documentation.

- 
**Check for resolution:** Confirm with the merchant that the problem is resolved after they follow the recommended steps.

- 
**Rollback/Recovery:** In the case of a failed update or a new issue appearing, advise the merchant to revert to their previous plugin version and provide the collected information for a more in-depth investigation.

## ESCALATION** ⏫**

- Examples of situations requiring escalation:

  - The merchant is on the latest plugin version and is still experiencing the issue

  - The issue is complex or cannot be resolved with the standard troubleshooting steps

  - The problem is affecting multiple transactions or a large number of customers

- Required information to include:

  - All the information you collected in the initial steps, such as the Magento and plugin versions, Payment/Request IDs, store URLs, and detailed replication steps.

- Instructions for the agent working the case:

  - Stay on the case and monitor for updates. Keep the merchant informed of the progress and notify them once the engineering team provides a resolution or asks for additional information.

## RESOURCES ⭐️

| Related Articles |
| --- |
| **Internal Articles**   - [Magento 2 Troubleshooting Tips](https://checkout.atlassian.net/wiki/spaces/EPKB/pages/1679819983/Magento+2+General+tips+for+troubleshooting)  - [Magento - Confluence](https://checkout.atlassian.net/wiki/spaces/SE1/pages/6723862583/Magento) |
| **Merchant Facing Articles**   - [Checkout.com Docs](https://www.checkout.com/docs/payments/accept-payments/connect-to-an-ecommerce-platform/magento-2)  - [Adobe Marketplace](https://commercemarketplace.adobe.com/checkoutcom-magento2.html)  - [GitHub Repository](https://github.com/checkout/checkout-magento2-plugin) |

## FAQs** ****❓**

What is the most common reason for Magento plugin issues?

Often, issues are related to outdated plugin versions or incorrect configuration settings after an update or new installation.Can I troubleshoot without a Payment ID?

Yes, but a Payment ID significantly speeds up the process by allowing you to directly check transactional logs in Datadog. Without it, you will need to rely more on replication steps and general site diagnostics.Where can I find the latest Magento plugin version?

The latest version is available on the official Checkout.com GitHub repository for the Magento 2 plugin.
