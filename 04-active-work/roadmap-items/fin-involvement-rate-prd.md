# PRD: Fin Involvement Rate & AI Resolution Rate — 80% Target by End 2026

**Author:** Charlie Wildish  
**Date:** February 2026  
**Approvers:** Director of Operations, Director of Operations Excellence, VP of Product  
**Stage:** Solution Design  
**Status:** Draft  
**Last Updated:** February 2026  
**Stakeholders:** Care Operations (own 80% target), Engineering (email + webform migration + instrumentation), Zendesk Admins (tagging, routing, reporting), Content team (resolution-rate content), Product (Intercom/Fin).

**Roadmap alignment (Care & Support):** Reference `2026 deliverables.md` and `01-knowledge-base/strategy/care-product-model.md`.


| Field                | Value                                                                                                                                                                                                                                                                                       |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2026 deliverable** | AI First Resolution Using Fin                                                                                                                                                                                                                                                               |
| **Strategic goal**   | Reduce cost of support                                                                                                                                                                                                                                                                      |
| **Flywheel domain**  | 1. Input (channel mix) · 2. Orchestration (triage, Fin as first touchpoint)                                                                                                                                                                                                                 |
| **How it fits**      | Today Fin is Dashboard chat only (9.2% involvement). This PRD defines the five levers (Fin on email, Standard→Fin Dashboard, Webform→Fin chat, Account unlock form, maintain chat) to reach 80% Fin involvement by end 2026, paired with 70% resolution at 80% via content and data access. |


---

## Executive Summary

We are reducing Checkout's cost of support and giving merchants a faster support experience by making Fin the first touchpoint for 80% of contacts by end 2026. Today Fin is Dashboard chat only (9.2% involvement). Five levers close the gap: Fin on Email (Premium/Enterprise), enforce success plan so Standard uses Fin (Dashboard), Webform→Fin chat migration, Account unlock form→Fin, and maintain Fin chat. ~18.7% of contacts are unreachable (Email Internal, Other channel), so ceiling is ~81%; levers must average ~96% Fin involvement to hit 80%. We pair involvement with resolution investments (content, data access, feature gaps) so the target is 70% resolution rate at 80% involvement; overall AI resolution = involvement × resolution (e.g. 80% × 70% ≈ 56% of contacts).

**One sentence for support:** "We're making Fin the first touchpoint for most contacts so more queries are resolved by AI; your job is to handle what Fin can't resolve and set merchant expectations on channel (e.g. Standard → Dashboard, Premium/Enterprise → Fin may reply first to email)."

> **Executive takeaway:** By end 2026, Fin is the first touchpoint for 80% of contacts; we pair that with resolution investments so support and merchants see a better experience, not just higher volume. If we have to protect support capacity or customer trust, we phase lever rollout rather than compromise quality.

**Ask / Decisions:**

- Policy for sharing payments data over email using Fin reviewed and approved by InfoSec and Architecture Review Board by Q2 (gates Phase 3).
- Agree involvement target and achievable thresholds with Care Ops and leadership.
- Content/Eng alignment on resolution rate instrumentation.
- CPO call on Webform vs email sequencing/resourcing.

---

## Problem Space

**Problem statement:** We need to reduce cost of support and provide a faster experience; 80% Fin involvement (Fin as first touchpoint for most contacts) with 70% resolution at that involvement drives overall AI resolution. Today Fin is Dashboard chat only (9.2% involvement). Email (Merchant) and Webform have 0% Fin; those merchants never see Fin.

**Who is affected:** All merchant segments (Standard, Enterprise, Premium) and Care Operations (own 80% target). Premium/Enterprise use email most; Standard sends 26.6% via email today despite no Dedicated Email entitlement per [care-success-plans.md](../../01-knowledge-base/products/care-success-plans.md).

**Evidence:** Channel split (source: `support_contacts_flat_table_2025_last_6m.csv`, last 6 months; definitions: [support_contacts_flat_table_2025_metric_definitions.md](../../01-knowledge-base/metrics/support_contacts_flat_table_2025_metric_definitions.md)):


