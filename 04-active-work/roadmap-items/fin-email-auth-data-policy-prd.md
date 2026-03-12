---
confluence_space_key: MTC
confluence_parent_page_id: "8041431176"
confluence_page_id: "8105492559"
title: PRD: Fin on Email — Authentication & Data Access Policy
---
# PRD: Fin on Email — Authentication & Data Access Policy

**Author:** Charlie Wildish
**Date:** February 2026
**Approvers:** Director of Operations, Director of Operations Excellence, Security, Legal & Compliance
**Stage:** Solution Design
**Status:** Draft
**Last Updated:** February 2026
**Stakeholders:** Care Operations, Operational Excellence, Zendesk Admins, Engineering, Security, Legal & Compliance


| Field                | Value                                                                                                                                                                                                                                                                         |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2026 deliverable** | AI First Resolution Using Fin                                                                                                                                                                                                                                                 |
| **Strategic goal**   | Reduce cost of support                                                                                                                                                                                                                                                        |
| **Flywheel domain**  | 3. Fuel (data/knowledge for Fin) · 1. Input (email channel)                                                                                                                                                                                                                  |
| **How it fits**      | Fin today can do FAQ over email but not payment lookups because email is unauthenticated. This PRD defines auth and data access so Fin can safely return payment data on email, unlocking the largest lever for AI resolution on the email channel (payment-by-ID/Reference). |

---

## Executive Summary

Fin today only runs in the authenticated Dashboard; email is unauthenticated so Fin cannot do payment lookups there. At least 50% of email queries are payment-by-ID/Reference, the biggest lever for AI resolution. This PRD defines authentication and data access so Fin can safely return payment data on email. Fin's native verification-code flow removes the need for custom OTP; work is mainly config, policy, and integration with identification infrastructure.

Expected impact: material increase in AI resolution rate on email and lower cost per contact for Premium/Enterprise merchants who use email as their primary channel.

---

## Problem Space

**Problem statement:** Fin can answer FAQs over email but cannot perform payment lookups because it cannot verify who is asking. Roughly 50% of email volume is payment-by-ID/Reference; all of that currently goes to human agents. That gap is the main constraint on AI resolution on email.

**Who is affected:** Merchant ops teams (wait for agents instead of instant answer), CX (handle automatable volume), Care Ops and Op Ex (capped resolution), Premium and Enterprise merchants (email is their primary support channel).

**Evidence:**

- Email pilot and taxonomy data indicate at least 50% of email queries are payment-by-ID/Reference.
- Agents already return payment data over email; the marginal risk from Fin is scale and lack of human judgment, not a new data class.
- Standard tier is directed to Dashboard; Premium/Enterprise (bulk of volume) use email as primary channel.

**Competitive context:**

- **Who we compare to:** Other PSPs and support tooling that offer email support with data lookups (e.g. Stripe, Adyen support models).
- **How they address this:** Email support often combined with link-based or login-based verification before returning transaction data.
- **How we compare:** We lag on automated payment data over email; Fin on Dashboard already has full capability. Closing the gap on email aligns us with merchant expectation and reduces cost.
- **Implications:** Auth and data policy are must-haves; optional step-up (OTP) is a confirmatory tool, not a mandatory gate for standard payment data.

**Why now:** Email is the primary channel for Premium/Enterprise; half of queries are payment lookup and are automatable with verified identity. Identification work (domain mapping, Salesforce/Dashboard) is in flight; building on it now avoids delay and unlocks the largest email-resolution lever.

---

## Goals and Success Metrics

**Business goals:** Increase AI resolution rate on email to reduce cost per contact; maintain zero security incidents from email data disclosure; achieve 100% PCI DSS / GDPR policy compliance for data returned over email.

**Merchant goals:** Get immediate answers to payment-by-ID/Reference queries over email without waiting for a human agent; retain ability to use email as primary support channel (Premium/Enterprise).

**Non-goals:** Fin Dashboard behaviour (Level 3 unchanged); Standard tier email entitlement; Consumer/B2C; voice/chat auth; returning PAN or consumer PII over email; mandating Dashboard for ops.

