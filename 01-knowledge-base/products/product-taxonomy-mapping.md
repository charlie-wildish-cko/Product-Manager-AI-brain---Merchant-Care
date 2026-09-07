# Product to Support Taxonomy Mapping

**Status: hypothesis, unvalidated.** No product field exists on Zendesk tickets yet, so this mapping was built by cross-referencing documentation, not real contact data. Treat every row as a candidate signal, not ground truth. Revalidate once a product field lands on tickets (Zendesk custom field, or Fin Procedure metadata) — see "How to validate" below.

**Data file:** [`product-taxonomy-mapping.tsv`](product-taxonomy-mapping.tsv) — 177 rows covering 141 of 180 documented products (39 products had no plausible support-relevant link and are listed as "No mapping" below, not silently dropped).

---

## Purpose

Given a product, predict which support taxonomy Issue Types it's likely to generate contacts for — and the reverse: given a spike in an Issue Type, narrow down which products are the likely driver. Feeds three use cases:

- **Fin classification aid** — product context as a signal in Fin Attribute definitions.
- **Reactive product-quality signal** — a product launch or change predicts which issue types are likely to move (Reflex-style accountability).
- **Retrospective analysis** — attribute historical contact volume back to products once real tagging exists.

## Method

- **Grain: Issue Type**, not Case Type (too coarse) or Reason (too granular to map by documentation alone).
- **Source of signal**: [`product-definitions.md`](product-definitions.md)'s `Applies if` / `Does not apply if` / `Contact risk` / `Likely keywords` fields, cross-referenced against [`support-taxonomy.md`](../processes/support-taxonomy.md)'s `select this if` criteria per Issue Type. Both files already use a comparable structured schema, which is what makes this cross-reference tractable.
- **Strength, not boolean**:
  - `primary` — the issue type is a direct, expected consequence of using this product.
  - `possible` — plausible but secondary, indirect, or edge-case.
- Capped at up to 5 issue-type links per product. Links were rejected where the only connection was generic ("it's a payment method so it touches Accepting Payments") — every row must cite a specific shared signal in its `rationale` column.
- Built via 11 parallel category-batch passes over all 180 documented products, each batch given the full taxonomy text and its assigned product slice from `product-definitions.md`.

## Current coverage

| | Count |
|---|---|
| Total documented products | 180 |
| Products with at least one mapping | 141 |
| Products with no plausible mapping | 39 |
| Total product-to-issue-type links | 177 |
| `primary` links | 118 |
| `possible` links | 59 |

## No mapping (considered, not missed)

These products were reviewed against the full taxonomy and had no plausible support-contact footprint — typically internal/backend infrastructure, reference/config data, or not-yet-launched features with no live merchant-facing surface yet.

**Authentication / Business Account:** Standalone Authentication, Transfers, Same and Cross-currency Transfers, Pre-Disputes, Remember Me

**Issuing / Network Tokens / Payment Links / RTAU:** Authentication (Issuing), BIN Management, Card Product, Cardholder, Entity Structure, Issuing Region, Physical card PIN, SCA Exemptions (Issuing), SCA Out of Scope (Issuing), Real-Time Account Updater

**Partner Integrations and Plugins:** ACI, BR-DGE, GIG, Gr4vy, IXOPay, Payrails

**Payment Methods:** BLIK, Boleto Bancario, Cash App, Diners Club International, EFTPOS, Fawry, Jaywan, Klarna (Gateway), Klarna Crypto, Knet, STAR, STC Pay, TrueMoney, Twint, Venmo, WeChat Pay HK, Wero, Zip

## Known limitation

Two BNPL products (Swish, Vipps) show a `Disputes` link with `possible` strength despite their rationale stating the product does *not* support disputes — the link exists because merchants ask "can this be disputed?" even when the answer is no. This is a real support-contact driver worth keeping, but don't read `strength: possible` here as "this product has dispute risk" — read it as "this product generates dispute-status enquiries."

## How to validate

This mapping is unvalidated by design — it will be wrong in the tail. Correct it once either becomes available:

1. A product field on Zendesk tickets (even partial), cross-tabbed against actual issue-type volume per product.
2. Fin Procedure metadata that ties a resolved contact back to a specific product.

Until then, use this for directional prioritisation (e.g. scoping which issue types to check first when a product changes), not as a precise attribution source.
