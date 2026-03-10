# Fin Involvement Rate & AI Resolution Rate - 80% Target by End 2026

**Status**: Draft  
**Owner**: Charlie Wildish  
**Last Updated**: February 2026  
**Stakeholders**: Care Operations (own 80% target), Engineering (email + webform migration + instrumentation), Zendesk Admins (tagging, routing, reporting), Content team (resolution-rate content), Product (Intercom/Fin) (Fin behaviour and UX).

## Executive Summary

**Targets:** **80% Fin involvement rate** and **70% resolution rate at 80% involvement** by end of 2026. Overall AI resolution = involvement × resolution (e.g. 80% × 70% ≈ 56% of contacts).

**Strategy:** Drive involvement first to increase throughput and learn what Fin can’t solve, and to boost overall Care resolution; then balance resolution rate (via feature gaps, content, and data access for Fin) so we control that overall AI resolution. 70% at 80% depends on feature gaps, content, and data access.

**One sentence for support:** “We’re making Fin the first touchpoint for most contacts so more queries are resolved by AI; your job is to handle what Fin can’t resolve and set merchant expectations on channel (e.g. Standard → Dashboard, Premium/Enterprise → Fin may reply first to email).”

**Today:** 9.2% involvement (23,481 contacts, last 6m). **Levers to 80%:** (1) Fin on Email (Premium/Enterprise), (2) enforce success plan → Standard to Fin (Dashboard), (3) Webform → Fin chat, (4) Account unlock form → Fin, (5) maintain Fin chat. Unreachable (Email Internal 9.2%, Other 9.5%) = 18.7% → ceiling ~81%; levers need ~96% Fin involvement on average.

> **Executive takeaway (the one thing we want everyone to remember):** By end 2026, Fin is the first touchpoint for 80% of contacts; we pair that with resolution investments (content, data access, feature gaps) so support and merchants see a better experience, not just higher volume. If we have to protect support capacity or customer trust, we phase lever rollout rather than compromise quality.

**Ask / Decisions:** Policy for sharing payments data over email using Fin reviewed and approved by InfoSec and Architecture Review Board by Q2 (gates Phase 3 - Fin on email with payments data in Q3); agree involvement target and achievable thresholds with Care Ops (and leadership); Content/Eng for resolution instrumentation; CPO call on Webform vs email sequencing/resourcing. “70% at 80% involvement.”

## Problem

**Metric definitions (context)**

- **Fin involvement rate** — (Contacts where Fin was the first touchpoint) / (Total support contacts). Denominator = all support contacts (Zendesk tickets + Fin-only resolved); unreachable channels (Email Internal, Other) stay in the denominator. Numerator = contacts where Fin participated (e.g. channel = Fin (Dashboard), or Zendesk tickets with `fin_involved = true` once Fin on email is live). Source: [support_contacts_flat_table_2025_metric_definitions.md](../../01-knowledge-base/metrics/support_contacts_flat_table_2025_metric_definitions.md).
- **AI resolution rate** — Of contacts where Fin was involved, the share that Fin resolved without human escalation. (Fin-resolved contacts / Fin-involved contacts). Measured only on the Fin-involved subset.
- **Overall AI resolution** — Share of *all* support contacts that Fin resolved. = Involvement rate × AI resolution rate (e.g. 80% × 70% ≈ 56% of all contacts).

**What problem are we solving, and who has it?**  
We are reducing Checkout’s cost of support and providing a faster support experience to merchants. 80% involvement = Fin as first touchpoint for most contacts; with 70% resolution at 80% that drives overall AI resolution (lower cost-per-contact, better experience). Today Fin is Dashboard chat only. **Gaps:**

1. **Email (Merchant)** (45%): Fin not on email; Premium/Enterprise use it most; Standard 26.6% via email (not entitled). 0% Fin.
2. **Email (Internal)** (9.2%): CKO-submitted; **unreachable** - in denominator only.
3. **Webform & API** (22.1%): Separate channel; Fin can’t run in it. Lever = migrate to Fin chat.

Even 100% of chat would only give ~9.2% involvement (last-6m actual). **Source:** `support_contacts_flat_table_2025_last_6m.csv`, definitions in `support_contacts_flat_table_2025_metric_definitions.md`.

**How are they solving it today?**  
No workaround. Email and Webform go to humans; those merchants never see Fin.

**Why solve this now?**  
80% is a 2026 target and unblocks Care flywheel. Fin on email (Premium/Enterprise) is in development; this PRD defines the rest. 70% resolution at 80% depends on feature gaps, content, and data (content strategy + policy for sharing payments data over email using Fin).

**Strategy:** Drive involvement first (throughput + signal on what Fin can’t solve), then balance resolution so involvement × resolution = % of contacts resolved by Fin. Target: 70% resolution at 80% involvement.

## Volume Model: Path to 80%

**Actuals - channel split and current Fin involvement** (source: `support_contacts_flat_table_2025_last_6m.csv`, last 6 months; definitions: `support_contacts_flat_table_2025_metric_definitions.md`).

*Channel* = how the merchant initiated contact (aligned with [support_contacts_flat_table_2025_metric_definitions.md](../../01-knowledge-base/metrics/support_contacts_flat_table_2025_metric_definitions.md)):

- **Email (Merchant)** - Submitted via email by the merchant
- **Email (Internal)** - Submitted via email by CKO (internal; `raised_by_cko` tag). **Unreachable by Fin.**
- **Webform & API** - Submitted via web form or API
- **Fin (Dashboard)** - Started in Fin (Dashboard chat)
- **Account unlock form** - In the flat table: *channel = Other* AND *case_type = ACCOUNT MANAGEMENT & ACCESS* AND *issue_type = Login & Access*. Account unlock web form; **Fin-eligible** (Lever 4).
- **Other** - All other channels not listed above (phone, Slack/IM, AM/TAM, etc.). Excludes Account unlock form. **Unreachable by Fin.**

**Unreachable channel** - A channel through which contacts arrive where Fin cannot be deployed as the first touchpoint, by design or by constraint. These contacts stay in the involvement-rate denominator but cannot be converted to Fin-involved. In this model: **Email (Internal)** (CKO-submitted); **Other** (phone P1s, Dedicated Slack/IM (Premium), AM/TAM-submitted). **Account unlock form** is a separate channel and is Fin-eligible (Lever 4). Contacts on unreachable channels should be tagged `fin_unreachable` in reporting so the structural ceiling is visible.

| Channel | % of all contacts | Fin involvement today | Gap |
| --- | --- | --- | --- |
| Email (Merchant) | **45.0%** | ❌ 0% - not deployed | Deploy Fin on email (Premium/Enterprise) |
| Webform & API | **22.1%** | ❌ 0% - separate channel | Migrate contacts to Fin chat |
| **Account unlock form** | **4.9%** | ❌ 0% - not yet applied | Apply Fin (Lever 4) |
| Other (phone, Slack/IM, AM/TAM, etc.) | **9.5%** | ❌ Unreachable by Fin | - |
| Email (Internal) | **9.2%** | ❌ Unreachable by Fin (CKO-submitted) | - |
| Fin (Dashboard chat) | **9.2%** | ✅ ~100% by definition | Maintain |


**Current involvement rate: 9.2%** (2,162 Fin contacts / 23,481 total).

**By Merchant segment:**


| Segment    | % of total contacts | % of merchants | Current Fin involvement | Email % | Webform % |
| ---------- | ------------------- | -------------- | ----------------------- | ------- | --------- |
| Standard   | 34.6%               | 75%            | **16.9%**               | 26.6%   | 33.5%     |
| Enterprise | 28.6%               | 20%            | **6.2%**                | 54.1%   | 21.6%     |
| Premium    | 20.7%               | 5%             | **4.0%**                | 54.9%   | 16.2%     |


