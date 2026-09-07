---
id: 21991183358098
section_id: 21991160796434
title: "Internal CKO HTTP errors MENA"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/21991183358098-Internal-CKO-HTTP-errors-MENA"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:40:23Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQT889RQXXSG27BB4ZJ0M"]
label_names: ["case_transactions", "MENA", "case_transactions_issue_api_http_error_http_4xx_5xx", "internal_cko_http_errors"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

**Important: **In most cases the API HTTP error will be on CKO side at Gateway level, but on some occasions there could be other reasons for the HTTP error e.g. configuration. 

## Process Steps

1. 
**API HTTP error **on CKO side at Gateway level (in most cases):

  1. Use [Datadog](https://app.datadoghq.com/logs?query=service%3A%22Gateway%20API%22%20env%3Aproduction[%E2%80%A6]ing=true&from_ts=1720088159613&to_ts=1720692959613&live=true) to identify HTTP errors [per client ID](https://app.datadoghq.com/logs?query=service%3A%22Gateway%20API%22%20env%3Aproduction[%E2%80%A6]ing=true&from_ts=1720088112207&to_ts=1720692912207&live=true).

    1. Once you have the client ID, copy the client ID into the DD search bar

    2. You can see the HTTP status code and can filter by date

    3. This will show you if there is an outage that requires further investigation. If so, follow the below steps to reach out to the OC team.

  2. OC outreach:

    1. When there is an issue on CKO Gateway side, then the OC team posts this HTTP error on your #OCchannel

    2. If you get notified of a HTTP error yourself then post this on the channel for review by the OC team

    3. Care to revert and give an example of the Payment ID/ raise a ticket to the OC team

    4. OC will investigate on their end and explain the reason for this error

    5. Care to then go back to the merchant and explain the error/issue

## Glossaries and Definitions:

For **Key Terms and Definitions** on Transactions as well as an **introduction into MENA Gateway and non-Gateway merchants**, please see ****[Transactions Glossary](https://checkoutint.zendesk.com/hc/en-us/articles/21991201065106-Transactions-Glossary-Introduction)**.  **
 
 
 
 
 
 
 
 
 

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Transactions articles, please see ****[Transactions Tools & Permissions](https://checkoutint.zendesk.com/hc/en-us/articles/21991176883474-Transactions-Tools-Permissions)**.**
