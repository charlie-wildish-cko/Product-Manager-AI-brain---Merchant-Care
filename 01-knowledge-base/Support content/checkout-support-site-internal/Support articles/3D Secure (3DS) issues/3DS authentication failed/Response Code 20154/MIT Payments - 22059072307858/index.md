---
id: 22059072307858
section_id: 22057326312210
title: "MIT Payments"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22059072307858-MIT-Payments"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:37:34Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRP1QGWAFPTEP0CSMC1WBV"]
label_names: ["global", "response_code_20154", "case_3ds_issue_response_code_20151_-_20156", "case_3ds_issue_response_code_20151_-_20159", "mit_payments", "case_3ds_issues"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

The below article covers recurring MIT payments failing with 20154.  
 

## Process Steps

1. Open [Retool](https://retoolprod.mgmt.ckotech.co/apps/a04c8c20-72cf-11eb-bea4-e7bba7ba05e6/payment-performance-shared-debug/Traffic%20Insights#payment_id=), input the Payment ID into the **Give me an ID** field, and select **Query**. 

  1. Please see the example below in the screenshots of Payment ID pay_n2bdgdsrgijefiyqkyrqxom7qi 

1. When the data loads, check the tab on the right to see if the payment included the **Previous Charge Id**

1. Please see the example of a successful recurring payment type

1. inform the merchant of a soft decline because of previous charge ID is not included in recurring subscription transactions

  1. In the case of MIT, a 20154 soft decline usually means that there’s something wrong with request parameters. Either the flags are not correct or the initial payment referred to in the previous_payment_id is not a valid SCA authorisation

Please see this [ticket](https://checkout1360.zendesk.com/agent/tickets/5719) in Zendesk as an example of the issue above.

## Glossaries and Definitions:

For **Key Terms and Definitions** on 3DS, please see ****[3DS Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22059673420818-3DS-Glossary-Introduction)   

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the 3DS articles, please see ****[3DS Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22059810908306-3DS-Tools-Permissions)
