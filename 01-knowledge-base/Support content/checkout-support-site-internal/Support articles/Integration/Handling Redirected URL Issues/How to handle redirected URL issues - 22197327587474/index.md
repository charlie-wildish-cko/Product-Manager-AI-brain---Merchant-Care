---
id: 22197327587474
section_id: 22188556181906
title: "How to handle redirected URL issues"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22197327587474-How-to-handle-redirected-URL-issues"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:37:32Z"
permission_group_id: 26838654181266
content_tag_ids: ["01H8EDHC0MTG4YFD7E4B42CE0V"]
label_names: ["global", "case_integration", "case_integration_issue_redirected_url_issues", "how_to_handle_redirected_url_issues"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

This article outlines the steps to troubleshoot and resolve issues related to redirected URLs for payment requests in Checkout.com. Merchants may encounter situations where payments are redirected to incorrect URLs.

## Process Steps

**Identifying the Issue**

When a merchant submits a payment request, they can either:

- Pass in the success and failure URLs as part of the request.

- Use the URLs configured under the processing channels on the Client Admin Tool (CAT) as default.

If a merchant reports that the payment is redirected to the wrong URL, it may indicate that the default URLs are being used.

 **Verify URLs in CAT**

1. 
**Access CAT**:

  - Ensure you have access to CAT using the appropriate environment URL:

    - 
**Sandbox**: [Sandbox Environment](https://client-admin.cko-sbox.ckotech.co/web/)

    - 
**Production**: [Production Environment](https://client-admin.cko-prod.ckotech.co/web/)

2. 
**Check Success/Failure URLs**:

  - Log in to CAT and navigate to the processing channel associated with the merchant (Entity → Processing → Gateway → select the relevant Processing Channel)

  - Verify the configured success and failure URLs.

1. 
**Confirm with the Merchant**:

  - Contact the merchant to confirm whether the URLs configured in CAT match their intended success and failure URLs.

 **6.6.2.2  Check 3DS Log**

1. 
**Access 3DS Log: **Use Datadog to access the 3DS log for the specific transaction

2. 
**Verify Redirection URL:**

  1. Check the 3DS log to see if the user was redirected

  2. Confirm the URL used for redirection by looking at the parameter _RedirectUri_

1. 
**Resolving the Issue **based on the findings from the above steps:

  1. 
**Correct URLs in CAT:**

    - If the URLs in CAT are incorrect, update them to the correct success and failure URLs as specified by the merchant

  2. 
**Confirm API Request Parameters:**

    - Ensure that the merchant is correctly passing the success and failure URLs as part of the payment request, if not relying on defaults

  3. 
**Follow-Up**

    1. 
**Test the Changes**:

      1. After making corrections, ask the merchant to conduct a test transaction to ensure that the redirection URLs are functioning as expected

    2. 
**Communicate with Merchant**:

      1. Inform the merchant of the changes made and the outcome of the test transaction

      2. Guide how to correctly configure URLs in future payment requests

If you are unable to resolve the issue through the above steps, escalate to the appropriate team or use the following Slack support channel: **#ask-gateway**

## Glossaries and Definitions:

For **Key Terms and Definitions** on Integration Issues, please see ****[Integrations Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22198412339346-Integrations-Glossary-Introduction)  

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Integration Issues articles, please see ****[Integrations Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22198326164754-Integrations-Tools-Permissions)
