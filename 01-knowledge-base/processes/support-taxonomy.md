# Support Query Taxonomy — Merchant Care

> Three-level classification system applied to all Zendesk tickets: **Case Type → Issue Type → Reason**.  
> Taxonomy definitions source: `Merchant Care - Case Classification v4.0 - Taxonomy v4.csv` (June 2026)  
> Volume actuals source: `Contact breakdown since April 2026.md` (native V4/"Unified" taxonomy labels, since 1 April 2026 — 14,654 contacts through 1 July 2026). This is the first cut reported directly in V4 case type names, so the V3→V4 mapping previously used against `support_contacts_flat_table_2025_last_6m.csv` is no longer needed. `support_contacts_flat_table_2025_last_6m.csv` is archived (`05-archive/2026/data-exports/`) — superseded by this cut for taxonomy mix purposes; keep using the archived CSV for other metrics not yet covered by the new file (Fin involvement rate, segment, sales_territory, billing_region — see `support_contacts_flat_table_2025_metric_definitions.md`).  
> Owner: Charlie Wildish — refresh when either source file is updated.  
> Payment and fintech terms used in this document follow definitions in [`checkout-terminology.md`](../payment-domain/checkout-terminology.md).


## Taxonomy Tree

### Accepting payments
*Refers to the technical lifecycle of customer-initiated transactions (processing, authorization, capture/void, refunds/reversals, disputes) for goods and services. Does NOT include enabling new payment methods, configuration of processing channels, or updating billing/statement descriptors — use ACCOUNT MANAGEMENT AND ACCESS instead. Decline codes 20XXX / 30XXX / 40XXX belong here.*

**Key distinctions:**
- *Lifecycle vs config* — the lifecycle outcome of a transaction (declines, stuck status, missing transaction, refund failure) belongs here; enabling a payment method or processing channel does not.
- *Payment ops* — payment outcomes without integration failures (declines, 3DS failures, chargebacks, refund failures) belong here.
- *Refund execution* — questions about refund execution, status, or failure itself belong here.

**Transaction status (non 3DS & refunds)** — Refers to the status, outcome, or root cause of failure for specific payment attempts or individual customers. Select this for "Why did this fail?" or "Where is the money?" queries regarding single or specific groups of transactions. Do NOT select this for 3DS/Authentication issues (use Authentication (3DS) issue type) or refund-related queries (use Refunds issue type).
- *Declined / failed action* — IF a customer payment was explicitly rejected with a response code by a bank or scheme, OR if the merchant requests a root cause analysis for specific declined transactions, error codes, or failures related to a single customer/card THEN select this.
- *Stuck in status / status enquiry* — IF a merchant reports a payment stuck in an intermediate payment state (e.g. Authorized or Captured), requests confirmation of a current status OR questions the root cause and processing logic behind a specific transaction outcome (e.g. unexpected voids or approvals) THEN select this.
- *Missing or unrecognised transaction* — IF a merchant claims a transaction occurred but cannot find it in the portal/logs OR asks for a general investigation where there is ambiguity about the transaction or its' status THEN select this.
- *Customer charged twice* — IF merchant reports a duplicate charge THEN select this.
- *Proof of payment (ARN, RNN, bulk)* — IF a merchant requests specific transaction identifiers (e.g., ARN, RRN) to provide to a customer, OR requests bulk transaction metadata/logs THEN select this.
- *Failed but customer charged* — If merchant says their customer was charged but payment declined then select this

**Refunds** — Includes failed refunds, refunds that need to be reversed, and requests for proof that a refund was issued.
- *Refund failed / manual refund* — IF an attempt to return funds results in a decline message or the merchant is unable to process the refund self-service due to technical failures (e.g., failed voids), scheme rules (e.g., exceeded time limits/MADA window), or acquirer constraints. Also select this in cases whenever the merchant explicitly requests a manual refund or asks the support team to intervene to finalize the return.
- *Refund proof* — IF a merchant needs documentation to prove a refund was processed to a customer THEN select this.
- *Refund reversal* — IF a processed refund needs to be undone or was done in error THEN select this.
- *Refund status enquiry* — IF the merchant is inquiring about the current status of a refund (e.g., pending, declined, successful) or reporting a status discrepancy where the dashboard state does not match expectations. Select this for refunds stuck in 'Pending', investigations into why funds have not reached the customer, or general verification of a refund's lifecycle.

