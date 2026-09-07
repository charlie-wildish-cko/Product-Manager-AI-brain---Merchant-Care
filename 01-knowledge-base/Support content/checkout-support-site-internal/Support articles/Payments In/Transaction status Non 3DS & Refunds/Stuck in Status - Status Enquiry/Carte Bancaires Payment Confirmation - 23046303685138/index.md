---
id: 23046303685138
section_id: 23045937114898
title: "Carte Bancaires Payment Confirmation"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/23046303685138-Carte-Bancaires-Payment-Confirmation"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-03-18T13:40:21Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQT889RQXXSG27BB4ZJ0M"]
label_names: ["case_transactions", "case_transactions_issue_status_proof", "carte_bancaires_transaction_status", "application_error"]
user_segment_ids: [11003606966930]
archive: false
---

**Use this article when**

A merchant contacts Checkout.com with a query about a Carte Bancaires transaction, specifically if the merchant has not received funds or if they believe a customer was double-billed.

**Case type: **Payments in

**Issue Type: **Transaction status (Non 3DS & Refunds)

**Reason: **Stuck in status / status enquiryINTRODUCTION TO CARTE BANCAIRES TRANSACTION STATUS 💬

Carte Bancaires, also known as 'Carte Bleue', is a widely used French payment card. It's accepted both in France and internationally. 

The card is issued by various banks and allows cardholders to make payments at participating merchants. Transactions made with Carte Bancaires are processed through Arkea, a bank that offers third-party payment facilitation solutions.

Files are generated daily at 4 am and 4 pm GMT, excluding weekends. Clearing is handled by Arkea. Payment proofs aren't available at the Checkout level, and no settlement files are received. Confirmation files arrive 4-5 hours after clearing files are sent to Arkea.PROCESS FOR CHECKING THE TRANSACTION 🖊️

💡 **Convert the Payment ID to a GUID before you start**

Before you can query a transaction, you must convert its payment ID into a Global Unique Identifier (GUID) using Retool.

- Go to Retool

- In the Input ID field and enter the payment ID

- Click Decode

- Copy the GUID from the Result field

 

## HERMES PROCESS STEPS 🖊️

Use  [Hermes](https://data-access-tool.cko-prod.ckotech.co/data-access-tool-web) to check if the transaction has been generated in the Outgoing table.

**For Refunds:**

```xml
select CLEARED, RRN, * from 
"LANDING"."INTEGRATION"."CP_CARTESBANCAIRES_PROD_CARD_REFUND"
where rrn in  ('')
```

**For Purchase:**

```xml
select CLEARED, RRN, * from 
"LANDING"."INTEGRATION"."CP_CARTESBANCAIRES_PROD_PURCHASE_INVOICE"
where rrn in ('')
```

If the transaction is not present in the Outgoing table, there may be an issue like:

- Application Error

- Validation Error

- Reject from Schemes

- Timeout

- File Generator

A ticket needs to be raised to [Payment Engineering Operations](https://checkoutsupport.freshservice.com/a/catalog/request-items/600) to investigate. Check the clearing file name and generated date:

```xml
select FILE_NAME,GENERATED_DATE, STATUS from 
"LANDING"."INTEGRATION"."CP_CARTESBANCAIRES_PROD_OUTGOING_FILE" where 
OUTGOING_FILE_ID =''

```

Check the **Status** column to know the state of the file:

- SendForClearing: We have already submitted the files to Arkea, and we are waiting for the confirmation file

- Cleared: Confirmation files have already been received and loaded in the confirmation table

- RejectedFile: We encountered issues with transactions in the file, and we need to correct the transactions and reload it

 

## SNOWFLAKE PROCESS STEPS 🖊️

To check Carte Bancaires transactions, use the following query (replace **<your_transaction_id>** as needed): 

```xml
select  
  t.ResponseShortMessage,
  t.Acquirerreferenceid,
  t.BCTransactionId,
  t.BCOriginalTransactionId,
  t.BCChargeId,
  t.TrackID,
  t.Amount,
  t.CurrencyCode,
  t.AcceptorCountry,
  t.AcceptorCity,
  ma.MerchantAccountName,
  t.MerchantAccountId,
  t.businessid,
  t.TransactionId,
  t.rootTransactionId,
  t.transactiondate,
  t.Status
FROM "LANDING"."GATEWAY"."DBO_TRANSACTIONS" t
INNER JOIN "LANDING"."ADMINISTRATION"."DBO_ACQUIRERCREDENTIAL" ac ON t.AcquirerCredentialId = ac.AcquirerCredentialId
INNER JOIN "LANDING"."ADMINISTRATION"."DBO_MERCHANTACCOUNT" ma ON t.MerchantAccountId = ma.merchantaccountid
LEFT JOIN "LANDING"."INTEGRATION"."CP_CARTESBANCAIRES_PROD_PURCHASE_INVOICE" p ON p.TRANSACTION_ID = t.TRANSACTIONID
WHERE ac.AcquirerId IN (77)
  AND t.ActionCodeId IN (5)
  AND t.GatewayResponseCode = '10000'
  AND t.TransactionId = '<your_transaction_id>';
```

 

**For an introduction on Clearing, Settlements & Authorisation queries that Merchant Care may receive from merchants, please see****** [Clearing, Settlements & Authorisation Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/23047190761874-Clearing-Settlements-Authorisation-Introduction)
