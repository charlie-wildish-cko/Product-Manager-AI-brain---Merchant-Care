---
id: 22197327103122
section_id: 22188517144978
title: "Troubleshooting Webhook Authentication"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22197327103122-Troubleshooting-Webhook-Authentication"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-12-09T10:13:32Z"
permission_group_id: 26838654181266
content_tag_ids: ["01H8EDHC0MTG4YFD7E4B42CE0V", "01JVM5TPJQV63X1YGHPGKWQTJN"]
label_names: ["global", "case_integration", "case_integration_issue_webhook_not_working", "webhook_documentation", "webhook_introduction", "webhooks", "webhook_authentication"]
user_segment_ids: [11003606966930]
archive: false
---

**Use this article **

To troubleshoot the reason a webhook is failing, this could be due to incorrect authentication.INTRODUCTION TO WEBHOOK AUTHENTICATION💬

Incorrect authentication is a common reason for webhook failures. The **Webhook Auth** and **Private Key** must match on both the merchant's server and in their Checkout.com Dashboard to ensure a secure and successful connection.PROCESS TO TROUBLESHOOT WEBHOOK AUTHENTICATION 🖊️

Ask the merchant to confirm that the Webhook keys, **Authorization Header Key **and **Signature Key, **generated in the Webhooks page in the Dashboard's developer section match the merchant's server configuration. 

 

**If the keys do not match: **

- If the merchant has the correct keys saved elsewhere (e.g. in their SDK), they can configure their setup with the correct keys. 

- If the merchant does not have the keys saved, they will need to create a **new webhook** and generate new authentication and private keys. 

- They should then delete the old, incorrect webhook. The steps the merchant should take are provided in the external documentation: [Webhooks](https://www.checkout.com/docs/business-operations/use-the-dashboard/developers/webhooks#Create_a_webhook_configuration)

RESOURCES ⭐️

| External Documentation |
| --- |
| Merchants can find detailed webhook management documentation in these resources:   - [Webhooks - Docs](https://www.checkout.com/docs/business-operations/use-the-dashboard/developers/webhooks)  - [Manage Webhooks - Docs](https://www.checkout.com/docs/business-operations/use-the-dashboard/developers/webhooks#manage-webhooks)  - [Event Types - Docs](https://www.checkout.com/docs/business-operations/use-the-dashboard/developers/webhooks#event-types)  - [Webhook Management - Docs](https://www.checkout.com/docs/business-operations/use-the-dashboard/developers/webhooks#webhook-management) |
