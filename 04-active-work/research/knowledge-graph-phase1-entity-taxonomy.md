# Knowledge Graph Layer — Phase 1: Entity Taxonomy

> **Goal**: Produce a stable, canonical list of entity classes and entities derived from the existing support contact taxonomy. No graph structure yet — this is the vocabulary the graph will be built on.
>
> **Sources**:
> - `01-knowledge-base/processes/support-taxonomy.md` (V3, February 2026) — entity classes 1–3, 7–8
> - `Product category and name definitions - Sheet1.csv` (April 2026, new source of truth) — entity classes 4–6
> - `01-knowledge-base/products/customer-segments.md` — entity class 10
>
> **Scope**: B2B support only. The B2C taxonomy does not yet exist — B2C (Consumer/Braavos) is excluded from all phases until that taxonomy is defined (2027+). See note under Class 10.
>
> **Resolution scope**: All resolution actors — Fin (autonomous AI), Agent Consultant (AI-assisted human), Human L1, Human L2, External. The graph does not model Fin in isolation. It models the knowledge and data required to resolve each Reason across the full actor stack. See Classes 11–13.
>
> **Owner**: Charlie Wildish (draft); Content team (knowledge assets); Process Architect (SOPs/playbooks); Engineering (data integrations)
> **Status**: Draft — not yet validated against Fin query data or agent SOP content

---

## Entity Classes

Thirteen entity classes in total. Classes 1–3 map directly to the taxonomy's three-level structure. Classes 4–6 are sourced from the canonical product catalogue CSV. Classes 7–9 are implicit in the taxonomy and need to be surfaced explicitly. Class 10 was added in the April 2026 design review — the original 9-class list omitted segment context, which is required for routing differentiation. Classes 11–13 were added to extend the graph beyond Fin to the full resolution actor stack (Fin, Agent Consultant, Human agents).

| # | Entity Class | Description | Source |
|---|---|---|---|
| 1 | **Domain** | Top-level support area. Equivalent to Case Type. | Taxonomy — Case Type |
| 2 | **Problem Type** | Structured problem category within a domain. Equivalent to Issue Type. | Taxonomy — Issue Type |
| 3 | **Reason** | Specific problem statement. Leaf node in taxonomy. Central hub node — everything else connects through it. | Taxonomy — Reason |
| 4 | **Product Category** | Canonical product grouping (e.g. Disputes, Payouts, Vault). | Product catalogue CSV |
| 5 | **Product / Feature** | Named Checkout product within a category (e.g. Pre-Disputes, Bank Payouts, Forward API). | Product catalogue CSV |
| 6 | **Payment Method** | Specific payment method or card scheme (e.g. SEPA Direct Debit Core, Klarna BNPL, Mada). Treated as a separate class due to volume and geographic distribution. | Product catalogue CSV — Payment Methods category |
| 7 | **Integration Method** | How the merchant connects to Checkout: technical integration (API, Flow, HPP, SDK) or via a partner platform (Shopify, WooCommerce, Gr4vy). | Taxonomy + Product catalogue CSV — Partner Integrations category |
| 8 | **Action Type** | The resolution action required to close the contact. Determines automability across all actors. | Implied by Reasons |
| 9 | **Error / State** | Specific error code or status state that triggered the contact. | Implied by Reasons |
| 10 | **Customer Segment** | Which B2B merchant segment raised the contact. Determines handling path and which actor is primary. B2C excluded until consumer taxonomy is defined (2027+). | `customer-segments.md` |
| 11 | **Resolution Actor** | Who handles the contact: Fin, Agent Consultant, Human L1, Human L2, External. The graph models knowledge and data requirements per actor, not just per Reason. | Design |
| 12 | **Knowledge Asset** | A structured knowledge artefact used by an actor to resolve a contact. Subtypes: KB article, SOP, escalation playbook, policy rule. Tacit knowledge (no doc exists) surfaces as a gap — a Reason with no mapped Knowledge Asset for a given Actor. | Content team; Process Architect; Operations Excellence |
| 13 | **Tool / System** | The system an actor uses to access data for a given Reason. Distinct from the data itself. Examples: Fin Procedure, Agent Consultant context panel, Zendesk admin, internal admin portal, partner / scheme portal. | Engineering; Operations |

Classes 7–9 are not yet fully enumerated — they are the extension work of Phase 1. Classes 11–13 are new additions — initial entity lists in sections below, full enumeration in Phase 1b.

---

## Class 1 — Domain (13 entities)

Directly from Case Type. No additions needed.