> **Notable**: Per [care-success-plans.md](../../01-knowledge-base/products/care-success-plans.md) (Channel Entitlements), Standard has **no Dedicated Email** - only AI Agent, Dashboard Webform, and Live Chat. Standard still sends 26.6% of their contacts via email today (out of entitlement). Enforcing the success plan makes Standard a lever to **increase Fin (Dashboard)** volume: those contacts will use Fin in Dashboard instead of email.

**The structural ceiling and what 80% requires:**

**~18.7% of all contacts are unreachable by Fin:** Email (Internal) (9.2%; CKO-submitted) + Other (9.5%; phone P1s, Dedicated Slack/IM, AM/TAM). These stay in the denominator. The maximum theoretical involvement rate is **~81%**. The 80% target is just below this ceiling - reaching it requires the eligible levers (Email (Merchant), Webform, **Account unlock form**, Fin chat) to average **~96% Fin involvement**.

**Path to 80% - scenario model (last 6 months contact volumes, all contacts in denominator):**


| Lever                                                                              | Contacts   | % of total | At 80% Fin | At 90% Fin | At 96% Fin |
| ---------------------------------------------------------------------------------- | ---------- | ---------- | ---------- | ---------- | ---------- |
| Premium/Enterprise Email (Merchant) - Fin deployed                                 | 6,304      | 26.8%      | 5,043      | 5,674      | 6,051      |
| Standard → Fin (Dashboard) (enforce success plan: no email per care-success-plans) | 4,878      | 20.8%      | 3,902      | 4,390      | 4,683      |
| Webform → Fin chat migration                                                       | 5,198      | 22.1%      | 4,158      | 4,678      | 4,990      |
| Account unlock form - Fin applied                                                  | 1,159      | 4.9%       | 927        | 1,043      | 1,113      |
| Fin (Dashboard chat) - maintain                                                    | 2,162      | 9.2%       | 2,162      | 2,162      | 2,162      |
| **Unreachable** (Email (Internal) + Other) | **4,391** | **18.7%** | 0 | 0 | 0 |
| **Total contacts**                                                                 | **23,481** |            | **16,193** | **17,947** | **18,999** |
| **Overall involvement rate**                                                       |            |            | **69.0%**  | **76.4%**  | **80.9%**  |


> **The 80% target requires levers to reach ~96% Fin involvement on average** (because Email (Internal) and Other are unreachable channels, 18.7% of the denominator). With last-6m volumes, at 96% per lever the overall rate reaches **80.9%** (hits 80%). At 80% per lever: 69.0%. At 90%: 76.4%. The Standard lever **increases Fin (Dashboard)** volume: per care-success-plans Standard cannot use email, so enforcing that directs Standard contacts to Fin in Dashboard; it is a policy change and can be executed independently of Fin-on-email.

**Model assumptions:**

1. **Channel mix is static.** The model uses last-6m channel proportions and holds them fixed. In practice, email share could grow (e.g. Enterprise/Premium increase in volume, or more merchants default to email over time), which would increase the absolute contacts that levers 1–2 must convert and could push the required lever execution rate above 96%. Conversely, email share could fall if merchants shift behaviour - the model does not capture either direction. Revisit channel mix assumptions each quarter.

2. **Fin (Dashboard chat) share does not grow organically.** The model treats Fin (Dashboard) as a maintained baseline (9.2%), not a growing one. In practice, Dashboard chat adoption may increase over time - particularly as Webform migration proceeds, as Dashboard UX improvements make chat more prominent, or as merchants become more familiar with Fin. Any organic growth in Fin (Dashboard) share would lift involvement rate ahead of the lever model and reduce the execution pressure on other levers. This is an upside not modelled; track actual Fin (Dashboard) share monthly and update the baseline if it moves.

**Merchant segment distribution (last 6 months actuals)**:


| Segment    | % of contacts | % of merchants |
| ---------- | ------------- | -------------- |
| Standard   | 34.6%         | 75%            |
| Enterprise | 28.6%         | 20%            |
| Premium    | 20.7%         | 5%             |


## Goals & Success Metrics

### Involvement rate: current vs target


| merchant_segment | Current (last 6m) | Target  | Notes                                                      |
| ----------------- | ----------------- | ------- | ---------------------------------------------------------- |
| Standard        | 16.9%             | 80%+    | Enforce success plan → Fin (Dashboard) + Webform migration |
| Enterprise      | 6.2%              | 78%     | Fin on Email (Merchant) + Webform migration                |
| Premium         | 4.0%              | 75%     | Fin on Email (Merchant) + Webform migration                |
| **Total**       | **9.2%**          | **80%** | End of 2026                                                |


**Levers to reach target**

- **Lever 1** - Fin on Email (Merchant) (Premium/Enterprise): moves Enterprise, Premium.
- **Lever 2** - Standard → Fin (Dashboard) (enforce success plan): moves **Standard** only.
- **Lever 3** - Webform → Fin chat migration: **applies to all Merchant segments** (cross-cutting lever).
- **Lever 4** - **Account unlock form** → Fin: the Account unlock form channel (case_type = ACCOUNT MANAGEMENT & ACCESS, issue_type = Login & Access, channel = Other in flat table); all Merchant segments; 4.9% of contacts.
- **Lever 5** - Maintain Fin (Dashboard): no new volume; preserves current Fin (Dashboard) share.

**Lever uplift to involvement rate** (at 96% Fin involvement on each lever; denominator = 23,481 total contacts):


| Lever                                   | New Fin contacts | Uplift (pp)    |
| --------------------------------------- | ---------------- | -------------- |
| Lever 1 - Fin on Email (Merchant) (Premium/Enterprise) | +6,051           | +25.8          |
| Lever 2 - Standard → Fin (Dashboard)    | +4,683           | +19.9          |
| Lever 3 - Webform → Fin chat            | +4,990           | +21.2          |
| Lever 4 - Account unlock form           | +1,113           | +4.7           |
| Lever 5 - Maintain                      | (2,162 existing) | (9.2 baseline) |
| **Total after levers**                  | **18,999**       | **80.9%**      |


**Uplift split per Merchant segment** (at 96% lever execution; Merchant segment rate = Fin contacts / Merchant segment contacts):


| merchant_segment | Current rate | Uplift (pp) | Rate after levers |
| ----------------- | ------------ | ----------- | ----------------- |
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


**Uplift split per Merchant segment: with vs without data auth** (at 96% on other levers; Lever 1 as above):


| merchant_segment | Current | With data auth: rate after | Without: rate after | Uplift with | Uplift without |
| ----------------- | ------- | -------------------------- | ------------------- | ----------- | -------------- |
| Standard        | 16.9%   | 74.9%                      | 74.9%               | +58.0 pp    | +58.0 pp       |
| Enterprise      | 6.2%    | **78.8%**                  | 42.5%               | +72.6 pp    | +36.3 pp       |
| Premium         | 4.0%    | **78.2%**                  | 24.9%               | +74.2 pp    | +20.9 pp       |


Standard is unchanged (no Lever 1). Enterprise and Premium miss ~80% and ~79% targets without data auth; with it they move into the high 70s. Need-auth volume in Lever 1: scale proportionally from last-6m Premium/Enterprise Email (Payments In + Payouts).

> Path-to-80% scenario (contact counts and 96% lever rates) is in the Volume Model section above.


| Metric                                  | Current State              | Target  | Timeline                                                                    |
| --------------------------------------- | -------------------------- | ------- | --------------------------------------------------------------------------- |
| Fin involvement rate (all Merchant segments)        | **9.2%** (last 6m actuals) | **80%** | End of 2026                                                                 |
| AI resolution rate (at 80% involvement) | ~70%                       | **70%** | End of 2026 (conditional on feature gaps, content, data access - see below) |


