---
id: 22734656538514
section_id: 21991136181650
title: "Refund proof for Giropay/efs"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22734656538514-Refund-proof-for-Giropay-efs"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:35:56Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQT889RQXXSG27BB4ZJ0M"]
label_names: ["case_transactions", "ROW", "case_transactions_issue_refund_proof_apm", "refund_proof_for_giropay_eps", "confirmation_of_received_funds"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

Today when a merchant wants to confirm receipt of funds, the queries are normally sent when their customer has been debited in error or has sent us funds in error. This information is available in the reconciliation banking integrations report and can be cross-referenced in the relevant payments platform e.g. Sofort portal. The below article explains the integration report and its associated fields.

## Process Steps

### Giropay/eps

1. Open the [banking integrations report](https://checkoutinternal.eu.looker.com/explore/bank-integrations/reconciliation_report?qid=9cGMMFYjlnKae6hY5kTDxI&origin_space=1373&toggle=fil,vis)

2. When filtering to locate settlements or refunds related to Giropay/eps transactions, use the _AccountName_ or _AccountNumber_ fields:-

  1. 
_AccountName_ field value: 

    1. Checkout SAS Cust EUR

    2. CHECKOUT CUST EUR

    3. CKO FR - Settlement -EUR

    4. CKO LTD - Settlement - EUR

  2. 
_AccountNumber_ field value: 

    1. 6161573552

    2. 500002716

    3. 49051544

    4. 14937333

3. To receive a comprehensive end-of-day report without displaying duplicated transactions in the results, filter on the ReportType field

  1. 
_ReportType_ field value: MT940

4. 
_InformationForAccountOwner_ field contains identifiers or IBANs that can be used to locate a payment.

 

### Case Example 1

_BAI=142;YOUR REF=PDC5FA0F56D31C46;B/O CUSTOMER=DE71217500000164837445 BOULBABA TAB A;PAID TO=CHASDEFXXXX;REC FROM=NOLADE21NOS;REMARK=/REMI/BEST: . 09.11.2023 15:35 WINA MAX FRANCE VORG: 100602683-21354575 REC: XIQCRIC4D4UEVKOWB65OV3JEQM/RE F/PDC5FA0F56D31C461E9AB99F61078552F E/SCT/_

| Customer's IBAN and name | **B/O CUSTOMER=DE71217500000164837445 BOULBABA TAB A** |
| --- | --- |
| Payment ID excluding the prefix "pay_" | **REC: XIQCRIC4D4UEVKOWB65OV3JEQM** |

On the Giropay portal, the IBAN and reason should match the details in _InformationForAccountOwner_. The Payment ID (without the prefix) should also match the details.

**Please note**: when searching for the Payment ID in Looker, **search in both uppercase and lowercase** to successfully locate the transaction (see below).

**Giropay**:-

****

**Looker**:-

  
 

### Case Example 2

Below is a query on received funds for a voided giropay transaction:-

In Looker, utilise the **Proof of Payment** information to locate and confirm receipt on the bank statement:-

## Glossaries and Definitions:

For **Key Terms and Definitions** on Transactions as well as an **introduction into MENA Gateway and non-Gateway merchants**, please see ****[Transactions Glossary](https://checkoutint.zendesk.com/hc/en-us/articles/21991201065106-Transactions-Glossary-Introduction)**.  **
 
 
 
 
 
 
 
 
 

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Transactions articles, please see ****[Transactions Tools & Permissions](https://checkoutint.zendesk.com/hc/en-us/articles/21991176883474-Transactions-Tools-Permissions)**.**
