---
id: 29565277481618
section_id: 22188546107666
title: "Apple Pay Setup"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/29565277481618-Apple-Pay-Setup"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-09-29T11:28:12Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JVM5WYPR2CFA1MQCGT9B790K", "01K5E3PNA13CNSNF38GYBE23WS", "01K5E3Q929BVJGYQCW8MWEBA4W", "01K5E3QP3GVVK69RACH0BTQYC9"]
label_names: ["apple_pay", "apple_pay_setup"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**  

To set up and integrate Apple Pay, it details the two available integration methods: API Only (for direct integration) and Flow (for simplified integration).  

**Problem:** A merchant needs to integrate Apple Pay as a payment method on their website.

**Solution:** Follow the step-by-step instructions for either the API Only or Flow integration method to enable Apple Pay.

## DESCRIBE THE ISSUE 💬

This guide provides the necessary steps to integrate Apple Pay. Depending on technical resources and customization needs, choose one of two integration paths. 

The **API Only** integration offers maximum control but requires significant development effort, including managing certificates and your own backend. The **Flow** integration is a simpler, streamlined approach where most of the technical complexity is handled for a merchant.

## KEY TAKEAWAYS 🔑

- There are two setup methods: **API Only** and **Flow**

- 
**API Only** provides full customization and requires an Apple Developer Account and significant backend development

- 
**Flow** offers a quick and simple setup with less development effort required

- Domain verification is a mandatory step for both methods

- Common setup errors for the API Only method are often related to incorrect file paths, certificate mismatches, or expired SSL certificates

## PROCESS FOR APPLE PAY SETUP 🖊️

Follow the instructions for the integration method the merchant has chosen.          

**Method 1: ******[API Only Setup](https://www.checkout.com/docs/payments/add-payment-methods/apple-pay/api-only)

This process requires you to perform several technical steps to generate certificates and handle the integration.
           **Step 1. Set up Your Apple Developer Account and Certificates**          

The merchant must perform these steps in their Apple Developer Account to generate the required certificates and verify their domain. Talk them through these actions:

- 
**Create a Merchant ID (MID):** In the Apple Developer account, navigate to the "Merchant IDs" section and register a new Merchant ID with a description and identifier.

- 
**Generate a Certificate Signing Request (CSR):** Use an API client like Postman to send a request to the `applepay/signing-requests` endpoint. Save the content of the response into a `.csr` file.

- 
**Create the Payment Processing Certificate:** In the Apple Developer account, create a new certificate and upload the `.csr` file just created. Download the resulting `apple_pay.cer` file.

- 
**Prepare and Upload the Certificate:** Use an `openssl` command to Base64-encode the downloaded certificate file. Use a `curl` command to upload the encoded content to the `/applepay/certificates` endpoint.

- 
**Prepare and Verify the Domain:** In the Apple Developer account, add the domain(s). Download the domain verification file and host it on the server at the specified `/.well-known/` path.

- 
**Create the Merchant Identity Certificate:** Use `openssl` to generate a new CSR and private key (`.key`) file. Upload this new CSR to the "Apple Pay Merchant Identity Certificate" section of the developer account and download the resulting `merchant_id.cer` file. Convert this file to a `.pem` file using another `openssl` command.

            **Step 2. Implement the Frontend**          

The merchant must code their website to display the Apple Pay button and request an `ApplePaySession` when a user clicks it.
            **Step 3. Implement the Backend**          

The backend must be able to validate a merchant identity with Apple. It must also decrypt the payment token received from Apple or send it to Checkout.com to be converted into a card token (`tok_...`).
            **Step 4. Submit the Payment to Checkout.com**          

Using the decrypted Apple Pay token or the Checkout.com card token, submit the payment through the Payments API.

**Method 2: ******[Flow Setup](https://www.checkout.com/docs/payments/add-payment-methods/apple-pay/web)

This is a simplified process managed primarily through a Slack channel.
            **Step 1. Integrate the Flow Script**          

Integrate Flow into the website using the provided `npm` package or script.
            **Step 2. Initiate Onboarding in Slack**          

The request to enable Apple Pay is made in the `#applepay-onboarding` Slack channel. The pinned message contains detailed instructions.
            **Step 3. Provide Domain Verification File**          

- The merchant will be provided with the domain verification file.

- They must place this verification file on their server at the specified location (`/.well-known/...`) for both your sandbox and production domains.

            **Step 4. Confirm Onboarding**          

Once the merchant confirms the file is live on their domain, the team will complete the enablement process.

## RESOLUTION ⚒️

The expected result is a fully functional Apple Pay button on the merchant's website, capable of processing transactions securely.

- 
**Remediation Steps:**

  - For **API Only** errors, check the browser's developer console for specific error codes (e.g., 400, 417), which often point to incorrect file paths or a Merchant ID mismatch.

  - If an `sslv3 alert certificate expired` error appears, the certificate is no longer valid. The merchant must create new `.pem` and `.key` files by repeating the certificate creation steps.

- 
**How to Verify Resolution:** To confirm that the setup is complete and correct, the merchant must process a transaction. The status cannot be verified until a payment is made.

 

## ESCALATION** ⏫**

- 
**Flow Integration Issues:** For all onboarding requests and issues related to the Flow integration, use the `#applepay-onboarding` /`#ask-flow`Slack channel.

- 
**API Only Technical Issues:** For technical issues with the API Only setup (e.g., certificate validation, token decryption), escalate to the appropriate technical support Slack channel.

- 
**Follow-up:** Chase for updates in the relevant channel if no response is received within 24 hours.

            

         

## FAQs** ****❓**

What are the most common errors during an API Only setup?

The three most common errors are:

- 
**OpenSSL error... No such file or directory:** This indicates an incorrect file path to the .pem or .key file, a wrong passphrase, or an incorrect file format. Ensure the file path is correct and accessible on your server.

- 
**Payment Services Exception... statusCode: 417:** This means the Merchant ID (MID) in the certificate does not match the MID in the session request. The MID in your code must exactly match the identifier in your Apple Developer account.

- 
**Payment Services Exception... statusCode: 400:** This error also points to an incorrect file path for the .pem and/or .key files, indicating they are not accessible from your server.

How can I troubleshoot these errors?

Errors can often be found in your browser's developer tools, specifically the Network tab, when the payment is attempted. An error like "merchant validation failed" will appear as a failed network request, often with a status code like 417.What should I do if my SSL certificate has expired?

If you see an `sslv3 alert certificate expired` error, the certificate is no longer valid. You must create new `.pem` and `.key` files by following the certificate creation steps in the Apple Pay documentation.Can Apple Pay work on browsers other than Safari (e.g., Chrome)?

Yes, for **API Only** integrations, Apple has introduced a feature allowing payments on third-party browsers like Chrome. The user is presented with a QR code to scan with their iPhone, which then authorizes the payment via Face ID or Touch ID. However, Apple Pay via **Flow** is not yet officially supported on Chrome.
