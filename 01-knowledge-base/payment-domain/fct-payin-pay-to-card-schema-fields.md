# fct_payin / fct_pay_to_card Schema Field Definitions

> dbt docs blocks (`{% docs %}`) defining every column on `fct_payin` (card and APM payins) and `fct_pay_to_card` (Pay to Card payouts). This file does not yet cover bank payouts (`fct_bank_payout_event`) — that schema exists in the source repo but hasn't been pulled in here yet. Use this as the authoritative field-level reference when defining or explaining a payin or Pay to Card field — do not paraphrase a field definition from memory if it exists here.
>
> Source of truth: [cko-bi/gcp-data-analytics-dbt](https://github.com/cko-bi/gcp-data-analytics-dbt/tree/main/models/payment/mart) `models/payment/mart/` — each dbt model has a `.sql` + `.yml` pair; the `.yml` holds the column definitions. When asked to update this doc and its schemas, pull from `models/payment/mart/`, not `docs/payment_docs.md` (the original source used to create this file, now superseded as the update source). Models present as of 2026-09-07: `fct_payin`, `fct_payin_event`, `fct_payin_daily`, `fct_card_payin_event`, `fct_apm_payin_event`, `fct_card_payout`, `fct_bank_payout_event`, `fct_dispute_event`, `fct_reported_fraud_event`, `fct_transaction_risk_analysis_payin`, `fct_unreferenced_refund`.
>
> Access: `github` MCP connector `get_file_contents` (owner `cko-bi`, repo `gcp-data-analytics-dbt`), or `gh api repos/cko-bi/gcp-data-analytics-dbt/contents/<path>` after `unset GITHUB_TOKEN` (a stale env token overrides the working `gh` keyring auth).

# Primary Keys

{% docs payment_id %}
 
The unique identifier for a payment. For Payins, this is the Base32-encoded Charge ID. For Pay to Card payments, this is either the Base32-encoded Pay to Card token (on ABC) or the Base32-encoded GUID provided by Gateway (on NAS).

Sample values: `pay_mbabizu24eiu5amqpywkyl2rve`, `pay_y2q65lfkzi2urm7fditklvlufy`.

{% enddocs %}


# Foreign Keys

{% docs client_id %}

Identifier for the client - NAS only. e.g. cli_yichxtu4g4mudex75pthbhjkhq

{% enddocs %}


{% docs entity_id %}

The identifier for the NAS entity e.g. ent_22h2taklnoqral4oerffhacb2i

{% enddocs %}

{% docs sub_entity_id %}

This field is populated for merchants that segment processing under multiple sub-entities. It is an identifier for a sub-entity (sub-merchant) within a Payment Facilitator (PayFac) or platform/Marketplace hierarchy. Follows the same format as entity_id (e.g., ent_22czlzdw4jkvu3366x4be7cu34). Card only — always blank for APM payins.

{% enddocs %}

{% docs payfac_sub_entity_id %}

Payfac only — the sub-entity under which the payment was processed. For split/marketplace payments this is the first sub-entity on the request; for non-split payments it falls back to sub_entity_id.  Sample value: ent_22h2taklnoqral4oerffhacb2i.

{% enddocs %}

{% docs sub_entity_name %}

Name of the single sub-merchant the payment was processed under within a Payment Facilitator (PayFac) or Marketplace hierarchy.

{% enddocs %}

{% docs merchant_account_id %}

[Legacy field] Identifier number of the MBC merchant account e.g. 100135

{% enddocs %}


{% docs business_id %}

[Legacy field] Identifier number of the MBC business, e.g. 100005.

{% enddocs %}


{% docs channel_id %}

[Legacy field] The unique identifier of the channel e.g. 221621.

{% enddocs %}


{% docs processing_channel_id %}

The identifier of the processing channel. Sample values: pc_6k7jcjztullutk6ahxsozrlw6q, pc_fqiy3ll3is6u7pvai3qacpkkbi.

{% enddocs %}

{% docs segment_dimension_hash %}

Checkout.com-defined hash of the segment dimensions (brand, business category, market). Can be used to search payments by segment. Sample value: dih_undlkvbo4pwvvnfhlopkwtzvta.

{% enddocs %}

{% docs segment_name %}

Human-readable name of the merchant identity segment, typically a brand, merchant, or product label (e.g. `Vinted Pay`, `Mango pay`, `Lacoste-Ecom`, `Edenred France`).

{% enddocs %}


# Timestamps


{% docs requested_at %}

The time when a payment request was made.

{% enddocs %}


{% docs declined_at %}

The time when a payment request was declined. NULL for approved or pending payments.

{% enddocs %}

{% docs approved_at %}

The time when a payment request was approved. NULL for declined or pending payments.

{% enddocs %}


{% docs pay_to_card_outcome_at %}

The time when the payment outcome occurred. This will be the timestamp for when the payment request was either approved or declined. 

{% enddocs %}


# Merchant Category Code

{% docs mcc_used_payment_level %}

The Merchant Category Code (MCC) is a four-digit number used to describe a Merchant's primary business.

For Payins, this is the Merchant Category Code used in the latest successful authorisation if one exists, otherwise the most recent declined authorisation.

For Pay to Card payments, this is the Merchant Category Code used for the Payment. There can only be a single Merchant Category code associated to the payment.

Sample values:  `5411` (Grocery Stores), `5812` (Eating Places & Restaurants), `5816` (Digital Goods – Games), `7995` (Betting) etc.

{% enddocs %}

{% docs mcc_used_transaction_level %}

Merchant Category Code (4-digit ISO 18245) for the merchant on this transaction. Used to describe a Merchant's primary business.

Sample values:  `5411` (Grocery Stores), `5812` (Eating Places & Restaurants), `5816` (Digital Goods – Games), `7995` (Betting) etc.

{% enddocs %}

{% docs mcc %}
ISO 18245 4-digit Merchant Category Code is a four-digit number used to describe a Merchant's primary business.
Sample values:  `5411` (Grocery Stores), `5812` (Eating Places & Restaurants), `5816` (Digital Goods – Games), `7995` (Betting) etc.
{% enddocs %}


{% docs mcc_desc %}

The long description of the merchant category code used during payment e.g Miscellaneous Publishing and Printing.

{% enddocs %}

{% docs mcc_desc_transaction_level %}

The long description of the merchant category code used for the transaction e.g Miscellaneous Publishing and Printing.

{% enddocs %}


{% docs mcc_group %}

The business-defined Merchant Category Group used during payment. Sample values: Hotels & Accommodation, General Retail & High Street, Business & Professional Services, etc.

{% enddocs %}

{% docs industry_name %}

Industry of the merchant category code used during payment. Sample values:  Services, Hotel / Motel, Retail, etc.

{% enddocs %}

# Payment

{% docs request_correlation_id %}

The correlation identifier taken from the payment request event in Gateway. This is a payment-level field - used to trace the original payment request across Checkout services.

{% enddocs %}

{% docs is_gateway_services_only %}

Indicates whether Gateway Services Only is on for the payment. When true, Checkout.com is not involved in acquiring and settlement and is purely providing technical support; fraud reporting is not eligible.

{% enddocs %}

{% docs is_three_ds_requested %}

Indicates whether the payment is requested to be 3DS authenticated by the merchant. Does not mean the payment will be processed with 3DS. Card only — always blank for APM payins.

{% enddocs %}

{% docs business_model %}

The integrated-platform business model for the payment. Sample values: 'payfac' (the merchant operates as a payment facilitator, aggregating sub-merchants under a master account); 'marketplace' (the merchant operates a marketplace with multiple sub-entities sharing split payments); 'Payment Facilitator' (mapped value). Blank when neither model applies (standalone business). Card only — always blank for APM payins.

{% enddocs %}

{% docs is_gwc %}

Indicates whether the transaction took place on Gateway Core (GWC), the legacy Checkout.com gateway.

{% enddocs %}

{% docs is_nas %}

Indicates whether the merchant is registered on the New Account Structure (NAS — Checkout.com's modern account model) rather than the legacy ABC account structure.

{% enddocs %}


{% docs payment_currency_iso3 %}

The original currency the payment was requested in (ISO 4217 three-letter currency code). Sample values: GBP, USD, EUR.

{% enddocs %}

{% docs is_authentication %}

Indicates whether 3DS was initiated by Gateway. Does not include Sessions standalone or 3rd party 3DS providers. Card only — always blank for APM payins.

{% enddocs %}

{% docs is_captured %}

A flag to indicate if the payment was partially captured or captured. A payment is deemed to be partially captured if the total amount captured is less than the authorised amount.

{% enddocs %}

{% docs is_authorised %}

A flag to indicate if authorisation was successful.

{% enddocs %}

{% docs is_authorisation %}

A flag to indicate if authorisation was attempted.

{% enddocs %}

{% docs platform_name %}

The e-commerce platform or payment orchestrator that originated the payment. Recognised values include orchestrators (Payrails, Primer, BR-DGE, Yuno, Spreedly, Gr4vy), e-commerce platforms (Shopify, Magento, WooCommerce, BigCommerce, SFCC, Prestashop), and subscription platforms (Chargebee, Zuora, Recurly).

{% enddocs %}

{% docs is_accepted %}

A flag to indicate if the payment was accepted; authorised for card charge and captured for alternative charge.

{% enddocs %}

{% docs geographic_scope %}

Geographic scope is a calculated value, based on card scheme rules, which defines whether a transaction is considered domestic or cross-border. This field is not populated for MBC Pay to Card payments.

{% enddocs %}

{% docs funds_transfer_type %}

Returns Visa's BAI (Business Application Indicator) or Mastercard's TTI (Transaction Type Indicator). It defines the business purpose of the payment.

{% enddocs %}

{% docs purpose %}

The reason for the payment (e.g. Income, Gifts, LoanPayment).

{% enddocs %}

{% docs is_acceptance_retried %}

Flag to determine if the payment has a cascading retry or an SCA retry following a soft decline. Card only — always blank for APM payins.

{% enddocs %}

{% docs is_sca_retry %}

Flag to determine if the payment has an SCA retry following a 20154 soft decline.

{% enddocs %}

{% docs is_authorisation_reattempted %}

Flag to determine if the payment has more than one attempt at authorisation.

{% enddocs %}

{% docs scheme_transaction_id %}

The transaction identifier from Scheme VISA/Mastercard.

{% enddocs %}

{% docs retrieval_reference_number %}

Retrieval Reference Number (RRN) RRN, is a 12-digit numeric identifier, generated by the acquirer and sent to the card schemes as a part of the authorisation request. Used by acquirers for settlement and dispute identification.

{% enddocs %}

{% docs is_merchant_initiated %}

Indicates the seller initiated the payment on behalf of a customer without the need for additional 
cardholder authentication, e.g. installments, or recurring payments for subscriptions. Differentiates between Merchant-initiated Transaction (MIT) vs. Customer-Initiated Transaction (CIT). Card only — always blank for APM payins.

{% enddocs %}

{% docs is_card_on_file %}

Indicates the payment was made using card-on-file credentials — i.e. a previously stored card used either by the cardholder (CIT) or merchant (MIT) for a follow-up transaction. Card only — always blank for APM payins.

{% enddocs %}

{% docs transaction_event_data %}

Transaction-level information for troubleshooting and mapping back out to other sources.

{% enddocs %}

{% docs transaction_type %}

An indicator that determines the type of charge as required by the card scheme. Sample values: `Regular`, `Recurring`, `Unscheduled`, `Installment`, `MOTO` (Merchant-Offline/Telephone Order).

{% enddocs %}



# Payment Method

{% docs payment_method_name %}

For card payments: card scheme, e.g. visa, mastercard, cartes_bancaires, amex, dinersclub. For alternative payment methods: the APM, e.g. klarna, knet, tamara, ach, stcpay, mbway, klarna, ideal, paypal.

{% enddocs %}


{% docs is_apm %}

A flag to show if a payment was from an alternative payment method.

{% enddocs %}


# Card

{% docs card_type %}

The scheme card type. Sample values: `Credit`, `Debit`, `Prepaid` (funds drawn from a pre-loaded balance), `Deferred Debit` (settled at month end), `Charge` (full balance paid each billing cycle), `Unknown` (the scheme did not return a type). Card only — always blank for APM payins.

{% enddocs %}


{% docs card_verification_value_check %}

Result of the CVV security-code check returned by the issuer. Sample values: 'Y' (matched), 'D' (did not match), 'N' (should be present but not provided). Additional information: https://www.checkout.com/docs/developer-resources/codes/cvv-response-codes. Card only — always blank for APM payins.

{% enddocs %}


{% docs card_bin %}

The 6-digit card Bank Identification Number.  Sample value: `425860`. Card only — always blank for APM payins.

{% enddocs %}

{% docs card_network_token_type %}

The name of the network token type (which includes wallets) to which the card belongs. Sample values: 'VTS' (Visa Token Service), 'MDES' (Mastercard Digital Enablement Service), 'ApplePay', 'GooglePay'. Blank when the card was not presented via a network token. Card only — always blank for APM payins.

{% enddocs %}


{% docs billing_descriptor_name %}

The name of the billing descriptor. This is the text that is displayed on the customer's credit card statement identifying a purchase from a merchant's website. Not applicable for APM payments. Sample values: 1688.com, Netflix.com.

{% enddocs %}


{% docs issuing_country %}

The country in which the card issuer is based. Sample values: `United States`, `United Kingdom`, `France`, `Australia`, `Canada`. Card only — always blank for APM payins.

{% enddocs %}


{% docs issuing_country_iso2 %}

The two-letter ISO code (ISO 3166-1 alpha-2 code) of the country in which the issuer is based.  Sample values: `US`, `GB`, `FR`, `AU`, `CA`. Card only — always blank for APM payins.

{% enddocs %}


{% docs issuing_region %}

The region in which the issuer is based. Sample values: `North America`, `Europe`, `Asia and Pacific`, `Central and South America`, `Middle East and Africa`. Card only — always blank for APM payins.

{% enddocs %}


{% docs issuing_bank %}

The name of the bank from which the card was issued. Sample values: `Al Rajhi Banking & Inv. Corp.`, `Barclays Bank Uk Plc`, `Lloyds Bank Plc`. Card only — always blank for APM payins.

{% enddocs %}

{% docs card_token_format %}

The name of the token format type which was used when the payment was made, either pan_only or cryptogram_3ds. Card only — always blank for APM payins.

{% enddocs %}

{% docs billing_address_country_iso2 %}

The billing country associated to the card. Will be NULL if the customer has input country incorrectly. Card only — always blank for APM payins.

{% enddocs %}


{% docs card_fingerprint %}

A hash of the card number used to compare card numbers without exposing the PAN. Card only — always blank for APM payins. Sample values: `adcb9214966eb0cf23a1d4946e8c58d34acf`, `b18abf08b1a2c8e61a01b4ecf6a3e7b92dfa`.

{% enddocs %}

{% docs card_local_schemes %}

An array of the local card schemes associated with the card, for co-badged cards. Sample values: cartes_bancaires, omannet, maestro, nyce. Card only — always blank for APM payins.

{% enddocs %}

{% docs card_product_id %}

The scheme product identifier for the card, e.g., Platinum MasterCard® Card. Card only — always blank for APM payins.

{% enddocs %}

{% docs card_masked_number %}

 The masked card PAN, e.g. 424242******4242. Card only — always blank for APM payins.

{% enddocs %}

{% docs payout_card_holder_name %}

Full name of the cardholder or company receiving the payment. For individuals, this is a concatenation of first and last name. PII.

{% enddocs %}

{% docs payin_card_holder_name %}

The cardholder name associated to the card used for payment, as input by the customer. Card only — always blank for APM payins.

{% enddocs %}

{% docs card_wallet %}

The name of the electronic wallet to which the card belongs, i.e. ApplePay or GooglePay currently. Card only — always blank for APM payins.

{% enddocs %}



# Acquirer

{% docs global_acquirer_id %}

Card only, indicates the name of the global acquirer identifier. Sample value: `cko-visa`.

For Payins, this will be the global acquirer identifier of the selected authorisation transaction: the successful authorisation when one exists, otherwise the most recent declined attempt.

{% enddocs %}

{% docs acquirer_name %}

Name of the acquirer that processed the authorisation, Checkout.com or a third party e.g. Checkout MC. For APMs, can be NULL when no acquirer is specified. Sample values: `Checkout MC`, `Checkout Visa`, `Checkout Discover`. NULL for some APM payments.

{% enddocs %}


{% docs acquirer_country %}

The name of the country in which the acquirer is based. For APMs, can be NULL when no acquirer specified.  Sample values: `United States`, `France`, `United Kingdom`, `Hong Kong`, `United Arab Emirates`.

{% enddocs %}


{% docs acquirer_region %}

The region in which the acquirer is based. For APMs, can be NULL when no acquirer specified.  Sample values: `North America`, `Europe`, `Asia and Pacific`, `Middle East and Africa`.

{% enddocs %}


{% docs acquirer_country_iso2 %}

The two-letter ISO code of the country in which the acquirer is based. For APMs, can be NULL when no acquirer specified.  Sample values: `US`, `FR`, `GB`, `HK`, `AE`.

{% enddocs %}


{% docs acquirer_bin %}

The 6-digit acquirer Bank Identification Number. Sample values: 147243, 518489.

{% enddocs %}


{% docs legal_acquirer_name %}

The legal name of the acquiring entity. Sample values: Checkout SAS, Checkout Ltd., Cross River Bank, Checkout APAC Pte Ltd., Checkout MENA FZ LLC.

{% enddocs %}

# Merchant

{% docs card_acceptor_id %}

The Card Acceptor Identification Code (CAID) uniquely identifies a service establishment at a single geographic location. It is generated by the acquirer and passed to the scheme on the authorisation. Note: due to a historical data correction, values for transactions on or before 2025-02-06 17:00 UTC were copied from scheme_merchant_id; values after that date are the acquirer-provided card_acceptor_id. For ABC the business ID is returned; for NAS the ID relates to a processor. 'Not applicable' for APMs, and NULL for NAS Pay to Card.  Sample value: `771085`.

{% enddocs %}

{% docs scheme_merchant_id %}

The Merchant Identification Number (MID) for the transaction, identifies the business account receiving the funds, generated by the acquirer and used by the scheme for reporting and dispute workflows.

{% enddocs %}

# Request

{% docs request_merchant_reference %}

 A merchant-supplied reference string attached to the payment request. For cards, this is an optional reference (such as an order ID) a merchant can use to later identify the charge. Formally known as track_id. For APMs, this is the merchant business identifier.

{% enddocs %}

{% docs payment_request_origin %}

Indicates the origin of the payment request (e.g., **Flow Web**, **Hosted Payment Page Web**, **Payment Link Web**, **Flow Android/iOS**,  **Frames Web** or **Frames Android/iOS**). The value is primarily inferred from the header sent to the Gateway at the time of the request. To ensure data completeness in `fct_payin`, if the Gateway value is "Not available", this column is automatically enriched with the derived value from `request_origin_integration_name` where available. For a full description, lineage, and examples, see the [DataHub Glossary](https://datahub.zta.ckotech.co/glossaryTerm/urn:li:glossaryTerm:826ae06c-6bed-4c2c-adba-fbcefc5352e8/Documentation?is_lineage_mode=false). If you need to understand the usage of Flow enabled interfaces, please include the following request origin values: Flow Android, Flow Web, Flow iOS, Hosted Payment Page We and Payment Link Web.

{% enddocs %}

{% docs request_origin_integration_name %}

Derived origin of the payment request. Possible values are Flow Web, Payment Link Web, Hosted Payment Page Web, Frames Web, and Frames Android/iOS. The Frames Web/Android/iOS fields are derived using the card tokenised events generated by Frames and are updated daily. Flow Web, Payment Link Web, and Hosted Payment Page Web are derived using payment session API data. Use this field to get Flow/HPP/PL payments from 2024-01-27 to 2024-12-17 and Frames payments from 2023-01-27 onwards.

{% enddocs %}

# Authentication


{% docs address_verification_service_check %}

Address Verification Service (AVS) result, comparing the cardholder-provided billing address against the issuer's records. Common values: 'Y'/'D'/'M' (full match), 'X' (full match incl. 9-digit postcode), 'A'/'W'/'Z' (partial match), 'N' (no match), 'U' (unavailable), 'S' (not supported), 'P' (not applicable), 'R' (system unavailable, retry). See https://www.checkout.com/docs/developer-resources/codes/avs-codes for the full list. Card only — always blank for APM payins.

{% enddocs %}

{% docs authentication_electronic_commerce_indicator %}

The Electronic Commerce Indicator (ECI) returned at the authentication stage for this payment. Indicates the level of security used when the cardholder provided payment information. The scheme may downgrade the initial ECI at authorisation (see authorisation_electronic_commerce_indicator). Used for 3DS and Network Token payments.  Sample values: 05 (fully authenticated), 06 (attempted), 07 (non-secure). Indicates the level of authentication achieved.

{% enddocs %}

{% docs electronic_commerce_indicator %}

Electronic Commerce Indicator (ECI) indicating the authentication assurance level and liability shift result. Value meaning varies by scheme. Mastercard: '02'/'2' = 3DS successful, liability shifts to issuer. '01'/'1' = 3DS via stand-in, liability shifts to issuer. '07' = 3DS successful for recurring, liability shifts to issuer. '04' = frictionless via Identity Check Data Only, merchant retains liability. '06' = SCA-exempt, merchant retains liability. '00'/'0' = 3DS failed or not attempted, merchant retains liability. 'N0'/'N2' = non-payment authentication only. Visa/Amex/Discover/JCB/DCI: '05'/'5' = 3DS successful, liability shifts to issuer. '06'/'6' = 3DS via stand-in, liability shifts to issuer. '07'/'7' = 3DS exemption used or failed, merchant retains liability. Card only — always blank for APM payins.

{% enddocs %}

# Outcomes


{% docs pay_to_card_outcome %}

Outcome of the Payment Request: approved, balance reserved declined, sanction screening declined, manual decline or card processing declined.

{% enddocs %}

{% docs fraud_outcome %}

Whether the given payment_id has been reported as fraudulent by VISA or Mastercard; fraud vs non_fraud.

{% enddocs %}

{% docs capture_event_outcome %}

Describes the outcome of the capture event (partially captured, captured, declined, deferred, etc)

{% enddocs %}

{% docs void_event_outcome %}

Describes the outcome of the void event (voided, declined, partially voided, etc)

{% enddocs %}

{% docs refund_event_outcome %}

Describes the outcome of the refund event (refunded, declined, partially refunded, etc)

{% enddocs %}

# Gateway Response

{% docs gateway_response_code %}

The gateway response code of the approval or decline event. Sample values: 10000, 50002, 50003.

{% enddocs %}

{% docs payment_gateway_response_code %}

The gateway response code of the approval or decline event.

{% enddocs %}

{% docs payout_gateway_response_code_samples %}

Sample values: 10000 (Approved), 50003 (insufficient funds), 20093 (violation of law), 20059 (Suspected Fraud), 30046 (Closed account), 2005C (Refused by issuer).

{% enddocs %}


{% docs gateway_response_summary %}

The short description of the approval or decline gateway response code. For example; 'Approved', 'Request failed sanctions screening', 'Balance reservation insufficient funds'.

{% enddocs %}


{% docs is_internal_decline %}

Indicates whether the payment request was declined as part of logic internal to Checkout.

{% enddocs %}

{% docs authorisation_gateway_response_code %}

The gateway response code of the successful authorisation event. Otherwise, the gateway response code of the first declined authorisation. Codes starting with '1' indicate approval; other codes indicate a decline. Set to 'not_available' when the payment did not reach authorisation. Sample values: `10000` (Approved), `20005` (Declined - Do Not Honour), `20051` (Insufficient Funds).

{% enddocs %}

{% docs authorisation_gateway_response_summary %}

The short description of the authorisation gateway response code.

{% enddocs %}

{% docs latest_authorisation_gateway_response_code %}

The gateway response code of the most recent authorisation event. In the event of multiple declines, it may differ from the first declined authorisation.

{% enddocs %}

{% docs latest_authorisation_gateway_response_summary %}

The short description of the last authorisation gateway response code.

{% enddocs %}

{% docs return_gateway_response_code %}

The gateway response code of the returned event. APM only — always blank for card payins.

{% enddocs %}

{% docs return_gateway_response_summary %}

The short description of the return gateway response code. APM only — always blank for card payins.

{% enddocs %}

{% docs capture_gateway_response_summary %}

Short description of the capture gateway response code.

{% enddocs %}

{% enddocs %}

{% docs void_gateway_response_summary %}

The short description of the void gateway response code.

{% enddocs %}

{% enddocs %}

{% docs refund_gateway_response_summary %}

The short description of the refund gateway response code.

{% enddocs %}

{% docs risk_decline_gateway_response_code %}

The gateway response code of the pre-authorisation risk-decline event.

{% enddocs %}

{% docs risk_decline_gateway_response_summary %}

The short description of the risk-decline gateway response code.

{% enddocs %}

{% docs acceptance_gateway_response_code %}

The gateway response code associated with the acceptance event.  For APMs, acceptance is measured at capture. For card payments, this is the authorisation response code if an authorisation exists, otherwise the authentication or risk-decline code. It is 'not_available' when no acceptance event exists or when a non-authorisation event carries the default '10000'.

{% enddocs %}

{% docs acceptance_gateway_response_summary %}

The short description of the acceptance gateway response code. It is 'Not available' when no acceptance event exists or when a non-authorisation event carries the default '10000'.

{% enddocs %}

{% docs acceptance_gateway_response_code_list %}

An object containing arrays of gateway response codes at each lifecycle stage (risk, authentication, authorisation, void, capture) for the payment. Each key maps to an array of codes in transaction-time order; empty stages are NULL or empty arrays. The authentication array is always NULL for APM payments.

{% enddocs %}

{% docs void_gateway_response_code %}

The gateway response code of the first void event associated with the payment.

{% enddocs %}

{% docs void_outcome_at %}

The processing time of the earliest successful void if any, otherwise the decline time of the earliest void decline. NULL when the payment never reached a void event.

{% enddocs %}

{% docs latest_voided_at %}

The time of the latest successful void event on the payment.

{% enddocs %}

{% docs void_outcome %}

Outcome of the payment during the void stage.

{% enddocs %}

{% docs capture_gateway_response_code %}

Gateway response code for the capture event that determined the capture outcome. Reflects the successful capture when one exists, otherwise the earliest capture decline. 'not_available' when no capture event exists.

{% enddocs %}

{% docs refund_gateway_response_code %}

The gateway response code of the earliest successful refund when one exists, otherwise the earliest refund decline.

{% enddocs %}

# Measures

## Requests
{% docs requested_amount %}

The payment request amount in its original currency.

{% enddocs %}


{% docs requested_amount_usd %}

The payment request amount in US Dollars.

{% enddocs %}


{% docs requested_amount_eur %}

The payment request amount in Euros.

{% enddocs %}


{% docs requested_amount_gbp %}

The payment request amount in Sterling.

{% enddocs %}


{% docs requested_payments %}

Count of payment requests.

{% enddocs %}

## Authorisation

{% docs authorisation_payments %}

Count of payments where authorisation was attempted and either authorised or declined.

{% enddocs %}

{% docs authorised_payments %}

Count of payments which successfully authorised.

{% enddocs %}


## Acceptance
{% docs approved_amount %}

The approved amount in its original currency.

{% enddocs %}


{% docs approved_amount_usd %}

The approved amount in US Dollars.

{% enddocs %}


{% docs approved_amount_eur %}

The approved amount in Euros.

{% enddocs %}


{% docs approved_amount_gbp %}

The approved amount in Sterling.

{% enddocs %}


{% docs approved_payments %}

Count of approved payment requests.

{% enddocs %}

{% docs accepted_payments %}

Count of payments where the payment was accepted; authorised for card charge and captured for alternative charge.

{% enddocs %}

## Declines

{% docs declined_amount %}

The total value of payments where the payment request was declined, in its original currency.

For Payins, this is where the payment was declined during acceptance.

{% enddocs %}


{% docs declined_amount_usd %}

The total value of payments where the payment request was declined, in US Dollars.

For Payins, this is where the payment was declined during acceptance.

{% enddocs %}


{% docs declined_amount_eur %}

The total value of payments where the payment request was declined, in Euros.

For Payins, this is where the payment was declined during acceptance.

{% enddocs %}


{% docs declined_amount_gbp %}

The total value of payments where the payment request was declined, in Stirling.

For Payins, this is where the payment was declined during acceptance.

{% enddocs %}


{% docs declined_payments %}

Count of declined payment requests.

For Payins, this is where the payment was declined during acceptance, acceptance_outcome is either hard_declined, soft_declined, risk_declined, expired, cancelled or void.

{% enddocs %}


## Declines - Balance Reservation

{% docs balance_reserved_declined_amount %}

The total value of payments where the payment request failed at the Balance Reservation stage of the Pay to Card flow, in its original currency.

{% enddocs %}


{% docs balance_reserved_declined_amount_usd %}

The total value of payments where the payment request failed at the Balance Reservation stage of the Pay to Card flow, in US Dollars.

{% enddocs %}


{% docs balance_reserved_declined_amount_eur %}

The total value of payments where the payment request failed at the Balance Reservation stage of the Pay to Card flow, in Euros.

{% enddocs %}


{% docs balance_reserved_declined_amount_gbp %}

The total value of payments where the payment request failed at the Balance Reservation stage of the Pay to Card flow, in Sterling.

{% enddocs %}


{% docs balance_reserved_declined_payments %}

Count of payment requests declined at the Balance Reservation stage of the Pay to Card flow.

{% enddocs %}


## Declines - Sanction Screening

{% docs sanction_screening_declined_amount %}

The total value of payments where the payment request failed at the Sanctions Screening stage of the Pay to Card flow, in its original currency.

{% enddocs %}


{% docs sanction_screening_declined_amount_usd %}

The total value of payments where the payment request failed at the Sanctions Screening stage of the Pay to Card flow, in US Dollars.

{% enddocs %}


{% docs sanction_screening_declined_amount_eur %}

The total value of payments where the payment request failed at the Sanctions Screening stage of the Pay to Card flow, in Euros.

{% enddocs %}


{% docs sanction_screening_declined_amount_gbp %}

The total value of payments where the payment request failed at the Sanctions Screening stage of the Pay to Card flow, in Sterling.

{% enddocs %}


{% docs sanction_screening_declined_payments %}

Count of payment requests declined at the Sanctions Screening stage of the Pay to Card flow.

{% enddocs %}


## Declines - Card Processing

{% docs card_processing_declined_amount %}

The total value of payments where the payment request was declined at the Card Processing stage of the Pay to Card flow, in its original currency.

{% enddocs %}


{% docs card_processing_declined_amount_usd %}

The total value of payments where the payment request was declined at the Card Processing stage of the Pay to Card flow, in US Dollars.

{% enddocs %}


{% docs card_processing_declined_amount_eur %}

The total value of payments where the payment request was declined at the Card Processing stage of the Pay to Card flow, in Euros.

{% enddocs %}


{% docs card_processing_declined_amount_gbp %}

The total value of payments where the payment request was declined at the Card Processing stage of the Pay to Card flow, in Sterling.

{% enddocs %}


{% docs card_processing_declined_payments %}

Count of payment requests declined at the Card Processing stage of the Pay to Card flow.

{% enddocs %}

## Declines - Manual Decline

{% docs manual_decline_declined_amount %}

The total value of payments where the payment request was manually declined by an Analyst prior to the Card Processing stage of the Pay to Card flow, in its original currency.

{% enddocs %}


{% docs manual_decline_declined_amount_usd %}

The total value of payments where the payment request was manually declined by an Analyst prior to the Card Processing stage of the Pay to Card flow, in US Dollars.

{% enddocs %}


{% docs manual_decline_declined_amount_eur %}

The total value of payments where the payment request was manually declined by an Analyst prior to the Card Processing stage of the Pay to Card flow, in Euros.

{% enddocs %}


{% docs manual_decline_declined_amount_gbp %}

The total value of payments where the payment request was manually declined by an Analyst prior to the Card Processing stage of the Pay to Card flow, in Sterling.

{% enddocs %}


{% docs manual_decline_declined_payments %}

Count of payment requests manually declined by an Analyst prior to the Card Processing stage of the Pay to Card flow.

{% enddocs %}

## Time Lags

{% docs time_request_to_outcome_seconds %}

The number of seconds between the requested_at timestamp and the pay_to_card_outcome_at timestamp.

{% enddocs %}

## Fraud Report Eligible Captured

{% docs fraud_report_eligible_captured_events %}

Count of captured and partially captured events that are fraud report eligible.

{% enddocs %}

{% docs fraud_report_eligible_captured_amount %}

The value of captures and partial captures that are fraud report eligible in its original currency.

{% enddocs %}

{% docs captured_amount %}
The total value of successful full and partial captures on the payment, in its original currency.
{% enddocs %}

{% docs fraud_report_eligible_captured_amount_eur %}

 The value of captures and partial captures that are fraud report eligible in Euros.

{% enddocs %}

{% docs fraud_report_eligible_captured_payments %}

Count of payments where the payment was captured or partially captured and is fraud report eligible.

{% enddocs %}

{% docs fraud_report_eligible_captured_amount_usd %}

 The value of captures and partial captures that are fraud report eligible in US Dollars.

{% enddocs %}

{% docs fraud_report_eligible_captured_amount_gbp %}

The value of captures and partial captures that are fraud report eligible in Sterling.

{% enddocs %}


## Audit Fields

{% docs is_full_refresh %}

True if the data was inserted during a full refresh.

{% enddocs %}


{% docs pay_to_card_abc_ingestion_at %}

The latest timestamp that data was ingested to the Snowflake LANDING database for the ABC Pay to Card payment ID. 

{% enddocs %}


{% docs pay_to_card_nas_ingestion_at %}

The latest timestamp that data was ingested to the Snowflake SOURCE database for the NAS Pay to Card payment ID. 

{% enddocs %}


{% docs is_recurring %}

Indicates whether the payment was flagged as a recurring transaction at request time.

{% enddocs %}


{% docs is_split_payment_an_option %}

Indicates whether the payment supports split payments (true when one or more request sub-entities are present).

{% enddocs %}


{% docs is_three_ds_allow_upgrade %}

Indicates whether the payment request permits the payment to be upgraded to 3DS (e.g. by Intelligent Acceptance) even if not originally requested. Card only — always blank for APM payins.

{% enddocs %}


{% docs is_three_ds_protocol_version %}

Indicates whether a 3DS protocol version was specified in the payment request. Card only — always blank for APM payins.

{% enddocs %}


{% docs is_skip_risk_check_requested %}

Indicates whether the merchant requested to skip risk checks. Does not mean risk checks were actually skipped.

{% enddocs %}


{% docs is_risk_declined_capture %}

Indicates whether a capture on the payment was declined due to a pre-capture risk check. Card only — always blank for APM payins.

{% enddocs %}


{% docs is_partial_authorisation_requested %}

Indicates whether partial authorisation is enabled for the payment, allowing the issuer to approve a lesser amount than requested. Card only — always blank for APM payins.

{% enddocs %}


{% docs is_3ri %}

Indicates whether the payment went through 3D requester-initiated authentication (3RI), also known as merchant-initiated authentication — used for account verification and re-authentication of recurring payments. Card only — always blank for APM payins.

{% enddocs %}


{% docs is_remember_me %}

Indicates whether the payment was made using Remember Me, which lets customers save their card for faster future checkout.

{% enddocs %}


# Common APM & Card payment fields

{% docs acceptance_outcome %}

Outcome of the payment considered for acceptance-rate reporting.

{% enddocs %}

{% docs authentication_outcome %}

Outcome of the payment during the authentication (3DS) stage.

{% enddocs %}

{% docs authentication_source %}

How the merchant integrated 3DS authentication. Sample values: Integrated (authentication performed within the payment request), Standalone (authentication performed separately via Sessions).

{% enddocs %}

{% docs authentication_status_reason %}

Machine-readable code from the Directory Server (DS) or Access Control Server (ACS) describing the 3DS transaction status outcome. Sample values: '14' (transaction timed out at the ACS), '22' (ACS malfunction). Card only — always blank for APM payins.

{% enddocs %}

{% docs challenge_indicator_merchant_preference %}

The merchant's preference for whether a 3DS challenge should be performed. Sample values: 'no_preference' (the issuer's ACS decides); 'challenge_requested' (merchant requests a challenge); 'challenge_requested_mandate' (challenge mandated by the merchant); 'no_challenge_requested' (merchant explicitly requests no challenge, typically when applying an SCA exemption); 'transaction_risk_assessment' / 'low_value' (preference expressed as an exemption request). Card only — always blank for APM payins.

{% enddocs %}

{% docs acceptance_outcome_at %}

The time the payment's acceptance outcome was determined.

{% enddocs %}

{% docs api_version %}

The Checkout.com API version the payment request was made against. Sample value: 2.0.

{% enddocs %}

{% docs authorisation_amount %}

The authorisation amount taken from the successful authorisation when one exists, otherwise the most recent declined attempt. 

{% enddocs %}

{% docs authorisation_attempts %}

Count of authorisation attempts on the payment, including both successful and declined authorisations. Sample values: 0, 1. (APMs do not retry authorisation).

{% enddocs %}

{% docs authorisation_outcome %}

Outcome of the payment during the authorisation stage.

{% enddocs %}

{% docs authorisation_increment_outcome %}

Outcome of the payment when an authorisation increment is attempted. An authorisation increment (or incremental authorisation) is an additional authorisation request that occurs after an initial approved authorisation within the same payment lifecycle. It allows a merchant to increase the authorised amount being held on a cardholder's account, or in some cases (Mastercard only) extend the authorisation validity period. Can be incremented or declined if increment was attempted, or non_authorisation_increment if the payment went straight to capture. Card only, not_applicable for APMs.

{% enddocs %}

{% docs authorisation_outcome_at %}

The time the authorisation outcome was determined. NULL when authorisation did not occur.

{% enddocs %}

{% docs authorised_amount %}

The total successfully-authorised amount on the payment, in its original currency (sum across successful authorisation events).

{% enddocs %}

{% docs bc_charge_id %}

The GW3 masked charge identifier. Present only on legacy ABC charges.

{% enddocs %}

{% docs capture_at %}

Timestamp at which the charge is requested to be captured, when delayed/scheduled capture was requested. NULL when no delayed capture was scheduled.

{% enddocs %}

{% docs capture_outcome %}

Outcome of the payment during the capture stage. Sample values: captured, not_available, declined, partially_captured.

{% enddocs %}

{% docs capture_outcome_at %}

The time the payment's capture outcome was determined - the processing time of the earliest successful capture if any, otherwise the decline time of the earliest capture decline.

{% enddocs %}

{% docs captured_events %}

Count of successful capture events on the payment, including both full and partial captures.

{% enddocs %}

{% docs charge_id %}

Checkout-issued UUID identifying the charge; one value per payment, present on every event in the payment lifecycle. Sample value: 89135679-9001-892f-9d37-b6bcd12210ab.

{% enddocs %}

{% docs customer_card_id %}

Identifier of the customer's stored payment source (the card within the customer's wallet).

{% enddocs %}

{% docs customer_email %}

The customer's email address on the payment request.

{% enddocs %}

{% docs customer_email_domain %}

The domain portion of the customer's email address (the part after '@'), as input by the customer.

{% enddocs %}

{% docs customer_id %}

Identifier of the customer on the payment request.

{% enddocs %}

{% docs customer_name %}

The customer's name on the payment request, as input by the customer.

{% enddocs %}

{% docs event_stream_id %}

Identifier of the gateway event stream the payment's events belong to.  Sample values: Gateway.Charge-00001fb4-bc01-8dff-9966-8729ad679211 (card), Gateway.AlternativeCharge-00001fb4-bc01-8dff-9966-8729ad679211 (APM).

{% enddocs %}

{% docs fallback_status_udf_1 %}

The PSP cascade position derived from udf_1.

{% enddocs %}

{% docs gateway_chargeback_outcome %}

Outcome of the chargeback stage from the Gateway's perspective.  APM only. Sample values: not_available, non_gateway_chargeback (a refund or return exists but no chargeback), alternative_chargeback (an APM chargeback was raised; ACH Direct Debit-US is treated as a return instead).

{% enddocs %}

{% docs gateway_chargeback_outcome_at %}

The time the gateway chargeback outcome was determined.

{% enddocs %}

{% docs is_automatic_capture_requested %}

Indicates whether the merchant requested the charge to be captured automatically after authorisation, rather than via a separate capture call.

{% enddocs %}

{% docs is_batch_payment %}

Indicates whether the payment was submitted as part of a batch payment file.

{% enddocs %}

{% docs is_flagged_authorisation %}

Indicates whether an authorisation on this payment was risk-flagged (gateway response code 10100).

{% enddocs %}

{% docs is_mada %}

Indicates whether the transaction was routed through MADA (Saudi Payments Network). Specific to Saudi Arabia / MENA.

{% enddocs %}

{% docs is_refunded %}

Indicates whether the payment was refunded or partially refunded (true when at least one successful refund event exists).

{% enddocs %}

{% docs latest_captured_at %}

The time of the latest successful capture event on the payment.

{% enddocs %}

{% docs latest_refunded_at %}

The time of the latest successful refund event on the payment.

{% enddocs %}

{% docs platform_metadata %}

Platform-specific metadata associated with the payment request, e.g. 'Platform Data - Magento 2.4.5'; identifies the e-commerce plugin or integration that originated the payment.

{% enddocs %}

{% docs payment_outcome %}

The furthest stage the payment reached in its lifecycle, where later stages take precedence over earlier ones — a refund outranks a capture, which outranks a void, an authorisation, acceptance and authentication — defaulting to 'requested' when no later stage was reached. Sample values: captured, expired, hard_declined, partially_refunded, refunded, voided, requested, cancelled.

{% enddocs %}

{% docs refund_outcome %}

Outcome of the payment during the refund stage. Sample values: not_available, partially_refunded, refunded, non_refund (a chargeback or return was raised instead), declined.

{% enddocs %}

{% docs request_outcome %}

Outcome at the request stage of the payment lifecycle.

{% enddocs %}

{% docs refund_outcome_at %}

The processing time of the earliest successful refund if any, otherwise the decline time of the earliest refund decline.

{% enddocs %}

{% docs refunded_amount %}

The total value of successful full and partial refunds on the payment, in its original currency.

{% enddocs %}

{% docs request_description %}

Free-text description of the payment, supplied by the merchant in the payment request, displayed alongside the charge. Sample value: 'du Pay Cash in'.

{% enddocs %}

{% docs request_sub_entities %}

An array of sub-entities sharing the charge, for split/marketplace payments. Each element holds the sub-entity id, name, merchant reference, split amount, and commission percentage and amount. Taken from the payment request.

{% enddocs %}

{% docs request_sub_entities_array_size %}

Number of sub-entities (marketplace participants) on the payment from requested event. 0 for standard single-beneficiary payments.

{% enddocs %}

{% docs risk_decline_outcome %}

Outcome of the payment at the pre-authorisation risk-decline stage.

{% enddocs %}

{% docs risk_decline_outcome_at %}

The time the payment was declined during pre-authorisation risk checks. NULL when the payment was not risk-declined.

{% enddocs %}

{% docs risk_declined_amount %}

The requested payment amount, in its original currency, when the payment was declined during pre-authorisation risk checks. 0 when the payment was not risk-declined.

{% enddocs %}

{% docs segment_brand %}

Name of the merchant's brand, defined by the merchant in the payment request. Sample values: Faces, Zable, lulumoney.com.

{% enddocs %}

{% docs segment_business_category %}

Name of the business category, defined by the merchant in the payment request. Sample values: Ecom, Credit Cards, Money Remittance.

{% enddocs %}

{% docs segment_market %}

Name of the market where the merchant operates, defined by the merchant in the payment request. Sample values: UAE, EU, United Kingdom.

{% enddocs %}

{% docs sender_address_line_1 %}

First line of the funds sender's address. Populated for money-transfers, account funding, funding refund and payout transactions. Card only — always blank for APM payins.

{% enddocs %}

{% docs sender_address_line_2 %}

Second line of the funds sender's address. On payin, populated only for money-transfer / account-funding card payments. Card only — always blank for APM payins.

{% enddocs %}

{% docs sender_address_town_city %}

Town or city of the funds sender's address. Populated for money-transfers, account funding, funding refund and payout transactions. Card only — always blank for APM payins.

{% enddocs %}

{% docs sender_address_postcode %}

Postcode / ZIP of the funds sender's address. Populated for money-transfers, account funding, funding refund and payout transactions. Card only — always blank for APM payins.

{% enddocs %}

{% docs sender_address_state %}

State or region of the funds sender's address. Populated for money-transfers, account funding, funding refund and payout transactions. Card only — always blank for APM payins.

{% enddocs %}

{% docs sender_address_country_iso2 %}

Two-letter ISO code of the funds sender's country. Populated for money-transfers, account funding, funding refund and payout transactions. Card only — always blank for APM payins.

{% enddocs %}

{% docs sender_name %}

Full name of the funds sender, formed by combining their first and last name. Populated for money-transfers, account funding, funding refund and payout transactions. Card only — always blank for APM payins.

{% enddocs %}

{% docs payin_shipping_address_line_1 %}

First line of the goods recipient's shipping address (usually house number and street), as entered by the customer at payment time.

{% enddocs %}

{% docs payin_shipping_address_line_2 %}

Second line of the goods recipient's shipping address (e.g. apartment, suite or building), as entered by the customer at payment time.

{% enddocs %}

{% docs payin_shipping_address_town_city %}

Town or city of the goods recipient's shipping address, as entered by the customer at payment time.

{% enddocs %}

{% docs payin_shipping_address_state %}

State or region of the goods recipient's shipping address, as entered by the customer at payment time.

{% enddocs %}

{% docs payin_shipping_address_postcode %}

Postcode / ZIP of the goods recipient's shipping address, as entered by the customer at payment time.

{% enddocs %}

{% docs payin_shipping_address_country_iso2 %}

Two-letter ISO code of the goods recipient's shipping address country. NULL when not provided or invalid. Sample values: `US`, `GB`, `FR`, `AU`, `CA`. 

{% enddocs %}

{% docs payin_shipping_address_region %}

The geographic region of the shipping address country input by the customer. Sample values: Europe, Asia and Pacific, Middle East and Africa, North America, Central and South America.

{% enddocs %}

{% docs payin_shipping_address_phone_number %}

Phone number recorded against the goods recipient's shipping address, as entered by the customer at payment time.

{% enddocs %}

{% docs payin_shipping_address_phone_country_code %}

Country code of the phone number recorded against the goods recipient's shipping address. Sample values: +44, +1, +49.

{% enddocs %}

{% docs source_id %}

Identifier of the payment source / instrument used for the payment, stored securely in the CKO Vault. Applicable to card charge and SEPA alternative charge payments. Sample value: c587e991-f912-4db6-b8a0-ca138d443d23.

{% enddocs %}

{% docs instrument_source_id %}

The ID of the payment instrument in 'src_' format, used to identify the stored card across APIs. Sample value: src_shuypris7g3e3ofazijy2rb5em. Card only — always blank for APM payins.

{% enddocs %}

{% docs source_type %}

The type of payment source / instrument used. For APM, the provider name on the request event. Sample values: 'card' (physical or virtual card, raw PAN), 'network_token' (a network token, VTS or MDES, which can improve authorisation rates and reduce fraud), 'id', 'token', 'knet', 'tamara', 'ach', 'stcpay', 'mbway', 'provider_token' (stored token), 'bank_account' (stored bank-account reference).

{% enddocs %}

{% docs traffic_type %}

Transaction traffic classification for the payment.

{% enddocs %}

{% docs udf_1 %}

User-defined field 1 — merchant-supplied free-text metadata, passed through unchanged. Often carries a PSP cascade routing hint (e.g. fallback, original, first_try) or a network indicator (e.g. mada). Sample value: `3653553849`, `MADA`.

{% enddocs %}

{% docs udf_2 %}

User-defined field 2 — merchant-supplied free-text metadata, passed through unchanged. Sample value: `card`, `sbpay`, `0`.

{% enddocs %}

{% docs udf_3 %}

User-defined field 3 — merchant-supplied free-text metadata, passed through unchanged. Sample value: 53826027, `EPHARMACY`, `hostinger.com`, `4`.

{% enddocs %}

{% docs udf_4 %}

User-defined field 4 — merchant-supplied free-text metadata, passed through unchanged. Sample value:  `0`, `1`, `80000455`, +***94942290.

{% enddocs %}

{% docs udf_5 %}

User-defined field 5 — merchant-supplied free-text metadata, passed through unchanged. Sample values: `CRY00001`, `Checkout Champ`, `1`.

{% enddocs %}

{% docs is_account_funding_transaction_requested %}

A flag to determine if the payment requested funds to be pulled and used to fund a non-merchant account. For example, to load a prepaid card, top up a wallet, or fund a person-to-person (P2P) money transfer. NULL if the merchant didn't provide a value in the upapi request. Card only — always blank for APM payins.

{% enddocs %}

{% docs is_force_captured %}

Indicates whether the payment was captured after being voided (force capture). Card only — always blank for APM payins.

{% enddocs %}

{% docs desired_payment_state %}

The desired terminal state of the payment if it cannot be completed (e.g. after a timeout). Observed values: 'Expired': the payment should expire, returning it to a non-terminal state. 'Declined': the payment should be treated as declined. Blank: no desired state was set. 

{% enddocs %}

{% docs retry_request_max_attempts %}

The maximum number of authorisation retry attempts requested, excluding the initial authorisation. Configured by the merchant on the payment request. Sample value: 5. NULL for APM.

{% enddocs %}

{% docs retry_request_end_after_days %}

The maximum number of days between the initial request and the final retry attempt (for dunning retries). Configured by the merchant on the payment request. Sample value: 30. NULL for APM.

{% enddocs %}

{% docs refund_type %}

The type of refund processed on this payment. Possible values: 'Referenced': the refund is linked to the original authorisation transaction (the vast majority). 'Unreferenced': the refund is not linked to a prior capture — a standalone credit.

{% enddocs %}

{% docs unreferenced_refund_type %}

Type of refund processed on the payment. Always 'Unreferenced' in this model — the refund is not linked to a prior capture, it is a standalone credit. See `fct_payin_event` for the broader value set including 'Referenced'.

{% enddocs %}

{% docs payin_current_attempt %}

The current authorization retry attempt, starts at 0 then increments for every retry attempt.

{% enddocs %}

{% docs payin_dunning_current_attempt %}

The current dunning authorization retry attempt number. Starts at 0 for the initial attempt and increments for every subsequent retry.

{% enddocs %}

{% docs is_attempt_n3ds_an_option %}

Indicates whether attempting non-3D Secure (N3DS) is an option for this payment based on merchant configuration. Card only — always blank for APM payins.

{% enddocs %}

{% docs prism_score %}

Risk score returned by Fraud Detection (formerly Prism). Higher values indicate higher risk. Sample values: 0–100. NULL for APM. Gateway-sourced before `2026-08-12`; RA Data Product-sourced from `2026-08-12` onward.

{% enddocs %}


{% docs is_account_funding_transaction_processed %}

A flag to determine if the transaction in which funds were pulled from were used to fund a non-merchant account. For example, to load a prepaid card, top up a wallet, or fund a person-to-person (P2P) money transfer. Card only — always blank for APM payins.

{% enddocs %}

{% docs voided_amount %}

The total value of successful voids on the payment, in its original currency.

{% enddocs %}

{% docs capture_enhanced_scheme_data_submitted %}

The enhanced scheme data qualification level submitted to the scheme on the earliest successful ChargeCaptured transaction for the payment. Indicates the level of enriched data sent with the transaction (e.g. for Visa DCAP / Level 3 interchange optimisation). Only populated for cards, not APM. Sample values: none, level_3, dcap, NULL.

{% enddocs %}

{% docs enhanced_scheme_data_submitted %}

The enhanced scheme data qualification level submitted to the scheme on the transaction event. Indicates the level of enriched data sent with the transaction (e.g. for Visa DCAP / Level 3 interchange optimisation). Only populated for cards, not APM. For payin_event models the event-level value is coalesced with the payment-level value (from the earliest successful capture). Sample values: none, level_3, dcap, NULL.

{% enddocs %}

{% docs checkout_legal_entity_code %}

The Checkout.com legal entity the merchant is contracted with on the authorisation transaction. Part of the MALPB Transaction Stamping fields. Only populated for cards, not APM. For payin_event models the event-level value is coalesced with the payment-level value. Sample values: `cko-llc-usa`, `cko-sas`, `cko-ltd-uk`, `cko-ltd-hkg`, `cko-apac-ltd`. Used for Merchant creditor, revenue recognition, invoicing, reporting, safeguarding.

{% enddocs %}

{% docs acquirer_legal_entity_code %}

The Checkout.com legal entity the acquirer is contracted with on the authorisation transaction (e.g. 'cko-llc-usa'). Part of the MALPB Transaction Stamping fields. Only populated for cards, not APM. For payin_event models the event-level value is coalesced with the payment-level value. Sample values: `cko-llc-usa`, `cko-sas`, `cko-ltd-uk`, `cko-ltd-hkg`, `cko-apac-ltd`, `cko-ca`. Used for scheme-debtor accounting, acquiring liability, settlement attribution.

{% enddocs %}

{% docs acquirer_code %}

Acquirer identifier code stamped on the authorisation transaction. Part of the MALPB Transaction Stamping fields. Only populated for cards, not APM. For payin_event models the event-level value is coalesced with the payment-level value.  Sample values: `CKO` (Checkout), `CRB` (Cross River Bank), `PW` (Pathward).

{% enddocs %}

{% docs banking_partner_code %}

Banking partner identifier code stamped on the authorisation transaction (e.g. 'CRB' for Cross River Bank). Part of the MALPB Transaction Stamping fields. Only populated for cards, not APM. For payin_event models the event-level value is coalesced with the payment-level value.   Sample values: `CRB` (Cross River Bank), `JPM` (JPMorgan), `CIT` (Citibank), `BC`, `SCB`, `PAT`.

{% enddocs %}

{% docs is_card_present %}

Indicates whether the card was physically present at the point of sale, i.e. an In-Person Payments (IPP) card-present transaction as opposed to an eCommerce (card-not-present) one. Only populated for cards — always FALSE for APM payins. On the payin (payment-level) models this is the value from the payment request. On the payin_event models this is the value on the event itself (e.g. refund events carry their own value).

{% enddocs %}

{% docs card_entry_mode %}

How the card details were captured at the point of interaction for an In-Person Payments (IPP) transaction, e.g. chip, contactless or magnetic stripe. Only populated for cards, not APM, and only for card-present transactions — NULL for eCommerce payments. On the payin (payment-level) models this is the value from the payment request. On the payin_event models this is the value on the event itself (e.g. refund events carry their own value).

{% enddocs %}

{% docs is_card_pin_present %}

Indicates whether a cardholder PIN was supplied with the In-Person Payments (IPP) transaction, i.e. the payment was PIN-authenticated at the terminal. Only populated for cards — always FALSE for APM payins. On the payin (payment-level) models this is the value from the payment request. On the payin_event models this is the value on the event itself (e.g. refund events carry their own value).

{% enddocs %}

{% docs terminal_id %}

Identifier of the physical payment terminal (point-of-interaction device) that processed an In-Person Payments (IPP) transaction. Sourced from the payment request. Only populated for cards, not APM, and only for card-present transactions — NULL for eCommerce payments. For payin_event models non-refund events inherit the payment request value while refund events carry their own value.

{% enddocs %}

{% docs terminal_local_at %}

The transaction timestamp as recorded by the payment terminal in the terminal's own local time for an In-Person Payments (IPP) transaction. Note: although stored as a BigQuery TIMESTAMP (which BigQuery renders as UTC), the value is local terminal time and must NOT be converted to another time zone — confirmed with Gateway. Sourced from the payment request. Only populated for cards, not APM, and only for card-present transactions — NULL for eCommerce payments. For payin_event models non-refund events inherit the payment request value while refund events carry their own value.

{% enddocs %}

{% docs account_name_inquiry %}

The overall Account Name Inquiry (ANI) result for the payment. ANI is a Visa/Mastercard scheme feature that checks the cardholder's name against the name held by the issuing bank. Card only — always blank for APM payins. More information: https://www.checkout.com/docs/developer-resources/codes/ani-codes. 

{% enddocs %}

{% docs account_name_inquiry_first_name %}

Account Name Inquiry (ANI) match status for the cardholder's first name. Sample values: 'full_match', 'partial_match', 'no_match', 'unverified'. NULL when the ANI check was not requested. Card only — always blank for APM payins. More information: https://www.checkout.com/docs/developer-resources/codes/ani-codes. 

{% enddocs %}

{% docs account_name_inquiry_middle_name %}

Account Name Inquiry (ANI) match status for the cardholder's middle name. Sample values: 'full_match', 'partial_match', 'no_match', 'unverified'. NULL when the ANI check was not requested. Card only — always blank for APM payins. More information: https://www.checkout.com/docs/developer-resources/codes/ani-codes. 

{% enddocs %}

{% docs account_name_inquiry_last_name %}

Account Name Inquiry (ANI) match status for the cardholder's last name. Sample values: 'full_match', 'partial_match', 'no_match', 'unverified'. NULL when the ANI check was not requested.  Card only — always blank for APM payins. More information: https://www.checkout.com/docs/developer-resources/codes/ani-codes.

{% enddocs %}

{% docs has_account_name_inquiry_full_match %}

Flag indicating whether any of the Account Name Inquiry (ANI) name fields (first, middle, last) returned 'full_match'. NULL when the ANI check was not requested. Card only — always blank for APM payins. More information: https://www.checkout.com/docs/developer-resources/codes/ani-codes.

{% enddocs %}

{% docs has_previous_payment_id %}

Flag indicating if the payment has a reference to a previous payment ID (e.g. for recurring or retry charges).

{% enddocs %}

{% docs authentication_method %}

The method used to authenticate the payment. Sample values: 'ACS - Challenged' (active challenge via OTP/biometric), 'ACS - Frictionless' (silent), 'ACS - ACS specific authentication', 'Acquirer exemption - Frictionless', 'Scheme stand in - Frictionless', 'Data Only / 3RI' (Mastercard Data Only or 3RI merchant-initiated), 'Mastercard unknown' / 'Visa unknown', '3DS1' (legacy 3DS v1).

{% enddocs %}

{% docs authentication_response %}

Response code from the issuer's Access Control Server (ACS) for the authentication attempt. Sample values: 'Y' (successful), 'N' (failed), 'U' (unavailable), 'A' (attempted, card not enrolled — partial liability shift may apply), 'I' (informational, issuer did not perform the check), 'C' (challenge required), 'R' (rejected, should not be retried).

{% enddocs %}

{% docs three_ds_exemption_requested %}

The SCA exemption requested by the merchant. Sample values: 'transaction_risk_assessment' (TRA exemption; 'transaction_risk_assesment' is also seen), 'low_value', 'recurring_operation', 'out_of_sca_scope', 'secure_corporate_payment', 'data_share', 'trusted_listing', '3ds_outage', 'not_supported', 'other'. Blank when no exemption was requested. See three_ds_exemption_code for the raw, unfiltered value. Card only — always blank for APM payins.

{% enddocs %}

{% docs three_ds_exemption_code %}

The SCA exemption code requested by the merchant. Sample values: 'transaction_risk_assessment' (TRA exemption; the misspelling 'transaction_risk_assesment' is also seen), 'low_value', 'none', 'recurring_operation', 'out_of_sca_scope', 'secure_corporate_payment', 'trusted_listing', '3ds_outage', 'data_share', 'not_supported', 'other'. Blank when no exemption was requested. See three_ds_exemption_requested for the same value with 'none' filtered out. Card only — always blank for APM payins.

{% enddocs %}

{% docs three_ds_upgrade_reason %}

The reason the payment was upgraded to 3DS authentication, typically following a soft decline. Sample values: 'intelligent_acceptance' (upgraded by Checkout.com's Intelligent Acceptance), 'risk' (upgraded due to a risk assessment), 'sca_retry' (retried with 3DS following an SCA-required soft decline). NULL when no upgrade occurred. Card only — always blank for APM payins.

{% enddocs %}

{% docs authentication_exemption_attempted %}

The 3DS exemption attempted during authentication. An authentication may have been attempted with an exemption but later upgraded to a challenged flow. NULL when no exemption was requested or the value was 'none'. Sample values: low_value, trusted_beneficiary. Card only — always blank for APM payins.

{% enddocs %}

{% docs exemption_applied %}

The SCA exemption type applied during authorisation. Values include 'none' (full authentication required), 'transaction_risk_assessment' (risk-based analysis; misspelling 'transaction_risk_assesment' also observed), 'low_value' (below the low-value threshold, typically €30), 'low_risk_program', 'recurring_operation', 'out_of_sca_scope', '3ds_outage', 'secure_corporate_payment', 'data_share', 'trusted_listing', 'no_authentication', 'other'. Card only — always blank for APM payins.

{% enddocs %}

{% docs authentication_flow_type %}

The type of 3DS authentication flow. Sample values: 'challenged' (cardholder actively verified, e.g. OTP/biometric), 'frictionless' (authenticated silently), 'frictionless_delegated' (delegated to the acquirer or third party), 'decoupled' (authenticated independently of the payment session, e.g. via a banking app). Blank when no 3DS authentication was performed. Card only — always blank for APM payins.

{% enddocs %}

{% docs action_id %}

Identifier of the gateway action that produced this event. Sample value: act_22222ayb234i3ik7ruf5xvvvsy.

{% enddocs %}

{% docs event_at %}

Timestamp (UTC) when the gateway event was emitted.

{% enddocs %}

{% docs acquirer_region_used_payment_level %}

Payment-level acquirer region on the acceptance event. Sample values: Europe, North America, Asia and Pacific, Middle East and Africa.

{% enddocs %}

{% docs action_code_description %}

Human-readable label for the action phase of the event. Sample values: Capture, Authorisation, Expiry, Refund, Return, Void Authorisation. Blank for events the mapping does not classify (e.g. chargeback, risk-decline).

{% enddocs %}

{% docs batch_id %}

Identifier of the batch-payment file the charge was submitted in. NULL when not part of a batch.

{% enddocs %}

{% docs bc_transaction_id %}

Legacy GW3 masked transaction identifier for the event. NULL for APM events. Sample value: 89DAEE777J1D397F08DB.

{% enddocs %}

{% docs original_bc_transaction_id %}

Legacy GW3 transaction identifier when the event is a follow-on action (e.g. refund referencing the original capture). NULL for APM events. Sample value: 19CAEE777T1D397F698E.

{% enddocs %}

{% docs captured_amount_eur %}

Total value of captures and partial captures in Euros. NULL for APM.

{% enddocs %}

{% docs captured_amount_gbp %}

Total value of captures and partial captures in Sterling. NULL for APM.

{% enddocs %}

{% docs captured_amount_usd %}

Total value of captures and partial captures in US Dollars. NULL for APM.

{% enddocs %}

{% docs clr_type %}

Gateway-internal .NET event class name (CLR type) of the originating event. Sample values: Gateway.Public.Events.ChargeAuthorised (card), Gateway.Public.Events.AlternativeChargeRequested (APM).

{% enddocs %}

{% docs correlation_id %}

Correlation identifier linking the event to its originating request across services. Sample value: 000005de-c948-4030-ba87-48be55d26e64.

{% enddocs %}

{% docs currency_name %}

Human-readable name of the payment currency. Sample values: British Pound, US Dollar, Euro, UAE Dirham, Kuwaiti Dinar, Saudi Riyal.

{% enddocs %}

{% docs currency_symbol %}

3-letter ISO 4217 currency code of the payment. Sample values: GBP, USD, EUR, AED, KWD, SAR.

{% enddocs %}

{% docs customer_ip %}

IP address the customer initiated the transaction from. Used for geolocation and fraud / risk screening.

{% enddocs %}

{% docs customer_ip_country_iso2 %}

2-letter ISO country code resolved from the customer's IP address. Sample values: GB, US, DE, FR, SA, NL. NULL when the IP could not be geolocated. Gateway-sourced before `2026-08-12`; RA Data Product-sourced from `2026-08-12` onward.

{% enddocs %}

{% docs decoded_action_id %}

Decoded action identifier; for card payments this maps to the action_id / charge_id, for APM it equals charge_id. Sample value: 730a386d-6e01-8947-9951-a0f94937718a.

{% enddocs %}

{% docs description %}

Free-text description attached to the event by the merchant or gateway. Sample value: 'Sylius Checkout Payment', '1051802440000001201'.

{% enddocs %}

{% docs event_id %}

Identifier of the individual gateway event. Sample values: evt_abcdef1234567890abcdef1234 (card), 00000042-471e-4b35-8173-c8a831e4b42f (APM).

{% enddocs %}

{% docs event_outcome %}

Outcome of the payment lifecycle event. Card payin sample values: requested, authenticated, risk_declined, authorised, declined, incremented, captured, partially_captured, voided, refunded, partially_refunded. APM payin sample values: requested, captured, deferred, expired, returned, cancelled.
A single event can span multiple transactions (attempts) — e.g. a ChargeAuthorised event may contain a declined attempt followed by an authorised one, so event_outcome can differ across rows for the same event.

{% enddocs %}

{% docs event_type %}

Type of the gateway event in the payment's lifecycle.
Card sample values: ChargeRequested, ChargeAuthenticated, ChargeAuthorised, ChargeCaptured, ChargePartiallyCaptured, ChargeVoided, ChargeRefunded, etc.
APM sample values: AlternativeChargeRequested, AlternativeChargeAuthorised, AlternativeChargeCaptured, AlternativeChargeRefunded, AlternativeChargeVoided, AlternativeChargeReturned, etc.

{% enddocs %}

{% docs gateway_response_details %}

Additional free-text detail on the gateway response. Sample values: Approved, 3D Secure Required, Do Not Honour, Insufficient Funds, Invalid Card Number, Customer Cancellation.

{% enddocs %}

{% docs industry_name_used_payment_level %}

Payment-level industry name for the payment-level MCC. Sample values: Restaurants / Bars, Clothing Stores, Retail, Quasi Cash.

{% enddocs %}

{% docs is_enriched %}

Indicates whether a request event was observed (same as is_enriched_request). true: request event present. false: no request event.

{% enddocs %}

{% docs is_enriched_request %}

Indicates whether a payment request event was observed for this payment. true: request present. false: only later-stage events landed.

{% enddocs %}

{% docs is_increment %}

Indicates whether the event is an incremental authorisation. true: incremental authorisation. false: base authorisation or non-authorisation event.

{% enddocs %}

{% docs is_successful_authorisation %}

Indicates whether the event is a successful authorisation. For cards: true on ChargeAuthorised events. For APMs (measured at capture): true on AlternativeChargeCaptured events. false: any other event.

{% enddocs %}

{% docs is_successful_capture %}

Indicates whether the event is a successful capture. true: ChargeCaptured / AlternativeChargeCaptured event. false: any other event (partial captures are not flagged).

{% enddocs %}

{% docs mcc_desc_used_payment_level %}

Payment-level MCC description (from the acceptance event). Sample values: FAST FOOD RESTAURANTS, MEN'S & WOMEN'S CLOTHING STORES, WIRE TRANSFER MONEY ORDERS.

{% enddocs %}

{% docs mcc_group_used_payment_level %}

Payment-level MCC group (a reporting grouping of related MCCs). Sample values: Restaurants, Clothing, General Retail & High Street, Financial Services.

{% enddocs %}

{% docs merchant_reference %}

Merchant-supplied reference (e.g. an order ID) attached to the payment; formerly known as track_id. Sample values: order_12345 (card), hs-up881987301 (APM).

{% enddocs %}

{% docs metadata_transaction_id %}

Transaction identifier stored in the event metadata, typically the MSSQL-side id for legacy/ABC reconciliation.

{% enddocs %}

{% docs mssql_transaction_id %}

MSSQL-side transaction identifier (same value as metadata_transaction_id).

{% enddocs %}

{% docs partial_flag %}

Indicates whether the event is a partial-amount action (partial capture, refund, chargeback). true: partial action. false: full-amount action.

{% enddocs %}

{% docs payment_code %}

Short payment-type code from the acquirer reference. Sample values: CC (Credit Cards) for card, LP (Local Payments) for APM. Blank when no acquirer match is found.

{% enddocs %}

{% docs payment_method_id %}

Internal numeric identifier of the payment method. APM only — always blank for card payins.

{% enddocs %}

{% docs payment_method_product_type %}

Product type from the alternative charge response. Sample values: pay_in_full, pay_later, pay_by_instalment_2, pay_by_instalment_4, regular, Mini Program, In-App, QR Code. NULL for card payments.

{% enddocs %}

{% docs payment_type %}

Human-readable payment-type label resolved from the acquirer lookup. Sample values: Credit Cards (card), Local Payments (APM). Blank when no acquirer match is found.

{% enddocs %}

{% docs processed_at %}

Timestamp (UTC) when the gateway finished processing this event.

{% enddocs %}

{% docs processing_settings_accommodation_data %}

Accommodation/hotel booking metadata, present when the charge funds a hotel booking. Each element holds the property name and check-in / check-out dates. Populated only for accommodation/lodging merchants.

{% enddocs %}

{% docs processing_settings_airline_data %}

Airline ticket metadata — an array of structs per ticket with ticket_issue_date, ticket_issuing_carrier_code and flight_leg_details (carrier_code, departure_airport, arrival_airport, departure_date, departure_time). Populated only for airline merchants.

{% enddocs %}

{% docs status %}

Status label for the event. Card sample values: Authorised, Declined, Captured, Voided, Refunded, Pending. APM sample values: Pending, Captured, Deferred Capture, Expired, Authorised, Declined, Refunded. Blank on events with no provider status.

{% enddocs %}

{% docs sub_entities %}

Array of sub-entities sharing the charge, for split/marketplace payments. Each element holds the sub-entity id, name, merchant reference, split amount, and commission percentage and amount.

{% enddocs %}

{% docs sub_entities_array_size %}

Number of sub-entities (marketplace participants) on the payment. 0 for standard single-beneficiary payments.

{% enddocs %}

{% docs subscription_id %}

Identifier of the subscription the charge belongs to (recurring / instalment agreement). NULL for one-off payments.

{% enddocs %}

{% docs transaction_acquirer_transaction_id %}

Acquirer-side transaction identifier returned for the event (on events carrying a transaction block). Sample values: 51129720260622000000MCSGU15JB0621 (card), 193a13e3-bd3c-4036-8e9a-403b21e0f4d9 (APM).

{% enddocs %}

{% docs transaction_amount %}

Amount of this event in the payment's original currency (major units), e.g. the captured amount on a capture event. For APM, falls back to the payment-level requested amount when missing on the event.

{% enddocs %}

{% docs transaction_amount_eur %}

transaction_amount converted to Euro (EUR) at the daily FX rate for the transaction date. NULL when no FX rate is available.

{% enddocs %}

{% docs transaction_amount_gbp %}

transaction_amount converted to British Pound Sterling (GBP) at the daily FX rate for the transaction date. NULL when no FX rate is available.

{% enddocs %}

{% docs transaction_amount_usd %}

transaction_amount converted to US Dollar (USD) at the daily FX rate for the transaction date. NULL when no FX rate is available.

{% enddocs %}

{% docs transaction_at %}

Timestamp (UTC) when the transaction occurred.

{% enddocs %}

{% docs transaction_event_unique_key %}

Primary key of the payin event — a deterministic surrogate key unique to each card or APM gateway event, derived from charge_id, event_type and the transaction_id (falling back to event_id when transaction_id is absent).

{% enddocs %}

{% docs transaction_id %}

Gateway-assigned transaction identifier on the event; a payment can have several transactions (e.g. cascaded attempts).

{% enddocs %}

{% docs acquirer_reference_number %}

Acquirer Reference Number (ARN) — a scheme-issued identifier the acquirer attaches to a card transaction for settlement reconciliation, retrieval requests, and dispute tracking. Length and format vary by card scheme: Visa and Mastercard typically use a 23-character ARN; other schemes (e.g. Cartes Bancaires, Amex, JCB) use different layouts, commonly 12 characters or shorter. Sample values: 24445005108000123456789 (Visa/Mastercard), 639744794455 (Cartes Bancaires). Card-only — does not apply to alternative payment methods (APMs).

{% enddocs %}

# Pay To Card — Destination party

{% docs destination_name %}

Full name of the destination party (the recipient of the payout). For individuals, this is the cardholder's name (concatenation of first and last name); for corporate destinations, this is the company name.

{% enddocs %}

{% docs destination_first_name %}

First name of the destination party when the recipient is an individual.

{% enddocs %}

{% docs destination_last_name %}

Last name of the destination party when the recipient is an individual.

{% enddocs %}

{% docs destination_company_name %}

Company name of the destination party when the payout recipient is a corporate entity. NULL for individuals.

{% enddocs %}

{% docs destination_type %}

Type of the destination party. Sample values: Individual, Corporate. `Government` is proto-defined but not currently observed in production data.

{% enddocs %}

{% docs destination_dob %}

Date of birth of the destination party (`YYYY-MM-DD` string), provided by the merchant for AML/regulatory checks.

{% enddocs %}

{% docs destination_country_of_birth %}

Country name of the destination party's country of birth. Predominantly NULL — only populated by merchants who supply country-of-birth data for AML/regulatory checks.

{% enddocs %}

{% docs destination_country_iso2 %}

ISO-3166-1 alpha-2 country code of the destination party's address (upper-cased). Sample values: US, GB, UA, ES, UZ, FR, RO.

{% enddocs %}

{% docs destination_state %}

State or region of the destination party's address.

{% enddocs %}

{% docs destination_city %}

City of the destination party's address.

{% enddocs %}

{% docs destination_address_line_1 %}

First line of the destination party's address (street / building).

{% enddocs %}

{% docs destination_address_line_2 %}

Second line of the destination party's address (apartment / suite).

{% enddocs %}

{% docs destination_zip_code %}

Postal or ZIP code of the destination party's address.

{% enddocs %}

{% docs destination_email %}

Email address of the destination party.

{% enddocs %}

{% docs acquirer_bid %}

The acquirer Business ID (BID). Sourced from the acquirer credentials configuration. Consistently NULL in the current sample window. Card only — always blank for APM payins.

{% enddocs %}

{% docs acquirer_id %}

The identifier of the acquirer used for the authorisation transaction. Sample values: 22, 23. Card only — always blank for APM payins.

{% enddocs %}

{% docs acquirer_processor_name %}

The name of the processor used by the acquirer for this payment. Card only — always blank for APM payins.

{% enddocs %}

{% docs affiliate_id %}

The identifier for the Conversion Affiliate — the downstream sub-entity under the On-Ramp Provider that executes the fiat-to-digital-currency conversion. This is a required field for merchants that are Visa-registered ramp provider operating with affiliates. Card only — always blank for APM payins.

{% enddocs %}

{% docs affiliate_url %}

The affiliate URL. This is a required field for merchants that are Visa-registered ramp provider operating with affiliates. Card only — always blank for APM payins.

{% enddocs %}

{% docs authenticated_payments %}

Count of payments where authentication was successful (0 or 1 per payment). Only includes payments that completed authentication with a positive outcome. Card only — always blank for APM payins.

{% enddocs %}

{% docs authentication_exemption_applied %}

The 3DS exemption that was applied during authentication, only possible for frictionless authentications. Blank when no exemption was applied or when authentication was challenged. Card only — always blank for APM payins.

{% enddocs %}

{% docs authentication_outcome_at %}

Timestamp (UTC) of the latest authentication event for the payment — the moment the 3DS authentication result was returned. NULL when no authentication was attempted. Card only — always blank for APM payins.

{% enddocs %}

{% docs authentication_pan_type %}

The PAN type used at authentication. When 'dpan' a network token was used, when 'fpan' the card account number was used. Sample values: fpan, dpan, mpan. Card only — always blank for APM payins.

{% enddocs %}

{% docs authentication_payments %}

Count of payments where authentication was attempted (0 or 1 per payment). Includes both successful and failed authentication attempts. Card only — always blank for APM payins.

{% enddocs %}

{% docs authorisation_acquirer_credential_id %}

The acquirer credential identifier used specifically during the authorisation stage of the payment. Card only — always blank for APM payins.

{% enddocs %}

{% docs authorisation_acquirer_response_code %}

The acquirer specific response code of the successful authorisation event. Otherwise, the acquirer response code of the first declined authorisation. Card only — always blank for APM payins.

{% enddocs %}

{% docs authorisation_acquirer_response_code_list %}

A list of all acquirer response codes received at authorisation stage in order of transaction timestamp. Card only — always blank for APM payins.

{% enddocs %}

{% docs authorisation_acquirer_response_desc %}

The description that is mapped to the response code for the specific acquirer. Card only — always blank for APM payins.

{% enddocs %}

{% docs authorisation_increment_outcome_at %}

The time the payment was first incremented. Card only — always blank for APM payins.

{% enddocs %}

{% docs authorisation_pan_type %}

The PAN type used at authorisation. When 'dpan' a network token was used, when 'fpan' the card account number was used. Sample values: fpan, dpan, mpan. Card only — always blank for APM payins.

{% enddocs %}

{% docs authorisation_recommendation_code %}

The recommendation code returned by the scheme during authorisation. Provides additional information on how a transaction should be retried. Sample values: 01 (updated or additional information required), 02 (try again later), 03 (do not try again). Card only — always blank for APM payins.

{% enddocs %}

{% docs authorisation_type %}

The authorisation type. Sample values: final, estimated. Card only — always blank for APM payins.

{% enddocs %}

{% docs billing_address_line_1 %}

The billing address line 1 associated to the card, input by the customer. Card only — always blank for APM payins.

{% enddocs %}

{% docs billing_address_line_2 %}

The billing address line 2 associated to the card, input by the customer. Card only — always blank for APM payins.

{% enddocs %}

{% docs billing_address_phone_number %}

The billing phone number associated to the card, input by the customer. Card only — always blank for APM payins.

{% enddocs %}

{% docs billing_address_postcode %}

The billing postcode associated to the card, input by the customer. Card only — always blank for APM payins.

{% enddocs %}

{% docs billing_address_state %}

The billing state associated to the card, input by the customer. Card only — always blank for APM payins.

{% enddocs %}

{% docs billing_address_town_city %}

The billing town/city associated to the card, input by the customer. Card only — always blank for APM payins.

{% enddocs %}

{% docs capture_acquirer_response_code %}

The acquirer response code of the first successful capture event. Otherwise, the acquirer response code of the first declined capture. Card only — always blank for APM payins.

{% enddocs %}

{% docs capture_acquirer_response_desc %}

The description that is mapped to the response code for the specific acquirer. Card only — always blank for APM payins.

{% enddocs %}

{% docs card_bin_max %}

The full card Bank Identification Number, usually 8-digit for Visa and Mastercard, falling back to the standard 6-digit BIN if not available. Sample values: 41883000, 43425611, 53512067. Card only — always blank for APM payins.

{% enddocs %}

{% docs card_category %}

The scheme category of the card. Sample values: Consumer (personal card), Commercial (business card). Card only — always blank for APM payins.

{% enddocs %}

{% docs card_charge_ingestion_at %}

Timestamp (UTC) when the card charge record was ingested into the data platform from the Flink stream. Used to keep the freshest version when a payment is re-ingested. NULL for APM payments.

{% enddocs %}

{% docs card_charge_updated_at %}

Timestamp when this payment was last updated at in the int_card_payin table. Card only — always blank for APM payins.

{% enddocs %}

{% docs card_product_code %}

The scheme product code for the card. Card only — always blank for APM payins.

{% enddocs %}

{% docs card_scheme_local %}

The local or domestic card scheme for co-badged cards, applied alongside the international scheme. Sample values: mada (Saudi domestic debit), cartes_bancaires (French domestic), maestro, pulse, star, nyce, accel, omannet. Blank when there is no local scheme and the transaction processed on the international scheme only. Card only — always blank for APM payins.

{% enddocs %}

{% docs card_vault_id %}

The identifier of the card PAN encrypted and stored in the Vault. Card only — always blank for APM payins.

{% enddocs %}

{% docs challenge_indicator_used %}

The challenge indicator actually used during the payment's authentication stage. NULL when the payment did not go through authentication, or when the authorisation 3DS-upgraded the payment (superseding the merchant's original preference). Card only — always blank for APM payins.

{% enddocs %}

{% docs incremented_amount %}

The total value of authorisation incrementations in the payment's original currency (major units). Card only — always blank for APM payins.

{% enddocs %}

{% docs incremented_amount_eur %}

The total value of authorisation incrementations converted to Euros at the transaction-date FX rate. Card only — always blank for APM payins.

{% enddocs %}

{% docs incremented_amount_gbp %}

The total value of authorisation incrementations converted to Sterling at the transaction-date FX rate. Card only — always blank for APM payins.

{% enddocs %}

{% docs incremented_amount_usd %}

The total value of authorisation incrementations converted to US Dollars at the transaction-date FX rate. Card only — always blank for APM payins.

{% enddocs %}

{% docs incremented_payments %}

Count of payments where the authorisation was incremented (0 or 1 per payment). Authorisation increments increase the authorised amount without creating a new authorisation. Card only — always blank for APM payins.

{% enddocs %}

{% docs is_attempt_n3ds_activated %}

Flag indicating if the Attempt Non-3DS (N3D) feature was activated for this payment. true: the merchant enabled attempt-N3D, allowing the payment to proceed to authorisation without 3DS if authentication is not possible (e.g. card/issuer does not support 3DS). Card only — always blank for APM payins.

{% enddocs %}

{% docs is_authentication_not_possible %}

Indicates whether 3DS authentication was not possible, used to identify 3DS downgrade to non-3DS. true: the payment requested 3DS (with attempt-N3D enabled) but authentication could not complete, signalled by ECI '0'/'00' (non-Mastercard) or '7'/'07' (Mastercard). false: authentication was possible, or attempt-N3D was not enabled, or 3DS was not requested. Card only — always blank for APM payins.

{% enddocs %}

{% docs is_card_cko_network_token_available %}

Indicates whether a Checkout.com-provisioned network token (VTS or MDES) is available for this card. Network tokens can improve authorisation rates and reduce fraud risk. See is_cko_network_token_used for actual usage. Card only — always blank for APM payins.

{% enddocs %}

{% docs is_card_expired %}

Returns true if the card was expired at the time of the payment request. Card only — always blank for APM payins.

{% enddocs %}

{% docs is_card_store_for_future_use %}

Flag indicating if the payment request includes storing the card for future use. Card only — always blank for APM payins.

{% enddocs %}

{% docs is_card_verification %}

Flag indicating if the payment is a card verification (zero-value authorisation to verify card details). Card only — always blank for APM payins.

{% enddocs %}

{% docs is_card_verification_value_check_present %}

Flag indicating if a Card Verification Value (CVV) was present in the payment request. Card only — always blank for APM payins.

{% enddocs %}

{% docs is_cko_network_token_used %}

Indicates whether a Checkout.com-provisioned network token (VTS or MDES) was used for processing at the authentication or authorisation stage. Card only — always blank for APM payins.

{% enddocs %}

{% docs is_dunning_retry_canceled %}

Flag indicating if the dunning retry associated with a payment was cancelled. Dunning retries are asynchronous retry attempts (can occur over a span of multiple days) at a later time, either per a retry schedule provided by the merchant or per CKO's smart retry logic. Card only — always blank for APM payins.

{% enddocs %}

{% docs is_mpan %}

Flag indicating if the payment uses MPAN. Card only — always blank for APM payins.

{% enddocs %}

{% docs is_over_captured %}

The flag to indicate if the captured amount is greater than the authorised amount. Card only — always blank for APM payins.

{% enddocs %}

{% docs is_regular_dunning_requested %}

The flag to show whether the merchant payment request was configured to include Regular Dunning. Card only — always blank for APM payins.

{% enddocs %}

{% docs is_regulated %}

The flag to indicate if the payment is regulated. Card only — always blank for APM payins.

{% enddocs %}

{% docs is_three_ds_exemption_executed %}

Flag indicating if a 3DS exemption was successfully executed (applied and honoured) during the payment's authentication or authorisation stage. true: an exemption was applied and the payment proceeded without a full 3DS challenge; false: no exemption was executed (either none was requested, or the request was denied by the issuer/scheme). Card only — always blank for APM payins.

{% enddocs %}

{% docs is_three_ds_upgrade %}

Flag indicating if the payment was upgraded to 3DS authentication following a soft decline on a previous authorisation attempt. true: Routing applied a new-authentication modification (typically after a 20154 SCA-required decline) and the payment was retried with 3DS; false: no 3DS upgrade occurred. Card only — always blank for APM payins.

{% enddocs %}

{% docs issuing_country_risk_level %}

The risk level of the country in which the issuer is based. Sample values: Low, Normal, High, Unacceptable. Card only — always blank for APM payins.

{% enddocs %}

{% docs merchant_terminal_id %}

The terminal ID associated with the merchant for this payment. Card only — always blank for APM payins.

{% enddocs %}

{% docs non_authentication_payments %}

Count of payments which proceeded to authorisation without attempting authentication (0 or 1 per payment). Includes payments where 3DS was not requested or not applicable. Card only — always blank for APM payins.

{% enddocs %}

{% docs payment_account_reference %}

A unique identifier for a primary account number (PAN). The reference is shared across the physical card and all associated network tokens, like Apple Pay or Google Pay. This enables you to link all transactions made with the card or tokens to the same account. Card only — always blank for APM payins.

{% enddocs %}

{% docs pinless_debit_type %}

Indicates the type of pinless debit. Sample values: bill_pay, ecommerce. Card only — always blank for APM payins.

{% enddocs %}

{% docs preferred_scheme %}

The preferred card scheme for co-badged cards, indicating which scheme should be used to process the payment. Falls back to card_scheme_local if the merchant's preferred_scheme is not set. Sample values: visa, cartes_bancaires, mastercard. Card only — always blank for APM payins.

{% enddocs %}

{% docs processor_bin_cib %}

The processor BIN CIB (Card Issuer Bank) identifier used for routing. Card only — always blank for APM payins.

{% enddocs %}

{% docs provider_key %}

Key to load specific configurations for sub-merchants in the card processing platform. Equivalent to `processing_profile_id` in the table `dim_entity_configuration`. Card only — always blank for APM payins.

{% enddocs %}

{% docs purchase_country %}

The two-letter ISO country code of the purchase country. This is a required field for merchants that are Visa-registered ramp provider operating with affiliates. Card only — always blank for APM payins.

{% enddocs %}

{% docs purchase_type %}

The digital item type for the payment. Sample values: blockchain, cbdc, cryptocurrency, nft, stablecoin. Required for merchants that are Visa-registered ramp providers operating with affiliates. Card only — always blank for APM payins.

{% enddocs %}

{% docs refund_acquirer_response_code %}

The acquirer response code of the first successful refund event. Otherwise, the acquirer response code of the first declined refund. Card only — always blank for APM payins.

{% enddocs %}

{% docs refund_acquirer_response_desc %}

The description mapped to the acquirer response code for the refund. Card only — always blank for APM payins.

{% enddocs %}

{% docs regular_dunning_end_after_days %}

The number of days that a payment configured for Regular Dunning can be retried. Configured by the merchant. Card only — always blank for APM payins.

{% enddocs %}

{% docs regular_dunning_max_attempts %}

The maximum number of retry attempts that a payment configured for Regular Dunning should have, excluding the initial attempt. Configured by the merchant. Card only — always blank for APM payins.

{% enddocs %}

{% docs regular_dunning_retry_type %}

The regular dunning retry type. Sample values: dunning, smart_dunning. Card only — always blank for APM payins.

{% enddocs %}

{% docs request_metadata %}

Additional metadata provided in the payment request. Card only — always blank for APM payins.

{% enddocs %}

{% docs request_xid %}

The XID (transaction identifier) from the 3DS authentication request. Card only — always blank for APM payins.

{% enddocs %}

{% docs scheme_merchant_preference %}

The merchant's explicit scheme preference for co-badged card routing. Sample values: visa, cartes_bancaires, mastercard. Card only — always blank for APM payins.

{% enddocs %}

{% docs three_ds_protocol_version %}

The version of 3DS that was requested for the authentication. Does not mean the payment will be processed with that 3DS version. Sample values: 1, 2. Card only — always blank for APM payins.

{% enddocs %}

{% docs alternative_charge_ingestion_at %}

Timestamp (UTC) the latest event for this APM payment was ingested into the upstream apm_payin source. APM only — always blank for card payins.

{% enddocs %}

{% docs alternative_charge_updated_at %}

Timestamp when this payment was last updated at in the int_apm_payin table. APM only — always blank for card payins.

{% enddocs %}

{% docs alternative_chargeback_amount %}

Total APM chargeback amount in the payment's original currency (major units). Excludes ACH Direct Debit-US, which is treated as a return. APM only.

{% enddocs %}

{% docs alternative_chargeback_amount_eur %}

Total APM chargeback amount converted to Euros at the transaction-date FX rate (major units). Excludes ACH Direct Debit-US. APM only.

{% enddocs %}

{% docs alternative_chargeback_amount_gbp %}

Total APM chargeback amount converted to Sterling at the transaction-date FX rate (major units). Excludes ACH Direct Debit-US. APM only.

{% enddocs %}

{% docs alternative_chargeback_amount_usd %}

Total APM chargeback amount converted to US Dollars at the transaction-date FX rate (major units). Excludes ACH Direct Debit-US. APM only.

{% enddocs %}

{% docs alternative_chargeback_payments %}

Payment counter (0 or 1) flagging an APM chargeback. Excludes ACH Direct Debit-US, which is treated as a return. APM only.

{% enddocs %}

{% docs capture_deferred_amount %}

The total value of deferred and partially deferred capturesin the payment's original currency (major units). APM only.

{% enddocs %}

{% docs capture_deferred_amount_eur %}

The total value of deferred and partially deferred capturesconverted to Euros at the transaction-date FX rate (major units). APM only.

{% enddocs %}

{% docs capture_deferred_amount_gbp %}

The total value of deferred and partially deferred capturesconverted to Sterling at the transaction-date FX rate (major units). APM only.

{% enddocs %}

{% docs capture_deferred_amount_usd %}

The total value of deferred and partially deferred capturesconverted to US Dollars at the transaction-date FX rate (major units). APM only.

{% enddocs %}

{% docs capture_deferred_payments %}

Count of payments where capture was deferred or partially deferred. APM only — always blank for card payins.

{% enddocs %}

{% docs defer_capture_outcome %}

Outcome of the deferred-capture stage, used by APMs that confirm capture asynchronously. Sample values: 'deferred' (full amount deferred), 'non_deferred' (captured directly), 'not_available', 'partially_deferred'. 'not_applicable' for card payments. APM only — always blank for card payins.

{% enddocs %}

{% docs defer_capture_outcome_at %}

Timestamp (UTC) of the first deferred-capture event on the payment. NULL when capture was not deferred. APM only.

{% enddocs %}

{% docs defer_refund_outcome %}

APM only outcome of the payment during defer refund, either deferred or partially_deferred when a payment has deferred refund or non_deferred if the payment went straight to refund. not_applicable for card payments.

{% enddocs %}

{% docs defer_refund_outcome_at %}

Timestamp (UTC) of the first deferred-refund event on the payment. NULL when the refund was not deferred. APM only.

{% enddocs %}

{% docs refund_deferred_amount %}

The total value of deferred and partially deferred refundsin the payment's original currency (major units). APM only. Does not include unreferenced refunds.

{% enddocs %}

{% docs refund_deferred_amount_eur %}

The total value of deferred and partially deferred refundsconverted to Euros at the transaction-date FX rate (major units). APM only. Does not include unreferenced refunds.

{% enddocs %}

{% docs refund_deferred_amount_gbp %}

The total value of deferred and partially deferred refundsconverted to Sterling at the transaction-date FX rate (major units). APM only. Does not include unreferenced refunds.

{% enddocs %}

{% docs refund_deferred_amount_usd %}

The total value of deferred and partially deferred refundsconverted to US Dollars at the transaction-date FX rate (major units). APM only. Does not include unreferenced refunds.

{% enddocs %}

{% docs refund_deferred_payments %}

Count of payments where refund was deferred or partially deferred. APM only — always blank for card payins.

{% enddocs %}

{% docs return_outcome %}

Outcome of the return stage (APM only — e.g. ACH and SEPA returns). Sample values: 'not_available', 'non_return' (a refund or chargeback exists but no return), 'returned'. 'not_applicable' for card payments.

{% enddocs %}

{% docs return_outcome_at %}

Timestamp (UTC) of the first return event on the payment. NULL when the payment was not returned. APM only.

{% enddocs %}

{% docs returned_amount %}

The total value of returned payments in its original currency. APM only.

{% enddocs %}

{% docs returned_amount_eur %}

The total value of returned payments in Euros. APM only.

{% enddocs %}

{% docs returned_amount_gbp %}

The total value of returned payments in Sterling. APM only.

{% enddocs %}

{% docs returned_amount_usd %}

The total value of returned payments in US Dollars. APM only.

{% enddocs %}

{% docs returned_payments %}

Count of payments where the payment was returned. APM only.

{% enddocs %}

{% docs service_type %}

Service/delivery type associated with a successful capture (e.g. ACH). Sample values: Sameday, Standard. Blank for APMs that do not use it. APM only — always blank for card payins.

{% enddocs %}

{% docs billing_address_region %}

The billing country associated to the card. Will be NULL if the customer has input country incorrectly. Card only — always blank for APM payins.

{% enddocs %}

{% docs card_expiry_month %}

The card expiry month, e.g., 12. Card only — always blank for APM payins.

{% enddocs %}

{% docs card_expiry_year %}

The card expiry year, e.g., 2026. Card only — always blank for APM payins.

{% enddocs %}

{% docs card_fingerprint_historic %}

A historic hash of the card number used to compare card numbers without exposing the PAN. Card only — always blank for APM payins.

{% enddocs %}

{% docs is_partial_authorisation %}

Indicates if partial authorisation was executed during the payment. Card only — always blank for APM payins.

{% enddocs %}

{% docs previous_scheme_transaction_id %}

Transaction ID of the previous transaction used by the scheme for recurring / MIT payments. Card only — always blank for APM payins.

{% enddocs %}

{% docs recipient_account_number %}

The recipient's account number. Card only — always blank for APM payins.

{% enddocs %}

{% docs recipient_name %}

The recipient's name (normalised first name + last name). Card only — always blank for APM payins.

{% enddocs %}

{% docs recipient_zip %}

The recipient's postcode. Card only — always blank for APM payins.

{% enddocs %}

{% docs authorisation_merchant_advice_code %}

Merchant Advice Codes (MACs) provided during authorisation by the scheme. Can indicate the payment card type, or, for declined transactions, whether the payment can be retried and how long to wait before doing so. Sample values: 02, 24, 40. See https://www.checkout.com/docs/developer-resources/codes/recommendation-codes#Mastercard_merchant_advice_codes. Card only — always blank for APM payins.

{% enddocs %}

{% docs merchant_advice_code %}

Merchant Advice Code indicating recommended action on a declined transaction. Sample values: 01 (Updated or additional information required), 02 (Try again later), 03 (Do not try again). See https://www.checkout.com/docs/developer-resources/codes/recommendation-codes#Mastercard_merchant_advice_codes.

{% enddocs %}

{% docs merchant_advice_summary %}

Human-readable summary of the merchant advice code. Sample values: New account information available, Cannot approve at this time, Do not try again.

{% enddocs %}

{% docs billing_descriptor_city %}

City appearing on the billing descriptor shown to the cardholder.

{% enddocs %}

{% docs authorisation_merchant_advice_summary %}

The recommendation summary associated with a given Merchant Advice Code (MAC). Sample values: Do not try again, Retry after four days, Non-reloadable prepaid card. See https://www.checkout.com/docs/developer-resources/codes/recommendation-codes#Mastercard_merchant_advice_codes. Card only — always blank for APM payins.

{% enddocs %}

{% docs is_bemi_entity %}

TRUE when the entity belongs to bemi-uab-lt, False otherwise. This field can be either pre-computed (for example fct_payin_daily) or joined at read-time via entity_id (fct_payin).

{% enddocs %}
