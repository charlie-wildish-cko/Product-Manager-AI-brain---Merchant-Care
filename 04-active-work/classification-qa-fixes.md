# Classification QA — Fix Hitlist

## Run: 2026-07-07

Source: classification-qa-log.tsv — 107 new rows this run (103 verifiable), 179 total rows in log to date
Ranked by impact — Tier 1 (case type) first, since a case type fix also recovers Issue Type and Reason accuracy for every affected contact. Within a tier, ranked by contacts affected.

### 1. [Tier 1] Account management over-capture (account/config/reset language) — 3 contacts (2.8% of this run's batch)
**Gap type:** ambiguous_boundary
**Pattern:** Account management's Enablement / Account-changes scope is unbounded, so any contact using 'account', 'configuration', 'reset', or 'setup' language is absorbed here even when the real object is a decline on an already-live method, API keys, or integration design. All three were wrongly routed to Account management.
**Recommended fix:** Tighten the Account management (and access) case-type scope to only enable/activate a not-yet-live payment method or change account-level settings. Add exclude_when + disambiguation so that (a) declines/failures of an already-enabled method route to Accepting payments → Transaction status even when 'setup/configuration' is mentioned, (b) API-key issues including keys missing after an account reset route to Technical issue → API keys, and (c) integration-approach/API-capability questions route to Technical issue → API integration. Words like 'account', 'reset', 'configuration', 'setup' must not by themselves pull a contact to Account management.
**Example contacts:** 215561052998551, 215561053088988, 215561053051903 — (full text and raw labels in the TSV)

### 2. [Tier 1] Payouts vs Accepting payments boundary (money-out vs money-in) — 2 contacts (1.9% of this run's batch)
**Gap type:** ambiguous_boundary
**Pattern:** The money-out (Payouts) vs money-in (Accepting payments) boundary is undefined, so generic 'status'/withdrawal/refund language crosses it in both directions — a remittance status query fell into Accepting payments, and a refund request carrying withdrawal/WPID IDs fell into Payouts.
**Recommended fix:** Define the Payouts vs Accepting payments boundary by money direction and explicit merchant framing. Add include_when to Payouts for money-out/remittance status requests naming a remitter/beneficiary or partner/remittance reference, and exclude_when to Accepting payments → Transaction status for money-out status queries. Conversely, when the merchant explicitly frames the request as a refund, classify as Accepting payments → Refunds even if withdrawal/WPID identifiers are present.
**Example contacts:** 215561053519679, 215561052885589 — (full text and raw labels in the TSV)

### 3. [Tier 1] Non-canonical 'Fraud detection' case type emitted — 1 contacts (0.9% of this run's batch)
**Gap type:** invalid_label
**Pattern:** Fin invented a non-canonical Case Type ('Fraud detection'). Fraud is an issue type within Accepting payments, not a standalone top-level Case Type.
**Recommended fix:** Constrain classifier output to the 14 canonical Case Types (never emit 'Fraud detection'). Add a note to Accepting payments that blocked/fraud-flagged transaction investigations belong here via the Fraud & risk controls issue type; this contact maps to Accepting payments → Transaction status → Declined / failed action.
**Example contacts:** 215561052631619 — (full text and raw labels in the TSV)

### 4. [Tier 1] Non-actionable query worded as a payout status request → General — 1 contacts (0.9% of this run's batch)
**Gap type:** ambiguous_boundary
**Pattern:** A non-actionable follow-up/duplicate superficially worded as a payout status query was pulled to Payouts; the General case type has no criteria to reclaim superficially-genuine but unactionable contacts.
**Recommended fix:** Add a disambiguation to the General case type and an exclude_when to Payouts: contacts presenting as withdrawal/payout status queries that are non-actionable, unresolvable, or follow-ups/duplicates route to General → Inquiries → Spam/duplicate/no action, not Payouts.
**Example contacts:** 215561052598028 — (full text and raw labels in the TSV)

