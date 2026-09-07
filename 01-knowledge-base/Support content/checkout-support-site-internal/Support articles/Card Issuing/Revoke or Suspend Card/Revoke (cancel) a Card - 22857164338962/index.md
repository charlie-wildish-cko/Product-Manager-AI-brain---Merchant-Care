---
id: 22857164338962
section_id: 28482720682002
title: "Revoke (cancel) a Card"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22857164338962-Revoke-cancel-a-Card"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-31T17:01:12Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JNGXCVNHFQB2TX90T7Z1YKMZ"]
label_names: ["global", "issuing", "case_card_issuing", "case_card_issuing_cancel_revoke_card_dashboard_api"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

If a cardholder reports their card as lost or stolen, or if there is confirmed fraudulent activity, you can cancel or "revoke" a card to permanently freeze it and automatically decline any new transactions.

**Please note**: Revoking a card is a one-way action. The card cannot be reactivated. You do not need to suspend a card before revoking it. 

## Process Steps

**How To**

1. Sign in to [Dashboard](https://dashboard.checkout.com/)

2. Go to Issuing > Cards

3. Select the card you want to revoke

4. If the client wants to immediately revoke the card, go to the “Card details” and select “Revoke card”

5. If the client wants to schedule a date for the card to be revoked, select the dropdown icon to view additional options and select “Schedule revoke date”

6. To update or remove a card's revocation date, select the card in Dashboard and select the date displayed in the revocation message.

7. If the client wants to revoke a card using the API, they can call the [Revoke a card](https://api-reference.checkout.com/#operation/revokeCard) endpoint

 **Troubleshooting Revocation via the Dashboard**

1. Ensure the user has sufficient permissions to revoke a card

  1. Dashboard >  Settings > User permissions > Users > Select the user > User profile > Permissions >  Issuing > Confirm the permissions for create are enabled

2. Ensure the card is eligible for revocation (i.e. active) by checking its status

  1. Dashboard > Issuing > Cards >  Search by Cardholder ID > filter by cardholder name, card ID, or the last four digits

  2. Inactive or Suspended: the card may need to be activated first to revoke (depending on the program rules)

  3. If the card status is invalid or cannot be found, confirm the card exists in the issuing program.

3. Attempt the Revocation

  1. Dashboard > Issuing > Cards >  Search by Cardholder ID > Card details > Revoke card

  2. If the button is greyed out or unavailable, confirm that there are no pending disputes or holds on the card

4. Error Logs in Dashboard:

  1. Have the user check the Activity Logs in Dashboard for error messages or logs related to the failed revocation attempt

 **Troubleshooting Revocation via API**

1. 
Ensure the Authorization header contains a valid API key:

```Authorization: Bearer <YOUR_API_KEY>
```

2. Confirm the API key has permission to manage cards

3. 
Ensure the {card_id} in the request is correct and retrieve the card’s details using the Retrieve Card API to verify the card exists and is eligible for revocation:

```GET https://api.checkout.com/issuing/cards/{card_id}
```

4. 
Check the request using the below API call and review the response status:

```curl -X POST https://api.checkout.com/issuing/cards/crd_123456789/revoke \
-H "Authorization: Bearer sk_test_1234567890abcdef" \
-H "Content-Type: application/json"
```

5. Analyse error responses:

  1. 401 - Unauthorized: ensure correct API and permissions are being used

  2. 404- Cardholder ID not found: verify it exists and the ID is correct

  3. 409 - Conflict: the card is already revoked or blocked

  4. 500 - Internal server error: retry at a later time or escalate to the Issuing team

6. Ensure there are no network or connectivity issues between the client’s system and Checkout’s API

7. Test the revocation request in the sandbox environment to confirm the issue is not specific to production

8. If the client has tried to revoke the card through the API, and it is not showing as revoked on the Dashboard, you may need to [raise a Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277)

## Glossaries and Definitions:

For **Key Terms and Definitions** on Card Issuing Issues, please see ****[Card Issuing Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22857173195794-Issuing-Glossary-Introduction) 

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Card Issuing articles, please see ****[Card Issuing Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22857178933394-Issuing-Tools-Permissions)