**Success metrics:**


| Metric                                                                         | Why it matters                                    | Baseline                                                                                                             | Target                                                                          | Source                                                                                   |
| -------------------------------------------------------------------------------- | --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| AI resolution rate on email channel                                            | Primary outcome for cost reduction                | TBC — establish by Q3 2026 via resolution rate instrumentation (owner: Product Data Scientist)                      | Informed by 50%+ addressable query volume; target set once baseline established | `fin_email_data_returned` events; resolution rate dashboard                              |
| % of payment-by-ID/Reference queries handled by Fin without human intervention | Direct measure of policy and auth success         | ~0% (Fin on email not yet live)                                                                                      | TBC — establish by Q3 2026 once Fin on email live (owner: Charlie Wildish)     | `fin_email_ticket_classified` and `fin_email_data_returned` events; 6 months post-launch |
| % of payment queries escalated due to unidentified org (Level 0)               | Drives domain mapping and identification coverage | TBC — establish from`fin_auth_level` tagging in Phase 1 (owner: Product Data Scientist; deadline: Phase 1 complete) | Decreasing quarter-on-quarter                                                   | `fin_email_escalated` events tagged with reason; 3 months post-launch                    |
| Security incidents attributable to email data disclosure                       | Compliance and trust                              | 0                                                                                                                    | 0 (maintained)                                                                  | Security incident log; ongoing                                                           |
| PCI DSS / GDPR policy compliance                                               | Legal and regulatory                              | N/A (policy not yet approved)                                                                                        | 100%; no prohibited data returned over email                                    | Policy sign-off; audit log; at launch and ongoing                                        |

---

## Customer Segments & Needs

**Customer segment(s):** Premium and Enterprise merchants (and their ops teams) who use email as their primary support channel. Secondary: Care Ops and Op Ex (need Fin to handle more email volume safely); CX agents (need clear audit trail when reviewing Fin-handled tickets).

**User stories / jobs-to-be-done:**

- **Merchant ops — payment lookup:** As a merchant payment ops team member who emails support with a Payment ID or Reference, I want Fin to look up that payment and return status and outcome, so that I get an immediate answer without waiting for a human agent.
- **Product team/CX agent — review:** As a CX agent reviewing a ticket Fin handled on email, I want to see what authentication level was established and what data Fin returned, so that I can verify correct handling and pick up escalations with full context.

---

## Proposed Solution & Scope

**Solution overview:** We define a formal data access policy (Security and Legal sign-off) and an identification-level model (Level 0–3) so Fin can safely return payment data on email. Org identification (Salesforce, Dashboard, domain mapping) is the gate for payment data, not mandatory OTP. Fin exclusion rules (e.g. @checkout.com on CC, high CC count) run before any Fin involvement. Fin's native verification code is available as an optional confirmation tool. Every payment response includes a Dashboard deep link; no PAN or consumer PII is ever returned over email.

**In scope:**

- Formal data access policy approved by Security and Legal & Compliance.
- Identification level assessment on every inbound email ticket (Level 0–3).
- Fin exclusion rules (Zendesk triggers): no Fin involvement when @checkout.com is CC'd or more than 2 people are CC'd.
- Payment data return at Level 1 and Level 2 (org-identified) with data minimisation and Dashboard deep link.
- Hard blocks: no PANs, consumer PII, or cardholder-identifying data over email; no data for Payment IDs that do not belong to the identified org.
- Zendesk ticket logging of identification level and data returned for agent review.
- Optional email verification (step-up) as confirmatory tool, not mandatory gate for standard payment data.

**Out of scope:**

- Fin Dashboard behaviour (Level 3 unchanged).
- Standard tier email entitlement.
- Consumer/B2C; voice/chat auth.
- PAN/consumer PII return (hard limits).
- Mandating Dashboard for ops (would help Level 2 but out of scope).

**How it works — Fin decision flow:**

