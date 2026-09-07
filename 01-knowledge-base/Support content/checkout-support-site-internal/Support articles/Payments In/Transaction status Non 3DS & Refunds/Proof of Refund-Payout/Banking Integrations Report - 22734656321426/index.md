---
id: 22734656321426
section_id: 21991136181650
title: "Banking Integrations Report"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22734656321426-Banking-Integrations-Report"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:35:56Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQT889RQXXSG27BB4ZJ0M"]
label_names: ["case_transactions", "ROW", "case_transactions_issue_banking_integrations_report", "banking_integrations_report"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

Today when a merchant wants to confirm receipt of funds, the queries are normally sent when their customer has been debited in error or has sent us funds in error. This information is available in the reconciliation banking integrations report and can be cross-referenced in the relevant payments platform e.g. Sofort portal. The below article explains the integration report and its associated fields.

## Report Fields

 The below table explains each of the fields in the [banking integrations report](https://checkoutinternal.eu.looker.com/explore/bank-integrations/reconciliation_report?qid=9cGMMFYjlnKae6hY5kTDxI&origin_space=1373&toggle=fil,vis):-

| **Field Name** | **Description** | **Details** |
| --- | --- | --- |
| **AccountName** | This is based on information from Nostro Accounts. Account identifiers (i.e. account number or IBAN) are used to look up the account name | • CKO SAS - Sofort - EUR = Sofort      • iDeal Settlement Account = iDeal / Giropay / eps refunds      • Checkout SAS Cust EUR – SAS Giropay/eps settlements (moving to JPM)      • CHECKOUT CUST EUR – LTD Giropay/eps settlements      • CKO LTD - Settlement - EUR = Giropay/eps      • CKO FR - Settlement -EUR - Giropay/eps settlements      • Checkout SEPA DD Settlements EUR - Sepa DD NAS |
| **AccountNumber** | This is based on information from Nostro Accounts. Account identifiers (i.e. account number or IBAN) are used to look up the account number | • 6161644460 = Sofort      • 500002716 = Giropay/eps      • 49051544 = Giropay/eps      • 6161573552 = Giropay/eps      •14937333 = Giropay/eps      • 6231418242 = Sepa DD NAS      • 0008563036 = SAS ideal / Giropay / eps refunds      • 0006521558 = Ltd ideal / Giropay / eps refunds |
| **AccountType** | This is based on information from Nostro Accounts. Account identifiers (i.e. account number or IBAN) are used to look up the account type | Safeguarding or Settlement |
| **Bank** | This is based on information from Nostro Accounts. Account identifiers (i.e. account number or IBAN) are used to look up the bank name | • Barclays Bank Ireland PLC Paris Branch      • J.P. MORGAN SE      • Barclays Bank Plc      • ING |
| **BankReference** | Unique reference allocated by the bank |  |
| **CCY** | Currency | EUR |
| **DateTimeReceived** | The date the record is written to CKO database |  |
| **DebiCreditMark** | Indicator of credit or Debit to bank account | D = Debit   C = Credit – money received |
| **InformationForAccountOwner** | This field contains additional information about the transaction line, which is to be passed on to the account owner. | This will contain the identifier to locate the payment |
| **LegalEntity** | This is based on information from Nostro Accounts. Account identifiers (i.e. account number or IBAN) are used to look up the legal entity | Checkout SAS Checkout Ltd |
| **ReferenceForAccountOwner** | This is the reference of the message (SWIFT or any other) or document that resulted in this entry. This is a reference that the account owner can use to identify the reason for the entry. | Can contain customer's name |
| **Scheme** | Our team allocates scheme per transaction based on the information in other fields | As this is an allocated field based on other fields it is not always reliable |
| **Type** | Type of statement received from bank | MT942 = intra-day statements MT940 = end-of-day statements |
| **ValueDate** | The date on which the debit/credit is effective. |  |
| **Amount** | Amount in decimal |  |

 

## Glossaries and Definitions:

For **Key Terms and Definitions** on Transactions as well as an **introduction into MENA Gateway and non-Gateway merchants**, please see ****[Transactions Glossary](https://checkoutint.zendesk.com/hc/en-us/articles/21991201065106-Transactions-Glossary-Introduction)**.  **
 
 
 
 
 
 
 
 
 

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Transactions articles, please see ****[Transactions Tools & Permissions](https://checkoutint.zendesk.com/hc/en-us/articles/21991176883474-Transactions-Tools-Permissions)**.**
