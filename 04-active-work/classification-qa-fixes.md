# Classification QA — Fix Hitlist

## Run: 2026-07-01

Source: classification-qa-log.tsv — 72 new rows this run (70 verifiable), 72 total rows in log to date
Ranked by impact — Tier 1 (case type) first, since a case type fix also recovers Issue Type and Reason accuracy for every affected contact. Within a tier, ranked by contacts affected.

### 1. [Tier 1] Outbound payout status/action misrouted to Accepting payments — 4 contacts (5.6% of this run's batch)
**Gap type:** ambiguous_boundary
**Pattern:** Card payout requests from remittance/disbursement merchants (TransferGo, ProFee) read as generic transaction status/cancellation enquiries, so Fin routes them to Accepting payments. The Case Type definitions do not disambiguate outbound money movement from inbound transactions.
**Recommended fix:** Add disambiguation to the Payouts Case Type: include_when the transaction is outbound money movement (Push to Card, disbursement, withdrawal, remittance payout) including status confirmation, cancellation, or reversal requests, and reference payout signals (pay_ prefix, Push to Card, disbursement, remittance flow). Add exclude_when to Accepting payments for any outbound/payout status, cancellation, or reversal request.
**Example contacts:** 215561042172722, 215561042266091, 215561044221902, 215561042439306 — (full text and raw labels in the TSV)

### 2. [Tier 1] Funds/settlement enquiries misrouted to Accepting payments on cited payment ID — 3 contacts (4.2% of this run's batch)
**Gap type:** ambiguous_boundary
**Pattern:** Enquiries about settlement/funds status, adjustments, or marketplace escrow releases get routed to Accepting payments (or Settlements) because they cite a payment/pay_ reference or use "release/pending" language. The boundary between transaction-level status and funds/settlement enquiries is undefined when a payment ID is present.
**Recommended fix:** Add disambiguation to the Funds and fees Case Type: include_when the enquiry concerns whether funds have settled/been received, an adjustment (adj_), or fee reconciliation, even when a payment ID is quoted; exclude_when the enquiry concerns a specific transaction/escrow/marketplace release stuck in status (route to Accepting payments). Add exclude_when to Accepting payments for funds-settlement and adjustment lookups; clarify Settlements covers merchant balance settlement only, not individual transaction/escrow releases.
**Example contacts:** 215561042868078, 215561042082374, 215561041265754 — (full text and raw labels in the TSV)

### 3. [Tier 1] Overly broad case types capture no-action/external/spam items — 2 contacts (2.8% of this run's batch)
**Gap type:** wrong_scope
**Pattern:** Actionable-sounding language (refund batch, invoice) triggers a specific Case Type even when the item is a missing-attachment no-action, an external third-party/phishing invoice, or otherwise carries no usable Checkout transaction detail. Accepting payments and Funds and fees scopes are too broad.
**Recommended fix:** Add exclude_when rules routing to General/Inquiries: (a) requests whose actionable content is only in a missing/unreadable attachment with no transaction detail in the body; (b) third-party or external-vendor invoices and suspected phishing forwards. Clarify Billing & fees covers Checkout.com invoices/fees only, and that empty/attachment-only requests default to General.
**Example contacts:** 215561044652842, 215561041755243 — (full text and raw labels in the TSV)

### 4. [Tier 1] Merchant-side checkout ID field misrouted to Identity Verification — 1 contact (1.4% of this run's batch)
**Gap type:** wrong_scope
**Pattern:** A request to remove a national ID input field from the merchant's own checkout integration matched the "national ID" token and routed to Identity Verification. The IDV Case Type scope is too broad and captures any mention of ID fields.
**Recommended fix:** Add an exclude_when to the Identity Verification Case Type: exclude contacts about form/checkout fields in the merchant's own website integration. Disambiguate that IDV covers the Checkout.com IDV product (document checks, facial recognition), not merchant-side data-capture fields, which belong in Technical issue.
**Example contacts:** 215561040834179 — (full text and raw labels in the TSV)

### 5. [Tier 1] Reference-data lookups default to General instead of Data and analytics — 1 contact (1.4% of this run's batch)
**Gap type:** ambiguous_boundary
**Pattern:** A request to confirm MID/CID entity-to-channel mappings is reference-data reporting but fell back to General/Inquiries because no Case Type clearly owns account/processing configuration reference data.
**Recommended fix:** Add disambiguation to the Data and analytics Case Type: include_when the request is for reference/configuration data such as MID, CID, or entity-to-channel mappings. Add an exclude_when to General to prevent reference-data lookups defaulting to Inquiries.
**Example contacts:** 215561040719736 — (full text and raw labels in the TSV)

