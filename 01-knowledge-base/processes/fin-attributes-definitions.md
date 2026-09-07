# Fin Attributes — Classification Definitions

Ready-to-paste attribute value descriptions for Intercom Fin Attributes, mirroring the canonical taxonomy in [`support-taxonomy.md`](support-taxonomy.md). Structure is 3-level parent-child: **Case Type** (top-level attribute) → **Issue Type** (child attribute, scoped within its Case Type) → **Reason** (grandchild attribute, scoped within its Issue Type).

**Do not edit `support-taxonomy.md`'s structure to match this file.** That document uses a different markdown structure that the `/taxonomy-classification-qa` skill parses directly to build its valid-pairs set — this file is a separate, purpose-built handoff for whoever administers Fin Attributes in Intercom. When the taxonomy changes, update both files. Every "Key distinction," parenthetical example, and edge case from `support-taxonomy.md` is preserved below — nothing here should read as a paraphrase of the source; if a distinction existed there, it exists here as an Applies-if/Does-not-apply-if bullet or an Example.

**Owner:** Charlie Wildish. Regenerate this file (or the affected sections) whenever `support-taxonomy.md` changes, or when a `/taxonomy-classification-qa` run identifies a Fin abstention or ambiguous-boundary fix that should be folded back into an Attribute description.

---

## How to use this file

- Each `##`/`###`/`####` heading below is one Fin Attribute value. Copy the block under it (name, description, Applies if / Does not apply if / Example / Likely keywords) directly into the corresponding Attribute value in Intercom.
- Per Intercom's guidance, every Issue Type level should have a general-purpose "Other/Uncategorized" value so Fin has a safe fallback instead of abstaining. Two are already documented in the source taxonomy as explicit defaults (Payouts → Card payouts, Identity Verification → N/A) — these are called out inline. For every other Case Type, consider adding an explicit "Other" Issue Type value if abstention shows up in a future QA run for that branch.
- Entries marked **[Proposed addition]** do not yet exist in `support-taxonomy.md` — they were identified as gaps during `/taxonomy-classification-qa` runs. Add them to the source taxonomy first (with sign-off) before pasting into Intercom, so the two files stay in sync.

---

## Case Type: Accepting payments

Refers to the technical lifecycle of customer-initiated transactions (processing, authorization, capture/void, refunds/reversals, disputes) for goods and services. Decline codes **20XXX / 30XXX / 40XXX** belong here.

**Applies if the customer:**
- Reports a decline, stuck transaction, missing transaction, duplicate charge, or refund problem for a specific payment or group of payments — the *lifecycle outcome* of a transaction.
- Reports a payment outcome issue with no integration failure involved: declines, 3DS failures, chargebacks, refund failures ("payment ops").
- Asks about refund execution, refund status, or refund failure itself ("refund execution").
- Cites a `pay_` transaction ID, a decline code (20XXX/30XXX/40XXX), or ARN/RRN in the context of a transaction outcome.

**Does not apply if the customer:**
- Wants to enable a new payment method, currency, or processing channel, or update billing/statement descriptors — that's *configuration*, not lifecycle, even though it's the same payment method (use Account management and access).
- Is asking about money moving out to an end recipient (payout, remittance, disbursement) rather than a customer-initiated payment (use Payouts).
- Is asking about merchant balance settlement or fees rather than an individual transaction (use Funds and fees).
- Attributes a decline to tokenisation, card-on-file, or network-token configuration rather than the payment outcome itself (use Technical issue → Tokens).

**Likely keywords:** declined, transaction status, refund, 3DS, chargeback, dispute, fraud, acceptance rate, pay_, decline code

### Issue Type: Transaction status (non 3DS & refunds)

Refers to the status, outcome, or root cause of failure for specific payment attempts or individual customers. Select this for "Why did this fail?" or "Where is the money?" queries regarding single or specific groups of transactions.

**Applies if the customer:**
- Asks "why did this fail?" or "where is the money?" for a single or specific group of transactions.
- Reports a transaction stuck in an intermediate state, a missing/unrecognised transaction, or a duplicate charge.
- Requests proof-of-payment identifiers (ARN, RRN) or bulk transaction metadata.

**Does not apply if the customer:**
- Is asking specifically about a 3DS/authentication issue (use Authentication (3DS)).
- Is asking about a refund's execution, status, or failure (use Refunds).
- Reports a trend or high volume of declines across many transactions rather than a specific one (use Performance).
- Attributes the decline to tokenisation, card-on-file setup, or network-token configuration (use Technical issue → Tokens).

**Likely keywords:** declined, stuck, pending, missing transaction, charged twice, proof of payment, ARN, RRN

#### Reason: Declined / failed action

**Applies if the customer:**
- Reports a payment explicitly rejected with a response code by a bank or scheme.
- Requests root-cause analysis for a specific declined transaction, error code, or failure tied to a single customer/card.
- Says funds were deducted but not received, with no confirmed intermediate hold state.

**Does not apply if the customer:**
- Describes a confirmed intermediate state (e.g. Authorized/Captured) rather than an outright decline (use Stuck in status / status enquiry).

**Example:** "Why did this payment get declined with error code 20005?"

**Likely keywords:** declined, error code, response code, rejected, failed payment

#### Reason: Stuck in status / status enquiry

**Applies if the customer:**
- Reports a payment stuck in an intermediate payment state (e.g. **Authorized** or **Captured**).
- Requests confirmation of a current status.
- Questions the root cause and processing logic behind a specific transaction outcome (e.g. **unexpected voids or approvals**).

**Does not apply if the customer:**
- Reports an explicit decline/rejection with no confirmed intermediate state (use Declined / failed action).

**Example:** "This payment has been stuck in Authorized for three days — why hasn't it captured?"

**Likely keywords:** stuck, pending, status enquiry, authorized, captured, unexpected void, unexpected approval

#### Reason: Missing or unrecognised transaction

**Applies if the customer:**
- Claims a transaction occurred but cannot find it in the portal or logs.
- Asks for a general investigation where there is ambiguity about the transaction or its status.

**Does not apply if the customer:**
- Has already identified the specific transaction and is asking about its status or decline reason (use Stuck in status or Declined / failed action).

**Example:** "My customer says they paid but I can't find any record of this transaction on the dashboard."

**Likely keywords:** can't find, missing transaction, not showing, unrecognised charge

#### Reason: Customer charged twice

**Applies if the customer:** Reports a duplicate charge.

**Does not apply if the customer:** Reports a single charge that seems wrong in amount rather than duplicated (use Fee inquiry or Reconciliation issue as appropriate).

**Example:** "My customer was charged twice for the same order."

**Likely keywords:** charged twice, duplicate charge, double charge

#### Reason: Proof of payment (ARN, RNN, bulk)

**Applies if the customer:**
- Requests a specific transaction identifier (e.g. **ARN, RRN**) to provide to a customer.
- Requests bulk transaction metadata or logs.

**Does not apply if the customer:** Is asking for a refund proof specifically (use Refunds → Refund proof).

**Example:** "Can you send me the ARN for this transaction so I can give it to my customer's bank?"

**Likely keywords:** ARN, RRN, proof of payment, transaction reference, bulk export

#### Reason: Failed but customer charged

**Applies if the customer:** Says their customer was charged but the payment shows as declined/failed on the merchant's side.

**Does not apply if the customer:** Is reporting a duplicate charge rather than a charged-but-failed mismatch (use Customer charged twice).

**Example:** "My customer says the payment went through on their end, but our dashboard shows it as declined."

**Likely keywords:** charged but declined, customer charged failed payment

### Issue Type: Refunds

Includes failed refunds, refunds that need to be reversed, and requests for proof that a refund was issued.

**Applies if the customer:**
- Reports a refund that failed, needs manual intervention, needs to be reversed, or needs proof.
- Explicitly frames the request as a refund, even if withdrawal/payout-style identifiers (e.g. WPID) are present.
- Asks about the status of a pending or discrepant refund.

**Does not apply if the customer:**
- Is asking about the status of the original (non-refund) transaction (use Transaction status).
- References a `dsp_` dispute entity ID or frames the request as a chargeback credit rather than a merchant-initiated refund (use Disputes).
- Says refunds are blocked systemically due to a risk/account hold (use Fraud & risk controls → Risk rules).
- Is asking about a payout to an end recipient rather than a refund to their own customer (use Payouts).

**Likely keywords:** refund, refund status, refund proof, manual refund, refund reversal, credit back

#### Reason: Refund failed / manual refund

**Applies if the customer:**
- Reports an attempt to return funds resulted in a decline message, or they're unable to process the refund self-service due to **technical failures (e.g. failed voids)**, **scheme rules (e.g. exceeded time limits/MADA window)**, or **acquirer constraints**.
- Explicitly requests a manual refund or asks support to intervene to finalize the return.
- Reports a failed or missing void that they want resolved via a refund.

**Does not apply if the customer:** Is asking to undo/reverse a refund that already succeeded (use Refund reversal).

**Example:** "The refund keeps failing — we're past the MADA window, can you process it manually?"

**Likely keywords:** refund failed, manual refund, can't process refund, failed void, MADA window, exceeded time limit, acquirer constraint

#### Reason: Refund proof

**Applies if the customer:** Needs documentation to prove a refund was processed to their customer.

**Does not apply if the customer:** Is primarily asking to confirm the refund's current status rather than requesting documentation (use Refund status enquiry) — when both are requested, default to Refund status enquiry unless proof is the explicit primary ask.

**Example:** "Can you send proof the refund was issued? My customer's bank needs it."

**Likely keywords:** proof of refund, refund confirmation, refund receipt

#### Reason: Refund reversal

**Applies if the customer:**
- Reports a processed refund needs to be undone or was done in error.
- Requests recall/recovery of a refund that was sent successfully but to an inaccessible destination (e.g. a closed account).

**Does not apply if the customer:** Reports the refund itself failed to process (use Refund failed / manual refund).

**Example:** "We refunded the wrong amount by mistake — can this be reversed?"

**Likely keywords:** reverse refund, refund done in error, recall refund, refund sent to closed account

#### Reason: Refund status enquiry

**Applies if the customer:**
- Asks about the current status of a refund (e.g. **pending, declined, successful**) or reports a status discrepancy where the dashboard state doesn't match expectations.
- Asks about a refund stuck in "**Pending**," or investigates why funds haven't reached the customer, or wants general verification of a refund's lifecycle.

**Does not apply if the customer:** Is primarily requesting documentation/proof rather than a status update (use Refund proof).

**Example:** "This refund has been stuck in Pending for a week — what's happening?"

**Likely keywords:** refund status, is my refund pending, refund not received

### Issue Type: Authentication (3DS)

Queries about 3DS/Authentication issues.

