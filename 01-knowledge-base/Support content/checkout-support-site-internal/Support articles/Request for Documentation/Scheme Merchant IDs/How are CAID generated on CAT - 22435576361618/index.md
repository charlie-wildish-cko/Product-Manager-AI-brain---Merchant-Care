---
id: 22435576361618
section_id: 22435335461522
title: "How are CAID generated on CAT?"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22435576361618-How-are-CAID-generated-on-CAT"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:36:40Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JBHFK1FTRFHHXXN4PTQS8A0A"]
label_names: ["global", "case_request_for_documentation", "case_rfd_issue_scheme_merchant_ids", "how_are_caid_generated_on_cat"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

The CAID lies on the Scheme Processing Profile within CAT. CAID is generated based on entity, MCC and Acceptor Country combination. When updating a processor we have 4 options.

## Process Steps

| **Options** | **Scenarios** |
| --- | --- |
| To apply the default CAID - First-time CAID generated under an entity is known as the **default** | -  Use default CAID (Optional) |
| -  Card acceptor ID (Optional) |  |
| -  MCC |  |
| -  Force CAT to generate a new CAID (Optional) |  |
| To autogenerate a new CAID  - To create a New CAID other than the default, you then force CAT  - If you do not toggle the _Force CAT to generate a new CAID_, the processor will take up the default | -  Use default CAID (Optional) |
| -  Card acceptor ID (Optional) |  |
| -  MCC |  |
| -  Force CAT to generate a new CAID (Optional) |  |
| To register a bespoke CAID or reuse a non-default CAID from another processor  - Paste the CAID you want to manually enable  - Selete the MCC and Save | -  Use default CAID (Optional) |
| -  Card acceptor ID (Optional) |  |
| -  MCC |  |
| -  Force CAT to generate a new CAID (Optional) |  |

  
For more information regarding CAID Generation - CP Payout Processing Profiles, please click [here](https://checkout.atlassian.net/wiki/spaces/PTCV2/pages/4865590143/CAID+Generation+-+CP+Payout+Processing+Profiles).

## Glossaries and Definitions:

For **Key Terms and Definitions** on Scheme Merchant IDs Issues, please see ****[Scheme Merchant IDs Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22435560608402-Scheme-Merchant-IDs-Glossary-Introduction) For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Scheme Merchant IDs articles, please see ****[Scheme Merchant IDs Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22435536975122-Scheme-Merchant-IDs-Tools-Permissions)
