---
id: 22435536544146
section_id: 26818689421074
title: "Case Classification"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22435536544146-Case-Classification"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-04-10T11:25:11Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JBYRMGF77CKY5K23E5CZMHAV"]
label_names: ["case_classification", "case_classification_guidance"]
user_segment_ids: [11003606966930]
archive: false
---

**Case classification** is the way we categorise support cases based on what the merchant is actually experiencing. Cases are grouped by merchant-reported issues. 

Use this guide to select the right **Case Type** and **Issue Type** every time.**Case Types, Issue Types & Reasons****Case Classification (Updated)**

**Objective:** To provide a standardized taxonomy for classifying merchant inquiries in Zendesk. Each Case Type is broken down into Issue Types and specific Reasons with clear definitions to ensure data accuracy and proper routing.

## **Accepting payments ⬅️**

**Definition:** Refers to the technical lifecycle of customer-initiated transactions (processing, authorization, capture/void, refunds/reversals, disputes) for goods and services.

_Note: Do NOT select this for requests to enable new payment methods or update billing descriptors, use **Account management** instead._

| **Issue Type** | **Reason** | **Reason Definition** |
| --- | --- | --- |
| **Transaction status** | Declined / failed action | IF a customer payment was explicitly rejected with a response code by a bank or scheme, OR if the merchant requests a root cause analysis for specific declined transactions or error codes. |
|  | Stuck in status / status enquiry | IF a merchant reports a payment stuck in an intermediate state (e.g. Authorized or Captured), requests confirmation of current status, or questions processing logic. |
|  | Missing or unrecognised transaction | IF a merchant claims a transaction occurred but cannot find it in the portal/logs, or asks for investigation where there is ambiguity. |
|  | Customer charged twice | IF a merchant reports a duplicate charge. |
|  | Proof of payment (ARN, RNN, bulk) | IF a merchant requests specific identifiers (ARN, RRN) to provide to a customer or requests bulk transaction metadata/logs. |
|  | Failed but customer charged | IF the merchant reports that their customer was charged despite the payment showing as declined in the system. |
| **Refunds** | Refund failed / manual refund | IF an attempt to return funds results in a decline or the merchant cannot process the refund self-service due to technical/scheme rules. |
|  | Refund proof | IF a merchant needs documentation to prove a refund was successfully processed. |
|  | Refund reversal | IF a processed refund needs to be undone or was performed in error. |
|  | Refund status enquiry | IF the merchant is inquiring about the current status of a refund or reporting a status discrepancy. |
| **Authentication (3DS)** | 3DS decline | IF a transaction fails with a 3DS-related error or the authentication process is not triggered/completed as expected. |
|  | Liability shift status | IF the merchant is asking about liability shift for a 3DS processed payment or chargeback protection logic. |
|  | SCA / exemption issue | IF the query relates to Strong Customer Authentication rules or requests to bypass 3DS. |
| **Fraud and risk** | Risk rules | IF a payment was blocked by the Risk engine, or the merchant requests changes to risk rules, blocklists, or threshold settings. |
|  | Trustlist & decline list | IF the merchant wants to add/remove specific entities (IP, Email, Card) from a block or allow list. |
|  | AVS / CVV mismatch | IF the issue relates to Address Verification Service (AVS) or CVV checks and failures. |
|  | Velocity limit reached | IF blocks are occurring due to too many attempts in a short timeframe. |
| **Disputes** | Dispute status | IF the merchant is inquiring about the status, lifecycle, or outcome of a dispute. |
|  | Dispute adjustment | IF the merchant seeks clarification on financial adjustments resulting from disputes (e.g., unexpected debits). |
|  | Evidence help and submission | IF the merchant is actively defending a dispute and needs guidance on required documents or file submission. |
| **Performance** | Acceptance rate issue / optimisation | IF a merchant reports a drop in overall approval ratios or flags a trend of declines across multiple transactions. |
|  | All payments failing | IF the merchant reports a systemic failure where most or all payments are failing. |

 

## **Payouts ➡️**

**Definition:** Refers to the lifecycle of a payout made by card or bank payout, including status, declines, reversals, and proofs.

| **Issue Type** | **Reason** | **Reason Definition** |
| --- | --- | --- |
| **Bank payouts** | Declined / failed bank payout | IF a bank payout was declined by the receiving institution. |
|  | Proof of bank payout | IF the recipient claims they haven't received funds and the merchant needs a confirmation receipt. |
|  | Bank payout stuck in pending / status inquiry | For bank payouts that are delayed, stuck, or held for compliance/sanctions reviews. |
|  | Bank payout returns | IF a merchant asks to reverse or return a bank payout. |
| **Card payouts** | Card payout stuck in pending / status inquiry | IF a merchant asks why a card payout is stuck in a "Pending" state. |
|  | Declined / failed card payout | IF a merchant asks why a card payout was declined. |
|  | Proof of card payout | IF the merchant needs a card payout proof or RRN to provide to a customer. |
|  | Card payout reversal | IF a merchant asks to reverse a card payout. |

 

## **Funds and fees 💰**

**Definition:** Refers to the flow of money in the merchant balance, their settlements, and any associated fees.

