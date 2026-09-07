---
id: 29459755737618
section_id: 22188517144978
title: "User Unable to Create Webhooks Error"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/29459755737618-User-Unable-to-Create-Webhooks-Error"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-12-09T09:22:57Z"
permission_group_id: 26838654181266
content_tag_ids: ["01H8EDHC0MTG4YFD7E4B42CE0V", "01JVM5TPJQV63X1YGHPGKWQTJN"]
label_names: ["global", "webhook_troubleshooting", "case_integration", "webhook_troubleshooting_steps", "case_integration_issue_webhook_not_working"]
user_segment_ids: [11003606966930]
archive: false
---

**Use this article when**

A merchant is unable to create a new webhook in the Dashboard. INTRODUCTION TO THE ISSUE 💬 

A user may report that they are unable to create a new webhook in the Dashboard. This issue is typically caused by incorrect user permissions or disabled services.

⚠️ **Note:** For live accounts, the Merchant Config team must handle key changes. For sandbox accounts, the Merchant Care team can perform these changes.  TROUBLESHOOTING A USER UNABLE TO CREATE WEBHOOKS ERROR🖊️

- Verify if the user has the necessary permissions in the Dashboard under **Settings > User Permissions > Notifications**

💡 Access management should be handled by the merchant

- Next, check the **Client Admin Tool (CAT)** to make sure the **"Flow"** service is enabled for the client

- Finally, check the access keys to ensure the **"Flow" scope** is enabled

- **Keys → Access keys → Select the access key → Search 'flow' and check the related scopes**

- Do the same for the API keys

ESCALATION ⬆️

If the issue persists:

- Please raise escalations with the L2 team

- Use the: #ask-notifications Slack channel to consult the notifications team
