---
id: 22857180694290
section_id: 28483258495890
title: "GET Card Retrieval Issues"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22857180694290-GET-Card-Retrieval-Issues"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:34:43Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JNGXCVNHFQB2TX90T7Z1YKMZ"]
label_names: ["global", "issuing", "case_card_issuing", "case_card_issuing_get_card_retrieval_issues"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

A **404 error** when retrieving card details via the getCardDetails method typically indicates that the requested resource (card) is not found (example case [here](https://checkout.slack.com/archives/C03BA1XC9D4/p1710317580189029)). Common causes and solutions are below:-

| **Cause** | **Resolution** |
| --- | --- |
| Incorrect Card ID | Ensure the correct card ID is used in the request |
| Card does not exist | Confirm that the card exists in the issuing system via the Dashboard |
| Card has been deleted or activated | Check the card status; if inactive, activate the card before attempting to fetch details. |
| Permission issue | Verify that the API key or user has permissions to access the requested resource |
| Endpoint is misconfigured | Confirm the API endpoint is correct and matches the environment (e.g., production vs. sandbox) |

## Process Steps

Steps for the client to resolve this issue:-

1. Log in to Dashboard

2. Navigate to **Issuing > Cards** and search for the card using the provided ID

3. Confirm that the card exists and is active (a card might not be retrievable if it has been deactivated, blocked, or deleted)

4. Validate the API request

  1. Ensure that the endpoint used in the API request is correct:  
GET https://api.checkout.com/issuing/cards/{cardId}

  2. Replace {cardId} with the correct card identifier

5. Headers and Authentication

  1. Verify that the API request includes the correct headers, such as the API key:  
Authorization: Bearer <Your API Key>

  2. The API key must have the necessary permissions to access card details

6. Error Response Details

  1. Analyse the full error response to identify any additional context (e.g. full message body, timestamp, correlationID, etc). The **404** could indicate:

    1. The card ID is incorrect or not found

    2. The card has been removed or archived

7. Verify Input Parameters

  1. Double-check the parameters being sent to the getCardDetails method

    1. Ensure the cardId is passed correctly

    2. Confirm the API call isn’t inadvertently modified in your code (e.g. missing headers or malformed URLs)

8. Inspect Callback Logic

  1. Ensure the cardDetailsCallback logic handles errors gracefully and that the onError method provides sufficient diagnostic output

9. Retry with the Correct Details

  1. After validating the card ID and ensuring the card exists, retry the API call with the corrected request

Any further issues, or if the client cannot solve the issue, reach out to [#ask-issuing-cms](https://checkout.enterprise.slack.com/archives/C03BA1XC9D4)

## Glossaries and Definitions:

For **Key Terms and Definitions** on Card Issuing Issues, please see ****[Card Issuing Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22857173195794-Issuing-Glossary-Introduction) For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Card Issuing articles, please see ****[Card Issuing Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22857178933394-Issuing-Tools-Permissions)
