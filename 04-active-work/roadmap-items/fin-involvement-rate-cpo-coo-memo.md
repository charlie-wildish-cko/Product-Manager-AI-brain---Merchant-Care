# Fin Involvement Rate: Plan to Reach 80% by End of 2026

**To**: CPO, COO  
**From**: Charlie Wildish  
**Date**: February 2026  
**Topic**: Fin involvement rate is 9.2% today — structural gap, not a product gap. This is the plan to reach 80% by end of 2026.

## Summary

Fin only runs on Dashboard chat, which accounts for 9.2% of contacts. The other 90% arrive via email and the Webform where Fin has never been deployed. Five levers across those channels get us to 80.9% at the end of 2026 — but only if: (1) data policy is approved for Fin on email, and (2) Standard merchants are redirected from email to Fin chat. Without data policy approval, Enterprise and Premium miss their targets; without the Standard redirect, the second-largest lever stalls.

## Where We Are Today

Fin involvement is **9.2%** (2,162 / 23,481 contacts; last 6 months). ~18.7% of contacts are structurally unreachable by Fin — internal CKO email and phone/Slack/IM channels — which sets the **hard ceiling at ~81%**. The 80% target sits just inside it.


| Channel                         | % of contacts | Fin today               |
| ------------------------------- | ------------- | ----------------------- |
| Email (Merchant)                | 45.0%         | ❌ 0% — not deployed     |
| Webform & API                   | 22.1%         | ❌ 0% — separate channel |
| Account unlock form             | 4.9%          | ❌ 0% — not yet applied  |
| Other (phone, Slack/IM, AM/TAM) | 9.5%          | ❌ Unreachable           |
| Email (Internal / CKO)          | 9.2%          | ❌ Unreachable           |
| Fin (Dashboard chat)            | 9.2%          | ✅ ~100%                 |


By tier: **Standard 16.9%, Enterprise 6.2%, Premium 4.0%.** Enterprise and Premium send >54% of their contacts via email — where Fin has no presence.

## Strategy: Drive Involvement First, Then Balance Resolution

Getting Fin in front of more contacts immediately increases throughput and reveals where Fin fails — giving us the signal to invest in content, features, and data access. As involvement rises, resolution rate will dip because the query mix gets harder (email and Webform contacts are more complex than self-selected chat users). The plan accounts for this: **the target is 70% resolution rate at 80% involvement**, conditional on filling feature gaps, content, and data access in parallel.

**Involvement rate and resolution rate are tracked separately. This plan covers involvement.**

**How involvement and resolution interact as we scale:**


| Involvement rate       | Query mix                  | Assumed resolution rate | Overall AI resolution | Depends on                                              |
| ---------------------- | -------------------------- | ----------------------- | --------------------- | ------------------------------------------------------- |
| 10–15% (today)         | Chat-only                  | 60–70%                  | ~8–11%                | —                                                       |
| 25–35%                 | + Standard redirect to Fin | 50–60%                  | ~13–21%               | Policy enforcement                                      |
| 45–55%                 | + Webform migration        | 45–55%                  | ~20–30%               | Fin replicating Webform intake                          |
| 65–75%                 | + Email (P/E)              | 40–55%                  | ~26–41%               | Data auth + feature gaps                                |
| 78–82% (no investment) | Full mix                   | 35–45%                  | ~28–37%               | Nothing extra — but resolution is low                   |
| **78–82% (target)**    | Full mix                   | **70%**                 | **~55–57%**           | Feature gaps filled, content in place, data access live |


*Overall AI resolution = involvement rate × resolution rate.*

## The Five Levers

At **96% Fin involvement per lever**, overall rate reaches **80.9%**. At 80% per lever: 69.0%. At 90%: 76.4%. The bar is high — all levers must execute.


| Lever                                                                                         | Contacts   | % of total | Uplift at 96%     |
| --------------------------------------------------------------------------------------------- | ---------- | ---------- | ----------------- |
| **L1 — Fin on Email (Premium/Enterprise)**                                                    | 6,304      | 26.8%      | **+25.8 pp**      |
| **L2 — Standard → Fin (Dashboard)** (enforce success plan: Standard has no email entitlement) | 4,878      | 20.8%      | **+19.9 pp**      |
| **L3 — Webform → Fin chat** (Fin replicates Webform intake + routing)                         | 5,198      | 22.1%      | **+21.2 pp**      |
| **L4 — Account unlock form → Fin**                                                            | 1,159      | 4.9%       | +4.7 pp           |
| **L5 — Maintain Dashboard chat**                                                              | 2,162      | 9.2%       | (9.2 pp baseline) |
| Unreachable (not a lever)                                                                     | 4,391      | 18.7%      | 0                 |
| **Total**                                                                                     | **23,481** |            | **80.9%**         |


