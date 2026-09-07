---
id: 21991182137618
section_id: 23045958401426
title: "Processing channel switched off"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/21991182137618-Processing-channel-switched-off"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:40:01Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQT889RQXXSG27BB4ZJ0M"]
label_names: ["case_transactions", "ROW", "case_transactions_issue_all_transactions_failing", "processing_channel_switched_off"]
user_segment_ids: [11003606966930]
archive: false
---

## Process Steps

1. If the merchant is non compliant then the processing channel may be switched off after review by Risk. The merchant may not be aware that they have been suspended which is why they reach out to Care to find out why ‘all transactions are failing’ 

2. Go onto the Client Admin tool and check the status of the merchant. 

  1. If the merchant’s status is active then go back to the merchant and ask them further details e.g. Which error code is coming up, which channel’s transactions are failing.

  2. If the merchant’s status is ‘inactive’ this means they are terminated.

3. Check Datadog we can see if the processing channel has been switched off.

  1. Use the request ID on Datadog to see the error code for why the transaction is failing

4. Once the merchant responds with extra information for the transaction that is ‘Active’ on the above tools then;

  1. Go onto the ‘client admin tool’ and click on ‘Processing’. Select the channel and look at ‘authorisation’. If this is ‘disabled’ then this may mean that traffic was suspended. 

  2. Inform Merchant Config that all transactions are failing and explain that the ‘authorisation’ has been ‘disabled’. Next, request further information from Config as to why this has happened. E.g the traffic may be suspended due to non-compliance from the merchant. 

  3. Find out if this was already communicated to the merchant before going back to them.

  4. For Tiers 1-3 reach out to the CSM and request them to inform the merchant about the suspension (if the merchant is not already aware).

  5. If this is an ‘unmanaged (Tier 4)’ merchant;

    1. Care will inform the merchant about the suspension (if the merchant is not already aware).

## Glossaries and Definitions:

For **Key Terms and Definitions** on Transactions as well as an **introduction into MENA Gateway and non-Gateway merchants**, please see ****[Transactions Glossary](https://checkoutint.zendesk.com/hc/en-us/articles/21991201065106-Transactions-Glossary-Introduction)**.  **
 
 
 
 
 
 
 
 
 

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Transactions articles, please see ****[Transactions Tools & Permissions](https://checkoutint.zendesk.com/hc/en-us/articles/21991176883474-Transactions-Tools-Permissions)**.**