> **Note**: Involvement rate and resolution rate are distinct. Involvement rate = Fin is the first touchpoint. Resolution rate = Fin resolves without human escalation. Both are tracked; this PRD's primary goal is involvement rate. **Target: 70% resolution rate at 80% involvement** - achievable only if feature gaps are filled, right content is in place, and Fin has the data access it needs (e.g. auth, APIs for Payments In / Payouts).

**Failure definition:** We would consider this programme a failure if: (1) involvement rate cannot exceed 50%, or (2) Fin involvement materially harms merchant experience (e.g. sustained CSAT decline or material escalations from Commercial). In either case we would reassess lever rollout and resolution investments before pushing involvement further.

**Expected relationship: involvement rate ↑ → resolution rate ↓ (query-mix effect) unless we invest**  
As involvement rate increases, Fin sees a broader and harder query mix: chat-heavy volume is self-selected and often simpler; adding Standard redirect, Webform migration, and Email (Merchant) brings in more complex and multi-step issues. Resolution rate will dip as involvement rises **unless** we fill feature gaps, add the right content, and give Fin the data it needs. The **target is 70% resolution rate at 80% involvement**, based on those investments. The matrix below shows how resolution rate could move by stage, and what “70% at 80%” depends on.

**Assumption matrix: resolution rate by involvement rate** (illustrative; update with baselines and as levers launch)

*Overall resolution rate* = involvement rate × assumed resolution rate (i.e. % of *all* contacts that Fin resolves, not just Fin-involved).

| Involvement rate (approx.) | Query mix shift | Assumed resolution rate (Fin-resolved / Fin-involved) | **Overall resolution rate** (% of all contacts resolved by Fin) | Rationale |
| --- | --- | --- | --- | --- |
| 10–15% (today) | Chat-only, some Standard | **60–70%** (base) | **~8–11%** | Self-selected chat users; simpler, often transactional queries. |
| 25–35% | + Standard redirect (email/webform → chat) | **50–60%** (base) | **~13–21%** | New volume from email/webform; more process questions; some dip vs. chat-only. |
| 45–55% | + Webform migration | **45–55%** (base) | **~20–30%** | Webform users often have structured, multi-field issues; mix is harder. |
| 65–75% | + Email (Merchant) (Premium/Enterprise) | **40–55%** (base) | **~26–41%** | Email brings long-form, context-heavy queries; resolution rate lifts as feature gaps and data access (e.g. auth) are filled. |
| 78–82% *(no resolution uplift)* | Full mix, all levers | **35–45%** (base) | **~28–37%** | Same involvement as target, but **no investment** in feature gaps, content, or data access. Full mix with today’s capabilities; resolution rate on involved contacts stays low. |
| **78–82% (target)** | Full mix, all levers | **70% (target)** | **~55–57%** | **Target:** 70% resolution at 80% involvement. Depends on: **feature gaps filled** (e.g. Webform-like intake, routing), **right content** (content strategy), and **data for Fin to access** (auth, APIs for Payments In / Payouts, balance/settlement where applicable). Without these, resolution rate at full mix would sit lower; with them, 70% is the goal. |


*Use for planning:* Treat the “base” column as a mid-case; consider low/high bounds (e.g. ±10 pp) for scenarios. Revisit with real resolution-rate baselines once instrumentation is live and after each major lever. Track feature gaps, content coverage, and data-access readiness alongside resolution rate so “70% at 80%” stays grounded in delivery.

## User Stories

**As a merchant (any Merchant segment) who previously used the Dashboard Webform**, I want the Dashboard support entry point to guide me to Fin chat first, so that I get an instant response rather than waiting in a human queue.

**Acceptance Criteria**:

- The Dashboard support entry point presents Fin chat as the primary CTA; the Webform is a secondary or fallback option, not presented at the same level
- Merchants who navigate to the Webform are shown a Fin chat prompt before proceeding to the form
- If Fin cannot resolve, it creates the Zendesk ticket on the merchant's behalf (same outcome as the Webform, but with Fin context attached)
- The Webform remains available as a fallback - this is a migration, not removal

**As an Enterprise or Premium merchant**, I want Fin to respond to my email support queries (where appropriate) before a human agent does, so that I get faster answers outside business hours and for routine questions.

**Acceptance Criteria**:

- Fin is invoked on inbound **Email (Merchant)** tickets from Enterprise and Premium merchants (Email (Internal) / CKO-submitted is out of scope)
- Fin applies exclusion rules (see [fin-email-auth-data-policy-prd.md](fin-email-auth-data-policy-prd.md)) before engaging
- Fin attempts resolution and only creates a human-routed ticket if it cannot resolve
- Involvement rate on email is tracked per Merchant segment

**As a Care Operations manager**, I want to see Fin's involvement rate broken down by Merchant segment and channel in a single dashboard, so that I can track progress against the 80% target and identify where adoption is lagging.

**Acceptance Criteria**:

- A reportable metric for Fin involvement rate exists, segmented by: Merchant segment (Standard / Enterprise / Premium), channel (chat / email / webform / account unlock form / other)
- Baseline involvement rates are established in Q1 2026
- Weekly reporting available from the point of instrumentation

**As a Care Product Manager**, I want to understand which contacts are structurally unreachable by Fin (e.g. Dedicated Slack/IM, phone, AM/TAM submissions), so that I can report the theoretical ceiling alongside the involvement rate and explain why 100% is not achievable.

**Acceptance Criteria**:

- Contacts where Fin cannot be involved (Email (Internal), phone, Dedicated Slack/IM, AM/TAM submissions) are tagged as `fin_unreachable` and visible as a separate category in reporting - they remain in the denominator
- The theoretical ceiling (~81% based on last-6m data - 18.7% unreachable) is documented and surfaced in the involvement rate dashboard so leadership understands the maximum achievable rate

### Support-facing summary: what agents need to know

- **One sentence for merchants:** “Fin will often be the first to respond (in Dashboard or, for Premium/Enterprise, by email); if Fin can’t fix it, a human will take over with full context.”
- **How tickets will change:** More tickets will be tagged `fin_involved`; new tag `fin_unreachable` for contacts we don’t route to Fin. After Webform migration, some tickets will be created by Fin on the merchant’s behalf (same fields as Webform). Escalation path is unchanged; ticket will contain Fin context.
- **Likely merchant questions and suggested answers:**
  - *“Why did I get a link to Dashboard instead of email?”* - “Standard support is delivered via the Dashboard so you get a faster response from our AI agent, Fin.”
  - *“Who replied to my email?”* - “For Premium/Enterprise, Fin may reply first. If Fin couldn’t resolve it, a human agent has taken over with full context.”
  - *“Where’s the support form?”* - “We’ve moved to Fin chat as the main way to get help; you’ll get an instant response. The form is still available if you need to attach files.”
- **Where to find updates:** Playbooks and runbooks will be updated before each phase (Standard redirect, Fin on email, Webform migration); Care Operations will brief agents before go-live.

## Requirements

#### Must Have (P0)

