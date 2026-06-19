# David / Charlie — Payment Data Table for AI

**Date:** 2026-05-20  
**Attendees:** Charlie Wildish, David Monasie  
**Drive source:** 1YW3Q9ippb1Z2njxwii4Vyx8_eCrvsAiymAEkkKPxNOw

## Context

Working session to review the payment data reference table architecture — the lookup/mapping sheet that converts raw payment metadata fields into plain English AI summaries.

## Key Points

- UX model agreed: high-level overview as default; merchant or agent can drill into granular detail on request. Works for both audiences.
- Table structure: field name + value + applicable payment method/region (wildcard = all) + AI summary.
- **Mada**: ~20% of support tickets. Specific 20030 format error message with refund window guidance (30 days for Visa, 24 hours for Mastercard). Bespoke messaging justified.
- **PayPal**: distinct "expired" status message needed.
- **Additional scenarios to cover**: payout reversals (Visa/Mastercard only, time-limited); APMs that cannot be refunded via API; acquirer-specific behaviours (TPA/SAB MPGs — specific settlement logic and edge cases).
- **Authentication flows**: challenge vs frictionless distinction. Even if merchant mandates challenge, ACS/issuer decides. This nuance should be embedded as a message.
- **`global_acquirer_name` field** can drive scenario branching — TPA/SAB MPGs is the key example.
- V1 target: cover 90–95% of scenarios before embedding into payment data automations.

## Insights

- Mada's disproportionate share (~20% of tickets) already justifies bespoke messaging and validates the payment data table as a priority.
- The table codifies tacit domain knowledge that is not documented anywhere in Checkout currently — it is both an AI tooling asset and an institutional knowledge asset.
- This table is the payment-data layer underpinning the May 14 workshop reference table, the Fin Procedures data access work, and the Agent Consultant semantic layer.
