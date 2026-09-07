---
id: 33733206953874
section_id: 21991160900754
title: "Transaction Reversals 101"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/33733206953874-Transaction-Reversals-101"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-03-03T12:32:36Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQT889RQXXSG27BB4ZJ0M"]
label_names: []
user_segment_ids: [11003606966930]
archive: false
---

**Use this article to**

This article provides the high-level policy for reversing transactions. A **reversal** cancels a transaction at the scheme level (Visa or Mastercard) as if it never occurred.**Refund Reversals vs. Capture Reversals 🔄**

- **Refund Reversal:** Undoes a refund where money was sent back to a cardholder. This is the most common request for Merchant Care.

- **Capture Reversal:** Undoes a capture where money was collected from a customer. This is reserved **only** for internal Checkout.com system errors (e.g., duplicate captures caused by a bug).

**When to Use a Refund Reversal**Merchant Care considers a reversal when a merchant reports an error and needs to stop money from being sent back to a cardholder. Typical scenarios include: 

- Wrong Amount: e.g., refunding 100 EUR instead of 10 EUR.

- Wrong Recipient: Refund sent to the incorrect customer or card ID.

- Duplicate Refund: The same payment was accidentally refunded twice.

- Refund Attack: Bulk fraudulent refunds that must be stopped immediately.

**Eligibility Checklist ✅**

Before starting a reversal, you must verify that the transaction meets **all** the following criteria:

| ** Feature** | ** Visa** | ** Mastercard** |
| --- | --- | --- |
| ** Time Limit** | Up to **30 calendar days** from the refund cleared date. | Within **24 hours** (1 calendar day) of initiation. ⚠️ If the 24-hour window has passed, a reversal is only possible if the issuer explicitly approves it in writing - which has a very low chance of success. |
| ** Required Status** | Must be `CLEARED` in Agent Toolkit or Hermes | Must be `CLEARED` in Agent Toolkit or Hermes |
| ** Exclusions** | **Payouts** (SMS/Visa Direct) cannot be reversed. | **"Moneysend"** MessageTypes cannot be reversed. |
