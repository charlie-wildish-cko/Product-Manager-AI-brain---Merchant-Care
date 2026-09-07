---
id: 27822417036690
section_id: 27822398640530
title: "Authentication FAQs"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/27822417036690-Authentication-FAQs"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:34:11Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JZ88GPVA5D0SPHG3JNW36TE8"]
label_names: ["authentication", "SPA"]
user_segment_ids: [11003606966930]
archive: false
---

Use this article for frequently asked questions for online payment processing, including Google Pay transactions, liability shifts and recurring payments.

## 

## GENERAL AUTHENTICATION FAQs** ❓**

 Is it valid for a card issuer to challenge a recurring Merchant Initiated Transaction (MIT), and what can cause these transactions to be soft-declined?

Yes, it is reasonable for an issuing bank to challenge and decline a recurring MIT if the initial transaction in the series did not meet the necessary authentication requirements.

For a series of recurring MITs to be processed successfully, the very first transaction, known as the Cardholder Initiated Transaction (CIT), must have been a "challenged" transaction. This means the cardholder had to actively authenticate themselves (e.g., by entering a password or a one-time code).

A "frictionless" 3DS transaction on the initial CIT, where the customer's identity was verified in the background without a direct challenge, is not sufficient to establish the mandate for subsequent recurring MITs. This can lead to the issuer soft-declining the later MITs due to the lack of a strong initial customer authentication.

To resolve this, it is recommended to:

1. Review the referenced initial CIT to confirm that it was a fully challenged transaction.

2. If the initial CIT was not challenged, the merchant should be advised to re-initiate a new CIT with the customer, ensuring that the appropriate challenge indicator is set to establish a valid basis for future recurring payments.

 Can a card issuer challenge a recurring payment?

Yes, an issuer can decline a recurring MIT if the first payment in the series was not properly authenticated. The very first transaction, initiated by the cardholder (CIT), must have been "challenged," meaning the customer had to actively verify their identity (e.g., with a password). A "frictionless" initial transaction, where authentication happens in the background without a direct customer challenge, is not enough to validate future recurring payments.

If recurring payments are being soft-declined, you should:

- Check if the initial transaction was fully challenged.

- If not, have the customer make a new, challenged payment to authorize future recurring transactions.

 

 Why would a merchant lose a dispute on a recurring payment (MIT) even with a favorable ECI value?

For recurring payments, known as Merchant Initiated Transactions (MITs), the merchant usually holds the liability for disputes, meaning liability shift does not apply. 

An ECI (E-commerce Indicator) value of seven often indicates a successful authentication. However, specific payment network rules for MITs override general liability shift rules, so the merchant remains liable.

 

 

 

 

 How can I look into payment failures like "interceptor timeouts"?

When a high number of payments fail because of an "interceptor timeout," it usually means there is an issue with how the seller's website is handling the redirect to the security authentication page.

The best way to investigate this is to follow a two-step process:

1. 
 
**Get a high-level view with Looker:** Start by using the Looker reporting tool. This will help you understand the scale of the problem without needing to check individual transaction logs. You can filter the report to see a clear breakdown of why payments are failing, such as:

  - 
 
**Interceptor timeouts:** These often point to a problem with the seller's website setup.

  - 
 
**ACS timeouts:** The card issuer's security system timed out.

  - 
 
**Challenge request not received:** The request for a security challenge (like a code sent to a phone) was not received by the issuer's system.

This view can confirm how widespread the issue is (e.g., "48% of our payment failures are interceptor timeouts").

2. 
**Examine specific examples with Datadog:** Once Looker has confirmed the trend, you can use Datadog to "deep dive" into the logs of specific failed transactions to find the root cause. You should also ask the seller for more details about their setup, such as if they use a third-party service like
**IA (Intelligent Acceptance)** to manage their payment security, as this could be a factor.

 When should I use Looker and when should I use Datadog?

The tool you choose depends on what you are investigating, but using a combination of both is often the most effective method.

- 
 
**Use Looker for the "big picture":** Looker is best for analysing broad trends. Use it to answer general questions like, "Why are more payments being declined this month?" or "Why are so many payments timing out?". It helps you see the scope of a problem across thousands of transactions.

- 
 
**Use Datadog for the fine details:** Datadog is the right tool when you need to investigate the specific logs of a single payment to see exactly what went wrong. It provides granular details that you cannot get in Looker. It is also perfect for monitoring a seller's payments in real-time, for instance, when they are launching a new product.

A good workflow is to start in Looker to identify a trend, and then move to Datadog to examine specific examples and find the underlying cause.

 

### 

 

 Why does the same payment card sometimes get a text message code and other times a banking app approval?

The type of security check a cardholder receives is decided entirely by the company that issued the card (e.g., their bank) and its **ACS (Access Control Server)**, which is the system that manages these security checks.

The **PSP (Payment Service Provider)** has no control or influence over the method chosen.

The card issuer's systems decide which authentication methods they support (such as a one-time password via text message or an approval in a banking app) and which one to use for any given transaction. 

