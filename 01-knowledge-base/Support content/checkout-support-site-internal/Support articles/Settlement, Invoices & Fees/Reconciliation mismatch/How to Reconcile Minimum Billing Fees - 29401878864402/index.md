---
id: 29401878864402
section_id: 21991159491218
title: "How to Reconcile Minimum Billing Fees"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/29401878864402-How-to-Reconcile-Minimum-Billing-Fees"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T09:17:11Z"
permission_group_id: 26838654181266
content_tag_ids: ["01K4QH2BDBYR4Z8C0ZMABD2R7M"]
label_names: ["case_settlements", "reconciliation_mismatch_queries", "case_settlements_issue_mismatch_in_reconciliation"]
user_segment_ids: [11003606966930]
archive: false
---

**Use this article when**

A merchant has reached out because they've been charged a Minimum Billing Fee that doesn't seem to align with their expected amount.

INTRODUCTION TO RECONCILE MINIMUM BILLING FEES 💬

The merchant has calculated a different minimum billing fee based on their invoice, and they're asking for clarification on how the fee is calculated. Follow the steps below to reconcile the Minimum Billing Fee and provide a clear explanation to the merchant.

💡 Financial actions (or balance) reports should be downloaded from the merchant dashboard for the month in consideration.

Case example:

PROCESS FOR RECONCILING MINIMUM BILLING FEES 🖊️Step 1: Verify the Minimum Billing Amount in Client Admin Tool (CAT)

1. Go to CAT and search for the merchant:-

2. 
Select the merchant and navigate to the "Minimum billing" section:- 

3. 
Check the **Minimum Income Amount** and **Minimum Income Currency** to confirm the configured fee. In this example case, the amount is USD 7,500:-

Step 2: Identify the Relevant Month 

1. Identify the month for which the merchant was charged the Minimum Billing Fee. The merchant will usually provide this information in their communication or a copy of their invoice.
⚠️**Warning:** If the merchant hasn't provided this information, you must ask them to confirm which month's invoice contains the fee. Step 3: Set the Date in the Looker Report 

1. Open the [Looker report](https://checkoutinternal.eu.looker.com/explore/ledger_financial_actions/finance_financial_actions_report?qid=prMmjpzxXzz2tRQ8mm7Bl8)

2. Set the date range to the month _before_ the invoice month. Minimum Billing fees are always calculated based on the previous month's activity and charged on the next available invoice

3. 
In the example case, the fee was on the September invoice, so set the Looker report date range for
**August 2025**

Step 4: Download and Analyse the Report 

1. Run the report and download the results as a CSV file

2. Open the CSV and look at column **M**, "Total Holding Amount (Holding Currency)". This column shows the actual processing fees for the previous month (in our example, the total amount is $1,698.22):-

Step 5: Calculate the Fee and Reconcile 

1. Subtract the total processing fees from the Looker report (column M) from the Minimum Billing amount configured in CAT

2. Example **Calculation:** Minimum Billing Amount ($7,500) - Total Processing Fees ($1,698.22) = **$5,801.78** which matches the fee the merchant was charged, successfully reconciling the amount

ESCALATION ⬆️If the calculated amount does not match the amount the merchant was charged, or if you encounter discrepancies in the data, escalate the case to the appropriate finance team.Provide a clear summary of your findings, including:

- Merchant Name

- Invoice Date

- Expected Amount

- Calculated Amount

FAQ's ⁉️**Q: Why is the Minimum Billing Fee charged on the next month's invoice?****A:** The fee is charged on the next available invoice because it is calculated based on the previous month's card processing fees. For example, a fee computed for January's processing fees would appear on the February invoice.