- **Involvement rate instrumentation**: Fin involvement rate must be measurable before any lever can be tracked. Define the metric: (Fin-touched contacts) / (total inbound contacts eligible for Fin), segmented by Merchant segment and channel. Instrument in Intercom/Zendesk reporting before other levers launch.
- **Standard support model enforcement - increase Fin (Dashboard)**: Per [care-success-plans.md](../../01-knowledge-base/products/care-success-plans.md) (Channel Entitlements), Standard has **no Dedicated Email** - only AI Agent, Dashboard Webform, and Live Chat. Yet 44.8% of Standard’s 2025 contacts arrived via email (6,505 total; 5,261 Email (Merchant) redirectable - 1,244 Email (Internal) is unreachable). Enforcing the success plan - stopping email acceptance for Standard and directing those contacts to Fin (Dashboard) - **increases Fin (Dashboard)** volume. It is a policy and routing change and requires a Zendesk trigger change (e.g. auto-reply/redirect to Dashboard, similar to the Tier 4 email redirect in 2025), not Fin application build. At 96% Fin involvement on redirected contacts, this adds ~4,683 Fin contacts and simplifies the email Fin deployment (Lever 1) by removing Standard from scope.
- **Fin on email (Premium/Enterprise) - Email (Merchant) only**: Deploy Fin as the first responder on inbound Email (Merchant) tickets from Premium and Enterprise. 26.8% of all contacts (6,304). Email (Internal) is not in scope (unreachable by Fin). Authentication and policy for sharing payments data over email using Fin defined in [fin-email-auth-data-policy-prd.md](fin-email-auth-data-policy-prd.md). Standard is excluded from this lever once the support model enforcement (above) is in place.
- **Per-Merchant-segment involvement rate targets confirmed**: Before Q2, validate the per-Merchant-segment targets in the volume model above against actual baseline data and confirm the 80% aggregate target is achievable.

**Definition of done / Ready for dev**: Involvement rate instrumented and reported by Merchant segment/channel; policy for sharing payments data over email using Fin reviewed and approved by InfoSec and Architecture Review Board; per-Merchant-segment targets confirmed vs. actuals.

#### Should Have (P1)

- **Webform → Fin chat migration**: 22.1% of contacts (5,198); 0% Fin today. Fin must replicate Webform: structured intake, ticket fields, routing. Then Fin chat replaces Webform as primary entry. **DoD:** Webform spec signed off by Zendesk Admins; runbook for Fin-created tickets; agents briefed before go-live.
- **Dashboard chat prominence (all Merchant segments)**: Alongside the Webform migration, ensure Fin chat is the most prominent support entry point in the Dashboard across all Merchant segments. This covers both Webform migration and general chat adoption. Webform migration is Care Product owned; Dashboard UX changes (support entry point) scoped with Dashboard Engineering as needed.
- **Exclusion ceiling documented per Merchant segment**: Document what % of contacts are structurally ineligible for Fin per Merchant segment (Email (Internal), Premium Dedicated Slack/IM, phone P1s, AM/TAM). This defines the realistic ceiling (~81%) and prevents the 80% target from being misread as 100%.

#### Nice to Have (P2)

- **Fin involvement rate by merchant (not just Merchant segment)**: Track involvement rate at the individual merchant level to identify specific accounts where Fin has low or no involvement, enabling targeted nudges or channel configuration changes.
- **Proactive Fin surfacing in Merchant Dashboard**: For common high-volume issue types (e.g. payment status queries, settlement questions), surface a Fin prompt contextually in the Dashboard at the point where the merchant is likely to have a question - before they contact support at all. Reduces inbound volume rather than just involvement rate.

**Constraints**:

- **Channel entitlements are fixed by Merchant segment**: Fin deployment must respect the channel entitlements in [care-success-plans.md](../../01-knowledge-base/products/care-success-plans.md). Standard merchants do not have dedicated email; email Fin is Premium/Enterprise only.
- **Sharing payments data over email using Fin**: When Fin handles Payments In or Payouts on email (Phase 3), it must operate within the approved policy for sharing payments data over email using Fin ([fin-email-auth-data-policy-prd.md](fin-email-auth-data-policy-prd.md)). Review and approval by InfoSec and Architecture Review Board is a hard gate before Phase 3 (Fin on email with payments data sharing) goes live.
- **Structural ceiling**: ~18.7% of contacts cannot have Fin involvement: Email (Internal) (9.2%; CKO-submitted) + Other channel (phone P1s, Dedicated Slack/IM, AM/TAM, ~9.5%). Account unlock form is a separate channel and a lever (Lever 4), not unreachable. Unreachable contacts remain in the denominator and should be tagged `fin_unreachable` so the ceiling (~81%) is visible in reporting.
- **Resolution rate target (70% at 80% involvement)**: Reaching 70% resolution rate at 80% involvement depends on **filling feature gaps** (e.g. Webform-like intake, routing), **right content** (content strategy), and **data for Fin to access** (auth, APIs for Payments In / Payouts, balance/settlement). The content strategy ([content-strategy-2026.md](../../01-knowledge-base/strategy/content-strategy-2026.md)) and policy for sharing payments data over email using Fin are parallel dependencies - involvement rate and resolution rate must be tracked together.
- **Go-live gates**: We will not launch Fin on email with payments data sharing (Phase 3) without the policy for sharing payments data over email using Fin being reviewed and approved by InfoSec and Architecture Review Board. Phase 2 (Fin on email without payments data) goes live in Q2 with auth classifier only. We will not migrate Webform as the primary entry point until Fin replicates Webform behaviour (fields, routing) and support playbooks are updated and agents briefed.

## Approach

**The five levers in priority order:**

**Lever 1 - Fin on Email (Merchant) (Premium/Enterprise) [P0]**  
Premium/Enterprise Email (Merchant) only = 26.8% of all contacts (6,304; last 6m); Fin involvement = 0%. Email (Internal) is unreachable by Fin - not in scope. In development - driven by fin-email-auth-data-policy-prd.md. At 96% Fin involvement: +6,051 Fin contacts.

> **Note - Fin on email as a Dashboard and self-serve bridge**: When Fin responds to an email query, responses will include contextual links to the merchant's Dashboard and relevant self-serve resources (e.g. documentation, status pages). This serves two purposes: (1) it increases the likelihood Fin can resolve the query without human escalation by directing merchants to the right tool or information; (2) it surfaces the Dashboard and self-serve channels to Premium/Enterprise merchants who currently default to email, supporting longer-term channel shift. This is a design requirement for the email Fin UX - not just a content add-on.

**Lever 2 - Standard → Fin (Dashboard) (enforce success plan) [P0]**  
Per care-success-plans.md (Channel Entitlements), Standard has no Dedicated Email - only AI Agent, Dashboard Webform, Live Chat. Standard Email (Merchant) + Webform = 20.8% of all contacts (4,878). Today Standard email arrives at support@checkout.com; routing change: direct those contacts to Fin (Dashboard) instead (e.g. auto-reply with link to Dashboard chat - exact mechanism TBD with Care Operations). Enforcing the success plan increases Fin (Dashboard) volume. POLICY and ROUTING change - no email for Standard; redirect to Fin (Dashboard). At 96% Fin involvement on redirected contacts: +4,683 additional Fin contacts.

**Lever 3 - Webform → Fin chat migration (all Merchant segments) [P0]**  
Webform & API = 22.1% of all contacts (5,198; last 6m); Fin involvement = 0%. The Webform is a separate Zendesk intake product; Fin runs in Intercom. **Alternatives considered:** Delivering AI answers inside the Webform was considered; Fin does not support that. Intercom recommended using Fin as the primary entry (auto-classification, conversational intake) rather than a form - full migration was chosen for that reason. Integration would require Webform to call Intercom or vice versa; migration (redirect to Fin chat) is the chosen path. Fin must replicate Webform behaviour (structured intake, ticket fields, routing). After migration, on escalation Fin creates the Zendesk ticket on the merchant's behalf (same fields as Webform) so agents see equivalent context. At 96% Fin involvement: +4,990 additional Fin contacts.

**Lever 4 - Account unlock form → Fin [P1]**  
**Account unlock form** (channel: in flat table, Other + case_type = ACCOUNT MANAGEMENT & ACCESS + issue_type = Login & Access) = 4.9% of all contacts (1,159). Implementation: redirect to Fin chat or embed Fin in form flow - TBD with Engineering; same UX principle as Webform migration (Fin as first touchpoint). At 96% Fin involvement: +1,113 additional Fin contacts.

**Lever 5 - Maintain Fin chat involvement [P1]**  
Fin (Dashboard chat) = 9.2% of contacts today (2,162); by definition nearly 100% involved.

