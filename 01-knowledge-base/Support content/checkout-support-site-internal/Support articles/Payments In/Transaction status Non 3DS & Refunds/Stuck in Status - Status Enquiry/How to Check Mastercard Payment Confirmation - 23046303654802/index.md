---
id: 23046303654802
section_id: 23045937114898
title: "How to Check Mastercard Payment Confirmation"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/23046303654802-How-to-Check-Mastercard-Payment-Confirmation"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-03-18T13:40:33Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQT889RQXXSG27BB4ZJ0M"]
label_names: ["case_transactions", "case_transactions_issue_status_proof", "global", "mastercard_transaction_status"]
user_segment_ids: [11003606966930]
archive: false
---

**Use this article when**

Checking the status of a Mastercard transaction, specifically focusing on the clearing status. 

**Case type: **Payments in

**Issue Type: **Transaction status (Non 3DS & Refunds)

**Reason: **Stuck in status / status enquiry

## INTRODUCTION TO THE ISSUE 💬

Checking the status of a Mastercard transaction is useful for investigating issues like transaction duplicates, reversals, or a pending clearing status.

- Clearing file generation occurs every 1 hour

- Mastercard has 6 settlement cut-off cycles

- Settlement files are received 6 times per day

PROCESS TO CHECK A MASTERCARD TRANSACTION STATUS🖊️

1. In the Zendesk ticket, go to **Apps**, and expand the **Checkout Agent Toolkit**

2. Click the relevant Payment ID to bring up the **Details** and **Timeline** view

3. Under **Details** **> Card details**, you can confirm the **Card** **type** and the **Scheme** (e.g. Visa, Mastercard):-

4. Under **Timeline**, you will see the clearing status of the relevant payment

5. As a backup, and if available, you can input and convert the Payment ID to a GUID, then copy it, and check the clearing status on the Clearing events Retool with the GUID:-

  1. Retool > Input ID > Decode > Copy > Paste into Retool search bar to check the gateway and clearing status

 ESCALATIONS⬆️If the transaction is not present in the Outgoing table, there may be an issue, like:

- Application Error

- Validation Error

- Rejection from Schemes

- Timeout

- File generator

A ticket needs to be raised to [Payment Engineering Operations](https://checkoutsupport.freshservice.com/a/catalog/request-items/600) to investigate.
