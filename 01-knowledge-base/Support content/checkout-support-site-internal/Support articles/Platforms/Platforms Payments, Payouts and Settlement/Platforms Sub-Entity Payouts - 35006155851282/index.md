---
id: 35006155851282
section_id: 35005877878290
title: "Platforms: Sub-Entity Payouts"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/35006155851282-Platforms-Sub-Entity-Payouts"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-04-22T10:14:02Z"
permission_group_id: 26838654181266
content_tag_ids: []
label_names: []
user_segment_ids: [11003606966930]
archive: false
---

This article explains the two types of payouts available for sub-entities - bank payouts and card payouts, and the difference between on-demand and scheduled payouts.**What is a payout?**

A payout is the transfer of funds from a sub-entity's Checkout.com account to an external account - either a bank account or a card. Payouts are separate from settlements (see Article 8). The key difference is:

|  | **Settlement** | **Payout** |
| --- | --- | --- |
| What it is | Automatic transfer of captured payment funds to the sub-entity's bank account on a schedule | Manual or on-demand transfer instructed by the platform |
| Who controls timing | Configured schedule (daily, weekly, monthly) | Platform instructs when to send |
| Destination | Bank account only | Bank account or card |

**Bank payouts**

Bank payouts transfer funds from the sub-entity's Checkout.com account to a verified bank account.

Bank payouts can be:

- 
**On-demand:** The platform instructs a payout immediately, outside of the regular settlement schedule.

- 
**Scheduled:** Payouts happen automatically at a set frequency — daily, weekly, or monthly. See Article 8 for how to configure a settlement schedule.

[Technical docs.](https://www.checkout.com/docs/platforms/for-saas/process-sub-entity-payouts/process-sub-entity-bank-payouts)**Card payouts**

Card payouts transfer funds to a card (debit card). Card payouts are on-demand only — there is no scheduled option for card payouts.

[Technical docs](https://www.checkout.com/docs/platforms/for-saas/process-sub-entity-payouts/process-sub-entity-card-payouts).**Payout summary**

| **Payout type** | **On-demand?** | **Scheduled?** | **Destination** |
| --- | --- | --- | --- |
| Bank payout | Yes | Yes | Bank account |
| Card payout | Yes | No | Card (debit) |

**Troubleshooting / common questions**

**Q: A customer wants to know why they can't set up a scheduled card payout.**

Card payouts are on-demand only. Scheduled payouts are only available for bank payouts. This is a product limitation, not a configuration issue.

**Q: An on-demand payout was instructed but funds haven't arrived.**

Check the sub-entity's Payable balance first — there need to be sufficient funds available. Also check whether any minimum balance threshold (threshold field) is set on the payout schedule that may be blocking the payout. See Article 9 for balance types.

**Q: A customer asks why a payout didn't go out on the expected day.**

Check the settlement schedule configuration and whether the scheduled day fell on a non-business day. If it did, the payout moves to the next business day. See Article 8 for detail on schedules and non-business day handling.
