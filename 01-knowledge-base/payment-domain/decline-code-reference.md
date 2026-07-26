---
source: "internal — decline_code_mappings.csv (Payments/Acceptance); Checkout.com 'Enhanced API response codes' docs export (enhanced-api-response-codes.pdf) for payout/refund (50xxx) codes and payout-specific notes on 20xxx/30xxx"
source_type: "manual"
last_updated: "2026-07-26"
tags: [payment-domain, decline-codes, payouts, bank-payouts, card-payouts, reference, customer-agent]
desc: "Full per-code decline/response reference covering payins and card/bank payouts: Checkout five-digit codes, plain descriptions, recovery actions, and retry/remediation disposition. The lookup layer beneath debugging-payment-declines.md."
type: reference
emoji: card_index
status: "PROVISIONAL — pending senior L2 + Content review. Items marked [TBC — L2] are unresolved. The 50xxx payout/refund section is sourced from Checkout's public API docs export only (no curated recovery-action source yet) — treat Recovery text there as a first-pass distillation, not reviewed guidance."
---
# Decline & Payout Response Code Reference

Per-code lookup for Checkout.com five-digit response codes, covering **payins and card/bank payouts in one source**. This is the **lookup layer**; the **method layer** (who declined, how to reason, what the record cannot show) is `debugging-payment-declines.md` — currently scoped to payins only. Use them together: read the code range first (method doc §1), then resolve the specific code here.

Scope: this file covers issuer/scheme (`20xxx` / `30xxx`), 3DS (`2015x`), gateway/config (`201xx`) codes — which apply to **both payins and card payouts** (many carry a distinct payout-specific meaning, noted per-code below) — and `50xxx` (**Payout and Refund declines**, Checkout-side pre-flight rejects covering both card and bank payout rails). It does **not** cover `4xxxx` (Checkout risk engine, payin-only) or `INTERNAL*` (Card Processing pre-scheme rejects). Those stay with `debugging-payment-declines.md` Branch A.

