---
id: 32772122303122
section_id: 32772067326994
title: "How to Handle MCR Queries for Tiered Accounts"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/32772122303122-How-to-Handle-MCR-Queries-for-Tiered-Accounts"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-01-23T12:17:04Z"
permission_group_id: 26838654181266
content_tag_ids: ["01KFNCD9YG0HD37HD5M68H6WWP"]
label_names: ["Unmanaged_Merchants", "MCR"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

This article outlines the process for handling Merchant Change Requests (MCR) for tiered accounts, specifically determining when to involve an Account Manager (AM) versus escalating to the MCR team.

**Problem/Solution**

Tiered merchants request account changes, but the correct routing depends on whether the account is managed or unmanaged. Verify AM assignment in Salesforce or Zendesk; hand over managed accounts to the AM, and transfer unmanaged accounts to the MCR queue using the designated macro.

## DESCRIBE THE ISSUE 💬

Agents receive requests from merchants regarding account modifications (such as payouts, legal entities, or currencies). The agent must verify if an Account Manager is assigned to take ownership or if the request must be processed via the MCR queue.

 

## KEY TAKEAWAYS 🔑

- Tiered accounts are consistently allocated an Account Manager (AM) due to their revenue contribution.

- If Zendesk indicates no AM, verify in Salesforce under the account name.

- Managed accounts are handled by the AM; unmanaged accounts (typically Tier 3 or Tier 4) go to the MCR team.

- Always use the specific MCR Request > Unmanaged merchants macro for unmanaged transfers.

## PROCESS FOR HANDLING MCR QUERIES FOR TIERED ACCOUNTS 🖊️

This process outlines how to identify the account status and route the Merchant Change Request (MCR) to the correct department.
**Step 1. Verify Account Manager Assignment**

- Check the "Account Information" section in Salesforce or the respective field in Zendesk.

****

- The absence of an assigned Account Manager in these fields confirms the account is "unmanaged".

**Step 2. Handle Managed Accounts (AM Assigned)**

- If an AM is listed, tag the Account Manager in your Zendesk ticket.

- Provide a summary of the merchant's request and formally request their assistance in taking ownership of the inquiry.

- Once the AM acknowledges the request, mark the case as resolved.

**Step 3. Handle Unmanaged Accounts (No AM Assigned)**

- Requests from unmanaged merchants (usually Tier 3 or Tier 4) must be escalated to the MCR team.

- Select the **'MCR Macro - MCR Request - Unmanaged merchants'** in Zendesk.

- Include a concise summary detailing the change request within the transfer to the MCR queue.

## RESOLUTION ⚒️

- **Managed Accounts:** The Account Manager takes ownership of the correspondence and the support ticket is closed.

- **Unmanaged Accounts:** The ticket is successfully transferred to the MCR queue with a clear summary for processing.

## ESCALATION** ⏫**

- 
**Scenario:** Unmanaged merchant requesting account changes.

- 
**Macro:** MCR > MCR Request > Unmanaged merchants

- 
**Instruction:** Ensure a concise summary accompanies the submission.

 

## FAQs** ****❓**

How do I know if an account is unmanaged?

The absence of an assigned Account Manager (AM) in the respective field within Zendesk or Salesforce confirms the status as unmanaged.Which tiers are typically unmanaged?

Unmanaged merchants are typically designated as Tier 3 or Tier 4.
