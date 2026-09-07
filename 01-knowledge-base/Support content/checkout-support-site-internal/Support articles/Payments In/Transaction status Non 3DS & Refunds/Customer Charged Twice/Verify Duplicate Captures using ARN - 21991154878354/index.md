---
id: 21991154878354
section_id: 21991151380370
title: "Verify Duplicate Captures using ARN"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/21991154878354-Verify-Duplicate-Captures-using-ARN"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-03-18T13:48:08Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQT889RQXXSG27BB4ZJ0M"]
label_names: ["case_transactions", "verify_duplicate_captures_using_arn", "case_transactions_issue_duplicate_transactions", "ROW"]
user_segment_ids: [11003606966930]
archive: false
---

**Case type: **Payments in

**Issue Type: **Transaction status (Non 3DS & Refunds)

**Reason: **Customer charged twice

## Introduction

The merchant will reach out claiming the customer has been charged twice. First, we need to check if we have a single or double record of this transaction.

1. If single transaction, then we need to verify duplicate captures using ARN

2. If double transaction, then we need to verify duplicate transaction

## Process Steps

1. For a duplicate capture, a single transaction amount has been debited twice

  1. To verify a duplicate capture has taken place, follow the steps in the confluence page [here](https://checkout.atlassian.net/wiki/spaces/CHEC/pages/5311464129/Verify+Duplicate+Captures+using+ARN).

  2. If there is a duplicate capture, reach out to the clearing team using [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277) (select ‘clearing’ under ‘the field ‘Domain’) and ask them to provide advice on how to proceed forward. 

  3. If you do not see any duplicate captures then follow the below process to see if there have been two separate transactions.

## Glossaries and Definitions:

For **Key Terms and Definitions** on Transactions as well as an **introduction into MENA Gateway and non-Gateway merchants**, please see ****[Transactions Glossary](https://checkoutint.zendesk.com/hc/en-us/articles/21991201065106-Transactions-Glossary-Introduction)**.  **
 
 
 
 
 
 
 
 
 

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Transactions articles, please see ****[Transactions Tools & Permissions](https://checkoutint.zendesk.com/hc/en-us/articles/21991176883474-Transactions-Tools-Permissions)**.**
