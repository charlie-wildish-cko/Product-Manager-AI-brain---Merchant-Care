---
id: 28619470952210
section_id: 22188552840594
title: "Missing APMs on Payment Links"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/28619470952210-Missing-APMs-on-Payment-Links"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-08-22T12:56:53Z"
permission_group_id: 26838654181266
content_tag_ids: ["01K22QDZK4ZA0NHE1A5BX5QXA9", "01K22QE2SDP3E9QE5FMXQVA3MJ", "01K22QR1W0F5KSAXZENTFSDVG2", "01K22QRD6ESAZZ3N4XATFDCKM9"]
label_names: ["payment_link", "case_integration_issue_payment_links", "hosted_payments_and_payment_links_troubleshooting"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

A merchant reports that a desired Alternative Payment Method (APM) is not available as an option on their Payment Links, even though they expected it to be.

**APM not available:** An expected Alternative Payment Method (APM) is not showing when the Payment Links is loaded. 

**Solution**: Investigate and correct potential issues by checking the payment request fields (like currency, country and items array) and verifying the APM is correctly configured on the merchant's account.

 

## DESCRIBE THE ISSUE 💬

A merchant may report that a specific Alternative Payment Method (APM), which they expect to offer, is not appearing as an option on their Payment Links (PL). This guide provides the steps to diagnose and resolve this issue, ensuring that all correctly configured APMs are displayed to the customer.

 
 

## KEY TAKEAWAYS 🔑

- If an Alternative Payment Method (APM) is missing from the PL, first verify that the transaction's country and currency are supported for that APM

- For certain APMs like PayPal and Klarna, ensure the PL creation request includes an `items` array in the body

- Always consult the specific APM's [documentation](https://www.checkout.com/docs/payments/add-payment-methods) to confirm all mandatory fields are being sent in the request

- You can prevent specific payment methods from appearing on the PL by passing them in the `disabled_payment_methods` field of the API request

 

## RESOURCES 📍

| Tools | Case Examples | Related |
| --- | --- | --- |
| [Datadog](https://checkout.okta.com/app/datadog/exk3pc6ufjEUny7u3357/sso/saml) [Hosted Pages Enablement Tool](https://retoolprod.mgmt.ckotech.co/apps/f67192a4-a90a-11ec-841c-938543b18be9/launchpad/Merchant%20Hosted%20Pages%20Enablement) Client Admin Tool | [19422](https://checkout1360.zendesk.com/agent/tickets/19422%20) [53841](https://checkout1360.zendesk.com/agent/tickets/53841) | [APM Live Portfolio](https://checkout.atlassian.net/wiki/spaces/APM/pages/5137072925/APM+Portfolio) |

## PROCESS FOR ENABLING APM ON Payment Links 🖊️

### Step 1. Check Country and Currency Dependencies

- Many APMs are only available in specific countries and for specific currencies.You may have to create an entity specific to the region supporting that APM

- Use the ****[APM Live Portfolio](https://checkout.atlassian.net/wiki/spaces/APM/pages/5137072925/APM+Portfolio) to verify that the transaction's country and currency combination is supported for the desired APM

### Step 2. Verify the 'items' Array in the Request

- Some APMs, such as PayPal, require detailed order information to be displayed

- Check the merchant's PL creation request in [Datadog](https://app.datadoghq.eu/logs?query=%40scope%3Apayment-links%2Fcreate%20env%3Aprod%20service%3Apl%20%40EntityId%3Aent_z6xs6eigzmoehpqa6hyfhpmyn4&agg_m=count&agg_m_source=base&agg_t=count&clustering_pattern_field_path=message&cols=env%2Cservice%2Cstatus%2C%40PaymentLinksId%2C%40MerchantId&fromUser=true&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=desc&view=spans&viz=stream&from_ts=1740240986820&to_ts=1740413786820&live=true). If the desired APM requires it, ensure that the request body includes an `items` array with product details

### Step 3. Consult the Specific APM Documentation

- The most critical step is to review the official Checkout.com [documentation](https://www.checkout.com/docs/payments/add-payment-methods) for the specific APM in question

- The documentation will provide a definitive list of all required fields and a valid example request. Compare the merchant's request body against the documentation to identify any missing or malformed parameters

### Step 4. Confirm Account Configuration

- Ensure the APM has been correctly configured on the merchant's account in the Hosted Pages enablement tool

- In the **Client Admin Tool (CAT)**, navigate to the merchant's processing profiles. Verify that the APM is enabled and properly configured. For detailed guidance on credentials and setup in sandbox, refer to the ****[APM on NAS documentation](https://checkout.atlassian.net/wiki/spaces/APM/pages/4393566788/APM+on+NAS+Processing+profile+configuration#Tamara-%E2%9A%99%EF%B8%8F)

## RESOLUTION ⚒️

**Expected Result**

- The desired APM will be visible as a payment option on the merchant's PL, provided the conditions for that APM (e.g. currency, country) are met for the specific transaction

**Remediation Steps**

- 
**Configuration Fix**: If the APM was not configured on the account, enable it on the merchant's processing profile in the Client Admin Tool (CAT)

- 
**Request Body Fix**: If parameters were missing from the API call, the merchant must update their integration to include all fields required by the APM, such as correcting currency codes or adding an `items` array

**Check Problem is Resolved**

- Ask the merchant to generate a new PL link for a transaction that meets the criteria for the APM in question

- Have the merchant load the PL link and confirm that the APM button is now visible and selectable

**Rollback/Recovery**

- If enabling a new APM causes unexpected issues, it can be disabled in the merchant's processing profile in CAT

- If the merchant's code changes were the cause, they can roll back their code to the previous version

## ESCALATION** ⏫**

If you have verified all configurations and the APM is still not appearing, please seek further assistance in the `**#payment-interfaces**` Slack channel

 
 

## FAQs** ****❓**

How can I remove the Apple Pay or Google Pay button from the Payment Links?You can hide these buttons/APMs by passing a specific parameter in your `Create a Payment Links Session` API request.

- 
**To hide Apple Pay**: Pass `"disabled_payment_methods":["applepay"]`.

- 
**To hide Google Pay**: Pass `"disabled_payment_methods":["googlepay"]`

Are there special instructions for Shopify merchants regarding Apple Pay and Google Pay using Offsite plugin ?Yes, the process differs depending on their integration type.

- 
**Shopify Onsite**: Merchants using this integration do not need to register a separate account with Apple Pay. They should follow the Shopify onsite payments app guide to activate Apple Pay and must adhere to Apple's Acceptable Use Guidelines. The same steps apply to Google Pay.

- 
**Shopify Offsite**: For merchants using the offsite plugin, Apple Pay and Google Pay will only be available for MENA customers.