**Authentication (3DS)** — Queries about 3DS/Authentication issues
- *3DS decline* — IF a transaction fails, is declined with a 3DS-related error, or the authentication process (OTP, App redirect, or initiation) is not triggered or completed as expected THEN select this.
- *Liability shift status* — If the merchant is asking about liability shift for a 3DS processed payment or chargeback (e.g. chargeback protection logic) then select this
- *SCA / exemption issue* — IF query relates to Strong Customer Authentication rules or requests to skip 3DS THEN select this.

**Fraud & risk controls** — Queries about Fraud controls and settings
- *Risk rules* — IF a payment was blocked by fraud settings or the Risk engine, OR the merchant requests changes to risk rules, blocklists, allowlists, or threshold settings.
- *Trustlist & decline list* — IF merchant wants to add/remove specific entities (IP, Email, Card) from a block or allow list THEN select this.
- *AVS / CVV mismatch* — IF the issue relates to Address Verification Service (AVS) or CVV checks, including payment failures due to mismatches, inquiries about check results, or questions regarding the logic of how these checks are performed and displayed.
- *Velocity limit reached* — IF blocks are occurring due to too many attempts in a short timeframe THEN select this.

**Disputes** — Queries about lifecycle of Disputes/Chargebacks
- *Dispute status* — IF the merchant is inquiring about the status, lifecycle, or outcome of a dispute (e.g., Won/Lost, Pre-Arb), or questioning its validity. Also select this for operational issues such as locating transactions involved in disputes, troubleshooting missing notifications (emails/RFIs), configuring dispute services (e.g., RDR, ARNs, API automation), or clarifying the financial impact on funds (e.g., held/released amounts).
- *Dispute adjustment* — IF the merchant is questioning, reporting discrepancies in, or seeking clarification on the financial adjustments resulting from disputes or chargebacks such as unexpected debits, duplicate charges, credit adjustments (UPDT), missing chargeback refunds, or confusion about how dispute outcomes have impacted their balance THEN select this.
- *Evidence help and submission* — IF the merchant is actively defending a dispute or RFI. Select this for submitting files (including manual upload requests), troubleshooting dashboard submission errors, or asking for strategic guidance on which specific documents are required to contest the case.

**Performance** — Queries about acceptance rate performance or multiple payment failures
- *Acceptance rate issue / optimisation* — IF a merchant reports a drop in overall approval ratios, asks for optimization advice, or flags a trend of declines across multiple transactions, THEN select this.
- *All payments failing* — If the merchant is saying they have large amount of payment failure issues or systemic payment failures then select this.


### Payouts
*Refers to the lifecycle of a payout made by card or bank payout. Includes status, declines, reversals, and proofs of payout. Does NOT include settlement of merchant balances (use FUNDS AND FEES instead).*

**Bank payouts** — Queries about payouts sent via bank transfer rails (SEPA, SWIFT, Faster Payments, ACH, wire transfers). Select this IF the ticket explicitly mentions: bank account, IBAN, SWIFT/BIC codes, MT103, beneficiary bank, wire transfer, bank-specific references, sanctions/AML screening holds, Inpay references, or name discrepancy verification. Also select this for payouts requiring RFI (Request for Information) for compliance screening. Do NOT select this if the payout method is unclear—use Card Payouts instead
- *Declined / failed bank payout* — IF a bank payout was declined THEN select this.
- *Proof of bank payout* — IF the recipient claims they haven't received funds from a bank payout and the merchant needs a confirmation receipt THEN select this.
- *Bank payout stuck in pending or status inquiry* — Select this category when a merchant inquires about a bank payout that is currently delayed, stuck in processing, or showing a pending status. This definition encompasses all scenarios where a bank payout is held for compliance checks, sanctions reviews, or risk assessments, often requiring a Request for Information (RFI) to resolve the hold. It is also the correct selection for general status investigations, discrepancies in payout amounts
- *Bank payout returns* — If a merchant asks to reverse a bank payout then select this

