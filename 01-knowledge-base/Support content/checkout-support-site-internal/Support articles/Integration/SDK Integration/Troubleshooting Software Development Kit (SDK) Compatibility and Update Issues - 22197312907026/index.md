---
id: 22197312907026
section_id: 22188565766930
title: "Troubleshooting Software Development Kit (SDK) Compatibility and Update Issues"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22197312907026-Troubleshooting-Software-Development-Kit-SDK-Compatibility-and-Update-Issues"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-09-12T15:44:29Z"
permission_group_id: 26838654181266
content_tag_ids: ["01H8EDHC0MTG4YFD7E4B42CE0V"]
label_names: ["global", "case_integration", "integration_and_usage_of_sdks", "sdks_troubleshooting_resources", "sdk", "sdk_compatibility"]
user_segment_ids: [11003606966930]
archive: false
---

**Use this article when**

Troubleshoot common issues that can occur when integrating and using Checkout.com SDKs, including Mobile SDKs (iOS and Android), Card Issuing SDKs, and 3D Secure SDKs.

It covers problems with version mismatches, API errors, and post-update conflicts. INTRODUCTION TO SDK ISSUES💬

An SDK (Software Development Kit) is a packaged set of tools that helps developers build software for a specific platform or product. It typically includes libraries, APIs, documentation, sample code, and sometimes tooling to streamline integration and development.

Merchants may encounter issues with their Checkout.com SDKs, especially after a recent update to their website or the SDK itself. These problems can be caused by a mismatch between the SDK's version requirements and the merchant's current environment. PROCESS TO TROUBLESHOOT AN SDK ISSUE 🖊️

### Step 1: Identify the SDK and Merchant Environment

- Determine the platform or e-commerce solution being used (e.g. Shopify, Magento, WooCommerce, a custom-built site) and the Checkout.com SDK the merchant is using

- Identify the programming language and version

- Confirm the device, browser and operating system

### Step 2: Check for Compatibility Issues

- Go to the specific SDK's repository on the [Checkout.com GitHub page](https://github.com/checkout)

- Look for the README.md file or a similar document that lists minimum version requirements for the programming language, framework, and other dependencies

- Compare these requirements with the versions the merchant is using and if they are not compatible, advise the merchant on the necessary upgrades

- Ask for recent changes or updates to the merchant’s website

### Step 3: Troubleshoot Issues After an SDK Update

- If the issue occurred after an update, it is likely a compatibility problem with different package versions

- Request that the merchant provide a list of their relevant package versions

- Verify that the merchant's package versions meet the minimum requirements listed in the SDK's documentation on GitHub

- If the minimum versions are met, the issue may be more complex. Proceed to the escalation step

### Step 4: Provide Resources and Support Channels

- If the issue is not a simple compatibility problem, guide the merchant to the appropriate resources

  - Direct them to the main **Checkout.com GitHub page** for access to all SDK libraries

  - For specific internal queries, direct the relevant teams to the appropriate Slack channels

RESOLUTION ⚒️

- 
**Compatibility Issues:** The issue is resolved when the merchant has updated their programming language or framework versions to meet the SDK's requirements

- 
**Post-Update Issues:** The issue is resolved when the root cause has been identified (e.g., a specific package conflict) and a solution has been provided by the SDK team

### How to Check Resolution

- Confirm with the merchant that they have made the recommended changes

- If a ticket was raised, track its status and communicate the resolution to the merchant

ESCALATIONS ⬆️

- 
**When to Escalate:** If the merchant has confirmed that their environment meets all version requirements and is still experiencing issues after an update, the issue should be escalated to the relevant SDK team.

- 
**How to Escalate:**

  1. Assign the ticket to the Merchant Care L2 team

  2. Include all relevant information:

    - The merchant's name and ID

    - The specific SDK and version they are using

    - The programming language, framework and all package versions

    - A detailed description of the error and the steps to reproduce it

    - Any troubleshooting steps already performed

  3. 
**Slack Channels:** Used for internal communication and escalation:

    - #payment-interfaces

    - #ask-frames-sdks

    - #ask-3ds-mobile-sdks

- 
**During Escalation:** Keep the merchant informed of the status of the ticket and heck for updates from the relevant team and follow up as needed.

RESOURCES ⭐️

| External Merchant facing content | - [Developer Resources SDKs](https://www.checkout.com/docs/developer-resources/sdks)  - [3DS-SDK](https://www.checkout.com/docs/developer-resources/sdks/3ds-sdks)  - [3DS-ANDROID-SDK](https://www.checkout.com/docs/developer-resources/sdks/3ds-sdks/3ds-android-sdk)  - [3DS-IOS-SDK](https://www.checkout.com/docs/developer-resources/sdks/3ds-sdks/3ds-ios-sdk)  - [CARD-ISSUING-SDK](https://www.checkout.com/docs/developer-resources/sdks/card-issuing-sdks)  - [RISK-SDK](https://www.checkout.com/docs/developer-resources/sdks/risk-sdks)  - [GITHUB](https://github.com/checkout) |
| --- | --- |

FAQs ⁉️

**Q: How do I know which SDK version the merchant is using?** A: This information should be provided by the merchant. If they are unsure, they can find the version number in their project's dependency file.

**Q: Where can I find the list of required versions for an SDK?** A: The minimum version requirements are typically listed in the README.md file within the specific SDK's repository on the Checkout.com GitHub page.

**Q: A merchant is asking for support on a custom integration that uses an SDK. What should I do?** A: Follow the troubleshooting steps to check for compatibility and update issues. If the issue is complex and not a known problem, it may need to be escalated to the SDK team.
