---
id: 22059044688146
section_id: 22057257485074
title: "How to resolve 20151 through retool"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22059044688146-How-to-resolve-20151-through-retool"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:35:57Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRP1QGWAFPTEP0CSMC1WBV"]
label_names: ["global", "case_3ds_issue_response_code_20151_-_20156", "case_3ds_issue_response_code_20151_-_20159", "how_to_resolve_20151_through_retool", "case_3ds_issues", "response_code_20151"]
user_segment_ids: [11003606966930]
archive: false
---

## Process Steps

1. Open [Retool](https://retoolprod.mgmt.ckotech.co/apps/a04c8c20-72cf-11eb-bea4-e7bba7ba05e6/payment-performance-shared-debug/Traffic%20Insights#payment_id=), input the payment ID into the **Give me an ID** field and select **Query**  
  
  
  
 

2. Under Event type, select the appropriate event as per the table documented. The common event types are **AuthenticationUnavailable**, **AuthenticationDeclined **or **AuthenticationRejected**  
  
  
  
 

3. Use the Authentication tab and review the indicators for the decoded 3DS events  
  
  
 

4. Correlate the authentication event, transaction status and reason to the below table for common scenarios and their recommendations: 

| **Event Type** | **Status** | **Reason** | **Decoded Message** | **Solution** | **Sample payment id** |
| --- | --- | --- | --- | --- | --- |
| Authentication Unavailable | N | 01 | Cardholder failed authentication | Cardholder needs to contact the issuing bank to ensure they are permitted to process | pay_sm6zgiwxmmtebbdjdxsa4te36q |
| Authentication Rejected | R | 05 | Expired card | Cardholder to contact their issuing bank, as they are not permitted to process transactions using this method currently. The cardholder would need to update the card details with a valid and up-to-date card | pay_2hexz6nculxulpj3zl5ne7ln5a |
| Authentication Unavailable | U | 08 | No card record | Cardholder to contact the issuing bank to ensure the card is valid. Use a different card or alternative method to make a payment Alternatively, inform the merchant to ensure that the saved card information for customers is updated in their BIN list to ensure that card ranges API can be accessed. (This is only valid for merchants that use stored cards for future use or use our service to provide NT) | pay_sdikhkzziageno3oopdygkh2eq |
| Authentication Declined | N | 09 | Security failure | Inform the merchant to inform the cardholder to contact their issuing bank to ensure the card is valid and permitted to process these transactions | pay_nslcrtyxfckkdbypg7lbggkqo4 |
| Authentication Rejected | R | 11 | Suspected fraud | Inform the merchant to inform the cardholder to contact their issuing bank as the payment had failed due to suspected fraud  Also, check out these articles on [3DSecure Messages EMVCo](https://checkout.atlassian.net/wiki/spaces/32/pages/357531847/2.1+3-D+Secure+Messages+EMVCo) and [Authentication Response Message (ARes)](https://checkout.atlassian.net/wiki/spaces/32/pages/617317039/2.2+3-D+Secure+Messages+EMVCo#Authentication-Response-Message-(ARes)) for more information. | pay_6mub3ai5tqa25jlx2uwhizaw5a |
| Authentication Declined | N | 12 | Transaction not permitted to cardholder | Inform the merchant to inform the cardholder to contact their issuing bank as they are not permitted to currently process transactions in the method | pay_uqo3waqu24futhbynfhacpaoyq |
| Authentication Declined | U | 22 | ACS technical issue | Ensure that the merchant is sending the correct information; If they are using non-hosted integration, then the issue is on the merchant side If the issue is impacting a large volume of transaction from a singular ACS and integration is hosted integration, then contact the OC team Please refer to the relevant protocol version, when investigating this issue here - [3DSecure Messages EMVCo](https://checkout.atlassian.net/wiki/spaces/32/pages/617317039/2.2+3-D+Secure+Messages+EMVCo) |  |

## Glossaries and Definitions:

For **Key Terms and Definitions** on 3DS, please see ****[3DS Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22059673420818-3DS-Glossary-Introduction)   For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the 3DS articles, please see ****[3DS Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22059810908306-3DS-Tools-Permissions)
