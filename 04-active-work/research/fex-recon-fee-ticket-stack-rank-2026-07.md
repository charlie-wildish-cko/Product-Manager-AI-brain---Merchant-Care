# FEX Reporting & Recon/Fee Ticket Analysis — Stack Rank for Finance Experience Product Review

**Date:** 2026-07-14
**Source data:** "FEX reporting tickets last 6 months" (93 tickets) and "Recon and fee tickets last 6 months" (623 tickets), 716 tickets total. Fields used: Case Type / Issue Type / Reason (Unified), Zendesk Description (first customer message), Zendesk Group (L1 vs L2/Seniors), Contacts.
**Purpose:** Identify and rank the underlying merchant problems driving these two ticket cuts, for Finance Experience product team prioritisation.

---

## Methodology

1. Grouped both files by taxonomy (Case Type / Issue Type / Reason) to get volume and L1/L2 split per category.
2. Read description text within each category to find sub-themes — the taxonomy tags group tickets that are actually different underlying problems (e.g. "Reconciliation issue" covers everything from missing transactions to timezone confusion).
3. Merged sub-themes that appear in both files under the same root cause (e.g. "no reference ID to map a report line to a transaction" shows up under both Reconciliation and Fee inquiry).
4. Ranked using a **weighted score** = ticket count, with L2/Seniors tickets counted at 2x (L2 is the more expensive, second-line channel per your flag). This surfaces problems that are expensive to run even at lower volume, not just the loudest by count.

**Confidence note:** FEX file (93 tickets) was read in full. Recon file (623 tickets) sub-theme counts are sample-based (agent read ~150-160 of 623, keyword-clustered and extrapolated) — treat Recon sub-theme volumes as directional, not exact. Taxonomy-level totals (the table below) are exact.

---

## Taxonomy-level volume (exact counts)

| Case Type | Issue Type | Reason | Count | L1 | L2 | %L2 | Weighted score |
|---|---|---|---|---|---|---|---|
| Funds and fees | Settlements | Reconciliation issue | 322 | 232 | 88 | 27% | 410 |
| Funds and fees | Billing & fees | Fee inquiry | 296 | 233 | 43 | 15% | 339 |
| Data and analytics | Reporting | Data mismatch / missing | 23 | 1 | 22 | 96% | 45 |
| Data and analytics | Reporting | Report not generated / missing | 23 | 1 | 22 | 96% | 45 |
| Data and analytics | Reporting | SFTP configuration | 21 | 1 | 20 | 95% | 41 |
| Data and analytics | Reporting | Custom report request | 13 | 0 | 13 | 100% | 26 |
| Data and analytics | Reporting | Other | 11 | 1 | 10 | 91% | 21 |
| (residual: stray Funds and fees/Reporting, Transaction status non-3DS, Accepting payments) | | | 6 | 4 | 2 | 33% | 8 |

Two things jump out before even reading descriptions: the Recon file is high-volume but mostly L1-resolvable (15-27% L2); the FEX file is low-volume but almost entirely escalates to L2 (91-100%) — every FEX reporting ticket is expensive to run regardless of its size.

---

## Stack rank — cross-cutting problems

Ranked by weighted score where estimable; problems 8-9 are ranked above their score on severity/reputational risk, flagged explicitly.

### 1. Fee/invoice line-item breakdown and taxonomy clarity — ~198 tickets, 15-19% L2
**Problem:** Merchants see a fee total (interchange, scheme fee, MDR, gateway fee) on a settlement/invoice line but can't get a breakdown of what it's composed of, or don't understand how CKO's fee taxonomy maps to what they expected. Not a data bug — it's a comprehension/self-service gap.
**Evidence:** Pagsmile MENA (111953): "is there a breakdown of how you charge for the 0.07 gateway fee?" Beamo.co (124982): "why the interchange variable fee is missing?" UAB ConnectPay (113751): asks CKO to confirm mapping of dashboard fee labels to invoice categories.
**Escalation:** Flat 15-19% across all fee sub-themes — no sub-theme escalates meaningfully above baseline, meaning L1 usually resolves this with an explanation. That confirms the fix is content/self-service, not engineering.
**Recommended fix:** Self-service fee breakdown view or documentation (fee taxonomy glossary mapped 1:1 to invoice line labels), not a support-driven explanation loop. Owner: Fin/content + FEX product.

