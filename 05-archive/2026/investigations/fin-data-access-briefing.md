# Fin AI Agent: Data Access Roadmap

> **Owner**: Charlie Wildish
> **Last updated**: March 2026
> **Deliverables**: MCD-573 AI First Resolution Using Fin (Continuous) · MCD-568 Improve Fin Resolution Through Procedures (Q2 2026)

---

## Executive Summary

Fin resolves contacts at $0.90 per resolution versus $40 for a human agent. Today, its resolution rate is constrained not by AI capability but by data access: Fin can answer generic questions using knowledge articles, but cannot look up merchant-specific data.

Approximately 15,000+ contacts every 6 months fall into query types where the answer exists in a Checkout system — and Fin has no access to it. Payments alone accounts for over 10,000 of those contacts, with an API that is already live and integrated for agents.

Closing this gap is not a Fin configuration task. It requires API and data layer commitments from Card Payments Processing, Checkout Business Account, Client Balances, Client Reporting, and NOC. Fin accesses data exclusively through Procedures — structured resolution workflows that call external APIs at specific steps. Data access is a prerequisite for building those Procedures; it is not sufficient on its own.

This document maps each integration area, API availability, data gaps, owning product team, and earliest delivery timeline.

---

## Status Summary

| Area | Contacts / 6m | API available? | Data gaps | Product team | Earliest Fin integration | Priority |
|---|---|---|---|---|---|---|
| Payments (In) | ~10,049 | Yes | Clearing status, settled status, TPA status + gateway sync, APM success-after-failure + gateway status update — missing until Q4 2026. Backend migration to new source of truth H1 2026. | Card Payments Processing | Q2 2026 | P1 |
| Payouts ⚑ | ~2,345 | Yes | RFI flag when blocking a payout; issuing bank decline status; payout delayed or stuck vs expected processing time. Credential scope and Fin integration not yet confirmed. | Card Payments Processing | TBC | P2 |
| User Management / Login | 2,228 | Yes | Security and legal review required before surfacing account-level data through Fin. | Dashboard / Identity (TBC) | Q2 2026 (pending review) | P2 |
| Settlements | 858 | No — H2 2026 | Data latency fix required (T+1 vs real-time); blocked on Agent Consultant Phase 2 data layer. | Checkout Business Account | H2 2026 | P2 |
| Analytics / Reporting | 763 | No — not confirmed | MCP availability not confirmed. Documentation coverage also required alongside data access. | Client Reporting / Data Connectivity | TBC | P2 |
| Outages (VisionNotify) | Spike-dependent | Yes | No data gaps. All endpoints live: `GET /incidents`, `GET /incidents/{id}`, `GET /incidents/clients/{client_id}`. Ready to integrate. | NOC (Nirvan Bahadoor) | Q2 2026 | P2 |
| Balance | 409 | No — not confirmed | API availability and credential scope not confirmed. | Client Balances | TBC | P2 |
| Webhooks | 182 | No — H2 2026 | Delivery log not accessible. Rides on Agent Consultant Phase 2 data layer. | API / Integrations (TBC) | H2 2026 | P3 |
| Clearing / TPA (Payments extension) | Subset of above | No — Q4 2026 | Extension of Payments integration; clearing/TPA data not available in API until Payments migration completes. | Card Payments Processing | Q4 2026 | P3 |

⚑ Flagged gap — not in original backlog. Needs investigation before scoping.

**Note — shared dependency**: Settlements, Webhooks, and Balance all depend on the Agent Consultant Phase 2 data layer. If that slips from H2 2026, all three move with it.

---

## Delivery Timeline

| Timeline | Integration | Action required | Owner |
|---|---|---|---|
| **Q2 2026** | Payments (In) | Build Fin Procedures for Transaction Status, Refunds, Disputes, 3DS, Risk. Target new data source post-migration — do not integrate against legacy endpoint. | Care Product + Card Payments Processing |
| **Q2 2026** | Outages | Build Fin Procedure using `GET /incidents/clients/{client_id}` to confirm merchant impact during incidents. | Care Product + NOC |
| **Q2 2026** | User Management / Login | Initiate security and legal review. Build Procedure once cleared. | Care Product + Dashboard/Identity + Legal |
| **H1 2026** | Payments (In) — data migration | Track migration to new source of truth. No Fin action required; ensure Procedure targets correct endpoint post-cutover. | Card Payments Processing |
| **H2 2026** | Settlements | Build Procedure once data layer is live. Confirm latency resolution before go-live — Fin must set accurate expectations for periods where data is not yet available. | Care Product + Checkout Business Account |
| **H2 2026** | Webhooks | Build Procedure. Incremental effort once Agent Consultant Phase 2 data layer is live. | Care Product + API/Integrations |
| **TBC** | Balance | Confirm API availability with Client Balances. Build Procedure. | Care Product + Client Balances |
| **TBC** | Analytics / Reporting | Confirm MCP availability and query scope. Build Procedure once confirmed. | Care Product + Client Reporting |
| **TBC** | Payouts | Confirm query scope and credential access with Card Payments Processing. Scope Fin Procedure. | Care Product + Card Payments Processing |
| **Q4 2026** | Clearing / TPA (Payments extension) | Extend Payments Procedure once clearing/TPA data is available in the API. | Care Product + Card Payments Processing |

---

## Open Questions

1. **Payouts** — confirm credential scope for Fin and agree integration timeline with Card Payments Processing. What query types does the API currently support?
2. **User Management** — who initiates the security and legal review? What is the expected timeline and approval process?
3. **Balance API** — confirm availability and credential scope with Client Balances team.
4. **Analytics / Reporting** — confirm MCP availability and query scope with Client Reporting / Data Connectivity. Is MCP the correct integration route or does it require a custom API?
5. **Agent Consultant Phase 2 data layer** — confirm H2 2026 delivery timeline. Settlements, Webhooks, and Balance are all gated on this.
