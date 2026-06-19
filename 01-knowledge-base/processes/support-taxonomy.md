# Support Query Taxonomy — Merchant Care

> Three-level classification system applied to all Zendesk tickets: **Case Type → Issue Type → Reason**.  
> Taxonomy definitions source: `Merchant Care - Case Classification v4.0 - Taxonomy v4.csv` (June 2026)  
> Volume actuals source: `support_contacts_flat_table_2025_last_6m.csv` (last 6 months view; volumes reflect V3 case type labels — see name mapping note in Summary Counts section)  
> Owner: Charlie Wildish — refresh when either source file is updated.  
> Payment and fintech terms used in this document follow definitions in [`checkout-terminology.md`](../payment-domain/checkout-terminology.md).


## Taxonomy Tree

### Accepting payments
*Refers to the technical lifecycle of customer-initiated transactions (processing, authorization, capture/void, refunds/reversals, disputes) for goods and services. Does NOT include enabling new payment methods, configuration of processing channels, or updating billing/statement descriptors — use ACCOUNT MANAGEMENT & ACCESS instead. Decline codes 20XXX / 30XXX / 40XXX belong here.*

| Issue Type | Reasons |
| --- | --- |
| **Transaction status (non 3DS & refunds)** | Declined / failed action; Stuck in status / status enquiry; Missing or unrecognised transaction; Customer charged twice; Proof of payment (ARN, RNN, bulk); Failed but customer charged |
| **Authentication (3DS)** | 3DS decline; Liability shift status; SCA / exemption issue |
| **Refunds** | Refund failed / manual refund; Refund proof; Refund reversal; Refund status enquiry |
| **Fraud & risk controls** | Risk rules; Trustlist & decline list; AVS / CVV mismatch; Velocity limit reached |
| **Disputes** | Dispute status; Dispute adjustment; Evidence help and submission |
| **Performance** | Acceptance rate issue / optimisation; All payments failing |


### Payouts
*Refers to the lifecycle of a payout made by card or bank payout. Includes status, declines, reversals, and proofs of payout. Does NOT include settlement of merchant balances (use FUNDS AND FEES instead).*

| Issue Type | Reasons |
| --- | --- |
| **Bank payouts** | Declined / failed bank payout; Proof of bank payout; Bank payout stuck in pending or status inquiry; Bank payout returns |
| **Card payouts** | Card payout stuck in pending or status inquiry; Declined / failed card payout; Proof of card payout; Card payout reversal |


### Funds and fees
*Refers to the flow of money in the merchant balance and their settlements and any associated fees. Includes settlement delays, reconciliation issues, balance queries, and invoice/fee inquiries.*

| Issue Type | Reasons |
| --- | --- |
| **Settlements** | Delayed / missing settlement; Reconciliation issue |
| **Balances** | Balance confirmation; Negative balance; Balance top up; Balance explanation |
| **Billing & fees** | Invoice request; Fee inquiry |


### Technical issue
*Refers to integration or technical issues (API/SDK/webhook/connectivity), including HTTP 4xx/5xx errors, keys, tokens, and test environment issues. Does NOT include payment performance or outcome issues (use Accepting payments instead).*

| Issue Type | Reasons |
| --- | --- |
| **API keys** | Create / edit keys; Key scopes |
| **API integration** | API error 4XX / logic error; API error 5XX; Idempotency / timeout |
| **Tokens** | Network tokens; Token migration |
| **Integration methods** | Flow / frames; Payment links / hosted payment pages; SDK issue; E-commerce plugin; Apple Pay / Google Pay |
| **Webhooks** | Webhook setup; Signature verification or delivery failure; Missing webhook data |
| **Test environment** | Sandbox issue |


### Data and analytics
*Refers to issues about reports either from the Dashboard or via SFTP. Includes issues about how to get a report and issues with report data.*

| Issue Type | Reasons |
| --- | --- |
| **Reporting** | Report not generated / missing; Data mismatch / missing data; Custom report request; SFTP configuration |


### Platforms
*Covers Independent Software Vendors (ISVs) utilising Checkout.com's Integrated Platforms product to embed payments. Includes sub-merchant onboarding and fund distribution for marketplace/platform merchants.*