### 2. Missing reference/payment ID on report and fee lines — ~140 tickets combined, elevated L2 (~30%+)
**Problem:** Report and adjustment lines (settlement, fee, FAR) frequently show no `pay_` ID, ARN, or reference — merchants can't tie a line item back to a specific transaction. Appears identically in both files: reconciliation (~89 tickets) and fee adjustments (~51 tickets), plus stray rows (Tabby, Zain KSA).
**Evidence:** NymCard (111536): "the Reference ID is null... Can you tell me which Reference ID these fee adjustments apply to?" Al Tayer Retail Omni (140918): "the ARN number on checkout is not matching with our settlement report." Minor International (141538): "Why does it not have a reference number and payment id?"
**Recommended fix:** Product/data fix — ensure every report/adjustment line carries a resolvable transaction reference by default. This is the single most repeated structural complaint across both ticket cuts.

### 3. Report format/structure comprehension — ~74+ tickets
**Problem:** Merchants (often finance/ops, not engineers) can't parse the FAR/settlement file structure — column meaning, multiple files per period, naming conventions.
**Evidence:** Farfetch (137561): pastes raw FAR column headers as the entire complaint. DANIBROOK (140552): confused by oddly-split CSV files per entity/currency.
**Recommended fix:** Documentation/UX — annotated report schema reference, in-product tooltips. Owner: content + FEX.

### 4. Transactions genuinely missing from reports/feeds — ~34 tickets combined, 53% L2 in Recon bucket
**Problem:** Distinct from #2 — the transaction isn't just hard to find, it's absent from the report/payout file entirely, often at a period boundary or SFTP feed gap.
**Evidence:** Organic Formula Shop (115352): "January 31st transactions excluded from the Jan Payout report." Winamax (124541): "nearly 400 transactions are missing... verified as captured on your dashboard." BYTEDANCE (107195): "2 missing refund transactions."
**Recommended fix:** Engineering — this is a genuine data-integrity gap, not a comprehension issue. Highest escalation rate of any Recon sub-theme (53%). Priority for engineering triage.

### 5. Report delivery / feed reliability (SFTP + API-vs-file inconsistency) — ~47 tickets combined, 39-100% L2
**Problem:** Reports/files simply don't arrive on schedule, or data visible via one channel (API, dashboard) is absent from another (SFTP file). Includes the largest single theme in the FEX file: settlement/payout files absent from SFTP for extended periods.
**Evidence:** Careem (132047): "gap of approximately 8 weeks of settlement data." Moonpay (124558): flagged business-critical. SONY EUROPE (105899): actions visible in Financial Actions API but absent from FAR by Date/Payout ID. BYTEDANCE (139080): "stopped receiving settlement files... since 0603."
**Recommended fix:** Engineering — pipeline reliability. Near-100% L2 in the FEX bucket; this is expensive every time it happens even though volume is modest.

### 6. FX/multi-currency reconciliation and fee transparency — ~90 tickets combined (37 recon + 53 fee), 15-32% L2
**Problem:** Two flavours of the same root cause — FX isn't clearly isolated in reconciliation reports, and merchants can't get the specific conversion rate applied to a transaction.
**Evidence:** 37GAMES (117892): "$3K discrepancy... relative to the holding currency amount." Temu (133440): requests explicit scheme FX rate table.
**Recommended fix:** Product — surface applied FX rate per transaction in reports; isolate FX as its own report column.

