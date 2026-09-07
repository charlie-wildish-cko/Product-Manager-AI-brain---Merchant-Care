---
id: 22059018125586
section_id: 28482643882898
title: "Card Activation via Dashboard or API"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22059018125586-Card-Activation-via-Dashboard-or-API"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-31T16:58:43Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQ6H2MNP5MYX42MCMHAGX"]
label_names: ["global", "unable_to_activate_card_through_dashboard", "case_issuing", "case_issuing_queries"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

Clients can activate virtual or physical cards using the Dashboard or API. The cardholder can also activate the physical card themselves by performing their first Chip and PIN transaction at a point of sale (POS), or by withdrawing cash at an ATM. 

## Process Steps

Clients can activate virtual or physical cards using the Dashboard or API. The cardholder can also activate the physical card themselves by performing their first Chip and PIN transaction at a point of sale (POS), or by withdrawing cash at an ATM. **How To**

1. Physical Card Activation:

  1. Chip and PIN Transaction**: **

    1. Performing the first transaction using Chip and PIN at a point of sale (POS) terminal or withdrawing cash at an ATM will automatically activate the card

  2. Dashboard Activation:

    1. Log in to Dashboard

    2. Navigate to Issuing > Cards

    3. Select the card to activate and click on “Activate card”

  3. API Activation:

    1. Advise the client to utilise the Checkout.com API to [activate the card](https://www.checkout.com/docs/card-issuing/manage-cards/activate,-suspend,-or-revoke-a-card#Activate_a_card_using_the_API) programmatically

    2. 
Send a POST request to the endpoint:

```https://api.checkout.com/issuing/cards/{cardId}/activate
```

    3. Replace {cardId} with the actual card identifier

    4. Ensure proper authentication and required headers are included in the request

2. Virtual Card Activation

  1. Automatic Activation: By default, new virtual cards are marked as active upon creation, requiring no additional activation steps

  2. Manual Activation (if necessary): If the virtual card is inactive, follow the same steps as for physical cards using the Dashboard or API to activate it

3. Additional Considerations

  1. 3D Secure Enrollment

    1. For enhanced security, especially for online transactions, enrol the card in 3D Secure (3DS)

    2. In the Dashboard, go to Issuing > Cards, select the card, and choose Set up 3D Secure

    3. Alternatively, use the API endpoint: [https://api.checkout.com/issuing/cards/{cardId}/3ds-enrollment](https://api.checkout.com/issuing/cards/%7BcardId%7D/3ds-enrollment)

    4. Provide necessary details such as the cardholder's locale and phone number

  2. Suspended Cards

    1. If a card is suspended, it must be reactivated before use

    2. Use the Dashboard or API methods mentioned above to reactivate the card

**Troubleshooting**

The key issues and fixes to consider for card activation are 

- Eligibility: Ensure the cardholder has completed all necessary steps, such as KYC verification, if applicable

- Incorrect Card ID: Double-check you have the correct card ID

- Card status: Verify the card’s status (e.g., inactive or suspended)

- Permissions: Ensure the API key or user role has permission to create and activate cards

- Malformed Request: Validate the request payload and headers in API calls

**Dashboard Steps**

1. For this issue, the cardholder should provide you with: 

  1. The Cardholder ID 

2. To best assist the cardholder, triage by answering the below questions:

  1. Can they see an option to create a card in Dashboard? If so, do they see the option to select single-use or multi-use cards?

  2. When selecting a card (post creation), is there an option to Activate card?

  3. Have all mandatory fields been populated?

  4. Do they receive any errors? If so, what is the error and at what stage do they get it?

3. Check if the "Create Card" option is available:-

  1. Dashboard > Issuing > Cards

  2. On the Cards page, check that the option to create a card is visible on the top right

4. Check the user permissions

  1. Dashboard > Settings > User permissions > Team Permissions > Users, and select the user

  2. 
User profile > Permissions > Issuing and check that ‘Create and edit cards and cardholders’ is enabled for the user:-

5. If the user has read-only permissions, they will not be able to activate cards. They should discuss this |with teir Admin. If the user does have the correct permissions and is still not able to create/activate cards, [raise a Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277)

**API Steps**If there is a card activation issue on the API side, the below check the following regarding activation:

1. 
Validate the card_id using the Retrieve Card API:

```GET https://api.checkout.com/issuing/cards/{card_id}
```

2. Ensure the card is eligible for activation i.e. it is not ‘inactive’ or ‘suspended’

3. Verify the correct endpoint is being used to activate the card:

```curl -X POST https://api.checkout.com/issuing/cards/{card_id}/activate \
-H "Authorization: Bearer sk_test_1234567890abcdef" \
-H "Content-Type: application/json”
```

1. Validate the response code as below:-

  1. 400 - Invalid request: check all required fields are included and formatted correctly

  2. 401 - Unauthorized: ensure correct API and permissions are being used

  3. 404 - Cardholder ID not found: verify it exists and the ID is correct

  4. 409 - Conflict: check for duplicate card creation

  5. 500 - Internal server error: retry at a later time or escalate to the Issuing team

2. Verify that the API key used in the request is valid and active

3. Ensure the API key has the right permissions (Dashboard > API Keys section)

4. 
Confirm the Authorization header is correctly formatted:

```Authorization: Bearer sk_test_1234567890abcdef
```

5. Check for timeout issues: this could be network latency or backend delay in CKO, so try to activate it again after a brief interval

  1. Have the client or cardholder double-check their code sending the request or test their API calls in sandbox

## Glossaries and Definitions:

For **Key Terms and Definitions** on Card Issuing Issues, please see ****[Card Issuing Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22857173195794-Issuing-Glossary-Introduction) For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Card Issuing articles, please see ****[Card Issuing Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22857178933394-Issuing-Tools-Permissions)
