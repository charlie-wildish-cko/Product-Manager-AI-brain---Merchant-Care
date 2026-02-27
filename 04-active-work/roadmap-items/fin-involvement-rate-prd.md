# Fin Involvement Rate & AI Resolution Rate — 80% Target by End 2026

**Status**: Draft  
**Owner**: Charlie Wildish  
**Last Updated**: February 2026  
**Stakeholders**: Care Operations, Engineering, Zendesk Admins, Content team, Product (Intercom/Fin)

## Executive Summary

**Targets:** **80% Fin involvement rate** and **70% resolution rate at 80% involvement** by end of 2026. Involvement rate = % of contacts where Fin is the first touchpoint; resolution rate = % of Fin-involved contacts that Fin resolves without human escalation. Overall AI resolution of our contacts = involvement × resolution (e.g. 80% × 70% ≈ 56% of all contacts resolved by Fin).

**Strategy:** Drive involvement first to increase throughput and learn what Fin can’t solve, and to boost overall Care resolution; then balance resolution rate (via feature gaps, content, and data access for Fin) so we control that overall AI resolution. The 70% resolution target at 80% involvement depends on filling feature gaps, right content, and data for Fin to access.

**Today:** Fin involvement is **9.2%** (last 6 months, 23,481 contacts). Channels: **Email (Merchant)** (45%) — no Fin; **Webform** (22.1%) — separate channel; **Account unlock form** (4.9%; identified as Other + case_type = ACCOUNT MANAGEMENT & ACCESS + issue_type = Login & Access) — Fin-eligible, Lever 4; **Other** (9.5%) and **Email (Internal)** (9.2%) — unreachable. Reaching 80% requires: (1) Fin on Email (Merchant) for Premium/Enterprise, (2) enforce success plan so Standard use Fin (Dashboard) — [care-success-plans.md](../../01-knowledge-base/products/care-success-plans.md) gives Standard no email entitlement, (3) migrate Webform to Fin chat, (4) apply Fin on **Account unlock form**, (5) maintain Fin chat. Unreachable channels (≈18.7%) cap the ceiling at **≈81%**; eligible levers must reach **≈96% Fin involvement** on average to hit 80%.

## Problem

**What problem are we solving, and who has it?**  
The business target is 80% Fin involvement rate by end of 2026. Today, Fin is only available in the authenticated Dashboard chat experience. Two structural gaps prevent 80% from being reachable:

1. **Email (Merchant)** (45.0% of all contacts): Fin is not deployed on merchant-initiated email. Premium/Enterprise send the majority of their contacts via Email (Merchant); Standard also sends 26.6% via email (not entitled). Fin involvement on Email (Merchant) is 0%.
2. **Email (Internal)** (9.2% of all contacts): Submitted by CKO (internal; `raised_by_cko` tag). Structurally **unreachable by Fin** — not in scope for the involvement rate levers; stays in denominator and counts against the rate.
3. **Webform & API** (22.1% of all contacts): The Dashboard Webform is a separate technical channel — Fin cannot run inside it. These contacts go directly to a human queue. The lever is migrating these contacts to Fin chat instead.

These two gaps mean that even if Fin handled 100% of existing chat contacts, the current maximum involvement rate would be ~9.2% — which is what the last-6m data shows. **Source**: `support_contacts_flat_table_2025_last_6m.csv` (definitions: `support_contacts_flat_table_2025_metric_definitions.md`), 23,481 support contacts (last 6 months).

**How are they solving it today?**  
There is no workaround. Email contacts from Premium and Enterprise go directly to human agents. Webform contacts go directly to the human queue. Merchants who use these channels never encounter Fin.

**Why solve this now?**  

- The 80% involvement rate is a stated 2026 target and a prerequisite for hitting the cost-per-contact and AI resolution rate targets in the Care flywheel model
- Fin email for Premium/Enterprise (the largest single lever) is already in development — this PRD defines what else must happen in parallel to reach 80%
- The target is **70% resolution rate at 80% involvement** — reached by filling feature gaps, right content, and data access for Fin; the content strategy and Fin email data policy are the main enablers

**Strategy: drive involvement first, then balance resolution**  
Increasing Fin involvement rate does two things: (1) **drives more AI adoption**, which increases throughput and gives us more signal on what Fin *can’t* solve — so we learn faster where to invest in content, feature gaps, and data access; (2) **helps boost overall resolution of Care** by making Fin the first touchpoint for more contacts. We then **balance resolution rate** (the % of Fin-involved contacts that Fin resolves) so that we **control overall AI resolution of our contacts** — i.e. involvement × resolution = % of all contacts resolved by Fin. That balance is the 70% resolution-at-80%-involvement target, enabled by feature gaps, content, and data for Fin.

## Volume Model: Path to 80%

**Actuals — channel split and current Fin involvement** (source: `support_contacts_flat_table_2025_last_6m.csv`, last 6 months; definitions: `support_contacts_flat_table_2025_metric_definitions.md`).

*Channel* = how the merchant initiated contact (aligned with [support_contacts_flat_table_2025_metric_definitions.md](../../01-knowledge-base/processes/support_contacts_flat_table_2025_metric_definitions.md)):

