---
id: 21991190413714
section_id: 21991144826258
title: "Fee Breakdown Queries on NAS"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/21991190413714-Fee-Breakdown-Queries-on-NAS"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:33:44Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHQKPVKA7XAZRYSRWE7JRH4"]
label_names: ["case_settlements", "case_settlements_issue_fees_charged_for_transaction", "mena", "transaction_fees_queries"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

To investigate and provide a detailed fee breakdown for a merchant's transactions using the Financial Actions report on Looker.

**Problem:** A merchant is questioning the fees applied to their transactions

**Solution:** Use the Financial Actions report in Looker to provide a transparent itemized breakdown of all fees
DESCRIBE THE ISSUE 💬

A merchant has contacted support to query the fees they have been charged. They want a clear, itemized breakdown of the fees applied to specific transactions. 

⚠️ For **MBC**** **merchants, a ticket needs to be raised with the Cost of Sales Operations team [schemepricingandinterchange@checkout.com](mailto:schemepricingandinterchange@checkout.com)

PROCESS FOR FEE BREAKDOWN RESOLUTION 🖊️
1. Access the Financial Actions Report

- Open the Financial Actions report on Looker

2. Filter the Report

- In the filter section, apply the following settings:

  - 
**Date Range:** Select the specific date range for the merchant's query. This can be a specific year or a custom range.

  - 
**Client Name:** Choose the merchant's name from the drop-down menu.

  - 
**Fee Type:** Set this to both `Scheme` and `Interchange`.

  - 
**Note:** Interchange data is subject to a one-day lag and will not appear for transactions processed on the current day.

  - 
**Financial Action Type:** Select both `Fee` and `Capture`.

  - 
**Action Group ID:** If the merchant has provided specific payment IDs, enter them into this filter.

3. Analyze the Results

- Once the search results are displayed, interpret the following columns to answer the merchant's query:

  - 
**Action Type:** This shows the transaction type (e.g., `authorization`, `capture`, `card verification`, `Void`) on which the fee was applied.

  - 
**Fee Detail:** This provides a description of each individual fee charged.

  - 
**Total Processing/Holding Amount:** This column shows the exact amount of each fee for the transaction.

  - 
**Note:** Rows with `Financial Action Type = "Fee"` represent the fees, while rows with `Financial Action Type = "Capture"` represent the transaction's processing volume.

### RESOLUTION ⚒️

Following these steps will produce a detailed, itemized list of all fees associated with the specified transactions. You will be able to provide the merchant with a clear breakdown, explaining each charge as listed in the `Fee Detail` column. The resolution is confirmed when the data provided matches the merchant's inquiries and provides a satisfactory explanation.

 

### ESCALATION ⏫

If the merchant’s query falls outside the scope of this SOP or is highly complex, Merchant Care should raise this with the FTS L2 team. They have access to the required level of fee granularity to answer these queries.

**Required Information:**

- A clear description of the issue

- All steps taken, including the filters used in Looker

- Screenshots of the report results

- The merchant's name, case number, and a list of the specific transaction IDs in question
