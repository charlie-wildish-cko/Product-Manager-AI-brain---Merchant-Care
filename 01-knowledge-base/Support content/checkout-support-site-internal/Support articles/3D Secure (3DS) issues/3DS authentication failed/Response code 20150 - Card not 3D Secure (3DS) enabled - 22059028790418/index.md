---
id: 22059028790418
section_id: 22057285830034
title: "Response code 20150 - Card not 3D Secure (3DS) enabled"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22059028790418-Response-code-20150-Card-not-3D-Secure-3DS-enabled"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:37:34Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRP1QGWAFPTEP0CSMC1WBV"]
label_names: ["global", "case_3ds_issue_response_code_20151_-_20156", "case_3ds_issue_response_code_20151_-_20159", "case_3ds_issues", "response_code_20150_card_not_3ds_enabled"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

This response code is received when a card used for a transaction fails validation for 3DS support. In 3DS2, if the card does not support 3DS2, the Card Ranges API will return “0” ranges. In simple terms, the payment failed because the authentication had not been enabled for 3DS or the card was not registered to be processed for 3DS. The below screenshots are examples of payment ID **pay_kme7tl6uao727eywjijzg7bkke** using the Mastercard Scheme, where the payment had failed with a 20150.

## Process Steps

1. Open [Retool](https://retoolprod.mgmt.ckotech.co/apps/a04c8c20-72cf-11eb-bea4-e7bba7ba05e6/payment-performance-shared-debug/Traffic%20Insights#payment_id=)

2. Enter the Payment ID in the “Give me an ID” field, and select **Query** to see the Payment ID events

1. Please select the **ChargeAuthenticationRejected** event

1. Paste the **CorrelationID** into [Datadog](https://app.datadoghq.com/logs?query=%40CorrelationId%3A%2816b6ee7c-fd1d-4a31-8e3a-1bc296209fbe%29&agg_m=count&agg_m_source=base&agg_t=count&cols=service%2C%40http.status_code%2C%40PaymentAction&fromUser=true&index=processing&messageDisplay=inline&refresh_mode=sliding&saved-view-id=88535&storage=hot&stream_sort=time%2Cdesc&viz=stream&from_ts=1712658031337&to_ts=1715250031337&live=true) and search for the_ ThreeDs2.Session.API_ in the logs.

2. Under the _ThreeDs2.Sessions.API_, view the status code and response from the scheme

  1. A status code of **403: forbidden** indicates that the 3DS authentication was blocked

1. In the _ThreeDS2.CardRanges.API, _look at the range returned.

  1. A result of “0” indicates that the card does not support 3DS

Cardholders must contact the issuing bank to ensure they are enabled to process authentication i.e. the card setup may need to be corrected.

## Glossaries and Definitions:

For **Key Terms and Definitions** on 3DS, please see ****[3DS Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22059673420818-3DS-Glossary-Introduction)   

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the 3DS articles, please see ****[3DS Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22059810908306-3DS-Tools-Permissions)
