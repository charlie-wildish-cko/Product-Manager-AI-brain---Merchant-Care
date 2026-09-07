---
id: 23046303716370
section_id: 23045937114898
title: "SAB (GW3) Payment Confirmation"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/23046303716370-SAB-GW3-Payment-Confirmation"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-03-18T13:40:05Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQT889RQXXSG27BB4ZJ0M"]
label_names: ["case_transactions", "case_transactions_issue_status_proof", "global", "sab_gw3_transaction_status"]
user_segment_ids: [11003606966930]
archive: false
---

**Case type: **Payments in

**Issue Type: **Transaction status (Non 3DS & Refunds)

**Reason: **Stuck in status / status enquiry

## Introduction

Below are the steps to take when checking if transactions have been sent for clearing, are cleared or are rejected. This will also help resolve scenarios such as funds not received or double billing.

**Please note: **the payment ID needs to be converted into a GUID before running any queries mentioned in this section. To do this:-

1. Go into Retool

2. In the **Input ID **field, enter the payment ID

1. Click **Decode**

2. Under **Result**, copy the GUID 

## Process Steps

Only MBC (GW3) transactions can be queried on Snowflake/Hermes at the moment. NAS transactions can only be queried by the Payment Engineering Operations Team, therefore a ticket will need to be raised to the Payment Engineering Operations team. Proof of Payments can only be requested from SAB. No settlement files are received from SAB. Clearing files are sent every day at 1am GMT (interval 00:00 - 00:00 GMT)  
 

1. Check the transaction status and Clearing filename:-

```select
ogt.TransactionDate,
ogt.TransactionAmount,
ogt.TransactionCurrencyCode,
ogt.MerchantName,
ogt.AcquirerReferenceNumber,
ogt.TransactionId,
ogf.FileName,
ogf.CreatedDate
from "LANDING"."TPPCAT"."DBO_OUTGOINGTRANSACTION" ogt, 
"LANDING"."TPPCAT"."DBO_OUTGOINGFILE" ogf
where ogt.OutgoingFileId=ogf.OutgoingFileId
and ogt.AcquirerReferenceNumber in ('')
order by ogt.createddate desc
```

## Glossaries and Definitions:

**For an introduction on Clearing, Settlements & Authorisation queries that Merchant Care may receive from merchants, please see****** [Clearing, Settlements & Authorisation Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/23047190761874-Clearing-Settlements-Authorisation-Introduction)
