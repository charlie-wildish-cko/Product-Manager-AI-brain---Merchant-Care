---
id: 30665546666130
section_id: 30665400135058
title: "Bank Payout - Pending Troubleshooting and Procedure"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/30665546666130-Bank-Payout-Pending-Troubleshooting-and-Procedure"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-12-08T15:20:43Z"
permission_group_id: 26838654181266
content_tag_ids: []
label_names: []
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

This article is for **Merchant Care teammates** who need to manage and clarify queries about **Pending Payouts(Pay to Bank)** and why Payouts are late or Confirmed but the funds haven't settled yet. Use this guide to identify where a payout is stuck (FinCrime, Thunes, or LHV) and what steps to take next.**Introduction to Topic 💬**

In the **Pay to Bank** (3rd Party Payouts) process, transactions flow through multiple checkpoints, causing some payouts to be momentarily stuck before final approval is returned. This document helps you understand these checkpoints, which include internal **sanctions screening** by the Compliance Team (FinCrime) and similar checks by our **Banking Partners** (Thunes and LHV) and how to resolve the resulting delays.

**Contact Details for Thunes & LHV:**

****[operations@lhv.com](mailto:operations@lhv.com)  
****[support@thunes.com](mailto:support@thunes.com)** **  
  
Further escalation contacts can be found in this document [here](https://checkout.atlassian.net/wiki/spaces/BP/pages/6965526768/Banking+Partners+-+Contact+details+escalation+paths)**Process Steps for Pending Payouts**

The goal is to identify which step the payout is stuck on to determine the correct action.**Tool and Permissions**

You will need access to the **Payouts Search Tool** and the **Banking Partner portals** (Thunes Portal, LHV Portal).

**Step 1. Identify a Payout Stuck on FinCrime** 

1. 
**Open the Payouts Search Tool**.

2. 
**Enter the payout ID** provided by the merchant.

3. 
**Identify the latest event generated**. If the transaction is stuck in FinCrime, the last event will be **PayToBankScreeningResponse**.

4. 
**Escalate** the list of stuck payouts by posting the **paymentIds** on the **#ask-fincrime** or #support_transaction-operations Slack channel so the team can take action.

**Step 2. Identify a Payout Stuck on Thunes** 

There are three main states to check on the Thunes Portal:

- 2.1. SLS Review Status: This means Thunes is performing its sanctions screening.

  1. 
**Login to the Thunes Portal** - steps can be found in this Zendesk article: https://checkoutint.zendesk.com/hc/en-us/articles/21991182397330-Declined-Bank-Payout-Troubleshooting-Guide

  2. In the **View Transactions** section, filter the transaction using the **PaymentID** and the **Confirmed** status.

  3. Once you confirm the transaction is under sanctions list screening, **escalate to Thunes Support** to ask for an update. Be sure to provide the **Thunes transactionId** available on the Portal.

- 2.2. Submitted Status : This means Thunes has dispatched the transaction to its receiving partner, which is performing its own regulatory checks.

  1. Follow steps 1 & 2 from Section 2.1.

  2. 
**Escalate to Thunes Support** to chase their receiving partner for an update.

- 2.3. RFIs (Request for Information) : Some transactions are pending because Thunes has requested an RFI for specific information (like beneficiary or sender details).

  1. 
**Check the Status on the Payouts Search Tool** (it will show **Pending**).

  2. Check the Thunes RFIs email notifications([#thunes-rfi-notifications](https://checkout.enterprise.slack.com/archives/C08CKTBPK98): private channel). If Thunes are unresponsive, escalate to **#ask-bank-payouts **and contact the AM of Thunes.

  3. The Compliance Team liaises with the merchant to get the information and shares it with Thunes for validation, which can cause delays.

**Step 3. Identify a Payout Stuck on LHV** 

1. 
**Check on the Payout Search Tool** for the full history of events.

  - 
_Note:_ A transaction might appear pending on the Payout Search Tool due to a **fallback to another processing rail**. This is indicated by two different **PayoutDispatched** events with different **routing_key** values.

2. 
**Verify additional information on DataDog**. Look for the **“PDNG”** status, which usually indicates an **RFI** or another manual process is the cause of the delay.

3. 
**If the logs don't provide enough information**, reach out to LHV support (**operations@lhv.com**) with the **third_party_message_request_id** and **third_party_message_response_id** from the **PayoutDispatchedReceived** event to ask for an update.

**⚠️ Merchants might contact us before the 24-hour review is complete. Please remind them that reviews take up to 24 hours and to wait until then.**

| Use this macro: Payouts > Payout Pending (inquiry in 24 hours screening SLA) |
| --- |

**Resolution 🛠️**

If there is **no visible latency** and a merchant is complaining about funds still not settled after the payout is Confirmed:

1. 
**Ask the merchant to provide proof of payment**.

2. 
**Contact the banking partner** to ask for an update and request the proof of payment where applicable to share back to the merchant.

**Escalation ⏫**

Escalation is required when a payout is stuck internally or externally:

- 
**Stuck on FinCrime (Internal Sanctions Screening)**: Post the paymentIds on the **#ask-fincrime** or **#support_transaction-operations** Slack channel.

- 
**Stuck on Thunes (SLS Review or Submitted Status)**: Escalate to **Thunes Support** with the Thunes transactionId.

- 
**Stuck on LHV (Manual Process/RFI)**: Email LHV support (**operations@lhv.com**) with the third_party_message_request_id and third_party_message_response_id.

**Resources 📍**

| **Tools** | **Related** |  |
| --- | --- | --- |
|  | **Payout Search Tool** (Retool app to investigate payout status) | **Jira** (Submit access requests for Payout Search Tool)  **Bug Reporting:** For issues with the Payout Search Tool, contact **#ask-bank-payouts** on Slack |
|  | **Thunes Portal** |  |
|  | **LHV Portal** |  |

**FAQs ❓**

- 
**Why is my Payout Pending?**

  - A payout can be pending because it is stuck in an internal (CKO) sanctions screening by the Compliance Team (**FinCrime**), or with a **Banking Partner** (**Thunes** or **LHV**) for their own regulatory checks or due to an **RFI** (Request for Information).

- 
**Why is my Payout late/confirmed but funds not settled yet?**

  - This occurs when there is a delay in the final confirmation or fund settlement with the banking partner or receiving partner, even if the transaction has passed CKO's internal checks.
