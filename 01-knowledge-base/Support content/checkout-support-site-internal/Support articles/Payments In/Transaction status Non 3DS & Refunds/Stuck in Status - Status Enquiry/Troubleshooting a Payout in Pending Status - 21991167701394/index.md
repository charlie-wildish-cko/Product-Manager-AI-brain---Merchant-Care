---
id: 21991167701394
section_id: 23045937114898
title: "Troubleshooting a Payout in Pending Status"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/21991167701394-Troubleshooting-a-Payout-in-Pending-Status"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-03-18T13:41:57Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQT889RQXXSG27BB4ZJ0M"]
label_names: ["case_transactions", "ROW", "payout", "case_transactions_issue_status_proof"]
user_segment_ids: [11003606966930]
archive: false
---

**Use this article when**

Resolving cases where a merchant reports that a payout is stuck in a "PENDING" status. 

**Case type: **Payments in

**Issue Type: **Transaction status (Non 3DS & Refunds)

**Reason: **Stuck in status / status enquiryINTRODUCTION TO PAYOUTS IN A PENDING STATE 💬

There are several possible reasons for a bank or card payout in _Pending_ status, including:

- Timeline thresholds – Confirm that the delay exceeds the standard payout processing timelines.

- Sanctions screening – All transactions undergo sanctions screening to ensure compliance with international regulations. This process can cause delays, particularly if further information is required.

- Requests for additional information – Checkout.com may need to check certain details before completing the payout.

- Beneficiary details – If the beneficiary’s information is incorrect or incomplete, this can cause processing delays.

Transaction monitoring requests help us meet regulatory obligations with our banking and regulatory partners. If our system cannot approve the payment automatically, an alert is raised and our Operations Team reviews it within 24 hours. 

A payout may appear as "pending" in the system when it's under review by the Transaction Monitoring Team. This review is part of a standard security protocol and may require additional information from the merchant to be completed. 

We may request customer ID details or more payment data, such as the source of funds, or the purpose of the payment.

We'll email the merchant with a request, and they must respond within 10 calendar days from when we sent the request. See the merchant-facing article: [Respond to compliance requests](https://www.checkout.com/docs/business-operations/respond-to-compliance-requests#How_it_works) for more information.

 

**⚠️ Merchants might contact us before the 24-hour review is complete. Please remind them that reviews take up to 24 hours and to wait until then.**

| Use this macro: Payouts > Payout Pending (inquiry in 24 hours screening SLA) |
| --- |

PROCESS TO TROUBLESHOOT PAYOUTS IN A PENDING STATE 🖊️Step 1: Confirm the Transaction Status

First, check the current status of the payout:

- Access Retool > Payouts > Payout-Search

- Enter the Payment ID, The system will display the transaction's current status

Step 2: Check for a Request for Further Information (RFI)

If the status is "PENDING," the next step is to check if an RFI has been sent to the merchant.

- Access Retool > fxp-fincrime > RFI (Full Version)

- Enter the Payment ID

- The dashboard will show if the transaction was flagged for an RFI

- If an RFI was sent, click on Open > Request Details to view the timeline and the specific information requested from the merchant

**(A) Scenario A: RFI Sent**

- Inform the merchant that the transaction was flagged by our Transaction Monitoring Team, which has sent an RFI

- Advise the merchant to provide the requested information so the payout can be released, they must respond within 10 calendar days from when we sent the request

**(B) Scenario B: RFI Response Received, but Payout is Still Pending**

- If the merchant confirms they've already provided the information and the RFI status is "Received Further Information" but the payout is still "PENDING," contact the Transaction Monitoring Team via macro in Zendesk to request a review of the payout.

**(C) Scenario C: No RFI Sent Within 24 Hours**

- If no RFI has been sent within 24 hours of the transaction, contact the Transaction Monitoring Team via macro in Zendesk and ask them to review the payout
Step 3: Check Event Codes with Alfred

To get a more detailed history of the payout, you can use the Alfred tool.

- Access Retool > fxp-fincrime > Alfred 2

- Enter the Payment ID

- This will display all event codes related to the payout, which can tell you if an RFI was sent, a reply was received, or the payout was released

💡 Tip: Refer to the full list of [Alfred Event Codes](https://checkout.atlassian.net/wiki/spaces/FCT/pages/5320736853/ALFRED+App#Event-definitions)RESOLUTION ✅

Once the Transaction Monitoring Team has reviewed the payout and the merchant has provided the necessary information, the "pending" status should be resolved. 

The funds will typically reflect in the cardholder’s account within 24 to 48 hours after the payout is cleared.Remediation Steps

- If the payout has bounced back, create a case with the Disputes Team and include the merchant in the email correspondence. Advise the merchant that the Disputes Team will handle the rest

- If the payout is still pending after 24-48 hours and the Alfred script shows no result (meaning it wasn't sent to clearing), create a [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277) for the Clearing Team

  - Use the designated form, selecting 'clearing' for the domain the Clearing Team will investigate and provide further guidance

  - You can also message #ask-card-payouts for pending transactions after an RFI has been sent out and responded to

ESCALATION ⬆️

When to Escalate:

- When the payout has been in a "Pending" status for more than 24-48 hours and has not been cleared

- If the payout was disputed and bounced back (according to scheme portal), please follow the below instructions:

  - Search the payment ID in salesforce and see if adjustment for the payment ID was raised and completed already - if Yes, then search adjustment ID from payment ID using this [Looker](https://checkoutinternal.eu.looker.com/explore/nas_adjustments/lightning_adjustments_aggregate?toggle=fil&qid=9EPO4JA3EXAH3aSL6CSaFc) link(FAR)

  - if No(for example, no SF ticket found, adjustment was raised but not completed yet etc), then transfer the case to Dispute Team, cced the merchant, and resolve the case at merchant care level.

- If the Transaction Monitoring Team or Clearing Team needs to take action or review the case

- Required Information:

  - Payment ID and ARN

  - Current status from Retool

  - Any relevant event codes from Alfred

  - Proof of RFI sent or received

  - Dispute case number (if the transaction is disputed) 

- Follow-up:

  - Monitor the case for updates from the respective teams (Disputes, Clearing, or Transaction Monitoring)

  - Notify the merchant of any new developments

  - Inform the merchant that the respective team will follow up directly

RESOURCES ⭐️

| Related Articles |
| --- |
| Merchant Facing Article: [Card Payouts or bank payouts pending](https://support.checkout.com/hc/en-us/articles/18226752867346-Card-payouts-or-bank-payouts-pending) |
