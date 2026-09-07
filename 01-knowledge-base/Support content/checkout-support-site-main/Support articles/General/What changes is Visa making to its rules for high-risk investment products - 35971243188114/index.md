---
id: 35971243188114
section_id: 16340605590546
title: "What changes is Visa making to its rules for high-risk investment products?"
url: "https://support.checkout.com/hc/en-us/articles/35971243188114-What-changes-is-Visa-making-to-its-rules-for-high-risk-investment-products"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-06-03T10:49:33Z"
permission_group_id: 11003577394706
content_tag_ids: ["01KSSVY39WVZC4KMH11A33K1K6"]
label_names: ["Accepting payments - Transaction status (non 3DS & refunds) - Stuck in status / status enquiry"]
user_segment_ids: []
archive: false
---

Visa plans to place high-risk investment products under the scope of its Business Application Indicator (BAI) for liquid and cryptocurrency assets from October 18, 2026. After this date, the BAI will also cover the following product types. 

- Contracts for differences (CFDs)
- Binary options
- Rolling spot foreign exchange (forex) trading
- Financial spread betting (prediction markets)
- Cryptocurrency options trading
- Initial coin offerings (ICOs)

Visa considers these products to fall under the scope of High Integrity Risk Financial Trading, which carry additional processing requirements.

## What do merchants offering these products need to do?

### Switch to Account Funding Transactions from purchase

If you offer these products, you'll need to start processing them as [Account Funding Transactions](https://www.checkout.com/docs/payments/manage-payments/perform-an-account-funding-transaction) (AFTs), instead of purchase transactions. 

AFTs offer richer transaction data than purchase, including information about the recipients and senders of funds. Our [docs](https://www.checkout.com/docs/payments/manage-payments/perform-an-account-funding-transaction) outline the API fields needed to flag transactions as AFTs, and what information is required for domestic and cross-border transactions in each region.

**Note:** Before you can switch to AFTs, we'll need to register your business. Speak to your Account Manager or [contact support](https://dashboard.checkout.com/support) for help with registration. 

You can continue to use Original Credit Transactions (Card Payouts) for the payout of proceeds from investments and trading.

### Register under the Visa Integrity Risk Program

Checkout.com will also need to register you under the Visa Integrity Risk Program (VIRP) before October 18. This is Visa’s compliance framework designed to prevent illegal and brand-damaging activity on the Visa network.

As part of the registration, your Checkout.com team may need to contact you for information about your business. We’re here to work with you to make registration as simple as possible, and if you have any questions, please don’t hesitate to contact us.

Note that registration under VIRP includes a $950 application fee and an annual $950 renewal fee. We will pass these fees through to your business under our Interchange++ pricing.

## Frequently Asked Questions

**Why is Visa making these changes?**

Visa believes that the products in scope involve elevated regulatory and market conduct risks and require added due diligence. By making these changes, Visa will standardize how funds move into trading accounts, ensuring that senders and recipients are clearly identified.

**What happens if I don’t switch to AFTs and register under the VIRP before October 18?**

If you don’t switch to AFTs and register under the VIRP by the deadline, you may see increased decline rates by issuers and non-compliance fines from Visa. Rest assured that we will work with you to ensure you’re ready.

**Does the mandate apply globally?**

Yes. This is a global mandate affecting all Visa regions.

**What is an Account Funding Transaction (AFT)?**

An AFT is a transaction type that identifies when a merchant pulls funds from a cardholder’s account to fund a non-merchant account, such as a trading account or cryptocurrency wallet. AFTs require more data fields, such as information about the sender and the transfer’s purpose.

You can find out more about processing AFTs in our [documentation](https://www.checkout.com/docs/payments/manage-payments/perform-an-account-funding-transaction).

**How do I register for the Visa Integrity Risk Program and AFT processing?**

Checkout.com will handle your onboarding, and we’ll be in touch if we need any documentation from you as part of the registration process.

**Will there be any impact on my payment processing costs?**

AFTs may have different interchange fee structures than purchase transactions. In some regions they are cheaper, but in others, they may be more expensive. We recommend speaking to your Account Manager or support team to understand how switching to AFTs may affect your costs.

**Will switching to AFTs affect my authorization rates?**

We’ll work with you to monitor your authorization rates following your switch to AFTs. Should we see a significant decrease we will work proactively with the schemes and issuers to address this.

**Does Mastercard have a similar mandate in place?**

Mastercard already mandates AFTs for all transactions processed under MCC 6211 (Securities) in the United States and Canada. By March 31, 2027, all merchants processing under MCC 6211 must switch to processing AFTs in the UK, Europe, and MENA regions.