- **Email (Merchant)** — Submitted via email by the merchant
- **Email (Internal)** — Submitted via email by CKO (internal; `raised_by_cko` tag). **Unreachable by Fin.**
- **Webform & API** — Submitted via web form or API
- **Fin (Dashboard)** — Started in Fin (Dashboard chat)
- **Account unlock form** — In the flat table: *channel = Other* AND *case_type = ACCOUNT MANAGEMENT & ACCESS* AND *issue_type = Login & Access*. Account unlock web form; **Fin-eligible** (Lever 4).
- **Other** — All other channels not listed above (phone, Slack/IM, AM/TAM, etc.). Excludes Account unlock form. **Unreachable by Fin.**

**Unreachable channel** — A channel through which contacts arrive where Fin cannot be deployed as the first touchpoint, by design or by constraint. These contacts stay in the involvement-rate denominator but cannot be converted to Fin-involved. In this model: **Email (Internal)** (CKO-submitted); **Other** (phone P1s, Dedicated Slack/IM (Premium), AM/TAM-submitted). **Account unlock form** is a separate channel and is Fin-eligible (Lever 4). Contacts on unreachable channels should be tagged `fin_unreachable` in reporting so the structural ceiling is visible.

| Channel | % of all contacts | Fin involvement today | Gap |
| --- | --- | --- | --- |
| Email (Merchant) | **45.0%** | ❌ 0% — not deployed | Deploy Fin on email (Premium/Enterprise) |
| Webform & API | **22.1%** | ❌ 0% — separate channel | Migrate contacts to Fin chat |
| **Account unlock form** | **4.9%** | ❌ 0% — not yet applied | Apply Fin (Lever 4) |
| Other (phone, Slack/IM, AM/TAM, etc.) | **9.5%** | ❌ Unreachable by Fin | — |
| Email (Internal) | **9.2%** | ❌ Unreachable by Fin (CKO-submitted) | — |
| Fin (Dashboard chat) | **9.2%** | ✅ ~100% by definition | Maintain |


**Current involvement rate: 9.2%** (2,162 Fin contacts / 23,481 total).

**By support segment:**


| Segment    | % of total contacts | Current Fin involvement | Email % | Webform % |
| ---------- | ------------------- | ----------------------- | ------- | --------- |
| Standard   | 34.6%               | **16.9%**               | 26.6%   | 33.5%     |
| Enterprise | 28.6%               | **6.2%**                | 54.1%   | 21.6%     |
| Premium    | 20.7%               | **4.0%**                | 54.9%   | 16.2%     |


> **Notable**: Per [care-success-plans.md](../../01-knowledge-base/products/care-success-plans.md) (Channel Entitlements), Standard has **no Dedicated Email** — only AI Agent, Dashboard Webform, and Live Chat. Standard still sends 26.6% of their contacts via email today (out of entitlement). Enforcing the success plan makes Standard a lever to **increase Fin (Dashboard)** volume: those contacts will use Fin in Dashboard instead of email.

**The structural ceiling and what 80% requires:**

**~18.7% of all contacts are unreachable by Fin:** Email (Internal) (9.2%; CKO-submitted) + Other (9.5%; phone P1s, Dedicated Slack/IM, AM/TAM). These stay in the denominator. The maximum theoretical involvement rate is **~81%**. The 80% target is just below this ceiling — reaching it requires the eligible levers (Email (Merchant), Webform, **Account unlock form**, Fin chat) to average **~96% Fin involvement**.

**Path to 80% — scenario model (last 6 months contact volumes, all contacts in denominator):**


| Lever                                                                              | Contacts   | % of total | At 80% Fin | At 90% Fin | At 96% Fin |
| ---------------------------------------------------------------------------------- | ---------- | ---------- | ---------- | ---------- | ---------- |
| Premium/Enterprise Email (Merchant) — Fin deployed                                 | 6,304      | 26.8%      | 5,043      | 5,674      | 6,051      |
| Standard → Fin (Dashboard) (enforce success plan: no email per care-success-plans) | 4,878      | 20.8%      | 3,902      | 4,390      | 4,683      |
| Webform → Fin chat migration                                                       | 5,198      | 22.1%      | 4,158      | 4,678      | 4,990      |
| Account unlock form — Fin applied                                                  | 1,159      | 4.9%       | 927        | 1,043      | 1,113      |
| Fin (Dashboard chat) — maintain                                                    | 2,162      | 9.2%       | 2,162      | 2,162      | 2,162      |
| **Unreachable** (Email (Internal) + Other) | **4,391** | **18.7%** | 0 | 0 | 0 |
| **Total contacts**                                                                 | **23,481** |            | **16,193** | **17,947** | **18,999** |
| **Overall involvement rate**                                                       |            |            | **69.0%**  | **76.4%**  | **80.9%**  |


> **The 80% target requires levers to reach ~96% Fin involvement on average** (because Email (Internal) and Other are unreachable channels, 18.7% of the denominator). With last-6m volumes, at 96% per lever the overall rate reaches **80.9%** (hits 80%). At 80% per lever: 69.0%. At 90%: 76.4%. The Standard lever **increases Fin (Dashboard)** volume: per care-success-plans Standard cannot use email, so enforcing that directs Standard contacts to Fin in Dashboard; it is a policy change and can be executed independently of Fin-on-email.

