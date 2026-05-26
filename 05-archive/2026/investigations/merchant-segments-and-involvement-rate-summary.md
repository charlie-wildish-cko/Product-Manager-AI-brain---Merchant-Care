# Merchant Segments & Fin Involvement Rate — Summary for COO / CPO

**Purpose:** Quick reference on what Merchant Segments are and how they connect to the 80% Fin involvement rate plan.

---

## What are Merchant Segments?

**Merchant Segments** are the three **support-plan tiers** for B2B merchants: **Standard**, **Enterprise**, and **Premium**. They are not product lines (Platform, Issuing, etc.) — they are how we tier *support* based on who the merchant is. Assignment uses three Salesforce fields: **Tier** (1–5, revenue/TPV), **Incentive Rating** (Gold/Silver/Bronze, revenue potential), and **Account Owner Territory = SAT** (Strategic Account Treatment for high-value brands).

**Short definition per segment (including proposed data definition):**

| Segment | Who they are | Data definition (proposed) |
|--------|---------------|----------------------------|
| **Premium** | Highest-revenue and strategic brands; mission-critical operations, named AM, highest-touch support (e.g. Netflix, Uber, Spotify). | Account Owner Territory = `SAT` **or** (Tier = `1` **and** Incentive Rating = `Gold`) |
| **Enterprise** | Strong revenue or growth potential; meaningful TPV or Gold/Silver upside; have an AM (e.g. eToro, Plus500). | Tier = `1` (not Gold) **or** Incentive Rating = `Gold` (not Tier 1) **or** (Tier = `2` **and** Incentive Rating = `Silver`) |
| **Standard** | Long-tail merchants; lower revenue, Bronze incentive rating; rely on Dashboard and self-service; Tier 5 has no AM. | All remaining — typically Incentive Rating = `Bronze` and Tier = `3`, `4`, or `5` |

**Segment size and volume:** Support volume is concentrated in the smaller segments.


| Segment    | % of merchants | % of tickets (2025 baseline) | % of contacts (last 6m) |
| ---------- | -------------- | ---------------------------- | ----------------------- |
| Standard   | 75%            | 36%                          | 34.6%                   |
| Enterprise | 20%            | 33%                          | 28.6%                   |
| Premium    | 5%             | 31%                          | 20.7%                   |


Full logic and examples: [care-success-plans.md](../01-knowledge-base/products/care-success-plans.md).

**Why it matters for Care:** Each segment has different **channel entitlements** and **SLAs**. Standard has no dedicated email — only AI Agent, Dashboard Webform, and Live Chat. Enterprise and Premium get email; Premium also gets Dedicated Slack/IM.

---

## How do they relate to the involvement rate plan?

The 80% Fin involvement target is **built by segment** because:

1. **Channel mix differs by segment.**  
   Standard sends 26.6% of contacts via email (despite not being entitled to it) and 33.5% via Webform. Enterprise and Premium each send >54% via email. So the *levers* that move the needle are different per segment.

2. **Levers are segment-specific or cross-cutting.**  
   - **Lever 1 — Fin on email:** **Premium & Enterprise only.** Standard is not entitled to email, so they’re out of scope for this lever.  
   - **Lever 2 — Standard → Fin (Dashboard):** **Standard only.** Enforcing the success plan (no email for Standard) redirects their email traffic to Fin in the Dashboard.  
   - **Levers 3–5 (Webform migration, Account unlock form, maintain chat):** Apply to **all segments**.

3. **Baselines and targets are per segment.**  
   Today: Standard 16.9%, Enterprise 6.2%, Premium 4.0% (last 6m). Target end of 2026: all segments in the high 70s–80% range so that **overall** involvement reaches 80%. We track and report by segment so we can see where adoption is lagging.

4. **The ceiling is segment-relevant.**  
   ~18.7% of all contacts are unreachable by Fin (internal CKO email, phone, Dedicated Slack/IM, AM/TAM). Premium has more of that (e.g. Dedicated Slack/IM), so their theoretical ceiling can be slightly lower — we document unreachable % per segment so the 80% target isn’t misread as “100%.”

---

## One-line takeaway

**Merchant Segments (Standard / Enterprise / Premium) are our support tiers; the involvement rate plan uses them to decide which levers apply to which merchants and to track progress toward 80% Fin involvement by end of 2026.**

---

**Source:** [care-success-plans.md](../01-knowledge-base/products/care-success-plans.md), [fin-involvement-rate-prd.md](roadmap-items/fin-involvement-rate-prd.md), [fin-involvement-rate-cpo-coo-memo.md](roadmap-items/fin-involvement-rate-cpo-coo-memo.md)