| Entity | Contact Volume (last 6m) | % of Total |
|---|---|---|
| PAYMENTS (IN) | 10,049 | 42.8% |
| ACCOUNT MANAGEMENT & ACCESS | 3,961 | 16.9% |
| PAYOUTS | 2,345 | 10.0% |
| TECHNICAL ISSUE | 1,828 | 7.8% |
| FUNDS AND FEES | 1,760 | 7.5% |
| GENERAL | 1,802 | 7.7% |
| DATA AND ANALYTICS | 763 | 3.2% |
| NON MERCHANT REQUESTS | 350 | 1.5% |
| COMPLIANCE & AUDIT | 283 | 1.2% |
| FEEDBACK | 142 | 0.6% |
| ISSUING | 88 | 0.4% |
| PLATFORMS | 85 | 0.4% |
| IDENTITY VERIFICATION | 25 | 0.1% |

---

## Class 2 — Problem Type (37 entities)

Directly from Issue Type. Full list:

| Domain | Problem Type |
|---|---|
| PAYMENTS (IN) | Transaction Status |
| PAYMENTS (IN) | Authentication (3DS) |
| PAYMENTS (IN) | Refunds |
| PAYMENTS (IN) | Fraud & Risk Controls |
| PAYMENTS (IN) | Disputes / Chargebacks |
| PAYMENTS (IN) | Performance |
| PAYOUTS | Bank Payouts |
| PAYOUTS | Card Payouts |
| FUNDS AND FEES | Balance |
| FUNDS AND FEES | Settlements |
| FUNDS AND FEES | Billing & Fees |
| TECHNICAL ISSUE | API Credentials |
| TECHNICAL ISSUE | API Integration |
| TECHNICAL ISSUE | Integration Methods |
| TECHNICAL ISSUE | Webhooks |
| TECHNICAL ISSUE | Tokens |
| TECHNICAL ISSUE | Environment |
| ACCOUNT MANAGEMENT & ACCESS | Account Changes |
| ACCOUNT MANAGEMENT & ACCESS | Login & Access |
| DATA AND ANALYTICS | Reporting |
| PLATFORMS | Sub-Merchant Onboarding |
| PLATFORMS | Transfers & Splits |
| COMPLIANCE & AUDIT | Compliance Evidence |
| COMPLIANCE & AUDIT | Other Compliance |
| ISSUING | Card Management |
| ISSUING | Issuing Transactions, Money & Reports |
| ISSUING | Issuing Digital Wallets |
| ISSUING | Logistics |
| ISSUING | Mobile App / SDK |
| IDENTITY VERIFICATION | Verification and Technical Support |
| IDENTITY VERIFICATION | Security, Privacy and Compliance |
| IDENTITY VERIFICATION | Formal Complaint |
| IDENTITY VERIFICATION | N/A |
| FEEDBACK | Product Feedback |
| GENERAL | Inquiries |
| No Action Required | No Response Needed |
| Non-Merchant Requests | Cardholders / Third Parties |

---

## Class 3 — Reason (~103 entities)

Directly from Reason column in taxonomy. Not enumerated again here — use taxonomy source doc as the canonical list. Phase 1 task: confirm total count from source CSV and flag any Reasons that appear in the CSV but not in the taxonomy doc.

**Known gap**: Reasons in `support_contacts_flat_table_2025_last_6m.csv` may not exactly match V3 taxonomy definitions — this needs reconciliation before Phase 2 tagging begins.

---

## Class 4 — Product Category (21 entities)

Sourced from the canonical product catalogue CSV. Replaces the rough extraction previously inferred from taxonomy language.

| Product Category | Description |
|---|---|
| Authentication | 3DS and standalone authentication services |
| Business Account | Settlements, Balances, Transfers, Corporate Cards |
| Dashboard | Merchant-facing portal |
| Disputes | Chargebacks and pre-dispute management |
| Flow | Customisable payment components (web) |
| Flow / Mobile SDK | Flow for Android, iOS, React Native |
| Fraud Detection | Risk rules and fraud scoring (free + Pro) |
| Hosted Payment Page | Low-integration hosted checkout |
| Identity Verification | KYC/KYB — document, face, business screening |
| Intelligent Acceptance | AI-powered acceptance rate optimisation |
| Internal Products | Notifications and Webhooks |
| Issuing | Card issuance, management, physical cards |
| Network Tokens | Scheme-issued token credentials |
| Partner Integrations and Plugins | Third-party platforms and orchestrators |
| Payment Links | Shareable payment URL / QR code tool |
| Payment Methods | APMs and card schemes (see Class 6) |
| Payouts | Bank and card outbound payouts |
| Real-Time Account Updater | Automated card detail refresh |
| Reporting & Analytics | Reports, APIs, SFTP, Analytics Assistant |
| Treasury & FX | FX rate products for acquiring and payouts |
| Vault | Secure credential and token storage |

---

## Class 5 — Product / Feature (~100 entities)

Canonical product names from the CSV. Grouped by category below. Apple Pay and Google Pay appear as both Payment Methods and as integration capabilities within Issuing Digital Wallets — both nodes exist; the relationship between them is Phase 4 work.