**Unreachable** (in denominator, not levers): Email (Internal) + Other = 4,391 (18.7%). Ceiling ~81%.

**Measurement framework:**

The involvement rate is measured against **all contacts** - the denominator is the full contact volume with no exclusions.

- **Denominator**: all inbound support contacts = Zendesk tickets + Fin-only resolved (no exclusions). Lock this definition with Care Operations - see [support_contacts_flat_table_2025_metric_definitions.md](../../01-knowledge-base/metrics/support_contacts_flat_table_2025_metric_definitions.md).
- **Numerator**: contacts where Fin was involved: (1) channel = Fin (Dashboard) - includes Fin-only resolved contacts that never became a Zendesk ticket, counted via Intercom/Fin channel or equivalent event in the live pipeline; (2) Zendesk tickets with `fin_involved = true` (e.g. Fin-on-email escalation). Ensure Fin-only resolved is counted in both denominator and numerator; logic must align with metric definitions so the rate is consistent over time.
- **Structurally unreachable contacts** (~18.7% of total - Email (Internal) 9.2%, plus Other channel: phone P1s, Dedicated Slack/IM, AM/TAM) are included in the denominator and count against the rate. **Account unlock form** is a separate channel and a lever (Lever 4), not unreachable. They set the theoretical ceiling at ~81%. Tag `fin_unreachable` and track separately so leadership can see the hard ceiling alongside the progress metric.
- **Reporting and instrumentation ownership:** Single source of truth for involvement rate = support contacts flat table (and live equivalent). Involvement rate dashboard exists; refresh cadence at least weekly so Care Ops and leadership can track progress. Fin tags (`fin_involved`, `fin_unreachable`) are already built into Fin’s logic with Zendesk and are reportable. Resolution rate (Fin-resolved / Fin-involved) is a separate metric; instrumentation and ownership aligned with content strategy and Fin behaviour - ensure it is defined and reportable so we can track “70% at 80% involvement” (see Goals & Success Metrics).

**Key UX decisions:**

- Fin must be positioned as the entry point, not an optional step after a ticket is already created
- For email, Fin responds before a human agent is assigned - not as a post-assignment FAQ bot
- For Webform migration, the approach is to make Fin capable of replicating everything the Webform does today: structured intake, correct Zendesk ticket field population, and routing logic. Once Fin can do this end-to-end, it becomes the functionally equivalent replacement. The Webform may be retained as a fallback for edge cases (e.g. attachment uploads) but should not be the primary entry point. This is within Care Product team control - no Dashboard product team dependency.
- The Webform should remain available as a fallback for merchants who explicitly need it (e.g. attachment uploads, complex forms) - the goal is migration, not removal

**Technical notes:**

- Lever 1 (email): Intercom/Fin configuration + Engineering (identification classifier, Zendesk field tagging) - see [fin-email-auth-data-policy-prd.md](fin-email-auth-data-policy-prd.md)
- Lever 3 (Webform migration): Care Product owned. Support entry point UX may require Dashboard Engineering involvement depending on where the entry point is hosted; scope with Dashboard as needed. Not an Intercom or Zendesk Admin change.
- Involvement rate reporting: requires a shared definition between Intercom and Zendesk. Zendesk tickets created from Fin escalations must be tagged `fin_involved = true`. Webform tickets that bypassed Fin should be tagged separately to track migration progress.

**Failure modes and error handling** (support and agent visibility):

- **Fin on email**: When Fin times out, mis-classifies, or cannot safely engage (e.g. auth failure), the ticket must route to a human agent with clear context (e.g. “Fin did not engage - reason: [timeout / exclusion rule / auth]”). Runbook and agent-facing docs must describe what the agent sees and how to triage. Define before Phase 2 go-live.
- **Webform migration**: When Fin cannot create the Zendesk ticket on the merchant’s behalf (e.g. integration failure, missing required field), a fallback path must exist so the contact still reaches support (e.g. merchant directed to submit via Webform fallback or ticket created with minimal fields and tagged for follow-up). Runbook must cover “Fin-created ticket failed” so agents know how to handle. Define before Phase 4 go-live.

## Out of Scope

- **Trade-offs**: Resolution rate feature work beyond content/data is out of scope for this programme; no delay to other roadmap items implied.
- **Resolution rate optimisation** - target is 70% resolution rate at 80% involvement, enabled by feature gaps, content, and data access. This PRD tracks involvement rate; resolution rate is driven by content strategy and policy for sharing payments data over email (Fin), tracked in [content-strategy-2026.md](../../01-knowledge-base/strategy/content-strategy-2026.md).
- **Removing the Dashboard Webform** - this programme migrates contacts from Webform to Fin chat; it does not require removing the Webform entirely. The Webform remains as a fallback channel.
- **Fin integration inside the Webform** - technically not possible; the lever is channel migration, not Webform integration.
- **Email (Internal)** - CKO-submitted email (`raised_by_cko` tag) is structurally unreachable by Fin. In the denominator; not a lever for this programme.
- **AM/TAM-submitted tickets** - tickets submitted by Account Managers or TAMs on behalf of merchants are not merchant-direct contacts. They are included in the denominator as part of the **Other** channel (unreachable by Fin); they do not get Fin involvement and thus count against the rate. The denominator remains *all* support contacts (see Measurement framework).
- **Phone channel** - P1 phone contacts are excluded from Fin involvement; out of scope for this programme.
- **Dedicated Slack/IM (Premium)** - Premium's Dedicated Slack/IM channel is not a Fin channel. Included in the denominator as part of **Other** (unreachable by Fin); counts against the rate.
- **B2C consumer support** - 2027 workstream, separate programme.
- **Sonar (internal AI agent)** - internal staff channel; separate from this programme.
- **Settlement status and balance API** - P2 Fin capability tracked in [fin-email-auth-data-policy-prd.md](fin-email-auth-data-policy-prd.md); improves resolution rate once involvement rate infrastructure is in place.

## Launch Plan

- **Phase 1 - Standard support model enforcement (Q2 2026)**: Stop accepting email from Standard merchants; redirect Email (Merchant) + Webform to Fin chat where applicable (4,878 contacts = 20.8% of total). Policy and routing change; requires a Zendesk trigger change (e.g. auto-reply/redirect to Dashboard, similar to Tier 4 email redirect in 2025), not Fin application build. **Dependency:** Premium/Enterprise email routing rules (Phase 2) must be in place at the same time as, or before, Standard enforcement so that rules are applied cleanly and systematically across all Merchant segments. Ops runbook: Standard email auto-reply / redirect message and go-live date TBD with Care Operations; no change to existing queues during transition.
- **Phase 2 - Fin on email without payments data sharing (Q2 2026)**: Launch Fin on email for Premium and Enterprise for **non-Payments issues only** (no sharing of payments data). Also apply Fin on the Account unlock form (Lever 4; 4.9% of contacts) in the same phase. Gated on auth classifier (org identification). Standard is out of scope. Premium/Enterprise email routing rules from this phase are a dependency for Phase 1 Standard enforcement.
- **Phase 3 - Fin on email with payments data sharing (Q3 2026)**: Enable Fin to handle **Payments In and Payouts** queries on email (~64% of Lever 1 Premium/Enterprise email volume). Gated on: (1) policy for sharing payments data over email using Fin reviewed and approved by InfoSec and Architecture Review Board, and (2) auth solution built so Fin can access merchant/transaction context. Standard is out of scope.
- **Phase 4 - Webform migration (Q3 2026)**: Care Product owned. Make Fin chat the primary support entry point in the Dashboard; intercept or redirect Webform-intent contacts to Fin chat before they submit a form. Coordinate with Dashboard Engineering for any hosted-surface changes as needed. Monitor shift in Webform vs. chat contact split.
- **Phase 5 - Gap close (Q3 2026)**: Assess involvement rate against target using Phase 1–4 data. Identify any residual gaps and address (e.g. chat adoption improvements, edge cases in email exclusion rules).
- **Phase 6 - Target review (Q4 2026)**: Confirm 80% achieved or identify remaining structural gaps. Decide whether to adjust the target or add levers if not on track.

