---
id: 21991199433746
section_id: 21991145440786
title: "SAB TPA manual process - MENA SAB Manual refund"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/21991199433746-SAB-TPA-manual-process-MENA-SAB-Manual-refund"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-09-29T17:13:39Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQT889RQXXSG27BB4ZJ0M"]
label_names: ["case_transactions", "MENA", "case_transactions_issue_smr_sab_manual_refund", "sab_tpa_manual_process"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

For handling manual refunds for MADA card transactions that have failed due to a 30-day time limit.

**Problem:** A refund for a MADA card transaction failed after the 30-day refund window. 

**Solution:** Submit a manual refund request to SAB via a shared spreadsheet.

### DESCRIBE THE ISSUE 💬

This refund process applies only to MADA transactions due to refund limitations on MADA Cards. According to current guidelines, the maximum time frame for a standard refund on a MADA payment is 30 days. If this period has passed, refund attempts will receive a 20030 response code indicating a Format Error.

If a refund is identified as MADA, processed on acquirer SAB and failed with response code 20030, then a manual refund request is raised by adding the transaction details to this [Sheet](https://docs.google.com/spreadsheets/d/1LiOtz-4bwIBgK6GpOaFkG4gNRpCDgCCmta2Az9BGSsw/edit?gid=294594464#gid=294594464).

More details on MADA transactions and BINs can be found in the [documentation](https://www.checkout.com/docs/payments/add-payment-methods/mada).KEY TAKEAWAYS 🔑

- This process applies **only** to **MADA transactions** processed by the **SAB MPGS** acquirer

- A manual refund is required when a standard refund attempt fails with a **20030 response code**

- The manual request is submitted by adding specific transaction details to a shared [Sheet](https://docs.google.com/spreadsheets/d/1LiOtz-4bwIBgK6GpOaFkG4gNRpCDgCCmta2Az9BGSsw/edit?gid=294594464#gid=294594464)

- The merchant must provide their **12-digit SAB bank account number** for the specific Merchant ID (MID)

PROCESS STEPS🖊️

⚠️ Please follow these instructions carefully to ensure accurate and timely refund processing.

Before initiating a manual refund, check:

- **MADA Transaction**: This refund process is only for MADA transactions - due to limitation on refunds for MADA Cards.

-  The maximum allowed window for a normal refund on a MADA payment is 30 days - if this period is over, then refund attempts will return a 20030 response code corresponding to Format Error.

- 
**Acquirer**: The acquirer should be SAB MPGS; do not enter SAB TPP transactions on this sheet! This can be identified from the Details tab under the Checkout Agent Toolkit on Zendesk.

- **The Refund should not have failed with a Hard decline**: Check if the merchant already attempted a refund, and the decline should not be a HARD DECLINE, e.g. such as 30043, corresponding to Stolen/Pick Up Card.

- **SAB Bank Account Number: **Make sure that you have the Merchant’s Bank account number for the MID on which the transaction was processed. The account number refers to the SAB Bank account number associated with the merchant for a specific Merchant ID (MID).

❌ **SAB Bank Account Number: **This information must be provided by the merchant - this is not the bank account number of the cardholder

- If the bank account number isn't on the ticket, please check previous MID entries on the refund sheet.

- If these entries exist, the bank account number will match the earlier one and be 12 digits long.

### Step 1. Search for the Payment ID in the Checkout Agent Toolkit on Zendesk

Fill in the details as a new row  on this [Google sheet](https://docs.google.com/spreadsheets/d/1LiOtz-4bwIBgK6GpOaFkG4gNRpCDgCCmta2Az9BGSsw/edit?gid=294594464#gid=294594464) 

- **Merchant Name:** The Merchant Name can be found on the Zendesk ticket  

- **Retrieval Reference Number(RRN):** The RRN can be obtained on the Details tab under Payment details:- 

- 
**Account Number:** The account number is the SAB Bank account linked to the merchant's Merchant ID (MID) and must be provided by the merchant - this is not the cardholder's bank account number. 

- 
If unavailable on the ticket, check previous MID entries on the refund sheet; the 12-digit account number will match earlier entries.

- 
**Merchant ID(MID): **The MID details can be obtained on the Details tab under Merchant IDs:- 

- 
**Authorisation Code:** The Authorisation code for the payment can be found on the Details tab under Acquirer Response:-

- **Transaction Date: **The transaction date for the payment can be seen in the Timeline tab
💡Please note to enter the date value in MM/DD/YYYY format                    

- 
**Transaction Amount:**The transaction amount appears when you click the payment ID in the Checkout Agent Toolkit. 
⚠️ Enter only the value, not the currency on the sheet

- **Refund Amount: **The refund amount is generally mentioned by the merchant in the ticket; if not, please refer to the Timeline tab

✅ Note: Please add the Zendesk Ticket number and agent name against each entry on the sheetMANUAL REFUND PROCESS 🖊️

- The list of refunds will be shared with SAB daily before 1:00 PM, except Fridays and Saturdays

- Once processed, stakeholders will update the sheet by adding the corresponding CPS ID

- The CPS ID serves as proof of the refund, which can be shared with the merchant

- Please note that for some transactions, the CPS ID may not be provided. Instead, it will be noted as "SAB to SAB," indicating that the cardholder’s bank was also SAB, and the refund was processed as an internal transaction

- In these cases, the customer may use the authorisation RRN should they need to contact the bank.

**⚠️ Note: Agents should only fill columns with green headers. Do not fill columns with grey headers.**Sample email sent to SAB by associated stakeholders:
