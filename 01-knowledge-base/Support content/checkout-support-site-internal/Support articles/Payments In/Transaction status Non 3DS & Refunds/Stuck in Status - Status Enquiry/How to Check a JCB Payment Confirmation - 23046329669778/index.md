---
id: 23046329669778
section_id: 23045937114898
title: "How to Check a JCB Payment Confirmation"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/23046329669778-How-to-Check-a-JCB-Payment-Confirmation"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-03-18T13:41:06Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQT889RQXXSG27BB4ZJ0M"]
label_names: ["case_transactions", "case_transactions_issue_status_proof", "global", "jcb_transaction_status"]
user_segment_ids: [11003606966930]
archive: false
---

**Use this article when**

A JCB merchant contacts us to resolve issues like delayed funds or double billing by verifying transaction status - whether sent for clearing, cleared, or rejected.

**Case type: **Payments in

**Issue Type: **Transaction status (Non 3DS & Refunds)

**Reason: **Stuck in status / status enquiry

## 

## INTRODUCTION TO JCB 💬

JCB stands for Japan Credit Bureau. It’s a Tokyo-based credit card company and payment network. In Japan, JCB is a major domestic card scheme, handling both issuing and acquiring. 

💡**Tip:** Clearing files are generated every 2 hours, starting at 1 AM GMT, with a cut-off time of 7 AM GMT. Settlement files are loaded daily at 12:30 PM GMT, except on weekends.PROCESS TO CHECK A JCB TRANSACTION STATUS🖊️

### Step 1: Convert the Payment ID to a GUID

⚠️ The payment ID needs to be converted into a GUID before running any queries mentioned in this section

- Go into Retool

- In the **Input ID **field, enter the payment ID

- Click **Decode**

- Under **Result**, copy the GUID 

### Step 2: Check the Transaction Status on Hermes or Snowflake

This step verifies the transaction's clearing status and checks if it's in the outgoing transaction table.

⚠️ Ensure you take the ARN (Acquirer Reference Number) from the `JCB_OUTGOINGTRANSACTION` table and not the Gateway table

- Log in to [Hermes](https://data-access-tool.cko-prod.ckotech.co/data-access-tool-web)

- Ensure you have the following server and database selected:

  - 
**Server**: Production (prod-agl1) - Read19 (App.DataTool.Merlin_DB_Support_Team)

  - 
**Database**: Gateway

- Run the following query, replacing the placeholder with the GUID you copied:

```Select clearingstatus, arn, createddate, * from 
"LANDING"."INTEGRATION"."JCB_OUTGOINGTRANSACTION" where paymentid in (''))
```

⁉️See below escalations if the transaction is not present

OR

You can also use Snowflake to check the clearing status of JCB outgoing transactions:

- Log in to Snowflake

- Run the following query:

```
SELECT
arn,
TransactionId,
rootTransactionId,
transactiondate,
clearingStatus,
createddate,
CaptureTransactionDate
FROM LANDING.INTEGRATION.JCB_OUTGOINGTRANSACTION
ORDER BY transactiondate DESC;
```

- The `clearingStatus` column will show the status as **PENDING**, **CLEARED**, or **FAILED**. You can filter the results by `TransactionId` or a date range if needed

### Step 3: Check for Transaction Settlement

To confirm if the transaction has been settled, run this query on Hermes:

```Select *from "LANDING"."INTEGRATION"."JCB_INCOMINGRECONCILIATIONDATA" where arn in ('')
```

ESCALATION ⬆️

If the transaction is not present in the `JCB_OUTGOINGTRANSACTION` table on Hermes, this may indicate an issue like:

- Application Error

- Validation Error

- A rejection from a Scheme

- A Timeout

- A File Generator problem

 In this situation, a ticket must be raised for the [Payment Engineering Operations](https://checkoutsupport.freshservice.com/a/catalog/request-items/600) team to investigate.
