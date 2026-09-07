---
id: 27600343939858
section_id: 22188537440658
title: "Flow FAQs"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/27600343939858-Flow-FAQs"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-12-29T17:05:32Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JCGQCYWP2Z76A49GXQY22K11"]
label_names: ["flow", "faqs"]
user_segment_ids: [11003606966930]
archive: false
---

**Use this article when:**

You need answers for frequently asked questions about Flow

 

## General Flow FAQs ❓

 What are the minimum SDK requirements for integration? 

To integrate Flow for Mobile, you will need the following minimum versions:

- 
**Android SDK**: Minimum SDK 21.

- 
**iOS SDK**: Minimum iOS 15, Xcode 16, and Swift 6.

 What is the file size of the Flow for Mobile SDKs?

Based on the SDK v1-Beta released in January 2025, the sizes are:

- 
**Flow for Mobile iOS SDK**: 1.6 MB.

- 
**Flow for Mobile Android SDK**: 4.1 MB.

 How do you enable your merchant to use Flow and specific payment methods?

You should use the Hosted Pages Enablement retool application. This tool allows you to enable Flow and specific payment methods for a merchant, using their processing profile in CAT as a guide.

 What API keys and scopes do you need to create in the Dashboard for Flow?

You need to create a Secret Key with the `payment-sessions` scope and a Public Key with the `payment-sessions:pay` and `vault-tokenization` scopes.

 Which merchant details are ignored when configuring Flow for Payment Components?

When using the enablement tool, the Merchant processing settings, Creditor information for SEPA, and Branding and customisation sections are not required and will be ignored.

 Can your customers save their card details for future use within the Flow component?

While storing cards to the vault works with Flow, the option for a customer to save their card directly when the component is rendered is not yet available (expected Q3). Currently, you must ask the user to save their card before the Flow component is loaded.

## 

## iOS 🍎

 Is the Apple Pay onboarding process different for the iOS SDK compared to the web?

Yes, the process is different.

- 
**Web**: Apple Pay onboarding is managed through APMe (Apple Pay Mass Enablement).

- 
**Mobile**: For the iOS SDK, merchants are required to create their own payment processing certificates.

 How do you handle Apple Pay onboarding for Flow?

You need to verify your domain using our specific domain verification file. You can choose to onboard yourself using the provided guides, use the `#applepay-onboarding` Slack channel, or use the enroll a domain service API.

 How do you verify that a merchant's domain is correctly set up for Apple Pay via Slack?

Check that the domain verification file is available by navigating to the domain plus the `.well-known` path. The file should be available at `/.well-known/apple-developer-merchantid-domain-association`.

 Are there specific browser or security requirements for Apple Pay?

Yes, Apple Pay will not function on third-party browsers such as Chrome, and your domain must use the secure https protocol rather than http.

## 

## Android Integration 🤖

 What is required from you to set up Google Pay for Flow?

You must share your Google merchant ID with us so it can be added to the Hosted Pages Tool. Additionally, you are required to verify your domain within your Google business console.

## 

## PayPal 💳

 How do you find the correct PayPal Merchant ID for onboarding?

You can find the PayPal Merchant ID within the merchant's PayPal processing profile in CAT. This value must match the one provided in the Hosted Pages Tool.

 How do you confirm a PayPal sandbox email address when it is created via Integrated Signup?

Since sandbox emails are not real, you must link the test account to your PayPal Developer account under 'Testing Tools'. Trigger the confirmation email from the sandbox site and locate the link within the 'Notifications' menu of your PayPal Developer Dashboard.

## 

## Troubleshooting 🛠️

 What should you do if you encounter the Google Pay error OR_BIBED_11?

This error typically indicates that the merchant has not completed registration in the Google Pay console. Ensure the domain is verified and the Google Merchant ID is correctly added to the Hosted Enablement tool.

 How do you resolve the Apple Pay merchant_not_enrolled error?

This error occurs if the domain has not been enrolled for APME. Refer to the enrollment steps via Slack or API to resolve this.

 How does Flow handle Alternative Payment Methods (APMs) that require a payment context?

Flow manages this automatically by creating the payment context in the background. This means you no longer have to manually listen for status updates before updating the frontend.
