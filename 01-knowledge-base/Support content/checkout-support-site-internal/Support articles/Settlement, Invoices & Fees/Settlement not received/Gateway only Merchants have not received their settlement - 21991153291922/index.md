---
id: 21991153291922
section_id: 21991150886162
title: "Gateway only Merchants have not received their settlement"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/21991153291922-Gateway-only-Merchants-have-not-received-their-settlement"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:36:45Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHQKPVKA7XAZRYSRWE7JRH4"]
label_names: ["row", "case_settlements", "case_settlements_issue_settlement_not_received", "gateway_only_merchants_have_not_received_their_settlement"]
user_segment_ids: [11003606966930]
archive: false
---

## Process Steps

Agents should first ensure that the merchant is Gateway only. To do this, please follow the steps below:**MBC Merchants**

**Payment ID**

1. On Retool, go to Traffic Insights and perform a query using the payment ID 

2. Scroll down the Traffic Insights query results page and find the “Transaction Data” section. Within this section, you will find Merchant data.   

3. Obtain the Account Channel Name (Business Name) or Business ID as required

 **Business Name**Once you have the Business Name, go to [Hub Admin](https://hub-admin.ckotech.co/admin/summary?iss=https:%2F%2Fidentity.checkout.com) and follow the below steps:

1. Type the Business Name in the search field and perform a search

2. From the results, select the relevant Business - this will open up that merchant’s account

3. Go to Processing Settings, 

4. Go to Processors Management

5. **In the Processors table, you will see which processor is gateway or non-gateway by looking at the “GW Only” column. **

**Key for “GW Only” column: **

- 
**Yes: **Gateway** **

- 
**No: **non-Gateway

 NAS Merchants**Payment ID**

1. On Retool, go to Traffic Insights and perform a query using the payment ID

2. Scroll down the Traffic Insights query results page and find the “Transaction Data” section.

3. Within this section, you will find Merchant data 

4. Obtain the Account Channel Name (Business Name) or Business ID as required

 **Merchant Account Name, Entity ID, Client ID, or Processing Channel**

1. On CAT Admin Tool, type the relevant merchant information that you have (e.g. merchant account name) and perform a search   

2. From the search results, select the correct merchant - this will open up the merchant’s account.

3. Select the relevant entity from the merchant entities’ list   

4. On the left-hand side menu:

  1. Select “Processing”

  2. Select “Gateway”

5. From the provided gateway processing channels list, select the required processing channel 

6. Select the relevant processor  

7. Under “Payment Gateway Settings” you will see if the merchant is gateway or non-gateway.

**Key**:

- 
**Yes**: Gateway

- 
**No**: Non-gateway

 Once confirmed that the processor of the transaction is Gateway, advise the merchant that they must raise the issue with their acquirer since they are the ones managing their settlements. If the merchant is not gateway, follow the guidance in [Settlement not received - MT103 required](https://checkoutint.zendesk.com/hc/en-us/articles/21991189120018-Settlement-not-received-MT103-required) article.

## Glossaries and Definitions:

For **Key Terms and Definitions** on Transactions as well as an **introduction into MENA Gateway and non-Gateway merchants**, please see ****[Settlements Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/21991207693458-Settlements-Glossary-Introduction)   For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Transactions articles, please see ****[Settlements Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/21991176789266-Settlements-Tools-Permissions)