| Category | Products |
|---|---|
| Authentication | Authentication |
| Business Account | Balances; Corporate Cards; Settlements; Transfers |
| Dashboard | Dashboard |
| Disputes | Disputes; Pre-Disputes |
| Flow | Flow Web; Remember Me |
| Flow / Mobile SDK | Flow Android SDK; Flow iOS SDK; Flow React Native SDK |
| Fraud Detection | Fraud Detection (free); Fraud Detection Pro |
| Hosted Payment Page | Hosted Payment Page |
| Identity Verification | Business Screening; Business Verification; Face Authentication; ID Document Verification; Identity Verification |
| Intelligent Acceptance | Intelligent Acceptance |
| Internal Products | Notifications |
| Issuing | Authentication; BIN Management; Card Product; Cardholder; Cards; Digital Wallets; Entity Structure; Fraud; Issuing Region; Physical Card PIN; Physical Cards; Reporting; SCA Exemptions; SCA Out of Scope; Simulation; Spending Controls; Transactions |
| Network Tokens | Network Tokens |
| Partner Integrations and Plugins | Basis Theory; BigCommerce; BR-DGE; Chargebee; Chargify; GIG; Gr4vy; Magento 2; OpenCart; Payrails; Salesforce Commerce Cloud; SAP Commerce Cloud; Shopify (offsite); Shopify (onsite); Spreedly; WooCommerce; Zuora |
| Payment Links | Payment Links |
| Payouts | Bank Payouts; Card Payouts |
| Real-Time Account Updater | Real-Time Account Updater |
| Reporting & Analytics | Analytics Assistant; Dashboard Reports; Dashboard Reports (non-financial); Predictive Interchange; Reports API; Reports API (non-financial); SFTP Reports; SFTP (non-financial) |
| Treasury & FX | Acquiring – Custom FX markup; Acquiring – Daily FX Rates; Acquiring – FX Live Market Rates; Acquiring – Scheme FX Rates; PTC – FX based on Scheme FX; Internal – Cash ladder reporting; Internal – FX Blotter reporting |
| Vault | Forward API; Integrated Vault; Standalone Vault |

**Taxonomy mapping gap**: Several product categories have no corresponding Domain in the support taxonomy. These are unmapped contact risk areas where Fin has no structured handling path:

| Product Category | Taxonomy Domain | Gap |
|---|---|---|
| Vault | TECHNICAL ISSUE (partial — tokens) | No explicit mapping for Forward API, Standalone Vault |
| Treasury & FX | None | No taxonomy domain at all |
| Real-Time Account Updater | None | No taxonomy domain at all |
| Intelligent Acceptance | PAYMENTS (IN) → Performance (implied) | No explicit mapping |
| Remember Me | TECHNICAL ISSUE (partial) | No explicit mapping |
| Corporate Cards | FUNDS AND FEES (partial) | No explicit mapping |
| Partner Integrations | TECHNICAL ISSUE → Integration Methods (collapsed) | 17 named partners collapsed to "E-Commerce Plugin" |

These gaps need resolving before Phase 2: either the taxonomy adds new Reasons to cover them, or they are confirmed as out-of-scope for Fin.

---

## Class 6 — Payment Method (68 entities)

Payment Methods are treated as a separate entity class. At 68 named methods across 6 continents, collapsing them into Class 5 would obscure the coverage problem: Fin content almost certainly does not address payment-method-specific failure modes (e.g. Mada decline codes, SEPA mandate errors, Klarna refund flows) as distinct nodes. Phase 2 will expose which payment methods have zero content coverage.

| Region | Payment Methods |
|---|---|
| Global card schemes | Visa; Mastercard; American Express (Collecting); American Express (Gateway); Diners Club International; Discover; JCB; UnionPay (Gateway) |
| US debit networks | ACH Direct Debit; Accel; Maestro; NYCE; Pulse; STAR |
| Europe | Bacs; Bancontact; BLIK; Cartes Bancaires; eps; iDEAL; MB Way; MobilePay; Multibanco; Przelewy24; SEPA Direct Debit Core; SEPA Direct Debit B2B; SeQura; Sofort; Swish; Twint; Vipps; Wero |
| Middle East & Africa | Benefit Payment Gateway; BenefitPay; Fawry; Jaywan; Knet; Mada; Omannet; QPay; STC Pay; Tabby (Collecting); Tabby (Gateway); Tamara (Collecting); Tamara (Gateway) |
| Asia-Pacific | AlipayCN; AlipayHK; DANA; EFTPOS; GCash; KakaoPay; Octopus; PayNow; Samsung Pay; Touch 'n Go; TrueMoney; WeChat Pay CN; WeChat Pay HK |
| Latin America | Boleto Bancario; Pix |
| BNPL / Wallets (global) | Alma; Klarna (Gateway); Klarna BNPL (Collecting); Klarna Crypto; Klarna Debit Risk; PayPal; Venmo |

**Note**: Apple Pay and Google Pay sit in both Payment Methods and Issuing Digital Wallets. Both nodes are valid — the relationship (wallet-as-payment-method vs wallet-as-issuance-channel) is Phase 4 graph structure work.

