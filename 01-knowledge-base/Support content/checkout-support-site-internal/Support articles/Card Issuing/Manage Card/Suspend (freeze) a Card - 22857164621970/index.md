---
id: 22857164621970
section_id: 28482671122194
title: "Suspend (freeze) a Card"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22857164621970-Suspend-freeze-a-Card"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-31T16:57:13Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JNGXCVNHFQB2TX90T7Z1YKMZ"]
label_names: ["global", "issuing", "case_card_issuing", "case_card_issuing_suspend_freeze_card"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

If a cardholder's card has been lost or stolen, or if there's suspected fraudulent activity, you can suspend a card to temporarily freeze it and automatically block any new transactions.

**Please note**: The following actions are still allowed on a suspended card:

- Authorisation requests linked to a previous transaction (e.g. an incremental authorisation)

- Recurring payments through merchant-initiated transactions (MITs)

- Refunds

- Reversals

- Chargebacks

## Process Steps

**How To**

1. Sign in to Dashboard

2. Go to Issuing > Cards

3. Select the card you want to suspend

4. In the “Card details” screen that appears, select “Suspend card”

5. Alternatively, if the client wants to action this via the API, they can call the [Suspend a card](https://www.checkout.com/docs/card-issuing/manage-cards/activate,-suspend,-or-revoke-a-card#Suspend_a_card_using_the_API) endpoint

6. If the card no longer needs to be suspended, the user can simply reactivate it (Issuing > Cards > Search by Card ID > identify the suspended card, and on the Card details page, activate it)

**Troubleshooting Card Suspension Issues**

**Dashboard**

1. Ensure the card exists in the system (Issuing > Cards > Search by Card ID)

2. Ensure the card can be suspended (i.e. must have active status)

3. Ensure the user has the permissions to suspend cards (Dashboard >  Settings > User permissions > Users > select the user > User profile > Permissions >  Issuing) - if not, they need to escalate to their Administrator

4. Attempt suspension to see if there are any errors - on the Card details screen, click Suspend card

  1. If the button is greyed out or unresponsive

    1. Confirm there are no system-wide or CKO issues

    2. Refresh the Dashboard and/or clear the browser cache and retry

  2. Check for Errors in Logs:

    1. Have the user review the Activity Logs in Dashboard and share any specific issues

**API**

1. 
Ensure the user is using the correct endpoint:-

```POST https://api.checkout.com/issuing/cards/{card_id}/suspend
```

2. 
Check the Authorization header. Ensure the API key in the request is valid and active, and confirm it has permissions for card management actions:-

```Authorization: Bearer sk_test_1234567890abcdef
```

3. 
Ensure the {card_id} provided in the request is correct and use the **Retrieve Card API** to confirm the card exists:-

```GET https://api.checkout.com/issuing/cards/{card_id}
```

4. Ensure the API request follows the correct syntax:-

```curl -X POST https://api.checkout.com/issuing/cards/crd_123456789/suspend \
-H "Authorization: Bearer sk_test_1234567890abcdef" \
-H "Content-Type: application/json"
```

1. Analyse error responses:

  1. 401 - Unauthorized: ensure correct API and permissions are being used

  2. 404- Cardholder ID not found: verify it exists and the ID is correct

  3. 409 - Conflict: the card is already revoked or blocked

  4. 500 - Internal server error: retry at a later time or escalate to the Issuing team

2. Correct any issues (e.g. invalid API key, incorrect card ID) and retry the suspension request

3. If the client has tried to suspend the card through the API, and it is not showing as suspended on the Dashboard, you may need to [raise a Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277)

## Glossaries and Definitions:

For **Key Terms and Definitions** on Card Issuing Issues, please see ****[Card Issuing Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22857173195794-Issuing-Glossary-Introduction) 

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Card Issuing articles, please see ****[Card Issuing Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22857178933394-Issuing-Tools-Permissions)
