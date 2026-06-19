# Invygo — Merchant Support Needs

**Meeting:** Gabriele D'Elia / Charlie — 2026-01-20  
**AM:** Gabriele D'Elia  
**Segment:** Tier 2, MENA (Dubai), car rental  
**Drive source:** 1sDMzzjO0j64JqIzMqotgtG8WH0_CBDUAZuKFB2DkELQ

---

## Merchant Profile

Tier 2 car rental merchant based in Dubai. Low payments sophistication — has its own support team that contacts Checkout on behalf of end customers. Active dashboard users (~40 users logging in per week for payments and settlements). Processes with Mada in KSA via a Third Party Acquirer (TPA/SAB).

---

## Support Channels Used

- Email (primary)
- Dashboard (operational use — payments, settlements pages)

---

## Primary Support Needs and Pain Points

**Mada refunds via TPA (KSA)**
~300 of Invygo's ~350 tickets are Mada refund requests. Mada payments processed via SAB (Saudi Acquiring Bank) cannot be refunded through the standard process after 30 days and require manual processing. The root cause is the car rental model: unexpected post-rental charges (e.g. fines, damage) arise long after the rental period, triggering late refund requests.

Ownership of the Mada refund process is contested between Invygo, Checkout, and the TPA. Merchants in KSA/GCC never interact directly with the bank — Checkout holds that relationship.
> "Charlie: 'I've got a list of we've got about 350 tickets from them. 300 were for the refund and that's primary.'"
> "Gabriele: 'The TPA is kind of okay with this process because it removes some complexity from them and knowing these banks in Saudi probably they will push back to take ownership.'"

No self-service or automated resolution path exists for these queries.

---

## Key Insights

- Invygo's ticket profile is almost entirely one issue: Mada/TPA refunds. Solving the TPA automation problem would reduce this merchant's contact volume by ~85%.
- TPA issues are structurally resistant to automation — no API to receive refund batches, ownership is contested, and the Financial Partnerships team needs to negotiate with the bank.
- MENA merchants in KSA/GCC that process with Mada and a TPA have a predictable support pattern. Invygo is likely not unique.
- The care team's workaround (spreadsheets sent to TPA up to 3× per week) is manual, brittle, and costly.
> "Our agents had to collect a spreadsheet and send a spreadsheet every three times a week. Like it's stupid. In 2026 we have to do those." — Charlie
