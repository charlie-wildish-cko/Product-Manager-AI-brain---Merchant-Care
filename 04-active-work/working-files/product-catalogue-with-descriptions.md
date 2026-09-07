# Product Catalogue with Descriptions

Source files:
- `01-knowledge-base/Checkout Products and teams.csv` (product list, categories, teams)
- `01-knowledge-base/products/product-definitions.md` (product descriptions, matched by `### <Product name>` heading and its `**What it is:**` line)

Generated: 2026-08-20

**Total products: 262. Missing a definition: 0.**

Format: `**Product name** (category) [Product State]: description`

Product State breakdown: Not on roadmap 85 · General availability 73 · Mixed availability 32 · Roadmap 28 · Beta 27 · blank/unset 8 · Deprecated 5 · Don't sell 4

## Agentic Commerce

- **Commerce Protocols** (Agentic Commerce) [Mixed availability]: Catalogue category for emerging agentic-commerce protocols that would let AI agents transact on a merchant's behalf (not yet fully documented).
- **Movement Protocols** (Agentic Commerce) [Roadmap]: Catalogue entry for a related agentic-commerce capability covering movement protocols (not yet fully documented).
- **Trust Protocols** (Agentic Commerce) [Roadmap]: Catalogue entry for a related agentic-commerce capability covering trust/verification standards between agents and merchants (not yet fully documented).

## Analytics

- **Analytics AI Assistant** (Analytics) [blank/unset]: AI-powered analytics assistant that helps merchants explore payment data in natural language, visualise performance, and identify actions to improve results.
- **Custom Analytics** (Analytics) [blank/unset]: Automated notifications that alert merchants to important changes in their payment performance.
- **Payment Lifecycle Analytics** (Analytics) [blank/unset]: Pre-built dashboard tracking end-to-end payment performance from request to acceptance, with payment-level visibility.

## Authentication

- **Bundled Authentication** (Authentication) [General availability]: Configurable authentication platform combining 3DS, Google SPA, and Passkeys for regulatory compliance, fraud reduction, and conversion optimisation.
- **Standalone Authentication** (Authentication) [General availability]: Authentication (e.g. 3DS) performed as a separate API call, decoupled from the payment authorization request.

## Business Account

- **Balances** (Business Account) [General availability]: Real-time view of funds held in Checkout Business Account sub-accounts across currencies.
- **Corporate Cards** (Business Account) [Beta]: Business cards for operational spending, linked to the Checkout Business Account.
- **Fund Acceleration** (Business Account) [Mixed availability]: Service that settles merchant funds faster than scheme collection timelines (e.g. T+1 to merchant vs T+3 from schemes).
- **Interest** (Business Account) [Roadmap]: Catalogue entry for interest on merchant balances held in a Checkout.com Business Account. No Airtable overview text available.
- **Same and Cross-currency Transfers** (Business Account) [Beta]: On-demand fund transfers between Checkout.com accounts in the same or different currencies.

## Dashboard

- **Account Settings** (Dashboard) [General availability]: Dashboard area for managing a merchant's own business/account-level profile information (e.g. business details, notification preferences, contact information).
- **Dashboard** (Dashboard) [General availability]: Checkout.com's merchant-facing web portal for managing payments, settings, and reporting.
- **Settings & Access** (Dashboard) [General availability]: Dashboard area for managing user roles, team member access, and API key/permissions configuration.

## Disputes

- **Disputes** (Disputes) [Mixed availability]: Chargeback management system for responding when customers challenge transaction validity.
- **Pre-Disputes** (Disputes) [General availability]: Early dispute resolution mechanism to resolve customer concerns before they escalate to chargebacks.

## Flow

- **Flow Web** (Flow) [General availability]: Pre-built, customizable payment interface for embedding in websites.
- **Remember Me** (Flow) [General availability]: Feature allowing customers to save payment details across all Remember Me-enabled merchants.

## Fraud Detection

- **Fraud Detection** (Fraud Detection) [General availability]: Rules-based solution for managing payment fraud risk by controlling which payments are accepted.
- **Fraud Detection Pro** (Fraud Detection) [General availability]: Enhanced fraud detection with more complex risk strategies and additional features.

## Hosted Payment Page

- **Hosted Payment Page** (Hosted Payment Page) [General availability]: Checkout.com-hosted page to which merchants redirect customers to complete payment.

## Identity Verification

