# Fin AI on Email — Behaviour Specification

**Status**: Draft for review  
**Author**: Charlie Wildish  
**Date**: February 2026  
**Related**: [`known-challenges.md`](../../01-knowledge-base/processes/known-challenges.md), [`ai-agent-operations.md`](../../01-knowledge-base/processes/ai-agent-operations.md)


## Problem Statement

Fin operates as an Agent seat in Zendesk and can respond to email tickets. The email channel has structural properties that require clear configuration to avoid AI responses in the wrong scenarios:

- **Multiple CC'd people** — merchant ops teams CC account managers, internal stakeholders, and other team members. AI replies in these threads risk noise, errors in front of AMs, or responding to the wrong person.
- **No authenticated session** — email provides no identity signal. Fin cannot verify who is writing or return payment-specific data without org-level identification.
- **No single conversation owner** — unlike Dashboard chat, email threads have no clear session boundary and multiple people can contribute.


## Intended Flow

```
1. Ticket received in Zendesk (any channel)
         ↓
2. Enrichment webhook fires
   — Salesforce lookup (merchant identification)
   — Merchant tier, org record, AM details populated
   — Metadata tags applied (CC composition, identification status)
         ↓
3. Webhook completes → applies tag: webhook_complete
         ↓
4. Zendesk trigger: webhook_complete → assign Fin to ticket
         ↓
5. Fin classifies ticket using taxonomy
         ↓
6. Fin applies escalation rules
   (classification + enrichment data + metadata tags all available)
         ↓
         ├── No escalation rule triggered
         │        ↓
         │   Fin attempts response
         │        ↓
         │   ├── Resolved → ticket closed / tagged fin_resolved
         │   └── Unresolved → escalate to human agent
         │
         └── Escalation rule triggered
                  ↓
             Route to human agent immediately (no Fin response)
```

**Key principles**:
- Fin is only assigned once enrichment is complete — it always has merchant context when it classifies
- `webhook_complete` is the gate; Fin never sees a raw, unenriched ticket
- Metadata tags (CC composition, identification status) should be set by the enrichment webhook or alongside it, so they are present when Fin starts
- Fin's escalation rules are the sole decision point for respond vs. route-to-human


## Two Layers of Routing

There are two distinct inputs to the escalation decision:

| Layer | What It Detects | Who Configures It |
|-------|----------------|------------------|
| **1. Ticket metadata** (Zendesk tags) | CC composition, merchant identification status | Zendesk admin via triggers |
| **2. Content classification** (Fin) | Query type and intent | Charlie via Fin escalation rules |

Both layers feed into Fin's escalation rules. A ticket can be escalated based on content (e.g. fraud query) *or* metadata (e.g. AM on CC) — either condition is sufficient.


## Layer 1 — Zendesk Tags (Metadata)

Metadata tags are applied by the enrichment webhook (or Zendesk triggers that run before `webhook_complete` fires). Because Fin is only assigned after `webhook_complete`, it always has these tags available when it classifies — no race condition.

| Tag | Set By | Condition | Purpose |
|-----|--------|-----------|---------|
| `webhook_complete` | Enrichment webhook | Webhook finishes executing | Gates Fin assignment |
| `fin_am_cc` | Enrichment webhook or Zendesk trigger | `@checkout.com` address in CC or requester field | Flag AM/internal involvement |
| `fin_high_cc` | Zendesk trigger | CC count > 3 | Flag complex stakeholder thread |
| `fin_unidentified` | Enrichment webhook | Merchant not matched in Salesforce | Flag unknown merchant — Dispatch queue |
| `fin_webform` | Zendesk trigger | Ticket originated from Dashboard webform | Authenticated channel — different escalation rules may apply |

> **Note**: The enrichment webhook is the natural place to set `fin_am_cc` and `fin_unidentified` since it already has Salesforce data. `fin_high_cc` can be a simple Zendesk trigger on CC count. All tags should be present before `webhook_complete` is applied.


## Layer 2 — Classification Taxonomy

Fin classifies every ticket into one of the following categories. The taxonomy drives escalation rules.

### Proposed Taxonomy

| Category | Examples | Fin Handles? |
|----------|----------|-------------|
| **Integration & API** | Webhook setup, API errors, SDK questions, endpoint docs | ✅ Yes |
| **Product How-To** | Dashboard navigation, feature configuration, report access | ✅ Yes |
| **Error Code / Decline Explanation** | Generic error codes, decline reason explanation | ✅ Yes |
| **Payment Status** | Transaction lookup, payment outcome | ⚠️ Identified merchants only |
| **Settlement & Payouts** | Payout schedule, settlement dates, missing payout | ⚠️ Identified merchants only |
| **Refund Query** | Refund status, how to issue a refund | ⚠️ Identified merchants only |
| **Account & User Management** | Adding users, permissions, Dashboard access | ❌ Escalate — account-level action |
| **Bank & Financial Details** | Bank account changes, reserve queries | ❌ Escalate — requires individual auth |
| **Dispute & Chargeback** | Chargeback evidence, dispute response | ❌ Escalate — requires investigation |
| **Fraud & Risk** | Suspected fraud, account compromise, risk flags | ❌ Escalate — urgent, human judgment |
| **Compliance & Legal** | PCI, PSD2, regulatory queries, legal requests | ❌ Escalate — specialist required |
| **Complaint / Escalation** | Dissatisfaction, SLA breach, formal complaint | ❌ Escalate — relationship risk |
| **Unclassified** | Fin cannot determine category with confidence | ❌ Escalate — default safe |

