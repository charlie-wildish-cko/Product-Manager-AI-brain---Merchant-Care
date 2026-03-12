# Checkout.com Product Definitions

Source: checkout.com/docs (scraped March 2026)
Cross-reference: `01-knowledge-base/Checkout Products and teams.csv`

**Planned use**: Map against support contact data to identify which products drive contact volumes.

---

## How to read this file

| Column | Meaning |
|---|---|
| Product | Name as it appears in the product catalogue CSV |
| Category | From the CSV |
| What it is | One-sentence definition from docs |
| Geography | Countries/regions where customers can use it |
| Payment type | Wallet / bank transfer / card scheme / BNPL / etc. |
| Integration notes | Key merchant setup or complexity signals |
| Contact risk | Pre-populated where inferable from product type; to be validated against contact data |

Contact risk tags: `high` / `medium` / `low` / `unknown`
Risk reasons: dispute-prone · mandate-management · setup-complexity · redirect-failure · auth-friction · account-management

---

## Payment Methods

| Product | Geography | Payment type | What it is | Integration notes | Contact risk |
|---|---|---|---|---|---|
| Apple Pay | Global (non-EEA/UK requires account manager) | Digital wallet | Enables customers to authenticate card payments using Touch ID or Face ID without manually entering card details. | Requires domain registration; Apple Pay via KNET available for Kuwait; special rules for Mada outside Saudi Arabia. | low — well-understood; friction mainly at setup |
| Google Pay | Global (UAE/SA require account manager approval) | Digital wallet | Enables one-touch payments on website or Android app using cards connected to a Google account. | Requires Google Pay & Wallet Console registration, domain allowlisting, and public key configuration. | low — well-understood; friction mainly at setup |
| ACH Direct Debit | United States | Bank transfer / direct debit | Electronic funds transfer enabling US customers to move money between bank accounts. | Requires explicit written consent (NACHA rules); pre-notification requirements; account manager enablement needed. | high — mandate management, payment failures, NACHA compliance queries |
| AlipayCN | Customers: China. Merchants: HK, Singapore, EEA, UK | Wallet | Mobile payment service for Chinese consumers enabling one-time and recurring purchases. | Redirect flow; CNY/HKD/SGD currencies; account manager enablement needed. | medium — regional; redirect failures, currency queries |
| AlipayHK | Customers: Hong Kong. Merchants: HK, Singapore, EEA, UK | Wallet | Mobile payment service for Hong Kong consumers enabling one-time and recurring purchases. | Redirect flow; HKD/SGD currencies; account manager enablement needed. | medium — regional; redirect failures |
| Alma | Europe | BNPL | Buy-now-pay-later solution enabling customers to pay 15 or 30 days after purchase. | Account manager enablement needed; webhook-driven lifecycle. | medium — BNPL dispute risk, instalment queries |
| Bancontact | Belgium | Card-based | Enables secure online card payments in Belgium. | Redirect flow; webhook required. | low — mature, well-understood |
| Benefit Payment Gateway | Bahrain | Online banking (redirect) | Enables secure online payments in Bahrain. | Redirect flow; BHD settlement; account manager enablement. | low — niche geography, low volume expected |
| Bizum | Spain | Bank transfer | Instant bank transfer payment using a phone number, popular in Spain. | Redirect flow; account manager enablement. | medium — bank transfer failures, phone number lookup issues |
| BLIK | Poland | Bank transfer | Real-time mobile payment method in Poland using a 6-digit code. | Roadmap status; no live doc yet. | unknown |
| Boleto Bancario | Brazil | Voucher | Cash voucher payment method in Brazil. | Deprecated — no longer supported. | n/a — deprecated |
| Cartes Bancaires | France | Card scheme | France's predominant card scheme, typically co-branded with Visa or Mastercard. | Auto-retry on Visa/MC if CB declines technically (opt-out available). | medium — co-brand routing queries, retry logic |
| DANA | Customers: Indonesia. Merchants: HK, Singapore, EEA, UK | Wallet | Mobile payment service for Indonesian consumers enabling one-time and recurring purchases. | Flow only; redirect; account manager enablement. | medium — regional; redirect failures |
| Diners Club International | Global | Card scheme | Global credit card scheme accepted alongside Mastercard. | Standard card processing. | low |
| Discover | Global | Card scheme | Global credit card scheme, especially strong in US. | Standard card processing; part of PINless debit US debit network. | low |
| EFTPOS | Australia (Roadmap) | Card scheme | Australian domestic debit card scheme. | Roadmap — not yet live. | unknown |
| eps | Austria | Online banking | Enables online purchases through secure bank transfers in Austria. | Flow only; redirect; account manager enablement; refunds via API only (not Dashboard). | medium — refund process friction |
| Fawry | Egypt | Cash/voucher | Egyptian cash payment and digital payments network. | Don't sell status — not actively sold. | n/a |
| GCash | Customers: Philippines. Merchants: HK, Singapore, EEA, UK | Wallet | Mobile payment service for Filipino consumers enabling one-time and recurring purchases. | Flow or API; redirect; auto-capture only; account manager enablement. | medium — regional; redirect failures |
| Google Pay | Global | Digital wallet | See above. | — | low |
| iDEAL | Netherlands | Bank transfer (online banking) | Direct online bank transfer from customer's bank account to merchant's bank account. | Auto-capture only; webhook required; account manager enablement. | medium — bank transfer failures, payment status queries |
| Jaywan | UAE/GCC (Roadmap) | Card scheme | Emerging GCC domestic debit card scheme. | Roadmap — not yet live. | unknown |
| JCB | Asia, global | Card scheme | Japanese card scheme accepted globally, especially in Asia. | Mixed availability; processed via CP Berlin team. | low |
| KakaoPay | Customers: Korea. Merchants: HK, Singapore, EEA, UK | Wallet | Mobile payment service for Korean consumers enabling one-time and recurring purchases. | Flow or API; redirect; auto-capture only; KRW/HKD/SGD. | medium — regional |
| Klarna BNPL (Collecting) | Europe, US, AU + others | BNPL | Flexible payment options: pay now, pay later, or pay in instalments. | Requires Klarna Merchant Portal registration; webhook-driven; dispute notifications in Klarna portal. | high — BNPL dispute-prone, instalment queries, high-risk order monitoring |
| Klarna (Gateway) | — | BNPL | Gateway model for Klarna — not actively sold. | Don't sell status. | n/a |
| Klarna Crypto | — | BNPL / Crypto | Klarna's crypto payment option. | Beta. | unknown |
| Klarna Debit Risk (Collecting) | AT, BE, FI, DE, NL, ES, SE | Pay-by-bank | Klarna's bank transfer option for restricted/high-risk merchant segments. | API-only (no hosted UI); auto-capture; no disputes or void; Beta. | medium — niche; eligibility queries |
| Knet | Kuwait | Debit card (domestic) | Enables purchases with local Kuwaiti debit cards issued by member banks. | Redirect; auto-capture; account manager enablement. | low |
| Mada | Saudi Arabia (also international co-branded) | Debit card (domestic + Visa/MC) | Saudi Arabia's domestic payment network, co-branded internationally with Visa/Mastercard. | Full capture only (no partial); 3DS recommended; BIN list maintenance required. | medium — capture restriction queries, Apple Pay routing rules |
| Maestro | Global | Card scheme | Mastercard's international debit card scheme (Pilot status). | Pilot. | unknown |
| Mastercard | Global | Card scheme | Leading global card scheme for credit and debit payments. | Mixed availability; multiple processing teams. | low |
| MB Way | Portugal | Digital wallet | Popular digital wallet in Portugal for online payments. | Flow only; redirect; account manager enablement. | low |
| MobilePay | Denmark, Finland | Wallet | Leading Nordic mobile wallet for instant payments via smartphone. | Manual or auto-capture; Flow or API; account manager enablement. | low |
| Multibanco | Portugal | Voucher | Enables cash or debit payments at ATMs or via banking app across Portugal. | Redirect; webhook required; account manager enablement. | medium — voucher expiry queries, async payment status |
| NYCE | United States | Debit network (PINless) | US regional debit network, part of PINless debit processing. | Enabled via PINless Debit product. | low |
| Octopus | Hong Kong | Digital wallet | Contactless card and digital wallet payments in Hong Kong. | Beta; Flow or API; account manager enablement. | unknown — Beta |
| OmanNET | Oman | Debit card (domestic) | Domestic payment network in Oman for online debit card payments. | API-only; OTP authentication may apply. | medium — OTP/auth friction |
| PayNow | Singapore | Digital wallet (real-time transfer) | Real-time payment service in Singapore enabling fund transfers via mobile number. | Auto-capture only; no chargebacks or recurring; account manager enablement. | low |
| PayPal | Global (Pay Later: AU, FR, DE, IT, ES, US) | Digital wallet | Enables payments using credit/debit cards connected to a PayPal account, with Pay Now, Continue, and Pay Later options. | Digital goods require explicit PayPal agreement; Seller Protection requires full name/address. | medium — PayPal dispute process differs from card disputes; Pay Later queries |
| Pix | Brazil (Roadmap) | Bank transfer (instant) | Brazil's instant payment system operated by the central bank. | Roadmap — not yet live. | unknown |
| Przelewy24 | Poland | Online banking | Enables secure online payments in Poland via redirect. | Redirect; webhook; account manager enablement; various response codes to handle. | medium — redirect/bank transfer failures |
| Pulse | United States | Debit network (PINless) | US regional debit network, part of PINless debit processing. | Enabled via PINless Debit product. | low |
| QPay | Qatar | Online banking | Enables secure online payments in Qatar via bank transfer gateway. | No auto-capture, auth, or recurring; refunds only; account manager enablement. | low — limited capabilities reduce query surface |
| Samsung Pay | Global (Roadmap) | Digital wallet | Samsung's mobile payment wallet. | Roadmap — not yet live. | unknown |
| SEPA Direct Debit Core | SEPA region (EU) | Direct debit (B2C) | Standard SEPA direct debit for consumer bank accounts across the EU. | Mandate required with 14-day pre-notification; IBAN/BIC collection; creditor ID needed. | high — mandate management, payment failures, pre-notification queries |
| SEPA Direct Debit B2B | SEPA region (EU) | Direct debit (B2B) | SEPA direct debit variant for business-to-business transactions. | Same mandate requirements as Core but B2B only; Beta. | high — same as Core; B2B adds complexity |
| SeQura | Spain | BNPL | Instalment payment plans popular in Spain. | Redirect; API only; manual or auto capture; account manager enablement. | medium — BNPL instalment queries |
| Sofort | Europe | Online banking | Sofort online banking payment (deprecated). | Deprecated — no longer supported. | n/a — deprecated |
| STAR | United States | Debit network (PINless) | US regional debit network, part of PINless debit processing. | Enabled via PINless Debit product. | low |
| Accel | United States | Debit network (PINless) | US regional debit network, part of PINless debit processing. | Enabled via PINless Debit product. | low |
| STC Pay | Saudi Arabia | Digital wallet | Digital wallet enabling fund transfers and ecommerce payments in Saudi Arabia. | Flow or API; auto-capture; account manager enablement. | low |
| Swish | Sweden | Bank transfer (mobile) | Popular Swedish mobile payment app for instant online purchases via banking app. | Beta; redirect; no chargebacks or recurring; account manager enablement. | low |
| Tabby (Collecting) | MENA | BNPL | Splits payments into four instalments, popular in MENA. | Gateway and Collecting models; manual or auto capture; account manager enablement. | high — BNPL, instalment queries, dispute-prone |
| Tabby (Gateway) | MENA | BNPL | Gateway model for Tabby BNPL in MENA. | Beta. | high — same as Collecting |
| Tamara (Collecting) | UAE, Saudi Arabia | BNPL | Split or deferred payment options for UAE and Saudi consumers. | Flow only; auto-capture; no recurring; account manager enablement. | high — BNPL, dispute-prone |
| Tamara (Gateway) | UAE, Saudi Arabia | BNPL | Gateway model for Tamara in UAE and Saudi Arabia. | Beta. | high — same as Collecting |
| Touch 'n Go | Customers: Malaysia. Merchants: HK, Singapore, EEA, UK | Wallet | Mobile payment service for Malaysian consumers with recurring payment support. | Flow only; redirect; auto-capture; account manager enablement. | medium — regional |
| TrueMoney | Customers: Thailand. Merchants: HK, Singapore, EEA, UK | Wallet | Mobile payment service for Thai consumers enabling one-time and recurring purchases. | Flow or API; redirect; auto-capture; account manager enablement. | medium — regional |
| Twint | Switzerland | Digital wallet | Swiss mobile payment wallet (pass-through or prepaid card). | Manual capture only (full capture); no recurring; redirect; account manager enablement. | medium — capture restrictions, no recurring = setup queries |
| UnionPay - Gateway | Asia, global | Card scheme | China's dominant card scheme, accepted globally. | Beta; processed via CP Berlin. | medium — acceptance rate queries |
| Venmo | United States | Digital wallet (P2P) | Social payment service for US customers to pay businesses and friends. | US-only; USD only; Venmo app required; account manager enablement. | low |
| Vipps | Norway (customers: NO, SE) | Wallet | Leading Nordic mobile wallet for instant smartphone payments. | Manual capture; no disputes or recurring; Flow or API; account manager enablement. | low |
| Visa | Global | Card scheme | World's largest card network for credit and debit payments. | Mixed availability; multiple processing teams. | low |
| WeChat Pay CN | Customers: China. Merchants: varies | Wallet | WeChat Pay for mainland Chinese consumers. | Redirect; auto-capture; 10-minute payment expiry; account manager enablement. | medium — regional; expiry/redirect queries |
| WeChat Pay HK | Customers: Hong Kong. Merchants: varies | Wallet | WeChat Pay for Hong Kong consumers. | Redirect; auto-capture; 10-minute payment expiry; account manager enablement. | medium — regional |
| Wero | Europe (Roadmap) | Wallet | European mobile payment wallet (pan-European initiative). | Roadmap — not yet live. | unknown |

