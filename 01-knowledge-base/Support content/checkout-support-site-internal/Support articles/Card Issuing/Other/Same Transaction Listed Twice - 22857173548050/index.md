---
id: 22857173548050
section_id: 28483258495890
title: "Same Transaction Listed Twice"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22857173548050-Same-Transaction-Listed-Twice"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-31T17:01:33Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JNGXCVNHFQB2TX90T7Z1YKMZ"]
label_names: ["global", "issuing", "case_card_issuing", "case_card_issuing_same_transaction_listed_twice"]
user_segment_ids: [11003606966930]
archive: false
---

## Process Steps

1. For this issue, the client needs to provide us with: 

  1. The Card ID

  2. The Transaction ID

2. Initial question to ask: Can you see this in the transaction history on the application or within the Dashboard?

3. Duplicate transactions should not happen, however, if the client says that they have the same transaction listed twice, investigate this using one of the below systems:

  1. Dashboard

  2. Datadog

  3. Retool

Step-by-step guidance:

1. Obtain the transaction ID from the merchant (you can also search on the Dashboard using the Cardholder ID or the Card ID)

2. Go to Dashboard (see 2a below), Datadog (2b below), or Retool (2c below) to check the transaction

  1. Dashboard

    1. On Okta, click on Dashboard Production

    2. Under Account, click on the drop-down and search for the client account name

1. Click on "Card Issuing", then “Transactions” and enter the Transaction ID in the search box to see the transaction status under “Status”(you can also search by Card)

1. You can then click on the individual transactions to get more information about them, e.g. to see if they have been approved or rejected:-

2. Datadog:

  1. Open [(this link provides the required query to check the transaction)](https://app.datadoghq.com/logs?query=source%3Aissuing%20env%3Aprod%20-status%3Adebug%[%E2%80%A6]=stream&from_ts=1685348700811&to_ts=1685424008919&live=false)

  2. Insert the Transaction ID into the "Search for" tab

  3. Run the query with the Transaction ID

  4. Datadog will then provide information on the transaction (the screenshot below shows an example of transaction declines due to “Velocity Reached")

1. Retool

  1. Log into the Issuing [Retool](https://retoolprod.mgmt.ckotech.co/apps/issuing/Issuing%20internal%20tool%20prod) (for access requests click [here](https://checkout.atlassian.net/wiki/spaces/IE/pages/5621188578/Accessing+Issuing+Retool#3.-Access-the-Issuing-Retool-Dashboard))

  2. Click on the “Transactions” tab

1. Enter the transaction ID in the search box and click on "Search"

1. When the results appear, check “Status” to see the transaction’s status and whether it has been declined

2. To obtain further information on the decline reason, scroll down and go to “Events timeline" on the right to see the decline reason (the screenshot below shows an example of a transaction decline due to velocity reached)

1. You can also check the transaction by clicking on View in DataDog (as long as the transaction is less than 2 weeks old) to see the transaction details there

2. If you do see a duplicate transaction, this could be a duplicate authorisation that we have processed twice. Regardless of the reason, duplicate transactions should not happen and if you ever find these, you must [raise a Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277) for this to be investigated.

3. If you would like to check the transaction in DataDog (if it is recent enough to still be present in DataDog, i.e if the transaction occurred within the last two weeks), you can click on the purple "View in DataDog" button and the system will take you to the specific transaction automatically.

To check the transaction using any of the three tools, please see the guidance [here](https://checkout.lightning.force.com/lightning/r/Knowledge__kav/ka008000000I0jeAAC/view).

## Glossaries and Definitions:

For **Key Terms and Definitions** on Card Issuing Issues, please see ****[Card Issuing Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22857173195794-Issuing-Glossary-Introduction) For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Card Issuing articles, please see ****[Card Issuing Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22857178933394-Issuing-Tools-Permissions)
