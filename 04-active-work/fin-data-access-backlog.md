# Fin Data Access Backlog

> **Deliverable**: AI First Resolution Using Fin (Continuous)
> **Flywheel**: Handle + Fuel
> **Strategic goal**: Reduce cost of support
> **Metrics**: Fin involvement rate · AI resolution rate · Cost per contact
> **Owner**: Charlie Wildish
> **Last updated**: March 2026

---

## Purpose

Fin's resolution rate is constrained by the data it can access. Today, Fin can answer questions using knowledge articles and documentation. For a large share of contacts — particularly in Payments, Account Management, and Funds & Fees — merchants need a specific answer about their account, not a generic one.

This backlog tracks the data sources Fin should be able to access (via API or MCP) to answer data-dependent queries without human escalation. Each entry maps to a contact type from the support taxonomy and is prioritised by contact volume × data availability.

**How data access works in Fin**: Data is surfaced through **Procedures** — Fin's equivalent of SOPs. A Procedure defines the steps Fin follows to resolve a specific contact type, including which API calls to make, what data to retrieve, and how to present the result. Data sources in this backlog are accessed via Procedures, not by Fin making ad hoc API calls. Each entry should eventually map to one or more Procedures. See also: `2026 deliverables.md` → Improve Fin Resolution Through Procedures (Q2).

**Also relevant for**: Agent Consultant (data retrieval capability) — entries marked with ✦ are shared-value items where the same integration benefits both Fin and agents. Engineering should build these as shared data services rather than duplicating integration work.

**Excluded from this backlog**: Login & Access is the highest-volume single issue type (281 contacts / 6 months) but is primarily an account access problem — MFA resets, SSO misconfigurations, locked accounts. Data access alone does not resolve these. A separate entry covers the User Management API as a lookup tool to identify the required remediation action, but full resolution requires process and tooling changes beyond data access.

---

## Entry Template

| Field | Description |
|---|---|
| **Data source** | System or API name |
| **Query types enabled** | What merchant questions this allows Fin to answer |
| **Contact types** | Taxonomy case type / issue type this addresses |
| **Contact volume** | Contacts per 6 months from actuals (flat table, last 6m) |
| **Integration method** | API / MCP / Other |
| **Access model** | Read-only / Action (with HITL) |
| **Data availability** | Confirmed live / Not confirmed / H2 2026 / Q4 2026 |
| **Complexity** | Low / Medium / High |
| **Status** | Proposed / Scoped / In delivery / Live |
| **Notes** | Dependencies, constraints, risks |

---

## Backlog

### P1 — Highest volume, data available now

---

#### Payments API ✦
| Field | Value |
|---|---|
| **Data source** | Checkout Payments API |
| **Query types enabled** | Transaction status; declined payment reason; capture/void status; idempotency check; proof of payment (ARN/RRN); refund status; refund failure reason; dispute status; evidence submission deadline; 3DS outcome; liability shift confirmation; SCA exemption applied; fraud/risk rule triggered; APM transaction status |
| **Contact types** | PAYMENTS (IN) → Transaction Status, Refunds, Disputes/Chargebacks, Authentication (3DS), Fraud & Risk Controls, Performance |
| **Contact volume** | ~10,049 contacts / 6 months (Refunds 4,114; Transaction Status 3,679; Disputes 745; 3DS 591; Risk 533; Performance 387 — all same API) |
| **Integration method** | API |
| **Access model** | Read-only (refund initiation and dispute evidence submission = HITL via Agent Consultant) |
| **Data availability** | Confirmed live |
| **Complexity** | Medium |
| **Status** | Proposed |
| **Notes** | Payment Tool is already live for agents and Fin on Dashboard — posts payment metadata when a Payment ID is found. This backlog entry covers extending that to the full query set listed above. Backend data source is being migrated to source of truth in H1 2026 (product team owns this change) — integration should align with the new source to avoid inheriting stale data. Clearing/TPA data is currently missing from the Payments API; ETA Q4 2026 — treat as a P3 extension of this entry once available. Refund initiation and dispute evidence submission are HITL actions, not read-only; keep in Agent Consultant scope. |

