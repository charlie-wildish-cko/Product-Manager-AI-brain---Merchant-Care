# Flow of auto-detecting amount - Half Million recurring setup

**Date:** 2026-09-03
**Attendees:** Asma Hawari (Checkout, solutions), Mawaddah Al Behery (Checkout, commercial), Checkout.com Support. Merchant: Syed Yousuf, Mohammad Almousa, Abdelmegid Elrefaey (Half Million, KSA). Integrator: Amr Allam, Ayman Soliman, A. Hossameldin (Ejada)
**Drive source:** 12_s_h0LcvcAyn0J8zXA1EFuPEOQw8QRXKdZxS5H_crg

## Context

Merchant integration support call with Half Million, a Saudi F&B subscription business, on why enabling recurring payments appeared to break card verification. Captured here because the confusion is a reusable support-content and Fin-procedure candidate.

## Key Points

**The merchant's problem**
- Enabling the recurring-payment option in the API appeared to conflict with card verification (3DS/CVV). With recurring on, verification did not work. With recurring off, verification worked.

**The answer: a CIT/MIT chain**
- First transaction is a Customer Initiated Transaction: 3DS enabled (mandatory in KSA/MEA, all payments must be 3DS), `merchant_initiated: false`, `payment_type: recurring`, full card details plus CVV. Save the returned payment ID (`pay_...`) and the permanent card token.
- Subsequent charges are Merchant Initiated Transactions: `merchant_initiated: true`, `payment_type: recurring`, `previous_payment_id` set to the CIT payment ID (which carries the completed 3DS), permanent card token, amount, currency. No 3DS or OTP needed.
- `recurring` is correct rather than `unscheduled` because intervals are defined: fixed amount every 30 days, quantity-based (e.g. 30 cups over 30 days, up to 2 per day), with manual top-up if the balance is used early.

**Integration boundaries**
- CIT can be done in the Flow SDK. MITs must be backend `/payments` API calls outside Flow. The merchant must build DB storage for the permanent token and previous payment ID per customer.
- Parameters change when the merchant moves platform (transcript garbled: MBGS to NBG).
- MID-level configuration changes are needed for KSA, coordinated by Asma with MDA and the commercial team.
- Sandbox verification before production.

**Commercial context**
- Half Million terminated its contract with the previous vendor and moved to Ejada, the same vendor used by its sister company. Syed declined to give the reason for the termination when asked.

## Insights

- Reusable example of a high-frequency merchant confusion: merchants believe "recurring" and "3DS verification" are mutually exclusive. The real answer is the CIT/MIT chain with `previous_payment_id`. Strong candidate for a support article and a Fin procedure, especially for MEA merchants where 3DS is mandatory on the initial transaction.
- Second recurring theme: the Flow SDK covers only the first transaction. MITs require a backend integration. Merchants integrating via Flow hit this wall and contact support.
- Third: KSA recurring setups need MID-level config changes, so resolution has a commercial and config dependency, not just a developer fix. That makes it a multi-step contact rather than a single deflectable answer.
- Transcript quality is poor in the closing minutes with heavy cross-talk and mangled proper nouns. Vendor and platform names here are unreliable.