**Model assumptions:**

1. **Channel mix is static.** The model uses last-6m channel proportions and holds them fixed. In practice, email share could grow (e.g. Enterprise/Premium increase in volume, or more merchants default to email over time), which would increase the absolute contacts that levers 1–2 must convert and could push the required lever execution rate above 96%. Conversely, email share could fall if merchants shift behaviour — the model does not capture either direction. Revisit channel mix assumptions each quarter.

2. **Fin (Dashboard chat) share does not grow organically.** The model treats Fin (Dashboard) as a maintained baseline (9.2%), not a growing one. In practice, Dashboard chat adoption may increase over time — particularly as Webform migration proceeds, as Dashboard UX improvements make chat more prominent, or as merchants become more familiar with Fin. Any organic growth in Fin (Dashboard) share would lift involvement rate ahead of the lever model and reduce the execution pressure on other levers. This is an upside not modelled; track actual Fin (Dashboard) share monthly and update the baseline if it moves.

**Tier distribution (last 6 months actuals)**:


| Segment    | % of contacts |
| ---------- | ------------- |
| Standard   | 34.6%         |
| Enterprise | 28.6%         |
| Premium    | 20.7%         |


## Goals & Success Metrics

### Involvement rate: current vs target


| support_segment | Current (last 6m) | Target  | Notes                                                      |
| --------------- | ----------------- | ------- | ---------------------------------------------------------- |
| Standard        | 16.9%             | 80%+    | Enforce success plan → Fin (Dashboard) + Webform migration |
| Enterprise      | 6.2%              | 78%     | Fin on Email (Merchant) + Webform migration                |
| Premium         | 4.0%              | 75%     | Fin on Email (Merchant) + Webform migration                |
| **Total**       | **9.2%**          | **80%** | End of 2026                                                |


**Levers to reach target**

- **Lever 1** — Fin on Email (Merchant) (Premium/Enterprise): moves Enterprise, Premium.
- **Lever 2** — Standard → Fin (Dashboard) (enforce success plan): moves **Standard** only.
- **Lever 3** — Webform → Fin chat migration: **applies to all segments** (cross-cutting lever).
- **Lever 4** — **Account unlock form** → Fin: the Account unlock form channel (case_type = ACCOUNT MANAGEMENT & ACCESS, issue_type = Login & Access, channel = Other in flat table); all segments; 4.9% of contacts.
- **Lever 5** — Maintain Fin (Dashboard): no new volume; preserves current Fin (Dashboard) share.

**Lever uplift to involvement rate** (at 96% Fin involvement on each lever; denominator = 23,481 total contacts):


| Lever                                   | New Fin contacts | Uplift (pp)    |
| --------------------------------------- | ---------------- | -------------- |
| Lever 1 — Fin on Email (Merchant) (P/E) | +6,051           | +25.8          |
| Lever 2 — Standard → Fin (Dashboard)    | +4,683           | +19.9          |
| Lever 3 — Webform → Fin chat            | +4,990           | +21.2          |
| Lever 4 — Account unlock form           | +1,113           | +4.7           |
| Lever 5 — Maintain                      | (2,162 existing) | (9.2 baseline) |
| **Total after levers**                  | **18,999**       | **80.9%**      |


**Uplift split per segment** (at 96% lever execution; segment rate = Fin contacts / segment contacts):


| support_segment | Current rate | Uplift (pp) | Rate after levers |
| --------------- | ------------ | ----------- | ----------------- |
| Standard        | 16.9%        | +58.0       | **74.9%**         |
| Enterprise      | 6.2%         | +72.6       | **78.8%**         |
| Premium         | 4.0%         | +74.2       | **78.2%**         |


**Fin on email: assumption on data authentication**

*Assumption:* All **PAYMENTS (IN)** and **PAYOUTS** queries need data authentication for Fin to handle them on email (e.g. merchant/transaction context). Of Lever 1 volume (Premium/Enterprise Email Merchant), **~4,035 contacts** (64%) are Payments In + Payouts; **~2,269** are other case types. Without a data-authentication solution, Fin on email can only run on the “other” volume for that lever.

**Lever 1 uplift with vs without data auth** (overall involvement rate):


| Scenario                                                           | Lever 1 new Fin contacts | Lever 1 uplift (pp) |
| ------------------------------------------------------------------ | ------------------------ | ------------------- |
| **With** data auth (Fin can handle Payments In + Payouts on email) | +6,051                   | +25.8               |
| **Without** (Fin on email only for non–Payments In / non–Payouts)  | +2,178                   | +9.3                |
| **Delta from data auth solution**                                  | +3,873                   | **+16.5**           |


**Uplift split per segment: with vs without data auth** (at 96% on other levers; Lever 1 as above):


| support_segment | Current | With data auth: rate after | Without: rate after | Uplift with | Uplift without |
| --------------- | ------- | -------------------------- | ------------------- | ----------- | -------------- |
| Standard        | 16.9%   | 74.9%                      | 74.9%               | +58.0 pp    | +58.0 pp       |
| Enterprise      | 6.2%    | **78.8%**                  | 42.5%               | +72.6 pp    | +36.3 pp       |
| Premium         | 4.0%    | **78.2%**                  | 24.9%               | +74.2 pp    | +20.9 pp       |


