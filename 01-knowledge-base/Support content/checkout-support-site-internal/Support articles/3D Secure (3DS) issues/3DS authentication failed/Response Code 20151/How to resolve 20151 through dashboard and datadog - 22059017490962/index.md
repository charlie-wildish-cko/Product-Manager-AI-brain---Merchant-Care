---
id: 22059017490962
section_id: 22057257485074
title: "How to resolve 20151 through dashboard and datadog"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22059017490962-How-to-resolve-20151-through-dashboard-and-datadog"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:39:58Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRP1QGWAFPTEP0CSMC1WBV"]
label_names: ["global", "case_3ds_issue_response_code_20151_-_20156", "case_3ds_issue_response_code_20151_-_20159", "case_3ds_issues", "response_code_20151", "how_to_resolve_20151_through_dashboard_and_datadog"]
user_segment_ids: [11003606966930]
archive: false
---

## Process Steps

1. Confirm with the merchant what the impacted decline response code is (if not known)

  1. The merchant needs to confirm that the impacted response code is RC20151

2. Take the Payment ID and check the 3DS status on [Dashboard](https://dashboard.checkout.com). The transaction must appear as Authentication failed

1. Identify the scheme type of the transaction under **Payment Method**

2. Scroll down on the same transaction details until you see the section **3DS Authentication**

1. From the 3DS authentication section, find the following:-

  1. Transaction Status

  2. Transaction Status reason

  3. Status Reason

  4. Protocol Version

2. Open [CKO docs here](https://www.checkout.com/docs/business-operations/use-the-dashboard/payment-activity/track-3ds-events) to view the meaning of the different transaction statuses and reason codes returned:-

  1. Transaction Status = N

  2. Transaction Status reason = 19

  3. Status Reason = ARES status

  4. Protocol Version = 2.1.0

3. Carry out an in-depth investigation using [Datadog](https://app.datadoghq.com/logs?query=%40PaymentId%3A%28pay_xsj37yvkfu2ezewtvphv74jx2a%29&agg_m=count&agg_m_source=base&agg_t=count&cols=service%2C%40http.status_code%2C%40PaymentAction&fromUser=true&index=processing&messageDisplay=inline&refresh_mode=sliding&saved-view-id=88535&storage=hot&stream_sort=time%2Cdesc&viz=stream&from_ts=1712658031337&to_ts=1715250031337&live=true), by copying the payment ID and pasting it into the search area:-

1. Look for the first **“POST”** API call for authorisation of the Gateway API service

1. Once you have identified this, open the logs, look for the **CorrelationID** then click on setting **Replace filter with CorrelationId**

  1. A new set of logs will be refreshed on your Datadog page

1. Open any log under **“Services”** called **“ThreeDS2.Sessions.Api”** and look for **“ThreeDS2.Sessions.Api”**

1. Add **SessionId** to the search bar by clicking on **add to filter**

  1. Please ensure you add OR between the Correlation and Session IDs

1. Now that you are in the session domain logs, look for the [service called ThreeDS2.Expirer](https://app.datadoghq.com/logs?query=%40Properties.CorrelationId%3A557ee8e7-2eef-918d-b834-9df0413f01ff%20OR%20%40Properties.SessionId%3A351d5c1f-ff8a-4fb5-9b0e-698a84d396c8&agg_m=count&agg_m_source=base&agg_t=count&cols=service%2C%40http.status_code%2C%40PaymentAction&event=AgAAAY9cl1g9EzoC_wAAAAAAAAAYAAAAAEFZOWNsMTY4QUFCNHF2dzcxZU5HRWdBQQAAACQAAAAAMDE4ZjVjYTItNWE3Yi00MTBiLThiZTctY2RhNDU2MDgyOTU0&fromUser=true&index=processing&messageDisplay=inline&refresh_mode=sliding&saved-view-id=88535&storage=hot&stream_sort=time%2Cdesc&viz=stream&from_ts=1712658031337&to_ts=1715250031337&live=true)

1. Find the last **ThreeSD2.Sessions.API** log and open the log

1. From the logs, scroll down to the response body and use CTRL+F to locate **response_code**

1. Inform the merchant of the following:

  1. After reviewing the logs, we noticed that the Issuer’s ACS response returned the following reason: N = Not Authenticated /Account Not Verified; Transaction denied, 19 = Exceeds ACS maximum challenges. Please request the cardholder to contact the issuing bank first before re-attempting any transaction

## Glossaries and Definitions:

For **Key Terms and Definitions** on 3DS, please see ****[3DS Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22059673420818-3DS-Glossary-Introduction)   

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the 3DS articles, please see ****[3DS Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22059810908306-3DS-Tools-Permissions)
