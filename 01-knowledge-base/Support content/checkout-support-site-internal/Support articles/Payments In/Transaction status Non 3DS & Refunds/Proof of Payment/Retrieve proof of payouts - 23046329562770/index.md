---
id: 23046329562770
section_id: 23046197784338
title: "Retrieve proof of payouts"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/23046329562770-Retrieve-proof-of-payouts"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-03-18T13:57:50Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQT889RQXXSG27BB4ZJ0M"]
label_names: ["case_transactions", "global", "case_transactions_issue_refund_proof_schemes", "proof_of_payments_funds_not_received", "retrieval_for_proof_of_payouts_example"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

Use this guide to retrieve proof of payouts for merchants using Retool and VisaOnline.

**Case type: **Payments in

**Issue Type: **Transaction status (Non 3DS & Refunds)

**Reason: **Proof of payment (ARN, RNN, bulk)BEFORE YOU START ▶️

You need access to:

- **Retool** (specifically the `payout-search` folder)

- **VisaOnline**

- The **Payment ID** (e.g., `pay_rqo76...`) provided by the merchant

## PROCESS

1. For example, take **pay_rqo76dlrpkeedfudtbnwkwxn3y** from the merchant Livescore Betting and Gaming Limited

2. We copy and paste the payment ID into the Payouts-Search Folder on Retool as shown below:

1. Upon inserting the payment ID into the search bar, the below screen will appear:

1. On the bottom left-hand side, we have all of the different events which pertain to the inserted payment ID. Click on the **CardProcessingPassed** event:-

1. Upon choosing the CardProcessingPassed Event, the event details are displayed on the right-hand side as shown below. Look for the **Scheme_Transaction_ID**:

****

1. Log in to [VisaOnline](https://www.visaonline.com/)

2. Insert the **Scheme_Transaction_ID** in the Transaction ID field. Set the correct date range according to the date the transaction was processed:-

8. ⚠️ Ensure that the Standard list is checked and not the expanded list - this ensures the proofs are populated

9. Click on **Submit**. The required file will be available to download and **Save As PDF**:
