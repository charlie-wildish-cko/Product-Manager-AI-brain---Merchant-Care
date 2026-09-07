---
id: 23046329640594
section_id: 23045937114898
title: "How to Check a DCI Payment Confirmation"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/23046329640594-How-to-Check-a-DCI-Payment-Confirmation"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-03-18T13:41:20Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQT889RQXXSG27BB4ZJ0M"]
label_names: ["case_transactions", "case_transactions_issue_status_proof", "global", "dci_transaction_status", "diners_club_international", "dci"]
user_segment_ids: [11003606966930]
archive: false
---

**Use this article when**

A DCI merchant contacts us to resolve issues like delayed funds or double billing by verifying transaction status - whether sent for clearing, cleared, or rejected.

**Case type: **Payments in

**Issue Type: **Transaction status (Non 3DS & Refunds)

**Reason: **Stuck in status / status enquiryINTRODUCTION TO DCI💬

DCI stands for Diners Club International, a card scheme/network. In several internal docs it’s referenced as “DCI (Diners Club International)” and treated as a payment scheme supported across products and regions.

 This guide provides a step-by-step process for checking the status of a DCI (Diners Club International) transaction. This is useful for resolving issues such as double billing, funds not being received, or simply verifying that a transaction has been sent for clearing, has cleared, or was rejected.

**💡 ****Tip:** Before you begin, it’s important to understand the file generation schedules. Clearing files are generated every 12 hours (8 AM and 8 PM GMT) with an 11 AM GMT cut-off time. Settlement files are received daily at 2:30 PM GMT, except on weekends.PROCESS FOR CHECKING A DCI TRANSACTION STATUS🖊️

### Step 1: Convert the Payment ID into a GUID

- Go into Retool

- In the **Input ID **field, enter the payment ID

- Click **Decode**

- Under **Result**, copy the GUID 

### Step 2: Check the Transaction Status on Hermes or Snowflake

Once you have the GUID you can check the transaction's status.

- Access [Hermes](https://data-access-tool.cko-prod.ckotech.co/data-access-tool-web)

- Ensure you have selected the correct server and database:

  - 
**Server:** Production (prod-agl1) - Read19 (App.DataTool.Merlin_DB_Support_Team)

  - 
**Database:** Gateway

- Run one of the following queries to check the transaction status

```Select clearingstatus, dcidetailid, createddate, * from 
"LANDING"."INTEGRATION"."DCI_DCIDETAIL" where  DECRYPTEDPAYMENTID in ('')
```

OR

```Select clearingstatus, dcidetailid, createddate, * from 
"LANDING"."INTEGRATION"."DCI_DCIDETAIL" where  referencenumber in ('')
```

⁉️See below escalations if the transaction is not present

### OR

You can also use Snowflake to check the clearing status of DCI transactions:

- Log in to Snowflake

To check a DCI transaction on Snowflake, you typically query the **DCI_DCIDETAIL** table, which holds transaction details and clearing statuses.

- Run the following query:

```
SELECT 
  TransactionId,
  rootTransactionId,
  transactiondate,
  clearingStatus,
  referencenumber,
  VersionAndAuthenticationAction
FROM LANDING.INTEGRATION.DCI_DCIDETAIL
WHERE TransactionId = '<your_transaction_id_here>'
ORDER BY transactiondate DESC;

```

### Step 3: Check if the Transaction has been Settled

To determine if a transaction has been settled, use the following query:

```Select *from "LANDING"."INTEGRATION"."DCI_CFCHARGERECORD" where dcidetailid in ('')

```

ESCALATION ⬆️

If the transaction is not present in the `DCI_DCIDETAIL` table or the Outgoing table, it indicates a potential issue, like:

- Application Error

- Validation Error

- A rejection from a Scheme

- A Timeout

 In this situation, a ticket must be raised for the [Payment Engineering Operations](https://checkoutsupport.freshservice.com/a/catalog/request-items/600) team to investigate.

 

##
