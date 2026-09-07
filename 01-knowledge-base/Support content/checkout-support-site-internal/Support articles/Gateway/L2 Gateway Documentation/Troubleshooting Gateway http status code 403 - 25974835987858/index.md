---
id: 25974835987858
section_id: 27992533473042
title: "Troubleshooting Gateway http status code 403"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/25974835987858-Troubleshooting-Gateway-http-status-code-403"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-31T16:03:53Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JWRC3HBBCWV9KD022M3M3WQQ", "01K09SJVY23XRXR71VSJXQDKPT"]
label_names: ["L2", "403", "API_error", "gateway", "HTTP_403"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article:**

Use this article to investigate why Gateway returns  http status code 403, this usually means:

**Invalid Payment State:** The action is not allowed given the current status of the payment (e.g. trying to refund an already voided payment, or refunding an authorized but not yet captured payment)

**Disabled Action:** The specific payment action is disabled in the merchant's configuration within the Client Admin Tool (CAT) for the processing channel used

## DESCRIBE THE ISSUE** 💬**

A merchant might say "I'm trying to refund a payment and I'm getting a 403 API response" 

While this example focuses on refunds, the investigation and resolution process applies to any payment action returning a 403.

 

## TOOLING**📍**

Click here to see what tools are needed

| [Datadog](https://app.datadoghq.com/logs?query=&cols=service%2C%40http.status_code&fromUser=true&index=processing&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=desc&viz=stream&from_ts=1749890157609&to_ts=1752482157609&live=true) | [Sherlock](https://retoolprod.mgmt.ckotech.co/apps/918d2a72-4c5a-11ec-88dc-53fd2c6a4170/gateway/Sherlock) | Client Admin Tool  CAT |
| --- | --- | --- |
| Access granted via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274)  - Select the following:    - Role: Standard    - Reason: Needed for BAU in merchant care | Access granted via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274)  - Select the following:    - Environment: Production    - Group_Name: `App.Retool.Prod.Gateway-Viewer` | Description: New joiner merchant care level 2 team Environment: Sandbox and Production  Permissions: Super User (both environments) - Super Admin ( sandbox only) Reason: To resolve merchant related issues raised through Salesforce |

 

## PROCESS FOR INVESTIGATING 403 RESPONSES** 🖊️**

### Step 1 . Locate the Payment and Confirm the 403 Error

**If the merchant provides the Payment ID:**

- Go to **Datadog**

- Use the search query: `@PaymentId:[Payment ID]`

- Example: `@PaymentId:pay_tcgshuqv4n7etharunag7n3ag4`

- Review the logs to find the payment action (e.g. a refund call) and confirm it received a `403` status code.