| Issue Type | Reasons |
| --- | --- |
| **Sub-merchant onboarding** | Merchant activation and verification; Doc upload error |
| **Transfers & splits** | Transfer or split failed |


### Card issuing
*Refers to issuing-related issues. Includes physical or virtual card issues and controls on these cards, issuing transactions, digital wallets, and SDK integration.*

| Issue Type | Reasons |
| --- | --- |
| **Card management** | Create / activate card; Revoke / suspend; Spend controls |
| **Card deliveries** | Physical card delivery |
| **Issuing digital wallets** | Apple Pay / Google Pay |
| **Issuing mobile SDK** | Issuing SDK integration / upgrade |
| **Issuing transactions, funds and reports** | Issuing balance; Issuing settlement & reconciliation; Issuing fees; Issuing transaction declined / unexpected behavior |


### Account management & access
*Refers to access to the Dashboard/Portal to use a feature, or making structural changes to the account. Includes login issues, user permissions, and account configuration. Does NOT include payment processing or integration issues.*

| Issue Type | Reasons |
| --- | --- |
| **Login & access** | Login error / MFA / SSO; User permissions; Dashboard user audit evidence; Dashboard error |
| **Account changes** | Pricing change; Account settings update; Terminations |


### Feedback
*Sentiment and product suggestions. Not a support query — no resolution required.*

| Issue Type | Reasons |
| --- | --- |
| **Product feedback** | Feature request; Feature usage |


### Compliance & audit
*Refers to requests for documentation for audit/compliance purposes, including PCI, AOC, sensitive data, and other compliance docs.*

| Issue Type | Reasons |
| --- | --- |
| **Compliance evidence** | PCI / AOC request; Audit request; Sensitive data request; Other compliance docs |


### General
*Refers to general inquiries which do not fit other case types.*

| Issue Type | Reasons |
| --- | --- |
| **Inquiries** | Sales inquiry; Spam / duplicate / no action / follow ups |


### Identity verification
*Refers to the Identity Verification (IDV) product and services, which use document checks, facial recognition, and automation to verify identity. Includes verification support, compliance, and security queries.*

| Issue Type | Reasons |
| --- | --- |
| **Verification and technical support** | Verification inquiry; Setup support; Technical & platform |
| **Security, privacy and compliance** | Data privacy; Account & compliance; Security |
| **Formal complaint** | Formal complaint |
| **N/A** | 3rd party; Automated; Follow up; Sales lead; Self resolved; Spam |


### No action required
*Manual classification by agents only. Applied to contacts requiring no Care response.*

| Issue Type | Reasons |
| --- | --- |
| **Duplicate** | — |
| **Spam** | — |
| **Sales Enquiry** | — |


### Non-merchant requests
*Manual classification by agents only. Contacts originating from parties other than the merchant — routed or closed without standard support handling.*

| Issue Type | Reasons |
| --- | --- |
| **Cardholder Complaints** | — |
| **Issuing Bank Requests** | — |
| **Authorities** | — |
| **Schemes** | — |
| **TPA Requests** | — |
| **Other** | — |


## Summary Counts & Volume

> **V3 → V4 name mapping**: Volume actuals in the table below come from `support_contacts_flat_table_2025_last_6m.csv`, which uses V3 case type labels. Mapped to V4 names as follows: PAYMENTS (IN) → Accepting payments · ACCOUNT MANAGEMENT & ACCESS → Account management & access · PAYOUTS → Payouts · FUNDS AND FEES → Funds and fees · TECHNICAL ISSUE → Technical issue · GENERAL → General · DATA AND ANALYTICS → Data and analytics · NON MERCHANT REQUESTS → Non-merchant requests · COMPLIANCE & AUDIT → Compliance & audit · FEEDBACK → Feedback · IDENTITY VERIFICATION → Identity verification · ISSUING → Card issuing · PLATFORMS → Platforms.

