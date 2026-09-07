---
id: 22197313011986
section_id: 22188546107666
title: "Apple Pay"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22197313011986-Apple-Pay"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:34:42Z"
permission_group_id: 26838654181266
content_tag_ids: ["01H8EDHC0MTG4YFD7E4B42CE0V"]
label_names: ["global", "case_integration", "apple_pay", "apple_pay_and_google_pay_integration"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

Apple Pay enables Apple customers to authenticate card payments using Touch ID or Face ID. This eliminates the need for them to manually enter their card and shipping details.

## Process Steps

**Documentation**

For detailed client-facing integration documentation, refer to:

- 
[Apple Pay Integration Guide](https://www.checkout.com/docs/payments/add-payment-methods/apple-pay) - CKO

- 
This guide outlines the steps required to enable Apple Pay in-app and on the web - [Apple Pay Merchant Integration Guide](https://developer.apple.com/apple-pay/Apple-Pay-Merchant-Integration-Guide.pdf).
 

**Common Queries**

**Query**:  The merchant is receiving 500 error codes for Apple Pay payments

**Solution**: 

1. Check whether the merchant has processed Apple Pay payments recently via the Dashboard 

2. If so, we can assume that the error is not coming from their CKO configuration

3. If not, please further investigate the issue by escalating to the relevant team via Slack (e.g. if the issue is occurring via Flow → [#ask-flow](https://checkout.slack.com/archives/C04MK0MTABY), HPP/PL → [#payment-interfaces](https://checkout.slack.com/archives/C0193U64C2E))

**Query:** The Apple Pay button has disappeared as a payment option on the website. 

**Solution:**

1. Ensure Apple Pay is enabled on the site or e-commerce plugin.

2. Verify the business account is set up on the Apple Developer portal.

3. Upload all necessary certificates to the checkout account.

4. Follow the instructions from the Checkout.com documentation.

Additionally, check:

1. The browser being used is Safari (Apple Pay only works on Apple devices and Safari browsers)

2. The device has a payment card saved to the Wallet app (or System Preferences) for Apple Pay.

3. The device can perform Apple Pay payments elsewhere.

**Query: **The card number that appears on Checkout’s portal seems to be different from the actual card number used by the client.

**Solution: **

1. Please note that this is expected behaviour as the real PAN is never exposed to us by Apple Pay. We only receive the DPAN (Digital PAN) info that Apple generates for us - this is how Apple Pay is designed.

**Query: **A merchant would like to omit the Apple Pay button from the Hosted Payment Page,

**Solution**: 

1. To omit Apple Pay from HPP you can pass the parameter "disabled_payment_methods": "applepay"

[https://api-reference.checkout.com/#operation/createAHostedPaymentsSession](https://api-reference.checkout.com/#operation/createAHostedPaymentsSession)

****

  
**Query:** A merchant would like to make recurring unscheduled MIT payments using the Previous Payment ID use the following steps: 

**Solution: **

1. Please refer the merchant to the following [documentation](https://www.checkout.com/docs/payments/accept-payments/pay-with-stored-card-details/recurring-payments-with-stored-card-details): 

  1. Use the instrument ID obtained with a GET request to the /payments/ API. You will need the payment ID from the initial CIT Apple Pay transaction. This API will show the instrument ID (e.g., src_xxxxx)

  2. 
For the MIT, use the source.type.id and source.id.src_xxxxxx
 

**Error Messages**

```statusMessage: 'Payment Services Exception merchantId={{merchantID}} unauthorized to process transactions on behalf of merchantId={{merchantID}} reason=348634E1A817B9F919AD2061E921DDDB8C9BB7E1AE327FBD4EE40084C75B7BF6 never authorized mass enablement transactions to occur via 628E38C54349C7E9F0CAB5281919503A1EA8294FCD6C044F7B0FF0CCB3685039', statusCode: '400'
```

This shows that the merchant does not have the correct file path to their .pem and/or .key files. Advise them to check the path configured to the files is accessible from their server.

```
statusMessage: 'Payment Services Exception merchantId={{merchantID}} unauthorized to process transactions on behalf of merchantId={{merchantID}}  reason=48766840F29BC658FFED7A5554CB3EC3EBA65C2148F01469BF84978F1EBF6395 is not a registered merchant in WWDR and isn't properly authorized via Mass Enablement, either.","statusCode":"417"
```

This shows that the merchant identifier is not the same as the MID saved on the  Apple Pay developer account. Compare the MID (Identifier) from the Apple Pay developer account with the merchant's side.

Below is an example of the Apple Pay developer MID:

  
 

**“Payment not completed” error message on the Apple Pay UI**

**Solution:**

- Ask the merchant to restart their Apple setup

- They should then ensure that their domain is verified

- If they are still encountering this issue, ask them to check whether the correct “supportedNetworks”, “currencyCode” and “merchantCapabilities” are sent. Please refer them to the following Apple Developer page [Creating an Apple Pay Session](https://developer.apple.com/documentation/apple_pay_on_the_web/apple_pay_js_api/creating_an_apple_pay_session).

**Note for MENA Merchants**

- MADA Apple Pay outside Saudi Arabia - make sure countryCode is not SA and ”mada” is not in SupportedNetworks

- MADA Apple Pay in Saudi Arabia - countryCode = SA and SupportNetworks includes “mada”

 **Renewing Processing Certificates Before Expiration**

Apple Pay developers should be aware that their Payment Processing Certificates have a limited lifespan. As the expiration date approaches, Apple proactively sends reminder notifications to the team agent of your Apple Developer Account. These notifications are sent 30 days, 15 days, and 7 days before the certificate expires.

The Payment Processing Certificate plays a crucial role in Apple Pay transactions, as it's used to encrypt the Apple Pay token. Each certificate remains valid for 25 months from its activation date. It's essential to renew your certificate before it expires. Failure to replace the Certificate Signing Request (CSR) and activate a new certificate before the expiration date will result in all Apple Pay transactions failing.

If your certificate expires, users will experience a poor user interface/user experience (UI/UX). Specifically, after the user completes Touch ID verification, the payment sheet will be dismissed with an error message stating "Payment Not Complete!". To avoid this issue and ensure uninterrupted Apple Pay functionality, it's crucial to renew your certificate promptly.

Steps to renew certificate:

1. Follow steps 2 - 8 from the documentation [here](https://www.checkout.com/docs/payments/add-payment-methods/apple-pay#Step_2:_Generate_a_Certificate_Signing_Request_(CSR)), step 5 is not necessary as this is only for domain verification. 

2. **Do not activate the payment processing certificate!**

3. After completion of the above steps, add the .pem and .key files to your server. 

4. Have the Apple pay .pem and .key file paths pointing towards the newly created .pem and .key files from within the backend server or your e-commerce settings UI. 

5. Activate your payment processing certificate on the Apple developer page.

6. Processing will now be working with the new certificate.

Common questions:

Q. Can there be more than one payment processing certificate in my Apple Pay MID account?

A. Yes there can be more than one payment processing certificate created but only one can be active at any one time.

Q. Will there be any downtime?

A. Minimal to no downtime will be observed if the steps [above](https://docs.google.com/document/d/1RzCBwOFMRM9COW0XJ3VGK8GkZWusU_qzCMv-4Dul4Uc/edit?tab=t.0#heading=h.s7nkudjftmw1) are followed. Before saving changes to the file path in Step 4, the Apple Pay developer page should be open and ready to activate the new payment processing certificate once the file path changes are made to the backend/ecommerce settings.

 **Instructions for Shopify Merchants**

If the merchant is integrated with Shopify Onsite, they do not need to register an account with Apple Pay or Google Pay. Ensure they have followed these steps to activate Apple Pay:

1. Visit the [Shopify onsite payments app guide](https://www.checkout.com/docs/payments/accept-payments/connect-to-an-ecommerce-platform/shopify-onsite-payments-app).

2. Please note that to offer Apple Pay in their store, the merchant must adhere to [Apple's Acceptable Use Guidelines](https://developer.apple.com/apple-pay/acceptable-use-guidelines-for-websites/).

3. Follow the step-by-step instructions to enable Apple Pay after setting up your Shopify web store. The same steps apply to Google Pay.

If the merchant is integrated with Shopify offsite:

1. Follow the [steps](https://www.checkout.com/docs/payments/accept-payments/connect-to-an-ecommerce-platform/shopify-offsite-payments-app#Install_the_payments_app) to install the app.

2. Apple Pay and Google Pay will only be available for MENA customers on our offsite plugin and will not work for MENA customers on the onsite plugin. 

When a Shopify merchant has created the API Key, ensure that they have not selected the 'Allow any processing channel' option as this will cause payments to fail.

## Glossaries and Definitions:

For **Key Terms and Definitions** on Integration Issues, please see ****[Integrations Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22198412339346-Integrations-Glossary-Introduction)  

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Integration Issues articles, please see ****[Integrations Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22198326164754-Integrations-Tools-Permissions)