[Datadog example](https://app.datadoghq.com/logs?query=%40PaymentId%3A%2A&agg_m=count&agg_m_source=base&agg_t=count&clustering_pattern_field_path=message&cols=service%2Csource&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=time%2Cdesc&viz=stream&from_ts=1752501884492&to_ts=1752674684492&live=true)

Example: @PaymentId:pay_tcgshuqv4n7etharunag7n3ag4

 

**If the merchant does NOT provide a Payment ID:**

- Find the merchant’s Client ID (CLI) in the Zendesk ticket

- Go to **Datadog**

- Use the search query: `@http.status_code:403 @CkoClientId:[Client ID]`

[Datadog example](https://app.datadoghq.com/logs?query=%40http.status_code%3A403%20%40CkoClientId%3A%2A&agg_m=count&agg_m_source=base&agg_t=count&clustering_pattern_field_path=message&cols=service%2Csource&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=time%2Cdesc&viz=stream&from_ts=1752501884492&to_ts=1752674684492&live=true)

Example @http.status_code:403 @CkoClientId:cli_i6ogsej4iktetmrdqrw5zpdbry 

- Click on the "Gateway API" logs to retrieve the relevant `PaymentId`

Once you have the Payment ID and have confirmed the `403` error in Datadog, proceed to the next step

### Step 2: Identify the root cause

Now, determine why the action was forbidden

✅ **Best Practice:** Always check for an invalid payment state first. It's the most common cause and is quicker to diagnose than checking account configurations.**Cause A: Invalid action due to payment status**

Check **Payment Events** in Sherlock

- Search for the Payment ID in Sherlock

- Review the Payment Events timeline and the current payment status

- Check if the requested action is logical. For example, has this payment already been refunded or voided? Was it ever captured?

 

💡Tip: If the events show the payment has already been refunded, attempting another refund will result in a 403. This is an invalid action.

If this is the case, proceed to the **Resolution** section. If the action seems valid based on the payment status, proceed to Root Cause: Invalid action due to Merchant's Configuration as below**Cause B: Invalid action due to Merchant's configuration**

This happens when the action is disabled in the merchant's settings within the Client Admin Tool (CAT).

- Search for the paymentID in Datadog logs

  - Confirm the 403 response for the specific action (e.g. refund endpoint)

@PaymentId:* 

 

- Check in **Sherlock**

- Verify that the action (e.g.refund) is a theoretically appropriate action for this payment based on its status in Harmonia

- Check internal events

- Check the rejected event- which shows the action that is disabled and indicates it's disabled in CAT

In this example is the RefundRejected event - which shows acquirer_refunds_disabled and indicates refunds are disabled in CAT

- Check the client's configuration in CAT

  - Log in to CAT and select the merchant's account

  - Navigate to **Processing** 

- Navigate to **Gateway and Processing Channel**

- Review the settings for the relevant processing channel

- Example: Observe if "**Refunds**" are disabled for the merchant under this processing channel

 

 

## RESOLUTION **🛠️**

Based on your findings in Step 2, follow the appropriate resolution path below

**If the cause was an Invalid Payment State:**

- Inform the merchant that the request is invalid given the payment's current status and clearly explain why the action is not permitted.

- 
**Example script:** _"The _`_403_`_ error is occurring because this payment (ID: _`_$pay_...$_`_) has already been refunded on [Date]. A payment cannot be refunded in full more than once."_

**If the cause was a Disabled Merchant Configuration:**

- Inform the merchant that the action is currently disabled in their account configuration for that processing channel

- Ask if they would like to have this feature enabled

- If they confirm **Yes**, submit a request to the Merchant Configuration team by transferring the ticket in Zendesk (`Transfer > Merchant Configuration`)

⚠️ **Warning:** Some features may be disabled intentionally for risk or fraud prevention. If the Merchant Configuration team informs you that the feature cannot be enabled for this reason, cautiously inform the merchant that their account is under review. If they are a managed merchant, advise them to contact their designated Account Manager (AM).

## ESCALATION** ⏫**

If you have completed the investigation and the root cause is not an invalid payment state or a disabled configuration, you must escalate the issue.

- 
**When to Escalate:** When the `403` error's cause is not identifiable through the steps above

- 
**How to Escalate:** Raise a request to **Gateway L3** using the [Request form](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277)

- 
**Required Information:** Include the `PaymentId`, the troubleshooting steps you have already taken and links to the relevant logs in Datadog

- 
**Agent Responsibilities:** You must remain the case owner. Monitor the escalation for updates and keep the merchant informed of the progress.

**FAQ's ❓**

 What is a 403 Forbidden error?It's a standard HTTP status code indicating that the server understood the client's request but is refusing to fulfill it. Unlike a `401 Unauthorized` error, authentication is not the issue; permission is.

 Can I enable a disabled feature for a merchant myself in CAT?No. All merchant configuration changes must be handled by the dedicated Merchant Configuration team to ensure proper validation and prevent unintended consequences. Always follow the process of transferring the ticket.

 What if the payment status in Sherlock seems incorrect?If you suspect the payment status itself is wrong or stuck, this could be a separate issue. Include this suspicion and any supporting evidence in your escalation to L3.

## 

## RESOURCES** ****⭐**

**\****Case Examples**

- [Case 43296](https://checkout1360.zendesk.com/agent/tickets/43296)

- [Case 69800](https://checkout1360.zendesk.com/agent/tickets/69800)

**Related Articles**

****[How to investigate a payment error 401](https://checkout.atlassian.net/wiki/spaces/GW/pages/5624430773/How+to+Investigate+payment+errors#401)
