# Platform Customer Segment

> Part of the broader customer segment model — see `01-knowledge-base/products/customer-segments.md` for the full picture.

## What is a Platform?

A **Platform** (also referred to internally as an **ISV — Independent Software Vendor**) is a Checkout.com merchant that operates as an intermediary — typically a **vertical SaaS business** that has embedded payments into its core product, enabling its own customers (merchants) to accept payments through it. Platforms often operate as **Payment Facilitators (PayFacs)**: they take on the merchant of record responsibility and the direct merchant relationship, with Checkout.com as the underlying acquirer.

The three-tier relationship is:

```
Checkout.com  ──►  Platform (ISV)  ──►  Merchant
```

- **Checkout.com** provides payment processing, data, and Dashboard/API access to the Platform. It is the Platform's payment infrastructure.
- **Platform (ISV)** integrates with Checkout.com and exposes payments to their merchants via their own product portal. Experienced with payments. **Considered Tier 1** in the merchant hierarchy.
- **Merchant** (the ISV's customer) manages their business through the Platform's portal. Inexperienced with payments — they interact with the Platform's abstraction layer, not Checkout.com directly. **Considered Tier 3–4** in the merchant hierarchy.

> Reference diagram: `/Users/charlie.wildish/.cursor/projects/Users-charlie-wildish-Charlie-PM-brain/assets/image-d93a75d6-5288-4a5f-8b72-c011d41c22cf.png`

The Platform is Checkout.com's direct customer. The merchants beneath the Platform are the Platform's customers — Checkout.com has no direct relationship with them.

> **Future direction**: Checkout.com may choose to act as a PayFac itself in the future, directly contracting with and owning the merchant relationship rather than routing it through the Platform. No timeline is confirmed. If this materialises, it would significantly change the support model — Checkout.com would become L1 for merchants directly, rather than L2 via the Platform. This document should be updated when that direction is confirmed.


## Key Design Considerations

Two important considerations flagged in the Platform model that have implications for product and support design:

**1. The information surfacing problem**
The Platform is responsible for surfacing the right payment information to their merchants. If a merchant fails onboarding checks, or a payment fails, or settlement is late — the Platform needs to translate and communicate this clearly. If they don't, the merchant contacts the Platform, which creates overhead and a poor experience for both the merchant and Checkout.com.

*Implication*: The data and APIs Checkout.com provides to the Platform need to make this surfacing easy. Gaps here flow downstream into support contacts.

**2. The merchant payments knowledge problem**
Merchants are described as **inexperienced with payments** — they interact with the Platform's simplification/translation layer, not with Checkout.com's products directly. If the payment experience is confusing or broken, they will ask the Platform for help, and the Platform escalates to Checkout.com.

*Implication*: Checkout.com cannot assume merchant-level payments literacy in any support interaction that passes through this chain. The complexity must be absorbed at the Platform layer. This is flagged as something to review post-ISV launch to assess how big a problem it is in practice.


## Real-World Examples

### Sunday — Restaurants
[Checkout.com case study](https://checkout.com/case-studies/sunday-brings-the-ease-of-online-payments-to-the-offline-dining-experience)

**What it is**: A QR code payment platform for restaurants. Diners scan a table QR code to split the bill, pay, tip, and leave — in ~10 seconds. Sunday uses Checkout.com Acquiring, 3DS Authentication, and Intelligent Acceptance.

**Sub-merchant model**: Sunday is the Platform and Checkout.com direct customer. The **restaurants** are Sunday's sub-merchants. Diners are the end payers.

**Support flow**: Diner has a problem → complains to restaurant → restaurant contacts Sunday (L1) → Sunday cannot resolve → Sunday contacts Checkout.com (L2)

**Support characteristics**:
- High time pressure — a restaurant that can't take payments during a dinner service is a crisis
- CNP (Card-Not-Present) transactions in an in-person dining environment — unusual risk profile
- Issues may be systemic (affecting many restaurants at once, e.g. a processing outage)
- Bill splitting and tip amounts add complexity to transaction queries
- Sunday operates as a PayFac with its own [Platform Merchant Terms](https://checkout.com/legal/sunday-merchant-fr-eea) on Checkout.com


### Golfmanager — Golf Clubs
[golfmanager.com](https://golfmanager.com)

**What it is**: A 100% cloud-based SaaS platform for golf club management — tee sheets, memberships, pro shop, restaurant POS, academy modules. Trusted by 34 of the Top 100 Golf Resorts in Continental Europe. Operates in 30+ countries.

**Sub-merchant model**: Golfmanager is the Platform. The **golf clubs** are their sub-merchants. Golfers, members, and visitors are the end payers.

**Support characteristics**:
- Recurring membership fee payments (SEPA direct debit, subscription billing) — failures affect long-term member relationships
- Multi-currency, operating across 30+ European countries
- High integration complexity — tee sheet, POS, and payment systems are tightly coupled
- Queries may relate to SEPA mandates, failed direct debits, or reconciliation across club departments


### Guesty — Short-Term Rental / Vacation Property Managers
[guesty.com](https://guesty.com)

**What it is**: A property management platform (PMS) for short-term rental and vacation rental hosts. Manages listings, reservations, payments, and operations for property managers.

**Sub-merchant model**: Guesty is the Platform. The **property managers** (who manage one or many properties) are their sub-merchants. Guests (travellers) are the end payers.

**Support characteristics**:
- Security deposit pre-authorisations and refunds are a common and contentious query type — guests dispute charges, property managers dispute refunds
- Chargeback-heavy vertical (guests frequently dispute vacation rental charges)
- Sub-account structure: Guesty uses a `accountId.subAccountId` model — queries may relate to a specific property manager's sub-account
- Settlement delays directly affect property managers who rely on timely payouts


## The Common Pattern Across These Examples

| | Sunday | Golfmanager | Guesty |
|---|---|---|---|
| **Vertical** | Hospitality (restaurants) | Sports & leisure (golf) | Travel & STR |
| **Sub-merchants** | Restaurants | Golf clubs | Property managers |
| **End payers** | Diners | Golfers / members | Guests / travellers |
| **Payment type** | CNP in-person | Online + in-person (POS) | Online (booking) + pre-auth |
| **Recurring payments** | No | Yes (membership fees) | Sometimes (subscription management) |
| **Chargeback risk** | Medium | Low–Medium | High |
| **Support urgency** | Very high (live service) | Medium | Medium–high (guest disputes) |

All three share the same structural support challenge: **a sub-merchant has a problem, the Platform contacts Checkout.com on their behalf, and Checkout.com must identify the Platform, locate the specific sub-merchant, and investigate at the sub-merchant level**.



## The Support Challenge

### Who contacts Checkout.com?

**Platform/ISV businesses** contact Checkout.com support on two types of issues:
1. **Their own platform-level issues** — configuration, integration, account management
2. **Issues affecting their merchants** — a merchant's payment failed, a merchant's settlement is delayed, etc.

When a Platform contacts support **on behalf of a merchant**, Checkout.com needs to understand:
- Which Platform/ISV is raising the ticket?
- Which merchant is the issue actually about?
- What is the nature of that merchant's relationship to the Platform?

### The Identification Problem

When Platforms email support@checkout.com, there is currently no automatic way to:
- Identify the contact as a Platform user (vs. a standard merchant)
- Determine which sub-merchant they're raising on behalf of
- Route the ticket to the right team with the right context

This must be solved for the support model to work effectively at scale.


## The Support Model

### Checkout.com's Role

Checkout.com acts as **Level 2 (second-line) support** for Platform (ISV) businesses:

```
Merchant has a problem
        ↓
Platform / ISV (Level 1) — attempts to resolve for their merchant
        ↓
Platform cannot resolve → escalates to Checkout.com (Level 2)
        ↓
Checkout.com support investigates on behalf of Platform + merchant
```

Checkout.com does **not** have a direct support relationship with individual merchants — that is the Platform's responsibility. All communication goes via the Platform.

### What This Means for Support Operations

| Area | Challenge | Solution Needed |
|------|-----------|-----------------|
| **Identification** | Know it's a Platform/ISV contact, not a standard merchant | Dashboard webform tagging, email routing logic |
| **Context** | Understand which merchant the issue is about | Structured ticket fields, merchant lookup capability |
| **Triage** | Route to agents equipped to handle Platform queries | Zendesk routing rules based on Platform/ISV flag |
| **Investigation** | Agents need to look up merchant-level transaction/account data | Internal tooling to traverse Platform → Merchant hierarchy |
| **Communication** | Respond to the Platform only (never directly to their merchant) | Clear communication protocols |


## Dashboard Support Flow (Webform)

For Platform users raising tickets through the dashboard:

**Required capabilities**:
- [ ] Platform users can select "I'm raising this on behalf of a merchant"
- [ ] They can specify / search for which merchant the issue relates to
- [ ] The ticket captures both Platform and merchant context
- [ ] Zendesk receives both Platform ID and merchant ID
- [ ] Routing rules apply Platform/ISV-specific logic


## Email Support Flow

For Platform users who email support@checkout.com:

**Required capabilities**:
- [ ] Identify the sender as a Platform/ISV user (email domain, account lookup, or header)
- [ ] Present a structured intake flow (e.g. auto-reply with webform link, or Intercom prompt)
- [ ] Capture merchant context before routing to an agent
- [ ] Route to agents trained to handle Platform/ISV queries


## Fin AI Agent Considerations

Currently Fin is not designed for the Platform model. Gaps:
- Fin doesn't know if the user is a Platform (e.g. Sunday's support team vs. a standard merchant)
- Fin can't differentiate "help with my account" vs. "help with my sub-merchant's account"
- Fin doesn't have access to sub-merchant data (e.g. a specific restaurant's transaction within Sunday's account)
- Fin has no vertical context (a golf club membership fee failure requires different handling than a restaurant table payment)

**Future state**:
- Fin identifies Platform users at the start of the conversation
- Fin can take Platform + sub-merchant context as input (e.g. "which restaurant / golf club / property manager is this about?")
- Fin can answer Platform-specific questions (e.g. "how do I check my sub-merchant's settlement status?")
- Fin understands the L1/L2 boundary — what Sunday/Golfmanager/Guesty should resolve themselves vs. what requires Checkout.com investigation


## Agent Knowledge Requirements

Support agents handling Platform queries need to know:
- How the Platform product works (sub-merchant hierarchy, payment flows)
- How to look up a seller within a Platform account
- The boundary between what Checkout.com supports vs. what is the Platform's responsibility
- How to communicate via the Platform (not directly to the seller)

**Training gap**: L1 agents currently handle standard merchant queries. Platform queries may require L2 routing or specialist training.


## Key Dependencies

| Dependency | Team | Notes |
|------------|------|-------|
| Platform product capabilities | Platform Product team | Charlie's team is a consumer of their product, not the owner |
| Seller lookup tooling | Engineering | Needs to be built or integrated |
| Zendesk routing rules | Zendesk Admins | Configuration work once flows are defined |
| Fin AI updates | Engineering + Intercom | Future phase |
| Agent training | Operations Excellence | Knowledge Manager + Process Architect |
| Operating procedures | Operations Excellence (Process Architect) | New procedures for Platform handling |


## Success Metrics

| Metric | Measurement |
|--------|-------------|
| Platform tickets correctly identified | % with Platform flag on Zendesk ticket |
| First contact resolution for Platform | % resolved without escalation to L2 |
| Time to resolution for Platform tickets | Average hours/days |
| Agent confidence with Platform queries | CSAT / quality score on Platform tickets |


## Research & Stakeholder Input

- **US Platforms support needs (Jul 2025)** — Transcript of interview with US sales team (Michael Taylor, Jeff Schmidt, Brian Foley) on Platform segment support challenges: onboarding visibility, suspensions/terminations/funds holds, platform control over terminations, Stripe Connect comparison, payment and payout visibility, data traceability, and handling payment failures/declines. Key follow-up: tracing payment through full lifecycle to settlement.  
  → `01-knowledge-base/processes/US Platforms - support needs - 2025_07_17.md`

## Open Questions

- [ ] How many Platform merchants exist today / expected this year?
- [ ] What volume of tickets do they currently generate?
- [ ] Are Platform tickets currently distinguishable in Zendesk, or completely mixed with standard merchants?
- [ ] Which team owns the Platform product — are they a stakeholder/partner?
- [ ] What seller data can agents already access today?
- [ ] Is there a target date for Platform support launch?


**Last Updated**: February 2026  
**Owner**: Charlie Wildish  
**Status**: Active delivery — primary focus for 2026
