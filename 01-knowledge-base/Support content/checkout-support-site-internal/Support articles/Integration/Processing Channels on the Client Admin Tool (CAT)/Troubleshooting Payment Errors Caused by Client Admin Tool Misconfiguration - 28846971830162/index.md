---
id: 28846971830162
section_id: 22188504904594
title: "Troubleshooting Payment Errors Caused by Client Admin Tool Misconfiguration"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/28846971830162-Troubleshooting-Payment-Errors-Caused-by-Client-Admin-Tool-Misconfiguration"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-09-29T11:15:52Z"
permission_group_id: 26838654181266
content_tag_ids: ["01K2YZ5KJE86ZR8XY13DKPRSCT", "01K2YZ6M6DAR6SYE43GX5V7X9D", "01K2YZ71B1237QRXWTV9MWVZB9"]
label_names: ["currency_not_configured", "no_processor_configured_for_card_scheme"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article - **Use this article to figure out if a payment error is related to a Client Admin Tool (CAT) configuration issue

**Problem - **An error shown in Datadog, such as currency_not_configured points towards a misconfigured field in CAT

**Solution - **Identify the specific misconfiguration in CAT using Datadog logs and alter the settings to resolve the payment error

 

## DESCRIBE THE ISSUE 💬

The Client Admin Tool (CAT) is an interface used to configure client accounts. This includes setting up merchant sandbox accounts for testing and viewing the configuration details for live production accounts.

Occasionally, configuration issues within CAT can lead to payment processing errors. These problems often appear as `422` error messages in Datadog logs, such as `currency_not_configured`, `no_processor_configured_for_card_scheme` or `aft_processor_not_matched`.

This article outlines the process for identifying and resolving these errors by correcting the configuration in CAT.

## 

## KEY TAKEAWAYS 🔑

- Begin troubleshooting by examining the specific error message in Datadog logs to guide your investigation in CAT

- Before making any changes, gather all relevant IDs (e.g., `pc_`, `pr_`, `pp_`) to accurately trace the transaction's path

- Use the GWC Processor Admin tool to archive, not delete, old gateway processors to ensure payments route correctly

- Always confirm your fix by running a test transaction in the merchant's sandbox environment

## RESOURCES 📍

| Tools | Related |
| --- | --- |
| **Cloudflare Access**: Required to access CAT environments **Client Admin Tool (CAT)**: Access to the QA, Sandbox, and Production environments **Datadog**: For viewing payment logs and identifying error messages. **Retool**: Access to the ****[GWC Processor Admin](https://retoolsbox.mgmt.ckotech.co/apps/80d0829c-53a2-11ed-a526-d3c0a2a13d1c/routing/GWC%20Processor%20Admin) application for archiving processors. | [Create Gateway Processing Channel UI](https://checkout.atlassian.net/wiki/spaces/ATLAS/pages/1043890614/Key+settings) |

## PROCESS FOR TROUBLESHOOTING CAT ERRORS 🖊️

**Step 1. Identify the Root Cause in Datadog**

Start by viewing the payment response in the Datadog logs to find the error message (e.g., `currency_not_configured`) that points to a specific configuration issue in CAT.

Be mindful of the payment type. Legacy "Manual processors" might process standard payments correctly but can cause failures for specific transactions like Account Funding Transactions (AFTs).
**Step 2. Gather Key Information**

From the Datadog logs, collect the following IDs to understand the full transaction path:

- Processing Channel ID (`pc_...`)

- Gateway Processor ID (`pr_...`)

- Processing Profile ID (`pp_...`)

**Step 3. Investigate the Configuration in CAT**

- Use the IDs you collected to navigate to the correct **Processing Profile** in CAT.

- Check the configuration for errors:

  - Is the correct currency enabled on the profile?

  - Is the Merchant Category Code (MCC) correct?

**⚠️ Warning:** If you update the MCC on a processing profile, you must also update the corresponding gateway processor to reflect the new MCC.
**Step 4. Replicate the Issue in a Sandbox Environment**

If you review the merchant's production/sandbox setup and find no obvious errors, replicate their processor settings in a sandbox account to reproduce the issue. 

If your test works but the merchant's still fails, compare the sandbox configurations side-by-side to find the discrepancy.
**Step 5. Remediation Steps**

- 
**For a **`**currency_not_configured**`** error**:

  - Check the currency value being sent in the payment request in Datadog.

  - Navigate to the processing profile in CAT and ensure that currency is enabled.

- 
**For a **`**no_processor_configured_for_card_scheme**`** error**:

  - Confirm that a processor for the specific card scheme exists on the processing channel.

  - If one exists, ensure an authentication processor is connected to the gateway processor.

  - If no gateway processor exists, you will need to create a new processing profile for that card scheme and add it to the gateway and authentication processors.

**Step 6. Archive Unwanted Processors (If Necessary)**

If you need to add a new processing profile, you may need to archive an old or non-functioning gateway processor first.

- Open the **GWC Processor Admin** tool in Retool.

- Enter the **Processing Channel ID** (`pc_...`) and the **Gateway Processor ID** (`pr_...`).

- Select the **Archive** action and click **Submit**.

- Refresh the processing channel in CAT to confirm the old processor has been removed.

**⚠️Warning:** Always **archive** a processor instead of deleting it. Archiving is reversible, while deletion is permanent. Note that only gateway processors can be archived, not authentication processors.

## RESOLUTION ⚒️

**Check Problem is Resolved**

Once you have applied the fix, run a test transaction in the merchant's sandbox account to confirm that the issue is resolved.

💡If you created a new secret key in the merchant's sandbox account for testing, remember to delete it after you have confirmed the solution.
**Rollback/Recovery**

If you need to restore a processor, you can unarchive it by following these steps:

- Open the **GWC Processor Admin** tool in Retool.

- Enter the **Processing Channel ID** and the **Processor ID**.

- Select the **Unarchive** action and click **Submit**.

- Refresh the CAT processing channel view to confirm the processor has been restored.

## ESCALATION** ⏫**

If you have followed the steps in this guide and are still unable to resolve the configuration error, please escalate the issue to the **#ask-merchantadmintools** Slack channel for further assistance.

## FAQs** ****❓**

Why do I need to archive an old processor before adding a new one?

Even if a new, working processor is added to the processing channel, payments may still be routed through the old, non-working processor if it is ranked higher in the system. It is best practice to archive the incorrect processor to ensure all payments are routed correctly.