Standard is unchanged (no Lever 1). Enterprise and Premium miss ~80% and ~79% targets without data auth; with it they move into the high 70s. Need-auth volume in Lever 1: scale proportionally from last-6m P/E Email (Payments In + Payouts).

> Path-to-80% scenario (contact counts and 96% lever rates) is in the Volume Model section above.


| Metric                                  | Current State              | Target  | Timeline                                                                    |
| --------------------------------------- | -------------------------- | ------- | --------------------------------------------------------------------------- |
| Fin involvement rate (all tiers)        | **9.2%** (last 6m actuals) | **80%** | End of 2026                                                                 |
| AI resolution rate (at 80% involvement) | ~70%                       | **70%** | End of 2026 (conditional on feature gaps, content, data access — see below) |


> **Note**: Involvement rate and resolution rate are distinct. Involvement rate = Fin is the first touchpoint. Resolution rate = Fin resolves without human escalation. Both are tracked; this PRD's primary goal is involvement rate. **Target: 70% resolution rate at 80% involvement** — achievable only if feature gaps are filled, right content is in place, and Fin has the data access it needs (e.g. auth, APIs for Payments In / Payouts).

**Expected relationship: involvement rate ↑ → resolution rate ↓ (query-mix effect) unless we invest**  
As involvement rate increases, Fin sees a broader and harder query mix: chat-heavy volume is self-selected and often simpler; adding Standard redirect, Webform migration, and Email (Merchant) brings in more complex and multi-step issues. Resolution rate will dip as involvement rises **unless** we fill feature gaps, add the right content, and give Fin the data it needs. The **target is 70% resolution rate at 80% involvement**, based on those investments. The matrix below shows how resolution rate could move by stage, and what “70% at 80%” depends on.

**Assumption matrix: resolution rate by involvement rate** (illustrative; update with baselines and as levers launch)

*Overall resolution rate* = involvement rate × assumed resolution rate (i.e. % of *all* contacts that Fin resolves, not just Fin-involved).

| Involvement rate (approx.) | Query mix shift | Assumed resolution rate (Fin-resolved / Fin-involved) | **Overall resolution rate** (% of all contacts resolved by Fin) | Rationale |
| --- | --- | --- | --- | --- |
| 10–15% (today) | Chat-only, some Standard | **60–70%** (base) | **~8–11%** | Self-selected chat users; simpler, often transactional queries. |
| 25–35% | + Standard redirect (email/webform → chat) | **50–60%** (base) | **~13–21%** | New volume from email/webform; more process questions; some dip vs. chat-only. |
| 45–55% | + Webform migration | **45–55%** (base) | **~20–30%** | Webform users often have structured, multi-field issues; mix is harder. |
| 65–75% | + Email (Merchant) (P/E) | **40–55%** (base) | **~26–41%** | Email brings long-form, context-heavy queries; resolution rate lifts as feature gaps and data access (e.g. auth) are filled. |
| 78–82% *(no resolution uplift)* | Full mix, all levers | **35–45%** (base) | **~28–37%** | Same involvement as target, but **no investment** in feature gaps, content, or data access. Full mix with today’s capabilities; resolution rate on involved contacts stays low. |
| **78–82% (target)** | Full mix, all levers | **70% (target)** | **~55–57%** | **Target:** 70% resolution at 80% involvement. Depends on: **feature gaps filled** (e.g. Webform-like intake, routing), **right content** (content strategy), and **data for Fin to access** (auth, APIs for Payments In / Payouts, balance/settlement where applicable). Without these, resolution rate at full mix would sit lower; with them, 70% is the goal. |


*Use for planning:* Treat the “base” column as a mid-case; consider low/high bounds (e.g. ±10 pp) for scenarios. Revisit with real resolution-rate baselines once instrumentation is live and after each major lever. Track feature gaps, content coverage, and data-access readiness alongside resolution rate so “70% at 80%” stays grounded in delivery.

## User Stories

**As a merchant (any tier) who previously used the Dashboard Webform**, I want the Dashboard support entry point to guide me to Fin chat first, so that I get an instant response rather than waiting in a human queue.

**Acceptance Criteria**:

- The Dashboard support entry point presents Fin chat as the primary CTA; the Webform is a secondary or fallback option, not presented at the same level
- Merchants who navigate to the Webform are shown a Fin chat prompt before proceeding to the form
- If Fin cannot resolve, it creates the Zendesk ticket on the merchant's behalf (same outcome as the Webform, but with Fin context attached)
- The Webform remains available as a fallback — this is a migration, not removal

**As an Enterprise or Premium merchant**, I want Fin to respond to my email support queries (where appropriate) before a human agent does, so that I get faster answers outside business hours and for routine questions.

**Acceptance Criteria**:

- Fin is invoked on inbound **Email (Merchant)** tickets from Enterprise and Premium merchants (Email (Internal) / CKO-submitted is out of scope)
- Fin applies exclusion rules (see [fin-email-auth-data-policy-prd.md](fin-email-auth-data-policy-prd.md)) before engaging
- Fin attempts resolution and only creates a human-routed ticket if it cannot resolve
- Involvement rate on email is tracked per tier