---

### P2 — High value, data not yet confirmed or H2 2026

---

#### User Management API ✦
| Field | Value |
|---|---|
| **Data source** | Checkout User Management API |
| **Query types enabled** | MFA status; SSO configuration check; account lock status; user permissions; dashboard access level |
| **Contact types** | ACCOUNT MANAGEMENT & ACCESS → Login & Access |
| **Contact volume** | 2,228 contacts / 6 months |
| **Integration method** | API |
| **Access model** | Read-only |
| **Data availability** | Confirmed live |
| **Complexity** | Medium |
| **Status** | Proposed |
| **API reference** | https://usermanagement-qa-int.cko-qa.ckotech.co/swagger/index.html |
| **Notes** | Login & Access is the highest-volume issue type. Fin cannot resolve MFA lockouts or SSO issues autonomously, but surfacing the account status (e.g. "your MFA device is registered but locked — here is the reset flow") removes the need for merchant to wait for agent confirmation. Requires security and legal review before account-level data is surfaced through Fin. |

---

#### Settlements API ✦
| Field | Value |
|---|---|
| **Data source** | Checkout Settlements / Reporting API |
| **Query types enabled** | Settlement status; delayed or missing settlement; reconciliation gap explanation; net settlement amount breakdown |
| **Contact types** | FUNDS AND FEES → Settlements |
| **Contact volume** | 858 contacts / 6 months |
| **Integration method** | API |
| **Access model** | Read-only |
| **Data availability** | H2 2026 |
| **Complexity** | Medium |
| **Status** | Proposed |
| **Notes** | Blocked on data latency fix for Settlements/Balances (Agent Consultant Phase 2 critical path). Once resolved, this is a straightforward read integration. Confirm latency (T+1 vs real-time) — Fin must set accurate expectations when data is not yet available for the period in question. |

---

#### Analytics MCP ✦
| Field | Value |
|---|---|
| **Data source** | Checkout Analytics MCP |
| **Query types enabled** | Report generation status; data mismatch explanation; SFTP delivery confirmation; custom report status |
| **Contact types** | DATA AND ANALYTICS → Reporting |
| **Contact volume** | 763 contacts / 6 months |
| **Integration method** | MCP |
| **Access model** | Read-only |
| **Data availability** | Not confirmed |
| **Complexity** | Medium |
| **Status** | Proposed |
| **Notes** | MCP is the preferred route over a custom API integration — lower engineering overhead if the Analytics MCP is available. Confirm availability and query scope before scoping. Data mismatch queries often require understanding of report logic as much as raw data — documentation coverage is needed alongside data access to make this useful. |

---

#### VisionNotify (Incident / Outage API)
| Field | Value |
|---|---|
| **Data source** | VisionNotify — internal incident lifecycle management platform |
| **Query types enabled** | Current outage confirmation; affected services and clients; incident status and history; ETA for resolution |
| **Contact types** | PAYMENTS (IN) → Performance (All Payments Failing); TECHNICAL ISSUE → API Integration |
| **Contact volume** | Spike-dependent — high deflection value during incidents |
| **Integration method** | API (REST, internal) |
| **Access model** | Read-only (`GET /incidents`, `GET /incidents/{incident_id}`, `GET /incidents/clients/{client_id}`) |
| **Data availability** | Confirmed (internal API exists; `GET /incidents` is planned — confirm GA status) |
| **Complexity** | Low |
| **Status** | Proposed |
| **API reference** | https://checkout.atlassian.net/wiki/spaces/NOC/pages/7008912153/VisionNotify+API+Documentation |
| **Notes** | VisionNotify is Checkout's internal incident platform — RESTful API with DynamoDB persistence, API key auth via Lambda Authorizer, SNS notifications to Merchant Care. During outages, contact volume spikes sharply; Fin surfacing incident status before merchants escalate is high-leverage deflection. The `GET /incidents/clients/{client_id}` endpoint allows filtering by impacted client — enabling Fin to confirm whether a specific merchant is affected. `GET /incidents` (all incidents) is currently planned, not live — confirm availability. Owner: Nirvan Bahadoor (NOC). |

