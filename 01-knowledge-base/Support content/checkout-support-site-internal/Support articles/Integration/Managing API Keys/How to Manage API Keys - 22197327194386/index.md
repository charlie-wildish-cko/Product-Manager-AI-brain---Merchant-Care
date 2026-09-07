---
id: 22197327194386
section_id: 22188504535954
title: "How to Manage API Keys"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22197327194386-How-to-Manage-API-Keys"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:34:10Z"
permission_group_id: 26838654181266
content_tag_ids: ["01H8EDHC0MTG4YFD7E4B42CE0V"]
label_names: ["global", "case_integration", "how_to_manage_api_keys", "case_integration_issue_access_and_api_keys_issues"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

For managing API keys used for server-to-server communication with Checkout.com, including authentication mechanisms, key management and troubleshooting common issues.

## 

## Introduction

This section outlines the procedures for managing API keys used for server-to-server communication with Checkout.com, including authentication mechanisms, key management, and troubleshooting common issues.

Please refer to the following [confluence](https://checkout.atlassian.net/wiki/spaces/ATLAS/pages/1043890614/Key+settings) page which details how to Manage Keys on CAT.

**Note**: Merchants are able to manage API keys via the Dashboard, please direct them to [API keys external documentation](https://www.checkout.com/docs/developer-resources/api/manage-api-keys/api-keys#Manage_your_keys_in_the_Dashboard)  
 [](https://www.checkout.com/docs/developer-resources/api/manage-api-keys/api-keys#Manage_your_keys_in_the_Dashboard) 

## Process Steps

**Authentication Mechanisms**

Checkout.com supports two authentication mechanisms for server-to-server communication:

- Access Keys (OAuth 2.0)

- Secret Keys

These keys can be used to make API calls to your account, such as processing payments, refunds, etc. For more information on managing API keys, refer to the documentation: [Manage API Keys](https://www.checkout.com/docs/developer-resources/api/manage-api-keys)  
 **Key Management Best Practices**

1. Limit Access: Merchants should restrict access to API keys and avoid sharing them publicly or storing them in version control systems.

2. Do not request merchants' production secret keys as this is bad practice.  
 

**Using API Keys**Checkout’s Unified Payments API offers a streamlined integration experience giving merchants access to all supported payment methods via a single payments endpoint. The Unified Payments API has been processing live merchant payments since September 2018. All new merchants have been put directly onto UPAPI since the beginning of 2019.When requesting payments through the Unified Payments API, merchants have two options for routing payments through your processing channels:

1. 
**Single Key for All Processing Channels: **Specify the processing channel in your payment request

2. 
**Multiple Keys for Each Processing Channel: **There is no need to specify the processing channel in your payment request

3. 
**Third-party sites/e-comm platform not directly integrated with CKO: **If there is no area to specify a processing channel on a third-party setting, then the API key must have an individual processing channel selected in CAT and the ‘Allow Any Processing Channel’ toggle should be switched off

 Escalations: Slack channel: #ask-iamProduct owner: OCS Merchant User Data 

## Glossaries and Definitions:

For **Key Terms and Definitions** on Integration Issues, please see ****[Integrations Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22198412339346-Integrations-Glossary-Introduction)  For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Integration Issues articles, please see ****[Integrations Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22198326164754-Integrations-Tools-Permissions)
