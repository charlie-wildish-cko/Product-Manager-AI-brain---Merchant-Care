---
id: 29508914445970
section_id: 26832912736274
title: "Visa/Mastercard Scheme Reject - Child Case Handling"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/29508914445970-Visa-Mastercard-Scheme-Reject-Child-Case-Handling"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-03-10T07:21:19Z"
permission_group_id: 26838654181266
content_tag_ids: ["01K5BG5AVFV17Q6RCVA9EHYKHQ", "01K5BG5EWMJVH9JYV5RA8A7SV6"]
label_names: ["scheme_reject", "scheme_decline", "clearing_reject", "blocked_transaction"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**   

To understand and resolve payment transactions that fail during the clearing phase. This article provides guidance on handling child cases generated from Visa/Mastercard scheme reject reports. 

**Problem: **Payment transactions appear successful to a merchant but are later rejected by the card scheme during the clearing phase.   

**Solution:** Manually create and handle child cases to inform merchants or their account managers about the failed transactions and outline necessary next steps.   

       

## INTRODUCTION TO THE ISSUE 💬

A "scheme reject" occurs when a payment network, like Visa or Mastercard, blocks a transaction during the **clearing phase**. 

This creates an information gap because merchants only see a "Capture" status, even if the transaction is later rejected by the payment scheme during the clearing phase. As a result, we must manually inform them of these failed transactions by sharing a report. 

These rejects fall into two categories:

- 
**Pre-clearing Reject:** Occurs before the clearing stage. This type of reject does not trigger a "Clearing failed event," meaning funds do not automatically move back to the merchant. Therefore, these transactions require manual adjustments.

- 
**Post-clearing Reject:** Occurs after the clearing process has begun. This rejection _does_ generate a "Clearing failed event," which automatically triggers the necessary fund adjustments, so no manual adjustments are required.

This article covers how to handle child cases of scheme reject parent case. (Parent case handling is described in Visa/Mastercard Scheme Reject - Parent case handling) 

## KEY TAKEAWAYS 🔑

- A scheme reject is a transaction blocked by a payment network during the clearing phase

- There are two types of scheme rejects: Pre-clearing and Post-clearing

  - Pre-clearing rejects require manual adjustments because a "Clearing failed event" is not triggered

  - Post-clearing rejects do not require manual adjustment as a "Clearing failed event" is automatically generated

- Since merchants do not receive automatic notifications for these rejects, we must manually share reports with them

## RESOURCES 📍

| Tools | Case Examples | Related |
| --- | --- | --- |
| - Zendesk search function  - Google spreadsheet | Zendesk ticket [72186](https://checkout1360.zendesk.com/agent/tickets/72186) Zendesk ticket  [49794](https://checkout1360.zendesk.com/agent/tickets/49794) Zendesk ticket [49781](https://checkout1360.zendesk.com/agent/tickets/49781) | [PROCESS Transactions rejected at scheme level](https://checkout.atlassian.net/wiki/spaces/PEO/pages/6525027718/PROCESS+Transactions+rejected+at+scheme+level) [PROCESS VISA Reject Response Code](https://checkout.atlassian.net/wiki/spaces/CNO/pages/5599986349/PROCESS+VISA+Reject+Response+Code) [PROCESS MC Reject Response Code](https://checkout.atlassian.net/wiki/spaces/CNO/pages/5599822496/PROCESS+MC+Reject+Response+Code) |

HANDLING A SCHEME REJECT REPORT 📁

Here's a breakdown of the process once we receive a scheme reject report from the Card Processing team:

1. We'll first **assign the case** and treat it as the **parent case**

2. Next, we'll **create a separate child case for each client** affected by the report

3. Once all the child cases are created, the parent case can be **resolved**

4. Each child case will then be placed in a specific queue, where it will be manually **handled by an agent** 

Essentially, we're taking one large issue (the parent case) and breaking it down into smaller, manageable tasks (child cases) so that each client's issue can be addressed efficiently by the right team.

## PROCESS FOR SCHEME REJECT RESOLUTION 🖊️

Step 1. Locate Merchant or AM/TAM Contact Information

Share the scheme reject report with either the merchants’ available contact or AM/TAM. 

- Attempt to locate the merchants’ contact details on the [contact person for scheme reject spreadsheet](https://docs.google.com/spreadsheets/d/1HWI9aqXvWJ4AHcA2BteR-otSXcn7bBsTiwYzp9VY2vs/edit?gid=0#gid=0)

- If the merchant's contact is not available, find the Account Manager's (AM) or Technical Account Manager's (TAM) email address by searching for the Client ID in Zendesk. 

Step 2. Send the Report

- Once you have the correct contact, share the scheme reject report with them via email or a Zendesk side conversation.

- Use the appropriate macro template for either "Scheme reject - to AM/TAM" or "Scheme reject - to Merchants" to ensure consistent and accurate communication.

## RESOLUTION ⚒️

- If a refund was rejected, the merchant will need to process the refund using an alternative method, like a bank transfer.

- 
If a capture was rejected, the merchant will need to find an alternative way to charge the customer, as the payment did not go through.
**Rollback/Recovery**

- The Finance team handles internal adjustments for post-clearing rejects. Transactions rejected at the pre-clearing level will not have a "presentmentfailed event," requiring a manual adjustment by the Payment team.               

## ESCALATION** ⏫**

If you require further clarification or have questions that are not addressed in this SOP, escalate the case by reaching out to the Card Processing (CP) team or Satoka.

FAQs** ****❓**          

 

Why do we need to manually share scheme reject reports?

Merchants only see a 'Capture' status for a transaction, even if it is later rejected by the payment scheme during the clearing phase. This creates a critical information gap that requires manual notification to the merchant.What is the difference between Pre-clearing and Post-clearing rejects?

Pre-clearing rejects happen before the clearing stage and do not trigger a 'Clearing failed event,' which means manual adjustments are needed. Post-clearing rejects occur after the clearing process has begun and automatically trigger a 'Clearing failed event,' so no manual adjustments are required.Do we need to raise an adjustment request to the Payment team?

No. The Card Processing team sends the scheme reject file to both the Merchant Care and Payment (Treasury) teams. The Payment team is responsible for making the necessary adjustments on their side.Why are some transactions rejected due to inactive BINs when the initial authorization was approved?

The clearing stage is when funds are moved from the issuer to the acquirer bank. A BIN can be inactive for a short or long period, and we do not have visibility on the exact range impacted. 

Blocking the authorization and capture attempt might prevent a transaction that would have been cleared by the scheme from going through. Our internal team is working with schemes to find a long-term solution.I noticed that some transactions are a year old. Why the delay?

We work with the schemes to reprocess clearing rejects until we receive a final confirmation that the clearing cannot be finalized. The delay is due to the process of attempting to clear the transaction multiple times over a period.Will these reports ever be automated?

The Card Processing Product and Engineering team is working on this issue, but no ETA has been provided. We will be notified when a solution, including potential automation, is available.
