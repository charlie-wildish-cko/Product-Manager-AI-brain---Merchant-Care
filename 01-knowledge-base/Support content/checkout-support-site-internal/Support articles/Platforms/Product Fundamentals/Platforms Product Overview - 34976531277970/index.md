---
id: 34976531277970
section_id: 34976307095826
title: "Platforms: Product Overview"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/34976531277970-Platforms-Product-Overview"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-04-21T10:12:36Z"
permission_group_id: 26838654181266
content_tag_ids: []
label_names: []
user_segment_ids: [11003606966930]
archive: false
---

This article explains what Platforms for SaaS is, how it differs from PayFac, how money moves through the system, which payment methods are supported, and how sub-accounts work. 

## **What is Platforms for SaaS?**

Platforms for SaaS is a Checkout.com product designed for software companies that process payments on behalf of the businesses that use their platform. These businesses are called sub-entities.

A typical example: a software platform that provides booking tools to hundreds of independent restaurants. Each restaurant is a sub-entity. The software company - the platform - uses Checkout.com to accept card payments on behalf of all of them.

Because the platform is not licensed or regulated to handle money directly, Checkout.com takes responsibility for the compliance and due diligence checks needed to onboard each sub-entity.

## **How Platforms for SaaS differs from PayFac**

Both products let a platform process payments on behalf of other businesses. The key difference is regulatory responsibility:

|  | **Platforms for SaaS** | **PayFac (Payment Facilitator)** |
| --- | --- | --- |
| Regulated? | No - the platform is unregulated | Yes - the platform holds a payment facilitator licence |
| Who does compliance checks? | Checkout.com handles all due diligence on sub-entities | The platform takes on compliance responsibility |
| Best suited for | SaaS companies wanting Checkout.com to handle regulatory complexity | Platforms that are already regulated and want more control |

_⚠️ If a customer asks whether they should use Platforms for SaaS or PayFac, this is a commercial and technical question. Do not advise - escalate to the account manager._

## **How funds flow**

When a customer pays for something on a sub-entity's platform, here is what happens to the money:

1. The customer pays. The payment is processed by Checkout.com.

2. Checkout.com routes the funds. Based on the payment, funds are split between the platform and the sub-entity according to pre-agreed rules.

3. Fees are deducted. Checkout.com takes its fees from the platform's share.

4. The sub-entity receives their funds. Settlement is paid directly to the sub-entity's verified bank account on a schedule configured for them.

The platform can also charge the sub-entity a commission - a cut of each transaction for providing the software and payment infrastructure. See Article 6 for detail on commission models.

## **Holding currencies and sub-accounts**

When a sub-entity is onboarded, the platform specifies one or more holding currencies - for example, USD, GBP, or EUR. Checkout.com creates a separate sub-account for each currency.

Funds are routed to the matching sub-account based on the currency of the payment:

- A payment in USD goes to the sub-entity's USD sub-account.

- A payment in GBP goes to the sub-entity's GBP sub-account.

- A payment in any other currency goes to the sub-entity's default holding currency sub-account.

The platform sets the default holding currency during onboarding. For example, if the default is USD, a payment in Japanese yen would be converted and held in USD.

## **Supported payment methods**

The following payment methods are available to sub-entities on Platforms for SaaS:

- Visa

- Mastercard

- American Express

- Discover

- ACH Direct Debit (US bank transfers)

- Apple Pay

- Google Pay

- Cartes Bancaires (French card network)

- PINless Debit

_⚠️ Payment method availability may depend on the sub-entity's region and onboarding status. If a customer asks why a specific payment method is not working, check the sub-entity's status and capabilities first — see__ Article 4._
