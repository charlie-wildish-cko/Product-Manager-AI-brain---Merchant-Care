---
id: 23188666220690
section_id: 21991136181650
title: "PPRO Refunds"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/23188666220690-PPRO-Refunds"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-09-25T11:20:53Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQT889RQXXSG27BB4ZJ0M"]
label_names: ["case_transactions", "case_transactions_issue_refund_proof_apm", "confirmation_of_received_funds", "ppro_expired", "refund_proof_for_ppro", "ppro_voided"]
user_segment_ids: [11003606966930]
archive: false
---

**Use this article when**

Investigating and escalating a refund request for PPRO which supports full and partial refunds for Bancontact, Sepa, P24 & Multibanco.INTRODUCTION TO PPRO REFUNDS 💬 

PPRO is a payment aggregator that allows merchants to accept **Alternative Payment Methods (APMs)**, such as Bancontact, Multibanco, SEPA and P24. PPRO handles the processing and collection of funds, simplifying the process for merchants.

While PPRO supports both full and partial refunds for these APMs, manual refunds for PPRO transactions are not handled by the Level 1 Merchant Care team. Therefore, this guide will focus on the necessary steps to investigate the transaction's status before escalating the request to the L2 Merchant Care team.

See the: [PPRO Response codes](https://checkout.atlassian.net/wiki/spaces/APM/pages/6478659591/PPRO+Response+Codes) article

⚠️ **Warning:** The L1 Merchant Care team cannot handle manual refunds for PPRO transactionsPROCESS FOR INVESTIGATING A REFUND REQUEST 👀

**Step 1. Locate the Transaction: **Use the payment ID to find the transaction on the Dashboard

**Step 2. Verify Event Type:** Paste the payment ID into Retool and look for the event type. Select either:

- 
`**AlternativeChargeCancelled**` or;

- `**AlternativeChargeExpired**`

 

**Step 3. Find the AcquirerTransactionID:** Once you open the events in Retool, find and copy the `**AcquirerTransactionID**`

**Check PPRO Backend:**

- Paste the `AcquirerTransactionID` into the **TxID textbox** on the PPRO backend

- Set the correct date range and search for the transaction

**Examine Funds Status:**

- Check the `**FundsStatus**` field

- If the status is `**NotExpected**` this means funds were not received, and no refund is needed

- If the status is `**Received**` you need to perform additional checks - see step 4

**Step 4. Funds Received - Conduct Further Checks **

- Check if the payment ID is listed in the ****[APM Reconciliation Google Sheet](https://docs.google.com/spreadsheets/d/13xCWhxBD-Zmeh9dxnNrek8xCHnpXaHA9snFLPUHUKSc/edit?gid=1814191337#gid=1814191337%20)

  - If it is, follow the recommended action in **column J**

  - If not, use the ****[Looker Report](https://checkoutinternal.eu.looker.com/looks/11419?toggle=fil&qid=tbmsa8DQgFLk4hEtz4KifG) to check the status in the **Status column**

RESOLUTION ⚒️

**Step 5. Determine Action and Escalation Path:**

- The Status is `**Cancelled, Expired or Declined**`, escalate to the L2 team, who will perform a refund on the PPRO Backend

- If the status is `**Deferred**` or `**Captured**`, a refund cannot be processed via the backend

ESCALATIONS ⬆️

Once you have completed your investigation, compile all the information, escalate the case to the L2 APM Team, and follow these steps:

- In Zendesk, apply the **L1>L2 macro** from the dropdown menu

- Select **APM** from the next dropdown and click **NEW/OPEN** to assign the case to L2 Merchant Care

**Merchant requests proof of refunds**

Proof of refunds is provided by the PPRO Team. Please email `**support@ppro.com**` with the screenshots from the backend and the transaction details. They will attach the proof to the email sent. Normally, this takes 1-2 business days.

- **Apply Macro -> Transfer -> External -> APM -> (Name of affected APM)**