---

## Acceptance & Checkout Products

| Product | Category | What it is | Key capabilities | Contact risk |
|---|---|---|---|---|
| Flow Web | Flow | Pre-built, customizable payment interface for embedding in websites. | Handles tokenisation, 3DS auth, payment method display, input validation; Remember Me support; responsive design. | medium — integration setup queries, 3DS friction |
| Flow Android SDK | Flow / Mobile SDK | Pre-built payment UI embeddable in Android apps. | Built-in 3DS, Apple/Google Pay, customizable UI; min SDK 21. | medium — SDK integration queries |
| Flow iOS SDK | Flow / Mobile SDK | Pre-built payment UI embeddable in iOS apps. | Built-in 3DS, Apple/Google Pay, customizable UI; min iOS 15. | medium — SDK integration queries |
| Flow React Native SDK | Flow / Mobile SDK | Pre-built payment UI for React Native apps. | Don't sell status. | n/a |
| Hosted Payment Page | Hosted Payment Page | Checkout.com-hosted page to which merchants redirect customers to complete payment. | PCI compliance handled by CKO; 40+ payment methods; Remember Me; 24-hour session validity; branding customisation. | medium — redirect/session expiry queries, customisation |
| Payment Links | Payments Links | Unique URL redirecting customers to a Hosted Payments Page to complete payment. | No-code option; 40+ methods; shareable via any channel; Dashboard or API management. | low — simple product; main queries around expiry or method availability |
| Remember Me | Flow | Feature allowing customers to save payment details across all Remember Me-enabled merchants. | Cross-merchant credential access; tokenised storage in Vault. | medium — privacy queries, unexpected card charges |

