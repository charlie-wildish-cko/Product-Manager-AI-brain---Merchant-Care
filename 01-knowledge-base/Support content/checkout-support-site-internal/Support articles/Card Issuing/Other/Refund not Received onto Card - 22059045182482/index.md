---
id: 22059045182482
section_id: 28483258495890
title: "Refund not Received onto Card"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22059045182482-Refund-not-Received-onto-Card"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-30T17:08:34Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JNGXCVNHFQB2TX90T7Z1YKMZ"]
label_names: ["global", "issuing", "case_card_issuing", "case_card_issuing_refund_not_received_onto_card"]
user_segment_ids: [11003606966930]
archive: false
---

## **Process Steps **

**Please note** refunds need to be made within 6 months of the transaction (this is a mandate by Mastercard and Visa)

1. For this issue, we want the client to provide us with:

  1. The Card ID

  2. The Transaction ID

2. Find out when the refund was made (refunds can take up to 10 days). If it has been more than 10 days, check to see if the transaction is in Datadog or Dashboard:

  1. Dashboard

    1. Open [Dashboard](https://dashboard.checkout.com)

    2. In the ‘Search Clients and Entities’ box, search for the Client’s name and switch view

    3. Under Issuing, click on ‘All transactions’

    4. In the ‘Search by Transaction ID’ box, enter the transaction details provided by the client

    5. Review the results and check the ‘Status’ column for transactions with a status of ‘Presentment received’ to confirm the refund is complete

    6. Click on the individual transaction(s) to get more information about including the associated card and cardholder details

  2. Datadog

    1. Open Datadog using this [link](https://app.datadoghq.com/logs?query=source%3Aissuing%20env%3Aprod%20-status%3Adebug%[%E2%80%A6]=stream&from_ts=1685348700811&to_ts=1685424008919&live=false)

    2. Insert the Transaction ID into the ‘Search for’ tab

    3. Run the query with the Transaction ID

    4. Review the results from the search, including the transaction details. Please note that Datadog will only provide information for transactions that have occurred in the past 2 weeks

3. If you cannot see the transaction on Dashboard or Datadog, send the [Chargeback questionnaire](https://checkout.atlassian.net/wiki/download/attachments/5667817833/Chargeback%20Letter%20Form%20_%20Issuing.pdf?api=v2) to the client to fill in, and advise them to submit the completed questionnaire to the Disputes team: [issuing_disputes@checkout.com](mailto:issuing_disputes@checkout.com)

4. If the client still has not received the refund:

  1. Confirm that we have processed it on our end, otherwise raise a [Jira ticket](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277) to request for the presentment to be re-sent

## Glossaries and Definitions:

For **Key Terms and Definitions** on Card Issuing Issues, please see ****[Card Issuing Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22857173195794-Issuing-Glossary-Introduction) 

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Card Issuing articles, please see ****[Card Issuing Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22857178933394-Issuing-Tools-Permissions)
