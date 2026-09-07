---
id: 22197332680082
section_id: 22188504904594
title: "Alternative Payment Methods (APMs) Configuration and Troubleshooting"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22197332680082-Alternative-Payment-Methods-APMs-Configuration-and-Troubleshooting"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-09-29T18:19:07Z"
permission_group_id: 26838654181266
content_tag_ids: ["01H8EDHC0MTG4YFD7E4B42CE0V"]
label_names: ["apms", "global", "case_integration", "processing_channels_on_cat", "APM config", "apm"]
user_segment_ids: [11003606966930]
archive: false
---

**Use this article when**

Configuring and troubleshooting Alternative Payment Methods (APMs) for merchants. It is primarily for the **Merchant Care L1 team** to help with setup and common configuration problems.

**Problem/Symptom:** A merchant is having issues with their APM setup or functionality.INTRODUCTION TO APM CONFIGURATION💬

We configure an AMP to let merchants accept specific payment methods in certain countries/currencies and route payments correctly. This setup ensures:

- Proper processing profiles and gateway processors for end-to-end payment authorization and reconciliation.

- The APM service has the merchant’s credentials to communicate with third parties via onboarding/config endpoints.

- Internal components (like APM Consumer and Scheduler) are configured for event flow and reconciliation, especially for Reverse API APMs requiring Scheduler setup in Secrets Manager.

TOOLING 📍

| **Retool ** Request access using this🔗[Link](https://checkoutsupport.freshservice.com/support/catalog/items/722). | Complete the ticket with the following information:   -  **Environment**: Production  -  **Application Name(s)**: GWC Processor Admin  -  **Permission**: Viewer |
| --- | --- |

## MERCHANT CARE LEVEL 1 GUIDANCE 🖊️

Sandbox Environment

- APMs are configured under **processing profiles**

- 
**Tier 4 merchants** should be directed to the **Merchant Care L2 (Integrations)** team for sandbox configuration - this team uses the ****[CAT Configuration Helper](https://cat-configuration-helper.ckotech.co/) tool

- **Tiers 1-3 merchants** must contact their **Account Manager (AM)** or **Solutions Engineer (SE)** for APM setup

Production Environment

- APMs are configured by the **Merchant Configuration** team

- For **Tiers 1-3**, the **AM/Sales team** submits a **Merchant Configuration Request (MCR)**, which must include an updated pricing schedule and merchant consent

- For **Tier 4 merchants**, the **Merchant Care L1** team is responsible for raising the **MCR** to the Merchant Configuration team

Troubleshooting APM Configuration

If a merchant is experiencing issues, follow these steps:

- 
**Account Configuration Check:** Use the ****[CAT APM configuration guide](https://checkout.atlassian.net/wiki/spaces/APM/pages/4393566788/APM+on+NAS+Processing+profile+configuration#Sofort-%E2%9A%99%EF%B8%8F) to verify all settings are correct

- 
**Reconfigure Processors:**

  - Check that the **processors** and **processing channels** are set up correctly.

  - If a processor is causing issues, you may **archive** it

  - Use the **GWC Processor Admin** tool to perform this action

 

**💡Tip:** Archive instead of delete, as archival can be reversed 

- To archive a processor, select the correct environment, and provide the **processing channel ID** and **processor ID**

ESCALATIONS ⬆️

For issues that cannot be resolved using the steps above, or for specific configuration requests, escalate accordingly:

- 
**Sandbox Configuration (Tier 4):** Escalate to the **Merchant Care L2 (Integrations)** team.

- 
**Production Configuration (Tiers 1-3):** Direct the merchant to their **AM/Sales team** to submit a **Merchant Configuration Request (MCR)**.

- 
**Additional Assistance:** Consult the **#apms-support** Slack channel to get help from the APM team.

RESOURCES ⭐️

| -  **APM Live Portfolio:** Use this [tool](https://checkout.atlassian.net/wiki/spaces/APM/pages/5137072925/APM+Live+Portfolio) to check the availability of specific APMs by country   -  **Confluence Page:** For detailed instructions on processing profile configuration and required credentials for sandbox APM setup follow [this Confluence Page](https://checkout.atlassian.net/wiki/spaces/APM/pages/4393566788/APM+on+NAS+Processing+profile+configuration)   - **Slack Support:** For additional assistance, consult the **#apms-support** Slack channel to engage with the APM team |
| --- |
