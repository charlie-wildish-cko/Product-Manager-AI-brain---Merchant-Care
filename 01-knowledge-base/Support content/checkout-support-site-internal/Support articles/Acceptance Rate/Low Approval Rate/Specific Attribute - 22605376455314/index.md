---
id: 22605376455314
section_id: 22604736721426
title: "Specific Attribute"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22605376455314-Specific-Attribute"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:36:00Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRPB6VB7BVTRFPB2N2PA9E"]
label_names: ["global", "specific_attribute", "case_acceptance_performance_low_approval_rate", "case_acceptance_performance", "low_acceptance_rate", "acceptance_rate_performance_issue"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

We receive requests from Merchants after they notice a drop in their acceptance rate performance or an ongoing issue with a specific issuer bank, scheme or region. The request can reach Merchant Care on the same day or a few days after the drop in performance occurred. 

## Process Steps

### Using Looker

The investigation following an overall performance drop can lead to identifying a specific attribute being the root cause such as a card bin, issuer bank, region or even transaction type. Some merchants can also flag these attributes in their initial requests.

The flow below will help to investigate based on these specific attributes.

The graph below shows the performance of a BIN for a given period to identify the drops in performance. This report can be filtered with the merchant's information.

[Looker link](https://checkoutinternal.eu.looker.com/explore/payment_lifecycle/fct_payin?toggle=fil,vis&qid=UBoOZ6IBfYh9O83fYrIAqG)

You can add another attribute to the fields and pivot to have better understanding of the impacted transactions. For example, the ‘Transaction Type’ was added to compare the performance of recurring and regular transactions. The graph indicates that the drop affects recurring transactions.

[Looker Link](https://checkoutinternal.eu.looker.com/explore/payment_lifecycle/fct_payin?toggle=fil,vis&qid=oPPcWLOwi26VC7EiLYZTdu)

In the fields, you can also replace the acceptance rate with Requested Payments (#), Authenticated Payments (#), Non-Authentication Payments (#) and Authorised Payments (#) to identify if the issue is related to authentication or authorisation. 

As shown in the graph below, the authorisation dropped with the authenticated transactions while the number of authentication attempts and non-authentication attempts follows the same trend. We can conclude that the authentication drop is affecting the authorisation success rate. If the authorisation drops despite having a normal authentication success rate, the investigation will focus more on the authorisation failed attempts.

[Looker link](https://checkoutinternal.eu.looker.com/explore/payment_lifecycle/fct_payin?toggle=vis&qid=32SZSqQhi42n8DSaDHZCGp)

The graph below shows the response code trend over a given period to identify any unusual increase or decrease in response code. From this point, you can change the filters and fields that will help identify the impacted attribute.

[Looker Link](https://checkoutinternal.eu.looker.com/explore/payment_lifecycle/fct_payin?toggle=vis&qid=pUW1qfeqyIdK6bTihmWL9y)

The video below shows how to switch the trend analysis from response code to issuer bank analysis for a specific response code.

Attribute trend analysis

[https://checkout.zoom.us/rec/share/t0UG03JUd0B6g3wU6YFJd2SpRR3uGWT4QskSY0RZkom-xq5PUb__Y3hdQGG5BpTO.Egjvh-N-wHzMsJkK?startTime=1727090753000](https://checkout.zoom.us/rec/share/t0UG03JUd0B6g3wU6YFJd2SpRR3uGWT4QskSY0RZkom-xq5PUb__Y3hdQGG5BpTO.Egjvh-N-wHzMsJkK?startTime=1727090753000)

Passcode: %p%1R$C1

### Using Datadog

The graph below shows the issuer banks with the highest number of declines with a specific response.

[DD link](https://app.datadoghq.com/logs?query=service%3A%28%22Gateway%20API%22%20OR%20Merchant.Api%29%20%40MerchantId%3A%2A%20%40Properties.CkoClientId%3A%2A%20%40GatewayResponseCode%3A20091%20%40Properties.Response.Source.Bin%3A%2A%20%40PaymentAction%3Aauthorization%20%40Properties.AcquirerId%3A%2A%20%40Properties.Response.Source.Scheme%3A%2A%20%40Properties.Response.Source.Issuer%3A%2A%20env%3A%28prod%20OR%20production%29&agg_m=count&agg_m_source=base&agg_q=%40Properties.Response.Source.Issuer&agg_q_source=base&agg_t=count&analyticsOptions=%5B%22line%22%2C%22dog_classic%22%2Cnull%2Cnull%2C%22value%22%5D&cols=service%2C%40account.account_name%2C%40PaymentId%2C%40MerchantName%2C%40Properties.AcquirerId%2C%40Properties.NetworkTokenType%2C%40GatewayResponseCode%2C%40Properties.CkoClientId%2C%40EntityId%2C%40MerchantId%2C%40Properties.ProcessorId%2C%40Properties.Response.Source.CardWalletType%2C%40Properties.Response.Source.Issuer%2C%40Properties.Response.Source.Bin%2C%40Properties.Response.Source.Scheme%2C%40Properties.Response.Source.SchemeLocal%2C%40PaymentAction&fromUser=true&messageDisplay=inline&refresh_mode=paused&storage=hot&stream_sort=time%2Cdesc&top_n=10&top_o=top&viz=toplist&x_missing=true&from_ts=1730719380000&to_ts=1730732940000&live=false)

The highlighted section below contains the attributes being displayed and can be updated with the attributes from the search section.

This [Datadog link](https://app.datadoghq.com/logs?query=service%3A%28%22Gateway%20API%22%20OR%20Merchant.Api%29%20%40MerchantId%3A%2A%20%40Properties.CkoClientId%3A%2A%20%40GatewayResponseCode%3A%2A%20%40Properties.Response.Source.Bin%3A%2A%20%40PaymentAction%3Aauthorization%20%40Properties.AcquirerId%3A%2A%20%40Properties.Response.Source.Scheme%3A%2A%20%40Properties.Response.Source.Issuer%3A%2A%20env%3A%28prod%20OR%20production%29&agg_m=count&agg_m_source=base&agg_q=%40Properties.Response.Source.Issuer&agg_q_source=base&agg_t=count&analyticsOptions=%5B%22line%22%2C%22dog_classic%22%2Cnull%2Cnull%2C%22value%22%5D&cols=service%2C%40account.account_name%2C%40PaymentId%2C%40MerchantName%2C%40Properties.AcquirerId%2C%40Properties.NetworkTokenType%2C%40GatewayResponseCode%2C%40Properties.CkoClientId%2C%40EntityId%2C%40MerchantId%2C%40Properties.ProcessorId%2C%40Properties.Response.Source.CardWalletType%2C%40Properties.Response.Source.Issuer%2C%40Properties.Response.Source.Bin%2C%40Properties.Response.Source.Scheme%2C%40Properties.Response.Source.SchemeLocal%2C%40PaymentAction&fromUser=true&messageDisplay=inline&refresh_mode=paused&storage=hot&stream_sort=time%2Cdesc&top_n=10&top_o=top&viz=stream&x_missing=true&from_ts=1730719380000&to_ts=1730732940000&live=false) can be used as a template and the recording below shows how to update the fields based on the information provided. The recording also includes how to visualise the data using a graph.

[https://checkout.zoom.us/rec/share/CdmC3J7mbkS5F2Vg7R-7-wbcIQJef6tQsDytTIS5NMqEZiH6bWgg-TF4Y70wM8RX.IfC06EcA1vicFog5?startTime=1731032609000](https://checkout.zoom.us/rec/share/CdmC3J7mbkS5F2Vg7R-7-wbcIQJef6tQsDytTIS5NMqEZiH6bWgg-TF4Y70wM8RX.IfC06EcA1vicFog5?startTime=1731032609000)

Passcode: ?ZwZ6x94

If you have identified any specific attribute being impacted, reach out to OC team (**#support_oc** Slack channel) to investigate on a potential incident. If the OC Team confirm the issue impacts the specific merchant and the root cause is not issuer related or the merchant is using _Intelligence acceptance_, contact the Performance Team (**#ask_performance** Slack channel). Where the performance drop is issuer related, inform the TAM/AM to contact the issuer outreach team or raise directly with the IO Team (Catalogue form [46](https://checkout.atlassian.net/jira/core/projects/IO/form/46)) if the merchant is unmanaged. The information required to raise the request is available in the form.

## Glossaries and Definitions:

For **Key Terms and Definitions** on Acceptance Rate Issues, please see ****[Acceptance Rate Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22605423721874-Acceptance-Rate-Glossary-Introduction) 

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Acceptance Rate articles, please see ****[Acceptance Rate Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22605407475858-Acceptance-Rate-Tools-Permissions)
