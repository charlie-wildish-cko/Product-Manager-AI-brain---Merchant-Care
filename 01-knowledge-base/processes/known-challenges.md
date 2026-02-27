# Known Challenges & Constraints

> These are real, documented constraints that shape product decisions. Reference when evaluating solutions — any proposal that ignores these will fail in practice.


## 1. Email Channel — Hard to Automate with AI

### The Challenge
Email (support@checkout.com) is the preferred channel for many merchants because their internal teams use **shared inboxes or ticketing systems** (e.g. Zendesk, Freshdesk, Intercom on the merchant side). The actual requesters are operational teams within the merchant — customer support, payment ops, disputes ops, finance ops — not developers or individuals with a personal inbox.

This creates several AI automation problems:

- **Multiple people on CC**: Emails often have account managers, internal stakeholders, or multiple ops team members copied. AI replies risk going to the wrong person or creating noise in threads with many participants.
- **Shared inbox context**: Replies may be picked up by a different person than the sender. There is no authenticated, persistent session like in the Dashboard AI Agent.
- **No authentication mechanism**: Email provides no way to verify who is asking or retrieve payment data on their behalf. Fin AI Agent relies on authenticated Dashboard sessions — that mechanism doesn't exist on email.
- **Thread complexity**: Email threads can span weeks with multiple topics mixed in a single chain.

### How Fin Actually Works in This Context
- **Fin operates as an Agent seat in Zendesk** — it can respond to any Zendesk ticket, including email-originated ones. Fin is already "on" email in a limited sense.
- A **pilot was run on Tier 3 (Standard) email** — Fin as a Zendesk agent seat. Generic/FAQ queries can be handled, but payment-specific responses are blocked by the lack of identity verification.
- **Standard tier email is being deprecated**: Standard merchants will be directed to Dashboard and AI Agent as their primary channels. Email as a dedicated channel is reserved for Premium and Enterprise. The Standard email pilot findings remain relevant as a reference but are not the target state.

### Product Implications
- Any email AI solution requires either: (a) an authentication step before payment data is shared, or (b) restricting AI responses to non-sensitive, generic content only
- The focus for email AI is **Premium and Enterprise** — the tiers with dedicated email entitlement
- AI Agent adoption on email is fundamentally limited until authentication is solved; this work is now scoped to Premium/Enterprise email volume


## 2. Merchant Identification Over Email

### The Challenge
When a merchant emails support@checkout.com, Checkout.com often **cannot identify who is contacting us**. This happens because:

- Merchant operational team members (payment ops, disputes, finance ops) are not required to have a Checkout.com Dashboard account
- There is high **team churn** at merchant organisations — people join, leave, and rotate across roles frequently
- Checkout.com does not mandate Dashboard login or authentication to raise a support request via email

### The Identification Process (Current)

When an email arrives in Zendesk:

```
Email received
      ↓
Email address looked up in Salesforce (CRM) + Dashboard user management
      ↓
      ├── FOUND → Ticket matched to organisation record
      │            → Ticket automatically enriched with merchant data
      │            → SLA set based on merchant tier
      │            → Routed to Level 1 queue
      │
      └── NOT FOUND → Ticket drops into Dispatch queue
                       → Manual review by agent
                       → Agent attempts to identify merchant and match manually
```

### The Dispatch Queue
The **Dispatch queue** is a manual triage step for unidentified email contacts. It is a direct cost and delay driver:
- Every unidentified ticket adds agent time before the clock even starts on resolution
- SLA timer may not start until merchant is identified and ticket is matched
- Scale of the problem is unknown but likely significant given high merchant team churn

### Why It's Hard to Fix
- **Dashboard sign-up is merchant-controlled**: there is no self-serve registration flow. A merchant's Admin or Owner must invite team members. Ops team members can't just sign themselves up — it requires the merchant's internal admin to act, which is hard to enforce at scale.
- Mandating Dashboard accounts for all ops team members requires merchant organisational change, not just a product feature
- **Domain mapping doesn't exist yet** — it's a future idea being considered for Premium/Enterprise, not a live capability
- Platform merchants add further complexity: the contact may be the Platform, not the seller, and neither may be in the CRM

