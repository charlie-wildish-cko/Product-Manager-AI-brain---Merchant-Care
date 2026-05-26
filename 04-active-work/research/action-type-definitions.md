# Action Type Definitions

> **Owner**: Charlie Wildish (draft) — for review with Engineering Manager and Knowledge Manager
> **Status**: Draft — not yet validated against SOP content or Fin Procedures backlog
> **Purpose**: Define Action Types as the join key between Reason nodes and Data Source availability in the knowledge graph. Action Types determine Fin automability and drive `DATA_AVAILABLE_FOR` edge modelling in the data layer graph.
>
> **Source**: Derived from Reason labels in `01-knowledge-base/processes/support-taxonomy.md` (V3, Feb 2026) and Class 8 draft in `04-active-work/research/knowledge-graph-phase1-entity-taxonomy.md`.

---

## Summary Table

| # | Action Type | Automation candidacy | Data required? | Knowledge required? |
|---|---|---|---|---|
| 1 | Status lookup | Fin-resolvable | Yes | No |
| 2 | Proof retrieval | Fin-resolvable | Yes | No |
| 3 | Explanation / education | Fin-resolvable | No | Yes |
| 4 | Data investigation | Conditional | Yes | Partial |
| 5 | Configuration change | Conditional | Yes | Yes |
| 6 | Access / credential action | Conditional | Yes | Partial |
| 7 | Escalation / triage | Conditional | Yes | No |
| 8 | Manual processing | Human-in-the-loop | Yes | No |
| 9 | Dispute submission | Human-in-the-loop | Yes | Yes |
| 10 | Onboarding action | Human-in-the-loop | Yes | Yes |
| 11 | No action | Fin-autonomous | No | No |

---

## Definitions

### 1. Status lookup

**Definition**: Retrieve the current state of a transaction, payout, balance, settlement, or process. The merchant needs to know *what is happening* — no change to the record, no document, no explanation needed.

**Example Reasons**: Stuck in status / Status Enquiry; Payout status inquiry; Balance confirmation; Card payout stuck in Pending; Bank payout stuck in Pending

**Data shape**: Fin receives an identifier (transaction ID, payout ID, merchant ID) → queries the relevant API → returns current status + timeline (e.g. authorised → captured → settled on [date]).

**Data sources by domain**:
| Domain | Source | Availability |
|---|---|---|
| Payments (In) | Card Payments Processing API | Live (with data migration gaps until Q4 2026) |
| Payouts | Card Payments Processing API | Live (credential scope TBC) |
| Balance | Client Balances API | TBC |
| Settlements | Checkout Business Account data layer | H2 2026 |
| Outages | VisionNotify API | Live |

**Automation candidacy**: Fin-resolvable — this is the primary candidate Action Type for Fin Procedures. Retrieves, does not change. No financial or compliance risk. Every Status lookup Reason with a live data source is a Fin Procedure candidate.

---

### 2. Proof retrieval

**Definition**: Obtain documentary evidence the merchant needs — an ARN, RNN, bank confirmation, settlement statement, or payment audit record. Different from Status lookup: the output is a reference or document, not a status value.

**Example Reasons**: Proof of payment (ARN, RNN, Bulk); Proof of Bank Payout; Audit request; Settlement statement

**Data shape**: Fin receives a transaction or settlement ID → queries the relevant API or reporting system → returns the specific reference or record (e.g. ARN: 74039004123456789012345).

**Data sources**: Card Payments Processing API (ARN/RNN); Reports API / SFTP (settlement statements); Audit log API (if available).

**Automation candidacy**: Fin-resolvable for standard references (ARN, RNN, payout confirmation). Conditional for bulk or complex audit requests — Fin can retrieve individual records; multi-record audit packages may require human assembly.

---

### 3. Explanation / education

**Definition**: Explain how a product, process, scheme rule, or error code works. No account-specific data needed — the answer is the same for every merchant asking the same question.

**Example Reasons**: Liability Shift Status; AVS / CVV Mismatch; Velocity Limit Reached; Scheme fees explanation; 3DS authentication flow; Webhook signature verification

**Data shape**: None — knowledge only. Fin retrieves from the knowledge base, not from an API.

**Data sources**: N/A

**Automation candidacy**: Fin-resolvable with content coverage alone. This is the only Action Type where content is sufficient and data access is not a blocker. Every Reason in this category maps to a `COVERED_BY` edge requirement, not a `DATA_AVAILABLE_FOR` edge. Important for the resolvability matrix: a high-volume Explanation Reason with no content = content gap, not a data problem.

