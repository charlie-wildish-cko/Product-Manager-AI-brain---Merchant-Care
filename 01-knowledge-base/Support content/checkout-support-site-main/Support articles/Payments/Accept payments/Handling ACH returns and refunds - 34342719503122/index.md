---
id: 34342719503122
section_id: 14321751128850
title: "Handling ACH returns and refunds"
url: "https://support.checkout.com/hc/en-us/articles/34342719503122-Handling-ACH-returns-and-refunds"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-05-06T13:56:29Z"
permission_group_id: 11003577394706
content_tag_ids: []
label_names: ["Accepting payments - Refunds - Refund reversal"]
user_segment_ids: []
archive: false
---

An [Automated Clearing House (ACH) return](https://www.checkout.com/blog/ach-returns-explained) means the receiving bank, also known as the Receiving Depository Financial Institution (RDFI), could not collect funds from your customer's account. A return can happen for various reasons, for example:

- The customer has insufficient funds in their bank account.
- The customer's bank account is closed or frozen.
- The customer claims they did not authorize the purchase.

A return can still happen after you manually issue a refund for the ACH payment. To avoid double-funding a customer, you must distinguish between two post-refund scenarios:

1. Authorized returns after a refund
2. Disputed returns after a refund

Both of these scenarios have their own time windows in which the original payment can be returned to the customer. Refunding an ACH payment during this return window carries a high risk of financial loss.

## Authorized returns after a refund

These occur when the ACH payment fails after submission (for example, due to insufficient funds or a closed account). Common return codes in this case can be:

- `R01` – Insufficient funds
- `R02` – Account closed
- `R09` – Uncollected funds

The return window for authorized returns is typically up to two banking days after the payment is captured, but some banks may take up to three to five business days.

When you issue a refund (an ACH credit push) within this five-day window:

1. The refund is processed even if the original debit is later returned for insufficient funds, as the account is still open and able to receive credits.
2. If there's a return, Checkout.com updates the payment status to _Returned_. This is the final status for an ACH returned payment. Because of this, your refund request shows as deferred on your Dashboard.
3. Checkout.com gets debited for the refunded amount, and the loss passes to you. You then see two debit entries in your financial action report.

Because of this, we recommend you do not process any refunds during at least the first five days after processing an ACH payment.

For cases where the return code is `R01` (insufficient funds, response code `20051`), consider retrying the payment.

For more information, see our [ACH payment flow and timing](https://www.checkout.com/docs/payments/add-payment-methods/ach-direct-debit/api-only#Payment_flow_and_timing) documentation.

## Disputed returns after a refund

These occur when the customer claims they did not authorize the debit or have revoked authorization, and they contact you for a refund. Common return codes in this case are:

- `R05` – Unauthorized debit to consumer account
- `R07` – Authorization revoked by customer
- `R10` – Customer advises not authorized
- `R11` – Customer advises entry not in accordance with the terms of the authorization
- `R29` – Corporate customer advises not authorized

The return window for unauthorized transactions can be up to 60 calendar days for consumer accounts. For certain dispute cases, the window extends to two years under NACHA (National Automated Clearing House Association) rules.

If you issue a refund within the first three to five business days:

- The customer can still dispute the original debit, leading to the funds being pulled back again.
- You could be double-charged: once for the refund you sent and again for the return.

Because of this, wait for the initial return window to close before refunding.