---

## Class 7 — Integration Method

Revised from Class 5. Now split into two sub-types: **technical integration** (how merchants call the Checkout API) and **partner integration** (orchestration platforms and e-commerce plugins from Class 5 / Partner Integrations). Both are integration methods that affect which Fin Procedure applies and where errors originate.

**Technical integration**

| Method | Notes |
|---|---|
| REST API (direct) | Covers API Error 4XX / 5XX reasons across multiple domains |
| Flow Web | Checkout-hosted JS drop-in |
| Flow Mobile SDK | iOS, Android, React Native variants |
| Hosted Payment Page | No-code redirect |
| Payment Links | No-code shareable URL |
| Sandbox / Test environment | Distinct environment — not a prod integration method |

**Partner integration** (17 named platforms — see Class 5, Partner Integrations and Plugins for full list)

Includes: Shopify (onsite/offsite); WooCommerce; Magento 2; BigCommerce; SAP Commerce Cloud; Salesforce Commerce Cloud; OpenCart — plus payment orchestrators: Gr4vy; Spreedly; Payrails; BR-DGE; Basis Theory.

These are significant for Fin because a merchant on Shopify (onsite) has a different resolution path than one on direct REST API — the error origin may be in the plugin, not Checkout's core platform.

---

## Class 8 — Action Type

Resolution actions implied by Reason labels. Extracted here as a first-pass enumeration.

| Action Type | Example Reasons |
|---|---|
| Status lookup | Stuck in status / Status Enquiry; Payout status inquiry; Balance confirmation |
| Proof / Evidence retrieval | Proof of payment (ARN, RNN, Bulk); Proof of Bank Payout; Audit request |
| Manual processing | Refund failed / Manual Refund; Manual payout correction |
| Configuration change | Risk Rules; Account settings update; Webhook setup; SFTP Configuration |
| Access / credential reset | Login Error / MFA / SSO; Create / Edit Keys |
| Dispute submission | Evidence Help and submission |
| Escalation / triage | All Payments Failing; Acceptance Rate Issue |
| Data investigation | Data Mismatch / Missing; Reconciliation issue |
| Onboarding action | Merchant activation and verification; Create / Activate Card |
| No action | Spam / Duplicate / No action; No action required by Merchant Care |

**Note**: Action Types are the primary input for Fin Procedure design. A Reason that maps to "Status lookup" is a candidate for a Fin data integration Procedure (BigQuery or API call). A Reason that maps to "Configuration change" requires human-in-the-loop unless it can be safely automated.

---

## Class 9 — Error / State

Error codes and status states that merchants report as triggers for contacts. Not explicitly enumerated in the taxonomy but embedded in Reason labels.

| Error / State | Source Reason | Domain |
|---|---|---|
| Declined | Declined / Failed Action; Declined / Failed Bank payout; Declined / Failed card payout | Multiple |
| Failed | Refund failed; Transfer or split failed | Multiple |
| Pending | Bank payout stuck in Pending; Card payout stuck in Pending | PAYOUTS |
| 4XX (client error) | API Error 4XX / Logic Error | TECHNICAL ISSUE |
| 5XX (server error) | API Error 5XX | TECHNICAL ISSUE |
| Timeout | Idempotency / Timeout | TECHNICAL ISSUE |
| Signature verification failure | Signature Verification or Delivery Failure | TECHNICAL ISSUE |
| AVS / CVV mismatch | AVS / CVV Mismatch | PAYMENTS (IN) |
| Velocity limit reached | Velocity Limit Reached | PAYMENTS (IN) |
| Negative balance | Negative balance | FUNDS AND FEES |
| Liability shift status | Liability Shift Status | PAYMENTS (IN) |

**Gap**: This list is derived from natural language in Reason labels, not from a canonical error code registry. Phase 2 work should cross-reference against the API reference (`01-knowledge-base/Support content/API reference/`) to bind these to formal error codes and states.

---

## Class 10 — Customer Segment (4 entities, B2B only)

Added in design review, April 2026. The original 9-class taxonomy had no concept of who is raising the contact. Without Segment, the graph cannot model the fact that the same Reason has a different handling path depending on merchant type — a Platform contact about "Transfers & Splits" requires L2 human handling (Checkout is second-line for Platform merchants), whereas the same Domain for Enterprise may be Fin-resolvable.

| Segment | Description | Source |
|---|---|---|
| Enterprise | Direct merchants integrating Checkout APIs. Standard, Enterprise, and Premium tiers. | `customer-segments.md` |
| Platform | Marketplace operators with sub-merchants beneath them. Checkout acts as L2; Platform is L1 for its merchants. | `customer-segments.md` |
| Payfac | Small merchants where Checkout is the primary PayFac. TBC — timing not confirmed. | `customer-segments.md` |
| Issuing | Merchants using Checkout card issuance capabilities. Small segment; low contact volume currently. | `customer-segments.md` |

