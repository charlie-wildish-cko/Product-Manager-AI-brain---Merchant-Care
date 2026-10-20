# Payment Search API — Field Descriptions

> Field-level reference for the Payment Search API response. Use this to understand what each field means and what values to expect.

## Top-level (`data`)

`id` — Unique payment identifier. Base32-encoded Charge ID.

`status` — Current payment status (e.g. Approved, Declined). Reflects the furthest lifecycle stage the payment has reached — a refund outranks a capture, which outranks a void, an authorisation, acceptance, and authentication — defaulting to "requested" if no later stage was reached. Sample values: captured, expired, hard_declined, partially_refunded, refunded, voided, requested, cancelled.

`amount` — The payment request amount, in its original currency.

`currency` — The original currency the payment was requested in (three-letter ISO 4217 code), e.g. GBP, USD, EUR.

`reference` — An optional merchant-supplied reference (such as an order ID) used to identify the charge. Also referred to as `track_id`.

`metadata` — Arbitrary key-value metadata attached to the payment by the merchant. Card only — always blank for APM payins.

`requested_on` — The time when the payment request was made.

`processing_channel_id` — The identifier of the processing channel. Sample values: `pc_6k7jcjztullutk6ahxsozrlw6q`, `pc_fqiy3ll3is6u7pvai3qacpkkbi`.

`response_code` — The latest relevant gateway response code for acceptance. For card payments, this is the authorisation response code if an authorisation exists, otherwise the authentication or risk-decline code. `not_available` when no acceptance event exists. For APMs, acceptance is measured at capture.

`response_summary` — Short description of the acceptance gateway response code, e.g. "Approved", "Request failed sanctions screening", "Balance reservation insufficient funds". "Not available" when no acceptance event exists.

`last_four_card_digits` — Last four digits of the card used for the payment.

`bin` — Bank Identification Number. First 6 digits of the card used for the payment.

`card_expiry_month` — Card expiry month, e.g. 12. Card only — always blank for APM payins.

`card_expiry_year` — Card expiry year, e.g. 2026. Card only — always blank for APM payins.

`issuer` — Name of the card-issuing bank. Sample values: `Al Rajhi Banking & Inv. Corp.`, `Barclays Bank Uk Plc`, `Lloyds Bank Plc`. Card only — always blank for APM payins.

`issuer_country` — Two-letter ISO 3166-1 alpha-2 country code of the card-issuing bank. Sample values: `US`, `GB`, `FR`, `AU`, `CA`. Card only — always blank for APM payins.

`avs_check` — Address Verification Service (AVS) result, comparing the cardholder-provided billing address against the issuer's records. Common values: `Y`/`D`/`M` (full match), `X` (full match incl. 9-digit postcode), `A`/`W`/`Z` (partial match), `N` (no match), `U` (unavailable), `S` (not supported), `P` (not applicable), `R` (system unavailable, retry). Card only — always blank for APM payins.

`card_scheme_local` — The local or domestic card scheme for co-badged cards, applied alongside the international scheme. Sample values: `mada` (Saudi domestic debit), `cartes_bancaires` (French domestic), `maestro`, `pulse`, `star`, `nyce`, `accel`, `omannet`. Blank when there is no local scheme and the transaction processed on the international scheme only. Card only — always blank for APM payins.

`payment_method` — For card payments: the card scheme (e.g. `visa`, `mastercard`, `cartes_bancaires`, `amex`, `dinersclub`). For alternative payment methods: the APM name (e.g. `klarna`, `knet`, `tamara`, `ach`, `stcpay`, `mbway`, `ideal`, `paypal`).

`scheme` — The name of the scheme used for acquiring (e.g. Visa, Mastercard). For co-badged cards, this reflects the scheme actually selected for routing — either the merchant's explicit preference or a fallback to the domestic scheme.

