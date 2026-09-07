---
id: 28386856168978
section_id: 22188552840594
title: "Onboarding a Merchant for Hosted Payment Pages"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/28386856168978-Onboarding-a-Merchant-for-Hosted-Payment-Pages"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-30T17:20:44Z"
permission_group_id: 26838654181266
content_tag_ids: ["01K0YPEVRSXXEYB936K329TF6D", "01K0YPFNT4QX4PX3Q34M6Z4789"]
label_names: ["HPP", "payment_interfaces"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

To onboard a merchant to use Hosted Payment Pages (HPP), merchants who are not properly onboarded for this product will be unable to create hosted payment pages.

**HPP create error**:  Merchant is seeing a 401 when calling the /hosted-payments API

**Onboarding request: **Merchant has requested to use HPP

 

## DESCRIBE THE ISSUE 💬

The merchant has requested to be onboarded for HPP or they're facing a 401 response from the API /hosted-payments.

 
 

## KEY TAKEAWAYS 🔑

- To enable Hosted Payment Pages for a merchant, you must use the "Merchant Hosted Pages Enablement" application in Retool

- A merchant receiving a `401` error when trying to create a HPP usually indicates they have not been onboarded for the HPP product

- The HPP creation request must be sent with a secret key, and a public key with access to the correct entity must also exist on the account

 

## RESOURCES 📍

| Tools | Related |
| --- | --- |
| [Merchant Hosted Pages Enablement](https://retoolprod.mgmt.ckotech.co/apps/f67192a4-a90a-11ec-841c-938543b18be9/launchpad/Merchant%20Hosted%20Pages%20Enablement)   Access granted via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274)    -  **Environment**: Production  -  **Application Name(s)**: Merchant Hosted Pages Enablement  -  **Permission**: Viewer - you can use and interact with apps | [Confluence documentation](https://checkout.atlassian.net/wiki/spaces/PI/pages/6092881943/Payment+Experience+FAQ+Document#HostedPaymentsPage-/-PaymentLinks) |

## PROCESS FOR ONBOARDING HOSTED PAYMENT PAGES 🖊️

### Step 1. Gather Required Information from the Merchant

The merchant needs to provide information for the HPP setup, see below for sample text you can ask the merchant:

```Since you want to use Hosted Payment Pages can you answer the following questions for onboarding purposes:
1. Display Name
2. 3ds enabled/disabled
3. Attempt non-3D secure enabled/disabled
4. Capture enabled/disabled
5. Capture time - Default 0
6. Card Schemes enabled - Options: Visa, Mastercard, Amex, Cartes Bancaires, Mada etc.
7. APMs - See here[](https://www.checkout.com/docs/payments/accept-payments/accept-a-payment-on-a-hosted-page#Supported_payment_methods) for all supported APMs
8. Optional - Terms and conditions URL 
9. Checkout.com logo in footer Yes or no ?
Let me know once we onboarded if you would like to customize your payment link:
https://www.checkout.com/docs/payments/accept-payments/create-a-payment-link/customize[](https://www.checkout.com/docs/payments/accept-payments/create-a-payment-link/customize-payment-links)
```

### 

### Step 2. Onboard the Merchant Using Retool

- Navigate to the **Merchant Hosted Pages Enablement** tool in Retool

- Enter the merchant's **Entity ID** and select the correct **Environment**

- Carefully input the configuration details you gathered from the merchant into the corresponding fields in the tool in Step 1

- Once all information is entered correctly, click **"Onboard/Update merchant"** to complete the process.

### Step 3. Monitor and Confirm

- After onboarding, monitor the merchant's entity in [Datadog](https://app.datadoghq.com/logs?query=%40scope%3Ahosted-payments%2Fcreate%20env%3Aprod%20service%3Ahpp%20%40EntityId%3Aent_z6xs6eigzmoehpqa6hyfhpmyn4&agg_m=count&agg_m_source=base&agg_t=count&clustering_pattern_field_path=message&cols=env%2Cservice%2Cstatus%2C%40HostedPaymentPageId%2C%40MerchantId&fromUser=true&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=desc&view=spans&viz=stream&from_ts=1740240986820&to_ts=1740413786820&live=true) to confirm that HPP creation requests are now successful

- The merchant should now be able to request a hosted payment page via the API and receive a redirect link in the response

## RESOLUTION ⚒️

**Expected Result**

- The merchant will be able to successfully create a Hosted Payment Page via an API request and receive a valid redirect URL in the response, resolving the `401` error

**Remediation Steps**

- The primary fix is to complete the onboarding process using the **Merchant Hosted Pages Enablement** tool in Retool, ensuring all required fields are filled in correctly

**Check Problem is Resolved**

- Monitor the merchant's entity on Datadog for successful HPP creation requests

- Ask the merchant to perform a test API request to create a payment link and confirm they receive a successful response and can access the payment page

**Rollback/Recovery**

- If any onboarding settings are incorrect, they can be modified by re-entering the information in the **Merchant Hosted Pages Enablement** tool and clicking "Onboard/Update merchant" again

 

## ESCALATION** ⏫**

- If the Hosted Payment Page does not perform as expected after following these steps, escalate the issue to the `**#payment-interfaces**` Slack channel for further assistance.

 
 

## FAQs** ****❓**

A customer is being redirected to the wrong URL after a payment attempt. How can we fix this?This issue can occur if default success/failure URLs are being used instead of the ones specified in the API request.

- 
**Verify URLs in CAT**: Log in to the Client Admin Tool (CAT) and check the configured `success_url` and `failure_url` for the merchant's processing channel. Confirm these URLs with the merchant.

- 
**Check 3DS Logs**: In Datadog, access the 3DS log for the transaction and find the `RedirectUri` parameter to confirm which URL was actually used for redirection.

- 
**Correct and Test**: If the URLs in CAT are incorrect, update them. Advise the merchant to ensure they are passing the correct URLs in the payment request if they do not wish to use the defaults. A test transaction should be conducted to confirm the fix

Is the hosted pages enablement tool used for onboarding Payment Links and Flow as well ?Yes