**Card payouts** — Queries about payouts sent via card networks (Visa Direct, Mastercard Send, Pay to Card/PTC, OCT). Select this IF the ticket mentions: Visa, Mastercard, card payout, card-based, ARN (Acquirer Reference Number), RRN, issuing bank, issuer, cardholder, or any card scheme reference. When the payout method is ambiguous or unclear (e.g., generic "withdrawal" or "payout" without specifying the rail), default to Card Payouts as they represent the majority of payout volume.
- *Card payout stuck in pending or status inquiry* — If a merchant asks why a card payout is stuck in Pending then select this
- *Declined / failed card payout* — If a merchant asks why a card payout was declined Paid but customer didn't receive money then select this
- *Proof of card payout* — IF merchant needs a card payout proof or Retrieval Reference Number (RRN) to give to a customer THEN select this.
- *Card payout reversal* — If a merchant asks to reverse a card payout then select this


### Funds and fees
*Refers to the flow of money in the merchant balance and their settlements and any associated fees. Includes settlement delays, reconciliation issues, balance queries, and invoice/fee inquiries.*

**Key distinctions:**
- *Reconciliation* — settlement reconciliation and cash-movement interpretation, or mismatched financial amounts (wrong settlement amount, unexpected fee), belong here.
- *Fees* — questions about fees (interchange/scheme/gateway fees, tax invoices, pricing checks), including "why fee wasn't refunded", belong here.

**Settlements** — Queries about Settlement lifecycle and reconciliation
- *Delayed / missing settlement* — IF an expected settlement is not showing on Dashboard or not arrived in the merchant's bank account THEN select this.
- *Reconciliation issue* — IF merchant is struggling to match report or Dashboard data to their bank statement entries or is reporting a discrepancy between expected and actual balances THEN select this.

**Balances** — Queries about Balance status and confirmation
- *Balance confirmation* — If the merchant needs a Statement of account (SOA) or balance confirmation document for audit purposes THEN select this
- *Negative balance* — IF the merchant is struggling to understand why they have a negative balance on their account THEN select this
- *Balance top up* — IF the merchant needs to top up their balance THEN select this
- *Balance explanation* — IF the merchant needs help understanding their balance or how funds are allocated, reports balance discrepancies or is unable to reconcile figures between reports or different balance types

**Billing & fees** — Queries about fees charged
- *Invoice request* — IF merchant needs a copy of their tax or service invoice THEN select this.
- *Fee inquiry* — IF merchant questions a specific charge (e.g., Interchange, Scheme fee) THEN select this.


### Technical issue
*Refers to integration or technical issues (API/SDK/webhook/connectivity), including HTTP 4xx/5xx errors, keys, tokens, and test environment issues. Does NOT include payment performance or outcome issues (use Accepting payments instead).*

**Key distinctions:**
- *HTTP codes* — explicit HTTP status codes (400/401/403/404/409/422/429/500/502/503) or API/endpoint/SDK failures (e.g. "API returned 500") belong here.
- *Integration symptoms* — plugin/checkout UI/integration behaviour (redirects, saved cards, a payment method disappearing from the site) belongs here.
- *Network tokens* — Network Tokenization / Network Tokens / token migration / enabling NT questions belong here.
- *Unexplained charges* — a customer charged an amount not reflected in Checkout.com records (wallet surcharge, 3DS fee, issuer fee) belongs here as an integration-layer investigation.

**API keys** — Queries regarding the management of authentication keys (Secret/Public OAuth) and their access permissions.
- *Create / edit keys* — If the merchant is asking about how to create, edit or troubleshoot API keys then select this
- *Key scopes* — Select this if the merchant is inquiring about which permissions are required or if they are explicitly requesting that specific scopes, such as /metadata/card, be granted to their API keys.

