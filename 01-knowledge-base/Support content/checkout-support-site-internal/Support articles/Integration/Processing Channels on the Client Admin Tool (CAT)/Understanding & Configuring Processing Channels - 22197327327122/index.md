---
id: 22197327327122
section_id: 22188504904594
title: "Understanding & Configuring Processing Channels"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22197327327122-Understanding-Configuring-Processing-Channels"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-31T16:09:01Z"
permission_group_id: 26838654181266
content_tag_ids: ["01H8EDHC0MTG4YFD7E4B42CE0V"]
label_names: ["global", "case_integration", "understanding_and_configuring_processing_channels", "processing_channels_on_cat"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

This section outlines the procedures for managing and configuring processing channels using the Client Admin Tool (CAT). CAT is a user interface plugin and API that integrates directly into the New Account Structure (NAS) product network.

To report any bugs with CAT, please reach out to the team that owns the page that the error is occurring on - [MASUP - (CAT) Configuration ownership](https://checkout.atlassian.net/wiki/spaces/OACSO/pages/5761663418/MASUP+-+CAT+Configuration+ownership).

## Process Steps

**Accessing the Client Admin Tool (CAT)**

Instructions on how to access CAT can be found here:

- [Access to CAT](https://checkout.atlassian.net/wiki/spaces/ATLAS/pages/1183547415/Access+to+CAT)

Please note that to access any of the environments, you will need to have access and connect to Cloudflare. If you do not yet have access, you can request access by completing this [Jira form](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274).

Once you have access to Cloudflare, use the following URLs to access CAT environments:

- [Sandbox](https://client-admin.cko-sbox.ckotech.co/web/)

- 
[Production](https://client-admin.cko-prod.ckotech.co/web/)  
 

**Understanding Processing Channels****Definition and Usage:**

- 
**Processing Channel**: Represents a specific line of business and is tied to a legal entity. Each processing channel is unique across the entire client and cannot be shared by multiple legal entities.

- 
**Merchant Category Code (MCC)**: Each processing channel is generally associated with a single MCC.

- 
**Gateway Configuration**: The processors are associated with the processing channel.

In legacy systems, the processing channel is similar to a Business, and it can identify which legal entity made the request.**Migration to Profile Processors:**Previously, CAT processing channels were configured using Manual processors. These should have been migrated to profile processors, but as some client's accounts were configured before the use of profile processors, the Visa, Mastercard and AMEX manual processors can cause issues as gateway mapping for different events is not updated. e.g. In Sandbox trying to test AFTs (Account funding transactions) will fail on manual processors as the AFT flag cannot be added.If a merchant is having issues with manual processors, the process is to archive the manual processors using the retool application ‘GWC Processor Admin’. If you do not already have access to the GWC Processor Admin tool, please raise a ticket [here](https://checkoutsupport.freshservice.com/support/catalog/items/566).

1. 
To archive a processor, select the environment, enter the processing channel ID and processor ID and press ‘submit'

2. Once this is done, configure the profile processors for that scheme and add this profile processor to the gateway and the authentication processing channels.

  1. Gateway Processing Channel

  2. Authentication Processing Channel 

  
  
**6.4.3 Configuring Processing Channels**
Refer to the following Confluence page for detailed instructions on configuring processing channels:

- [Create Gateway Processing Channel UI](https://checkout.atlassian.net/wiki/spaces/ATLAS/pages/1261207637/Create+Gateway+Processing+Channel+UI)

## Glossaries and Definitions:

For **Key Terms and Definitions** on Integration Issues, please see ****[Integrations Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22198412339346-Integrations-Glossary-Introduction)  For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Integration Issues articles, please see ****[Integrations Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22198326164754-Integrations-Tools-Permissions)