**B2C is excluded.** The consumer support taxonomy does not yet exist. When defined (2027+, ahead of Braavos launch), B2C slots in as a fifth Segment entity — the graph structure is compatible. B2C will require new Domains, Problem Types, and Reasons (balance disputes, card freeze, complaint handling, FOS referral, vulnerable customer escalation) before any `RAISED_BY` edges can be created.

---

## Class 11 — Resolution Actor (5 entities)

Added April 2026. The graph previously modelled Fin as the only resolution actor — the question was "can Fin resolve this?" The expanded model covers the full actor stack. Each actor has distinct knowledge and data requirements for the same Reason. The graph models those requirements per actor, not just per Reason, making knowledge and data gaps visible across the entire support operation.

| Actor | Description | Cost benchmark |
|---|---|---|
| **Fin** | Autonomous AI agent. Resolves without human involvement. Knowledge: KB articles via Procedures. Data: API integrations and BigQuery via Fin Procedures. | $0.90/resolution |
| **Agent Consultant** | AI assistant to human agents. Surfaces knowledge, context, and recommended actions at the point of resolution. Does not resolve autonomously — reduces human handle time and improves consistency. Knowledge: SOPs, KB articles, policy rules. Data: Customer 360, transaction history, case history. | Handle time reduction on human cost |
| **Human L1** | Care agent (first line). Resolves standard contacts using SOPs, tools, and KB. Escalates to L2 when outside scope or authority. Knowledge: SOPs, playbooks, KB articles, training. Data: Zendesk, internal admin portal, partner tools. | ~$40/contact |
| **Human L2** | Specialist or senior agent (second line). Handles escalations requiring deeper system access, exception authority, or partner/scheme involvement. Knowledge: Specialist SOPs, escalation criteria, policy authority. Data: Deep system access, partner/scheme portals, external APIs. | ~$40+/contact |
| **External** | Third-party actor (acquiring bank, card scheme, issuer, partner platform). Required when resolution depends on action outside Checkout's control. Examples: chargeback outcome with Visa, issuer confirmation for a declined transaction. | N/A — dependency |

**Key insight**: The same Reason can have different primary actors by segment. A Platform contact about "Transfers & Splits" is Human L2 (Checkout is second-line); the same Reason for Enterprise may be Fin-resolvable. The actor-segment combination determines the resolution path.

---

## Class 12 — Knowledge Asset (4 subtypes)

Added April 2026. Previously the graph modelled only KB articles as knowledge objects, via `COVERED_BY` edges. The expanded model recognises four distinct Knowledge Asset subtypes, each required by different actors. Tacit knowledge — things agents resolve from experience with no documented artefact — surfaces in the graph as a gap: a Reason with no mapped Knowledge Asset for a given Actor. This makes invisible knowledge visible as a structural deficit.

| Subtype | Description | Primary actor | Owner |
|---|---|---|---|
| **KB article** | Fin-facing and merchant-facing content published in Zendesk Guide. Addresses a Reason directly or provides background. | Fin, Agent Consultant | Content Strategist |
| **SOP** | Care Agent standard operating procedure. Step-by-step resolution instructions for L1 agents. Equivalent to a Fin Procedure for humans. | Human L1 | Process Architect |
| **Escalation playbook** | Criteria and steps for escalating a Reason from L1 to L2 or External. Defines when escalation is appropriate, not just who to escalate to. | Human L1, Human L2 | Operations |
| **Policy rule** | Explicit business rule governing resolution authority. Examples: refund thresholds, exception approval levels, data disclosure rules. | Human L1, Human L2, Agent Consultant | Operations Excellence |

**Governance note**: Each Knowledge Asset subtype has a named owner above. When a product or process changes, the graph must surface all Knowledge Assets with `REQUIRES_KNOWLEDGE` edges to the affected entity — not just KB articles. SOPs and playbooks are equally at risk of going stale from product changes.

---

## Class 13 — Tool / System (initial enumeration)

Added April 2026. Distinct from Data Assets (what data exists) and Knowledge Assets (what knowledge exists) — Tools are the systems actors use to access data for a given Reason. Modelling Tools separately makes tooling gaps and access permission gaps visible: an actor may have the knowledge and data in principle, but lack the tool or credential scope to access it.

| Tool | Actor | Access type |
|---|---|---|
| Fin Procedure | Fin | API integration or BigQuery query. The Procedure is the access mechanism — no Procedure = no data access regardless of whether the data exists. |
| Agent Consultant context panel | Agent Consultant | Customer 360 surface, case history, recommended actions. Configured by Product/Content. |
| Zendesk admin (ticket view) | Human L1, Human L2 | Ticket history, tags, macros, SLA state. Standard access. |
| Internal admin portal | Human L1, Human L2 | Account settings, balance tools, configuration state. Access tiers vary by agent role. |
| Dashboard (merchant portal) | Human L1 (read-only view) | Merchant-side transaction and account view. Used for context, not action. |
| Partner / scheme portal | Human L2, External | Visa DPS, issuer portal, bank partner portal. L2-only access; requires specific credentials and training. |
| BigQuery / data tooling | Human L2, Data team | Ad hoc query for investigation. Not a standard L1 tool. |

