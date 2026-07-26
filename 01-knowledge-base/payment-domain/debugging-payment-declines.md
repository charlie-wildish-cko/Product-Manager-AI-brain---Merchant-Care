# Debugging Payment Declines & Payout Failures

How I diagnose declines and payout failures from the **Payment Search API** record, using Checkout.com's own code references. Give me a payment/payout `id`, an `arn`/RRN, or a `reference` — single-identifier lookups only, no filters (BIN, issuer, scheme, country, date range) and no multi-payment search — and I work from that one structured record.

Sections 1–7 are written for **payins**. Section 8 covers **card and bank payouts**, which diverge structurally from payins (a second, Checkout-side decline layer exists before the issuer/network layer, and the record shows less of the picture — see §8).

This doc cross-references:
- Field schema: `01-knowledge-base/metrics/payment search API schema.md`
- Code references: `Tech Docs/Articles/2 Developer resources/5 Codes/` (API response codes, AVS, CVV, ECI, Recommendation codes)
- Per-code lookup, payins and payouts: `decline-code-reference.md` (its `50xxx` section and payout notes on `20xxx`/`30xxx` are the counterpart to this doc's §8)

---

## 1. Read the response code range first, not the raw ISO code

Checkout.com does **not** return raw ISO 8583 codes in `response_code`. It returns its own five-digit code, and the **range prefix already buckets the decline**. The ISO value survives as the last digits (ISO `51` becomes `20051`), but you read the bucket and the *who* off the prefix.

| `response_code` range | Meaning | Who declined |
|---|---|---|
| `10xxx` | Approved | — |
| `20xxx` | Soft decline (retry may succeed) | Issuer / scheme |
| `30xxx` | Hard decline (fix required before retry) | Issuer / scheme |
| `4xxxx` | Risk response | **Checkout.com / risk engine** |
| `50xxx` | Payout/refund decline | **Checkout.com** (pre-flight, before the payout reached the network/bank) |
| `INTERNAL*` | Pre-scheme validation reject | **Checkout.com / Card Processing** |

The single most useful read: a `4xxxx` code means *we* declined it (maps to `risk_flagged: true` / `risk_score` in the schema), while `20xxx`/`30xxx` means the **issuer** declined it. That distinction changes the fix entirely (tune our rules vs. cardholder/issuer action).

**`50xxx` only appears on payout/refund records, never on a payin.** It is the payout equivalent of the `4xxxx` distinction above — it means *Checkout* rejected the payout before submission, not the recipient's issuer or bank. See §8 for how this interacts with `20xxx`/`30xxx` on a card payout.

**Internal vs acquirer — the "internal 12 vs plain 12" rule.** An `INTERNAL*` code (e.g. `INTERNAL12` invalid transaction, `INTERNAL2` invalid value/amount) is a Card Processing validation reject that happened *before* the request reached the scheme. A plain `12` (surviving in a `20xxx`) is a straight issuer/scheme decline. They look alike and are the most common L1 misread. Tell them apart with **`acquirer_response`**: a pre-scheme internal reject has no acquirer authorisation data (`acquirer_response.acquirer_response_code` / `authorisation_description` empty or absent — the message never left Checkout), whereas an issuer decline carries an acquirer code and description. If you see an `INTERNAL*` code, name the internal reason and stop; do not narrate a 3DS/issuer story.

**Issuer declines are advisory only.** For a `20xxx`/`30xxx`, Checkout has no more insight than the record shows unless the scheme/issuer gives explicit feedback that a specific data element was missing. Card Processing knows no more than the record either. Give the reason and the retry recommendation as *guidance*; do not assert a definitive root cause the record does not support.

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

This table is the reasoning subset. The full per-code enumeration (all `20xxx` / `30xxx` / `2015x` codes with plain descriptions, merchant recovery actions, and retry disposition) is `decline-code-reference.md`.

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
- **Acquirer routing** — payload-formatting variations during network routing can inadvertently trigger an issuer risk block. The record shows the outcome, not the malformed field — the record alone cannot confirm a formatting delta.
- **Soft declines are often risk scores, not hard blocks** — a `20xxx` is frequently an issuer risk-*score* outcome (velocity, cross-border, anomalous MCC evaluated by engines like Falcon), which is exactly why it is advisory and retry-timed rather than a Checkout fault.

## 6. Credential lifecycle (recurring / card-on-file)

This is the schema's weakest area. Reference docs exist for **Network token provisioning codes** and **Real-Time Account Updater response codes**, but the search schema exposes none of:
- Network-token status (VDEP/MDES cryptogram active/suspended/deleted) — only `card_wallet_type` (Apple/Google Pay).
- Account Updater response (did a new card get mapped before the billing run).
- CIT vs MIT classification (`payment_type` is Regular/MOTO only) and the original network transaction ID / trace ID.

A `recommendation_code: 01` on a recurring decline is the cue to run Account Updater before retrying.

## 7. When not to debug in-house (spike, TPA)

- **Spike vs one-off.** Single-identifier scope means I cannot count occurrences across a merchant's traffic myself. If the context indicates a pattern (several payments failing the same way), don't hunt for a per-payment root cause — flag it as likely systemic and route to issuer outreach / the performance team (they have a bot) to confirm and size it.
- **TPA declines.** If the acquiring route is a Third Party Acquirer (e.g. Omanet, Cyber Source, MENA acquirers), ~95% of TPA declines cannot be resolved internally and must go to the TPA directly. Checkout and Card Processing have no additional visibility. Surface the TPA reference and route via the TPA escalation process; do not investigate further in-house.

## 8. Payouts

Payouts are a different diagnostic problem from payins, not a variant of the decline logic — the record shows less of the picture, and there's a second decline layer (Checkout itself) that doesn't exist for payins. The code-level lookup (what each code means, recovery action) now lives in `decline-code-reference.md`; this section is the reasoning layer on top of it — the payout counterpart to §1–2 above.

### 8.1 Recognition and rail

- `type: payout` (top-level) or `actions[].type: Credit` flags a payout record.
- **Establish the rail before reading any code** — bank payout or card payout. The diagnostic path fully diverges from here:
  - **Card payout** — behaves structurally like a payin decline: it can be rejected by Checkout pre-submission (`50xxx`), or declined by the recipient's card issuer/network after submission (`20xxx`/`30xxx`, same range as payin declines, reinterpreted — see below).
  - **Bank payout** — has no card-network decline layer. The record's main signal is `50xxx` (Checkout pre-flight, including `50401`–`50494` bank-account validation) or `status` alone (pending / returned) with no code — see 8.3.

### 8.2 Card payouts — two decline layers, read in order

1. **`50xxx` first.** Checkout rejected the payout before it reached the card network — compliance/sanctions (`500xx`), balance (`50003`/`50280`), recipient/sender/instruction validation, or amount/velocity limits. This is a Checkout-side rejection, not the recipient's card issuer, and it has no `recommendation_code` — there's no issuer response to advise on. See `decline-code-reference.md` §`50xxx` for the per-code disposition.
2. **`20xxx`/`30xxx` second, if `50xxx` isn't present.** Checkout submitted the payout and the recipient's card issuer or network declined it. This is the **same code range as payin declines**, but the meaning flips: it's the recipient's issuer refusing an incoming push payment, not the customer's bank refusing an outgoing charge. Not every `20xxx`/`30xxx` code carries a distinct payout reading — where the source specifically documents one (e.g. `20005`, `20057`, `20061`, `20065`, `20091`, `30015`, `30016`–`30019`, `30034`, `30045`), it's flagged in `decline-code-reference.md`; for codes with no payout-specific note, read the payin description but remember the direction is reversed (recipient, not customer).
3. **`recommendation_code` / MAC apply here, same as §2**, because this layer is a genuine issuer/network response — same caveat about respecting the MAC retry window before reattempting a payout.
4. **`partner_response_code` is the raw layer beneath both.** Scheme/issuer-specific, not stable across schemes — use it when the summary code doesn't explain the decline, same posture as raw codes on payin declines.

### 8.3 Bank payouts — status is the primary signal, not a code

Most real bank-payout issues surface as `status` (pending, returned) rather than a decline code, because there's no network-decline layer analogous to card payouts:

- **`50xxx` present** — read it directly; `50401`–`50494` (bank-account/beneficiary validation) is the dominant bucket for "why hasn't this landed." `50260` "Returned error" and `50499` "Payout Returned" mean the payout was sent and then bounced back — the record may not carry *why* beyond that; check `partner_response_code` first, and if empty, this is a genuine gap (see 8.4).
- **`status` alone, no code** — sanctions/RFI hold, beneficiary-detail error not yet coded, or clearing delay. This is the case the record cannot resolve — see 8.4.

### 8.4 What the record still can't tell me, for payouts specifically

Even with `decline-code-reference.md`'s `50xxx` table, the Payment Search record does not carry: the specific sanctions/RFI hold reason (only that one exists), the banking partner's own return reason when it isn't folded into a `50xxx` code or exposed via `partner_response_code`, or the clearing-delay cause. That detail lives in Retool (Payout-Search, Alfred, RFI dashboard), Snowflake (`MC_CHARGEBACKCONSOLIDATED`), and Salesforce (adjustments) — not in this record. Route via the owning team per the relevant SOP (`Care Agent SOPs/zendesk-kb/stuck-in-status-status-enquiry/`, `pay-to-bank/`) rather than guessing past what the code shows.

### 8.5 Still to confirm

The `50xxx` code table itself is unreviewed (see `decline-code-reference.md` Open items). Specific to this reasoning layer, still needs a Payouts/Pay-to-Card owner to confirm:
- Whether `recommendation_code` / MAC are ever populated on a `50xxx`-declined payout (expected no, since it's a Checkout-side reject, not an issuer response) — treat as unconfirmed rather than assumed.
- Whether `partner_response_code` is reliably populated for bank-payout returns, or only for card payouts as the PDF's example suggests.
- Whether a spike/systemic pattern across payouts (e.g. many `50401`s for one banking corridor) should route the same way as the payin spike/TPA guidance in §7, or differently.

---

## Sequential debugging checklist — payins

```
[Identify]         -> single-identifier lookup only: id · arn/RRN · reference
       │              (no filters, no multi-payment search)
       ▼
[Read code range]  -> 2xxxx/3xxxx = issuer/scheme · 4xxxx = Checkout risk engine
       │              INTERNAL* = Card Processing pre-scheme reject
       │              (cross-check risk_flagged · risk_score for 4xxxx;
       │               empty acquirer_response confirms an internal reject)
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

## Sequential debugging checklist — payouts

```
[Identify]          -> type: payout / actions[].type: Credit; single-identifier lookup only
       ▼
[Establish rail]    -> bank payout or card payout — path fully diverges from here
       ▼
  ┌─ [Card payout] ──────────────────────────────────────────────┐
  │  [Read 50xxx]     -> Checkout pre-flight reject? (compliance/  │
  │       │               balance/recipient/sender/limit)          │
  │       ▼ (if none)                                              │
  │  [Read 20xxx/30xxx] -> recipient issuer/network decline        │
  │       │               (payin code range, reversed direction —  │
  │       │                payout-specific note if one exists)     │
  │       ▼                                                        │
  │  [Read retry rec] -> recommendation_code / MAC apply here       │
  │       ▼                                                        │
  │  [Raw layer]      -> partner_response_code if summary unclear  │
  └────────────────────────────────────────────────────────────────┘
  ┌─ [Bank payout] ──────────────────────────────────────────────┐
  │  [Read 50xxx]     -> 50401–50494 = bank-account/beneficiary    │
  │       │               validation; 50260/50499 = returned       │
  │       ▼ (if no code)                                           │
  │  [Read status]    -> pending/returned with no code = sanctions/│
  │                      RFI hold, uncoded detail error, or        │
  │                      clearing delay — NOT resolvable from this │
  │                      record; route to Retool/Snowflake/SF      │
  └──────────────────────────────────────────────────────────────┘
```

## What the Payment Search record cannot tell me

**Payins.** Ask for the raw payload only when root cause needs one of these:
CVV/CVC2 result code · raw 3DS `transStatus`/CAVV · applied SCA exemption flag · MCC · network-token (VDEP/MDES) status · Account Updater response · CIT/MIT classification and original network transaction ID.

**Payouts.** The record cannot show: the specific sanctions/RFI hold reason (only that a hold exists) · the banking partner's own return reason when not folded into a `50xxx` code or exposed via `partner_response_code` · the clearing-delay cause. That detail lives in Retool (Payout-Search, Alfred, RFI dashboard), Snowflake (`MC_CHARGEBACKCONSOLIDATED`), and Salesforce (adjustments) — see §8.4.
