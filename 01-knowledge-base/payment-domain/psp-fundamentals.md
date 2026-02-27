# PSP Fundamentals

> This document provides foundational knowledge about Payment Service Providers and payment processing. Reference this when explaining payment concepts to non-technical stakeholders or when onboarding new team members.

## What is a PSP?

A **Payment Service Provider (PSP)** is a company that enables merchants (businesses) to accept electronic payments from customers. PSPs act as an intermediary between merchants, customers, banks, and card networks.

### Why Merchants Use PSPs

**Single Integration**: Connect once to accept multiple payment methods (cards, wallets, bank transfers)

**Global Reach**: Process payments in multiple currencies and regions

**Compliance**: PSP handles complex regulations (PCI-DSS, PSD2, AML, etc.)

**Fraud Protection**: Built-in tools to detect and prevent fraudulent transactions

**Optimization**: Smart routing, retry logic, and tools to maximize payment success

**Speed to Market**: Start accepting payments quickly without building payment infrastructure

## The Payment Ecosystem

### Key Players

**Cardholder**: The customer making a purchase

**Merchant**: The business selling goods or services

**Payment Service Provider (PSP)**: Processes payments on behalf of merchants (Checkout.com's role)

**Acquirer**: Bank that processes card payments for the merchant

**Card Networks**: Visa, Mastercard, Amex - operate payment infrastructure

**Issuer**: Bank that issued the customer's payment card

**Payment Gateway**: Technology that securely transmits payment data

### How They Work Together

```
Cardholder -> Merchant -> PSP -> Acquirer -> Card Network -> Issuer
                                                                |
                              Authorization Response <-----------
```

## Payment Processing Flow

### Phase 1: Authorization

1. **Customer initiates payment** on merchant's website/app
2. **Merchant sends payment request** to PSP with card details and amount
3. **PSP validates request** and routes to appropriate acquirer
4. **Acquirer forwards** to card network (Visa, Mastercard, etc.)
5. **Card network routes** to issuing bank
6. **Issuer checks**:
   - Is card valid and not stolen?
   - Does customer have sufficient funds?
   - Is transaction within card limits?
   - Does fraud screening pass?
7. **Issuer responds** with approval or decline
8. **Response travels back** through the chain to merchant
9. **Funds are held** on customer's card (not transferred yet)

**Timing**: Typically 1-3 seconds

### Phase 2: Capture

- **Merchant confirms** they will fulfill the order
- **Capture request** sent to PSP
- Can capture **full amount or partial** (e.g., for split shipments)
- Can capture **immediately or later** (e.g., at time of shipment)
- **Funds officially committed** to transfer

**Timing**: Immediate to several days after authorization

### Phase 3: Settlement

- **Funds actually move** between banks
- **Typically occurs** T+1 to T+3 days after capture
- **PSP transfers money** from acquirer to merchant's bank account
- **Fees are deducted** (interchange fees, PSP fees)

**Timing**: 1-3 business days

### Phase 4: Reconciliation

- **Merchant verifies** expected funds received
- **Match transactions** to actual bank deposits
- **Identify discrepancies** (chargebacks, refunds, adjustments)

## Common Payment Operations

### Refund
- **Return money** to customer after capture
- Can be **full or partial**
- Takes **5-10 days** to appear on customer's card
- **Fees typically not refunded** to merchant

### Void
- **Cancel authorization** before capture
- **No money movement** occurs
- Must be done **same day** as authorization
- **Releases hold** on customer's funds

### Chargeback
- **Customer disputes** charge with their bank
- **Issuer reverses** transaction and takes funds back
- **Merchant can respond** with evidence
- **Costly** for merchant (fees + lost goods/services)
- Can result in **account termination** if rate is too high

### Recurring Payment
- **Scheduled charges** for subscriptions or installments
- Uses **stored payment method** (tokenized card)
- Requires **customer agreement** and compliance with regulations
- Needs **retry logic** for failed payments

## Payment Security

### PCI-DSS Compliance
- **Industry standard** for handling card data
- **PSPs are PCI-certified** so merchants don't need to be (for most integrations)
- Never **store raw card numbers** - use tokens instead
- **Annual audits** and security assessments required

### 3D Secure (3DS)
- **Additional authentication** step for card payments
- **Customer verifies identity** (password, SMS code, biometric)
- **Reduces fraud** and shifts liability from merchant to issuer
- **Required in Europe** (PSD2/SCA regulations)
- Can **reduce conversion** due to extra step

### Tokenization
- Replace **sensitive card data** with secure token
- **Tokens are useless** if stolen
- Enable **repeat payments** without storing card numbers
- **PCI compliance benefit** - reduced scope

### Fraud Detection
- **Real-time screening** of every transaction
- **Velocity checks**: Too many transactions too quickly
- **Geolocation**: Payment location vs. billing address
- **Device fingerprinting**: Recognize trusted devices
- **Machine learning**: Pattern recognition for fraud
- **Manual review**: High-risk transactions reviewed by humans

## Payment Methods Beyond Cards

### Digital Wallets
- **Apple Pay, Google Pay, PayPal**
- Customer stores payment methods in wallet
- **Fast checkout** experience
- Often includes **additional security** (biometric auth)

### Bank Transfers
- **Direct bank-to-bank** payment
- **Lower fees** than cards
- **Slower processing** (days, not seconds)
- **Regional variations**: ACH (US), SEPA (Europe), BACS (UK)

### Alternative Payment Methods (APMs)
- **Local payment methods** popular in specific regions
- Examples: iDEAL (Netherlands), Bancontact (Belgium), Boleto (Brazil)
- **Higher conversion** for local customers
- **Different integration** requirements per method

### Buy Now Pay Later (BNPL)
- **Installment payments** (e.g., Klarna, Afterpay, Affirm)
- Customer pays over time, merchant receives full amount upfront
- **Popular with younger consumers**
- **Higher approval rates** than cards

## Key Metrics & Optimization

### Authorization Rate
- **Percentage of payments approved** by issuer
- Target: **>85%** (varies by industry and region)
- **Low rates** indicate fraud concerns, technical issues, or card issues

### Decline Rate
- **Percentage of payments rejected**
- **Hard decline**: Card expired, insufficient funds (merchant can't retry)
- **Soft decline**: Temporary issue (can retry)
- Improve with: better fraud settings, local payment methods, smart retry

### Conversion Rate
- **Percentage of payment attempts** that successfully complete
- Factors: Payment method availability, checkout UX, fraud settings
- Even **small improvements** (1-2%) = significant revenue

### Chargeback Rate
- **Chargebacks** divided by total transactions
- Target: **<1%** (exceeding can lead to fines or account termination)
- Reduce with: clear billing descriptors, good customer service, fraud prevention


**Last Updated**: [Date]
**Owner**: Charlie Wildish
