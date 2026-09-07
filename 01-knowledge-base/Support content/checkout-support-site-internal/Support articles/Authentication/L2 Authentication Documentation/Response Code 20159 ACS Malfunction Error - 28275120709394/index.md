---
id: 28275120709394
section_id: 27822398640530
title: "Response Code 20159: ACS Malfunction Error"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/28275120709394-Response-Code-20159-ACS-Malfunction-Error"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-30T17:22:16Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JVS37HQR3H46AK9P20R40BMR", "01JZ88GPVA5D0SPHG3JNW36TE8"]
label_names: ["L2", "SOP", "authentication", "Troubleshooting guide"]
user_segment_ids: [11003606966930]
archive: false
---

This article explains **response code 20159**, which indicates an "ACS Malfunction" error. You might see a message like: "The payment failed due to a technical issue with the ACS used to perform 3DS authentication. If the issue persists, contact Checkout.com." This error means there was a technical problem with the Access Control Server (ACS) during 3D Secure (3DS) authentication, causing the payment to fail. If this issue continues, the merchant should contact Checkout.com.

 

## DESCRIBE THE ISSUE 💬

Merchants report transactions failing with** response code 20159**. From their perspective, the customer's payment failed during the 3D Secure verification process or, the authentication process is not going through.

 
 

## KEY TAKEAWAYS 🔑

- This  error signifies a technical issue with the Access Control Server (ACS) during 3D Secure (3DS) authentication.

- Declines are typically returned by the issuing bank (or ACS provider on their behalf) and is generally not due to our platform or merchant integration.

 

## RESOURCES 📍

| Tools | Case Examples | Related |
| --- | --- | --- |
| Checkout Agent Toolkit (ZD App) | [Case 20159](https://checkout1360.zendesk.com/agent/tickets/20159) |  |
| [Dashboard](https://dashboard.checkout.com/) [](https://checkout.atlassian.net/wiki/spaces/LL/database/6990364784?atl_f=PAGETREE) | [Case 60968](https://checkout1360.zendesk.com/agent/tickets/60968) | [Understand authentication failures](https://www.checkout.com/docs/payments/authenticate-payments/3d-secure/understand-authentication-failures) |
| [Traffic Insights](https://retoolprod.mgmt.ckotech.co/apps/a04c8c20-72cf-11eb-bea4-e7bba7ba05e6/payment-performance-shared-debug/Traffic%20Insights#payment_id=pay_pk4tedtjwlbudnbk3yfpkgsvoe) | [Case 57792](https://checkout1360.zendesk.com/agent/tickets/57792) |  |
| [Datadog](https://app.datadoghq.com/logs?query=&agg_m=count&agg_m_source=base&agg_t=count&cols=host%2Cservice%2C%40Properties.EventType&fromUser=true&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=time%2Cdesc&viz=stream&from_ts=1666681487938&to_ts=1666940687938&live=true) |  |  |

## PROCESS FOR 20159 FAILURE INVESTIGATION 🖊️

**Investigation on Dashboard**

Find the specific transaction on the Dashboard using Payment ID or other reference, and scroll down on the transaction details page until you locate the **"Authentication"** section

**Review Authentication Details:** In this section, observe the following key fields:

- **Transaction Status**

- **Transaction Status Reason**

- 
**Challenge Cancel** (Note: This field may not always be available)

Transaction status reason 22 indicates a transaction failure due to an ACS technical issue. In our documentation, you can find the meanings of the different transaction statuses and reason codes returned.

**Note**: The status reason codes are different from API response codes. These codes are returned by the issuer’s authentication service to indicate why the authentication failed.

 
**Investigation on Checkout Agent Toolkit**

Open the Zendesk ticket, click on **Apps**, and expand **Checkout** **Agent** Toolkit:- 

Select the relevant payment ID(s) to see the **Details** tab and **Timeline** tab. If you lack any information, go to **Helpful links** to access other tools:-

E.g. in Traffic Insights (Retool), paste the payment ID in the search and select the **Authentication** tab:-

 
**Investigation on Datadog**

In cases where there are no transaction status reason, you can use this [datadog filter](https://app.datadoghq.eu/logs?query=service%3AThreeDS2.Sessions.Api%20status%3Aerror&agg_m=count&agg_m_source=base&agg_t=count&clustering_pattern_field_path=message&cols=host%2Cservice%2C%40errorDescription&fromUser=true&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=desc&viz=stream&from_ts=1758104338549&to_ts=1758105238549&live=true%20) to look for any errors returned by the scheme.

You can replace the client ID accoridingly.

**For trends**

In case the merchant/requestor is complaining about multiple failures with this response code, you can make use of the [Datadog filter](https://app.datadoghq.com/logs?query=%28source%3Aauthentication%20service%3AThreeDS2.Sessions.Api%20env%3Aprod%2A%20%40Properties.ProtocolVersion%3A2%2A%20%40http.method%3APOST%20%40Properties.Status%3Achallenged%20%403ds2.transaction_status%3AN%20%28%40Properties.ClientId%3A%2Acli%2A%20OR%20%40Properties.IsMbc%3Afalse%29%20%40Properties.ClientId%3Acli_ewvyw5lqkvxexcohedbsg5abey%29&agg_m=count&agg_m_source=base&agg_q=%403ds2.transaction_status_reason%2C%40Properties.ThreeDsMethodUrl&agg_q_source=base%2Cbase&agg_t=count&analyticsOptions=%5B%22bars%22%2C%22dog_classic%22%2Cnull%2Cnull%2C%22value%22%5D&clustering_pattern_field_path=message&cols=host%2Cservice&fromUser=true&messageDisplay=inline&refresh_mode=sliding&sort_m=%2C&sort_m_source=%2C&sort_t=%2C&storage=hot&stream_sort=time%2Cdesc&top_n=10%2C10&top_o=top%2Ctop&viz=query_table&x_missing=true%2Ctrue&from_ts=1730369741514&to_ts=1731665741514&live=true) to see all affected ACS URLS. (replace the client ID accordingly)

You can share the most affected ACS URL when filling out the Issuer outreach [form](https://checkout.atlassian.net/jira/core/projects/IO/form/46). 

## RESOLUTION ⚒️

- This response code is returned by the issuing bank when it declines a transaction due to an ACS technical issue.

- In most cases, the failures are due to technical outages at the ACS levels. You can reach out to the OC team on [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277) to provide details of the trends with the particular ACS. 

- When they confirm that this issue is occurring intermittently and may require further understanding, you can reach out to the issuer outreach team - [Form](https://checkout.atlassian.net/jira/core/projects/IO/form/46)

 

## ESCALATION** ⏫**

- 
If a significant increase in 20159 failures is visible from one particular ACS provider, raise this with the issuer outreach team, providing necessary information. (TAM and AM are also able to raise this with them)
 

 
 

## FAQs** ****❓**

Can a 20159 error resolve itself?Yes, often, ACS malfunctions are intermittent technical issues. If the problem is temporary, retrying the payment after some time may result in a successful transaction.