---

## Optimisation Products

| Product | Category | What it is | Key capabilities | Contact risk |
|---|---|---|---|---|
| Intelligent Acceptance | Intelligent Acceptance | AI-powered solution that dynamically applies optimisations to maximise payment conversion. | 3DS/SCA exemption management; adaptive messaging; network token provisioning; smart routing; performance dashboard. Requires 5,000+ monthly transactions. | low — self-serve insights; queries mainly around expected vs actual uplift |
| Network Tokens | Network Tokens | Unique digital identifiers replacing card PANs to improve acceptance and security. | Auto-updated when underlying card changes; reduces declines from expired cards; improves security. | low — mostly invisible to merchants; queries on tokenisation failures |
| Real-Time Account Updater | Real-Time Account Updater | Service that automatically updates stored card details when they change. | Monitors stored credentials; auto-refreshes on issuer update; Mastercard and Visa supported; webhook notifications. | low — queries mainly on unexpected updates or reconciliation |

---

## Vault & Credential Storage

| Product | Category | What it is | Key capabilities | Contact risk |
|---|---|---|---|---|
| Integrated Vault | Vault | Credential storage embedded within Checkout.com's payment processing. | Stores customer details, payment instruments, and network tokens; only the merchant can access their own vault. | medium — tokenisation queries, stored credential management |
| Standalone Vault | Vault | Independent credential storage for merchants who need vault services without full CKO payment processing. | Beta; separate deployment from payment processing. | medium — Beta; setup and integration queries |
| Forward API | Vault | Beta feature enabling merchants to enrich payment requests with CKO-stored credentials and forward them to third-party API endpoints. | Allows use of CKO-stored tokens with external processors. | medium — Beta; third-party routing queries |

