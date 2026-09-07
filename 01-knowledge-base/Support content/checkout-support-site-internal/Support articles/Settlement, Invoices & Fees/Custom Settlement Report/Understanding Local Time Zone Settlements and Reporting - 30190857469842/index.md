---
id: 30190857469842
section_id: 21991159537682
title: "Understanding Local Time Zone Settlements and Reporting"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/30190857469842-Understanding-Local-Time-Zone-Settlements-and-Reporting"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-13T13:31:13Z"
permission_group_id: 26838654181266
content_tag_ids: []
label_names: []
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

To understand the local time zone feature for settlements and reports, which addresses reconciliation and liquidity issues for clients by shifting from a default UTC (Coordinated Universal Time) system to a local time zone system.

## DESCRIBE THE ISSUE 💬

Before this feature, all settlements and reports were based on UTC. This created a discrepancy for clients, particularly in the APAC (Asia-Pacific) and US regions, who operate on a different time zone. 

This misalignment caused gaps in cash and local time reconciliation and led to a liquidity gap, as transactions that occurred between the local midnight and the UTC midnight would settle on different days (T+2).

 

## KEY TAKEAWAYS 🔑

**Updating a time zone:** If a merchant wishes to update their timezone they can self-serve through the dashboard, direct them to the [update settlement timezone](https://www.checkout.com/docs/funds-management/receive-settlements/manage-settlements#Update_settlement_time_zone) article.

**Liquidity Impact:** The feature does not change settlement speed (T+X). The only change is that the "end of day" balance shifts from midnight UTC to midnight local time. There is a positive liquidity impact for clients in the US.

## VIEWING SETTLEMENTS & REPORTS 👀

Once a local time zone is configured, settlements and reports will automatically reflect the change.

**Settlements:**

- Settlements for local time zones are generated at 5 a.m. local time, instead of the previous 2 a.m. UTC time.

- The Settlement Details page on the Dashboard will display the timeline in the local time zone. A tooltip will show the time zone (either local or 'UTC').

- The "Settlement creation date" indicates when the settlement was generated and will now reflect the local time.

**Reports:**

- Report generation times have shifted from a fixed UTC schedule to a local time-based schedule.

- 
**Financial Actions by Date Range** and **Balance Statements** are generated at 3 a.m. in the entity's time zone.

- 
**Financial Actions by Payout**, **Payout Summary**, and **Settlement Statements** are generated at 10 a.m. in the entity's time zone.

- All these reports are expected to be available by 12 p.m. local time.

- Timestamps in reports like **ProcessedOn** and **RequestedOn** will now reflect the local time. Optional UTC columns (`ProcessedOnUtc` and `RequestedOnUtc`) are available via a request.

- 
**Invoices** will remain in UTC and will not follow the local time zone configuration. This may cause a discrepancy when reconciling monthly invoices with local time-based financial reports.

## RESOURCES 📍

| Related |
| --- |
| External Articles   - [Impact of changing settlement time zone](https://support.checkout.com/hc/en-us/articles/19748300519186-Impact-of-settlement-time-zone-change-on-Dashboard-reports)  - [Receive settlements](https://www.checkout.com/docs/funds-management/receive-settlements#Settlement_time_zone)  - [APAC settlement time zones](https://support.checkout.com/hc/en-us/articles/28408053624082-Changes-to-your-settlement-time-zone-in-APAC) |

## FAQs** ****❓**

What is the impact of changing a time zone?

Moving to a local time zone will create either a "short" or "extended" settlement for the first settlement period, depending on when the change takes place and the time zone offset. After this initial period, the settlements will return to a normal 24-hour cycle.

- 
**APAC/MENA:** The first settlement will be **shorter**, with a duration of 24 hours minus the UTC offset.

- 
**US:** The first settlement will be **extended**, lasting 24 hours plus the UTC offset.

What happens if a client's entity spans multiple time zones?All "local settlements" for a single Checkout.com (CKO) entity are generated in one batch at 5 a.m. local time, as configured for that entity.Does changing to a local time zone impact settlement speed or liquidity?The new feature does not change when funds become available, so a T+2 merchant will remain T+2. The only change is that the "end of day" balance being settled shifts from midnight UTC to midnight local time. There is a positive liquidity impact for clients in the US.
