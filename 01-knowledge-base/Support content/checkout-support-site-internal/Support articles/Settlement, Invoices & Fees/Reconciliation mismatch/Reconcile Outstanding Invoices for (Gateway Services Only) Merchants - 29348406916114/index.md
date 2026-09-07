---
id: 29348406916114
section_id: 21991159491218
title: "Reconcile Outstanding Invoices for (Gateway Services Only) Merchants"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/29348406916114-Reconcile-Outstanding-Invoices-for-Gateway-Services-Only-Merchants"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-12-09T09:24:03Z"
permission_group_id: 26838654181266
content_tag_ids: ["01K4QH2BDBYR4Z8C0ZMABD2R7M"]
label_names: ["case_settlements", "mena", "Settlement invoices and fees - Reconciliation mismatch"]
user_segment_ids: [11003606966930]
archive: false
---

**Use this article when**

Gateway Services Merchants and internal teams notice a mismatch between the amounts on their invoices and the total amounts in their Financial Actions Reports (FARs) and this needs to be reconciled.INTRODUCTION TO RECONCILIATION MISMATCH QUERIES 💬

Merchants and internal teams may notice a mismatch between the amounts on their invoices and the total amounts in their Financial Actions Reports (FARs). This can happen for several reasons, incuding:

- Timing differences in fee application

- Specific fee types not being accounted for in the initial comparison

These discrepancies can lead to questions about billing and account balances, particularly a negative balance on the dashboard.

**⚠️ Note:** For Gateway Services (GWS) merchants, a statement report will not generate because the acquirer directly settles them.

PROCESS FOR RECONCILIATING A GATEWAY SERVICES ONLY (GWS-only) MERCHANT INVOICE MISMATCH 🖊️

**Step 1. Identify the Issue**

Read the ticket to understand the merchant's query regarding outstanding invoices and transaction details

**Step 2. Open the Statement of Account**

If the merchant has provided it open the Statement of Account, otherwise request a copy from them

 

**Step 3. Identify the Date Range**

Locate the **Invoice Date** column on the SOA to find the relevant date range

 

**Step 4. Generate the FAR**

Go to the **Reports** section on the dashboard and generate a Financial Actions Report for the corresponding month

 

**Step 5. Calculate the Total and Compare**

- In the FAR, find the **Holding Currency Amount** column and use the SUM function to calculate the total amount

- Compare the calculated sum from the FAR with the amount on the statement of account

- If the fees appear to be applied to the next month's invoice, explain to the merchant that fees from the previous month are sometimes paid on the next month's invoice