1. **Exclusion rules (Fin stands down):** Evaluated at ticket creation by Fin. If @checkout.com on CC or more than 2 CC'd → `fin_eligible = false` → human only.
2. **Identification level:** If `fin_eligible = true`, classifier sets Level 0–3. Level 0 → Fin offers FAQ and tries to triage by asking for specific data to help without a lookup; merchant can ask to escalate to human. No payment data at Level 0. Level 1+ → data lookup allowed within policy.
3. **Hard limits:** No PAN, consumer PII, or data for Payment IDs not belonging to the identified org; cross-merchant data never.

**Proposed Identification levels:**


| Level                  | How established                 | Payment data?                                             |
| ------------------------ | --------------------------------- | ----------------------------------------------------------- |
| 0 — Unidentified      | No record match anywhere        | No; Fin triages; merchant can request escalation to human |
| 1 — Domain-mapped     | Email domain matches org record | Yes; status and outcome for provided Payment ID           |
| 2 — Known contact     | Salesforce or Dashboard match   | Yes; status, outcome, dispute data                        |
| 3 — Dashboard session | Authenticated Dashboard login   | Yes; full Fin capability (unchanged by this PRD)          |

**Data classification (summary):** Documentation/FAQs at all levels. Org config and transaction status/outcome at Level 1+. Consumer PII and PAN never over email. Full data classification table and edge cases are in the Appendix.

**Email verification (optional):** Fin's native verification code is available for confirmatory use (e.g. borderline org identification, Security-mandated step-up for specific data types). Not a mandatory gate for standard payment data at Level 1 or 2. If not completed or timed out, Fin routes to human with context.

> Alternatives evaluated: see Appendix.

---

## Requirements

Prioritisation: Must have (P0), Should have (P1), Nice to have (P2).

**Requirements by audience / domain**


| Domain                    | Requirement IDs                               | Purpose                                                                                                                                                                                                |
| --------------------------- | ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Merchant**              | FR-3, FR-5, FR-6, FR-8, FR-12, NFR-4, NFR-5   | Payment data and deep link; triage and escalation when unauthenticated; clear "cannot authenticate" messaging; data minimisation; ticket not blocked if OTP fails.                                     |
| **Care Ops / CX**         | FR-2, FR-6, FR-7, FR-9, NFR-5                 | Exclusion rules so Fin stands down when appropriate; escalation path and ticket context; ticket logging and auth-level tag for review and reporting; configurable policy; OTP failure routes to agent. |
| **Analytics & Reporting** | FR-0, FR-7, FR-10, FR-11, NFR-3               | Instrumentation; auth-level tagging for reporting; audit log queryable for compliance and trends; step-up completion/drop-off (P2); logging of every data return.                                      |
| **Security & Compliance** | FR-2, FR-4, FR-10, NFR-1, NFR-2, NFR-3, NFR-4 | Exclusion rules; no PAN/PII; audit log; Security review of OTP; Legal sign-off; data minimisation. Policy approval is a gate (see Rollout Plan Phase 1 entry criteria).                                |
| **Product / Platform**    | FR-0, FR-1, FR-9                              | Instrumentation; identification classifier; configurable data policy rules (Zendesk admins / Engineering).                                                                                             |

### Functional requirements

> **Gate vs requirement:** If a requirement depends on an open decision that has not been made, do not write it as a functional requirement. Capture it as an Open Question and reference it in the Rollout phase entry criteria. Promote it to the FR list only once the decision is made.

**FR-0 — Instrumentation (P0):** Key events (`fin_email_ticket_classified`, `fin_email_data_returned`, `fin_email_escalated`) must be implemented, validated in staging, and confirmed firing before Phase 1 go-live.
*Acceptance criteria:* Given Phase 1 launch, when Engineering and Product Data Scientist validate in staging, then all listed events fire correctly with correct fields; no Phase 1 go-live until confirmed.

**FR-1:** Every inbound email ticket receives an identification level (0–3) from Salesforce, Dashboard, and domain mapping lookup.
*Acceptance criteria:* Given a new email ticket, when the classifier runs, then the ticket is tagged with `fin_auth_level` (0–3). Level 0 = no match; Level 1 = domain-mapped; Level 2 = known contact; Level 3 = N/A for email (Dashboard only).