`card_type` — The scheme card type. Sample values: `Credit`, `Debit`, `Prepaid` (funds drawn from a pre-loaded balance), `Deferred Debit` (settled at month end), `Charge` (full balance paid each billing cycle), `Unknown` (the scheme did not return a type). Card only — always blank for APM payins.

`card_wallet_type` — The name of the electronic wallet associated with the card, e.g. `ApplePay`, `GooglePay`. Card only — always blank for APM payins.

`is_disputed` — Boolean indicating whether the payment has an open dispute.

`recommendation_code` — Risk recommendation code returned by the risk engine at authorisation. Provides guidance on how a declined transaction should be retried. Sample values: `01` (updated or additional information required), `02` (try again later), `03` (do not try again).

`total_authorized` — The total successfully-authorised amount on the payment, in its original currency. Sum across successful authorisation events.

`total_captured` — The total value of successful full and partial captures on the payment, in its original currency.

`total_refunded` — The total value of successful full and partial refunds on the payment, in its original currency. Does not include unreferenced refunds (standalone credits not linked to a prior capture).

`eci` — Electronic Commerce Indicator. Indicates the authentication assurance level and liability shift result achieved for the payment. Meaning varies by scheme — for Mastercard, `02`/`2` = 3DS successful with liability shift to issuer, `00`/`0` = 3DS failed or not attempted with merchant retaining liability; for Visa/Amex/Discover/JCB/DCI, `05`/`5` = 3DS successful with liability shift, `07`/`7` = exemption used or failed with merchant retaining liability. Card only — always blank for APM payins.

`three_ds_protocol_version` — The version of 3DS requested for authentication (e.g. 1 or 2). Does not guarantee the payment was processed with that version. Card only — always blank for APM payins.

`arn` — Acquirer Reference Number. A scheme-issued identifier the acquirer attaches to a card transaction for settlement reconciliation, retrieval requests, and dispute tracking. Length and format vary by scheme — Visa and Mastercard typically use a 23-character ARN; other schemes (e.g. Cartes Bancaires, Amex, JCB) use shorter formats, commonly 12 characters. Depending on the acquirer, this field can instead hold a Retrieval Reference Number (RRN) — a 12-digit numeric identifier generated by the acquirer and sent to the schemes as part of the authorisation request (see `transaction_retrieval_reference_number` below) — rather than a true ARN; check the value's format if the distinction matters. Card only — does not apply to APMs.

`payment_type` — An indicator that determines the type of charge as required by the card scheme. Sample values: `Regular`, `Recurring`, `Unscheduled`, `Installment`, `MOTO` (Merchant-Offline/Telephone Order).

`type` — Direction of the transaction: `payin` (funds moving from customer to merchant) or `payout` (funds moving from merchant to a recipient).

`authentication_status` — Outcome of the payment during the authentication (3DS) stage. Values: `authenticated`, `failed`, `expired`, `rejected`.

`risk_flagged` — Boolean indicating whether an authorisation on the payment was risk-flagged by the risk engine (corresponds to gateway response code 10100).

`risk_score` — Numerical risk score assigned to the payment by the risk engine (Fraud Detection, formerly Prism). Higher values indicate higher risk. Range 0–100. NULL for APM payments.

## `actions[]` (per-action detail)

Each payment can have multiple actions across its lifecycle (e.g. an authorisation followed by a capture, followed by a refund). This array holds one entry per action.

`id` — Identifier for the specific action within the payment.

`transaction_id` — Gateway-assigned identifier linking this action to its parent transaction. A payment can have several transactions, e.g. cascaded authorisation attempts.

`type` — Action type. Card sample values: `Authorization`, `Capture`, `Refund`, `Credit`, `Void`. APM sample values follow the same lifecycle stages (request, capture, refund, void, return).

`processed_on` — The time this specific action was processed by the gateway.

`status` — Outcome status of this action. Card sample values: `Authorised`, `Declined`, `Captured`, `Voided`, `Refunded`, `Pending`. APM sample values: `Pending`, `Captured`, `Deferred Capture`, `Expired`, `Authorised`, `Declined`, `Refunded`.

