---
id: 22605376677906
section_id: 22604776982290
title: "3DS not loading as payment stuck in authorisation"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22605376677906-3DS-not-loading-as-payment-stuck-in-authorisation"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:35:59Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRP1QGWAFPTEP0CSMC1WBV"]
label_names: ["global", "case_3ds_issues", "case_3ds_issue_page_not_loading", "3ds_not_loading_as_payment_stuck_in_authorization", "3ds_not_loading_as_payment_stuck_in_authorisation"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

Issue: Payment failed as 3DS not loading on IOS.

## Process Steps

**Example issue**  
The customer on IOS goes into their Banking App and authorises the payment. The customer returns to our app and it gets stuck on loading as if it's still waiting for a response and subsequently times out.

**How to investigate this issue**

1. Open [Retool](https://retoolprod.mgmt.ckotech.co/apps/a04c8c20-72cf-11eb-bea4-e7bba7ba05e6/payment-performance-shared-debug/Traffic%20Insights#payment_id=)

2. In the "Give me an ID" box, input the Payment ID (e.g. Pay_mbqsxw543ccktdbaqi6qbgf4t4)

3. Select the "AuthenticationDeclined" event to retrieve the logs for the failed payment (see the screenshot below):

4. In the logs, check the response details (in the screenshot below it shows the payment had failed with ACS ‘14’ timed-out error):  
  
  
 

**Resolution**The root cause of the payment failure was because of an ACS timeout issue, which had caused the payments to get stuck. To resolve this issue, the merchant would need to retry the payment to check and resolve this issue.However, if this issue isn’t resolved with a retry, then this issue would need to be escalated to Level 2 Merchant Care for further assistance.Please see the example ticket [here](https://checkout.lightning.force.com/lightning/r/Case/5000800004rforiAAA/view).

## Glossaries and Definitions:

For **Key Terms and Definitions** on 3DS, please see ****[3DS Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22059673420818-3DS-Glossary-Introduction)   For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the 3DS articles, please see ****[3DS Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22059810908306-3DS-Tools-Permissions)
