---
id: 21991193197970
section_id: 21991164304274
title: "MPGS API & Cybersource Transaction Status & Proof of ARN/RNN"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/21991193197970-MPGS-API-Cybersource-Transaction-Status-Proof-of-ARN-RNN"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-09-25T12:36:36Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQT889RQXXSG27BB4ZJ0M"]
label_names: ["case_transactions", "case_transactions_issue_status_proof", "MENA", "MPGS_API_&_Cybersource"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

For troubleshooting transaction status inquiries and providing proof of transaction details, such as an ARN (Acquirer Reference Number) or RRN (Retrieval Reference Number).

**Problem:** A merchant requires proof of a transaction's status or details (e.g., failed, refunded, voided).

**Solution:** Use specific tools like Postman, acquirer portals, and internal logs to verify the transaction status and provide the merchant with the necessary proof.

 DESCRIBE THE ISSUE 💬

Merchants contact support to verify the status of a transaction or to request proof, often due to customer disputes, failed transactions, or confusion regarding refunds and voids. The audience for this SOP includes support agents who need to access transaction data across different payment gateways, specifically Mastercard Payment Gateway Services (MPGS) and Cybersource. 

**When the transactions have failed due to MPGS timeout**

- Postman should be sufficient to check the actual status of the transaction or,

- Acquirer portal can be used to check the status of the transaction (MPGS/ Cybersource)

**To check the status of the refund**

- Postman should be sufficient to check the actual status of the transaction or,

- Acquirer portal can be used to check the status of the transaction (MPGS/ Cybersource)

**When there is a void transaction/ issues relating to a void transaction:**

- The RRN should be sufficient proof of the void

- Postman should be sufficient to check for the RRN or,

- Acquirer portal can be used to check for the RRN (MPGS/ Cybersource)

KEY TAKEAWAYS 🔑

- Use internal tools like Postman and DataDog to perform initial checks on transaction and refund statuses.

- Access acquirer portals (MPGS/Cybersource) for in-depth verification and to obtain official proof, such as screenshots.

- For MPGS, you may need to request portal credentials from the acquirer if they are not already available.

- For Cybersource, use the Merchant Reference Number or RequestID to find transactions.

- An RRN is often sufficient proof for voided transactions.

- If a merchant cannot provide portal access, reach out to the acquirer directly with all transaction details to request proof.

PROCESS FOR TRANSACTION STATUS & PROOF 🖊️

## MPGS API & Portal

This process applies to all acquirers using Mastercard MPGS

**Check Transaction Status via MPGS API**

- Use DataDog to retrieve the MID/Token and Order ID from the MPGS logs. 

- With this information, you can verify the transaction status directly through the MPGS API.

**Obtain Screenshot Proof from the MPGS Portal**

-  If the merchant requires a screenshot as proof, you must log in to the MPGS portal.

- Find the relevant acquirer portal link from the table provided below.

- If you need credentials, first check the Active MID credentials Gsheet. If not available, contact the acquirer to request them.

| **Acquirer Name** | **Acquirer Portal** |
| --- | --- |
| SABB MPGS | [https://ap-gateway.mastercard.com/ma/login.s](https://ap-gateway.mastercard.com/ma/login.s) |
| Mashreq MPGS | [https://ap-gateway.mastercard.com/ma/login.s](https://ap-gateway.mastercard.com/ma/login.s) |
| Mashreq Cybersource | <> |
| Mashreq MIGS | [https://migs.mastercard.com.au/ma/login.s](https://migs.mastercard.com.au/ma/login.s) |
| Network International Cybersource | [https://network.ubc.cybersource.com/ebc2/](https://network.ubc.cybersource.com/ebc2/) |
| Doha Bank | [https://dohabank.gateway.mastercard.com/ma/login.s](https://dohabank.gateway.mastercard.com/ma/login.s) |
| Bank Muscat | [https://bankmuscat.gateway.mastercard.com/ma/login.s](https://bankmuscat.gateway.mastercard.com/ma/login.s) |
| MEPS | [https://mepspay.gateway.mastercard.com/ma/login.s](https://mepspay.gateway.mastercard.com/ma/login.s) |
| Bank Muscat Cybersource | [https://bankmuscat.ubc.cybersource.com/ebc2/](https://bankmuscat.ubc.cybersource.com/ebc2/) |
| National Bank of Kuwait | [https://nbk.ubc.cybersource.com/ebc2/](https://nbk.ubc.cybersource.com/ebc2/) |
| AESA MPGS | [https://aesa.gateway.mastercard.com/ma/login.s](https://aesa.gateway.mastercard.com/ma/login.s) |
| NBE MPGS | [https://nbe.gateway.mastercard.com/ma/login.s](https://nbe.gateway.mastercard.com/ma/login.s) |
| ANB | [https://anb.gateway.mastercard.com/ma/login.s](https://anb.gateway.mastercard.com/ma/login.s) |

- Once logged in, search for the transaction- typically using the RRN.

- Take a screenshot of the transaction status page and email it to the merchant

 

### Cybersource Portal

 

This process applies to all acquirers using Cybersource.

**Log into the  ******[Cybersource Portal](https://ebc2.cybersource.com/ebc2/app/TransactionManagement/details?requestId=6809402917066418304276&merchantId=mashreq_8108771_aed&fromSimilarSearch=false&goBackCount=-2) 

- Find the MID from the Cybersource authorization API in DataDog.

- Refer to this [sheet](https://docs.google.com/spreadsheets/d/1x-6_2QW8a7U9yyzUabGLS8ajxCYMuS8qfI300kc_EZE/edit#gid=0) to locate the password to the MID and log in to [Cybersource](https://ebc2.cybersource.com/ebc2/app/TransactionManagement/details?requestId=6809402917066418304276&merchantId=mashreq_8108771_aed&fromSimilarSearch=false&goBackCount=-2) using the new password.

**Search for the Transaction**

- Navigate to **Transaction Management**, then **Transactions**.

- Click **Add Filter** and select **Merchant Reference Number**.

- Enter the reference number and adjust the date range. If you are using the `AcquirerRefrenceID` from Hermes, use the `RequestID` filter instead.

- Click on the `Request ID` to open the transaction details.

**Find the ARN or RRN**

- On the transaction details page, scroll down to the **Processor Information** section. The ARN or RRN will be listed here.