This decision is based on their own internal rules and risk assessment. Some issuers may even give the cardholder a choice of which method to use on the challenge page itself.

 

### 

## 

What causes "Content Security Policy (CSP)" errors during the payment authentication step?

These errors typically happen when a seller chooses to display the payment authentication page within an

**iFrame** (an inline frame that embeds one webpage within another) on their own checkout page.

The seller's own website security rules, known as a **CSP (Content Security Policy)** or **CORS (Cross-Origin Resource Sharing)**, may block our authentication page from loading correctly inside their iFrame. The situation can become even more complex if our authentication page then needs to open _another_ iFrame to show the bank's security challenge page, creating a "nested" iFrame, which often leads to security conflicts.

It is the **seller's responsibility** to fix these errors. They must update their website's Content Security Policy to allow content from the necessary payment domains to be displayed properly.

## 

Can sellers control the customer experience during payment authentication?

Yes, sellers have full control over how they handle the redirect to the authentication page. The customer's experience will depend on which of the two main integration methods they choose:

- 
 
**iFrame Integration:** The seller can show the authentication page in a window embedded directly on their checkout page. This keeps the customer on the seller's website for a seamless experience.

- 
 
**Full Page Redirect:** The seller can redirect the customer away from their site to a separate, full-screen authentication page. This approach often avoids the technical CSP and iFrame-related errors mentioned previously.

The choice between these two methods is entirely up to the seller and how they wish to design their customer's checkout journey.

## 

What’s the difference between integrated and standalone authentication?The core difference lies in who owns the orchestration of the authentication and payment flow. With integrated authentication, Checkout.com takes care of everything-the merchant simply submits a payment session request and Checkout handles 3DS and payment processing.  Standalone, gives merchants full control to run the 3DS flow themselves using Checkout’s authentication capabilities and options to send the final payment to any PSP or acquirer. Standalone is often chosen by merchants who want more orchestration control or need to authenticate with Checkout.com but acquire elsewhere.

**Key distinctions:**

| **Feature** | **Integrated** | **Standalone** |
| --- | --- | --- |
| Authentication Ownership | Checkout.com | Merchant |
| Payment Processing | Tied to Checkout’s gateway | Any PSP or gateway |
| Endpoint | /sessions/internal | /sessions |
| Front-end Flow | Must be hosted via interceptor | Hosted or non-hosted |
| Use Case | Simpler flows, full Checkout use | Complex orchestration, PSP flexibility |

  
 

 What are hosted and non-hosted authentication flows?

In the standalone model, merchants can choose how to implement the front-end of 3DS. 

**Hosted flows**** **use Checkout.com’s interceptor, a managed user interface that handles everything from device data collection to challenge presentation. This is the easier option. 

**Non-hosted** gives the merchant full control over the front-end, including UI, challenge screen and data collection- but also comes with more complexity.

Whilst both options are available for standalone flows, integrated authentication is always hosted.

**Comparison Table:**

| **Area** | **Hosted** | **Non-Hosted** |
| --- | --- | --- |
| **UI Implementation** | **Checkout.com** | **Merchant** |
| --- | --- | --- |
| **Redirect Required** | **Yes (to interceptor)** | **No** |
| --- | --- | --- |
| **3DS Challenge UI** | **Provided by Checkout** | **Handled by merchant** |
| --- | --- | --- |
| **Device Data Collection** | **Automatic via interceptor** | **Manual via ****PUT /collect-data ****Or provided in the initial Sessions request.** |
| --- | --- | --- |

 When should I use standalone authentication?

Use standalone authentication when you need flexibility, regional coverage, or multi-PSP orchestration. It separates authentication from acquiring, allowing you to authenticate a transaction via Checkout.com and then send it to a different PSP or acquirer.

This is particularly useful in regions where Checkout doesn’t yet support acquiring, but can still provide strong 3DS authentication. 

**Reasons to choose standalone:**

- You need to **authenticate with Checkout but acquire elsewhere**

- You want to **optimize routing logic** (e.g. based on success rates or cost)

- You're a **global merchant** operating in markets outside Checkout’s acquiring footprint

- You require **fine-grained control** over the front-end experience and session timing.  
 

## 

Can I authenticate with Checkout.com even if it doesn't support acquiring in my region?Yes. Checkout.com’s authentication services are not geographically restricted in the same way acquiring services are. You can use Checkout’s 3DS capabilities worldwide, even in regions where it doesn’t offer payment acquiring.
This setup is possible because authentication is decoupled from the acquiring layer in standalone integrations.
  
Example Scenario: A merchant in Mexico, authenticates with Checkout.com (standalone flow), acquires payment through a local PSP (Clip, Conekta).  
 

## 

 What are the implementation differences between hosted and non-hosted flows?Non-hosted implementation gives merchants full control over the front-end, but it also requires handling several technical responsibilities that Checkout normally manages in hosted flows. These include 3DS Method handling and challenge presentation.Session expiry is more common in non-hosted flows—especially when merchants forget to send device/browser data or fail to implement the challenge flow properly.**Key Implementation Tasks:**