**"Identified merchants only"** = ticket is matched to an org record (Salesforce lookup succeeded, `fin_unidentified` tag absent). If unidentified, these also escalate.


## Fin Escalation Rules

Fin escalates to a human agent if **any** of the following conditions are met:

### Content-Based Escalation
- Classification is: Account & User Management, Bank & Financial Details, Dispute & Chargeback, Fraud & Risk, Compliance & Legal, Complaint / Escalation, or Unclassified
- Classification is Payment Status / Settlement / Refund AND `fin_unidentified` tag is present

### Metadata-Based Escalation (from Zendesk tags)
- `fin_am_cc` is present — route to human regardless of query type; notify the relevant AM/agent
- `fin_high_cc` is present — route to L1 triage
- `fin_unidentified` is present AND query requires payment data

### Behavioural Escalation
- Fin cannot answer with sufficient confidence after knowledge base search
- Merchant explicitly requests a human agent
- Negative sentiment / urgency keywords detected: "unacceptable", "escalate", "CEO", "legal", "regulator", "complaint"


## First-Response Model

Fin on email operates as a **first-response handler only**, not a full conversational agent.

- Fin responds **once** to the initial query
- If the merchant replies and the issue is unresolved, the ticket routes to a human agent for follow-up (tagged `fin_responded`)
- Fin does not continue the email thread through multiple exchanges

**Rationale**: Email threading, multiple CC'd participants, and topic drift across long threads make multi-turn AI conversations unreliable. A single, accurate first response that resolves 20–30% of tickets outright is more valuable than a conversational model that risks errors in complex threads.


## Reply Configuration

| Setting | Recommended Value | Reason |
|---------|------------------|--------|
| Reply mode | **Reply to requester only** (not reply-all) | Prevents AI responses going to AMs and all CC'd stakeholders |
| Response timing | **Wait 3 minutes** before responding | Allows rapid follow-up messages from the sender to arrive before Fin drafts a response |
| Signature | "Checkout.com Support — AI-assisted response. A member of our team will follow up if this hasn't resolved your query." | Sets expectations; transparent about AI involvement |


## Fin's Response Format on Email

```
[Direct answer — 1–2 sentences]

[Supporting detail, steps, or documentation link — bullets where appropriate]

[Clear next step or resolution confirmation]


If this hasn't resolved your query, reply to this email and a member of our team will be in touch.
Checkout.com Support — AI-assisted response.
```

Do not:
- Ask multiple clarifying questions in one response (pick the most important one)
- Return payment-specific data (transaction amounts, card detail) for unidentified merchants
- Reference or address CC'd people by name


## Open Questions

| Question | Owner | Priority |
|----------|-------|----------|
| Does the current taxonomy align with Zendesk's existing ticket categories / tagging structure? | Charlie + Operations | High |
| Can the enrichment webhook set `fin_am_cc` and `fin_unidentified` tags before applying `webhook_complete`? Confirm webhook logic and tag order with engineering. | Engineering | High |
| What is the current % of email tickets that would fall into Fin-handleable categories? (Determines realistic deflection ceiling) | Data | High |
| What data can Fin safely return to org-matched (but not individually verified) contacts? Needs compliance sign-off. | Charlie + Legal/Compliance | High |
| Does Fin respect Zendesk tags as inputs to escalation rules natively, or does this require custom configuration? | Zendesk admin | Medium |
| Does the 3-minute response delay need a Zendesk time-based trigger, or is this configurable in Fin directly? | Zendesk admin | Medium |
| Should Dashboard webform tickets (`fin_webform`) have broader Fin behaviour given the user is authenticated? | Charlie | Medium |


## Success Metrics

| Metric | Notes |
|--------|-------|
| Fin first-response resolution rate on email | % of email tickets Fin resolves with no human follow-up |
| Classification accuracy | % of tickets correctly classified vs. manually reviewed sample |
| Escalation rule trigger rate by condition | Which rules fire most — informs taxonomy and rule refinement |
| Merchant CSAT for Fin-resolved email tickets | Should be ≥ human-resolved CSAT; if lower, scope needs narrowing |
| Misfire rate | Cases where Fin responded when it should have escalated (track `fin_am_cc` tickets that got a Fin response) |


## Next Steps

1. **Validate taxonomy** with Operations team — does it map to how tickets are currently categorised?
2. **Confirm Zendesk admin feasibility** — trigger execution order, tag-reading by Fin, response delay configuration
3. **Compliance check** — define what data Fin can return to org-matched unverified contacts on email
4. **Data pull** — what % of email volume falls into Fin-handleable categories?
5. **Pilot design** — controlled pilot scoped to Integration & API and Product How-To categories (lowest risk, no payment data)


**Last Updated**: February 2026  
**Status**: Draft — pending taxonomy validation and Zendesk admin feasibility review
