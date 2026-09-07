---
id: 35761991854482
section_id: 16339901521682
title: "What changes is Mastercard making to its scam monitoring program?"
url: "https://support.checkout.com/hc/en-us/articles/35761991854482-What-changes-is-Mastercard-making-to-its-scam-monitoring-program"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-05-21T08:47:44Z"
permission_group_id: 11003577394706
content_tag_ids: []
label_names: ["Platforms - Sub-merchant onboarding - Merchant activation and verification"]
user_segment_ids: []
archive: false
---

Mastercard is updating their potential scam merchant monitoring standards from July 24, 2026.

Once these changes take effect, Checkout.com and our payment facilitators must investigate merchants within 72 hours if they meet the following conditions.

## **For new merchants**

_Mastercard defines new merchants as having less than six months of Mastercard transaction processing history, processing more than 500 transactions per month._

- More than 5% of purchases result in refunds and chargebacks combined over a rolling 30-day period, or
- Two separate issuers report at least one transaction using fraud type 56 - manipulation of cardholder, or
- Two or more issuers raise fraud or non-fraud chargebacks where the supporting documentation mentions a scam, manipulation, or similar terms

## **For all merchants**

- The merchant’s authorization approval rate drops by at least 50%, or below 30%, over a 72-hour period where the merchant processed more than 25 purchase transactions (BIN attacks and acquirer / system outages don’t count towards this threshold), or
- Checkout.com receives a Global Rules Investigation Processing (GRIP - Mastercard’s monitoring program designed to address high fraud and suspected scams) letter from Mastercard, linking a merchant to suspected scam activity, or
- Checkout.com receives alerts from a Merchant Monitoring Service Provider identifying a potential scam merchant or a merchant potentially conducting illegal activity

## **What happens following an investigation?**

Checkout.com will investigate the flagged merchant to assess if they are potentially conducting scams. If we believe that a scam is taking place, we must immediately stop the merchant from processing any Mastercard and Maestro transactions.

## **What about false positives?**

False positives are possible under the program. If we are satisfied that no scam activity has taken place, we’ll continue processing as normal, but the merchant will remain under ongoing monitoring and could be flagged in the future.

## **What do payment facilitators need to do?**

The most important thing for payment facilitators is to educate your merchants about the program, including key metrics and how to avoid misleading practices during the payment process. You may wish to:

- Review how other payment facilitators have communicated these changes to their sub-merchants
- Publish informational blogs for your customers
- Send your customers an email or notification alert
- Advise them on which products can help proactively manage disputes and fraud
- Provide advice on best practices for receipts, refund and cancellation policies, subscription policies, and billing descriptor management 
- Train your support teams on how to manage merchant inquiries about the program 

If you have any questions about how these changes will affect your business, please don’t hesitate to reach out to your Account Manager.

## **Frequently asked questions**

**Why has Mastercard included refunds in the 5% threshold for new merchants?**

Traditionally, monitoring programs focused only on chargebacks. However, high refund rates can be a leading indicator of scams e.g. a merchant is trying to avoid chargeback alerts by quickly refunding customers, or customers are constantly requesting money back due to misleading marketing.

Mastercard now views high refund volume as a potential signal of deceptive practices.

**What is fraud type 56 – manipulation of cardholder?**

This is a Mastercard fraud category that indicates that the cardholder authorized the transaction but was tricked by the merchant. Examples include investment, romance, and purchase scams.

**If a merchant’s authorization rate drops due to a technical issue, will they be monitored?**

No. Mastercard has specified that acquirer or system outages and BIN attacks are excluded from their calculations.

**What is required for an acquirer if a merchant triggers the investigation threshold?**

Within 72 hours, we must initiate and conduct a meaningful review. This typically involves reviewing the merchant’s website for misleading claims, analyzing the merchant’s recent transaction patterns, and requesting clarification or documentation from the merchant.

By the end of the investigation window, we must have a preliminary determination – either confirmed scam, which requires immediate cessation of Mastercard and Maestro transactions, or legitimate merchant, which requires ongoing monitoring.

**If a merchant is confirmed as legitimate, does Checkout need to report this to Mastercard?**

Mastercard will require us to maintain a record of our investigation and the rationale for why we believe the merchant is legitimate. This is critical to prove we performed due diligence if the merchant breaches a threshold in the future.

**Does the ‘new merchant’ status reset if they change their business name or MCC?**

Mastercard looks at processing history. For the purposes of the program, the six month clock starts from the date of the first Mastercard transaction processed under that specific merchant identity.

**If Checkout terminates a merchant for scam activity, do we have to add them to the MATCH list?**

Yes. If we confirm that a merchant engaged in scam or fraudulent activity, we must follow standard industry procedures, including reporting the merchant to the MATCH database.
