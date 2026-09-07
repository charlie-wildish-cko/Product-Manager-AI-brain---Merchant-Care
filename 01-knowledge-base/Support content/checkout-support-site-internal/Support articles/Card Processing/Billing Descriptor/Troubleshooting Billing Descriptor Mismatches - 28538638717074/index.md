---
id: 28538638717074
section_id: 28767955575826
title: "Troubleshooting Billing Descriptor Mismatches"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/28538638717074-Troubleshooting-Billing-Descriptor-Mismatches"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-01-22T16:19:02Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JVS26PBA73NGJJETCPWS3SPE", "01JWRC3HBBCWV9KD022M3M3WQQ", "01JWRC46WWC378V6E80MQ1J31Q", "01K1X916G4H91REAG5PKAXMYBP"]
label_names: ["L2", "Troubleshooting", "dynamic descriptor", "bank statement name", "billing descriptor mismatch"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

To troubleshoot why an incorrect billing descriptor appears on a customer's bank statement or the Checkout dashboard for schemes Visa, Mastercard, Amex and DCI.

**Problem/Solution**

Common causes include incorrect billing descriptor name, phone number or email address showing on the customer's statement or in dashboard.

## DESCRIBE THE ISSUE 💬

A merchant has reported that a customer's bank statement or their Checkout dashboard shows a different billing descriptor than expected.

NOTE: These troubleshooting steps apply to all acceptor fields (Name, Phone, Email), not just the `AcceptorName` used in this example.

## KEY TAKEAWAYS 🔑

- Use Datadog to check the payment request's `billing_descriptor.name`

- Verify the `Properties.AcceptorName` in Card Processing logs

- Compare these two names to identify where the mismatch is occurring

- The **Client Admin Tool (CAT)** reveals a merchant's dynamic descriptor settings

- Engage the Card Processing L3 team for Amex and Discover issues

## TOOLING**📍**

Click here to see the tools you'll need 

| **Tool** | **Access** |
| --- | --- |
| [Datadog](https://app.datadoghq.com/logs?query=&cols=service%2C%40http.status_code&fromUser=true&index=processing&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=desc&viz=stream&from_ts=1749890157609&to_ts=1752482157609&live=true) | - Access is granted via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274)   - Select the following:    - Role: Standard    - Reason: Needed for BAU in merchant care |
| [Traffic Insights](https://retoolprod.mgmt.ckotech.co/apps/a04c8c20-72cf-11eb-bea4-e7bba7ba05e6/payment-performance-shared-debug/Traffic%20Insights) | - Access is granted via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274)   - Select the following:    - Environment: Production    - Group_Name: `App.Retool.Prod.Payment-Performance-Internal-Viewers` |
| [Client Admin Tool (CAT)](https://client-admin.cko-prod.ckotech.co/web/nas/) | - Access is granted via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274)   - Select the following (2 separate requests):    - Environment: Production/Sandbox    - Permissions: Super User (Prod)/Super Admin (Sbox)     - Team Name: Merchant Care     - Reason: Needed for BAU in Merchant Care L2 |

## PROCESS FOR TROUBLESHOOTING BILLING DESCRIPTOR MISMATCHES 🖊️

### Step 1: Check the merchant's payment request

- In Datadog, using the payment ID (pay_xxx) search the `/payments` endpoint logs (example logs [here](https://app.datadoghq.eu/logs?query=%40PaymentId%3A%2A%20service%3A%22Gateway%20API%22%20%40http.url_details.path%3A%22%2Fpayments%22%20%40Request.BillingDescriptor.Name%3A%2A&agg_m=count&agg_m_source=base&agg_t=count&clustering_pattern_field_path=message&cols=service%2C%40http.status_code%2C%40Request.BillingDescriptor.Name&fromUser=true&index=processing&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=desc&viz=stream&from_ts=1754318704167&to_ts=1754405104167&live=true)) for the `billing_descriptor.name` value sent by the merchant

- 
For example payment pay_gi3ksa4eonfefdvyqphkfzoxgy, `billing_descriptor.name: "Circle K GiftCard"` was sent by the merchant:

### Step 2: Check the Card Processing logs

- Review the authorisation logs (example logs [here](https://app.datadoghq.eu/logs?query=%40PaymentId%3A%2A%20%40Properties.ActionType%3AAuthorization%20source%3Acard-processing%20%40Properties.AcceptorName%3A%2A&agg_m=count&agg_m_source=base&agg_t=count&clustering_pattern_field_path=message&cols=service%2C%40http.status_code%2C%40Properties.AcceptorName&index=processing&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=desc&viz=stream&from_ts=1754318853303&to_ts=1754405253303&live=true)) for the `Properties.AcceptorName` to see what our system sent to the card scheme

- 
For example payment pay_gi3ksa4eonfefdvyqphkfzoxgy, `Properties.AcceptorName:"Castorama Gift Card"` sent to the card scheme

### Step 3: Compare the names

- 
**Scenario 1: **`**billing_descriptor.name**`** DOES NOT match **`**Properties.AcceptorName**`

  - Proceed to Step 4, this indicates an issue with the merchant's configuration

- 
**Scenario 2: **`**billing_descriptor.name**`** MATCHES **`**Properties.AcceptorName**`

  - Proceed to Resolution; this suggests the issue is outside our control (with the scheme or issuing bank)

- 
**Scenario 3: **`**billing_descriptor.name**`** MATCHES **`**Properties.AcceptorName**`** or **`**@Properties.GatewayAuthorizeRequest.BillingDescriptor.Name**`** and scheme is Amex or DCI**

  - Proceed to Resolution; this suggests an issue with the merchant registration details on our side or a problem outside our control (with the scheme or issuing bank)

- 
**Scenario 4: **`**billing_descriptor.name**`** is incorrect from the merchant's side**

  - Proceed to Resolution; if the `billing_descriptor.name` in the DD logs is not what the merchant expected, the issue is on their end

- For example payment pay_gi3ksa4eonfefdvyqphkfzoxgy, it falls under Scenario 1

### Step 4: Check Client Admin Tool to review their configuration

- 
Check the processor settings to see what `Acceptor trading name` is displayed as per below (see example [here](https://client-admin.cko-prod.ckotech.co/web/nas/entities/ent_ga3z3htmc6numaqgqdy3ae3eu4/gateway-processing-channels/pc_6i3vywtzanyedij2xoohc7vc3q/gateway-processing-channel-details/pr_sfac74756kwefcsxfvbohhtk4e/gateway-profile-processor-details)): 

- 
Check whether dynamic descriptor is enabled as per below:

  - 
**Enabled:** Our system uses the name from the payment request

  - 
**Disabled:** Our system uses the default `Acceptor trading name` value from CAT (see example [here](https://client-admin.cko-prod.ckotech.co/web/nas/entities/ent_ga3z3htmc6numaqgqdy3ae3eu4/gateway-processing-channels/pc_6i3vywtzanyedij2xoohc7vc3q/gateway-processing-channel-details/pr_sfac74756kwefcsxfvbohhtk4e/gateway-profile-processor-details))

- For example payment pay_gi3ksa4eonfefdvyqphkfzoxgy, `Acceptor trading name` was showing as `Castorama Gift Card` and since dynamic descriptor was disabled it used the default value in CAT rather than what the merchant sent

## RESOLUTION ⚒️

### Raise it to merchant configuration team (Scenario 1)

- Escalate to the Merchant Configuration team (ZD macro; Transfer > Merchant Configuration > Global) to update the `Acceptor trading name` or dynamic descriptor toggle

### Root cause is from the scheme/issuer (Scenario 2 and 3)

- Explain to the merchant that our systems sent the correct descriptor and the issue lies with the card scheme or issuing bank. Advise the cardholder to contact their bank

### Raise it with payment configuration team (Scenario 3)

- Escalate to Payment Configuration (ZD macro; Transfer > Eng > Payment Configuration) to verify stored billing descriptors. Since we send these for Amex and DCI, any internal misconfigurations will be identified here; otherwise, the issue is with the scheme or issuer.

### Ask the merchant to correct their request (Scenario 4)

- Advise the merchant to correct the `billing_descriptor.name` in their payment request

## ESCALATION** ⏫**

- Escalate to the Card Processing L3 team using the form [here](https://checkoutsupport.freshservice.com/support/login) for Amex and Discover issues, or if further investigation is needed.

## RESOURCES** ****⭐**

| **Case Examples** | **Related** |
| --- | --- |
| - [Case 72045](https://checkout1360.zendesk.com/agent/tickets/72045)  - [Case 64420](https://checkout1360.zendesk.com/agent/tickets/64420)  - [Case 47873](https://checkout1360.zendesk.com/agent/tickets/47873) | [Confluence - Billing Descriptor Issues](https://checkout.atlassian.net/wiki/spaces/GW/pages/5893652875/How+to+investigate+billing+descriptor+issues) |