---

## Risk & Fraud Products

| Product | Category | What it is | Key capabilities | Contact risk |
|---|---|---|---|---|
| Authentication (3DS) | Authentication | Security protocol requiring customers to complete an additional authentication step for online card payments. | Frictionless and challenge flows; liability shift to issuer on success; SCA compliance for Europe; supports Visa Secure, MC Identity Check, Amex SafeKey. | high — 3DS friction causes abandonment; false declines; SCA exemption queries |
| Fraud Detection | Fraud Detection | Rules-based solution for managing payment fraud risk by controlling which payments are accepted. | Risk rules and lists; pre-auth and post-auth assessment; strategy testing and simulation; AVS; fraud flagging. | medium — false positive queries, rule tuning requests |
| Fraud Detection Pro | Fraud Detection | Enhanced fraud detection with more complex risk strategies and additional features. | Everything in Fraud Detection plus advanced strategy building and upgraded services. | medium — same as base, higher complexity |
| Disputes | Disputes | Chargeback management system for responding when customers challenge transaction validity. | Real-time monitoring; evidence submission; dispute acceptance or challenge; scheme programme monitoring; reporting. | high — core operational product; high contact volume expected |
| Pre-Disputes | Disputes | Early dispute resolution mechanism to resolve customer concerns before they escalate to chargebacks. | Intervenes in the pre-chargeback window to avoid formal dispute. | high — closely related to Disputes volume |

