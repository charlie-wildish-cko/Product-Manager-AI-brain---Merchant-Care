---
id: 22459222649618
section_id: 22459200587154
title: "Collections Process for Unmanaged Merchants"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22459222649618-Collections-Process-for-Unmanaged-Merchants"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-09-29T12:32:20Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JC18TX3J6QEHECZM3C62R3J1"]
label_names: ["collections", "unmanaged_merchants", "collections_process_for_unmanaged_merchants"]
user_segment_ids: [11003606966930]
archive: false
---

**Use this article when**

A merchant has a negative balance on their account. Follow the collections process to contact the merchant and reassign the case to the Collections Team if necessary.
INTRODUCTION TO COLLECTIONS 💬

**Collections** refers to the process used to recover money that is owed by merchants who have an outstanding (unpaid) negative balance. 

### KEY TAKEAWAYS 🔑

- All collections cases are subject to a **77-day SLA**

- The Care team's role is to initiate contact using a series of automated macros

- The **Collections form** must be used for all collections-related cases

- If a merchant responds reassign the case to the Collections team immediately

- If a merchant does not respond after 77 days the Care team's role concludes and the case is handed back to the Collections team

### PROCESS FOR UNMANAGED MERCHANT COLLECTIONS 🖊️

**Step 1. Receive and Assign the Case**

- A collections case will be created in Zendesk via an email from `collections@checkout.com`.

- The email will contain the merchant's balance, contact name, and email.

- Assign the case to yourself using the normal Zendesk procedure.

- Ensure the form on the case is set to **"Collections."** If it is not, change it from "Merchant Care" to "Collections."

**Step 2. Update Client Details**

- Change the case requester from `Alex Grimwood` to the merchant's email address provided by the Collections team

- If the merchant's email is not in Zendesk contact a team lead to add it

- Use the **Checkout Toolkit** app to find any additional client details if needed

**Step 3. Execute the Contact Strategy**

- Upon receiving the case, a **77-day SLA** begins

- Follow the contact strategy outlined in the table below. Use the provided macros in the **"Collections"** macro folder

- When using a macro replace `[xxxx]` with the negative balance amount (do not include the minus sign)

| **Day** | **Email Type** | **Action** |
| --- | --- | --- |
| **Day 1** | Negative Balance Reminder (10-30) | Send an initial reminder email to the merchant within 24hours of receiving the request (if possible) |
| **Day 14** | Negative Balance Reminder (10-30) | Resend the reminder email |
| **Day 28** | Negative Balance Past Due Email 1 (30-60) | Send the first past due email |
| **Day 42** | Negative Balance Past Due Email 1 (30-60) | Resend the first past due email |
| **Day 56** | Negative Balance Past Due Email 2 (60-90) | Send the second past due email |
| **Day 70** | Negative Balance Past Due Email 2 (60-90) | Resend the second past due email |
| **Day 77** | No email required to be sent to the Merchant | Send a notification to the Collections Team, confirming that the case has been handed back for their final action |

**Step 4. Manage Case Status and Follow-up**

- 
**If the merchant responds:** The case will re-open automatically. Immediately reassign the case to the Collections Team using the **"Reassign to Collections team"** macro.

- 
**If the merchant does NOT respond:** The case will auto-re-open every 14 days. Check the case history to determine which chaser email to send next. When sending a chaser macro, you **MUST** select the **"Waiting for Merchant after Chaser"** status. For all other instances of waiting for a reply, use **"Waiting on Requester."**

- 
**At Day 77:** If the merchant has not responded, the Care team's role is complete. Reassign the case to `Alex Grimwood` using the **"Reassign to Collections team"** macro. The case remains open for the Collections team to take further action.

ESCALATIONS ⬆️

- You cannot find the merchant's email address or other required details

- The merchant's account information appears incorrect in the system

- You are unable to correctly apply the Collections form or macros

**Required information to include:**

- A clear description of the issue

- Merchant name and ID

- The steps you have already taken

- Any error messages or unexpected behavior

**Instructions for the agent working the case:**

- Reassign the case to your Team Lead

- Add a clear note in the case explaining the issue

- Monitor the case for updates from the Team Lead

KEY TERMS 📖

| **Term** | **Definition** |
| --- | --- |
| **Negative Balance** | Occurs when a currency account lacks sufficient funds to cover applied fees and transactions such as MMB, refunds and chargebacks. |
| **Days Past Due (DPD)** | The number of days a merchant's balance has remained negative after falling below 0. The metric used by Collections to measure how long an account has been in arrears. |
| **Default** | Once a merchant is +90 days past due they are in Default of their obligations and internally will be reported as a loss. Though collections efforts will continue. |