**Note**: Explanation often accompanies Status lookup in the same contact — "Why is my payment in this status?" requires both a status retrieval and an explanation of what that status means. These should be modelled as separate Reasons if volume warrants, or as a compound Reason with both edge types.

---

### 4. Data investigation

**Definition**: Diagnose a discrepancy, mismatch, or missing entry in reported data. The merchant has data that does not match what Checkout shows — Fin must retrieve both sides and identify the gap.

**Example Reasons**: Data Mismatch / Missing; Reconciliation issue; Missing transaction from report; SFTP file not received

**Data shape**: Fin receives a date range, merchant ID, and the merchant's claimed figure → queries reporting APIs and transaction data → returns the Checkout-side record set for comparison. More complex than Status lookup: requires joining across multiple data sources or comparing against merchant-supplied data.

**Data sources**: Reports API; Dashboard Reports (financial and non-financial); Card Payments Processing API; SFTP delivery logs (H2 2026).

**Automation candidacy**: Conditional. Fin can retrieve and surface both sides of a discrepancy for simple cases (e.g. single missing transaction). Complex reconciliation gaps — multi-day, multi-currency, bulk — require human investigation. Fin's role is to retrieve context and eliminate simple mismatches before escalating.

---

### 5. Configuration change

**Definition**: Update an account setting, risk rule, webhook endpoint, SFTP credential, notification preference, or other configuration value. Unlike Status lookup, this changes the record.

**Example Reasons**: Risk Rules; Webhook setup; SFTP Configuration; Account settings update; Notification preferences

**Data shape**: Fin receives the desired change → validates against permitted change types → executes (if Fin-autonomous) or surfaces for agent approval (HITL).

**Data sources**: Dashboard / Configuration API; Webhooks API (H2 2026); Risk API.

**Automation candidacy**: Conditional — split by risk level.
- **Fin-autonomous (approved)**: low-risk, reversible changes (e.g. notification preferences, webhook endpoint updates where the merchant controls the destination)
- **Human-in-the-loop**: risk rule changes; API key permissions; anything that affects payment flow or fraud thresholds

Risk rule changes that affect payment acceptance rates or fraud exposure must remain HITL regardless of Fin capability maturity. The HITL boundary here is a policy decision, not a technical one.

---

### 6. Access / credential action

**Definition**: Reset or manage a login, MFA device, SSO link, or API key. Includes account-level access changes (add/remove user, change permissions) and technical credential management (create/revoke API keys).

**Example Reasons**: Login Error / MFA / SSO; Create / Edit Keys; User access request; Account locked

**Data shape**: Fin receives user or account identifier → checks account state → executes reset (if permitted) or routes to agent with pre-fetched account context.

**Data sources**: User Management API (available; security review pending for Fin use).

**Automation candidacy**: Conditional — split by security posture.
- **Fin-autonomous**: locked account unblock (where automated unlock is permitted by security policy); re-send MFA
- **Human-in-the-loop**: API key creation/revocation; permission changes; account-level access grants

Security and legal review is required before Fin surfaces any account-level data through this Action Type. This is the current blocker for User Management / Login (Q2 2026 dependency).

---

### 7. Escalation / triage

**Definition**: Identify the root cause of a systemic issue affecting the merchant — all payments failing, an acceptance rate drop, an active outage. Fin's role is to surface context (outage status, error patterns, merchant impact) before human triage or to resolve if the issue is a known outage.

**Example Reasons**: All Payments Failing; Acceptance Rate Issue; Suspected fraud spike; Gateway errors

**Data shape**: Fin retrieves outage status (VisionNotify API), recent error rate for the merchant (Card Payments Processing API), and incident context → surfaces to merchant or escalates to agent with pre-loaded context.

**Data sources**: VisionNotify API (live); Card Payments Processing API; Datadog RUM API (not yet connected).

**Automation candidacy**: Conditional.
- **Fin-resolvable**: known active outage — Fin confirms merchant impact using `GET /incidents/clients/{client_id}`, provides status and ETA, closes contact
- **Fin-as-triage**: no outage found — Fin retrieves error context and escalates with pre-loaded data; human agent investigates
- **Human only**: suspected fraud spike or complex acceptance degradation — Fin cannot diagnose; escalation with context

---

### 8. Manual processing

**Definition**: Execute a financial action — manual refund, payout correction, fund movement, or chargeback credit. Changes money or balances. Requires human authorisation by definition.

**Example Reasons**: Refund failed / Manual Refund; Manual payout correction; Transfer or split failed

**Data shape**: Fin retrieves the transaction record and confirms eligibility (e.g. refund window, original amount) → presents to agent for approval → agent executes.

