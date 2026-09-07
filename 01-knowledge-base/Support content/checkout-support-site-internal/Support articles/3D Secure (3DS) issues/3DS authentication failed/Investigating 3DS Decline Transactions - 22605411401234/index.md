---
id: 22605411401234
section_id: 22057285830034
title: "Investigating 3DS Decline Transactions"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22605411401234-Investigating-3DS-Decline-Transactions"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:34:11Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRP1QGWAFPTEP0CSMC1WBV"]
label_names: ["global", "case_3ds_issues", "faq_for_authentication", "faqs"]
user_segment_ids: [11003606966930]
archive: false
---

## Process Steps

### **Investigating 3DS Decline Transactions**

**Access Authentication Tab**

To investigate a 3DS decline, follow these steps:

1. 
**Access the Authentication Tab:** Begin by navigating to the Authentication tab on retool

2. 
**Check Decoded Indicators:** Review the decoded indicators to get an overview of the potential reason for the decline. These indicators will provide insights into why the 3DS authentication failed

  
 

### **Investigating the Increase of a Specific 3DS Response Code**

**Check Overall Gateway Response Code**

- 
**Tool Required:** Datadog Dashboard - [OC 3DS Dashboard](https://app.datadoghq.com/dashboard/tc5-w9f-28q/oc-3ds-dashboard?fromUser=false&refresh_mode=sliding&from_ts=1720957593385&to_ts=1723549593385&live=true)

- 
**Action:** Check the overall Gateway response code for the merchant for the past two weeks to identify any trends or spikes

- 
**DD Link:** Overall Gateway Response Code - [here](https://app.datadoghq.com/logs?query=service%3A%22Gateway%20API%22%20%40Properties.CkoClientId%3Acli_nilibeucitcu5c7ql3mnzxqoqm&agg_m=count&agg_m_source=base&agg_q=%40GatewayResponseCode&agg_q_source=base&agg_t=count&cols=host%2Cservice&fromUser=true&index=processing&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=desc&top_n=10&top_o=top&viz=sunburst&x_missing=true&from_ts=1626016547911&to_ts=1628608547911&live=true)

 

### **Analyse Failures Related to Authentication**

- 
**Action:** Examine the number of failures related to authentication. Look for any spikes or anomalies in the data, as these can indicate underlying issues

- 
**DD Link:** Authentication Failures - [here](https://app.datadoghq.com/logs?query=source%3Aauthentication%20env%3Aprod%2A%20service%3AThreeDS2.Sessions.Api%20%40Properties.ClientId%3Acli_nilibeucitcu5c7ql3mnzxqoqm%20-%40Properties.Status%3A%28pending%20OR%20challenged%20OR%20approved%29%20&agg_m=count&agg_m_source=base&agg_q=%40Properties.Status&agg_q_source=base&agg_t=count&analyticsOptions=%5B%22bars%22%2C%22dog_classic%22%2Cnull%2Cnull%5D&cols=service%2C%40Properties.Action%2C%40Properties.MerchantName%2C%40Properties.ClientId%2C%40Properties.IsMbc%2C%40Properties.MerchantAccountId%2C%40Properties.AcquirerMerchantId%2C%40Properties.AcquirerName%2C%40Properties.Status%2C%40Properties.StatusReason%2C%40Properties.NewStatus%2C%40http.method%2C%40http.status_code%2C%40Properties.Scheme%2C%40Properties.IssuerBin%2C%40Properties.IssuerName%2C%40Properties.IssuerCountry%2C%40Properties.ProtocolVersion%2C%40Elapsed%2C%40Properties.ThreeDsMethodUrl%2C%40Properties.AcsInfo.Url%2C%40Properties.ProcessingChannelId%2C%40Properties.ProcessorId&fromUser=true&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=time%2Cdesc&top_n=10&top_o=top&view=spans&viz=timeseries&x_missing=true&from_ts=1713772255925&to_ts=1715068255925&live=true)

- 
**Analysis:** For example, if you observe a spike in expired transactions on a specific date (e.g., Saturday, 27 April 2024), investigate further

### **Investigate the Number of incoming 3DS Requests**

- 
**Action:** Review the number of 3DS requests for the merchant to determine if there is a correlation between increased transaction volume and the number of declines

- 
**DD Link:** Number of 3DS Requests - [here](https://app.datadoghq.com/dashboard/tc5-w9f-28q/oc-3ds-dashboard?fromUser=true&fullscreen_end_ts=1715074799782&fullscreen_paused=false&fullscreen_refresh_mode=sliding&fullscreen_section=overview&fullscreen_start_ts=1712482799782&fullscreen_widget=7376075273796626&refresh_mode=sliding&tpl_var_GWC_Client_ID%5B0%5D=cli_nilibeucitcu5c7ql3mnzxqoqm&view=spans&from_ts=1712482778901&to_ts=1715074778901&live=true)

 

### **Breakdown of Failed Transactions by Issuing Bank**

- 
**Action:** Analyse the breakdown of failed transactions by issuing banks to identify if any specific banks are contributing to the increase in declines

- 
**DD Link:** Failed Transactions by Issuing Bank - [here](https://app.datadoghq.com/logs?query=source%3Aauthentication%20env%3Aprod%2A%20service%3AThreeDS2.Sessions.Api%20%40Properties.ClientId%3Acli_nilibeucitcu5c7ql3mnzxqoqm%20%40Properties.Status%3Adeclined%20&agg_m=count&agg_m_source=base&agg_q=%40Properties.IssuerName&agg_q_source=base&agg_t=count&analyticsOptions=%5B%22bars%22%2C%22dog_classic%22%2Cnull%2Cnull%5D&cols=service%2C%40Properties.Action%2C%40Properties.MerchantName%2C%40Properties.ClientId%2C%40Properties.IsMbc%2C%40Properties.MerchantAccountId%2C%40Properties.AcquirerMerchantId%2C%40Properties.AcquirerName%2C%40Properties.Status%2C%40Properties.StatusReason%2C%40Properties.NewStatus%2C%40http.method%2C%40http.status_code%2C%40Properties.Scheme%2C%40Properties.IssuerBin%2C%40Properties.IssuerName%2C%40Properties.IssuerCountry%2C%40Properties.ProtocolVersion%2C%40Elapsed%2C%40Properties.ThreeDsMethodUrl%2C%40Properties.AcsInfo.Url%2C%40Properties.ProcessingChannelId%2C%40Properties.ProcessorId&fromUser=true&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=time%2Cdesc&top_n=10&top_o=top&view=spans&viz=timeseries&x_missing=true&from_ts=1712483415731&to_ts=1715075415731&live=true)

### **Filter by Issuer**

Since most transactions are processed through the Issuer Al Rajhi, filter the data to show only transactions processed by this issuer. This will help narrow down the issue to specific transactions.

- 
**Link:** Filter by Issuer - [here](https://app.datadoghq.com/logs?query=source%3Aauthentication%20env%3Aprod%2A%20service%3AThreeDS2.Sessions.Api%20%40Properties.ClientId%3Acli_nilibeucitcu5c7ql3mnzxqoqm%20%40Properties.IssuerName%3A%28%22Al%20Rajhi%20Banking%20%26%20Inv.%20Corp.%22%20OR%20%22AL%20RAJHI%20BANKING%20AND%20INVESTMENT%20CORP.%22%29%20&agg_m=count&agg_m_source=base&agg_q=%40Properties.Status&agg_q_source=base&agg_t=count&analyticsOptions=%5B%22bars%22%2C%22dog_classic%22%2Cnull%2Cnull%5D&cols=service%2C%40Properties.Action%2C%40Properties.MerchantName%2C%40Properties.ClientId%2C%40Properties.IsMbc%2C%40Properties.MerchantAccountId%2C%40Properties.AcquirerMerchantId%2C%40Properties.AcquirerName%2C%40Properties.Status%2C%40Properties.StatusReason%2C%40Properties.NewStatus%2C%40http.method%2C%40http.status_code%2C%40Properties.Scheme%2C%40Properties.IssuerBin%2C%40Properties.IssuerName%2C%40Properties.IssuerCountry%2C%40Properties.ProtocolVersion%2C%40Elapsed%2C%40Properties.ThreeDsMethodUrl%2C%40Properties.AcsInfo.Url%2C%40Properties.ProcessingChannelId%2C%40Properties.ProcessorId&fromUser=true&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=time%2Cdesc&top_n=100&top_o=top&view=spans&viz=timeseries&x_missing=true&from_ts=1712483943762&to_ts=1715075943762&live=true)

  
We can check on the OC channel if any issues were reported during the timeframe. If no issue is reported, we can raise a ticket to the OC team - [here](https://checkoutsupport.freshservice.com/support/catalog/items/406)

## Glossaries and Definitions:

For **Key Terms and Definitions** on 3DS, please see ****[3DS Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22059673420818-3DS-Glossary-Introduction)   

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the 3DS articles, please see ****[3DS Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22059810908306-3DS-Tools-Permissions)