**FR-2:** Fin does not respond to any ticket where (a) a @checkout.com address is CC'd, or (b) more than 2 people are CC'd.
*Acceptance criteria:* Given an email ticket, when a Zendesk trigger evaluates CC list, then if either condition holds, `fin_eligible = false` and Fin is not assigned. These rules apply to all Fin email involvement (including FAQ).

**FR-3:** Fin may return transaction status and outcome data to Level 1 and Level 2 requesters; OTP is optional identity confirmation, not a mandatory blocker.
*Acceptance criteria:* Given Level 1 or Level 2 and a payment-by-ID/Reference query, when Fin looks up the payment for the identified org, then Fin returns summary (status, outcome, plain-language explanation) and a Dashboard deep link, without requiring step-up unless policy explicitly requires it for that data type.

**FR-4:** Fin never returns PANs, consumer personal data, or cardholder-identifying information over email at any identification level.
*Acceptance criteria:* Given any request, when the response would include PAN or consumer PII, then Fin declines and routes to human. No such data appears in any Fin email response.

**FR-5:** Every payment lookup response includes a direct deep link to the payment record in the Merchant Dashboard.
*Acceptance criteria:* Given a successful payment lookup, when Fin responds, then the email contains a stable URL to the payment record (e.g. dashboard.checkout.com/payments/{id}). Deep link format TBC with Dashboard Engineering.

**FR-6:** Fin escalates to a human agent when org cannot be identified (Level 0) for a data query, or when the query falls outside the data policy (e.g. wrong org, consumer PII requested).
*Acceptance criteria:* Given Level 0 and a payment data query, when Fin evaluates, then Fin first tries to triage by asking for specific data to help solve without a lookup (e.g. clarifying the issue); the merchant can ask to escalate if that is not helping, and Fin then routes to a human agent. Fin does not return payment data at Level 0. Given a Payment ID that does not belong to the identified org, when Fin checks, then Fin declines and routes to human.

**FR-7:** Zendesk ticket records identification level and data returned for agent review.
*Acceptance criteria:* Given a Fin-handled email ticket, when an agent opens it, then the ticket shows authentication level achieved and what data Fin returned (conversation log); agent can see whether step-up was completed or timed out. Tickets are tagged with authentication level for reporting use.

**FR-8 (P1):** When Fin cannot authenticate the requester (Level 0), Fin communicates that we cannot authenticate their request (e.g. "We couldn't verify your account for this request"). Where applicable, Fin may also explain why certain data cannot be returned at other levels.

**FR-9 (P1):** Data policy rules are configurable (Zendesk admins or Engineering can update without code deployment where possible).

**FR-10 (P1):** Audit log of all data returned over email by Fin is queryable for compliance review.

**FR-11 (P2):** Step-up completion rate and drop-off analysis are tracked to optimise the flow.

**FR-12 (P2):** Settlement status lookup and balance lookup (subject to API access and Security/Legal policy approval; shared with Fin on Dashboard).

### Non-functional requirements

**NFR-1 — Security:** Fin's native email verification flow (expiry, single-use, delivery failure) is reviewed and approved by Security before use to gate data access.

**NFR-2 — Compliance:** Data policy is formally signed off by Legal & Compliance. No data-return capability goes live without this approval. Policy is reviewed at least annually or when regulations change (PCI DSS, GDPR, PSD3).

**NFR-3 —Auditability:** Every instance of data returned by Fin over email is logged with timestamp, ticket ID, authentication level, and data type returned. Logs retained per applicable data retention policy.

**NFR-4 — Privacy:** Fin responses apply data minimisation (minimum data necessary to resolve the query).

**NFR-5 — Availability:** If OTP delivery fails, Fin routes to human agent; the ticket is not blocked silently.

---

## Instrumentation and Monitoring

**Key events to instrument (suggested tags but should be Fin native):**

