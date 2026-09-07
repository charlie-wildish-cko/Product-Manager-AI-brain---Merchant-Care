---
id: 21991175438738
section_id: 21991145423250
title: "Cybersource"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/21991175438738-Cybersource"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:37:31Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQT889RQXXSG27BB4ZJ0M"]
label_names: ["case_transactions", "MENA", "case_transactions_issue_unable_to_capture_payment", "cybersource"]
user_segment_ids: [11003606966930]
archive: false
---

## Process Steps

1. All acquirers can follow the below process

2. Check transaction status via the Cybersource portal

3. Log into the [Cybersource portal](https://ebc2.cybersource.com/ebc2/app/TransactionManagement/details?requestId=6809402917066418304276&merchantId=mashreq_8108771_aed&fromSimilarSearch=false&goBackCount=-2) with the available credentials

  1. Locate the MID from Cybersource authorisation API from datadog

  2. Refer to [this sheet](https://docs.google.com/spreadsheets/d/1x-6_2QW8a7U9yyzUabGLS8ajxCYMuS8qfI300kc_EZE/edit#gid=0) to locate the password to the MID and log in to [Cybersource](https://ebc2.cybersource.com/ebc2/app/TransactionManagement/details?requestId=6809402917066418304276&merchantId=mashreq_8108771_aed&fromSimilarSearch=false&goBackCount=-2) using the new password

  3. Go to the option Transaction Management. Select Transactions

4. Click on ‘add filter’. Choose the option Merchant Reference Number

5. Enter the reference number and adjust the date range accordingly

**Note**: If using the AcquirerReferenceID from Hermes, add the filter RequestID.Once the transaction has been located and is in an authorised state, select it and proceed to Capture as requested by the merchant.

## Glossaries and Definitions:

For **Key Terms and Definitions** on Transactions as well as an **introduction into MENA Gateway and non-Gateway merchants**, please see ****[Transactions Glossary](https://checkoutint.zendesk.com/hc/en-us/articles/21991201065106-Transactions-Glossary-Introduction)**.  **
 
 
 
 
 
 
 
 
 
For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Transactions articles, please see ****[Transactions Tools & Permissions](https://checkoutint.zendesk.com/hc/en-us/articles/21991176883474-Transactions-Tools-Permissions)**.**
