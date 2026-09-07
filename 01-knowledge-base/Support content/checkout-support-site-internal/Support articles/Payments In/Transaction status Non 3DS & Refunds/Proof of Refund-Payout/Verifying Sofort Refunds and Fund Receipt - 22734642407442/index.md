---
id: 22734642407442
section_id: 21991136181650
title: "Verifying Sofort Refunds and Fund Receipt"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22734642407442-Verifying-Sofort-Refunds-and-Fund-Receipt"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-01-15T13:35:36Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQT889RQXXSG27BB4ZJ0M"]
label_names: ["case_transactions", "ROW", "case_transactions_issue_refund_proof_apm", "refund_proof_for_sofort", "confirmation_of_received_funds"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

Use this guide when a merchant wants to confirm the receipt of funds from Sofort, usually because a customer has been debited in error or has sent funds in error.

## DESCRIBE THE ISSUE 💬

Merchants may inquire about the status of funds when a customer claims a discrepancy, such as an erroneous debit. This information is verified using the reconciliation banking integrations report and cross-referenced with the relevant payments platform, such as the Sofort portal.

## PROCESS FOR VERIFYING SOFORT TRANSACTIONS 🖊️

Follow these steps to locate specific transactions and verify fund movement using the banking integrations report.Step 1. Access and Filter the Report

- Open the [banking integrations report](https://checkoutinternal.eu.looker.com/explore/bank-integrations/reconciliation_report?qid=9cGMMFYjlnKae6hY5kTDxI&origin_space=1373&toggle=fil,vis)

- 
Filter the report using the following identifiers to locate Sofort transactions:

  - 
_AccountName_ field value: CKO SAS - Sofort – EUR

  - 
_AccountNumber_ field value: 6161644460

- 
To ensure you view a comprehensive end-of-day report without duplicated transactions, filter the Report Type:

  -  _ReportType_ field value: MT940 

Step 2. Locate the Payment Identifier

- Check the `InformationForAccountOwner` field in the report.

- This field contains the identifiers or IBANs required to locate the specific payment.

 

**💡 Note:** Watch for spaces within the `InformationForAccountOwner` data when matching details.
  
 Step 3. Cross-Reference Data

- Match the **Track ID** and **Acquirer Transaction ID** from the internal data with the bank statement.

- 
In Looker, use the Proof of Payment information to confirm receipt on the bank statement.

  - 
 
_Example:_ You can identify if a payment has been refunded back to the customer by looking for the Debit/Credit mark.

### Case Example 1

_BAI=142;YOUR REF=NOTPROVIDED;B/O CUSTOMER=DE57100500001068414355 JAMES OBED K ITSON;PAID TO=CHASDEFXXXX;REC FROM=BELADEBEXXX;REMARK=/REMI/REMITLY COM - A791D5ED3CE9D 2 03145-731305-654CD471-5281/REF/NOTPROVIDED/SCT/_

| Customer's IBAN and name | **B/O CUSTOMER=DE57100500001068414355 JAMES OBED K ITSON**: |
| --- | --- |
| Remittance information with Merchant, Track ID, and Acquirer Transaction ID. | **REMARK=/REMI/****REMITLY COM**** - ****A791D5ED3CE9D**** ****2 03145-731305-654CD471-5281**: |

In the [Sofort portal](http://www.sofort.com/payment/users/login) we can see this payment relates to the below and all relevant details can be matched with _InformationForAccountOwner*_:-

_*** Watch for spaces in InformationForAccountOwner**_

Along with the associated payment in Looker: pay_qkmqyx7s5ccuxgoy6ox46oigpa

****

**Matching Track ID and Acquirer Transaction ID:**

| **Source** | **Track ID** | **Acquirer Transaction ID** |
| --- | --- | --- |
| Bank Statement | A791D5ED3CE9D | 2 03145-731305-654CD471-5281 |
| Looker | a791d5ed3ce9d54876004094679a690f | 203145-731305-654CD471-5281 |

Please note:

- Track IDs may vary in length, and the case might differ between bank statements and CKO's data

- Watch for space between 2 and 0 on the bank statement

- If payment is not in “Captured” state, the Acquirer Transaction ID cannot be used  
 

### Case Example 2

Below is an example of a query to check if we have received funds that have been deducted from a customer account:-  
In Looker, utilise the **Proof of Payment** information to locate and confirm receipt on the bank statement (in this example you can also see the payment has been refunded back to the customer, shown but the Debit Credit mark):- 

## RESOLUTION 🛠️

By following these steps, you should be able to confirm whether funds have been received or if a refund has been processed, allowing you to provide proof to the merchant.Troubleshooting & Key Reminders

- 
 
**Case Sensitivity:** Track IDs may vary in length, and the case (upper/lower) might differ between bank statements and Checkout.com's data.

- 
 
**Formatting discrepancies:** Watch for unexpected spaces, such as a space between digits (e.g., between 2 and 0) on the bank statement.

- 
 
**Payment State:** The Acquirer Transaction ID can **only** be used if the payment is in the "Captured" state.

## FAQs ❓

**Q: What should I do if the Acquirer Transaction ID doesn't work?** A: Ensure the payment status is set to "Captured." If the payment is not in the "Captured" state, the Acquirer Transaction ID cannot be used for matching.**Q: Why do the Track IDs look different on the bank statement?** A: Track IDs can vary in length, and the character case (capitalization) may differ between the bank statement and our internal data. Always check for these variations when searching.
