# Checkout.com Product Definitions

Source of truth: Airtable Product Catalogue (synced May 2026)
Definitions enriched from: checkout.com/docs (scraped March 2026)

**Planned use**: Map against support contact data to identify which products drive contact volumes.

> Payment and fintech terms used in this document follow definitions in [`checkout-terminology.md`](../payment-domain/checkout-terminology.md).

---

## How to read this file

Each `##` heading is a product category from the Airtable Product Catalogue. Each `###` heading beneath it is one product, structured to mirror the Applies-if / Does-not-apply-if / Example / Likely-keywords format used for Fin Attribute definitions in [`fin-attributes-definitions.md`](../processes/fin-attributes-definitions.md), adapted here for product identification:

| Field | Meaning |
| --- | --- |
| What it is | One-sentence definition from docs |
| Geography / Payment type | Countries/regions and payment type (Payment Methods only) |
| Key capabilities / Integration notes | Key merchant setup or complexity signals |
| Contact risk | Pre-populated where inferable from product type; to be validated against contact data |
| Applies if the merchant | Signals Fin should use to classify an inbound contact under this product |
| Does not apply if the merchant | Signals pointing to a different, easily-confused sibling product instead — named explicitly |
| Example | A realistic merchant quote that should trigger this classification |
| Likely keywords | Terms and phrases associated with this product |

Contact risk tags: `high` / `medium` / `low` / `unknown`
Risk reasons: dispute-prone · mandate-management · setup-complexity · redirect-failure · auth-friction · account-management

---

## Authentication

### Authentication
**What it is:** Security protocol requiring customers to complete an additional authentication step for online card payments.
**Key capabilities:** Frictionless and challenge flows; liability shift to issuer on success; SCA compliance for Europe; supports Visa Secure, MC Identity Check, Amex SafeKey.
**Contact risk:** high — 3DS friction causes abandonment; false declines; SCA exemption queries

**Applies if the merchant:**
- Reports 3DS, 3D Secure, or SCA authentication behaviour (challenge, frictionless outcome, false decline, liability shift, or SCA exemption) on a standard card payment authorization flow.

**Does not apply if the merchant:**
- Explicitly describes combining multiple auth methods (e.g. 3DS plus Passkeys or Google SPA) or configuring which method runs — that is Bundled Authentication. If they describe running authentication as its own separate API call decoupled from the payment request, that is Standalone Authentication.

**Example:** "Customers are getting a 3DS challenge screen and abandoning checkout — can we apply an SCA exemption?"

**Likely keywords:** 3DS, 3D Secure, SCA, authentication failure, liability shift, frictionless flow, challenge flow, Visa Secure, MC Identity Check, Amex SafeKey, false decline, SCA exemption

---

### Bundled Authentication
**What it is:** Configurable authentication platform combining 3DS, Google SPA, and Passkeys for regulatory compliance, fraud reduction, and conversion optimisation.
**Key capabilities:** Supports 3DS, Google SPA, and Passkeys; configurable per merchant; single integration for multiple auth methods.
**Contact risk:** medium — same friction as Authentication; queries on passkey setup, Google SPA config, multi-method behaviour

**Applies if the merchant:**
- Asks about setting up or configuring Passkeys or Google SPA alongside 3DS, or managing multiple authentication methods through one integration.

**Does not apply if the merchant:**
- Is only asking about a plain 3DS challenge/frictionless outcome with no mention of Passkeys or Google SPA — that is Authentication. If they describe authentication running as a decoupled, separate API call from payment, that is Standalone Authentication.

**Example:** "We want to enable Passkeys alongside our existing 3DS setup — how do we configure that in one integration?"

**Likely keywords:** Bundled Authentication, passkeys, Google SPA, multi-method authentication, combined auth methods, configuring 3DS plus passkeys, single integration authentication

---

### Standalone Authentication
**What it is:** Authentication (e.g. 3DS) performed as a separate API call, decoupled from the payment authorization request.
**Key capabilities:** Decouples authentication from payment; supports merchants managing their own routing or a separate gateway.
**Contact risk:** medium — same friction as Authentication; queries on decoupled auth flow and linking the authentication result to payment

**Applies if the merchant:**
- Describes calling authentication as its own API request, separate from the payment authorization call, often because they route payment through a different gateway or handle authorization themselves.

**Does not apply if the merchant:**
- Is running authentication as part of the standard combined payment authorization flow (no separate call) — that is Authentication. If they are combining multiple auth methods (Passkeys, Google SPA) rather than decoupling the call, that is Bundled Authentication.

**Example:** "We call 3DS as a separate authentication request and then send the result to our own gateway for authorization — how do we link the two?"

**Likely keywords:** Standalone Authentication, decoupled authentication, separate authentication call, authentication API independent of payment, linking authentication result to authorization

---

## Business Account

### Balances
**What it is:** Real-time view of funds held in Checkout Business Account sub-accounts across currencies.
**Key capabilities:** Multi-currency balance visibility; cash flow monitoring.
**Contact risk:** medium — balance discrepancy queries, currency queries

**Applies if the merchant:**
- Asks about the current or available balance shown for a Checkout Business Account sub-account, in any currency, or reports a balance figure that looks wrong.

**Does not apply if the merchant:**
- Is asking why funds haven't arrived from Checkout.com into their external bank account (that's Settlements) or why an on-platform transfer between sub-accounts hasn't landed (that's Transfers). Balances is about the standing figure, not fund movement.

**Example:** "My EUR sub-account balance dropped overnight and I can't see why."

**Likely keywords:** balance, available funds, multi-currency balance, balance discrepancy, sub-account balance, Checkout Business Account balance, cash flow view

---

### Corporate Cards
**What it is:** Business cards for operational spending, linked to the Checkout Business Account.
**Contact risk:** unknown — Pilot

**Applies if the merchant:**
- References a Corporate Card issued for business expenses, linked to their Checkout Business Account, including card issuance, activation, or spend queries.

