---
id: 29598059294354
section_id: 22188546107666
title: "Google Pay Setup"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/29598059294354-Google-Pay-Setup"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-09-29T09:01:38Z"
permission_group_id: 26838654181266
content_tag_ids: ["01K5GZBB1WTESD7J7JK1VGJ33V", "01K5GZHJQ14D5W6BRXEKQ9JK89", "01K5GZHSVCNH8FVEGYA03E9TNR"]
label_names: ["google_pay", "apple_pay_and_google_pay_integration", "google_pay_flow", "google_pay_setup", "google_pay_api_only", "how_to_set_up_google_pay"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

This document provides instructions for setting up and integrating Google Pay, a digital wallet service that allows for secure payments.

## DESCRIBE THE ISSUE 💬

The process of setting up Google Pay involves choosing an integration method (API Only or Flow), registering details with Google, and configuring the setup using specific tools. This guide is for anyone responsible for the technical setup and configuration of Google Pay.

 

## KEY TAKEAWAYS 🔑

- There are two primary integration methods: API Only (direct integration) and Flow (simplified web integration)

- Registering the merchants profile and domain in the Google Pay & Wallet Console to get a merchant ID is a required first step for both methods

- The API Only method requires merchants to handle token decryption on their server

- The Flow method simplifies setup by using the "Merchant Hosted Pages Enablement" tool in Retool

- Domain verification in the Google Business Console is mandatory for both integration types

## RESOURCES 📍

| Tools | Case Examples | Related |
| --- | --- | --- |
| [Google Pay & Wallet Console](https://pay.google.com/business/console) [Merchant Hosted Pages Enablement (Retool)](https://example.retool.com/apps) | [Zendesk Ticket: 33467](https://checkout1360.zendesk.com/agent/tickets/33467) | [Google Pay Documentation](https://developers.google.com/pay/api/web/overview) |

## PROCESS FOR SETTING UP GOOGLE PAY 🖊️

This guide outlines two distinct methods for setting up Google Pay. Choose the method that best suits the merchant's technical resources and customization needs.
**Method 1: API Only (Direct Integration)**

This method offers maximum control and customization and is best for those with specific UI/UX requirements who can manage server-side decryption.

**Option A: Using a Checkout.com Token**

1. 
**Google Pay Setup:** Register your profile and domain in the [Google Pay & Wallet Console](https://pay.google.com/business/console) to obtain your Google Pay merchant ID.

2. 
**Frontend Implementation:** Display the Google Pay button on your website. When a payment is initiated, receive the encrypted payment token from Google and send it to your server.

3. 
**Backend Decryption:** On your server, send the payment token to the `/tokens` endpoint. This will convert it into a CKO card token (prefixed with `tok_`).

4. 
**CKO API Call:** Submit a payment request to the CKO API using the `tok_` card token generated in the previous step.

**Option B: Using a Pre-decrypted Token**

1. 
**Google Pay Setup:** Register your profile and domain in the [Google Pay & Wallet Console](https://pay.google.com/business/console) to obtain your Google Pay merchant ID.

2. 
**Frontend Implementation:** Display the Google Pay button. When a payment is initiated, receive the encrypted payment token and send it to your server.

3. 
**Backend Decryption:** On your server, use your private key to decrypt the payload from Google. Extract the raw token details (DPAN, expiry, ECI, cryptogram).

4. 
**CKO API Call:** Submit a payment request to the CKO API using the `network_token` source, populated with the decrypted details.

**Method 2: Web Integration (Flow)**

This approach requires significantly less development effort and is ideal for a quick and easy setup.

1. 
**Flow Integration:** Complete the standard Flow integration setup first.

2. 
**Configuration:** In the Retool ["Merchant Hosted Pages Enablement" tool](https://example.retool.com/apps), onboard Google Pay by entering your Google Pay merchant ID.

3. 
**Verify Domain:** Ensure you have verified your domain in your Google Business Console. During this process, the integration type should be set to "Gateway".

4. 
**Confirm Onboarding:** Process a test transaction to confirm that Google Pay is working correctly through the Flow integration.

## RESOLUTION ⚒️

- 
**Expected Result:** Google Pay will be successfully integrated and available as a payment option. Customers will be able to complete purchases using their Google Pay wallet, providing a fast and secure checkout experience.

- 
**Remediation Steps:** To verify the setup is correct, process a test transaction using Google Pay in a testing environment. The transaction should appear successfully in the dashboard.

- 
**Rollback/Recovery:** If issues arise, review the configuration steps, ensuring the Google Pay Merchant ID is correct and the domain is verified. The integration can be disabled in payment settings if needed.

 

## FAQs** ****❓**

What is the difference between the API Only and Flow integration methods?

The API Only method gives you full control over the user experience but requires you to handle token decryption. The Flow method is a simplified integration where Checkout.com handles most of the complexity, including token decryption.What is the Google Pay Business Console used for?

the Google Pay Business Console is used for verifying a domain, which is a required step for both API Only and Flow integrations. The integration type should be set to "Gateway".
