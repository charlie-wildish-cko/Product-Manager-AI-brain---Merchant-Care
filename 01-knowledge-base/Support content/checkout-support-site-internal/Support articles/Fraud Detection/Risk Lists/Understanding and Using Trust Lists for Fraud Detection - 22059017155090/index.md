---
id: 22059017155090
section_id: 22044818478354
title: "Understanding and Using Trust Lists for Fraud Detection"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22059017155090-Understanding-and-Using-Trust-Lists-for-Fraud-Detection"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-15T16:45:08Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRPZZM25CJTKMYW0WZXMXX"]
label_names: ["global", "lists", "risk_rules", "case_fraud_issue_decline_list_risk_rules", "trust_lists", "case_fraud_detection", "bypass_risk_rules"]
user_segment_ids: [11003606966930]
archive: false
---

**Use this article when**

Supporting a merchant who is experiencing issues when trying to add or edit entries in Trust List - which are part of the risk strategy rules.INTRODUCTION TO TRUST LISTS 💬

Trust Lists are used to bypass a merchant's risk strategy. Trust Lists are a powerful tool, but it's crucial to understand their limitations, especially regarding global risk assessments. Merchants can add the following types of entries to their trust list:

- Email addresses

- Email domains

- Payment IPs

Users may encounter issues when trying to add or edit entries in a merchant's Trust Lists. This can happen due to:

- A lack of proper permissions - see the related [user permissions](https://www.checkout.com/docs/business-operations/use-the-dashboard/manage-users/user-permissions) article

- If a payment was declined despite an entry being on a Trust List, it was likely due to a global Checkout.com's policy

- If a user is having trouble adding an entry, confirm they have the correct permissions

⚠️ Only owners, risk managers and admins can edit lists, including adding or removing entries.

## PROCESS STEPS 🖊️

**Step 1. Check User Permissions**

The most common reason a user can't edit a list is a permissions issue. Confirm the user has one of the required roles: 

- **Owner**

- **Risk Manager**

- **Admin**

If not, advise them to contact an admin to have their permissions updated

**Step 2. Confirm the List Type**

Trust Lists are collections of custom values that can be used in rules, they can contain the following types of entries:

- Email addresses

- Email domains

- Payment IPs

**Step 3. Explain Trust List Functionality**

Explain to the user that Trust Lists will override a merchant's risk strategy if a payment attribute matches a value in the list.

**Step 4. Address Potential Conflicts**

Clarify that Trust Lists do **not** override **Checkout.com's global risk assessment**. A payment may still be declined even if it is on a merchant's Trust List. 

Also, note that while a Trust List entry will bypass **velocity rules**, it will not bypass rules set at the client level.ESCALATIONS ⬆️

If the user has the correct permissions and the issue persists, escalate the case to the **Risk Operations team** with the following information:

- User's name and email

- The merchant's name

- The specific list they are trying to edit

- A screenshot or detailed description of the error message they are receiving

FAQs ⁉️

**Q: Why was a payment declined even though the email was on my Trust List?** A: Trust Lists can't override **global CKO risk policies**. The payment was likely declined due to a global assessment.

**Q: Can a user with a **`**Viewer**`** role edit a Trust List?** A: No, only **Owners**, **Risk Managers**, and **Admins** have the necessary permissions to edit lists.

**Q: Do Trust Lists bypass all risk rules?** A: No. They bypass the merchant's risk strategy and velocity rules but **do not** bypass rules set at the client level or CKO's global risk assessment.RESOURCES 📍

| Related Articles |
| --- |
| External Merchant facing Content   - [Create risk rules and lists](https://www.checkout.com/docs/business-operations/prevent-fraud/create-risk-rules-and-lists)  - [User Permissions](https://www.checkout.com/docs/business-operations/use-the-dashboard/manage-users/user-permissions) |