**API integration** — Queries regarding raw API responses, HTTP status codes, and network connectivity. (Use this as the "catch-all" for API errors that are not specific to a Plugin, Flow, Frames, SDK or Payment Links).
- *API error 4XX / logic error* — IF the merchant encounters HTTP 400-level errors (e.g., 404 Not Found, 422 Validation Error) indicating the issue lies with the request, OR reports functional integration bugs. Specific scenarios include redirect parameter mismatches, invalid data formats, missing response payloads, or logic errors where the system rejects the input.
- *API error 5XX* — Choose this category when the merchant reports HTTP 500-level errors, indicating that the request was valid but the server failed to fulfill it due to technical faults like Service Unavailable (503). This definition applies to broader infrastructure problems, including issues with the overall API status, synchronization failures caused by server crashes, or internal system errors that prevent the completion of the request. It is the correct selection for outages or downtimes where the provider's system is unresponsive.
- *Idempotency / timeout* — If the merchant is getting timeout or idempotency issues on API requests then select this

**Tokens** — Queries about tokens (including token migration and network tokens)
- *Network tokens* — IF the issue involves Network Tokens, including inquiries about token migration, provisioning status, or specific technical errors related to tokenization logic (e.g., PEM values or cryptograms).
- *Token migration* — If the merchant is asking about import or export of their Tokens then select this

**Integration methods** — IF the merchant is inquiring about the specific interface, library, or platform used to process payments, including hosted pages, plugins, SDKs, payment links, or digital wallets, THEN select this.
- *Flow / frames* — If the merchant is asking about Flow or Frames or migration to Flow
- *Payment links / hosted payment pages* — If a merchant is asking about Payment Links or Hosted Payment Page issues then select this
- *SDK issue* — If a merchant is asking about an SDK issue then select this
- *E-commerce plugin* — If a merchant is asking about an Plugin issue like Shopify, Woocommerce and others then select this
- *Apple Pay / Google Pay* — IF the merchant is asking about Apple Pay or Google Pay setup, integration, certificates, domain verification, or method-specific errors THEN select this.

**Webhooks** — Queries about webhooks
- *Webhook setup* — Select this category when a merchant is unable to successfully configure or connect their webhooks, including errors within third-party plugins like Shopify or requests for initial registration in environments like Sandbox. This definition covers all configuration-stage inquiries, such as Endpoint Registration Failures, where the listener URL cannot be saved, or when the merchant needs assistance enabling the service before any live transactions occur.
- *Signature verification or delivery failure* — Select this category if the merchant reports webhook delivery issues, including: Delivery Latency, missed notifications/callbacks for specific events (like entity creation), synchronization failures where a Status Mismatch occurs because the webhook never arrived to update their system, dispatch timing investigations, or timeouts where the merchant questions if the webhook failed to sync a successful capture to their dashboard. Also select this for signature verification issues, including: questions about security headers, source IP verification, how to cryptographically verify the webhook signature, the secret key, the hashing algorithm used, or why their local verification logic is failing to authenticate the incoming request.
- *Missing webhook data* — Select this category if the merchant reports inconsistent metadata, such as a missing orderId, or specifically points out that the Payload Data Format does not match their expectations. This definition applies when the webhook was successfully delivered, but the content inside was incomplete or incorrect, necessitating an investigation into why specific fields were excluded from the payload.

**Test environment** — IF the issue involves transaction failures, configuration problems, or testing specifically within the Sandbox/Test environments, THEN select this.
- *Sandbox issue* — IF the issue is about the non-production/testing environment THEN select this.


### Data and analytics
*Refers to issues about reports either from the Dashboard or via SFTP. Includes issues about how to get a report and issues with report data.*

**Key distinctions:**
- *Report data vs access* — a report that's missing/incorrect/not generated, a data mismatch, or a time-range/filter/SFTP-delivery issue belongs here.
- *Network tokens reporting* — questions about which report/API field shows NT status, or an NT flag mismatch between systems, belong here.
- *Data quality* — reconciliation issues caused by data format/export problems (Excel truncation, unreadable ARNs, missing columns, encoding issues) belong here.

