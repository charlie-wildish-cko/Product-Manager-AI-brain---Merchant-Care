---
id: 23046334077842
section_id: 23045937114898
title: "How to Check AMEX EU Payment Confirmation"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/23046334077842-How-to-Check-AMEX-EU-Payment-Confirmation"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-03-18T13:41:33Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQT889RQXXSG27BB4ZJ0M"]
label_names: ["case_transactions", "case_transactions_issue_status_proof", "global", "amex_eu_transaction_status", "amex"]
user_segment_ids: [11003606966930]
archive: false
---

**Use this article when**

An AMEX EU merchant contacts us to resolve issues like delayed funds or double billing by verifying transaction status - whether sent for clearing, cleared, or rejected.

**Case type: **Payments in

**Issue Type: **Transaction status (Non 3DS & Refunds)

**Reason: **Stuck in status / status enquiry

## INTRODUCTION TO AMEX EU💬

American Express (AMEX) is a global financial services company best known for its charge cards and credit cards. AMEX EU is the American Express (non‑US) processing and settlement setup for Europe.

**💡 ****Tip: **Clearing files are generated daily from 6pm to 6pm GMT and sent to AMEX at 7pm, with an 8pm GMT cut-off. Confirmation files arrive at 9pm GMT, updating status from PENDING to CLEARED. 

Settlement files load into the AMEX_RECORDOFCHARGE table around 6 AM GMT.

 

PROCESS FOR CHECKING AMEX EU TRANSACTION STATUS🖊️

### Step 1: Convert the Payment ID into a GUID

- Go into Retool

- In the **Input ID **field, enter the payment ID

- Click **Decode**

- Under **Result**, copy the GUID 

 

### Option 1. Check Transaction Status in Agent Toolkit

Use the Settlement details and Timeline in the Agent Toolkit to check for cleared or settled payments

### 

### Option 2. Check Transaction Status in Snowflake

You can also use Snowflake to check AMEX transactions, which is useful for retrieving transaction details using the **Acquirer Reference Number (ARN)**.

- Identify the ARN(s) for the transaction(s) you need to check.

- Run the following SQL query on Snowflake

- Replace `' YOUR_ARN_HERE '` with the actual ARN(s) 

💡 You can check multiple ARNs by separating them with commas

```
SELECT acquirer_reference_number, payment_id, transaction_id, charge_id, status, action_code_id
FROM core.core.core_payment
WHERE transaction_date > '2022-01-01'
AND acquirer_reference_number IN (
' YOUR_ARN_HERE '
)
``` [cite: 29, 30, 31, 32, 33]
```
