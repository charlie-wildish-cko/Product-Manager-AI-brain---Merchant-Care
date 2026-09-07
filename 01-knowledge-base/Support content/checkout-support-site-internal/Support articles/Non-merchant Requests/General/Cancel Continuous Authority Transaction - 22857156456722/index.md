---
id: 22857156456722
section_id: 28544539846802
title: "Cancel Continuous Authority Transaction"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22857156456722-Cancel-Continuous-Authority-Transaction"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-11-16T08:59:19Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRS13HJX19Z5T3VSS7TJF7"]
label_names: ["global", "case_non-merchant_requests", "case_nmr_issue_issuing_bank_requests", "cancellation_of_continuous_authority_transaction"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

If an issuing bank contacts Merchant Care requesting that a merchant revoke all future charges for a specific cardholder due to an account issue (non-fraudulent).INTRODUCTION 💬 

A continuous payment authority (CPA), also known as a recurring card payment, is an agreement where a customer gives a company permission to regularly take money from their debit or credit card. 

The issue arises when an issuing bank contacts Merchant Care to enforce a mandate, often referred to as a "Future Charge Revocation" or "Cease Future Billing," for a cardholder. The request is for the merchant to ensure no future charges are processed for the card number provided, typically involving a payment processing or subscription service product.

⚠️ It is crucial to understand that this is a non-fraudulent mandate. 

It is a direct instruction from the card-issuing institution to prevent future financial activity, possibly due to a lost/stolen card or other account issues, but not classified as a fraudulent transaction requiring a chargeback or refund process. The agent's role is to facilitate the communication of this critical instruction to the merchant.

****KEY TAKEAWAYS 🔑

- This process is for **non-fraudulent** future charge revocation requests from an issuing bank.

- The initial step involves locating the relevant transaction using the **Acquirer Reference Number (ARN)** in the designated internal tool.

- The merchant or Account Manager (AM) must be notified immediately via a side conversation, including all transaction and card details.

- Once the merchant is notified, Merchant Care's action is complete; the merchant is responsible for implementation and any direct cardholder communication.

 PROCESS FOR FUTURE CHARGE REVOCATION MANDATE 🖊️

This process requires a combination of standard checks and data compilation to ensure the merchant receives the correct, actionable information. 

### **Step 1. Locate the Cardholder's Transaction Details**

- Use the **ARN** provided by the issuing bank to search for the original transaction in the [Payin Event Looker](https://checkoutinternal.eu.looker.com/explore/payment_lifecycle/fct_payin_event?toggle=fil&qid=3cjXIbJlvPlgXvNyFlsRgX)

- **Adjust the search criteria**, such as the event date, to ensure it matches the transaction date.

### **Step 2. Compile Necessary Transaction Data**

Gather the required fields, ensuring they are compiled clearly for the merchant/AM:

- Event Date

- Entity Name

- Entity ID

- Payment ID

- Reference

- Acquirer Reference Number (ARN)

- Masked Card Number

- Amount

### **Step 3. Initiate Communication with the Merchant/Account Manager (AM)**

- Open a **side conversation** on the existing support ticket directed to the Merchant or the assigned Account Manager.

- **Include all the data compiled in Step 2**.

- **Append the original communication from the issuing bank** using the "insert ticket comments" feature to provide full context.

### **Step 4. Notify the Issuing Bank and Resolve Case**

- Reply to the issuing bank's communication to confirm the merchant has been successfully notified of the required charge revocation.

**⚠️ Note:** The merchant is now responsible for preventing future charges and must liaise directly with the cardholder if necessary.

- **Resolve the case** in the case management system.
WHAT TO TELL THE MERCHANT 🗣️

 

- **Initial Notification:** "We have received a direct mandate from the card-issuing bank regarding a cardholder associated with your account. They are requesting an immediate revocation of all future recurring charges for this card number."

- **Actionable Instruction:** "Please treat this as a mandatory instruction from the card issuer. Your team must implement the necessary steps to prevent any future billing for the card details provided: [Insert relevant data from Step 2]."

- **Final Accountability:** "Your company is responsible for implementing this action and handling any necessary direct communication with the cardholder."