**Reporting** — Queries about Reports and data within
- *Report not generated / missing* — IF the merchant is unable to successfully generate, download, or access a specific report for any reason. Select this for issues regarding file availability, download failures, missing formats, or requests for manual extraction due to dashboard access limitations.
- *Data mismatch / missing data* — IF there is a discrepancy or data gap in reports THEN select this.
- *Custom report request* — IF the merchant requires a specific data set or column configuration not available by default THEN select this.
- *SFTP configuration* — If a merchant is asking about reporting using SFTP then select this


### Platforms
*Covers Independent Software Vendors (ISVs) utilising Checkout.com's Integrated Platforms product to embed payments. Includes sub-merchant onboarding and fund distribution for marketplace/platform merchants.*

**Key distinction:** the "Platform trap" — use this case type ONLY when explicitly dealing with a marketplace/ISV and its sub-merchants: splits/transfers or sub-merchant onboarding. Do not use it as a catch-all for any Platform-segment merchant's contact.

**Sub-merchant onboarding** — Queries about onboarding merchants
- *Merchant activation and verification* — IF issues relate to the KYC, verification, or creation of a sub-merchant THEN select this.
- *Doc upload error* — IF issues relate to the sub merchant document upload then select this

**Transfers & splits** — Queries about Transfers to merchants
- *Transfer or split failed* — IF funds were not distributed correctly between the platform and sub-merchant THEN select this.


### Card issuing
*Refers to issuing-related issues. Includes physical or virtual card issues and controls on these cards, issuing transactions, digital wallets, and SDK integration.*

**Card management** — Queries about managing cards
- *Create / activate card* — IF merchant is having trouble setting up or enabling a new card THEN select this.
- *Revoke / suspend* — IF merchant needs to cancel or temporarily freeze an active card THEN select this.
- *Spend controls* — IF query is about adjusting limits or blocking specific categories (MCC) THEN select this.

**Card deliveries** — Queries about card deliveries
- *Physical card delivery* — IF merchant is checking status or reporting a card lost in the mail THEN select this.

**Issuing digital wallets** — Queries about adding issued cards to Apple Pay or Google Pay
- *Apple Pay / Google Pay* — IF a cardholder cannot add their issued card to Apple Pay or Google Pay, or the card is not working correctly in their digital wallet (e.g., provisioning failures, token errors) THEN select this.

**Issuing mobile SDK** — Queries about the Issuing mobile SDK
- *Issuing SDK integration / upgrade* — IF the merchant is integrating, upgrading, or troubleshooting the Issuing mobile SDK THEN select this.

**Issuing transactions, funds and reports** — Questions about card transactions, settlement, fees, or balance
- *Issuing balance* — IF the merchant has questions about card funding balance, available funds per currency, insufficient funds errors, or operational reserves THEN select this.
- *Issuing settlement & reconciliation* — IF the merchant has questions about issuing settlement timing, report mismatches, or reconciliation issues THEN select this.
- *Issuing fees* — IF the merchant has questions about issuing fees (Interchange, scheme fees, CKO fees) THEN select this.
- *Issuing transaction declined / unexpected behavior* — IF the merchant needs to understand why an issued card transaction was declined or behaved unexpectedly THEN select this.


### Account management and access
*Refers to access to the Dashboard/Portal to use a feature, or making structural changes to the account. Includes login issues, user permissions, and account configuration. Select this if the merchant requests to add, enable, or configure specific payment methods (e.g. Amex, SEPA, APMs), currencies, schemes, or processing channels, or to update billing/statement descriptors. Does NOT include payment processing or integration issues.*

