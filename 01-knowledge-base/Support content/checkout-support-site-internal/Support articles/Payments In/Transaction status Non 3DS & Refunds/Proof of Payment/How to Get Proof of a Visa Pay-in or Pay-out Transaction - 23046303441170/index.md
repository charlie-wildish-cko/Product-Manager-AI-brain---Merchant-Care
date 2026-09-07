---
id: 23046303441170
section_id: 23046197784338
title: "How to Get Proof of a Visa Pay-in or Pay-out Transaction"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/23046303441170-How-to-Get-Proof-of-a-Visa-Pay-in-or-Pay-out-Transaction"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-03-18T14:00:59Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQT889RQXXSG27BB4ZJ0M", "01JYS1V9038NHAQZ1S78P1F2K3"]
label_names: ["case_transactions", "case_transactions_issue_refund_proof_schemes", "proof_of_payments_funds_not_received", "visa_gw3_gwc", "GWC", "GW3"]
user_segment_ids: [11003606966930]
archive: false
---

**Use this article when**

You need to get proof of a transaction or refund for both Visa pay-ins and payouts using the VisaOnline portal.

This guide specifically helps address customer disputes regarding missing payouts or refunds by providing traceable evidence.

**Case type: **Payments in

**Issue Type: **Transaction status (Non 3DS & Refunds)

**Reason: **Proof of payment (ARN, RNN, bulk)INTRODUCTION💬

The ARN is a unique 15-23 digit number that allows the cardholder's bank to trace the refund. It serves as the ultimate 'Proof of Refund', in addition to the scheme level proof. 

You need to retrieve proof of a specific transaction or refund processed through the Visa network, which may be a "pay-in" (a payment received) or a "payout" (a pay to card). 

This proof is typically required for reconciliation, dispute resolution, or record-keeping. The process involves using the VisaOnline portal to search for and download the transaction details.

This proof is typically a PDF document containing all the transaction details.

| ⚠️Note   Please note that for JCB transactions, there is no proof of refund that can be provided. This limitation comes from the scheme itself — unlike Visa or Mastercard, JCB does not issue proof of refund.   We can only provide the refund ARNs. (Kindly check if there's any bounce back via chargebacks using Retool- Clearing Events) |
| --- |

PROCESS FOR GETTING PROOF OF A VISA PAY-IN TRANSACTION🖊️

To get the details of a specific transaction (Payins & Payouts) from VISAOnline, you'll need the following information before you log into the Visa portal:

**Pay-in:**

- Acquirer Reference Number (ARN)

- Transaction Identifier

- Date of transaction

- Amount and Currency

💡**Tip:** Use the following SQL script to retrieve these details for the pay-in transaction you are investigating:

Tool: Hermes   
Server: Production(prod-agl1) - Read19 (App.DataTool.Merlin_DB_Clearing_Support)  
Database: Integration

```SELECT votr.acquirerreferencenumber,vps.TransactionIdentifier,votr.amount,votr.SourceCurrencyCode,votr.clearingstatus,votr.createddate
FROM integration.dbo.visaoutgoingpaymentservicedata vps, integration.dbo.visaoutgoingtransactionrecord votr
WHERE vps.VisaOutgoingTransactionRecordId =votr.VisaOutgoingTransactionRecordId
AND votr.acquirerreferencenumber ='XXXXXXXXXXXXXXXXXXX'
```

💡**Tip:** Instead of using Hermes, you can find all the details from agent toolkit except transaction identifier (scheme transaction ID). Regarding Transaction Identifier (scheme transaction ID), you can find retool- traffic insight (capture/auth log) 

**Payout:**

- Payout ID

- Transaction Identifier (Scheme Transaction ID)

- Date of transaction

- Amount

💡**Tip:** You can retrieve the Transaction Identifier using Payout(retool)

**Step 1: Log in to VisaOnline**

- Log in to your **Okta dashboard**

- From the "My Apps" section, click on the **Visa** app. This will automatically log you into the Visa Access portal

- Once inside, you can switch between regions by clicking on your name in the top menu bar

**Step 2: Navigate to Transaction Inquiry**

- From the "My Services" menu, select **Visa Resolve Online**

- Click on **Inquiry**, and then select **Transaction Inquiry**

**Step 3: Retrieve Transaction Details**

- On the Transaction Inquiry page, enter the **Transaction Identifier** and the **date interval** for the transaction

- Click **Submit**

****

- The transaction details page will appear
✅ Verify that the transaction amount and other details match the requested data**Step 4: Download the Proof**

- Select the checkbox for the specific transaction you want to get proof for

- Click the **Transaction Details** button

- A new pop-up window will appear with the full transaction details

- Click the **Save as PDF** button to download the proof of the transaction in a PDF format

## RESOLUTION ⚒️

- Following the steps above should result in a PDF document containing the requested transaction details. This document confirms that the transaction has been cleared on our end.

- 
Remediation Steps

  - Email the merchant with the downloaded PDF

  - Explain that the ARN has been checked and the transaction has been cleared on our side

  - Advise the merchant to have their customer check with their bank, as the funds have been successfully transferred

FAQs⁉️**Q: What is an Acquirer Reference Number (ARN)?** A: An ARN is a unique number assigned by Visa to each transaction. It can be used to track a transaction through the entire payment process.**Q: What if the transaction details don't match?** A: Double-check the information you entered, especially the Transaction Identifier, date range, and region. If the details still don't match, you may be looking at the wrong transaction. If you're still unable to find the correct transaction, you may need to escalate the issue.**Q: What if the customer says the bank cannot see the transaction even with the PDF? ****A:**Explain to the merchant that the evidence from the schemes is definitive proof that the transaction has been cleared. The customer should double-check with their bank's fraud department or a different representative, as the issue is likely on their end.
