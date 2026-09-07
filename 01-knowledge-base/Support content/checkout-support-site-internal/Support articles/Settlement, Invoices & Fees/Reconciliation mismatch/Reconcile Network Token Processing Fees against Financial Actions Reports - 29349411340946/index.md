---
id: 29349411340946
section_id: 21991159491218
title: "Reconcile Network Token Processing Fees against Financial Actions Reports"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/29349411340946-Reconcile-Network-Token-Processing-Fees-against-Financial-Actions-Reports"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-12-09T09:26:18Z"
permission_group_id: 26838654181266
content_tag_ids: ["01K4QH2BDBYR4Z8C0ZMABD2R7M"]
label_names: ["case_settlements", "reconciliation_mismatch_queries", "mena"]
user_segment_ids: [11003606966930]
archive: false
---

**Use this article when**

Merchants and internal teams notice a mismatch between the amounts on their invoices and the total amounts in their Financial Actions Reports (FARs) and this needs to be reconciled for a single invoice.INTRODUCTION TO RECONCILIATION MISMATCH QUERIES 💬

Merchants and internal teams may notice a mismatch between the amounts on their invoices and the total amounts in their Financial Actions Reports (FARs). This can happen for several reasons, incuding:

- Timing differences in fee application

- Specific fee types not being accounted for in the initial comparison

These discrepancies can lead to questions about billing and account balances, particularly a negative balance on the dashboard.

PROCESS FOR RECONCILIATING NETWORK TOKEN PROCESSING FEES 🖊️

### Step 1. Identify the Issue

- A merchant may inquire about missing "Network Token Provisioning Fixed Fees" on an invoice

### Step 2. Locate the Invoice

-  Find the relevant invoice on the merchant's dashboard. For this example, we will use an invoice for April 2025

- Example invoice: the amount to reconcile is **69.08** AED

 

### Step 3. Note the Amount and Date

- Identify the **Network tokens processing** amount (e.g., 69.08 AED) and the invoice period (e.g., 01 Apr 2025 - 30 Apr 2025)

 

### Step 4. Download the Financial Actions Reports

-  Go to **Reports** and generate a Financial Actions Report for the invoice period

### Step 5. Filter the FAR for Network Tokens:

- Filter column J for **"Network Token Provisioning"** and **"Network Token Update"**

- Scroll to column AE and filter for **"Network Token Provisioning Fixed Fee"** and **"Network Token Update Fixed Fee"**

### Step 6. Calculate and Compare

- Use the SUM function on the filtered **Holding Currency Amount** column and compare the total with the amount from the invoice. The values should be identical.
