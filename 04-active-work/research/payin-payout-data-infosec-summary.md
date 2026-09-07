---
confluence_space_key: MTC
confluence_parent_page_id: 8041431176
title: Payin & Payout Data Sharing — InfoSec Review Summary
---

> **Deliverables**: Connect bot gateway to Payin and Payout BQ data source (Q3) · Customer Agent — Payout analysis (Q4) · Settlements analysis — Customer Agent (Q4, TBC) · Fin Data Policy Phase 1/2 (Q2–Q3)
> **Audience**: InfoSec / data governance review
> **Owner**: Charlie Wildish
> **Status**: Draft — requesting review before any payout data reaches Fin or Customer Agent. Settlements/Balances/Fees added as a preliminary preview, not a full review (see note below)
> **Last updated**: 2026-09-04

---

## Ask

We want to give two AI systems read access to payment (payin) and payout data so they can answer merchant support queries without a human agent. Before wiring this up, we need:

1. Confirmation of whether this falls under the existing Fin Data Policy / ARB sign-off track, or needs its own review.
2. A decision on the PII/PCI exposure questions below — in particular, **payout data has not yet been through the same "safe for AI to say out loud" scoping that payin has** (see "What's unresolved," below). We'd like that resolved before Q4, when Customer Agent starts reasoning over payout data.
3. Confirmation of what data-handling terms exist with Intercom (Fin's host) at the level of granularity in this doc, and whether Customer Agent's reasoning step runs on infrastructure that keeps the underlying data inside Checkout's boundary.

**Scope note**: this document is a full field-level review for payin and payout only. Settlements, Balances, and Fees are added below as a preliminary preview based on the public API schemas, because they're named in [fin-data-access-backlog.md](fin-data-access-backlog.md) and the 2026 roadmap as the next data sources Fin/Customer Agent will need. None of the three is live for Fin yet (Settlements: H2 2026, blocked on a latency fix; Balance: availability not confirmed; Financial Actions: confirmed live but not yet wired to Fin). Treat the preview as a heads-up, not a substitute for the same depth of review payin/payout got — recommend a proper pass once any of the three moves toward a live Fin/Customer Agent connection. Outages/Incidents (VisionNotify) is a different case: **that one is already live in Fin** (shipped Q2 2026) — included here as a retroactive check, not a pre-launch gate.

---

## What we're proposing

Two AI systems, two different risk profiles:

- **Fin** — Intercom's AI agent, installed in the Checkout Dashboard (merchant-facing chat) and in Zendesk (email/ticket handling). Anything Fin says to a merchant, or any data passed into Fin's own reasoning process, leaves Checkout's infrastructure for Intercom's.
- **Customer Agent** — a Care-owned reasoning layer that queries BigQuery and internal systems directly, reasons over the result, and returns a distilled plain-language answer to Fin. By design, **raw data does not leave Care's systems** through this path — Fin receives only the finished explanation, not the underlying fields. This is the main architectural safeguard in the current design, and worth confirming still holds once payout is added: verify Customer Agent's model itself runs on infrastructure that doesn't send raw records to a third party as part of its own reasoning step.

A third, lower-risk surface: **Agent Consultant**, which surfaces this data to human Care agents inside Zendesk — internal users, existing access controls, not covered in detail here but referenced where it changes what's "internal-only" vs. "Fin-facing."

The underlying field-level detail is in [payin-payout-data-requirements-master-list.md](payin-payout-data-requirements-master-list.md). This document summarises the PII/PCI shape of that data for review.

---

## What data is involved

**TLDR**: no full card numbers, no raw CVV values, and no raw cryptographic 3DS payloads appear anywhere in this scope. The sensitive categories are cardholder/customer PII (mostly already scoped internal-only), risk/fraud signals (already internal-only), and payout recipient/sender PII (not yet scoped at all).

**Example customer questions this data answers**:
- Payin: "Why was my payment declined?" · "Has this payment been refunded?" · "Was 3D Secure applied to this transaction?" · "Why is there a dispute on this payment, and when do I need to respond?"
- Payout: "Why hasn't my payout arrived yet?" · "Where was this payout sent?" · "Why was my payout declined or returned?"

| Category | Examples | Sensitivity | Current scoping |
|---|---|---|---|
| Payment identifiers & status | Payment ID, status, amount, currency, merchant reference | Low | Fin-facing — needed for nearly every query |
| Card metadata | BIN, last 4 digits, expiry month/year, scheme, card type, wallet type | PCI-adjacent, not regulated cardholder data | Mostly Fin-facing; expiry date and full cardholder name are marked internal-only |
| Cardholder/customer PII | Name, email, IP address, billing/shipping address, device fingerprint | PII | **Already scoped internal-only** — marked "Fin: No" in the business requirements sheet |
| Risk/fraud signals | Risk score, fraud rule triggers, device/IP reputation (Tor/VPN/proxy flags) | Sensitive, fraud-operational | **Already scoped internal-only** |
| Dispute data | Reason, status, disputed amount, evidence deadline | Moderate | Fin-facing — no PII beyond the payment itself |
| **Payout recipient/sender data** | Full name, address, date of birth, tax ID, ID document number, bank account number/IBAN, phone number | **PII, higher sensitivity than payin** | **Not yet scoped** — no Fin-facing/internal-only decision made for any payout field |

The dbt data contracts for all three underlying tables (`fct_payin`, `fct_card_payout`, `fct_bank_payout_event`) are tagged `security_classification: confidential` at the source, and PII-bearing columns are individually flagged `contains_pii: true` in the schema — that flagging is extensive on the payout side in particular (recipient/sender name, address, DOB, tax ID, ID number, bank account number are all flagged).

### What is explicitly NOT in scope

No field in the underlying schemas exposes: the full Primary Account Number (PAN), the raw CVV/CVC value (only a match/no-match *result* is available), track/chip data, or a raw 3DS cryptographic payload (CAVV). Worth stating directly to pre-empt the most obvious PCI question — this is a PII and payout-PII review, not a cardholder-data-environment (CDE) review.

---

## Settlements, Balances, and Fees — preliminary preview

Based on the public Checkout API schemas (`Balance`, `FinancialAction`, `FinancialActionBreakdown` — no dedicated Settlement schema was found; settlement data appears to be reported through Financial Actions and a `payout_type: AdHocSettlement` value on the bank payout mart, not a separate object — **needs confirmation with data/eng**). No dbt mart has been pulled for these domains, unlike payin/payout, so this is shallower than the rest of this document.

**Example customer questions this data answers**:
- Balances: "What's my available balance right now?" · "Why is my balance negative?" · "How much do I need to top up to release a payout?"
- Fees / Financial Actions: "What fee was taken on this transaction?" · "What FX rate applied to this payment?" · "Which settlement was this payment included in?"
- Settlements: "Why hasn't my settlement arrived?" · "What payments were included in this settlement?"

| Category | Examples | Sensitivity | Notes |
|---|---|---|---|
| Balances | Pending, available, payable, collateral, and operational balance amounts, per currency account | Business-financial, not PII | No cardholder or individual data at all — this is the merchant's own account position. **Main risk here is authorization, not PII/PCI**: confirm Fin/Customer Agent only ever returns a balance for the entity the requester is actually authenticated as, since a balance is meaningful business-confidential data if it leaked to the wrong merchant or platform sub-entity |
| Fees / Financial Actions | Payment ID, action type, entity/sub-entity ID, currency account ID, response code, MCC, FX rate and amounts, BIN, issuing bank, card type/category, acquirer reference number, AFT flag | PCI-adjacent (BIN, card type — same category already accepted for payin), otherwise business-financial | No new PII categories beyond what's already in the payin review: no cardholder name, email, address, or device data appears in this schema. Full PAN, CVV, and 3DS payloads are absent here too |
| Settlements | Not confirmed — likely surfaced via Financial Actions' `Payout ID` linkage, or via `payout_type: AdHocSettlement` on the bank payout mart | Not yet assessed | Needs its own field-level pass before this is meaningful for InfoSec review |

**Preliminary read**: Fees and Financial Actions look like a similar risk profile to payin (PCI-adjacent card metadata, no new cardholder PII) — likely a smaller lift for InfoSec than payout was. Balances introduces an authorization/entity-scoping question rather than a PII/PCI one. Settlements can't be assessed yet.

---

## Outages / Incidents (VisionNotify) — already live, retroactive check

This one already ships in Fin — "Add Outages API to Fin so it can tell merchants about outages impacting them" was marked Complete in Q2 2026.

**Example customer question**: "Is there an outage affecting my payments right now?"

**What Fin shares in response**: incident status, which of the merchant's own services are affected, and an ETA for resolution — scoped to that merchant's account only, pulled via a client-facing endpoint that infers the client from the caller's login rather than a merchant-supplied ID.

**The one open question**: whether the underlying data ever includes information about *other* merchants affected by the same incident, and whether an incident's free-text description could name a vendor or admit internal fault in a way that shouldn't go out verbatim in a support chat. Neither has been confirmed with a field-level schema review yet — recommend closing that out given this is already in production.

---

## What's already a good control

The payin side has already been through a first-pass risk-based filter: the business requirements sheet marks card expiry date, cardholder name, device signals, IP address, card fingerprint, issuing country, and all risk/fraud sub-signals as internal-only (`Fin: No`) — meaning Fin is not intended to ever say these out loud to a merchant, even though Agent Consultant (human-agent-facing, internal) can see them. That's the right default split and doesn't need InfoSec re-litigation unless the review below changes it.

---

## What's unresolved

1. **Payout PII has no Fin/Internal decision yet.** Every payin field went through a "should Fin be able to say this" pass; no payout field has. Payout carries materially more sensitive PII than payin (DOB, tax ID, ID document numbers, bank account details on top of name/address) — recommend this scoping happens with InfoSec input before the Q4 "Customer Agent — Payout analysis" deliverable ships, not after.
2. **Intercom (Fin's host) data-handling terms** — need confirmation these cover payment and payout PII at this granularity: data residency, retention period, whether Intercom trains models on this data, and what's covered by the existing Fin Data Policy workstream (2026 deliverables.md references Phase 1/2 sign-off via ARB — confirm this review is additive to that, not duplicative).
3. **Customer Agent's model hosting boundary** — confirm the reasoning step (the LLM call itself, not just the BQ query) runs on infrastructure that keeps raw records inside Checkout's boundary. "Data does not leave Care's systems" is the intended design; this needs an operational confirmation, not just a design statement.
4. **Output-level leakage risk** — even a field marked "Fin-facing: Yes" could leak more than intended depending on phrasing. Example: reading out a dispute reason verbatim, or a decline explanation that incidentally names an internal risk-rule trigger. Recommend a review pass on Fin's actual response templates once Customer Agent's decline-explainer is built, not just on the field list.
5. **Retrieval reference number / ARN ambiguity** — flagged in the master list as needing verification with data/eng; noting here because ARN/RRN are scheme-level identifiers that could be used to correlate a payment across systems, which may be relevant to a data-minimization assessment.
6. **Settlements, Balances, Fees have no field-level review at all** — see the preliminary preview above. Balances raises an authorization/entity-scoping question (right merchant, not wrong data); Settlements can't be assessed until its schema is confirmed with data/eng.
7. **VisionNotify (outages/incidents) already shipped without this kind of review.** No confirmed answer on whether an incident response could ever include other merchants' impact data, or whether free-text incident descriptions could leak vendor names or admit internal fault. Retroactive, not a launch gate, but recommend closing it out promptly since it's already live.

---

## Recommendation

1. Treat this as an extension of the existing Fin Data Policy ARB track — confirm scope with whoever owns that process rather than opening a parallel review.
2. Sign off on the payin Fin-facing/internal-only split as already scoped (Table above), pending no objection.
3. Run the same Fin-facing/internal-only scoping exercise on payout fields, with InfoSec input from the start rather than as a post-hoc review — this is the single highest-value ask in this document.
4. Get written confirmation of Intercom's data-handling terms at this data granularity, and Customer Agent's model-hosting boundary, before either system goes live on payout data.
5. Before Settlements, Balances, or Fees connect to Fin/Customer Agent (per the roadmap timing in the Scope note above), run the same depth of review payin/payout got here — in particular, confirm entity-scoping controls for Balances and get a real schema for Settlements.
6. Retroactively confirm VisionNotify never surfaces another merchant's impact data and get its incident response schema reviewed for free-text leakage risk — this one is already in production, so treat it as the most time-sensitive item on this list.