| **Issue Type** | **Reason** | **Reason Definition** |
| --- | --- | --- |
| **Settlements** | Delayed / missing settlement | IF an expected settlement is not showing on the Dashboard or has not arrived in the merchant's bank account. |
|  | Reconciliation issue | IF the merchant is struggling to match report data to bank statements or reports a discrepancy. |
| **Balances** | Balance confirmation | IF the merchant needs a Statement of Account (SOA) or balance confirmation for audit purposes. |
|  | Negative balance | IF the merchant needs help understanding why they have a negative balance. |
|  | Balance top up | IF the merchant needs to top up their account balance. |
|  | Balance explanation | IF the merchant needs help understanding how funds are allocated or reports discrepancies. |
| **Billing** | Invoice request | IF the merchant needs a copy of their tax or service invoice. |
|  | Fee inquiry | IF the merchant questions a specific charge (e.g., Interchange, Scheme fees, or service fees). |

 

## **Technical setup 🧑🏼‍💻**

**Definition:** Refers to integration or technical issues (API/SDK/webhook/connectivity), including HTTP errors, keys, tokens, and environment issues.

| **Issue Type** | **Reason** | **Reason Definition** |
| --- | --- | --- |
| **API keys** | Create / edit keys | IF the merchant is asking how to create, edit, or troubleshoot API keys. |
|  | Key scopes | IF the merchant is inquiring about required permissions or requesting specific scopes. |
| **API integration** | API error 4XX / logic error | IF the merchant encounters HTTP 400-level errors or reports functional integration bugs. |
|  | API error 5XX | IF the merchant reports HTTP 500-level errors (Service Unavailable, etc.). |
|  | Idempotency / timeout | IF the merchant is experiencing timeout or idempotency issues on API requests. |
| **Tokens** | Network tokens | IF the issue involves Network Tokens, migration, or provisioning status. |
|  | Token migration | IF the merchant is asking about the import or export of their payment tokens. |
| **Integration methods** | Flow / frames | Inquiries regarding Checkout Flow, Frames, or migration to these methods. |
|  | Payment links / HPP | Inquiries regarding Payment Links or Hosted Payment Page issues. |
|  | SDK issue | Inquiries regarding mobile or web SDK issues. |
|  | E-commerce plugin | Inquiries regarding plugins like Shopify, WooCommerce, Magento, etc. |
|  | Apple Pay / Google Pay | Inquiries regarding digital wallet setup, certificates, or domain verification. |
| **Webhooks** | Webhook setup | IF a merchant is unable to successfully configure or connect their webhooks. |
|  | Signature verification / delivery failure | IF the merchant reports delivery latency, missed notifications, or signature logic failures. |
|  | Missing webhook data | IF the merchant reports that the payload data format does not match expectations. |
| **Test environment** | Sandbox issue | IF the issue relates specifically to the non-production/Sandbox environment. |

 

## **Account management ✅**

**Definition:** Refers to dashboard/portal access or structural account changes, including Payment Method enablement and profile updates.

| **Issue Type** | **Reason** | **Reason Definition** |
| --- | --- | --- |
| **Login and access** | Login error / MFA / SSO | IF the merchant cannot enter the Dashboard due to password, MFA, or SSO/SAML errors. |
|  | User permissions | IF adding/removing users or changing what a specific user can see/do. |
|  | Dashboard user audit evidence | IF the merchant requests an audit log of actions performed in the portal. |
|  | Dashboard error | IF a Dashboard page fails to load or behaves unexpectedly after successful login. |
| **Account updates** | Pricing change | IF the merchant is requesting to update their contract or commission rates. |
|  | Account settings update | IF the request involves configuring processing channels or updating legal/administrative details. |
|  | Terminations | IF the merchant explicitly asks to close their account. |

 

## **Data and analytics 📊**

**Definition:** Refers to issues about reports from the Dashboard or via SFTP, including data quality and generation.

| **Issue Type** | **Reason** | **Reason Definition** |
| --- | --- | --- |
| **Reporting** | Report not generated / missing | IF the merchant is unable to generate, download, or access a specific report. |
|  | Data mismatch / missing | IF there is a discrepancy or data gap within the reports. |
|  | Custom report request | IF the merchant requires a specific data set or column configuration not available by default. |
|  | SFTP configuration | Inquiries regarding automated reporting via SFTP. |

 

## **Compliance and audit 👀**

**Definition:** Refers to requests for documentation for audit or compliance purposes.

| **Issue Type** | **Reason** | **Reason Definition** |
| --- | --- | --- |
| **Compliance evidence** | PCI / AOC request | IF the merchant asks for security compliance certificates (AOC/PCI-DSS). |
|  | Audit request | IF the query is for formal audit evidence or due diligence questionnaires. |
|  | Sensitive data request | IF the merchant requests sensitive customer information (e.g., full PAN) for legal/regulatory bodies. |
|  | Other compliance docs | General requests for other compliance or regulatory documentation. |

 

## **Identity verification 🪪**

**Definition:** Refers to the KYC/KYB onboarding process and verification requirements.

| **Issue Type** | **Reason** | **Reason Definition** |
| --- | --- | --- |
| **Verification support** | Verification inquiry | General questions regarding the status or requirements of account verification. |
|  | Setup support | IF the merchant needs help during the initial verification setup phase. |
|  | Technical & platform | IF there are technical blockers preventing the submission of verification documents. |
| **Security & Privacy** | Data privacy | Queries regarding GDPR, data handling, or privacy rights. |
|  | Security | Inquiries regarding account security or potential breaches. |
|  | Account & compliance | Verification queries related specifically to account-level compliance blocks. |
