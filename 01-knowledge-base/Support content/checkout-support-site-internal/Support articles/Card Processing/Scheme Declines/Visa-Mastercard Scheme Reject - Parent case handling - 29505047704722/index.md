---
id: 29505047704722
section_id: 26832912736274
title: "Visa/Mastercard Scheme Reject - Parent case handling"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/29505047704722-Visa-Mastercard-Scheme-Reject-Parent-case-handling"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-03-10T07:21:34Z"
permission_group_id: 26838654181266
content_tag_ids: ["01K5BG5AVFV17Q6RCVA9EHYKHQ", "01K5BG5EWMJVH9JYV5RA8A7SV6"]
label_names: ["scheme_declines", "scheme_reject", "scheme_decline", "clearing_reject"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

This article explains how to handle a Visa/Mastercard scheme reject report by creating and managing parent and child support tickets. 

**Problem:** Merchants are not automatically notified when transactions are rejected at the clearing stage.

**Solution:** Manually create and manage support tickets to inform clients of scheme rejects and ensure proper internal handling.

## INTRODUCTION TO THE ISSUE 💬

A "scheme reject" occurs when a transaction is blocked by a payment network like Visa or Mastercard during the clearing phase. This creates a critical information gap for merchants, as their transaction status remains "Capture" even after the rejection, leaving them unaware of the failure. To close this gap, we must manually share a report with each affected client.

These rejects fall into two categories:

- 
**Pre-clearing Reject:** Occurs before the clearing stage. This type of reject does not trigger a "Clearing failed event," meaning funds do not automatically move back to the merchant. Therefore, these transactions require manual adjustments.

- 
**Post-clearing Reject:** Occurs after the clearing process has begun. This rejection _does_ generate a "Clearing failed event," which automatically triggers the necessary fund adjustments, so no manual adjustments are required.

The audience for this SOP is agents who receive and process these scheme reject reports. The product is the transaction processing system, and the topic is managing scheme rejects.

For process, first we receive scheme reject report from the Card Processing team, which include multiple clients. In order to divide the list per client and share it with them separately, we use 'Rejection Processing Hub' automation, configured by the OE team (Joel), which creates child cases per client. 

 

## KEY TAKEAWAYS 🔑

- A scheme reject is a transaction rejection that occurs during the clearing phase

- Merchants are not automatically notified of these rejects, requiring manual communication

- Parent cases are sent from CP team, with rejected transaction list including multiple clients

- Pre-clearing rejects require manual adjustments, whereas post-clearing rejects do not

- The Payment (Treasury) team is responsible for making manual adjustments

HANDLING A SCHEME REJECT REPORT 📁

Here's a breakdown of the process once we receive a scheme reject report from the Card Processing team:

1. We'll first **assign the case** and treat it as the **parent case**

2. Next, we'll **create a separate child case for each client**

3. Once all the child cases are created, the parent case can be **resolved**

4. Each child case will then be placed in a specific queue, where it will be manually **handled by an agent** 

Essentially, we're taking one large issue (the parent case) and breaking it down into smaller, manageable tasks (child cases) so that each client's issue can be addressed efficiently by the right team.

## PROCESS FOR PARENT CASE HANDLING 🖊️

**Entry point: receive scheme reject report from the Card Processing team**

**Step 1. Prepare the Parent Case and Google Sheet**

⚠️ Once you receive the scheme reject report (the parent case) from the Card Processing (CP) team, immediately duplicate the attached Google Sheet. This copy will serve as your "master list" to avoid modifying the original file.

**Step 2. Create Child Cases for Each Client**

You can create child cases in bulk by using '[Rejection Processing Hub](https://docs.google.com/spreadsheets/d/1dTeQh_CdO2eqpaie73M8jQ765gL7TcBR0dv5yCgQuRc/edit?gid=550207786#gid=550207786)'. (Instructions are stored in 'Landing Page' sheet.)  

**Step 3. Check if the created child cases are in the dedicated queue **

It would be recommended to check child cases in each queue to see if the automation works as expected. 

 

## RESOLUTION ⚒️

Successfully following these steps results in the correct sharing of scheme reject information with Account Managers (AMs) and merchants. 

By breaking down one large parent case into smaller, client-specific child cases, you ensure that each issue is handled efficiently by the appropriate team, regardless of the report's volume. 

The process is completed when a child ticket has been created for every client on the report, and the parent case is closed.

 

## ESCALATION** ⏫**

If you have questions or need clarification regarding the scheme reject itself, contact the CP (Card Processing) team. 

Regarding automation, contact Joel in OE team. 

## RESOURCES 📍

| Tools | Case Examples | Related Articles |
| --- | --- | --- |
| - Zendesk search function  - Google spreadsheet | [Zendesk ticket 72186](https://checkout1360.zendesk.com/agent/tickets/72186) [Zendesk ticket 65623](https://checkout1360.zendesk.com/agent/tickets/65623) [Zendesk ticket 110705](https://checkout1360.zendesk.com/agent/tickets/110705) | [Transactions rejected at scheme level](https://checkout.atlassian.net/wiki/spaces/PEO/pages/6525027718/PROCESS+Transactions+rejected+at+scheme+level) |

 

## FAQs** ****❓**

Why do we need to manually create tickets and share reports?

Merchants are not automatically informed when a transaction is rejected at the clearing stage, as the status remains "Capture." We must manually share a report to ensure they are aware of the failed transactions.Why doesn't Merchant Care raise adjustment requests?

The Card Processing team sends the scheme reject file to both the Merchant Care and Payment (Treasury) teams. The Payment team is responsible for making any necessary adjustments on their end, so the Merchant Care team does not need to raise a separate request.Where can I find other FAQs from merchants?

FAQs from merchants and account managers are stored in the article titled "Scheme reject - child case handling".
