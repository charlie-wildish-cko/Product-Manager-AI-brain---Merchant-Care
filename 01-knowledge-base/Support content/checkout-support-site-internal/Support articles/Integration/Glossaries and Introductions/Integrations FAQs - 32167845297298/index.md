---
id: 32167845297298
section_id: 22197990418450
title: "Integrations FAQs"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/32167845297298-Integrations-FAQs"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-01-12T17:46:18Z"
permission_group_id: 26838654181266
content_tag_ids: []
label_names: []
user_segment_ids: [11003606966930]
archive: false
---

**Use this article when:**

You need answers for frequently asked questions about Hosted Payments, Payment Links, Postman API, Apple Pay, and CAT integration queries.

 

## Hosted Payments Pages (HPP) 🖥️

 What are the primary benefits of using Hosted Payment Pages (HPP)?

HPP provides a pre-built, mobile-responsive UI that auto-displays relevant payment methods based on customer location. It ensures secure compliance by requiring the lowest PCI level and featuring built-in 3D Secure 2.0.

 Can you customise the display name shown to customers on the HPP?

Yes, you can set a "display_name" parameter. This is particularly useful if your merchant has multiple processing channels and wants to mirror a specific brand name on the checkout page.

 How do you onboard a merchant for HPP?

First, you must create and configure the merchant's sandbox or production account in the Client Admin Tool (CAT). Once the profile is set, you use the Retool enablement app to onboard the Entity ID for HPP. Finally, the merchant can create an HPP session via API or SDK.

## 

## Payment Links (PL) 🔗

 What are the primary benefits of using Payment Links (PL)?

Payment Links are ideal for one-time payments and require no technical integration, as links can be generated in the Dashboard and sent via email or messaging apps.

 Can your customers use WhatsApp to receive Payment Links?

Yes, the secure portal allows you to share generated Payment Links directly via WhatsApp, email, or text message.

 How does the "max_attempts" parameter affect customer retries on HPP or PL?

This parameter constrains the number of retry attempts a customer can make if their initial transaction fails. The default value is 5 retries.

## 

## Postman API 🚀

 How do you configure variables in Postman to streamline your requests?

You can set up global or collection variables by clicking on the 'API reference' folder and navigating to the 'Variables' tab. This allows you to store and reuse values like API keys, Entity IDs, and Processing Channel IDs.

 How do you send a full card payment request using Postman?

Open the 'Payments' folder, select the 'Full card payment' request, and ensure your secret key is added to the 'Authorization' header with the 'Bearer' prefix. You must provide a JSON body containing the transaction details before clicking 'Send'.

 How do Postman scripts automate the tokenization process for you?

Certain requests contain scripts that automatically update collection variables, such as a token_id, based on the response of a previous request. This allows you to chain requests together without copying and pasting IDs manually.

## 

## Apple Pay 🍎

 What are the primary methods for onboarding a merchant for Apple Pay?

You can onboard a merchant either via the dedicated #applepay-onboarding Slack channel for a manual approach or by using the 'Enroll a domain to Apple Pay' service API for automated integration.

 What technical requirements must be met before enrolling a domain for Apple Pay via API?

You must ensure the merchant has added the vault:apme-enrollment scope to their access key pair and has placed the domain association file at the /.well-known/ path on their server.

 What is the recommended approach for onboarding non-technical merchants for Apple Pay?

The recommended approach is using the #applepay-onboarding Slack channel. You should provide the merchant with the domain verification file from the channel's pinned messages and ask them to upload it to their server at the /.well-known/apple-developer-merchantid-domain-association location.

 How do you verify a merchant's Apple Pay domain association file after they upload it?

Navigate to the merchant's domain plus the /.well-known/ path in your browser. The file should be available at that location as text or an automatic download to confirm the merchant has successfully hosted it.

 What details must you provide in the Slack channel to complete Apple Pay enrollment?

Once the domain association file is verified, post the merchant's Client ID (cli_), their site domain URL, and the specific environment (production or sandbox) into the Slack channel.

## 

## Client Admin Tool (CAT) 🛠️

 What is the Client Admin Tool (CAT) and what access level do you have?

CAT is a centralised platform for managing external client accounts. You have full configuration access for sandbox environments, but read-only access for production.

 How do you enable advanced services like Flow or Network Tokens for a client?

At the Client Level within CAT, you can navigate to the 'Services' section to enable functionalities such as Vault, Flow, Intelligent Acceptance, Network Tokens, and the Real-time Account Updater.

 How do you configure a new processing profile for a Card or APM in CAT?

Navigate to Processing - Processing Profiles and click 'Add processing profile'. Select the processor type (Card or APM) and appropriate acquirer. Use MCC 0742 by default and select 'Payin' for APMs and card schemes.

 What is the final step to ensure a new processing profile is active?

After creating the profile, you must add it to the processing channel via Gateway - Add profile processor. If setting up a Card processor, you must also add an authentication profile processor.

## 

## Google Pay 🤖

 Do you need to provide a Google Pay Merchant ID for HPP integrations?

No, a Google Pay Merchant ID is not required for HPP. If the field in the enablement tool is left empty, the merchant can still process Google Pay transactions because HPP uses our internal certificates.

 What information must you request from a merchant to onboard them for Google Pay with Flow?

You must ask for the merchant's Google merchant ID, which they can find in their Google Pay & Wallet Console. Once received, paste this ID into the Google Pay section of the Hosted Enablement Tool and update the merchant.

 How do you verify that a merchant has correctly configured their domain for Google Pay?

The merchant must confirm they have verified their domain within their Google Pay & Wallet Console, specifically in the 'Integrate with your website' subsection of the Google Pay API section.

## 

## Token Migration (Vault) 🔐

 What are the two main scenarios where you would perform a token migration?

You would typically handle token migrations during "Bulk Export" (moving tokens to another provider) or "Individual Export" scenarios, depending on the merchant's requirements.

 What documents must you have in place before you can begin a token migration?

You must ensure that the prerequisite documents, specifically the Attestation of Compliance (AOC) and the PGP key, are provided and verified before the migration starts.

 How do you securely transfer files during a token migration?

You should use an SFTP-based transfer method. It is recommended that you use a client like Filezilla to manage these transfers to the SFTP server.

 What is the approval process you must follow for a token export?

You must use the Retool "vault explorer" app to initiate the export. This requires multiple layers of authorisation, including approval from your line manager, the compliance team, and the infosec team.

 How long are uploaded token migration files stored on the FSTP server?

You should refer to the internal storage policy to determine the specific "stored time" for files on the FSTP server, as these are cleared periodically for security.

## 

## Troubleshooting 🛠️

 What should you investigate if a merchant receives a 401 error code when creating an HPP?

A 401 error typically indicates that the merchant is not yet onboarded or enabled for HPP. You should also check for API key mismatches between sandbox and production.

 What does a 422 "payment_method_not_allowed" error signify during HPP testing?

This often means the specific card scheme or payment method has not been enabled for that merchant in CAT or the HPP enablement tool.