| Channel                         | % of contacts | Fin today                   | Gap                             |
| ------------------------------- | ------------- | --------------------------- | ------------------------------- |
| Email (Merchant)                | 45.0%         | 0%                          | Deploy Fin (Premium/Enterprise) |
| Webform & API                   | 22.1%         | 0%                          | Migrate to Fin chat             |
| Account unlock form             | 4.9%          | 0%                          | Apply Fin (Lever 4)             |
| Other (phone, Slack/IM, AM/TAM) | 9.5%          | Unreachable                 | -                               |
| Email (Internal)                | 9.2%          | Unreachable (CKO-submitted) | -                               |
| Fin (Dashboard chat)            | 9.2%          | ~100%                       | Maintain                        |


Current involvement: 9.2% (2,162 Fin contacts / 23,481 total). Unreachable = 18.7% → ceiling ~81%.

**Competitive context:** N/A for this programme (internal capability and channel mix).

**Why now:** 80% is a 2026 target and unblocks the Care flywheel. Fin on email (Premium/Enterprise) is in development; this PRD defines the rest. 70% resolution at 80% depends on feature gaps, content, and data (content strategy + policy for sharing payments data over email using Fin).

---

## Goals and Success Metrics

**Business goals:** Reduce cost of support; 80% Fin involvement by end 2026; 70% resolution rate at 80% involvement (enabled by feature gaps, content, and data access).

**Merchant goals:** Faster resolution; Fin as first touchpoint where entitled (Standard: Dashboard; Premium/Enterprise: Fin may reply first on email).

**Non-goals:** Resolution-rate feature work beyond content/data; removing the Webform (migration, not removal); Email (Internal); B2C; Sonar; settlement/balance API (P2 elsewhere). AM/TAM, phone, Dedicated Slack/IM remain in denominator as unreachable.

**Success metrics:**


| Metric                                  | Why it matters                                                              | Baseline       | Target                 | Source                                                       |
| --------------------------------------- | --------------------------------------------------------------------------- | -------------- | ---------------------- | ------------------------------------------------------------ |
| Fin involvement rate (all segments)     | Primary outcome; path to cost reduction                                     | 9.2% (last 6m) | 80%                    | End of 2026; support contacts flat table                     |
| AI resolution rate (at 80% involvement) | Quality of Fin resolution; overall AI resolution = involvement × resolution | ~70% (target)  | 70%                    | Conditional on feature gaps, content, data; content strategy |
| Structurally unreachable %              | Ceiling for involvement; 100% not achievable                                | 18.7%          | Reported; ceiling ~81% | Tag `fin_unreachable`; denominator unchanged                 |


Per-segment targets (at 96% lever execution): Standard 74.9%, Enterprise 78.8%, Premium 78.2%. Without data auth on email, Enterprise/Premium miss targets; data auth adds +16.5 pp to Lever 1 (see Appendix).

**Failure definition:** We would consider this a failure if (1) involvement rate cannot exceed 50%, or (2) Fin involvement materially harms merchant experience (sustained CSAT decline or material Commercial escalations). In either case we reassess lever rollout and resolution investments.

**Resolution rate vs involvement:** As involvement rises, Fin sees a harder query mix; resolution rate will dip unless we fill feature gaps, add content, and give Fin data access. Target 70% resolution at 80% involvement depends on those investments. Instrumentation and ownership for resolution rate sit with Content/Fin and Product Data Science (separate workstream).

---

## Customer Segments & Needs

**Customer segment(s):** Standard, Enterprise, Premium (all merchant segments); Care Operations and Care Product (reporting and ceiling visibility).

**User stories**

- **As a merchant (any segment) who previously used the Dashboard Webform,** I want the support entry point to guide me to Fin chat first, so that I get an instant response. *AC:* Fin chat is primary CTA; Webform secondary/fallback; Fin creates Zendesk ticket on escalation with same fields as Webform; Webform remains as fallback.
- **As an Enterprise or Premium merchant,** I want Fin to respond to my email support queries (where appropriate) before a human, so that I get faster answers. *AC:* Fin invoked on Email (Merchant) for Enterprise/Premium only; exclusion rules applied ([fin-email-auth-data-policy-prd.md](fin-email-auth-data-policy-prd.md)); Fin attempts resolution and only creates ticket if it cannot resolve; involvement on email tracked by segment.
- **As a Care Operations manager,** I want Fin involvement rate by Merchant segment and channel in one dashboard, so that I can track progress to 80% and see where adoption lags. *AC:* Reportable metric by segment and channel; baseline Q1 2026; weekly reporting. **As a Care Product Manager,** I want unreachable contacts tagged and the ceiling (~81%) visible so leadership understands 100% is not achievable. *AC:* `fin_unreachable` tag; ceiling in dashboard.

