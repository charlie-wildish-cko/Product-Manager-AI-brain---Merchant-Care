---
id: 27739097587858
section_id: 27616639185042
title: "What to do when a payout fails but the Merchant says it succeeded"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/27739097587858-What-to-do-when-a-payout-fails-but-the-Merchant-says-it-succeeded"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-31T17:08:12Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JYHD3VT0SMH2B173EZEKRH5D"]
label_names: ["payout", "card_payout", "payout_discrepancy"]
user_segment_ids: [11003606966930]
archive: false
---

**Use this article when:**

A merchant claims a card payout was successful (captured), but our system records show the transaction as declined or failed. 

Merchant care can investigate this mismatch by validating the merchant's claim against our system data and determining the correct escalation path.

## DESCRIBE THE ISSUE** 💬**

This article addresses situations where a merchant reports a discrepancy with a card payout. The merchant claims that a payout transaction was successfully captured, and their customer confirms that the funds were debited from their bank account.

However, when reviewing the transaction in our system (the PTC Dashboard) the status is recorded as "FAILED" or "DECLINED". 

 

## RESOURCES **📍**

| Tools | Case Examples | Related |
| --- | --- | --- |
| [PTC Dashboard](https://retoolprod.mgmt.ckotech.co/apps/62fcaf16-f4c4-11ed-a804-2bcf189b4b36/payouts/payout-search) [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277) | [65841](https://checkout1360.zendesk.com/agent/tickets/65841) | [Pay to Card Information Request](https://checkoutsupport.freshservice.com/support/catalog/items/277) |

 

## PROCESS FOR PAYOUT DISCREPANCIES: DECLINED VS. CAPTURED CLAIMS** **** 🖊️**

**Step 1. Confirm the Discrepancy**

- Verify the merchant's claim against our records

- 
**Action:** Match the transaction details provided by the merchant with the transaction record in the PTC Dashboard

- 
**Expected Result:** You should see the transaction status in our system as:

  - "FAILED" or "DECLINED"

**Step 2. Find Our Decline Reason**

It's important to understand why our system declined the payment

- 
**Action:** In the PTC Dashboard, find the specific decline code or reason associated with the transaction - note this down as it'll be needed for your investigation and any potential escalation

**Step 3. Request Proof of Debit**

To verify if funds actually left the cardholder's account, you must request evidence from the merchant

- 
**Action:** Ask the merchant to provide a copy of the cardholder’s bank statement that clearly shows the transaction date

💡**Tip:** Explain to the merchant that the bank statement is essential evidence that allows us to investigate the discrepancy with the Payout team.

 

**Step 4. Analyze the Bank Statement**

Once you receive the bank statement review it carefully

- 
**Action:** Check the statement for a debit entry that matches the transaction in question

**💡 Best Practice:** Always document your analysis of the bank statement in your ticket notes, including the date you received it and the result of your review.

## RESOLUTION **🛠️**

✅ Matching Debit Found

- If a **matching debit is found**, you'll need to escalate the case

**Action:** Escalate the case to the **Payout team**. You can do this via:

- 
**Slack:** Post in the `#ask-card-payouts` channel

- 
**Jira: **[Raise a ticket here](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277)

**Provide Information:** Include the following key details in your escalation request:

- The original claim from the merchant

- The decline reason from our system

- A copy of the cardholder's bank statement showing the debit

**Inform the Merchant:** Let the merchant know that you have escalated the issue for a deeper investigation and that you will update them once you hear back⛔ No Matching Debit Found

- If **no debit is found**, this confirms our system's record. Inform the merchant of your findings and close the ticket.

 

## FAQs** ❓**

 What do I do if the merchant cannot or will not provide the cardholder's bank statement?

The bank statement is essential evidence required to challenge our system's data. Without it, we cannot confirm a debit occurred. 

Politely explain to the merchant that without this proof, you must rely on the "declined" status recorded in our system, and you will have to close the investigation. 

 What does the Payout team do after I escalate a case?

The Payout team will conduct an in-depth investigation using the evidence you provided. They will diagnose the root cause (timing issue, reconciliation error, bank reporting anomaly, actual debit despite our decline) and provide a resolution or next stepsand provide a final resolution.
