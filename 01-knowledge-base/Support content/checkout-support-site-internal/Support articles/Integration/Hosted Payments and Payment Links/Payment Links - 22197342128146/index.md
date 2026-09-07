---
id: 22197342128146
section_id: 22188552840594
title: "Payment Links"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22197342128146-Payment-Links"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:35:55Z"
permission_group_id: 26838654181266
content_tag_ids: ["01H8EDHC0MTG4YFD7E4B42CE0V"]
label_names: ["global", "case_integration", "case_integration_issue_payment_links"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

Payment Links allow merchants to integrate with the Unified Payments API easily, enabling payment acceptance through various channels, such as email, social media, live chat, or text messages. Customers are directed to a Hosted Payments Page to complete the payment.

## Process Steps

**Setup Instructions**

To begin using Payment Links, merchants will need to email support@checkout.com and specify 

1. The client name &  entity name

2. If 3D Secure is required to be on by default and if attempt non-3DS is needed

3. If Capture is required to be on by default

4. [If using Payment Links], The terms and conditions URL

5. Precise whether it is a sandbox account or live account

6. Confirm the scheme & APM required

Merchants will need to be onboarded correctly via the ‘Merchant Hosted Pages Enablement’ Retool app. Please refer to the following instructions on how to do this: [How to enable HPP and Payment Link](https://checkout.atlassian.net/wiki/spaces/SE1/pages/5912102398/How+to+enable+HPP+and+PLink).

Once they are onboarded, the merchant can now begin sending payment links. For detailed (merchant-facing) instructions, refer to [Create a Payment Link](https://www.checkout.com/docs/payments/accept-payments/create-a-payment-link).**Access to Retool**

Ensure you have access to Retool by completing the following steps:

1. 
**Request Retool Access**: [Request Link](https://checkoutsupport.freshservice.com/support/catalog/items/566)

2. 
**Complete the Ticket**:

  1. 
**Environment**: Production

  2. 
**Application Name(s)**: Merchant Hosted Pages Enablement

  3. 
**Permission**: Viewer - you can use and interact with apps

**Usage**

1. 
**Creation and Distribution**: Merchants create a payment link and send it to customers via text, email, or chatbot for phone orders

2. 
**Features**:

  1. Full API Access

  2. Handle full PAN numbers and card details (for PCI SAQ-D compliant merchants)

  3. Merchants who are not PCI compliant should use Checkout.com’s frames and HPP solutions to avoid handling raw card details

## Glossaries and Definitions:

For **Key Terms and Definitions** on Integration Issues, please see ****[Integrations Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22198412339346-Integrations-Glossary-Introduction)  

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Integration Issues articles, please see ****[Integrations Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22198326164754-Integrations-Tools-Permissions)
