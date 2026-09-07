---
id: 22197332717586
section_id: 22188552840594
title: "Setting up Hosted Payments Pages"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22197332717586-Setting-up-Hosted-Payments-Pages"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:34:10Z"
permission_group_id: 26838654181266
content_tag_ids: ["01H8EDHC0MTG4YFD7E4B42CE0V"]
label_names: ["global", "case_integration", "case_integration_issue_hosted_payment_page"]
user_segment_ids: [11003606966930]
archive: false
---

## Process Steps

Setup Instructions

To set up Hosted Payments Pages, unmanaged merchants will need to email [support@checkout.com](mailto:support@checkout.com) and specify their payment capture and 3D Secure settings during integration. 

Merchants will need to be onboarded correctly via the ‘Merchant Hosted Pages Enablement’ Retool app. Merchant Care teammates will need to perform this step for **Tier 4 merchants only**. Please refer to the following instructions on how to do this: [How to enable HPP and Payment Link](https://checkout.atlassian.net/wiki/spaces/SE1/pages/5912102398/How+to+enable+HPP+and+PLink).

Once they are onboarded, the merchant can now begin sending payment links. For detailed (merchant-facing) instructions, refer to [Create a Payment Link](https://www.checkout.com/docs/payments/accept-payments/create-a-payment-link).**Access to Retool**

Ensure you have access to Retool by completing the following steps:

1. 
**Request Retool Access**: [Request Link](https://checkoutsupport.freshservice.com/support/catalog/items/566)

2. 
**Complete the Ticket**:

  - 
**Environment**: Production

  - 
**Application Name(s)**: Merchant Hosted Pages Enablement

  - 
**Permission**: Viewer - you can use and interact with apps

 **Usage**

1. 
**Redirection Solution**: Merchants add order information in the hosted payments request and redirect users to the URL provided in the response. Users will see a preconfigured checkout page to complete the transaction.

2. 
**Features**:

  1. Simple and fast setup with API code.

  2. Fixed layout, no branding.

  3. Automatically processes 3DS, managed by Checkout.com.

  4. Specific categories (e.g., 6012) may require additional card details

## Glossaries and Definitions:

For **Key Terms and Definitions** on Integration Issues, please see ****[Integrations Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22198412339346-Integrations-Glossary-Introduction)  

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Integration Issues articles, please see ****[Integrations Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22198326164754-Integrations-Tools-Permissions)
