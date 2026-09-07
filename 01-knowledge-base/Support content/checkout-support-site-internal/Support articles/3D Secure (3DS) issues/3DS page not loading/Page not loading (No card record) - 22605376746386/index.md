---
id: 22605376746386
section_id: 22604776982290
title: "Page not loading (No card record)"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22605376746386-Page-not-loading-No-card-record"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:35:59Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRP1QGWAFPTEP0CSMC1WBV"]
label_names: ["global", "case_3ds_issues", "case_3ds_issue_page_not_loading", "page_not_loading_no_card_record"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

**Issue Example: **A customer from Colombia is trying to make this purchase, but somewhere in the 3DS process the page stops loading. This is the full [link](https://www.usimmigrationsupport.net/failure/?cko-session-id=sid_7r4b3lqfigkejf34slz7oa4wnu).

## Process Steps

1. Open [Retool](https://retoolprod.mgmt.ckotech.co/apps/a04c8c20-72cf-11eb-bea4-e7bba7ba05e6/payment-performance-shared-debug/Traffic%20Insights#payment_id=)

2. In the "Give me an ID" box, input the payment ID (e.g. pay_fh76t2ts6qne3fkni3rvswsouy) and hit "Query"

3. When the results have been populated, please navigate to the authentication tab and check the information regarding the payment ID (see the screenshot below, which highlights the no-card record issue)

 

**Resolution**

The user didn’t fill in any card details, which caused the transaction to fail. Also, check that the cardholder is enabled to process these transactions. The cardholder would need to contact their issuing bank if this issue persists.

Please see the ticket example [here](https://checkout1360.zendesk.com/agent/tickets/14234).

## Glossaries and Definitions:

For **Key Terms and Definitions** on 3DS, please see ****[3DS Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22059673420818-3DS-Glossary-Introduction)   

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the 3DS articles, please see ****[3DS Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22059810908306-3DS-Tools-Permissions)
