---
id: 29350197272466
section_id: 21991135647762
title: "How to Identify and Reconcile a Negative Balance"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/29350197272466-How-to-Identify-and-Reconcile-a-Negative-Balance"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-14T14:27:55Z"
permission_group_id: 26838654181266
content_tag_ids: ["01K4QH2BDBYR4Z8C0ZMABD2R7M"]
label_names: ["case_settlements", "reconciliation_mismatch_queries", "mena", "Settlement invoices and fees - Reconciliation mismatch"]
user_segment_ids: [11003606966930]
archive: false
---

**Use this article when**

A payment hasn't settled and you need to investigate the reason, this can be a symptom of a negative balance. This issue is typically caused by fees processed after the most recent payout.

This article will help you identify a negative balance and guide you on reconciliation.INTRODUCTION TO RECONCILIATION MISMATCH QUERIES 💬

A negative dashboard balance typically occurs when fees are processed and deducted from the account after a payout has been completed. 

⚠️ The balance will remain negative until new transactions generate a positive balance or until the fees are settled.

⭐️ Merchant Self Serve Action: [how to add funds via Dashboard](https://www.checkout.com/docs/funds-management/move-funds/add-funds)

PROCESS FOR RECONCILING NEGATIVE BALANCES 🖊️

Example of a problem description from the ticket

### Step 1. Identify the Negative Balance

- Navigate to the merchant's dashboard and go to Business account > Balances

- Note the negative balance amount and currency

### Step 2. Download the Financial Actions Report

- Generate a Financial Actions Report for the current month

### Step 3. Find the Last Payout

- Open the FAR and filter the Requested On column by the most recent date

- In the Breakdown Type column find the last 'Payout' entry

- Consider all fees processed after this payout

- In this example only an interchange fixed fee of ( -0.468 ) was applied and if you round off -0.468 to 2 decimal places, you will get** -0.47**.

### Step 4. Sum the Fees

- Sum all the fee-related transactions that occurred after the last payout

### Step 5. Compare

- The sum of these fees should match the negative balance on the dashboard

ESCALATION ⬆️

If you cannot reconcile the amounts using the steps above, the issue may require further investigation.

**For negative balance issues (terminated or inactive merchants)**

-  Use this [Looker report](https://checkoutinternal.eu.looker.com/explore/ledger_financial_actions/finance_financial_actions_report?toggle=fil&qid=ReMu12nYJckZcxZed4A9FK)

- Open the provided Looker link and add the currency account ID

- Set the date filter to the last settlement date found in the dashboard's **Settlements** section

- Run the report, sum the values in column M, and compare the total to the negative balance

- If they do not match, escalate to the next level of support with the Looker report details
