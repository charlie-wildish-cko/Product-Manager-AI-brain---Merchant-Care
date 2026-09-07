---
id: 23046303747730
section_id: 23045958401426
title: "Mastercard Reject Response Code"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/23046303747730-Mastercard-Reject-Response-Code"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:34:12Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQT889RQXXSG27BB4ZJ0M", "01JYS4X06G4P1FBXP4YZEWJKKH"]
label_names: ["case_transactions", "global", "case_transactions_issue_request_for_information_on_rejects", "visa_and_mastercard_rejects", "0021", "2666", "2667", "2668", "2669", "0011"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

To understand what a Mastercard reject response code means 

## DESCRIBE THE ISSUE** 💬**

This article explains common Mastercard reject response codes that can occur during transaction processing.

 Understanding these codes will help you identify the root cause of a declined or rejected transaction and take the appropriate steps to resolve the issue.

## REJECT CODES** 🔢**

Below is a breakdown of specific Mastercard reject codes, what they mean and how to address them.

| Code | Code Meaning | Details |
| --- | --- | --- |
| 0021 | Recurring Payment Cancellation Service | This error code indicates that a cardholder has requested to stop a recurring payment.  Cardholders sometimes contact their issuing bank to halt recurring payments instead of canceling directly with the merchant. The card issuer then instructs Mastercard to block these transactions. To prevent this error, you should remove the affected cardholder from your subscribers list for any subscription-based Merchant-Initiated Transactions (MITs). |
| 0011 | DE2 Primary Account Number (PAN) Account Range Invalid | This rejection code means that the Bank Identification Number (BIN) of the issuer is no longer active. |
| 2666 | Transaction Blocked for Sender | These codes signify that the transaction was blocked by Mastercard because of sanctions.  The block can be applied to the sender or the receiver. |
| 2667 | Transaction Blocked for Sender |  |
| 2668 | Transaction Blocked for Receiver (due to sanctions at the issuer level) |  |
| 2669 | Transaction Blocked for Receiver |  |
