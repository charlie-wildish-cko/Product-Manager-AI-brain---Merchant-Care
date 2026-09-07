---
id: 27693869653010
section_id: 23045958401426
title: "VISA Reject Response Code"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/27693869653010-VISA-Reject-Response-Code"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:34:12Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JYS1V9038NHAQZ1S78P1F2K3"]
label_names: ["visa_and_mastercard_rejects", "c1", "gq", "9e", "d5", "C0", "c2", "d3"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

To understand what a VISA reject response code means 

 

## DESCRIBE THE ISSUE** 💬**

This article explains common VISA reject response codes that can occur during transaction processing.

 Understanding these codes will help you identify the root cause of a declined or rejected transaction and take the appropriate steps to resolve the issue.

 

## REJECT CODES** 🔢**

Below is a breakdown of specific VISA reject codes, what they mean and how to address them.

| Code | Code Meaning | Details |
| --- | --- | --- |
| C0 | Stop This Payment | These error codes appear when a cardholder has asked their issuing bank to stop a payment or all future payments. This is often related to recurring or subscription-based transactions. The cardholder's bank uses the Visa Stop Payment Service (VSPS) to block these transactions. To resolve these errors, you should remove the cardholder from your list of subscribers to prevent future transaction rejections for subscription payments (Merchant Initiated Transactions - MITs). |
| C1 | Stop All Future Payments |  |
| C2 | Stop All Merchants |  |
| GQ | Transaction is blocked for source or destination | This code indicates that the transaction was blocked. This can happen for several reasons, including:  - Attempting an Account Funding Transaction (AFT) to or from certain cross-border countries that do not permit it.  - Transactions involving Russian Bank Identification Numbers (BINs) due to sanctions. |
| 9E | Token to PAN relationship not found | This error typically occurs when a refund is attempted on a tokenized transaction.  VISA's system purges the link between the token and the Primary Account Number (PAN) for refunds on transactions that are over a year old. |
| D5 | Embargoed Country Code | Transaction was stopped because the merchant, issuer, or acquirer country code has been embargoed. This is a result of the card's BIN being blocked at the VISA level due to sanctions. |
| D3 | Transaction Amount Converts to Zero | This rejection happens when converting the transaction amount from the source currency to the settlement currency (like USD) results in a value of zero. -  **Example:** A transaction of 1 Malagasy Ariary (MGA) converts to approximately $0.00023 USD. VISA will reject this transaction because the rounded value is zero. |
