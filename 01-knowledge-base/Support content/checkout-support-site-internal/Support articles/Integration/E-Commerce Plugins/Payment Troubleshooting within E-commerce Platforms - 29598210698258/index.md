---
id: 29598210698258
section_id: 22188523357458
title: "Payment Troubleshooting within E-commerce Platforms"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/29598210698258-Payment-Troubleshooting-within-E-commerce-Platforms"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-09-29T11:58:10Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JVM5R67ANQB2F922VYV5Z7VD", "01K5GZVEK1B94QWX6RFY35W9DM", "01K5GZW7TJYASYHRCHAXC203ZA", "01K5GZWCMAW9Q9WJXYY7KYP59X", "01K5GZWHE209642VAAW7F0DP7G", "01K5GZWNJRS1EM2K755PZFGKH3", "01K5GZWWRG88JJYYS7SBZ7TPGC"]
label_names: ["ecommerce_plugins", "ecommerce_plugins_troubleshooting", "payment_failed"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

Use this guide when payments are failing on a merchant's e-commerce store for a platform that Checkout.com directly integrates with, such as Shopify, Magento, or WooCommerce etc.

**Problem:** Payments on an e-commerce platform are being declined or are failing, and/or the order status is not being updated correctly on the site. This leads to lost sales and a poor customer experience.

**Solution:** This guide provides a step-by-step process to diagnose the root cause of payment failures by checking plugin versions, platform settings, and payment data.

## DESCRIBE THE ISSUE 💬

Merchants are experiencing issues with payments on their e-commerce store (e.g., Shopify, Magento, WooCommerce). Transactions may be failing, or the order status in the admin panel is not updating correctly after a payment attempt. This guide is for anyone troubleshooting these issues to determine if the problem lies with the e-commerce plugin configuration or a more general payment processing issue.

 

## KEY TAKEAWAYS 🔑

- The first step is to distinguish if the issue is caused by the e-commerce plugin or a general payment problem

- Check the plugin version in Datadog using the `Request.Metadata.udf5` parameter from a failed payment log

- Always compare the current plugin version against the latest version available on GitHub

- Incorrect API key configuration is a common issue; some platforms require that only one processing channel is selected for the key

- If a bug is found detailed information must be gathered before reporting it for escalation

## RESOURCES 📍

| Tools | Case Examples | Related |
| --- | --- | --- |
| [Datadog](https://app.datadoghq.com/) [GitHub](https://github.com/) Temporary Store Access | [Example 1](https://checkout1360.zendesk.com/agent/tickets/37404) [Example 2](https://checkout1360.zendesk.com/agent/tickets/10640) | [Connect to an e-commerce platform](https://example.com/docs/e-commerce) |

## PROCESS FOR TROUBLESHOOTING E-COMMERCE PAYMENT FAILURES 🖊️

This process helps identify whether an issue is caused by the e-commerce plugin or a general payment processing problem.
**Step 1. Initial Investigation**

- 
**Check Plugin Version in Datadog:**

  - Obtain a `Payment ID` for a failed transaction

  - In Datadog, search for the payment and view the gateway logs. The `Request.Metadata.udf5` parameter contains the e-commerce platform and plugin version (e.g., `Magento 2 | 2.2.8`)

  - Check this version against the latest version available on GitHub - an outdated plugin may contain bugs that a newer version has fixed

- 
**Verify API Key Configuration:**

  - Incorrect API key settings are a common cause of payment failures on e-commerce platforms

  - Check the specific documentation for your platform to confirm how processing channels should be configured for the API key

💡 For some platforms like Shopify only one processing channel should be selected
**Step 2. Reporting a Bug**

If you identify a bug, it is essential to gather comprehensive information before reporting it. Use the following checklist (example for Magento) as a template:

**Plugin Details:**

- Checkout.com plugin version installed

- Is it the standard (vanilla) version or has it been customized?

**Platform Environment:**

- E-commerce platform and version (e.g., Magento 2.4 Community)

- PHP version

- Is the bug in Sandbox or Production?

**Replication Details:**

- Can you provide sandbox/test environment access for replication?

- What exact steps did the customer perform to trigger the issue?

- Which payment method was used (Card, Apple Pay, Google Pay, Klarna, etc.)?

**Observed Behavior:**

- What is the expected behavior?

- What is the actual behavior observed?

- Are there any error messages or codes? (Include full text or screenshots).

**Logs & Consistency:**

- Can you provide system and exception logs from your e-commerce platform?

- Is the issue consistent or intermittent?

- Does it happen for all customers/payments or only in specific cases?

## RESOLUTION ⚒️

- 
**Expected Result:** By following these steps, you will identify the cause of the payment failure, whether it's an outdated plugin, a configuration error, or a platform bug. After applying the fix (e.g., updating the plugin, correcting API key settings), payments will process successfully, and order statuses will update correctly.

- 
**Remediation Steps:** After making a change, process a test payment on your store to confirm the issue is resolved. Check the order in your e-commerce admin panel to ensure the status is updated correctly. Review the new payment logs in Datadog to confirm there are no errors.

- 
**Rollback/Recovery:** If updating a plugin causes new issues, you can typically roll back to the previous version from a backup. Configuration changes, like API key settings, can be reverted in the Dashboard. Always backup your store before making significant changes like plugin updates.

 

## ESCALATION** ⏫**

If you cannot resolve the issue after initial troubleshooting, please escalate to the appropriate team via the dedicated Slack channel for your e-commerce platform:

- `#shopify`

- `#magento`

- `#woocommerce`

- `#sfcc`

 
 

## FAQs** ****❓**

Why is my order status not updating after a payment?

This is most often a webhook issue. Check the webhook logs in Datadog for the specific payment to see if the webhook notifications were successfully delivered to your server.How do I find which version of the Checkout.com plugin I'm using?

Search for a recent payment ID from your store in Datadog. The gateway logs will contain a `metadata.udf5` field, which shows the e-commerce platform and the plugin version number.Why are test payments failing on my Shopify store?

While there can be many reasons for this, one of the most common issues is with the API key configuration. For Shopify, the "Allow any processing channel" toggle on the API key must be disabled, and only one processing channel should be selected.