---

#### Balance API ✦
| Field | Value |
|---|---|
| **Data source** | Checkout Balance API |
| **Query types enabled** | Current balance confirmation; negative balance explanation; balance top-up guidance |
| **Contact types** | FUNDS AND FEES → Balance |
| **Contact volume** | 409 contacts / 6 months |
| **Integration method** | API |
| **Access model** | Read-only |
| **Data availability** | Not confirmed |
| **Complexity** | Low |
| **Status** | Proposed |
| **Notes** | Straightforward read once available. Confirm API availability and credential scope for Fin. |

---

### P3 — Lower volume or longer horizon

---

#### Webhook Delivery Logs ✦
| Field | Value |
|---|---|
| **Data source** | Checkout Webhooks API / internal delivery log |
| **Query types enabled** | Webhook delivery status; failure reason; retry count; last attempted timestamp |
| **Contact types** | TECHNICAL ISSUE → Webhooks |
| **Contact volume** | 182 contacts / 6 months |
| **Integration method** | API |
| **Access model** | Read-only |
| **Data availability** | H2 2026 |
| **Complexity** | Medium |
| **Status** | Proposed |
| **Notes** | Low volume but rides on the Agent Consultant Phase 2 data layer (H2 2026) — incremental effort once that foundation is live. Merchants contact when they believe a webhook has not fired; Fin confirming delivery status and failure reason resolves most of these without escalation. Distinguish between "not delivered" (retrying) and "delivered but not received" (merchant-side issue). |

---

#### Clearing / TPA Data (Payments API extension)
| Field | Value |
|---|---|
| **Data source** | Checkout Payments API (Clearing/TPA data) |
| **Query types enabled** | Clearing status for a specific transaction; TPA routing confirmation; clearing cycle explanation |
| **Contact types** | PAYMENTS (IN) → Transaction Status (clearing-specific) |
| **Contact volume** | Subset of Payments API contacts |
| **Integration method** | API (same as Payments API) |
| **Access model** | Read-only |
| **Data availability** | Q4 2026 (data currently missing from Payments API; ETA Q4 2026) |
| **Complexity** | Low (same integration as Payments API) |
| **Status** | Proposed |
| **Notes** | Not a separate integration — an extension of the P1 Payments API entry once the clearing/TPA data is available in the API. TPA requests from third parties (Non-Merchant Requests case type) are out of scope for Fin; this entry covers merchant-facing clearing queries only. |

---

## Prioritisation Summary

| Priority | Data source | Contacts / 6m | Data availability | Complexity | Procedure defined? |
|---|---|---|---|---|---|
| P1 | Payments API (Transaction Status, Refunds, Disputes, 3DS, Risk, APMs) | ~10,049 | Confirmed live | Medium | No |
| P2 | User Management API (Login & Access) | 2,228 | Not confirmed | Medium | No |
| P2 | Settlements API | 858 | H2 2026 | Medium | No |
| P2 | Analytics MCP (Reporting) | 763 | Not confirmed | Medium | No |
| P2 | Balance API | 409 | Not confirmed | Low | No |
| P2 | VisionNotify (Incident API) | Spike-dependent | Confirmed (partial) | Low | No |
| P3 | Webhook Delivery Logs | 182 | H2 2026 | Medium | No |
| P3 | Clearing / TPA Data (Payments API extension) | Subset of Payments | Q4 2026 | Low | No |

---

## Open Questions

1. **User Management API** — API confirmed (Swagger: https://usermanagement-qa-int.cko-qa.ckotech.co/swagger/index.html). Confirm data access policy and security/legal review requirements before surfacing account-level data through Fin.
2. **Balance API** — confirm availability timeline and credential scope for Fin.
3. **Analytics MCP** — confirm availability and query scope; validate MCP is the right integration route.
4. **Clearing/TPA** — confirm Q4 2026 timeline and whether any interim data is accessible before the Payments API migration completes.
