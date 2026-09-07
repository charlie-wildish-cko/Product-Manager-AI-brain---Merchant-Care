---
id: 21991190473234
section_id: 21991151064338
title: "Unsettled Transactions for SABB TPP Merchants"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/21991190473234-Unsettled-Transactions-for-SABB-TPP-Merchants"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-09-24T09:51:42Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHQKPVKA7XAZRYSRWE7JRH4"]
label_names: ["case_settlements", "case_settlements_issue_have_i_been_settled_for_this_payment", "mena", "sab_tpp"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

If a SABB TPP merchant wants to check if their transactions have been captured, as they haven't been settled yet.INTRODUCTION TO SAB TPP💬

SABB TPP refers to a payment processing setup involving the Saudi Arabia British Bank (SABB) and Checkout.com. In this setup, Visa and Mastercard transactions for merchants in Saudi Arabia are routed through Checkout's Third Party Processor (TPP) rails, with SABB acting as a sponsor bank .PROCESS TO CHECK TRANSACTIONS FOR A SABB TPP🖊️  

### Step 1. Determine the transaction processor

Check the **GlobalAcquirerId** to see how the transaction was processed. Launch Traffic Insights retool using the pay_id to check the GlobalAcquirerId.

- If the `GlobalAcquirerId` is **"sabb-mpgs"**, the transaction was processed through **SABB_MPGS**

- If the `GlobalAcquirerId` does **not** contain "sabb-mpgs", the transaction was processed directly through **SABB **

### Step 2. Check the transaction status or escalate depending on the transaction processor

**If the transaction was processed through SABB_MPGS, check the transaction status:**

- Use Postman to directly check the final status on the MPGS portal

- Inform the merchant of the final status

- If the transaction was successfully captured or refunded, provide the merchant with the captured or refunded RRN (Retrieval Reference Number) and a screenshot of the status

- If the transaction failed, provide the merchant with the declined RRN and a screenshot

**If the transaction was processed directly through SABB:**

- 
[Raise a request](https://checkoutsupport.freshservice.com/support/catalog/items/600) with the Card Processing Team

- Select "Clearing" as the domain

- Request the CAT file name on which the transaction was shared with SABB. The CAT file is the clearing file

- Once you have the CAT file name, [contact the SABB Team](https://docs.google.com/spreadsheets/d/1ipGueNYij7yEEr1y9S-0Ba0lqS9Ia3Wbsnm6YuvwoaQ/edit?gid=1449834641#gid=1449834641) to confirm if they received the transaction details within that file

💡 Tip: This type of request may come from an existing conversation between SABB and the merchant, with SABB involving Checkout.com to get the CAT file name.
