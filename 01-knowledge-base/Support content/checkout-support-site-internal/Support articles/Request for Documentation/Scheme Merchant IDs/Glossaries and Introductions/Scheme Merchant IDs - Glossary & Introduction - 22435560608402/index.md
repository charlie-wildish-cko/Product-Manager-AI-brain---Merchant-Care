---
id: 22435560608402
section_id: 22435344941714
title: "Scheme Merchant IDs - Glossary & Introduction"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22435560608402-Scheme-Merchant-IDs-Glossary-Introduction"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:36:40Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JBHFK1FTRFHHXXN4PTQS8A0A"]
label_names: ["global", "glossaries_and_introductions", "case_request_for_documentation", "scheme_merchant_ids_glossary_and_introduction", "case_rfd_issue_scheme_merchant_ids"]
user_segment_ids: [11003606966930]
archive: false
---

## Key Terms & Definitions

| **Term** | **Definition** |
| --- | --- |
| **CAT** | Client Admin Tool |
| **Care Team** | Merchant Care Team |
| **Config Team** | Merchant Configuration Team |
| **MID** | Merchant Identification |
| **CAID** | Card Acceptor Identification |

## **Introduction**

### **Purpose**

The Scheme Merchant ID or Card Acceptor ID (also known as Merchant ID or MID by some internal stakeholders and merchants) is a unique identifier assigned to a merchant by their payment processor (in this context Checkout.com) when they set up a merchant account. This identifier is used in card payment transactions to track and associate payments with the specific merchant. The Card Acceptor ID plays a crucial role in merchants' overall payment process.

## **Context**

### **Merchant requires the CAID for various reasons as follows:**

1. **Processing Payments**

The Card Acceptor ID is embedded in each transaction when a customer makes a card payment. This ID:

- Identifies the merchant to the payment processor or acquirer.

- Tracks transactions that occur at a specific merchant location or across multiple locations.

1. **Managing Multiple Locations or Business Units**

Each location might have its own Card Acceptor ID for businesses with multiple physical locations or business units. This helps in:

- Tracking sales by location: Merchants can easily monitor which store or business unit performs better.

- Reconciling payments: When each location or business unit has its ID, matching payments with the appropriate accounts or locations becomes simpler.

- Fraud prevention: By segmenting transactions by location, merchants can better spot unusual activity that might indicate fraud.

1. **Fraud Detection and Monitoring**

The Card Acceptor ID can be used for monitoring and security:

- Flagging suspicious activities: Processors can use the Card Acceptor ID to detect unusual patterns across a merchant's transactions and prevent potential fraud.

- Chargeback and dispute management: The ID helps to efficiently track transactions tied to disputes or chargebacks and identify patterns that may need further investigation. 

1. **Reporting and Analytics**

Merchants often use their Card Acceptor ID to access detailed reports and insights from their payment processor or acquiring bank. These reports provide:

- Transaction details: Broken down by payment method, time of day, or location (if multiple Card Acceptor IDs are used).

- Sales trends: Analyzing overall sales data and identifying peaks and lows in business activity.

- Reconciliation of funds: Matching payments to the Card Acceptor ID ensures merchants can accurately reconcile funds in their bank account.

1. **Managing Multiple Merchant Accounts**

For large corporations or conglomerates, having different Card Acceptor IDs for different divisions or product lines simplifies:

- Segregation of financial data: By assigning distinct IDs, different departments or subsidiaries can manage their finances independently while still using the same overall business entity.

- Customizing customer experiences: Different business units or online platforms may offer distinct payment methods, tailored pricing, or special promotions, all of which can be tracked using different Card Acceptor IDs. 

1. **Facilitating Compliance with Payment Standards**

Since the Card Acceptor ID is linked to the merchant’s payment processing account, it plays a role in ensuring:

- PCI-DSS Compliance: This ensures that merchants adhere to data security standards when accepting card payments.

- Regulatory Reporting: The unique identifier helps in generating necessary reports for tax authorities or regulators.

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Scheme Merchant IDs articles, please see ****[Scheme Merchant IDs Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22435536975122-Scheme-Merchant-IDs-Tools-Permissions)