### 5. [Tier 1] Per-transaction settlement state → Transaction status (not Settlements) — 1 contacts (0.9% of this run's batch)
**Gap type:** ambiguous_boundary
**Pattern:** The word 'settlement' pulled a single named-transaction settlement-state query into Funds and fees → Settlements; Settlements is not bounded against per-transaction queries.
**Recommended fix:** Add an exclude_when to Funds and fees → Settlements and a disambiguation: merchant-balance settlement/reconciliation stays in Settlements, but the settlement state or outcome of a single named transaction goes to Accepting payments → Transaction status.
**Example contacts:** 215561052758654 — (full text and raw labels in the TSV)

### 6. [Tier 1] Return of merchant's own settled funds → Settlements (not Payouts) — 1 contacts (0.9% of this run's batch)
**Gap type:** ambiguous_boundary
**Pattern:** 'Returns/reversals' language routed a re-release of the merchant's own settled balance to their own bank account into Payouts → Bank payout returns; the payouts-to-recipients vs settlement-of-own-balance distinction was lost.
**Recommended fix:** Strengthen the Payouts scope note and add a disambiguation: returns/re-releases of the merchant's own settled funds to their own bank account are Funds and fees → Settlements; Payouts covers only payouts to end recipients.
**Example contacts:** 215561052831201 — (full text and raw labels in the TSV)

### 7. [Tier 1] Tokenisation-attributed declines → Technical Tokens (not Transaction status) — 1 contacts (0.9% of this run's batch)
**Gap type:** ambiguous_boundary
**Pattern:** The presence of a decline code overrode the tokenisation root-cause signal, routing a network-token / card-on-file configuration query to Transaction status instead of Technical issue → Tokens.
**Recommended fix:** Add a disambiguation to Technical issue → Tokens and an exclude_when to Accepting payments → Transaction status: when the merchant attributes declines to tokenisation / card-on-file / network-token configuration, classify as Technical issue → Tokens even when a decline code is present.
**Example contacts:** 215561052961861 — (full text and raw labels in the TSV)

### 8. [Fin abstention, not a taxonomy gap] Payouts case matched but Fin left Issue Type blank — 4 contacts (3.7% of this run's batch)
**Gap type:** fin_abstention (corrected from invalid_label on 2026-07-07 — see note below)
**Pattern:** Fin correctly matched Case Type (Payouts) on all 4 contacts but left Issue Type blank rather than committing to Card payouts. All 4 had a reachable, correct answer in Zendesk (Card payouts, in 3 different Reasons) — this is a completion/confidence failure in the classifier, not an ambiguous or missing taxonomy definition. No taxonomy or classifier-definitions change will fix this.
**Recommended fix:** Fix at the Fin/classifier configuration level: require Fin to always emit an Issue Type once Case Type is resolved with confidence, applying the documented 'default to Card payouts when the rail is ambiguous' rule instead of abstaining. If Fin's confidence threshold for Issue Type is set higher than for Case Type, lower it or add a fallback default rather than leaving the field null. This also blocks Reason scoring downstream for all 4 contacts — fixing abstention here recovers Issue Type AND Reason accuracy for this cluster.
**Example contacts:** 215561053715242, 215561053324955, 215561051845290, 215561052799516 — (full text and raw labels in the TSV)

**Correction note (2026-07-07):** this cluster was originally logged with `gap_type=invalid_label` and a taxonomy-definition-flavored fix ("codify a default rule"). On review, blank ≠ wrong label — Fin didn't misclassify, it declined to classify. Reclassified as `fin_abstention`. See "What to fix" summary at the bottom of this run's section.

