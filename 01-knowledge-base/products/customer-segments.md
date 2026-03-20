# Customer Segments

> Overview of all customer segments supported by Checkout.com's Customer Support (Merchant Care) team. Covers (1) **end customer personas** — who we design for and prioritise (B2B: Ops teams at the merchant; B2C: cardholders and Braavos end users) — and (2) **business segments** — Enterprise, Platform, Payfac, Issuing, Identity, B2C.

## Why it matters

Not all contacts cost the same and not all merchants need the same support. Without a clear segment model, Merchant Care cannot make rational decisions about where to invest — whether in AI deflection, agent tooling, self-service, or human coverage — because there is no shared view of who the customer is and what they need.

The segment model provides that foundation. It determines which merchants get which support experience (via Care Success Plans), how contact volumes and costs are attributed, and where product investment will have the most impact. It also sets the boundary between B2B and B2C support — two fundamentally different models with different channels, regulatory requirements, and cost structures.

Getting segments right matters most when the portfolio is growing. Platform is the primary 2026 focus because the support model for that segment doesn't yet exist. B2C is the 2027 challenge because Consumer Duty obligations apply from day one of the Braavos launch.

## End merchant customer personas (Merchant Care context)

**We solve for Ops teams at the merchant:** Support, Risk, and Finance. This is **B2B support only** — the personas and taxonomy below describe who contacts Merchant Care from our business (merchant) customers. B2C support (separate model) will serve **cardholders and end users of Project Braavos**. Who contacts us (and what they contact us about) is reflected in our taxonomy and in contact volumes — Case Types and Issue Types map to these three Ops domains. See `01-knowledge-base/processes/support-taxonomy.md` for the full taxonomy and volume view.

Within our B2B merchants, the people who contact or could be served by Merchant Care fall into two broad **end merchant customer** segments. This framing clarifies who we design for and who we do not prioritise.

| Segment | White glove servicing | Need | Pain points | Opportunities |
|--------|------------------------|------|-------------|---------------|
| **Merchant Ops teams (Support, Risk, Finance)** | Low | Solve transaction-based queries from their customers quickly; solve regional (e.g. MENA) transaction issues; swift response on complex transaction issues; visibility on Balance & Settlement payouts | Data gaps in Dashboard and data APIs for key data; diagnosing transaction issues not intuitive in Dashboard; unclear what they can/cannot do on Dashboard; lack of understanding of Balances logic; settlement traceability issues | Add payments data to Dashboard that covers typical support scenarios and expose to Finance; better education on payments (operational side); fix root causes to prevent failures; education on Balance behaviours and drivers; education on Settlements; better visibility of settlement delays in Dashboard. Swift response on complex issues: not an issue — handled by Merchant Care today or their AM. |
| **Payments leaders & specialists** | High | Advice on how to optimise payment performance / acceptance rate | Tricky without AM/SE support | Self-serve tools for merchants without dedicated AM/SE — e.g. Payments Intelligent Search (Dashboard Analytics Product team). |

- **Target segment for Care:** **Merchant Ops teams (Support, Risk, Finance)** — low white-glove expectation, high need for fast resolution, data visibility, and education. Our taxonomy and volumes reflect this: PAYMENTS (IN), PAYOUTS, FUNDS AND FEES, plus Fraud & Risk and Disputes, map to the queries these teams raise. Our product and content work should prioritise this persona.
- **Not priority for Care:** **Payments leaders & specialists** — high white-glove expectation; optimise-for-performance advice is managed by Account teams (AM/SE). We do not prioritise this segment; self-serve tools for those without AM/SE sit with Dashboard Analytics Product.

---

## Segment Summary

| Segment | Care Plan Tier | Support Complexity | 2026 Priority |
|---------|---------------|-------------------|---------------|
| **Enterprise (Direct) — Premium** | Premium | Very High | Maintain quality, Phase II features |
| **Enterprise (Direct) — Enterprise** | Enterprise | High | Maintain quality, Phase II features |
| **Enterprise (Direct) — Standard** | Standard | Medium | AI deflection, self-service |
| **Platform** | Varies (Platform-level TBD) | Very High | Primary delivery focus — build the model |
| **Checkout Payfac** | Standard (TBC) | Medium | TBC — timing not confirmed |
| **Card Issuing** | Standard / Enterprise | Medium | Monitor |
| **Identity Verification** | Standard / Enterprise | Medium | Monitor |
| **B2C Consumer** | Consumer (new) | Low-Medium | 2027+ |