**Support-facing summary**

- **One sentence for merchants:** "Fin will often be the first to respond (Dashboard or, for Premium/Enterprise, by email); if Fin can't fix it, a human will take over with full context."
- **How tickets change:** More `fin_involved`; new tag `fin_unreachable`. After Webform migration, some tickets created by Fin on merchant's behalf (same fields as Webform). Escalation path unchanged; ticket contains Fin context.
- **Likely Q&A:** "Why link to Dashboard?" → "Standard support is via Dashboard for a faster response from Fin." "Who replied to my email?" → "For Premium/Enterprise, Fin may reply first; if not resolved, a human has full context." "Where's the form?" → "Fin chat is the main entry; form still available for attachments."
- **Updates:** Playbooks and runbooks updated before each phase; Care Operations briefs agents before go-live.

---

## Proposed Solution & Scope

**Solution overview:** Five levers in priority order: (1) Fin on Email (Merchant) for Premium/Enterprise, (2) Standard → Fin (Dashboard) by enforcing success plan (no email for Standard), (3) Webform → Fin chat migration, (4) Account unlock form → Fin, (5) maintain Fin (Dashboard) chat. Unreachable (Email Internal + Other) = 18.7%; ceiling ~81%. Reaching 80% requires levers to average ~96% Fin involvement. Email responses will include Dashboard and self-serve links to support resolution and channel shift.

**In scope:**

- Involvement rate instrumentation (by segment and channel) before levers launch.
- Standard support model enforcement (redirect Standard email to Fin Dashboard; policy/routing).
- Fin on email (Premium/Enterprise), Email (Merchant) only; auth and data policy per [fin-email-auth-data-policy-prd.md](fin-email-auth-data-policy-prd.md).
- Webform → Fin chat migration (Fin replicates Webform behaviour; primary entry; Webform fallback).
- Account unlock form → Fin.
- Maintain Fin (Dashboard) chat.
- Reporting: involvement rate dashboard, `fin_involved` / `fin_unreachable` tags, unreachable % (ceiling).

**Out of scope:** Resolution-rate feature work beyond content/data; removing Webform entirely; Fin inside Webform (not possible); Email (Internal); AM/TAM, phone, Dedicated Slack/IM as Fin channels (in denominator as unreachable); B2C; Sonar; settlement/balance API (P2 in fin-email-auth-data-policy-prd).

---

## Alternatives Considered

**Option 1 — AI inside Webform:** Deliver Fin answers inside the Webform. Rejected: Fin does not support that; Intercom recommended Fin as primary entry (conversational intake). Migration to Fin chat chosen.

**Option 2 — Full Webform deprecation:** Remove Webform once Fin replicates behaviour. Rejected: Webform retained as fallback (e.g. attachments, edge cases). Goal is migration, not removal.

**Why this approach:** Lever-based model addresses each channel explicitly; policy (Standard) and product (email, webform, account unlock) changes are separable and can be phased.

---

## Key Assumptions and Validation

- **Channel mix is static for planning.** Model uses last-6m proportions. Revisit channel mix quarterly; if email share grows, lever execution rate may need to exceed 96%.
- **Fin (Dashboard) share baseline (9.2%) is maintained.** Organic growth in chat would lift involvement and reduce pressure on other levers; track Fin (Dashboard) share monthly.
- **70% resolution at 80% involvement** depends on feature gaps filled, right content, and data access (auth, APIs for Payments In/Payouts). Validate with resolution-rate instrumentation and content strategy; track alongside involvement.
- **Policy for sharing payments data over email using Fin** is approved by InfoSec and Architecture Review Board before Phase 3. Hard gate; escalate if not resolved by end Q1.

