---
id: 23047190761874
section_id: 21991121506450
title: "Clearing, Settlements & Authorisation Introduction"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/23047190761874-Clearing-Settlements-Authorisation-Introduction"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-01-22T15:22:09Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQT889RQXXSG27BB4ZJ0M"]
label_names: ["case_transactions", "global", "Glossary_and_introductions", "Clearing_settlements_authorisation_introduction"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article:**

This guide is for **Merchant Care teams** (L1 and L2) to efficiently resolve common clearing, settlement, and authorization issues. 

It aims to reduce escalations to Payment Engineering Operations by empowering you with clear steps and guidelines, ensuring faster resolution times for merchants.

## 

 

## ESCALATION MATRIX** ⏫**

The below named articles contain all procedural steps for the common use cases under Clearing, Settlement and Authorisation. When classifying these cases, the case type is primarily ‘Transactions’ and the feature type is ‘Payment Method’. Select the relevant issue type and product type based on the merchant’s issue. 

For **Clearing and Settlements**, these should be escalated to Payment Eng Ops (Card Processing L3) if further investigation is needed. Please see below example request types:

- 
[All Reversal Request articles](https://checkoutint.zendesk.com/hc/en-us/sections/23046190282514-Reversal-Requests) in the Global Transactions section

  - [Performing Reversals on MC/VISA Clearing Platform](https://checkoutint.zendesk.com/hc/en-us/articles/23046303290130-Performing-Reversals-on-MC-VISA-Clearing-Platform)

  - [Mastercard Reversal via API](https://checkoutint.zendesk.com/hc/en-us/articles/23046333912210-Mastercard-Reversal-via-API)

  - [Visa Reversal via API](https://checkoutint.zendesk.com/hc/en-us/articles/23046303329554-Visa-Reversal-via-API)

- 
[All Proof of Payments/Funds Not Received articles](https://checkoutint.zendesk.com/hc/en-us/sections/23046197784338-Proof-of-Payments-Funds-Not-Received) in the Global Transactions section:

  - [Mastercard](https://checkoutint.zendesk.com/hc/en-us/articles/23046298377746-Mastercard)

  - [Visa GW3/GWC](https://checkoutint.zendesk.com/hc/en-us/articles/23046303441170-Visa-GW3-GWC)

  - [Retrieval for Proof of Payouts (example)](https://checkoutint.zendesk.com/hc/en-us/articles/23046329562770-Retrieval-for-Proof-of-Payouts-example)

- [Request for Information on Rejects article](https://checkoutint.zendesk.com/hc/en-us/sections/23045958401426-Request-for-Information-on-Rejects)

- [BIN Enablement article](https://checkoutint.zendesk.com/hc/en-us/sections/23045954287122-BIN-Enablement)

- [20054 Expiry Date Issue article](https://checkoutint.zendesk.com/hc/en-us/articles/23046343726994-20054-Expiry-Date-Issue)

- 
[All Transaction Status articles](https://checkoutint.zendesk.com/hc/en-us/sections/23045937114898-Transaction-Status) found in the Global Transactions section:

  - [SAB (GW3) Transaction Status](https://checkoutint.zendesk.com/hc/en-us/articles/23046303716370-SAB-GW3-Transaction-Status)

  - 
[Carte Bancaires Transaction Status](https://checkoutint.zendesk.com/hc/en-us/articles/23046303685138-Carte-Bancaires-Transaction-Status)[](https://checkoutint.zendesk.com/hc/en-us/articles/23046303685138-Carte-Bancaires-Transaction-Status)

  - [Mastercard Transaction Status](https://checkoutint.zendesk.com/hc/en-us/articles/23046303654802-Mastercard-Transaction-Status)

  - [Visa Transaction Status](https://checkoutint.zendesk.com/hc/en-us/articles/23046329689234-Visa-Transaction-Status)

  - [JCB Transaction Status](https://checkoutint.zendesk.com/hc/en-us/articles/23046329669778-JCB-Transaction-Status)

  - [DCI Transaction Status](https://checkoutint.zendesk.com/hc/en-us/articles/23046329640594-DCI-Transaction-Status)

  - [AMEX EU Transaction Status](https://checkoutint.zendesk.com/hc/en-us/articles/23046334077842-AMEX-EU-Transaction-Status)

For **Authorisations and Payins,** queries these should be escalated to Merchant Care L2 if further investigation is required. Please see below example request types (SOP links are not exhaustive):

- 
[Scheme Declines](https://checkoutint.zendesk.com/hc/en-us/sections/26832912736274-Scheme-Declines) (minus scheme reject SOPs)

- [Internal Card Processing Declines](https://checkoutint.zendesk.com/hc/en-us/sections/27060550224018-Internal-Error)

- [Third Party Acquirer Declines](https://checkoutint.zendesk.com/hc/en-us/sections/27060573159058-Third-party-Acquirer-Declines)

- [Billing Descriptor Mismatches](https://checkoutint.zendesk.com/hc/en-us/articles/28538638717074-Troubleshooting-Billing-Descriptor-Mismatches)

- [Account Funding Transaction Declines](https://checkoutint.zendesk.com/hc/en-us/sections/28530815273106-Account-Funding-Transactions-AFTs)

NOTE: For MENA region, please see below escalation matrix for TPAs which should be followed before escalating to Merchant Care L2:

- [TPA MENA Escalation Process](https://checkoutint.zendesk.com/hc/en-us/articles/24729067247506-TPA-Escalation-MENA)

## **ROLES & RESPONSIBILITIES ****🛠️**

 Click here to see the roles and responsibilities for L1, L2 & L3 **Level 1: Merchant Care (L1)**

- 
**Role:** First line of support.

- 
**Responsibilities:** Work from pre-defined knowledge base procedures to solve and answer the merchant’s query. Triage incoming issues and identify appropriate escalation paths.

- 
**Expected Actions:** Initial troubleshooting, data gathering, accurate classification.

- 
**Trigger for Escalation to L2:** Issue requires advanced troubleshooting, tooling access (beyond basic Retool/Hermes), or is not covered by knowledge base guides. Please note only Authorisation and Payins queries should be escalated to L2, for Clearing and Settlements this should go directly to L3.

**Level 2: Merchant Care (L2)**

- 
**Role:** Advanced support for clearing, settlement and authorization.

- 
**Responsibilities:** Review issues holistically, use expertise to access advanced tooling or databases, and resolve merchant problems. L2 handles all clearing, settlement, or authorization issues **excluding those explicitly defined for L3 escalation**.

- 
**Expected Actions:** Deep-dive investigation, direct resolution, detailed documentation.

- 
**Trigger for Escalation to L3:** Issue falls under the "L3 Escalation Triggers" list (see below).

**Level 3: Payment Engineering Operations (L3)**

- 
**Role:** Technical experts with specialized access and knowledge of payment systems.

- 
**Responsibilities:** Solve complex technical issues requiring database access, specific tooling, or engineering intervention.

- 
**Expected Actions:** System analysis, bug identification, collaboration with engineering, high-confidence issue resolution.

- 
**Trigger for Escalation:** System-wide outage, critical data issue, or incident requiring executive oversight/cross-functional major incident management.

 

## RESOURCES **📍**

| Tools | Case Examples | Related |
| --- | --- | --- |
| - Checkout Agent Toolkit  - Hermes  - Snowflake  - Jumpbox  - Looker  - Datadog  [See Ops Tools Library](https://checkout.atlassian.net/wiki/spaces/LL/database/6990364784?atl_f=PAGETREE) for access requests, training and log in links | Similar case examples and solutions | Links to related articles or external content |

 

 

## KEY TERMS & DEFINITIONS

 
Click here to see the key terms and definitions

| Term | **Definition** |
| --- | --- |
| **AMEX** | American Express |
| **DCI** | Diners Club International |
| **BIN** | A Bank Identification Number (BIN) is the initial set of four to six numbers on a card that identifies the institution |
| **GWC** | Stands for Gateway Core, the newest and latest version of the Gateway, built using .NET core |
| **GW3** | Also known as Merchant API, GW3 is the legacy gateway currently used by most of our clients. It is built using .NET 4.6 |
