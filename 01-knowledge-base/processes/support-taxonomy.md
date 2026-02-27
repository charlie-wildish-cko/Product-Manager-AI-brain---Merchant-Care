# Support Query Taxonomy — Merchant Care

> Three-level classification system applied to all Zendesk tickets: **Case Type → Issue Type → Reason**.  
> Taxonomy definitions source: `Merchant Care - Taxonomy Analysis - Taxonomy Definitions - V3.csv` (February 2026)  
> Volume actuals source: `support_contacts_flat_table_2025_last_6m.csv` (last 6 months view)  
> Owner: Charlie Wildish — refresh when either source file is updated.


## Taxonomy Tree

### PAYMENTS (IN)
*Inbound transaction lifecycle — processing, authorisation, capture/void, refunds, disputes. Does NOT include enabling new payment methods or configuration (use ACCOUNT MANAGEMENT).*

| Issue Type | Reasons |
| --- | --- |
| **Transaction Status** | Declined / Failed Action; Stuck in status / Status Enquiry; Missing or Unrecognised Transaction; Customer charged twice; Proof of payment (ARN, RNN, Bulk); Failed but customer charged |
| **Authentication (3DS)** | 3DS decline; Liability Shift Status; SCA / Exemption Issue |
| **Refunds** | Refund failed / Manual Refund; Refund proof; Refund reversal; Refund status enquiry |
| **Fraud & Risk Controls** | Risk Rules; Trustlist & Decline List; AVS / CVV Mismatch; Velocity Limit Reached |
| **Disputes / Chargebacks** | Dispute status; Dispute Adjustment; Evidence Help and submission |
| **Performance** | Acceptance Rate Issue / Optimisation; All Payments Failing |


### PAYOUTS
*Outbound money movement — bank and card payouts.*

| Issue Type | Reasons |
| --- | --- |
| **Bank Payouts** | Declined / Failed Bank payout; Proof of Bank Payout; Bank payout stuck in Pending or status Inquiry; Bank Payout Returns |
| **Card Payouts** | Card payout stuck in Pending or status Inquiry; Declined / Failed card payout; Proof of Card Payout; Card payout reversal |


### FUNDS AND FEES
*Merchant balances, settlements, invoices, and fee queries.*

| Issue Type | Reasons |
| --- | --- |
| **Balance** | Balance confirmation; Negative balance; Balance top up; Balance explanation |
| **Settlements** | Delayed / Missing Settlement; Reconciliation issue |
| **Billing & Fees** | Invoice Request; Fee Inquiry |


### TECHNICAL ISSUE
*API, integration, webhooks, tokens, and environment issues.*

| Issue Type | Reasons |
| --- | --- |
| **API Credentials** | Create / Edit Keys; Key Scopes |
| **API Integration** | API Error 4XX / Logic Error; API Error 5XX; Idempotency / Timeout |
| **Integration Methods** | Flow / Frames; Payment Links / Hosted Payment Pages; SDK issue; E-Commerce Plugin; Apple Pay / Google Pay |
| **Webhooks** | Webhook setup; Signature Verification or Delivery Failure; Missing Webhook data |
| **Tokens** | Network tokens; Token migration |
| **Environment** | Sandbox Issue |


### ACCOUNT MANAGEMENT & ACCESS
*Account settings, user management, login issues.*

| Issue Type | Reasons |
| --- | --- |
| **Account Changes** | Pricing Change; Account settings update; Terminations |
| **Login & Access** | Login Error / MFA / SSO; User Permissions; Dashboard user audit evidence; Dashboard Error |


### DATA AND ANALYTICS
*Reporting queries — data availability, accuracy, and configuration.*

| Issue Type | Reasons |
| --- | --- |
| **Reporting** | Report Not Generated / Missing; Data Mismatch / Missing; Custom Report Request; SFTP Configuration |


### PLATFORMS
*Sub-merchant onboarding and fund distribution for marketplace/platform merchants.*

| Issue Type | Reasons |
| --- | --- |
| **Sub-Merchant Onboarding** | Merchant activation and verification; Doc Upload Error |
| **Transfers & Splits** | Transfer or split Failed |


### COMPLIANCE & AUDIT
*PCI, audit evidence, and regulatory documentation requests.*

| Issue Type | Reasons |
| --- | --- |
| **Compliance Evidence** | PCI / AOC Request; Audit request; Sensitive Data Request |
| **Other Compliance** | Other compliance docs |


### ISSUING
*Card issuance, issuing transactions, and issuing-specific integration.*

| Issue Type | Reasons |
| --- | --- |
| **Card Management** | Create / Activate Card; Revoke / Suspend; Spend Controls |
| **Issuing Transactions, Money & Reports** | Issuing Balance; Issuing Settlement & Reconciliation; Issuing Fees; Issuing Transaction Declined / Unexpected Behavior |
| **Issuing Digital Wallets** | Apple Pay / Google Pay |
| **Logistics** | Physical Card Delivery |
| **Mobile App / SDK** | Issuing SDK Integration / Upgrade |


### IDENTITY VERIFICATION
*KYC/KYB verification product queries.*

| Issue Type | Reasons |
| --- | --- |
| **Verification and Technical Support** | Verification Inquiry; Setup Support; Technical & Platform |
| **Security, Privacy and Compliance** | Data Privacy; Account & Compliance; Security |
| **Formal Complaint** | Formal Complaint |
| **N/A** | Automated; Follow Up; Sales Lead; Self Resolved; Spam; 3rd Party |


### FEEDBACK
*Merchant product feedback — not a support query, no resolution required.*

