---
id: 22064124487058
section_id: 22057326312210
title: "3DS Response Code 20154: Recurring Payment Processed with Regular Flow"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22064124487058-3DS-Response-Code-20154-Recurring-Payment-Processed-with-Regular-Flow"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:34:09Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRP1QGWAFPTEP0CSMC1WBV"]
label_names: ["global", "response_code_20154", "case_3ds_issue_response_code_20151_-_20156", "case_3ds_issue_response_code_20151_-_20159", "case_3ds_issues", "20154_response_recurring_payment_processed_with_regular_flow"]
user_segment_ids: [11003606966930]
archive: false
---

## Process Steps

1. Confirm with the merchant the impacted decline response code (if not mentioned yet), and the that the impacted response code is RC20154.

2. 
**Scenario 1**: One or a few payments over a short period indicate a 3DS issue

  1. Open Dashboard

  2. Take the sample Payment ID provided by the merchant and check if these transactions were declined with RC20154

  3. Once confirmed, run this [looker report](https://checkoutinternal.eu.looker.com/explore/payment_lifecycle/fct_payin?toggle=fil,vis&qid=qi8XbXfj9Og1DYf3ezGh1J) to understand the merchant’s request body

  4. If the field **3DS requested** returns No, this means that the merchant is not attempting a 3DS transaction

  5. Now the merchant has the right to request a non-3DS transaction as long as the payment type is recurring

  6. Check the same [looker report](https://checkoutinternal.eu.looker.com/explore/payment_lifecycle/fct_payin?toggle=fil,vis&qid=i6paCE9S9iAXVlM6TE3dkn) if the field **Merchant initiated** = Yes/No

  7. Now that you have your looker report ready, you can use this to decide on the issue

    1. If the merchant is not making recurring payments + decline returned RC20154, they can re-attempt the transaction with 3DS enabled “true” where the likelihood of approval by the issuing bank should fix the RC20154 decline response code

    2. If the merchant is making recurring payments + decline returned RC20154, they should check the [fields for MIT](https://www.checkout.com/docs/payments/accept-payments/pay-with-stored-card-details/recurring-payments-with-stored-card-details) in the request body to confirm it has:

__

1. The possible reason behind returning RC20154 for recurring transactions is most likely related to

  1. The merchant sets the payment type “Regular” but is trying to make recurring (MIT) payments

2. The merchant needs to either

  1. Set payment type “regular” but set 3DS enable to “true” if not doing recurring, or

  2. Set payment type “recurring” but set all mandatory fields as displayed below

__

## Glossaries and Definitions:

For **Key Terms and Definitions** on 3DS, please see ****[3DS Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22059673420818-3DS-Glossary-Introduction)   

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the 3DS articles, please see ****[3DS Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22059810908306-3DS-Tools-Permissions)
