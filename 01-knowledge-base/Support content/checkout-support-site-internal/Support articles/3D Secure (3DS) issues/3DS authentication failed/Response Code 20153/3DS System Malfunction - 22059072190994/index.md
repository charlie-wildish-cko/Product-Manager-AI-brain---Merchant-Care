---
id: 22059072190994
section_id: 22057325140626
title: "3DS System Malfunction"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22059072190994-3DS-System-Malfunction"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:39:57Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRP1QGWAFPTEP0CSMC1WBV"]
label_names: ["global", "case_3ds_issue_response_code_20151_-_20156", "case_3ds_issue_response_code_20151_-_20159", "3ds_system_malfunction", "case_3ds_issues", "response_code_20153"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

The response code is related to a 3DS system malfunction: _‘The payment failed due to a technical issue or a technical malfunction’_’

## Process Steps

1. Ensure the merchant has sent the relevant information such as a payment ID, session ID, correlation ID, and action ID. When you have received the relevant information from the merchant, investigate this issue further to gain a better understanding of the root cause of the failure. 

2. Open [Retool](https://retoolprod.mgmt.ckotech.co/apps/a04c8c20-72cf-11eb-bea4-e7bba7ba05e6/payment-performance-shared-debug/Traffic%20Insights#payment_id=), input the Payment ID into the **Give me an ID** field, and select **Query**

  1. Please see the example below in the screenshots of Payment ID pay_hkup5h3y5d6efhmc4rrdqegzp4; select the event **AuthenticationUnavailable**

3. Check the response code and response reason in the log for the **AuthenticationUnavailable** event  
  

  

1. Raise the issue with the OC team to investigate if there was a possible outage

  1. Reason: the payment may have failed because the 3DS authenticator couldn’t be located. This issue is caused by a 3DS outage with the issuing bank or a system malfunction occurred

Please see this [ticket](https://checkout.lightning.force.com/lightning/r/Case/5000800004ayckfAAA/view?ws=%2Flightning%2Fr%2FEmailMessage%2F02s0800001epmcDAAQ%2Fview) on Salesforce as an example of the use case.

## Glossaries and Definitions:

For **Key Terms and Definitions** on 3DS, please see ****[3DS Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22059673420818-3DS-Glossary-Introduction)   For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the 3DS articles, please see ****[3DS Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22059810908306-3DS-Tools-Permissions)
