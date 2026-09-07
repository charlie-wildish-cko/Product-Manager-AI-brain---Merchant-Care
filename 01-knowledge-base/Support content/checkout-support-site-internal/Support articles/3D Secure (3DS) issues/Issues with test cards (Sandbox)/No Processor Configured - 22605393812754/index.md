---
id: 22605393812754
section_id: 22604832741650
title: "No Processor Configured"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22605393812754-No-Processor-Configured"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:35:59Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRP1QGWAFPTEP0CSMC1WBV"]
label_names: ["global", "case_3ds_issues", "no_processor_configured", "case_3ds_issue_issues_with_test_cards_sandbox"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

**Issue**: Payment is not being processed using the relevant scheme in the MENA Region

## Process Steps

**How to investigate this issue**

1. Check that the processor has been configured correctly

2. Ensure that processing is using the correct protocol

**Resolution**

1. We checked the processing on the old platform to confirm if they used to process AMEX and did not find AMEX transactions for the past 6 months. This issue had been resolved as there wasn’t an AMEX processor configured.  This means that AMEX needs to be enabled on the account to be able to process customer AMEX cards

2. TARAMA FZ LLC is a UAE legal entity and AMEX can only be configured as gateway only. The merchant needs to reach out to AMEX to get the GW AMEX MID for each currency that needs to be enabled

3. Once we have the MIDs and the pricing consent, we will initiate the change request to enable AMEX for your account.

Please see the ticket [here](https://checkout1360.zendesk.com/agent/tickets/14955).

## Glossaries and Definitions

For **Key Terms and Definitions** on 3DS, please see ****[3DS Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22059673420818-3DS-Glossary-Introduction)   

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the 3DS articles, please see ****[3DS Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22059810908306-3DS-Tools-Permissions)
