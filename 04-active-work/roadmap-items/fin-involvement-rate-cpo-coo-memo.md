# Fin Involvement Rate: Plan to Reach 80% by End of 2026

**To**: CPO, COO  
**From**: Charlie Wildish  
**Date**: February 2026  
**Topic**: Fin involvement rate is 9.2% today - structural gap, not a product gap. This is the plan to reach 80% by end of 2026.

## **Previous context:**

Modelling in the plan is based on volume for the new ++[Support plans/segments](https://docs.google.com/document/d/15OHpvfbfWVldFgKrJQB2L4dAJoWliuGKnQU2ZY0bZAc/edit?tab=t.sx7hqqinjh6q)++. Please familiarise with this if needed to see how these are calculated.

**Metric definitions (context)**

- **Fin involvement rate** — Share of all support contacts where Fin was the first touchpoint. Denominator = total support contacts (Zendesk tickets + Fin-only resolved); numerator = contacts where Fin participated (e.g. Dashboard chat, or email tickets with Fin as first responder once deployed). Unreachable channels (internal CKO email, phone, Slack/IM) stay in the denominator and set the ~81% ceiling.
- **AI resolution rate** — Of contacts where Fin was involved, the share that Fin resolved without human escalation (Fin-resolved / Fin-involved).
- **Overall AI resolution** — Share of all contacts resolved by Fin = involvement rate × resolution rate (e.g. 80% × 70% ≈ 56%).

## **Summary**

**Why we're doing this:** Reduce Checkout's cost of support and provide a faster support experience to merchants. Fin only runs today on Dashboard chat, which accounts for 9-12% of contacts. The other ~90% arrive via email (small T3 involvement for Fin) and the Webform where Fin has not been deployed. Five levers across those channels get us to ~80% at the end of 2026, but only if: (1) security policy is approved for Fin on email sharing payments data, and (2) Standard merchants are redirected from email to Fin chat.

## **What We Need**

1. **Approve policy for sharing payments data over email using Fin - Q2 (gates Phase 3, Q3).** We need a solution reviewed and approved by InfoSec and the Architecture Review Board. Required for Fin on email with payments data sharing (Phase 3). Without it, the Premium/Enterprise email lever is halved (+9.3 pp not +25.8 pp).
2. **Align on ++[Standard email enforcement plan](https://docs.google.com/document/d/15OHpvfbfWVldFgKrJQB2L4dAJoWliuGKnQU2ZY0bZAc/edit?tab=t.916l0zwg5t1p)++ - Q1.** Standard will not be entitled to emailing us, but 26.6% of their contacts still arrive that way. Redirecting them to Fin chat is a policy and routing change; it requires a Zendesk trigger change (e.g. auto-reply/redirect to Dashboard, similar to Tier 4 email redirect in 2025), not Fin application build.
3. **Agree the involvement target and achievable thresholds - Q1.** Agree the target for involvement and the thresholds we can reach (e.g. ~81% ceiling, 80% target). 18.7% of contacts (internal CKO email + phone/Slack/IM) are permanently unreachable and stay in the denominator.

## **Where We Are Today**

Fin involvement is ~**10-12%** (2,162 / 23,481 contacts; last 6 months). ~19% of contacts are structurally unreachable by Fin - internal CKO email and IM channels - which sets the **hard ceiling at ~81%** for now.

**Merchant segment context** (volume vs. merchant base): support volume is concentrated in the smaller segments.


| Segment    | % of merchants | % of contacts |
| ---------- | -------------- | ------------- |
| Standard   | 75%            | 34.6%         |
| Enterprise | 20%            | 28.6%         |
| Premium    | 5%             | 20.7%         |



|                                                    |                   |                         |
| -------------------------------------------------- | ----------------- | ----------------------- |
| **Channel**                                        | **% of contacts** | **Fin today**           |
| Email (Merchant)                                   | 45.0%             | ✅ 1-2% - just T3        |
| Merchant Webform                                   | 22%               | ❌ 0% - separate channel |
| Dashboard Account unlock form                      | 5%                | ❌ 0% - not yet applied  |
| Other (APAC IM mostly)                             | 9.5%              | ❌ Unreachable           |
| Internal tickets from Checkout (mostly Commercial) | 8-9%              | ❌ Unreachable           |
| Fin (Dashboard chat)                               | ~10%              | ✅ ~100%                 |


## **Strategy: Drive Involvement First, then Resolution**

**Why?** So we can learn more about how to increase resolution rate through greater data capture & problem definition.

- **Involvement rate will rise before resolution rate does.** As Fin reaches email and Webform contacts, the query mix gets harder - email and Webform contacts are more complex than self-selected chat users. Resolution rate will dip. That is expected.
- **The target is 70% resolution rate at 80% involvement** - but that requires filling self-serve feature gaps, content coverage, and data access to be delivered in parallel for Fin. Involvement rate and resolution rate are tracked separately. This plan covers involvement work only.

**Estimated view on how involvement and resolution interact as we scale:**


|                        |                                    |                             |                           |                                                                                  |
| ---------------------- | ---------------------------------- | --------------------------- | ------------------------- | -------------------------------------------------------------------------------- |
| **Involvement rate**   | **Query mix**                      | **Assumed resolution rate** | **Overall AI resolution** | **Depends on**                                                                   |
| 10–15% (today)         | Chat-only                          | 60–70%                      | ~8–11%                    | -                                                                                |
| 25–35%                 | + Standard segment redirect to Fin | 50–60%                      | ~13–21%                   | Policy enforcement                                                               |
| 45–55%                 | + Webform migration                | 45–55%                      | ~20–30%                   | Fin replicating Webform intake                                                   |
| 65–75%                 | + Email (Premium/Enterprise)       | 40–55%                      | ~26–40%                   | Payments data sharing + feature gaps filled                                      |
| 78–82% (no investment) | Full mix                           | 35–45%                      | ~30–45%                   |                                                                                  |
| **78–82% (target)**    | Full mix                           | **70%**                     | **~55–57%**               | More feature gaps filled, content in place, source of truth payments data access |


*Overall AI resolution = involvement rate × resolution rate.*

**What is failure?** (1) Involvement rate cannot exceed 50%, or (2) Fin involvement materially harms merchant experience (e.g. sustained CSAT decline or material escalations from Commercial). In either case we reassess lever rollout and resolution investments before pushing involvement further. If we have to protect support capacity or customer trust, we phase lever rollout rather than compromise quality.

## **The five levers to increase involvement rate**


|                                                                                               |              |                |                   |
| --------------------------------------------------------------------------------------------- | ------------ | -------------- | ----------------- |
| **Lever**                                                                                     | **Contacts** | **% of total** | **Uplift**        |
| **L1 - Fin on Email (Premium/Enterprise)**                                                    | 6,304        | 26.8%          | **+25.8 pp**      |
| **L2 - Standard → Fin (Dashboard)** (enforce success plan: Standard has no email entitlement) | 4,878        | 20.8%          | **+19.9 pp**      |
| **L3 - Webform → Fin chat** (Fin replicates Webform intake + routing)                         | 5,198        | 22.1%          | **+21.2 pp**      |
| **L4 - Account unlock form → Fin**                                                            | 1,159        | 4.9%           | +4.7 pp           |
| **L5 - Maintain Dashboard chat**                                                              | 2,162        | 9.2%           | (9.2 pp baseline) |
| Unreachable (not a lever)                                                                     | 4,391        | 18.7%          | 0                 |
| **Total**                                                                                     | **23,481**   |                | **80.9%**         |


**Sharing payments data is the critical dependency for Lever 1.** ~64% of Premium/Enterprise email volume is Payments In and Payouts queries that require merchant/transaction data. Without data auth, Lever 1 is worth +9.3 pp not +25.8 pp.


|              |                    |                      |                   |
| ------------ | ------------------ | -------------------- | ----------------- |
|              | **Lever 1 uplift** | **Enterprise after** | **Premium after** |
| With data    | +25.8 pp           | 78.8%                | 78.2%             |
| Without data | +9.3 pp            | 42.5%                | 24.9%             |


**Dashboard adoption driver for Lever 1:** Fin email responses will include contextual links to the merchant's Dashboard and relevant self-serve resources - increasing resolution rate and surfacing self-serve to Premium/Enterprise merchants who currently default to email.

## **Phased Plan**


|                                                                          |            |                                                                                                                                                           |                           |
| ------------------------------------------------------------------------ | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| **Phase**                                                                | **Timing** | **What**                                                                                                                                                  | **Owner**                 |
| **1 - Standard enforcement**                                             | Q2 2026    | Stop accepting email from Standard; redirect to Fin chat. Policy + Zendesk trigger change (e.g. Tier 4-style redirect). Fastest lever.                    | Care Operations & Product |
| **2 - Fin on email without payments data sharing & Account unlock form** | Q2 2026    | Launch Fin on email for Premium/Enterprise for non-Payments issues only (no sharing of payments data). + Account unlock form. Gated on auth classifier.   | Product                   |
| **3 - Fin on email with payments data sharing**                          | Q3 2026    | Enable Fin to handle Payments In and Payouts on email. Gated on policy for sharing payments data (InfoSec + ARB) approved and auth solution built.        | Product                   |
| **4 - Webform migration**                                                | Q3 2026    | Care Product owned. Fin chat replaces Webform as primary support entry point; coordinate with Dashboard Engineering for hosted-surface changes as needed. | Care Product              |
| **5 - Gap close**                                                        | Q3 2026    | Assess rate vs target; address residual gaps                                                                                                              | Charlie Wildish           |
| **6 - Target review**                                                    | Q4 2026    | Confirm 80% achieved or adjust                                                                                                                            | Charlie Wildish           |


## **Key Assumptions**

Three assumptions that would materially change the plan if wrong:

1. **Data auth unlocks Lever 1.** Without it, Premium/Enterprise email is worth +9.3 pp not +25.8 pp. If delayed past Q2, the plan needs to be revisited.
2. **Standard redirects successfully.** 26.6% of Standard contacts arrive via email today despite no email entitlement. The Zendesk trigger (e.g. auto-reply/redirect to Dashboard, like Tier 4 in 2025) must capture most of them for Lever 2 to deliver.
3. **Fin replicates Webform end-to-end.** Lever 3 requires Fin to replicate structured intake, ticket field population, and routing. If it can't, a residual Webform population stays outside Fin's reach. (We considered AI answers inside the Webform; Fin doesn't support that. Intercom recommended Fin as primary entry - migration was chosen for that reason.)

Supporting assumptions (tracked quarterly, not plan-breaking unless significantly wrong):

- Channel mix holds at last-6m proportions. If email share grows, the 96% execution bar gets harder; if it falls, easier.
- Dashboard chat baseline stays at ~9.2%. Any organic lift from Webform migration reduces pressure on other levers - upside not in the model.
- The ~81% ceiling is fixed. Any growth in unreachable channels (internal email, phone, Slack/IM) tightens it.

**Owner**: Charlie Wildish  
**Next update**: Q1 2026 - after denominator confirmed and policy for sharing payments data over email (Fin) decided  
**Questions to**: Charlie Wildish  
**Source data**: `support_contacts_flat_table_2025_last_6m.csv` (23,481 contacts, last 6 months)