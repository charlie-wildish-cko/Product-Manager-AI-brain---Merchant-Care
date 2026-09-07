---
id: 22605393174546
section_id: 22604776982290
title: "404 Issue"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22605393174546-404-Issue"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:36:00Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRP1QGWAFPTEP0CSMC1WBV"]
label_names: ["global", "case_3ds_issues", "case_3ds_issue_page_not_loading", "404 issue"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

Issue—404 Interceptor issue—The page is not loading as the session has expired. This error generally occurs when the merchant attempts multiple GET requests.

## Process Steps

Tools needed

- Datadog

- Retool

**How to investigate this issue**

Check the session interceptor logs

1. Retrieve the correlation ID for the payment

2. Retrieve the Session ID for the payment

3. Open datadog

index:processing (@Properties.SessionResourceId:sid_qmedn7qvfv4ejjv2waylvcohze OR @CorrelationId:8d6532a4-1052-4c4b-912b-b1237be504c9) service:Sessions.Interceptor

Please see the DD logs [here<>](https://app.datadoghq.com/logs?query=%28%40Properties.SessionResourceId%3Asid_qmedn7qvfv4ejjv2waylvcohze%20OR%20%40CorrelationId%3A8d6532a4-1052-4c4b-912b-b1237be504c9%29%20service%3ASessions.Interceptor&agg_m=count&agg_m_source=base&agg_q=%40ActionName&agg_q_source=base&agg_t=count&analyticsOptions=%5B%22bars%22%2C%22dog_classic%22%2Cnull%2Cnull%5D&cols=service%2C%40http.status_code%2C%40ChargeId&event=AgAAAZF0WGou0HQJWAAAAAAAAAAYAAAAAEFaRjBXSEJEQUFCUVpHejVWbW1GT1FBTQAAACQAAAAAMDE5MTc0NjAtYWYzOS00MGVmLWJhOTYtZjI4YjU1NDI4ZmEx&fromUser=true&index=processing&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=time%2Cdesc&top_n=10&top_o=top&viz=stream&x_missing=true&from_ts=1660565359745&to_ts=1661861359745&live=true). If the error is 404, then it’s a merchant or possible device issue, as the session has expired.

**Resolution**

The payment would need to be attempted again in a new session as the previous payment session had expired. The cardholder has a 15-minute timeframe to complete authentication, or the payment will expire.

Additionally, this ticket could be escalated to L2 or possibly Gateway to provide further insight (if necessary).

Example ticket: [https://checkout1360.zendesk.com/agent/tickets/20129](https://checkout1360.zendesk.com/agent/tickets/20129)

Please see the resolution example email sent to the merchant below:

| _Hey Dina,_ _I hope you are well. Thank you for your patience._ _I've received an update from the engineering team, they have stated that the 404 has been returned by the interceptor when loading an authentication that exists because the request happened on an outdated session, effectively 15 minutes after its creation._ _If you have any further questions or require any further assistance, please don't hesitate to contact me._ _Many Thanks,_ _Rochan Trotman_ _Level 2 Merchant Care Support_ |
| --- |

## Glossaries and Definitions:

For **Key Terms and Definitions** on 3DS, please see ****[3DS Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22059673420818-3DS-Glossary-Introduction)   

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the 3DS articles, please see ****[3DS Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22059810908306-3DS-Tools-Permissions)
