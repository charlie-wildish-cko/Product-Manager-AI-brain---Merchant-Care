---
confluence_space_key: MTC
confluence_parent_page_id: 8041431176
title: Fin Involvement Rate & AI Resolution Rate — 2026 Progress Chart
---

# Fin Involvement Rate & AI Resolution Rate — 2026 Progress Chart

**Owner:** Charlie Wildish
**Audience:** CPO
**Last updated:** March 2026
**Source:** [fin-involvement-rate-cpo-coo-memo.md](roadmap-items/fin-involvement-rate-cpo-coo-memo.md)

---

## Targets

| Metric | Baseline (2025) | End of 2026 target |
|---|---|---|
| Fin involvement rate | 9.2% | **80%** |
| AI resolution rate (at 80% involvement) | 60–70% | **70%** |
| Overall AI resolution (involvement × resolution) | ~8–11% | **~56%** |

> **Ceiling:** 18.7% of contacts are structurally unreachable by Fin (internal CKO email, phone, Dedicated Slack/IM). The hard ceiling is ~81%. The 80% target is achievable; 100% is not.

---

## 2026 Progress Chart

| Period | Involvement rate (plan) | Involvement rate (actual) | Resolution rate (plan) | Resolution rate (actual) | Involvement rate driver | Resolution rate driver |
|---|---|---|---|---|---|---|
| **Start (2025 baseline)** | 9.2% | | 60–70% | | Fin on Dashboard chat only | Chat-only query mix; self-selected merchants |
| **Q1 2026** | 9–12% | | 60–70% | | Baseline confirmed; no new levers live | Same query mix; instrumentation set up |
| **Q2 2026** | ~30% | | 50–60% | | L2: Standard redirected to Fin chat; L1: Fin on email for non-payments queries (Premium/Enterprise) | Harder query mix as Standard joins; content investment begins |
| **Q3 2026** | ~65% → **~80%** | | 45–55%, then recovering | | L1: Fin on email with payments data (post data auth approval); L3: Webform migrated to Fin chat; L4: Account unlock form via Fin — all major levers land this quarter | Email and Webform queries harder; data access and feature gaps filled driving recovery toward 70% |
| **Q4 2026** | **~80% sustained** | | **70%** | | No new levers — gap close, residual edge cases addressed, target confirmed | Full content coverage and data access realised; resolution rate target confirmed |

*Fill in the "actual" columns each quarter. Overall AI resolution = involvement rate × resolution rate.*

---

## How We Get There — The Five Levers

| Lever | What changes | Contacts affected | Involvement uplift | Phase |
|---|---|---|---|---|
| **L1 — Fin on email (Premium/Enterprise)** | Fin becomes first responder on merchant email | 6,304 | **+25.8 pp** | Q2 (non-payments) / Q3 (payments) |
| **L2 — Standard redirect to Fin (Dashboard)** | Standard merchants no longer entitled to email; redirected to Fin chat | 4,878 | **+19.9 pp** | Q2 |
| **L3 — Webform migration to Fin chat** | Fin chat replaces Webform as primary Dashboard support entry point | 5,198 | **+21.2 pp** | Q3 |
| **L4 — Account unlock form via Fin** | Account unlock flow handled by Fin | 1,159 | +4.7 pp | Q3 |
| **L5 — Maintain Dashboard chat** | Existing Fin chat baseline | 2,162 | 9.2 pp (baseline) | Ongoing |
| Unreachable (not a lever) | Internal CKO email, phone, Slack/IM | 4,391 | 0 | — |
| **Total** | | **23,481** | **80.9%** | |

> **Critical dependency — Lever 1:** 64% of Premium/Enterprise email is Payments In and Payouts queries. These require payments data sharing, which needs InfoSec and ARB approval (target Q2). Without this approval, Lever 1 is worth +9.3 pp not +25.8 pp. Per-segment targets with and without data auth:
>
> | | Lever 1 uplift | Enterprise end-state | Premium end-state |
> |---|---|---|---|
> | With data auth | +25.8 pp | 78.8% | 78.2% |
> | Without data auth | +9.3 pp | 42.5% | 24.9% |

---

## Resolution Rate: Expected Dip, Then Recovery

> **The resolution rate dip in Q2–Q3 is expected, not a failure signal.** As Fin is deployed to email and Webform, the query mix gets harder. Standard and email contacts are more complex than self-selected chat users. Resolution rate will fall before it recovers. The 70% end-state target depends on: content coverage, payments data access for Fin, and feature gap closure — all tracked as separate workstreams.

| Involvement rate | Query mix | Assumed resolution rate | Overall AI resolution |
|---|---|---|---|
| 10–15% (today) | Chat only | 60–70% | ~8–11% |
| 25–35% | + Standard redirect | 50–60% | ~13–21% |
| 45–55% | + Webform migration | 45–55% | ~20–30% |
| 65–75% | + Email (Premium/Enterprise) | 40–55% | ~26–40% |
| 78–82% (no investment) | Full mix | 35–45% | ~30–45% |
| **78–82% (target)** | Full mix | **70%** | **~55–57%** |

---

## Per-Segment Targets (End 2026)

| Segment | % of contacts | Involvement baseline | Target | Primary lever |
|---|---|---|---|---|
| Standard | 34.6% | 16.9% | ~75% | L2: redirect email to Fin chat |
| Enterprise | 28.6% | 6.2% | ~79% | L1: Fin on email (requires data auth) |
| Premium | 20.7% | 4.0% | ~78% | L1: Fin on email (requires data auth) |

---

## Failure Conditions

This programme would be reassessed if:
1. Involvement rate cannot exceed 50% after Phases 1–3 are live, or
2. Fin involvement materially harms merchant experience (sustained CSAT decline or material commercial escalations).

In either case, lever rollout is paused and resolution investments are reviewed before pushing involvement further.
