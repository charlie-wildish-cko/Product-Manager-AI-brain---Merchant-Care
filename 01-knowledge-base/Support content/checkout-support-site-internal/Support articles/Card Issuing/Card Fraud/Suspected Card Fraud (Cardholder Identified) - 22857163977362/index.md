---
id: 22857163977362
section_id: 28482801562002
title: "Suspected Card Fraud (Cardholder Identified)"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22857163977362-Suspected-Card-Fraud-Cardholder-Identified"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:35:11Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JNGXCVNHFQB2TX90T7Z1YKMZ"]
label_names: ["global", "issuing", "case_card_issuing", "case_card_issuing_suspected_card_fraud_cardholder_identified"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

Checkout could be alerted to fraudulent activity on a client’s issuing account in 2 ways:-

1. Via the client or cardholder

2. Via internal teams e.g. Risk Operations or Compliance Operations

If the client or a cardholder becomes aware of suspected fraudulent issuing transactions and raises it with Checkout, please follow the below steps.

## Process Steps

1. The information that you require from the client or cardholder for this issue is:

  1. The Card ID

  2. The Transaction ID(s)

2. Actions to take:

  1. Check if the client or cardholder has suspended the card:-

    1. 
**Dashboard**: Dashboard > Issuing > Cards > Search by Card ID > Status

    2. 
**Retrieve Card API**:

```GET https://api.checkout.com/issuing/cards/{card_id}
```

  2. If the card is not suspended, send a request to [fraudsupport@checkout.com](mailto:fraudsupport@checkout.com) for the card to be suspended

    1. Ensure you specify the relevant card ID(s) and transaction (IDs)

    2. Inform the cardholder that the Issuing team will be in contact

  3. If the card is suspended, check if the client or cardholder has filled out a [dispute letter](https://checkout.atlassian.net/wiki/download/attachments/5667817833/Chargeback%20Letter%20Form%20_%20Issuing%20(1).pdf?api=v2)

    1. If completed, forward the dispute letter to [issuing_disputes@checkout.com](mailto:issuing_dispute@checkout.com)

    2. If not completed, ask the cardholder to fill it out and submit it to [issuing_disputes@checkout.com](mailto:issuing_dispute@checkout.com)

    3. Inform the cardholder that the Card Disputes team will check if the dispute is fraudulent or non-fraudulent, and will revert to them directly with the outcome and next steps

## Glossaries and Definitions:

For **Key Terms and Definitions** on Card Issuing Issues, please see ****[Card Issuing Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22857173195794-Issuing-Glossary-Introduction) 

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Card Issuing articles, please see ****[Card Issuing Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22857178933394-Issuing-Tools-Permissions)