**Key distinctions:**
- *Enablement* — a request to enable/configure a payment method, currency, scheme, MID, or processing channel, or to update billing/statement descriptors, belongs here, not Accepting payments.
- *Access blockers* — if the primary blocker is access/permissions (can't access/view/download a report or section, missing permission), it belongs here.

**Login & access** — Queries about Dashboard login failures or setup
- *Login error / MFA / SSO* — IF merchant cannot enter the Dashboard due to password issues, MFA/2FA problems, SSO errors, or requires assistance setting up or troubleshooting SAML/Single Sign-On configuration THEN select this
- *User permissions* — IF adding/removing merchants or changing what a specific merchant can see/do THEN select this.
- *Dashboard user audit evidence* — IF merchant wants an audit log of who performed which action in the portal THEN select this.
- *Dashboard error* — IF the merchant reports a Dashboard page or feature that fails to load, displays an error message or error code, or behaves unexpectedly after successful login such as pages showing "Unable to load", transaction details not opening, or specific Dashboard sections returning errors THEN select this. Do NOT select this for login/authentication failures (use Login Error / 2FA) or permission-related access issues (use User Permissions).

**Account changes** — Requests regarding overall Account changes such as the merchant entity's commercial terms, structural platform configuration, or lifecycle status. Also select this for configuration updates, including retrieving identifiers or correcting settings like Billing Descriptors and MCCs.
- *Pricing change* — IF merchant is requesting to update their contract or commission rates THEN select this.
- *Account settings update* — IF the request involves configuring processing channels (e.g., new MIDs, environment setup), retrieving account identifiers (e.g., BINs, MCCs), changing account status (e.g., activation, restriction), or updating administrative profile details (bank info, legal address), THEN select this.
- *Terminations* — IF merchant explicitly asks to Terminate or close their account THEN select this.


### Feedback
*Sentiment and product suggestions. Not a support query — no resolution required.*

**Product feedback** — Queries about providing feedback about the features offered by Checkout and how to request or use them
- *Feature request* — IF merchant suggests a new functionality that does not currently exist THEN select this
- *Feature usage* — IF merchant asks "How do I use this existing feature?" THEN select this.


### Compliance and audit
*Refers to requests for documentation for audit/compliance purposes, including PCI, AOC, sensitive data, and other compliance docs.*

**Compliance evidence** — Queries about requesting compliance documentation from Checkout
- *PCI / AOC request* — IF merchant asks for security compliance certificates (AOC/PCI-DSS) THEN select this.
- *Audit request* — IF query is for formal audit evidence or due diligence questionnaires THEN select this.
- *Sensitive data request* — IF the merchant requests sensitive customer information such as full PAN (Primary Account Number), unmasked card numbers, or other protected cardholder data, typically in response to legal authorities, law enforcement, regulatory bodies, or court orders THEN select this.
- *Other compliance docs*


### General
*Refers to general inquiries which do not fit other case types.*

**Inquiries** — Queries about buying our services or Sales or anything else
- *Sales inquiry* — IF a prospect wants to buy services or add new products THEN select this.
- *Spam / duplicate / no action / follow ups* — IF the ticket is spam, empty, a follow up. an OOO reply, or an accidental double-post THEN select this.


### Identity Verification
*Refers to the Identity Verification (IDV) product and services, which use document checks, facial recognition, and automation to verify identity. Includes verification support, compliance, and security queries.*

**Verification and technical support** — Review rejected verifications, update configurations and resolve technical errors.
- *Verification inquiry* — Queries about specific identity verification results, including requests to correct extracted data (name, DOB), re-verification due to suspected fraud, understanding why a verification was rejected, or inquiries about a specific IDV ID.
- *Setup support* — Queries about IDV configuration and onboarding, including adding or removing accepted document types or countries, dashboard access, certificate management (mTLS), or customization options.
- *Technical & platform* — Technical issues with the IDV platform, including verifications stuck in pending, document capture failures, API errors, webhook issues, or integration problems.

**Security, privacy and compliance** — Submit requests related to data privacy rights, report security incidents, or request compliance documentation.
- *Data privacy* — Requests related to data privacy rights, including data deletion/erasure requests (GDPR), requests for copies of personal data, identity theft reports, or questions about privacy policy and data handling.
- *Account & compliance* — Queries about IDV account-level compliance, regulatory requirements, or compliance certifications.
- *Security* — Queries related to IDV security concerns, security incidents, or security certifications.

**Formal complaint** — Submit a formal complaint about the identity verification service.
- *Formal complaint* — Formal complaints about the IDV service requiring escalation or with legal/compliance implications.

**N/A** — Tickets that do not require action or do not fit other IDV issue types.
- *3rd party* — IF the ticket was submitted by or relates to a third party and does not require IDV team action THEN select this.
- *Automated* — IF the ticket was generated automatically by a system and does not require manual action THEN select this.
- *Follow up* — IF the ticket is a follow-up to a previous request that has already been resolved THEN select this.
- *Sales lead* — IF the ticket is a sales inquiry or lead rather than a support request THEN select this.
- *Self resolved* — IF the issue was resolved by the merchant before agent intervention THEN select this.
- *Spam* — IF the ticket is spam or irrelevant THEN select this.


### No action required
*Manual classification by agents only. Applied to contacts requiring no Care response.*

- **Duplicate**
- **Spam**
- **Sales Enquiry**


### Non-merchant requests
*Manual classification by agents only. Contacts originating from parties other than the merchant — routed or closed without standard support handling.*

- **Cardholder Complaints**
- **Issuing Bank Requests**
- **Authorities**
- **Schemes**
- **TPA Requests**
- **Other**


## Summary Counts & Volume

> **Since 1 April 2026**, volume actuals are reported natively in V4/"Unified" case type names — no V3→V4 mapping required. Non-merchant requests and No action required are manual, agent-only classifications and do not appear in this automated cut (excluded from the table and from the 100% total, as before).

| Case Type | Issue Types | Reasons | Contacts | % of Volume |
| --- | --- | --- | --- | --- |
| Accepting payments | 6 | 20 | 6,376 | **43.5%** |
| Payouts | 2 | 8 | 1,843 | **12.6%** |
| Technical issue | 6 | 18 | 1,636 | **11.2%** |
| Account management and access | 2 | 7 | 1,554 | **10.6%** |
| Funds and fees | 3 | 9 | 1,090 | **7.4%** |
| General | 1 | 2 | 874 | **6.0%** |
| Identity Verification | 4 | 10 | 612 | **4.2%** |
| Data and analytics | 1 | 4 | 436 | **3.0%** |
| Compliance and audit | 1 | 4 | 98 | **0.7%** |
| Feedback | 1 | 2 | 62 | **0.4%** |
| Card issuing | 5 | 10 | 39 | **0.3%** |
| Platforms | 2 | 3 | 34 | **0.2%** |
| **Total** | **34** | **97** | **14,654** | **100%** |

> V4 taxonomy counts: 14 case types · 43 issue types · 99 L3 reasons. Volume actuals from `Contact breakdown since April 2026.md` (1 April – 1 July 2026, ~3 months, 14,654 contacts). No action required and Non-merchant requests are excluded from the volume table (no automated contact volume in this cut).
>
> **Data quality note**: this cut carries a long tail of misclassified issue-type/case-type combinations (e.g. "Refunds" tagged under Payouts, "Transaction status" tagged under seven different case types) — each individually under 1% of its parent case type's volume, but collectively indicating classifier/agent tagging noise at the issue-type level. Case-type-level mix above is not materially affected. Run `/taxonomy-classification-qa` before relying on issue-type-level splits from this cut.


**Prioritisation implications:**

> Note: ranking below reflects the April–June 2026 cut. Relative order shifted from the prior 6-month view — Payouts and Technical issue both moved above Account management and access, and Identity Verification moved out of the long tail. Treat this as a live re-prioritisation trigger, not just a numbers refresh.

- **Accepting payments at 43.5%** remains the single highest-leverage area for AI resolution rate improvement and content investment. The content strategy's Transactions guide programme (projected 15.53% Fin resolution rate uplift) is the highest-impact initiative available. See `content-strategy-2026.md`.
- **Payouts at 12.6%** (up from 10.0%) — moderately complex to automate; Card payouts (largest single issue type in this cut) and Bank payouts status queries are the primary drivers.
- **Technical issue at 11.2%** (up from 7.8%) — complex to automate; most require data access and diagnostic tooling rather than content alone. Now the third-largest category — worth revisiting whether it's adequately resourced relative to its new share of volume.
- **Account management and access at 10.6%** (down from 16.9%) — still a top-four category. Two issue types: Login & access and Account changes. Login & access is operationally urgent — merchants cannot work until resolved. **Specific Fin opportunity**: a share of Account management and access contacts arrive via "Other" channel (likely the account unlock web form). Unlike the general Dashboard Webform, Fin can be applied to the account unlock form. See `fin-involvement-rate-prd.md` for Fin-eligible volume — re-check against this cut, as the prior ~1,159 contact (~4.9%) estimate was based on the 6-month view.
- **Funds and fees at 7.4%** — primary target for the content strategy's Balances & Settlements initiative (P2 settlement status and balance API lookups for Fin — see `fin-email-auth-data-policy-prd.md`).
- **General at 6.0%** — covers sales inquiries, spam, duplicates, and no-action contacts. A meaningful share is likely already auto-closed or triaged — worth auditing for quick wins.
- **Identity Verification at 4.2%** (up from 0.1%) — the largest mix shift in this cut. Verify whether this reflects genuine IDV volume growth or a classification/reporting change before acting on it; if genuine, this case type now warrants active prioritisation rather than long-tail monitoring.
- **Long tail (< 4% each)**: Data and analytics, Compliance and audit, Feedback, Card issuing, Platforms — monitor rather than prioritise for AI/content investment until the top categories are well contained. Non-merchant requests (previously 1.5%) does not appear in this cut — manual classification only, see note below.


## Known Gaps & Notes

**B2C taxonomy (2027)** — No consumer-facing query types exist yet. The 2027 consumer wallet launch will require new case types or issue types covering: balance disputes, interest queries, card freeze/unfreeze, rewards/cashback issues, and vulnerable customer escalation. These need to be defined before launch. See `care-product-model.md` → B2C Launch Considerations.

**B2B banking taxonomy (2028+)** — Funds and fees covers current PSP balance queries but has no provision for interest/yield, merchant deposits, or treasury management. These will need adding when B2B banking products launch. See `care-product-model.md` → B2B Banking Evolution.

**Identity Verification structure** — Identity Verification is a newer standalone document verification product with its own taxonomy embedded here. The N/A issue type (with reasons like Automated, Self resolved, Spam) classifies non-actionable contacts for this product rather than being a support query type in the traditional sense. Identity Verification is planned to be integrated into payment verification in 2027, at which point its taxonomy will likely need to be restructured: some issue types may merge into Accepting payments → Authentication, and product-specific reasons reviewed for relevance. **Update (July 2026)**: volume share jumped from 0.1% to 4.2% in the April–June cut — confirm whether this is genuine growth before the 2027 integration plan is finalised.

**Platforms is light** — Only two issue types and three reasons. Given Platform is the primary 2026 delivery focus, this is likely intentionally minimal for now and will need expanding as the Platform support model develops.

**No action required and Non-merchant requests** — V4 defines these with no L3 reasons (agent-only, manual classification). These case types are excluded from AI classification and Fin routing, and do not appear at all in the native V4 volume cut (`Contact breakdown since April 2026.md`) — confirm this is expected (manual-only, as designed) rather than a routing/tagging gap.

**Compliance and audit** — V4 consolidates from two issue types (Compliance evidence + Other compliance) into one issue type (Compliance evidence) with "Other compliance docs" as a reason. Issue type count drops from 2 to 1.

**Issue-type-level tagging noise (July 2026)** — The April–June cut shows reasons and issue types attached to the wrong case type in a long tail of low-volume rows (e.g. "Refunds" under Payouts, "Card management" reasons appearing under Accepting payments). Case-type totals in the Summary Counts & Volume table are reliable; issue-type-level splits within each case type should be QA'd before use in prioritisation decisions.
