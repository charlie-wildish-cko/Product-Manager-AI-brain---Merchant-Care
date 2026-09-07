---
id: 29835307864338
section_id: 29824613373714
title: "Configuring a Merchant for Intelligent Acceptance (IA)"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/29835307864338-Configuring-a-Merchant-for-Intelligent-Acceptance-IA"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-11-18T14:31:34Z"
permission_group_id: 26838654181266
content_tag_ids: ["01K6AASRZ015NW9D6WTY6VAF3X", "01KA9E5P6SV6YT66FXH3ZHMSVC", "01KA9EAWAZDR0YQJAQJ63NKW93"]
label_names: ["IA", "IA_strategy", "IA_Configuration"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

Use this article as a guide to ensure a merchant is correctly configured on **Intelligent Acceptance (IA)** via the Client Admin Tool (CAT) for optimal payment performance. Incorrect configuration, especially regarding 3DS handling, can lead to failed payments.DESCRIBE THE ISSUE 💬 

A merchant requires proper configuration in CAT to maximize the value of the Intelligent Acceptance product. Choosing an incorrect strategy, particularly concerning 3DS (3D Secure) handling, can result in sub-optimal performance and poor merchant experience.

**💡 Note:** This process is typically carried out by the Merchant Configuration team following requests from Commercial teams.KEY TAKEAWAYS 🔑

- The **most critical step** is selecting the correct IA strategy (template), which is based on the merchant's ability to handle 3DS redirects.

- **Traffic Allocation** should ideally be set to **100%** to accelerate the algorithm's learning and value demonstration.

- Custom templates allow for enabling specific **Add-Ons** to further tailor the optimization strategy.

- IA traffic optimization **cannot** currently be limited by specific entity, region, or MCC.

TOOLING**📍**

| Tools | Access |
| --- | --- |
| **Client Admin tool (CAT) ******[here](https://client-admin.cko-prod.ckotech.co/web/nas/) **Environment: **Sandbox and Production | **Permissions: **Super User (both environments) - Super Admin ( sandbox only) ** Access granted via ******[jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274) |

PROCESS FOR INTELLIGENT ACCEPTANCE CONFIGURATION 🖊️ 

⚠️ **Warning:** Before proceeding, verify the merchant meets the [Intelligent Acceptance Eligibility Criteria](https://checkoutint.zendesk.com/hc/en-us/articles/30272267778578-Intelligent-Acceptance-Eligibility-Criteria) - Do not configure if the merchant is not a good fit.

### **Step 1: Set the Traffic Allocation Percentage**

This determines the percentage of the merchant's traffic IA is allowed to optimize.

- Open **CAT** and select the merchant

- Navigate to **Services** > **Intelligent Acceptance**

- Select **Traffic Allocation**

- Set the desired percentage

**Best Practice:** Set the allocation to **100%**. This provides maximum data for faster algorithm learning and value demonstration.

**Staggered Rollout:** If a lower percentage is requested, inform the merchant that this will increase the time needed to prove the product's impact. Avoid frequent changes to this setting.

 

### 

### **Step 2: Select the Right Strategy (Template)**

⚠️ This step is critical and relies on the Account Manager's understanding of the merchant's technical capabilities.

Select the **Configuration** section:

| **Option** | **Template** | **When to Use** |
| --- | --- | --- |
| **A. Simple Config** | `default_intelligent_acceptance` | For simple needs without customization. **Note:** Does not support custom Add-Ons. |
| **B. Custom Config** | Determined by 3DS capability (see below). | For merchants requiring customization and Add-Ons. |

Custom Configuration Selection

Determine if the merchant's integration can handle a **3DS redirect URL** in the API response:

- **✅ If YES:** Select `custom_3ds_upgrade`. This enables IA to upgrade transactions to 3DS for powerful optimization.

- **❌ If NO:** Select `custom-no-3ds-upgrade`. This prevents IA from attempting 3DS upgrades, avoiding integration failures. _Recommended for merchants with high US traffic where 3DS is less common._

### **Step 3: Configure Add-Ons (Custom Templates Only)**

If a custom template was selected, you can enable or disable specific add-on features to fine-tune the strategy.

- **Reference:** Consult the [Intelligent Acceptance Strategies (CAT onboarding)](https://checkout.atlassian.net/wiki/spaces/ARM/pages/5757370964/Intelligent+Acceptance+Strategies+CAT+onboarding) documentation for a full list and description of available add-ons 

 

## ESCALATION ⬆️

If CAT displays a "pilot program" message and prevents you from onboarding the merchant:

- Contact the **Payment Performance team** via their **jira** project

- Request that they remove the merchant from the pilot program

- Once removed, proceed with the standard onboarding process above

**Required Information for Escalation:**

- The merchant's ID

- A clear description of the merchant's use case

- Details of the issue or error message encountered in CAT

 

## RELATED ARTICLES ⭐

| - [Intelligent Acceptance Strategies (CAT onboarding)](https://checkout.atlassian.net/wiki/spaces/ARM/pages/5757370964/Intelligent+Acceptance+Strategies+CAT+onboarding)  - [Troubleshooting Gateway Http Status Code 401](https://checkoutint.zendesk.com/hc/en-us/articles/Troubleshooting%20Gateway%20HTTP%20Status%20Code%20401-Troubleshooting-Gateway-http-status-code-401) |
| --- |
