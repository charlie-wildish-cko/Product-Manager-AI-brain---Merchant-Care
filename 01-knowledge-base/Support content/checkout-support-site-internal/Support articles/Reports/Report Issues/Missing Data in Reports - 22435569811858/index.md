---
id: 22435569811858
section_id: 22329315187858
title: "Missing Data in Reports"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22435569811858-Missing-Data-in-Reports"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-09-17T16:09:07Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQBAM2Q5EGSKD3634VFBT"]
label_names: ["global", "case_reports", "mismatch_or_missing_data", "case_reports_issue_mismatch_missing_data", "data\\-discrepancy", "missing_data", "mismatched_data", "discrepancy"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article **

To investigate and resolve issues when a merchant reports a discrepancy or missing data in their reports. 

**Problem** - A merchant's report shows missing or incorrect data compared to their internal records

**Solution** - Investigate common causes like timezone differences or reporting lags and provide the merchant with actionable steps to resolve the discrepancyDESCRIBE THE ISSUE 💬

A merchant has contacted support to report a discrepancy in their financial reports, stating that certain payments or transactions are either missing or incorrect. This issue affects the merchant's ability to reconcile their financial data. KEY TAKEAWAYS 🔑

- Check for common causes first, such as timezone differences, reporting delays, or transaction status mismatches

- Escalate the case to L2 support if the problem is systemic, affects many transactions, or if you can't identify a clear cause.

PROCESS FOR RESOLVING DATA DISCREPANCIES 🖊️Step 1. Gather Initial Information 

Begin by acknowledging the merchant's concern and reassuring them that you will help them. To expedite the investigation, request the following specific details:

- The exact name of the report and the date/time range of the discrepancy

- Specific examples of missing or incorrect transactions, such as `payment_id` values

- A description of the expected data versus what is actually shown

- The source they are using for comparison (e.g., internal system, third-party app)

Step 2. Investigate and Form an Initial Hypothesis 

Use the information provided by the merchant to query internal systems and identify the root cause. Check for these common issues:

- 
**Timezone Discrepancy:** Our reports default to UTC, while the merchant's system may use a different timezone

- 
**Reporting Lag:** Advise the merchant that some reports may have a slight delay and ask them to wait a few minutes and refresh

- 
**Transaction Statuses:** Confirm if the merchant's report includes all transaction statuses (e.g., `authorized`, `captured`, `voided`)

- 
**API vs. Dashboard Discrepancy:** If they are using both, check if the data is being pulled from different endpoints or reports

Step 3. Communicate Findings and Provide Actionable Steps

 Once you have a conclusion, report back to the merchant promptly. Provide clear, actionable steps using bullet points or a numbered list:

- 
**Example (Timezone):** "Our reports are in UTC by default. Could you adjust your report to UTC to see if the numbers align?".

- 
**Example (Status Mismatch):** "Upon reviewing `pay_xxxxxx`, I see it has an `authorized` status but hasn't been `captured` yet. Please check if your report is set to include all transaction statuses".

- Document the entire conversation and your findings in an internal note on the case.

Step 4. Offer Guidance and Escalate When Needed 

Provide the merchant with proactive advice to prevent future issues:

- For reconciliation, recommend using the **Reconciliation Report** as the primary source of truth

- For integration, suggest ensuring that their webhook endpoint is configured to receive all event types for real-time updates

RESOLUTION ⚒️

Following these steps should help the merchant resolve the discrepancy. The expected result is that the data in their report will align with the data in our system after they apply the recommended fixes (e.g., adjusting the timezone or report settings).

- 
 
**Remediation Steps:** Guide the merchant to check their report settings, such as timezone, transaction statuses, and data sources.

- 
**Check that the problem is fully resolved:** Ask the merchant to confirm if the discrepancy is gone after applying the steps.

ESCALATION ⏫

- 
**Situations requiring escalation:** If your initial investigation does not find a clear cause, or if the issue is systemic and affects a large number of transactions.

- 
**Required information:** The Zendesk case number, details of the merchant's request, your investigation findings, and any relevant `payment_id` examples.

- 
 
**Instructions for the agent:** Inform the merchant that the investigation may take longer and that you will provide an update as soon as you have more information. Stay on the case and monitor for updates.

- 
**How to follow up and when to chase:** Set an internal reminder to follow up with the L2 team within a reasonable timeframe (e.g., 24-48 hours) if you haven't received an update.
