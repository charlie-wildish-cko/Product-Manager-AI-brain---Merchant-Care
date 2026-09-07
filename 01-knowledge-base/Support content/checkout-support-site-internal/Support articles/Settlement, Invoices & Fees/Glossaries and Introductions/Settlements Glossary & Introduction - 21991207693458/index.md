---
id: 21991207693458
section_id: 21991151260690
title: "Settlements Glossary & Introduction"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/21991207693458-Settlements-Glossary-Introduction"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:36:42Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHQKPVKA7XAZRYSRWE7JRH4"]
label_names: ["case_settlements", "global", "settlements_Glossary_and_introduction"]
user_segment_ids: [11003606966930]
archive: false
---

## Key Terms & Definitions

| **Term** | **Definition** |
| --- | --- |
| **ROW** | Rest of the World |
| **ABC/HUB** | Legacy account structure/environment for Checkout merchants |
| **NAS** | New Account Structure. This is the new account environment that all Checkout merchants are moving to |
| **Gateway Merchants ** | Gateway merchants only use CKO’s technology to be able to process their transactions. Gateway merchants need a third-party acquirer (TPA) to process their transactions and get their settlements. |
| **Non-Gateway Merchants ** | Non-gateway merchants use CKO for both the technology and acquiring services. |
| **TPA** | Third-Party Acquirer |
| **Acquirer** | A bank or financial institution that processes credit or debit card payments on behalf of merchants. They sit between the gateway and the card schemes |
| **SAB** | Saudi British Bank - an acquirer in Saudi Arabia. |
| **Mashreq ** | Mashreq Bank - our main acquirer in the UAE. |
| **MPGS ** | MPGS, or MasterCard Payment Gateway Services, is a comprehensive payment processing platform provided by MasterCard which our third-party acquirer (TPA) utilizes. |

## Introduction to the Gateway/Non-Gateway Model:

This section is particularly helpful for MENA requests where Gateway merchants are common.  

When working through MENA requests, the first step that agents need to take is to understand whether the merchant is a Gateway or non-Gateway merchant. To do this, it is important to first understand the difference between the two:

| **Gateway Merchants** | **Non-Gateway Merchants ** |
| --- | --- |
| CKO only provides the technology for gateway merchants to be able to process their transactions.  CKO does not act as the acquirer for these merchants and as such, we are not responsible for payments of settlements.  Gateway merchants need to have an agreement with a third-party acquirer (TPA) to process their transactions and get their settlements. In MENA, Mashreq is the TPA that merchants use. | CKO provides both the technology and acquiring services to these merchants, i.e.      CKO is responsible for the E2E transaction flow for these merchants and we deal with all payments and settlements for these merchants. |
| CKO also has an agreement with SAB (SAB TPP) whereby the transaction is processed by CKO, but the settlement is done by SAB. |  |

### Check if a Merchant is Gateway or Non-Gateway:

| **MBC Merchants** |  |  |
| --- | --- | --- |
| **Information Available** | **Action Required** | **Additional Guidance ** |
| **Payment ID** | On Retool, go to Traffic Insights and perform a query using the payment ID | **** |
| Scroll down the Traffic Insights query results page and find the “Transaction Data” section.  Within this section, you will find Merchant data.       Obtain the Account Channel Name (Business Name) or Business ID as required | **** |  |
| **Business Name ** | Once you have the Business Name, go to [Hub Admin](https://hub-admin.ckotech.co/admin/summary?iss=https:%2F%2Fidentity.checkout.com) and follow the below steps:    1. Type the Business Name in the search field and perform a search,   2. From the results, select the relevant Business - this will open up that merchant’s account,   3. Go to Processing Settings,   4. Go to Processors Management  5. In the Processors table, you will see which processor is gateway or non-gateway by looking at the “GW Only” column.   Key for “GW Only” column:    - Yes: Gateway   - No: non-Gateway | **** |

 

| **NAS Merchants** |  |  |
| --- | --- | --- |
| **Information Available** | **Action Required** | **Additional Guidance ** |
| **Payment ID** | On Retool, go to Traffic Insights and perform a query using the payment ID | **** |
| Scroll down the Traffic Insights query results page and find the “Transaction Data” section.  Within this section, you will find Merchant data.       Obtain the Account Channel Name (Business Name) or Business ID as required | **** |  |
| **Merchant Account Name, or ** **Entity ID, or ** **Client ID, or ** **Processing Channel ** | On CAT Admin Tool, type the relevant merchant information that you have (e.g. merchant account name) and perform a search | **** |
| From the search results, select the correct merchant - this will open up the merchant’s account. |  |  |
| Select the relevant entity from the merchant entities’ list | **** |  |
| On the left-hand side menu:   - Select “Processing”  - Select “Gateway”  - From the provided gateway processing channels list, select the required processing channel | **** |  |
| Select the relevant processor | **** |  |
| Under “Payment Gateway Settings” you will see if the merchant is gateway or non-gateway.  Key:    - Yes: Gateway   - No: Non-gateway | **** |  |

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Transactions articles, please see ****[Settlements Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/21991176789266-Settlements-Tools-Permissions)
