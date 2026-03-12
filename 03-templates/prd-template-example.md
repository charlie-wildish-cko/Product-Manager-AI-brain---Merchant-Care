# PRD Template Example: Annotated Sections

> This is a **partial example**, not a full PRD. It shows only the four sections most commonly done poorly, using a Care & Support scenario. Each section includes an italicised annotation explaining why it's structured this way. Use [prd-template.md](prd-template.md) for the full template.
>
> Source scenario: Fin Involvement Rate (simplified for illustration).

---

## Section 1: Roadmap alignment block

*The block must be filled before writing any other section, then the TODO line deleted. All four fields must be specific — no placeholders. "How it fits" must name the mechanism, not just restate the goal.*

| Field | Value |
|-------|-------|
| **2026 deliverable** | AI First Resolution Using Fin |
| **Strategic goal** | Reduce cost of support |
| **Flywheel domain** | 1. Input (channel mix) · 2. Orchestration (triage, Fin as first touchpoint) |
| **How it fits** | Today Fin is Dashboard chat only (9.2% involvement). This PRD defines five channel levers to reach 80% Fin involvement by end 2026, pairing involvement growth with resolution investments so cost per contact falls as quality is maintained. |

*Notice: the TODO line is gone. The "How it fits" field names the mechanism (five levers, specific current baseline, specific target) rather than saying "supports our AI strategy". Leadership can assess strategic alignment from this table alone before reading the rest.*

---

## Section 2: Success metrics table

*Every Baseline cell must contain a real value or "TBC — establish by [date]". A bare TBC is not acceptable. The Source column must name the specific data source so anyone can verify the number. Targets should be time-bound.*

> **Rule:** Every Baseline cell must contain a value or "TBC — establish by [date]". A bare TBC is not acceptable.

| Metric | Why it matters | Baseline | Target | Source |
|--------|---------------|----------|--------|--------|
| Fin involvement rate (all segments) | Primary outcome; path to cost reduction | 9.2% (last 6m, source: `support_contacts_flat_table_2025_last_6m.csv`) | 80% by end 2026 | Support contacts flat table and live equivalent; definition locked with Care Ops by Q1 2026 |
| AI resolution rate (at 80% involvement) | Quality of Fin resolution; overall AI resolution = involvement × resolution | ~70% (modelled target; no live baseline yet — establish by Q2 2026 via resolution rate instrumentation) | 70% at 80% involvement | Fin resolution data; definition and instrumentation owned by Content/Fin and Product Data Science |
| Structurally unreachable % | Sets ceiling; 100% involvement is not achievable | 18.7% (Email Internal 9.2% + Other 9.5%; last 6m) | Reported; ceiling ~81% | `fin_unreachable` tag; denominator unchanged |

*Notice: no row has a bare "TBC". The second row has a conditional baseline with a deadline for establishing a live value. The third row has a real number with its components broken out. Anyone reading this can verify the targets, data sources, and when unknowns will be resolved.*

---

## Section 3: Requirements — gate vs requirement

*Pending decisions are NOT functional requirements. If a requirement depends on a decision that has not been made, it goes to Open Questions. It is promoted to the FR list only once the decision is made. FR-0 (Instrumentation) is always P0 and always present.*

> **Gate vs requirement:** If a requirement depends on an open decision that has not been made, do not write it as a functional requirement. Capture it as an Open Question and reference it in the Rollout phase entry criteria. Promote it to the FR list only once the decision is made.

**Requirements by audience / domain**

| Domain | Requirement IDs | Purpose |
|--------|-----------------|---------|
| **Care Ops / CX** | FR-0, FR-1, FR-2 | Instrumentation and reporting; Standard redirect and runbooks |
| **Merchant** | FR-3 | Fin as first touchpoint for email (Premium/Enterprise) |
| **Analytics & Reporting** | FR-0, NFR-1 | Involvement rate by segment/channel; unreachable ceiling |

### Functional requirements

| ID | Area | Requirement | Priority |
|----|------|-------------|----------|
| **FR-0** | **Instrumentation** | **Key events defined in the Instrumentation section must be implemented, validated in staging, and confirmed firing before Phase 1 go-live.** *AC: All listed events fire correctly in staging; validated by Data Scientist and Engineering before Phase 1 entry.* | **P0** |
| FR-1 | Involvement reporting | Fin involvement rate measurable by merchant segment and channel before levers launch. *AC: Metric defined (Fin-touched / total contacts); denominator = all support contacts; definition locked with Care Ops; Zendesk/Intercom reporting in place.* | P0 |
| FR-2 | Standard enforcement | Standard merchants redirected from email to Fin Dashboard. *AC: Standard email no longer accepted; auto-redirect in place; runbook and redirect message agreed with Care Ops before go-live.* | P0 |
| FR-3 | Fin on email | Fin as first responder on Email (Merchant) for Premium and Enterprise. *AC: Fin invoked on eligible tickets; exclusion rules applied; resolution attempted before human ticket; involvement on email tracked by segment.* | P1 |

**Open Questions** *(decisions needed before these can become requirements)*

- **Webform fields and routing spec**: Fin must replicate Webform behaviour exactly. Spec sign-off required from Zendesk Admins before FR-4 (Webform migration) can be written. [Owner: Zendesk Admins; deadline: end Q1 2026]
- **Policy for payments data over email**: Phase 3 gated on InfoSec and ARB approval. Until approved, Fin on email is limited to non-Payments queries. [Owner: InfoSec / ARB; deadline: end Q2 2026]

*Notice: the two open questions above would appear as "FR-4: Policy approved" and "FR-5: Webform spec signed off" in a poorly-written PRD. Here they are correctly placed as gates. FR-4 and FR-5 will be written when those decisions are made. The Rollout Plan's Phase 3 entry criteria reference these gates explicitly.*

---

## Section 4: Instrumentation and monitoring

*Always name the mandatory Care events explicitly. Always include a silent failure detection bullet with a named owner. Events must use field names from the metric definitions doc.*

**Key events to instrument:**

- `contact_created`: `channel` (email_merchant / webform / fin_chat / email_internal / other), `case_type`, `issue_type`, `fin_involved` (boolean), `merchant_segment` (standard / enterprise / premium) — field names from [support_contacts_flat_table_2025_metric_definitions.md](../01-knowledge-base/metrics/support_contacts_flat_table_2025_metric_definitions.md)
- `contact_resolved`: `resolved_by` (fin / agent / merchant_self_serve), `handle_time_seconds`, `fin_involved`
- `fin_unreachable_tagged`: fires when a contact is tagged `fin_unreachable` (Email Internal, Other channel); tracks ceiling

**Internal dashboards and monitoring:**

- Fin involvement rate by segment and channel: weekly cadence; owner Care Ops / Charlie Wildish
- Unreachable % (ceiling): weekly alongside involvement; confirms ceiling ~81%

**Validation approach:**

- Pre-launch: validate `fin_involved` and `fin_unreachable` tags fire correctly in staging using test contacts across each channel; compare event counts to expected channel volume
- Silent failure detection: daily row count alert on `contact_created` events — if daily count drops >20% from 7-day average, alert fires to Engineering and Data Scientist. Null-field alert on `fin_involved` if null rate >5%. Owner: Product Data Scientist; cadence: daily automated check.

*Notice: field names are specific and traceable to the metric definitions doc. Silent failure detection has a named owner, a threshold, and a cadence — not just "monitor for issues".*

---

*For the full PRD template, see [prd-template.md](prd-template.md). For the draft-critique-refine workflow, see [../02-workflows/draft-critique-refine.md](../02-workflows/draft-critique-refine.md).*
