---
id: 21991200634514
section_id: 21991152036114
title: "SAB TPP transactions (Non MADA)"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/21991200634514-SAB-TPP-transactions-Non-MADA"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-30T17:10:01Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQT889RQXXSG27BB4ZJ0M"]
label_names: ["case_transactions", "MENA", "case_transactions_issue_refund", "SAB_TPP_transactions_(Non_MADA)", "Non_MADA_20030_Refund_failures"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

**Important: **KSA has a manual refund process due to the 30 day limitation for MADA. All other acquirers outside of KSA can be done directly from the Dashboard. For manual refunds please refer to this [highspot page](https://docs.google.com/spreadsheets/d/1g1I4-FixwMxsF07SLu_3mtin_650uVW-0MVOzS84xg8/edit#gid=1386391676) which gives you a breakdown of the process for KSA acquirers.

## Process Steps

1. Follow the below process when the merchant states that the refund was not received by the cardholder.

2. 
Email from merchant which should include:

  1. Payment ID or Payment reference number 

  2. 
Go to [Retool](https://retoolprod.mgmt.ckotech.co/apps/payment-performance-shared-debug/Traffic%20Insights#payment_id=) and look for the transaction details.

3. 
How to identify if its a SAB TPP transaction:

  1. 
Go to [Retool](https://retoolprod.mgmt.ckotech.co/apps/payment-performance-shared-debug/Traffic%20Insights#payment_id=) and use the Payment ID to search and determine if this transaction is a SAB TPP transaction, click on charge authorised event, look for the Global acquirer ID which will shown as SAB VISA/ SAB Mastercard which means its a TPP processor and the processing is done by CKO. 

4. 
Raise with the Clearing card processing team internally who will action this and take it forward.

  1. 
Raise a [Jira ticket](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277) and ask the team if the SABB TPP transaction was cleared (share the Payment ID). 

5. Clearing team will come back and confirm if the refund has been successful and Care to go back to the merchant to confirm it has been done. The confirmation from the clearing team will be in terms of clearing file number which will be in the sample format: _Filename - 269165-20240531-0000001820.cat.pgp_

## Glossaries and Definitions:

For **Key Terms and Definitions** on Transactions as well as an **introduction into MENA Gateway and non-Gateway merchants**, please see ****[Transactions Glossary](https://checkoutint.zendesk.com/hc/en-us/articles/21991201065106-Transactions-Glossary-Introduction)**.  **
 
 
 
 
 
 
 
 
 

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Transactions articles, please see ****[Transactions Tools & Permissions](https://checkoutint.zendesk.com/hc/en-us/articles/21991176883474-Transactions-Tools-Permissions)**.**