**Applies if the customer:**
- Reports a transaction failing or being declined with a 3DS-related error, or the authentication process (**OTP, App redirect, or initiation**) not triggering or completing as expected.
- Asks about liability shift for a 3DS-processed payment or chargeback (e.g. **chargeback protection logic**).
- Asks about Strong Customer Authentication rules or requests to skip 3DS.

**Does not apply if the customer:** Reports a non-3DS decline (use Transaction status → Declined / failed action).

**Likely keywords:** 3DS, OTP, authentication failed, liability shift, SCA, exemption

#### Reason: 3DS decline

**Applies if the customer:** Reports a transaction failing/declining with a 3DS-related error, or the authentication process (OTP, App redirect, or initiation) is not triggered or completed as expected.

**Does not apply if the customer:** Is asking about liability shift specifically rather than the decline itself (use Liability shift status).

**Example:** "The OTP prompt never shows up and the payment fails — is this a 3DS issue?"

**Likely keywords:** 3DS declined, OTP failed, authentication not triggered

#### Reason: Liability shift status

**Applies if the customer:** Asks about liability shift for a 3DS-processed payment or chargeback (e.g. chargeback protection logic).

**Does not apply if the customer:** Is reporting a 3DS decline with no liability-shift question (use 3DS decline).

**Example:** "If this transaction was 3DS-authenticated, are we protected on the chargeback?"

**Likely keywords:** liability shift, chargeback protection, 3DS liability

#### Reason: SCA / exemption issue

**Applies if the customer:** Asks about Strong Customer Authentication rules or requests to skip 3DS.

**Example:** "Can we apply for an SCA exemption on low-value transactions?"

**Likely keywords:** SCA, exemption, skip 3DS, strong customer authentication

### Issue Type: Fraud & risk controls

Queries about fraud controls and settings.

**Applies if the customer:**
- Reports a payment blocked by fraud settings or the Risk engine, or requests changes to risk rules, blocklists, allowlists, or threshold settings.
- Wants to add/remove a specific entity (**IP, Email, or Card**) from a block or allow list.
- Reports an issue relating to **Address Verification Service (AVS) or CVV checks** — failures due to mismatches, check-result inquiries, or how these checks are performed/displayed.
- Reports blocks occurring due to too many attempts in a short timeframe (**velocity limit**).
- Reports refunds systemically blocked due to a risk/account hold (addressed to Risk team, "can't refund anyone").

**Does not apply if the customer:** Is asking about a specific refund's status with no risk-hold context (use Refunds).

**Likely keywords:** risk rules, blocklist, allowlist, velocity limit, AVS, CVV, fraud block

#### Reason: Risk rules

**Applies if the customer:** Reports a payment blocked by fraud settings/Risk engine, or requests changes to risk rules/blocklists/allowlists/thresholds. Also applies when refunds are blocked systemically due to a risk hold.

**Likely keywords:** risk engine, blocked by fraud, risk rule change, can't refund risk hold

#### Reason: Trustlist & decline list

**Applies if the customer:** Wants to add/remove a specific entity (IP, Email, Card) from a block or allow list.

**Likely keywords:** trustlist, decline list, add to blocklist, remove from allowlist

#### Reason: AVS / CVV mismatch

**Applies if the customer:** Reports a payment failure due to AVS or CVV mismatch, or asks how these checks are performed/displayed.

**Likely keywords:** AVS mismatch, CVV mismatch, address verification

#### Reason: Velocity limit reached

**Applies if the customer:** Reports blocks occurring due to too many attempts in a short timeframe.

**Likely keywords:** velocity limit, too many attempts, rate limited

### Issue Type: Disputes

Queries about the lifecycle of disputes/chargebacks.

**Applies if the customer:**
- Asks about the status, lifecycle, or outcome of a dispute (e.g. **Won/Lost, Pre-Arb**), or questions its validity.
- Has an operational issue: locating transactions involved in disputes, troubleshooting missing notifications (**emails/RFIs**), configuring dispute services (e.g. **RDR, ARNs, API automation**), or clarifying the financial impact on funds (e.g. **held/released amounts**).
- Questions or reports discrepancies in financial adjustments from disputes/chargebacks: **unexpected debits, duplicate charges, credit adjustments (UPDT), missing chargeback refunds**, or confusion about balance impact.
- Is actively defending a dispute or RFI: submitting files (**including manual upload requests**), troubleshooting dashboard submission errors, or asking which specific documents are required to contest the case.
- References a `dsp_` entity ID, even if phrased as a "credit back" or refund request.

**Does not apply if the customer:** Is requesting a standard merchant-initiated refund with no dispute/chargeback context (use Refunds).

**Likely keywords:** dispute, chargeback, RFI, evidence, pre-arb, dsp_, credit adjustment, UPDT

#### Reason: Dispute status

**Applies if the customer:**
- Asks about the status, lifecycle, or outcome of a dispute (Won/Lost, Pre-Arb), or questions its validity.
- Has an operational issue: locating dispute transactions, missing RFI/notification emails, dispute-service configuration (RDR, ARNs, API automation), or held/released fund clarification.

**Example:** "What's the status of this dispute — has it been won or lost yet?"

**Likely keywords:** dispute status, won lost, pre-arb, missing RFI, RDR configuration

#### Reason: Dispute adjustment

**Applies if the customer:** Questions or reports discrepancies in financial adjustments from disputes/chargebacks — unexpected debits, duplicate charges, credit adjustments (UPDT), missing chargeback refunds, or balance-impact confusion.

**Example:** "There's an unexpected UPDT credit adjustment on my balance — what caused it?"

**Likely keywords:** dispute adjustment, UPDT, chargeback debit, balance impact from dispute

#### Reason: Evidence help and submission

**Applies if the customer:** Is actively defending a dispute or RFI — submitting files (including manual upload requests), troubleshooting dashboard submission errors, or asking which documents are required.

**Example:** "What documents do I need to submit to contest this chargeback?"

**Likely keywords:** submit evidence, RFI documents, dispute evidence upload

### Issue Type: Performance

Queries about acceptance rate performance or multiple payment failures.

**Applies if the customer:**
- Reports a drop in overall approval ratios, asks for optimization advice, or flags a trend of declines across multiple transactions.
- Reports a large volume/systemic pattern of payment failures rather than a single transaction.

**Does not apply if the customer:** Is asking about a single, specific transaction's decline reason (use Transaction status → Declined / failed action).

**Likely keywords:** acceptance rate, decline trend, approval ratio, multiple failures, systemic decline

#### Reason: Acceptance rate issue / optimisation

**Applies if the customer:** Reports a drop in overall approval ratios, asks for optimization advice, or flags a trend of declines across multiple transactions.

**Likely keywords:** acceptance rate drop, optimize approvals, decline trend

#### Reason: All payments failing

**Applies if the customer:** Reports a large volume of payment failures or systemic payment failures.

**Likely keywords:** all payments failing, systemic outage, everything declining

---

## Case Type: Payouts

Refers to the lifecycle of a payout made by card or bank payout. Includes status, declines, reversals, and proofs of payout.

**Applies if the customer:**
- Asks about a payout, withdrawal, or transfer to an end recipient — status, decline, proof, cancellation, or reversal.
- Uses generic references (Payout ID, Partner ID, reference number) with no bank-specific identifiers.

**Does not apply if the customer:**
- Is asking about settlement of their own merchant balance to their own bank account — that's a Funds and fees matter, not a payout to an end recipient (use Funds and fees → Settlements).
- Explicitly frames the request as a refund to their end customer, even if withdrawal-style identifiers are present (use Accepting payments → Refunds).
- Is reporting a non-actionable, unresolvable, or follow-up/duplicate contact that superficially mentions payout status (use General → Inquiries).
- Is asking about managing, activating, or controlling a Checkout-issued card (create/activate, freeze, spend limits) rather than sending money via a card network to an end recipient — that's Card issuing, not Payouts, even though both mention "card."

**Likely keywords:** payout, withdrawal, transfer, remittance, disbursement, payout ID

### Issue Type: Bank payouts

Queries about payouts sent via bank transfer rails (**SEPA, SWIFT, Faster Payments, ACH, wire transfers**) only. Select based on the actual payment rail, not the type of proof document requested.

**Applies if the ticket explicitly mentions:**
- Bank account, IBAN, SWIFT/BIC codes, MT103, beneficiary bank, wire transfer, or other bank-specific references.
- Sanctions/AML screening holds, **Inpay references**, or name-discrepancy verification.
- A payout requiring RFI (Request for Information) for compliance screening.

**Does not apply if the customer:**
- Asks for a "SWIFT receipt" or mentions a "bank account number" but the underlying rail is card-based — this is normal customer phrasing for any payout proof request and does not by itself indicate the rail (use Card payouts).
- Provides no bank-specific identifier at all — do NOT select this if the payout method is unclear (use Card payouts, the documented default).

**Likely keywords:** IBAN, SWIFT, BIC, MT103, wire transfer, beneficiary bank, SEPA, ACH, sanctions screening, Inpay, name discrepancy

#### Reason: Declined / failed bank payout

**Applies if the customer:** Reports a bank payout that was declined.

**Likely keywords:** bank payout declined, wire transfer failed

#### Reason: Proof of bank payout

**Applies if the customer:** The recipient claims they haven't received funds from a bank payout and the merchant needs a confirmation receipt — with a true bank rail confirmed (IBAN/SWIFT/MT103).

**Likely keywords:** proof of bank payout, wire confirmation, SWIFT MT103 receipt (bank rail confirmed)

#### Reason: Bank payout stuck in pending or status inquiry

**Applies if the customer:** Inquires about a bank payout that is delayed, stuck in processing, or showing a pending status — including all scenarios where a bank payout is **held for compliance checks, sanctions reviews, or risk assessments**, often requiring an RFI to resolve the hold. Also covers general status investigations and discrepancies in payout amounts, on a confirmed bank rail.

**Likely keywords:** bank payout pending, sanctions hold, RFI bank payout, compliance hold, payout amount discrepancy

#### Reason: Bank payout returns

**Applies if the customer:** Asks to reverse a bank payout.

**Does not apply if the customer:** Is asking to re-release the merchant's own settled balance to their own bank account after a return/reversal (use Funds and fees → Settlements).

**Likely keywords:** reverse bank payout, bank payout return

### Issue Type: Card payouts

Queries about payouts sent via card networks (**Visa Direct, Mastercard Send, Pay to Card/PTC, OCT**). **This is the documented default Issue Type for Payouts when the rail is ambiguous or unclear** — do not leave Issue Type blank; select Card payouts rather than abstaining.

**Applies if the ticket mentions:**
- Visa, Mastercard, card payout, card-based, ARN (**Acquirer Reference Number**), RRN, issuing bank, issuer, cardholder, or any card scheme reference.
- A generic "withdrawal" or "payout" with **no rail specified** — when the payout method is ambiguous or unclear, default to Card payouts, as they represent the majority of payout volume.

