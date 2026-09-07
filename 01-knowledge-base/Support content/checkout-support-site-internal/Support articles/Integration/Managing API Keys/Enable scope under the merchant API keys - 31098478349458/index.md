---
id: 31098478349458
section_id: 22188504535954
title: "Enable scope under the merchant API keys"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/31098478349458-Enable-scope-under-the-merchant-API-keys"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-11-16T10:05:50Z"
permission_group_id: 26838654181266
content_tag_ids: []
label_names: []
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

Use this process when a merchant requests an API scope that is not available for self-service and requires specialized configuration.INTRODUCTION 💬

In the world of APIs, the scope defines the specific permissions or access rights that an application (like a third-party app) is granted when it uses an API.

💡 It answers the question: "What is this app allowed to _do_ or _see_?"

The process of **enabling scope** serves two main purposes:

1. **Security:** It ensures that an application can only access the minimum amount of data or functionality it needs to work. 

2. **Functionality:** It tells the API exactly what requests to accept from the third-party app. I

KEY TKEAWAYS 🔑

- Merchants can self-serve and add scopes to their keys via the Dashboard - this allows them to manage their API keys and associated scopes without needing additional configuration.

- Some sensitive scopes are not made available to the merchant to update via self-serve.

### ⚡️ Merchant Self-Service API Scopes

Merchants can enable the following essential configuration and onboarding scopes themselves:

| **Category** | **Scope Purpose** | **Examples of Scopes** |
| --- | --- | --- |
| **Apple Pay Domain Management** | Manage authorized domains for Apple Pay integration. | Register Merchant (add domain), Unregister Merchant (remove domain). |
| **Google Pay Onboarding** | Initiate setup and register domains for Google Pay. | Onboard Merchant (start process, accept ToS), Register Merchant's Domain. |
| **Payment Interfaces (Vault/Middleware)** | Set up static keys for essential payment functions (e.g., Hosted Pages). | `vault:tokenization`, `middleware:merchants-public`. |

PROCESS TO REQUEST SCOPE ENABLEMENTS 🖊️

This process is used when a merchant requires an API scope that is unavailable for self-service and must be requested from the Configuration Team.

### Step 1. Preparation & Verification

- **Confirm API Key:** Ask the merchant to confirm the exact display name of the API key that needs modification.

- **Identify Scope:** Clearly identify the specific, technical name of the scope (e.g., `reports:read:full`) that the merchant needs to add or remove.

### Step 2. Escalate to the Merchant Configuration Team

| Use this macro: Tranfer > Merchant Configuration > Regional |
| --- |

- **Populate Details:** Add details to the macro: API Key Display Name, the Merchant ID (if required), the Action (ADD or REMOVE), and the exact Scope Name.

### Step 3. Follow-Up and Completion

- **Inform Merchant:** Communicate to the merchant that the request has been escalated and provide the expected turnaround time.

1. **Await Confirmation:** Monitor the internal request until the Configuration Team confirms the scope update is complete.

2. **Final Notification & Testing:** Reply back to the merchant confirming the change and instruct them to check and test the new functionality on their end.
