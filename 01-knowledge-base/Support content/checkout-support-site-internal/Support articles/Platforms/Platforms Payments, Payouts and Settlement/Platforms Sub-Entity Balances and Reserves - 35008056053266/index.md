---
id: 35008056053266
section_id: 35005877878290
title: "Platforms: Sub-Entity Balances and Reserves"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/35008056053266-Platforms-Sub-Entity-Balances-and-Reserves"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-04-22T11:15:13Z"
permission_group_id: 26838654181266
content_tag_ids: []
label_names: []
user_segment_ids: [11003606966930]
archive: false
---

This article explains the five balance types that a sub-entity's account can hold, how to retrieve balances, what a reserve is, why Checkout.com applies reserves, and how to look up a sub-entity's reserve rule.

**High ticket risk: Sub-entities frequently ask why some of their funds aren't available. Understanding balance types and reserve rules is essential for answering these queries.****Balance types explained**

A sub-entity's account holds funds in different buckets depending on their state. Here is what each one means:

| **Balance type** | **What it means** | **Can it be paid out?** |
| --- | --- | --- |
| Pending | Funds from captured payments that haven't yet become available. They're held while Checkout.com waits for the settlement window to close. | Not yet |
| Available | Funds that have passed their settlement speed window and are ready to be settled or paid out. | Yes - subject to minimum threshold |
| Payable | Funds that have been moved from Available and are queued for payment to the sub-entity's bank account. | In progress |
| Collateral | Funds held as a reserve (see reserve rules below). These are held by Checkout.com to cover potential chargebacks or refunds. | No - held until the reserve period ends |
| Operational | Funds used for operational purposes — for example, to cover fees or adjustments. | No - managed by Checkout.com |

**How to retrieve sub-entity balances**

The platform calls the Retrieve Entity Balances endpoint (GET), passing the sub-entity ID.

The response returns the current amounts across all five balance types for each holding currency.

[Technical docs.](https://www.checkout.com/docs/platforms/for-saas/manage-sub-entity-balances)
**What is a reserve?**

A reserve is a portion of a sub-entity's funds that Checkout.com holds back from the Available balance. This is a risk management mechanism.

Checkout.com uses reserves to protect against:

- Chargebacks — when a customer disputes a payment and the funds need to be returned

- Refunds — when a sub-entity issues a refund and the funds need to be covered

- Other costs Checkout.com may become liable for on behalf of the sub-entity

Funds in the Collateral balance are the sub-entity's money — but Checkout.com holds them for a defined period before releasing them. Once the holding period ends, they move to the Available balance.
**Rolling reserve — how it works**

The most common reserve type is a rolling reserve. Checkout.com holds back a percentage of captured funds for a set number of weeks. After that period, the held funds roll into the Available balance.

Example: a 10% rolling reserve held for two weeks. For every $100 captured, $10 goes to the Collateral balance. Two weeks later, that $10 moves to Available and can be settled.
**How to retrieve reserve rule details**

The platform calls the Get Reserve Rule Details endpoint (GET), passing both the sub-entity ID and the reserve rule ID.

The response shows:

- The reserve type (for example, rolling)

- The percentage held

- The holding duration (in weeks)

- The date the rule came into effect

[Technical docs.](https://www.checkout.com/docs/platforms/for-saas/manage-sub-entity-balances)
**Troubleshooting / common questions**

**Q: A sub-entity says they're missing funds — the numbers don't add up.**

Check all five balance types. Funds may be in Pending (not yet available), Collateral (held under a reserve), or Payable (being processed). Walk through each balance type with the customer before escalating.

**Q: A sub-entity is asking why Checkout.com is 'holding their money'.**

Explain that the Collateral balance is a reserve — a common risk management practice for payment processors. Checkout.com holds a percentage of captured funds for a fixed period to cover potential chargebacks or refunds. The funds are not lost — they will be released once the holding period ends. Direct the customer to retrieve their reserve rule details to see the exact percentage and timeline.

**Q: A platform wants to know when reserve funds will be released.**

Retrieve the reserve rule using the API. The holding_duration field shows how many weeks the funds are held. Count from when each batch of funds was captured to calculate when they'll be released.

**Q: A customer wants to dispute or reduce their reserve.**

Reserve rules are set by Checkout.com's risk team. The platform cannot change these via the API. Escalate to the account manager.
