---
id: 22197313084050
section_id: 22188546107666
title: "Google Pay"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22197313084050-Google-Pay"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:37:31Z"
permission_group_id: 26838654181266
content_tag_ids: ["01H8EDHC0MTG4YFD7E4B42CE0V"]
label_names: ["global", "case_integration", "google_pay", "apple_pay_and_google_pay_integration"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

Google Pay enables customers to securely perform one-touch payments using any credit or debit card connected to their Google account.

## Process Steps

**Documentation**

For detailed client-facing documentation, refer to:

- [Google Pay Integration Guide](https://www.checkout.com/docs/payments/add-payment-methods/google-pay)

- For troubleshooting Google Pay payments, refer to the [Google Pay troubleshooting guide](https://developers.google.com/pay/api/android/support/troubleshooting) for assistance with error codes

 **Common Queries**

**Query:** The merchant is receiving 500 error codes for Google Pay payments

**Solution:**

1. Check whether the merchant has processed Google Pay payments recently via the Dashboard

2. If so, we can assume that the error is not coming from their CKO configuration

3. If not, please further investigate the issue by escalating to the relevant team via Slack (e.g. if the issue is occurring via Flow → #ask-flow, HPP/PL → #payment-interfaces)

  
**Query: **Finding the Merchant ID for Google Pay in Checkout.com's e-commerce platform plug-in

**Solution: **

1. Please refer the merchant to the documentation for the merchant's specific e-commerce platform, which can be found in the [E-Commerce Platform Documentation](https://www.checkout.com/docs/payments/accept-payments/connect-to-an-ecommerce-platform).

**Query: **The card number that appears on Checkout’s portal seems to be different than the actual card number used by the client

**Solution: **

1. Google Pay uses a DPAN in cryptogram mode, and it also has a ‘PAN Only’ mode – this is when you save your card details directly in Google Chrome and not in your phone's wallet. Google Pay will generate a virtual card number and this will be shown instead. 

  1. PAN_ONLY - the card is stored on file with your customer’s Google account. Thus, the payment credentials are not bound to an Android device (for example, desktop or non-Android mobile web).

  2. CRYPTOGRAM_3DS - Google Pay offers SCA compliance by binding payment credentials to an Android device and allowing issuers to delegate the authentication to Google for all subsequent payments on that device.

  3. When a customer adds their card to Google Pay (On an Android device), Google will automatically generate a new card number called a DPAN (Device PAN) with a new expiration date. The DPAN is completely different from the real card number:

    1. If customers add the same card to multiple devices, a different DPAN is generated each time

    2. If the card is removed from their device, the DPAN is invalidated automatically

    3. If the same card is added again, a new DPAN is generated

**Query: **The** **merchant wants to omit the Google Pay button from the Hosted Payment Page.

**Solution: **

1. To omit Google Pay from HPP you can pass the parameter "disabled_payment_methods":"googlepay"

[https://api-reference.checkout.com/#operation/createAHostedPaymentsSession](https://api-reference.checkout.com/#operation/createAHostedPaymentsSession)

****

**Query: **The merchant has received the “Token_data_invalid” error message. 

**Solution:** 

1. View the token request in Datadog, and make sure all parameters are being passed according to [docs](https://www.checkout.com/docs/payments/add-payment-methods/google-pay#Step_2:_Tokenize_the_Google_Pay_payment_data) and the below example

```"token_data": {

   "protocolVersion": "ECv1",

   "signature": "TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ",

   "signedMessage": "{\"encryptedMessage\": \"ZW5jcnlwdGVkTWVzc2FnZQ==\", \"ephemeralPublicKey\": \"ZXBoZW1lcmFsUHVibGljS2V5\", \"tag\": \"c2lnbmF0dXJl\"}"

 }
```

 **Instructions for Shopify Merchants**

If the merchant is integrated with Shopify Onsite, they do not need to register an account with Apple Pay or Google Pay. Ensure they have followed these steps to activate Apple Pay:

1. Visit the [Shopify onsite payments app guide](https://www.checkout.com/docs/payments/accept-payments/connect-to-an-ecommerce-platform/shopify-onsite-payments-app).

2. Please note that to offer Apple Pay in their store, the merchant must adhere to [Apple's Acceptable Use Guidelines](https://developer.apple.com/apple-pay/acceptable-use-guidelines-for-websites/).

3. Follow the step-by-step instructions to enable Apple Pay after setting up your Shopify web store. The same steps apply to Google Pay.

If the merchant is integrated with Shopify offsite:

1. Follow the [steps](https://www.checkout.com/docs/payments/accept-payments/connect-to-an-ecommerce-platform/shopify-offsite-payments-app#Install_the_payments_app) to install the app.

2. Apple Pay and Google Pay will only be available for MENA customers on our offsite plugin and will not work for MENA customers on the onsite plugin.   
 

**6.10.3.1 Note**When a Shopify merchant has created the API Key, ensure that they have not selected the 'Allow any processing channel' option as this will cause payments to fail.

## Glossaries and Definitions:

For **Key Terms and Definitions** on Integration Issues, please see ****[Integrations Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22198412339346-Integrations-Glossary-Introduction)  For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Integration Issues articles, please see ****[Integrations Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22198326164754-Integrations-Tools-Permissions)