### Product Implications
- Contact enrichment and identification quality directly affects SLA adherence, routing accuracy, and cost per contact
- Domain mapping expansion (currently Enterprise/Premium only) to Standard tier would reduce Dispatch queue volume
- Any self-serve or AI solution is blocked until the identity problem is solved
- The Platform support model must address identification — a Platform contacting on behalf of a seller may have neither entity in the CRM
- Improving identification is a prerequisite for many downstream improvements (AI on email, automated routing, SLA accuracy)


## 3. AI Agent Adoption Blocked by Authentication Gap

### The Challenge
The **Fin AI Agent lives inside the authenticated Dashboard**. This is its strength (it knows who the user is) and its limitation (it only reaches merchants who log in to the Dashboard to seek help).

Merchant ops teams prefer email → email has no authentication → AI Agent is not accessible on the channel most merchants use.

### Current State

| Channel | Authentication | AI Available | Payment Data Returnable |
|---------|---------------|-------------|------------------------|
| Dashboard (Fin AI Agent) | ✅ Authenticated | ✅ Yes | ✅ Yes (user verified) |
| Email | ❌ No authentication | ❌ Not deployed | ❌ No (identity unverified) |
| Dashboard Webform | ✅ Authenticated | ❌ Not currently | ✅ Possible |

### How Fin Operates on Email
**Fin runs as an Agent seat in Zendesk**, which means it can respond to any Zendesk ticket — including email-originated ones. This is the mechanism used in the Tier 3 email pilot.

**Email AI Pilot finding (Tier 3 / Standard)**:
- Generic/FAQ responses can be automated — Fin as Zendesk agent handles these fine
- **Payment-specific responses cannot** — returning transaction data, settlement info, or account-specific detail to an unauthenticated email address is a security risk
- The majority of merchant queries are payment-specific → the pilot's scope was severely limited

**Dashboard sign-up constraint**: There is no self-serve registration. Dashboard accounts are managed by the merchant's own Admin or Owner — Checkout.com cannot directly onboard individual ops team members. Any solution requiring "just create a Dashboard account" is blocked by this merchant-side dependency.

### The Core Tension
```
Where merchants contact us → Email (unauthenticated)
Where AI works best       → Authenticated channel (Dashboard)
```

These are not currently the same place.

### Chosen Approach (in progress — see PRD)

> Full detail: `04-active-work/roadmap-items/fin-email-auth-data-policy-prd.md`

The solution is in active development. Key decisions made:

- **Gate = org identification, not individual auth**: Fin may return payment data (status, outcome code) once the merchant org is identified via Salesforce, Dashboard, or domain mapping — consistent with what agents already do today
- **Identification hierarchy**: Salesforce/Dashboard match (primary) → domain mapping (fallback) → unidentified (FAQ only)
- **Email verification code (OTP)**: Fin has a native flow to send a code and verify via reply to a separate sender email. Used as an optional confirmation tool, not a mandatory gate for standard payment data
- **CC-based exclusion rules**: Fin does not engage at all if a @checkout.com address is CC'd or more than 2 people are CC'd — applies to all Fin email involvement, not just data queries
- **Standard response pattern**: Payment status summary in email + direct deep link to the payment record in the Merchant Dashboard
- **Hard limits remain**: PANs and consumer PII are never returned over email regardless of identification level
- **Implementation**: Zendesk triggers set `fin_eligible` and `fin_auth_level` fields on tickets; Fin config reads those fields to control involvement and data entitlements


## How These Challenges Interact

These three challenges are interconnected:

```
Merchants prefer email
        ↓
Email has no authentication
        ↓
Can't identify the requester        → Dispatch queue (manual cost)
Can't verify identity for AI        → Human agent required
Can't return payment data safely    → AI resolution rate capped
        ↓
AI Agent adoption stays low         → Cost per contact stays high
```

Solving any one of these in isolation has limited impact. The highest-leverage intervention is **solving authentication on email** — it directly unblocks all three.


## Relationship to 2026 Goals

| Goal | How These Challenges Block It |
|------|------------------------------|
| Reduce contact rate | Unidentified merchants can't be proactively helped; poor routing increases re-contacts |
| Reduce cost per contact | Dispatch queue adds cost before resolution even starts; human-only email is expensive |
| Improve AI resolution rate | Structurally capped while email has no auth |
| Platform support model | Platform + seller identity doubly complex over email |
| Fin AI API access | High value only if Fin is on the right channels to use it |


**Last Updated**: February 2026  
**Owner**: Charlie Wildish
