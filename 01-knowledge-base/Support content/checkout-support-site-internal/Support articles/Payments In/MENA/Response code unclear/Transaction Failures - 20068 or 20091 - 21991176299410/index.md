---
id: 21991176299410
section_id: 21991145657362
title: "Transaction Failures - 20068 or 20091"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/21991176299410-Transaction-Failures-20068-or-20091"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:40:22Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQT889RQXXSG27BB4ZJ0M"]
label_names: ["case_transactions", "case_transactions_issue_transaction_declined_reason_response_codes_unclear", "MENA", "Transaction_Failures_20068_or_20091"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

**Important: Transaction** failures can be the cause of the merchant reaching out due to a declined reason/response code unclear. The transaction can fail due to the below reasons specifically for MENA:

1. 20030

2. 20068

3. 20091

If you want to see the full list of decline response codes then take a look [here](https://www.checkout.com/docs/developer-resources/codes/api-response-codes#20xxx_-_SOFT_DECLINE). This covers decline response codes across all regions.

## Process Steps

1. Mostly related to MPGS downtime

2. Check the OC channel on Slack: #OCchannel

3. If you find an incident related to an MPGS outage during the timeframe when the merchant has reported an issue, you can revert to the merchant with the impact details

4. If the merchant wants to know the actual status of the transactions, this can be verified using the MPGS API (postman) or logging into the acquirer portal - follow the same steps under the [MPGS API - Unable to capture](https://checkoutint.zendesk.com/hc/en-us/articles/21991167920018-MPGS-API-unable-to-capture) article

5. Analyse the trend of declines for a merchant by client ID using [Datadog](https://app.datadoghq.com/logs?query=%28%28service%3AMerchant.Api%20OR%20service%3A%2[%E2%80%A6]ing=true&from_ts=1664101251355&to_ts=1666693251355&live=true)

## Glossaries and Definitions:

For **Key Terms and Definitions** on Transactions as well as an **introduction into MENA Gateway and non-Gateway merchants**, please see ****[Transactions Glossary](https://checkoutint.zendesk.com/hc/en-us/articles/21991201065106-Transactions-Glossary-Introduction)**.  **
 
 
 
 
 
 
 
 
 

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Transactions articles, please see ****[Transactions Tools & Permissions](https://checkoutint.zendesk.com/hc/en-us/articles/21991176883474-Transactions-Tools-Permissions)**.**
