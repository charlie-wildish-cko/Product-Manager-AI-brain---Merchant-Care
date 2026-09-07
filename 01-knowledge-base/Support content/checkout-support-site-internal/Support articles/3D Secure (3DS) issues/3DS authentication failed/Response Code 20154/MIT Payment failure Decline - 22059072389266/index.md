---
id: 22059072389266
section_id: 22057326312210
title: "MIT Payment failure Decline"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22059072389266-MIT-Payment-failure-Decline"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:37:34Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRP1QGWAFPTEP0CSMC1WBV"]
label_names: ["global", "response_code_20154", "case_3ds_issue_response_code_20151_-_20156", "case_3ds_issue_response_code_20151_-_20159", "mit_payment_failure_decline", "case_3ds_issues"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

This article ensures the payment request adheres to SCA requirements and leverages the previous successful authentication for subsequent payments. To investigate this issue, compare the previous successful payment with the failed payment.

## Process Steps

1. Open [Retool](https://retoolprod.mgmt.ckotech.co/apps/a04c8c20-72cf-11eb-bea4-e7bba7ba05e6/payment-performance-shared-debug/Traffic%20Insights#payment_id=), input the Payment ID into the **Give me an ID** field, and select **Query**

  1. Please see the example below in the screenshots of Payment ID pay_s3zgbnltudfuhko23tuklly4eu 

1. Under the **Event type**, select the **ChargeRequested** event and check the email address for the customer and that the email address is an auto-generated CKO email address:

1. Secondly, check the previous successful payment, by selecting the **PreAuthenticationRiskAssessed** event:

1. Check the email address of the previous successful payment, which used the customer's email address:

  
With the above example, we investigated the failed MIT and received the [recommendation code](https://www.checkout.com/docs/developer-resources/codes/recommendation-codes) **01 'Updated or additional information required'**. We compared the failed attempt to the successful one and the only difference we identified was that the email addresses sent differed as Checkout generated them. However, we can't confirm if the issuer declined the transaction for that reason. On the issuer side, there can be rules being triggered and declining transactions despite sending the previous payment ID.

1. Recommend the cardholder liaise with the issuer bank by providing the transaction details and asking what field(s) has triggered the response

Please see this [ticket](https://checkout1360.zendesk.com/agent/tickets/24916) in Zendesk as an example of the issue above. Also here are examples of [successful](https://retoolprod.mgmt.ckotech.co/apps/a04c8c20-72cf-11eb-bea4-e7bba7ba05e6/payment-performance-shared-debug/Traffic%20Insights#payment_id=pay_e67yfmdk5m5ujoelopd2pt7okq) and [failed](https://retoolprod.mgmt.ckotech.co/apps/a04c8c20-72cf-11eb-bea4-e7bba7ba05e6/payment-performance-shared-debug/Traffic%20Insights#payment_id=pay_s3zgbnltudfuhko23tuklly4eu) payment logs. Additionally, here is a Checkout doc regarding [recurring payments with stored card details](https://www.checkout.com/docs/payments/accept-payments/pay-with-stored-card-details/recurring-payments-with-stored-card-details).

## Glossaries and Definitions:

For **Key Terms and Definitions** on 3DS, please see ****[3DS Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22059673420818-3DS-Glossary-Introduction)   

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the 3DS articles, please see ****[3DS Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22059810908306-3DS-Tools-Permissions)
