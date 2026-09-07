---
id: 30451383323794
section_id: 29824613373714
title: "Modifying an Active Intelligent Acceptance (IA) Strategy"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/30451383323794-Modifying-an-Active-Intelligent-Acceptance-IA-Strategy"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-11-19T13:20:40Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTZ6WEQ3S7TQ9KW35WKJXPDX", "01JWRC3HBBCWV9KD022M3M3WQQ", "01K6AASRZ015NW9D6WTY6VAF3X", "01KA9EAWAZDR0YQJAQJ63NKW93"]
label_names: ["IA", "IA_Configuration"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

Use this guide to understand and execute modifications to an existing **Intelligent Acceptance (IA)** configuration for a merchant using the **Client Admin Tool (CAT)**. This process is necessary when a merchant's business requirements or technical capabilities change post-onboarding.DESCRIBE THE ISSUE 💬

After initial onboarding, a merchant may need to **modify their active IA strategy**. This article outlines the three methods of adjustment and clarifies the scope of possible changes within CAT, ensuring modifications align with the merchant's current capabilities and goals.KEY TAKEAWAYS 🔑

- All IA strategy adjustments are performed in the **Client Admin Tool (CAT)** by the Merchant Configuration team.

- There are three primary adjustment methods: **Changing the Core Strategy Template**, **Enabling/ Disabling Add-On Features**, and **Adjusting Traffic Allocation**.

- **Add-Ons** are only available for merchants on a **Custom Strategy Template**.

- **Frequent changes** to **Traffic Allocation** are highly discouraged as they complicate the measurement of IA's impact.

- IA traffic **cannot** be restricted to specific entities, regions, MCCs, processing channels, or traffic types.

TOOLING📍

| **Tool** | **Environment** | **Permissions** | **Access** |
| --- | --- | --- | --- |
| **Client Admin Tool (CAT) ******[here](https://client-admin.cko-prod.ckotech.co/web/nas/clients/cli_z52caftvrpqedc3oqs2hva3ume/entities) | Sandbox and Production | Super User (both), Super Admin (Sandbox only) | Access granted via [jira link for access] |

PROCESS FOR ADJUSTING AN ACTIVE IA STRATEGY 🖊️

This process is completed by the Merchant Configuration Team, L2 Support should understand the steps involved.

### Prerequisite: Access the Configuration

- Open **CAT** and select the merchant.

- Navigate to **Services** > **Intelligent Acceptance**

### 1. Changing the Core Strategy Template

This involves switching the merchant's base configuration (e.g., from `default_intelligent_acceptance` to `custom_no_3ds_upgrade`).

| **Action** | **How to Change** | **When to Use** |
| --- | --- | --- |
| **Change Template** | Select a new template from the **Strategy** dropdown in CAT. | The merchant's **core technical capabilities have changed** (e.g., they can now handle 3DS redirects > switch to `custom_3ds_upgrade`). **OR** The merchant requires the use of **Add-Ons** (must switch from `default` to a `custom` template). |

### 2. Enabling or Disabling Add-On Features

This is the most common way to fine-tune a strategy and is **only available for Custom templates**.

- **How:** Use the add-on controls (checkboxes) in CAT to enable or disable specific optimization groups (e.g., enabling the "Disable CVV optimizations" box).

- **When to Use:** Ideal for tailoring the IA service to a merchant's preferences **without changing the entire strategy**.

### 3. Adjusting Traffic Allocation Percentage

This changes the percentage of the merchant's total transaction volume processed by IA.

- **How:** Navigate to the **Traffic Allocation** section in CAT and set a value between 0 and 100.

**❗ Important Warning:** **DO NOT** change this value frequently. Each change negatively affects the ability to measure IA's impact and demonstrate value. Frequent requests must be **escalated**.

**Reference:** Consult the 'Intelligent Acceptance Strategies (CAT onboarding)' documentation for a full list and description of available add-ons [here](https://checkout.atlassian.net/wiki/spaces/ARM/pages/5757370964/Intelligent+Acceptance+Strategies+CAT+onboarding)

### What Cannot Be Adjusted or Implemented ❌

IA's scope is defined and **cannot** be restricted to specific:

- Entities

- Regions

- MCCs

- Processing Channel

- Traffic types

Additionally, **new features are not implemented to fix incorrect merchant payloads**. Merchant payload issues must be resolved by the merchant.ESCALATION ⏫

Escalate the following situations to the **Payment Performance Team** via their **jira** project.

- A merchant is requesting **frequent changes** to their traffic allocation percentage.

- A merchant is flagged as **"pilot"** in CAT, preventing enablement/modification. Request to have them moved to **GA (General Availability)**.

- A merchant is requesting a **new optimization feature** that is not currently available as an add-on. Include the use case in detail.

FAQs ❓

**Why shouldn't I frequently change the Traffic Allocation Percentage?**

Each change affects the overall measurement of IA's impact, making it harder to accurately prove the value of the service.

**What configuration changes are not possible?**

It is not possible to restrict IA processing to specific entities, regions, MCCs, processing channels, or traffic types.

**What should I do if a merchant wants a new optimization feature?**

Escalate the request via the #ask-intelligent-acceptance Slack channel, explaining the use case in detail.