**Does not apply if the customer:** Mentions IBAN, SWIFT/BIC, MT103, beneficiary bank, or wire transfer (use Bank payouts).

**Likely keywords:** card payout, Visa Direct, Mastercard Send, Pay to Card, OCT, ARN, RRN, cardholder

#### Reason: Card payout stuck in pending or status inquiry

**Applies if the customer:** Asks why a card payout is stuck in Pending, or requests general status confirmation with no bank rail specified.

**Likely keywords:** card payout pending, payout status, when will I receive payout

#### Reason: Declined / failed card payout

**Applies if the customer:** Asks why a card payout was declined, reports the payout showed **Paid but the customer didn't receive money**, or asks to cancel/reject a payout **before it has processed**.

**Does not apply if the customer:** Asks to reverse or undo a card payout that has **already completed successfully** (use Card payout reversal).

**Likely keywords:** card payout declined, paid but not received, cancel payout before processing, reject payout

#### Reason: Proof of card payout

**Applies if the customer:** Needs a card payout proof or **Retrieval Reference Number (RRN)** to give to a customer, with no bank rail specified.

**Likely keywords:** proof of card payout, RRN, payout receipt (no bank rail)

#### Reason: Card payout reversal

**Applies if the customer:** Asks to reverse or undo a card payout that has **already completed successfully**.

**Does not apply if the customer:** Asks to cancel or reject a payout **before it has processed** (use Declined / failed card payout).

**Likely keywords:** reverse card payout, undo completed payout

---

## Case Type: Funds and fees

Refers to the flow of money in the merchant balance and their settlements, and any associated fees. Includes settlement delays, reconciliation issues, balance queries, and invoice/fee inquiries.

**Applies if the customer:**
- Reports settlement reconciliation and cash-movement interpretation issues, or mismatched financial amounts (**wrong settlement amount, unexpected fee**).
- Asks about fees (**interchange/scheme/gateway fees, tax invoices, pricing checks**), including "**why fee wasn't refunded**."
- Asks about returns/re-releases of their own settled funds to their own bank account.

**Does not apply if the customer:**
- Asks about the settlement state or outcome of one specific named transaction (use Accepting payments → Transaction status).
- Asks about a payout to an end recipient rather than their own merchant balance (use Payouts).
- Reports a reconciliation problem caused by a data-format/export defect (Excel truncation, unreadable ARNs, encoding issues) rather than a financial amount mismatch (use Data and analytics → Reporting → Data mismatch / missing data).

**Likely keywords:** settlement, balance, reconciliation, invoice, fee, statement of account, gateway fee, pricing check

### Issue Type: Settlements

Queries about settlement lifecycle and reconciliation.

**Applies if the customer:**
- Reports an expected settlement not showing on Dashboard or not arrived in their bank account.
- Is struggling to match report/Dashboard data to bank statement entries, or reports a discrepancy between expected and actual balances.
- Asks about returns/re-releases of their own settled funds to their own bank account (e.g. after a payout provider reversal).

**Does not apply if the customer:**
- Asks about the settlement state of one specific named transaction, using the word "settlement" generically (use Accepting payments → Transaction status).
- Reports a reconciliation problem caused by a data-format/export defect rather than a financial mismatch (use Data and analytics → Reporting → Data mismatch / missing data).
- Is confused about their balance figure itself or how funds are allocated, with no bank-statement matching involved (use Balances → Balance explanation).

**Likely keywords:** settlement delayed, missing settlement, reconciliation, settlement mismatch, return of funds

#### Reason: Delayed / missing settlement

**Applies if the customer:** An expected settlement is not showing on Dashboard or hasn't arrived in the merchant's bank account.

**Likely keywords:** settlement not received, missing settlement

#### Reason: Reconciliation issue

**Applies if the customer:** Is struggling to match report or Dashboard data to their bank statement entries, or is reporting a discrepancy between expected and actual balances — including mismatched financial amounts (wrong settlement amount, unexpected fee) and cash-movement interpretation.

**Does not apply if the customer:**
- Is confused about their balance figure itself or how funds are allocated, with no bank-statement matching involved (use Balances → Balance explanation).
- Has a reconciliation problem caused by a data-format/export defect — Excel truncation, unreadable ARNs, encoding issues — rather than mismatched financial amounts (use Data and analytics → Reporting → Data mismatch / missing data).

**Likely keywords:** reconciliation, doesn't match bank statement, balance discrepancy, wrong settlement amount, unexpected fee

#### Reason: Other **[Proposed addition]**

Identified during `/taxonomy-classification-qa` (2026-07-07) — not yet in `support-taxonomy.md`. The current taxonomy only defines Delayed/missing settlement and Reconciliation issue under Settlements; a contact about returns/re-releases of the merchant's own settled funds to their own bank account had no clean home. Add to the source taxonomy before pasting into Intercom.

**Applies if the customer:** Has a settlement-related query about returns, re-releases of their own funds, or another settlement topic not covered by Delayed/missing settlement or Reconciliation issue.

**Likely keywords:** settlement return, re-release funds, other settlement query

### Issue Type: Balances

Queries about balance status and confirmation.

**Applies if the customer:**
- Needs a Statement of Account (SOA) or balance confirmation document for audit purposes.
- Is struggling to understand why they have a negative balance.
- Needs to top up their balance.
- Needs help understanding their balance or how funds are allocated, reports balance discrepancies, or is unable to reconcile figures between reports or different balance types.

**Does not apply if the customer:** Is specifically trying to match Dashboard/report data to their bank statement entries (use Settlements → Reconciliation issue).

**Likely keywords:** balance confirmation, negative balance, top up, balance explanation, statement of account

#### Reason: Balance confirmation

**Applies if the customer:** Needs a Statement of Account (SOA) or balance confirmation document for audit purposes.

**Likely keywords:** SOA, balance confirmation, audit document

#### Reason: Negative balance

**Applies if the customer:** Is struggling to understand why they have a negative balance on their account.

**Likely keywords:** negative balance, why is my balance negative

#### Reason: Balance top up

**Applies if the customer:** Needs to top up their balance.

**Likely keywords:** top up balance, add funds to balance

#### Reason: Balance explanation

**Applies if the customer:** Needs help understanding their balance or how funds are allocated, reports balance discrepancies, or is unable to reconcile figures between reports or different balance types.

**Does not apply if the customer:** Is specifically trying to match Dashboard/report data to their bank statement entries (use Settlements → Reconciliation issue).

**Likely keywords:** explain my balance, balance doesn't add up, fund allocation

### Issue Type: Billing & fees

Queries about fees charged.

**Applies if the customer:**
- Needs a copy of their tax or service invoice.
- Questions a specific charge (e.g. **Interchange, Scheme fee**).

**Likely keywords:** invoice, fee inquiry, interchange fee, scheme fee, tax invoice

#### Reason: Invoice request

**Applies if the customer:** Needs a copy of their tax or service invoice — Checkout.com's own billing to the merchant (see product-definitions.md → Financial Report).

**Likely keywords:** invoice copy, tax invoice request

#### Reason: Fee inquiry

**Applies if the customer:** Questions a specific charge (e.g. Interchange, Scheme fee).

**Likely keywords:** why was I charged this fee, interchange fee question

---

## Case Type: Technical issue

Refers to integration or technical issues (API/SDK/webhook/connectivity), including HTTP 4xx/5xx errors, keys, tokens, and test environment issues.

**Applies if the customer:**
- Reports explicit HTTP status codes (**400/401/403/404/409/422/429/500/502/503**) or API/endpoint/SDK failures (e.g. "**API returned 500**").
- Reports plugin/checkout UI/integration behaviour issues: **redirects, saved cards, a payment method disappearing from the site**.
- Asks about Network Tokens, Vault, Card Metadata, Forwarding API, or Wallets — see those Issue Types for specifics.
- Attributes declines to tokenisation, card-on-file configuration, or network-token setup, even if a decline code is also present.
- Reports a customer charged an amount not reflected in Checkout.com records (**wallet surcharge, 3DS fee, issuer fee**) — treat as an integration-layer investigation.
- Asks about API key management, sandbox/test environment issues, or webhook setup/delivery.
- Asks about form/checkout fields in **their own website's data-capture integration**, distinct from the Checkout.com Identity Verification product itself (stays in Identity Verification).
- Reports acquiring-side MCC restrictions on processing channels (**`pc_*` IDs**) — not issued-card spend controls (Card issuing).

