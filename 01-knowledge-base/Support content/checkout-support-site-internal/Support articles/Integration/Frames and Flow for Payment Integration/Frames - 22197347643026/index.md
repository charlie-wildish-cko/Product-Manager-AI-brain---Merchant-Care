---
id: 22197347643026
section_id: 22188537440658
title: "Frames"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22197347643026-Frames"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:37:31Z"
permission_group_id: 26838654181266
content_tag_ids: ["01H8EDHC0MTG4YFD7E4B42CE0V"]
label_names: ["global", "case_integration", "frames_and_flow_for_payment_integration", "frames"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

Frames are a customisable white-labelled payment form embedded into a merchant's website. They securely exchange sensitive card information for a secure token to perform transactions without directly handling full PAN numbers (SAQ A compliance). Merchants integrate Frames by adding Checkout.com scripts and main element tags to their checkout page, ensuring fast and secure integration.

Key features:

1. Expose card brand.

2. Localise with pre-set languages or custom options.

3. Automatically processes 3D Secure (3DS), managed by Checkout.com.  

 

## Process Steps

**Implementation Details**

**Merchant-Facing Documentation**: [Accept a Payment on Your Website with Frames](https://www.checkout.com/docs/payments/accept-payments/accept-a-payment-on-your-website-with-frames)

Frames SDK information can be found in the Checkout GitHub repository and the documentation outlining the installation, which can be found via the links below:

- [iOS](https://www.checkout.com/docs/developer-resources/sdks/frames-ios-sdk)

- [Android](https://www.checkout.com/docs/developer-resources/sdks/frames-android-sdk)

**Troubleshooting**

To troubleshoot issues merchants may be facing we need to gather the below information from the merchant:

1. The name of the account in the Dashboard

2. What version of the Frames SDK has the merchant implemented (e.g. iOS, Android etc) and the version number for the SDK itself

3. Description of the issue the merchant is facing along with the site URL where Frames is implemented

4. If this is an issue with a specific payment, then the payment/request IDs

5. If the issue has been reproduced by the merchant multiple times, then reproduction steps would be required

Depending on the issue the teammate will then need to investigate based on insights from Datadog, GitHub (to view the SDK code) or even reading code snippets the merchant sends.

The **#ask-frames-sdks** channel can be used for any integration-related queries on the Frames SDK.

## Glossaries and Definitions:

For **Key Terms and Definitions** on Integration Issues, please see ****[Integrations Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22198412339346-Integrations-Glossary-Introduction)  

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Integration Issues articles, please see ****[Integrations Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22198326164754-Integrations-Tools-Permissions)
