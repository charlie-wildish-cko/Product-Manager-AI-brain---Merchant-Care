---
id: 21991154435474
section_id: 21991135647762
title: "Reconcile a Single Invoice"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/21991154435474-Reconcile-a-Single-Invoice"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-09-29T18:00:04Z"
permission_group_id: 26838654181266
content_tag_ids: ["01K4QH2BDBYR4Z8C0ZMABD2R7M"]
label_names: ["case_settlements", "reconciliation_mismatch_queries", "case_settlements_issue_mismatch_in_reconciliation", "mena"]
user_segment_ids: [11003606966930]
archive: false
---

**Use this article when**

Merchants and internal teams notice a mismatch between the amounts on their invoices and the total amounts in their Financial Actions Reports (FARs) and this needs to be reconciled for a single invoice.INTRODUCTION TO RECONCILIATION MISMATCH QUERIES 💬

Merchants and internal teams may notice a mismatch between the amounts on their invoices and the total amounts in their Financial Actions Reports (FARs). This can happen for several reasons, incuding:

- Timing differences in fee application

- Specific fee types not being accounted for in the initial comparison

These discrepancies can lead to questions about billing and account balances, particularly a negative balance on the dashboard.

PROCESS FOR RECONCILIATING A SINGLE INVOICE MISMATCH 🖊️

### Step 1. Identify the Invoice

- Go to the merchant's dashboard

- Navigate to Invoices and locate the relevant invoice

### Step 2. Identify the Date Range

- Open the invoice and note the Invoice period (e.g 01 Mar 2025 - 31 Mar 2025)

### Step 3. Download the Financial Actions Report (FAR)

- Go to the Reports section and download a Financial Actions Report for the exact date range you found on the invoice

Filter the FAR:

- Open the downloaded CSV file

- Filter the Holding Currency column to match the currency on the invoice

- Filter the Breakdown Type column to show only fee-related transactions. Select all options except for 'Capture', 'Payout', and 'Refund'

### Step 4. Calculate the Total Fees:

- Find the Holding Currency Amount column

- Use the SUM function in Excel to calculate the total sum of all the filtered fees in this column

### Step 5. Compare Values

- Compare the total sum from the FAR with the total amount on the invoice

## 

RESOLUTION ⚒️

The figures should match, if they do not:

- Recheck your calculations by performing all the steps again and if they still do not match you must escalate this to the regional billing team to provide a breakdown

- Use the transfer macro to send a support ticket to the regional billing team