**Does not apply if the customer:**
- Reports a payment performance/outcome issue with no technical/integration angle (use Accepting payments).
- Frames a live, already-enabled payment method's decline as "setup"/"configuration" (use Accepting payments).
- Asks about the Checkout.com Identity Verification product itself (use Identity Verification).
- Provides a `trx_` ID in the context of issued-card spend controls or lifecycle (use Card issuing).
- Is a cardholder adding their issued card to Apple Pay/Google Pay (use Card issuing → Issuing digital wallets, not this Case Type's Wallets Issue Type).
- Requests general BIN/issuer/scheme reference data with no specific data-accuracy dispute (use General → Inquiries → Reference data request, not Card Metadata).

**Likely keywords:** API error, HTTP 500, webhook, SDK, sandbox, API key, network token, vault, card metadata, forwarding API, wallet domain, integration, wallet surcharge, issuer fee

### Issue Type: API keys

Queries regarding the management of authentication keys (**Secret/Public OAuth**) and their access permissions.

**Applies if the customer:**
- Asks how to create, edit, or troubleshoot API keys.
- Inquires which permissions are required, or explicitly requests specific scopes (such as **`/metadata/card`**) be granted to their API keys.
- Reports API keys missing or inaccessible after an account change/reset.

**Does not apply if the customer:** Frames the same API-key issue as an "account reset" or "account configuration" problem — the core object (API keys) determines the routing, not the framing (use this Issue Type, not Account management and access).

**Likely keywords:** API key, create key, edit key, key scope, secret key, public key, /metadata/card, keys missing after reset

#### Reason: Create / edit keys

**Applies if the customer:** Asks about how to create, edit, or troubleshoot API keys.

**Likely keywords:** create API key, edit API key, key troubleshooting

#### Reason: Key scopes

**Applies if the customer:** Inquires which permissions are required, or explicitly requests specific scopes, such as `/metadata/card`, be granted to their API keys.

**Likely keywords:** key scope, API permission, grant scope, /metadata/card

### Issue Type: API integration

Queries regarding raw API responses, HTTP status codes, and network connectivity. Use this as the "catch-all" for API errors that are **not specific to a Plugin, Flow, Frames, SDK, Payment Links, Network Tokens, Vault, Card Metadata, Forwarding API, or Wallets**.

**Applies if the customer:**
- Encounters HTTP 400-level errors (e.g. **404 Not Found, 422 Validation Error**) indicating the issue lies with the request, or reports functional integration bugs — **redirect parameter mismatches, invalid data formats, missing response payloads, or logic errors** where the system rejects the input.
- Reports HTTP 500-level errors, indicating the request was valid but the server failed due to technical faults like **Service Unavailable (503)** — broader infrastructure problems, overall API status issues, sync failures from server crashes, or internal errors preventing completion. This is the correct selection for outages/downtimes where the provider's system is unresponsive.
- Reports timeout or idempotency issues on API requests.
- Asks about integration approach/API capability for a payment method (e.g. "can we still use the API-only integration for X"), even if phrased as an account/setup question.

**Does not apply if the customer:**
- Is asking to enable/activate a payment method rather than a question about integration design or API errors (use Account management and access).
- Reports a webhook delivery, signature-verification, or payload-content issue rather than a synchronous API call error (use Webhooks).
- Reports an API error specific to Network Tokens, Vault, Card Metadata, Forwarding API, or Wallets — use that Issue Type instead of this catch-all.

**Likely keywords:** API error, 400, 404, 422, 500, 503, timeout, idempotency, integration approach

#### Reason: API error 4XX / logic error

**Applies if the customer:** Encounters HTTP 400-level errors (e.g. 404 Not Found, 422 Validation Error) indicating the issue lies with the request, OR reports functional integration bugs — redirect parameter mismatches, invalid data formats, missing response payloads, or logic errors where the system rejects the input.

**Likely keywords:** 404, 422, bad request, invalid format, logic error, redirect mismatch

#### Reason: API error 5XX

**Applies if the customer:** Reports HTTP 500-level errors — the request was valid but the server failed due to technical faults like Service Unavailable (503). Applies to broader infrastructure problems, overall API status issues, sync failures caused by server crashes, or internal system errors preventing completion. This is the correct selection for outages or downtimes where the provider's system is unresponsive.

**Likely keywords:** 500, 503, service unavailable, outage, internal error, downtime

#### Reason: Idempotency / timeout

**Applies if the customer:** Is getting timeout or idempotency issues on API requests.

**Likely keywords:** timeout, idempotency key, request timed out

### Issue Type: Network Tokens

Queries about Network Tokens: onboarding, provisioning, billing, performance, and API errors. **[Renamed from "Tokens" — token migration moved to Vault]**

**Applies if the customer:**
- Reports onboarding issues for Network Tokens (e.g. a scheme-specific "Onboard to Mastercard" toggle not saving/applying for a client ID).
- Reports provisioning issues — missing or low network-token counts, whether it's a provisioning failure vs. not attempted, or how async provisioning / `provision_networktoken` works.
- Raises billing/fee concerns specific to Network Token fees (spikes, accuracy, fees charged on declined transactions).
- Reports an API error specific to network-token services (cryptogram retrieval failures, `INVALID_REQUESTOR`, TRID format questions, fallback to FPAN).
- Asks for an acceptance-rate/performance analysis tied specifically to Network Token usage, or is deciding whether to disable NT.
- Attributes declines (even with a decline code present) to tokenisation, card-on-file setup, or missing `payment_type`/`payment_plan` recurring parameters.

**Does not apply if the customer:**
- Asks about importing/exporting Vault tokens or instruments, or Vault customer/API errors — use Vault instead.
- Reports a decline with no tokenisation/network-token framing at all (use Accepting payments → Transaction status).

**Likely keywords:** network token, NT onboarding, provisioning, MDES, cryptogram, TRID, FPAN fallback, network token fee, NT performance, PEM

#### Reason: Onboarding

**Applies if the customer:** Asks about turning on or configuring network-token settings for a card scheme (e.g. an "Onboard to Mastercard" toggle in CAT) and it isn't saving or applying for their client ID(s).

**Example:** "I'm trying to turn on 'Onboard to Mastercard' toggle for Network Tokens in CAT. But after saving, I can see that the setting is not applied."

**Likely keywords:** onboard to Mastercard, network token toggle not saving, NT setting not applied

#### Reason: Provisioning

**Applies if the customer:** Asks why they have few or no network tokens provisioned, whether it's a provisioning failure vs. not being attempted, or how async provisioning / the `provision_networktoken` parameter works.

**Example:** "What I see is they have very less network tokens available... Is it because of provisioning failures? Is it because of provisioning not being attempted due to any other reason?"

**Likely keywords:** network token provisioning, async provisioning, provision_networktoken, low token count

#### Reason: Billing

**Applies if the customer:** Raises concerns about Network Token fees — an unexplained spike, accuracy of charges against lifecycle events, or whether fees are being charged on declined transactions.

**Example:** "I am escalating a billing concern... regarding a significant and unexplained surge in Network Token (NT) fees... Are we charging 'Token Creation' fees on transactions that resulted in a decline?"

**Likely keywords:** network token fee spike, NT billing, token creation fee, fee on decline

#### Reason: API errors

**Applies if the customer:** Reports an API error in network-token services — cryptogram retrieval failures, `INVALID_REQUESTOR`, TRID format questions, or payments falling back to FPAN.

**Example:** "100% of the requests for Mastercard is failing with an error 'INVALID_REQUESTOR'... is this a valid value?" (referring to a TRID)

**Likely keywords:** cryptogram error, INVALID_REQUESTOR, TRID, FPAN fallback, network-token-requestor logs

#### Reason: Performance

**Applies if the customer:** Asks for an acceptance-rate/performance analysis specifically tied to Network Token usage, including cost-benefit questions or whether to disable NT.

**Example:** "I need an analysis of Network Token performance for the merchant... they are currently evaluating whether to disable NT... I'm seeing an approximate uplift of just 1.5% in acceptance rate."

**Likely keywords:** NT acceptance rate uplift, network token performance analysis, disable NT

### Issue Type: Vault

Queries about Vault instruments, tokens, and customers — the card/customer data storage layer, distinct from Network Tokens.

**Applies if the customer:**
- Reports an API error calling a Vault endpoint (e.g. payment-sessions, instruments, a public-key/vault-ID mismatch).
- Reports issues creating, fetching, or managing a stored Instrument (e.g. Get Instrument returning 404 despite the instrument existing in the dashboard).
- Asks what makes a Vault token invalid, or reports errors on specific `tok_` values distinct from network tokens.
- Reports a Vault Customer record missing or behaving unexpectedly (e.g. `customer_not_found` after a migration).
- Asks about importing or exporting merchant tokens between Vault and another system.

**Does not apply if the customer:**
- Reports Network Token-specific onboarding, provisioning, billing, API-error, or performance issues — use Network Tokens instead.
- Reports card scheme/issuer metadata or BIN/issuer-data discrepancies — use Card Metadata instead.

**Likely keywords:** vault, instrument, tok_, token invalid, customer_not_found, vault id, public key mismatch, vault token migration

#### Reason: API errors

**Applies if the customer:** Reports an API error from a Vault endpoint, such as a payment-sessions submit failure or "No public key matching the vault id found."

**Example:** "CMC Markets are hitting a 422 payment_attempt_failed response when trying to call POST /payment-sessions/{id}/submit... No public key matching the vault id found."

**Likely keywords:** vault API error, payment_attempt_failed, public key vault id mismatch, 422 vault

#### Reason: Instruments

**Applies if the customer:** Reports issues creating, fetching, or listing a stored Instrument, such as the Get Instrument API returning 404 despite the instrument existing in the dashboard.

**Example:** "They have raised the issue that they are not able to fetch Instrument using Get Instrument API in Sandbox... I got 404 everytime i call Get Instrument API even the Instrument exist in dashboard."

**Likely keywords:** get instrument 404, instrument not found, vault instrument API

#### Reason: Tokens

**Applies if the customer:** Asks what makes a Vault token invalid, or reports an error on a specific `tok_` value distinct from a network token.

**Example:** "So what makes a token invalid then? Because there are separate errors for token_expired and token_used... so what else can make a token invalid?"

**Likely keywords:** vault token invalid, tok_expired, tok_used

#### Reason: Customers

**Applies if the customer:** Reports a Vault customer record missing, lost, or behaving unexpectedly, such as `customer_not_found` after a migration.

**Example:** "raised a case of customer_not_found errors for the customerId... it seems that this customer is not existing anymore whereas it was present historically."

**Likely keywords:** customer_not_found, vault customer missing, customer lost in migration

#### Reason: Token migration

**Applies if the customer:** Asks about importing or exporting merchant tokens between Vault and another system or provider.

**Likely keywords:** token import, token export, vault token migration

### Issue Type: Card Metadata

Queries about Card Metadata — BIN/issuer data-accuracy disputes on a specific card or transaction, card-payout eligibility fields, and API errors. Distinct from a generic request for reference data with no specific dispute.

**Applies if the customer:**
- Reports that BIN/issuer/scheme data returned for a specific card or transaction looks wrong, and asks Checkout to validate or correct it.
- Asks which Card Metadata field determines card-payout eligibility (e.g. domestic vs. cross-border) for a specific payout scenario.
- Reports an API error calling Card Metadata endpoints, or a downstream failure (e.g. a decline) traced back to a Card Metadata field value.

**Does not apply if the customer:**
- Asks for general BIN ranges, issuer identification, or scheme metadata with no specific transaction/data-accuracy dispute — use General → Inquiries → Reference data request instead.
- Asks about issued-card spend controls or lifecycle — use Card issuing instead.

**Likely keywords:** card metadata, BIN issuer mismatch, wrong issuer name, card payout eligibility, domestic cross border, local_scheme, preferred_scheme_not_applicable

#### Reason: BIN/Issuer data

**Applies if the customer:** Flags a specific BIN/card as returning an incorrect issuer name or other BIN/issuer data point, and asks Checkout to validate.

**Does not apply if the customer:** Asks for BIN ranges or issuer identification with no specific data dispute — use General → Inquiries → Reference data request instead.

**Example:** "We are seeing a wrong issuer name being returned for Amazon Cards in UAE... yet our data show them as NETWORK INTERNATIONAL LLC. Can you help me validate...?"

**Likely keywords:** wrong issuer name, BIN issuer mismatch, issuer data validation

#### Reason: Card Payout eligibility

**Applies if the customer:** Asks which Card Metadata field (e.g. domestic vs. cross-border eligibility) applies for a specific card-payout scenario.

**Example:** "Should they check the 'domestic' or 'cross border' eligibility fields in the metadata API response?... USD to USD funded card payout with recipient being a user with a Japan address."

**Likely keywords:** card payout eligibility, domestic cross border field, payout metadata

#### Reason: API errors

**Applies if the customer:** Reports an API error from Card Metadata endpoints, or a decline/failure traced to a Card Metadata field (e.g. `local_scheme`, `preferred_scheme_not_applicable`).

**Example:** "Couple of merchants have raised concerns about CB transactions failing with 422 ['preferred_scheme_not_applicable']... card.local_scheme and card.scheme comes from Card Metadata/Vault API."

**Likely keywords:** card metadata API error, preferred_scheme_not_applicable, local_scheme mismatch

### Issue Type: Forwarding API

Queries about Forwarding API — enabling merchants, allow-listing destination URLs, and API errors.

**Applies if the customer:**
- Requests Forwarding API be enabled for a client ID in Sandbox or Production.
- Requests a destination URL/domain be added to the Forwarding API allow list, or asks how allow-listing scope works (per-endpoint vs. domain-level).
- Reports an API/HTTP error on forwarded traffic and asks whether it originates from Checkout's side or the destination.

**Does not apply if the customer:** Reports a general API 4XX/5XX error with no Forwarding API context — use API integration instead.

**Likely keywords:** forwarding API, enable forwarding, allow list URL, whitelist domain, forward traffic 401

#### Reason: Enablement

**Applies if the customer:** Requests Forwarding API be enabled for a client ID, in Sandbox or Production.

**Example:** "Can you please enable dashboard analytics in sandbox for the client Id: cli_e75smvkyfrhuvmpb35q7gsppcu."

**Likely keywords:** enable forwarding API, forwarding API sandbox, forwarding API production

#### Reason: URL Allow listing

**Applies if the customer:** Requests a destination URL/domain be added to the allow list, or asks how domain vs. endpoint allow-listing scope works.

**Example:** "we need to whitelist some URLs... if we have multiple endpoints on the same domain, do we need to whitelist all of them or can we just whitelist the main domain/subdomain?"

**Likely keywords:** whitelist URL, allow list domain, forwarding destination endpoint

#### Reason: API errors

**Applies if the customer:** Reports an API/HTTP error on forwarded traffic and asks whether the failure originates from Checkout or the destination.

**Example:** "they are facing 401 Unauthorized at our side for a high volume of forward traffic... can you please help us understand is this originating from the destination or our side?"

**Likely keywords:** forwarding 401, forward traffic error, destination vs origin error

### Issue Type: Wallets

Queries about merchant-side Wallet payment onboarding and processing for Apple Pay and Google Pay, on the acceptance side — domain onboarding, domain errors, and API errors. Distinct from Card issuing → Issuing digital wallets, which covers a cardholder adding a Checkout-*issued* card to their own wallet.

**Applies if the customer:**
- Requests a merchant domain be onboarded for Apple Pay, or asks about Google Pay domain/merchant setup.
- Reports a wallet payment failing due to a domain/merchant-ID registration error (e.g. "merchant not registered for service").
- Reports an API error specific to an Apple Pay or Google Pay payment attempt.

**Does not apply if the customer:**
- Is a cardholder unable to add their Checkout-issued card to Apple Pay/Google Pay, or reports issuing-side provisioning/token errors in their own wallet — use Card issuing → Issuing digital wallets instead.
- Asks about Flow/Frames/SDK/plugin integration generally with no wallet-specific domain/API error — use Integration methods instead.

**Likely keywords:** apple pay domain onboarding, google pay domain, merchant not registered, wallet domain error, apple pay 403

#### Reason: Domain onboarding

**Applies if the customer:** Requests a merchant domain be onboarded/registered for Apple Pay or Google Pay, in production or sandbox.

**Example:** "Could you please onboard the merchant for Applepay on production... Domain: kaafmeem.api.checkout.com."

**Likely keywords:** apple pay domain onboarding, register domain apple pay, google pay onboarding

#### Reason: Domain errors

**Applies if the customer:** Reports a wallet payment failing due to a domain/merchant-ID registration error, such as "not registered for service."

**Example:** "Merchant... are unable to make Apple Pay payments and getting error - 'Payment Services Exception merchantId=... not registered for service'."

**Likely keywords:** merchant not registered, apple pay domain error, wallet registration failure

#### Reason: API errors

**Applies if the customer:** Reports an API/HTTP error specific to an Apple Pay or Google Pay payment attempt.

**Example:** "Merchant has tried with Apple Pay but got 403 error and their card payment is working fine... please can you check why it failed?"

**Likely keywords:** apple pay 403, google pay API error, wallet payment error

### Issue Type: Integration methods

The merchant is inquiring about the specific interface, library, or platform used to process payments — **hosted pages, plugins, SDKs, or payment links**.

**Applies if the customer:**
- Asks about Flow or Frames, or migration to Flow.
- Asks about Payment Links or Hosted Payment Page issues.
- Asks about an SDK issue.
- Asks about a Plugin issue like **Shopify, WooCommerce**, and others.

**Does not apply if the customer:** Asks specifically about Apple Pay/Google Pay domain onboarding, domain errors, or wallet-specific API errors — use Wallets instead.

**Likely keywords:** Flow, Frames, Payment Links, hosted payment page, SDK, plugin, Shopify, WooCommerce

#### Reason: Flow / frames

**Applies if the customer:** Is asking about Flow or Frames, or migration to Flow.

**Likely keywords:** Flow, Frames, migrate to Flow

#### Reason: Payment links / hosted payment pages

**Applies if the customer:** Is asking about Payment Links or Hosted Payment Page issues.

**Likely keywords:** payment link, hosted payment page

#### Reason: SDK issue

**Applies if the customer:** Is asking about an SDK issue.

**Likely keywords:** SDK error, SDK integration issue

#### Reason: E-commerce plugin

**Applies if the customer:** Is asking about a Plugin issue like Shopify, WooCommerce, and others.

**Likely keywords:** Shopify plugin, WooCommerce plugin, e-commerce plugin

### Issue Type: Webhooks

Queries about webhooks.

**Applies if the customer:**
- Is unable to successfully configure or connect their webhooks, including **errors within third-party plugins like Shopify** or requests for initial registration in environments like **Sandbox**. Covers all configuration-stage inquiries, such as **Endpoint Registration Failures** where the **listener URL cannot be saved**, or needing help enabling the service before any live transactions occur.
- Reports webhook delivery issues: **Delivery Latency**, missed notifications/callbacks for specific events (like **entity creation**), synchronization failures where a **Status Mismatch** occurs because the webhook never arrived to update their system, dispatch timing investigations, or timeouts where they question if the webhook **failed to sync a successful capture** to their dashboard.
- Reports signature verification issues: questions about security headers, source IP verification, how to cryptographically verify the webhook signature, the secret key, the hashing algorithm used, or why local verification logic is failing to authenticate the incoming request.
- Reports inconsistent metadata such as a **missing orderId**, or specifically points out the **Payload Data Format** doesn't match expectations — the webhook was delivered but content was incomplete/incorrect.

**Does not apply if the customer:** Reports a general API 4XX/5XX error on a synchronous API call with no webhook/async-delivery context (use API integration).

**Likely keywords:** webhook setup, webhook not firing, signature verification, missing webhook data, delivery failure, listener URL, entity creation, status mismatch, orderId

#### Reason: Webhook setup

**Applies if the customer:** Is unable to successfully configure or connect their webhooks, including errors within third-party plugins like Shopify or requests for initial registration in environments like Sandbox. Covers configuration-stage inquiries such as Endpoint Registration Failures where the listener URL cannot be saved, or needing help enabling the service before any live transactions occur.

**Example:** "I can't get the webhook listener URL to save in Sandbox — it just fails every time."

**Likely keywords:** webhook setup, endpoint registration, can't save webhook URL, sandbox registration

#### Reason: Signature verification or delivery failure

**Applies if the customer:** Reports webhook delivery issues (**Delivery Latency**, missed notifications/callbacks for specific events like **entity creation**, sync failures where a **Status Mismatch** occurs because the webhook never arrived, dispatch timing investigations, or timeouts questioning if the webhook **failed to sync a successful capture**) OR signature verification issues (security headers, source IP, cryptographic verification, secret key, hashing algorithm, local verification logic failing). Applies when the webhook did not fire/arrive at all, or fails authentication.

**Does not apply if the customer:** Reports the webhook arrived but its payload content is incomplete (use Missing webhook data).

**Example:** "We never received the webhook for this entity creation event — our system now shows a status mismatch."

**Likely keywords:** webhook didn't arrive, signature verification failed, delivery latency, missed webhook, entity creation, status mismatch, failed to sync capture

#### Reason: Missing webhook data

**Applies if the customer:** Reports inconsistent or incomplete metadata in a delivered webhook (such as a **missing orderId**), or specifically points out the **Payload Data Format** doesn't match their expectations. Applies when the webhook was successfully delivered, but the content inside was incomplete or incorrect.

**Does not apply if the customer:** Reports the webhook never arrived at all (use Signature verification or delivery failure).

**Example:** "The webhook arrived but the orderId field is missing from the payload."

**Likely keywords:** missing field in webhook, incomplete payload, orderId missing, payload data format

### Issue Type: Test environment

The issue involves transaction failures, configuration problems, or testing specifically within the **Sandbox/Test environments**.

**Applies if the customer:** Asks about an issue in the non-production/testing environment, including Sandbox SFTP/access requests.

**Does not apply if the customer:** Is asking a general "Inquiries" question unrelated to Sandbox/testing — there is no "Inquiries" Issue Type under Technical issue; that belongs to General.

**Likely keywords:** sandbox, test environment, sandbox SFTP access

#### Reason: Sandbox issue

**Applies if the customer:** Has an issue about the non-production/testing environment.

**Likely keywords:** sandbox error, test environment issue

---

## Case Type: Data and analytics

Refers to issues about reports, either from the Dashboard or via SFTP. Includes issues about how to get a report and issues with report data.

**Applies if the customer:**
- Reports a report that's missing, incorrect, not generated, has a data mismatch, or has a time-range/filter/SFTP-delivery issue ("report data vs access").
- Asks which report/API field shows **NT (Network Token) status**, or reports an **NT flag mismatch between systems** ("network tokens reporting").
- Reports a reconciliation issue caused by a **data format/export problem** — **Excel truncation, unreadable ARNs, missing columns, encoding issues** ("data quality").
- Asks what an unfamiliar or newly-introduced report field/category means (see proposed Reason below).

**Does not apply if the customer:**
- Reports a financial/balance reconciliation problem — a wrong settlement amount or a mismatch between their balance and their bank statement — with no data-format/export defect involved (use Funds and fees → Settlements → Reconciliation issue).
- Has a card-issuing-specific settlement or report mismatch (use Card issuing → Issuing transactions, funds and reports → Issuing settlement & reconciliation).

**Likely keywords:** report, dashboard export, SFTP, data mismatch, missing data, custom report, NT status field, Excel truncation, encoding issue

### Issue Type: Reporting

Queries about reports and data within.

**Applies if the customer:**
- Is unable to generate, download, or access a report for any reason.
- Reports a discrepancy or data gap — including an **NT status field/flag mismatch** between systems, or a **data-format/export quality problem** (Excel truncation, unreadable ARNs, missing columns, encoding issues) that's causing a reconciliation issue.
- Requires a custom dataset/column configuration not available by default.
- Asks about reporting via SFTP.

**Does not apply if the customer:** Reports a financial/balance reconciliation problem with no data-format/export defect involved (use Funds and fees → Settlements → Reconciliation issue).

**Likely keywords:** report not generated, missing report, data mismatch, custom report, SFTP, NT flag mismatch, Excel truncation, unreadable ARN

#### Reason: Report not generated / missing

**Applies if the customer:** Is unable to successfully generate, download, or access a specific report — file availability, download failures, missing formats, or manual-extraction requests due to dashboard access limitations.

**Likely keywords:** report won't generate, can't download report, report missing

#### Reason: Data mismatch / missing data

**Applies if the customer:**
- Reports a discrepancy or data gap in reports.
- Asks which report/API field shows NT (Network Token) status, or reports an NT flag mismatch between systems.
- Reports a reconciliation issue caused by a data format/export problem — Excel truncation, unreadable ARNs, missing columns, or encoding issues.

**Does not apply if the customer:**
- Is asking what an unfamiliar field or category means, without claiming a discrepancy (use New or unexplained report field — proposed).
- Is reporting a financial/balance mismatch (wrong settlement amount, balance vs bank statement) with no data-format/export defect involved (use Funds and fees → Settlements → Reconciliation issue).

**Example:** "The ARNs in this export are unreadable and some columns are truncated in Excel — can you fix the format?"

**Likely keywords:** doesn't match, discrepancy, missing rows, wrong number, incorrect total, NT status mismatch, Excel truncation, unreadable ARN, encoding issue

#### Reason: Custom report request

**Applies if the customer:** Requires a specific dataset or column configuration not available by default.

**Likely keywords:** custom report, custom column, specific dataset

#### Reason: SFTP configuration

**Applies if the customer:** Asks about reporting using SFTP.

**Likely keywords:** SFTP setup, SFTP access, SFTP report delivery

#### Reason: New or unexplained report field **[Proposed addition]**

Identified during `/taxonomy-classification-qa` (2026-07-07) — not yet in `support-taxonomy.md`. Add to the source taxonomy before pasting into Intercom.

**Applies if the customer:**
- Asks what a new, unfamiliar, or recently-introduced field, category, or breakdown type in a report means.
- Asks how a value's sign or behavior works (e.g. whether it credits or debits) without claiming a discrepancy.
- Asks how they'll be informed of future categorisation/schema changes.

**Does not apply if the customer:**
- Is reporting that figures don't reconcile (use Data mismatch / missing data).
- Is requesting a report they can't access (use Report not generated / missing).

**Example:** "I've noticed a new 'Fee Tax' breakdown type in our reporting — what is this and does the sign matter?"

**Likely keywords:** new category, what is this field, breakdown type, categorisation change, new field meaning

---

## Case Type: Platforms

Covers Independent Software Vendors (ISVs) using Checkout.com's Integrated Platforms product to embed payments. Includes sub-merchant onboarding and fund distribution for marketplace/platform merchants.

**Applies if the customer:** Is explicitly dealing with a marketplace/ISV and its sub-merchants — splits/transfers or sub-merchant onboarding.

**Does not apply if the customer:**
- Is a Platform-segment merchant contacting about a general payments/technical/account issue with no sub-merchant or marketplace-splits context. **This is the "Platform trap"** — use this Case Type ONLY when explicitly dealing with a marketplace/ISV and its sub-merchants; do not use it as a catch-all for any Platform-segment merchant's contact. Route by the actual topic (Accepting payments, Technical issue, etc.) instead.

**Likely keywords:** sub-merchant, marketplace, ISV, KYC, splits, transfers, platform merchant onboarding

### Issue Type: Sub-merchant onboarding

Queries about onboarding merchants.

**Applies if the customer:**
- Has an issue related to KYC, verification, or creation of a sub-merchant.
- Reports a sub-merchant document upload error.

**Likely keywords:** sub-merchant KYC, merchant verification, document upload error

#### Reason: Merchant activation and verification

**Applies if the customer:** Has an issue related to the KYC, verification, or creation of a sub-merchant.

**Likely keywords:** sub-merchant KYC, activation, verification

#### Reason: Doc upload error

**Applies if the customer:** Has an issue related to the sub-merchant document upload.

**Likely keywords:** document upload failed, upload error sub-merchant

### Issue Type: Transfers & splits

Queries about transfers to merchants.

**Applies if the customer:** Reports funds were not distributed correctly between the platform and sub-merchant.

**Likely keywords:** split failed, transfer failed, funds not distributed

#### Reason: Transfer or split failed

**Applies if the customer:** Reports funds were not distributed correctly between the platform and sub-merchant.

**Likely keywords:** transfer failed, split failed

---

## Case Type: Card issuing

Refers to card issuing related queries. Includes physical or virtual card issues and controls on these cards.

**Includes:**
- **Card Management**: create/activate issued cards, revoke/suspend, spend controls.
- **Logistics**: physical card delivery.

**Applies if the customer:**
- Asks about managing an issued card (create/activate, revoke/suspend, spend controls), card deliveries, adding an issued card to a digital wallet, the Issuing mobile SDK, or issuing transactions/funds/reports.
- Provides an ID matching the regex `^trx_[a-z0-9]{26}$` — this is an issued-card transaction ID and is a strong signal this Case Type applies.

**Does not apply if the customer:**
- Asks about BIN lookup, BIN expansion, issuer identification, or card scheme/issuer metadata inquiries — these are general inquiries, not issued card lifecycle actions (use General → Inquiries → Reference data request).
- Reports acquiring-side MCC restrictions on processing channels (`pc_*` IDs) — these are not issued-card spend controls; select Technical issue instead.
- Provides an ID matching the regex `^(pay)_(\w{26})$` — a `pay_` ID is an acquiring/acceptance-side transaction, not an issued-card transaction; do not treat it as evidence for this Case Type.
- Asks about sending a payout via a card network (e.g. Visa Direct, Mastercard Send) to an end recipient — that's Payouts → Card payouts, not an issued-card lifecycle action, even though both mention "card."
- Is a merchant asking about onboarding a website domain for Apple Pay/Google Pay acceptance, or a domain-registration error on the acceptance side — that's Technical issue → Wallets, not an issued-card wallet-provisioning issue.

**Likely keywords:** issued card, virtual card, physical card, issuing balance, issuing SDK, trx_, activate card, revoke card, spend control, card delivery

### Issue Type: Card management

Queries about managing cards.

**Applies if the customer:**
- Is having trouble setting up or enabling a new card.
- Needs to cancel or temporarily freeze an active card.
- Asks about adjusting limits or blocking specific categories (**MCC**).

**Likely keywords:** activate card, freeze card, spend control, MCC block

#### Reason: Create / activate card

**Applies if the customer:** Is having trouble setting up or enabling a new card.

**Likely keywords:** create card, activate card

#### Reason: Revoke / suspend

**Applies if the customer:** Needs to cancel or temporarily freeze an active card.

**Likely keywords:** cancel card, freeze card, suspend card

#### Reason: Spend controls

**Applies if the customer:** Asks about adjusting limits or blocking specific categories (MCC).

**Likely keywords:** spend limit, MCC block, spend control

### Issue Type: Card deliveries

Queries about card deliveries.

**Applies if the customer:** Is checking status or reporting a card lost in the mail.

**Likely keywords:** card delivery status, lost card in mail

#### Reason: Physical card delivery

**Applies if the customer:** Is checking status or reporting a card lost in the mail.

**Likely keywords:** physical card delivery, card lost in mail

### Issue Type: Issuing digital wallets

Queries about adding issued cards to Apple Pay or Google Pay.

**Applies if the customer:** Cannot add their issued card to Apple Pay or Google Pay, or the card is not working correctly in their digital wallet (e.g. **provisioning failures, token errors**).

**Does not apply if the customer:** Is a merchant asking about onboarding a website domain for Apple Pay/Google Pay acceptance, or a domain-registration error on the acceptance side — that's Technical issue → Wallets, not an issued-card wallet-provisioning issue.

**Likely keywords:** issued card Apple Pay, issued card Google Pay, provisioning failure, token error

#### Reason: Apple Pay / Google Pay

**Applies if the customer:** Cannot add their issued card to Apple Pay or Google Pay, or the card is not working correctly in their digital wallet (e.g. provisioning failures, token errors).

**Likely keywords:** can't add issued card to wallet, provisioning failure, token error

### Issue Type: Issuing mobile SDK

Queries about the Issuing mobile SDK.

**Applies if the customer:** Is integrating, upgrading, or troubleshooting the Issuing mobile SDK.

**Likely keywords:** issuing SDK, SDK upgrade, SDK integration

#### Reason: Issuing SDK integration / upgrade

**Applies if the customer:** Is integrating, upgrading, or troubleshooting the Issuing mobile SDK.

**Likely keywords:** issuing SDK integration, SDK upgrade

### Issue Type: Issuing transactions, funds and reports

Questions about card transactions, settlement, fees, or balance.

**Applies if the customer:**
- Has questions about card funding balance, available funds per currency, insufficient funds errors, or **operational reserves**.
- Has questions about issuing settlement timing, report mismatches, or reconciliation issues.
- Has questions about issuing fees (**Interchange, scheme fees, CKO fees**).
- Needs to understand why an issued card transaction was declined or behaved unexpectedly.

**Likely keywords:** issuing balance, issuing settlement, issuing fees, issued card declined, operational reserves

#### Reason: Issuing balance

**Applies if the customer:** Has questions about card funding balance, available funds per currency, insufficient funds errors, or operational reserves.

**Likely keywords:** issuing balance, insufficient funds, funding balance, operational reserves

#### Reason: Issuing settlement & reconciliation

**Applies if the customer:** Has questions about issuing settlement timing, report mismatches, or reconciliation issues.

**Likely keywords:** issuing settlement, issuing reconciliation

#### Reason: Issuing fees

**Applies if the customer:** Has questions about issuing fees (Interchange, scheme fees, CKO fees).

**Likely keywords:** issuing fee, interchange fee issued card, CKO fee

#### Reason: Issuing transaction declined / unexpected behavior

**Applies if the customer:** Needs to understand why an issued card transaction was declined or behaved unexpectedly.

**Likely keywords:** issued card declined, unexpected card behavior

---

## Case Type: Account management and access

Access to the Dashboard/Portal, or structural changes to the **production account** — login, missing permissions, audit logs, and account configuration (e.g. bank accounts). Also covers requests to add/enable/configure Payment Methods (Amex, SEPA, APMs), currencies, schemes, processing channels, or billing/statement descriptors. **Only use when the merchant explicitly requests a change to their own account settings.**

**Applies if the customer:**
- Can't log in, has 2FA/MFA/SSO issues, needs permission changes, needs activity/audit evidence, or reports a Checkout Dashboard UI failure (pages not saving, blank pages, broken buttons) — regardless of whether login is involved.
- Requests to add, enable, or configure a payment method (e.g. Amex, SEPA, APMs), currency, scheme, MID, or processing channel, or update billing/statement descriptors ("enablement").
- Reports the primary blocker is access/permissions — can't access/view/download a report or section, missing permission ("access blockers").
- Requests pricing changes, account settings updates (bank account change, legal entity updates), or terminations — in the production environment.

**Does not apply if the customer:**
- Is asking about the sandbox/test environment (use Technical issue).
- Reports a decline on an already-enabled method, even if "setup"/"configuration" is mentioned (use Accepting payments).
- Has an API-key issue, including keys missing after a reset (use Technical issue → API keys).
- Asks an integration-approach/API-capability question (use Technical issue → API integration).
- Is internal Checkout staff coordination, migration logistics, or call scheduling with no merchant action requested (use Non-merchant requests).

**Likely keywords:** login, 2FA, MFA, SSO, user permissions, activity evidence, dashboard not saving, blank page, broken button, enable payment method, Amex, SEPA, APM, billing descriptor, bank account change, legal entity update, pricing change, terminate account, production account

### Issue Type: Login & access

2FA/login/MFA errors, user permissions, SSO configuration, activity evidence, adding/removing users, dashboard access/ownership, and Checkout Dashboard UI failures.

**Applies if the customer:**
- Cannot enter the Dashboard due to password issues, MFA/2FA problems, SSO errors, or requires assistance setting up or troubleshooting **SAML/Single Sign-On** configuration.
- Is adding/removing merchant users, or changing what a specific merchant user can see/do.
- Wants activity or audit evidence of who performed which action in the portal.
- Reports dashboard access or ownership issues.
- Reports a Checkout Dashboard UI failure — **pages not saving, blank pages, broken buttons** — **regardless of whether login is involved.** This includes pages showing "Unable to load," transaction details not opening, or specific Dashboard sections returning errors.

**Does not apply if the customer:**
- Reports a permission-related access issue rather than a login failure (use User permissions, not Login error / MFA / SSO).
- Is asking about a sandbox/test-environment issue (use Technical issue).

**Likely keywords:** can't log in, password reset, 2FA, MFA, SSO, SAML, user permissions, activity evidence, audit log, dashboard access, dashboard ownership, page not saving, blank page, broken button, unable to load

#### Reason: Login error / MFA / SSO

**Applies if the customer:** Cannot enter the Dashboard due to password issues, MFA/2FA problems, SSO errors, or requires assistance setting up or troubleshooting SAML/Single Sign-On configuration.

**Likely keywords:** can't log in, forgot password, 2FA issue, MFA issue, SSO error, SAML setup

#### Reason: User permissions

**Applies if the customer:** Is adding/removing merchant users, or changing what a specific merchant user can see/do.

**Likely keywords:** add user, remove user, permission change, what can this user see

#### Reason: Dashboard user audit evidence

**Applies if the customer:** Wants activity or audit evidence of who performed which action in the portal.

**Likely keywords:** audit log, who did this, portal action history, activity evidence

#### Reason: Dashboard error

**Applies if the customer:** Reports a Checkout Dashboard UI failure — pages not saving, blank pages, broken buttons — regardless of whether login is involved. Includes pages showing "Unable to load," transaction details not opening, or specific Dashboard sections returning errors.

**Does not apply if the customer:** Has a login/authentication failure (use Login error / MFA / SSO) or a permission-related access issue (use User permissions).

**Example:** "The transaction details page shows 'Unable to load' every time I click into it — I am logged in fine." / "The save button on this settings page just doesn't do anything."

**Likely keywords:** dashboard won't load, page won't save, blank page, broken button, unable to load, section broken

### Issue Type: Account changes

Pricing changes, account settings updates (bank account change, legal entity updates), terminations, and general account setup and configuration **in the production environment**.

**Applies if the customer:**
- Is requesting to update their contract or commission rates (pricing changes).
- Requests an account settings update: **bank account change, legal entity updates**, configuring processing channels (e.g. new MIDs, environment setup), retrieving account identifiers tied to their own account (e.g. **MID, CID, BINs, MCCs, entity-to-channel mappings**), or changing account status (e.g. activation, restriction) — **in the production environment**.
- Explicitly asks to terminate or close their account.
- Has a general account setup/configuration request in production.

**Does not apply if the customer:**
- Is asking about the **sandbox or test environment** — select Technical issue instead.
- Has an API-key mechanics issue (creating, editing, missing keys) — route to Technical issue → API keys, even if framed as "account configuration."
- Reports a decline on an already-enabled method — use Accepting payments, even if "configuration" is mentioned.
- Is an internal Checkout staff coordination thread, migration logistics, or call-scheduling thread with no merchant action requested — that belongs to Non-merchant requests.
- Requests external/reference identifier data not tied to their own account — BIN ranges, issuer identification, scheme metadata, or Checkout's own acquirer ID/BIN sponsor/scheme IDs (use General → Inquiries → Reference data request instead).

**Likely keywords:** pricing change, commission rate, bank account change, legal entity update, MID setup, CID, environment setup, BIN, MCC, entity-to-channel mapping, billing descriptor, activation, restriction, terminate account, close account, production account setup

#### Reason: Pricing change

**Applies if the customer:** Is requesting to update their contract or commission rates.

**Likely keywords:** pricing change, commission rate, contract update

#### Reason: Account settings update

**Applies if the customer:** The request involves a bank account change, legal entity update, configuring processing channels (e.g. new MIDs, environment setup), retrieving account identifiers tied to their own account (e.g. MID, CID, BINs, MCCs, entity-to-channel mappings), or changing account status (e.g. activation, restriction) — in the production environment.

**Does not apply if the customer:** Requests external/reference identifier data not tied to their own account — BIN ranges, issuer identification, scheme metadata, or Checkout's own acquirer ID/BIN sponsor/scheme IDs (use General → Inquiries → Reference data request instead).

**Likely keywords:** bank account change, legal entity update, new MID, CID, environment setup, BIN, MCC lookup, entity-to-channel mapping, billing descriptor value, account status change

#### Reason: Terminations

**Applies if the customer:** Explicitly asks to terminate or close their account.

**Likely keywords:** terminate account, close account

---

## Case Type: Feedback

Sentiment and product suggestions. Not a support query — no resolution required.

**Applies if the customer:** Provides feedback about existing features, or asks how to use/request a feature.

**Likely keywords:** feature request, feedback, suggestion

### Issue Type: Product feedback

Queries about providing feedback about the features offered by Checkout and how to request or use them.

**Applies if the customer:**
- Suggests a new functionality that does not currently exist.
- Asks "How do I use this existing feature?"

**Likely keywords:** feature request, how do I use, suggestion

#### Reason: Feature request

**Applies if the customer:** Suggests a new functionality that does not currently exist.

**Likely keywords:** feature request, wish this existed

#### Reason: Feature usage

**Applies if the customer:** Asks "How do I use this existing feature?"

**Example:** "How do I use this existing feature?"

**Likely keywords:** how do I use, how does this feature work

---

## Case Type: Compliance and audit

Refers to requests for documentation for audit/compliance purposes, including PCI, AOC, sensitive data, and other compliance docs.

**Applies if the customer:** Requests security compliance certificates, formal audit evidence, or sensitive/protected cardholder data, typically for legal/regulatory purposes.

**Likely keywords:** PCI, AOC, audit evidence, due diligence questionnaire, sensitive data request

### Issue Type: Compliance evidence

Queries about requesting compliance documentation from Checkout.

**Applies if the customer:**
- Asks for security compliance certificates (**AOC/PCI-DSS**).
- Asks for formal audit evidence or due diligence questionnaires.
- Requests sensitive customer information such as full PAN (**Primary Account Number**), unmasked card numbers, or other protected cardholder data, typically in response to legal authorities, law enforcement, regulatory bodies, or court orders.
- Requests another compliance document not covered above.

**Does not apply if the customer:** Requests deletion, access, or correction of their own personal/identity-verification data under GDPR (use Identity Verification → Security, privacy and compliance → Data privacy) — this Issue Type covers Checkout-held cardholder/PAN data typically requested for law enforcement or audit, not the requester's own personal data rights.

**Likely keywords:** PCI DSS certificate, AOC, audit questionnaire, unmasked PAN, compliance document

#### Reason: PCI / AOC request

**Applies if the customer:** Asks for security compliance certificates (AOC/PCI-DSS).

**Likely keywords:** PCI certificate, AOC request

#### Reason: Audit request

**Applies if the customer:** Query is for formal audit evidence or due diligence questionnaires.

**Likely keywords:** audit evidence, due diligence questionnaire

#### Reason: Sensitive data request

**Applies if the customer:** Requests sensitive customer information such as full PAN (Primary Account Number), unmasked card numbers, or other protected cardholder data, typically in response to legal authorities, law enforcement, regulatory bodies, or court orders.

**Does not apply if the customer:** Requests deletion, access, or correction of their own personal/identity-verification data under GDPR (use Identity Verification → Security, privacy and compliance → Data privacy).

**Likely keywords:** full PAN, unmasked card number, law enforcement request

#### Reason: Other compliance docs

**Applies if the customer:** Requests a compliance document not covered by PCI/AOC, audit, or sensitive data requests. (No further condition is specified in the source taxonomy beyond the Issue Type description — treat as the catch-all within Compliance evidence.)

**Likely keywords:** other compliance document

---

## Case Type: General

Refers to general inquiries which do not fit other case types.

**Includes:** sales inquiries, spam, duplicate tickets (no action needed), empty/OOO/no-action messages, and requests for BIN ranges, issuer identification, scheme metadata, or card categorisation reference data. Also includes requests for Checkout's acquirer ID, BIN sponsor, merchant identifiers, or scheme IDs needed for local tax authority or regulatory reporting.

**Applies if the customer:**
- Wants to buy services, is a sales prospect, or the contact is spam/duplicate/no-action.
- Requests BIN ranges, issuer identification, scheme metadata, or card categorisation reference data.
- Requests Checkout's own acquirer ID, BIN sponsor, merchant identifiers, or scheme IDs needed for local tax authority or regulatory reporting.

**Does not apply if the customer:**
- Requests reference/configuration data tied to their own account — MID, CID, or entity-to-channel mappings (use Account management and access → Account changes → Account settings update instead).
- Flags a specific data-accuracy dispute on a BIN/issuer value already returned for a transaction or card — that's Technical issue → Card Metadata → BIN/Issuer data, not a general reference-data request.

**Likely keywords:** sales inquiry, spam, duplicate, follow up, no action needed, BIN range, issuer identification, scheme metadata, acquirer ID, BIN sponsor, tax reporting identifier

### Issue Type: Inquiries

Queries about buying our services or Sales or anything else, or requests for external/reference identifier data not tied to the merchant's own account configuration.

**Applies if the customer:**
- Is a prospect wanting to buy services or add new products.
- Sent a ticket that is spam, empty, a follow-up, an OOO reply, or an accidental double-post.
- Presents as a superficially genuine query (e.g. payout status) but is non-actionable, unresolvable, or a duplicate/follow-up with no real request.
- Requests BIN ranges, issuer identification, scheme metadata, card categorisation reference data, or Checkout's own acquirer ID/BIN sponsor/merchant identifiers/scheme IDs for tax or regulatory reporting.

**Does not apply if the customer:**
- Requests reference/configuration data tied to their own account (MID, CID, entity-to-channel mappings) — use Account management and access → Account changes → Account settings update instead.

**Likely keywords:** sales inquiry, buy services, spam, duplicate, OOO reply, no action needed, BIN range, issuer identification, scheme metadata

#### Reason: Sales inquiry

**Applies if the customer:** Is a prospect who wants to buy services or add new products.

**Likely keywords:** interested in your services, want to add product, sales question

#### Reason: Spam / duplicate / no action / follow ups

**Applies if the ticket:** Is spam, empty, a follow up, an OOO reply, or an accidental double-post — including contacts that superficially look like a genuine query but carry no actionable request.

**Likely keywords:** spam, duplicate ticket, OOO reply, follow up only, no action needed

#### Reason: Reference data request

**Applies if the customer:**
- Requests BIN ranges, issuer identification, scheme metadata, or card categorisation reference data.
- Requests Checkout's own acquirer ID, BIN sponsor, merchant identifiers, or scheme IDs needed for local tax authority or regulatory reporting.

**Does not apply if the customer:**
- Requests reference/configuration data tied to their own account — MID, CID, or entity-to-channel mappings (use Account management and access → Account changes → Account settings update instead).
- Flags a specific data-accuracy dispute on a BIN/issuer value already returned for a transaction or card (e.g. "this issuer name looks wrong") — that's Technical issue → Card Metadata → BIN/Issuer data, not a reference-data request.

**Example:** "Can you confirm Checkout's acquirer ID and BIN sponsor? Our tax authority needs it for a filing." / "What's the issuer identification for this BIN range?"

**Likely keywords:** BIN range, issuer identification, scheme metadata, acquirer ID, BIN sponsor, tax reporting, regulatory reporting, card categorisation reference data

---

## Case Type: Identity Verification

Refers to the Identity Verification (IDV) product and services, which use document checks, facial recognition, and automation (**with manual review where needed**) to verify a person's identity. Merchants use IDV for onboarding, KYC compliance, and fraud prevention.

**Applies if the customer:**
- Has a query about verification results, data privacy requests, platform configuration, or technical issues related to the IDV product.
- Has a query about IDV configuration/onboarding, IDV technical/platform issues, IDV-related privacy/security/compliance, or a formal complaint about the IDV service.

**Does not apply if the customer:**
- Asks about form/checkout fields in the **merchant's own website integration**. IDV covers the Checkout.com IDV product (document checks, facial recognition) — it does not cover merchant-side data-capture fields, which belong in **Technical issue**.

**Likely keywords:** identity verification, IDV, document check, facial recognition, KYC verification, manual review

### Issue Type: Verification and technical support

Review rejected verifications, update configurations, and resolve technical errors.

**Applies if the customer:**
- Has a query about specific identity verification results, including requests to correct extracted data (**name, DOB**), re-verification due to suspected fraud, understanding why a verification was rejected, or inquiries about a specific IDV ID.
- Has a query about IDV configuration and onboarding, including adding or removing accepted document types or countries, dashboard access, certificate management (**mTLS**), or customization options.
- Reports technical issues with the IDV platform, including verifications stuck in pending, document capture failures, API errors, webhook issues, or integration problems.

**Likely keywords:** verification rejected, IDV ID, re-verify, document types, dashboard access, mTLS, IDV stuck pending, IDV API error

#### Reason: Verification inquiry

**Applies if the customer:** Has queries about specific identity verification results, including requests to correct extracted data (name, DOB), re-verification due to suspected fraud, understanding why a verification was rejected, or inquiries about a specific IDV ID.

**Likely keywords:** verification rejected, correct my name, re-verify, IDV ID lookup

#### Reason: Setup support

**Applies if the customer:** Has queries about IDV configuration and onboarding, including adding or removing accepted document types or countries, dashboard access, certificate management (mTLS), or customization options.

**Likely keywords:** IDV setup, add document type, mTLS certificate, IDV onboarding, dashboard access

#### Reason: Technical & platform

**Applies if the customer:** Reports technical issues with the IDV platform, including verifications stuck in pending, document capture failures, API errors, webhook issues, or integration problems.

**Likely keywords:** IDV stuck pending, capture failure, IDV API error, IDV webhook issue

### Issue Type: Security, privacy and compliance

Submit requests related to data privacy rights, report security incidents, or request compliance documentation.

**Applies if the customer:**
- Has requests related to data privacy rights, including data deletion/erasure requests (**GDPR**), requests for copies of personal data, identity theft reports, or questions about privacy policy and data handling.
- Has queries about IDV account-level compliance, regulatory requirements, or compliance certifications.
- Has queries related to IDV security concerns, security incidents, or security certifications.

**Does not apply if the customer:** Requests full PAN, unmasked card numbers, or other protected cardholder data typically for law enforcement/audit purposes (use Compliance and audit → Compliance evidence → Sensitive data request).

**Likely keywords:** GDPR deletion, personal data copy, identity theft, IDV compliance, security incident

#### Reason: Data privacy

**Applies if the customer:** Has requests related to data privacy rights, including data deletion/erasure requests (GDPR), requests for copies of personal data, identity theft reports, or questions about privacy policy and data handling.

**Does not apply if the customer:** Requests full PAN, unmasked card numbers, or other protected cardholder data typically for law enforcement/audit purposes (use Compliance and audit → Compliance evidence → Sensitive data request).

**Likely keywords:** GDPR, data deletion, personal data request, identity theft report

#### Reason: Account & compliance

**Applies if the customer:** Has queries about IDV account-level compliance, regulatory requirements, or compliance certifications.

**Likely keywords:** IDV compliance, IDV regulatory question

#### Reason: Security

**Applies if the customer:** Has queries related to IDV security concerns, security incidents, or security certifications.

**Likely keywords:** IDV security incident, security certification

### Issue Type: Formal complaint

Submit a formal complaint about the identity verification service.

**Applies if the customer:** Submits a formal complaint about the IDV service requiring escalation or with legal/compliance implications.

**Likely keywords:** formal complaint, escalate IDV, legal complaint IDV

#### Reason: Formal complaint

**Applies if the customer:** Submits a formal complaint about the IDV service requiring escalation or with legal/compliance implications.

**Likely keywords:** formal complaint, escalate, IDV legal complaint

### Issue Type: N/A

Tickets that do not require action or do not fit other IDV issue types. **This is the documented default/"Other" Issue Type for the Identity Verification Case Type.**

**Applies if:**
- The ticket was submitted by or relates to a third party and does not require IDV team action.
- The ticket was generated automatically by a system and does not require manual action.
- The ticket is a follow-up to a previous request that has already been resolved.
- The ticket is a sales inquiry or lead rather than a support request.
- The issue was resolved by the merchant before agent intervention.
- The ticket is spam or irrelevant.

**Likely keywords:** third party, automated, follow up resolved, sales lead, self resolved, spam

#### Reason: 3rd party

**Applies if:** The ticket was submitted by or relates to a third party and does not require IDV team action.

#### Reason: Automated

**Applies if:** The ticket was generated automatically by a system and does not require manual action.

#### Reason: Follow up

**Applies if:** The ticket is a follow-up to a previous request that has already been resolved.

**Does not apply if:** The merchant resolved the current, not-yet-actioned issue themselves before any agent action was taken (use Self resolved).

#### Reason: Sales lead

**Applies if:** The ticket is a sales inquiry or lead rather than a support request.

#### Reason: Self resolved

**Applies if:** The issue was resolved by the merchant before agent intervention.

**Does not apply if:** The ticket is merely referencing or following up on a request Care already resolved in a prior interaction (use Follow up).

#### Reason: Spam

**Applies if:** The ticket is spam or irrelevant.

---

## Case Type: No action required

**Manual classification by agents only — not exposed as a Fin Attribute.** Applied to contacts requiring no Care response. No Issue Type descriptions or Reasons are defined for this branch (V4 taxonomy) — it exists purely as a manual disposition:
- **Duplicate**
- **Spam**
- **Sales Enquiry**

Excluded from Fin classification entirely; do not create a matching Fin Attribute value for this Case Type.

## Case Type: Non-merchant requests

**Manual classification by agents only — not exposed as a Fin Attribute.** Contacts originating from parties other than the merchant — routed or closed without standard support handling. No Issue Type descriptions or Reasons are defined for this branch (V4 taxonomy) — it exists purely as a manual disposition:
- **Cardholder Complaints**
- **Issuing Bank Requests**
- **Authorities**
- **Schemes**
- **TPA Requests**
- **Other**

Excluded from Fin classification entirely; do not create a matching Fin Attribute value for this Case Type.

**Note (2026-07-07):** Account management and access's updated definition explicitly routes internal Checkout staff coordination, migration logistics, or call-scheduling threads with no merchant action requested to this Case Type — reinforcing that this bucket isn't limited to cardholder/issuing-bank/authority contacts. `support-taxonomy.md` does not yet spell out this exclusion; flag if it should be added there too.

---

## Cross-cutting notes for whoever configures Fin Attributes

1. **Card payouts (under Payouts)** and **N/A (under Identity Verification)** are the only two documented default/"Other" values in the current taxonomy. Every other Issue Type list has no safe fallback — if Fin abstention shows up for a Case Type without one (flagged via `/taxonomy-classification-qa`'s `fin_abstention` gap_type), the fix is adding an explicit "Other/Uncategorized" Issue Type value there, not tuning a confidence setting.
2. **Reason-level abstention is invisible to standard QA math** — a QA run's `reason_match` accuracy stat treats "Fin left Reason blank" the same as "no ground truth to check against." Watch the `/taxonomy-classification-qa` fix hitlist's `fin_abstention` cluster for Reason-level entries specifically; they won't show up as a Reason accuracy drop.
3. When `/taxonomy-classification-qa` produces a new `ambiguous_boundary`, `wrong_scope`, or `missing_coverage` fix, update this file's corresponding Attribute value description directly (Applies if / Does not apply if / Likely keywords) and cross-check `support-taxonomy.md` for the same change.
