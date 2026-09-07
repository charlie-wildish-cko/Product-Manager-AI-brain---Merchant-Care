---
id: 27694605653906
section_id: 23045958401426
title: "All Payments Failing"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/27694605653906-All-Payments-Failing"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-31T16:08:05Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQT889RQXXSG27BB4ZJ0M", "01JYR94X1AAD1RXB70G1YJWXCT"]
label_names: ["case_transactions", "row", "terminated_merchant", "case_transactions_issue_all_transactions_failing"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article:**

When a merchant reports that all their transactions are failing.

## DESCRIBE THE ISSUE** 💬**

This article provides a comprehensive guide for troubleshooting scenarios where a merchant reports that all of their transactions are failing. This issue can stem from several distinct causes, including:

- A disabled processing channel

- A terminated merchant account

- A wider system anomaly

Following these steps will help you systematically diagnose the root cause, take appropriate action and communicate effectively with the merchant.

## RESOURCES **📍**

| Tools | Communication Channels |
| --- | --- |
| Client Admin tool: To check merchant status and configuration Datadog: To investigate transaction error codes Salesforce / Zendesk: To find historical case information for terminated merchants [See Ops Tools Library](https://checkout.atlassian.net/wiki/spaces/LL/database/6990364784?atl_f=PAGETREE) | **#OCchannel:** A monitoring channel (likely on Slack) where the Operations Centre (OC) team posts about system-wide issues. **Jira:** Used to escalate issues to the OC team. |

## PROCESS FOR TROUBLESHOOTING ALL MERCHANT TRANSACTIONS FAILING**  🖊️**

**Step 1: Check the Merchant's Status in Client Admin**

The first step is to determine if the merchant's account is active or has been terminated

- Navigate to the **Client Admin** tool

- Search for the merchant and check their account status

- Interpret the status:

  - If the status is **'active'**, the account is live. Proceed to **Step 2**

  - If the status is **'inactive'**, the merchant account has been terminated. Jump to the **"Process for Terminated Merchant"** section below

**Step 2: Investigate the Processing Channel**

If the merchant's account is active, the issue may be a suspended processing channel, often due to a compliance or risk-related decision

- While still in the **Client Admin** tool for the active merchant, click on the **'Processing'** tab

- Review the list of processing channels and check the status of the **'authorisation'** setting

- Interpret the status:

  - If the authorisation status is **'disabled'**, it means traffic for that channel has been suspended. Jump to the **"Process for Disabled Channel"** section below.

  - If the authorisation status is **'enabled'**, the issue lies elsewhere. Proceed to **Step 3**

💡 **Tip:** Ask the merchant which channel's transactions are failing or for a recent request ID. Use the request ID in Datadog to find the specific error code and confirm the channel.**Step 3: Check for System-Wide Anomalies**

If the merchant's account is active and the channel is enabled, the root cause could be a broader technical issue.

- Check the **#OCchannel** to see if the Operations Centre (OC) team has reported any ongoing incidents or anomalies that could be affecting the merchant

- Use the **Datadog** link to investigate the failing transactions and identify the response code. You can apply filters such as 'processing channel' or 'scheme' to narrow down the investigation

- If you identify a wider issue or cannot find the cause, proceed to the **"Escalation Paths"** section

## RESOLUTION **🛠️**

## Process for a Terminated Merchant

If the merchant's status is **'inactive'**, your goal is to inform them of the termination and provide context if possible.

- 
**Investigate the reason for termination.** You must find out why and when the account was terminated before contacting the merchant.

  - 
**For managed merchants (Tiers 1-3):** Reach out to the assigned Customer Success Manager (CSM) and request this information.

  - 
**For unmanaged merchants (Tier 4):** Find the agent who previously worked on the case. Look for related tickets or records in **Salesforce / Zendesk** that provide details on the termination.

- 
**Communicate with the merchant.** Once you have the necessary information, reach out to the merchant and inform them that their account was terminated.

## Process for a Disabled Channel

If the channel's **'authorisation'** is **'disabled'**, the channel has been suspended.

- 
**Inform the merchant** that all transactions are failing because the authorisation on their account has been disabled.

- 
**Investigate the reason.** Contact the **Config** team to understand why the traffic was suspended (e.g., due to non-compliance).

- 
**Find out if the merchant was already notified.** Check with the CSM or review recent case history.

- 
**Coordinate official communication:**

  - 
**For managed merchants (Tiers 1-3):** Reach out to the CSM and request they inform the merchant about the suspension (if they haven't already).

  - 
**For unmanaged merchants (Tier 4):** The Care team is responsible for informing the merchant about the suspension.

⚠️ **Warning:** Do not re-enable a disabled channel yourself. Suspensions are typically actioned by the Risk or Compliance team and must be handled through the proper channels.

## ESCALATION** ⏫**

If your initial investigation doesn't reveal a terminated account or a disabled channel escalate the issue to the OC team

**When to Escalate:** Escalate when you have ruled out a termination or suspension and suspect a wider technical problem

**How to Escalate:**

- Raise a ticket with the OC team via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277).

- Post the ticket details on the **#OCchannel** for visibility and monitoring.

**Information to Include:**

- Merchant ID (MID)

- Confirmation that you have already checked for termination and channel suspension

- Details from your Datadog investigation, including specific error codes and transaction IDs

- Any other relevant filters you identified (processing channel, scheme)

## FAQs** ❓**

 What is the difference between a 'terminated' merchant and one with a 'disabled' channel?A terminated ('inactive') merchant has had their entire account and contract permanently closed. A disabled channel is a temporary suspension of transaction processing, usually for risk or compliance reasons, while the account itself remains active.