**Data sources**: Card Payments Processing API; Checkout Business Account data layer.

**Automation candidacy**: Human-in-the-loop — no exceptions. Financial actions that change balances or initiate fund movements are outside Fin's autonomous scope at all maturity levels. Fin's role is pre-work: retrieve the record, confirm eligibility, present to agent in a single action.

---

### 9. Dispute submission

**Definition**: Prepare, submit, or respond to a chargeback or pre-dispute notification. Involves gathering evidence, meeting scheme deadlines, and submitting structured responses to card schemes.

**Example Reasons**: Evidence Help and submission; Dispute notification; Pre-dispute response; Chargeback reversal request

**Data shape**: Fin retrieves dispute record and deadline → guides merchant through evidence requirements → agent reviews and submits, or Fin assists with evidence compilation.

**Data sources**: Disputes API (live); Card Payments Processing API (for transaction context).

**Automation candidacy**: Human-in-the-loop. Evidence review and submission decisions carry financial liability and scheme-compliance risk. Fin can assist with retrieval and structuring; submission remains agent-controlled. Future Fin Procedure scope: automate evidence compilation for standard dispute types; agent reviews and submits.

---

### 10. Onboarding action

**Definition**: Complete a step in merchant onboarding or activation — KYC/KYB verification, account activation, card programme setup, entity structure configuration.

**Example Reasons**: Merchant activation and verification; Create / Activate Card; Entity structure changes; Sub-merchant onboarding (Platform contacts)

**Data shape**: Fin retrieves onboarding state → identifies missing steps or verification blockers → routes to appropriate internal team with context.

**Data sources**: Identity Verification API; Issuing API; Platform entity data.

**Automation candidacy**: Human-in-the-loop. Onboarding actions involve compliance decisions (KYC/KYB) and legal entity changes. Fin's role is retrieval and routing with context; human agent or compliance team completes the action.

---

### 11. No action

**Definition**: The contact requires no resolution action — spam, duplicate submission, misdirected contact (cardholder contacting merchant support), or a contact that closed itself (merchant already resolved).

**Example Reasons**: Spam / Duplicate / No action; No action required by Merchant Care; Cardholders / Third Parties (Non-Merchant Requests)

**Data shape**: None required.

**Data sources**: N/A

**Automation candidacy**: Fin-autonomous. Fin closes or redirects without agent involvement. No content or data needed. These contacts inflate contact volume without adding value — auto-closing them is a quick win for cost per contact.

---

## Resolvability by Action Type

| Action Type | Fin can resolve? | Blocker if not |
|---|---|---|
| Status lookup | Yes — if data source is live | Data source availability (see Status lookup table above) |
| Proof retrieval | Yes — for standard references | Reporting API access |
| Explanation / education | Yes — if content exists | Content coverage (`COVERED_BY` edge) |
| Data investigation | Partially | Data source completeness; complex cases need human |
| Configuration change | Partially | Policy decision on HITL boundary; config API access |
| Access / credential action | Partially | Security/legal review (User Management API) |
| Escalation / triage | Partially | Datadog RUM integration for non-outage cases |
| Manual processing | No — HITL always | Policy: financial actions require human authorisation |
| Dispute submission | No — HITL always | Scheme compliance risk; evidence liability |
| Onboarding action | No — HITL always | Compliance and KYC/KYB requirements |
| No action | Yes — Fin-autonomous | None |

---

## Open Questions

1. **Configuration change HITL boundary** — who defines the approved list of Fin-autonomous configuration changes? Engineering Manager + Legal + Security review required before any configuration Action Type goes to Fin Procedures scope.

2. **Explanation vs Status lookup in compound Reasons** — "Why is my payment failing?" requires both. How should this be modelled: two Reasons, one compound Reason with both edge types, or a single Reason with a flag? Recommend: keep as one Reason, model both `COVERED_BY` and `DATA_AVAILABLE_FOR` edges — the graph will show both gaps where they exist.

3. **Data investigation ceiling** — at what point does Fin stop and escalate? A clear escalation rule (e.g. "if discrepancy value > £X, or if > N transactions, escalate") is needed before this Action Type enters Procedures scope. Knowledge Manager and Process Architect should define this.

4. **Platform contacts and Action Type applicability** — several Action Types (Onboarding action, Configuration change, Escalation/triage) behave differently for Platform contacts vs Direct Merchants. The `RAISED_BY` edge (Reason → Customer Segment) handles this in the graph, but Fin Procedures will need Platform-specific variants for affected Action Types.