| **Task** | **Hosted** | **Non-Hosted** |
| --- | --- | --- |
| Device data collection | Automatically handled | Must call PUT /sessions/{id}/collect-data (Device data can alternatively be submitted in the initial Sessions request) |
| Challenge UI rendering | Done by interceptor | Must build your own UI |
| Handling 3DS Method | Included | Merchant responsibility |
| Analytics/telemetry logs | Provided | Must implement manually |

  
 

## 

 How can I tell which authentication model is being used in logs?Logs provide several indicators that help you distinguish between authentication types. **Log-Based Identification:**

| **Signal** | **Integrated** | **Standalone** |
| --- | --- | --- |
| Endpoint | /sessions/internal | /sessions |
| sessionSource field | gateway | merchant |
| Interceptor (hosted) logs | Always present | Present only in hosted standalone, Or if merchant utilizes our challenge-notification endpoint |
| Frontend activity logs | Redirects, challenge events | Missing in non-hosted |

**Pro Tip:**

- In integrated flows, you’ll always see a redirect to the interceptor

- In non-hosted standalone flows, you won’t see any interceptor logs at all  
  
  
 

## 

 Why might a standalone session expire?One common issue is failing to submit device/browser data via PUT /sessions/{id}/collect-data. If this doesn’t happen, the session expires due to lack of information needed for risk scoring and authentication routing.**Causes of Expiry:**

- No device data submitted

- Timeout between session creation and authentication start

- Incorrect sequencing of 3DS Method and challenge  
  
 

## 

 How can I detect if a user used their banking app?There’s no direct API indicator showing that a user opened their banking app, but log events can provide clues. For example, when a user switches tabs or minimizes the browser during authentication, the front-end logs a visibilitychange event.This is often seen in Out-of-Band (OOB) flows, where the user is redirected or prompted to take action in their banking app. However, it’s not conclusive proof—users may switch tabs for unrelated reasons.
**Example log line:**
CSS
CopyEdit
3DS visibility: hidden
This typically appears in the hosted interceptor logs  
 
 
 
  
 

## 

 Can I authenticate with Checkout and then use another PSP?Yes. This is a key strength of standalone authentication. It allows you to authenticate securely with Checkout.com and then route the transaction to any PSP of your choice.  
Many enterprise merchants use this to implement routing logic, failover protection, or regional acquirer strategies.**Benefits:**Full flexibility in routingUse Checkout’s authentication strength even where it doesn't acquireSeamless fallback in case of gateway issues 

## 

 How can I detect the authentication type (OTP, OOB, etc.)?Authentication type (e.g. whether a user received a one time passcode OTP or used their banking app) is **not included in the ****authentication requisition (****ARes**) but is available in the respective response (**RReq)** message. It can be present in the ARes if the authentication was challenged i.e. transStatus ”C”Look for the field that indicates authenticationType in the RReq to reliably determine the method used.
**Common Values:**

- 
01 – Static (rare)

- 
02 – One-Time Password (OTP)

- 
03 – Out-of-Band (OOB, e.g., banking app approval)  
 

**💡****Important: **ARes does not reliably contain this data, always refer to RReq for post-authentication details.  
 

## 

 

## GOOGLE PAY AUTHENTICATION FAQs** ❓**

 What are the different types of markings for Google Pay transactions and what do they mean?Google Pay transactions have markings that show how they were authenticated:

- 
**Google SPA Approved:** "SPA" stands for Secure Payment Application. This means the transaction was authenticated directly in the browser using the customer's saved Google Pay details. This can occur even if the customer doesn't explicitly choose "Google Pay" during checkout.

- 
**3DS Approved:** This shows the transaction was secured using 3D Secure (3DS). 3DS adds an extra security step, usually requiring customers to enter a password or a one-time code from their bank.

- 
**Unmarked:** A transaction without a specific marking is typically a standard payment from the Google Pay app or wallet that did not use the 3DS authentication process.

 Can a customer choose not to use Google SPA for authentication?Yes. When prompted to use Google SPA, a customer can select an option like "verify another way" to opt out. 
If the Google SPA authentication fails or is bypassed, the system will "fall back" to the standard 3D Secure (3DS) method to complete the authentication. A "3DS approved" marking could mean an initial Google SPA attempt was bypassed before being authenticated through 3DS.
 
   

## APPLE PAY AUTHENTICATION FAQs **❓**

 For Apple Pay recurring payments (MITs), what determines liability shift?For Apple Pay MITs, the presence of a cryptogram is more critical than the ECI value in determining liability shift.

- 
**Cryptogram:** This is a unique, encrypted code generated by the customer's device for each transaction. A cryptogram must be included in the transaction authorization to be considered for liability shift.

- 
**ECI (E-commerce Indicator):** This value only reflects the authentication outcome and does not determine liability on its own.

To confirm if liability shift is possible for an Apple Pay transaction, you must verify that a cryptogram was used during authorization.
 
 
 
  

##
