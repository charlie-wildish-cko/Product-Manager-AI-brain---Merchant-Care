---
id: 28539218946450
section_id: 28632977066386
title: "Regenerating Historical Invoices"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/28539218946450-Regenerating-Historical-Invoices"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-12-19T10:34:07Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JVM5QASZ36B7JH2989V6FM6S"]
label_names: ["generic_invoice", "L2", "Troubleshooting guide", "FTS", "re-generate_historical_invoice"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

To regenerate invoices for a merchant needing to update company information on a previously issued invoice.

 

## INTRODUCTION 💬

This article outlines the process for re-generating a historical invoice when a customer's entity details, such as their business address, have been updated. Following this process ensures that the customer receives an accurate, updated invoice.

## KEY TAKEAWAYS 🔑

**Invoice Generator: **

On the **first working day of each month** (according to the UK working days schedule), the **Invoice Generator** will operate and create **one invoice for each entity and their respective holding currency**.

Details can be found at [Invoice Generation Process](https://checkout.atlassian.net/wiki/x/NYKdVAE)
 

## RESOURCES **📍**

Click here to see the tools you'll need 

| Tools | Access | Case Examples |
| --- | --- | --- |
| [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277) | - Access via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277)   - If you don't have access, please contact the IT team in the `#ask-it` Slack channel | [Zendesk case 36595](https://checkout1360.zendesk.com/agent/tickets/36595) |

 

 

## PROCESS FOR RE-GENERATING A HISTORICAL INVOICE 🖊️

## Step 1. Identify the entity and month(s) for invoice re-issuance

- Entities names

- Entity IDs

- The specific month(s) for the invoices that need to be re-issued

## Step 2. Create a Level 3 Support Ticket

You will need to escalate this request to the Level 3 (L3) team by creating a ticket

- Go to [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277)

- Complete all other mandatory fields

- Submit the ticket

## Step 3. Link the Jira ticket to the Zendesk Ticket

To ensure both support tickets are linked, add the new Jira ticket reference to the original Zendesk ticket.

- Open the Merchant's Zendesk ticket

- Click **Apply Macro**

- Select the following macros in order: **Transfer** → **Eng** → **FE(L3) th**is will automatically generate and link the internal ticket

The internal ticket will be generated as part of this process

## Step 4: Notify the Merchant

- Reply to the merchant to confirm that their request is being processed

- Inform them that you will provide an update as soon as the re-generated invoice is ready for them to download

- Once the L3 team confirms the task is complete, check that the updated invoice is available on **Dashboard** and the SFTP server (where available) and then send the final confirmation to the merchant

## ESCALATION** ⏫**

Sometimes, an invoice cannot be automatically re-generated.

**Scenario:** Invoices that were manually created by the Billing team (this is common for some gross-settled merchants)

**Action:** Escalate the request directly to the **Billing team**. The correct team depends on the entity's geographical location.  
  
  
 

💡 **Tip:** If you have questions or are unsure about the process, you can ask for help in the `**#ask-fex-clientreporting**` Slack channel.
 

## FAQs** ****❓**

 
Can I re-generate historical invoices for merchant when switching legal entities?  
 No. We cannot re-generate historical invoices when a merchant switches legal entities if the tax rates are different between the old and new entities. We cannot retroactively apply different taxes to a past billing period. In this situation, a manual tax adjustment must be made.  
  
This process is documented here: [Legal Entity Migration - Invoicing Process Agreement](https://checkout.atlassian.net/wiki/spaces/MER/pages/6088392974/Legal+Entity+Migration+Invoicing+Process+Agreement)  
Source: [#SR-359811](https://checkoutsupport.freshservice.com/a/tickets/359811?current_tab=details)