### 6. [Tier 2] Card vs Bank payout rail misclassified for push-to-card remittance — 5 contacts (6.9% of this run's batch)
**Gap type:** ambiguous_boundary
**Pattern:** Within the correct Payouts Case Type, push-to-card remittance/disbursement payouts (Remitly, MoneyGram, NetBet) are classified as Bank payouts because the merchant uses transfer/deposit/withdrawal language without naming the rail. Applies across status, reversal, and proof-of-payout Issue Types.
**Recommended fix:** Add disambiguation between Bank payouts and Card payouts Issue Types: default remittance/disbursement/gambling-withdrawal flows (Remitly, MoneyGram, NetBet) that use push-to-card to Card payouts. Add signals (transfer #, push-to-card, deposit-to-card, EDD/deposit-date-to-card, withdrawal/stop-payout, proof-of-deposit) to the Card payouts include_when, and map reversals to Card payout reversal and proof requests to Proof of card payout. Clarify Bank payouts (and Bank payout returns / Proof of bank payout) require an explicit bank rail.
**Example contacts:** 215561044110418, 215561044215129, 215561042846792, 215561043149778, 215561041208437 — (full text and raw labels in the TSV)

### 7. [Tier 2] Refunds Issue Type over-captures on the word "refund" — 2 contacts (2.8% of this run's batch)
**Gap type:** ambiguous_boundary
**Pattern:** Within Accepting payments, Fin chooses Refunds whenever "refund" appears, even when the core issue is unexpected transaction/authorization behaviour or the claim is unactionable (cardholder cannot provide a statement). The Refunds vs Transaction status / no-action boundary is ambiguous.
**Recommended fix:** Tighten the Refunds Issue Type: it covers refund execution/status only. Add exclude_when for (a) investigations into why a transaction/authorization behaved unexpectedly or incorrect charge/refund amounts (route to Transaction status), and (b) unactionable/insufficient-evidence refund claims (handle as no-action). Correct taxonomy usage so no-action refund follow-ups map to General / Inquiries / Spam / duplicate / no action, since "Inquiries" does not exist under Accepting payments.
**Example contacts:** 215561043146730, 215561040769485 — (full text and raw labels in the TSV)

### 8. [Tier 3] Proof-of-payment Reason over-captures embedded status enquiries — 2 contacts (2.8% of this run's batch)
**Gap type:** reason_mismatch
**Pattern:** Within Transaction status / Card payouts, Fin selects a proof-of-payment Reason whenever an ARN/proof/receipt is mentioned, even when the primary ask is a stuck void/release timing question or funds-not-received confirmation. Proof vs status/pending Reasons are not disambiguated.
**Recommended fix:** Disambiguate the proof-of-payment Reasons: "Proof of payment (ARN, RNN, bulk)" applies only when the sole ask is a proof/ARN; when the primary issue is a stuck void/release with status/timing questions, use "Stuck in status / status enquiry". For Card payouts, "Proof of card payout" covers funds-not-received / confirm-receipt requests while "stuck in pending or status inquiry" covers still-pending payouts. Add exclude_when to proof Reasons for embedded status enquiries.
**Example contacts:** 215561040821257, 215561042450522 — (full text and raw labels in the TSV)

### 9. [Tier 3] Failure-severity Reasons overstate the failure — 2 contacts (2.8% of this run's batch)
**Gap type:** reason_mismatch
**Pattern:** Fin selects the most severe failure Reason ("Failed but customer charged", "All payments failing") when the evidence supports a milder one. A merchant asking why a payment failed, or reporting a partial spike in failures, does not meet the bar for a confirmed charge or a total outage.
**Recommended fix:** Add severity thresholds: "Failed but customer charged" requires confirmation the customer was charged on a failed payment (else "Declined / failed action" for investigate-why-it-failed); "All payments failing" requires a total/complete failure (100% decline or outage), while a rise in failures or degraded acceptance maps to "Acceptance rate issue / optimisation". Add exclude_when to both severe Reasons for unconfirmed/ambiguous or partial cases.
**Example contacts:** 215561042680853, 215561041259393 — (full text and raw labels in the TSV)

### 10. [Tier 3] Login access-provisioning misread as User permissions — 1 contact (1.4% of this run's batch)
**Gap type:** reason_mismatch
**Pattern:** Within Login & access, an initial system access/provisioning request via an email address is mapped to "User permissions" rather than access provisioning. The two Reasons are not disambiguated between changing an existing user's permissions and provisioning new access.
**Recommended fix:** Add disambiguation to the Login & access Reasons: "User permissions" covers changing roles/scopes of existing users; initial access-request/provisioning/onboarding maps to "Login error / MFA / SSO". Add include_when to "Login error / MFA / SSO" for new-access/onboarding requests.
**Example contacts:** 215561041315151 — (full text and raw labels in the TSV)
