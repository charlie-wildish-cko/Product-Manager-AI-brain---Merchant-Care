---
id: 22605392914450
section_id: 22604736721426
title: "Investigating a Performance Drop"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22605392914450-Investigating-a-Performance-Drop"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-31T16:51:20Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRPB6VB7BVTRFPB2N2PA9E"]
label_names: ["global", "overall_performance_drop", "case_acceptance_performance_low_approval_rate", "case_acceptance_performance", "low_acceptance_rate", "acceptance_rate_performance_issue"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

We receive requests from Merchants after they notice a drop in their acceptance rate performance or an ongoing issue with a specific issuer bank, scheme or region. The request can reach Merchant Care on the same day or a few days after the drop in performance occurred. 

## Process Steps

### Using Looker

We can receive requests from merchants mentioning that they noted a drop in their overall performance but cannot identify the source.

The flow below will help identify two important pieces of information: the date range or start date, if the issue is still ongoing, and at which level.

The graph shows each entity's daily acceptance rate for a given period. This report can be updated according to the merchant account structure.

[Looker Link](https://checkoutinternal.eu.looker.com/explore/payment_lifecycle/fct_payin?toggle=fil,vis&qid=Gj9uqNLfvvisqO7ePf597F)

The recording below shows how to update the looker report to make a quick analysis of the acceptance rate and update the report to refine the result.

Acceptance rate analysis

[https://checkout.zoom.us/rec/play/i-SxI0csyXRNzbinAI-Ozn8RpvkWiFWjpFHvxcojUKxaKu02tNtGLyp6zyCUZ3xY2GhNcHxRKC0HoJBr.h1aBSNIqqYD8F_sN](https://checkout.zoom.us/rec/play/i-SxI0csyXRNzbinAI-Ozn8RpvkWiFWjpFHvxcojUKxaKu02tNtGLyp6zyCUZ3xY2GhNcHxRKC0HoJBr.h1aBSNIqqYD8F_sN)

Passcode: WL=0Aw49

### Using Datadog

In some cases, the impacted timeframe is quite recent and the data is yet to be updated on Looker. You can use Datadog to determine if there is a drop in approved transactions. 

The [Datadog graph](https://app.datadoghq.com/logs?query=service%3A%28%22Gateway%20API%22%20OR%20Merchant.Api%29%20%40MerchantId%3A%2A%20%40Properties.CkoClientId%3Acli_u7wxnwvsmqyupia3x77hf42bqe%20%40GatewayResponseCode%3A%28%2A%29%20%40Properties.Response.Source.Bin%3A%2A%20%40PaymentAction%3Aauthorization%20%40Properties.AcquirerId%3A%2A%20%40Properties.Response.Source.Scheme%3A%2A%20-%40http.status_code%3A%3E499%20env%3A%28production%20OR%20prod%29&agg_m=count&agg_m_source=base&agg_q=%40GatewayResponseCode&agg_q_source=base&agg_t=count&analyticsOptions=%5B%22line%22%2C%22dog_classic%22%2C%22solid%22%2C%22normal%22%2C%22value%22%2C%22tags%22%2Cfalse%5D&cols=service%2C%40account.account_name%2C%40PaymentId%2C%40MerchantName%2C%40Properties.AcquirerId%2C%40Properties.NetworkTokenType%2C%40GatewayResponseCode%2C%40Properties.CkoClientId%2C%40EntityId%2C%40MerchantId%2C%40Properties.ProcessorId%2C%40Properties.Response.Source.CardWalletType%2C%40Properties.Response.Source.Issuer%2C%40Properties.Response.Source.Bin%2C%40Properties.Response.Source.Scheme%2C%40Properties.Response.Source.SchemeLocal%2C%40PaymentAction&fromUser=true&messageDisplay=inline&refresh_mode=paused&storage=hot&stream_sort=time%2Cdesc&top_n=10&top_o=top&viz=timeseries&x_missing=true&from_ts=1730538000000&to_ts=1730548800000&live=false) below shows the number of transactions based on the response codes for a specific Client ID. Hovering over a response code will highlight the same on the graph.

Once you have identified the impacted timeframe, update the date and time range. You can also exclude successful attempts to focus on declines. 

Click on ‘Top List’ to display the number of transactions per response code for the selected timeframe.

You can then filter with this specific response code for more accurate data and identify any spikes if required.

 

You can group by any attribute, such as the Merchant ID for the Processing channel ID, to identify where is the biggest impact.

If the issue is affecting all schemes under a specific processing channel or entity, we need to investigate further with internal stakeholders for recent changes that may affect the approval rate such as Configuration changes (**#merchant_configuration-merchant_care** Slack channel), schemes or country policy amendments (**#merchant-communications** Slack channel or [Highspot](https://checkout.highspot.com/)).

If the issue is affecting or has affected a specific scheme and no root cause has been identified, you may make a request to the [OC team](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277) to investigate further. A request should be raised with the Performance Team (**#ask-performance** Slack channel) and inform the AM/TAM where applicable after the OC team confirm the issue is specific to the merchant.

## Glossaries and Definitions:

For **Key Terms and Definitions** on Acceptance Rate Issues, please see ****[Acceptance Rate Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22605423721874-Acceptance-Rate-Glossary-Introduction) 

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Acceptance Rate articles, please see ****[Acceptance Rate Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22605407475858-Acceptance-Rate-Tools-Permissions)
