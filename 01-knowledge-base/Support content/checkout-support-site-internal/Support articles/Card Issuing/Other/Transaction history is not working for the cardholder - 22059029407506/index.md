---
id: 22059029407506
section_id: 28483258495890
title: "Transaction history is not working for the cardholder"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22059029407506-Transaction-history-is-not-working-for-the-cardholder"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-31T16:54:27Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JNGXCVNHFQB2TX90T7Z1YKMZ"]
label_names: ["global", "issuing", "case_card_issuing", "case_card_issuing_transaction_history_not_working_for_cardholder"]
user_segment_ids: [11003606966930]
archive: false
---

## Process Steps

For this issue, we would ideally want the client to provide us with:

- The cardholder ID from the Client Dashboard

- A screenshot of the issue that they are facing

The questions that you should be asking yourself to help you navigate this query are:

- Is this for all transactions or for a particular transaction expected to be shown that is not appearing?

- Have any transactions been performed?

- When was the last transaction performed?

Action Steps:

1. If the merchant cannot see their transaction history, you can:

  1. Ask the client to check if the API request has been received. If the transactions are not showing, please raise a [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277)

  2. Use the "Daily Authorization Report" Looker report to review the transactions. To access this report, please click [here](https://checkout.atlassian.net/wiki/spaces/IS/pages/4970381585/Issuing+Ops+Reports) to obtain the link to the report

    1. If there are missing transactions from the Looker report, please raise a [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277)
