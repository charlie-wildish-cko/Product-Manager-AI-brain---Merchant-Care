# Workshop — Mapping Payment Data into Merchant-Friendly Explanations

**Date:** 2026-05-14  
**Attendees:** Charlie Wildish, Keziah Zhou, Francisco Goncalves, Jyoti Sharma, Jonathan Tse, Xabi Telletxea  
**Drive source:** 1SrsIcIELVgSVSDs4tA7q7DbYteAKhCeuZWgcWX-SzE0

## Context

Workshop to build a reference table — a living master document Fin uses to interpret payment field combinations and generate accurate, merchant-friendly explanations. Payment queries are ~50% of support volume; Charlie's estimate is ~90% are automatable with the right semantic layer.

## Key Points

**Architecture principle**
- Fin acts as a query messenger that cross-references retrieved payment metadata against the reference table. Fin does not interpret logic independently — the reference table is the source of truth.
- One entry per scenario: field name + value + applicable payment method/region → AI summary.

**Scenario walkthroughs** (decisions and gaps per scenario):
- **3DS upgrade bugs**: document in reference table.
- **Billing descriptor issues** (issuer concatenation): no Checkout fix possible — acknowledgement only.
- **Third-party authenticated payments** (XID field): XID accessibility unconfirmed — engineering investigation needed.
- **Android WebView errors**: not loggable by Checkout — help article resolution.
- **Apple Pay vs Google Pay**: two Google Pay token types (PAN-only and cryptogram); each needs distinct messaging.
- **MIT/CIT lookups**: partially automatable depending on historical payment ID availability.
- **Issuer decline codes**: match response code + issuer + acquirer combinations; use Gemini strategy.
- **Internal decline codes 212 and 230** (AFT-related): fully automatable.
- **Risk/fraud decline codes** (global 43xxx rules): must not be disclosed in detail — vague response only. Sensitivity flag needed in the reference table.
- **MB Way timeouts**: manual refund via SIPs portal required, 100-day limit — flag payments over 100 days as ineligible.
- **Sandbox 401/404 errors**: unconfigured card schemes — important for ISV rollout.
- **Flow 404 errors**: session expiry — single article needed.
- **20000 response code**: appearing across multiple APM scenarios — high-priority mapping entry.

**Documentation debt identified**
- Rule 34 documentation not updated since 2022. Multiple scenarios resolve to "create a help article." This is a content infrastructure problem as much as an AI data problem.

## Insights

- The reference table is the canonical architecture for AI-generated payment explanations. This is the same "embedded knowledge in data" concept from the Care 2030 workshop and the Apr 17 payments data explanations session — all three workstreams are converging on the same model.
- The hardest scenarios require encoding field combinations, not individual field values — e.g. captured Mada vs. Visa refund rules, MIT referencing a prior CIT, ECI 0 on Google Pay.
- Global vs. merchant-level risk rules require different disclosure policies. The reference table needs a sensitivity/disclosure flag column.
- Two specific data availability gaps requiring engineering investigation before automation: XID field (third-party auth) and previous-payment-ID (MIT chains).
- MB Way is a candidate for tooling investment (Retool for APM status corrections), not just documentation.
