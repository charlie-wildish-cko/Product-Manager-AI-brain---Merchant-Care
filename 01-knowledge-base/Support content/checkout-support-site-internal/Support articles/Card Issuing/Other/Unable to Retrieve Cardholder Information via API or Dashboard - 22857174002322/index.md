---
id: 22857174002322
section_id: 28483258495890
title: "Unable to Retrieve Cardholder Information via API or Dashboard"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22857174002322-Unable-to-Retrieve-Cardholder-Information-via-API-or-Dashboard"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-31T16:53:52Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JNGXCVNHFQB2TX90T7Z1YKMZ"]
label_names: ["global", "issuing", "case_card_issuing", "case_card_issuing_unable_to_retrieve_cardholder_information_via_dashboard_or_api"]
user_segment_ids: [11003606966930]
archive: false
---

## Process Steps

1. For this query, the client should provide you with the following information: 

  1. A screenshot of the error or error message (e.g. if there is an error displayed on the mobile app)

  2. Cardholder ID

2. Steps to take:

  1. If you know of any existing API/Dashboard issues, this could be why the client is struggling to retrieve information. Inform them

  2. If not, please continue to step 3

3. Explore the following with the client or cardholder:

  1. Check Dashboard to see if the cardholder exists and what information we have for them 

    1. Open Dashboard and go to Issuing > Cardholders

    2. In the “Search by Cardholder ID” box, search using identifiers such as the cardholder ID, email address, or phone number, and click on the relevant cardholder to see the profile

    3. Review all cardholder details under “Cardholder”, “Address” and “Recent cards”

    4. Ensure the cardholder is active and not in a restricted or inactive state

    5. If the cardholder does not exist, confirm whether they were created successfully or if there was an issue during the creation process

  2. Which information are they trying to retrieve and for which cardholder?

    1. Identify the exact information the client is trying to access (e.g. cardholder name, address, card status, transaction history)

    2. Confirm whether they’re accessing this via Dashboard or the API

  3. What type of error message or error is occurring

    1. If accessing via Dashboard, ask for a screenshot or the exact error message shown

    2. If accessing via API, request the error message, code, and response from the API request. Common API errors include:

      1. Invalid cardholder ID or reference

      2. Authorisation errors (e.g. insufficient permissions)

      3. Connectivity issues

4. Resolve:-

  1. If you can see cardholder information, send this to the client and ask if the information is correct

  2. If the cardholder exists but you cannot see any cardholder information, please raise a [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277)

  3. If the client says that the information is not correct, this is likely due to an issue with the API - please raise a [J](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274)[ira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277)

  4. If the client says that the information is correct but they still cannot see it on the Dashboard, this could be a problem with their permissions. Check the permissions and if this is the root of the problem, advise the client. If the user has the correct permissions but is still not able to retrieve the necessary information, please raise a [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277)

## Glossaries and Definitions:

For **Key Terms and Definitions** on Card Issuing Issues, please see ****[Card Issuing Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22857173195794-Issuing-Glossary-Introduction) 

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Card Issuing articles, please see ****[Card Issuing Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22857178933394-Issuing-Tools-Permissions)