> **Provisional.** Payin `20xxx`/`30xxx` dispositions are derived from `decline_code_mappings.csv`, reviewed to the extent marked. The `50xxx` payout/refund section and the payout-specific notes on `20xxx`/`30xxx` codes are derived from `enhanced-api-response-codes.pdf` (Checkout's public API docs) — these carry response-text descriptions only, not a reviewed recovery-action source, so treat every `50xxx` Recovery entry as **[TBC — L2]** unless stated otherwise.

---

## How to use this file

1. **Rail first, then range, then code.** For payouts, establish the rail (bank vs. card) before reading a code — the same numeric code can mean different things depending on rail, and `50401`–`50494` only apply to bank payouts. For payins, establish who declined from the range prefix (method doc §1). Then look the exact code up here.
2. **Two response layers for payouts.** `50xxx` is Checkout declining the payout *before* it reaches the card network or bank (compliance, balance, recipient/sender/instruction validation, bank-account validation). `20xxx`/`30xxx` on a payout means the **recipient's card issuer or network** declined the push-to-card payout after Checkout submitted it — same code range as payin declines, reinterpreted (see per-code notes). `partner_response_code` on the payout response carries the raw scheme/bank code beneath either layer — use it as the ground truth when the summary code is ambiguous.
3. **Precedence for retry — live signal beats static default (payins).** The per-transaction `recommendation_code` (`01`/`02`/`03`) and Mastercard `partner_merchant_advice_code` (MAC) are authoritative. The **Category** column here is a per-code *default*, used only when no live recommendation is on the record. Order: **`recommendation_code` / MAC > Category (this file) > range prefix (coarsest)**. The Category legitimately refines the coarse "`20xxx` = retryable" heuristic (many `20xxx` codes are marked Permanent here), but never overrides a live recommendation.
4. **Recovery actions are merchant-facing and reference Checkout products.** They are the raw material for the customer explanation's "what to do next," not text to paste. Distil to the step the audience controls (see the Customer Agent prompt, Output → Rules).

### Naming collision — read this

The **Category value "Internal/Tech" and "Internal/Dispute" are NOT the same as the `INTERNAL*` response-code prefix.** `INTERNAL*` codes are Card Processing pre-scheme rejects (method doc §1, Branch A). "Internal/Tech" here is a *disposition label* on `20xxx` codes meaning a gateway/technical/reconciliation issue. Do not conflate them.

---

## Category → disposition and escalation

| Category | Meaning | Default handling | Escalation route |
|---|---|---|---|
| Temporary (retry possible) | Retry may succeed | Advisory + retry recommendation | `none` (Branch B), `needs_escalation: false` |
| Permanent (do not retry) | Will not approve on retry | Advisory, do not blind-retry, suggest different card / APM | `none` (Branch B), `needs_escalation: false` |
| Configuration (action needed) | Merchant setup / integration issue | Self-serve: relay the config step the merchant controls (`needs_escalation: false`). Handoff: route `configuration` (`merchant_configuration`) for codes needing a Checkout config / Support action (`20003`, `20102`, `20157`) | **[TBC — L2]** confirm which config codes are self-serve vs. handoff |
| Internal/Tech | Gateway / technical / reconciliation | Not customer-explainable from the code alone | **[TBC — L2]** likely `l2_payment_investigation` (`data_outside_record`); confirm which belong to `l3_card_processing` |
| Internal/Dispute | Dispute-related (`20018`) | Route to dispute handling | Dispute Procedure (see prompt: disputes are a candidate for their own Procedure) |

---

## Recovery action templates

Recurring recovery patterns, factored out so the table stays readable. The table references these by ID.

- **T1 — Temporary technical / infrequent.** Typically a transient technical error; occurs infrequently. Retry later or via Intelligent Acceptance; else prompt for a different card or APM.
- **T2 — Issuer risk assessment.** Issuer flagged the transaction as potentially high-risk. Retry with a different card or via Intelligent Acceptance; offer wallets / local APMs; suggest the cardholder contact their bank. Review risk appetite before widening retries.
- **T3 — Do not retry same card (fee-avoidance).** Issuer will not approve; do not retry the same card (avoids Visa Integrity / gateway fees). Prompt a different card or APM. AMLD5/closed-account variants add specific reasons.
- **T4 — 3DS optimisation.** Use Intelligent Acceptance to apply 3DS exceptions / preferential challenge indicators (`no_preference` default; `challenge_requested` when saving card-on-file or starting a MIT chain; note `no_challenge_requested` gives no liability shift in France). Promote Apple/Google Pay; offer non-3DS APMs; improve auth-message data quality.
- **T5 — Expired / outdated card.** Use Network Tokens or Real-Time Account Updater to refresh card details; prompt the cardholder to review card details; else different card / APM.
- **T6 — Recommendation-code-driven.** Read `recommendation_code`: `01` retry with updated details (RTAU); `02` retry later (funds/limit, via Intelligent Acceptance); `03` do not retry. Use Mastercard MAC where present.

---

## Code table

Sorted by code. "Recovery" gives a template ID or a short distillation. Blank source recovery is marked "—".

### `20xxx` — issuer / scheme (soft-range prefix)

| Code | Description | Category | Recovery | Notes |
|---|---|---|---|---|
| 20001 | Refer to card issuer | Temporary | T2 | |
| 20002 | Refer to card issuer - special conditions | Temporary | T2 | |
| 20003 | Invalid merchant or service provider | Configuration | Verify MID / MCC / acquirer config; open a Support request if a config mismatch is suspected | Support/config handoff |
| 20005 | Declined - Do not honour | Configuration | Review fraud rates (>35 bps is high); review recommendation codes; improve auth-message data quality; issuer outreach via Support/AM | Catch-all soft decline per method doc; retryable. **Payout:** recipient's card issuer declined the payout; if systemic for a recipient BIN, escalate to AM/Support |
| 20006 | Error / Invalid request parameters | Temporary | Prompt cardholder to review card details and retry; else different card / APM | |
| 20009 | Request in progress | Temporary | T1 | |
| 20010 | Partial value approved | Temporary | T1 | |
| 20012 | Invalid transaction | Permanent | T3 | |
| 20013 | Invalid value/amount | Temporary | Issuer restriction (e.g. daily limit); different card / APM; cardholder to review or reset limit | |
| 20014 | Invalid account number (no such number) | Permanent | Different card / APM; issuer outreach if repeated from same issuer | |
| 20017 | Customer cancellation | Permanent | Subscription-renewal context; RTAU to refresh details; else contact user | |
| 20018 | Customer dispute | Internal/Dispute | — | Route to dispute handling |
| 20019 | Re-enter transaction | Temporary | T1 | **[TBC — L2]** code 20019 has two source descriptions ("Re-enter transaction" / "Transaction has expired"); confirm which is authoritative |
| 20020 | Invalid response | Configuration | TPA MID config: confirm 3DS-mandatory rationale; check BIN blacklist; credit-only BIN routing; offer local APMs (BenefitPay/KNET/QPAY) | TPA-linked; see method doc Branch D |
| 20021 | No action taken (unable to back out prior transaction) | Temporary | T1 | |
| 20022 | Suspected malfunction | Temporary | T1 | |
| 20023 | Unacceptable transaction fee | Temporary | T1 | |
| 20024 | File update not supported by the receiver | Temporary | T1 | |
| 20025 | Unable to locate record on file | Temporary | T1 | **[TBC — L2]** 20025 has two source descriptions ("Unable to locate record" / "Account number missing from inquiry") |
| 20026 | Duplicate file update record | Temporary | T1 | |
| 20027 | File update field edit error | Temporary | T1 | |
| 20028 | File is temporarily unavailable | Temporary | T1 | |
| 20029 | File update not successful | Temporary | T1 | |
| 20030 | Format error | Temporary | Incorrectly formatted data; review special characters in form fields; retry / Intelligent Acceptance | |
| 20031 | Bank not supported by Switch | Temporary | T1 | |
| 20032 | Completed partially | Temporary | T1 | |
| 20033 | Previous scheme transaction ID invalid | Internal/Tech | — | |
| 20038 | Allowable PIN tries exceeded | Temporary | Input error / possible fraud; retry later / IA; different card / APM | |
| 20039 | No credit account | Temporary | T1 | |
| 20040 | Requested function not supported | Temporary | T1 | |
| 20042 | No universal value/amount | Temporary | T1 | |
| 20044 | No investment account | Temporary | T1 | |
| 20046 | Bank decline | Temporary | T1 | |
| 20051 | Insufficient funds | Temporary | MIT: align charge date to paydays / banking hours; IA or Dunning retry. CIT: local APMs. Falls under Visa System Integrity Monitoring Cat 2 (excessive manual retries raise fees); consider partial auth | Retry timing via `recommendation_code` / MAC |
| 20052 | No current (checking) account | Temporary | T1 | |
| 20053 | No savings account | Temporary | T1 | |
| 20054 | Expired card | Temporary | T5 | `30033` is the hard "Pick up" variant |
| 20055 | Incorrect PIN / PIN validation not possible | Temporary | T5 | |
| 20056 | No card record | Configuration | Carte Bancaire context; IA to retry over Visa/MC rails; else different card / APM | |
| 20057 | Transaction not permitted to cardholder | **[TBC — L2]** | Review cardholder comms; if AFT, IA downgrade / routing optimisation | **CONFLICT:** source lists 20057 twice, as Permanent ("not permitted to cardholder") and Temporary ("domestic debit not allowed, regional use only"). Resolve which disposition applies, or split into distinct sub-cases. **Payout:** recipient card issuer declined, likely a restricted recipient BIN — request an alternative payout method from the recipient; escalate to AM/Support if systemic for a BIN |
| 20058 | Transaction not permitted to terminal | Temporary | T1 | |
| 20059 | Suspected fraud | Temporary | Monitor issuer fraud rates (>35 bps high); Fraud Detection Pro; Network Tokens; IA + optimise 3DS for CIT; improve auth-message data; review recommendation codes; MIT 3RI / restart chain with challenge | **Source note corrected:** original text referenced "20051" for the Visa SIM Cat 2 caveat; that caveat belongs to 20051/20059 fraud handling, not a different code |
| 20060 | Card acceptor contact acquirer | Permanent | — | |
| 20061 | Activity amount limit exceeded | Temporary | — | **Payout:** recipient card's velocity limit exceeded; retry the payout the following day |
| 20062 | Restricted card | Temporary | — | |
| 20063 | Security violation | Temporary | — | |
| 20064 | Transaction does not fulfil AML requirement | Temporary | — | **[TBC — L2]** Temporary disposition on an AML failure looks wrong; verify |
| 20065 | Exceeds Withdrawal Frequency Limit | Temporary | — | Velocity limit, not SCA (per method doc). **Payout:** same as `20061` — recipient card velocity limit; retry the payout the following day |
| 20066 | Card acceptor call acquirer security | Permanent | — | |
| 20067 | Hard capture - Pick up card at ATM | Permanent | — | |
| 20068 | Response received too late / Timeout | Temporary | — | **[TBC — L2]** 20068 has two descriptions ("Timeout" / "Internal error") |
| 20075 | Allowable PIN-entry tries exceeded | Temporary | — | |
| 20078 | Blocked at first use (new/replacement card not unblocked) | Temporary | T1 | |
| 20082 | No security model / PIN cryptographic error / negative CAM, dCVV, iCVV, CVV | Temporary | — | **[TBC — L2]** 20082 has three source descriptions; confirm whether one code or a collision |
| 20083 | No accounts | Temporary | — | |
| 20084 | No PBF | Internal/Tech | — | |
| 20085 | PBF update error | Internal/Tech | — | |
| 20086 | ATM malfunction / Invalid authorization type | Temporary | — | **[TBC — L2]** 20086 has two descriptions |
| 20087 | Bad track data (invalid CVV and/or expiry date) | Temporary | — | |
| 20088 | Unable to dispense / process | Temporary | — | |
| 20089 | Administration error | Temporary | — | |
| 20090 | Cut-off in progress | Temporary | — | |
| 20091 | Issuer unavailable or switch is inoperative | Temporary | — | **Payout:** issuer's host system may be down, or connectivity was lost; retry the payout once resolved |
| 20092 | Destination cannot be found for routing | Temporary | — | |
| 20093 | Transaction cannot be completed; violation of law | Permanent | — | |
| 20094 | Duplicate transmission / invoice | Temporary | — | |
| 20095 | Reconcile error | Internal/Tech | — | |
| 20096 | System malfunction | Temporary | — | |
| 20097 | Reconciliation totals reset | Internal/Tech | — | |
| 20098 | MAC error | Internal/Tech | — | |
| 20099 | Other / Unidentified responses | Temporary | — | |
| 20100 | Invalid expiry date format | Temporary | — | |
| 20103 | Card type / payment method not supported | Temporary | — | |
| 20104 | Gateway reject - Invalid transaction | Temporary | — | |
| 20105 | Gateway reject - Violation | Temporary | — | |
| 20107 | Billing address is missing | Temporary | — | |
| 20108 | Declined - Updated cardholder available | Temporary | — | RTAU cue |
| 20118 | Transaction pending | Temporary | — | |
| 20123 | Missing basic data: zip, addr, member | Temporary | — | |
| 20124 | Missing CVV value (required for ecommerce) | Temporary | Prompt for CVV and retry; ensure CVV collection enabled; AM/Support for config | |
| 20193 | Invalid country code | Temporary | — | |

### `2015x` — 3DS / authentication (method doc Branch C)

| Code | Description | Category | Recovery | Notes |
|---|---|---|---|---|
| 20150 | Card not 3D Secure (3DS) enabled | Configuration | IA to decide 3DS vs non-3DS; ensure `n3DS` in payload for non-3DS attempts | |
| 20151 | Cardholder failed 3DS authentication | Configuration | T4 | |
| 20152 | Initial 3DS transaction not completed within 15 minutes | Configuration | T4 | |
| 20153 | 3DS system malfunction | Temporary | Monitor 3DS ACS status; coordinate with Support if persistent | |
| 20154 | 3DS authentication required | Configuration | T4 | The real SCA step-up code (method doc); `43401` is the risk-layer variant |
| 20155 | 3DS authentication service provided invalid authentication result | Configuration | — | |
| 20156 | Requested function not supported by the acquirer | Configuration | — | |

### `201xx` — gateway / token / config

| Code | Description | Category | Recovery | Notes |
|---|---|---|---|---|
| 20101 | No Account / No Customer (token incorrect or invalid) | Configuration | — | |
| 20102 | Invalid merchant / wallet ID | Configuration | — | Support/config handoff |
| 20106 | Unsupported currency | Configuration | — | |
| 20109 | Transaction already reversed / repeat-reversal inconsistent / capture larger than authorised | Internal/Tech | — | **[TBC — L2]** 20109 has three source descriptions |
| 20110 | Authorization completed | Internal/Tech | — | |
| 20111 | Transaction already reversed | Internal/Tech | — | |
| 20112 | Merchant not Mastercard SecureCode enabled | Configuration | Enable enhanced auth; IA exceptions/challenge indicators; DAF for high card-on-file volume; promote wallets; non-3DS APMs; non-SCA entity for cross-border (cost caveat) | |
| 20113 | Invalid property | Configuration | — | |
| 20114 | Token is incorrect | Configuration | — | |
| 20115 | Missing / Invalid lifetime | Configuration | — | |
| 20116 | Invalid encoding | Configuration | — | |
| 20117 | Invalid API version | Configuration | — | |
| 20119 | Invalid batch data and/or batch data is missing | Configuration | — | |
| 20120 | Invalid customer/user | Configuration | — | |
| 20121 | Transaction limit for merchant/terminal exceeded | Configuration | — | |
| 20122 | Mastercard installments not supported | Permanent | — | |
| 20157 | Invalid merchant configurations - Contact Support | Configuration | — | Support/config handoff |
| 20158 | Refund validity period has expired | Permanent | — | |
| 20179 | Lifecycle | Temporary | T6 | Recommendation-code-driven |
| 20182 | Policy | Temporary | T6 | Recommendation-code-driven |
| 20183 | Security | Temporary | T6 + Fraud Detection Pro / Network Tokens | Recommendation-code-driven |

### Sub-coded values (`200xx` letter forms)

| Code | Description | Category | Recovery | Notes |
|---|---|---|---|---|
| 2005C | Transaction not supported / blocked by issuer | Temporary | Issuer temporarily unable to approve (credit-risk / velocity / account-level limits); IA to retry at optimal time | Root cause confirmable only by issuer |
| 2006P | Cardholder ID verification failed | Temporary | — | |
| 200N0 | Force STIP | Internal/Tech | — | |
| 200N7 | Decline for CVV2 failure | Temporary | — | CVV result itself not in Payment Search record (method doc §4) |
| 200O5 | PIN required | Temporary | — | |
| 200P1 | Over daily limit | Temporary | — | |
| 200P9 | Limit exceeded. Enter a lesser value. | Temporary | — | |
| 200R1 | Issuer stop payment (this authorization) | Permanent | — | |
| 200R3 | Issuer stop payment (all authorizations) | Permanent | — | |
| 200S4 | PTLF full | Internal/Tech | — | |
| 200T2 | Invalid transaction date | Temporary | — | |
| 200T3 | Card not supported | Temporary | — | |
| 200T5 | CAF status = 0 or 9 | Internal/Tech | — | |

### `30xxx` — issuer / scheme hard-range ("Pick up" family)

All T2 recovery unless noted. Category is Permanent (do not retry) across the block.

| Code | Description | Category | Recovery | Notes |
|---|---|---|---|---|
| 30004 | Pick up card (No fraud) | Permanent | T2 | |
| 30007 | Pick up card - Special conditions | Permanent | T2 | |
| 30015 | No such issuer | Permanent | T2 | **Payout:** recipient card number is incorrect, invalid, or restricted; request an alternative payout method from the recipient, or ask them to contact their issuer; escalate to Checkout if systemic for a recipient BIN |
| 30016 | Issuer does not allow online gambling payout | Permanent | T2 | Payout-specific code (card payout) |
| 30017 | Issuer does not allow original credit transaction | Permanent | T2 | Payout-specific code (card payout / OCT) |
| 30018 | Issuer does not allow money transfer payout | Permanent | T2 | Payout-specific code (card payout) |
| 30019 | Issuer does not allow non-money transfer payout | Permanent | T2 | Payout-specific code (card payout) |
| 30020 | Invalid amount | Permanent | T2 | |
| 30021 | Total amount limit reached | Permanent | T2 | |
| 30022 | Total transaction count limit reached | Permanent | T2 | |
| 30033 | Expired card - Pick up | Permanent | T2 | Hard variant of `20054` |
| 30034 | Suspected fraud - Pick up | Permanent | T2 | **Payout:** issuer declined for suspected fraud; do not reattempt the payout — ask the recipient to contact their issuer |
| 30035 | Contact acquirer - Pick up | Permanent | T2 | |
| 30036 | Restricted card - Pick up | Permanent | T2 | |
| 30037 | Call acquirer security - Pick up | Permanent | T2 | |
| 30038 | Allowable PIN tries exceeded - Pick up | Permanent | T2 | |
| 30041 | Lost card - Pick up | Permanent | T2 | |
| 30043 | Stolen card - Pick up | Permanent | Do not retry one-off; for recurring, RTAU or contact user to update | |
| 30044 | Transaction rejected - AMLD5 | Permanent | T3 (anonymous non-reloadable prepaid > 50 EUR) | |
| 30045 | Invalid payout fund transfer type | Permanent | T3 | Payout-specific code: the fund transfer type is not in the issuer's list of allowed types for this configuration |
| 30046 | Closed account | Permanent | T3 + RTAU / Network Tokens | |

---

## `50xxx` — Payout and Refund declines (Checkout pre-flight)

`50xxx` means **Checkout.com declined the payout or refund request before it reached the card network or bank** — distinct from `20xxx`/`30xxx` above, which is the recipient's card issuer or network declining a payout Checkout already submitted. `50401`–`50494` apply to **bank payouts only** (beneficiary bank-account validation); the rest apply to both card and bank payouts unless noted. `50003` also applies to refunds.

> **Source caveat.** These codes and response texts come from `enhanced-api-response-codes.pdf` (Checkout's public API docs), which gives a code and a short response label but not curated recovery guidance. The Category and Recovery columns below are a first-pass distillation from the response text alone — **[TBC — L2]** applies to every row in this section until Payments/Payouts confirms disposition and merchant-facing recovery steps.

### Payout Category → disposition (draft)

| Category | Meaning | Default handling |
|---|---|---|
| Compliance/Risk | Sanctions, barred beneficiary, compliance hold | Not self-serve — needs compliance/RFI review, not a merchant retry |
| Balance | Sub-account has insufficient available balance to fund the payout | Merchant must top up or wait for balance; not a Checkout-side fault |
| Recipient/sender detail | Recipient or sender account/bank details invalid, missing, or unsupported | Merchant corrects the beneficiary/bank details and resubmits |
| Limit | Amount, velocity, or frequency limit exceeded | Merchant reduces amount, waits for the limit window to reset, or requests a limit increase |
| Configuration | Checkout-side setup/config issue | Support/config handoff |
| Returned / unknown | Payout was returned after being sent, or reason is unmapped | Data-outside-record investigation — same handling as Internal/Tech in the payin table |

### `500xx` — Compliance, balance, recipient/sender validation

| Code | Description | Category | Recovery | Notes |
|---|---|---|---|---|
| 50001 | Compliance error | Compliance/Risk | **[TBC — L2]** — likely needs compliance team review | |
| 50002 | Sanction screening failure | Compliance/Risk | **[TBC — L2]** — sanctions screening hit or data corruption; not merchant-actionable from the code alone | |
| 50003 | Balance reservation insufficient funds | Balance | Merchant tops up the sub-account or waits for available balance | Also applies to refunds |
| 50005 | Barred Beneficiary Error | Compliance/Risk | **[TBC — L2]** | |
| 50020 | Recipient error | Recipient/sender detail | **[TBC — L2]** — generic; check for a more specific code (`50021`–`50030`) on the same payout | |
| 50021 | Invalid recipient error | Recipient/sender detail | Merchant verifies and corrects recipient details, then resubmits | |
| 50022 | Unsupported recipient error | Recipient/sender detail | Merchant checks recipient eligibility for this payout method/rail | |
| 50023 | Recipient limit error | Limit | Recipient-side limit exceeded; check `50101`–`50106` for the specific limit type | |
| 50025 | Invalid Recipient Account Error | Recipient/sender detail | Merchant verifies and corrects the recipient's account details | |
| 50026 | Recipient Account Not Found | Recipient/sender detail | Merchant verifies the recipient account exists and details are correct | |
| 50027 | Recipient Bank Error | Recipient/sender detail | **[TBC — L2]** — likely a bank-side issue on the recipient's bank; not merchant-fixable without more detail | |
| 50030 | Invalid Recipient Details Error | Recipient/sender detail | Merchant verifies and corrects recipient details, then resubmits | |
| 50070 | Sender error | Recipient/sender detail | **[TBC — L2]** — sender-side (merchant's own account) issue; needs investigation | |

### `501xx` — Instruction and velocity limits

| Code | Description | Category | Recovery | Notes |
|---|---|---|---|---|
| 50100 | Instruction error | Limit | **[TBC — L2]** | |
| 50101 | Instruction amount limit error | Limit | Merchant reduces the payout amount or requests a limit increase | |
| 50102 | Instruction amount limit sender error | Limit | Sender-side (merchant) amount limit; reduce amount or request increase | |
| 50103 | Instruction amount limit recipient error | Limit | Recipient-side amount limit; reduce amount or use an alternative recipient method | |
| 50104 | Velocity limit | Limit | Retry after the velocity window resets (typically next day) | |
| 50105 | Velocity limit sender error | Limit | Sender-side velocity limit; retry after the window resets | |
| 50106 | Velocity limit recipient limit error | Limit | Recipient-side velocity limit; retry after the window resets | |

### `502xx`–`503xx` — Processing, validation, config, returns

| Code | Description | Category | Recovery | Notes |
|---|---|---|---|---|
| 50150 | Processing error | Configuration | **[TBC — L2]** | |
| 50180 | Validation error | Recipient/sender detail | **[TBC — L2]** — generic validation failure; check payout payload against API reference | |
| 50200 | Configuration error | Configuration | Support/config handoff | |
| 50240 | Cancellation error | Configuration | **[TBC — L2]** — error cancelling the payout, not a decline of the payout itself | |
| 50260 | Returned error | Returned / unknown | Data-outside-record investigation — the payout was returned after being sent; check `partner_response_code` for the underlying reason | |
| 50280 | Insufficient funds | Balance | Merchant tops up the sub-account or waits for available balance | |
| 50399 | Unmapped response | Returned / unknown | Data-outside-record investigation | |

### `504xx` — Bank account / beneficiary validation (bank payouts only)

| Code | Description | Category | Recovery | Notes |
|---|---|---|---|---|
| 50401 | Bank details invalid | Recipient/sender detail | Merchant verifies and corrects the recipient's bank details | |
| 50402 | Account not found | Recipient/sender detail | Merchant verifies the account number and bank | |
| 50403 | Account inactive | Recipient/sender detail | Recipient must reactivate the account, or merchant uses an alternative account | |
| 50404 | Account dormant | Recipient/sender detail | Recipient must reactivate the account, or merchant uses an alternative account | |
| 50405 | Account number invalid | Recipient/sender detail | Merchant verifies and corrects the account number | |
| 50406 | Branch not found | Recipient/sender detail | Merchant verifies the branch code/details | |
| 50407 | Branch code invalid | Recipient/sender detail | Merchant verifies and corrects the branch code | |
| 50408 | Branch code required | Recipient/sender detail | Merchant supplies the missing branch code | |
| 50409 | Bank code invalid | Recipient/sender detail | Merchant verifies and corrects the bank code | |
| 50410 | Bank code required | Recipient/sender detail | Merchant supplies the missing bank code | |
| 50441 | Account type required | Recipient/sender detail | Merchant supplies the missing account type | |
| 50451 | Account holder details invalid | Recipient/sender detail | Merchant verifies and corrects account holder details | |
| 50452 | Account holder identification number required | Recipient/sender detail | Merchant supplies the missing ID number | |
| 50453 | Account holder type not supported | Recipient/sender detail | Merchant checks whether this account holder type is eligible for the rail/corridor | |
| 50454 | Account holder type not allowed | Recipient/sender detail | Merchant checks whether this account holder type is eligible for the rail/corridor | |
| 50466 | Account closed | Recipient/sender detail | Merchant obtains an alternative account from the recipient | |
| 50471 | Account blocked | Recipient/sender detail | Recipient must resolve the block with their bank, or merchant uses an alternative account | |
| 50481 | Invalid debtor account type | Recipient/sender detail | **[TBC — L2]** — sender-side (merchant's) account type issue | |
| 50490 | Duplicate Payment | Recipient/sender detail | **[TBC — L2]** — check whether the payout was already sent before resubmitting | |
| 50491 | Account holder billing address details incorrect | Recipient/sender detail | Merchant verifies and corrects the billing address | |
| 50492 | Account holder billing address details required | Recipient/sender detail | Merchant supplies the missing billing address | |
| 50494 | Account holder billing address can not be PO box | Recipient/sender detail | Merchant supplies a non-PO-box address | |

### `50499`, `505xx` — Returns, amount/limit errors, unknown

| Code | Description | Category | Recovery | Notes |
|---|---|---|---|---|
| 50499 | Payout Returned | Returned / unknown | Data-outside-record investigation — funds were sent then returned by the bank; check `partner_response_code` for the bank's underlying reason | This is the "returned by the banking partner" case — Checkout normalises the bank's own return reason into this code plus `partner_response_code`, rather than exposing raw SEPA/NACHA-style codes |
| 50501 | Unsupported characters | Recipient/sender detail | Merchant removes unsupported characters from the payout payload and resubmits | |
| 50511 | Invalid amount | Recipient/sender detail | Merchant corrects the payout amount | |
| 50512 | Minimum amount not met | Limit | Merchant increases the payout amount to meet the minimum | |
| 50513 | Exceeded transaction value | Limit | Merchant reduces the payout amount or requests a limit increase | |
| 50514 | Exceeded daily limit | Limit | Merchant waits for the daily window to reset or requests a limit increase | |
| 50515 | Exceeded weekly limit | Limit | Merchant waits for the weekly window to reset or requests a limit increase | |
| 50517 | Exceeded monthly limit | Limit | Merchant waits for the monthly window to reset or requests a limit increase | |
| 50531 | Recalled | Returned / unknown | **[TBC — L2]** — payout was recalled; confirm who initiated the recall and whether funds return automatically | |
| 50599 | Unknown reason | Returned / unknown | Data-outside-record investigation | |

### Raw response code (`partner_response_code`)

For card payouts, Checkout also returns the underlying scheme/issuer response code in `partner_response_code`, alongside the summary `response_code` (`20xxx`/`30xxx`/`50xxx`). Values differ per scheme and are not stable — use scheme-specific documentation to interpret a raw code, and treat it as the ground-truth layer when the summary code alone doesn't explain the decline.

---

## Open items for L2 / Content review

1. **Duplicate codes** with multiple source descriptions: `20019`, `20025`, `20068`, `20082` (×3), `20086`, `20109` (×3). Confirm one authoritative description each, or document the sub-case split.
2. **Category conflict:** `20057` is listed both Permanent and Temporary. Resolve or split.
3. **Disposition sanity checks:** `20064` (AML failure marked Temporary) and any Permanent code marked with a retry-style recovery.
4. **Escalation routing:** `configuration` route (reason `merchant_configuration`) added to the prompt's contract 2026-07-23. All escalations go to a support agent; the route is a classification, not a team destination. Still to confirm: which Configuration codes are self-serve vs. handoff, and which route best fits "Internal/Tech" codes (`l2_payment_investigation` vs `l3_card_processing`).
5. **Source recovery text** was distilled into templates T1–T6; verify no material guidance was lost in factoring.
6. **`50xxx` section has no reviewed recovery-action source.** Every row was distilled directly from `enhanced-api-response-codes.pdf` response-text labels, not a curated CSV like the payin codes. Needs a Payments/Payouts-team pass to confirm Category, actual recovery steps, and escalation routing — same treatment the payin table already had.
7. **Payout Category framework is new and unvalidated** (Compliance/Risk, Balance, Recipient/sender detail, Limit, Configuration, Returned/unknown). Confirm this maps cleanly to how Payouts/Support actually triage, or whether it should mirror the payin Category set instead.
8. **`50xxx` codes not yet confirmed against a live payout response** — the PDF gives no worked example for `50xxx` the way it does for `20051` (raw code example). Confirm `partner_response_code` is actually populated on payout responses/webhooks for card payouts, and get one real example.
9. **Bank-payout-specific codes (`50401`–`50494`) not cross-checked against real bank-return scenarios** — confirm whether the banking partner's own return reason ever surfaces separately (e.g. via `partner_response_code`) or is always folded fully into one of these Checkout codes.