- `fin_email_ticket_classified`: Ticket ID, `fin_eligible`, `fin_auth_level`, timestamp. Captures outcome of exclusion and identification.
- `fin_email_data_returned`: Ticket ID, timestamp, auth level, data type (e.g. payment status, org config), payment ID if applicable. Used for audit and compliance.
- `fin_email_escalated`: Ticket ID, reason (Level 0, policy limit, wrong org, step-up timeout, etc.), timestamp.
- `fin_email_step_up_offered` / `fin_email_step_up_completed` / `fin_email_step_up_timed_out`: Ticket ID, timestamp. For P2 completion and drop-off analysis.

**Event properties (suggested tags):**

- `ticket_id`: Zendesk ticket ID.
- `fin_auth_level`: 0, 1, 2 (3 is Dashboard only).
- `fin_eligible`: boolean.
- `data_type`: e.g. payment_status, org_config, settlement_status (when in scope).

**Internal dashboards and monitoring:**

- Audit log view: queryable by date, ticket ID, auth level, data type; used by Product/Ops.
- Operational view: volume of Fin-handled vs escalated email tickets by auth level; step-up offer/completion/timeout rates (when P2 instrumented).

**Validation approach:**

- Staging tests: trigger exclusion and identification rules; verify ticket fields and Fin behaviour. Negative tests: Fin correctly declines out-of-policy and wrong-org requests.
- Post-launch: spot-check audit log entries against Zendesk tickets; data quality checks for required fields.
- Silent failure detection: daily count of `fin_email_ticket_classified` events — if drops >20% from 7-day average, alert fires to Engineering. Null-field alert on `fin_auth_level` if null rate >5%. Owner: Product Data Scientist; cadence: daily automated check.

---

## Risks, Assumptions, and Open Questions

**Risks:**

- **Fin returns out-of-policy data due to misconfiguration.** Mitigation: Policy enforcement as P0; negative UAT cases before launch; audit log for detection.
- **Fin returns transaction data to an unrelated person on the same merchant domain.** Mitigation: Payment ID must be provided by requester; data minimisation; consistent with agent baseline.
- **Deprovisioned account on mapped domain receives step-up email.** Mitigation: Step-up requires reply from inbox; deprovisioned account cannot reply; Fin times out and routes to human.
- **Compliance requirements change (e.g. PCI DSS v4, PSD3).** Mitigation: Annual policy review; Legal & Compliance as standing stakeholder.
- **Domain-mapped user disputes data access decision.** Mitigation: Clear Fin messaging on auth level; escalation to human always available.

**Key assumptions:**

- Agents' existing practice of returning payment data over email is under a legal basis (e.g. merchant DPA) that extends to Fin returning the same data automatically. *Validation: Legal & Compliance confirmation before launch.*
- Domain mapping and Salesforce/Dashboard identification will be available to tag tickets with auth level. *Validation: Dependency on Zendesk org domain mapping and identification work; OTP step-up partially compensates if delayed.*
- Fin's native email verification code behaviour (expiry, single-use, delivery failure) meets Security requirements when used to gate data. *Validation: Security review of Fin implementation before use for data gating.*
- Dashboard deep link URLs exist for individual payment records and are stable. *Validation: Confirm with Dashboard Engineering.*

**Open questions:**

- Data policy approval: What is the approved scope of Checkout.com payments data Fin is permitted to query (transaction fields, dispute fields, account config)? **GATE — no Phase 1 completion without this.** *(Owner: Security / Legal & Compliance + Engineering; target: end Q2 2026)*
- Settlement status and balance API access are also required for Fin over chat. Should policy approval and API scoping be driven by this PRD and shared? *(Owner: Charlie Wildish + Engineering; recommend this PRD as driver to avoid duplicate approval effort)*
- Should the data policy differ by merchant tier (e.g. Enterprise treated as higher-trust at Level 1)? *(Owner: Security + Care Leadership)*
- Does the same legal basis that covers agents returning payment data extend to Fin returning it automatically? *(Owner: Legal & Compliance; formal confirmation before launch)*
- What is the expiry and single-use behaviour of Fin's native email verification code, and does it meet Security's requirements for gating data access? *(Owner: Security + Intercom/Fin platform team)*

---

## Rollout Plan

