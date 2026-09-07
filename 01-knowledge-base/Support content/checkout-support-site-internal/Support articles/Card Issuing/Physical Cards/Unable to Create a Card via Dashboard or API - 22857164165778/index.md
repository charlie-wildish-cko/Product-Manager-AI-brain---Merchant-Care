---
id: 22857164165778
section_id: 28482812438674
title: "Unable to Create a Card via Dashboard or API"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22857164165778-Unable-to-Create-a-Card-via-Dashboard-or-API"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-31T17:00:17Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JNGXCVNHFQB2TX90T7Z1YKMZ"]
label_names: ["global", "issuing", "case_card_issuing", "case_card_issuing_unable_to_create_card_via_dashboard_api"]
user_segment_ids: [11003606966930]
archive: false
---

## Process Steps

**Dashboard**

1. For this issue, the client should provide you with:

  1. Cardholder ID

2. Explore/have the client or cardholder complete the following:

  1. When they select the Cards page within Dashboard, check that they see an option to create a card

    1. Log in to Dashboard and go to Issuing > Cards

    2. Ensure the 'Create Card' option is visible (Dashboard > Issuing > Cards > Create Card button near top right)

    3. If it is missing, the user may lack the necessary permissions. Review user roles and permissions 

      1. Go to Dashboard > Settings > User permissions > Users

      2. Search for and select the relevant user

      3. Under User profile > Permissions, expand the “Issuing permission” to see what permissions are assigned

  2. What error message is shown

    1. If an error occurs, note the exact message displayed

    2. Use the error message to diagnose the problem. For example, if the error indicates invalid input, verify the cardholder data entered

  3. At what stage do they receive the error? 

    1. Identify at which step the error arises e.g. during data entry, submission, or processing

    2. Understanding the error's timing can help pinpoint its cause, whether it's user input, system processing, or network issues

  4. If they see the option, do they see the option to select single-use or multi-use cards?

    1. After selecting 'Create Card,' verify that options for single-use and multi-use cards are available

    2. If options are missing, it could indicate configuration issues. The client may need to contact their system administrator or support team to ensure card types are correctly set up

  5. Are you prompted to enter cardholder details?

    1. Check if the system prompts for cardholder details during the card creation process

    2. If not prompted, there may be a system glitch. Try refreshing the page or clearing the browser cache

  6. Have all mandatory fields been entered?

    1. Identify and fill in all required fields, such as cardholder name, address, and card type

    2. Incomplete fields can prevent card creation. Double-check for any missed mandatory fields before proceeding

**API**If the issue to create a card is via the API, have the client complete the following steps:

1. 
Check and confirm the API endpoint is correct:

```POST https://api.checkout.com/issuing/cards
```

2. 
Ensure all mandatory fields are included and correctly formatted (the common required fields are type, cardholder ID, and billing address):

```{ "type": "virtual", 
"cardholder_id": "cardholder_123456", 
"billing_address": { 
"address_line1": "123 Main Street", 
"city": "City", 
"state": "State", 
"zip": "12345", 
"country": "US" 
} 
}
```

3. 
Confirm that the API key used is valid and has the required permissions for card creation

```Authorization: Bearer sk_test_1234567890abcdef
```

4. Replicate the request outside of the client’s system (using Postman or Curl) to verify if it is an API issue or a client issue

5. Analyse the API response and check what error codes occur:-

  1. 400 - Invalid request: check all required fields are included and formatted correctly

  2. 401 - Unauthorized: ensure correct API and permissions are being used

  3. 404 - Cardholder ID not found: verify it exists and the ID is correct

  4. 409 - Conflict: check for duplicate card creation

  5. 500 - Internal server error: retry at a later time or escalate to the Issuing team

6. 
Check that the cardholder exists using the Retrieve Cardholder API:

```GET https://api.checkout.com/issuing/cardholders/{cardholder_id}
```

7. 
If the cardholder doesn’t exist, create one using the Create Cardholder API:

```POST https://api.checkout.com/issuing/cardholders
```

8. Check that the card program (Dashboard > Issuing > Card Programs) is properly configured in Dashboard and supports the card type requested:-

  1. Card Program Status: this should be active, otherwise cards cannot be created

  2. Card Types Supported: virtual cards, physical cards, or both

  3. Spending Controls: review limits, MCC whitelists/blacklists, or geographies

  4. Funding Setup: ensure the balance is funded, or it can prevent card creation

9. Have the client test connectivity e.g. a GET request to check cardholder details, and ensure logging is enabled to capture responses/errors

10. Actions to take:-

  1. If this is available on Dashboard then it is most likely a user input or processing issue 

  2. If it is not available then it may be a permission issue (see step 2.a.iii above)

  3. If the user does have the correct permissions or if it is a wider issue for the client, [raise a Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277)

11. If you need to check the configuration on [CAT](https://checkout.atlassian.net/wiki/spaces/IE/pages/5876318279/Issuing+Configuration+Guide#Step-2.-CAT-setup), please contact Solutions Engineering or Merchant Configuration

## Glossaries and Definitions:

For **Key Terms and Definitions** on Card Issuing Issues, please see ****[Card Issuing Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22857173195794-Issuing-Glossary-Introduction) For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Card Issuing articles, please see ****[Card Issuing Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22857178933394-Issuing-Tools-Permissions)
