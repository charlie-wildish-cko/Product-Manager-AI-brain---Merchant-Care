---
id: 22197332503826
section_id: 22188504535954
title: "Troubleshooting API Keys Common Issues"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22197332503826-Troubleshooting-API-Keys-Common-Issues"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:37:32Z"
permission_group_id: 26838654181266
content_tag_ids: ["01H8EDHC0MTG4YFD7E4B42CE0V"]
label_names: ["global", "case_integration", "troubleshooting_api_keys_common_issues", "case_integration_issue_access_and_api_keys_issues"]
user_segment_ids: [11003606966930]
archive: false
---

## Process Steps

**Using Bearer Prefix**

When using new API keys, ensure the correct Bearer prefix is included:

- Format: Bearer sk_xxxxxx

 **Checking Scopes**

Different keys have specific scopes available to them. To see which scopes may be required depends on the API request the merchant is using.

To see if the API request has required scopes view the [API reference page](https://api-reference.checkout.com/). Please see the below example:

1. 
View a specified request 

2. 
Click on the dropdown "Security" tab 

3. 
View the required scopes list at the bottom of this dropdown.

4. Please verify that the necessary scopes are active for the keys being used.   
 

**Sandbox Environment**

1. In the Sandbox environment, keys may be deleted by dashboard users. Verify that the API Key or Access key still exists in the account dashboard. 

2. If the required keys have been deleted and the deleted key is being used, this will cause payments to result in a 401. In this case, the user can just create a new API key and relink it.

  
 

## Glossaries and Definitions:

For **Key Terms and Definitions** on Integration Issues, please see ****[Integrations Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22198412339346-Integrations-Glossary-Introduction)  For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Integration Issues articles, please see ****[Integrations Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22198326164754-Integrations-Tools-Permissions)