**Rollback**: Instrumentation has no rollback risk. Fin on email reverts by disabling Fin on that channel (Fin configuration, not code); no persistent state - disabling Fin stops new email contacts from being assigned to Fin; existing tickets unchanged. Webform migration reverts by restoring the Webform as the primary Dashboard support CTA (Dashboard config change).

**Training**: Minimal new training: brief agents on new tags (`fin_involved`, `fin_unreachable`), Fin-created tickets (when Fin creates the ticket on behalf of merchant after Webform migration or email), and the Standard redirect message before each phase. Existing Fin escalation playbooks apply; before Phase 1 (Standard redirect): runbook update for redirect message and go-live comms; before Phase 2 (Fin on email without payments data): runbook update for email-originated Fin tickets; before Phase 3 (Fin on email with payments data): runbook update for payments-data queries; before Phase 4 (Webform migration): runbook update for Fin-created tickets and where to find Fin context. Care Operations owns runbook updates and briefing; go-live for each lever is gated on “playbook updated and agents briefed.”

**Success criteria for ops**: Involvement rate tracked in existing dashboard; no increase in escalation rate or SLA breaches during lever rollout; unreachable contacts tagged and reported; agents know how to handle Fin-created tickets and Standard redirect; first-week support plan (e.g. monitor redirect effectiveness, email Fin resolution and escalation rate) in place for each major lever.

## Risks, Dependencies & Open Questions

**Risks**:


| Risk                                                                                   | Likelihood | Impact                                                                            | Mitigation                                                                                                                                                                                      |
| -------------------------------------------------------------------------------------- | ---------- | --------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 80% target requires ~80% Fin involvement on both email AND webform                     | High       | High - neither lever alone is sufficient                                          | Both levers are P0; track separately and jointly against the overall target model                                                                                                               |
| Policy for sharing payments data over email (Fin) - InfoSec/ARB review & approval delayed - blocks Phase 3 (Fin on email with payments data)                                      | Medium     | High - Email (Merchant) is 45% of contacts (Email (Internal) 9.2% is unreachable) | Track as hard dependency; escalate if not resolved by end Q1                                                                                                                                    |
| Fin cannot fully replicate Webform behaviour - some fields or routing not reproducible | Low–Medium | Medium - delays migration lever or leaves a residual Webform population           | Audit Webform fields and routing logic early; treat gaps as Fin configuration work items                                                                                                        |
| Account unlock form vs Other - reporting split                                          | Confirmed  | Low - now defined as channel (Other + case_type = AMA + issue_type = Login & Access) | Account unlock form is Lever 4 (4.9%); Other is unreachable (9.5%). Instrument reporting so both appear as distinct channels. |
| Standard email volume (26.6%) is higher than channel entitlements suggest              | Low        | Medium - Standard not entitled to email; routing may need fixing                  | Consider whether Standard email should be redirected to chat or webform as a contact-reduction measure                                                                                          |
| Fin resolution rate doesn't improve alongside involvement rate                         | Medium     | Medium - high involvement + low resolution = poor experience                      | Content strategy and involvement rate tracked in parallel                                                                                                                                       |
| Support capacity or resolution can't keep up with lever rollout                         | Low–Medium | Medium - quality or SLA risk if we push levers without readiness                   | If support capacity or resolution rate cannot keep up, we slow lever rollout (e.g. phase Webform migration by Merchant segment, delay email go-live for a Merchant segment) rather than compromise quality or customer trust. |

**Lever slip priority:** If we must ship one lever late, we slip Webform migration (Lever 3); Fin on email and Standard enforcement are higher priority for the path to 80%.

**Dependencies**:


| Dependency                                                                   | Owner                              | Status                                                                                      | Risk if Delayed                                                                                           |
| ---------------------------------------------------------------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| Policy for sharing payments data over email using Fin - reviewed & approved by InfoSec and Architecture Review Board | InfoSec / Architecture Review Board | Not started                                                                                 | Blocks Phase 3 (Fin on email with payments data sharing)                                                |
| Fin email auth classifier (Salesforce + domain mapping)                      | Engineering                        | In flight                                                                                   | Blocks email lever; partial mitigations available (domain mapping alone). Domain mapping supplies org context to the classifier; both required for email identification. |
| Zendesk org domain mapping                                                   | Engineering                        | In development (see [zendesk-org-domain-mapping-prd.md](zendesk-org-domain-mapping-prd.md)) | Blocks email identification layer                                                                         |
| Fin replicates Webform behaviour (structured intake, ticket fields, routing) | Zendesk Admins / Fin configuration | Not started                                                                                 | Blocks Webform migration lever - 22.1% of contacts; within Care Product team control                      |
| Content strategy + data access (70% resolution at 80% involvement)           | Content team / Engineering         | In progress                                                                                 | Feature gaps, right content, and data for Fin to access; without these, high involvement = low resolution |
| Resolution rate metric (Fin-resolved / Fin-involved): definition, instrumentation, reporting | Product Data Science + Content / Fin | Not started (separate workstream) | Needed to track “70% at 80% involvement”; align with content strategy and Fin behaviour; add to roadmap if not already scoped |


**Open questions**:

- What is Fin's current involvement rate on Dashboard chat today? *(Answered: 9.2% overall - see `support_contacts_flat_table_2025_last_6m.csv` + `support_contacts_flat_table_2025_metric_definitions.md`)*
- What is the exact channel split by Merchant segment? *(Answered: Email (Merchant) 45.0%, Webform & API 22.1%, Account unlock form 4.9%, Other 9.5%, Email (Internal) 9.2%, Fin (Dashboard) 9.2% - see Volume Model. Account unlock form = Other + case_type = ACCOUNT MANAGEMENT & ACCESS + issue_type = Login & Access.)*
- What makes up the Other channel (9.5%)? *(Answered: Other is now defined to exclude Account unlock form. Remaining Other is likely phone/Slack/IM/AM/TAM - confirm with Care Operations; all unreachable.)*
- What % of Premium contacts arrive via Dedicated Slack/IM specifically? *(Owner: Care Operations - "Other" share of Premium; understanding how much is Slack/IM vs. phone vs. other sets the Premium ceiling)*
- Are the involvement target and achievable thresholds (e.g. ~81% ceiling, 80% target) agreed with Care Operations and leadership? *(Owner: Charlie Wildish - agree the target for involvement and the thresholds we can reach so the 80% target and ceiling are understood)*
- What fields does the Webform currently populate on Zendesk tickets, and what routing logic does it apply? *(Owner: Zendesk Admins - this is the specification Fin must replicate before Webform migration can proceed)*
- Should the Webform be fully deprecated once Fin replicates its behaviour, or retained as a permanent fallback for edge cases (e.g. attachment uploads)? *(Owner: Care Operations - affects whether any Webform contacts remain outside Fin's reach long-term)*

## Timeline


| Milestone                                                        | Date     | Owner                        | Status |
| ---------------------------------------------------------------- | -------- | ---------------------------- | ------ |
| PRD complete                                                     | Feb 2026 | Charlie Wildish              | Draft  |
| Per-Merchant-segment targets confirmed vs. actuals              | Q1 2026  | Charlie Wildish              | ⏳      |
| Premium/Enterprise email routing rules in place (Phase 2)        | Q2 2026  | Engineering / Zendesk Admins | ⏳      |
| Fin on email without payments data sharing - live (Phase 2) + Account unlock form | Q2 2026  | Engineering / Zendesk Admins | ⏳      |
| Standard support model enforcement - live (Phase 1)             | Q2 2026  | Care Operations              | ⏳      |
| Policy for sharing payments data over email (Fin) - approved (gates Phase 3) | Q2 2026  | InfoSec / Architecture Review Board | ⏳      |
| Fin on email with payments data sharing - live (Phase 3)        | Q3 2026  | Engineering / Zendesk Admins | ⏳      |
| Webform → Fin chat migration - live (Phase 4)                    | Q3 2026  | Engineering                  | ⏳      |
| 80% involvement rate achieved                                    | Q4 2026  | Charlie Wildish              | ⏳      |


## Document Review Panel feedback

*Applied from [document-review-panel.md](../../02-workflows/document-review-panel.md) (customer support angle).*

### 1. Sam - Product Manager

**Concerns**
- No single “one sentence for support” in the doc - agents need a reusable line for *why* we’re doing this and what’s in/out of scope.
- “What to tell merchants” for each change (Standard redirect, Fin on email, Webform migration) wasn’t explicit - support could struggle to set expectations and deflect.
- Deflection / out-of-scope: what we tell customers who ask for 100% Fin or Fin on Internal email isn’t spelled out so support can deflect confidently.

**Suggested edits** *(partially applied)*  
- Added **One sentence for support** in Executive Summary.  
- Added **Support-facing summary: what agents need to know** with one sentence for merchants, how tickets change, likely Q&A, and where to find playbook updates.

---

### 2. Jordan - Software Engineering / Tech Lead

**Concerns**
- **Failure modes and error handling** not called out: e.g. Fin on email - what does the agent see when Fin mis-classifies or times out? Webform migration - what if Fin doesn’t create the ticket (fallback?).
- **Runbooks before go-live:** Launch Plan says “existing Fin escalation playbooks apply” but new flows (Fin on email, Fin-created tickets) need explicit runbook updates and escalation paths; Engineering/Tech lead wants these defined before Phase 2 and Phase 4.
- **Webform spec:** “What fields does the Webform currently populate?” is still an open question - definition of done for Webform migration should include “Webform field and routing spec documented and signed off by Zendesk Admins” so implementation isn’t blocked.

**Suggested edits** *(applied)*  
- Added **Failure modes and error handling** in Technical notes: Fin on email (timeout/mis-classification → agent view, runbook before Phase 2); Webform migration (fallback when Fin doesn’t create ticket, runbook before Phase 4).  
- In P1 Webform requirement, added **Definition of done for Webform migration:** Webform field and routing spec signed off by Zendesk Admins; runbook updated for Fin-created tickets and escalation path; agents briefed before go-live.

---

### 3. Alex - Operations Agent (Frontline Support)

**Concerns**
- No single place that says “what’s the one sentence I use with a merchant?” and “how does my queue/triage change?” - doc is long; frontline needs a scannable summary.
- Likely merchant questions (e.g. “Why did I get a link to Dashboard?”) and suggested answers weren’t in the doc - agents will get these questions on day one.
- Escalation path for Fin-created tickets (email or post-Webform): is it the same as today? Doc said “document in playbook” but didn’t state explicitly that escalation path is unchanged and ticket contains Fin context.

**Suggested edits** *(partially applied)*  
- Added **Support-facing summary** with one sentence for merchants, how tickets change, 3 likely Q&As, and where to find playbook updates.  
- Clarified in that section: escalation path unchanged; ticket will contain Fin context.

---

### 4. Morgan - Chief of Product

**Concerns**
- “One thing we want everyone (including support) to remember” isn’t stated - exec narrative could be sharper (e.g. “80% of contacts will have Fin as first touchpoint; we’re pairing that with resolution so it’s a better experience, not just more volume”).
- “Won’t ship without” conditions were implied (policy for sharing payments data over email using Fin, etc.) but not explicit - e.g. we will not go live on Fin-on-email without approval of that policy; we will not migrate Webform until Fin replicates behaviour and playbooks are updated.
- If we had to protect support capacity or trust, what would we cut? No one-liner (e.g. “We would phase lever rollout or slow Webform migration by Merchant segment rather than compromise quality”).

**Suggested edits** *(applied)*  
- Added **Go-live gates** in Constraints: no Fin on email without policy for sharing payments data over email using Fin being reviewed and approved by InfoSec and Architecture Review Board; no Webform migration until Fin replicates behaviour and playbooks updated and agents briefed.  
- Added **Executive takeaway** in Executive Summary and a new risk row in Risks: “Support capacity or resolution can’t keep up” - mitigation is to slow lever rollout (e.g. phase Webform migration by Merchant segment) rather than compromise quality or customer trust.

---

### 5. Casey - Chief of Operations

**Concerns**
- **Training** said “no new agent training required” but Webform migration and Fin on email change how tickets arrive - at minimum, agents need briefings on new tags, Fin-created tickets, and Standard redirect; training section should be phase-specific (what playbook/briefing before Phase 1, 2, 4).
- **Support readiness checklist** not explicit: runbook updates, agent briefing, redirect message approved, dashboard access - who owns what and by when so ops can plan.
- “First week after go-live” for each major lever (e.g. monitor Standard redirect effectiveness, email Fin resolution and escalation rate) wasn’t called out so teams know what “good” looks like in the first week.

**Suggested edits** *(partially applied)*  
- Expanded **Training** in Launch Plan to be phase-specific: runbook and briefing before Phase 1, 2, and 4; Care Operations owns; go-live gated on “playbook updated and agents briefed.”  
- Expanded **Success criteria for ops** to include agents knowing how to handle Fin-created tickets and Standard redirect, and first-week support plan for each major lever.

---

### 6. Riley - Product Data Scientist

**Concerns**
- **Denominator consistency:** Out of Scope stated that AM/TAM-submitted tickets are “excluded from the involvement rate denominator,” but the Measurement framework says the denominator is “all inbound support contacts” and structurally unreachable contacts (including Other channel: AM/TAM) “are included in the denominator.” So we’re either excluding AM/TAM (and the denominator isn’t “all”) or including them as part of Other - the doc was inconsistent. Need one clear definition so the metric is interpretable over time.
- **Resolution rate measurability:** The 70% resolution-at-80%-involvement target is defined (Fin-resolved / Fin-involved) but instrumentation and ownership aren’t in this PRD - resolution is pointed to content strategy. Without a single source of truth and a plan to report resolution rate, we can’t prove or disprove “70% at 80%.” Who owns the resolution rate metric and dashboard, and is it in scope for this programme or a dependency we’re assuming?
- **Reporting ownership and cadence:** Phase 1 says “build a live reporting dashboard” but doesn’t state who owns it (Data Science? Zendesk Admins? Care Ops?), refresh cadence (e.g. weekly), or that the denominator definition is locked with Care Ops before build so we don’t rework. Support/ops need to use the dashboard to make decisions - feasibility and usability should be explicit.
- **Fin-only resolved in numerator and denominator:** Denominator = “Zendesk tickets + Fin-only resolved.” Contacts that Fin resolves without creating a ticket (Fin-only resolved) must be counted in both denominator and numerator. Is that clearly instrumented (e.g. in Intercom) so we don’t undercount? The metric definitions doc defines `fin_only_resolved`; ensure the live pipeline and dashboard use the same logic.

**Suggested edits** *(applied)*  
- Corrected **Out of Scope** for AM/TAM and **Dedicated Slack/IM (Premium)**: both are *included* in the denominator as part of Other (unreachable), not excluded - aligns with Measurement framework.  
- Added **Reporting and instrumentation ownership** in Measurement framework.  
- **Denominator lock:** Measurement framework now states denominator = zendesk_tickets + fin_only_resolved (no exclusions) and “Lock this definition with Care Ops before dashboard build”; Phase 1 explicitly requires locking denominator with Care Ops before build.  
- **Fin-only resolved in numerator:** Measurement framework now describes how numerator is counted: Fin (Dashboard) channel (including Fin-only resolved via Intercom/Fin event) + Zendesk `fin_involved = true`; Phase 1 includes “document how Fin-only resolved is counted in the numerator” so live pipeline matches metric definitions.  
- **Resolution rate ownership:** New dependency row - “Resolution rate metric (definition, instrumentation, reporting)” - Owner: Product Data Science + Content/Fin; separate workstream; needed to track “70% at 80%.”

---

### 7. Quinn - Zendesk Administrator

**Concerns**
- **Tags and reporting:** `fin_involved` and `fin_unreachable` are called out; doc doesn't say who configures them (Zendesk Admins), when they must be in place (Phase 1 for involvement rate dashboard), or whether any new views/triggers/routing depend on these tags so agents and reporting work. Zendesk Admin wants a single place that says "config work before Phase 1: these tags; before Phase 2/4: [any trigger/view changes]."
- **Dashboard vs Zendesk:** Involvement rate dashboard owner is "TBD (Product Data Science + Zendesk Admins per Phase 1)" - Zendesk Admin needs clarity on whether the dashboard is in Zendesk Explore, a separate tool, or both, and what Zendesk Admins must build or maintain (e.g. Explore report by Merchant segment/channel, tagging pipeline).
- **Webform migration:** "Webform field and routing spec documented and signed off by Zendesk Admins" is in the Webform DoD - good. Open question "What fields does the Webform currently populate?" is owned by Zendesk Admins. Doc could add one line: "Zendesk Admins own the Webform spec and sign-off before Fin replication work starts" so the dependency is explicit.

**Suggested edits** *(clarified, not applied as originally written)*  
- Fin tags (`fin_involved`, `fin_unreachable`) are already built into Fin’s logic with Zendesk and are reportable - no net-new Zendesk config required for tagging. Measurement framework updated to state this; removed the “Zendesk Admins: configure…” and dashboard TBD line. Webform spec remains an open question owned by Zendesk Admins; did not add “sign-off gates” to Dependencies.

---

### 8. Reese - Content Strategist

**Concerns**
- **Content is a dependency but not in the "what to have in place before launch" list:** Resolution rate target (70% at 80% involvement) depends on "right content" and content strategy; doc points to content-strategy-2026.md and has a dependency row for Content team. Content Strategist wants to see "content readiness" called out in the same way as "playbook updated and agents briefed" - e.g. for Phase 2 (Fin on email), is there a content checklist (e.g. email response templates, Fin KB coverage for high-volume email topics) so we don't launch email Fin with gaps?
- **Resolution rate and content:** The 70% resolution target is explicitly out of scope for *this* PRD (tracked in content strategy). That's clear. What's missing for Content: "When we track resolution rate, what content work is in scope for each phase?" (e.g. Phase 2: email-related content; Phase 4: Webform-intent content). One sentence in Launch Plan or Dependencies would help Content plan.
- **No content owner in Timeline:** Timeline has Engineering, Zendesk Admins, Charlie; resolution rate dependency lists Content/Fin. Content Strategist would expect at least one milestone or dependency row that says "Content: [deliverable or sign-off] by [phase]" so content isn't a vague dependency.

**Suggested edits** *(not applied)*  
- Involvement work does not materially impact content needs for this PRD; agents already know about Fin AI Agent involvement and escalations. Content strategy and resolution rate remain a dependency for the 70% resolution target, but no phase-specific content readiness or deliverable was added to Launch Plan or Dependencies.

---

### 9. Taylor - VP of Product

**Concerns**
- **Executive takeaway is present but could be more repeatable:** "Executive takeaway" in Executive Summary is good ("By end 2026, Fin is the first touchpoint for 80% of contacts; we pair that with resolution investments…"). VP wants to be sure that's the *one* line they use with CPO - consider making it a single bold or blockquote so it's the default "what we want everyone to remember."
- **Cut line is in Risks but not in Summary:** "If we had to protect support capacity or trust, we'd slow lever rollout" is in the risk table and Constraints. VP would want that cut line visible in Executive Summary or Recommendation so they don't have to dig - e.g. one sentence: "If capacity or trust is at risk, we phase lever rollout rather than compromise quality."
- **Ask for leadership:** The "ask" (resources, sign-offs, sequencing) is spread across Dependencies and Go-live gates. VP would advocate more easily with one short "Ask" or "Decisions needed" line in Executive Summary or right after it: e.g. "We need: policy for sharing payments data over email using Fin reviewed and approved by InfoSec and ARB by Q1; denominator lock with Care Ops; Content/Eng alignment on resolution rate instrumentation."

**Suggested edits** *(applied)*  
- **Executive takeaway** formatted as blockquote and set as "the one thing we want everyone to remember"; added cut line: "If we have to protect support capacity or customer trust, we phase lever rollout rather than compromise quality."
- Added **Ask / Decisions needed** (4 bullets) after Executive Summary: policy for sharing payments data over email using Fin reviewed and approved by InfoSec and ARB; denominator lock with Care Ops; Content/Eng for resolution rate; CPO-level decision on sequencing/resourcing.

---

### Panel checklist

| Persona | Considered? | Actions / notes |
|---------|-------------|-----------------|
| Product Manager (Sam) | ☑ | One sentence for support + support-facing summary added. |
| Software Engineering/Tech lead (Jordan) | ☑ | Failure modes + Webform DoD + runbook gates applied. |
| Operations agent (Alex) | ☑ | Support summary + Q&A + escalation clarity added. |
| Chief of Product (Morgan) | ☑ | Go-live gates + Executive takeaway + risk row (slow lever rollout) applied. |
| Chief of Operations (Casey) | ☑ | Training and success criteria expanded in Launch Plan. |
| Product Data Scientist (Riley) | ☑ | Denominator (AM/TAM, Dedicated Slack) fixed; reporting ownership; denominator lock + Fin-only numerator + resolution rate dependency applied. |
| Zendesk Administrator (Quinn) | ☑ | Clarified: Fin tags already in Fin logic with Zendesk, reportable; no net-new config. |
| Content Strategist (Reese) | ☑ | Not applied: involvement work doesn’t impact content needs; agents already know Fin involvement/escalations. |
| VP of Product (Taylor) | ☑ | Executive takeaway blockquote, cut line, Ask/Decisions needed applied. |


## Appendix

- [support_contacts_flat_table_2025_last_6m.csv](../../01-knowledge-base/metrics/support_contacts_flat_table_2025_last_6m.csv) - Support contacts flat table, last 6 months (source for volume model)
- [support_contacts_flat_table_2025_metric_definitions.md](../../01-knowledge-base/metrics/support_contacts_flat_table_2025_metric_definitions.md) - Definitions for count metrics, dimensions, and derived metrics (zendesk_tickets, fin_only_resolved, support_contacts, channel, etc.)
- [fin-email-auth-data-policy-prd.md](fin-email-auth-data-policy-prd.md) - Fin on email: authentication, policy for sharing payments data over email, exclusion rules
- [zendesk-org-domain-mapping-prd.md](zendesk-org-domain-mapping-prd.md) - Org identification / domain mapping (email auth dependency)
- [care-success-plans.md](../../01-knowledge-base/products/care-success-plans.md) - Channel entitlements by Merchant segment (defines which channels Fin can operate on per Merchant segment)
- [content-strategy-2026.md](../../01-knowledge-base/strategy/content-strategy-2026.md) - Content team roadmap; resolution rate target 70% at 80% involvement (feature gaps, content, data access)
- [ai-agent-operations.md](../../01-knowledge-base/processes/ai-agent-operations.md) - Fin operations, escalation patterns, current constraints