---

## Identity Verification

| Product | Category | What it is | Key capabilities | Contact risk |
|---|---|---|---|---|
| Identity Verification | Identity Verification | KYC solution enabling businesses to verify the identity of individuals onboarding to their services. | ID document verification; facial biometrics; AML screening (PEPs, sanctions, adverse media). | medium — onboarding friction; false rejection queries |
| Face Authentication | Identity Verification | Facial biometric verification to validate applicant identity. | Standalone face check within the Identity Verification suite. | medium — biometric failure queries |
| ID Document Verification | Identity Verification | Verification that ID documents are authentic and match the individual. | Document authenticity check; cross-referenced with face auth. | medium — document rejection queries |
| Business Verification | Identity Verification | KYB (Know Your Business) verification for businesses. | Roadmap. | unknown |
| Business Screening | Identity Verification | AML screening of businesses against sanctions and adverse media databases. | Roadmap. | unknown |

---

## Payouts

| Product | Category | What it is | Key capabilities | Contact risk |
|---|---|---|---|---|
| Card Payouts | Payouts | Near-instant payouts directly to eligible payment cards. | Rapid disbursement; gig economy / instant settlement use cases; broader eligibility than bank payouts. | medium — failed payout queries, eligibility questions |
| Bank Payouts | Payouts | Payouts to bank accounts via local clearing methods and international payment rails. | Reusable payout instruments; Europe/UK/US merchants; international routing; lower cost than card. | medium — bank routing failures, account validation queries |

---

## Issuing

