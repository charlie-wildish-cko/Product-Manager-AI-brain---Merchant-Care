# SAR / DPO Keyword Detection for Zendesk Routing

**Deliverable**: Reduce Agent Effort on Dispatch and Email Clean Up Rules (Q2 2026)
**Flywheel**: Agent Experience + Governance
**Goal served**: Reduce cost of support (removes manual DPO triage from agent workload); supports existing DSAR referral process ([data-subject-access-requests-dsar.md](../../01-knowledge-base/processes/Care%20Agent%20SOPs/zendesk-kb/complaints/data-subject-access-requests-dsar.md)), which requires agents to identify these tickets manually today.

---

## Problem

Merchant Care has no AI classification for SAR/DPO requests. Agents identify them manually and forward to dpo@checkout.com via side conversation. Misses create regulatory risk (UK GDPR Article 15 responses are time-boxed) and delay routing. Keyword matching in a Zendesk trigger gives a first-pass safety net until proper classification exists.

---

## Tier 1 — High-confidence phrases (auto-route to DPO, single match sufficient)

These phrases are near-exclusively used in genuine SAR/DPO correspondence, including from law firms and claims-management companies.

- "subject access request"
- "data subject access request"
- "DSAR"
- "Article 15" (paired with GDPR — see Tier 3 combination logic)
- "data protection officer"
- "dpo@checkout.com"
- "right of access" (GDPR)
- "exercise my data protection rights"
- "exercise my rights under" + "GDPR" / "Data Protection Act"
- "ICO complaint" / "lodge a complaint with the ICO" / "report you to the ICO"
- "Data Protection Act 2018"

## Tier 2 — Medium-confidence terms (require combination, see logic below)

Common in SAR language but also appear in unrelated compliance, KYC, or product questions.

- "personal data"
- "controller" / "data controller" / "joint controller"
- "processing my data" / "data you hold on me" / "data you hold about me"
- "GDPR"
- "UK GDPR"
- "erasure" / "right to be forgotten" (Article 17 — adjacent right, same DPO routing per SOP)
- "rectification" (Article 16)
- "data portability" (Article 20)
- "object to processing" / "object to the processing" (Article 21)
- "preserve all documents" / "preserve all records" (common in escalation/legal-threat SARs)
- "statutory period" / "calendar month" (paired with "request" or "GDPR")

## Tier 3 — Combination logic

Zendesk trigger condition, in order of precedence:

1. **Auto-route to DPO, tag `sar_dpo_auto`**: Subject or Description contains **any Tier 1 phrase**.
2. **Route to DPO review queue, tag `sar_dpo_review`** (human confirms before forwarding): Subject or Description contains **two or more Tier 2 terms**, OR one Tier 2 term **and** a UK/EU jurisdiction reference ("UK GDPR", "ICO", "Data Protection Act").
3. **No action**: single Tier 2 term with no jurisdiction reference (likely a general privacy/ToS question, not a rights request).

This mirrors the two-tier structure already used for domain-based routing in [dispatch-email-cleanup/scoping.md](../prds/dispatch-email-cleanup/scoping.md) (auto-close vs. review), so it should slot into the same trigger set rather than requiring new infrastructure.

## Exclusions / false-positive guards

- Exclude tickets already tagged with an existing DPO/legal macro to avoid re-routing loops.
- Exclude internal-form submissions (Commercial/internal tickets) — these are agents referencing GDPR for merchant compliance questions, not data subjects exercising rights.
- "personal data" alone frequently appears in KYC/onboarding tickets ("please update my personal data") — never auto-route on this term alone.

## Source examples used to derive this list

Two real tickets provided by Charlie (2026-07-03): both are follow-up/escalation SARs referencing a prior request, Article 15 UK GDPR, ICO complaint threats, and named Checkout entities. Both would hit Tier 1 (multiple phrases each) — validates that Tier 1 alone catches escalation-stage SARs; Tier 2/3 logic is needed to catch first-contact SARs that may be less formally worded.

---

## Open questions

1. Confirm with the DPO team (per open question already logged in [dispatch-email-cleanup/scoping.md](../prds/dispatch-email-cleanup/scoping.md)) whether auto-routed tickets should also get an auto-reply to the requester, or silent internal routing only.
2. Confirm whether `Article 15` alone (without "GDPR" nearby) should be Tier 1 or Tier 3 — could false-positive on unrelated legal citations. Recommend requiring "Article 15" AND "GDPR" co-occurrence.
3. Should Tier 2 erasure/rectification/portability requests use the same DPO routing as SARs, or a separate queue? SOP currently only names DSARs explicitly.

## Next step

Hand to Zendesk config owner to build as a trigger (condition: Subject/Description contains at least one of Tier 1 list) alongside the Q2 dispatch/email clean-up work. Recommend a 2-week shadow period (tag only, no auto-route) to measure false-positive rate before enabling auto-routing.