---

## Requirements

**Requirements by audience / domain**


| Domain                    | Requirement IDs  | Purpose                                                                                                                   |
| ------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **Merchant**              | FR-1, FR-2, FR-3 | Fin as first touchpoint (Webform→chat, email for Premium/Enterprise, Account unlock); fallback where needed               |
| **Care Ops / CX**         | FR-4, FR-5, FR-6 | Instrumentation and reporting; Standard redirect and runbooks; Fin-created tickets and tags; exclusion ceiling documented |
| **Analytics & Reporting** | FR-4, NFR-1      | Involvement rate by segment/channel; unreachable %; weekly dashboard                                                      |
| **Product / Platform**    | FR-1–FR-7        | Instrumentation, Fin on email, Webform replication, routing, tags                                                         |


### Functional requirements

**Must Have (P0)**

- **FR-1 — Involvement rate instrumentation:** Fin involvement rate measurable by Merchant segment and channel before levers launch. *AC:* Metric defined (Fin-touched / total contacts); denominator = all support contacts (Zendesk + Fin-only resolved); locked with Care Ops; Intercom/Zendesk reporting in place.
- **FR-2 — Standard support model enforcement:** Per [care-success-plans.md](../../01-knowledge-base/products/care-success-plans.md), Standard has no Dedicated Email. Enforce by redirecting Standard email to Fin (Dashboard) (e.g. auto-reply/redirect). Policy and routing change; Zendesk trigger. *AC:* Standard email no longer accepted; redirect to Dashboard; runbook and message agreed with Care Ops.
- **FR-3 — Fin on email (Premium/Enterprise):** Fin as first responder on Email (Merchant) from Premium and Enterprise. Email (Internal) out of scope. Auth and data policy per [fin-email-auth-data-policy-prd.md](fin-email-auth-data-policy-prd.md). *AC:* Fin invoked on eligible tickets; exclusion rules applied; resolution attempted before human ticket; involvement on email tracked by segment.
- **FR-4 — Per-segment targets confirmed:** Validate per-segment targets vs actual baseline and confirm 80% aggregate achievable before Q2. *AC:* Targets confirmed with Care Ops/leadership.

**Definition of done (P0):** Involvement rate instrumented and reported; policy for sharing payments data over email using Fin approved by InfoSec and ARB; per-segment targets confirmed.

**Should Have (P1)**

- **FR-5 — Webform → Fin chat migration:** Fin replicates Webform (structured intake, ticket fields, routing); Fin chat becomes primary entry; Webform fallback. *AC:* Webform spec signed off by Zendesk Admins; runbook for Fin-created tickets; agents briefed before go-live.
- **FR-6 — Dashboard chat prominence:** Fin chat is the most prominent support entry in Dashboard for all segments (with Webform migration). *AC:* Scoped with Dashboard Engineering as needed.
- **FR-7 — Exclusion ceiling documented:** % structurally ineligible for Fin per segment (Email Internal, Slack/IM, phone, AM/TAM) documented; ceiling ~81% visible in reporting. *AC:* `fin_unreachable` tagged; dashboard shows ceiling.

**Nice to Have (P2)**

- **FR-8 — Involvement rate by merchant:** Track at individual merchant level for targeted nudges.
- **FR-9 — Proactive Fin in Dashboard:** Surface Fin contextually for high-volume issue types before contact.

### Non-functional requirements

- **NFR-1:** Involvement rate dashboard refresh at least weekly; single source of truth = support contacts flat table (and live equivalent). Fin-only resolved counted in both denominator and numerator; logic aligned with [support_contacts_flat_table_2025_metric_definitions.md](../../01-knowledge-base/metrics/support_contacts_flat_table_2025_metric_definitions.md).

**Constraints**

- Channel entitlements fixed by segment ([care-success-plans.md](../../01-knowledge-base/products/care-success-plans.md)); Standard no dedicated email; email Fin = Premium/Enterprise only.
- Payments data over email: Phase 3 gated on policy approved by InfoSec and ARB; Phase 2 = Fin on email without payments data (auth classifier only).
- Structural ceiling: 18.7% unreachable; tag `fin_unreachable`; remain in denominator.
- Go-live gates: No Phase 3 without policy approval; no Webform migration until Fin replicates behaviour and playbooks updated and agents briefed.