**Does not apply if the merchant:**
- Is asking about card payments they accept from customers (that's a payment method / card acceptance query, not Corporate Cards) or about the Business Account balance itself rather than a linked spending card.

**Example:** "How do I activate the Corporate Card linked to our Business Account?"

**Likely keywords:** Corporate Cards, business expense card, Checkout-linked spending card, pilot card programme, employee card

---

### Settlements
**What it is:** Process by which Checkout.com transfers collected payment funds to the merchant's account.
**Key capabilities:** Configurable settlement frequency; automatic crediting to sub-accounts.
**Contact risk:** high — settlement timing and amount queries are a major support driver

**Applies if the merchant:**
- Asks about when or how much money will be paid out from Checkout.com to their external bank account, settlement frequency, a settlement delay, or a mismatch between expected and received settlement amount.

**Does not apply if the merchant:**
- Is asking about moving funds between their own Checkout.com sub-accounts (that's Transfers) or about getting paid faster than the standard settlement schedule (that's Fund Acceleration). Settlements is the standard scheme-to-merchant-bank disbursement.

**Example:** "Our settlement was due yesterday and hasn't landed in our bank account — what's the delay?"

**Likely keywords:** settlement, payout timing, settlement delay, settlement amount, settlement report, funds transfer to merchant bank account, settlement frequency

---

### Transfers
**What it is:** Ability to move funds into sub-accounts on demand.
**Key capabilities:** Flexible fund movement between accounts; supports payout funding.
**Contact risk:** medium — transfer failure queries

**Applies if the merchant:**
- Reports an on-demand fund movement between their own Checkout.com sub-accounts failing, delaying, or behaving unexpectedly.

**Does not apply if the merchant:**
- Is asking about funds coming in from Checkout.com to their external bank account (that's Settlements) or about converting currency during that on-platform movement (that's Same and Cross-currency Transfers, if currency conversion is explicitly mentioned).

**Example:** "I tried to move funds from my main sub-account to my payout sub-account and the transfer failed."

**Likely keywords:** fund transfer, sub-account funding, on-demand fund movement, transfer failure, moving funds between accounts, payout funding

---

### Fund Acceleration
**What it is:** Service that settles merchant funds faster than scheme collection timelines (e.g. T+1 to merchant vs T+3 from schemes).
**Key capabilities:** Accelerated disbursement; reduces merchant cash flow lag vs standard settlement.
**Contact risk:** medium — settlement timing discrepancy queries

**Applies if the merchant:**
- Explicitly asks about receiving funds faster than the standard settlement timeline, references T+1 payout, or asks to enable/troubleshoot accelerated disbursement.

**Does not apply if the merchant:**
- Is simply asking why a standard settlement is late or how standard settlement frequency works with no mention of an accelerated or early-payout arrangement — that is Settlements.

**Example:** "We're on Fund Acceleration and expected T+1 payout, but funds came in on T+3 like standard settlement."

**Likely keywords:** fund acceleration, early settlement, T+1 payout, accelerated disbursement, faster settlement, cash flow lag

---

### Same and Cross-currency Transfers
**What it is:** On-demand fund transfers between Checkout.com accounts in the same or different currencies.
**Key capabilities:** Flexible on-platform fund movement; supports cross-currency conversion between sub-accounts.
**Contact risk:** medium — FX conversion queries, transfer failures

**Applies if the merchant:**
- Explicitly mentions converting currency as part of moving funds between their own Checkout.com sub-accounts, or asks about the FX rate applied to an on-platform transfer.

**Does not apply if the merchant:**
- Is moving funds between sub-accounts in the same currency with no conversion involved (that's the general Transfers product) or asking about incoming settlement FX from schemes (that's Settlements).

**Example:** "I transferred funds from my USD sub-account to my EUR sub-account and the conversion rate looks off."

**Likely keywords:** same-currency transfer, cross-currency transfer, on-platform FX transfer, currency conversion between sub-accounts, cross-currency fund movement

---

## Dashboard

### Dashboard
**What it is:** Checkout.com's merchant-facing web portal for managing payments, settings, and reporting.
**Contact risk:** high — access, permissions, and navigation queries are a major support category

**Applies if the merchant:**
- Reports a login failure, access error, permissions issue, user management problem, or general navigation confusion within the Checkout.com Dashboard web portal.

**Does not apply if the merchant:**
- Is reporting an issue with the underlying data shown in the Dashboard (e.g. a wrong balance or settlement amount) — classify those under the specific product (Balances, Settlements) rather than Dashboard, unless the complaint is specifically about accessing or navigating the portal itself.

**Example:** "I can't log into the Dashboard and I'm getting a permissions error."

**Likely keywords:** Dashboard login, Dashboard access, Dashboard error, permission issues, user management in Dashboard, merchant portal navigation

---

## Disputes

### Disputes
**What it is:** Chargeback management system for responding when customers challenge transaction validity.
**Key capabilities:** Real-time monitoring; evidence submission; dispute acceptance or challenge; scheme programme monitoring; reporting.
**Contact risk:** high — core operational product; high contact volume expected

**Applies if the merchant:**
- References a formal chargeback or dispute that has already been raised by the scheme, including evidence submission, dispute status, accept/challenge decisions, or scheme dispute programme monitoring.

**Does not apply if the merchant:**
- Is asking about resolving a customer concern before a formal chargeback has been filed — that is Pre-Disputes. Once the scheme has formally raised the dispute, it belongs under Disputes.

**Example:** "We received a chargeback notification and need to submit evidence before the deadline."

**Likely keywords:** disputes, chargebacks, dispute evidence submission, dispute status, scheme dispute programmes, chargeback response, dispute reporting

---

### Pre-Disputes
**What it is:** Early dispute resolution mechanism to resolve customer concerns before they escalate to chargebacks.
**Key capabilities:** Intervenes in the pre-chargeback window to avoid formal dispute.
**Contact risk:** high — closely related to Disputes volume

**Applies if the merchant:**
- Asks about resolving a customer complaint or concern before a formal chargeback has been raised, or references a pre-dispute or pre-chargeback alert/window.

**Does not apply if the merchant:**
- Is dealing with a chargeback that has already been formally raised by the scheme and requires evidence submission or a challenge decision — that is Disputes, not Pre-Disputes.

**Example:** "We got a pre-dispute alert on a transaction — can we resolve it with the customer before it turns into a chargeback?"

**Likely keywords:** pre-dispute, pre-chargeback, dispute prevention, early dispute resolution, pre-dispute alert, avoiding formal chargeback

## Flow

### Flow Web
**What it is:** Pre-built, customizable payment interface for embedding in websites.
**Key capabilities:** Handles tokenisation, 3DS auth, payment method display, input validation; Remember Me support; responsive design.
**Contact risk:** medium — integration setup queries, 3DS friction

**Applies if the merchant:**
- References Flow, Flow drop-in, embedded payment component, or web checkout integration issues
- Reports 3DS authentication friction or errors surfacing within the embedded checkout widget on their website
- Asks about Remember Me behaviour specifically within the Flow Web widget

**Does not apply if the merchant:**
- Is building a native mobile app and needs the payment UI embedded there instead — use Flow Android SDK, Flow iOS SDK, or Flow React Native SDK depending on platform
- Wants Checkout.com to host the entire payment page and handle the redirect rather than embedding a component on their own site — use Hosted Payment Page
- Is asking about saved-card behaviour across multiple unrelated merchants rather than within their own Flow integration — use Remember Me

**Example:** "Our Flow Web checkout is throwing a 3DS error on card entry, can you help debug the integration?"

**Likely keywords:** Flow, Flow drop-in, embedded payment component, web checkout integration, 3DS, 3D Secure, authentication friction, Remember Me, tokenisation, payment widget, checkout embed

---

### Remember Me
**What it is:** Feature allowing customers to save payment details across all Remember Me-enabled merchants.
**Key capabilities:** Cross-merchant credential access; tokenised storage in Vault.
**Contact risk:** medium — privacy queries, unexpected card charges

**Applies if the merchant:**
- References Remember Me, a saved card that appears across multiple merchants, an unexpected card charge at checkout, or cross-merchant credential access
- Raises a privacy or data-sharing concern about how their customer's card details are visible or usable on another merchant's site

**Does not apply if the merchant:**
- Is only asking about saved-card behaviour within their own single Flow Web integration, with no cross-merchant element — use Flow Web
- Is asking about card tokenisation or storage mechanics generally rather than the cross-merchant Remember Me experience — treat as a Vault query, not Remember Me

**Example:** "A customer says they were charged on our site using a card they saved with a different merchant, is that Remember Me?"

**Likely keywords:** Remember Me, saved card, cross-merchant, unexpected charge, unrecognised charge, shared credentials, tokenised card, Vault, checkout autofill

---

## Flow / Mobile SDK

### Flow Android SDK
**What it is:** Pre-built payment UI embeddable in Android apps.
**Key capabilities:** Built-in 3DS, Apple/Google Pay, customizable UI; min SDK 21.
**Contact risk:** medium — SDK integration queries

**Applies if the merchant:**
- References Flow for Android, Android SDK, or mobile payment UI on Android
- Reports issues with Google Pay or Apple Pay rendering inside their Android app checkout
- Asks about minimum SDK version 21 compatibility or build errors in an Android project

**Does not apply if the merchant:**
- Is integrating on iOS rather than Android — use Flow iOS SDK
- Is building with React Native rather than native Android — use Flow React Native SDK
- Wants the payment UI on their website rather than in a native mobile app — use Flow Web

**Example:** "We're getting a build error integrating the Flow Android SDK, is this a minimum SDK version issue?"

**Likely keywords:** Flow Android, Android SDK, mobile payment UI, Google Pay, Apple Pay Android, min SDK 21, native Android integration

---

### Flow iOS SDK
**What it is:** Pre-built payment UI embeddable in iOS apps.
**Key capabilities:** Built-in 3DS, Apple/Google Pay, customizable UI; min iOS 15.
**Contact risk:** medium — SDK integration queries

**Applies if the merchant:**
- References Flow for iOS, iOS SDK, or mobile payment UI on iPhone or iPad
- Reports Apple Pay rendering or 3DS issues inside their iOS app checkout
- Asks about minimum iOS 15 compatibility

**Does not apply if the merchant:**
- Is integrating on Android rather than iOS — use Flow Android SDK
- Is building with React Native rather than native iOS — use Flow React Native SDK
- Wants the payment UI on their website rather than in a native mobile app — use Flow Web

**Example:** "Our Flow iOS SDK integration fails Apple Pay validation on devices running iOS 15."

**Likely keywords:** Flow iOS, iOS SDK, mobile payment UI, iPhone, iPad, Apple Pay iOS, min iOS 15, native iOS integration

---

### Flow React Native SDK
**What it is:** Pre-built payment UI for React Native apps.
**Key capabilities:** Don't sell status.
**Contact risk:** n/a

**Applies if the merchant:**
- References Flow React Native or a React Native payments SDK

**Does not apply if the merchant:**
- Is building a native Android app rather than a React Native app — use Flow Android SDK
- Is building a native iOS app rather than a React Native app — use Flow iOS SDK

**Example:** "Is there a Flow SDK for React Native, or do we need to wrap the native SDKs ourselves?"

**Likely keywords:** Flow React Native, React Native payments SDK, cross-platform mobile checkout

---

## Fraud Detection

### Fraud Detection
**What it is:** Rules-based solution for managing payment fraud risk by controlling which payments are accepted.
**Key capabilities:** Risk rules and lists; pre-auth and post-auth assessment; strategy testing and simulation; AVS; fraud flagging.
**Contact risk:** medium — false positive queries, rule tuning requests

**Applies if the merchant:**
- References fraud rules, risk rules, Fraud Detection, false positives, AVS mismatch, or transaction flagging
- Is on the free tier and asks about basic risk rule setup, lists, or simulation/testing of a strategy

**Does not apply if the merchant:**
- Needs more complex, layered risk strategies or advanced strategy building beyond basic rules — use Fraud Detection Pro
- Is disputing a chargeback or asking about a filed dispute rather than pre/post-auth risk screening — treat as a Disputes query, not Fraud Detection

**Example:** "We're seeing a lot of false positives from our AVS rule, can we tune the risk strategy?"

**Likely keywords:** fraud rules, risk rules, Fraud Detection, false positive, AVS mismatch, transaction flagged, risk lists, pre-auth screening, post-auth screening, strategy simulation

---

### Fraud Detection Pro
**What it is:** Enhanced fraud detection with more complex risk strategies and additional features.
**Key capabilities:** Everything in Fraud Detection plus advanced strategy building and upgraded services.
**Contact risk:** medium — same as base, higher complexity

**Applies if the merchant:**
- References Fraud Detection Pro, advanced fraud strategy, complex risk rules, or upgraded fraud management
- Asks about capabilities beyond the free-tier rule set, such as multi-condition or layered strategy building

**Does not apply if the merchant:**
- Only needs basic risk rules, lists, or simple pre/post-auth flagging — use Fraud Detection
- Is asking about chargeback handling rather than upstream risk screening — treat as a Disputes query

**Example:** "We've outgrown basic Fraud Detection rules and need to build a more advanced risk strategy, is that Fraud Detection Pro?"

**Likely keywords:** Fraud Detection Pro, advanced fraud strategy, complex risk rules, upgraded fraud management, layered risk strategy, enhanced fraud tools

---

## Hosted Payment Page

### Hosted Payment Page
**What it is:** Checkout.com-hosted page to which merchants redirect customers to complete payment.
**Key capabilities:** PCI compliance handled by CKO; 40+ payment methods; Remember Me; 24-hour session validity; branding customisation.
**Contact risk:** medium — redirect/session expiry queries, customisation

**Applies if the merchant:**
- References HPP, Hosted Payment Page, redirect to Checkout.com checkout, payment page redirect, or session expiry after 24 hours
- Asks about branding or customisation options on the Checkout.com-hosted page, or about PCI compliance being handled by Checkout.com

**Does not apply if the merchant:**
- Wants to embed the payment UI directly on their own website rather than redirect to a Checkout.com-hosted page — use Flow Web
- Wants the payment UI embedded in a native or React Native mobile app rather than a hosted web redirect — use Flow Android SDK, Flow iOS SDK, or Flow React Native SDK

**Example:** "Our customer's session on the Hosted Payment Page expired before they finished paying, is that the 24-hour limit?"

**Likely keywords:** HPP, Hosted Payment Page, redirect checkout, payment page redirect, session expiry, 24-hour session, PCI compliance, branding customisation, hosted checkout link

---

## Identity Verification

### Address Document Verification
**What it is:** Verification of the authenticity and compliance of an address document, with data extraction via API.
**Key capabilities:** Roadmap.
**Contact risk:** unknown — Roadmap

**Applies if the merchant:**
- Asks about verifying a proof of address document, address document data extraction, or why an address document was rejected during onboarding

**Does not apply if the merchant:**
- Asks about verifying an applicant's identity document (passport, driving licence) rather than an address document — that is ID Document Verification
- Asks about verifying the business's registered address or business registration details rather than an individual's proof of address — that is closer to Business Verification

**Example:** "Why was my customer's utility bill rejected as proof of address?"

**Likely keywords:** address document verification, proof of address, POA check, address document rejection, utility bill verification, address extraction, onboarding address check

---

### AML Screening
**What it is:** Standalone check of an individual applicant against politically exposed persons (PEP), sanctions, and adverse media databases.
**Key capabilities:** PEP screening; sanctions screening; adverse media screening.
**Contact risk:** medium — false positive / screening hit queries

**Applies if the merchant:**
- Asks about screening an individual applicant against PEP, sanctions, or adverse media lists, or disputes a screening hit for a named individual

**Does not apply if the merchant:**
- Asks about screening a business entity against sanctions or adverse media lists rather than an individual — that is Business Screening
- Asks about verifying an individual's identity documents or biometrics rather than screening them against watchlists — that is Identity Verification or ID Document Verification

**Example:** "Our AML screening flagged an applicant as a potential PEP match, but it's a false positive. How do we clear it?"

**Likely keywords:** AML screening, PEP check, PEP match, sanctions screening, sanctions hit, adverse media screening, adverse media match, false positive, watchlist check, individual screening

---

### Business Screening
**What it is:** AML screening of businesses against sanctions and adverse media databases.
**Key capabilities:** Roadmap.
**Contact risk:** unknown

**Applies if the merchant:**
- Asks about screening a business entity (not an individual) against sanctions or adverse media databases, or disputes a business-level screening hit

**Does not apply if the merchant:**
- Asks about screening an individual applicant (e.g. a director or beneficial owner) against PEP, sanctions, or adverse media lists — that is AML Screening
- Asks about verifying the business's registration or ownership structure rather than screening it against watchlists — that is Business Verification

**Example:** "One of our onboarded merchant businesses came back with an adverse media hit. How do we review that?"

**Likely keywords:** business AML screening, business sanctions check, business adverse media screening, company watchlist match, entity screening, corporate sanctions hit

---

### Business Verification
**What it is:** KYB (Know Your Business) verification for businesses.
**Key capabilities:** Roadmap.
**Contact risk:** unknown

**Applies if the merchant:**
- Asks about verifying business identity, registration details, or KYB checks for a business entity onboarding

**Does not apply if the merchant:**
- Asks about screening a business against sanctions or adverse media lists rather than verifying its identity/registration — that is Business Screening
- Asks about verifying an individual's identity (e.g. a director) rather than the business entity itself — that is Identity Verification

**Example:** "What documents are needed to complete KYB verification for our onboarding business?"

**Likely keywords:** KYB, know your business, business verification, business identity check, business registration verification, company verification

---

### Face Authentication
**What it is:** Facial biometric verification to validate applicant identity.
**Key capabilities:** Standalone face check within the Identity Verification suite.
**Contact risk:** medium — biometric failure queries

**Applies if the merchant:**
- Asks specifically about a facial biometric scan, face match, or face authentication failure for an applicant

**Does not apply if the merchant:**
- Asks about document authenticity or cross-referencing a document photo rather than the live face scan itself — that is ID Document Verification
- Asks about the identity verification flow generally, without a specific biometric/face-match complaint — that is Identity Verification

**Example:** "Our applicant's face scan keeps failing to match their ID photo. What's causing that?"

**Likely keywords:** face authentication, facial biometrics, face scan failure, face match, liveness check, biometric verification failure, selfie verification

---

### ID Document Verification
**What it is:** Verification that ID documents are authentic and match the individual.
**Key capabilities:** Document authenticity check; cross-referenced with face auth.
**Contact risk:** medium — document rejection queries

**Applies if the merchant:**
- Asks about ID document rejection, authenticity checks, or passport/driving licence verification failures for an applicant

**Does not apply if the merchant:**
- Asks about proof of address document verification rather than an identity document (passport, licence) — that is Address Document Verification
- Asks purely about a facial biometric/face-match failure rather than the document itself — that is Face Authentication

**Example:** "Our applicant's passport keeps getting rejected during document verification. Why?"

**Likely keywords:** ID document verification, document authenticity, passport rejection, driving licence rejection, document check failure, identity document scan, document fraud check

---

### Identity Verification
**What it is:** KYC solution enabling businesses to verify the identity of individuals onboarding to their services.
**Key capabilities:** ID document verification; facial biometrics; AML screening (PEPs, sanctions, adverse media).
**Contact risk:** medium — onboarding friction; false rejection queries

**Applies if the merchant:**
- Asks generally about the KYC/IDV product, onboarding friction, or false rejections spanning document, biometric, and screening checks together

**Does not apply if the merchant:**
- Raises a specific, isolated issue with only the document check — that is ID Document Verification
- Raises a specific, isolated issue with only the facial biometric check — that is Face Authentication
- Raises a specific, isolated issue with only the PEP/sanctions/adverse media screening step — that is AML Screening
- Asks about verifying a business entity rather than an individual — that is Business Verification or Business Screening

**Example:** "Our KYC onboarding flow is rejecting too many legitimate applicants. Can you help us understand why?"

**Likely keywords:** identity verification, IDV, KYC, know your customer, onboarding verification, false rejection, document verification, facial biometrics, AML screening, PEP checks, sanctions screening

---

## Intelligent Acceptance

### Intelligent Acceptance
**What it is:** AI-powered solution that dynamically applies optimisations to maximise payment conversion.
**Key capabilities:** 3DS/SCA exemption management; adaptive messaging; network token provisioning; smart routing; performance dashboard. Requires 5,000+ monthly transactions.
**Contact risk:** low — self-serve insights; queries mainly around expected vs actual uplift

**Applies if the merchant:**
- Asks about Intelligent Acceptance itself, smart routing, 3DS/SCA exemption management, network token provisioning, or a gap between expected and actual acceptance rate uplift

**Does not apply if the merchant:**
- Asks about general payment authorization or decline reasons unrelated to the optimisation layer, or is below the 5,000+ monthly transaction eligibility threshold and asking why they can't access it — clarify eligibility rather than classifying as a product issue

**Example:** "We expected a bigger acceptance rate improvement from Intelligent Acceptance than what we're seeing on the dashboard."

**Likely keywords:** Intelligent Acceptance, acceptance rate optimisation, smart routing, 3DS exemption, SCA exemption management, network tokens, expected vs actual uplift, conversion optimisation dashboard

---

## Internal Products

### Notifications
**What it is:** Merchant notification system for payment events.
**Contact risk:** medium — notification configuration queries

**Applies if the merchant:**
- Asks about setting up or configuring webhooks, event notifications, or reports a missed payment event notification

**Does not apply if the merchant:**
- Asks about the underlying payment event itself (e.g. why a payment failed) rather than the notification/webhook delivery of that event — classify under the relevant payment product instead

**Example:** "We're not receiving webhook notifications for our capture events. Can you check our configuration?"

**Likely keywords:** webhooks, webhook configuration, notification setup, event notification, missed notification, webhook delivery failure, payment event alert

---

## Issuing

### Authentication (Issuing)
**What it is:** 3DS for transactions on issued cards.
**Key capabilities:** SCA compliance for issued cardholders.
**Contact risk:** medium — 3DS friction on issued cards.

**Applies if the merchant:**
- References 3DS challenges, SCA prompts, or authentication failures happening on transactions made with cards they issued to employees or customers
- Asks about configuring or troubleshooting SCA compliance for their issuing programme's cardholders

**Does not apply if the merchant:**
- Is describing 3DS/SCA friction on payments they are accepting as a merchant, not on cards they issue — that's the acquiring-side **Authentication** product
- Is asking about exempting or scoping issued-card transactions out of SCA entirely rather than the challenge flow itself — see **SCA Exemptions (Issuing)** or **SCA Out of Scope (Issuing)**

**Example:** "Our issued cardholders are getting declined at the 3DS challenge step when they use their virtual cards."

**Likely keywords:** 3DS issuing, SCA issued cards, authentication failure issued card, cardholder 3DS challenge, issuing SCA compliance, step-up authentication issued card

---

### BIN Management
**What it is:** Management of Bank Identification Numbers for an issuing programme.
**Key capabilities:** BIN allocation, configuration, and routing.
**Contact risk:** low — technical setup; low ongoing contact.

**Applies if the merchant:**
- References BIN allocation, BIN sponsorship, BIN configuration, or routing rules tied to the bank identification number of their issuing programme
- Asks which BIN their issued cards are drawing from or how BIN-level settings affect card behaviour

**Does not apply if the merchant:**
- Is asking about the card network, product type, or feature set attached to a specific card line rather than the BIN itself — see **Card Product**
- Is asking about the hierarchical setup of entities/participants in their programme rather than BIN-level routing — see **Entity Structure**
- Is asking about region-specific issuing settings rather than the BIN — see **Issuing Region**

**Example:** "Can you confirm which BIN our new virtual card product is issued under?"

**Likely keywords:** BIN, BIN allocation, bank identification number, BIN configuration, BIN sponsorship, BIN routing, issuing programme BIN

---

### Card Product
**What it is:** The card programme definition (network, product type, features).
**Key capabilities:** Configures the underlying card product rules.
**Contact risk:** low — configuration handled at setup.

**Applies if the merchant:**
- References the card programme's network (Visa/Mastercard), product type, or feature configuration (e.g. prepaid vs debit, credit line rules)
- Asks how to set up or amend the rules governing a specific card product line

**Does not apply if the merchant:**
- Is asking about the BIN their cards are issued under rather than the product rules layered on top of it — see **BIN Management**
- Is asking about the programme's entity hierarchy rather than the card product's own feature set — see **Entity Structure**
- Is asking about actual physical or virtual card issuance/activation for a cardholder — see **Cards** or **Physical Cards**

**Example:** "We want to add a new card product with different network and feature settings for our premium tier."

**Likely keywords:** card product configuration, card programme rules, card network setup Visa Mastercard, card product features, card product type

---

### Cardholder
**What it is:** Cardholder profile management.
**Key capabilities:** Create, update, and manage cardholders and their associated cards.
**Contact risk:** medium — cardholder data queries.

**Applies if the merchant:**
- References creating, updating, or looking up a cardholder profile (name, KYC data, contact details) independent of any specific card
- Asks how to link or manage multiple cards under one cardholder record

**Does not apply if the merchant:**
- Is asking about issuing, activating, or managing a specific virtual or physical card itself rather than the underlying person/profile — see **Cards** or **Physical Cards**
- Is asking about a card's PIN rather than the cardholder's profile data — see **Physical card PIN**

**Example:** "We need to update the KYC details on a cardholder profile before we can issue them a new card."

**Likely keywords:** cardholder profile, cardholder creation, cardholder data update, cardholder KYC, manage cardholder, cardholder record

---

### Cards
**What it is:** Physical and virtual card issuance for businesses to distribute to employees or customers.
**Key capabilities:** Card lifecycle management (activate, suspend, revoke); customisable card design; digital wallet integration.
**Contact risk:** medium — card activation/management queries.

**Applies if the merchant:**
- References issuing, activating, suspending, or revoking a virtual or physical card as part of their card programme
- Asks generally about card lifecycle management or customising card design across the programme

**Does not apply if the merchant:**
- Is asking specifically about a physical card's delivery, print design, or renewal — see **Physical Cards**
- Is asking about the cardholder's profile data rather than the card itself — see **Cardholder**
- Is asking about PIN set/change/unlock — see **Physical card PIN**
- Is asking about adding the card to Apple Pay / Google Pay — see **Digital Wallets (Issuing)**

**Example:** "How do we suspend an employee's card immediately after they leave the company?"

**Likely keywords:** card issuance, card activation, card suspension, card revoke, card lifecycle, virtual card, card design customisation

---

### Digital Wallets (Issuing)
**What it is:** Integration of issued cards into Apple Pay, Google Pay, etc.
**Key capabilities:** Wallet provisioning for virtual and physical cards.
**Contact risk:** medium — provisioning failures.

**Applies if the merchant:**
- References adding an issued card (virtual or physical) to Apple Pay or Google Pay and hitting a provisioning error or delay
- Asks how to enable wallet provisioning for their issuing programme

**Does not apply if the merchant:**
- Is asking about the card's own activation, suspension, or design rather than wallet provisioning specifically — see **Cards** or **Physical Cards**
- Is asking about issuing the underlying card product/BIN rather than the wallet integration layer — see **Card Product** or **BIN Management**

**Example:** "Our cardholder can't add their virtual card to Apple Pay — the provisioning request keeps failing."

**Likely keywords:** Apple Pay provisioning, Google Pay provisioning, digital wallet issued card, wallet provisioning failure, tokenisation issued card, add card to wallet

---

### Entity Structure
**What it is:** Hierarchical entity setup for card programme participants.
**Key capabilities:** Programme hierarchy configuration.
**Contact risk:** low — setup complexity.

**Applies if the merchant:**
- References the hierarchy of entities/participants within their issuing programme (e.g. parent company, subsidiaries, business units) and how they relate to one another
- Asks how to configure or restructure programme participant levels

**Does not apply if the merchant:**
- Is asking about the BIN their programme runs on rather than the participant hierarchy — see **BIN Management**
- Is asking about the card product's network/feature rules rather than entity hierarchy — see **Card Product**
- Is asking about geographic/regional configuration rather than organisational hierarchy — see **Issuing Region**

**Example:** "We're restructuring our issuing programme and need to add a new subsidiary entity beneath our parent account."

**Likely keywords:** entity structure, programme hierarchy, issuing participant configuration, entity setup, subsidiary entity, programme entity levels

---

### Fraud (Issuing)
**What it is:** Fraud management for issued card transactions.
**Key capabilities:** Fraud rule configuration for issuing.
**Contact risk:** medium.

**Applies if the merchant:**
- References fraud rules, fraud alerts, or suspicious activity on transactions made with cards they issued
- Asks how to configure fraud detection settings for their issuing programme

**Does not apply if the merchant:**
- Is describing fraud on payments they're accepting as a merchant (chargebacks, fraudulent purchases against them), not on cards they issue — that's the acquiring-side **Fraud Detection** product
- Is asking about limiting where/how much an issued card can spend rather than fraud detection itself — see **Spending Controls**

**Example:** "We got an alert flagging suspicious transactions on one of our issued cards — how do we adjust the fraud rules?"

**Likely keywords:** issuing fraud rules, fraud alert issued card, suspicious transaction issued card, fraud rule configuration issuing, issuing fraud management

---

### Issuing Region
**What it is:** Geographic region configuration for an issuing programme.
**Key capabilities:** Region-level programme settings.
**Contact risk:** low.

**Applies if the merchant:**
- References the geographic region their issuing programme is configured for and asks about region-specific settings or launching in a new region
- Asks whether their card programme supports issuance in a particular country/region

**Does not apply if the merchant:**
- Is asking about the BIN underpinning their programme rather than its regional configuration — see **BIN Management**
- Is asking about the entity/participant hierarchy rather than geography — see **Entity Structure**
- Is asking about the card product's features rather than where it's issuable — see **Card Product**

**Example:** "Can we extend our issuing programme to support cards issued in a new region?"

**Likely keywords:** issuing region configuration, geographic issuing settings, region launch issuing, regional issuing setup, issuing programme geography

---

### Physical card PIN
**What it is:** PIN management for physical issued cards.
**Key capabilities:** PIN set, change, unlock capabilities.
**Contact risk:** medium — PIN-related queries.

**Applies if the merchant:**
- References setting, changing, or unlocking the PIN on a physical issued card
- Asks about a cardholder being locked out due to repeated incorrect PIN attempts

**Does not apply if the merchant:**
- Is asking about the physical card's delivery, design, or activation rather than its PIN — see **Physical Cards**
- Is asking about the cardholder's profile rather than the card's PIN — see **Cardholder**
- Is describing a virtual card issue, which has no physical PIN — see **Cards**

**Example:** "Our cardholder is locked out of their physical card after entering the wrong PIN too many times."

**Likely keywords:** PIN set, PIN change, PIN unlock, physical card PIN, PIN locked, forgotten PIN issued card

---

### Physical Cards
**What it is:** Physical payment cards issued under a business's card programme.
**Key capabilities:** Design customisation; PIN management; activation/renewal.
**Contact risk:** medium — delivery and activation queries.

**Applies if the merchant:**
- References the physical card itself: delivery, print/design customisation, activation on receipt, or renewal ahead of expiry
- Asks why a cardholder hasn't received their physical card or how to reissue one

**Does not apply if the merchant:**
- Is asking specifically about the PIN rather than the card's delivery/design/activation — see **Physical card PIN**
- Is asking about a virtual card rather than a physical one — see **Cards**
- Is asking about the cardholder's profile data rather than the physical card object — see **Cardholder**

**Example:** "Our employee still hasn't received their physical card three weeks after we ordered it."

**Likely keywords:** physical card delivery, card design, physical card activation, card renewal, reissue physical card, card not received

---

### Reporting (Issuing)
**What it is:** Transaction and programme reporting for issuers.
**Key capabilities:** Reconciliation and analytics for issued card activity.
**Contact risk:** low.

**Applies if the merchant:**
- References aggregate reports, reconciliation files, or analytics/dashboards covering issued card activity across the programme
- Asks how to export or schedule issuing reports

**Does not apply if the merchant:**
- Is asking about a single specific transaction's status or detail rather than aggregate reporting — see **Transactions (Issuing)**
- Is asking about test-environment output from a simulated transaction rather than live reporting — see **Simulation (Issuing)**

**Example:** "We need a monthly reconciliation report covering all issued card transactions for our finance team."

**Likely keywords:** issuing reports, issuing reconciliation, issued card analytics, transaction report export, issuing dashboard

---

### SCA Exemptions (Issuing)
**What it is:** SCA exemption application for issued card transactions.
**Key capabilities:** Reduces friction for low-risk issued card payments.
**Contact risk:** low.

**Applies if the merchant:**
- References applying a specific SCA exemption (e.g. low-value, low-risk, trusted beneficiary) to a transaction on an issued card to skip the authentication challenge
- Asks why an exemption wasn't applied to a given issued-card transaction

**Does not apply if the merchant:**
- Is asking about transactions that fall entirely outside SCA scope by rule, rather than an exemption applied case-by-case — see **SCA Out of Scope (Issuing)**
- Is asking about the 3DS challenge flow itself rather than exemption logic — see **Authentication (Issuing)**

**Example:** "This low-value transaction on our issued card should have qualified for an SCA exemption but got challenged anyway."

**Likely keywords:** SCA exemption issuing, low-value exemption issued card, low-risk exemption, exemption not applied, issuing exemption logic

---

### SCA Out of Scope (Issuing)
**What it is:** Handling of transactions excluded from SCA requirements.
**Key capabilities:** Compliance scoping for issuing.
**Contact risk:** low.

**Applies if the merchant:**
- References transactions on issued cards that are categorically excluded from SCA requirements (e.g. certain MOTO or anonymous prepaid use cases), not exemption logic
- Asks whether a transaction type is in or out of SCA scope for their issuing programme

**Does not apply if the merchant:**
- Is asking about applying a discretionary exemption to an in-scope transaction — see **SCA Exemptions (Issuing)**
- Is asking about the challenge/authentication flow for an in-scope transaction — see **Authentication (Issuing)**

**Example:** "Are our anonymous prepaid card transactions considered out of SCA scope entirely, or do they still need an exemption?"

**Likely keywords:** SCA out of scope, SCA exclusion issuing, out-of-scope transaction, SCA compliance scoping, issuing SCA rules

---

### Simulation (Issuing)
**What it is:** Sandbox simulation of issuing transactions for testing.
**Key capabilities:** Test card authorisation and lifecycle events.
**Contact risk:** low — development only.

**Applies if the merchant:**
- References testing card authorisations or lifecycle events (issuance, activation, decline) in a sandbox/test environment before going live
- Asks how to simulate a specific issuing scenario during integration

**Does not apply if the merchant:**
- Is asking about a live transaction rather than a sandbox simulation — see **Transactions (Issuing)**
- Is asking about live reporting/reconciliation rather than test output — see **Reporting (Issuing)**
- Is asking about actually issuing a real card rather than simulating one — see **Cards**

**Example:** "How do we simulate a declined authorisation for an issued card in the sandbox before we go live?"

**Likely keywords:** issuing sandbox, test card authorisation, simulate issuing transaction, sandbox lifecycle event, issuing test environment

---

### Spending Controls
**What it is:** Configurable limits on how issued cards can be used.
**Key capabilities:** Budget limits, frequency controls, merchant category restrictions.
**Contact risk:** medium — limit queries, blocked transaction queries.

**Applies if the merchant:**
- References setting or troubleshooting spend limits, frequency caps, or merchant category (MCC) restrictions on an issued card
- Asks why a card transaction was blocked due to a spending limit or category restriction

**Does not apply if the merchant:**
- Is asking about a transaction blocked for suspected fraud rather than a configured limit — see **Fraud (Issuing)**
- Is asking about the card's activation/design/lifecycle rather than its spend rules — see **Cards**

**Example:** "Our employee's card was declined and I think it's hit its monthly spending limit — can you confirm?"

**Likely keywords:** spending limit, budget control, MCC restriction, frequency limit, card spend controls, transaction blocked limit

---

### Transactions (Issuing)
**What it is:** View and manage individual issuing transactions.
**Key capabilities:** Transaction history, details, and status.
**Contact risk:** medium — transaction query and reconciliation.

**Applies if the merchant:**
- References a specific issued card transaction and asks about its status, detail, or history
- Asks to look up an individual transaction rather than an aggregate report

**Does not apply if the merchant:**
- Is asking for an aggregate report or reconciliation file across many transactions rather than one specific transaction — see **Reporting (Issuing)**
- Is asking about a test-environment transaction rather than a live one — see **Simulation (Issuing)**

**Example:** "Can you pull up the status of this specific transaction on our issued card from yesterday?"

**Likely keywords:** issuing transaction lookup, transaction status issued card, transaction detail, transaction history, individual issuing transaction

---

## Network Tokens

### Network Tokens
**What it is:** Unique digital identifiers replacing card PANs to improve acceptance and security.
**Key capabilities:** Auto-updated when underlying card changes; reduces declines from expired cards; improves security.
**Contact risk:** low — mostly invisible to merchants; queries on tokenisation failures

**Applies if the merchant:**
- Asks why a card was tokenised or references a scheme/network token instead of the raw PAN
- Reports a decline tied to a token that failed to update after the underlying card changed
- Asks how tokenisation improves acceptance rates or protects stored card data

**Does not apply if the merchant:**
- Is asking about card details refreshing automatically without mentioning tokens specifically — that's Real-Time Account Updater, a separate (though related) service
- Is asking about storing card credentials generally rather than the token replacing the PAN — that's Vault (Integrated Vault or Standalone Vault)

**Example:** "One of our transactions declined and support mentioned it was a network token issue — what does that mean?"

**Likely keywords:** network token, scheme token, card PAN replacement, tokenisation failure, token-related decline, token provisioning, digital card identifier, token unexpectedly expired

---

## Payment Links

### Payment Links
**What it is:** Unique URL redirecting customers to a Hosted Payments Page to complete payment.
**Key capabilities:** No-code option; 40+ methods; shareable via any channel; Dashboard or API management.
**Contact risk:** low — simple product; main queries around expiry or method availability

**Applies if the merchant:**
- References a shareable payment URL, QR code, or "link-to-pay" they send customers directly
- Asks about creating, expiring, or resending a Payment Link from the Dashboard or via API
- Asks which payment methods are available on their Payment Link

**Does not apply if the merchant:**
- Is building a full checkout integration into their own website or app rather than sending a standalone link — that's a Hosted Payments Page integration or the Payments/Unified Payments API, not a Payment Link
- Is asking about in-person, tap-to-pay collection rather than a remote link — that's SoftPOS SDK or Unified Commerce

**Example:** "Can I set an expiry date on the payment link I send to customers by email?"

**Likely keywords:** payment link, shareable payment URL, QR code payment, link-to-pay, hosted payments page link, no-code payment link, link expiry

---

## Real-Time Account Updater

### Real-Time Account Updater
**What it is:** Service that automatically updates stored card details when they change.
**Key capabilities:** Monitors stored credentials; auto-refreshes on issuer update; Mastercard and Visa supported; webhook notifications.
**Contact risk:** low — queries mainly on unexpected updates or reconciliation

**Applies if the merchant:**
- Asks why a stored card's expiry date or number changed without customer action
- References Account Updater, RTAU, or an auto-refreshed stored card
- Asks about the webhook notification sent when a card on file is updated

**Does not apply if the merchant:**
- Is asking about the underlying credential storage itself rather than the auto-refresh mechanism — that's Vault (Integrated Vault or Standalone Vault)
- Is asking about a scheme token replacing the PAN rather than the card number itself updating — that's Network Tokens

**Example:** "We noticed a customer's stored card number changed automatically in our records — was that Checkout.com's Account Updater?"

**Likely keywords:** Account Updater, RTAU, Real-Time Account Updater, unexpected card detail update, stored card auto-refresh, card update webhook, Mastercard/Visa account updater

---

## Partner Integrations and Plugins

### ACI
**What it is:** Partner integration with ACI Worldwide, a global real-time payments and orchestration technology provider.
**Contact risk:** unknown — Roadmap

**Applies if the merchant:**
- Explicitly names ACI or ACI Worldwide as the routing or orchestration layer in front of Checkout.com
- Describes real-time payments infrastructure or orchestration technology provided by ACI

**Does not apply if the merchant:**
- Describes multi-PSP or multi-provider orchestration without naming ACI — could be BR-DGE, Gr4vy, Payrails, Spreedly, Primer.io, IXOPay, or YUNO; ask which orchestration vendor is in use
- Describes Latin America-specific routing — more likely YUNO, which is LatAm-focused

**Example:** "We route payments through ACI Worldwide into Checkout.com and a transaction failed to settle."

**Likely keywords:** ACI, ACI Worldwide, real-time payments orchestration, ACI integration, ACI routing

---

### Basis Theory
**What it is:** Token vault partner integration.
**Contact risk:** low

**Applies if the merchant:**
- Explicitly names Basis Theory as their tokenisation or vault provider
- Describes storing or proxying card data through a third-party token vault ahead of Checkout.com

**Does not apply if the merchant:**
- Names a different vault or orchestration partner that also offers tokenisation — Spreedly and Payrails both include vault capability, so confirm the exact vendor name before classifying
- Describes Checkout.com's own native vault product rather than a third-party vault

**Example:** "Our cards are tokenised in Basis Theory and we're seeing a mismatch when passing the token to Checkout.com."

**Likely keywords:** Basis Theory, token vault, tokenisation, third-party vault, card token proxy

---

### BigCommerce
**What it is:** Native Checkout.com plugin for BigCommerce merchants.
**Contact risk:** medium — plugin setup and update queries

**Applies if the merchant:**
- Names BigCommerce specifically as their storefront platform
- Reports plugin installation, configuration, or update issues within a BigCommerce admin panel

**Does not apply if the merchant:**
- Names a different ecommerce platform plugin — Magento 2, WooCommerce, Shopify (onsite or offsite), PrestaShop, SAP Commerce Cloud, SAP OPF, Salesforce Commerce Cloud, CommerceTools, Visualsoft, or OpenCart — check the platform name carefully since symptoms (checkout errors, plugin update failures) look identical across all of these
- Describes a headless or API-only integration with no named storefront platform

**Example:** "We updated the Checkout.com plugin on our BigCommerce store and now payments aren't showing at checkout."

**Likely keywords:** BigCommerce, BigCommerce plugin, BigCommerce app, storefront integration, plugin update, checkout error BigCommerce

---

### BR-DGE
**What it is:** Payment orchestration layer partner.
**Contact risk:** low

**Applies if the merchant:**
- Explicitly names BR-DGE as their orchestration or routing layer
- Describes multi-PSP routing decisions being managed through BR-DGE

**Does not apply if the merchant:**
- Names a different orchestration vendor — Gr4vy, Payrails, Spreedly, Primer.io, IXOPay, or YUNO — these all perform the same multi-PSP routing function, so the vendor name is the only reliable signal
- Describes regional-specific orchestration (LatAm) — more likely YUNO

**Example:** "BR-DGE is routing our transactions to Checkout.com and we want to check the failover logic."

**Likely keywords:** BR-DGE, payment orchestration, multi-PSP routing, orchestration layer, routing partner

---

### Chargebee
**What it is:** Subscription billing platform integration.
**Contact risk:** medium — recurring billing queries

**Applies if the merchant:**
- Explicitly names Chargebee as their subscription or recurring billing platform
- Describes recurring payment collection or dunning managed through Chargebee

**Does not apply if the merchant:**
- Names a different subscription billing platform — Chargify, Recurly, or Zuora — all four handle recurring billing similarly, so confirm the exact platform name
- Describes a one-off or non-recurring payment issue unrelated to subscription billing

**Example:** "Our Chargebee subscriptions are failing to charge the saved card via Checkout.com."

**Likely keywords:** Chargebee, subscription billing, recurring payments, Chargebee integration, dunning, subscription management

---

### Chargify
**What it is:** Subscription management platform integration.
**Contact risk:** medium — recurring billing queries

**Applies if the merchant:**
- Explicitly names Chargify as their subscription management platform
- Describes recurring billing cycles or plan management handled through Chargify

**Does not apply if the merchant:**
- Names a different subscription billing platform — Chargebee, Recurly, or Zuora — these are functionally similar, so rely on the exact vendor name given
- Describes Chargify as a rebrand name (Maxio) — still classify as Chargify unless the merchant clearly means a different tool

**Example:** "We use Chargify for our recurring plans and payments aren't syncing back from Checkout.com."

**Likely keywords:** Chargify, Maxio, subscription management, recurring billing, plan billing sync

---

### Dwolla
**What it is:** US-focused API-based payment infrastructure provider enabling bank transfers, instant payments, and account-to-account transactions.
**Key capabilities:** Card payouts / push-to-card via OCT Direct Funds Disbursement to Visa and Mastercard debit cards; RTAU for updated card details (Beta).
**Contact risk:** medium — payout delivery and card-update queries

**Applies if the merchant:**
- Explicitly names Dwolla as their payout or disbursement provider
- Describes push-to-card payouts, OCT Direct Funds Disbursement to Visa/Mastercard debit cards, or RTAU card-detail updates via Dwolla

**Does not apply if the merchant:**
- Describes bank transfers or account-to-account payments with no Dwolla mention and no US-specific framing — check whether they mean a different payout mechanism entirely, not a partner in this list
- Describes fitness/booking payments — that is Zingfit, not Dwolla

**Example:** "Our Dwolla push-to-card payout to a Visa debit card failed and the card details might be outdated."

**Likely keywords:** Dwolla, push-to-card, OCT Direct Funds Disbursement, RTAU, instant payout, bank transfer, account-to-account, debit card payout

---

### GIG
**What it is:** Partner integration.
**Contact risk:** unknown

**Applies if the merchant:**
- Explicitly names "GIG" as their integration or platform partner

**Does not apply if the merchant:**
- Given the generic name, "GIG" could be misheard or confused with an unrelated gig-economy platform reference rather than this specific partner integration — verify the merchant means the named partner, not a general gig-work platform, before classifying here

**Example:** "We're integrated with GIG and need help confirming our payment configuration."

**Likely keywords:** GIG, GIG integration, GIG platform

---

### Gr4vy
**What it is:** Payment orchestration layer partner.
**Contact risk:** low

**Applies if the merchant:**
- Explicitly names Gr4vy as their orchestration or routing layer
- Describes payment routing decisions or PSP failover managed through Gr4vy

**Does not apply if the merchant:**
- Names a different orchestration vendor — BR-DGE, Payrails, Spreedly, Primer.io, IXOPay, or YUNO — all serve the same function, so the vendor name is the deciding signal
- Describes a white-label orchestration platform specifically — more likely IXOPay

**Example:** "Gr4vy is routing our checkout traffic to Checkout.com and one route is failing."

**Likely keywords:** Gr4vy, payment orchestration, routing layer, PSP failover, orchestration partner

---

### IXOPay
**What it is:** Partner integration with IXOPay, a white-label payment orchestration platform used to manage multiple payment providers.
**Contact risk:** unknown — Roadmap

**Applies if the merchant:**
- Explicitly names IXOPay as their orchestration platform
- Describes a white-label orchestration setup managing multiple payment providers including Checkout.com

**Does not apply if the merchant:**
- Names a different orchestration vendor — BR-DGE, Gr4vy, Payrails, Spreedly, Primer.io, or YUNO — these overlap heavily in function, so confirm the exact vendor name
- Describes LatAm-specific routing — more likely YUNO

**Example:** "We manage our providers through IXOPay's white-label platform and Checkout.com isn't receiving routed volume."

**Likely keywords:** IXOPay, white-label orchestration, multi-provider routing, orchestration platform, provider management

---

### Magento 2
**What it is:** Native Checkout.com plugin for Magento 2 merchants.
**Contact risk:** medium — plugin setup and update queries

**Applies if the merchant:**
- Names Magento 2 or Adobe Commerce specifically as their storefront platform
- Reports checkout integration issues, plugin installation, or module update problems within a Magento admin

**Does not apply if the merchant:**
- Names a different ecommerce plugin platform — WooCommerce, BigCommerce, Shopify (onsite or offsite), PrestaShop, SAP Commerce Cloud, SAP OPF, Salesforce Commerce Cloud, CommerceTools, Visualsoft, or OpenCart — plugin symptoms look similar across all of these, so confirm platform name
- Refers to legacy Magento 1 — this plugin is Magento 2 only

**Example:** "The Checkout.com module for Magento 2 stopped processing payments after our Adobe Commerce upgrade."

**Likely keywords:** Magento 2, Adobe Commerce, Magento module, Magento plugin, checkout integration Magento

---

### Ocado Group
**What it is:** Platform integration for grocery ecommerce, using Checkout.com Flow for card payments.
**Key capabilities:** Flow integration (integrated payments or tokenization only); auto capture; refunds; voids; CIT and MIT support; integrated 3DS.
**Contact risk:** medium — plugin setup and card-only payment queries

**Applies if the merchant:**
- Explicitly names Ocado or Ocado Group as the platform
- Describes grocery ecommerce checkout using Checkout.com Flow, with capabilities limited to card payments (auth, capture, refunds, voids, CIT/MIT, integrated 3DS)

**Does not apply if the merchant:**
- Describes a different Flow-based headless integration with no Ocado reference — more likely CommerceTools or Primer.io depending on stack
- Describes fitness or booking payments — that's Zingfit, a different vertical platform integration

**Example:** "Our Ocado Flow integration is declining card payments at checkout with a 3DS error."

**Likely keywords:** Ocado, Ocado Group, grocery ecommerce, Checkout.com Flow, card-only payments, CIT, MIT, integrated 3DS

---

### OpenCart
**What it is:** Native Checkout.com plugin for OpenCart.
**Contact risk:** low

**Applies if the merchant:**
- Names OpenCart specifically as their storefront platform
- Reports plugin or extension issues within an OpenCart admin

**Does not apply if the merchant:**
- Names a different open-source or self-hosted ecommerce plugin — PrestaShop, WooCommerce, or Magento 2 — confirm exact platform name since setup symptoms overlap
- Describes an enterprise platform (SAP, Salesforce, CommerceTools) — those are separate, higher-tier integrations

**Example:** "Our OpenCart extension for Checkout.com isn't showing on the payment method list."

**Likely keywords:** OpenCart, OpenCart extension, OpenCart plugin, open-source storefront

---

### Payrails
**What it is:** Payment orchestration layer partner.
**Contact risk:** low

**Applies if the merchant:**
- Explicitly names Payrails as their orchestration or processor-routing layer
- Describes payment orchestration, vaulting, or multi-processor management through Payrails

**Does not apply if the merchant:**
- Names a different orchestration vendor — BR-DGE, Gr4vy, Spreedly, Primer.io, IXOPay, or YUNO — all overlap in function, so the vendor name decides classification
- Describes token vaulting only with no orchestration/routing component — could be Basis Theory or Spreedly instead

**Example:** "Payrails is orchestrating our processors and Checkout.com transactions are being routed incorrectly."

**Likely keywords:** Payrails, payment orchestration, processor routing, multi-processor management, orchestration layer

---

### Prestashop
**What it is:** Native Checkout.com plugin for PrestaShop, an open-source ecommerce platform. Deprecated — no longer actively supported.
**Contact risk:** n/a — deprecated

**Applies if the merchant:**
- Names PrestaShop specifically as their storefront platform
- Reports issues with the (deprecated, unsupported) Checkout.com PrestaShop plugin

**Does not apply if the merchant:**
- Names a different open-source plugin platform — OpenCart, WooCommerce, or Magento 2 — confirm exact platform name, especially since PrestaShop support has ended and merchants may be migrating to one of these
- Describes an actively supported plugin migration path away from PrestaShop — flag as a migration query, not a standard plugin support query

**Example:** "We're still on the Checkout.com PrestaShop plugin and need to know if it's still supported."

**Likely keywords:** PrestaShop, PrestaShop plugin, deprecated plugin, unsupported integration, PrestaShop checkout

---

### Salesforce Commerce Cloud
**What it is:** Native Checkout.com plugin for Salesforce Commerce Cloud.
**Contact risk:** medium — enterprise plugin setup queries

**Applies if the merchant:**
- Names Salesforce Commerce Cloud, SFCC, SFRA, or SiteGenesis specifically
- Reports cartridge installation, configuration, or checkout integration issues within an SFCC environment

**Does not apply if the merchant:**
- Names a different enterprise commerce platform — SAP Commerce Cloud, SAP OPF, or CommerceTools — these are all enterprise-tier integrations with similar setup complexity, so confirm exact platform
- Describes a mid-market plugin platform (Magento, BigCommerce, WooCommerce) — lower complexity, different support path

**Example:** "Our Checkout.com cartridge on SFRA is throwing an error at the payment step."

**Likely keywords:** Salesforce Commerce Cloud, SFCC, SFRA, SiteGenesis, cartridge integration, Salesforce checkout

---

### SAP Commerce Cloud
**What it is:** Native Checkout.com plugin for SAP Commerce Cloud.
**Contact risk:** medium — enterprise plugin setup queries

**Applies if the merchant:**
- Names SAP Commerce Cloud, SAP Hybris, or SAP B2C Accelerator specifically
- Reports integration or configuration issues within an SAP Commerce Cloud environment

**Does not apply if the merchant:**
- Names SAP OPF specifically — a distinct SAP integration (SAP Open Payment Framework) rather than SAP Commerce Cloud; confirm which SAP product is meant
- Names a different enterprise platform — Salesforce Commerce Cloud or CommerceTools — confirm exact platform name

**Example:** "We're on SAP Hybris and the Checkout.com B2C Accelerator module isn't capturing payments."

**Likely keywords:** SAP Commerce Cloud, SAP Hybris, SAP B2C Accelerator, SAP integration, enterprise commerce plugin

---

### Shopify (offsite)
**What it is:** Offsite redirect integration for Shopify merchants.
**Contact risk:** medium — redirect and reconciliation queries

**Applies if the merchant:**
- Names Shopify and describes being redirected off-site to a hosted payment page (HPP) rather than paying within the Shopify checkout itself
- Reports reconciliation issues tied to the redirect flow

**Does not apply if the merchant:**
- Describes paying without leaving the Shopify checkout page — that's Shopify (onsite), a distinct integration with different setup and support flow
- Names a different platform's redirect flow entirely — confirm "Shopify" is explicitly mentioned

**Example:** "Customers are redirected to a Checkout.com hosted page from our Shopify store and some payments aren't reconciling back to orders."

**Likely keywords:** Shopify offsite, HPP, hosted payment page, redirect checkout, Shopify redirect, reconciliation

---

### Shopify (onsite)
**What it is:** Native onsite Checkout.com integration for Shopify.
**Contact risk:** medium — plugin setup; Shopify-specific flows

**Applies if the merchant:**
- Names Shopify and describes paying directly within the native Shopify checkout without being redirected elsewhere
- Reports plugin setup or configuration issues specific to onsite Shopify payments

**Does not apply if the merchant:**
- Describes being redirected to a separate hosted page — that's Shopify (offsite), not onsite
- Names a different ecommerce platform plugin — confirm "Shopify" specifically before classifying here

**Example:** "Our Shopify checkout uses the native Checkout.com integration and payments are erroring without a redirect."

**Likely keywords:** Shopify onsite, native Shopify checkout, Shopify payments, Shopify plugin, in-checkout payment

---

### Spreedly
**What it is:** Payment orchestration and vault partner.
**Contact risk:** low

**Applies if the merchant:**
- Explicitly names Spreedly as their orchestration or vaulting partner
- Describes card vaulting combined with multi-gateway routing through Spreedly

**Does not apply if the merchant:**
- Names a different orchestration vendor — BR-DGE, Gr4vy, Payrails, Primer.io, IXOPay, or YUNO — these overlap in orchestration function, so confirm exact vendor name
- Describes vaulting only, with a dedicated token-vault vendor named — more likely Basis Theory

**Example:** "Spreedly is vaulting our cards and routing to Checkout.com, but the token pass-through is failing."

**Likely keywords:** Spreedly, payment orchestration, token vault, multi-gateway routing, card vaulting

---

### WooCommerce
**What it is:** Native Checkout.com plugin for WooCommerce merchants.
**Contact risk:** medium — plugin setup and update queries

**Applies if the merchant:**
- Names WooCommerce or WordPress checkout specifically
- Reports plugin installation, update, or configuration issues within a WooCommerce/WordPress admin

**Does not apply if the merchant:**
- Names a different plugin platform — Magento 2, BigCommerce, Shopify, PrestaShop, or OpenCart — confirm exact platform name since plugin-update symptoms are near-identical across all of these
- Describes an enterprise headless platform (SAP, Salesforce, CommerceTools) — different integration tier

**Example:** "After updating the WooCommerce plugin, Checkout.com payment methods disappeared from our WordPress checkout."

**Likely keywords:** WooCommerce, WordPress checkout, WooCommerce plugin, WooCommerce update, WordPress payment plugin

---

### YUNO
**What it is:** Partner integration with Yuno, a Latin America-focused payment orchestration platform.
**Contact risk:** unknown — Roadmap

**Applies if the merchant:**
- Explicitly names Yuno or YUNO as their orchestration partner
- Describes Latin America-specific payment routing through Yuno

**Does not apply if the merchant:**
- Names a different orchestration vendor with no LatAm framing — BR-DGE, Gr4vy, Payrails, Spreedly, Primer.io, or IXOPay — these are not regionally scoped, so a LatAm mention points to Yuno specifically
- Describes general multi-PSP routing outside of Latin America — likely a different orchestration partner

**Example:** "Yuno is orchestrating our LatAm payment methods into Checkout.com and a route is misconfigured."

**Likely keywords:** Yuno, YUNO, Latin America orchestration, LatAm payment routing, regional orchestration partner

---

### Zingfit
**What it is:** Native integration for Zingfit, a fitness and wellness studio booking and management platform, enabling in-platform payments.
**Contact risk:** medium — plugin setup and booking-payment queries

**Applies if the merchant:**
- Explicitly names Zingfit as their studio booking/management platform
- Describes in-platform payments tied to class bookings, memberships, or studio scheduling via Zingfit

**Does not apply if the merchant:**
- Describes grocery ecommerce checkout — that's Ocado Group, a different vertical platform integration
- Describes payout/disbursement rather than in-platform booking payments — more likely Dwolla

**Example:** "Members can't complete class booking payments through Zingfit and the transaction fails at checkout."

**Likely keywords:** Zingfit, studio booking, fitness studio payments, class booking payment, wellness platform payment

---

### Zuora
**What it is:** Subscription and recurring billing platform integration.
**Contact risk:** medium — recurring billing queries

**Applies if the merchant:**
- Explicitly names Zuora as their subscription or recurring revenue management platform
- Describes recurring billing cycles, invoicing, or revenue recognition tied to Zuora

**Does not apply if the merchant:**
- Names a different subscription billing platform — Chargebee, Chargify, or Recurly — all four are functionally similar, so rely on the exact vendor name
- Describes one-off transactions with no recurring billing component

**Example:** "Our Zuora subscription billing isn't syncing successful renewal charges back from Checkout.com."

**Likely keywords:** Zuora, subscription billing, recurring revenue management, Zuora integration, renewal billing sync

---

### CommerceTools
**What it is:** Headless commerce platform integration using Checkout.com Flow for payment processing, supporting cards, wallets, BNPL, and local payment methods.
**Key capabilities:** Checkout.com Flow embedded in CommerceTools Connect; full payment lifecycle (auth, capture, void, refund); webhook-driven status sync; multi-channel config.
**Contact risk:** medium — enterprise plugin setup; Flow integration queries; multi-channel configuration

**Applies if the merchant:**
- Explicitly names CommerceTools or CommerceTools Connect as their headless commerce platform
- Describes Checkout.com Flow embedded within a CommerceTools project, covering auth/capture/void/refund lifecycle, webhook-driven status sync, or multi-channel configuration

**Does not apply if the merchant:**
- Names a different enterprise or headless platform — SAP Commerce Cloud, SAP OPF, or Salesforce Commerce Cloud — confirm exact platform name given similar enterprise complexity
- Describes Flow usage with a different platform wrapper — Ocado Group also uses Flow but is grocery-specific and card-only

**Example:** "We're using CommerceTools Connect with Checkout.com Flow and webhook status updates aren't syncing across channels."

**Likely keywords:** CommerceTools, CommerceTools Connect, headless commerce, Checkout.com Flow, webhook sync, multi-channel configuration

---

### Primer.io
**What it is:** Payment orchestration platform with a Checkout.com integration supporting cards, Apple Pay, Google Pay, and Cartes Bancaires.
**Key capabilities:** Universal Checkout; subscriptions; reconciliation reports; transparent integration; Cartes Bancaires support.
**Contact risk:** low — orchestration layer; queries mainly on Checkout.com-specific behaviour within Primer

**Applies if the merchant:**
- Explicitly names Primer or Primer.io as their orchestration platform
- Describes Universal Checkout, subscriptions, reconciliation reporting, or Cartes Bancaires support routed through Primer to Checkout.com

**Does not apply if the merchant:**
- Names a different orchestration vendor — BR-DGE, Gr4vy, Payrails, Spreedly, IXOPay, or YUNO — these serve the same orchestration function, so confirm exact vendor
- Describes reconciliation issues with no orchestration partner named — could be a direct Checkout.com reconciliation query, not a Primer-specific one

**Example:** "We route Cartes Bancaires and card payments through Primer's Universal Checkout to Checkout.com and reconciliation reports don't match."

**Likely keywords:** Primer, Primer.io, Universal Checkout, Cartes Bancaires, payment orchestration, reconciliation reporting

---

### Recurly
**What it is:** Subscription management platform integration.
**Contact risk:** medium — recurring billing queries

**Applies if the merchant:**
- Explicitly names Recurly as their subscription management platform
- Describes recurring revenue management or subscription billing cycles through Recurly

**Does not apply if the merchant:**
- Names a different subscription billing platform — Chargebee, Chargify, or Zuora — all four overlap functionally, so confirm the exact platform name
- Describes a one-off transaction with no subscription component

**Example:** "Recurly is managing our subscriptions and recurring charges to Checkout.com are failing to process."

**Likely keywords:** Recurly, subscription management, recurring revenue management, subscription billing, Recurly integration

---

### SAP OPF
**What it is:** Native Checkout.com integration for SAP Open Payment Framework.
**Contact risk:** medium — enterprise plugin setup queries

**Applies if the merchant:**
- Explicitly names SAP OPF or SAP Open Payment Framework specifically
- Reports integration or configuration issues within an SAP OPF payment setup

**Does not apply if the merchant:**
- Names SAP Commerce Cloud, SAP Hybris, or SAP B2C Accelerator instead — a distinct SAP product from SAP OPF; confirm which SAP integration is meant
- Names a different enterprise platform — Salesforce Commerce Cloud or CommerceTools — confirm exact platform

**Example:** "Our SAP Open Payment Framework setup with Checkout.com is rejecting configuration on a new payment method."

**Likely keywords:** SAP OPF, SAP Open Payment Framework, SAP payment integration, enterprise SAP setup

---

### Visualsoft
**What it is:** Native Checkout.com payment integration for Visualsoft, an ecommerce platform for retailers.
**Contact risk:** medium — plugin setup queries

**Applies if the merchant:**
- Explicitly names Visualsoft as their ecommerce platform
- Reports plugin or payment integration setup issues within a Visualsoft storefront

**Does not apply if the merchant:**
- Names a different retailer-focused ecommerce plugin — BigCommerce, Magento 2, or WooCommerce — confirm exact platform name given similar retailer use cases
- Describes an enterprise headless platform instead — SAP, Salesforce, or CommerceTools, which serve larger merchants with different setup complexity

**Example:** "Our Visualsoft storefront isn't showing the Checkout.com payment integration at checkout."

**Likely keywords:** Visualsoft, Visualsoft plugin, retailer ecommerce platform, Visualsoft checkout, Visualsoft payment integration

---

## Payment Methods

### Accel
**What it is:** US regional debit network, part of PINless debit processing.
**Geography:** United States
**Payment type:** Debit network (PINless)
**Integration notes:** Enabled via PINless Debit product.
**Contact risk:** low — well-understood, low volume of merchant queries

**Applies if the merchant:**
- References Accel by name, US PINless debit routing, or transactions routed via the Accel debit network

**Does not apply if the merchant:**
- Is asking about a different US PINless debit network (e.g. NYCE, Pulse, STAR, Discover debit routing) rather than Accel specifically — confirm which network name they used before classifying

**Example:** "One of our US debit transactions shows it routed through Accel instead of the card scheme, why?"

**Likely keywords:** Accel, PINless debit, US debit network, debit routing, regional debit network, Accel network

---

### ACH Direct Debit
**What it is:** Electronic funds transfer enabling US customers to move money between bank accounts.
**Geography:** United States
**Payment type:** Bank transfer / direct debit
**Integration notes:** Requires explicit written consent (NACHA rules); pre-notification requirements; account manager enablement needed.
**Contact risk:** high — mandate management, payment failures, NACHA compliance queries

**Applies if the merchant:**
- References ACH, US bank-to-bank transfer, NACHA rules, written consent for a bank debit, pre-notification requirements, or failed/returned bank debits in USD

**Does not apply if the merchant:**
- Is describing a UK bank debit mandate (that's Bacs) or a card-based payment method rather than a US bank account debit — ACH is specifically US bank transfer under NACHA rules

**Example:** "A customer disputed an ACH debit and says they never gave written consent, what's our exposure?"

**Likely keywords:** ACH, ACH direct debit, NACHA, US bank transfer, written consent, pre-notification, bank account debit, USD bank debit, returned ACH payment

---

### AlipayCN
**What it is:** Mobile payment service for Chinese consumers enabling one-time and recurring purchases.
**Geography:** Customers: China. Merchants: HK, Singapore, EEA, UK
**Payment type:** Wallet
**Integration notes:** Redirect flow; CNY/HKD/SGD currencies; account manager enablement needed.
**Contact risk:** medium — regional; redirect failures, currency queries

**Applies if the merchant:**
- References Alipay for mainland Chinese customers, CNY-denominated wallet payments, or Alipay redirect failures tied to a Chinese customer base

**Does not apply if the merchant:**
- Is describing Alipay for Hong Kong customers or HKD-denominated wallet transactions — that's AlipayHK, a separate product with its own redirect flow and currency set

**Example:** "Our Chinese customers are getting redirected to Alipay but the payment isn't completing, can you check?"

**Likely keywords:** Alipay, AlipayCN, mainland China wallet, CNY payment, Chinese consumer wallet, Alipay redirect, China Alipay

---

### AlipayHK
**What it is:** Mobile payment service for Hong Kong consumers enabling one-time and recurring purchases.
**Geography:** Customers: Hong Kong. Merchants: HK, Singapore, EEA, UK
**Payment type:** Wallet
**Integration notes:** Redirect flow; HKD/SGD currencies; account manager enablement needed.
**Contact risk:** medium — regional; redirect failures

**Applies if the merchant:**
- References Alipay for Hong Kong customers specifically, HKD-denominated wallet payments, or AlipayHK by name

**Does not apply if the merchant:**
- Is describing Alipay for mainland Chinese customers or CNY-denominated transactions — that's AlipayCN, a distinct product despite the shared "Alipay" branding

**Example:** "We need AlipayHK enabled for our Hong Kong storefront, is that a separate setup from regular Alipay?"

**Likely keywords:** AlipayHK, Hong Kong wallet, HKD payment, Alipay Hong Kong, HK consumer wallet

---

### Alma
**What it is:** Buy-now-pay-later solution enabling customers to pay 15 or 30 days after purchase.
**Geography:** Europe
**Payment type:** BNPL
**Integration notes:** Account manager enablement needed; webhook-driven lifecycle.
**Contact risk:** medium — BNPL dispute risk, instalment queries

**Applies if the merchant:**
- References Alma by name, pay-in-15, pay-in-30, or a deferred single-payment BNPL option in Europe

**Does not apply if the merchant:**
- Is describing instalment-based BNPL with a different provider — clarify the provider name, since "pay later" phrasing alone is shared across BNPL products in this catalogue (e.g. Klarna)

**Example:** "A customer wants to know why their Alma pay-in-30 charge hasn't gone through yet."

**Likely keywords:** Alma, pay in 15, pay in 30, deferred payment, BNPL Europe, Alma webhook, Alma lifecycle status

---

### American Express - Collecting
**What it is:** Checkout.com acquires and settles Amex transactions directly.
**Geography:** Global
**Payment type:** Card scheme
**Integration notes:** Collecting model — CKO settles; different pricing structure to Visa/MC; account manager enablement.
**Contact risk:** medium — AmEx dispute process differs from Visa/MC; pricing queries

**Applies if the merchant:**
- References Amex/American Express transactions where Checkout.com handles settlement, asks about Amex-specific pricing through Checkout.com, or raises an Amex dispute that Checkout.com is processing

**Does not apply if the merchant:**
- States that Amex settles directly with them rather than through Checkout.com — that's American Express - Gateway, where dispute and settlement handling sits with Amex, not Checkout.com

**Example:** "Our Amex settlement report from Checkout.com doesn't match what we expected, can you explain the pricing?"

**Likely keywords:** Amex, American Express, Amex collecting, Amex settlement via Checkout, Amex pricing, Amex dispute (Checkout-settled)

---

### American Express - Gateway
**What it is:** Gateway model where Amex settles directly with the merchant.
**Geography:** Global
**Payment type:** Card scheme
**Integration notes:** Gateway model — AmEx settles directly; account manager enablement.
**Contact risk:** low — AmEx handles settlement; fewer merchant-facing queries

**Applies if the merchant:**
- References Amex transactions where American Express settles directly with them (not via Checkout.com), or asks Checkout.com only about gateway/processing status, not settlement or disputes

**Does not apply if the merchant:**
- Is asking about Amex settlement timing, Amex-specific pricing from Checkout.com, or an Amex dispute Checkout.com is managing — that's American Express - Collecting, where Checkout.com is the settling party

**Example:** "Amex pays us directly, so why is a transaction showing as pending in the Checkout.com dashboard?"

**Likely keywords:** Amex gateway, American Express direct settlement, Amex processing only, gateway model Amex

---

### Apple Pay
**What it is:** Enables customers to authenticate card payments using Touch ID or Face ID without manually entering card details.
**Geography:** Global (non-EEA/UK requires account manager)
**Payment type:** Digital wallet
**Integration notes:** Requires domain registration; Apple Pay via KNET available for Kuwait; special rules for Mada outside Saudi Arabia.
**Contact risk:** low — well-understood; friction mainly at setup

**Applies if the merchant:**
- References Apple Pay, Touch ID/Face ID checkout, the Apple Pay button not appearing, or Apple Pay domain registration/verification

**Does not apply if the merchant:**
- Is asking about Google Pay setup (Android one-touch wallet, Google Pay & Wallet Console) rather than Apple's device-based wallet — the two are the closest sibling pair among global digital wallets in this list

**Example:** "The Apple Pay button isn't showing on our checkout page even though we registered our domain."

**Likely keywords:** Apple Pay, Touch ID, Face ID, Apple Pay domain registration, Apple Pay button missing, KNET Apple Pay, Mada Apple Pay

---

### Bacs
**What it is:** UK bank debit scheme for recurring and one-off payments.
**Geography:** United Kingdom
**Payment type:** Bank transfer / direct debit
**Integration notes:** Mandate required; 3-day processing cycle; account manager enablement.
**Contact risk:** high — mandate management, payment timing queries, failures

**Applies if the merchant:**
- References Bacs by name, a UK direct debit mandate, the 3-day processing cycle, or recurring UK bank account payments

**Does not apply if the merchant:**
- Is describing a US bank account debit under NACHA rules — that's ACH Direct Debit, a separate product with different consent and timing rules despite the similar "bank debit mandate" concept

**Example:** "A customer's Bacs mandate payment failed and they're asking why it takes 3 days to confirm."

**Likely keywords:** Bacs, UK direct debit, Bacs mandate, 3-day processing, recurring UK bank payment, Bacs failure

---

### Bancontact
**What it is:** Enables secure online card payments in Belgium.
**Geography:** Belgium
**Payment type:** Card-based
**Integration notes:** Redirect flow; webhook required.
**Contact risk:** low — mature, well-understood

**Applies if the merchant:**
- References Bancontact by name, Belgian card payments, or Bancontact-specific redirect/decline behaviour

**Does not apply if the merchant:**
- Is describing a generic Visa/Mastercard decline with no Belgium-specific redirect step — Bancontact's redirect flow is the distinguishing signal versus standard card processing

**Example:** "We're seeing Bancontact payments fail after the redirect step, is this a webhook issue?"

**Likely keywords:** Bancontact, Belgian card payment, Bancontact redirect, Bancontact decline, Belgium checkout

---

### Benefit Payment Gateway
**What it is:** Enables secure online payments in Bahrain via the national payment gateway.
**Geography:** Bahrain
**Payment type:** Online banking (redirect)
**Integration notes:** Redirect flow; BHD settlement; account manager enablement.
**Contact risk:** low — niche geography, low volume expected

**Applies if the merchant:**
- References the Benefit national payment gateway, Bahraini debit card redirect payments, or BHD settlement through Benefit

**Does not apply if the merchant:**
- Is describing the BenefitPay mobile app wallet rather than the gateway redirect flow — the two share the "Benefit" brand but are distinct products with different integration models

**Example:** "Our Bahraini customers pay through the Benefit gateway but we're not seeing BHD settlement land correctly."

**Likely keywords:** Benefit, Benefit gateway, Bahrain national payment gateway, BHD settlement, Bahraini debit card, Benefit redirect

---

### BenefitPay
**What it is:** App-based payment allowing Bahraini users to pay and transfer funds via smartphone.
**Geography:** Bahrain
**Payment type:** Digital wallet
**Integration notes:** Account manager enablement.
**Contact risk:** low — niche geography, low volume expected

**Applies if the merchant:**
- References the BenefitPay mobile app, Bahraini smartphone wallet payments, or fund transfers via the BenefitPay app

**Does not apply if the merchant:**
- Is describing the Benefit Payment Gateway redirect flow (national online banking gateway) rather than the app-based wallet — confirm which "Benefit" product before classifying

**Example:** "A customer paid via the BenefitPay app but the transaction isn't showing in our dashboard."

**Likely keywords:** BenefitPay, Bahrain mobile wallet, BenefitPay app, Bahraini smartphone payment, BenefitPay transfer

---

### Bizum
**What it is:** Instant bank transfer payment using a phone number, popular in Spain.
**Geography:** Spain
**Payment type:** Bank transfer
**Integration notes:** Redirect flow; account manager enablement.
**Contact risk:** medium — bank transfer failures, phone number lookup issues

**Applies if the merchant:**
- References Bizum by name, Spanish phone-number-based bank transfer, or Bizum-specific redirect/lookup failures

**Does not apply if the merchant:**
- Is describing a Spanish card payment or a different European bank-redirect method (e.g. iDEAL in the Netherlands) rather than Bizum's phone-number-linked transfer

**Example:** "A customer's Bizum payment failed because the phone number lookup didn't match their bank account."

**Likely keywords:** Bizum, Spanish instant transfer, phone number payment, Bizum redirect, Bizum lookup failure

---

### BLIK
**What it is:** Real-time mobile payment method in Poland using a 6-digit code.
**Geography:** Poland
**Payment type:** Bank transfer
**Integration notes:** Roadmap status; no live doc yet.
**Contact risk:** unknown

**Applies if the merchant:**
- References BLIK by name, a Polish mobile payment code, or the 6-digit BLIK code flow

**Does not apply if the merchant:**
- Is asking about a live, currently-supported Polish payment method — BLIK is roadmap status with no live documentation, so treat any live-transaction complaint as likely misclassified

**Example:** "Do you support BLIK for our Polish customers yet, or is it still on the roadmap?"

**Likely keywords:** BLIK, Polish mobile payment, 6-digit code, Poland roadmap payment method

---

### Boleto Bancario
**What it is:** Cash voucher payment method in Brazil.
**Geography:** Brazil
**Payment type:** Voucher
**Integration notes:** Deprecated — no longer supported.
**Contact risk:** n/a — deprecated

**Applies if the merchant:**
- References Boleto or Boleto Bancário by name, or asks why a Brazilian cash voucher payment option is no longer available

**Does not apply if the merchant:**
- Is asking about a currently supported Brazilian payment method rather than the deprecated voucher — Boleto is no longer live, so redirect any active-payment-flow question elsewhere

**Example:** "Why can't we offer Boleto to our Brazilian customers anymore?"

**Likely keywords:** Boleto, Boleto Bancario, Brazilian cash voucher, deprecated Brazil payment, Boleto deprecation

---

### Cartes Bancaires
**What it is:** France's predominant card scheme, typically co-branded with Visa or Mastercard.
**Geography:** France
**Payment type:** Card scheme
**Integration notes:** Auto-retry on Visa/MC if CB declines technically (opt-out available).
**Contact risk:** medium — co-brand routing queries, retry logic

**Applies if the merchant:**
- References Cartes Bancaires or "CB" by name, French domestic card routing, co-branded Visa/CB or Mastercard/CB cards, or auto-retry behaviour after a CB decline

**Does not apply if the merchant:**
- Is asking about a plain Visa or Mastercard decline with no French co-brand or auto-retry context — CB is specifically the French co-branded domestic scheme, not a standalone international scheme

**Example:** "A French customer's card declined on Cartes Bancaires but the auto-retry to Visa also failed, what happened?"

**Likely keywords:** Cartes Bancaires, CB, French card scheme, co-branded card, CB auto-retry, French domestic routing, CB opt-out

---

### Cash App
**What it is:** US digital wallet and P2P app for instant bank-linked payments.
**Geography:** United States (Roadmap)
**Payment type:** Digital wallet
**Integration notes:** Roadmap — not yet live.
**Contact risk:** unknown — Roadmap

**Applies if the merchant:**
- References Cash App by name or asks about US P2P wallet payment support that is not yet live

**Does not apply if the merchant:**
- Is asking about a currently live US digital wallet (e.g. Apple Pay, Google Pay) rather than the not-yet-launched Cash App — flag the roadmap status rather than treating it as a live product issue

**Example:** "Can we accept Cash App payments yet, or is that still coming?"

**Likely keywords:** Cash App, US P2P wallet, Cash App roadmap, not yet live wallet US

---

### DANA
**What it is:** Mobile payment service for Indonesian consumers enabling one-time and recurring purchases.
**Geography:** Customers: Indonesia. Merchants: HK, Singapore, EEA, UK
**Payment type:** Wallet
**Integration notes:** Flow only; redirect; account manager enablement.
**Contact risk:** medium — regional; redirect failures

**Applies if the merchant:**
- References DANA by name, Indonesian mobile wallet payments, or redirect failures tied to Indonesian customers

**Does not apply if the merchant:**
- Is describing a different Southeast/East Asian regional wallet with a similar one-time/recurring redirect pattern — confirm the country and wallet name (e.g. GCash for the Philippines, KakaoPay for Korea) since these wallets share nearly identical integration patterns in this catalogue

**Example:** "Our Indonesian customers using DANA are getting stuck after the redirect, can you check the flow?"

**Likely keywords:** DANA, Indonesian wallet, DANA redirect, Indonesia mobile payment, DANA Flow

---

### Diners Club International
**What it is:** Global credit card scheme accepted alongside Mastercard.
**Geography:** Global
**Payment type:** Card scheme
**Integration notes:** Standard card processing.
**Contact risk:** low

**Applies if the merchant:**
- References Diners Club by name, Diners card acceptance, or Diners-specific declines

**Does not apply if the merchant:**
- Is asking about a generic Mastercard decline with no Diners branding mentioned — Diners Club rides on Mastercard's network but should only be classified here when the merchant names Diners specifically

**Example:** "A customer says their Diners Club card was declined, is that a scheme we support?"

**Likely keywords:** Diners Club, Diners Club International, Diners card acceptance, Diners decline

---

### Discover
**What it is:** Global credit card scheme, especially strong in US.
**Geography:** Global
**Payment type:** Card scheme
**Integration notes:** Standard card processing; part of PINless debit US debit network.
**Contact risk:** low

**Applies if the merchant:**
- References Discover card acceptance, Discover-specific declines, or PINless debit routing via the Discover network

**Does not apply if the merchant:**
- Is describing PINless debit routing via Accel specifically rather than Discover's own debit network — both are US PINless debit networks in this list, so confirm the exact network name before classifying

**Example:** "Why did this transaction route through Discover's PINless debit network instead of the card's primary scheme?"

**Likely keywords:** Discover, Discover card, Discover decline, Discover PINless debit, US Discover network

---

### EFTPOS
**What it is:** Australian domestic debit card scheme.
**Geography:** Australia (Roadmap)
**Payment type:** Card scheme
**Integration notes:** Roadmap — not yet live.
**Contact risk:** unknown

**Applies if the merchant:**
- References EFTPOS by name or asks about Australian domestic debit card support that isn't yet live

**Does not apply if the merchant:**
- Is asking about a live Australian card scheme transaction rather than the not-yet-launched EFTPOS product — flag as roadmap rather than an active-payment issue

**Example:** "When will EFTPOS be available for our Australian customers?"

**Likely keywords:** EFTPOS, Australian domestic debit, EFTPOS roadmap, Australia card scheme not live

---

### eps
**What it is:** Enables online purchases through secure bank transfers in Austria.
**Geography:** Austria
**Payment type:** Online banking
**Integration notes:** Flow only; redirect; account manager enablement; refunds via API only (not Dashboard).
**Contact risk:** medium — refund process friction

**Applies if the merchant:**
- References eps by name, Austrian online banking payments, or asks why an eps refund isn't available in the Dashboard

**Does not apply if the merchant:**
- Is trying to refund via the Dashboard and expecting it to work like other redirect methods — eps refunds are API-only, which is the key disambiguator versus other online banking products that support Dashboard refunds

**Example:** "I'm trying to refund an eps payment from the Dashboard but the option isn't there."

**Likely keywords:** eps, Austrian online banking, eps refund, API-only refund, eps redirect, Austria bank transfer

---

### Fawry
**What it is:** Egyptian cash payment and digital payments network.
**Geography:** Egypt
**Payment type:** Cash/voucher
**Integration notes:** Don't sell status — not actively sold.
**Contact risk:** n/a

**Applies if the merchant:**
- References Fawry by name or Egyptian cash payment network options

**Does not apply if the merchant:**
- Is asking to actively enable or sell Fawry as a new payment method — it carries "don't sell" status, so route to account management rather than treating as a standard enablement request

**Example:** "Can we get Fawry set up for our Egyptian customers?"

**Likely keywords:** Fawry, Egyptian cash payment, Fawry network, don't sell status Egypt

---

### GCash
**What it is:** Mobile payment service for Filipino consumers enabling one-time and recurring purchases.
**Geography:** Customers: Philippines. Merchants: HK, Singapore, EEA, UK
**Payment type:** Wallet
**Integration notes:** Flow or API; redirect; auto-capture only; account manager enablement.
**Contact risk:** medium — regional; redirect failures

**Applies if the merchant:**
- References GCash by name, Filipino mobile wallet payments, GCash redirect failures, or auto-capture-only behaviour for Philippine customers

**Does not apply if the merchant:**
- Is describing a different Southeast/East Asian wallet with the same one-time/recurring redirect pattern (e.g. DANA for Indonesia, KakaoPay for Korea) — confirm the country and wallet name, since these regional wallets are easily confused

**Example:** "GCash payments from our Filipino customers keep failing after redirect, and we can't do partial captures."

**Likely keywords:** GCash, Filipino wallet, GCash redirect, Philippines mobile payment, GCash auto-capture

---

### Google Pay
**What it is:** Enables one-touch payments on website or Android app using cards connected to a Google account.
**Geography:** Global (UAE/SA require account manager approval)
**Payment type:** Digital wallet
**Integration notes:** Requires Google Pay & Wallet Console registration, domain allowlisting, and public key configuration.
**Contact risk:** low — well-understood; friction mainly at setup

**Applies if the merchant:**
- References Google Pay, one-touch Android payments, the Google Pay & Wallet Console, domain allowlisting, or the Google Pay button not appearing

**Does not apply if the merchant:**
- Is asking about Apple Pay's Touch ID/Face ID flow or domain registration rather than Google's Wallet Console and allowlisting setup — the two wallets have parallel but distinct setup steps and should not be conflated

**Example:** "We registered our domain in the Google Pay & Wallet Console but the button still isn't showing on checkout."

**Likely keywords:** Google Pay, one-touch payment, Google Pay Wallet Console, domain allowlisting, Google Pay button missing, Android wallet, UAE Google Pay approval

---

### iDEAL
**What it is:** Direct online bank transfer from customer's bank account to merchant's bank account.
**Geography:** Netherlands
**Payment type:** Bank transfer (online banking)
**Integration notes:** Auto-capture only; webhook required; account manager enablement.
**Contact risk:** medium — bank transfer failures, payment status queries

**Applies if the merchant:**
- References iDEAL by name, Dutch bank transfer payments, Dutch online banking redirects, or iDEAL payment status enquiries

**Does not apply if the merchant:**
- Is describing a different European bank-redirect method with a similar auto-capture pattern (e.g. eps for Austria, Bizum for Spain) — confirm the country and product name before classifying under iDEAL

**Example:** "A Dutch customer paid via iDEAL but the order still shows as pending, can you check the webhook?"

**Likely keywords:** iDEAL, Dutch bank transfer, Netherlands online banking, iDEAL auto-capture, iDEAL webhook, iDEAL payment status

---

### Jaywan
**What it is:** Emerging GCC domestic debit card scheme.
**Geography:** UAE/GCC (Roadmap)
**Payment type:** Card scheme
**Integration notes:** Roadmap — not yet live.
**Contact risk:** unknown

**Applies if the merchant:**
- References Jaywan by name or asks about GCC domestic debit card support that isn't yet live

**Does not apply if the merchant:**
- Is asking about a live GCC card scheme or a different domestic debit brand (e.g. Mada, referenced under Apple Pay's special rules) rather than the not-yet-launched Jaywan — flag as roadmap

**Example:** "Is Jaywan support coming for our UAE customers, or still on the roadmap?"

**Likely keywords:** Jaywan, GCC domestic debit, UAE card scheme roadmap, emerging GCC scheme

---

### JCB
**What it is:** Japanese card scheme accepted globally, especially in Asia.
**Geography:** Asia, global
**Payment type:** Card scheme
**Integration notes:** Mixed availability; processed via CP Berlin team.
**Contact risk:** low

**Applies if the merchant:**
- References JCB by name, Japanese card scheme acceptance, or asks about JCB processing via the CP Berlin team

**Does not apply if the merchant:**
- Is asking about general card acceptance in Asia without naming JCB specifically — mixed availability means the merchant should confirm JCB is enabled for their region before assuming coverage

**Example:** "Is JCB acceptance live in our region, or does that depend on the CP Berlin team enabling it?"

**Likely keywords:** JCB, Japanese card scheme, JCB availability, CP Berlin processing, JCB Asia

---

### KakaoPay
**What it is:** Mobile payment service for Korean consumers enabling one-time and recurring purchases.
**Geography:** Customers: Korea. Merchants: HK, Singapore, EEA, UK
**Payment type:** Wallet
**Integration notes:** Flow or API; redirect; auto-capture only; KRW/HKD/SGD.
**Contact risk:** medium — regional

**Applies if the merchant:**
- References KakaoPay or KakaoTalk payment by name, Korean digital wallet payments, or KRW-denominated wallet transactions

**Does not apply if the merchant:**
- Is describing a different regional wallet with the same one-time/recurring auto-capture pattern (e.g. GCash for the Philippines, DANA for Indonesia) — confirm the country and wallet name, since these regional wallets follow near-identical integration patterns

**Example:** "Our Korean customers pay via KakaoPay but we're seeing failures on the auto-capture step."

**Likely keywords:** KakaoPay, KakaoTalk payment, Korean wallet, KRW payment, Korea digital wallet

---

### Klarna (Gateway)
**What it is:** Gateway model for Klarna — not actively sold.
**Geography:** —
**Payment type:** BNPL
**Integration notes:** Don't sell status.
**Contact risk:** n/a

**Applies if the merchant:**
- References Klarna in a gateway/direct-settlement model rather than Checkout.com collecting on their behalf, and is asking about this specifically

**Does not apply if the merchant:**
- Is asking about Klarna's collecting BNPL product (pay later, pay in instalments, Klarna Merchant Portal) — that's Klarna BNPL (Collecting), the actively sold product; Klarna (Gateway) carries "don't sell" status and should only be classified here if the merchant explicitly asks about the gateway model. Also distinct from Klarna Crypto (beta crypto option) and Klarna Debit Risk (Collecting) (bank transfer for restricted segments)

**Example:** "Can we use Klarna in a gateway setup where Klarna settles directly, rather than through Checkout.com?"

**Likely keywords:** Klarna gateway, Klarna direct settlement, Klarna don't sell, Klarna gateway model

---

### Klarna BNPL (Collecting)
**What it is:** Flexible payment options: pay now, pay later, or pay in instalments.
**Geography:** Europe, US, AU + others
**Payment type:** BNPL
**Integration notes:** Requires Klarna Merchant Portal registration; webhook-driven; dispute notifications in Klarna portal.
**Contact risk:** high — BNPL dispute-prone, instalment queries, high-risk order monitoring

**Applies if the merchant:**
- References Klarna BNPL, pay later, pay in instalments, the Klarna Merchant Portal, or Klarna dispute notifications

**Does not apply if the merchant:**
- Is asking about Klarna's gateway (direct-settlement, not sold) model — that's Klarna (Gateway); about Klarna's crypto option — that's Klarna Crypto; or about Klarna's bank-transfer product for restricted/high-risk segments — that's Klarna Debit Risk (Collecting), which is API-only with no disputes support, unlike this product

**Example:** "A customer disputed a Klarna instalment charge and it's showing in the Klarna Merchant Portal, how do we respond?"

**Likely keywords:** Klarna BNPL, pay later, pay in instalments, Klarna Merchant Portal, Klarna dispute, Klarna webhook, Klarna collecting

---

### Klarna Crypto
**What it is:** Klarna's crypto payment option.
**Geography:** —
**Payment type:** BNPL / Crypto
**Integration notes:** Beta.
**Contact risk:** unknown

**Applies if the merchant:**
- References Klarna crypto payments, paying via crypto through Klarna, or the Klarna Crypto beta

**Does not apply if the merchant:**
- Is asking about standard Klarna BNPL (pay later/instalments) or Klarna's bank-transfer product for restricted segments — Klarna Crypto is specifically the beta crypto payment rail, not a fiat instalment or bank-debit option

**Example:** "Is Klarna's crypto payment option available for our checkout yet, or still in beta?"

**Likely keywords:** Klarna crypto, crypto via Klarna, Klarna Crypto beta, Klarna cryptocurrency payment

---

### Klarna Debit Risk (Collecting)
**What it is:** Klarna's bank transfer option for restricted/high-risk merchant segments.
**Geography:** AT, BE, FI, DE, NL, ES, SE
**Payment type:** Pay-by-bank
**Integration notes:** API-only (no hosted UI); auto-capture; no disputes or void; Beta.
**Contact risk:** medium — niche; eligibility queries

**Applies if the merchant:**
- References Klarna bank transfer for a restricted or high-risk merchant segment, Klarna Debit Risk by name, or Klarna-branded A2A payments in AT/BE/FI/DE/NL/ES/SE

**Does not apply if the merchant:**
- Is asking about standard Klarna BNPL (pay later/instalments, hosted UI, disputes supported via the Klarna Merchant Portal) — that's Klarna BNPL (Collecting); Klarna Debit Risk is API-only, auto-capture, and explicitly has no disputes or void functionality, which is the key disambiguator

**Example:** "Can we void a Klarna Debit Risk transaction? A customer wants to cancel before it settles."

**Likely keywords:** Klarna Debit Risk, Klarna bank transfer, Klarna A2A, restricted segment Klarna, Klarna pay-by-bank, API-only Klarna, Klarna beta no disputes

---

### Knet
**What it is:** Enables purchases with local Kuwaiti debit cards issued by member banks.
**Geography:** Kuwait
**Payment type:** Debit card (domestic)
**Integration notes:** Redirect; auto-capture; account manager enablement.
**Contact risk:** low

**Applies if the merchant:**
- References KNET, Kuwaiti debit cards, or Kuwait-issued bank cards specifically

**Does not apply if the merchant:**
- Is asking about a Gulf domestic scheme other than Kuwait's (e.g. Mada for Saudi Arabia, Omannet for Oman) — route to that country's specific product instead

**Example:** "Our Kuwaiti customers say their KNET payment failed at checkout."

**Likely keywords:** KNET, K-Net, Kuwaiti debit card, Kuwait payment failure, Kuwait domestic card, member bank Kuwait

---

### Mada
**What it is:** Saudi Arabia's domestic payment network, co-branded internationally with Visa/Mastercard.
**Geography:** Saudi Arabia (also international co-branded)
**Payment type:** Debit card (domestic + Visa/MC)
**Integration notes:** Full capture only (no partial); 3DS recommended; BIN list maintenance required.
**Contact risk:** medium — capture restriction queries, Apple Pay routing rules

**Applies if the merchant:**
- References Mada, Saudi domestic debit cards, or a dual-branded Mada/Visa or Mada/Mastercard card
- Asks about full-capture-only restrictions or Apple Pay routing specific to Mada BINs

**Does not apply if the merchant:**
- Is asking about the underlying international scheme rules (Visa or Mastercard) rather than the Mada-specific domestic routing or capture restriction — route to Visa or Mastercard
- Is asking about a different Gulf domestic network (e.g. Omannet, STC Pay) — route to that product

**Example:** "We can't do a partial capture on a Mada transaction, is that expected?"

**Likely keywords:** Mada, Saudi domestic card, Mada decline, partial capture Mada, Mada Apple Pay, Mada BIN, Mada 3DS

---

### Maestro
**What it is:** Mastercard's international debit card scheme (Pilot status).
**Geography:** Global
**Payment type:** Card scheme
**Integration notes:** Pilot.
**Contact risk:** unknown

**Applies if the merchant:**
- References Maestro specifically, a Maestro-branded debit card, or a dual-branded Visa/Maestro or Mastercard/Maestro card being processed under Maestro rules

**Does not apply if the merchant:**
- Is asking about standard Mastercard credit/debit acceptance or scheme rules — route to Mastercard
- Is asking about Visa debit routing on a dual-branded card — route to Visa

**Example:** "Is Maestro fully supported yet, or still in pilot for our account?"

**Likely keywords:** Maestro, Maestro debit, Mastercard Maestro, dual-branded Visa Maestro, Maestro pilot, Maestro availability

---

### Mastercard
**What it is:** Leading global card scheme for credit and debit payments.
**Geography:** Global
**Payment type:** Card scheme
**Integration notes:** Mixed availability; multiple processing teams.
**Contact risk:** low

**Applies if the merchant:**
- References Mastercard specifically, Mastercard-branded card declines, or Mastercard scheme rules/fees

**Does not apply if the merchant:**
- Is asking about a competing global scheme (Visa, UnionPay) — route to that scheme
- Is asking about Mastercard's debit-only sibling scheme, Maestro — route to Maestro

**Example:** "We're seeing a spike in Mastercard declines this week, can you check scheme-side?"

**Likely keywords:** Mastercard, Mastercard decline, Mastercard scheme rules, Mastercard processing, Mastercard acceptance, Mastercard fees

---

### MB WAY
**What it is:** Portugal's most popular digital wallet, enabling fast PIN-authenticated payments online.
**Geography:** Portugal
**Payment type:** Digital wallet
**Integration notes:** Flow only; redirect; account manager enablement.
**Contact risk:** low

**Applies if the merchant:**
- References MB WAY, MB Way, or PIN-authenticated Portuguese wallet payments

**Does not apply if the merchant:**
- Is asking about the Portuguese ATM/voucher payment method instead — route to Multibanco

**Example:** "A customer's MB WAY payment isn't completing after they enter their PIN."

**Likely keywords:** MB WAY, MB Way, Portuguese wallet, PIN authentication Portugal, MB WAY payment failure

---

### MobilePay
**What it is:** Leading Nordic mobile wallet for instant payments via smartphone.
**Geography:** Denmark, Finland
**Payment type:** Wallet
**Integration notes:** Manual or auto-capture; Flow or API; account manager enablement.
**Contact risk:** low

**Applies if the merchant:**
- References MobilePay, Danish or Finnish mobile wallet payments

**Does not apply if the merchant:**
- Is asking about a different Nordic mobile wallet (e.g. Vipps for Norway/Sweden, Swish for Sweden) — route to that product

**Example:** "Our Danish customers pay via MobilePay, can we enable auto-capture?"

**Likely keywords:** MobilePay, Danish mobile wallet, Finnish mobile wallet, Nordic wallet, MobilePay capture

---

### Multibanco
**What it is:** Enables cash or debit payments at ATMs or via banking app across Portugal.
**Geography:** Portugal
**Payment type:** Voucher
**Integration notes:** Redirect; webhook required; account manager enablement.
**Contact risk:** medium — voucher expiry queries, async payment status

**Applies if the merchant:**
- References Multibanco, Portuguese ATM/voucher payments, or voucher expiry and async payment status issues

**Does not apply if the merchant:**
- Is asking about Portugal's PIN-based wallet instead — route to MB WAY

**Example:** "Our customer paid via Multibanco at an ATM but the order hasn't updated to paid."

**Likely keywords:** Multibanco, Portuguese ATM payment, Multibanco voucher, voucher expiry, async payment status, Multibanco webhook

---

### NYCE
**What it is:** US regional debit network, part of PINless debit processing.
**Geography:** United States
**Payment type:** Debit network (PINless)
**Integration notes:** Enabled via PINless Debit product.
**Contact risk:** low

**Applies if the merchant:**
- References NYCE specifically or asks which PINless debit network routed a US transaction

**Does not apply if the merchant:**
- Cannot actually distinguish NYCE from Pulse or STAR from a merchant-facing standpoint — these three are functionally identical PINless debit networks differing only in which network routed the transaction; if the merchant's query is really about PINless debit in general (not the specific network), classify under the general PINless Debit product rather than NYCE specifically

**Example:** "Our settlement report shows a transaction routed via NYCE, what does that mean for fees?"

**Likely keywords:** NYCE, PINless debit, US debit network routing, NYCE network, regional debit network

---

### Octopus
**What it is:** Contactless card and digital wallet payments in Hong Kong.
**Geography:** Hong Kong
**Payment type:** Digital wallet
**Integration notes:** Beta; Flow or API; account manager enablement.
**Contact risk:** unknown — Beta

**Applies if the merchant:**
- References Octopus, Octopus card, or Hong Kong contactless wallet payments

**Does not apply if the merchant:**
- Is asking about a different Hong Kong or China wallet (e.g. WeChat Pay HK) — route to that product

**Example:** "Can we accept Octopus card payments yet, or is it still in beta?"

**Likely keywords:** Octopus, Octopus card, Hong Kong contactless payment, Octopus wallet beta

---

### Omannet
**What it is:** Domestic payment network in Oman for online debit card payments.
**Geography:** Oman
**Payment type:** Debit card (domestic)
**Integration notes:** API-only; OTP authentication may apply.
**Contact risk:** medium — OTP/auth friction

**Applies if the merchant:**
- References Omannet, OmanNET, or Omani domestic debit cards, including OTP authentication friction

**Does not apply if the merchant:**
- Is asking about a different Gulf domestic network (e.g. Mada, Knet, STC Pay) — route to that country's specific product

**Example:** "Customers in Oman say they're not receiving the OTP to complete an Omannet payment."

**Likely keywords:** Omannet, OmanNET, Omani domestic debit, Oman national payment network, Omannet OTP, Oman authentication

---

### PayNow
**What it is:** Real-time payment service in Singapore enabling fund transfers via mobile number.
**Geography:** Singapore
**Payment type:** Digital wallet (real-time transfer)
**Integration notes:** Auto-capture only; no chargebacks or recurring; account manager enablement.
**Contact risk:** low

**Applies if the merchant:**
- References PayNow, Singapore real-time transfers, QR payments in SGD, or mobile-number-based payments

**Does not apply if the merchant:**
- Is asking about setting up a recurring or subscription payment via PayNow — this is out of scope since PayNow doesn't support recurring; clarify they need a different method for recurring Singapore payments
- Is asking about chargeback/dispute handling on a PayNow transaction — PayNow doesn't support chargebacks, so this indicates confusion with a card-based method

**Example:** "Can a customer set up a recurring PayNow payment for their subscription?"

**Likely keywords:** PayNow, Singapore real-time payment, SGD QR payment, mobile number transfer Singapore, PayNow auto-capture, no PayNow recurring

---

### PayPal
**What it is:** Enables payments using credit/debit cards connected to a PayPal account, with Pay Now, Continue, and Pay Later options.
**Geography:** Global (Pay Later: AU, FR, DE, IT, ES, US)
**Payment type:** Digital wallet
**Integration notes:** Digital goods require explicit PayPal agreement; Seller Protection requires full name/address.
**Contact risk:** medium — PayPal dispute process differs from card disputes; Pay Later queries

**Applies if the merchant:**
- References PayPal, PayPal wallet checkout, PayPal Pay Later/Pay in installments, PayPal Seller Protection, or the PayPal-specific dispute process

**Does not apply if the merchant:**
- Is asking about a regional BNPL provider instead (e.g. SeQura, Tabby, Tamara, Zip) — route to that specific BNPL product rather than PayPal's Pay Later
- Is asking about standard card scheme dispute rules (Visa/Mastercard chargebacks) rather than PayPal's own resolution process — clarify which applies

**Example:** "A customer disputed a PayPal transaction, does that follow the same process as a card chargeback?"

**Likely keywords:** PayPal, PayPal wallet, PayPal Pay Later, PayPal Seller Protection, PayPal dispute, PayPal Pay Now, PayPal digital goods agreement

---

### PayPay
**What it is:** Leading mobile wallet in Japan with 68M+ users, using QR-based payments with wide online reach.
**Geography:** Japan (Roadmap)
**Payment type:** Digital wallet
**Integration notes:** Roadmap — not yet live.
**Contact risk:** unknown — Roadmap

**Applies if the merchant:**
- References PayPay, Japanese QR wallet, or asks about accepting PayPay before general availability

**Does not apply if the merchant:**
- Is asking about a different Asia-Pacific QR wallet already live (e.g. WeChat Pay CN/HK, Octopus) — route to that product instead of the not-yet-live PayPay

**Example:** "When will PayPay be available for us to accept in Japan?"

**Likely keywords:** PayPay, Japanese QR wallet, Japan mobile payment, PayPay roadmap, PayPay availability

---

### Pix
**What it is:** Brazil's instant payment system operated by the central bank.
**Geography:** Brazil (Roadmap)
**Payment type:** Bank transfer (instant)
**Integration notes:** Roadmap — not yet live.
**Contact risk:** unknown

**Applies if the merchant:**
- References Pix, Brazilian instant payments, or Brazil central bank transfer scheme, including timeline questions before general availability

**Does not apply if the merchant:**
- Is asking about a different instant bank transfer method in another region (e.g. Swish, MobilePay) — route to that region's product

**Example:** "Do you have a timeline for when Pix will be supported for our Brazilian customers?"

**Likely keywords:** Pix, Brazilian instant payment, Brazil central bank transfer, Pix roadmap, Pix availability

---

### Przelewy24
**What it is:** Enables secure online payments in Poland via redirect.
**Geography:** Poland
**Payment type:** Online banking
**Integration notes:** Redirect; webhook; account manager enablement; various response codes to handle.
**Contact risk:** medium — redirect/bank transfer failures

**Applies if the merchant:**
- References Przelewy24, P24, Polish online banking, or redirect/response-code failures on a Polish bank transfer

**Does not apply if the merchant:**
- Is asking about a different European online banking redirect method (e.g. the deprecated Sofort) — route to that product

**Example:** "We're getting an unfamiliar response code back from Przelewy24, what does it mean?"

**Likely keywords:** Przelewy24, P24, Polish online banking, Poland bank redirect, Przelewy24 response code, Przelewy24 webhook

---

### Pulse
**What it is:** US regional debit network, part of PINless debit processing.
**Geography:** United States
**Payment type:** Debit network (PINless)
**Integration notes:** Enabled via PINless Debit product.
**Contact risk:** low

**Applies if the merchant:**
- References Pulse specifically or asks which PINless debit network (Pulse, part of the Discover family) routed a US transaction

**Does not apply if the merchant:**
- Cannot actually distinguish Pulse from NYCE or STAR from a merchant-facing standpoint — these three are functionally identical PINless debit networks differing only in which network routed the transaction; if the query is about PINless debit generally rather than the Pulse network specifically, classify under the general PINless Debit product

**Example:** "I see a transaction routed via Pulse in the settlement file, is that normal?"

**Likely keywords:** Pulse, PINless debit, Discover Pulse network, US debit network routing, Pulse settlement

---

### QPay
**What it is:** Enables secure online payments in Qatar via bank transfer gateway.
**Geography:** Qatar
**Payment type:** Online banking
**Integration notes:** No auto-capture, auth, or recurring; refunds only; account manager enablement.
**Contact risk:** low — limited capabilities reduce query surface

**Applies if the merchant:**
- References QPay, Qatari bank transfer gateway, or asks about the lack of auth/auto-capture/recurring support

**Does not apply if the merchant:**
- Is asking to set up a recurring QPay payment or authorize-only flow — this is out of scope since QPay only supports refunds with no auth/recurring; clarify limitation rather than misclassify as a bug

**Example:** "Can we set up a recurring subscription charge through QPay?"

**Likely keywords:** QPay, Qatar bank transfer, Qatar payment gateway, QPay refund only, QPay no recurring, Qatar payment failure

---

### Samsung Pay
**What it is:** Samsung's mobile payment wallet.
**Geography:** Global (Roadmap)
**Payment type:** Digital wallet
**Integration notes:** Roadmap — not yet live.
**Contact risk:** unknown

**Applies if the merchant:**
- References Samsung Pay, Samsung wallet, or Samsung contactless payments, including questions about future availability

**Does not apply if the merchant:**
- Is asking about a different mobile wallet already live (e.g. Twint, Octopus, MobilePay) — route to that product instead of the not-yet-live Samsung Pay

**Example:** "Is Samsung Pay on the roadmap, and when might it launch?"

**Likely keywords:** Samsung Pay, Samsung wallet, Samsung contactless, Samsung Pay roadmap, Samsung Pay availability

---

### SEPA Direct Debit B2B
**What it is:** SEPA direct debit variant for business-to-business transactions.
**Geography:** SEPA region (EU)
**Payment type:** Direct debit (B2B)
**Integration notes:** Same mandate requirements as Core but B2B only; Beta.
**Contact risk:** high — same as Core; B2B adds complexity

**Applies if the merchant:**
- References SEPA Direct Debit B2B, SDD B2B, or a business-to-business SEPA mandate specifically, or is in Beta and asking about B2B-only eligibility

**Does not apply if the merchant:**
- Is collecting from consumer bank accounts rather than business accounts — route to SEPA Direct Debit Core, which uses the same mandate mechanics but for B2C

**Example:** "We need to set up a SEPA mandate for a business customer, does that go through B2B or Core?"

**Likely keywords:** SEPA Direct Debit B2B, SDD B2B, business-to-business SEPA, SEPA B2B mandate, SEPA B2B beta

---

### SEPA Direct Debit Core
**What it is:** Standard SEPA direct debit for consumer bank accounts across the EU.
**Geography:** SEPA region (EU)
**Payment type:** Direct debit (B2C)
**Integration notes:** Mandate required with 14-day pre-notification; IBAN/BIC collection; creditor ID needed.
**Contact risk:** high — mandate management, payment failures, pre-notification queries

**Applies if the merchant:**
- References SEPA Direct Debit, SDD, SEPA mandate, IBAN/BIC collection, creditor ID setup, or the 14-day pre-notification requirement for consumer customers

**Does not apply if the merchant:**
- Is collecting from a business account under a B2B-only mandate — route to SEPA Direct Debit B2B

**Example:** "A customer's SEPA mandate failed, do we need to resend the pre-notification before retrying?"

**Likely keywords:** SEPA Direct Debit, SDD, SEPA mandate, pre-notification, IBAN, BIC, creditor ID, EU recurring debit

---

### SeQura
**What it is:** Instalment payment plans popular in Spain.
**Geography:** Spain
**Payment type:** BNPL
**Integration notes:** Redirect; API only; manual or auto capture; account manager enablement.
**Contact risk:** medium — BNPL instalment queries

**Applies if the merchant:**
- References SeQura, Spanish/Iberian instalment payments, or instalment payments in Spain, Portugal, or Italy

**Does not apply if the merchant:**
- Is asking about a Gulf-region BNPL provider (Tabby, Tamara) or a different-region BNPL provider (Zip) — route to that product instead

**Example:** "A customer wants to split their purchase into instalments via SeQura, how does capture work?"

**Likely keywords:** SeQura, Spanish BNPL, Iberian instalments, SeQura Spain Portugal Italy, SeQura capture

---

### Sofort
**What it is:** Sofort online banking payment (deprecated).
**Geography:** Europe
**Payment type:** Online banking
**Integration notes:** Deprecated — no longer supported.
**Contact risk:** n/a — deprecated

**Applies if the merchant:**
- References Sofort or Klarna Sofort and is asking why it no longer works or what to migrate to

**Does not apply if the merchant:**
- Is asking about a currently supported European online banking redirect method — route to Przelewy24 (Poland) as the active equivalent, or clarify their country to find the live alternative

**Example:** "Our Sofort integration stopped working, is it deprecated?"

**Likely keywords:** Sofort, Klarna Sofort, Sofort deprecated, Sofort no longer supported, Sofort migration

---

### STAR
**What it is:** US regional debit network, part of PINless debit processing.
**Geography:** United States
**Payment type:** Debit network (PINless)
**Integration notes:** Enabled via PINless Debit product.
**Contact risk:** low

**Applies if the merchant:**
- References STAR specifically or asks which PINless debit network routed a US transaction

**Does not apply if the merchant:**
- Cannot actually distinguish STAR from NYCE or Pulse from a merchant-facing standpoint — these three are functionally identical PINless debit networks differing only in which network routed the transaction; if the query is about PINless debit generally, classify under the general PINless Debit product rather than STAR specifically

**Example:** "Why does our settlement report show some debit transactions routed through STAR?"

**Likely keywords:** STAR, PINless debit, STAR network routing, US debit network, STAR settlement

---

### STC Pay
**What it is:** Digital wallet enabling fund transfers and ecommerce payments in Saudi Arabia.
**Geography:** Saudi Arabia
**Payment type:** Digital wallet
**Integration notes:** Flow or API; auto-capture; account manager enablement.
**Contact risk:** low

**Applies if the merchant:**
- References STC Pay, stc pay, or Saudi digital wallet payments

**Does not apply if the merchant:**
- Is asking about the Saudi domestic card network instead — route to Mada
- Is asking about a Gulf BNPL provider instead (Tabby, Tamara) — route to that product

**Example:** "How do we enable auto-capture for STC Pay transactions in KSA?"

**Likely keywords:** STC Pay, stc pay, Saudi digital wallet, KSA wallet payment, STC Pay auto-capture

---

### Swish
**What it is:** Popular Swedish mobile payment app for instant online purchases via banking app.
**Geography:** Sweden
**Payment type:** Bank transfer (mobile)
**Integration notes:** Beta; redirect; no chargebacks or recurring; account manager enablement.
**Contact risk:** low

**Applies if the merchant:**
- References Swish, Swedish mobile/banking-app payments, and is in Beta

**Does not apply if the merchant:**
- Is asking about setting up a recurring or subscription Swish payment — out of scope since Swish doesn't support recurring
- Is asking about a different Nordic wallet instead (e.g. Vipps for Norway, MobilePay for Denmark/Finland) — route to that product

**Example:** "Can a customer dispute a Swish payment the way they would a card chargeback?"

**Likely keywords:** Swish, Swedish mobile payment, Swish banking app, Swish beta, no Swish recurring, no Swish chargeback

---

### Tabby (Collecting)
**What it is:** Splits payments into four instalments, popular in MENA.
**Geography:** MENA
**Payment type:** BNPL
**Integration notes:** Gateway and Collecting models; manual or auto capture; account manager enablement.
**Contact risk:** high — BNPL, instalment queries, dispute-prone

**Applies if the merchant:**
- References Tabby, MENA BNPL, four-instalment payments, or Tabby disputes in UAE or KSA, and Checkout is collecting funds on the merchant's behalf (Collecting model)

**Does not apply if the merchant:**
- Is on the Gateway model where Tabby settles the merchant directly rather than Checkout collecting — route to Tabby (Gateway)
- Is asking about a different Gulf BNPL provider — route to Tamara (Collecting) or Tamara (Gateway)

**Example:** "A customer disputed a Tabby instalment purchase, how does that flow through since Checkout is collecting?"

**Likely keywords:** Tabby, Tabby Collecting, MENA BNPL, four instalments, Tabby dispute, Tabby UAE, Tabby KSA

---

### Tabby (Gateway)
**What it is:** Gateway model for Tabby BNPL in MENA.
**Geography:** MENA
**Payment type:** BNPL
**Integration notes:** Beta.
**Contact risk:** high — same as Collecting

**Applies if the merchant:**
- References Tabby operating on the Gateway model (Tabby settles the merchant directly) in MENA, and is in Beta

**Does not apply if the merchant:**
- Is on the Collecting model where Checkout collects funds on the merchant's behalf — route to Tabby (Collecting)
- Is asking about Tamara's gateway model instead — route to Tamara (Gateway)

**Example:** "We're on the Tabby gateway model in beta, is settlement handled by Tabby directly?"

**Likely keywords:** Tabby gateway, Tabby Gateway model, MENA BNPL gateway, Tabby beta, Tabby direct settlement

---

### Tamara (Collecting)
**What it is:** Split or deferred payment options for UAE and Saudi consumers.
**Geography:** UAE, Saudi Arabia
**Payment type:** BNPL
**Integration notes:** Flow only; auto-capture; no recurring; account manager enablement.
**Contact risk:** high — BNPL, dispute-prone

**Applies if the merchant:**
- References Tamara, Gulf BNPL, Tamara pay later, or Tamara instalments in UAE or KSA where Checkout is collecting on the merchant's behalf

**Does not apply if the merchant:**
- Is on the Gateway model where Tamara settles the merchant directly — route to Tamara (Gateway)
- Is asking about a different Gulf BNPL provider — route to Tabby (Collecting) or Tabby (Gateway)
- Is asking about setting up a recurring Tamara payment — out of scope since Tamara Collecting doesn't support recurring

**Example:** "How do refunds work on a Tamara deferred payment purchase in the UAE?"

**Likely keywords:** Tamara, Tamara Collecting, Gulf BNPL, Tamara pay later, Tamara instalments, Tamara UAE, Tamara KSA, no Tamara recurring

---

### Tamara (Gateway)
**What it is:** Gateway model for Tamara in UAE and Saudi Arabia.
**Geography:** UAE, Saudi Arabia
**Payment type:** BNPL
**Integration notes:** Beta.
**Contact risk:** high — same as Collecting

**Applies if the merchant:**
- References Tamara operating on the Gateway model (Tamara settles the merchant directly) in UAE or KSA, and is in Beta

**Does not apply if the merchant:**
- Is on the Collecting model — route to Tamara (Collecting)
- Is asking about Tabby's gateway model instead — route to Tabby (Gateway)

**Example:** "Is Tamara gateway settlement still in beta for our KSA storefront?"

**Likely keywords:** Tamara gateway, Tamara Gateway model, UAE KSA BNPL gateway, Tamara beta, Tamara direct settlement

---

### Touch 'n Go
**What it is:** Mobile payment service for Malaysian consumers with recurring payment support.
**Geography:** Customers: Malaysia. Merchants: HK, Singapore, EEA, UK
**Payment type:** Wallet
**Integration notes:** Flow only; redirect; auto-capture; account manager enablement.
**Contact risk:** medium — regional

**Applies if the merchant:**
- References Touch 'n Go, TnG, or Malaysian e-wallet payments, including recurring TNG payments

**Does not apply if the merchant:**
- Is asking about the Thai equivalent wallet instead — route to TrueMoney (different country, same regional-wallet pattern)

**Example:** "Can we set up recurring billing for Malaysian customers paying via Touch 'n Go?"

**Likely keywords:** Touch 'n Go, TnG, TNG eWallet, Malaysian e-wallet, TNG QR payment, TNG recurring

---

### TrueMoney
**What it is:** Mobile payment service for Thai consumers enabling one-time and recurring purchases.
**Geography:** Customers: Thailand. Merchants: HK, Singapore, EEA, UK
**Payment type:** Wallet
**Integration notes:** Flow or API; redirect; auto-capture; account manager enablement.
**Contact risk:** medium — regional

**Applies if the merchant:**
- References TrueMoney, Thai digital wallet, or TrueMoney payment failures, including one-time or recurring purchases

**Does not apply if the merchant:**
- Is asking about the Malaysian equivalent wallet instead — route to Touch 'n Go (different country, same regional-wallet pattern)

**Example:** "A Thai customer's TrueMoney recurring payment didn't go through this month."

**Likely keywords:** TrueMoney, Thai digital wallet, TrueMoney wallet, TrueMoney payment failure, TrueMoney recurring

---

### Twint
**What it is:** Swiss mobile payment wallet (pass-through or prepaid card).
**Geography:** Switzerland
**Payment type:** Digital wallet
**Integration notes:** Manual capture only (full capture); no recurring; redirect; account manager enablement.
**Contact risk:** medium — capture restrictions, no recurring = setup queries

**Applies if the merchant:**
- References Twint, Swiss mobile wallet, or asks about the full-capture-only restriction or lack of recurring support

**Does not apply if the merchant:**
- Is asking about setting up a recurring or subscription Twint payment — out of scope, Twint does not support recurring
- Is asking about auto-capture on Twint — out of scope, Twint only supports manual full capture

**Example:** "Why can we only do a full manual capture on Twint, not a partial one?"

**Likely keywords:** Twint, Swiss mobile wallet, Twint full capture, Twint manual capture, no Twint recurring, Twint Switzerland

---

### UnionPay
**What it is:** China's dominant card scheme, accepted globally.
**Geography:** Asia, global
**Payment type:** Card scheme
**Integration notes:** Beta; processed via CP Berlin.
**Contact risk:** medium — acceptance rate queries

**Applies if the merchant:**
- References UnionPay, UPI (as UnionPay's card network, not India's UPI), Chinese card payments, or UnionPay acceptance rates, and is in Beta

**Does not apply if the merchant:**
- Is asking about a competing global card scheme instead — route to Visa or Mastercard
- Is asking about a China-specific wallet rather than the card scheme — route to WeChat Pay CN

**Example:** "What's our current UnionPay acceptance rate now that it's processed via CP Berlin?"

**Likely keywords:** UnionPay, UPI card network, Chinese card payment, UnionPay acceptance, UnionPay beta, CP Berlin processing

---

### Venmo
**What it is:** Social payment service for US customers to pay businesses and friends.
**Geography:** United States
**Payment type:** Digital wallet (P2P)
**Integration notes:** US-only; USD only; Venmo app required; account manager enablement.
**Contact risk:** low

**Applies if the merchant:**
- References Venmo, US social payments, or Venmo business payments, and the customer is paying via the Venmo app in USD

**Does not apply if the merchant:**
- Is asking about accepting Venmo outside the US or in a non-USD currency — out of scope, Venmo is US-only and USD-only
- Is asking about a different P2P/social wallet — clarify which provider

**Example:** "Can our non-US customers pay us via Venmo?"

**Likely keywords:** Venmo, US social payment, Venmo business payment, Venmo app, Venmo USD only, Venmo US-only

---

### Vipps
**What it is:** Leading Nordic mobile wallet for instant smartphone payments.
**Geography:** Norway (customers: NO, SE)
**Payment type:** Wallet
**Integration notes:** Manual capture; no disputes or recurring; Flow or API; account manager enablement.
**Contact risk:** low

**Applies if the merchant:**
- References Vipps or Norwegian/Swedish mobile wallet payments, including manual capture questions

**Does not apply if the merchant:**
- Is asking about setting up a recurring Vipps payment or a Vipps dispute — out of scope, Vipps supports neither recurring nor disputes
- Is asking about a different Nordic wallet instead — route to MobilePay (Denmark/Finland)

**Example:** "Can we set up a recurring subscription for customers paying via Vipps?"

**Likely keywords:** Vipps, Norwegian mobile wallet, Vipps Sweden, Vipps manual capture, no Vipps recurring, no Vipps disputes

---

### Visa
**What it is:** World's largest card network for credit and debit payments.
**Geography:** Global
**Payment type:** Card scheme
**Integration notes:** Mixed availability; multiple processing teams.
**Contact risk:** low

**Applies if the merchant:**
- References Visa specifically, Visa-branded card declines, or Visa scheme rules/processing issues

**Does not apply if the merchant:**
- Is asking about a competing global scheme (Mastercard, UnionPay) — route to that scheme
- Is asking about a Visa-branded debit dual-brand running under Maestro rules — route to Maestro

**Example:** "We're seeing higher-than-usual decline rates on Visa transactions this week."

**Likely keywords:** Visa, Visa decline, Visa scheme rules, Visa processing, Visa acceptance, Visa card network

---

### WeChat Pay CN
**What it is:** WeChat Pay for mainland Chinese consumers.
**Geography:** Customers: China. Merchants: varies
**Payment type:** Wallet
**Integration notes:** Redirect; auto-capture; 10-minute payment expiry; account manager enablement.
**Contact risk:** medium — regional; expiry/redirect queries

**Applies if the merchant:**
- References WeChat Pay for mainland Chinese consumers, WeChat Pay CN, or the 10-minute payment expiry window on mainland transactions

**Does not apply if the merchant:**
- Is asking about WeChat Pay for Hong Kong consumers instead — route to WeChat Pay HK, a distinct product with its own consumer base despite the identical WeChat Pay branding

**Example:** "Our mainland Chinese customer's WeChat Pay QR code expired before they could scan it."

**Likely keywords:** WeChat Pay CN, WeChat Pay mainland China, WeChat Pay 10-minute expiry, WeChat Pay redirect, China WeChat wallet

---

### WeChat Pay HK
**What it is:** WeChat Pay for Hong Kong consumers.
**Geography:** Customers: Hong Kong. Merchants: varies
**Payment type:** Wallet
**Integration notes:** Redirect; auto-capture; 10-minute payment expiry; account manager enablement.
**Contact risk:** medium — regional

**Applies if the merchant:**
- References WeChat Pay for Hong Kong consumers or WeChat Pay HK specifically

**Does not apply if the merchant:**
- Is asking about WeChat Pay for mainland Chinese consumers instead — route to WeChat Pay CN, a distinct product despite the identical WeChat Pay branding

**Example:** "Do Hong Kong customers get the same 10-minute WeChat Pay expiry as mainland China?"

**Likely keywords:** WeChat Pay HK, WeChat Pay Hong Kong, WeChat Pay 10-minute expiry, Hong Kong WeChat wallet

---

### Wero
**What it is:** European mobile payment wallet (pan-European initiative).
**Geography:** Europe (Roadmap)
**Payment type:** Wallet
**Integration notes:** Roadmap — not yet live.
**Contact risk:** unknown

**Applies if the merchant:**
- References Wero, the pan-European mobile wallet initiative, or asks about its launch timeline before general availability

**Does not apply if the merchant:**
- Is asking about a country-specific European wallet that's already live (e.g. MB WAY, Swish, MobilePay, Vipps) — route to that specific product instead of the not-yet-live Wero

**Example:** "Is Wero going to replace national wallets like MB WAY once it launches?"

**Likely keywords:** Wero, pan-European wallet, European mobile payment initiative, Wero roadmap, Wero availability

---

### Zip
**What it is:** Leading BNPL provider in ANZ and North America, offering flexible instalments for shoppers with full payout to the merchant.
**Geography:** ANZ, North America (Roadmap)
**Payment type:** BNPL
**Integration notes:** Roadmap — not yet live.
**Contact risk:** unknown — Roadmap

**Applies if the merchant:**
- References Zip, Zip Co, ANZ or North America BNPL, or asks about the launch timeline before general availability

**Does not apply if the merchant:**
- Is asking about a Gulf-region BNPL provider instead (Tabby, Tamara) or the Spanish/Iberian equivalent (SeQura) — route to that product, since Zip is specifically the ANZ/North America provider

**Example:** "When will Zip be available for our North American storefront?"

**Likely keywords:** Zip, Zip Co, ANZ BNPL, North America BNPL, Zip instalments, Zip roadmap, Zip availability

---

## Payouts

### Bank Payouts
**What it is:** Payouts to bank accounts via local clearing methods and international payment rails.
**Key capabilities:** Reusable payout instruments; Europe/UK/US merchants; international routing; lower cost than card.
**Contact risk:** medium — bank routing failures, account validation queries

**Applies if the merchant:**
- Asks about a payout landing in, or failing to land in, a bank account
- References bank transfer, local clearing, or international bank routing for disbursements
- Asks about setting up or reusing a bank payout instrument

**Does not apply if the merchant:**
- References a payout to a card (see Card Payouts) rather than a bank account
- References settling funds into their own account under a self-settlement configuration (see Pay to Self)
- References disbursing funds to a third-party beneficiary rather than their own bank account (see Third Party Payouts)

**Example:** "Our bank payout from yesterday hasn't landed in the merchant's account yet, can you check the routing?"

**Likely keywords:** bank payout, bank transfer payout, payout to bank account, failed bank disbursement, local clearing, international payout rail, account validation, payout routing failure

---

### Card Payouts
**What it is:** Near-instant payouts directly to eligible payment cards.
**Key capabilities:** Rapid disbursement; gig economy / instant settlement use cases; broader eligibility than bank payouts.
**Contact risk:** medium — failed payout queries, eligibility questions

**Applies if the merchant:**
- Asks about a payout sent to a card rather than a bank account
- References instant or near-instant disbursement, especially gig economy or on-demand pay use cases
- Asks whether a card is eligible for receiving payouts

**Does not apply if the merchant:**
- References a payout to a bank account via local clearing or international rails (see Bank Payouts)
- References settling funds into their own account (see Pay to Self)
- References disbursing to a third-party beneficiary (see Third Party Payouts)

**Example:** "Can we push an instant payout to the driver's debit card instead of waiting for a bank transfer?"

**Likely keywords:** card payout, instant payout to card, near-instant disbursement, gig economy payout, card eligibility for payout, rapid disbursement, push to card

---

### Pay to Self
**What it is:** Settlement of Checkout.com-acquired funds into the merchant's own account.
**Key capabilities:** Variant of standard settlement; used where explicit self-settlement configuration is required.
**Contact risk:** low — variant of settlement; queries on account routing

**Applies if the merchant:**
- Asks about acquired funds settling into their own Checkout.com-linked account
- References a self-settlement configuration rather than a standard settlement flow
- Asks why funds are being settled to their own account instead of a payout destination

**Does not apply if the merchant:**
- References a payout to a bank account (see Bank Payouts) or card (see Card Payouts)
- References disbursing funds to a third party rather than themselves (see Third Party Payouts)
- Asks a general settlement timing/reconciliation question unrelated to the self-settlement configuration (see Financial Report)

**Example:** "Why is this batch settling to our own account instead of going out as a payout?"

**Likely keywords:** pay to self, self-settlement, settle to own account, self-settlement configuration, acquired funds routing to merchant

---

### Third Party Payouts
**What it is:** Settlement of funds to third-party beneficiaries rather than the primary merchant account.
**Key capabilities:** Supports disbursements to third parties; mixed availability.
**Contact risk:** medium — third-party routing, compliance, and eligibility queries

**Applies if the merchant:**
- Asks about disbursing funds to a third-party beneficiary rather than their own account
- Raises compliance or eligibility questions about paying out to a party other than the merchant itself
- References third-party payout routing or beneficiary setup

**Does not apply if the merchant:**
- References a payout to their own bank account (see Bank Payouts) or card (see Card Payouts)
- References settling into their own account (see Pay to Self)

**Example:** "We need to pay out a portion of these funds directly to our supplier, not to our own account."

**Likely keywords:** third party payouts, third-party beneficiary, settle to third party, disbursement to third party, beneficiary payout eligibility, third-party routing compliance

---

## Reporting & Analytics

### Analytics AI Assistant
**What it is:** AI-powered analytics assistant that helps merchants explore payment data in natural language, visualise performance, and identify actions to improve results.
**Key capabilities:** Natural language querying; performance visualisation; insight generation; actionable recommendations.
**Contact risk:** unknown — Beta

**Applies if the merchant:**
- Asks about querying payment data using natural language in the Dashboard
- References the Analytics Assistant or Analytics AI Assistant by name
- Asks for AI-generated recommendations or insights on payment performance

**Does not apply if the merchant:**
- Wants a downloadable or scheduled report rather than an interactive AI query (see Dashboard Reports or Dashboard Reports (non-financial))
- Wants a pre-built dashboard view of the payment funnel rather than AI-driven querying (see Payment Lifecycle Analytics)
- Wants to build a bespoke report or alert configuration (see Custom Analytics)

**Example:** "Can I just ask the Dashboard in plain English why my authorization rate dropped this week?"

**Likely keywords:** Analytics AI Assistant, Analytics Assistant, natural language payment query, AI analytics Dashboard, AI-generated insights, ask Dashboard a question

---

### Custom Analytics
**What it is:** Automated notifications that alert merchants to important changes in their payment performance.
**Key capabilities:** Configurable alerts; performance-change detection.
**Contact risk:** low — informational; setup queries

**Applies if the merchant:**
- Asks about setting up or configuring automated alerts on payment metrics
- Asks why they received (or didn't receive) a notification about a performance change
- References Custom Analytics by name

**Does not apply if the merchant:**
- Wants an interactive natural-language query tool rather than a configured alert (see Analytics AI Assistant)
- Wants a scheduled downloadable report rather than an alert (see Dashboard Reports / Reports API / SFTP Reports)
- Wants a pre-built performance dashboard rather than an alert (see Payment Lifecycle Analytics)

**Example:** "We want to be notified automatically if our decline rate spikes, how do we set that alert up?"

**Likely keywords:** Custom Analytics, payment performance alert, automated notification, alert configuration, performance-change detection

---

### Dashboard Reports
**What it is:** Web interface for generating and downloading financial and operational reports.
**Key capabilities:** On-demand or scheduled (daily/weekly/monthly); CSV download; field customisation; role-based access.
**Contact risk:** medium — report access, scheduling, and data discrepancy queries

**Applies if the merchant:**
- Asks about generating, scheduling, or downloading a financial report from the Dashboard
- Reports an access issue or permissions problem when trying to view a report in the Dashboard
- Disputes data shown in a Dashboard-generated CSV report

**Does not apply if the merchant:**
- The report in question is non-financial/operational data (see Dashboard Reports (non-financial))
- Wants programmatic/API access rather than the Dashboard UI (see Reports API)
- Wants file delivery via SFTP rather than Dashboard download (see SFTP Reports)
- Is asking about a specific named report type — Financial Report, Payment Operations Report, Issuing Report, Payment Lifecycle Analytics, Analytics AI Assistant, Custom Analytics, or Predictive Interchange — rather than general Dashboard report generation

**Example:** "I scheduled a weekly financial report in the Dashboard but the CSV download is missing fields I need."

**Likely keywords:** Dashboard report, financial report download, scheduled report, CSV export, report field customisation, report access issue, role-based report permissions, data discrepancy in report

---

### Dashboard Reports (non-financial)
**What it is:** Dashboard access to non-financial operational reports.
**Key capabilities:** Same as Dashboard Reports; separate data set.
**Contact risk:** low

**Applies if the merchant:**
- Asks about a non-financial or operational report accessed via the Dashboard
- Asks about generating or downloading operational data (not balances/fees/payouts) from the Dashboard

**Does not apply if the merchant:**
- The report in question covers financial data such as balances, payouts, fees, or taxes (see Dashboard Reports)
- Wants programmatic access to non-financial data (see Reports API (non-financial))
- Wants SFTP delivery of non-financial reports (see SFTP (non-financial reports))

**Example:** "Where in the Dashboard can I pull our non-financial operational report, not the balance one?"

**Likely keywords:** non-financial Dashboard report, operational reporting Dashboard, non-financial report download, Dashboard operational data

---

### Financial Report
**What it is:** Reporting suite providing a single source of truth for treasury and finance teams to reconcile balances, payouts, fees, and taxes across currencies.
**Key capabilities:** Multi-currency reconciliation; fee and tax breakdown; payout-vs-balance matching.
**Contact risk:** medium — reconciliation discrepancy queries

**Applies if the merchant:**
- Asks about reconciling balances, payouts, fees, or taxes across currencies
- Reports a discrepancy between a payout amount and their balance
- References the Financial Report by name for treasury/finance reconciliation

**Does not apply if the merchant:**
- Wants non-financial operational data such as fraud trends or authentication rates (see Payment Operations Report)
- Wants issuing-specific programme reporting (see Issuing Report)
- Wants a payment funnel view rather than a reconciliation report (see Payment Lifecycle Analytics)
- Wants natural-language querying rather than a structured report (see Analytics AI Assistant)
- Wants a forecasting tool for interchange cost rather than actuals reconciliation (see Predictive Interchange)

**Example:** "Our payout total doesn't match our balance for this period, can you help reconcile against the financial report?"

**Likely keywords:** Financial Report, financial reconciliation, balance and payout matching, multi-currency reconciliation, fee and tax breakdown, treasury reporting

---

### Issuing Report
**What it is:** Reporting suite giving issuers end-to-end visibility into card programme activity, from authorization to settlement, including disputes.
**Key capabilities:** Authorization-to-settlement transparency; cardholder behaviour monitoring; dispute and arbitration tracking.
**Contact risk:** low — reporting/analytics queries

**Applies if the merchant:**
- Runs a card issuing programme and asks about visibility into authorization-to-settlement activity
- Asks about tracking disputes or arbitration within their card programme reporting
- Asks about cardholder behaviour monitoring reports

**Does not apply if the merchant:**
- Is an acquiring merchant asking about acquiring-side financial reconciliation (see Financial Report)
- Wants non-financial acquiring-side operational data such as fraud or authentication trends (see Payment Operations Report)
- Wants a payment funnel dashboard rather than issuing-specific reporting (see Payment Lifecycle Analytics)

**Example:** "As an issuer, can we get a report showing our card programme from authorization through to settlement, including disputes?"

**Likely keywords:** Issuing Report, card programme reporting, issuing transaction visibility, authorization-to-settlement report, cardholder behaviour monitoring, issuing dispute tracking

---

### Payment Lifecycle Analytics
**What it is:** Pre-built dashboard tracking end-to-end payment performance from request to acceptance, with payment-level visibility.
**Key capabilities:** Funnel-style payment lifecycle view; payment-level drill-down.
**Contact risk:** low — self-serve insights

**Applies if the merchant:**
- Asks about a funnel view of payments from request through to acceptance
- Wants to drill down into an individual payment's lifecycle within a pre-built dashboard
- References Payment Lifecycle Analytics by name

**Does not apply if the merchant:**
- Wants a natural-language AI query tool rather than a pre-built dashboard (see Analytics AI Assistant)
- Wants a downloadable/scheduled report rather than a live dashboard (see Dashboard Reports)
- Wants financial reconciliation rather than a funnel view (see Financial Report)
- Wants non-financial operational reporting such as fraud/authentication trends (see Payment Operations Report)

**Example:** "Is there a dashboard where I can see the full funnel from payment request to acceptance for a single transaction?"

**Likely keywords:** Payment Lifecycle Analytics, payment funnel dashboard, request-to-acceptance tracking, payment-level drill-down, pre-built payment dashboard

---

### Payment Operations Report
**What it is:** Non-financial reporting suite covering customer behaviour, fraud trends, and authentication success to support risk and support teams.
**Key capabilities:** Fraud trend analysis; authentication success tracking; dispute risk management support.
**Contact risk:** low — operational reporting queries

**Applies if the merchant:**
- Asks about fraud trend reporting or authentication success rates
- Asks about non-financial reporting to support risk or dispute management teams
- References customer behaviour reporting distinct from financial reconciliation

**Does not apply if the merchant:**
- Wants financial reconciliation of balances, payouts, fees, or taxes (see Financial Report)
- Wants issuing-programme-specific reporting (see Issuing Report)
- Wants a payment funnel dashboard rather than fraud/authentication trend data (see Payment Lifecycle Analytics)

**Example:** "Can we get a report on authentication success rates and fraud trends, not the financial reconciliation one?"

**Likely keywords:** Payment Operations Report, non-financial reporting, fraud trend report, authentication success report, customer behaviour report, dispute risk reporting

---

### Predictive Interchange
**What it is:** Forecasting tool for interchange cost optimisation.
**Key capabilities:** Mixed availability; cost modelling for interchange fees.
**Contact risk:** low

**Applies if the merchant:**
- Asks about forecasting or optimising future interchange costs
- Asks for single-line interchange visibility or cost modelling rather than historical actuals
- References Predictive Interchange by name

**Does not apply if the merchant:**
- Wants historical actuals reconciliation of fees rather than a forecast (see Financial Report)
- Wants general fraud/authentication operational reporting (see Payment Operations Report)

**Example:** "Is there a tool that forecasts what our interchange costs will look like next quarter, not just what we've already paid?"

**Likely keywords:** Predictive Interchange, interchange fee forecasting, interchange cost optimisation, single line interchange reporting, interchange cost visibility

---

### Reports API
**What it is:** Programmatic interface for automated report retrieval at chosen intervals.
**Key capabilities:** Retrieve report metadata and files; integrate with reconciliation workflows.
**Contact risk:** low — developer-facing; queries mainly on field definitions

**Applies if the merchant:**
- Asks about retrieving financial report data programmatically via API
- Asks about field definitions or metadata returned by the Reports API
- Wants to automate report retrieval into their own reconciliation workflow

**Does not apply if the merchant:**
- The data requested is non-financial/operational (see Reports API (non-financial))
- Wants to use the Dashboard UI rather than an API (see Dashboard Reports)
- Wants scheduled file delivery via SFTP rather than API pull (see SFTP Reports)

**Example:** "We're pulling financial reports via the Reports API, can you confirm what this field in the response means?"

**Likely keywords:** Reports API, programmatic report retrieval, automated report access, API report field definition, report metadata endpoint

---

### Reports API (non-financial)
**What it is:** Reports API for operational/non-financial data.
**Key capabilities:** Same as Reports API; separate data set.
**Contact risk:** low

**Applies if the merchant:**
- Asks about retrieving non-financial or operational report data programmatically via API

**Does not apply if the merchant:**
- The data requested is financial (balances, payouts, fees, taxes) (see Reports API)
- Wants Dashboard UI access rather than API (see Dashboard Reports (non-financial))
- Wants SFTP delivery rather than API pull (see SFTP (non-financial reports))

**Example:** "Is there an API endpoint for pulling our non-financial operational data, separate from the financial Reports API?"

**Likely keywords:** Reports API non-financial, operational data API, non-financial report retrieval, API for operational reporting

---

### SFTP Reports
**What it is:** Scheduled CSV report delivery via SFTP.
**Key capabilities:** Automated delivery; pre-filtering by field; RSA key auth.
**Contact risk:** medium — SFTP connectivity, key management, scheduling queries

**Applies if the merchant:**
- Asks about scheduled CSV file delivery of financial reports via SFTP
- Reports an SFTP connectivity issue or asks about RSA key authentication setup
- Asks about pre-filtering fields for an SFTP-delivered financial report

**Does not apply if the merchant:**
- The report content is non-financial/operational (see SFTP (non-financial reports))
- Wants Dashboard download rather than SFTP delivery (see Dashboard Reports)
- Wants API pull rather than scheduled file delivery (see Reports API)

**Example:** "Our SFTP report delivery failed last night, can you check if it's an RSA key issue?"

**Likely keywords:** SFTP report delivery, SFTP connectivity issue, RSA key authentication, scheduled file delivery, financial report SFTP, SFTP field filtering

---

### SFTP (non-financial reports)
**What it is:** SFTP delivery for non-financial reports.
**Key capabilities:** Same as SFTP Reports; separate data set.
**Contact risk:** low

**Applies if the merchant:**
- Asks about scheduled SFTP delivery of non-financial or operational report data

**Does not apply if the merchant:**
- The report content is financial (see SFTP Reports)
- Wants Dashboard access rather than SFTP delivery (see Dashboard Reports (non-financial))
- Wants API pull rather than SFTP file delivery (see Reports API (non-financial))

**Example:** "We need our non-financial operational reports delivered by SFTP, is that a separate setup from the financial one?"

**Likely keywords:** SFTP non-financial reports, operational report SFTP delivery, non-financial file delivery, SFTP setup for operational data

---

## Treasury & FX

### Acquiring - Custom FX markup per currency pair
**What it is:** Custom FX markup configuration per currency pair.
**Key capabilities:** Bespoke FX pricing.
**Contact risk:** medium — FX rate discrepancy queries

**Applies if the merchant:**
- Asks about a bespoke or negotiated FX markup applied to a specific currency pair
- Disputes an FX rate that differs from the standard published rate for a currency pair
- Asks how to configure custom markup pricing per currency pair

**Does not apply if the merchant:**
- Asks about the standard 24-hour locked rate (see Acquiring - Daily FX Rates)
- Asks about a real-time market rate (see Acquiring - FX Live Market Rates)
- Asks about a scheme-set rate from Visa/Mastercard (see Acquiring - Scheme FX Rates)
- Asks about FX applied at payout time rather than acquiring (see PTC - FX based on Scheme FX rates)

**Example:** "The markup we agreed for EUR/USD doesn't match what's showing on this transaction, can you check our custom pricing?"

**Likely keywords:** custom FX markup, currency pair markup, bespoke FX rate, negotiated FX pricing, FX rate discrepancy, per-currency-pair pricing configuration

---

### Acquiring - Daily FX Rates
**What it is:** Daily FX rate service for acquiring transactions.
**Key capabilities:** Merchant-facing rate visibility.
**Contact risk:** low

**Applies if the merchant:**
- Asks about a rate that is locked for a 24-hour period
- Asks why the settlement amount in local currency is guaranteed for the day
- References the daily rate used for acquiring conversion

**Does not apply if the merchant:**
- Asks about a bespoke markup on a specific currency pair (see Acquiring - Custom FX markup per currency pair)
- Asks about a rate that moves in real time with the market (see Acquiring - FX Live Market Rates)
- Asks about a Visa/Mastercard scheme-set rate (see Acquiring - Scheme FX Rates)
- Asks about FX applied on a payout rather than acquiring (see PTC - FX based on Scheme FX rates)

**Example:** "What rate will apply to today's transactions, is it locked for the whole day?"

**Likely keywords:** daily FX rate, locked 24-hour exchange rate, guaranteed settlement amount, local currency conversion rate, daily rate acquiring

---

### Acquiring - FX Live Market Rates
**What it is:** Live market FX rate service for acquiring.
**Key capabilities:** Real-time rate display.
**Contact risk:** low

**Applies if the merchant:**
- Asks about a rate that updates in real time from the market (e.g. Bloomberg-sourced)
- Asks why the conversion rate at capture differs from a locked daily rate
- References live market rate rather than a fixed or scheme rate

**Does not apply if the merchant:**
- Asks about the fixed 24-hour rate (see Acquiring - Daily FX Rates)
- Asks about a bespoke markup per currency pair (see Acquiring - Custom FX markup per currency pair)
- Asks about a Visa/Mastercard scheme rate (see Acquiring - Scheme FX Rates)
- Asks about FX applied at payout (see PTC - FX based on Scheme FX rates)

**Example:** "The rate applied at capture keeps moving, is that the live market rate?"

**Likely keywords:** live FX rate, Bloomberg FX rate, real-time market rate, live market exchange rate, rate applied at capture, market-rate currency conversion

---

### Acquiring - Scheme FX Rates
**What it is:** Scheme-level FX rate service (Visa/Mastercard).
**Key capabilities:** Scheme rate transparency.
**Contact risk:** low

**Applies if the merchant:**
- Asks about the FX rate set directly by Visa or Mastercard
- Disputes a conversion rate and references the card scheme as the rate source
- Asks for transparency on scheme-level currency conversion

**Does not apply if the merchant:**
- Asks about the daily locked rate (see Acquiring - Daily FX Rates)
- Asks about a bespoke markup per currency pair (see Acquiring - Custom FX markup per currency pair)
- Asks about a real-time market rate (see Acquiring - FX Live Market Rates)
- Asks about scheme FX applied at payout time specifically (see PTC - FX based on Scheme FX rates)

**Example:** "This transaction converted at a Visa-set rate, can you confirm that's the scheme rate and not your own markup?"

**Likely keywords:** scheme FX rate, Visa FX rate, Mastercard FX rate, scheme-level currency conversion, card network exchange rate

---

### PTC - FX based on Scheme FX rates
**What it is:** Payment-time currency conversion using scheme FX rates (Visa/MC only).
**Key capabilities:** DCC-style conversion at scheme rates.
**Contact risk:** medium — FX conversion queries

**Applies if the merchant:**
- Asks about currency conversion applied specifically on a payout, not an acquiring transaction
- References cross-border card payout FX conversion
- Asks about scheme FX rates used at the point of payout (payment-time conversion / DCC-style)

**Does not apply if the merchant:**
- Asks about FX applied at capture/acquiring rather than payout (see the four Acquiring FX rate products: Custom FX markup, Daily FX Rates, FX Live Market Rates, Scheme FX Rates)
- Asks about the payout destination or delivery mechanism itself rather than the FX applied (see Bank Payouts or Card Payouts)
- Asks about settlement reconciliation across currencies rather than the conversion rate (see Financial Report)

**Example:** "The cross-border payout to our card converted at a scheme rate, can you confirm which rate applied at payout time?"

**Likely keywords:** payout-time currency conversion, PTC, cross-border card payout FX, scheme FX rates for payouts, DCC payout conversion, payment-time FX

---

## In-person Payments

### SoftPOS SDK
**What it is:** SDK that turns NFC-enabled devices (phone, tablet, kiosk) into secure payment terminals, embeddable in merchant apps.
**Key capabilities:** Tap-to-pay on existing hardware; no additional card reader required; embeddable in branded apps (2027).
**Contact risk:** medium — Roadmap; SDK integration queries expected

**Applies if the merchant:**
- References SoftPOS, SoftPOS SDK, or turning a phone/tablet into a card terminal via NFC
- Asks about embedding tap-to-pay directly into their own branded app
- Asks whether they need extra card-reader hardware to accept in-person payments

**Does not apply if the merchant:**
- Is asking about combining in-person and online payments under a single API rather than the tap-to-pay SDK specifically — that's Unified Commerce
- Is asking about dedicated card-reader hardware terminals rather than an app-embedded NFC solution — that falls outside SoftPOS SDK's scope

**Example:** "We want to let our staff take payments by tapping a customer's card on their own phone using our app — is that SoftPOS?"

**Likely keywords:** SoftPOS, SoftPOS SDK, tap-to-pay, NFC payment terminal, phone as card reader, embedded tap-to-pay, app-based POS

---

### Unified Commerce
**What it is:** Ability to process in-person and digital payments through the Unified Payments API using merchant-owned devices, combining HardPOS and SoftPOS revenue streams.
**Key capabilities:** Single API for in-person and digital payments; supports HardPOS and SoftPOS origination.
**Contact risk:** medium — Roadmap; integration and reconciliation queries expected

**Applies if the merchant:**
- Asks about reconciling in-person and online transactions through one unified API/reporting view
- References combining HardPOS and SoftPOS revenue streams
- Asks how in-person and digital payment channels are unified under Checkout.com's payments stack

**Does not apply if the merchant:**
- Is only asking about the phone-as-terminal SDK itself, without mentioning unifying it with online payments — that's SoftPOS SDK
- Is asking specifically about the API surface for online payments (UPAPI or Payment Setup API) with no in-person component — those are separate products under Unified Payments API

**Example:** "Can we see our in-store tap-to-pay transactions and our online transactions in the same reporting and API, rather than two separate systems?"

**Likely keywords:** Unified Commerce, HardPOS and SoftPOS, combined in-person and online payments, omnichannel reconciliation, single API in-person and digital

---

## Vault

### Forward API
**What it is:** Beta feature enabling merchants to enrich payment requests with CKO-stored credentials and forward them to third-party API endpoints.
**Key capabilities:** Allows use of CKO-stored tokens with external processors.
**Contact risk:** medium — Beta; third-party routing queries

**Applies if the merchant:**
- Asks about forwarding a Checkout.com-stored token or credential to a third-party processor or endpoint
- References the Forward API by name, or "using CKO credentials outside of CKO processing"
- Asks about enriching an external payment request with CKO-stored card data

**Does not apply if the merchant:**
- Is asking about storing credentials for use within Checkout.com's own processing, with no third-party forwarding involved — that's Integrated Vault
- Is asking about a standalone vault deployment with no processing (CKO or third-party) attached — that's Standalone Vault

**Example:** "We want to send a customer's Checkout.com-stored card token to another processor we also use — is that possible via the Forward API?"

**Likely keywords:** Forward API, forwarding tokens to third-party endpoint, CKO-stored credentials with external processor, third-party routing, Beta forwarding feature

---

### Integrated Vault
**What it is:** Credential storage embedded within Checkout.com's payment processing.
**Key capabilities:** Stores customer details, payment instruments, and network tokens; only the merchant can access their own vault.
**Contact risk:** medium — tokenisation queries, stored credential management

**Applies if the merchant:**
- Asks about storing customer payment instruments or card details as part of their CKO processing setup
- References "the Vault," stored credentials, or tokenised card storage tied to CKO transactions
- Asks who can access their vaulted data (access is merchant-only)

**Does not apply if the merchant:**
- Is asking about vault services decoupled from CKO payment processing — that's Standalone Vault
- Is asking about sending stored credentials on to a third-party processor — that's Forward API
- Is asking specifically about the network token layer rather than the general credential store — that's Network Tokens

**Example:** "How do we securely store our customers' card details for repeat payments through Checkout.com?"

**Likely keywords:** Vault, Integrated Vault, stored credentials, tokenised card storage, payment instrument management, customer detail storage, merchant-only vault access

---

### Standalone Vault
**What it is:** Independent credential storage for merchants who need vault services without full CKO payment processing.
**Key capabilities:** Beta; separate deployment from payment processing.
**Contact risk:** medium — Beta; setup and integration queries

**Applies if the merchant:**
- Asks about storing card credentials with Checkout.com without processing payments through Checkout.com
- References Standalone Vault by name or "vault-only" deployment
- Asks about Beta access or setup for an independent credential store

**Does not apply if the merchant:**
- Is storing credentials as part of their existing CKO payment processing flow — that's Integrated Vault
- Is asking about forwarding vaulted credentials to a third-party processor — that's Forward API

**Example:** "We don't process payments through Checkout.com yet, but we'd like to store card details with you separately — is that the Standalone Vault?"

**Likely keywords:** Standalone Vault, vault without CKO processing, independent credential storage, Beta vault deployment, vault-only setup

---

## Unified Payments API

### Unified Payments API (UPAPI)
**What it is:** Modern RESTful API for enterprise merchants unifying payment backends, replacing legacy API bundles.
**Key capabilities:** Single API surface for payments; enterprise-grade; general availability.
**Contact risk:** medium — enterprise integration complexity; migration queries from legacy API

**Applies if the merchant:**
- Asks about migrating from a legacy Checkout.com API bundle to a single unified API
- References UPAPI or "Unified Payments API" by name
- Is an enterprise merchant asking to consolidate multiple payment backends into one API surface

**Does not apply if the merchant:**
- Is specifically asking about a persistent session-based checkout flow with a Payment Setup ID — that's Payment Setup API
- Is asking about unifying in-person and online payment channels rather than backend API consolidation — that's Unified Commerce

**Example:** "We're on several older Checkout.com API integrations — can we move to one unified API instead?"

**Likely keywords:** UPAPI, Unified Payments API, enterprise backend unification, legacy API migration, single payments API surface, API consolidation

---

### Payment Setup API
**What it is:** Checkout.com's latest Payments API, maintaining a single payment session with a persistent Payment Setup ID across multiple payment attempts throughout checkout.
**Key capabilities:** Session-based (not single-request) payment flow; persists across retries; unique Payment Setup ID.
**Contact risk:** medium — Beta; session and retry-handling queries expected

**Applies if the merchant:**
- References a "Payment Setup ID" or a persistent session across multiple payment attempts
- Asks how retries or failed attempts are handled within one continuous checkout session
- Asks about Beta access to the Payment Setup API

**Does not apply if the merchant:**
- Is asking about a general single-request payment API without a persistent session concept — that's UPAPI or the standard Payments API
- Is asking about consolidating multiple legacy API bundles into one enterprise API surface, with no mention of session persistence — that's UPAPI

**Example:** "If a customer's card is declined and they retry with a different card, does Checkout.com keep it in the same payment session?"

**Likely keywords:** Payment Setup API, Payment Setup ID, session-based checkout, persistent payment session, retry handling, Beta payments API

---

*Last updated: July 2026 (source of truth updated to Airtable Product Catalogue). Enriched definitions from checkout.com/docs March 2026 scrape. Restructured July 2026 from a table format to per-product Applies-if/Does-not-apply-if/Example/Likely-keywords blocks, mirroring the Fin Attribute definition format in `fin-attributes-definitions.md`, to support Fin product classification. New products added: Bundled Authentication, Fund Acceleration, Same and Cross-currency Transfers, CommerceTools, Primer.io, Recurly, SAP OPF, Visualsoft, Pay to Self, Third Party Payouts, Unified Payments API (UPAPI), Dwolla, Ocado Group, Standalone Authentication, Address Document Verification, AML Screening, ACI, IXOPay, Prestashop, YUNO, Zingfit, Cash App, PayPay, Zip, Analytics AI Assistant (renamed from Analytics Assistant), Custom Analytics, Financial Report, Issuing Report, Payment Lifecycle Analytics, Payment Operations Report, SoftPOS SDK, Unified Commerce, Payment Setup API. ACI/IXOPay/Prestashop/YUNO/Zingfit are based on public company knowledge, not an Airtable overview — verify before relying on them for Fin classification. To be validated against support contact data when available.*