**Note — Fin on email as a Dashboard and self-serve bridge:** Fin email responses will include contextual links to the merchant's Dashboard and relevant self-serve resources. This serves two purposes: it increases Fin's resolution rate by directing merchants to the right tool; and it surfaces Dashboard and self-serve to Premium/Enterprise merchants who currently default to email, supporting longer-term channel shift. This is a design requirement for the email Fin UX, not a content add-on.

**Critical assumption — data authentication (Lever 1):** ~64% of Premium/Enterprise email volume is Payments In and Payouts queries that require merchant/transaction data. Without data auth, Lever 1 is worth +9.3 pp not +25.8 pp, and Enterprise and Premium miss their targets.


|                   | Lever 1 uplift | Enterprise after | Premium after |
| ----------------- | -------------- | ---------------- | ------------- |
| With data auth    | +25.8 pp       | 78.8%            | 78.2%         |
| Without data auth | +9.3 pp        | 42.5%            | 24.9%         |


## Phased Plan


| Phase                         | Timing     | What                                                                                                        | Owner                        |
| ----------------------------- | ---------- | ----------------------------------------------------------------------------------------------------------- | ---------------------------- |
| **1 — Instrument**            | Q1 2026    | Live involvement rate dashboard by tier/channel; tag unreachable contacts; confirm denominator              | Engineering + Zendesk Admins |
| **2a — Standard enforcement** | Q1–Q2 2026 | Stop accepting email from Standard; redirect to Fin chat. Policy change — no tech build. Fastest lever.     | Care Operations              |
| **2b — Fin on email (P/E)**   | Q2 2026    | Launch Fin on Email (Merchant) for Enterprise and Premium. Gated on data policy sign-off + auth classifier. | Engineering + Legal/Security |
| **3 — Webform migration**     | Q2–Q3 2026 | Fin chat replaces Webform as primary Dashboard support entry point. Dashboard Engineering dependency.       | Dashboard Engineering        |
| **4 — Gap close**             | Q3 2026    | Assess rate vs target; address residual gaps                                                                | Charlie Wildish              |
| **5 — Target review**         | Q4 2026    | Confirm 80% achieved or adjust                                                                              | Charlie Wildish              |


## Key Assumptions

1. **96% lever execution required.** Lower rates (80%, 90%) yield 69.0% and 76.4% respectively — both miss target.
2. **Data auth unlocks Lever 1.** Without it, E/P email is worth +9.3 pp not +25.8 pp. If delayed past Q2, the plan needs to be revisited.
3. **Standard redirects successfully.** 26.6% of Standard contacts arrive via email today despite no email entitlement. Assumes redirecting to Fin chat captures most of them.
4. **Fin replicates Webform.** Lever 3 requires Fin to replicate structured intake, ticket field population, and routing end-to-end. If it can't, a residual Webform population stays outside Fin's reach.
5. **Ceiling is fixed at ~81%.** Email (Internal) + Other (18.7%) are permanently unreachable. Any growth in those channels tightens the ceiling.
6. **Channel mix stays fixed.** The model holds last-6m channel proportions constant. If email share grows (e.g. Enterprise/Premium volume increases), levers 1–2 must convert more contacts and the 96% execution bar gets harder to hit. If email share falls, it gets easier. Review quarterly.
7. **Fin (Dashboard) share doesn't grow organically.** The model treats Dashboard chat as a static 9.2% baseline. In practice, chat adoption may increase as Webform migration proceeds and Dashboard UX improves — any organic lift reduces pressure on the other levers. This is an upside not in the model; track monthly.
8. **70% resolution at 80% involvement requires parallel investment.** Feature gaps, content coverage, and data access must be delivered in parallel — involvement rate alone does not get us there.

## What We Need

1. **Data policy decision (Security/Legal) — end Q1 2026.** Single biggest blocker. Without it, E/P email lever is halved and both tiers miss their targets.
2. **Standard email enforcement alignment — Q1 2026.** Care Operations sign-off needed; Standard is not entitled to email, but 26.6% of their contacts still arrive that way.
3. **Denominator confirmed with leadership — Q1 2026.** The ~81% ceiling must be understood before the 80% target is locked. Unreachable contacts stay in the denominator.
4. **Dashboard Engineering scoped for Webform migration — Q2 2026.** The only lever not within Care Product's control. Must be in Dashboard team's H1 plan.

---

**Owner**: Charlie Wildish  
**Next update**: Q1 2026 — after denominator confirmed and data policy decided  
**Questions to**: Charlie Wildish  
**Source data**: `support_contacts_flat_table_2025_last_6m.csv` (23,481 contacts, last 6 months)