**Rollout approach:** Phased by policy approval, then auth classifier, then Fin config and enforcement, then limited rollout (Premium/Enterprise) and full rollout. No data return until Security and Legal & Compliance approve the policy. Rollback: disable Fin data return on email (FAQ-only) via config.

### Phase 1: Policy and classifier - Q2

**Purpose:** Achieve policy sign-off and deploy the identification classifier so tickets are tagged with auth level.

**Entry criteria:**

- Technical: Draft data classification policy and OTP flow spec; identification classifier built and deployed (Salesforce + Dashboard + domain mapping).
- Operational: None.
- Business: **GATE — Data policy approved by Security and Legal & Compliance.** This is a hard go/no-go gate; no Phase 1 completion without this sign-off. Owner: Security + Legal & Compliance; target: end Q2 2026.

**Success criteria:**

- Policy document signed off; classifier sets `fin_auth_level` and `fin_eligible` on email tickets in target environment.

**Timeline:** Policy 2–3 weeks; classifier timeline TBC with Engineering.

### Phase 2: Fin configuration and enforcement - Q3

**Purpose:** Configure Fin verification flow and data policy rules; complete Security review of native OTP implementation; validate negative cases.

**Entry criteria:**

- Technical: Classifier live; Fin config reads `fin_eligible` and `fin_auth_level`; data policy rules configured.
- Operational: Security review of Fin native OTP implementation complete.
- Business: Policy approved (from Phase 1).

**Success criteria:**

- Fin returns data only within policy at Level 1/2; Fin correctly declines Level 0 data queries, wrong-org lookups, and out-of-policy requests in UAT. Audit logging verified.

**Timeline:** 1–2 days config + Security review; UAT with Care Operations.

### Phase 3: Limited rollout then general availability - Q3

**Purpose:** Validate in production with a controlled set of email tickets (Premium/Enterprise merchants only).

**Entry criteria:**

- Technical: All P0 requirements delivered; audit log and monitoring in place.
- Operational: Agent guidance published (what Fin handles vs routes to human); merchant-facing guidance on verification step if used.
- Business: Legal/compliance approvals complete (from Phase 1).

**Success criteria:**

- Limited: No P1 incidents; auth completion and escalation patterns within expectations. GA: Full rollout; ongoing audit log review cadence established.

**Timeline:** Limited rollout TBC; full rollout after success criteria met.

**Definition of Done:**

- Technical: All P0 requirements delivered and tested; exclusion and identification rules working; audit log capturing required events; no data return without policy approval.
- Operational: Support trained; runbooks/agent guidance and merchant guidance published; monitoring and alerting configured.
- Business: Data policy and OTP flow approved by Security and Legal & Compliance.

**Product dependencies:**


| Dependency                                         | Owner                        | Status                         | Risk if delayed                      |
| ---------------------------------------------------- | ------------------------------ | -------------------------------- | -------------------------------------- |
| Data policy approval (Security)                    | Security                     | Not started                    | Blocks all data return               |
| Data policy approval (Legal & Compliance)          | Legal & Compliance           | Not started                    | Blocks all data return               |
| Salesforce + Dashboard identification classifier   | Engineering                  | In flight (domain mapping PRD) | Blocks auth level tagging            |
| Fin native email verification flow                 | Fin/Intercom (config)        | Existing capability            | Security review required before use  |
| Fin data policy enforcement config                 | Zendesk Admins / Engineering | Not started                    | Blocks safe data return              |
| Payments API read access scoped for Fin            | Engineering                  | TBC                            | Blocks transaction lookups           |
| Dashboard deep link URL format for payment records | Dashboard Engineering        | TBC                            | Blocks standard response pattern     |
| Settlement/Balance API (P2)                        | Engineering                  | TBC                            | Blocks P2 settlement/balance lookups |

**Go-to-market:**

