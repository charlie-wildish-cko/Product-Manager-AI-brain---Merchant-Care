---
id: 27576244678418
section_id: 27992533473042
title: "Troubleshooting Missing Gateway Events - Captures and Refunds"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/27576244678418-Troubleshooting-Missing-Gateway-Events-Captures-and-Refunds"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-30T16:54:03Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JW93XRA9V38PV0NS2PYF1NJW", "01JWRC3HBBCWV9KD022M3M3WQQ", "01JWRC46WWC378V6E80MQ1J31Q", "01K09SJVY23XRXR71VSJXQDKPT", "01K09SSJ4XDJCTQ9EJPETVTG43", "01K09STJZ9CB100KSVXCRA1T2Q"]
label_names: ["stuck_in_captured", "stuck_in_authorised", "payment_status_incorrect", "missing_payment_events", "gateway_events_missing", "Gateway"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article:**

Use this article to investigate why Gateway events are missing

**Problem / Symptom**: Common causes include payment capture or refund events missing

## DESCRIBE THE ISSUE** 💬**

Internal teams are reporting missing Gateway events despite their internal reports showing payments as cleared or settled (e.g. capture/refund).

Merchants might ask:

- Why is my payment stuck in authorised state when we captured the payment

- Why is my payment stuck in captured state when we refunded the payment

## KEY TAKEAWAYS 🔑

- The issue is usually missing Gateway events for settled payments

- Use Datadog, Traffic Insights, Sherlock, and Clearing Events tools

- First, identify the payment and check if public events exist

- If public events are missing, check Sherlock for internal events

- Resolution involves a reversal, adjustment, or replaying the event via L3

## TOOLING**📍**

Click here to see the tools you'll need 

| **Tool** | **Access** |
| --- | --- |
| [Datadog](https://app.datadoghq.com/logs?query=&cols=service%2C%40http.status_code&fromUser=true&index=processing&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=desc&viz=stream&from_ts=1749890157609&to_ts=1752482157609&live=true) | - Access is granted via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274)   - Select the following:    - Role: Standard    - Reason: Needed for BAU in merchant care |
| [Traffic Insights](https://retoolprod.mgmt.ckotech.co/apps/a04c8c20-72cf-11eb-bea4-e7bba7ba05e6/payment-performance-shared-debug/Traffic%20Insights) | - Access is granted via[Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274)   - Select the following:    - Environment: Production    - Group_Name: `App.Retool.Prod.Payment-Performance-Internal-Viewers` |
| [Sherlock](https://retoolprod.mgmt.ckotech.co/apps/918d2a72-4c5a-11ec-88dc-53fd2c6a4170/gateway/Sherlock) | - Access is granted via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274)   - Select the following:    - Environment: Production    - Group_Name: `App.Retool.Prod.Gateway-Viewers` |
| [Test App KH](https://retoolsbox.mgmt.ckotech.co/apps/d7995950-b2a7-11ed-97ea-0328566f1311/gateway/Test%20App%20KH) (For Sandbox) | - Access is granted via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274)   - Select the following:    - Environment: Staging    - Permission: Viewer    - Group-Name: `App.Retool.Sbox.Gateway-Editors` |
| [Clearing Events](https://retoolprod.mgmt.ckotech.co/apps/2ca5f230-1197-11ed-822c-6f0a4549a613/cardprocessing/Clearing%20Events) | - Access is granted via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274)   - Select the following:    - Environment: Production    - Group_Name: `App.Retool.Prod.Cardprocessing-Viewers` |

 

**PROCESS FOR INVESTIGATING MISSING EVENTS**

### Step 1: Identify the Payment ID (pay_xxx)

- In Zendesk, open the relevant ticket from the merchant

- Click on the Apps icon to expand the Apps sidebar, and expand the **Checkout Agent tool**

- Under **Payments mentioned**, you will see the relevant payment ID(s) to see the **Details** and **Timeline**:- 

- Select the relevant payment ID to see the **Details** and **Timeline **for the payin event:-

### Step 2: Determine payment type and if the event is missing

Click on the **Timeline** tab to see what events can be found:-

- Payin events begin with `Charge*`:
 

- APM events begin with `AlternativeCharge*`:
Payout events are not in Traffic Insights; they're owned by the Pay To Card team. For more information, they can reach out to them via the form [here](https://checkoutsupport.freshservice.com/support/catalog/items/276) or [#ask-card-payouts](https://checkout.enterprise.slack.com/archives/C04776NRR8T).If it's a Payin or APM, check the **Checkout Agent Toolkit** for the event:

- 
**Event missing?** Proceed to Step 3

- 
**Event present?** The issue is likely on the user's end (e.g., report or downstream). We should tell them the events are in Gateway, and they should check further

### Step 3: Check internal events

Traffic insights can be accessed at the bottom of **Checkout Agent Toolkit**, under **Helpful links**Even if a public event is missing from Traffic Insights, you can often find internal events in Sherlock (Checkout Agent Toolkit > Helpful links > Sherlock), using the Payment IDExample: `pay_z7bp3ulclktennzi4tq4so2elm`

- Internal events: Shows `RefundRequested`

- Public events: No corresponding refund event

- Deduction: The merchant attempted a refund, but it failed

- A successful refund would show a `Refunded` internal event, which would generate a `ChargeRefunded` public event (e.g., `pay_r2wtasa27v5evfzexcbogeuxci`)

  - Internal events: Shows `Refunded`

- Public events: Shows `ChargeRefunded`

### Step 4: Check the logs for any errors and insights

- Search the Payment ID in [Datadog](https://app.datadoghq.com/logs?query=&cols=service%2C%40http.status_code&fromUser=true&index=processing&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=desc&viz=stream&from_ts=1749890157609&to_ts=1752482157609&live=true) (filter: `@PaymentId:pay_xxx`) to find errors or exceptions causing missing events

- Example: `pay_z7bp3ulclktennzi4tq4so2elm`

  - Logs indicate the refund event was missing due to a timeout between Gateway and Card Processing, leading to a cancelled refund request.

  - 

### Step 5: Check downstream for cleared/settled events

Sometimes, captures or refunds fail upstream but clear and settle downstream—a known issue between Gateway and Card ProcessingUse the Settlement details and Timeline in the Agent Toolkit to check for cleared or settled payments Should you need to utilise any information on clearing & settlement data that isn't in the Agent Toolkit, you can utilise [Clearing Events](https://retoolprod.mgmt.ckotech.co/apps/2ca5f230-1197-11ed-822c-6f0a4549a613/cardprocessing/Clearing%20Events).

## RESOLUTION **🛠️**

### 1. Request a reversal

Schemes which support reversals:

- For Visa or Mastercard payments within the allowed time limits (see [here](https://checkout.atlassian.net/wiki/spaces/PEO/pages/6525026936/PROCESS+Performing+reversals+on+MC+VISA+clearing+platform)), you can request a reversal by raising a new case with Merchant Care L1 and provide the ARN (Acquirer Reference Number).

- For Amex, DCI and JCB (see [here](https://checkout.atlassian.net/wiki/spaces/PEO/pages/6525027279/PROCESS+Reversal+Conditions)), you can request a reversal by raising a new case with Card Processing L3 via the form [here](https://checkoutsupport.freshservice.com/support/catalog/items/600) and provide the ARN.

- 
This will effectively undo the capture or refund downstream, making it as if it never happened.
💡**NOTE: Only request a reversal if the merchant doesn't need to retry the capture or refund. This action is irreversible, and once a reversal is made the merchant cannot perform subsequent captures or refunds via API.**

### 2. Request an adjustment

If a reversal isn't an option, you can ask the payments team (using the ZD macro: **Transfer > Treasury Payments**) to perform an adjustment. 

- 
**Provide the following:**

  - ARN

  - Clearance of transactions screenshot (Clearing Events tool)

  - Proof of scheme settlement from the Unified Scheme Settlement report on looker showing the value date (use looker report [here](https://checkoutinternal.eu.looker.com/explore/finance_treasury/unified_schemes_settlement?qid=LMKVFVhHB8iAesNiVYxab3&toggle=fil), if no access then either raise [here](https://checkoutsupport.freshservice.com/support/catalog/items/682) or ask FE L2 to assist).

- 
**For a missing capture event:** Request a **positive adjustment**. This is because the cardholder was charged, but the merchant hasn't received the funds.

- 
**For a missing refund event:** Request a **negative adjustment**. In this scenario, the cardholder received the funds, but the merchant hasn't been debited.

This process will correct the merchant's balance and statements.

### 3. Replay the missing event (Actioned by L3)

For Payins with a capture or refund made within 14 days, Gateway L3 may be able to replay missing events if they exist in our dead-letter queue (i.e. AWS DLQ) and the original capture or refund was reversed.

- If successful, this action will:

  - Generate a new capture or refund event in Gateway events/dashboard

  - Send the event for clearing and settlement

- For APMs (Alternative Payment Methods), Gateway L3 can request APM L3 to send the missing event, allowing them to manually replay it in AWS

## ESCALATION** ⏫**

If additional investigation is required or the events need to be fixed/replayed, then raise it with Gateway L3 team using the form [here](https://checkoutsupport.freshservice.com/support/catalog/items/588)

## RESOURCES** ****⭐**

| **Case Examples** | **Related** |
| --- | --- |
| - [Case 49102](https://checkout1360.zendesk.com/agent/tickets/49102)  - [Case 51090](https://checkout1360.zendesk.com/agent/tickets/51090)  - [Case 50954](https://checkout1360.zendesk.com/agent/tickets/50954)  - [Case 49373](https://checkout1360.zendesk.com/agent/tickets/49373) | - [Missing Events Workshop](https://checkout.atlassian.net/wiki/spaces/MCL2/pages/7056622347/GW+Workshops)  - [Confluence - How to investigate missing events](https://checkout.atlassian.net/wiki/spaces/GW/pages/5533926162/How+to+investigate+missing+events) |
