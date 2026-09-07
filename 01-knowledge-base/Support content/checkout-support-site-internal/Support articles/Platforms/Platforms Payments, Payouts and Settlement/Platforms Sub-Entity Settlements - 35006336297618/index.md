---
id: 35006336297618
section_id: 35005877878290
title: "Platforms: Sub-Entity Settlements"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/35006336297618-Platforms-Sub-Entity-Settlements"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-04-22T10:18:17Z"
permission_group_id: 26838654181266
content_tag_ids: []
label_names: []
user_segment_ids: [11003606966930]
archive: false
---

This article explains the full settlement lifecycle, settlement time zones, settlement schedules, settlement speed (T+X), currency holidays, and how to configure and retrieve a sub-entity's settlement schedule.

**⚠️ High ticket risk: Settlement delays, time zones, and T+X calculations are a common source of confusion. Read this article carefully and understand the balance lifecycle before handling settlement queries.****The settlement lifecycle**

Funds move through four stages from payment capture to bank account:

| **Stage** | **Balance type** | **What it means** |
| --- | --- | --- |
| 1. Payment captured | Pending | Checkout.com has collected the funds from the customer. A date is set for when they become available. The sub-entity cannot use these funds yet. |
| 2. Funds become available | Available | Every day at midnight in the sub-entity's settlement time zone, funds that have become available move from Pending to Available. Payments processed on non-business days are included in the next business day's batch. |
| 3. Settlement generated | Payable | When the sub-entity's next scheduled settlement is generated, the Available balance moves to Payable. Funds are now queued for payment. |
| 4. Paid to bank account | Paid out | The Payable balance is transferred to the sub-entity's bank account. The platform can also instruct this on-demand. |

**Settlement time zones**

Each sub-entity has a settlement time zone that determines when their daily Pending-to-Available batch runs. By default, this is set to the sub-entity's local time zone.

| **Time zone setting** | **When funds move from Pending to Available** | **When settlements are generated** |
| --- | --- | --- |
| UTC | Midnight UTC | 2:00 AM UTC |
| Any other time zone | Midnight local time | 5:00 AM local time, based on the Checkout.com regional entity the platform is contracted with |

This means a sub-entity set to UTC and one set to US/Eastern will have their funds batch at different real-world times. If a customer says funds haven't moved when they expected, check the time zone setting.**Settlement schedules**

The platform configures how often each sub-entity receives their settlement payout. Options:

- Daily — every weekday, excluding non-business days

- Weekly — a specific weekday of the platform's choice, excluding non-business days

- Monthly — the 1st or 15th of each month

If a scheduled payout date falls on a non-business day (weekend or public holiday in the sub-entity's settlement time zone), the payout is automatically moved to the next business day.**Settlement speed (T+X)**

Settlement speed is the time between when a payment is made and when the funds become Available. It's shown as T+X:

- **T** = the transaction date

- **X** = the number of business days after the transaction that funds become Available

Example: a payment is processed on Tuesday with a T+2 settlement speed. The funds become Available on Thursday. If the sub-entity's schedule is daily, they receive the funds on Thursday. If weekly on Fridays, they receive them on Friday.

Settlement speed varies by currency and can range from a few minutes to several days. The platform agrees their settlement speed with Checkout.com as part of their contract.**Currency holidays**

A currency holiday is a day when local banks do not process transactions in a specific currency. Currency holidays can delay settlement speed beyond the standard T+X.

For USD settlements, currency holidays are based on US banking holidays. If a currency holiday falls within the T+X window, funds become Available later than expected.

**When a customer reports a settlement delay, always check whether a currency holiday may be the cause before escalating.****How to retrieve a sub-entity's settlement schedule**

The platform calls the Retrieve a Sub-Entity's Payout Schedule endpoint (GET), passing the sub-entity ID.

The response shows:

- Whether the schedule is enabled

- The payment instrument ID used for payouts

- The frequency (daily, weekly, monthly) and day

- The minimum balance threshold — payouts are only triggered if the Available balance meets this threshold

[Technical docs.](https://www.checkout.com/docs/platforms/for-saas/manage-sub-entity-settlements)**How to update a sub-entity's settlement schedule**

The platform calls the Update a Sub-Entity's Payout Schedule endpoint (PUT), passing the sub-entity ID and the updated values.

Fields that can be updated:

- Whether the schedule is enabled or paused

- The minimum balance threshold (threshold) — if the Available balance is below this, the payout won't trigger

- The payment instrument ID used for payouts

- The frequency and day of the week or month

[Technical docs.](https://www.checkout.com/docs/platforms/for-saas/manage-sub-entity-settlements)**Minimum balance thresholds**

Each payout schedule has a threshold value. If the sub-entity's Available balance is below this amount, the scheduled payout does not trigger — even if it's the correct day.

This is a common cause of 'why didn't we get paid today' queries. Always check the threshold value and compare it to the Available balance when investigating a missed payout.**Troubleshooting / common questions**

**Q: A customer says their sub-entity didn't receive their settlement on the expected day.**

Check in order: 

1) Was the expected day a non-business day? 

2) Did a currency holiday fall within the settlement window? 

3) Is the sub-entity's Available balance above the minimum threshold? 

4) Is the payout schedule enabled?

 

**Q: A customer can't work out why funds are showing as Pending for longer than expected.**

Check the settlement speed (T+X) for the currency. If a currency holiday falls in the window, funds take longer to become Available. This is not a bug — it's expected behaviour.

**Q: A customer says they changed the settlement schedule but it hasn't taken effect.**

The updated schedule applies from the next settlement cycle. Changes do not apply retroactively to funds already in the settlement pipeline.