| Product | Category | What it is | Key capabilities | Contact risk |
|---|---|---|---|---|
| Cards | Issuing | Physical and virtual card issuance for businesses to distribute to employees or customers. | Card lifecycle management (activate, suspend, revoke); customisable card design; digital wallet integration. | medium — card activation/management queries |
| Physical Cards | Issuing | Physical payment cards issued under a business's card programme. | Design customisation; PIN management; activation/renewal. | medium — delivery and activation queries |
| Physical card PIN | Issuing | PIN management for physical issued cards. | PIN set, change, unlock capabilities. | medium — PIN-related queries |
| Card Product | Issuing | The card programme definition (network, product type, features). | Configures the underlying card product rules. | low — configuration handled at setup |
| BIN Management | Issuing | Management of Bank Identification Numbers for an issuing programme. | BIN allocation, configuration, and routing. | low — technical setup; low ongoing contact |
| Cardholder | Issuing | Cardholder profile management. | Create, update, and manage cardholders and their associated cards. | medium — cardholder data queries |
| Spending Controls | Issuing | Configurable limits on how issued cards can be used. | Budget limits, frequency controls, merchant category restrictions. | medium — limit queries, blocked transaction queries |
| Digital Wallets | Issuing | Integration of issued cards into Apple Pay, Google Pay, etc. | Wallet provisioning for virtual and physical cards. | medium — provisioning failures |
| Entity Structure | Issuing | Hierarchical entity setup for card programme participants. | Programme hierarchy configuration. | low — setup complexity |
| Reporting (Issuing) | Issuing | Transaction and programme reporting for issuers. | Reconciliation and analytics for issued card activity. | low |
| Authentication (Issuing) | Issuing | 3DS for transactions on issued cards. | SCA compliance for issued cardholders. | medium — 3DS friction on issued cards |
| Fraud (Issuing) | Issuing | Fraud management for issued card transactions. | Fraud rule configuration for issuing. | medium |
| SCA Exemptions (Issuing) | Issuing | SCA exemption application for issued card transactions. | Reduces friction for low-risk issued card payments. | low |
| SCA Out of Scope (Issuing) | Issuing | Handling of transactions excluded from SCA requirements. | Compliance scoping for issuing. | low |
| Simulation (Issuing) | Issuing | Sandbox simulation of issuing transactions for testing. | Test card authorisation and lifecycle events. | low — development only |
| Transactions (Issuing) | Issuing | View and manage individual issuing transactions. | Transaction history, details, and status. | medium — transaction query and reconciliation |
| Issuing Region | Issuing | Geographic region configuration for an issuing programme. | Region-level programme settings. | low |

---

## Business Account & Funds Management

| Product | Category | What it is | Key capabilities | Contact risk |
|---|---|---|---|---|
| Balances | Business Account | Real-time view of funds held in Checkout Business Account sub-accounts across currencies. | Multi-currency balance visibility; cash flow monitoring. | medium — balance discrepancy queries, currency queries |
| Settlements | Business Account | Process by which Checkout.com transfers collected payment funds to the merchant's account. | Configurable settlement frequency; automatic crediting to sub-accounts. | high — settlement timing and amount queries are a major support driver |
| Transfers | Business Account | Ability to move funds into sub-accounts on demand. | Flexible fund movement between accounts; supports payout funding. | medium — transfer failure queries |
| Corporate Cards | Business Account | Business cards for operational spending, linked to the Checkout Business Account. | Pilot; expense management use case. | unknown — Pilot |

---

## Reporting & Analytics

| Product | Category | What it is | Key capabilities | Contact risk |
|---|---|---|---|---|
| Dashboard Reports | Reporting & Analytics | Web interface for generating and downloading financial and operational reports. | On-demand or scheduled (daily/weekly/monthly); CSV download; field customisation; role-based access. | medium — report access, scheduling, and data discrepancy queries |
| Reports API | Reporting & Analytics | Programmatic interface for automated report retrieval at chosen intervals. | Retrieve report metadata and files; integrate with reconciliation workflows. | low — developer-facing; queries mainly on field definitions |
| Reports API (non-financial) | Reporting & Analytics | Reports API for operational/non-financial data. | Same as Reports API; separate data set. | low |
| Dashboard Reports (non-financial) | Reporting & Analytics | Dashboard access to non-financial operational reports. | Same as Dashboard Reports; separate data set. | low |
| SFTP Reports | Reporting & Analytics | Scheduled CSV report delivery via SFTP. | Automated delivery; pre-filtering by field; RSA key auth. | medium — SFTP connectivity, key management, scheduling queries |
| SFTP (non-financial reports) | Reporting & Analytics | SFTP delivery for non-financial reports. | Same as SFTP Reports; separate data set. | low |
| Analytics Assistant | Reporting & Analytics | AI-powered analytics assistant for querying payment data. | Beta; natural language querying of reporting data. | unknown — Beta |
| Predictive Interchange | Reporting & Analytics | Forecasting tool for interchange cost optimisation. | Mixed availability; cost modelling for interchange fees. | low |