- **Address Document Verification** (Identity Verification) [Roadmap]: Verification of the authenticity and compliance of an address document, with data extraction via API.
- **AML Screening** (Identity Verification) [Beta]: Standalone check of an individual applicant against politically exposed persons (PEP), sanctions, and adverse media databases.
- **Face Authentication** (Identity Verification) [Beta]: Facial biometric verification to validate applicant identity.
- **ID Document Verification** (Identity Verification) [Beta]: Verification that ID documents are authentic and match the individual.
- **Identity Verification** (Identity Verification) [General availability]: KYC solution enabling businesses to verify the identity of individuals onboarding to their services.

## In-person payments

- **SoftPOS SDK** (In-person payments) [Roadmap]: SDK that turns NFC-enabled devices (phone, tablet, kiosk) into secure payment terminals, embeddable in merchant apps.
- **Traditional HardPOS** (In-person payments) [Not on roadmap]: Traditional, dedicated payment terminals (such as Pax or Ingenico).
- **Unified Commerce** (In-person payments) [Roadmap]: Ability to process in-person and digital payments through the Unified Payments API using merchant-owned devices, combining HardPOS and SoftPOS revenue streams.

## Intelligent Acceptance

- **Intelligent Acceptance** (Intelligent Acceptance) [General availability]: AI-powered solution that dynamically applies optimisations to maximise payment conversion.

## Internal products

- **Airtable Product Catalogue** (Internal products) [General availability]: Internal Airtable database that holds the up-to-date, Product/Marketing/Commercial-verified record of every Checkout.com product.
- **Notifications** (Internal products) [blank/unset]: Merchant notification system for payment events.
- **Website Screening** (Internal products) [Beta]: Verifies a business' website compliance and extracts relevant information from the website.

## Issuing

- **Authentication** (Issuing) [Mixed availability]: 3DS for transactions on issued cards.
- **Cards** (Issuing) [Mixed availability]: Physical and virtual card issuance for businesses to distribute to employees or customers.
- **Configuration** (Issuing) [Mixed availability]: Setup and configuration of an issuing programme (card product setup, entity/BIN structure, cardholder configuration)
- **Control spending** (Issuing) [Mixed availability]: Airtable Product Catalogue label for the same capability documented below as Spending Controls — configurable limits on how issued cards can be used.
- **Developer needs** (Issuing) [Mixed availability]: Transactions API giving programmatic access to issuing transaction data across its full lifecycle, plus sandbox simulation and webhooks for real-time transaction and dispute events.
- **Disputes** (Issuing) [Mixed availability]: Issuing Disputes API supporting the full card chargeback lifecycle, from dispute creation through representment and arbitration.
- **Issuing for Platforms** (Issuing) [Roadmap]: Catalogue entry for extending Issuing capabilities to Platform (ISV) merchants. No Airtable overview text available.
- **Physical Cards** (Issuing) [Mixed availability]: Physical payment cards issued under a business's card programme.
- **Reporting** (Issuing) [Mixed availability]: Transaction and programme reporting for issuing customers.

## Mobile SDK, Flow

