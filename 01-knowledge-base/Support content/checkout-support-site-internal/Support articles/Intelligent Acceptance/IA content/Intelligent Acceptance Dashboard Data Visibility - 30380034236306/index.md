---
id: 30380034236306
section_id: 29824613373714
title: "Intelligent Acceptance Dashboard Data Visibility"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/30380034236306-Intelligent-Acceptance-Dashboard-Data-Visibility"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-12-09T10:19:42Z"
permission_group_id: 26838654181266
content_tag_ids: ["01KA9E1ZFZVTJQYGHHBKN624CR"]
label_names: ["L2", "IA", "IA_dashboard"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

To understand the **key performance metrics** displayed on the external **Checkout Dashboard for Intelligent Acceptance (IA)** and to troubleshoot common data visibility issues such as "Still Observing," "No Boost Observed," or a missing "Optimizations Applied" section.

**Problem:** Intelligent Acceptance Dashboard metrics are not visible or show a non-final status.

## TOOLING**📍**

 

**Checkout Dashboard ******[here](https://dashboard.checkout.com/)

Access via [jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274) 

## IA DASHBOARD INTRODUCTION 💬

The Checkout Dashboard is the primary tool for communicating IA performance data directly to the merchant. It is designed to be a clear, high-level overview of the benefit of using the IA service.

The dashboard displays the following key metrics and shows their evolution over time:

- Merchant AR: The merchant's overall Acceptance Rate, inclusive of the AR Boost

- AR Boost: The increase in Acceptance Rate that is a direct result of IA

- Transactions Optimised: The total number of transactions where at least one optimisation was applied (regardless of outcome of the transaction)

- Revenue Boost: An estimate of the revenue generated from transactions that were accepted due to IA's optimisations

 

At the bottom of the dashboard, the "Optimizations Applied" section breaks down IA services contributing to the metrics, highlighting the impact of optimizations like 3DS, Network Tokens, messaging, and retries.

The Optimized transactions view shows the number of optimized transactions over time.

## Issue Details

The merchant is viewing the external Checkout Dashboard for Intelligent Acceptance (IA) and notices that some key metrics, specifically the AR Boost and Revenue Boost, display a status like "Still Observing" or "No Boost Observed". 

Alternatively, the "Optimizations Applied" section may be missing or show no data. This prevents them from seeing a clear, complete overview of the benefit and performance of the IA service.

## KEY TAKEAWAYS 🔑

- The Checkout Dashboard's main purpose is to give merchants a clear, high-level view of IA's performance and benefits.

- Key metrics shown include Merchant AR, AR Boost, Transactions Optimised, and Revenue Boost.

- The "Optimizations Applied" section breaks down which IA services (like 3DS, Network Tokens, or retries) contributed to the metrics.

- "Still Observing" typically means the selected period is ongoing or the system is still collecting enough data for statistical confidence.

- "No Boost Observed" means there wasn't enough statistical confidence to determine if the measured impact was actually due to IA, or the merchant may not meet eligibility criteria.

- If basic troubleshooting (changing the time period) doesn't resolve a "No Boost Available" issue, it requires internal investigation and escalation.

TOOLING**📍**

| Tools | Access |
| --- | --- |
| [Checkout.com Dashboard](dashboard.checkout.com) **Environment: **Sandbox and Production | **Permissions: **Super User (both environments) - Super Admin ( sandbox only) ** Access granted via ******[jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274) |

 

## PROCESS FOR DASHBOARD DATA VISIBILITY ISSUES 🖊️

### Step 1. Understand the Missing Data Status

Check the status displayed on the dashboard for the missing metrics (AR Boost, Revenue Boost) and the Optimizations Applied section.

## "Still Observing" Status 👀

**What it means: **This status appears on the “**Boost from optimizations”** and **“Estimated** **revenue boost”** metrics, as well as on the tooltip for a given week/month, whenever the selected period is still ongoing (“This quarter”, “This month”).

**Reason**:

- The time period is not yet complete (e.g., current week/month)

- The merchant was recently onboarded (in the last few days) and the system is still assessing the appropriate time window

## "No Boost Observed" Status ❌

**What it means**: This status appears on the “Boost from optimizations” and “Estimated revenue boost” metrics, as well as on the tooltip for a given week/month, whenever it was not possible to determine IA impact.

**Possible Reasons**:

- The selected time frame lacks the statistical confidence needed to attribute the impact directly to IA (noise/other changes could be the cause)

- The merchant doesn't meet the eligibility criteria, preventing statistical confidence from being reached

## “Optimizations Applied” Section Is Not Showing / Not Showing Data 📉

**What it means**: This section will not show data when no Acceptance Rate (AR) boost is observed for the selected period.

**Possible reasons:**

- There was an internal error in retrieving the data required, and the entire section will fail to load.

- There is no statistical significance in the results for the selected period, and no data per section will show.

### Step 2. Troubleshoot by Adjusting the Time Period

The most common resolution for data visibility issues is to adjust the time frame, as the issue is often related to incomplete data or lack of statistical significance for the selected view.

Select a different time period: Advise the merchant to select a completed time period (e.g., last month instead of "This month" or "This quarter") to resolve the "Still Observing" status.

💡 Please note you can only select the pre-defined time windows.

Test a different period for Boost/Optimizations: Ask the merchant to choose a different period where they are known to have an AR boost to check if the data loads.

Test a shorter period for errors: If the "Optimizations Applied" section fails to load entirely, try reloading the page with a shorter time period to assess if there is an underlying loading error.

## RESOLUTION ⚒️

The issue is resolved when the expected metrics and sections are fully visible to the merchant.

## ESCALATION** ⏫**

Escalate the issue if the merchant's dashboard still shows "No Boost Available" (which includes "No Boost Observed" and lack of data due to no boost) _after_ ruling out the above reasons (i.e., you have tested different, completed time periods).

**Situations Requiring Escalation:**

- The dashboard consistently shows "No Boost Observed" across multiple, completed time periods.

- Troubleshooting steps, such as changing the time period, did not resolve the loading error for the "Optimizations Applied" section.

**Escalation Process:**

- The agent must first investigate possible reasons using the internal Intelligent Acceptance Retool dashboard.

- If the Retool investigation doesn't resolve the issue, escalate to intelligent acceptance via [jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277)

## FAQs** ****❓**

What is the difference between "Still Observing" and "No Boost Observed"?"Still Observing" is typically a temporary status meaning data is incomplete or the current period is ongoing. "No Boost Observed" is a conclusion that, for the selected period, IA's impact could not be statistically confirmed or the merchant may not be eligible.What does it mean for the data to lack "statistical confidence"?Statistical confidence means the system is not certain enough that the observed positive impact is definitely the result of Intelligent Acceptance optimisations, rather than "noise" or other changes in the payment flow.
