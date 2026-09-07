# Customer Segments

> Overview of all customer segments supported by Checkout.com's Customer Support (Merchant Care) team. Covers (1) **end customer personas** — who we design for and prioritise (B2B: Ops teams at the merchant; B2C: cardholders and end users of Ray, Open Banking, and Remember Me) — and (2) **business segments** — split first by B2B vs. B2C, then within B2B by White Glove (commercial name: Enterprise — Large Direct, Platforms, Card Issuing) vs. Not White Glove (commercial name: SMB). B2C is Consumer — a separate customer type, not a third value on the White Glove axis.

## Why it matters

Not all contacts cost the same and not all merchants need the same support. Without a clear segment model, Merchant Care cannot make rational decisions about where to invest — whether in AI deflection, agent tooling, self-service, or human coverage — because there is no shared view of who the customer is and what they need.

The segment model provides that foundation. It determines which merchants get which support experience (via Care Success Plans), how contact volumes and costs are attributed, and where product investment will have the most impact. It also sets the boundary between B2B and B2C support — two fundamentally different models with different channels, regulatory requirements, and cost structures.

Getting segments right matters most when the portfolio is growing. Platform is the primary 2026 focus because the support model for that segment doesn't yet exist. B2C is the 2027 challenge, though the regulatory driver differs by product: Open Banking carries UK Consumer Duty obligations from day one; Ray (replacing the now-ended Braavos proposition) is non-custodial and not launching in the UK, so Consumer Duty does not apply there — its regulatory surface is global AML/Travel Rule and KYC instead.

## 2030 Identity: What Support Investment Optimises For

Our support investment matches what's at stake for the customer and for us, not a flat approach. Our customers underpin what support we need to provide.

Across every segment, AI agents resolve routine queries and human agents own judgment. What changes by segment is where that line sits, and how easy it is to reach a human when needed:

- **White Glove (Enterprise: Large Direct, Platforms, Card Issuing).** AI-first, same as every segment. The difference is optionality: more channels, a named contact (Support Engineer, AM), and a faster, more direct path to a human when the AI can't resolve it. Investment, set by Care Plan tier, buys speed and choice of route to a person, not volume of human-handled tickets.
- **Not White Glove (SMB, no AM).** AI-first by design. Human as a tightly controlled fallback. Regulators treat sensitive issues like fund holds or account freezes as existential for this segment: an automated-only response here is a compliance failure, not just a bad experience.
- **B2C Consumer (Remember Me; Ray from 2026/27).** AI-first. Human as a rare, tightly scoped fallback. Success isn't response speed alone: it's whether someone feels safe with their money. Cost tolerance approaches near-zero at scale. For Open Banking, complaint handling and vulnerable-customer identification have to be live at launch (Consumer Duty). For Ray, there's no Consumer Duty equivalent, but the AI-first Care model still routes non-standard cases (KYC failure, complaints) to a human L2 lane by design.

**Open gap**: this identity assumes richer human options scale with Care Plan tier inside White Glove. Today, Growth's channel and SLA entitlements are identical to Essential's — no named contact, no extra channels (see `care-success-plans.md`). Closing that gap, so Growth actually delivers on White Glove's "more optionality" promise, is an open decision, not yet resolved.

## Segment Design Axes

Two axes explain why White Glove, Not White Glove, and B2C need fundamentally different support mechanisms, not just different SLAs. B2B splits into White Glove and Not White Glove; B2C (Consumer) is a separate customer type, not a third value on the same axis:

1. **Authentication enforceability** — can identity verification be required before contact?
2. **Cost tolerance** — how much cost-to-serve can the segment's economics absorb?

| Dimension | White Glove (Enterprise) | Not White Glove (SMB) | B2C Consumer |
|---|---|---|---|
| Authentication | Best-effort — cannot enforce pre-contact (buyer-side team churn, no obligation to pre-register) | 100% required before contact — precondition for automation and security | 100% required before contact — precondition for automation and security |
| Trust anchor | Company + Account Manager relationship, not individual identity | System record (verified user account) | System record (verified user account) |
| Verification approach | In-conversation (transaction/business detail check, AM confirmation) | Login/session-based, pre-contact | Login/session-based, pre-contact |
| Primary resolution | Human-led, AI-assisted (triage, drafting, lookups) | AI-first; human as controlled fallback | AI-first; human as rare, tightly-scoped fallback |
| Cost tolerance | High LTV per account absorbs cost-to-serve | Cost-to-serve must scale down as volume grows | Cost-to-serve must approach near-zero at scale |

This holds uniformly across White Glove's business models (Large Direct, Platforms, Card Issuing) — the AM-anchored trust model doesn't change for Platforms. What changes for Platforms is a separate, orthogonal problem: identifying which sub-merchant an issue is actually about once the Platform's own identity is established (see Platforms below and `01-knowledge-base/products/platform-segment.md`) — an identification/routing gap, not a different authentication or cost model.

## Behavioural Design Axes

The axes above explain segment economics (auth, cost). Three further axes — drawn from persona and segment research already in this knowledge base — describe how segments differ from a user-needs perspective, and should shape support experience design alongside auth and cost:

