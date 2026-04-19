# Knowledge Graph Layer — Phase 1: Entity Taxonomy

> **Goal**: Produce a stable, canonical list of entity classes and entities derived from the existing support contact taxonomy. No graph structure yet — this is the vocabulary the graph will be built on.
>
> **Sources**:
> - `01-knowledge-base/processes/support-taxonomy.md` (V3, February 2026) — entity classes 1–3, 7–8
> - `Product category and name definitions - Sheet1.csv` (April 2026, new source of truth) — entity classes 4–6
>
> **Owner**: Charlie Wildish (draft); transfer to Knowledge Model Owner on appointment
> **Status**: Draft — not yet validated against Fin query data or agent SOP content

---

## Entity Classes

Nine entity classes in total. Classes 1–3 map directly to the taxonomy's three-level structure. Classes 4–6 are now sourced from the canonical product catalogue CSV (replaces earlier estimates inferred from taxonomy language). Classes 7–9 are implicit in the taxonomy and need to be surfaced explicitly.

| # | Entity Class | Description | Source |
|---|---|---|---|
| 1 | **Domain** | Top-level support area. Equivalent to Case Type. | Taxonomy — Case Type |
| 2 | **Problem Type** | Structured problem category within a domain. Equivalent to Issue Type. | Taxonomy — Issue Type |
| 3 | **Reason** | Specific problem statement. Leaf node in taxonomy. | Taxonomy — Reason |
| 4 | **Product Category** | Canonical product grouping (e.g. Disputes, Payouts, Vault). | Product catalogue CSV |
| 5 | **Product / Feature** | Named Checkout product within a category (e.g. Pre-Disputes, Bank Payouts, Forward API). | Product catalogue CSV |
| 6 | **Payment Method** | Specific payment method or card scheme (e.g. SEPA Direct Debit Core, Klarna BNPL, Mada). Treated as a separate class due to volume and geographic distribution. | Product catalogue CSV — Payment Methods category |
| 7 | **Integration Method** | How the merchant connects to Checkout: technical integration (API, Flow, HPP, SDK) or via a partner platform (Shopify, WooCommerce, Gr4vy). | Taxonomy + Product catalogue CSV — Partner Integrations category |
| 8 | **Action Type** | The resolution action required to close the contact. | Implied by Reasons |
| 9 | **Error / State** | Specific error code or status state that triggered the contact. | Implied by Reasons |

Classes 7–9 are not yet fully enumerated — they are the extension work of Phase 1.

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

## Coverage Assessment

| Entity Class | Completeness | What's Missing |
|---|---|---|
| Domain | Complete (13 / 13) | Nothing — taxonomy is the source |
| Problem Type | Complete (37 / 37) | Nothing — taxonomy is the source |
| Reason | Near-complete (~103) | Reconciliation against CSV needed |
| Product Category | Complete (21 / 21) | Nothing — product catalogue CSV is the source |
| Product / Feature | Complete (~100) | Taxonomy mapping gaps documented above (Vault, FX, RTAU, etc.) |
| Payment Method | Complete (68) | No contact volume split by payment method yet — Phase 3 work |
| Integration Method | Good (technical: 6; partners: 17) | Webhook transport and token sub-types for Phase 4 |
| Action Type | Draft (10 categories) | Not yet validated against SOP content |
| Error / State | Partial (~11 extracted) | Not bound to API error code registry |

---

## Phase 1 Completion Criteria

- [ ] All 9 entity class definitions agreed with Knowledge Manager and Process Architect
- [ ] Reason count reconciled against `support_contacts_flat_table_2025_last_6m.csv`
- [ ] Taxonomy mapping gaps resolved for unmapped product categories (Vault, FX, RTAU, Intelligent Acceptance, Remember Me, Corporate Cards) — add Reasons or confirm out-of-scope for Fin
- [ ] Error / State list cross-referenced against API reference — bind to formal codes
- [ ] Action Type categories reviewed against Care Agent SOPs (`INDEX.md`) — confirm coverage
- [ ] Single named owner assigned per entity class (product team for product entities; Ops for resolution paths)
- [ ] Published to Confluence as living document before Phase 2 tagging begins

---

## Phase 2 Preview

With entity classes defined, Phase 2 maps existing Fin content articles against these entities. Output: a coverage matrix showing which entity nodes have mapped content and which are blank. High-volume nodes with no content coverage are the first content priorities.
