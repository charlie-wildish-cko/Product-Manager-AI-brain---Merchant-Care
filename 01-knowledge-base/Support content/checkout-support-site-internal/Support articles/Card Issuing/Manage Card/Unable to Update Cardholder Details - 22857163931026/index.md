---
id: 22857163931026
section_id: 28482671122194
title: "Unable to Update Cardholder Details"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22857163931026-Unable-to-Update-Cardholder-Details"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-31T16:56:18Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JNGXCVNHFQB2TX90T7Z1YKMZ"]
label_names: ["global", "issuing", "case_card_issuing", "case_card_issuing_unable_to_update_cardholder_details"]
user_segment_ids: [11003606966930]
archive: false
---

## Process Steps

1. For this issue, the cardholder should provide:

  1. Cardholder ID

  2. Details of the attempted update i.e. what specific fields are they editing

  3. Error messages or screenshots

2. For Dashboard issues

  1. Ensure the user has the correct permissions to update cardholder details (where permissions are lacking, cardholders should check with their Admin regarding access levels)

  2. Have the cardholder attempt the update to identify the point of failure (Dashboard > Issuing > Cardholders > Search by Cardholder ID > Select the cardholder > Edit/Update

    1. Some details (e.g., date of birth, identity details) may not be editable after creation due to regulatory compliance - in this case, the user may need to create a new cardholder profile

    2. Validate the formatting

      1. Email addresses must follow proper syntax

      2. Names must not contain invalid characters

      3. Phone numbers must include the correct country code

    3. If an error appears, note it and check:

      1. If required fields are missing

      2. If the format of data (e.g., email, phone number) is correct

      3. If the cardholder has pending compliance checks that block updates

  3. Attempt to refresh the session

    1. Log out and log back into Dashboard

    2. Clear the browser cache (not data)

    3. Try private/incognito mode, or use another browser

    4. If using a mobile app, suggest force-closing, clearing cache (not data) and re-open the app

  4. If the client is still not able to change the details, [raise a Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277)

3. For API issues, have the cardholder or client explore the following:-

  1. 
Use the **Update Cardholder API** to modify cardholder details:

```PUT https://api.checkout.com/issuing/cardholders/{cardholder_id}
```

4. 
Ensure the API request includes a valid API key with correct permissions:

```Authorization: Bearer <YOUR_API_KEY>
```

5. 
Use the **Retrieve Cardholder API** to confirm the cardholder exists before attempting an update:

```GET https://api.checkout.com/issuing/cardholders/{cardholder_id}
```

6. 
Ensure the request follows the proper format

```{
  "first_name": "John",
  "last_name": "Doe",
  "email": "johndoe@email.com",
  "phone_number": {
    "country_code": "+1",
    "number": "1234567890"
  },
  "billing_address": {
    "address_line1": "123 Main St",
    "city": "City",
    "state": "State",
    "zip": "12345",
    "country": "US"
  }
}
```

7. Review any errors - below are common errors and solutions:-

  1. 400 - Invalid request: check all required fields are included and formatted correctly

  2. 401 - Unauthorized: ensure correct API and permissions are being used

  3. 404 - Cardholder ID not found: verify it exists and the ID is correct

  4. 409 - Conflict: check for duplicate card creation

  5. 500 - Internal server error: retry at a later time or escalate to the Issuing team

8. Check for a wider issue using the [Checkout Staus Page](https://status.checkout.com/) i.e. verify if the issue is affecting other users or clients to confirm if there’s a known platform issue

If still not able to change the details, [raise a Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277)

## Glossaries and Definitions:

For **Key Terms and Definitions** on Card Issuing Issues, please see ****[Card Issuing Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22857173195794-Issuing-Glossary-Introduction) 

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Card Issuing articles, please see ****[Card Issuing Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22857178933394-Issuing-Tools-Permissions)
