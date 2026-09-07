---
id: 22435576382482
section_id: 22435335461522
title: "CAID Registration Requirement - Schemes and Third Parties"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22435576382482-CAID-Registration-Requirement-Schemes-and-Third-Parties"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-23T11:21:24Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JBHFK1FTRFHHXXN4PTQS8A0A"]
label_names: ["global", "case_request_for_documentation", "caid_registration_requirements_in_regards_to_schemes_and_third_parties", "case_rfd_issue_scheme_merchant_ids"]
user_segment_ids: [11003606966930]
archive: false
---

**Use this article **

To understand the Card Acceptor ID (CAID) generation and registration processes for merchants using specific services provided by various payment Schemes and Third Parties.

## INTRODUCTION TO CAID 💬

 Card Acceptor ID (CAID) is a unique identifier associated with a merchant and is used in various payment processing systems. Key points about CAID:

- **Purpose**: CAID is used to identify merchants in payment processing systems. It is crucial for schemes like Visa and MasterCard to process transactions and manage merchant profiles 

- **Generation**: CAID can be generated manually or automatically, depending on the system setup. For example, in some systems, CAID is auto-generated based on business settings, such as the entity ID and merchant category code (MCC) 

- **Usage**: CAID is used in various configurations and setups, such as MoR (Merchant of Record) and Marketplace setups, where it remains consistent across different processing profiles 

- **Integration**: CAID is integrated into various systems and tools, such as Visa Platform, Client Admin Tool, and Looker, to manage and extract merchant information 

- **Challenges**: There are challenges in managing CAID, such as ensuring its availability across different processing channels and avoiding false positives or negatives in transaction processing 

Overall, CAID is an essential component in the payment processing ecosystem, providing a standardized way to identify and manage merchant information across different platforms and systems.PROCESS 🖊️

### 🔒 3D Authentication via MasterConnect (Mastercard)

- 
**Scheme/Third Party:** MasterConnect via **MasterCard**

- 
**Usage:** A business-to-business (B2B) platform from Mastercard used by banks, issuers, and fintech companies to integrate Mastercard’s digital services, including 3DS merchant registration, fraud prevention, and digital payments.

- 
 
**CAID Generation:** The Mastercard CAID is populated under the Processing Profile and linked under both the Gateway Processing Channel and the Authentication Processing Channel.

- 
**CAID Registration Process:**

  - The merchant’s CAID along with the merchant Acceptor Name is used to register for 3D manually by the Merchant Configuration Team on the MasterConnect Portal.

  - The Config team logs in to the [MasterConnect Portal](https://www.mastercardconnect.com/-/sign-in) using the MasterConnect Credentials.

  - 
 
_Inquiry Contact:_ The Merchant Configuration team should be contacted for any inquiries.

### 💳 Card on File via Account Updater (Mastercard)

- 
**Scheme/Third Party:** Account Updater (RTAU)

- 
**Usage:** A service that automatically updates stored payment card information (e.g., due to expiration or reissue) to ensure recurring payments and stored card-on-file transactions process without interruption.

- 
 
**CAID Generation:** The Mastercard CAID is populated under the Processing Profile and linked under both the Gateway Processing Channel and the Authentication Processing Channel.

- 
**CAID Registration/Enablement:**

  - 
 
**Pricing:** The Config team sets the Account Updater Pricing under the VAS pricing Profile under the client entity on CAT.

  - 
 
**Enablement:** The RTAU (Real Time Account Updater) is configured under the client > Services > Real Time Account Updater.

### ⚡️ Rapid Dispute Resolution (Visa)

- 
**Scheme/Third Party:** Visa **Verifi**

- 
**Usage:** Verifi, a part of Visa, specializes in chargeback prevention, dispute management, and risk mitigation. It works with issuing banks to resolve issues using systems like Rapid Dispute Resolution to prevent disputes from escalating into full chargebacks.

- 
 
**CAID Registration Process:** Refer to [Enable/Disable Rapid Dispute Resolution (RDR)](https://checkout.atlassian.net/wiki/spaces/MC/pages/6269698151/Enable+Disable+Rapid+Dispute+Resolution+RDR) for more information.