---

## Design and User Experience

**Key UX principles:** Fin is the entry point, not an optional step after a ticket exists. On email, Fin responds before a human is assigned. For Webform migration, Fin replicates Webform behaviour (intake, fields, routing) then becomes primary entry; Webform remains fallback. Email Fin responses include Dashboard and self-serve links. See [fin-email-auth-data-policy-prd.md](fin-email-auth-data-policy-prd.md) for email auth and data UX.

---

## Instrumentation and Monitoring

**Key events/properties:** Fin involvement (numerator = Fin (Dashboard) channel + Zendesk `fin_involved = true`; denominator = all support contacts); `fin_involved`, `fin_unreachable`; segment and channel. Source: support contacts flat table and live equivalent.

**Dashboards:** Involvement rate by Merchant segment and channel; unreachable % (ceiling ~81%). Cadence: at least weekly.

**Validation:** Denominator locked with Care Ops before build; Fin-only resolved included in numerator; definition aligned with metric definitions doc. Failure modes: Fin on email (timeout/mis-classification/auth failure → ticket to human with context; runbook before Phase 2). Webform migration (Fin cannot create ticket → fallback to Webform or minimal ticket; runbook before Phase 4).

---

## Risks and Open Questions

**Risks**

- **80% requires strong execution on both email and webform levers.** Mitigation: Both P0; track jointly and separately.
- **Policy for payments data over email delayed.** Blocks Phase 3. Mitigation: Hard dependency; escalate by end Q1.
- **Fin cannot fully replicate Webform.** Mitigation: Audit fields and routing early; gaps = Fin config work.
- **Resolution rate doesn't improve with involvement.** Mitigation: Content strategy and involvement tracked in parallel.
- **Support capacity or resolution can't keep up.** Mitigation: Phase lever rollout (e.g. Webform by segment) rather than compromise quality or trust.

**Lever slip priority:** If one lever slips, slip Webform migration last; Fin on email and Standard enforcement are higher priority.

**Open questions**

- Webform fields and routing spec (owner: Zendesk Admins).
- Webform fully deprecated vs permanent fallback (owner: Care Operations).
- Premium Dedicated Slack/IM % of Other (owner: Care Operations).
- Involvement target and thresholds agreed with Care Ops and leadership (owner: Charlie Wildish).

---

## Rollout Plan

**Rollout approach:** Phased by lever. Rollback: disable Fin on channel (config) or restore Webform as primary CTA. If capacity or trust at risk, phase lever rollout rather than compromise quality.

### Phase 1 — Standard support model enforcement (Q2 2026)

**Purpose:** Redirect Standard email to Fin (Dashboard); increase Fin (Dashboard) volume.

**Entry criteria:** Premium/Enterprise email routing (Phase 2) in place at or before Phase 1 so rules apply cleanly; runbook and redirect message agreed with Care Ops.

**Success criteria:** Standard email redirected; no increase in escalation/SLA breaches; agents briefed.

**Timeline:** Q2 2026. Owner: Care Operations.

### Phase 2 — Fin on email without payments data + Account unlock form (Q2 2026)

**Purpose:** Fin on email for Premium/Enterprise (non-Payments only); Fin on Account unlock form.

**Entry criteria:** Auth classifier (org identification) in place; runbook for email-originated Fin tickets; agents briefed.

**Success criteria:** Fin live on email (no payments data) and Account unlock form; involvement tracked.

**Timeline:** Q2 2026. Owner: Engineering / Zendesk Admins.

### Phase 3 — Fin on email with payments data (Q3 2026)

**Purpose:** Fin handles Payments In and Payouts on email (~64% of Lever 1 volume).

**Entry criteria:** Policy for sharing payments data over email using Fin approved by InfoSec and ARB; auth solution for merchant/transaction context.

**Success criteria:** Fin returns payment data on email where policy allows; runbook updated.

