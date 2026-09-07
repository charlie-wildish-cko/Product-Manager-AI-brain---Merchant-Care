---
id: 29574468806290
section_id: 22188504535954
title: "Response code 401 or 403- Access or API Keys Scope Not Enabled"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/29574468806290-Response-code-401-or-403-Access-or-API-Keys-Scope-Not-Enabled"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-09-29T11:02:37Z"
permission_group_id: 26838654181266
content_tag_ids: []
label_names: ["403", "API_error", "401", "API_Keys", "Invalid_Scope", "access_keys"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

Use this article when a merchant reports receiving an Invalid Scope/401 (Unauthorised) or 403 Forbidden error. 

**Problem:** An API key is missing the required permissions(scopes) to process transactions.

**Solution:** Enable the correct scopes for the API key through the merchant's Dashboard or, if necessary, via the internal CAT tool.  

DESCRIBE THE ISSUE 💬

A merchant's transaction authorization requests fail because their API keys lack the necessary access permissions, or "scopes," leading to lower approval rates and lost revenue.   
This issue shows error codes like `Invalid Scope/401 (Unauthorised)` or `403 Forbidden`, caused by missing scopes on the API keys. Merchants may need specific scopes enabled during onboarding or testing if self-service options are insufficient.  
  
This guide helps identify if the issue is due to insufficient API key permissions and assists with enabling required scopes during onboarding or testing.  
  
💡 Merchants with owner permissions can manage their own API keys and scopes via the Dashboard, encourage them to self-serve by guiding them through the process 

KEY TAKEAWAYS 🔑  
 

- API keys must have the correct scopes enabled to function properly

- Merchants with owner permissions can manage their own API keys and scopes via the Dashboard

- Agents can check and update key scopes for merchants using the internal CAT tool

- Direct merchants to self-service documentation for a faster resolution. 

TROUBLESHOOTING INVALID SCOPE/401 OR 403 FORBIDDEN🖊️

  
**Step 1. Check Key Permissions (For Agents)**

- Navigate to the merchant's account in **CAT**

- Go to the **Keys** section

- Select the specific API key type that is experiencing the issue

- Review the associated scopes to determine if the necessary permissions are enabled

**Step 2. Remediate the Issue**

- 
**For Agents:** If the required scope is not enabled, enable it directly within CAT

- 
**For Merchants (Self-Service):**

  - Advise the merchant to sign into their **Dashboard**

  - Guide them to navigate to the **Developers** icon in the top navigation bar then select the **Keys** tab

  - Instruct them to enable the appropriate scopes for their API keys directly from their Dashboard

- Provide the following resources for their reference:

  - [Manage API Keys on Dashboard](https://www.google.com/search?q=https://checkout.atlassian.net/wiki/spaces/LL/database/6990364784%3Fatl_f%3DPAGETREE)

  - [API Authentication - Available Scopes & Claims](https://www.google.com/search?q=https://checkout.atlassian.net/wiki/spaces/LL/database/6990364784%3Fatl_f%3DPAGETREE)

RESOLUTION ⚒️

Merchants can self-manage their API keys and scopes. Users with owner permissions are authorised to view, create and edit scopes for all keys.

**L2 Support Agent Steps**

- If the required scope is not enabled for the key in CAT, enable it.

FAQs⁉️

**Q. Who can edit API key scopes?**

A. Only users with owner permissions on the merchant's account can edit API key scopes via the Dashboard. Agents can also enable scopes using the CAT tool.

## RESOURCES 📍

| Tools | Case Examples | Related |
| --- | --- | --- |
| - [CAT](https://client-admin.cko-sbox.ckotech.co/web/nas/)  -  [Dashboard](https://dashboard.sandbox.checkout.com/implicit/callback) | - [51201](https://checkout1360.zendesk.com/agent/tickets/51201)  - [46300](https://checkout1360.zendesk.com/agent/tickets/46300)  - [66797](https://checkout1360.zendesk.com/agent/tickets/66797) | - [Scope Creation Guidelines](https://checkout.atlassian.net/wiki/spaces/ACK/pages/5357568795/Scope+Creation+Guidelines)  - [Manage API Keys on Dashboard](https://www.checkout.com/docs/developer-resources/api/manage-api-keys/oauth-2-0-client-credentials#Manage_your_keys_in_the_Dashboard)   - [Dashboard scopes](https://checkout.atlassian.net/wiki/spaces/ACK/pages/5533171879/Dashboard+scopes)  - [API Authentication - Available Scopes & Claims](https://checkout.atlassian.net/wiki/spaces/ACK/pages/1063485997/API+Authentication+-+Available+Scopes+Claims) |