**As a Care Operations manager**, I want to see Fin's involvement rate broken down by tier and channel in a single dashboard, so that I can track progress against the 80% target and identify where adoption is lagging.

**Acceptance Criteria**:

- A reportable metric for Fin involvement rate exists, segmented by: tier (Standard / Enterprise / Premium), channel (chat / email / webform / account unlock form / other)
- Baseline involvement rates are established in Q1 2026
- Weekly reporting available from the point of instrumentation

**As a Care Product Manager**, I want to understand which contacts are structurally unreachable by Fin (e.g. Dedicated Slack/IM, phone, AM/TAM submissions), so that I can report the theoretical ceiling alongside the involvement rate and explain why 100% is not achievable.

**Acceptance Criteria**:

- Contacts where Fin cannot be involved (Email (Internal), phone, Dedicated Slack/IM, AM/TAM submissions) are tagged as `fin_unreachable` and visible as a separate category in reporting — they remain in the denominator
- The theoretical ceiling (~81% based on last-6m data — 18.7% unreachable) is documented and surfaced in the involvement rate dashboard so leadership understands the maximum achievable rate

## Requirements

#### Must Have (P0)

- **Involvement rate instrumentation**: Fin involvement rate must be measurable before any lever can be tracked. Define the metric: (Fin-touched contacts) / (total inbound contacts eligible for Fin), segmented by tier and channel. Instrument in Intercom/Zendesk reporting before other levers launch.
- **Standard support model enforcement — increase Fin (Dashboard)**: Per [care-success-plans.md](../../01-knowledge-base/products/care-success-plans.md) (Channel Entitlements), Standard has **no Dedicated Email** — only AI Agent, Dashboard Webform, and Live Chat. Yet 44.8% of Standard’s 2025 contacts arrived via email (6,505 total; 5,261 Email (Merchant) redirectable — 1,244 Email (Internal) is unreachable). Enforcing the success plan — stopping email acceptance for Standard and directing those contacts to Fin (Dashboard) — **increases Fin (Dashboard)** volume and is a policy and routing change. At 96% Fin involvement on redirected contacts, this adds ~4,683 Fin contacts and simplifies the email Fin deployment (Lever 1) by removing Standard from scope.
- **Fin on email (Premium/Enterprise) — Email (Merchant) only**: Deploy Fin as the first responder on inbound Email (Merchant) tickets from Premium and Enterprise. 26.8% of all contacts (6,304). Email (Internal) is not in scope (unreachable by Fin). Authentication and data policy defined in [fin-email-auth-data-policy-prd.md](fin-email-auth-data-policy-prd.md). Standard is excluded from this lever once the support model enforcement (above) is in place.
- **Per-tier involvement rate targets confirmed**: Before Q2, validate the per-tier targets in the volume model above against actual baseline data and confirm the 80% aggregate target is achievable.

#### Should Have (P1)

- **Webform → Fin chat migration (all tiers)**: The Webform & API channel carries 22.1% of all contacts (5,198; last 6m) and has 0% Fin involvement. This lever is within the Care Product team's control — the requirement is that Fin replicates everything the Webform does today: structured intake, correct Zendesk ticket field population, and routing logic. Once Fin can do this end-to-end, the Webform becomes redundant as a primary entry point and Fin chat replaces it. No Dashboard product team dependency.
- **Dashboard chat prominence (all tiers)**: Alongside the Webform migration, ensure Fin chat is the most prominent support entry point in the Dashboard across all tiers. This covers both Webform migration and general chat adoption. Requires Dashboard UX changes — input from Dashboard product team needed to scope the change.
- **Exclusion ceiling documented per tier**: Document what % of contacts are structurally ineligible for Fin per tier (Email (Internal), Premium Dedicated Slack/IM, phone P1s, AM/TAM). This defines the realistic ceiling (~81%) and prevents the 80% target from being misread as 100%.

#### Nice to Have (P2)

- **Fin involvement rate by merchant (not just tier)**: Track involvement rate at the individual merchant level to identify specific accounts where Fin has low or no involvement, enabling targeted nudges or channel configuration changes.
- **Proactive Fin surfacing in Merchant Dashboard**: For common high-volume issue types (e.g. payment status queries, settlement questions), surface a Fin prompt contextually in the Dashboard at the point where the merchant is likely to have a question — before they contact support at all. Reduces inbound volume rather than just involvement rate.

**Constraints**:

- **Channel entitlements are fixed by tier**: Fin deployment must respect the channel entitlements in [care-success-plans.md](../../01-knowledge-base/products/care-success-plans.md). Standard merchants do not have dedicated email; email Fin is Premium/Enterprise only.
- **Data policy**: Fin on email must operate within the approved data policy ([fin-email-auth-data-policy-prd.md](fin-email-auth-data-policy-prd.md)). Data policy sign-off is a hard gate before email involvement can be counted towards the target.
- **Structural ceiling**: ~18.7% of contacts cannot have Fin involvement: Email (Internal) (9.2%; CKO-submitted) + Other channel (phone P1s, Dedicated Slack/IM, AM/TAM, ~9.5%). Account unlock form is a separate channel and a lever (Lever 4), not unreachable. Unreachable contacts remain in the denominator and should be tagged `fin_unreachable` so the ceiling (~81%) is visible in reporting.
- **Resolution rate target (70% at 80% involvement)**: Reaching 70% resolution rate at 80% involvement depends on **filling feature gaps** (e.g. Webform-like intake, routing), **right content** (content strategy), and **data for Fin to access** (auth, APIs for Payments In / Payouts, balance/settlement). The content strategy ([content-strategy-2026.md](../../01-knowledge-base/strategy/content-strategy-2026.md)) and Fin email data policy are parallel dependencies — involvement rate and resolution rate must be tracked together.