**Tooling gap model**: A Reason may have a data source available but no Tool configured for the relevant Actor to access it. This is a distinct gap type from "data does not exist" — it requires a configuration or access change, not an API integration. The graph distinguishes these cases.

---

## Relationship Schema (Phase 1b)

Relationship types must be defined before Phase 2 (content coverage mapping) begins. Without them, Phase 2 produces a flat content list mapped to isolated nodes, not a traversable graph. The `INVOLVES` and `REQUIRES_KNOWLEDGE` edges are the minimum required to run a meaningful coverage matrix across all actors.

**Domain and product structure**

| Relationship | Direction | Cardinality | Notes |
|---|---|---|---|
| `CONTAINS` | Domain → Problem Type → Reason | 1:many | Hierarchical; already implicit in taxonomy structure |
| `INVOLVES` | Reason → Product/Feature | many:many | Core edge for content routing. A Reason may involve multiple products. |
| `INVOLVES` | Reason → Payment Method | many:many | Exposes APM-specific coverage gaps in Phase 2 |
| `RESOLVED_BY` | Reason → Action Type | many:1 | Determines automability across all actors — not just Fin. "Status lookup" = Fin candidate; "Configuration change" = human-in-loop by default |
| `RAISED_BY` | Reason → Customer Segment | many:many | With contact volume weight from CSV. Unlocks segment-differentiated routing in Phase 4 |
| `ROUTED_VIA` | Reason → Integration Method | many:many | Affects resolution path — Shopify merchant has different error origin than direct REST API |
| `TRIGGERS` | Error/State → Reason | many:many | Connects formal error codes to the Reasons they surface as |
| `BELONGS_TO` | Product/Feature → Product Category | many:1 | Hierarchical |

**Knowledge coverage — all actors**

| Relationship | Direction | Cardinality | Notes |
|---|---|---|---|
| `REQUIRES_KNOWLEDGE` | Reason × Actor → Knowledge Asset | many:many | What each actor needs to resolve this Reason. Absence = knowledge gap per actor. Replaces the Fin-only `COVERED_BY` model. |
| `REDUCES_TIME_FOR` | Knowledge Asset → Reason × Actor | many:many | **Phase 3** — Agent Consultant surfacing a SOP reduces L1 handle time. Measurable: compare handle time for contacts where AC surfaced an asset vs. where it did not. |

**Data coverage — all actors**

| Relationship | Direction | Cardinality | Notes |
|---|---|---|---|
| `DATA_AVAILABLE_FOR` | Reason × Actor → Data Source | many:many | **Data graph** — does the data needed to resolve this Reason exist and is it accessible for this Actor? Four states: no source / partial / blocked / live. Extends the Fin-only Procedure model to all actors. |
| `USES_TOOL` | Actor × Reason → Tool | many:many | Which Tool the Actor uses to access data for this Reason. A data source may exist but be inaccessible if no Tool is configured for that Actor. |

**Routing and escalation**

| Relationship | Direction | Cardinality | Notes |
|---|---|---|---|
| `HANDLED_BY` | Reason × Segment → Resolution Actor | many:many | **Phase 4** — the routing output. Now multi-actor: Fin → AC-assisted L1 → unassisted L1 → L2. Primary actor determined by current coverage state of `REQUIRES_KNOWLEDGE` and `DATA_AVAILABLE_FOR` edges. Living artifact as Procedures, SOPs, and AC configuration change. |
| `ESCALATES_TO` | Actor × Reason → Actor | many:many | When and to whom a Reason escalates. Distinguishes structural escalations (L2 is always right) from avoidable ones (L1 lacks tool or SOP). |

**Construction format**: Edges stored as a relationship CSV alongside this taxonomy doc:

```
source_class, source_entity, relationship_type, target_class, target_entity, actor, weight, state, notes
```

The `actor` column is new — it makes per-actor knowledge and data edges representable in the same flat format. `state` applies to `DATA_AVAILABLE_FOR` edges (no source / partial / blocked / live). Human-editable, queryable with Python (pandas), version-controlled (diff-friendly for BAU updates), and ingestible into a graph system later.

Phase 1b task: populate `INVOLVES` (Reason → Product) and `RAISED_BY` (Reason → Segment) for top-volume Reasons — PAYMENTS (IN) and ACCOUNT MANAGEMENT & ACCESS (~60% of contacts) — and agree the `REQUIRES_KNOWLEDGE` actor mapping for the same Reason set before Phase 2 begins.

---

## Taxonomy Coverage Gaps

