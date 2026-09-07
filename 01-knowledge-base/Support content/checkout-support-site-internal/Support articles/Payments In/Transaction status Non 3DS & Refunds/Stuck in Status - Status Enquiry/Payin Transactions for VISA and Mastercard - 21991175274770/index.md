---
id: 21991175274770
section_id: 23045937114898
title: "Payin Transactions for VISA and Mastercard"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/21991175274770-Payin-Transactions-for-VISA-and-Mastercard"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-03-18T13:41:45Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQT889RQXXSG27BB4ZJ0M"]
label_names: ["case_transactions", "ROW", "case_transactions_issue_status_proof", "payin"]
user_segment_ids: [11003606966930]
archive: false
---

**Use this article when**

Checking the status of payin transactions for the Visa and Mastercard schemes. 

**Case type: **Payments in

**Issue Type: **Transaction status (Non 3DS & Refunds)

**Reason: **Stuck in status / status enquiry

## 

### PROCESS TO CHECK A PAYIN TRANSACTION FOR VISA OR MASTERCARD 🖊️

The merchant may have already provided the customer with an Acquirer Reference Number (ARN) / Retrieval Reference Number (RRN), but the customer has come back saying the bank cannot see the refund. Check if the ARN has been cleared by using the Checkout Agent Toolkit on Zendesk.

1. In the Zendesk ticket, go to **Apps**, and expand the **Checkout Agent Toolkit**

2. Click the relevant Payment ID to bring up the **Details** and **Timeline** view

3. 
Under Payment Details, you will find the ARN/RRN:-

4. Under **Timeline**, you will see the clearing status of the relevant payment:-

5. Outcomes:

  1. 
**Transaction (e.g. refund) has cleared**: Let the merchant know that the refund has been successful. You can also share the screenshot with the clearing status with the merchant. Proof can also be shared from the Visa or MC Portals

  2. 
**If the merchant continues to face issues with the refund: **They can share the refund ARN with the customer. Using this as a reference, they can contact the issuing bank and track the transaction from their side

  3. 
**Failed status or no results**: This means that clearing was not completed, and you may need to escalate to the Clearing team, so you need to find out why this was the case by escalating to the Clearing team through [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277),. Advise the merchant that we are escalating the issue. The Clearing team will come back with their investigation, and based on their response, further action may be needed 

 

## Glossaries and Definitions:

For **Key Terms and Definitions** on Transactions as well as an **introduction into MENA Gateway and non-Gateway merchants**, please see ****[Transactions Glossary](https://checkoutint.zendesk.com/hc/en-us/articles/21991201065106-Transactions-Glossary-Introduction)**.  **
 
 
 
 
 
 
 
 
 
For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Transactions articles, please see ****[Transactions Tools & Permissions](https://checkoutint.zendesk.com/hc/en-us/articles/21991176883474-Transactions-Tools-Permissions)**.**
