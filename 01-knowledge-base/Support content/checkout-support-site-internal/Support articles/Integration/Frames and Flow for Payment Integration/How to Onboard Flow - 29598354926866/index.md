---
id: 29598354926866
section_id: 22188537440658
title: "How to Onboard Flow"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/29598354926866-How-to-Onboard-Flow"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-02-16T15:10:11Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JCGQCYWP2Z76A49GXQY22K11", "01K5H06EKVK584VVAPGFDW40D9", "01K5H06JBENFXSF63E7H9CP112"]
label_names: ["case_integration_issue_flow", "flow", "onboarding_a_flow_merchant", "flow_troubleshooting_and_escalations"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

For onboarding to Flow, our advanced payment solution. It covers everything from API key configuration to enabling Flow and various Alternative Payment Methods (APMs).

## DESCRIBE THE ISSUE 💬

You need to enable the Flow payment solution for a merchant. The setup process requires correct configuration of API keys and the use of specific internal tools (Retool, CAT) to enable different payment methods. This guide provides a detailed walkthrough for anyone responsible for the setup, ensuring all configurations are done correctly to prevent integration or processing errors.

[Flow AI Assistant](https://docs.google.com/document/d/14j3WWhRfbD6rkPxXHQhvFWb5MKyFSaZXCIE6jrxIWdE/edit?tab=t.0) 🤖

 
 

## KEY TAKEAWAYS 🔑

- The primary tool for onboarding is the "Merchant Hosted Pages Enablement" application in Retool

- Correct API key scopes are crucial for setup: `payment-sessions` for the Secret Key and `payment-sessions:pay`, `vault-tokenization` for the Public Key

- PayPal enablement requires finding and entering the PayPal Merchant ID from CAT into Retool

- Other Alternative Payment Methods (APMs) can be enabled via simple toggles in the Retool application

- Onboarding for Sandbox and Production environments can be completed at any time without impacting current live payment processing

## RESOURCES 📍

| Tools | Case Examples | Related |
| --- | --- | --- |
| [Merchant Hosted Pages Enablement (Retool)](https://example.retool.com/apps) [CAT (Client Admin Tool)](https://example.com/cat-login) [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274) | [Zendesk Case:77234](https://checkout1360.zendesk.com/agent/tickets/77234) [Zendesk Case: 67456](https://checkout1360.zendesk.com/agent/tickets/67456) [Zendek Case: 64120](https://checkout1360.zendesk.com/agent/tickets/64120) | [Cloudflare Access Guide](https://example.com/cloudflare-guide) [Flow Migration Questions Doc](https://example.com/flow-migration-doc) |

## PROCESS FOR ONBOARDING TO FLOW 🖊️

**Step 1. Configure API Keys**

Before using the enablement tool, ensure the correct API keys have been created in the Dashboard with the necessary scopes:

- 
**Secret Key Scope:** `payment-sessions`

- 
**Public Key Scopes:** `payment-sessions:pay`, `vault-tokenization`

**Step 2. Onboard via Retool**

The "Merchant Hosted Pages Enablement" tool in Retool is used for the main onboarding process.

- 
**Access the Tool:** Connect via Cloudflare and navigate to the [Merchant Hosted Pages Enablement tool](https://example.retool.com/apps).

- 
**Set Environment:** Select the correct `Environment` (Sbox or Prod) and set the `Merchant platform` to `NAS`.

- 
**Find the Merchant:** Enter the `Entity ID` and click `Onboard/Update merchant`.

- 
**Onboard or Update:**

  - If you see a `merchant_not_onboarded` message, click the `Onboard this merchant` button.

  - If details are already present, click `Update this merchant`.

- 
**Configure Settings:** Complete the necessary fields under the **Merchant details & Payment methods** sections. You can reference the processing profile in CAT to confirm which payment methods should be enabled.
**💡**** Note:** The "Merchant processing settings," "Creditor information for SEPA," and "Branding and customisation" sections are not required for Flow and will be ignored.

**Step 3. Enable Specific Payment Methods**

**PayPal**

- 
**Find Merchant ID:** Log in to CAT and navigate to the PayPal processing profile to find the PayPal Merchant ID.

- 
**Add to Retool:** Copy this ID and paste it into the `PayPal Merchant ID` field in the Hosted Pages Enablement Tool. Click `Update/Onboard this merchant` to save.

**Other Alternative Payment Methods (APMs)**

- All other APMs can be enabled for Flow using the toggle buttons next to each payment method in the Hosted Pages Enablement Tool.

- Switch the toggle on for each required APM and click `Update/Onboard this merchant` to save the configuration.

## RESOLUTION ⚒️

- 
**Expected Result:** After following these steps, Flow will be successfully enabled for the selected environment (Sandbox or Production). The configured payment methods, including PayPal and any chosen APMs, will be active and ready for integration.

- 
**Remediation Steps:** To verify the setup, check the status in the "Merchant Hosted Pages Enablement" Retool app. It should show the account as onboarded with the correct payment methods enabled.

 

## ESCALATION** ⏫**

- For general questions about Flow, use the **#ask-flow** Slack channel.

- For issues related to migrating from Frames to Flow, consult the [Flow migration questions document](https://example.com/flow-migration-doc).

 
 

## FAQs** ****❓**

What is the main difference between Flow and Frames?

Frames is a solution that only handles the tokenization of card details. Flow is an advanced, all-in-one solution that manages the complete payment flow, including both tokenization and the payment request. Flow is also fully customizable, allowing you to match the look and feel of your website, which is not possible with Frames.Can an account be onboarded to Flow in production before it is ready to go live?

Yes, onboarding for both sandbox and production can be done at any time and will not affect current payment processing. 

It is recommended to enable both environments at the same time to prevent delays if you decide to start testing in production unexpectedly.
