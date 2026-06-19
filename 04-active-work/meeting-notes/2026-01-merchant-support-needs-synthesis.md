# Merchant Support Needs — Discovery Series (January 2026)

**Source:** 8 meetings with AMs/TAMs, 13–22 January 2026  
**Purpose:** Understand support needs across top merchants before designing the tiered support model  
**Merchants covered:** Temu, eBay, Etraveli, Tango, Invygo, Tabby, Shein, Ant Financial, TapTap, Vesta, Calo  
**Drive folder:** https://drive.google.com/drive/folders/1Mnz7XMPGYaeZG0nHQ4_R9mYn06188zU8

---

## Key Findings

### 1. The AI agent is structurally inaccessible to the highest-value merchants

Temu, eBay, Shein, and Ant Financial all deliberately avoid the Checkout dashboard — either due to internal compliance rules (Temu, Shein) or strategic preference for API/report-first operations (eBay, Ant). These four merchants alone represent a significant share of TPV. The current AI agent (Fin) is dashboard-bound; it cannot reach them in their actual operating model. Any deflection strategy that relies on dashboard adoption will miss this segment entirely.

### 2. TPA / regional payment method issues account for ~25% of all annual tickets — and none of it can be automated

Mada refunds in KSA/MENA and APM issues in APAC (Mway, Multibanco, Pay to Card) follow the same pattern: no API exists to automate, manual escalation is required, and Checkout sits as intermediary between merchant and bank. Specific pain points:

- **Mada refunds after 30 days (and sometimes before):** Agents manually collect spreadsheets and send to TPAs up to 3× per week (Calo, Invygo). No batch refund API. Contested ownership — merchants never interact directly with the bank.
- **APM dispute/status queries (Shein):** ~60% of Shein's tickets. No dispute API for APMs; status checks require L2 escalation due to permission constraints.
- **Pay to Card RFI links (Shein):** Cardholders cannot open links; status requires manual L2 escalation. No API exists.
- **Proof of payout (Tango):** Scheme-portal document, issued manually, incurs a per-document fee (~$10). No API available.

Gabriele and Ahmad both independently estimated TPA issues at 25% of annual contact volume. Ahmad's recommendation: automate everything else first, then tackle TPA.

### 3. Transaction status and payment confirmation queries dominate — and are the most automatable

~60–70% of all care contacts are transaction-related (payment status, AR drops, void/refund confirmation). Validated independently across all 8 conversations. This is the clearest automation opportunity and the primary rationale for extending Fin to email/non-dashboard channels. Key blockers: authentication over email (no login token), and PCI/data handling sign-off from engineering.

### 4. Untracked support channels make true contact volumes invisible

APAC enterprises use proprietary IM apps that cannot integrate with Zendesk:
- **Temu:** Proprietary in-house IM (not WeChat)
- **Ant Financial:** DingTalk / InTalk (150-person chat group; tickets logged manually via screenshot)
- **ByteDance:** Lark (mentioned separately)
- **eBay:** Multiple dedicated Slack channels (AR, dev, P0/P1); almost never raises a Zendesk ticket

These accounts generate real support effort that is entirely absent from care metrics. Volume from top-tier merchants is systematically undercounted.

### 5. The VIP merchant definition is unresolved — and blocking the support model

Five separate conversations surfaced this. Current situation:
- No agreed company-wide definition; multiple conflicting versions in use
- Merchant tier is a poor proxy — some Tier 1s are unsophisticated and high-volume (Delivery Hero, Math Holdings); some Tier 2s are strategic (Calo at 100% SOW, growing 50% PV YoY)
- Tom Chesnoy's framing: VIP = accounts with genuine revenue upside, not just current tier
- Ahmad Jabr's framing: VIP designation should be region-dependent
- Gabriele's framing: net revenue and incentive rating (gold status) are better signals than tier alone

Practical signal available: share-of-wallet in Salesforce. <100% SOW = straightforwardly strategic. 100% SOW = requires AM input on growth trajectory.

### 6. Phone support is a known gap — raised by multiple merchants

Multiple AMs (Melissa for eBay, others) report merchants asking about phone support since joining Checkout. The current phone line is not fit for purpose. Other PSPs offer this. Merchant expectation is particularly strong for urgent/P0 scenarios. Proposed model: dedicated line restricted to VIP merchants, urgent queries only.

### 7. AMs and TAMs are absorbing queries that should route to formal channels

