---
id: 22059017683346
section_id: 22057326312210
title: "20154 response (3D Secure authentication required)"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22059017683346-20154-response-3D-Secure-authentication-required"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:37:34Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRP1QGWAFPTEP0CSMC1WBV"]
label_names: ["global", "response_code_20154", "20154_response_3ds_authentication_required", "case_3ds_issue_response_code_20151_-_20156", "case_3ds_issue_response_code_20151_-_20159", "case_3ds_issues"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

Mastercard returns a 20065 response code after the merchant receives a 20154 (3D Secure authentication required) from payment requests.

## Process Steps

1. Open [Retool](https://retoolprod.mgmt.ckotech.co/apps/a04c8c20-72cf-11eb-bea4-e7bba7ba05e6/payment-performance-shared-debug/Traffic%20Insights#payment_id=), input the Payment ID into the **Give me an ID** field, and select **Query**

  1. Please see the example below in the screenshots of Payment ID pay_laje2npm4pfetgpj3alhgrlyqi 

****

1. 
Under the **Event type**, select the **ChargeDeclined** event and check the response code is ‘65’ in the log
  
 

2. The payment failure can occur with a 20152 or a 20154 if there is an issue with an ACS outage, which is caused by the issuing bank. The issuing bank has aligned the failure with the Mastercard scheme, which maps the 65 response code with the 20154 (3D Secure authentication required) response code. Therefore, inform the merchant to inform the cardholder to contact their issuing bank or reattempt the payment, if there are no further possible ACS outages

**Note**: As this is mapped by Mastercard we cannot change how the message is received. Further explanation is available within this [confluence article](https://checkout.atlassian.net/wiki/spaces/CAC/pages/2047805284/SCA+Exemptions). Please see this Zendesk [ticket](https://checkout1360.zendesk.com/agent/tickets/9540) as an example of this issue.

## Glossaries and Definitions:

For **Key Terms and Definitions** on 3DS, please see ****[3DS Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22059673420818-3DS-Glossary-Introduction)   For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the 3DS articles, please see ****[3DS Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22059810908306-3DS-Tools-Permissions)
