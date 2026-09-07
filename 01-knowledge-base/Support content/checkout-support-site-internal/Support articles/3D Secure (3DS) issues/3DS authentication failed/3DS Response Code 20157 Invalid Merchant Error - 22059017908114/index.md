---
id: 22059017908114
section_id: 22057285830034
title: "3DS Response Code 20157: Invalid Merchant Error"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22059017908114-3DS-Response-Code-20157-Invalid-Merchant-Error"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:34:10Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRP1QGWAFPTEP0CSMC1WBV"]
label_names: ["global", "case_3ds_issue_response_code_20151_-_20156", "case_3ds_issue_response_code_20151_-_20159", "case_3ds_issues", "response_code_20157"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

This article covers invalid merchant errors; this would need to be handled by merchant configuration to ensure the merchant is set correctly.

## Process Steps

1. Open [Retool](https://retoolprod.mgmt.ckotech.co/apps/a04c8c20-72cf-11eb-bea4-e7bba7ba05e6/payment-performance-shared-debug/Traffic%20Insights#payment_id=), input the Payment ID into the **Give me an ID** field, and select **Query**

  1. The below screenshot shows an example with Payment ID pay_vc2ovc5uadjuloduypqsoawtta

1. Under the **Event type**, select the **ChargeDeclined** event, and locate ResponseDetails and ResponseSummary to identify the “**invalid Merchant Configurations - Contact support**” error response code

1. Escalate to the Merchant Configuration team to resolve this issue, by using the relevant macro on Zendesk

Please see this [ticket](https://checkout.lightning.force.com/lightning/r/Case/5000800005BbLevAAF/view) on Salesforce as an example of the issue above.

## Glossaries and Definitions:

For **Key Terms and Definitions** on 3DS, please see ****[3DS Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22059673420818-3DS-Glossary-Introduction)   

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the 3DS articles, please see ****[3DS Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22059810908306-3DS-Tools-Permissions)