| Dimension | White Glove (Enterprise) | Not White Glove (SMB) | B2C Consumer |
|---|---|---|---|
| Payments/product literacy | High — sophisticated technical teams self-diagnose before contacting (`customer-personas.md` — Maria, James) | Low — 69% have no dev resource; the dashboard must work as a daily ops tool, not an exception console | Low — relies on others for financial information; expects the app to explain, not require investigation |
| Trust fragility / switching behaviour | Low — AM relationship absorbs single-incident risk; churn is a sustained-relationship decision | Medium-high — switching triggered by failure events (fund holds, freezes), not routine comparison; no cash reserve to absorb delay | High — a single unresolved experience can end the relationship (Jordan, Ray); near-zero switching cost |
| Emotional register required | Efficiency-driven — "give me a fix that actually works," not reassurance (Maria: *"we need recommendations that actually solve the problem"*) | Survival-stakes, no-buffer — a payment outage or fund freeze threatens the business directly; the contact is often the owner, not a delegated employee, so urgency is immediate and personal | Safety/anxiety-driven — reassurance about money safety and control, not just efficiency (Jordan's primary anxiety: *"lack of visibility or control over finances"*) |

**Design implications — foundational, not AI-agent-specific:**

These axes are content and experience design problems first. Fin, Dashboard, Guide/Help Centre, and agent macros/SOPs are all *surfaces* that consume the same underlying content and tone decisions — the tiering has to be designed once, at the content layer, then surfaced consistently everywhere the customer already is. Fin is a messenger for this content, not the place the design decision gets made.

**Boundary with Care Success Plans**: Success Plans controls channel and SLA entitlement only (which door a customer walks through, how fast they get a response). Content depth and tone are applied downstream, inside the channel, by Fin's reply generation and Agent Consultant's suggested replies/actions — not by Success Plans. Keep these separate: Success Plans should not absorb content/experience scope.

- **Literacy → a content architecture, authored once per tier, surfaced everywhere.** The same underlying explanation (e.g. a decline reason) needs to exist in multiple literacy tiers — technical/API-referenced for White Glove (Enterprise), plain-language for Not White Glove (SMB), translated for Platform sub-merchants (who see Checkout only through the Platform's own UI — Checkout doesn't control that surface directly, so the content handed to the Platform to relay is itself a design decision), safety-reassuring for B2C. Author the tiers as structured content once; every surface (Dashboard transaction/error pages, Guide articles, agent macros, Fin) pulls from the same source rather than each channel inventing its own version.
- **Trust fragility → a proactive-surfacing decision, not a resolution-speed decision.** For Not White Glove (SMB) and B2C, the highest-leverage design move is reaching the customer before they need to contact anyone — in-app/Dashboard notifications ahead of a known failure, using Reflex-style insight to know what to surface and when. That's a product/UX placement decision (where does the warning appear, in which channel, before which action), not something Fin can solve by answering faster. For White Glove (Enterprise), the AM relationship already buffers single incidents, so the higher-leverage design investment is AM-facing escalation visibility instead.
- **Emotional register → a tone system owned by content design, applied uniformly.** Continuity/urgency framing for Not White Glove (SMB), safety-and-control framing for B2C, efficiency framing for White Glove (Enterprise) — this is a style and tone framework the Content Strategist defines once, then applies consistently across agent SOPs/macros, Dashboard copy, Guide articles, and Fin phrasing. It is a content design system decision, not a per-surface or per-AI-agent one.

## Business Model Axis

A fourth axis, distinct in kind from the three above: **business model** — is the merchant a Large Direct merchant, a Platform, or a Card Issuing customer (see the Business Model detail under White Glove below). This is a sub-attribute *within* the primary White Glove / Not White Glove segments, not a segment itself. Naming it as its own axis makes explicit what it actually controls.

**What it controls is different from literacy, trust fragility, and emotional register.** Those three axes govern *how* a piece of content is presented — depth, tone, register — for what is often the same underlying issue. Business model governs *which* content is even relevant in the first place. A Platform's sub-merchant lookup procedure and a Card Issuing customer's card lifecycle procedure aren't a differently-toned version of a Direct merchant's decline/settlement content — they're a different knowledge set, most of which doesn't apply outside that business model. This is a content-routing/retrieval concern, not a presentation concern.

**Stack implication**: business model is the second input Fin and Agent Consultant need at the point of reply generation, alongside literacy/tone. Literacy and tone shape *how* a reply reads; business model shapes *which* procedure set or knowledge base gets searched before any reply is drafted — Platform Procedures vs. standard Procedures vs. Issuing Procedures for Fin; the equivalent SOP set for Agent Consultant to surface to a human agent. Same ownership boundary as the Behavioural Design Axes above: this is Fin/Agent Consultant's job at the generation layer, not Care Success Plans'.

**Scoping — modelled mainly within White Glove for now, but not exclusive to it.** Today's build focus and documentation (Large Direct / Platforms / Card Issuing, below) sits inside White Glove (Enterprise), consistent with the working assumption that Platform and Card Issuing customers are White Glove by default. But business model is orthogonal to Care Plan tier and to AM presence — a Platform or Issuing customer without an AM (Not White Glove / Essential, Tier 5+) is unconfirmed today, not structurally impossible. Treat the White-Glove-only scoping as a working choice driven by where the data and build work currently is, not a rule that Platform/Issuing can't occur in Not White Glove — revisit if that population turns out to exist in volume.

## End merchant customer personas (Merchant Care context)

**We solve for Ops teams at the merchant:** Support, Risk, and Finance. This is **B2B support only** — the personas and taxonomy below describe who contacts Merchant Care from our business (merchant) customers. B2C support (separate model) will serve **cardholders and end users of Ray, Open Banking, and Remember Me**. Who contacts us (and what they contact us about) is reflected in our taxonomy and in contact volumes — Case Types and Issue Types map to these three Ops domains. See `01-knowledge-base/processes/support-taxonomy.md` for the full taxonomy and volume view.

Within our B2B merchants, the people who contact or could be served by Merchant Care fall into two broad **end merchant customer** segments. This framing clarifies who we design for and who we do not prioritise.

*Note: "white-glove servicing" in the table below is a persona-level expectation (does this individual role expect hands-on treatment), unrelated to the account-level White Glove / Not White Glove primary segment split defined later in this document (Account Manager presence). Don't conflate the two — a Merchant Ops contact at a White Glove (Enterprise) account is still "low white-glove servicing" in the sense meant here.*

| Segment | White glove servicing | Need | Pain points | Opportunities |
|--------|------------------------|------|-------------|---------------|
| **Merchant Ops teams (Support, Risk, Finance)** | Low | Solve transaction-based queries from their customers quickly; solve regional (e.g. MENA) transaction issues; swift response on complex transaction issues; visibility on Balance & Settlement payouts | Data gaps in Dashboard and data APIs for key data; diagnosing transaction issues not intuitive in Dashboard; unclear what they can/cannot do on Dashboard; lack of understanding of Balances logic; settlement traceability issues | Add payments data to Dashboard that covers typical support scenarios and expose to Finance; better education on payments (operational side); fix root causes to prevent failures; education on Balance behaviours and drivers; education on Settlements; better visibility of settlement delays in Dashboard. Swift response on complex issues: not an issue — handled by Merchant Care today or their AM. |
| **Payments leaders & specialists** | High | Advice on how to optimise payment performance / acceptance rate | Tricky without AM/SE support | Self-serve tools for merchants without dedicated AM/SE — e.g. Payments Intelligent Search (Dashboard Analytics Product team). |

- **Target segment for Care:** **Merchant Ops teams (Support, Risk, Finance)** — low white-glove expectation, high need for fast resolution, data visibility, and education. Our taxonomy and volumes reflect this: PAYMENTS (IN), PAYOUTS, FUNDS AND FEES, plus Fraud & Risk and Disputes, map to the queries these teams raise. Our product and content work should prioritise this persona.
- **Not priority for Care:** **Payments leaders & specialists** — high white-glove expectation; optimise-for-performance advice is managed by Account teams (AM/SE). We do not prioritise this segment; self-serve tools for those without AM/SE sit with Dashboard Analytics Product.

---

## Segment Summary

**Primary segment is White Glove / Not White Glove (AM presence). Enterprise and SMB are the commercial/Salesforce-facing names for those two primary segments, not segments in their own right.** Business model (Large Direct / Platform / Card Issuing) is a sub-attribute within each primary segment, not a segment.

| Primary Segment | Commercial Name | Business Model (sub-attribute) | Care Plan Tier | Support Complexity | 2026 Priority |
|---|---|---|---|---|---|
| **White Glove** | Enterprise | Large Direct | Premium / Enterprise / Growth — set by processing volume and potential | Medium – Very High (varies by tier) | Premium/Enterprise: maintain quality, Phase II features. Growth: AI deflection, self-service |
| **White Glove** | Enterprise | Platforms | Premium / Enterprise / Growth — set by processing volume and potential (platform-level tiering TBD) | Very High | Primary delivery focus — build the model |
| **White Glove** | Enterprise | Card Issuing | Premium / Enterprise / Growth — set by processing volume and potential (currently observed at Growth/Enterprise) | Medium | Monitor |
| **Not White Glove** | SMB | Unconfirmed — assumed Large Direct-only today (see working assumption below) | Essential (Tier 5+, no AM) (TBC) | Medium | end 2027 |
| *(outside this axis — separate customer type)* | B2C Consumer | N/A — consumer, not merchant | Consumer (new) | Low-Medium | 2027+ |

> Care tier definitions and SLAs: `01-knowledge-base/products/care-success-plans.md`
> B2C sits outside the White Glove / Not White Glove axis entirely — Account Manager relationships are a B2B commercial concept and don't apply to individual consumers. See B2C Consumer section below.


## White Glove (has an Account Manager)

**Commercial/Salesforce-facing name: Enterprise.**

**Defining criterion: has an Account Manager.** Not revenue, not business model, not Care Plan tier — AM presence. Premium, Enterprise, and Growth (Tier 3–4) all have an AM. This is the primary segment; "Enterprise" is the label used in Care Success Plans, Sales, and Salesforce for it. Not White Glove, below, is the no-AM counterpart (commercial name: SMB).

**Care Plan Tier is a separate axis from business model, and from the White Glove split itself.** Premium, Enterprise, and Growth tiers are set by processing volume and potential processing volume. Growth (Tier 3–4) is the White Glove tier at baseline entitlement level; it is now a formal, separate plan line from Essential (Tier 5+, no AM) in `care-success-plans.md`, split specifically on AM presence. Care Plan tier governs SLA and channel entitlement; the White Glove / Not White Glove split governs which segment-design axes (auth, literacy, tone — see Segment Design Axes and Behavioural Design Axes above) apply. Essential's SLA/channel entitlements are currently identical to Growth's, pending a separate decision on whether to differentiate them.

**Working assumption for Platform and Card Issuing: White Glove by default, unproven.** Large Direct merchants without an AM are straightforwardly Not White Glove (SMB/Essential). Platform and Card Issuing customers without an AM haven't been assessed against this boundary — treat them as White Glove for now rather than reclassifying by AM presence alone. The sub-merchant intermediation complexity that defines Platform doesn't disappear if the Platform itself lacks an AM, and there's no volume data yet on how many Platform/Issuing accounts sit in Not White Glove (Essential, Tier 5+). Revisit once that data exists.

### Business Model (sub-attribute within White Glove — see Business Model Axis above)

Business model — Large Direct, Platform, or Card Issuing — is an attribute *within* White Glove, not a separate segment. It determines content routing (which knowledge/Procedures apply), distinct from the White Glove/Not White Glove split, which determines auth/literacy/tone. Care's role across all three is specialist and judgment-led, not AI-deflection-first. AI supports the specialist; it doesn't replace the interaction. What differs across the three is where each sits on the build-versus-maintain-versus-monitor spectrum, not the support model itself:

- **Large Direct Merchants** — mature and scaling. Quality holds; the infrastructure behind it (specialist capacity, AI-assisted context) scales independently of headcount as volume grows.
- **Platforms** — the business model where the support model doesn't exist yet. Primary 2026 build focus.
- **Card Issuing** — flat and monitor-only. Specialist L2 handling, no active 2026 roadmap.

### Large Direct Merchants

#### What They Are
The core, established Checkout.com customer segment. These are businesses that integrate directly with Checkout.com's APIs and products to accept payments from their own customers. They have a direct 1:1 relationship with Checkout.com.

**Typical profile**:
- Large-scale merchants: retail, travel, marketplaces, digital goods, fintech
- Sophisticated technical teams with developers managing the integration
- High transaction volumes (small issues = significant financial impact)
- Often have dedicated account managers or customer success contacts

#### Support Characteristics
- **High expectations**: Enterprise merchants expect fast response times and deep technical expertise
- **Complex queries**: API integrations, routing configuration, settlement, multi-currency, 3DS
- **Relationship-sensitive**: Escalations can have commercial implications — at-risk merchants may churn
- **Well-resourced**: Usually have developers who can investigate issues on their side before contacting support
- **Multi-market**: Often operating across multiple geographies with varying compliance requirements

#### Support Model
- Access to all channels: email, dashboard webform, Intercom Fin AI Agent
- L1 handles initial triage; complex or relationship-sensitive issues escalate to L2
- Account managers may be involved in escalations for high-value merchants
- Checkout.com is direct and sole support provider (no intermediary)

#### Key Support Topics
- Payment acceptance (declines, routing, 3DS)
- API and integration troubleshooting
- Settlement and reconciliation
- Fraud and risk configuration
- Chargeback management
- Compliance (PCI, SCA, PSD2)
- Dashboard and reporting

#### PM Considerations
- Improvements to self-service docs (checkout.com/docs, api-reference) have high leverage here — these merchants have developers who will use them
- Any product change affecting APIs or integration flows generates Enterprise support tickets
- Contact rate improvements through better error messages, docs, and Fin AI all apply


### Platforms

#### What They Are
A **Platform** is a Checkout.com merchant that itself operates a marketplace or multi-sided platform, with **sub-merchants (sellers)** beneath it. The Platform is Checkout.com's direct customer; sellers are the Platform's customers.

**Typical profile**:
- Marketplace businesses (e.g. platforms for independent retailers or service providers)
- SaaS platforms that enable their clients to accept payments
- Checkout.com is the payments infrastructure; the Platform builds on top

> For full detail, see `01-knowledge-base/products/platform-segment.md`

#### Support Model (Summary)
- Checkout.com acts as **Level 2** — Platforms are L1 to their own sellers
- Platforms may contact Checkout.com for their own issues **or** on behalf of a seller
- When raising on behalf of a seller, the ticket must capture both Platform and seller identity
- Currently the **primary delivery focus for 2026** — the support model for this segment is being built

#### Key Difference from Large Direct Merchants
| | Large Direct | Platform |
|--|-----------|---------|
| Who contacts us | The merchant themselves | The Platform, often on behalf of a seller |
| Support relationship | Direct | Intermediated |
| Issue attribution | Always clear | May be Platform-level or seller-level |
| Checkout.com role | Sole support | Second-line support |
| Complexity | High | Very High (multi-entity) |


### Card Issuing

#### What They Are
Merchants using Checkout.com's **card issuing** capabilities — the ability to issue virtual or physical payment cards to their own customers or employees. These are typically fintechs, corporates, or platforms building card programmes on top of Checkout.com's issuing infrastructure.

**Typical use cases**:
- Corporate expense cards
- Consumer prepaid or debit cards
- Virtual cards for B2B supplier payments (e.g. travel agencies paying hotels)
- Reward or loyalty cards

#### Support Characteristics
- **Small segment** currently — low ticket volume
- Issues tend to be around card programme configuration, card lifecycle (issuance, cancellation, limits), transaction authorisation on issued cards, and cardholder disputes
- Technical complexity is high — these customers are builders, not just payment acceptors
- Issuing queries are distinct from acceptance queries and require specialist knowledge

#### Support Model
- Access to standard channels
- L2 typically handles issuing queries given technical complexity
- Small enough segment that specialist routing may be informal today

#### PM Considerations
- Low volume now — monitor rather than prioritise
- As the issuing product grows, dedicated support tooling and Fin AI coverage will be needed
- Fin AI will need issuing-specific knowledge articles to contain this query type


## Not White Glove (no Account Manager) *(New, 2027)*

**Commercial/Salesforce-facing name: SMB.**

**Defining criterion: no Account Manager.** The no-AM counterpart to White Glove above — not a revenue label, not a size label. "SMB" is the commercial name Care Success Plans, Sales, and Salesforce use for it. Maps to the Essential Care Plan tier (Tier 5+) in `care-success-plans.md`.

**Business model within Not White Glove is unconfirmed.** Today's documented population here is assumed Large Direct-only (small merchants and Payfac/Tier 5 expansion accounts). Whether Platform or Card Issuing customers exist in this segment (i.e. a Platform or Issuing account with no AM) is the same open data gap flagged in the White Glove working assumption above — not ruled out, just unobserved.

### What They Are
Small merchants that Checkout.com directly supports as the primary Platform or PayFac (Payment Facilitator), or SMB merchants onboarded through a Tier 5 expansion programme.

### Status
Timing is 2027 for the dedicated Payfac/Tier 5 expansion acquisition programme. Essential (the Care Plan tier — formerly described as "SMB" in Care Success Plans) is already active for Tier 5+ merchants in the book today; only the new acquisition motion is not yet in active delivery.

### How SMBs Think About Payments (research findings)
*Source: internal qual + quant synthesis — 5 In-Market Decision Makers interview transcripts (2023, named participants: Offsetted, Myra, Subjektiv, StylishAccessoriesShop, Hafven) + SMB Discovery Survey (Feb 2022, n=253). Credibility: Medium-High — qual and quant triangulate on core findings; AI-assisted synthesis, review before citing externally. Full findings, verbatim quotes, and pricing analysis: `01-knowledge-base/products/smb-research-findings.md`.*

SMBs do not self-identify as "SMB" — they describe themselves by business type and immediate problem, and treat payments as one operational job among many (finance, hiring, marketing) rather than a distinct category.

| Finding | Evidence | Implication for Care/product |
|---|---|---|
| **Self-serve, zero-dev onboarding is non-negotiable** | 69% of SMBs have no development resource (43% self-serve setup, 26% need only PSP technical support; Q79, n=253) | Any support or onboarding flow requiring API integration as the primary path loses most of this segment before a transaction is processed |
| **Checkout.com has a critical brand awareness gap** | Checkout.com recognised by 5.23% of surveyed SMBs vs. Stripe (79%) and PayPal (~100%) (Q67) | Direct/cold acquisition is not viable at current awareness; distribution must be platform-native (embedded in Wix, WooCommerce, GoDaddy) or via co-marketing until brand recognition improves |
| **No monthly fee is a hard filter**, not a preference | 3 of 5 qual participants; corroborated in survey free-text (Q52, Q68) — pay-as-you-earn is the expected model, especially for pre-revenue/seasonal businesses | Pricing/packaging for this segment should default to transaction-only fees; a monthly platform fee disqualifies early-stage SMBs outright |
| **The dashboard is a daily business-ops tool, not an exception console** | Live balance visibility rated extremely/very important by 79% (Q74); "send single invoices" ranked the #1 dashboard capability by 45.2% (Q78) | Minimum viable SMB dashboard = today's sales → expected settlement → send an invoice. Everything else is secondary |
| **Settlement accounts are sticky; PSP switching is not evaluated on an ongoing basis** | 72% never change settlement bank account (Q76); qual: switching cost is perceived as near-zero but only acted on given a materially better offer *and* zero friction | Once embedded, incumbents (Stripe/PayPal) hold structural advantage. Switching triggers are failure events (fund freeze, decline) or a frictionless, clearly-better offer — not routine comparison shopping |
| **Payment method defaults are market-specific** (unresolved gap) | Qual only (1 of 5): SEPA direct debit is table stakes in Germany; survey instrument's card-centric framing doesn't capture this | Treat as an unvalidated risk for any EEA go-to-market — do not assume card-first checkout is sufficient |
| **PSP brand/logo is a conversion signal SMBs pass to their own customers** | 2 of 5 qual participants; corroborated in survey free-text | Checkout.com's low brand awareness compounds here — a low-recognition badge provides weaker trust signal at the SMB's own checkout, which is a circular disadvantage against Stripe/PayPal |
| **Responsive support is a continuity requirement, not a premium tier** | 2 of 5 qual participants; corroborated in survey open-text (Q52, Q80) | Framing fast support as a paid upsell misreads this segment — a payment outage during live trading is unrecoverable revenue for an SMB |

**Pricing behaviour (from the same research):**
1. SMBs filter on fee *structure* before comparing rates — a monthly fee disqualifies regardless of the transaction rate.
2. Price is evaluated as part of a bundle (settlement speed, integration ease, support), not in isolation.
3. Free-to-start pricing drives long-term retention once the product proves out.
4. The switching threshold is "noticeably better," not "marginally cheaper" — comparison happens at initial selection, rarely after.
5. High price is tolerated when the PSP solves a non-substitutable compliance/workflow problem (e.g. a German SMB paying €700/month to Stripe for invoicing compliance it couldn't get cheaper elsewhere).

**Research gaps (unanswered by either source):** how SMBs self-categorise using the term "small business"; offline-first SMBs (card readers, SoftPOS); post-2022 PSP market share shifts (Stripe fee changes, Shopify Payments growth); what triggers an active PSP search vs. defaulting to a platform-bundled option.

### Industry-Wide SMB Support Pain Points (market context)
*Source: third-party market research synthesis ("The Friction Paradigm," AI-assisted, web-sourced — general PSP industry, not Checkout-specific). Use as directional market context, not primary evidence; verify any figure before citing externally.*

Broader industry data frames why SMB/mid-market merchants churn from PSPs, and where a differentiated support model could compete:

- **Account freezes and fund holds** are the most severe failure mode. PayFac-model PSPs (Stripe, PayPal, Square) use automated, low-context risk decisioning that can freeze accounts and hold funds 90–180 days with minimal human explanation — an existential risk for SMBs with no cash reserve.
- **Visa VAMP 2026 / Mastercard BRAM/ECM** tightened dispute-ratio thresholds sharply (e.g. Visa's "Excessive" tier dropped from 2.20% to as low as 0.90% for some tiers), with network fines that can reach $50,000+/month. SMBs lack the tooling (3DS2 configuration, Verifi RDR, Ethoca, representment evidence assembly) to manage this without consultative support.
- **The "Support Valley of Death"**: PSPs gate dedicated technical account management behind $50M+ annual volume, leaving mid-market merchants ($1M–$50M) — who have genuinely complex needs (multi-currency reconciliation, fraud routing, orchestration) — stuck in the same self-service queues as micro-merchants.
- **Fee opacity**: headline rates (e.g. Stripe's 2.9% + $0.30) understate effective cost once FX, subscription billing, invoicing, and dispute fees stack up — cross-border effective rates can reach 7.8–12.3%, driving reconciliation mistrust.
- **B2B reconciliation gap**: legacy payment messaging (SWIFT MT) truncates remittance data, forcing manual AR matching. The ISO 20022 migration (CBPR+ coexistence ends Nov 2025) offers structured data PSPs could expose in dashboards but mostly haven't yet.
- **AI/chatbot deflection is under regulatory pressure**: the CFPB has flagged "doom loop" chatbots that fail to escalate on financial disputes as a potential UDAAP violation; the FCA's Consumer Duty (in force since July 2023, applies to micro-enterprises) explicitly warns against disproportionate automated account freezes without human review.
- **Segmentation matters**: micro-merchants (<$100k) need fast, transparent risk communication (they can't survive a fund hold); mid-market SMBs ($1M–$50M) need consultative technical/compliance support currently reserved for enterprise tiers.

**Whitespace this suggests** (industry-level, not yet validated for Checkout.com): unbundling TAM-style support from high volume thresholds; dispute-management-as-a-service; human-in-the-loop risk communication ahead of freezes; surfacing ISO 20022 structured data for SMB reconciliation.

### Regional Regulatory Requirements for SMB Support
*Source: third-party regulatory research synthesis (general PSP industry, not Checkout-specific). Directional context — verify against current regulation and legal guidance before citing in a PRD or compliance-facing document.*

SMBs, particularly micro-enterprises, carry consumer-like regulatory protections in every major market Checkout.com operates in. Treating SMB support as unregulated B2B is a compliance risk, not just a UX gap.

| Region | Primary framework | SMB definition covered | Key operational mandate |
|---|---|---|---|
| UK | FCA Consumer Duty & DISP | Turnover < £6.5M, < 50 staff (micro-enterprise: turnover < €2M, < 10 staff) | Anti-"sludge practice" rules (no hiding phone numbers or dispute channels); formal complaints acknowledged and resolved within 15 business days; FOS access |
| EU | PSD2 Articles 30 & 61 (PSD3/PSR incoming) | Micro-enterprises: turnover < €2M, < 10 staff | Consumer-level rights by default (cannot be waived by contract); EBA-mandated 15 business day final response, extensible to 35 days only for exceptional technical reasons; free access to internal complaints process and an EDR scheme (e.g. FIN-NET) |
| US | CFPB / FTC UDAAP, state commercial disclosure laws (CA, NY, UT, VA), card scheme rules | Micro and mid-market merchants | Fee transparency and accessible support channels; card network SLAs on dispute processing and chargeback response windows |
| Australia | ASIC & AFCA scheme rules | Credit facilities up to $5M AUD or up to 100 employees | Free external ombudsman (AFCA) access for unresolved disputes; baseline cover for outages and unauthorised transactions |

### AI vs. Human Support: Regulatory Boundaries
Regulators across all four regions above prohibit fully automated support in three areas, regardless of how capable the AI is:

1. **Anti-"doom loop" rules (US CFPB, UK FCA).** Blocking or delaying escalation to a human during an active financial dispute is a UDAAP violation in the US and a Consumer Duty breach in the UK. AI must offer an immediate, visible path to a human at all times.
2. **Account freezes, reserves, and terminations (GDPR Art. 22).** Merchants have the right to a meaningful human review of automated decisions that significantly affect them financially. A human reviewing and rubber-stamping the AI's output does not satisfy this — the review has to be substantive.
3. **Formal complaint sign-off (15 business day statutory window, UK/EU).** AI can draft responses and collate evidence, but the final decision on a formal complaint — fee waivers, compensation, legal determinations — requires sign-off from a qualified human.

| Support domain | AI-automatable | Human required | Why |
|---|---|---|---|
| API integration & gateway setup | Yes | No | Technical support with no financial or legal harm risk |
| Chargeback evidence collation | Yes | No | Document gathering for card brand submission, not a decision |
| Account holds & appeals | Partial | Mandatory | GDPR Art. 22 requires substantive human review |
| Formal complaint sign-off | Partial | Mandatory | Binding statutory response requires compliance sign-off |
| Distressed merchant management | No | Mandatory | Vulnerable-customer handling requires human judgment and discretion |

**Design implications for Fin/Consumer Care:**
- Keep a visible, one-click human off-ramp in every AI chat surface, not buried behind menus.
- Configure automated hand-off triggers on keywords like "complaint," "ombudsman," "lawyer," "frozen funds," or detected frustration.
- Log which human reviewed and approved any account action, reserve change, or complaint resolution — an audit trail is the compliance evidence, not just good practice.
- Segment by entity size: route micro-enterprises through the stricter consumer-like SLA and escalation path by default; negotiated B2B terms can only apply where the merchant doesn't qualify for micro-enterprise protections.

This directly informs Open Banking's Consumer Duty readiness noted in the B2C Consumer section below — that product needs the anti-doom-loop and Art. 22 review paths live before launch, not retrofitted after. Ray, by contrast, is not UK-launched and carries no Consumer Duty obligation, though its own AI-first model still routes non-standard cases to a human L2 lane by design (see Ray Ops & Care manual).

### Notes
- May offer premium add-ons (faster SLAs, live chat) at extra cost
- Consumer Duty regulatory considerations apply depending on jurisdiction — see Regional Regulatory Requirements above for specifics by region
- Same support model as the Essential Care Plan tier (Tier 5+, no AM)
- Both research sources above carry an AI-assisted-synthesis disclaimer — treat findings as directional inputs to segment/product design, not final citations, until validated against current data


## B2C Consumer *(2027+)*

B2C support serves **cardholders and end users of Ray, Open Banking, and Remember Me** — a distinct model from B2B merchant Ops.

**Braavos (ended 2026-08-18)**: Checkout.com's earlier consumer neobank proposition. Ray is going ahead in its place — see `05-archive/2026/prds/braavos-care/README.md` for what changed. Where Braavos content below (competitive research, Consumer Duty framing) is cited historically, it does not automatically transfer to Ray.

> Competitive research: `01-knowledge-base/strategy/B2C Fintech Support Competitive Analysis.md` — benchmarks Monzo, Revolut, Starling, Zilch, and Klarna for support model design; written for Braavos's neobank model — re-validate applicability to Ray (a non-custodial crypto wallet, not a neobank) before reusing.
> Source for Ray and Open Banking detail below: `04-active-work/meeting-notes/2026-07/2026-07-13-consumer-support-asks-mapping.md` and the Ray Ops & Care Operating Manual. A third consumer product, Brazil/FX remittance, is in the same launch wave but isn't detailed here — see that meeting note.

### What They Are
Three active sub-segments under the B2C model:
- **Remember Me**: Users of Checkout.com's consumer card-saving product, accessed via Flow. **Live today** — consumers contact support via a webform on the Remember Me portal; tickets flow into the **Checkout Consumer** Zendesk brand. Volume is <10 tickets/week at this stage.
- **Ray**: Checkout.com's consumer stablecoin wallet + USD Visa card (owned by Max, Oliver, Luca, Fabio). **Non-custodial** — the user legally owns the wallet and its assets; Ray administers key management but Care can never freeze, seize, or move assets, or retrieve/reset keys. **Not launching in the UK** — no Consumer Duty exposure; regulatory surface is global AML/Travel Rule and KYC (via Ubble), Compliance-owned. Milestones: internal launch end Dec 2026 (50–100 people), external beta end Q1 2027. UAE is the #2 year-1 market (Arabic knowledge base needed; 6 launch languages total). *Volume/headcount model: TBD — waiting on accurate numbers from the Ray team. An earlier estimate existed but predates the Ray Ops & Care manual and is not accurate; not carrying it forward.*
- **Open Banking**: Consumer payment initiation and account information services, built on token.io (subcontracted via Modulr). Falls under **UK Consumer Duty** — once Checkout contracts directly with the payer, a consumer can complain about end-to-end service failure even where token.io or the payer's bank caused it. Data access via token.io/Modulr is locked down; the level of access Checkout actually has is unconfirmed.

### Ray: Wallet Architecture & End-User Context (Web3 Market Research)
*Source: third-party Web3 wallet ecosystem research synthesis (AI-assisted, web-sourced — general market landscape, not Checkout/Ray-specific). Directional context only — validate against the Ray Ops & Care manual and actual product architecture before citing in a PRD or compliance-facing document.*

Ray's model (non-custodial, Ray administers key management, Care cannot freeze/seize/move assets or retrieve/reset keys) matches the **MPC/smart-account embedded wallet** category in this research (comparable to Privy, ZenGo, Coinbase Smart Wallet, Fibo), not a legacy seed-phrase wallet:
- **No single point of key failure by design**: MPC splits key shards across the user's device, Ray's infrastructure, and (where used) a recovery service — no seed phrase for the user to lose, and no single party (including Care) holds a complete key. This is the architectural reason Care cannot reset or retrieve keys, not a policy choice — worth stating explicitly in KYC/recovery Care content so agents don't imply a reset is possible but withheld.
- **Recovery is MFA/biometric/cloud-enclave based, not seed-phrase based**: aligns with the Deposit & recovery lane's likely query pattern — users asking to "recover my wallet" should be routed to device/biometric/passkey recovery flows, not seed-phrase troubleshooting.
- **Target end-user profile matches this research's "Global Payment and Stablecoin Users" segment**: low-to-moderate technical tolerance, expects fintech-app-like UX (comparable to Venmo/Revolut), wants local fiat-currency display alongside stablecoin balances, and card checkout integration — consistent with Ray's USD Visa card pairing and with the "Safety/anxiety-driven" emotional register and low-literacy assumption already documented for B2C Consumer above.
- **Where support risk actually sits for this architecture**: this wallet category's failure modes are infrastructure-side (smart contract bugs, signing-relay/bundler downtime, cloud provider outages) rather than user error (lost seed phrase) — reinforces why Ray's Care model routes non-standard cases to a human L2 lane rather than expecting AI-only resolution of "my funds aren't showing" type queries.
- **Fee/gas sponsorship model is typically near-zero or sponsored** in this wallet category — relevant context for the "pricing/FX transparency" and "unclear exchange rate" query types already listed for Ray; users in this segment expect transparent, near-invisible fees and will flag any FX/gas cost they can't map to a familiar fintech mental model.

### Support Model
- **Remember Me (live)**: Checkout Consumer Zendesk brand active. Low volume, simple queries (card saving, OTP, purchase history). No AI Agent deployed yet. No formal SLA or tier framework.
- **Ray (internal Dec 2026 / external beta Q1 2027)**: AI-first by design per the Ray Ops & Care manual — AI L1 resolves across all 6 launch languages, escalating to a single L2 human queue (lanes: KYC, Deposit & recovery, Disputes, Account ops, Complaints, Data rights) and/or BPO overflow. Target AI L1 resolution ≥70% by GA, but no Fin deflection rate is yet committed in headcount planning — capacity is still modelled on gross contact volume pending that reconciliation. Query types: deposits, declines, fees, verification/KYC, tax ID or name mismatch, verification delays, pricing/FX transparency, unclear exchange rate, double payment, misdirected-deposit recovery. Headcount modelled in Mexico, Dubai, Mauritius, plus 1-2 in UK for treasury/transaction investigations (staff location, not a UK market launch).
- **Open Banking (timing TBC)**: Query types: consent/disclosure, unauthorised payments, wrong amount/duplicate, wrong beneficiary, failed/missing/delayed transfers, refund issues, fraud/scams, AIS consent (90-day limit), bank-selection confusion (pay-by-bank vs. card), servicing complaints. Headcount ownership not yet agreed: the Braavos team was its presumed home and that programme has ended.
- The Checkout Consumer Zendesk brand is the seed for the Ray and Open Banking support models — it needs significant configuration expansion to meet combined volume and regulatory requirements

**Open risk (2026)**: as of the 2026-07-13 mapping, Ray and Open Banking had landed on Care with no product-side definition of users, query types, CRM, authentication, or data access — Care was reverse-engineering requirements the product owners hadn't yet supplied. Data access remains a blocker for Open Banking (token.io/Modulr lock-down) and was a blocker for Ray pending system access; the Ray Ops & Care manual (received 2026-08-18) resolves much of Ray's Care-model ambiguity but not the volume/headcount reconciliation above. Ray's milestones (internal Dec 2026, external beta Q1 2027) are now confirmed in `2026 deliverables.md`; Open Banking and Brazil/FX timing remain a working assumption from the meeting note above — check `2026 deliverables.md` before citing a settled date for those.


## Segment Strategy: Support Cost & Contact Rate

Different segments have different cost profiles and levers:

| Segment (White Glove — Business Model) | Primary Cost Lever | Primary Contact Rate Lever |
|---------|-------------------|---------------------------|
| White Glove — Large Direct | Agent efficiency, better tooling | Better docs, Fin AI for common queries |
| White Glove — Platforms | Build the support model correctly (avoid manual rework) | Structured intake (right context first time) |
| White Glove — Card Issuing | L2 efficiency, specialist knowledge | Help articles for card programme questions |


**Last Updated**: July 2026  
**Owner**: Charlie Wildish
