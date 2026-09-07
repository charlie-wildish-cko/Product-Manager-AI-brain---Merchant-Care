---
id: 22197332618898
section_id: 22188504904594
title: "Troubleshooting Processing Channels"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22197332618898-Troubleshooting-Processing-Channels"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:37:32Z"
permission_group_id: 26838654181266
content_tag_ids: ["01H8EDHC0MTG4YFD7E4B42CE0V"]
label_names: ["global", "case_integration", "troubleshooting_processing_channels", "processing_channels_on_cat"]
user_segment_ids: [11003606966930]
archive: false
---

## Process Steps

1. Check Production Setup: Verify the merchant's production setup for any misconfigurations. For example, if a merchant has presented the issue that certain currencies are not being processed, the teammate will need to check that the desired currency(s) are enabled on NAS.

2. Reproduce Settings in Sandbox: If no misconfigurations are found, replicate the processor settings in the sandbox account to identify the issue, and send the same request the merchant is sending to reproduce the error.

For example, if the issue is with an API request, send the same request the merchant sent to reproduce the error and check which of the parameters are causing the issue. You will be able to find your request on Postman or Datadog, and the merchants on Datadog.

## Glossaries and Definitions:

For **Key Terms and Definitions** on Integration Issues, please see ****[Integrations Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22198412339346-Integrations-Glossary-Introduction)  

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Integration Issues articles, please see ****[Integrations Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22198326164754-Integrations-Tools-Permissions)