Tom Chesnoy: TAMs being used as catch-all escalation for Tier 1 unsophisticated merchants (Delivery Hero, Math Holdings) — diluting strategic focus. Ahmad Jabr receiving equivalent volume to the support team for Calo. Melissa for eBay managing multiple weekly calls on AR and integration queries. The support model redesign must define where AM/TAM engagement ends and formal support begins.

### 8. Self-service readiness varies widely — it's not just access, it's education

TapTap: large distributed support team (18 pages of dashboard users), but queries still come by email. Users have access but don't know how to use it. Vesta: reseller agents (Tekassi, CRBC) have no dashboard access due to a deliberate access decision by Vesta's own team — structural, not a product gap. Both are in scope for Q2 educational content pilot.

---

## Emerging Support Model (validated across series)

Three-tier model surfaced organically across conversations:

| Tier | Merchants (examples) | Support approach |
|---|---|---|
| **VIP** | Temu, eBay, Shein, Ant, Tango | Human touch + AM/TAM. No dashboard enforcement. Phone line for P0. AI optionally surfaced to AMs. |
| **Enterprise** | Etraveli, Tabby, Calo, TapTap, Kareem | Blended. Email + dashboard. AI agent on email (when auth solved). AM/TAM opt-in CC on tickets. |
| **Standard** | Vesta, Tier 2–5 | AI-first. Dashboard and web form as primary channels. Human escalation by exception. |

VIP vs Enterprise split is the unresolved decision. Criteria needed.

---

## Per-Merchant Quick Reference

| Merchant | AM | Region | Tier | Channel | Top issue | Dashboard? |
|---|---|---|---|---|---|---|
| Temu | Amber Lin | APAC | T1 | IM (proprietary) | Webhook mismatches, AR drops | No (compliance block) |
| eBay | Melissa | Global | T1 | Slack | AR monitoring, invoice reconciliation | Minimal (deliberate) |
| Etraveli | Konstantinos | — | T1 | Email + dashboard | OTA adjustment queries | Partial (finance team low-usage) |
| Tango | Konstantinos | Israel | T1 | — | Proof of payout | — |
| Invygo | Gabriele | MENA | T2 | Email | Mada refunds (300/350 tickets) | Yes (~40 users/week) |
| Tabby | Gabriele | MENA | T1 | AM-first | Auth failures, Mada TPA | Yes (~70–80 users/week) |
| Shein | Ziyuan/Madelyn | APAC | T1 | — | APM status, Pay to Card | No (compliance) |
| Ant Financial | Madelyn | APAC | T1 | DingTalk | Webhook misconfig, Payback sub-merchant issues | Partial |
| TapTap | Will | Africa/GCC | T1 | Email | Payment confirmation | Yes (but low knowledge) |
| Vesta | Will | UK | T2 | Email | Mada refunds, autoresponse loop | No (reseller access gap) |
| Calo | Ahmad | MENA/GCC | T2→T1 | AM + email | Mada/TPA manual refunds | — |

---

## Source Files (Google Drive)

| Meeting | Date | Drive ID |
|---|---|---|
| Amber / Charlie — Temu | 2026-01-13 | 1bpzDJMjMCB9Ah3niWRpdYKTzkE1FfjcgyUwe98JL_yc |
| Melissa / Charlie — eBay | 2026-01-13 | 1U-gL7lQvcLBmwMeFWz1u6XwBU34usZBiliKmq5gglbI |
| Tom / Charlie — support model | 2026-01-15 | 1sAS0Wind23QNeJ_FKYXTJugVVI3ht4wyE8t1oazvoeE |
| Konstantinos / Charlie — Etraveli + Tango | 2026-01-16 | 1TZMAGZjtvUqtwnI0KHRtamBwxYZEYY6-qbtUaaG9AFs |
| Gabriele / Charlie — Invygo + Tabby | 2026-01-20 | 1sDMzzjO0j64JqIzMqotgtG8WH0_CBDUAZuKFB2DkELQ |
| Ziyuan / Charlie — Shein + Ant Financial | 2026-01-21 | 1osy3pO4JJ1Gihy8K0havGtXhY19rn0T4_L3PExnQlB4 |
| Will / Charlie — TapTap + Vesta | 2026-01-21 | 1jLWIGF7SwSjUE29zfojVtuuhideju_N1W9oKALRKMFk |
| Ahmad / Charlie — Calo | 2026-01-22 | 1OlAM9XrM-wk9iohb4c-dGGdsuzydP52ijBStBMP6A3g |
