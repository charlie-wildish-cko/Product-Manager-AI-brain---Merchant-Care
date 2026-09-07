---
id: 21991207483922
section_id: 21991164381842
title: "Al Rajhi manual process"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/21991207483922-Al-Rajhi-manual-process"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:40:25Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQT889RQXXSG27BB4ZJ0M"]
label_names: ["case_transactions", "MENA", "MADA_20030_Refund_failures", "case_transactions_issue_refund", "Al_Rajhi_manual_process"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

**Important: **KSA has a manual refund process due to the 30 day limitation for MADA. All other acquirers outside of KSA can be done directly from the Dashboard. For manual refunds please refer to this [highspot page](https://docs.google.com/spreadsheets/d/1g1I4-FixwMxsF07SLu_3mtin_650uVW-0MVOzS84xg8/edit#gid=1386391676) which gives you a breakdown of the process for KSA acquirers.

## Process Steps

1. 
Find the contact details [here](https://docs.google.com/spreadsheets/d/1g1I4-FixwMxsF07SLu_3mtin_650uVW-0MVOzS84xg8/edit#gid=1386391676).

2. All required details to fill the manual refund template for Al Rajhi can be obtained from retool. The charge requested event points out the acquirer, the MID can be identified from Datadog or from Authentication session in traffic insights.

3. Use the below template below to send details to Al Rajhi (obtain details from Retool):

| RRN | Masked Card Number | Date of TRX | Transaction amount | Refund Amount | MID |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

1. The claim ID will then be shared by Al Rajhi, which can then be shared to the merchant as proof of refund.

## Glossaries and Definitions:

For **Key Terms and Definitions** on Transactions as well as an **introduction into MENA Gateway and non-Gateway merchants**, please see ****[Transactions Glossary](https://checkoutint.zendesk.com/hc/en-us/articles/21991201065106-Transactions-Glossary-Introduction)**.  **
 
 
 
 
 
 
 
 
 

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Transactions articles, please see ****[Transactions Tools & Permissions](https://checkoutint.zendesk.com/hc/en-us/articles/21991176883474-Transactions-Tools-Permissions)**.**
