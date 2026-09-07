---
id: 22197332805778
section_id: 22188552840594
title: "Setting Up Hosted Payments Pages and Payment Links"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22197332805778-Setting-Up-Hosted-Payments-Pages-and-Payment-Links"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T18:06:23Z"
permission_group_id: 26838654181266
content_tag_ids: ["01H8EDHC0MTG4YFD7E4B42CE0V"]
label_names: ["global", "case_integration", "case_integration_issue_hosted_payment_page", "case_integration_issue_payment_links", "supported_payment_methods"]
user_segment_ids: [11003606966930]
archive: false
---

**Use this article when**

Assisting a merchant to set up a Hosted Payments Pages (HPP) and Payment Links INTRODUCTION TO HPP & PAYMENT LINKS 💬

Hosted Payments Pages (HPP) and Payment Links are simple-to-use solutions that enable merchants to accept payments easily through various channels such as email, social media or text messages.   
These solutions redirect customers to a pre-configured checkout page for payment.  Features include:

- Full API Access

- Process full PAN and card details (for PCI SAQ-D compliant merchants)

- Non-PCI compliant merchants should use Checkout.com’s frames and HPP to avoid handling raw card data

TOOLING & RESOURCES 📍 

| Tooling | Related Content |
| --- | --- |
| **Retool Access**   - Request access using this [Link](https://checkoutsupport.freshservice.com/support/catalog/items/566)   - Environment: Production  - Application Name(s): Merchant Hosted Pages Enablement  - Permission: Viewer | [Hosted Payment Pages Introduction](https://checkoutint.zendesk.com/hc/en-us/articles/28595170747154) Merchant-facing articles   -  [Create a Payment Link](https://www.checkout.com/docs/payments/accept-payments/create-a-payment-link)   - [Accept a payment on a hosted payment page](https://www.checkout.com/docs/payments/accept-payments/accept-a-payment-on-a-hosted-page) |

PROCESS TO SET UP HPP & PAYMENT LINKS 🖊️

**Setup and Onboarding Steps**

To begin using HPP or Payment Links, merchants must provide the following details:

- Client and entity name

- Confirmation of whether 3D Secure and non-3D Secure attempts are required by default

- Confirmation of whether Capture is required by default

- The terms and conditions URL (if using Payment Links)

- Whether the setup is for a sandbox or live account

- The required schemes and APMs (Alternative Payment Methods)

**Merchant Onboarding**

Merchants must be onboarded correctly using the ['Merchant Hosted Pages Enablement' Retool app](https://retoolprod.mgmt.ckotech.co/apps/f67192a4-a90a-11ec-841c-938543b18be9/launchpad/Merchant%20Hosted%20Pages%20Enablement).   
For Tier 4 merchants, a Merchant Care team member will perform this step. 

- Onboard the client on CAT if not already done - How?

- Identify the Entity ID(s) you want to enable HPP/PLink for (enablement is at the entity level)

- Access the “Merchant Hosted Pages Enablement” app via the provided Retool link

- Select the environment (Sbox or Prod), merchant platform (NAS), and enter the Entity ID

- 
If the merchant isn’t onboarded, click “Onboard this merchant” and complete the onboarding form

**Merchant Details****Display Name**: This is the name that would be displayed to the cardholder on the payment page**Merchant Processing Settings 3D Secure**

- 3D secure enabled: As per client requirement

- Attempt non-3D secure: As per client requirement

**Capture**

- Capture: Default is true (amend as per client requirement)

- Capture on time: Default is 0

- Payment Link max amount: Default is 100,000

**Payment methods**

- Enable as per client requirement  
 
**Supported Payment Methods**  
Checkout.com offers a variety of payment methods for Hosted Payments and Payment Links. The available options may vary depending on the [region](https://checkout.atlassian.net/wiki/spaces/APM/pages/5137072925/APM+Live+Portfolio), see the [create a payment link page](https://www.checkout.com/docs/payments/accept-payments/create-a-payment-link) for a list of supported payment methods.💡 If a merchant would like to omit any payment method button from the Hosted Payment Page, they can pass the parameters listed [here](https://api-reference.checkout.com/#operation/createAHostedPaymentsSession).  
  
**Branding and customisation**

- Terms and conditions URL: Provided by merchant for production, not required in sandbox

- Show Checkout.com logo in footer: Default is enabled (amend as per client requirement)

Submit the form and wait for confirmation. If onboarding fails, review and correct the form inputs  
 RESOLUTION 🛠️Once the onboarding is complete, merchants can begin sending payment links or redirecting customers to hosted payment pages. For detailed, merchant-facing instructions, see the [Create a Payment Link](https://www.checkout.com/docs/payments/accept-payments/create-a-payment-link) guide.
