---
id: 21991167105938
section_id: 21991151380370
title: "Verify Duplicate Transaction"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/21991167105938-Verify-Duplicate-Transaction"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-03-18T13:47:41Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQT889RQXXSG27BB4ZJ0M"]
label_names: ["case_transactions", "case_transactions_issue_duplicate_transactions", "ROW", "verify_duplicate_transaction"]
user_segment_ids: [11003606966930]
archive: false
---

**Case type: **Payments in

**Issue Type: **Transaction status (Non 3DS & Refunds)

**Reason: **Customer charged twice

## Introduction

The merchant will reach out claiming the customer has been charged twice. First, we need to check if we have a single or double record of this transaction.

1. If single transaction, then we need to verify duplicate captures using ARN

2. If double transaction, then we need to verify duplicate transaction

## Process Steps

1. For a duplicate transaction, there will be two separate transactions e.g. two different payment IDs

2. The merchant should have provided a Payment ID or Truncated card number in their email, if not request this from the merchant.

3. You can search using Payment ID or Truncated card:

  1. **Payment ID/ Truncated card number:**

  2. Log into Dashboard

  3. Search for the merchant, click on the payment page, search with the Payment ID/ Truncated card number or card fingerprint (found in the payment method section).

  4. If you search by Truncated card number or card fingerprint, you will see the results directly on this page.

  5. If you search by Payment ID, click on the Payment and use the card number as a filter to search for a corresponding transaction. 

    1. If we only have only one transaction then inform the merchant of your findings and ask the merchant to get the customer to provide a bank statement showing this amount has been debited twice.

      1. If the customer has already provided proof but if the proof is a **mobile banking app screenshot**, this is not a reliable source of proof as sometimes the mobile banking app shows a record for authorisation and another record for the capture (which can confuse the customer as they think they have been charged twice). 

      2. Request the merchant to get the customer to provide an official bank statement showing this proof. If this is provided, reach out to the clearing team using [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277) (select ‘clearing’ under ‘the field ‘Domain’) and ask them to provide advice on how to proceed forward. 

## Glossaries and Definitions:

For **Key Terms and Definitions** on Transactions as well as an **introduction into MENA Gateway and non-Gateway merchants**, please see ****[Transactions Glossary](https://checkoutint.zendesk.com/hc/en-us/articles/21991201065106-Transactions-Glossary-Introduction)**.  **
 
 
 
 
 
 
 
 
 

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Transactions articles, please see ****[Transactions Tools & Permissions](https://checkoutint.zendesk.com/hc/en-us/articles/21991176883474-Transactions-Tools-Permissions)**.**