---

## Treasury & FX

| Product | Category | What it is | Key capabilities | Contact risk |
|---|---|---|---|---|
| Acquiring - Daily FX Rates | Treasury & FX | Daily FX rate service for acquiring transactions. | Merchant-facing rate visibility. | low |
| Acquiring - FX Live Market Rates | Treasury & FX | Live market FX rate service for acquiring. | Real-time rate display. | low |
| Acquiring - Scheme FX Rates | Treasury & FX | Scheme-level FX rate service (Visa/Mastercard). | Scheme rate transparency. | low |
| Acquiring - Custom FX markup per currency pair | Treasury & FX | Custom FX markup configuration per currency pair. | Bespoke FX pricing. | medium — FX rate discrepancy queries |
| PTC - FX based on Scheme FX rates | Treasury & FX | Payment-time currency conversion using scheme FX rates (Visa/MC only). | DCC-style conversion at scheme rates. | medium — FX conversion queries |

---

## Partner Integrations & Plugins

| Product | Category | What it is | Contact risk |
|---|---|---|---|
| BigCommerce | Partner Integrations and Plugins | Native Checkout.com plugin for BigCommerce merchants. | medium — plugin setup and update queries |
| Magento 2 | Partner Integrations and Plugins | Native Checkout.com plugin for Magento 2 merchants. | medium — plugin setup and update queries |
| WooCommerce | Partner Integrations and Plugins | Native Checkout.com plugin for WooCommerce merchants. | medium — plugin setup and update queries |
| Shopify (onsite) | Partner Integrations and Plugins | Native onsite Checkout.com integration for Shopify. | medium — plugin setup; Shopify-specific flows |
| Shopify (offsite) | Partner Integrations and Plugins | Offsite redirect integration for Shopify merchants. | medium — redirect and reconciliation queries |
| Salesforce Commerce Cloud | Partner Integrations and Plugins | Native Checkout.com plugin for Salesforce Commerce Cloud. | medium — enterprise plugin setup queries |
| SAP Commerce Cloud | Partner Integrations and Plugins | Native Checkout.com plugin for SAP Commerce Cloud. | medium — enterprise plugin setup queries |
| Basis Theory | Partner Integrations and Plugins | Token vault partner integration. | low |
| BR-DGE | Partner Integrations and Plugins | Payment orchestration layer partner. | low |
| Chargebee | Partner Integrations and Plugins | Subscription billing platform integration. | medium — recurring billing queries |
| Chargify | Partner Integrations and Plugins | Subscription management platform integration. | medium — recurring billing queries |
| GIG | Partner Integrations and Plugins | Partner integration. | unknown |
| Gr4vy | Partner Integrations and Plugins | Payment orchestration layer partner. | low |
| OpenCart | Partner Integrations and Plugins | Native Checkout.com plugin for OpenCart. | low |
| Payrails | Partner Integrations and Plugins | Payment orchestration layer partner. | low |
| Spreedly | Partner Integrations and Plugins | Payment orchestration and vault partner. | low |
| Zuora | Partner Integrations and Plugins | Subscription and recurring billing platform integration. | medium — recurring billing queries |

---

## Dashboard & Internal

| Product | Category | What it is | Contact risk |
|---|---|---|---|
| Dashboard | Dashboard | Checkout.com's merchant-facing web portal for managing payments, settings, and reporting. | high — access, permissions, and navigation queries are a major support category |
| Notifications | Internal products | Merchant notification system for payment events. | medium — notification configuration queries |

---

*Last updated: March 2026. To be validated against support contact data when available.*