- **Operational enablement:** Care Operations and Op Ex briefed on data policy, auth levels, and when Fin handles vs escalates. Agent guidance and internal knowledge updated. Runbooks for handling escalations and audit requests.
- **Merchant communications:** No broad merchant launch comms required for policy and auth; optional step-up flow explained in help content or in-product if step-up is used.
- **Sales enablement:** Not required for this initiative.
- **Documentation:** Data classification policy (internal); agent guidance; merchant-facing guidance on verification step if applicable. Owner: Charlie Wildish with Knowledge Manager and Zendesk Admins.

---

## Appendix

**Alternatives Considered:**

- **Option 1 — Mandatory OTP for all payment data on email:** Require step-up verification before any payment data. Rejected: agents do not require OTP today; org identification is the operational baseline. Mandatory OTP would add friction and reduce adoption without a clear compliance requirement.
- **Option 2 — No payment data on email; keep email FAQ-only:** No change to current state. Rejected: leaves the largest lever (payment-by-ID/Reference) unused and defers cost reduction and merchant benefit.
- **Why we chose this approach:** Align with current agent practice (org identification as gate), use optional step-up where Security or compliance need it, and minimise email payload (status, outcome, Dashboard link only) to control risk while unlocking AI resolution on email.

**Strategy and research:**

- `01-knowledge-base/processes/known-challenges.md` — Email authentication gap and AI resolution rate constraint
- `01-knowledge-base/processes/ai-agent-operations.md` — Fin AI Agent operations, email pilot findings
- `04-active-work/roadmap-items/zendesk-org-domain-mapping-prd.md` — Domain mapping and identification (classifier dependency)

**Technical and commercial:**

- Decision flow (exclusion → identification → data policy) and full data classification table are in the original PRD version; summarised in Design and User Experience above.
- Zendesk: ticket fields `fin_eligible`, `fin_auth_level`; triggers for exclusion (Checkout.com CC, high CC count) and identification classifier; step-up verified trigger.

**Detailed requirements and edge cases:**

- Level 0: Fin triages (FAQ, asks for specific data to help without lookup); merchant can ask to escalate; no payment data.
- Domain-mapped (Level 1) transaction data: Fin returns status/outcome for provided Payment ID; no step-up required.
- Shared inbox: Accepted baseline; data minimisation (status, outcome, no consumer PII).
- Deprovisioned email: Step-up times out; Fin routes to human; no data returned.
- Multiple Payment IDs/References: Process each; omit or escalate if any result would include consumer PII or wrong org.
- Payment ID belongs to different merchant: Fin declines; route to human.
- Reference matches multiple payments: Summary for all; if large, summarise and suggest refinement or Dashboard.
- Query requires consumer PII or PAN: Fin declines at any level; route to human with explanation.
- @checkout.com CC'd or >2 CC'd: Fin does not respond; ticket routes to human.

**Data classification table (reference):**


| Data type                             | L0  | L1  | L2  | L3  | Hard limit            |
| --------------------------------------- | ----- | ----- | ----- | ----- | ----------------------- |
| Documentation / FAQs                  | Yes | Yes | Yes | Yes | —                    |
| Org config status                     | No  | Yes | Yes | Yes | —                    |
| Transaction status / outcome (masked) | No  | Yes | Yes | Yes | —                    |
| Dispute / chargeback status           | No  | Yes | Yes | Yes | —                    |
| Consumer PII / PAN                    | No  | No  | No  | No  | Never over email      |
| Settlement status / Balance (P2)      | No  | Yes | Yes | Yes | Requires API + policy |

**Timeline (milestones):**


| Milestone                                       | Owner                         | Status |
| ------------------------------------------------- | ------------------------------- | -------- |
| PRD complete                                    | Charlie Wildish               | Draft  |
| Open questions resolved                         | Multiple                      | TBC    |
| Data policy approved                            | Security / Legal & Compliance | TBC    |
| Auth classifier built and deployed              | Engineering                   | TBC    |
| Fin verification configured + Security reviewed | Zendesk Admins / Security     | TBC    |
| Fin policy enforcement configured               | Zendesk Admins / Engineering  | TBC    |
| UAT complete                                    | Care Operations               | TBC    |
| Limited rollout (Premium/Enterprise)            | Care Operations / Engineering | TBC    |
| Full rollout                                    | Care Operations               | TBC    |
