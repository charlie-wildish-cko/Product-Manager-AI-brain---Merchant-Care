---
id: 23046343726994
section_id: 23045959776018
title: "Decline Code: 20054 - Expiry Date Issue"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/23046343726994-Decline-Code-20054-Expiry-Date-Issue"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-23T15:57:51Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQT889RQXXSG27BB4ZJ0M"]
label_names: ["case_transactions", "case_transactions_issue_transaction_declined_reason_response_codes_unclear", "global", "20054_expiry_date_issue"]
user_segment_ids: [11003606966930]
archive: false
---

Use this article when

Investigating decline code 20054, which indicates transactions are declined at the Auth level due to an incorrect expiry date entered.PROCESS 🖊️

Below are the steps to take when transactions decline at the Auth level due to an incorrect expiry date inputted when transacting:-

1. Check the expiry date of the card on the Hub/Dashboard

1. Check what the cardholder has inputted as the expiry date in the payment request in Datadog logs: 

1. Check if the cardholder has retried transacting with the correct expiry date in the DD logs.

2. Check for any warnings/errors in the Datadog logs for the concerned payment.

3. If there is no error and the declines are for the same issuer, the latter must be contacted.
