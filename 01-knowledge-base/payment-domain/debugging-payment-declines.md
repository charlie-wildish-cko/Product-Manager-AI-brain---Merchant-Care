# Debugging Payment Declines

How I diagnose declines from the **Payment Search API** record, using Checkout.com's own code references. Give me a payment `id`, `reference`, or a filter (BIN, issuer, scheme, country, date range) and I work from the structured record.

This doc cross-references:
- Field schema: `01-knowledge-base/metrics/payment search API schema.md`
- Code references: `Tech Docs/Articles/2 Developer resources/5 Codes/` (API response codes, AVS, CVV, ECI, Recommendation codes)

---

## 1. Read the response code range first, not the raw ISO code

Checkout.com does **not** return raw ISO 8583 codes in `response_code`. It returns its own five-digit code, and the **range prefix already buckets the decline**. The ISO value survives as the last digits (ISO `51` becomes `20051`), but you read the bucket and the *who* off the prefix.

| `response_code` range | Meaning | Who declined |
|---|---|---|
| `10xxx` | Approved | — |
| `20xxx` | Soft decline (retry may succeed) | Issuer / scheme |
| `30xxx` | Hard decline (fix required before retry) | Issuer / scheme |
| `4xxxx` | Risk response | **Checkout.com / risk engine** |
| `50xxx` | Payout decline | Checkout.com |

The single most useful read: a `4xxxx` code means *we* declined it (maps to `risk_flagged: true` / `risk_score` in the schema), while `20xxx`/`30xxx` means the **issuer** declined it. That distinction changes the fix entirely (tune our rules vs. cardholder/issuer action).

Common codes, corrected against the real taxonomy:

| `response_code` | `response_summary` | Bucket | Note |
|---|---|---|---|
| `20005` | Declined - Do not honour | Soft | The catch-all is a *soft* decline here, not a risk block. Retryable. |
| `20051` | Insufficient funds | Soft | Use `recommendation_code` / MAC for retry timing. |
| `20059` | Suspected fraud | Soft | Issuer-side suspicion, distinct from Checkout's `4xxxx` risk engine. |
| `20054` | Expired card | Soft | `30033` Expired card - Pick up is the hard variant. |
| `20014` | Invalid account number | Soft | — |
| `20065` | Exceeds withdrawal frequency | Soft | Velocity limit. **Not** SCA. |
| `20154` | 3DS authentication required | Soft | The real SCA step-up code (issuer wanted a challenge). |
| `43401` | 3DS authentication required | Risk | SCA step-up demanded by Checkout's risk layer. |
| `30041` / `30043` | Lost card / Stolen card - Pick up | Hard | Do not retry one-off; for recurring, request a new card. |
| `41101` / `42101` | Risk blocked transaction | Risk | Client- / entity-level risk rule. |
| `4x301` | Fraud score exceeds threshold | Risk | High `risk_score`. |
| `4x2xx` | Decline list (card / BIN / email / IP / domain) | Risk | On a client, entity, or Checkout decline list. |

## 2. Read the retry recommendation directly (don't guess backoff)

The explainer's "exponential backoff" guesswork is unnecessary. Checkout returns **`recommendation_code`** (present in the Payment Search schema, top-level and per-action):

| `recommendation_code` | Meaning | Action |
|---|---|---|
| `01` | Updated/additional info required | Trigger Account Updater, re-auth, or step up 3DS. Do not blind-retry. |
| `02` | Try again later | Retry is viable (over-limit, insufficient funds, velocity, blocked card). |
| `03` | Do not try again | Stop (account closed, suspected fraud, recurring agreement cancelled). |

For Mastercard, **`processing.partner_merchant_advice_code`** (MAC) gives the exact retry window, which is what governs Mastercard's Excessive Retry Prevention Programme:

| MAC | Action |
|---|---|
| `24`–`30` | Retry after 1h / 24h / 2d / 4d / 6d / 8d / 10d respectively |
| `21` | Do not try again (payment cancellation) |
| `40` / `41` | Non-reloadable prepaid / single-use virtual card |
| `42` | Sanctions score exceeded threshold |

Retrying outside the MAC window is a fineable scheme offence, so I check it before recommending another attempt.

## 3. Authentication and 3DS

The schema carries the outcome; the code refs tell me what the values mean.

