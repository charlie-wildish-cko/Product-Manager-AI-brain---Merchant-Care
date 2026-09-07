---
id: 28402906162066
section_id: 22188552840594
title: "Missing APMs on Hosted Payment Pages"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/28402906162066-Missing-APMs-on-Hosted-Payment-Pages"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-08-22T12:59:11Z"
permission_group_id: 26838654181266
content_tag_ids: ["01K0YPEVRSXXEYB936K329TF6D", "01K0YPFBSHBA4R57ZGBPSED26T"]
label_names: ["apm_enablement_hpp", "hosted_payment_pages", "HPP"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

A merchant reports that a desired Alternative Payment Method (APM) is not available as an option on their Hosted Payment Page, even though they expected it to be.

**APM not available:** An expected Alternative Payment Method (APM) is not showing when the Hosted Payment Page is loaded. 

**Solution**: Investigate and correct potential issues by checking the payment request fields (like currency, country and items array) and verifying the APM is correctly configured on the merchant's account.

 

## DESCRIBE THE ISSUE 💬

A merchant may report that a specific Alternative Payment Method (APM), which they expect to offer, is not appearing as an option on their Hosted Payment Page (HPP). This guide provides the steps to diagnose and resolve this issue, ensuring that all correctly configured APMs are displayed to the customer.

 
 

## KEY TAKEAWAYS 🔑

- If an Alternative Payment Method (APM) is missing from the HPP, first verify that the transaction's country and currency are supported for that APM

- For certain APMs like PayPal and Klarna, ensure the HPP creation request includes an `items` array in the body

- Always consult the specific APM's [documentation](https://www.checkout.com/docs/payments/add-payment-methods) to confirm all mandatory fields are being sent in the request

- You can prevent specific payment methods from appearing on the HPP by passing them in the `disabled_payment_methods` field of the API request

 

## RESOURCES 📍

| Tools | Case Examples | Related |
| --- | --- | --- |
| [Datadog](https://checkout.okta.com/app/datadog/exk3pc6ufjEUny7u3357/sso/saml) Hosted Enablement Tool Client Admin Tool | [19422](https://checkout1360.zendesk.com/agent/tickets/19422%20) [53841](https://checkout1360.zendesk.com/agent/tickets/53841) | [APM Live Portfolio](https://checkout.atlassian.net/wiki/spaces/APM/pages/5137072925/APM+Portfolio) |

## PROCESS FOR ENABLING APM ON HOSTED PAYMENT PAGE 🖊️

### Step 1. Check Country and Currency Dependencies

- Many APMs are only available in specific countries and for specific currencies.You may have to create an entity specific to the region supporting that APM

- Use the ****[APM Live Portfolio](https://checkout.atlassian.net/wiki/spaces/APM/pages/5137072925/APM+Portfolio) to verify that the transaction's country and currency combination is supported for the desired APM

### Step 2. Verify the 'items' Array in the Request

- Some APMs, such as PayPal, require detailed order information to be displayed

- Check the merchant's HPP creation request in [Datadog](https://app.datadoghq.eu/logs?query=%40scope%3Ahosted-payments%2Fcreate%20env%3Aprod%20service%3Ahpp%20%40EntityId%3Aent_z6xs6eigzmoehpqa6hyfhpmyn4&agg_m=count&agg_m_source=base&agg_t=count&clustering_pattern_field_path=message&cols=env%2Cservice%2Cstatus%2C%40HostedPaymentPageId%2C%40MerchantId&fromUser=true&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=desc&view=spans&viz=stream&from_ts=1740240986820&to_ts=1740413786820&live=true). If the desired APM requires it, ensure that the request body includes an `items` array with product details

### Step 3. Consult the Specific APM Documentation

- The most critical step is to review the official Checkout.com [documentation](https://www.checkout.com/docs/payments/add-payment-methods) for the specific APM in question

- The documentation will provide a definitive list of all required fields and a valid example request. Compare the merchant's request body against the documentation to identify any missing or malformed parameters

### Step 4. Confirm Account Configuration

- Ensure the APM has been correctly configured on the merchant's account

- In the **Client Admin Tool (CAT)**, navigate to the merchant's processing profiles. Verify that the APM is enabled and properly configured. For detailed guidance on credentials and setup in sandbox, refer to the ****[APM on NAS documentation](https://checkout.atlassian.net/wiki/spaces/APM/pages/4393566788/APM+on+NAS+Processing+profile+configuration#Tamara-%E2%9A%99%EF%B8%8F)

## RESOLUTION ⚒️

**Expected Result**

- The desired APM will be visible as a payment option on the merchant's HPP, provided the conditions for that APM (e.g. currency, country) are met for the specific transaction

**Remediation Steps**

- 
**Configuration Fix**: If the APM was not configured on the account, enable it on the merchant's processing profile in the Client Admin Tool (CAT)

- 
**Request Body Fix**: If parameters were missing from the API call, the merchant must update their integration to include all fields required by the APM, such as correcting currency codes or adding an `items` array

**Check Problem is Resolved**

- Ask the merchant to generate a new HPP link for a transaction that meets the criteria for the APM in question

- Have the merchant load the HPP link and confirm that the APM button is now visible and selectable

- 
**Rollback/Recovery**

  - If enabling a new APM causes unexpected issues, it can be disabled in the merchant's processing profile in CAT

  - If the merchant's code changes were the cause, they can roll back their code to the previous version

## ESCALATION** ⏫**

If you have verified all configurations and the APM is still not appearing, please seek further assistance in the `**#payment-interfaces**` Slack channel

 
 

## FAQs** ****❓**

How can I remove the Apple Pay or Google Pay button from the Hosted Payment Page?You can hide these buttons/APMs by passing a specific parameter in your `Create a Hosted Payments Session` API request.

- 
**To hide Apple Pay**: Pass `"disabled_payment_methods":["applepay"]`.

- 
**To hide Google Pay**: Pass `"disabled_payment_methods":["googlepay"]`

Are there special instructions for Shopify merchants regarding Apple Pay and Google Pay using Offsite plugin ?Yes, the process differs depending on their integration type.

- 
**Shopify Onsite**: Merchants using this integration do not need to register a separate account with Apple Pay. They should follow the Shopify onsite payments app guide to activate Apple Pay and must adhere to Apple's Acceptable Use Guidelines. The same steps apply to Google Pay.

- 
**Shopify Offsite**: For merchants using the offsite plugin, Apple Pay and Google Pay will only be available for MENA customers.