**Timeline:** Q3 2026. Owner: Engineering / Zendesk Admins.

### Phase 4 — Webform migration (Q3 2026)

**Purpose:** Fin chat primary support entry; Webform-intent contacts to Fin before form.

**Entry criteria:** Fin replicates Webform behaviour (fields, routing); Webform spec signed off; runbook for Fin-created tickets; agents briefed.

**Success criteria:** Fin primary entry; Webform fallback; no SLA breach; first-week support plan in place.

**Timeline:** Q3 2026. Owner: Care Product / Engineering.

### Phase 5 — Gap close (Q3 2026)

**Purpose:** Assess involvement vs target; address residual gaps (chat adoption, email exclusion edge cases).

**Timeline:** Q3 2026.

### Phase 6 — Target review (Q4 2026)

**Purpose:** Confirm 80% or identify remaining gaps; decide whether to adjust target or add levers.

**Timeline:** Q4 2026. Owner: Charlie Wildish.

**Definition of Done:** Instrumentation and tags live; policy approved for Phase 3; runbooks updated and agents briefed per phase; first-week support plan for each major lever; involvement rate tracked; no escalation/SLA breach increase.

**Product Dependencies**


| Dependency                                           | Owner                              | Risk if delayed                                                                                      |
| ---------------------------------------------------- | ---------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Policy for payments data over email (Fin) approved   | InfoSec / ARB                      | Blocks Phase 3                                                                                       |
| Fin email auth classifier + domain mapping           | Engineering                        | Blocks email lever                                                                                   |
| Zendesk org domain mapping                           | Engineering                        | Blocks email identification ([zendesk-org-domain-mapping-prd.md](zendesk-org-domain-mapping-prd.md)) |
| Fin replicates Webform behaviour                     | Zendesk Admins / Fin config        | Blocks Phase 4                                                                                       |
| Resolution rate metric (definition, instrumentation) | Product Data Science + Content/Fin | Needed to track 70% at 80%                                                                           |


**Go-to-market:** Care Operations owns runbook updates and agent briefing; go-live gated on "playbook updated and agents briefed" per phase. Success criteria for ops: involvement tracked; unreachable tagged; agents know Fin-created tickets and Standard redirect; first-week plan per major lever.

**Timeline (summary)**


| Milestone                                                | Date     | Owner                        |
| -------------------------------------------------------- | -------- | ---------------------------- |
| PRD complete                                             | Feb 2026 | Charlie Wildish              |
| Per-segment targets confirmed                            | Q1 2026  | Charlie Wildish              |
| Premium/Enterprise email routing (Phase 2)               | Q2 2026  | Engineering / Zendesk Admins |
| Fin on email without payments + Account unlock (Phase 2) | Q2 2026  | Engineering / Zendesk Admins |
| Standard enforcement (Phase 1)                           | Q2 2026  | Care Operations              |
| Policy for payments data over email approved             | Q2 2026  | InfoSec / ARB                |
| Fin on email with payments data (Phase 3)                | Q3 2026  | Engineering / Zendesk Admins |
| Webform migration (Phase 4)                              | Q3 2026  | Engineering                  |
| 80% involvement achieved                                 | Q4 2026  | Charlie Wildish              |


---

## Appendix

**Document Review Panel:** Review panel feedback has been applied; see Document Review Panel feedback below.

**Links**

- [support_contacts_flat_table_2025_last_6m.csv](../../01-knowledge-base/metrics/support_contacts_flat_table_2025_last_6m.csv) — Source for volume model
- [support_contacts_flat_table_2025_metric_definitions.md](../../01-knowledge-base/metrics/support_contacts_flat_table_2025_metric_definitions.md) — Metric definitions
- [fin-email-auth-data-policy-prd.md](fin-email-auth-data-policy-prd.md) — Fin on email: auth and data policy
- [zendesk-org-domain-mapping-prd.md](zendesk-org-domain-mapping-prd.md) — Org identification
- [care-success-plans.md](../../01-knowledge-base/products/care-success-plans.md) — Channel entitlements
- [content-strategy-2026.md](../../01-knowledge-base/strategy/content-strategy-2026.md) — Resolution rate target 70% at 80%
- [ai-agent-operations.md](../../01-knowledge-base/processes/ai-agent-operations.md) — Fin operations