- **`authentication_status`** (authenticated / failed / expired / rejected) approximates the 3DS `transStatus`. A `failed`/`expired` status under a `20154`/`43401` is the root cause: the merchant took the frictionless path and the issuer demanded a challenge. *Fix: restart and step up to a challenge.*
- **`eci`** is a scheme-specific coded value tied to liability shift, not a freeform level:
  - **Mastercard**: `02` success (shift), `01` stand-in success (shift), `07` recurring success (shift), `06` SCA-exempt (no shift), `00` failed/not attempted (**no shift**), `04` Identity Check Data Only (no shift).
  - **Visa / Amex / Discover / JCB / DCI**: `05` success (shift), `06` stand-in (shift), `07` exemption/failed/not attempted (**no shift**).
  - A no-shift ECI (`00` MC / `07` Visa) on a declined EEA transaction usually means the SCA gap *is* the decline cause, and liability sits with the merchant.
- **`three_ds_protocol_version`** and **`actions[].authentication_experience`** (frictionless vs challenge) confirm the flow taken.

The raw 3DS `transStatus`/CAVV payload and the applied SCA exemption flag (TRA, Low-Value, Trusted Beneficiary) are **not** in the search schema. Ask for the auth log if the diagnosis hinges on those.

## 4. Payload integrity

- **AVS** — `avs_check` carries the coded result. `D` (Visa) / `M` = full match; `A`/`B` = partial (street matches, ZIP/postcode doesn't); `G` = international issuer, not verified; `E` = system error. A postcode mismatch frequently triggers an automatic issuer decline (UK/US especially), so an `A` under a `20005` is a strong signal.
- **Expiry** — `card_expiry_month` / `card_expiry_year` confirm the card hasn't lapsed (cross-check a `20054`).
- **CVV** — Checkout's CVV result codes are `Y` (match), `D` (no match), `N` (should be present, absent), `P` (not performed), `U` (issuer unsupported), `X` (unavailable). **Not exposed in the Payment Search schema** — so a CVV-driven decline can't be confirmed from the record. This is a genuine gap; request the raw auth response.

## 5. Routing, cross-border, and category

- **Cross-border** — `issuer_country` against the acquiring geography (via `processing_channel_id`, `scheme_merchant_id`, `card_acceptor_id`) flags issuer default-blocks on international transactions. *Fix: evaluate local acquiring.*
- **Currency** — `currency` is the original request currency; conversion friction can drive soft declines.
- **MCC** — a Merchant Category Codes reference exists in the code docs, but the **four-digit MCC is not in the search schema**. I can read merchant identity, not category.

## 6. Credential lifecycle (recurring / card-on-file)

This is the schema's weakest area. Reference docs exist for **Network token provisioning codes** and **Real-Time Account Updater response codes**, but the search schema exposes none of:
- Network-token status (VDEP/MDES cryptogram active/suspended/deleted) — only `card_wallet_type` (Apple/Google Pay).
- Account Updater response (did a new card get mapped before the billing run).
- CIT vs MIT classification (`payment_type` is Regular/MOTO only) and the original network transaction ID / trace ID.

A `recommendation_code: 01` on a recurring decline is the cue to run Account Updater before retrying.

---

## Sequential debugging checklist

```
[Isolate scope]    -> filter records: single card, one issuer, one country, or global?
       │              (bin · issuer · issuer_country · scheme)
       ▼
[Read code range]  -> 2xxxx/3xxxx = issuer/scheme · 4xxxx = Checkout risk engine
       │              (cross-check risk_flagged · risk_score for 4xxxx)
       ▼
[Read retry rec]   -> recommendation_code 01/02/03 + partner_merchant_advice_code window
       │
       ▼
[Check auth]       -> authentication_status · eci (scheme-specific, liability shift) · experience
       │              (raw transStatus & exemption flags NOT in record)
       ▼
[Validate payload] -> avs_check · card_expiry_*
       │              (CVV result NOT in record)
       ▼
[Check routing]    -> processing_channel · scheme_merchant_id · issuer_country
                      (MCC, network-token & account-updater status NOT in record)
```

## What the Payment Search record cannot tell me

Ask for the raw payload only when root cause needs one of these:
CVV/CVC2 result code · raw 3DS `transStatus`/CAVV · applied SCA exemption flag · MCC · network-token (VDEP/MDES) status · Account Updater response · CIT/MIT classification and original network transaction ID.