## Approach

**The three levers in priority order:**

**Lever 1 — Fin on Email (Merchant) (Premium/Enterprise) [P0]**  
Premium/Enterprise Email (Merchant) only = 26.8% of all contacts (6,304; last 6m); Fin involvement = 0%. Email (Internal) is unreachable by Fin — not in scope. In development — driven by fin-email-auth-data-policy-prd.md. At 96% Fin involvement: +6,051 Fin contacts.

> **Note — Fin on email as a Dashboard and self-serve bridge**: When Fin responds to an email query, responses will include contextual links to the merchant's Dashboard and relevant self-serve resources (e.g. documentation, status pages). This serves two purposes: (1) it increases the likelihood Fin can resolve the query without human escalation by directing merchants to the right tool or information; (2) it surfaces the Dashboard and self-serve channels to Premium/Enterprise merchants who currently default to email, supporting longer-term channel shift. This is a design requirement for the email Fin UX — not just a content add-on.

**Lever 2 — Standard → Fin (Dashboard) (enforce success plan) [P0]**  
Per care-success-plans.md (Channel Entitlements), Standard has no Dedicated Email — only AI Agent, Dashboard Webform, Live Chat. Standard Email (Merchant) + Webform = 20.8% of all contacts (4,878). Enforcing the success plan increases Fin (Dashboard) volume: direct Standard contacts to Fin in Dashboard instead of email. POLICY and ROUTING change — no email for Standard; redirect to Fin (Dashboard). At 96% Fin involvement on redirected contacts: +4,683 additional Fin contacts.

**Lever 3 — Webform → Fin chat migration (all tiers) [P0]**  
Webform & API = 22.1% of all contacts (5,198; last 6m); Fin involvement = 0%. Fin must replicate Webform behaviour (structured intake, ticket fields, routing). At 96% Fin involvement: +4,990 additional Fin contacts.

**Lever 4 — Account unlock form → Fin [P1]**  
**Account unlock form** (channel: in flat table, Other + case_type = ACCOUNT MANAGEMENT & ACCESS + issue_type = Login & Access) = 4.9% of all contacts (1,159). At 96% Fin involvement: +1,113 additional Fin contacts.

**Lever 5 — Maintain Fin chat involvement [P1]**  
Fin (Dashboard chat) = 9.2% of contacts today (2,162); by definition nearly 100% involved.

**Unreachable** (in denominator, not levers): Email (Internal) + Other = 4,391 (18.7%). Ceiling ~81%.

**Measurement framework:**

The involvement rate is measured against **all contacts** — the denominator is the full contact volume with no exclusions.

- **Denominator**: all inbound support contacts (Zendesk tickets + Fin-only resolved)
- **Numerator**: contacts where Fin was involved (channel = Fin (Dashboard), or `fin_involved = true` tag on Zendesk ticket)
- **Structurally unreachable contacts** (~18.7% of total — Email (Internal) 9.2%, plus Other channel: phone P1s, Dedicated Slack/IM, AM/TAM) are included in the denominator and count against the rate. **Account unlock form** is a separate channel and a lever (Lever 4), not unreachable. They set the theoretical ceiling at ~81%. Tag `fin_unreachable` and track separately so leadership can see the hard ceiling alongside the progress metric.

**Key UX decisions:**

- Fin must be positioned as the entry point, not an optional step after a ticket is already created
- For email, Fin responds before a human agent is assigned — not as a post-assignment FAQ bot
- For Webform migration, the approach is to make Fin capable of replicating everything the Webform does today: structured intake, correct Zendesk ticket field population, and routing logic. Once Fin can do this end-to-end, it becomes the functionally equivalent replacement. The Webform may be retained as a fallback for edge cases (e.g. attachment uploads) but should not be the primary entry point. This is within Care Product team control — no Dashboard product team dependency.
- The Webform should remain available as a fallback for merchants who explicitly need it (e.g. attachment uploads, complex forms) — the goal is migration, not removal

**Technical notes:**

- Lever 1 (email): Intercom/Fin configuration + Engineering (identification classifier, Zendesk field tagging) — see [fin-email-auth-data-policy-prd.md](fin-email-auth-data-policy-prd.md)
- Lever 3 (Webform migration): Dashboard product team change to the support entry point UX. Not an Intercom or Zendesk Admin change — requires Dashboard Engineering involvement.
- Involvement rate reporting: requires a shared definition between Intercom and Zendesk. Zendesk tickets created from Fin escalations must be tagged `fin_involved = true`. Webform tickets that bypassed Fin should be tagged separately to track migration progress.