`amount` — Amount associated with this action, in the payment's original currency.

`auth_code` — Authorisation code returned by the issuer for this action.

`response_code` — Gateway response code for this specific action. Sample values: `10000` (Approved), `20005` (Declined - Do Not Honour), `20051` (Insufficient Funds).

`response_summary` — Short description of the gateway response code for this action.

`reference` — Merchant-supplied reference associated with this specific action. Formerly known as `track_id`.

`fraud_score` — Fraud score assigned to this action by the risk engine.

`authentication_experience` — The type of 3DS authentication flow used for this action. Sample values: `challenged` (cardholder actively verified, e.g. OTP/biometric), `frictionless` (authenticated silently), `frictionless_delegated` (delegated to the acquirer or third party), `decoupled` (authenticated independently of the payment session, e.g. via a banking app).

`reason_code` — Reason code explaining the action's outcome, e.g. a decline reason code, or a Merchant Advice Code recommending whether and how to retry (`01` updated/additional information required, `02` try again later, `03` do not try again).

`sanction_screening` — Result of sanction/AML screening applied to this action.

`processing.acquirer_reference_number` — Acquirer-assigned reference number for this action (see `arn` above for format details).

`processing.acquirer_transaction_id` — Acquirer-side transaction identifier returned for this action. Sample values: `51129720260622000000MCSGU15JB0621` (card), `193a13e3-bd3c-4036-8e9a-403b21e0f4d9` (APM).

`recommendation_code` — Risk recommendation code for this specific action, as returned by the scheme at authorisation.

`processing_channel_name` — Human-readable name of the processing channel used for this action.

`transaction_retrieval_reference_number` — Retrieval Reference Number (RRN). A 12-digit numeric identifier generated by the acquirer and sent to the card schemes as part of the authorisation request. Used by acquirers for settlement and dispute identification.

`scheme_merchant_id` — The Merchant Identification Number (MID) for the transaction. Identifies the business account receiving the funds; generated by the acquirer and used by the scheme for reporting and dispute workflows.

`card_acceptor_id` — The Card Acceptor Identification Code (CAID). Uniquely identifies a service establishment at a single geographic location; generated by the acquirer and passed to the scheme on the authorisation. Not applicable for APMs.

## `dispute_details`

Present only when a dispute has been raised against the payment.

`id` — Unique dispute identifier.

`status` — Current status of the dispute.

`reason` — Human-readable reason for the dispute, e.g. "Fraudulent transaction".

`reason_code` — Scheme-specific reason code for the dispute.

`initiated_on_date` — Date the dispute was raised by the cardholder.

`submit_evidence_by_date` — Deadline by which the merchant must submit dispute evidence.

`amount` — Disputed amount, in the payment's original currency.

`method` — Payment method involved in the dispute, e.g. "card".

`currency` — Currency of the disputed amount (three-letter ISO 4217 code).

`description` — Description of the disputed transaction.

`relevant_evidence` — List of evidence types relevant to contesting this dispute.

## `acquirer_response`

Raw response detail from the acquirer for each stage of the payment.

`authorisation_code` — Authorisation code returned by the acquirer.

`acquirer_response_code` — Raw response code returned by the acquirer for the authorisation. Otherwise, the acquirer response code of the first declined authorisation attempt.

`authorisation_description` — Human-readable description of the authorisation outcome from the acquirer.

`authorisation_codes` — List of all authorisation codes associated with this payment, in transaction-time order (e.g. where multiple authorisation attempts occurred, such as cascading retries).

`capture_code` — Acquirer response code for the capture action. Reflects the successful capture when one exists, otherwise the first declined capture attempt.

`capture_description` — Human-readable description of the capture outcome.

`refund_code` — Acquirer response code for the refund action. Reflects the successful refund when one exists, otherwise the first declined refund attempt.

`refund_description` — Human-readable description of the refund outcome.
