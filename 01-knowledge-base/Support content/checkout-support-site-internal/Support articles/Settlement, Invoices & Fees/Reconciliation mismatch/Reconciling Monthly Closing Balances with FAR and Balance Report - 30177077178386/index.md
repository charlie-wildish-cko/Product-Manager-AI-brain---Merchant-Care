---
id: 30177077178386
section_id: 21991159491218
title: "Reconciling Monthly Closing Balances with FAR and Balance Report"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/30177077178386-Reconciling-Monthly-Closing-Balances-with-FAR-and-Balance-Report"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T10:42:19Z"
permission_group_id: 26838654181266
content_tag_ids: []
label_names: []
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

Use this process to verify or **reconcile** a merchant's monthly closing balance by comparing the **Financial Actions Report (FAR)** and the **Balance Report**.

## DESCRIBE THE ISSUE 💬

A **merchant needs to verify their monthly closing balance** is accurate, or an **agent needs to reconcile a discrepancy** reported by the merchant regarding their monthly funds.

The goal is to ensure the **sum of all financial actions (FAR)** equals the **change in the balance (Balance Report)** for the month.

## RESOURCES 📍

| Case Examples | Related |
| --- | --- |
| [Zendesk Ticket: 83688](https://checkout1360.zendesk.com/agent/tickets/83688) | External Article: [Breakdown Types](https://www.checkout.com/docs/funds-management/retrieve-financial-reports/breakdown-types) |

## RECONCILE MONTHLY CLOSING BALANCE PROCESS🖊️

**Step 1. Gather Reports**

- Download the FAR and the Balance Report for the merchant's relevant Currency Account ID (sub-account).

- Both reports must cover the exact same period (e.g., 01/09/2025 to 30/09/2025) and timezone.

💡 For example : If the merchant wants to reconcile the September closing balance. Download the financial action report on dashboard for date range (01/09/2025 to 30/09/2025)

**Step 2. Filter the FAR**

-  In the **FAR**, filter by the **Currency Account ID** and the required **Date Range**.

**💡 Important:** Ensure your filter includes _all_ **Breakdown Types** that affect the account balance, including "Payout," as payouts are recorded actions that change the balance.

**Step 3. Sum Financial Actions**

- Sum the **Holding Currency Amount field** in the Financial Actions Report for the selected period.

- This total represents the net effect of all financial actions for the period.

**Step 4. Check the Balance Report**

- Locate the **Opening Available Balance** and the **Closing Available Balance** in the Balance Report for the same period.

**Step 5. Calculate the Difference**

- Calculate the net balance change: Closing Available Balance - Opening Available Balance.

## RESOLUTION ⚒️

The sum should match the difference between the **Opening Available Balance** and the **Closing Available Balance** in the Balance Report for that period.

The **Sum from FAR (Step 3)** **must match** the **Net Balance Change from the Balance Report (Step 5)**.

## ESCALATION** ⏫**

If the sum does not match, use the transfer macro template to transfer the case to FTS-L2

| Macro: L1>L2 (FTS) |
| --- |
