---
id: 22857179301266
section_id: 28483258495890
title: "Unable to Make a Payment"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22857179301266-Unable-to-Make-a-Payment"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-31T17:00:50Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JNGXCVNHFQB2TX90T7Z1YKMZ"]
label_names: ["global", "issuing", "case_card_issuing", "case_card_issuing_unable_to_make_a_payment"]
user_segment_ids: [11003606966930]
archive: false
---

## Process Steps

1. For this issue, we need the client to provide us with:

  1. The Card ID

2. There are a few things you should think about as a first step - all of these could direct you to the root cause of the issue:

  1. Check the Card status to make sure it is active

  2. Check the card expiry date

  3. Check the decline reasons

  4. Is this the first time the client has used this card?

  5. Is the transaction amount over the program thresholds?

  6. If the client has used the card before do they have enough remaining funds on the card?

3. If possible, your first port of call should be using Retool for this query as Retool can automatically link you to DataDog to show you the decline reason for the transaction, if the transaction was performed within the last two weeks (please use [this guide](https://checkout.lightning.force.com/lightning/r/Knowledge__kav/ka008000000I0jeAAC/view) in Retool if needed)

4. If you do not have access to Retool/cannot use it, check Dashboard to see if the card is active and not in a blocked state:

  1. Open Dashboard and search for the client’s account

  2. Click on "Card Issuing", then "Cards"

1. Check program thresholds for the client to see if the client has gone over their thresholds:

  1. Go to the client's folder on the shared drive and open the Issuing Questionnaire that the client filled in during their onboarding

  2. Check the "Volumes and Limits" page of the questionnaire to understand the client's thresholds

2. Check the transaction's decline reason in Datadog and refer to the decline reason definitions [here](https://checkout.atlassian.net/wiki/spaces/IP/pages/5641797798/Decline+Reason+Response+Summary)

  1. Obtain the transaction ID from the merchant and check the transaction in Datadog if the transaction was done within the last two weeks - see detailed instructions below.

    1. 
**For Non-Issuing Transactions**: Open DataDog using the following link and replacing the * at the end with the Payment ID

      1. [https://app.datadoghq.com/logs?query=%40PaymentId%3Apay_yk4w4az7hqwuhhk467typn5zqi%20[…]z=stream&from_ts=1706001330363&to_ts=1707297330363&live=true@PaymentId:*](https://app.datadoghq.com/logs?query=%40PaymentId%3Apay_yk4w4az7hqwuhhk467typn5zqi%20[%E2%80%A6]z=stream&from_ts=1706001330363&to_ts=1707297330363&live=true@PaymentId:*)

      2. If you need more granular information you can look into the [Card Processing logs](https://app.datadoghq.com/logs?query=trace_id%3Aaae69b3e-35b4-4c46-bd18-30f93354cdc2&[%E2%80%A6]z=stream&from_ts=1706001330363&to_ts=1707297330363&live=true)(sometimes the declines are from the issuer and a few are internal errors)

    2. 
**For Issuing Transactions**: Insert the Transaction ID into the "Search for" tab (highlighted in red in the below screenshot)

  2. Run the query with the Transaction ID

  3. Datadog will then provide the decline reason for the transaction, for example in the below screenshot the transaction was "Velocity Reached"

If you have completed the steps above and/or the transaction was completed over two weeks ago, [raise a Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277)

## Glossaries and Definitions:

For **Key Terms and Definitions** on Card Issuing Issues, please see ****[Card Issuing Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22857173195794-Issuing-Glossary-Introduction) 

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Card Issuing articles, please see ****[Card Issuing Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22857178933394-Issuing-Tools-Permissions)
