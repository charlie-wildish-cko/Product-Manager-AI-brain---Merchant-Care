---
id: 28894403296914
section_id: 26884699273746
title: "Swish Beta Launch"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/28894403296914-Swish-Beta-Launch"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-09-12T09:48:26Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JVW5V7B7TZ05VVPPCG5ZEHCF", "01K33N4AVEGT8WSHHXQPPMT2Z0"]
label_names: ["swish"]
user_segment_ids: [11003606966930]
archive: false
---

Here you'll find information about the beta launch of Swish
**OVERVIEW OF SWISH**** 👀**

**SWISH** is an app-based payment method in Sweden that allows consumers to pay online, in store and exchange money with friends. The app is easily usable by consumers, where they simply join using their mobile numbers and connect their bank accounts for payments. You can view [payment request details here.](https://checkout.atlassian.net/wiki/spaces/APM/pages/6813254096/Swish+-+Payment+Request)

## [🔗 Swish Training Video](https://drive.google.com/file/d/1VbofYBAhW7MaqHU0F1I6mZhCC-ORztHd/view?usp=sharing)

 Click for further details 

| Status | Beta |
| --- | --- |
| Release Date | 1 Sept 2025 |
| Expected Go Live | 25 Oct 2025 |
| Owner(s) | @Abhishek M |
| Support Channel | #apm-support-internal (For L2/L3 support) #ask-apms (For general merchant query) |

 

**FAQs ❓**How does Swish work?

- **In-store:** Customers enter the store’s Swish number and amount in the app, then confirm with BankID. QR code payments are also supported.

- **Online:** Customers select Swish at checkout, enter their phone number, and authorise the payment in the app with BankID.

 What is the payment flow for Swish?

- This is the payment flow for Swish:

- 
**Customer selects Swish** at checkout.

- **Merchant creates a payment request** with required details (amount, currency, account holder, etc.).

- The request is routed through CKO, APM, and PPRO to Swish.

- **Customer is redirected** to the Swish app (via app intent, QR code, or link) to authorise the payment.

- **After payment**, the customer is redirected back to the merchant’s site/app.

- **Status updates** (pending, captured, declined) are communicated back to the merchant via webhooks.

 What are the available entities for new merchants?Austria, Belgium, Denmark, Czech Republic, Germany, Estonia, Finland, Spain, France, Greece, Hungary, Italy, Lithuania, Latvia, Netherlands, Norway, Poland, Portugal, Switzerland, Sweden, United Kingdom

 

**ESCALATION 🔺**

- First line escalation- Product Manager - @Abhishek M

- 
For partner related queries related to Beta - Please liaise with the APM Product team

  - #apm-support-internal (For L2/L3 support)

  - #ask-apms (For general merchant query)