> Care tier definitions and SLAs: `01-knowledge-base/products/care-success-plans.md`


## Enterprise — Direct Merchants

### What They Are
The core, established Checkout.com customer segment. These are businesses that integrate directly with Checkout.com's APIs and products to accept payments from their own customers. They have a direct 1:1 relationship with Checkout.com.

**Typical profile**:
- Large-scale merchants: retail, travel, marketplaces, digital goods, fintech
- Sophisticated technical teams with developers managing the integration
- High transaction volumes (small issues = significant financial impact)
- Often have dedicated account managers or customer success contacts

### Support Characteristics
- **High expectations**: Enterprise merchants expect fast response times and deep technical expertise
- **Complex queries**: API integrations, routing configuration, settlement, multi-currency, 3DS
- **Relationship-sensitive**: Escalations can have commercial implications — at-risk merchants may churn
- **Well-resourced**: Usually have developers who can investigate issues on their side before contacting support
- **Multi-market**: Often operating across multiple geographies with varying compliance requirements

### Support Model
- Access to all channels: email, dashboard webform, Intercom Fin AI Agent
- L1 handles initial triage; complex or relationship-sensitive issues escalate to L2
- Account managers may be involved in escalations for high-value merchants
- Checkout.com is direct and sole support provider (no intermediary)

### Key Support Topics
- Payment acceptance (declines, routing, 3DS)
- API and integration troubleshooting
- Settlement and reconciliation
- Fraud and risk configuration
- Chargeback management
- Compliance (PCI, SCA, PSD2)
- Dashboard and reporting

### PM Considerations
- Improvements to self-service docs (checkout.com/docs, api-reference) have high leverage here — these merchants have developers who will use them
- Any product change affecting APIs or integration flows generates Enterprise support tickets
- Contact rate improvements through better error messages, docs, and Fin AI all apply


## Platform — Marketplace Operators

### What They Are
A **Platform** is a Checkout.com merchant that itself operates a marketplace or multi-sided platform, with **sub-merchants (sellers)** beneath it. The Platform is Checkout.com's direct customer; sellers are the Platform's customers.

**Typical profile**:
- Marketplace businesses (e.g. platforms for independent retailers or service providers)
- SaaS platforms that enable their clients to accept payments
- Checkout.com is the payments infrastructure; the Platform builds on top

> For full detail, see `01-knowledge-base/products/platform-segment.md`

### Support Model (Summary)
- Checkout.com acts as **Level 2** — Platforms are L1 to their own sellers
- Platforms may contact Checkout.com for their own issues **or** on behalf of a seller
- When raising on behalf of a seller, the ticket must capture both Platform and seller identity
- Currently the **primary delivery focus for 2026** — the support model for this segment is being built

### Key Difference from Enterprise
| | Enterprise | Platform |
|--|-----------|---------|
| Who contacts us | The merchant themselves | The Platform, often on behalf of a seller |
| Support relationship | Direct | Intermediated |
| Issue attribution | Always clear | May be Platform-level or seller-level |
| Checkout.com role | Sole support | Second-line support |
| Complexity | High | Very High (multi-entity) |


## Checkout Payfac — Direct Sub-Merchant Support *(New, TBC)*

### What They Are
Small merchants that Checkout.com directly supports as the primary Platform or PayFac (Payment Facilitator), or SMB merchants onboarded through a Tier 5 expansion programme. Similar profile to Standard-tier merchants.

### Status
Timing is TBC. This is a named segment in the Care Success Plans but not yet in active delivery.

### Notes
- May offer premium add-ons (faster SLAs, live chat) at extra cost
- Consumer Duty regulatory considerations may apply depending on jurisdiction
- Similar support model to Standard tier


## Card Issuing

### What They Are
Merchants using Checkout.com's **card issuing** capabilities — the ability to issue virtual or physical payment cards to their own customers or employees. These are typically fintechs, corporates, or platforms building card programmes on top of Checkout.com's issuing infrastructure.

**Typical use cases**:
- Corporate expense cards
- Consumer prepaid or debit cards
- Virtual cards for B2B supplier payments (e.g. travel agencies paying hotels)
- Reward or loyalty cards

