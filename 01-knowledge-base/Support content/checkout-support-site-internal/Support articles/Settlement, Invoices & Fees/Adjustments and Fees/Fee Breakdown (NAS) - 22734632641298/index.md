---
id: 22734632641298
section_id: 21991135458066
title: "Fee Breakdown (NAS)"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22734632641298-Fee-Breakdown-NAS"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:35:56Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHQKPVKA7XAZRYSRWE7JRH4"]
label_names: ["row", "case_settlements", "case_settlements_issue_transaction_fees", "fee_breakdown_nas"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

Merchants often raise tickets requesting explanations on the “Variable scheme fees” and “Fixed scheme fees” on their statements, as they see multiple lines of these two fee types.  Each line from the statement represents a different fee charged by the Scheme on different action codes. The breakdown can be obtained from our looker dashboards.

## Process Steps

1. Open Financial Actions report on [Looker](https://checkoutinternal.eu.looker.com/explore/ledger_financial_actions/finance_financial_actions_report?qid=nzmkSRjzOvDBVPZ20lvmFJ&origin_space=27&toggle=fil)

2. Under the filter section:-

  1. Select your date range (this can be changed to a specific date for the year)

  2. Select your client name from the drop-down

  3. Set the Fee Type to “Scheme” and “Interchange"  
**Note**: For interchange, the data can only be used for transactions processed more than a day before due to an IC lag. More information can be found [here](https://checkout.atlassian.net/wiki/spaces/SPI/pages/5972689418/Financial+Actions+Report+Query)

  4. Set the Financial Action Type to “Fee” and “Capture”

  5. If the merchant has shared specific payment IDs, populate them in the Action Group ID filter

1. Once search results are displayed, the following information is available to help answer the merchant’s query:-

  1. Action Type (this provides the action code on which the fee was applied - authorisation/capture/card verification/Void)

  2. Fee Detail (this describes each fee incurred for the transaction) 

  3. Total Processing/Holding Amount (this provides the breakdown of each fee amount charged on the transaction).

**Note**: All the lines where the **Financial Action Type = “Fee”** represent the different fees applied on the transaction. The ones with the **Financial Action Type = “Capture”** represent the processing volume for the transaction.

## Glossaries and Definitions:

For **Key Terms and Definitions** on Transactions as well as an **introduction into MENA Gateway and non-Gateway merchants**, please see ****[Settlements Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/21991207693458-Settlements-Glossary-Introduction)   For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Transactions articles, please see ****[Settlements Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/21991176789266-Settlements-Tools-Permissions)