| Issue Type | Reasons |
| --- | --- |
| **Product Feedback** | Feature request; Feature usage |


### GENERAL
*Miscellaneous inbound contacts that don't fit elsewhere.*

| Issue Type | Reasons |
| --- | --- |
| **Inquiries** | Sales inquiry; Spam / Duplicate / No action / Follow Ups |


### No Action Required
*Administrative classification for contacts that require no Care response.*

| Issue Type | Reasons |
| --- | --- |
| **No Response Needed** | No action required by Merchant Care; Duplicate; Spam |
| **Sales** | Sales Enquiry |


### Non-Merchant Requests
*Contacts originating from parties other than the merchant — routed or closed without standard support handling.*

| Issue Type | Reasons |
| --- | --- |
| **Cardholders** | Cardholder Complaints |
| **Third Parties** | Issuing Bank Requests; Authorities; Schemes; TPA Requests |


## Summary Counts & Volume

Contact volume actuals from `support_contacts_flat_table_2025_last_6m.csv` (last 6 months):

| Case Type | Issue Types | Reasons | Contacts | % of Volume |
| --- | --- | --- | --- | --- |
| PAYMENTS (IN) | 6 | 20 | 10,049 | **42.8%** |
| ACCOUNT MANAGEMENT & ACCESS | 2 | 7 | 3,961 | **16.9%** |
| PAYOUTS | 2 | 8 | 2,345 | **10.0%** |
| FUNDS AND FEES | 3 | 9 | 1,760 | **7.5%** |
| TECHNICAL ISSUE | 6 | 18 | 1,828 | **7.8%** |
| GENERAL | 1 | 2 | 1,802 | **7.7%** |
| DATA AND ANALYTICS | 1 | 4 | 763 | **3.2%** |
| NON MERCHANT REQUESTS | 2 | 5 | 350 | **1.5%** |
| COMPLIANCE & AUDIT | 2 | 5 | 283 | **1.2%** |
| FEEDBACK | 1 | 2 | 142 | **0.6%** |
| IDENTITY VERIFICATION | 4 | 10 | 25 | **0.1%** |
| ISSUING | 5 | 10 | 88 | **0.4%** |
| PLATFORMS | 2 | 3 | 85 | **0.4%** |
| **Total** | **37** | **~103** | **23,481** | **100%** |

> Summary counts from `support_contacts_flat_table_2025_last_6m.csv` (last 6 months). Previous estimates (from Charlie Wildish, February 2026) are superseded by these actuals.

**Prioritisation implications:**

- **PAYMENTS (IN) at 42.8%** remains the single highest-leverage area for AI resolution rate improvement and content investment. The content strategy's Transactions guide programme (projected 15.53% Fin resolution rate uplift) is the highest-impact initiative available. See `content-strategy-2026.md`.
- **ACCOUNT MANAGEMENT & ACCESS at 16.9%** is the second-largest category. Two issue types: Login & Access and Account Changes. Login & Access is operationally urgent — merchants cannot work until resolved. **Specific Fin opportunity**: a share of AMA contacts arrive via "Other" channel (likely the account unlock web form). Unlike the general Dashboard Webform, Fin can be applied to the account unlock form — ~1,159 contacts (~4.9% of total in last 6m) are Fin-eligible. See `fin-involvement-rate-prd.md`.
- **PAYOUTS at 10.0%** — moderately complex to automate; Bank Payout and Card Payout status queries are the primary issue types.
- **FUNDS AND FEES at 7.5%** — primary target for the content strategy's Balances & Settlements initiative (P2 settlement status and balance API lookups for Fin — see `fin-email-auth-data-policy-prd.md`). Third-tier priority by volume.
- **TECHNICAL ISSUE at 7.8%** — complex to automate; most require data access and diagnostic tooling rather than content alone.
- **GENERAL at 7.7%** — covers sales inquiries, spam, duplicates, and no-action contacts. A meaningful share is likely already auto-closed or triaged — worth auditing for quick wins.
- **Long tail (< 4% each)**: DATA AND ANALYTICS, NON MERCHANT REQUESTS, COMPLIANCE, FEEDBACK, IDENTITY VERIFICATION, ISSUING, PLATFORMS — monitor rather than prioritise for AI/content investment until the top four categories are well contained.


## Known Gaps & Notes

**B2C taxonomy (2027)** — No consumer-facing query types exist yet. The 2027 consumer wallet launch will require new case types or issue types covering: balance disputes, interest queries, card freeze/unfreeze, rewards/cashback issues, and vulnerable customer escalation. These need to be defined before launch. See `care-product-model.md` → B2C Launch Considerations.

**B2B banking taxonomy (2028+)** — FUNDS AND FEES covers current PSP balance queries but has no provision for interest/yield, merchant deposits, or treasury management. These will need adding when B2B banking products launch. See `care-product-model.md` → B2B Banking Evolution.

**IDENTITY VERIFICATION structure** — Identity Verification is a newer standalone document verification product with its own taxonomy embedded here. The N/A issue type (with reasons like Automated, Self Resolved, Spam) classifies non-actionable contacts for this product rather than being a support query type in the traditional sense — consistent with a product that has its own contact handling pattern. Identity Verification is planned to be integrated into payment verification in 2027, at which point its taxonomy will likely need to be restructured: some issue types may merge into PAYMENTS (IN) → Authentication, and product-specific reasons reviewed for relevance.

**PLATFORMS is light** — Only two issue types and three reasons. Given Platform is the primary 2026 delivery focus, this is likely intentionally minimal for now and will need expanding as the Platform support model develops.
