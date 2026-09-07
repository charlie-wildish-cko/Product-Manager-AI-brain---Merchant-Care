---
id: 23046329689234
section_id: 23045937114898
title: "How to Check Visa Payment Confirmation"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/23046329689234-How-to-Check-Visa-Payment-Confirmation"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-03-18T13:40:51Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQT889RQXXSG27BB4ZJ0M"]
label_names: ["case_transactions", "case_transactions_issue_status_proof", "global", "visa_transaction_status"]
user_segment_ids: [11003606966930]
archive: false
---

**Use this article when**

Checking the status of a Visa transaction, specifically focusing on the clearing status. 

**Case type: **Payments in

**Issue Type: **Transaction status (Non 3DS & Refunds)

**Reason: **Stuck in status / status enquiry

## 

## INTRODUCTION TO THE ISSUE 💬

Below are the steps to take when checking if transactions have been sent for clearing, are cleared or are rejected. This will also help resolve scenarios such as funds not being received or double-billing. 

## PROCESS TO CHECK A VISA TRANSACTION STATUS🖊️

1. In the Zendesk ticket, go to **Apps**, and expand the **Checkout Agent Toolkit**

2. Click the relevant Payment ID to bring up the **Details** and **Timeline** view

3. Under **Details** **> Card details**, you can confirm the **Card** **type** and the **Scheme** (e.g. Visa, Mastercard):-

4. Under **Timeline**, you will see the clearing status of the relevant payment

5. As a backup (if needed), you can input and convert the Payment ID to a GUID, then copy it, and check the clearing status on the Clearing events Retool with the GUID:-

  1. Retool > Input ID > Decode > Copy > Paste into Retool search bar to check the gateway and clearing status

 

## Glossaries and Definitions:

**For an introduction on Clearing, Settlements & Authorisation queries that Merchant Care may receive from merchants, please see****** [Clearing, Settlements & Authorisation Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/23047190761874-Clearing-Settlements-Authorisation-Introduction)
