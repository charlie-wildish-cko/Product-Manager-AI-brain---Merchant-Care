# Temu — Merchant Support Needs

**Meeting:** Amber Lin / Charlie — 2026-01-13  
**AM:** Amber Lin  
**Segment:** Tier 1, APAC, API-first enterprise  
**Drive source:** 1bpzDJMjMCB9Ah3niWRpdYKTzkE1FfjcgyUwe98JL_yc

---

## Merchant Profile

Top TPV generator. China-based operations. Multi-PSP. Does not use the Checkout dashboard due to an internal compliance policy preventing stakeholders from accessing individual PSP dashboards. All operations (reconciliation, disputes, transactions) run via API into their own internal portal. Reconciliation via SFTP reporting.

---

## Support Channels Used

- **Support email** (support@checkout.com) — used by ops and BD teams for reconciliation and disputes
- **Proprietary IM** — used for transaction-related issues and AR monitoring; Temu's own in-house app (not WeChat, not a third-party platform), no external integrations possible
- No dashboard usage (compliance block)

---

## Primary Support Needs and Pain Points

**Webhook / transaction status mismatches**
Temu relies on webhook finality but receives incorrect statuses — e.g. a decline response when the transaction actually succeeded. Triggers unnecessary support contacts.
> "The webhook respond with decline but in the end this transaction has been succeed then it will cause a bit confusion because they all rely on the web response but it's supposed to be like the final result but sometimes it will be changed."

**Acceptance rate monitoring**
Temu monitors AR at bin and country level, 24/7. Any drop triggers an IM query to verify whether it's isolated to their account or market-wide.
> "They anticipate a number drop so they need to make sure that that's they drop or entire apparently this being has been dropped for also for other merchants."

**Out-of-hours coverage**
Temu operates 10am–11pm, 6 days a week. After 8pm Checkout support is unavailable; AMs pick up IM messages.
> "After 8pm they will be still a lot IM messages be created there will be raising some issues regarding to the AR drops or some certain things and at that time AM and team has to pick up the message because the support is not available."

**Dashboard incompatibility (structural)**
Temu cannot use the dashboard by policy. Self-service tools and the current AI agent (Fin) are structurally inaccessible.

**APAC IM channel**
Temu's IM system is proprietary and closed to external integrations. All IM support is untracked — no Zendesk record exists for these interactions.

---

## Key Insights

- Fin and dashboard-based self-serve cannot reach Temu in its current form. Any AI deflection for this account requires a non-dashboard channel (email or IM integration).
- Webhook accuracy improvements would directly reduce contact volume before any AI layer is needed.
- L1 resolves ~two-thirds of Temu's tickets (146 L1 vs 77 L2 in data reviewed). Direct-to-L2 routing is not justified.
- APAC big-four merchants (Temu, Shein, and others) are structural outliers — the standard support product roadmap does not apply to them.
- After-hours coverage is a real gap: AMs are absorbing IM queries at night because the support team is unavailable.
