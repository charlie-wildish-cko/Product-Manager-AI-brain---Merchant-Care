# Product Definitions Backfill — Scope

**Anchor:** Reflex Q2/Q3 2026 (theme cluster → Product team mapping via Product Catalogue data). `product-definitions.md` feeds this mapping — a stale or incomplete file weakens Reflex's product attribution.

**Trigger:** 2026-08-13 catalogue sync found 108 products in the catalogue with no entry in `product-definitions.md`.

## Filtered to what's actually actionable

Of the 108 missing products, only **11 are in a live/customer-facing state** (General availability, Beta, Mixed availability, Pilot, or Live). The other 97 are `Roadmap` (11) or `Not on roadmap` (85, mostly long-tail regional Payment Methods — Affirm, Zelle, UPI, Amazon Pay, etc. — none of which merchants can currently use, so no support contacts to classify against them).

**Decision:** defer the 97 inactive products. Revisit only if the catalogue sync moves one of them into an active state.

## In scope — 11 products to write definitions for

| Product | Category | State |
|---|---|---|
| Commerce Protocols | Agentic Commerce | Mixed availability |
| Account Settings | Dashboard | General availability |
| Settings & Access | Dashboard | General availability |
| Configuration | Issuing | Mixed availability |
| Control spending | Issuing | Mixed availability |
| Developer needs | Issuing | Mixed availability |
| Reporting | Issuing | Mixed availability |
| Internal - FX Blotter reporting | Treasury & FX | General availability |
| PTC - FX based on Scheme FX rates (VISA/MC only) | Treasury & FX | General availability |
| Website Screening | Internal products | Beta |
| Airtable Product Catalogue | Internal products | General availability |

Note: the last two are internal/meta products (category = "Internal products") — per the sync skill's rule, flag rather than write a merchant-facing Fin definition; confirm with Product/Content whether they need a Zendesk field value at all.

## Status: done (2026-08-13)

All 9 non-internal products above now have entries in `product-definitions.md`, per instruction that the catalogue is source of truth — every catalogue value gets an entry, not just the ones with clean 1:1 overview text. Where a catalogue name maps to a capability already documented under a different heading, added a distinct entry that cross-references the fuller definition rather than skipping it:

- **PTC - FX based on Scheme FX rates (VISA/MC only)** — renamed existing heading to match the catalogue exactly (was missing the "(VISA/MC only)" suffix).
- **Reporting** and **Control spending** (Issuing) — added as short entries pointing to the existing fuller **Reporting (Issuing)** / **Spending Controls** definitions (same capability, catalogue uses a different label).
- **Developer needs** (Issuing) — added using its Airtable overview text (Transactions API / sandbox simulation / webhooks), cross-referenced against **Transactions (Issuing)**, **Simulation (Issuing)**, **Reporting (Issuing)**.
- **Configuration** (Issuing) — added as a general/umbrella entry; no Airtable overview, so it's written broadly and defers to the specific existing entries (BIN Management, Card Product, Cardholder, Entity Structure, Issuing Region) when a contact names a specific sub-area.
- **Account Settings** and **Settings & Access** (Dashboard) — added as distinct entries (profile/notifications vs. user roles/API keys), with the existing **Dashboard** entry updated to cross-reference both for disambiguation.
- **Internal - FX Blotter reporting** (Treasury & FX) — added, but flagged in its own entry as an internal treasury tool that shouldn't normally generate merchant contacts.
- **Commerce Protocols** (Agentic Commerce) — new `## Agentic Commerce` category section created (didn't exist before); entry flagged as unverified since Airtable has no overview text yet for this emerging capability — check with Product before relying on it for Fin classification.

**Still excluded:** Airtable Product Catalogue and Website Screening (category = "Internal products") — per the earlier agreement. Movement Protocols and Trust Protocols (Agentic Commerce, both still Roadmap) — deferred with the other 96 inactive-state products until they go live.

**Follow-up for Product/Content:** verify the Configuration and Commerce Protocols entries once Airtable overview text is filled in — both were written without source text and should be checked before Fin leans on them heavily.