### 9. [Tier 2 (invalid_label_only)] Issue Type left blank by both Fin and agent (field-enforcement gap) — 4 contacts (3.7% of this run's batch)
**Gap type:** invalid_label
**Pattern:** Case type was correct but both Fin and the agent left the Issue Type blank/invalid — a field-enforcement gap rather than a definition boundary, spanning login, account-settings/config, and no-action contacts.
**Recommended fix:** Enforce a non-null Issue Type in both classifier output and the Zendesk agent field. Map the recurring cases: login/password-failure → Account management and access → Login & access → Login error / MFA / SSO; API-key/processing-channel and billing-descriptor configuration → Account management and access → Account changes → Account settings update; contacts with no actionable request → General → Inquiries → Spam/duplicate/no action.
**Example contacts:** 215561052623197, 215561053064854, 215561052904889, 215561053298227 — (full text and raw labels in the TSV)

### 10. [Tier 2] Bank vs Card payouts classified by proof document, not actual rail — 3 contacts (2.8% of this run's batch)
**Gap type:** ambiguous_boundary
**Pattern:** Bank payouts keywords fire on the proof document requested (SWIFT/MT103) or a generic 'bank account number' rather than the actual payout rail, misrouting card payouts to Bank payouts → Proof of bank payout.
**Recommended fix:** Tighten the Bank payouts include_when to require true bank-rail identifiers (IBAN, SWIFT/BIC, MT103, wire reference) and add an exclude_when: classify payouts by the actual payment instrument's rail (pay_/scheme), not by the receipt document the customer requests or a generic 'bank account number'. A SWIFT-receipt request against a card payout stays Card payouts → Proof of card payout.
**Example contacts:** 215561053547131, 215561053137042, 215561052681814 — (full text and raw labels in the TSV)

### 11. [Fin abstention, not a taxonomy gap] Reason left blank despite correct Case Type + Issue Type — 1 contact (0.9% of this run's batch, newly surfaced 2026-07-07)
**Gap type:** fin_abstention
**Pattern:** Contact 215561052778684 — Fin correctly matched both Case Type (Data and analytics) and Issue Type (Reporting) but left Reason blank instead of committing to "Data mismatch / missing." This row was invisible to the original verdict logic: `reason_match` scores `n/a` whenever Fin's Reason field is blank, so a row where Fin is on the exact right branch and simply stops short gets silently treated as "no gap" rather than flagged. Worth checking whether other runs have the same blind spot.
**Recommended fix:** Same as cluster 8 — a classifier/prompt-level completion fix, not a taxonomy fix. Additionally, consider a QA-logic improvement: distinguish `reason_match=n/a (Fin abstained, ground truth exists)` from `reason_match=n/a (no ground truth to check against)` in future runs, since only the first is an actionable signal.
**Example contacts:** 215561052778684 — (full text and raw labels in the TSV)

---

**What to fix, this run — three separate root causes, not one:**

1. **Fin abstention on Issue Type/Reason (clusters 8, 11 — 5 contacts, but the highest-leverage single fix)**: this is a classifier confidence/completion problem, not a taxonomy problem. Fin reaches the correct branch and stops. No amount of editing `support-taxonomy.md` or the classifier definitions will fix this — it requires either lowering Fin's confidence threshold for Issue Type/Reason once Case Type is resolved, or adding an explicit "always commit to the best-fit label, never leave blank" instruction/fallback in the Fin classifier configuration itself. This is an Fin-administration fix (see CLAUDE.md note: "Fin administration is a shared responsibility across Product and Content with no dedicated owner") — flag to whoever owns Fin's classification prompt/confidence config.
2. **Taxonomy definition gaps (clusters 1–7, 10 — 12 contacts)**: genuine ambiguous boundaries or missing disambiguation in `support-taxonomy.md` (Account management over-capture, Payouts vs Accepting payments, Bank vs Card payouts by rail not document type, etc.). These *do* need definition edits — see each cluster's recommended_fix above.
3. **Zendesk agent tagging gaps (cluster 9 — 4 contacts)**: both Fin and the human agent left Issue Type blank. Not fixable via Fin or the taxonomy — this needs Zendesk-side enforcement that agents must populate Issue Type before closing a ticket, otherwise these rows can never be used as ground truth for QA.

10 additional smaller clusters not listed above, covering 12 contacts. See the TSV (gap_type, taxonomy_gap_candidate columns) for the long tail.

---

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
