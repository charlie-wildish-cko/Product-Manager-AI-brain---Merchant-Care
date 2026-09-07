---
id: 28535625363090
section_id: 28530815273106
title: "Account Funding Transactions (AFT) - Canada FAQs"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/28535625363090-Account-Funding-Transactions-AFT-Canada-FAQs"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-09-03T14:27:38Z"
permission_group_id: 26838654181266
content_tag_ids: ["01K1TJH612G6QYB2YGFB63VE4Q"]
label_names: ["AFT", "Canada", "Interac"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

Use this document to understand common questions about setting up and processing Account Funding Transactions (AFTs) specifically within the Canadian market. This guide covers Canadian AFT overview, use cases, technical requirements, and processing specifics in Canada.
INTRODUCTION TO AFT 💬

Account Funding Transactions (AFTs) allow merchants to push funds directly to a customer's debit or credit card. In Canada, this primarily includes Interac e-Transfer Bulk Disbursal. This document provides answers to frequently asked questions regarding the setup, functionality, and processing of AFTs specific to the Canadian market.

GENERAL QUESTIONS 👀

**What are Account Funding Transactions (AFTs)?**

AFTs are a type of payment transaction where funds are sent from a merchant's account directly to a customer's card. This differs from traditional payment transactions where funds are pulled from a customer's card to a merchant's account.

**What is the primary use case for AFTs in Canada?**

In Canada, a primary use case is Interac e-Transfer Bulk Disbursal, a solution that enables large volumes of payments to be sent directly to Canadian bank accounts.

**Are AFTs supported in Canada?**

Yes, AFTs are supported in Canada via Interac , as well as Visa and Mastercard.

**What is Interac AFT?**

Interac AFT refers to the processing of Account Funding Transactions specifically through the Interac network in Canada, typically leveraging Interac e-Transfer Bulk Disbursal for pushing funds directly to Canadian bank accounts.

**What is the difference between an AFT and a refund?**

- An AFT pushes new funds to a card and is not necessarily linked to a previous transaction.

- A refund returns previously captured funds to a card and is always linked to an original payment.

TECHNICAL QUESTIONS 👨🏼‍💻

**What API is used for Canadian AFTs?**

Canadian AFTs are processed using the

**Payments** API. For push payments, the source object in the request should contain type: card and the payment_type should be Account_Funding. The capture field should be true. The transaction is processed as a chargeCaptured event.

**How do I initiate a Canadian AFT?**

To initiate an AFT, you must make a server-to-server request to the

**Payments** API. The request will include the card details, amount, currency, and other relevant transaction information. Set the payment_type field to Account_Funding.

**What specific fields are required for Canadian AFTs via Interac?**

For Interac e-Transfer Bulk Disbursal, additional fields are required for the destination object, such as:

- 
type: email or type: phone_number

- account_holder_name

- 
account_holder_email or account_holder_phone

- sender_name

- 
message (optional)

- 
payment_descriptor (optional)

- 
invoice_number (optional)

**What specific fields are required for Visa AFTs in Canada?**

For Visa AFTs, the requirements vary based on the transaction type (Domestic vs. Cross-Border):

- 
**Domestic Transactions**

  - Recipient Information: Optional

  - Sender Information: Optional

- 
**Cross-Border Transactions**

  - Recipient Information: First Name, Last Name, Account Number¹, Address, City, State², Country

  - Sender Information: First Name, Last Name, Address, Date of birth, City, State², Country

  - Additional Information: Purpose of Payment³ (if sender is from Argentina, Bangladesh, Chile, Colombia, Egypt, India, or Mexico)

¹ Any identifier, such as the first six and last four digits of the PAN, an IBAN, Wallet ID, internal account number, or phone number related to the funded account.

² Required if the Sender or Recipient Country is the USA or Canada.

³ Required if the sender is from Argentina, Bangladesh, Chile, Colombia, Egypt, India, or Mexico.

If the recipient is a Visa-issued card in Australia, New Zealand, or the South Pacific, address.address_line1 must be provided. This field can be omitted if the recipient is an account, such as a digital wallet.

**What specific fields are required for Mastercard AFTs in Canada?**

For Mastercard Funding Transactions, the following information is required for both Domestic and Cross-Border transactions in the Canada acquiring region:

- 
**Recipient Information**: First Name, Last Name, Country, Account Number¹.

- 
**Sender Information**: Optional.

It is recommended to use the PAN, but any identifier related to the account to be funded is allowed. This includes part of the PAN (the first six digits and the last four digits), an IBAN, Wallet ID, an internal account number, or a phone number.

**How are Canadian AFTs identified in my transaction data?**

AFTs will appear as chargeCaptured transactions with payment_type:Account_Funding in your transaction reports and API responses.

PROCESSING & COMPLIANCE QUESTIONS ℹ️

**What are the processing timelines for Canadian AFTs?**

Funds are typically received by the cardholder within minutes (near real-time). It can take up to 30 minutes for the payment to settle, and in some cases, up to 3-5 business days depending on the issuing bank's processing times.

**Can Canadian AFTs be reversed or refunded?**

AFTs can generally be reversed within a short window after the original transaction. Once the funds have been settled, a separate refund or return process may be required by scheme rules.

**Are there transaction limits for Visa AFTs?**

Yes, Visa has transaction limits for AFTs, such as USD 100,000 per day for Domestic Money Transfer and USD 50,000 per day for Cross-Border Money Transfer. Transactions that exceed these limits will be declined.

**Are there transaction limits for Mastercard Funding Transactions?**

Yes, Mastercard has limits for funding transactions, such as a USD 25,000 single transaction limit and a USD 50,000 monthly limit for transfers to a user's own debit or prepaid accounts.

RELATED ⭐️

[Page: Visa and Canada AFT Launch Readiness](https://checkout.atlassian.net/wiki/spaces/PRUB/pages/7222689884/Visa+and+Canada+AFT+Launch+Readiness)