The 7 product categories with no taxonomy domain are a content gap, not a confirmed out-of-scope. Two distinct cases:

| Category | Gap type | Action |
|---|---|---|
| Vault | Contacts likely miscategorised as TECHNICAL ISSUE → Tokens or API Integration | Investigate CSV data; add Reasons if contacts exist |
| Treasury & FX | Likely low volume; may sit under FUNDS AND FEES informally | Investigate CSV data; add Reasons if contacts exist |
| Real-Time Account Updater | Likely low volume; no current taxonomy node | Investigate CSV data; add Reasons if contacts exist |
| Intelligent Acceptance | Contacts implied under PAYMENTS (IN) → Performance | Add explicit Reason or confirm absorbed |
| Remember Me | Contacts split across TECHNICAL ISSUE and B2C path | Clarify scope; B2C taxonomy will cover cardholder side |
| Corporate Cards | Contacts likely under FUNDS AND FEES | Investigate CSV data; add Reasons if contacts exist |
| Partner Integrations | 17 named partners collapsed to "E-Commerce Plugin" | Phase 2 should surface per-partner volume; expand Reasons if significant |

Goal: no gaps. Content team covers all nodes once the taxonomy is complete.

---

## Automated Tagging — Reflex Capability

Manual tagging of 879 articles against the entity taxonomy will not scale and will drift as articles are updated. The tagging workflow is built in three stages:

**Phase 2 — LLM-assisted batch tagging (Reflex AI Engine)**
The Reflex AI Engine (`01-knowledge-base/products/reflex.md`) already lists "content gap identification" as a named function. Phase 2 implements this: Reflex reads each article against the entity taxonomy and outputs suggested `COVERED_BY`, `INVOLVES`, and `ROUTED_VIA` edges as CSV rows. Content team reviews suggestions (approve/reject) rather than tagging from scratch. High confidence for product/method mentions (exact-match against entity names); lower for Reason mapping (requires understanding of what the article solves, not just what it mentions) — human review required for Reason edges. This runs as a scheduled Reflex job, not a one-off script, so new articles are processed as they are published.

**Phase 3 — Fin usage signal feedback**
Reflex already ingests Fin conversation metadata. When Fin surfaces an article for a contact that has a tagged Reason, a `COVERED_BY` edge can be inferred from usage. Articles that resolve contacts reinforce edges; articles that fail to resolve flag gaps. This becomes the primary signal for edge weight over time, and validates or overrides the static Phase 2 tags.

**End state — authoring-time tagging**
A mandatory taxonomy tag field in Zendesk Guide authoring workflow. Publishing an article produces `COVERED_BY` edges automatically — zero retrospective tagging work. Requires the Reason entity list to be stable (Phase 1 completion criteria) and a Zendesk Guide custom field synced to the relationship CSV.

**Product release trigger (end state)**
When a product changes, the graph flags every article with a `COVERED_BY` or `INVOLVES` edge to that product entity for review — before the change ships. Prevents content drift from product changes that invalidate articles without triggering updates.

**Extended scope — SOPs and playbooks**: The same LLM-assisted tagging approach applies to SOP content (`01-knowledge-base/processes/Care Agent SOPs/`). Reflex reads each SOP against the entity taxonomy and outputs suggested `REQUIRES_KNOWLEDGE` edges (Reason × Human L1 → SOP). Process Architect reviews. This is Phase 2 work alongside KB article tagging — not a later phase.

**Product release trigger (end state)**: When a product changes, the graph flags every Knowledge Asset (KB article, SOP, playbook, policy rule) with a `REQUIRES_KNOWLEDGE` edge to the affected entity for review — before the change ships. Previously this was scoped to KB articles only. The expanded model catches SOPs and playbooks that are equally at risk of staleness from product changes.

**Architectural note**: Reflex is the write path for the knowledge and data graph. The graph is the structured output Reflex produces; Fin and Agent Consultant read from it to route contacts, select content, and surface knowledge assets. Loop: Reflex analyses contacts/content/SOPs → populates graph edges → Fin and AC use graph → resolution outcomes feed back into Reflex for validation.

---

## Coverage Assessment

| Entity Class | Completeness | What's Missing |
|---|---|---|
| Domain | Complete (13 / 13) | Nothing — taxonomy is the source |
| Problem Type | Complete (37 / 37) | Nothing — taxonomy is the source |
| Reason | Near-complete (~103) | Reconciliation against CSV needed |
| Product Category | Complete (21 / 21) | Nothing — product catalogue CSV is the source |
| Product / Feature | Complete (~100) | Taxonomy mapping gaps documented above |
| Payment Method | Complete (68) | No contact volume split by payment method yet — Phase 3 work |
| Integration Method | Good (technical: 6; partners: 17) | Webhook transport and token sub-types for Phase 4 |
| Action Type | Draft (10 categories) | Not yet validated against SOP content or human agent SOPs |
| Error / State | Partial (~11 extracted) | Not bound to API error code registry |
| Customer Segment | Draft (4 B2B entities) | Contact volume split by segment not yet aggregated; B2C excluded until 2027 |
| Resolution Actor | Draft (5 entities) | Per-actor knowledge and data requirements not yet mapped; owned by multiple teams |
| Knowledge Asset | Draft (4 subtypes defined) | SOP inventory not yet enumerated; playbooks and policy rules not yet catalogued |
| Tool / System | Draft (7 tools listed) | Access tier mapping per Reason not yet modelled; credential scope gaps not assessed |

