---
id: 21991168389522
section_id: 21991145544082
title: "Captured transaction"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/21991168389522-Captured-transaction"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:37:31Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQT889RQXXSG27BB4ZJ0M"]
label_names: ["case_transactions", "case_transactions_issue_unable_to_void_payment", "MENA", "captured_transaction"]
user_segment_ids: [11003606966930]
archive: false
---

## Process Steps

1. Check transaction status via the MPGS API.

  1. 
From DataDog we can get this information from MPGS logs:

  2. Once we have the MID/Token and order ID, From MPGS we can verify the transaction status 

2. Go back to the merchant and explain the below if you see the transaction is ‘captured’:

  1. If the transaction appears as captured then a void will not go through

  2. If the merchant wants to void a payment they need to refund the payment

## Glossaries and Definitions:

For **Key Terms and Definitions** on Transactions as well as an **introduction into MENA Gateway and non-Gateway merchants**, please see ****[Transactions Glossary](https://checkoutint.zendesk.com/hc/en-us/articles/21991201065106-Transactions-Glossary-Introduction)**.  **
 
 
 
 
 
 
 
 
 
For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Transactions articles, please see ****[Transactions Tools & Permissions](https://checkoutint.zendesk.com/hc/en-us/articles/21991176883474-Transactions-Tools-Permissions)**.**
