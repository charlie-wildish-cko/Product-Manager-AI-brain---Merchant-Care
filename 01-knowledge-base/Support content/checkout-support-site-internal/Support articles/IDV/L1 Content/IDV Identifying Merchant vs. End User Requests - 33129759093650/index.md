---
id: 33129759093650
section_id: 32304308299922
title: "IDV: Identifying Merchant vs. End User Requests"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/33129759093650-IDV-Identifying-Merchant-vs-End-User-Requests"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-02-10T10:52:54Z"
permission_group_id: 26838654181266
content_tag_ids: ["01KE6V773EPR1K1MSSMYWHJ6T4"]
label_names: ["IDV"]
user_segment_ids: [11003606966930]
archive: false
---

**Use this article **

To help you understand when an IDV ticket has been raised by the merchant or the end user/customer.

When you work IDV cases you'll get emails from two very different groups of people. It is important to know who is who so we can give them the right kind of help.

- **Merchants** are the companies that use our IDV product to send to customers to verify their identity.

- **End Users** are the individual people using our IDV app through those companies.

 

### **Guide to Common Customer Service Requester Types 👀**

  
_This guide outlines the most frequent ticket categories and how to handle them effectively._

 

| Merchant 🏢### | End-User 👨🏻‍💼### |
| --- | --- |
| **Merchant: DocuSign**   These are complex tickets due to their multi-layered internal infrastructure.   -  **The UUID Trap:** DocuSign often provides their **internal UUIDs**. **We cannot use these to look up sessions in our system.**   -  **Technical Noise:** They frequently report internal DocuSign errors as "CKO-IDV" issues. Whenever there is an issue to validate a "signer" but the idv is valid, this is a sign to proceed on the ticket with extra care as the issue might not be on CKO-IDV side. | **End-Users (Uber Drivers)**   These tickets typically come from individual drivers rather than a merchant contact.   -  **The Signal:** Usually sent from personal email addresses. Users rarely provide a UUID and often report being "blocked" during identity verification.  -  **The Watch-out:** **Do not misclassify these as Data Privacy requests.** While both come from end-users, Data Privacy requests need to be escalated but all other End-user queries can be answered directly. |
| **Merchant: a3bc**   A  merchant focused on government-level security standards.  -  **Core Issues:** Frequent reports regarding **extraction failures** (OCR issues) and **fraudulent user flags**. |  |
| **Merchant: Yousign**   A competitor to DocuSign in the e-signature space. No specific alerts. |  |

 
Merchant Requests🏢Merchants like DocuSign, Treezor, A3BC manage multiple users and contact us regarding platform configurations, or technical errors.

### Key Indicators:

- **Email Address:** Usually a professional domain (e.g., `@docusign.com`, `@treezor.com`, `@a3bc.io`).

- **Language:** Professional, technical, and often includes specific IDs or document model numbers.

- **Request Type:** Feature or configuration requests, technical investigations, request to update a customer name.

  The End User (The Customer) 👨🏻‍💼An End User is a single person (like an Uber Eats driver) trying to prove who they are. They just want to use IDV so they can verify their identity and start work or use an app.

- **The Email:** They use personal addresses (like `@gmail.com` or `@icloud.com`).

- **The Request:** They are usually stuck. They need a new link because theirs expired, or they want to know why they haven't been "passed" yet.

- **The Language:** They use "I" and "Me" and they might sound worried or in a hurry.
