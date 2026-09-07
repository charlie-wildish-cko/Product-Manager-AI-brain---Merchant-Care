---
confluence_space_key: MTC
confluence_parent_page_id: 8041431176
title: Payin & Payout Data Requirements — Master List for AI Agents
---

> **Deliverables**: Connect bot gateway to Payin and Payout BQ data source (Q3) · Payment reference lookup (Q3) · Customer Agent — Payout analysis (Q4) · Configure Fin for new PLC data source from Payments Search API (Q3)
> **Flywheel**: Fuel
> **Strategic goal**: Reduce cost of support
> **Metrics**: Fin involvement rate · AI resolution rate · Cost per contact
> **Owner**: Charlie Wildish
> **Status**: Draft — first pass, payin/payout only
> **Last updated**: 2026-09-04

---

## Purpose

Fin and Agent Consultant can only resolve data-dependent queries if the underlying data is actually reachable through an API, MCP, or BQ table. [fin-data-access-backlog.md](fin-data-access-backlog.md) tracks this at the **data source** level (e.g. "Payments API — confirmed live"). This document goes one level deeper: **field level**, in one master table per domain.

**TLDR**: almost every field Support needs for payin and payout already exists in the BQ marts (`fct_payin`, `fct_card_payout`, `fct_bank_payout_event`). The real gap is that the Payment Search API — what Fin and Customer Agent actually query today — exposes only a subset of it. That's a data-*plumbing* decision (query BQ directly vs. extend the API), not a data-*availability* problem. A short list of genuine gaps remains regardless of which path is chosen: Clearing status, Settlement ID, raw ACS transStatus/CAVV, and an explicit TPA-route flag.

### Sources

1. **Business requirements** — the "Payments" and "Payout" tabs of Charlie's [payment query fields sheet](https://docs.google.com/spreadsheets/d/1MpJuXQ6DPSRz3QLEVRaYX6aXYTaIC6RLxK6IDazBYjE/edit?gid=1616920855) — which fields Support needs, and (for payin only — payout hasn't been scoped yet) whether each is safe to expose via Fin (merchant-facing) vs. internal-only (Agent Consultant/human agents).
2. **The dbt mart schemas** — `fct_payin`, `fct_bank_payout_event`, `fct_card_payout` (`.yml` contracts, normally at `github.com/cko-bi/gcp-data-analytics-dbt/tree/main/models/payment/mart`; supplied directly by Charlie after GitHub access failed in this environment). Saved to [`dbt-schemas/`](../working-files/dbt-schemas/). **This is the authoritative source for the "BQ column" column below** — it's the actual data the Q3 "Connect bot gateway to Payin and Payout BQ data source" deliverable will connect to.
3. **Payment Search API — two schema docs, not reconciled with each other**:
   - [`payment search API schema.md`](../../01-knowledge-base/metrics/payment%20search%20API%20schema.md) — richer; the one Customer Agent's own spec treats as authoritative.
   - [`payment-search-spec.yaml`](../working-files/payment-search-spec.yaml) — an OpenAPI 3.0 spec for `POST /payments/search`; narrower for payin, but the only one of the two that models payout at all.
   - Both are what Fin/Customer Agent actually query **today**; the dbt schemas show what's *possible*, not what's *wired up*.
