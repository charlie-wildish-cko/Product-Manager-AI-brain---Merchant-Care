---
id: 31061908424210
section_id: 29824613373714
title: "Intelligent Acceptance: Strategy & Add-On Reference"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/31061908424210-Intelligent-Acceptance-Strategy-Add-On-Reference"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-12-09T10:20:45Z"
permission_group_id: 26838654181266
content_tag_ids: []
label_names: []
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

To understand the available Intelligent Acceptance (IA) strategies within the **Client Admin Tool (CAT)** and the specific **Add-On** features that can be enabled with custom configurations. 

This is essential for selecting the correct strategy based on a merchant's technical integration and business goals.

## KEY IA STRATEGY DIFFERENCES 🔑

The choice of strategy primarily depends on the merchant's ability to handle **3D Secure (3DS) Redirects**.

⚠️ This is the single most critical factor that determines the configuration template.

 

| **Description** | **Key Requirement/Benefit** | **Add-On Support** |
| --- | --- | --- |
| Strategy template: default_intelligent_acceptance The standard, out-of-the-box strategy. IA handles general payment optimization (e.g., adaptive messaging, dynamic routing) without specific customization. | Simple and zero-touch. **Does not attempt 3DS Upgrades.** | ❌ **NOT SUPPORTED** |
| Strategy Template: custom_3DS_upgrade Recommended for merchants whose integration can successfully manage a **3DS Redirect URL** from the payment gateway in the API response. | Allows IA to strategically **upgrade** low-risk, non-3DS transactions to 3DS to maximize liability shift and acceptance. | ✅ **SUPPORTED** |
| Strategy Template: Customer-no-3DS-upgrade Used for merchants who require custom optimizations but **cannot** handle a 3DS Redirect, or for specific markets where 3DS is less common (e.g., high-volume US traffic). | Prevents IA from attempting 3DS Upgrades, avoiding potential integration failures and payment friction. | ✅ **SUPPORTED** |

💡 Best Practice: The `custom_3ds_upgrade` strategy offers the most powerful optimization potential by leveraging the liability shift benefit of 3DS authentication. Always select this if the merchant's integration supports it.

## IA ADD-ON FEATURES (CUSTOM STRATEGIES ONLY) ⊕

Add-Ons are modular features that can be enabled or disabled to fine-tune the optimization logic for merchants using a **Custom** strategy (`custom_3ds_upgrade` or `custom-no-3ds-upgrade`).

| **Add-On Feature** | **Description** | **Business Impact** |
| --- | --- | --- |
| **Dynamic Routing** | IA dynamically routes transactions across multiple configured processing channels in real-time to find the path with the highest probability of approval and/or lowest cost. | Maximizes acceptance rates by circumventing temporary processor outages or low-performance routing rules. |
| **Intelligent Retries** | Automatically re-submits certain declined transactions (e.g., soft declines like 'Do Not Honor') using a different channel, time, or modified data, based on predicted success. | Recovers failed transactions, directly increasing revenue without merchant intervention. |
| **Adaptive Messaging** | Adjusts or enriches the data fields sent in the transaction request (e.g., ISO formats, specific 3DS fields) to meet the unique preferences or requirements of the card Issuer/Network. | Reduces unnecessary "soft" declines caused by technical formatting issues or missing/incorrect data. |
| **Network Tokenization** | Strategically requests and utilizes Network Tokens (e.g., Visa Token Service, Mastercard Digital Enablement Service) instead of the Primary Account Number (PAN) for certain transactions. | Improves security, reduces fraud, and often results in higher acceptance rates due to better issuer confidence and no card expiration date issues. |

### PROCESS: CCONFIGURATION STEPS IN CAT 🖊️

1. Open the **Client Admin Tool (CAT)** and navigate to the merchant's IA configuration.

2. Ensure a **Custom Strategy** (`custom_3ds_upgrade` or `custom-no-3ds-upgrade`) is selected.

3. Locate the **Add-Ons** section.

4. Toggle the required features **ON** or **OFF** based on the merchant's agreed-upon strategy.

5. **Save** the changes to deploy the configuration.

 

## COMMON CONFIGURATION WARNINGS ⚠️

| **Issue** | **Resolution / Best Practice** |
| --- | --- |
| **Pilot Program Lock** | If CAT prevents configuration due to a "pilot program" status, **Escalate** immediately to the Payment Performance team via JIRA to request removal. |
| **Traffic Allocation** | Setting traffic below 100% slows down IA's learning curve. **Advise commercial team** to set it to 100% for fastest time-to-value. |
| **Selecting Wrong 3DS Strategy** | If `custom_3ds_upgrade` is used for a non-3DS capable merchant, it will cause **payment failures**. Always confirm the merchant's integration capability first. |

 

## RELATED ARTICLES ⭐

-  [Configuring a Merchant for Intelligent Acceptance (IA)](https://checkoutint.zendesk.com/hc/en-us/articles/29835307864338)
