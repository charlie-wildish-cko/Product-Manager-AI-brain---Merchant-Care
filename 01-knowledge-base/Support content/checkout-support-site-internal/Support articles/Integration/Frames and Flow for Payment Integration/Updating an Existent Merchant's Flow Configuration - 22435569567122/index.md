---
id: 22435569567122
section_id: 22188537440658
title: "Updating an Existent Merchant's Flow Configuration"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22435569567122-Updating-an-Existent-Merchant-s-Flow-Configuration"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:36:41Z"
permission_group_id: 26838654181266
content_tag_ids: ["01H8EDHC0MTG4YFD7E4B42CE0V"]
label_names: ["global", "case_integration", "case_integration_issue_flow", "updating_an_existent_merchants_flow_configuration"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

Where an existing merchant wants to update their configuration, typically to add a new card scheme or payment method to Flow, the below steps should be followed.

## Process Steps

1. Access the _Merchant Hosted Pages Enablement_ retool application

2. Set the environment to **Prod**

3. Set the merchant platform to **NAS**

4. Enter the entity ID that’s being onboarded

5. Click **Onboard/Update merchant** on the bottom right

6. On the next screen, you should see a _Merchant Found_ message and the existing merchant config in a read-only view

  1. If you see a _merchant_not_onboarded_ message, this means that this entity ID has not been onboarded (please visit this [article](https://checkoutint.zendesk.com/hc/en-us/articles/22435560098706))

7. Click the **Update this merchant** button to proceed to the update page  

8. Make the required updates on the next screen

  1. The Merchant processing settings, Creditor information for SEPA and Branding and customisation are not required for Flow and will be ignored if set

  2. For the card schemes and Alternative Payment methods (APMs) please ensure that what’s being requested has been onboarded/enabled on the merchant’s account before enabling on Flow

  3. For PayPal, you must provide the PayPal Merchant ID. This should be the same value as the one in CAT (see [here](https://checkout.atlassian.net/wiki/spaces/APM/pages/5042765942) for more information)

  4. For Google Pay, you must provide the Google Pay Merchant ID that the requester provides

9. Click the Update this merchant to save the changes

## Glossary & Definitions:

For **Key Terms and Definitions** on Integration Issues, please see ****[Integrations Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22198412339346-Integrations-Glossary-Introduction)  For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Integration Issues articles, please see ****[Integrations Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22198326164754-Integrations-Tools-Permissions)
