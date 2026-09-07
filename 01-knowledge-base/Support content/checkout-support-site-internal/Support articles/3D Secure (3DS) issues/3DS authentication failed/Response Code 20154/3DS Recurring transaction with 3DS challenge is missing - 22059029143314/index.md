---
id: 22059029143314
section_id: 22057326312210
title: "3DS Recurring transaction with 3DS challenge is missing"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22059029143314-3DS-Recurring-transaction-with-3DS-challenge-is-missing"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:39:57Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRP1QGWAFPTEP0CSMC1WBV"]
label_names: ["global", "response_code_20154", "case_3ds_issue_response_code_20151_-_20156", "case_3ds_issue_response_code_20151_-_20159", "case_3ds_issues", "3ds_recurring_transaction_with_3ds_challenge_is_missing"]
user_segment_ids: [11003606966930]
archive: false
---

## Process Steps

3DS challenge requests for recurring transactions where the merchant sets the flag to 3ds.enabled = true, but the 3DS challenge is missing.

1. Ensure the following for SCA compliance:

  1. For customer-initiated payments, use:

  2. merchant_initated: false

  3. payment_type: <"Regular"/ "Recurring"/"MOTO"/"Installment">

  4. 3ds.enabled: true

  5. 3ds.challenge_indicator: challenge_requested_mandate

2. For merchant-initiated subsequent payments, use:

  1. merchant_initated: true

  2. previous_payment_id: <authenticated payment ID>

  3. payment_type: <"Recurring"/"Installment">

  
This ensures the payment request adheres to SCA requirements and leverages the previous successful authentication for subsequent payments.

## Glossaries and Definitions:

For **Key Terms and Definitions** on 3DS, please see ****[3DS Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22059673420818-3DS-Glossary-Introduction)   

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the 3DS articles, please see ****[3DS Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22059810908306-3DS-Tools-Permissions)
