---
id: 22435560098706
section_id: 22188537440658
title: "How to Onboard a Flow Merchant"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22435560098706-How-to-Onboard-a-Flow-Merchant"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-02-16T15:09:54Z"
permission_group_id: 26838654181266
content_tag_ids: ["01H8EDHC0MTG4YFD7E4B42CE0V"]
label_names: ["global", "case_integration", "case_integration_issue_flow", "onboarding_a_flow_merchant"]
user_segment_ids: [11003606966930]
archive: false
---

**Use this article when**

You need to onboard a merchant to Flow, this process is essential for enabling a merchant to accept payments through our hosted pages.

## PROCESS TO ONBOARD A FLOW MERCHANT 🖊️

[Flow AI Assistant](https://docs.google.com/document/d/14j3WWhRfbD6rkPxXHQhvFWb5MKyFSaZXCIE6jrxIWdE/edit?tab=t.0) 🤖

### Step 1. Access the Enablement Tool

Begin by navigating to the [Merchant Hosted Pages Enablement retool](https://retoolprod.mgmt.ckotech.co/apps/f67192a4-a90a-11ec-841c-938543b18be9/launchpad/Merchant%20Hosted%20Pages%20Enablement) application.

### Step 2. Configure the Environment

- Set the environment to Prod

- Set the merchant platform to NAS

- Enter the entity ID for the merchant you are onboarding

### Step 3. Initiate the Onboarding Check

- Click the Onboard/Update merchant button

✅ Success: If you see a `merchant_not_onboarded` message, proceed to the next step.

⚠️ Warning: If you see a `Merchant Found` message, the merchant is already onboarded. You do not need to continue with this process.

### Step 4. Complete Merchant Details

- Fill in the required information under the Merchant details & Payment methods section.

- The sections for Merchant processing settings, Creditor information for SEPA, and Branding and customisation are not required for Flow and can be ignored.

### Step 5. Enable Payment Methods

Before enabling any card schemes or Alternative Payment Methods (APMs) in this tool, ensure they have already been enabled on the merchant's account.

- PayPal: You must provide the PayPal Merchant ID. This ID should match the value found in CAT.

- Google Pay: You must provide the Google Pay Merchant ID as given by the requester.

### Step 6. Finalize Onboarding

Once all the necessary information is entered, click the Onboard this merchant button at the bottom of the page to complete the process.

Related Confluence article: [PayPal on NAS: How to onboard a merchant](https://checkout.atlassian.net/wiki/x/doCSLAE)