### Volume model (detailed)

Channel definitions and scenario table (last 6 months; denominator = 23,481). Unreachable = Email (Internal) 9.2% + Other 9.5% = 18.7%. Account unlock form = Other + case_type ACCOUNT MANAGEMENT & ACCESS + issue_type Login & Access (4.9%; Lever 4).


| Lever                               | Contacts   | % of total | At 96% Fin         |
| ----------------------------------- | ---------- | ---------- | ------------------ |
| Premium/Enterprise Email (Merchant) | 6,304      | 26.8%      | 6,051              |
| Standard → Fin (Dashboard)          | 4,878      | 20.8%      | 4,683              |
| Webform → Fin chat                  | 5,198      | 22.1%      | 4,990              |
| Account unlock form                 | 1,159      | 4.9%       | 1,113              |
| Fin (Dashboard) maintain            | 2,162      | 9.2%       | 2,162              |
| Unreachable                         | 4,391      | 18.7%      | 0                  |
| **Total**                           | **23,481** |            | **18,999 (80.9%)** |


At 80% per lever: 69.0%; at 90%: 76.4%. Model assumptions: channel mix static (revisit quarterly); Fin (Dashboard) share not modelled as growing (track monthly).

**Lever 1 with vs without data auth:** With data auth +6,051 Fin contacts (+25.8 pp). Without (non–Payments In / non–Payouts only) +2,178 (+9.3 pp). Delta +16.5 pp. Enterprise/Premium miss segment targets without data auth; Standard unchanged (no Lever 1).

### Full risk and dependency tables


| Risk                                      | Likelihood | Impact | Mitigation                                    |
| ----------------------------------------- | ---------- | ------ | --------------------------------------------- |
| 80% requires both email and webform       | High       | High   | Both P0; track jointly and separately         |
| Policy (payments data over email) delayed | Medium     | High   | Hard dependency; escalate by end Q1           |
| Fin cannot fully replicate Webform        | Low–Medium | Medium | Audit early; gaps = Fin config                |
| Resolution rate doesn't improve           | Medium     | Medium | Content strategy in parallel                  |
| Support capacity can't keep up            | Low–Medium | Medium | Phase lever rollout; don't compromise quality |



| Dependency                                           | Owner                              | Risk if delayed                        |
| ---------------------------------------------------- | ---------------------------------- | -------------------------------------- |
| Policy for payments data over email approved         | InfoSec / ARB                      | Blocks Phase 3                         |
| Fin email auth classifier + domain mapping           | Engineering                        | Blocks email lever                     |
| Zendesk org domain mapping                           | Engineering                        | Blocks email identification            |
| Fin replicates Webform behaviour                     | Zendesk Admins / Fin config        | Blocks Phase 4                         |
| Content strategy + data access (70% at 80%)          | Content / Engineering              | High involvement + low resolution risk |
| Resolution rate metric (definition, instrumentation) | Product Data Science + Content/Fin | Cannot track 70% at 80%                |


### Document Review Panel feedback

*Applied from [document-review-panel.md](../../02-workflows/document-review-panel.md).*

- **Sam (PM):** One sentence for support and support-facing summary added.
- **Jordan (Eng):** Failure modes and Webform DoD and runbook gates applied.
- **Alex (Ops):** Support summary, Q&A, escalation path clarity added.
- **Morgan (Chief Product):** Go-live gates, Executive takeaway, risk row (slow lever rollout) applied.
- **Casey (Chief Ops):** Training and success criteria expanded in Rollout Plan.
- **Riley (Data Science):** Denominator (AM/TAM, Dedicated Slack in denominator); reporting ownership; Fin-only in numerator; resolution rate dependency applied.
- **Quinn (Zendesk):** Fin tags in Fin logic with Zendesk, reportable; no net-new config.
- **Reese (Content):** Content strategy remains dependency; no phase-specific content deliverable added.
- **Taylor (VP Product):** Executive takeaway blockquote, cut line, Ask/Decisions needed applied.