### 7. Genuine data-integrity bugs surfaced by sophisticated merchants — ~7-8 tickets, 90-100% L2, flagged for severity not volume
**Problem:** Low count, but these are confirmed defects found by merchants doing their own reconciliation, not comprehension gaps.
**Evidence:** CEXIO (116115): "response_description column value is incorrectly shifted into breakdown_type and processing_currency_amount columns." Minor International (142967): "There should only be 1 Financial Actions By Payout ID report per entity per day. But that does not seem to be the case." Expedia (134632): 5 AliPay payments captured/refunded twice in a settlement file. Alviere (117609): settlement file missing the "Capture" breakdown type present in all others.
**Recommended fix:** Direct engineering triage — small volume, high reputational/financial risk if unaddressed (duplicate settlement entries, corrupted columns).

### 8. Timing/timezone-driven false mismatches — ~10 tickets, 50% L2
**Problem:** Reports generated in different timezones (UTC vs. local — HKT, Riyadh, Bahrain) or around a daily cutoff produce apparent discrepancies that are actually period-boundary artifacts.
**Evidence:** Sharaf (113651): "Balance Action Report in both UTC and Riyadh time zones... discrepancy of AED 5.50." AL ANSARI EXCHANGE (116927): transactions after 20:00 cutoff settle two days later than expected.
**Recommended fix:** Cheap documentation fix (state report timezone/cutoff explicitly on every report) — punches above its weight at 50% escalation for a ~10-minute-to-explain issue once documented.

### 9. Recurring manual report requests that should be scheduled deliveries — ~8+ tickets, low volume, 100% preventable
**Problem:** Same merchants (Guesty x3, Finsa x3+) request the identical report on a recurring cadence via support instead of having it scheduled.
**Evidence:** Guesty submits "report of all sub entities balances (UK and Luxemburg)" three separate times (133555, 134069, 132441). Finsa requests the same payout/balance report monthly across multiple tickets.
**Recommended fix:** Cheapest fix in this entire analysis — enable self-service report scheduling. Directly eliminates repeat contacts from known accounts.

### 10. SFTP/report onboarding and field-enablement friction — ~20 tickets combined, self-service gap
**Problem:** Routine, repeatable config tasks (new SFTP connection, enabling report fields/columns) require a support ticket and backend provisioning rather than self-service.
**Evidence:** Wise (128976): "missing fields in the FAR... Can we please enable these ASAP? They need these fields to go live." Discover Car Hire (130231): requests SFTP setup for Settlements/Payouts reports.
**Recommended fix:** Self-service SFTP/field configuration in-dashboard.

### 11. Chargeback fee disputes — ~18 tickets
**Problem:** Merchants dispute the existence, amount, or contractual basis of chargeback fees, or find discrepancies between dashboard-shown and FAR-shown chargeback fees.
**Evidence:** Bookdelivery.com (142204): "What's this 29 pound chargeback fee? This is not what we have under contract."
**Recommended fix:** Content/comms — clearer chargeback fee documentation at point of charge, cross-check dashboard vs. FAR consistency.

---

## Cross-cutting observations

- **Data quality gap:** ~15-18 tickets across both files are screenshot-only or auto-generated IM tickets with no usable text — these couldn't be themed from description alone. Worth flagging to whoever owns ticket intake QA.
- **Recon file (fee/reconciliation) is largely an L1-resolvable comprehension problem** (content/self-service fixes dominate: #1, #3, #6-part, #9, #10, #11). **FEX file (reporting) is where the genuine engineering bugs concentrate** (#4, #5, #7) — small volume, near-100% L2, business-critical flags present (Moonpay).
- If FEX product capacity is constrained, the highest-leverage split is: **content/self-service team takes #1, #3, #9, #10, #11; engineering takes #4, #5, #7** as a priority queue regardless of raw volume, since these are the ones actively burning L2 capacity per ticket.

## Recommended next step

Validate the Recon sub-theme volumes (currently sample-extrapolated) with a full classification pass if this analysis is going into a roadmap decision rather than a directional review — happy to run that as a follow-up.