- **Flow Android SDK** (Mobile SDK, Flow) [General availability]: Pre-built payment UI embeddable in Android apps.
- **Flow iOS SDK** (Mobile SDK, Flow) [General availability]: Pre-built payment UI embeddable in iOS apps.
- **Flow React Native SDK** (Mobile SDK, Flow) [Don't sell]: Pre-built payment UI for React Native apps.

## Network Tokens

- **Network Tokens** (Network Tokens) [General availability]: Unique digital identifiers replacing card PANs to improve acceptance and security.

## Partner Integrations and Plugins

- **ACI** (Partner Integrations and Plugins) [Roadmap]: Partner integration with ACI Worldwide, a global real-time payments and orchestration technology provider.
- **Basis Theory** (Partner Integrations and Plugins) [General availability]: Token vault partner integration.
- **BigCommerce** (Partner Integrations and Plugins) [General availability]: Native Checkout.com plugin for BigCommerce merchants.
- **BR-DGE** (Partner Integrations and Plugins) [General availability]: Payment orchestration layer partner.
- **Cell Point Digital** (Partner Integrations and Plugins) [General availability]: Payment orchestration partner providing dynamic payment routing across acquirers and PSPs, used heavily in travel/airline.
- **Chargebee** (Partner Integrations and Plugins) [General availability]: Subscription billing platform integration.
- **Chargify** (Partner Integrations and Plugins) [Don't sell]: Subscription management platform integration.
- **CommerceTools** (Partner Integrations and Plugins) [Roadmap]: Headless commerce platform integration using Checkout.com Flow for payment processing, supporting cards, wallets, BNPL, and local payment methods.
- **Dwolla** (Partner Integrations and Plugins) [Mixed availability]: US-focused API-based payment infrastructure provider enabling bank transfers, instant payments, and account-to-account transactions.
- **GIG** (Partner Integrations and Plugins) [Roadmap]: Partner integration.
- **Gr4vy** (Partner Integrations and Plugins) [General availability]: Payment orchestration layer partner.
- **IXOPay** (Partner Integrations and Plugins) [Roadmap]: Partner integration with IXOPay, a white-label payment orchestration platform used to manage multiple payment providers.
- **Magento 2** (Partner Integrations and Plugins) [General availability]: Native Checkout.com plugin for Magento 2 merchants.
- **Ocado Group** (Partner Integrations and Plugins) [General availability]: Platform integration for grocery ecommerce, using Checkout.com Flow for card payments.
- **OpenCart** (Partner Integrations and Plugins) [Deprecated]: Native Checkout.com plugin for OpenCart.
- **Orb (WithOrb)** (Partner Integrations and Plugins) [Not on roadmap]: Catalogue entry for a partner integration with Orb (WithOrb), a billing/usage-based invoicing platform. No Airtable overview text available.
- **Payrails** (Partner Integrations and Plugins) [General availability]: Payment orchestration layer partner.
- **Prestashop** (Partner Integrations and Plugins) [Deprecated]: Native Checkout.com plugin for PrestaShop, an open-source ecommerce platform (deprecated, no longer actively supported).
- **Primer.io** (Partner Integrations and Plugins) [General availability]: Payment orchestration platform with a Checkout.com integration supporting cards, Apple Pay, Google Pay, and Cartes Bancaires.
- **Recurly** (Partner Integrations and Plugins) [General availability]: Subscription management platform integration.
- **Salesforce Commerce Cloud** (Partner Integrations and Plugins) [General availability]: Native Checkout.com plugin for Salesforce Commerce Cloud.
- **SAP Commerce Cloud** (Partner Integrations and Plugins) [General availability]: Native Checkout.com plugin for SAP Commerce Cloud.
- **SAP OPF** (Partner Integrations and Plugins) [General availability]: Native Checkout.com integration for SAP Open Payment Framework.
- **Shopify (offsite)** (Partner Integrations and Plugins) [General availability]: Offsite redirect integration for Shopify merchants.
- **Shopify (onsite)** (Partner Integrations and Plugins) [General availability]: Native onsite Checkout.com integration for Shopify.
- **Spreedly** (Partner Integrations and Plugins) [General availability]: Payment orchestration and vault partner.
- **Stripe Orchestration** (Partner Integrations and Plugins) [Roadmap]: Catalogue entry for a partner integration with Stripe as an orchestration layer routing to Checkout.com. No Airtable overview text available.
- **Travelsoft Pay** (Partner Integrations and Plugins) [Roadmap]: Travel-native payment orchestration and virtual card issuing platform for OTAs, tour operators, and bedbanks.
- **Visualsoft** (Partner Integrations and Plugins) [Mixed availability]: Native Checkout.com payment integration for Visualsoft, an ecommerce platform for retailers.
- **WooCommerce** (Partner Integrations and Plugins) [General availability]: Native Checkout.com plugin for WooCommerce merchants.
- **YUNO** (Partner Integrations and Plugins) [Roadmap]: Partner integration with Yuno, a Latin America-focused payment orchestration platform.
- **Zingfit** (Partner Integrations and Plugins) [Mixed availability]: Native integration for Zingfit, a fitness and wellness studio booking and management platform, enabling in-platform payments.
- **Zuora** (Partner Integrations and Plugins) [General availability]: Subscription and recurring billing platform integration.

## Payment Methods

- **Aani** (Payment Methods) [Roadmap]: UAE's central instant‑payments system accessible via mobile app.
- **Accel** (Payment Methods) [General availability]: US regional debit network, part of PINless debit processing.
- **ACH Direct Debit** (Payment Methods) [General availability]: Electronic funds transfer enabling US customers to move money between bank accounts.
- **Affirm** (Payment Methods) [Not on roadmap]: US and Canada BNPL service offering interest‑free or low‑interest installments.
- **Afterpay** (Payment Methods) [Not on roadmap]: Global BNPL platform with four equal, interest‑free payments every two weeks.
- **AlipayCN** (Payment Methods) [Mixed availability]: Mobile payment service for Chinese consumers enabling one-time and recurring purchases.
- **AlipayHK** (Payment Methods) [Mixed availability]: Mobile payment service for Hong Kong consumers enabling one-time and recurring purchases.
- **Alma** (Payment Methods) [General availability]: Buy-now-pay-later solution enabling customers to pay 15 or 30 days after purchase.
- **Amazon Pay** (Payment Methods) [Not on roadmap]: Trusted digital wallet using customers' Amazon credentials for checkout.
- **American Express - Collecting** (Payment Methods) [Mixed availability]: Checkout.com acquires and settles Amex transactions directly.
- **American Express - Gateway** (Payment Methods) [Mixed availability]: Gateway model where Amex settles directly with the merchant.
- **Apple Pay** (Payment Methods) [General availability]: Enables customers to authenticate card payments using Touch ID or Face ID without manually entering card details.
- **Atome** (Payment Methods) [Not on roadmap]: Interest‑free installment payment solution active across Southeast Asia.
- **auPay** (Payment Methods) [Not on roadmap]: Japanese QR‑based wallet and loyalty app by KDDI with 38 million users.
- **Autogiro** (Payment Methods) [Not on roadmap]: Swedish recurring bank direct debit scheme.
- **Avtalegiro** (Payment Methods) [Not on roadmap]: Norwegian recurring bank direct debit scheme.
- **Bacs** (Payment Methods) [Roadmap]: UK bank debit scheme for recurring and one-off payments.
- **Bancomat** (Payment Methods) [Not on roadmap]: Italy's national debit card network, connecting all major banks.
- **Bancomat Pay** (Payment Methods) [Not on roadmap]: Mobile wallet from Italy's Bancomat network for fast, cashless payments.
- **Bancontact** (Payment Methods) [General availability]: Enables secure online card payments in Belgium.
- **BankAxept** (Payment Methods) [Not on roadmap]: Norway's national debit card scheme with broad coverage.
- **BECS Direct Debit** (Payment Methods) [Not on roadmap]: Australia's automated bank debit system for recurring payments.
- **Benefit Payment Gateway** (Payment Methods) [General availability]: Enables secure online payments in Bahrain via the national payment gateway.
- **BenefitPay** (Payment Methods) [Deprecated]: App-based payment allowing Bahraini users to pay and transfer funds via smartphone.
- **Betailingsservice** (Payment Methods) [Not on roadmap]: Danish recurring bank direct debit scheme (Betalingsservice).
- **Bizum** (Payment Methods) [Beta]: Instant bank transfer payment using a phone number, popular in Spain.
- **BLIK** (Payment Methods) [Beta]: Real-time mobile payment method in Poland using a 6-digit code.
- **Boleto Bancario** (Payment Methods) [Deprecated]: Cash voucher payment method in Brazil.
- **Boost** (Payment Methods) [Not on roadmap]: Malaysia's all-in-one QR wallet with rewards and bill pay.
- **Bre-B** (Payment Methods) [Not on roadmap]: Real-time payment system enabling instant bank transfers in Brazil.
- **Capitecpay** (Payment Methods) [Not on roadmap]: Bank-linked online payment solution for South African merchants.
- **Cartes Bancaires** (Payment Methods) [General availability]: France's predominant card scheme, typically co-branded with Visa or Mastercard.
- **Cash App** (Payment Methods) [Roadmap]: US digital wallet and P2P app for instant bank-linked payments.
- **Clearpay** (Payment Methods) [Not on roadmap]: Afterpay's UK BNPL service for interest-free installment payments.
- **DANA** (Payment Methods) [Mixed availability]: Mobile payment service for Indonesian consumers enabling one-time and recurring purchases.
- **Dankort** (Payment Methods) [Not on roadmap]: Denmark's domestic debit network with Visa co-branding.
- **Daviplata** (Payment Methods) [Not on roadmap]: Mobile wallet by Davivienda enabling instant local payments in Colombia.
- **dBarai** (Payment Methods) [Not on roadmap]: NTT Docomo's mobile wallet for QR and barcode-based payments.
- **DBS PayLah!** (Payment Methods) [Not on roadmap]: Digital wallet by DBS enabling instant PayNow-linked transfers.
- **Diners Club International** (Payment Methods) [General availability]: Global credit card scheme accepted alongside Mastercard.
- **Discover** (Payment Methods) [General availability]: Global credit card scheme, especially strong in US.
- **DragonPay** (Payment Methods) [Not on roadmap]: Alternative payments network for bank, wallet, and cash transfers.
- **DuitNow** (Payment Methods) [Not on roadmap]: Malaysia's instant bank transfer system connecting all major banks.
- **eFaktura** (Payment Methods) [Not on roadmap]: Norwegian e-invoice payment method delivered via online banking.
- **EFT Pre-Authorized Debit** (Payment Methods) [Not on roadmap]: Recurring bank debit solution regulated by Payments Canada.
- **EFTPOS** (Payment Methods) [Roadmap]: Australian domestic debit card scheme.
- **Elo** (Payment Methods) [Not on roadmap]: Brazil's major domestic card brand for all payment types.
- **eps** (Payment Methods) [General availability]: Enables online purchases through secure bank transfers in Austria.
- **eps (Hong Kong)** (Payment Methods) [Not on roadmap]: Hong Kong's domestic debit network for real-time payments.
- **Fawry** (Payment Methods) [Don't sell]: Egyptian cash payment and digital payments network.
- **FPS** (Payment Methods) [Not on roadmap]: Hong Kong's regulated instant payments network for all banks and wallets.
- **FPX** (Payment Methods) [Not on roadmap]: Malaysia's national online bank transfer system by PayNet.
- **GCash** (Payment Methods) [Mixed availability]: Mobile payment service for Filipino consumers enabling one-time and recurring purchases.
- **Girocard** (Payment Methods) [Not on roadmap]: Germany's local debit network enabling secure real-time payments.
- **GiroPay** (Payment Methods) [Not on roadmap]: No longer exists as a brand.
- **Google Pay** (Payment Methods) [General availability]: Enables one-touch payments on website or Android app using cards connected to a Google account.
- **GoPay** (Payment Methods) [Not on roadmap]: Gojek's digital wallet powering instant payments across Indonesia.
- **GrabPay** (Payment Methods) [Not on roadmap]: Grab's regional wallet supporting digital commerce and daily payments.
- **iDEAL** (Payment Methods) [General availability]: Direct online bank transfer from customer's bank account to merchant's bank account.
- **Illicado** (Payment Methods) [Not on roadmap]: France's most popular gift card for flexible online spending.
- **Interac** (Payment Methods) [Roadmap]: Canada's local debit and e-transfer network for secure payments.
- **Jaywan** (Payment Methods) [Roadmap]: Emerging GCC domestic debit card scheme.
- **JCB** (Payment Methods) [Mixed availability]: Japanese card scheme accepted globally, especially in Asia.
- **KakaoPay** (Payment Methods) [Mixed availability]: Mobile payment service for Korean consumers enabling one-time and recurring purchases.
- **Klarna (Gateway)** (Payment Methods) [Don't sell]: Gateway model for Klarna — not actively sold.
- **Klarna BNPL (Collecting)** (Payment Methods) [Mixed availability]: Flexible payment options: pay now, pay later, or pay in instalments.
- **Klarna Crypto** (Payment Methods) [Beta]: Klarna's crypto payment option.
- **Klarna Debit Risk (Collecting)** (Payment Methods) [Beta]: Klarna's bank transfer option for restricted/high-risk merchant segments.
- **Knet** (Payment Methods) [General availability]: Enables purchases with local Kuwaiti debit cards issued by member banks.
- **Konbini Payments** (Payment Methods) [Not on roadmap]: Cash payment option via convenience stores for Japanese consumers.
- **LINE Pay** (Payment Methods) [Not on roadmap]: LINE Pay is a payment method available in Japan that allows users to make purchases using the LINE Pay mobile app.
- **LiqPay** (Payment Methods) [Not on roadmap]: Ukraine's top payment gateway for card, bank, and wallet transfers.
- **LPay** (Payment Methods) [Not on roadmap]: Lpay is an E-wallet service in South Korea that allows users to store and manage their money digitally.
- **MACH** (Payment Methods) [Not on roadmap]: Chile's fast-growing digital wallet for cardless transactions.
- **Mada** (Payment Methods) [General availability]: Saudi Arabia's domestic payment network, co-branded internationally with Visa/Mastercard.
- **Maestro** (Payment Methods) [Beta]: Mastercard's international debit card scheme (Pilot status).
- **Mastercard** (Payment Methods) [Mixed availability]: Leading global card scheme for credit and debit payments.
- **maximum** (Payment Methods) [Not on roadmap]: Turkey's top card and wallet brand offering loyalty and flexibility.
- **MB WAY** (Payment Methods) [General availability]: Portugal's most popular digital wallet, enabling fast PIN-authenticated payments online.
- **Mercado Pago** (Payment Methods) [Not on roadmap]: Digital wallet and payments platform used across Latin America.
- **MobilePay** (Payment Methods) [Beta]: Leading Nordic mobile wallet for instant payments via smartphone.
- **MoMo** (Payment Methods) [Not on roadmap]: MoMo is an e-wallet in Vietnam with 5 million users and with more than 70% of the market share.
- **MonoPay** (Payment Methods) [Not on roadmap]: Ukrainian digital wallet offering instant bank-linked payments.
- **Multibanco** (Payment Methods) [General availability]: Enables cash or debit payments at ATMs or via banking app across Portugal.
- **MyDebit** (Payment Methods) [Not on roadmap]: Malaysia's domestic debit card network for secure payments.
- **NaverPay** (Payment Methods) [Not on roadmap]: South Korea's wallet for one-click payments within the Naver ecosystem.
- **Nequi** (Payment Methods) [Not on roadmap]: Digital wallet by Bancolombia supporting instant payments.
- **Nordea** (Payment Methods) [Not on roadmap]: Online banking payments through Nordea's secure platform.
- **NYCE** (Payment Methods) [General availability]: US regional debit network, part of PINless debit processing.
- **Octopus** (Payment Methods) [Beta]: Contactless card and digital wallet payments in Hong Kong.
- **Omannet** (Payment Methods) [General availability]: Domestic payment network in Oman for online debit card payments.
- **Oney** (Payment Methods) [Not on roadmap]: European BNPL and consumer credit provider.
- **Open Banking** (Payment Methods) [Roadmap]: Pay-by-bank method letting customers pay merchants directly from their bank account over local account-to-account rails, authorised in their banking app via SCA.
- **papara** (Payment Methods) [Not on roadmap]: Leading Turkish wallet enabling low-cost instant transactions.
- **paycell** (Payment Methods) [Not on roadmap]: Turkcell's wallet enabling fast and flexible payments in Turkey.
- **Payco** (Payment Methods) [Not on roadmap]: Payco is a highly popular payment method in South Korea
- **Payconiq** (Payment Methods) [Not on roadmap]: Mobile bank payment network for instant QR-based transactions.
- **PayID** (Payment Methods) [Not on roadmap]: PayID lets Australians send and receive instant bank transfers using easy identifiers like email or phone—no BSB or account number needed.
- **PayMe** (Payment Methods) [Not on roadmap]: HSBC's social wallet for fast, secure payments in Hong Kong.
- **PayNow** (Payment Methods) [Beta]: Real-time payment service in Singapore enabling fund transfers via mobile number.
- **PayPal** (Payment Methods) [General availability]: Enables payments using credit/debit cards connected to a PayPal account, with Pay Now, Continue, and Pay Later options.
- **PayPay** (Payment Methods) [Roadmap]: Leading mobile wallet in Japan with 68M+ users, using QR-based payments with wide online reach.
- **PayPo** (Payment Methods) [Not on roadmap]: Widely used across top Polish online stores.
- **PaysafeCard** (Payment Methods) [Roadmap]: Widely used in gaming, streaming, and online services.
- **Paytm** (Payment Methods) [Not on roadmap]: Part of India's largest fintech platform for banking and lending.
- **PayTO** (Payment Methods) [Not on roadmap]: PayTo enables recurring direct-debit authorisations on the NPP, giving merchants flexible, real-time pull payments with customer consent.
- **Paze** (Payment Methods) [Not on roadmap]: US bank-backed digital wallet consortium (Visa/Mastercard network banks) for online checkout.
- **Pix** (Payment Methods) [Roadmap]: Brazil's instant payment system operated by the central bank.
- **PLIN** (Payment Methods) [Not on roadmap]: Peru's instant bank transfer network using mobile identifiers.
- **POLi** (Payment Methods) [Not on roadmap]: POLi enables instant, secure bank-to-bank payments in Australia and New Zealand via customers' online-banking portals—no cards required.
- **PostFinance** (Payment Methods) [Not on roadmap]: PostFinance offers Swiss merchants an integrated payment gateway supporting cards, e-banking, invoices, and local methods under one platform.
- **Privat24** (Payment Methods) [Not on roadmap]: Online banking platform enabling instant payments via PrivatBank.
- **PromptPay** (Payment Methods) [Not on roadmap]: Thailand's national instant payments network using mobile IDs or QR.
- **Przelewy24** (Payment Methods) [General availability]: Enables secure online payments in Poland via redirect.
- **PSE** (Payment Methods) [Not on roadmap]: Colombia's trusted online bank transfer network by ACH Colombia.
- **Pulse** (Payment Methods) [General availability]: US regional debit network, part of PINless debit processing.
- **QPay** (Payment Methods) [General availability]: Enables secure online payments in Qatar via bank transfer gateway.
- **Rabbit LINE PAY** (Payment Methods) [Not on roadmap]: LINE-integrated wallet offering QR and online payments in Thailand.
- **Rakuten Pay** (Payment Methods) [Not on roadmap]: Rakuten's wallet for online, in-app, and in-store QR payments.
- **Ratepay** (Payment Methods) [Not on roadmap]: BNPL solution for invoice and installments across DACH markets.
- **Red Compra** (Payment Methods) [Not on roadmap]: Chile's domestic debit card scheme for in-store and online payments.
- **Riverty** (Payment Methods) [Not on roadmap]: European BNPL provider driving sales with flexible pay-later options.
- **Samsung Pay** (Payment Methods) [Roadmap]: Samsung's mobile payment wallet.
- **Satispay** (Payment Methods) [Not on roadmap]: Italian mobile wallet for QR and bank-linked payments.
- **SEPA Direct Debit B2B** (Payment Methods) [Beta]: SEPA direct debit variant for business-to-business transactions.
- **SEPA Direct Debit Core** (Payment Methods) [General availability]: Standard SEPA direct debit for consumer bank accounts across the EU.
- **SeQura** (Payment Methods) [Beta]: Instalment payment plans popular in Spain.
- **ShopeePay** (Payment Methods) [Not on roadmap]: ShopeePay is Shopee's official in-app e-wallet regulated by the Bangko Sentral ng Philipinas, which allows shoppers to conveniently top-up and pay for online and offline purchases.
- **Sofort** (Payment Methods) [Deprecated]: Sofort online banking payment (deprecated).
- **SPEI** (Payment Methods) [Not on roadmap]: Mexico's central bank-operated real-time payment network.
- **Splitit** (Payment Methods) [Not on roadmap]: Splitit lets customers use existing credit cards to split payments into interest-free installments, preserving credit lines and minimizing fraud.
- **SSGPAY** (Payment Methods) [Not on roadmap]: Online payment gateway letting merchants accept cards, e-wallets, bank transfers, and SSG MONEY virtual currency.
- **Stablecoin Acceptance (via Coinbase)** (Payment Methods) [Roadmap]: Lets consumers check out using USDC stablecoin, which Coinbase converts to fiat at a 1:1 rate before Checkout.com settles it to the merchant as standard fiat currency.
- **STAR** (Payment Methods) [General availability]: US regional debit network, part of PINless debit processing.
- **STC Pay** (Payment Methods) [General availability]: Digital wallet enabling fund transfers and ecommerce payments in Saudi Arabia.
- **Sunbit** (Payment Methods) [Not on roadmap]: US point-of-sale financing / BNPL provider.
- **Swish** (Payment Methods) [Beta]: Popular Swedish mobile payment app for instant online purchases via banking app.
- **Tabby (Collecting)** (Payment Methods) [Beta]: Splits payments into four instalments, popular in MENA.
- **Tabby (Gateway)** (Payment Methods) [Beta]: Gateway model for Tabby BNPL in MENA.
- **Tamara (Collecting)** (Payment Methods) [Beta]: Split or deferred payment options for UAE and Saudi consumers.
- **Tamara (Gateway)** (Payment Methods) [Beta]: Gateway model for Tamara in UAE and Saudi Arabia.
- **Toss Pay** (Payment Methods) [Not on roadmap]: South Korean digital wallet for fast online and QR payments.
- **Touch 'n Go** (Payment Methods) [Mixed availability]: Mobile payment service for Malaysian consumers with recurring payment support.
- **troy** (Payment Methods) [Not on roadmap]: Turkey's national card scheme offering debit, credit, and prepaid support.
- **TrueMoney** (Payment Methods) [Mixed availability]: Mobile payment service for Thai consumers enabling one-time and recurring purchases.
- **Trustly** (Payment Methods) [Not on roadmap]: Trustly uses open-banking to offer account-to-account payments across Europe, with instant payouts, no cards, and minimal fees.
- **Twint** (Payment Methods) [Beta]: Swiss mobile payment wallet (pass-through or prepaid card).
- **UnionPay** (Payment Methods) [Beta]: China's dominant card scheme, accepted globally.
- **UPI** (Payment Methods) [Not on roadmap]: India's instant bank transfer network powered by NPCI.
- **Venmo** (Payment Methods) [General availability]: Social payment service for US customers to pay businesses and friends.
- **ViaBill** (Payment Methods) [Not on roadmap]: BNPL platform offering interest-free monthly installments.
- **Vipps** (Payment Methods) [Beta]: Leading Nordic mobile wallet for instant smartphone payments.
- **Visa** (Payment Methods) [Mixed availability]: World's largest card network for credit and debit payments.
- **WeChat Pay CN** (Payment Methods) [Mixed availability]: WeChat Pay for mainland Chinese consumers.
- **WeChat Pay HK** (Payment Methods) [Mixed availability]: WeChat Pay for Hong Kong consumers.
- **Wero** (Payment Methods) [Roadmap]: European mobile payment wallet (pan-European initiative).
- **Yape** (Payment Methods) [Not on roadmap]: Peru's leading mobile wallet for instant QR and P2P payments.
- **ZaloPay** (Payment Methods) [Not on roadmap]: ZaloPay is a Vietnamese mobile wallet and payment platform associated with the Zalo messaging app.
- **Zelle** (Payment Methods) [Not on roadmap]: US real-time bank transfer network integrated with major banks.
- **Zip** (Payment Methods) [Roadmap]: Leading BNPL provider in ANZ and North America, offering flexible instalments for shoppers with full payout to the merchant.

## Payment Setup

- **Payment Setup API** (Payment Setup) [Beta]: Checkout.com's latest Payments API, maintaining a single payment session with a persistent Payment Setup ID across multiple payment attempts throughout checkout.

## Payments Links

- **Payment Links** (Payments Links) [General availability]: Unique URL redirecting customers to a Hosted Payments Page to complete payment.

## Payouts

- **Third Party Payouts** (Payouts) [Mixed availability]: Current catalogue product for payout of funds to third-party beneficiaries rather than the primary merchant account, covering both payout rails — bank and card.

## Payouts, Business Account

- **Pay to Self** (Payouts, Business Account) [Mixed availability]: Settlement of Checkout.com-acquired funds into the merchant's own account.

## Real-Time Account Updater

- **Real-Time Account Updater** (Real-Time Account Updater) [Mixed availability]: Service that automatically updates stored card details when they change.

## Reporting

- **Financial Report** (Reporting) [blank/unset]: Reporting suite providing a single source of truth for treasury and finance teams to reconcile balances, payouts, fees, and taxes across currencies.
- **Issuing Report** (Reporting) [blank/unset]: Reporting suite giving issuers end-to-end visibility into card programme activity, from authorization to settlement, including disputes.
- **Payment Operations Report** (Reporting) [blank/unset]: Non-financial reporting suite covering customer behaviour, fraud trends, and authentication success to support risk and support teams.
- **Predictive Interchange** (Reporting) [Mixed availability]: Forecasting tool for interchange cost optimisation.

## Treasury & FX

- **Acquiring - Custom FX markup per currency pair** (Treasury & FX) [General availability]: Custom FX markup configuration per currency pair.
- **Acquiring - Daily FX Rates** (Treasury & FX) [General availability]: Daily FX rate service for acquiring transactions.
- **Acquiring - FX Live Market Rates** (Treasury & FX) [General availability]: Live market FX rate service for acquiring.
- **Acquiring - Scheme FX Rates** (Treasury & FX) [General availability]: Scheme-level FX rate service (Visa/Mastercard).
- **Internal - Cash ladder reporting** (Treasury & FX) [blank/unset]: Internal treasury reporting tool tracking Checkout.com's own cash ladder/liquidity positions. Not a merchant-facing product. No Airtable overview text available.
- **Internal - FX Blotter reporting** (Treasury & FX) [General availability]: Internal treasury reporting tool tracking Checkout.com's own FX exposure and blotter positions across currencies. Not a merchant-facing product.
- **PTB - FX based on Live Market Rates** (Treasury & FX) [Not on roadmap]: Catalogue entry for payment-time currency conversion at live market rates (payout-side equivalent of Acquiring - FX Live Market Rates). No Airtable overview text available.
- **PTC - FX based on Scheme FX rates (VISA/MC only)** (Treasury & FX) [General availability]: Payment-time currency conversion using scheme FX rates (Visa/MC only).

## Unified Payments API

- **Unified Payments API (UPAPI)** (Unified Payments API) [General availability]: Modern RESTful API for enterprise merchants unifying payment backends, replacing legacy API bundles.

## Vault

- **Forward API** (Vault) [Beta]: Beta feature enabling merchants to enrich payment requests with CKO-stored credentials and forward them to third-party API endpoints.
- **Integrated Vault** (Vault) [General availability]: Credential storage embedded within Checkout.com's payment processing.
- **Standalone Vault** (Vault) [Beta]: Independent credential storage for merchants who need vault services without full CKO payment processing.
