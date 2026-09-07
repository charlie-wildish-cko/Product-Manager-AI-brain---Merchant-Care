---
id: 29188561707026
section_id: 29188640182674
title: "Understanding Differences Between a Gateway and Non-Gateway Model"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/29188561707026-Understanding-Differences-Between-a-Gateway-and-Non-Gateway-Model"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-09-08T09:37:06Z"
permission_group_id: 26838654181266
content_tag_ids: []
label_names: ["gateway_merchants", "non_gateway_merchants", "Gateway"]
user_segment_ids: [11003606966930]
archive: false
---

**Use this article to**

Understand the difference between a gateway and non-gateway model and to identify what model the merchant is using.INTRODUCTION TO GATEWAY/NON-GATEWAY MODELS 💬

It's important to understand the difference between Gateway and Non-Gateway merchants, especially when working with requests from the MENA region, where Gateway merchants are common. 

In the MENA region, payments with MADA, Saudi Arabia's domestic payment network, are accepted. MADA's partnerships with major card schemes like Visa and Mastercard ensure that these cards are accepted both locally and globally.

The first thing agents should do when handling MENA requests is to determine the type of merchant they are dealing with. Here are the main differences:

| **Information** | **Gateway Merchants** | **Non-Gateway Merchants** |
| --- | --- | --- |
| Checkout's Role | Provides only the technology for transaction processing. | Provides both the technology and acquiring services. |
| Acquiring Entity | Checkout does not act as the acquirer; merchants must have an agreement with a Third-Party Acquirer (TPA). | Checkout is the acquirer, responsible for the end-to-end (E2E) transaction flow, including all payments and settlements. |
| Refund Responsibility | The merchant is responsible for handling refund processes if a refund failure occurs, due to direct fund flow. | Checkout manages all aspects of payments and settlements. |
| TPA Requirement | Requires an agreement with a Third-Party Acquirer (TPA) to process transactions. A directory of TPAs in MENA is available for reference __[here](https://docs.google.com/spreadsheets/d/1ipGueNYij7yEEr1y9S-0Ba0lqS9Ia3Wbsnm6YuvwoaQ/edit#gid=1771915325). | Checkout also maintains an agreement with SAB (TPP), where we processes the transaction, and SAB handles the settlement. |

IDENTIFYING A GATEWAY/NON-GATEWAY MERCHANT 👀

| **Information Available** | **Tool/Platform** | **Action Required** | **Outcome/Guidance** |
| --- | --- | --- | --- |
| Payment ID | Retool - Traffic Insights | - Navigate to Traffic Insights in Retool   - Perform a query using the provided Payment ID  -  Scroll to the "Transaction Data" section within the query results  -  Locate the Merchant data within this section | This step allows you to obtain the Account Channel Name (Business Name) or Client ID associated with the Payment ID, which can then be used in the CAT Admin Tool for further verification. |
| Merchant Account Name, Entity ID, Client ID, or Processing Channel (Any of these) | CAT Admin Tool | - Open the CAT Admin Tool  - Input the available merchant information (e.g., Merchant Account Name) into the search bar  - Select the correct merchant from the search results to access their account details  - From the merchant entities' list, select the relevant entity  - In the left-hand side menu, navigate to "Processing", then select "Gateway"  - From the displayed gateway processing channels, choose the required processing channel  - Select the relevant processor | Under "Payment Gateway Settings", you will find a clear indicator:   • "Yes" signifies a Gateway merchant.   • "No" signifies a Non-Gateway merchant.  This definitively identifies the merchant's operational classification based on their payment gateway configuration. |