| Case Type | Issue Types | Reasons | Contacts | % of Volume |
| --- | --- | --- | --- | --- |
| Accepting payments | 6 | 20 | 10,049 | **42.8%** |
| Account management & access | 2 | 7 | 3,961 | **16.9%** |
| Payouts | 2 | 8 | 2,345 | **10.0%** |
| Funds and fees | 3 | 9 | 1,760 | **7.5%** |
| Technical issue | 6 | 18 | 1,828 | **7.8%** |
| General | 1 | 2 | 1,802 | **7.7%** |
| Data and analytics | 1 | 4 | 763 | **3.2%** |
| Non-merchant requests | 2 | 5 | 350 | **1.5%** |
| Compliance & audit | 1 | 4 | 283 | **1.2%** |
| Feedback | 1 | 2 | 142 | **0.6%** |
| Card issuing | 5 | 10 | 88 | **0.4%** |
| Identity verification | 4 | 10 | 25 | **0.1%** |
| Platforms | 2 | 3 | 85 | **0.4%** |
| **Total** | **36** | **~102** | **23,481** | **100%** |

> V4 taxonomy counts: 14 case types · 43 issue types · 99 L3 reasons. Volume actuals from `support_contacts_flat_table_2025_last_6m.csv`. No action required is excluded from volume table (no merchant-facing contact volume).


**Prioritisation implications:**

- **Accepting payments at 42.8%** remains the single highest-leverage area for AI resolution rate improvement and content investment. The content strategy's Transactions guide programme (projected 15.53% Fin resolution rate uplift) is the highest-impact initiative available. See `content-strategy-2026.md`.
- **Account management & access at 16.9%** is the second-largest category. Two issue types: Login & access and Account changes. Login & access is operationally urgent — merchants cannot work until resolved. **Specific Fin opportunity**: a share of Account management & access contacts arrive via "Other" channel (likely the account unlock web form). Unlike the general Dashboard Webform, Fin can be applied to the account unlock form — ~1,159 contacts (~4.9% of total in last 6m) are Fin-eligible. See `fin-involvement-rate-prd.md`.
- **Payouts at 10.0%** — moderately complex to automate; Bank payouts and Card payouts status queries are the primary issue types.
- **Funds and fees at 7.5%** — primary target for the content strategy's Balances & Settlements initiative (P2 settlement status and balance API lookups for Fin — see `fin-email-auth-data-policy-prd.md`). Third-tier priority by volume.
- **Technical issue at 7.8%** — complex to automate; most require data access and diagnostic tooling rather than content alone.
- **General at 7.7%** — covers sales inquiries, spam, duplicates, and no-action contacts. A meaningful share is likely already auto-closed or triaged — worth auditing for quick wins.
- **Long tail (< 4% each)**: Data and analytics, Non-merchant requests, Compliance & audit, Feedback, Identity verification, Card issuing, Platforms — monitor rather than prioritise for AI/content investment until the top four categories are well contained.


## Known Gaps & Notes

**B2C taxonomy (2027)** — No consumer-facing query types exist yet. The 2027 consumer wallet launch will require new case types or issue types covering: balance disputes, interest queries, card freeze/unfreeze, rewards/cashback issues, and vulnerable customer escalation. These need to be defined before launch. See `care-product-model.md` → B2C Launch Considerations.

**B2B banking taxonomy (2028+)** — Funds and fees covers current PSP balance queries but has no provision for interest/yield, merchant deposits, or treasury management. These will need adding when B2B banking products launch. See `care-product-model.md` → B2B Banking Evolution.

**Identity verification structure** — Identity verification is a newer standalone document verification product with its own taxonomy embedded here. The N/A issue type (with reasons like Automated, Self resolved, Spam) classifies non-actionable contacts for this product rather than being a support query type in the traditional sense. Identity verification is planned to be integrated into payment verification in 2027, at which point its taxonomy will likely need to be restructured: some issue types may merge into Accepting payments → Authentication, and product-specific reasons reviewed for relevance.

**Platforms is light** — Only two issue types and three reasons. Given Platform is the primary 2026 delivery focus, this is likely intentionally minimal for now and will need expanding as the Platform support model develops.

**No action required and Non-merchant requests** — V4 defines these with no L3 reasons (agent-only, manual classification). These case types are excluded from AI classification and Fin routing.

**Compliance & audit** — V4 consolidates from two issue types (Compliance evidence + Other compliance) into one issue type (Compliance evidence) with "Other compliance docs" as a reason. Issue type count drops from 2 to 1.