4. **Customer Agent reasoning requirements** — the draft [Transaction Analyser](https://docs.google.com/document/d/1BqJrfwy0Cj3Nkag2aH-_6E-pFRv7j9dt1_UQwc5_6jo/edit) prompt spec — see the dedicated section below.

**GitHub access note**: `GITHUB_TOKEN` in this environment is invalid/expired. Refresh it if a future pass needs to pull dbt schema updates directly rather than relying on manual file drops.

---

## Master table — Payin (`fct_payin`)

63 fields flagged "Need in Support = Yes" in the business sheet, cross-referenced against `fct_payin` and both Payment Search API schemas.

**TLDR**: 4 confirmed gaps (bold below) exist even at BQ layer — everything else is available in `fct_payin`; roughly a third of those fields aren't in either Payment Search API schema today.

| Field | `fct_payin` column(s) | In Payment Search API? | Fin-facing | Notes |
|---|---|---|---|---|
| 3DS protocol version | `three_ds_protocol_version` | Yes (both) | Yes | |
| Acquirer name | `acquirer_name` | No | Yes | BQ-only |
| Acquirer reference number (ARN) | Not confirmed as a flat column — appears only nested inside `dispute_event_data[]`/`fraud_event_data[]` | Yes (`arn`, schema.md only) | Yes | **Needs verification**: sheet treats ARN as distinct from RRN; confirm a payment-level flat ARN column exists |
| Acquirer response code | `authorisation_acquirer_response_code`, `capture_acquirer_response_code`, `refund_acquirer_response_code` | Yes (schema.md `acquirer_response.acquirer_response_code`) | Yes | BQ breaks this out per action stage — richer than the API |
| ACS challenge mandated | No exact match — `challenge_indicator_used` records the outcome, not an issuer-mandated flag | No | Yes | **Needs verification** of exact semantics |
| Action ID | `decoded_action_id` (+ nested `dispute_event_data[].action_id`) | Yes (both) | Yes | |
| Amount | `requested_amount` (+ per-stage: `authorisation_amount`, `captured_amount`, etc.) | Yes (both) | Yes | |
| Authentication experience | Not confirmed by exact name — closest is `authentication_flow_type`/`authentication_method` | Yes (both) | Yes | **Needs verification** this is the same concept |
| Authentication status | `authentication_outcome` | Yes (schema.md) | Yes | |
| Authentication transaction status (raw ACS Y/N/U/A/C/R) | **Not found** | No | Yes | **Confirmed gap** |
| Authorization Code | Not confirmed as a payment-grain flat column (fct_payin aggregates by outcome, not raw per-action codes) | Yes (both, `actions[].auth_code`) | Yes | **Needs verification** |
| Transaction ID (gateway transaction ID per action — auth, capture, refund, etc.) | Not found as a flat payment-grain column — `transaction_id` only appears nested inside `dispute_event_data[]` and `fraud_event_data[]`, scoped to disputes/fraud events only, not every action | Yes — `actions[].transaction_id` in `payment search API schema.md` ("identifier linking this action to the parent transaction"); absent from `payment-search-spec.yaml` | *(not in sheet)* | **Confirmed gap** (Charlie, 2026-09-07) — same pattern as Authorization Code above: fct_payin doesn't expose a per-action array at all, so any per-action identifier is only reachable via the API, not BQ. Distinct from `scheme_transaction_id` (the network/scheme-level ID, which does exist as a flat BQ column) |
| AVS check | `address_verification_service_check` | Yes (both) | Yes | |
| Card acceptor ID (CAID) | `card_acceptor_id` | Yes (schema.md only) | Yes | |
| Card activity (risk sub-signal) | `pre_authentication_risk_assessment_route_details` (nested rule triggers — no 1:1 "card activity" bucket) | No | Yes | Partial match, not exact |
| Card expiry date | `card_expiry_month`, `card_expiry_year` | Yes (both) | **No** | Internal only (PCI) |
| Card wallet type | `card_wallet` | Yes (both) | Yes | |
| Cardholder name | `cardholder_name` | Yes (both) | **No** | Internal only (PII) |
| Challenge indicator | `challenge_indicator_merchant_preference`, `challenge_indicator_used` | No | Yes | BQ-only |
| **Clearing status** | **Not found** | No | Yes | **Confirmed gap** — matches sheet's own flag; Q4 2026 ETA per [fin-data-access-backlog.md](fin-data-access-backlog.md) |
| Currency | `payment_currency_iso3` | Yes (both) | Yes | |
| CVV check | `card_verification_value_check`, `is_card_verification_value_check_present` | No | Yes | BQ-only |
| Date created | `requested_at` — no separate "created" timestamp found | Yes (`requested_on`, partial) | Yes | May be the same event as Requested on — confirm with business whether a real distinction is intended |
| Device activity (risk sub-signal) | `device_ip`, `is_fingerprint_ip_vpn`/`_proxy`/`_tor`/`_bogon_ip` | No | **No** | BQ-only, internal, richer than sheet concept |
| Device IP address | `device_ip` | No | **No** | BQ-only, internal, PII |
| Dispute ID | `dispute_event_data[].dispute_id` (nested) | Yes (`dispute_details.id`, schema.md) | Yes | |
| Dispute initiated date | `disputed_at` (payment-level earliest) / `dispute_event_data[].dispute_created_at` | Yes (schema.md) | Yes | |
| Dispute reason | `dispute_description_list` | Yes (schema.md) | Yes | |
| Dispute reason code | `dispute_reason_code_list` | Yes (schema.md) | Yes | |
| Dispute status | `dispute_outcome`, `receive_dispute_outcome` | Yes (schema.md) | Yes | |
| Disputed amount | `disputed_amount` (+ currency variants) | Yes (schema.md) | Yes | |
| Electronic Commerce Indicator (ECI) | `electronic_commerce_indicator` | Yes (both) | Yes | |
| Email | `customer_email` | Yes (both) | **No** | Internal only, PII |
| Fingerprint | `card_fingerprint`, `card_fingerprint_historic` | Yes (both) | **No** | Internal only |
| Fraud history (risk sub-signal) | `is_fraud_reported`, `fraud_reason_list`, `fraud_type_list`, `fraud_event_data` | No | Yes | BQ-only, richer than sheet concept |
| Fraud score | `prism_score` (ML-only score) | Yes (both, `actions[].fraud_score`) | Yes | BQ distinguishes `prism_score` (ML only) from the combined `pre_authentication_risk_assessment_score` — confirm which the sheet means |
| Identity (risk sub-signal) | Not confirmed as a distinct column | No | **No** | **Needs verification** — likely folded into risk-assessment rule triggers, not a standalone field |
| IP address | `customer_ip` | No | **No** | BQ-only, internal, PII |
| Is AFT | `is_account_funding_transaction_requested`, `is_account_funding_transaction_processed` (+ `has_aft_retry`) | No | Yes | BQ-only. **No AFT type/geography breakdown exists for payin** (domestic vs. cross-border) — only boolean flags. Contrast with `fct_card_payout`, which has `geographic_scope` (Domestic/CrossBorder/Unknown) for payouts. Could be derived by comparing `issuing_country`/`issuing_country_iso2` against `acquirer_country`/`acquirer_country_iso2`, but that's not a pre-built field — confirmed gap (Charlie, 2026-09-07) |
| Is disputed | `is_disputed` | Yes (both) | Yes | |
| Issuing bank | Not confirmed as a distinct column (only country/region fields spotted) | Yes (both, `issuer`) | Yes | **Needs verification** — API has it, BQ presence unclear |
| Issuing country | `issuing_country`, `issuing_country_iso2` | Yes (both) | **No** | Internal only |
| Local scheme | `card_scheme_local`, `card_local_schemes` | Yes (both) | Yes | |
| Locations (risk sub-signal) | `customer_ip_city`, `customer_ip_timezone`, `is_customer_ip_tor`/`_vpn`/`_proxy`/`_bogon_ip`, `device_ip_country` | No | **No** | BQ-only, internal, richer than sheet concept |
| Network token available | `is_card_cko_network_token_available` (+ `card_network_token_type`, `card_token_format`) | No | Yes | BQ-only. Answers "could a network token be used for this card" — eligibility, not what was actually used on this payment |
| Source type (token / ID / card) — was this payin submitted with a token, a stored source ID, or a raw card number | `source_type` | Partial — `source.type` exists in `payment-search-spec.yaml`, but its own description says it collapses to `card` for any card-derived source (token or raw PAN alike), so it does not reliably distinguish them in the response. Absent from `payment search API schema.md` entirely | *(not in sheet)* | **Confirmed correct field** (Charlie, 2026-09-04). Raised by a solutions engineer distinguishing FPAN-submitted vs NT/DPAN-submitted payins |
| Network token used (this payment) | `is_cko_network_token_used` | No | *(not in sheet)* | **Confirmed correct field** (Charlie, 2026-09-04), alongside `source_type` above. Distinct from "Network token available" above, which is an eligibility flag, not an actual-use flag |
| PAN type used at authorisation / authentication (FPAN vs DPAN) | `authorisation_pan_type`, `authentication_pan_type` | No | *(not in sheet)* | Not yet confirmed with Charlie — offered as a secondary signal since it records what was actually used for processing rather than what was submitted. CKO can sync-provision a network token against the FPAN before payment, so `source_type` and the processed PAN type can differ — worth checking if `source_type`/`is_cko_network_token_used` alone don't fully answer a given query |
| Token Authentication Verification Value present | `token_authentication_verification_value`, `request_token_authentication_verification_value` | No | *(not in sheet)* | New — TAVV is network-token-specific; a populated value is itself a signal the payment ran on a token. `request_...` is what the merchant sent, the other is what CKO returned at authorisation — compare both if reconciling a discrepancy |
| Payment ID | `payment_id` | Yes (both) | Yes | |
| Payment method | `payment_method_name`, `payment_method_group` | Yes (both) | Yes | |
| Payment type | `payment_type` | Yes (both) | Yes | Enum values need confirming (CIT/MIT is covered separately by `is_merchant_initiated`) |
| Processing channel name | **Not found** (only `processing_channel_id`) | Yes (`actions[].processing_channel_name`, schema.md) | Yes | Rare case — API has it, BQ doesn't |
| Recommendation code | `authorisation_recommendation_code` | Yes (schema.md only) | Yes | |
| Reference | `request_merchant_reference` | Yes (both) | Yes | |
| Requested on | `requested_at` | Yes (both) | Yes | |
| Response code | `acceptance_gateway_response_code` (+ per-stage variants) | Yes (both) | Yes | |
| Response summary | `acceptance_gateway_response_summary` (+ per-stage variants) | Yes (both) | Yes | |
| Retrieval reference number (RRN) | Not confirmed as a flat column distinct from ARN | Yes (`transaction_retrieval_reference_number`, schema.md — confirmed distinct from `arn`) | Yes | **Needs verification** in BQ |
| Risk flagged | `is_flagged_authorisation`, `pre_authentication_risk_assessment_outcome` | Yes (both, `risk_flagged`) | Yes | |
| Scheme merchant ID | `scheme_merchant_id` | Yes (schema.md only) | Yes | |
| **Settlement ID** | **Not found** | No | Yes | **Confirmed gap** — needs Financial Actions API or a settlements mart |
| Status | `payment_outcome`, `acceptance_outcome` | Yes (both) | Yes | |
| Submit evidence by date | `dispute_event_data[].evidence_required_by` (nested) | Yes (`dispute_details.submit_evidence_by_date`, schema.md) | Yes | |
| Total authorised | `authorised_amount` | Yes (both, `balances.total_authorized`) | Yes | |
| Total captured | `captured_amount` | Yes (both) | Yes | |
| Total refunded | `refunded_amount` | Yes (both) | Yes | |
| Transaction direction | Not a field — direction is structural (querying `fct_payin` vs. a payout mart) | Yes (`type`, schema.md) | Yes | API models it as a field; BQ models it as table choice |
| **Partner Merchant Advice Code (MAC)** | `authorisation_merchant_advice_code`, `authorisation_merchant_advice_summary` | No | *(not in sheet)* | Not a sheet field, but the Transaction Analyser doc flags this as unconfirmed and builds a compliance-relevant rule on it — see Customer Agent section below |

**Also confirmed absent from `fct_payin`, per the Transaction Analyser doc's own gap list**: raw 3DS CAVV payload, Account Updater raw response (only a `has_au_retry` flag exists), MCC¹, TPA route identification.

¹ *Correction: MCC is actually present as `mcc_used_payment_level`/`mcc_desc`/`mcc_group` — see the Customer Agent section below for where the doc's "not in schema" claims do and don't hold up.*

---

## Master table — Payout (`fct_card_payout` and `fct_bank_payout_event`)

~30 field concepts from the sheet's Payout tab. **No "Need in Support / For Fin / For Internal" scoping has been run on payout yet** — that column is blank throughout; running that exercise is the main open item, not data availability.

**TLDR**: no gaps against the business sheet, in either the BQ marts or the Payment Search API. Payout is the one place the API itself (not just BQ) has near-complete coverage — `payment-search-spec.yaml` is the only schema doc that models payout, and it matches the sheet almost field-for-field.

| Field | Applies to | `fct_card_payout` / `fct_bank_payout_event` column(s) | In Payment Search API (`payment-search-spec.yaml`)? |
|---|---|---|---|
| Requested on | Both | `requested_at` (card) / `payout_initiated_at` (bank) | Yes (`requested_on`, both) |
| Status | Both | `status`, `card_payout_outcome` (card) / `payout_event_type` (bank — full lifecycle: Created/Dispatched/Confirmed/Rejected/Returned) | Yes (`status`) — coarse only, BQ lifecycle is richer |
| Amount | Both | `requested_amount` (card) / `instruction_destination_amount` (bank) | Yes (`amount`) |
| Currency | Both | `payment_currency_iso3` (card) / `instruction_destination_currency_iso3` (bank) | Yes (`currency`) |
| Reference | Both | `reference` (card) / `recipient_reference`, `sender_reference` (bank) | Yes (`reference`) |
| Billing descriptor reference | Both | `billing_descriptor_name`/`reference` (card) / `recipient_billing_descriptor` (bank) | Yes (`billing_descriptor.reference`) |
| Processing channel ID | Both | `processing_channel_id` | Yes |
| Metadata | Card only | Not confirmed as a distinct column in `fct_card_payout` | Yes (`metadata`, CardPayout) — **needs verification in BQ** |
| Destination type | Both | `destination_type` (card); implicit for bank (table = bank) | Yes (`destination.type`) |
| Destination ID | Card | Not confirmed as an explicit column — inferred via `card_masked_number`/`card_bin` | Yes (`destination.id`) |
| Destination card expiry month/year | Card | `card_expiry_month`, `card_expiry_year` | Yes |
| Destination scheme | Card | `card_brand` | Yes (`destination.scheme`) |
| Destination last 4 digits | Card | `card_masked_number` | Yes (`destination.last4`) |
| Destination issuer / issuer country | Card | `issuing_bank`, `issuing_country`, `issuing_country_iso2` | Yes |
| Destination account holder name | Card | `card_holder_name`/`first_name`/`last_name` | Yes |
| Destination ID | Bank | `recipient_payment_instrument_id` | Yes (`destination.id`) |
| Destination bank code | Bank | `recipient_bank_code` | Yes |
| Destination branch code | Bank | `recipient_bank_branch_code` | Yes |
| Destination IBAN | Bank | `recipient_bank_account_iban` | Yes |
| Destination country | Bank | `recipient_address_country_iso2` **or** `instruction_country_iso2` — two candidate columns, ambiguous | Yes (`destination.country`) |
| Destination account holder name | Bank | `recipient_first_name`/`last_name`/`company_name` | Yes |
| Sender name | Both | `sender_full_name`/`first_name`/`last_name` (card) / `sender_first_name`/`last_name` (bank) | Yes |
| Sender type | Card only | `sender_type` | Yes (CardPayout only — matches sheet's "specific funds transfer types" note) |
| Action ID | Both | `action_id` | Yes |
| Action type | Both | `action_code_description` (card — hardcoded "Original Credit" for NAS records, weak match) / `payout_event_type` (bank) | Yes (`actions[].type`) |
| Processed on | Both | `card_payout_outcome_at`/`processed_at` (card) / `occurred_at` (bank) | Yes (`actions[].processed_on`) |
| Retrieval reference number | Card only | `retrieval_reference_number` | Yes (`actions[].processing.acquirer_reference_number`, CardPayout only — matches sheet exactly) |
| Response code / summary | Both | `gateway_response_code`/`summary` (card) / `cko_response_code`/`description` (bank) | Yes |
| Action reference | Both | Not clearly distinct from `reference` in either mart | Yes (`actions[].reference`) |
| Sanction screening | Card only | `sanctions_screening_status`, `sanctions_screening_manual_review_required` | Yes (`actions[].sanction_screening`, CardPayout only — matches sheet exactly) |
| Wallet (Apple Pay / Google Pay) | Card only | `card_wallet` | No — `CardPayout` in `payment-search-spec.yaml` has no wallet field | Not in the original sheet. Confirmed present in `fct_card_payout` (same column name as payin's `card_wallet`) |

**Bank-side sanction screening** uses a different (legacy) shape — `screening_result_action` plus `SanctionsScreeningAccepted`/`SanctionsScreeningRejected` lifecycle events — rather than a flat per-action flag like the card side.

---

## Fields available in the BQ marts with no business requirement yet

Not sheet gaps — these exist and go beyond what's currently been asked for. Worth reviewing next time support/Fin use cases for payin/payout are scoped.

**Payin** (`fct_payin`): routing/retry diagnostics (`has_sca_retry`, `has_processor_cascading`, `has_dunning_retry`, `has_aft_retry`, `has_avs_modification_retry`, `has_cvv_modification_retry`, `latest_retry_type_list`, `attempt_data_list` — a full per-attempt array); fraud reporting detail (`fraud_reason_list`, `fraud_type_list`, `fraud_event_data` struct); a full per-dispute-event array (`dispute_event_data`) carrying scheme case numbers, financial indicator codes, and evidence-submission arrays. These map directly onto "why did this keep failing / was this retried" and "give me the full dispute history" query types.

**Payout** (`fct_card_payout` / `fct_bank_payout_event`): richer decline-reason bucketing than the sheet asks for — `card_payout_outcome` (balance_reserved / sanction_screening / card_processing / manual_decline) and `rejection_data_failure_code` (categorised bank-rail rejection reasons) plus raw NACHA/SEPA return codes (`R02`–`R16`, `AC01`, `AC04`, `MS03`, `RR04`); `geographic_scope` (Domestic/CrossBorder); `funds_transfer_type`; `purpose`; `meta_business_category` (B2B/B2C/C2C/C2B); `validation_data_status` (recipient-account pre-validation: Pass/Caution/Fail) — directly relevant to a future payout decline-explainer.

---

## Customer Agent (Transaction Analyser) — where its "not in the schema" flags land now

The draft Transaction Analyser spec reasons over the two narrower Payment Search API schemas, not `fct_payin` directly. Its own explicit gap list, checked against `fct_payin`:

| Flagged as "not in schema" by the doc | Actually in `fct_payin`? |
|---|---|
| CVV/CVC2 result code | **Yes** — `card_verification_value_check` |
| MCC | **Yes** — `mcc_used_payment_level`, `mcc_desc`, `mcc_group` |
| Network token (VDEP/MDES) status | **Yes** — `is_card_cko_network_token_available`, `card_network_token_type` |
| CIT/MIT classification | **Yes** — `is_merchant_initiated` |
| `partner_merchant_advice_code` (MAC) — flagged as unconfirmed; a compliance-relevant Mastercard retry rule depends on it | **Yes**, differently named — `authorisation_merchant_advice_code` |
| Original network transaction ID | **Yes** — `scheme_transaction_id` / `previous_scheme_transaction_id` |
| Raw 3DS transStatus / CAVV | **Not confirmed** — don't assume resolved |
| Applied SCA exemption flag | **Yes** — `three_ds_exemption_code`, `authentication_exemption_applied` |
| Account Updater response | **Partially** — only a retry-attempt flag (`has_au_retry`), not the raw response |
| TPA identification mechanism | **Not confirmed** — plausible via acquirer/processor fields, no explicit flag |

**Implication**: Customer Agent's decline-explainer logic isn't data-starved — the Payment Search API it's built to call is the bottleneck. Two paths: (a) extend the Payment Search API with these fields, or (b) have Customer Agent query `fct_payin` directly (bihourly refresh — confirm that latency is acceptable for real-time decline explanation). This is the central open question for the Q3/Q4 Customer Agent work.

**Payout has no equivalent Customer Agent reasoning spec yet.** The doc's payout handling is a placeholder (recognise the record, report status/response code, escalate). Given BQ coverage is strong — including `validation_data_status` and categorised rejection/return codes — the blocker for the Q4 "Customer Agent — Payout analysis" deliverable is a reasoning spec and a query path, not missing data.

---

## Open Questions

1. **Does Customer Agent query the Payment Search API or BQ directly?** Determines whether every "No" in the API column above is an API-extension task or already solved by a BQ connection.
2. **Rows marked "Needs verification"** in the payin table (ARN as a flat column, Authentication experience, Authorization Code, Issuing bank, RRN, ACS challenge mandated, Identity) — confirm with data/eng before treating any of them as resolved or as gaps.
3. **Raw ACS transStatus / CAVV** — not confirmed present anywhere. May be a permanent gap (PCI-sensitive raw scheme data may not belong in an analytics mart).
4. **TPA route identification** — no explicit field anywhere; decide whether to infer from acquirer/processor fields or request an explicit flag.
5. **Payout Fin/Internal scoping** — no decision made yet for any payout field.
6. **Two Payment Search API schema docs, not reconciled** with each other or with a named live API version.
7. **Payout root-cause data outside Payment Search** — the Transaction Analyser doc names Retool (Payout-Search, Alfred, RFI dashboard), Snowflake (`MC_CHARGEBACKCONSOLIDATED`), and Salesforce (adjustments). Given how strong the BQ marts turned out to be, re-check whether these are still needed.
8. **Risk sub-signal exposure and PII/PCI governance** — see [payin-payout-data-infosec-summary.md](payin-payout-data-infosec-summary.md) for the data-sharing risk review this pass surfaced.

---

## Next Steps

1. Decide the Payment-Search-API-vs-BQ-direct question for Customer Agent.
2. Run the Fin/Internal scoping exercise on the payout tab.
3. Resolve every "Needs verification" row with data/eng.
4. Refresh `GITHUB_TOKEN` for future direct pulls.
5. Fold confirmed-available fields into [fin-data-access-backlog.md](fin-data-access-backlog.md) as scoped Procedures, once the API-vs-BQ decision is made.
6. Get InfoSec sign-off on data sharing before wiring any of this into Fin or Customer Agent — see [payin-payout-data-infosec-summary.md](payin-payout-data-infosec-summary.md).
7. Extend this master list beyond payin/payout — Settlements, Disputes (a full dispute mart likely exists given `dispute_event_data`'s richness), User Management, and Fraud/Risk.
