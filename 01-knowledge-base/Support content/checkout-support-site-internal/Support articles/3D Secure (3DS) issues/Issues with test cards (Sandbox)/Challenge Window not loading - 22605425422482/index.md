---
id: 22605425422482
section_id: 22604832741650
title: "Challenge Window not loading"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22605425422482-Challenge-Window-not-loading"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:35:57Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRP1QGWAFPTEP0CSMC1WBV"]
label_names: ["global", "case_3ds_issues", "case_3ds_issue_issues_with_test_cards_sandbox", "challenge_window_not_loading"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

Issue: The 3DS panel does not appear when processing within Sandbox and the result is not showing in the dashboard

## Process Steps

1. Firstly, obtain the payment ID&

2. Input the payment ID into the [Retool](https://retoolprod.mgmt.ckotech.co/apps/a04c8c20-72cf-11eb-bea4-e7bba7ba05e6/payment-performance-shared-debug/Traffic%20Insights#payment_id=)

3. Select and check the event "3ds.authenticated" logs

4. Check the flow type would help to determine if the merchant would like to challenge the cardholder or if they prefer to process payments (e.g. for payment ID **pay_wehgmxr6whoerbrbpsrvyvippq **used the flow type frictionless). Please see the screenshot below:

5. 
For payment ID, **pay_wewwcojvhusezoyrdghnlwtqum**, this payment used the challenged flow type (please see the screenshot below):

**Resolution**There are two different ways to process authentication. This would be using frictionless and the challenged payment flow. The first transaction used the frictionless payment flow, however on the second attempt the payment had used the challenged payment flow and this was reflected on Dashboard.Please see this [ticket](https://checkout1360.zendesk.com/agent/tickets/28991) as an example.

## Glossaries and Definitions:

For **Key Terms and Definitions** on 3DS, please see ****[3DS Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22059673420818-3DS-Glossary-Introduction)   For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the 3DS articles, please see ****[3DS Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22059810908306-3DS-Tools-Permissions)