---

## Phase 1 Completion Criteria

- [ ] All 10 entity class definitions agreed with Content team, Knowledge Manager, and Process Architect
- [ ] Reason count reconciled against `support_contacts_flat_table_2025_last_6m.csv`
- [ ] Taxonomy mapping gaps investigated for all 7 unmapped product categories — add Reasons or confirm contacts are absorbed elsewhere
- [ ] Error / State list cross-referenced against API reference — bind to formal codes
- [ ] Action Type categories reviewed against Care Agent SOPs (`INDEX.md`) — confirm coverage
- [ ] Single named owner assigned per entity class
- [ ] Published to Confluence as living document before Phase 2 tagging begins

## Phase 1b Completion Criteria (required before Phase 2)

- [ ] Relationship schema agreed (all relationship types above, including new actor-scoped types)
- [ ] Relationship CSV format agreed with `actor` and `state` columns added; first file created
- [ ] `INVOLVES` edges populated for top-volume Reasons: all Reasons under PAYMENTS (IN) and ACCOUNT MANAGEMENT & ACCESS
- [ ] `RAISED_BY` edges populated for the same Reasons, with volume weights from `support_contacts_flat_table_2025_last_6m.csv`
- [ ] `REQUIRES_KNOWLEDGE` actor mapping agreed for top-volume Reasons — which actor needs which Knowledge Asset subtype per Reason
- [ ] Named owner assigned per entity class, including Classes 11–13 (Resolution Actor, Knowledge Asset, Tool)
- [ ] Reflex Phase 2 scoped to include LLM-assisted tagging of both KB articles and SOP content

---

## Phase Sequencing

| Phase | Deliverable | Blocker for next |
|---|---|---|
| Phase 1 | Entity classes + vocabulary (this doc), now including Classes 11–13 | Relationship types, Reason count reconciliation, gap investigation, owner assignment for all 13 classes |
| Phase 1b | Relationship schema + starter edges | `INVOLVES`, `RAISED_BY`, and `REQUIRES_KNOWLEDGE` actor mapping populated for top-volume Reasons; relationship CSV created |
| Phase 2 | Full knowledge coverage matrix (all actors) | Reflex LLM tagging of 879 KB articles and SOP inventory; `REQUIRES_KNOWLEDGE` edges reviewed by Content team and Process Architect |
| Phase 3 | Volume-weighted graph + data coverage layer | Contact volume split by Segment and Payment Method; `DATA_AVAILABLE_FOR` edges populated per actor; Fin usage signals feed back into edge weights |
| Phase 4 | Full resolution routing map | `HANDLED_BY` (Reason × Segment → Actor) and `ESCALATES_TO` chains defined; input to Fin Procedures PRD and Agent Consultant configuration; becomes living BAU artifact |

---

## Phase 2 Preview

With entity classes and relationship schema defined (Phases 1 + 1b), Phase 2 maps existing knowledge assets against Reason nodes via `REQUIRES_KNOWLEDGE` edges across all actors — not just Fin content.

**KB articles** (879): Reflex AI Engine generates suggested edges; Content team reviews. Same approach as originally scoped.

**SOPs** (~526 articles in Zendesk KB, 125 folders): Reflex generates suggested `REQUIRES_KNOWLEDGE` (Reason × Human L1 → SOP) edges; Process Architect reviews. This is new scope for Phase 2 — not a later phase — because SOP gaps and KB article gaps are the same class of problem requiring the same fix mechanism.

**Playbooks and policy rules**: Inventory required before tagging can begin. Process Architect and Operations Excellence to enumerate. Likely smaller in volume; high priority because gaps here create escalation inconsistency and quality failures.

The Phase 2 matrix distinguishes three gap types:
- **No knowledge asset exists** for this Reason × Actor — asset needs to be created
- **Asset exists but is unmapped** — edge needs to be created; content may already cover this
- **No taxonomy node exists** — contacts are being miscategorised; taxonomy fix required before content gap can be assessed

Prioritisation: high-volume Reasons with no mapped knowledge asset for any actor are the first fix. High-volume Reasons with KB coverage for Fin but no SOP for L1 are the second priority — these are contacts Fin escalates that L1 cannot resolve quickly without guidance.

Phase 2 answers: which knowledge assets exist, for which actors? It does not answer whether Fin or AC can resolve the Reason (Phase 4), or whether the data required is available (Phase 3).