## Out of Scope

- **Resolution rate optimisation** — target is 70% resolution rate at 80% involvement, enabled by feature gaps, content, and data access. This PRD tracks involvement rate; resolution rate is driven by content strategy and data policy, tracked in [content-strategy-2026.md](../../01-knowledge-base/strategy/content-strategy-2026.md).
- **Removing the Dashboard Webform** — this programme migrates contacts from Webform to Fin chat; it does not require removing the Webform entirely. The Webform remains as a fallback channel.
- **Fin integration inside the Webform** — technically not possible; the lever is channel migration, not Webform integration.
- **Email (Internal)** — CKO-submitted email (`raised_by_cko` tag) is structurally unreachable by Fin. In the denominator; not a lever for this programme.
- **AM/TAM-submitted tickets** — tickets submitted by Account Managers or TAMs on behalf of merchants are not merchant-direct contacts. These are excluded from the involvement rate denominator.
- **Phone channel** — P1 phone contacts are excluded from Fin involvement; out of scope for this programme.
- **Dedicated Slack/IM (Premium)** — Premium's Dedicated Slack/IM channel is not a Fin channel. Excluded from denominator.
- **B2C consumer support** — 2027 workstream, separate programme.
- **Sonar (internal AI agent)** — internal staff channel; separate from this programme.
- **Settlement status and balance API** — P2 Fin capability tracked in [fin-email-auth-data-policy-prd.md](fin-email-auth-data-policy-prd.md); improves resolution rate once involvement rate infrastructure is in place.

## Launch Plan

- **Phase 1 — Instrument (Q1 2026)**: Baselines now available from last-6m data (9.2% overall; 23,481 contacts; see Volume Model; source: `support_contacts_flat_table_2025_last_6m.csv` + `support_contacts_flat_table_2025_metric_definitions.md`). Remaining Phase 1 work: build a live reporting dashboard for Fin involvement rate by tier/channel; tag Webform tickets separately to measure migration progress; confirm denominator definition with Care Operations leadership; investigate "Other" channel composition.
- **Phase 2a — Standard support model enforcement (Q1–Q2 2026)**: Stop accepting email from Standard merchants; redirect Email (Merchant) + Webform to Fin chat where applicable (4,878 contacts = 20.8% of total). Policy and routing change — no Fin technical build required. Fastest lever to ship.
- **Phase 2b — Fin on email — Premium/Enterprise (Q2 2026)**: Launch Fin on email for Premium and Enterprise (gated on data policy sign-off and auth classifier). Standard is out of scope for this lever.
- **Phase 3 — Webform migration (Q2–Q3 2026)**: Work with Dashboard product team to make Fin chat the primary support entry point in the Dashboard. Intercept or redirect Webform-intent contacts to Fin chat before they submit a form. Monitor shift in Webform vs. chat contact split.
- **Phase 4 — Gap close (Q3 2026)**: Assess involvement rate against target using Phase 1–3 data. Identify any residual gaps and address (e.g. chat adoption improvements, edge cases in email exclusion rules).
- **Phase 5 — Target review (Q4 2026)**: Confirm 80% achieved or identify remaining structural gaps. Decide whether to adjust the target or add levers if not on track.

**Rollback**: Instrumentation has no rollback risk. Fin on email reverts by disabling Fin on that channel (Fin configuration, not code). Webform migration reverts by restoring the Webform as the primary Dashboard support CTA (Dashboard config change).

## Risks, Dependencies & Open Questions

**Risks**:


| Risk                                                                                   | Likelihood | Impact                                                                            | Mitigation                                                                                                                                                                                      |
| -------------------------------------------------------------------------------------- | ---------- | --------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 80% target requires ~80% Fin involvement on both email AND webform                     | High       | High — neither lever alone is sufficient                                          | Both levers are P0; track separately and jointly against the overall target model                                                                                                               |
| Data policy sign-off delayed — blocks email lever                                      | Medium     | High — Email (Merchant) is 45% of contacts (Email (Internal) 9.2% is unreachable) | Track as hard dependency; escalate if not resolved by end Q1                                                                                                                                    |
| Fin cannot fully replicate Webform behaviour — some fields or routing not reproducible | Low–Medium | Medium — delays migration lever or leaves a residual Webform population           | Audit Webform fields and routing logic early; treat gaps as Fin configuration work items                                                                                                        |
| Account unlock form vs Other — reporting split                                          | Confirmed  | Low — now defined as channel (Other + case_type = AMA + issue_type = Login & Access) | Account unlock form is Lever 4 (4.9%); Other is unreachable (9.5%). Instrument reporting so both appear as distinct channels. |
| Standard email volume (26.6%) is higher than channel entitlements suggest              | Low        | Medium — Standard not entitled to email; routing may need fixing                  | Consider whether Standard email should be redirected to chat or webform as a contact-reduction measure                                                                                          |
| Fin resolution rate doesn't improve alongside involvement rate                         | Medium     | Medium — high involvement + low resolution = poor experience                      | Content strategy and involvement rate tracked in parallel                                                                                                                                       |


**Dependencies**:


| Dependency                                                                   | Owner                              | Status                                                                                      | Risk if Delayed                                                                                           |
| ---------------------------------------------------------------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| Fin on email data policy approval (Security + Legal)                         | Security / Legal & Compliance      | Not started                                                                                 | Blocks email lever — biggest single dependency                                                            |
| Fin email auth classifier (Salesforce + domain mapping)                      | Engineering                        | In flight                                                                                   | Blocks email lever; partial mitigations available (domain mapping alone)                                  |
| Zendesk org domain mapping                                                   | Engineering                        | In development (see [zendesk-org-domain-mapping-prd.md](zendesk-org-domain-mapping-prd.md)) | Blocks email identification layer                                                                         |
| Involvement rate instrumentation                                             | Engineering + Zendesk Admins       | Not started                                                                                 | Blocks all measurement; must be Phase 1                                                                   |
| Fin replicates Webform behaviour (structured intake, ticket fields, routing) | Zendesk Admins / Fin configuration | Not started                                                                                 | Blocks Webform migration lever — 22.1% of contacts; within Care Product team control                      |
| Content strategy + data access (70% resolution at 80% involvement)           | Content team / Engineering         | In progress                                                                                 | Feature gaps, right content, and data for Fin to access; without these, high involvement = low resolution |


**Open questions**:

- What is Fin's current involvement rate on Dashboard chat today? *(Answered: 9.2% overall — see `support_contacts_flat_table_2025_last_6m.csv` + `support_contacts_flat_table_2025_metric_definitions.md`)*
- What is the exact channel split by tier? *(Answered: Email (Merchant) 45.0%, Webform & API 22.1%, Account unlock form 4.9%, Other 9.5%, Email (Internal) 9.2%, Fin (Dashboard) 9.2% — see Volume Model. Account unlock form = Other + case_type = ACCOUNT MANAGEMENT & ACCESS + issue_type = Login & Access.)*
- What makes up the Other channel (9.5%)? *(Answered: Other is now defined to exclude Account unlock form. Remaining Other is likely phone/Slack/IM/AM/TAM — confirm with Care Operations; all unreachable.)*
- What % of Premium contacts arrive via Dedicated Slack/IM specifically? *(Owner: Care Operations — "Other" share of Premium; understanding how much is Slack/IM vs. phone vs. other sets the Premium ceiling)*
- Is the denominator definition (all contacts, no exclusions) agreed with Care Operations leadership? *(Owner: Charlie Wildish — the ~18.7% unreachable (Email (Internal) + Other channel) stay in the denominator; leadership needs to understand the theoretical ceiling of ~81% before the 80% target is locked)*
- What fields does the Webform currently populate on Zendesk tickets, and what routing logic does it apply? *(Owner: Zendesk Admins — this is the specification Fin must replicate before Webform migration can proceed)*
- Should the Webform be fully deprecated once Fin replicates its behaviour, or retained as a permanent fallback for edge cases (e.g. attachment uploads)? *(Owner: Care Operations — affects whether any Webform contacts remain outside Fin's reach long-term)*

## Timeline


| Milestone                                   | Date       | Owner                        | Status |
| ------------------------------------------- | ---------- | ---------------------------- | ------ |
| PRD complete                                | Feb 2026   | Charlie Wildish              | Draft  |
| Baseline involvement rate instrumented      | Q1 2026    | Engineering + Zendesk Admins | ⏳      |
| Per-tier targets confirmed vs. actuals      | Q1 2026    | Charlie Wildish              | ⏳      |
| Fin on email — data policy approved         | Q1 2026    | Security / Legal             | ⏳      |
| Fin on email — live (Premium/Enterprise)    | Q2 2026    | Engineering / Zendesk Admins | ⏳      |
| Fin on Dashboard Webform — live             | Q2–Q3 2026 | Engineering                  | ⏳      |
| Dashboard chat adoption improvements — live | Q3 2026    | Zendesk Admins               | ⏳      |
| 80% involvement rate achieved               | Q4 2026    | Charlie Wildish              | ⏳      |


## Appendix

- [support_contacts_flat_table_2025_last_6m.csv](../../01-knowledge-base/processes/support_contacts_flat_table_2025_last_6m.csv) — Support contacts flat table, last 6 months (source for volume model)
- [support_contacts_flat_table_2025_metric_definitions.md](../../01-knowledge-base/processes/support_contacts_flat_table_2025_metric_definitions.md) — Definitions for count metrics, dimensions, and derived metrics (zendesk_tickets, fin_only_resolved, support_contacts, channel, etc.)
- [fin-email-auth-data-policy-prd.md](fin-email-auth-data-policy-prd.md) — Fin on email: authentication, data policy, exclusion rules
- [zendesk-org-domain-mapping-prd.md](zendesk-org-domain-mapping-prd.md) — Org identification / domain mapping (email auth dependency)
- [care-success-plans.md](../../01-knowledge-base/products/care-success-plans.md) — Channel entitlements by tier (defines which channels Fin can operate on per tier)
- [content-strategy-2026.md](../../01-knowledge-base/strategy/content-strategy-2026.md) — Content team roadmap; resolution rate target 70% at 80% involvement (feature gaps, content, data access)
- [ai-agent-operations.md](../../01-knowledge-base/processes/ai-agent-operations.md) — Fin operations, escalation patterns, current constraints