### Support Characteristics
- **Small segment** currently — low ticket volume
- Issues tend to be around card programme configuration, card lifecycle (issuance, cancellation, limits), transaction authorisation on issued cards, and cardholder disputes
- Technical complexity is high — these customers are builders, not just payment acceptors
- Issuing queries are distinct from acceptance queries and require specialist knowledge

### Support Model
- Access to standard channels
- L2 typically handles issuing queries given technical complexity
- Small enough segment that specialist routing may be informal today

### PM Considerations
- Low volume now — monitor rather than prioritise
- As the issuing product grows, dedicated support tooling and Fin AI coverage will be needed
- Fin AI will need issuing-specific knowledge articles to contain this query type


## Identity Verification

### What They Are
Merchants using Checkout.com's **Identity Verification (KYC/KYB)** product — tools to verify the identity of their end users or business customers as part of onboarding or compliance workflows.

**Typical use cases**:
- Fintech companies verifying new account holders
- Platforms verifying marketplace sellers before they can transact
- Any regulated business needing to confirm customer identity

### Support Characteristics
- **Small segment** currently — low ticket volume
- Issues tend to be around verification workflow configuration, failed verification results, integration with Checkout.com's ID verification APIs, and compliance questions
- Queries are distinct from payment acceptance and require knowledge of the verification product
- Sensitive area — verification failures can block merchants' customers from transacting

### Support Model
- Access to standard channels
- L2 typically handles due to technical and compliance complexity
- Small enough segment that specialist routing may be informal today

### PM Considerations
- Low volume now — monitor rather than prioritise
- Identity Verification is currently a standalone document verification product; planned integration into payment verification in 2027 will change the support model — queries will likely merge into the PAYMENTS (IN) taxonomy rather than sitting as a separate case type
- Cross-segment relevance: Platform merchants may use Identity Verification to onboard their sellers
- Taxonomy note: Identity Verification has its own embedded taxonomy in the current CSV (`support-taxonomy.md`); this will need restructuring at the point of 2027 integration


## B2C Consumer *(2027+)*

B2C support serves **cardholders and end users of Project Braavos** — a distinct model from B2B merchant Ops.

> Competitive research: `01-knowledge-base/strategy/B2C Fintech Support Competitive Analysis.md` — benchmarks Monzo, Revolut, Starling, Zilch, and Klarna for support model design ahead of the 2027 launch.

### What They Are
Two sub-segments under the B2C model:
- **Remember Me**: Users of Checkout.com's consumer card-saving product, accessed via Flow. **Live today** — consumers contact support via a webform on the Remember Me portal; tickets flow into the **Checkout Consumer** Zendesk brand. Volume is <10 tickets/week at this stage.
- **Braavos Neobank**: Customers of Checkout.com's consumer neobank proposition — planned for 2027+

### Support Model
- **Remember Me (live)**: Checkout Consumer Zendesk brand active. Low volume, simple queries (card saving, OTP, purchase history). No AI Agent deployed yet. No formal SLA or tier framework.
- **Braavos (2027+, to be defined)**:
  - AI Agent as primary channel
  - Phone support mandatory (likely regulatory requirement for banking product)
  - Business-hours human coverage
  - Likely requires BPO partner for first-line contact handling
  - SLA within hours
  - Complaint handling as a distinct regulated function (Consumer Duty, 8-week FRL, FOS referral rights)
  - Fundamentally different from B2B — simpler queries, much higher volume, consumer protection obligations
- The Checkout Consumer Zendesk brand is the seed for the Braavos support model — it needs significant configuration expansion to meet Braavos volume and regulatory requirements


## Segment Strategy: Support Cost & Contact Rate

Different segments have different cost profiles and levers:

| Segment | Primary Cost Lever | Primary Contact Rate Lever |
|---------|-------------------|---------------------------|
| Enterprise | Agent efficiency, better tooling | Better docs, Fin AI for common queries |
| Platform | Build the support model correctly (avoid manual rework) | Structured intake (right context first time) |
| Card Issuing | L2 efficiency, specialist knowledge | Help articles for card programme questions |
| Identity Verification | L2 efficiency | Help articles for verification flows |


**Last Updated**: February 2026  
**Owner**: Charlie Wildish
