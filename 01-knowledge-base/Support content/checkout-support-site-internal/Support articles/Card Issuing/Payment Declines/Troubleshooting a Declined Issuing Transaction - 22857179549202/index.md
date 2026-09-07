---
id: 22857179549202
section_id: 28482948435346
title: "Troubleshooting a Declined Issuing Transaction"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22857179549202-Troubleshooting-a-Declined-Issuing-Transaction"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-31T16:15:21Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JNGXCVNHFQB2TX90T7Z1YKMZ"]
label_names: ["global", "issuing", "case_card_issuing", "case_card_issuing_transaction_has_been_declined"]
user_segment_ids: [11003606966930]
archive: false
---

**Use this article when**

The merchant contacts us because they've got a decline code or a simple message on their terminal or website indicating the reason for the failed transaction.INTRODUCTION TO DECLINED TRANSACTIONS 💬

Issuing decline codes indicate why a transaction was declined by the issuer. They help merchants and acquirers understand and address the issue. 

Common reasons for Issuing Decline Codes:

- 
**Authentication Failures**: Declines occur if card authentication fails due to incorrect details or process issues

- 
**Security Concerns**: Suspected fraud or unauthorized transactions can cause declines

- 
**Policy Violations**: Transactions breaching issuer policies, like exceeding limits, may be declined

- 
**Technical Issues**: Network outages or processing errors can lead to declines

- 
**Insufficient Funds**: Declines happen if the account lacks enough funds

- 
**Card Restrictions**: Restrictions on international or certain merchant categories can cause declines

These codes help diagnose transaction failures and guide merchants on retrying or other actions.PROCESS TO TROUBLESHOOTING A DECLINED TRANSACTION 🖊️

### Step 1: Merchant Self-Service Guidance

Direct the merchant to follow these steps to troubleshoot the issue on their own.

1. Obtain the Card ID or Transaction ID - ensure you have the necessary identifiers to look up the transaction

2. Check the transaction on the Dashboard

  - Log in to the Dashboard

  - Navigate to Issuing > Transactions

  - Search for the specific transaction using the ID

3. Identify the decline reason

  - Hover over the info icon next to the transaction status

  - A tooltip will appear, showing the decline reason (e.g. "velocity reached")

### Step 2: Explore the Transaction

If the merchant is unable to find or understand the decline reason, explore the following details with them

**Locate the transaction details**

- Log in to the Dashboard

- Go to Issuing > Transactions

- Locate the specific transaction to view details such as the amount, merchant name and location

**Identify the error message**

- In the transaction details, check the decline code and description

- Refer to the [Issuing Decline Codes](https://www.checkout.com/docs/developer-resources/codes/issuing-decline-codes) to understand the cause

- Check the exact error message the cardholder saw on the terminal or website and compare it to the decline reason in the logs

**Check the card status**

- From the Dashboard, go to Issuing > Cards

- Search for the card using the cardholder's details or the Card ID

- Verify the card's status (e.g Active, Suspended or Blocked)

- If the card is blocked, identify the reason (e.g. fraud prevention, client request, or compliance action)

**Verify available funds**

- Check the balance of the currency account linked to the card

- Review any spending limits or category restrictions to ensure the transaction did not exceed them

- If the decline reason is "insufficient funds," advise the merchant that the client needs to add funds to the currency account

- Guide the merchant to [enable balance notifications](https://www.checkout.com/docs/funds-management/manage-funds/balances/manage-balances#Configure_balance_notifications_) by going to Dashboard > Profile Icon > Notifications tab > Balance tab > toggle Enable balance notifications

**Review the Auth Relay Response**

- If the merchant uses Auth Relay, check if the transaction was declined by a merchant based on their Auth Relay Response

### Step 3: Additional Troubleshooting Steps

If the issue persists, consider these further troubleshooting steps

**Check for authentication issues**

- If the transaction used 3D Secure or another authentication process, verify that the authentication was successfully completed

**Verify merchant-specific restrictions**

- Confirm if the card has restrictions on certain merchant categories or geographic locations

**Check for system outages or errors**

- Determine if the decline was due to a temporary system issue on the merchant's side or a network problem

### Step 4: Using Internal Tools for Further Investigation

For a more detailed investigation use Datadog and Retool to see the decline reason

**Datadog**

- Log in to Datadog

- Insert the Transaction ID into the "Search for" tab and run the query to see the transaction status and reasons

**Retool**

- Log in to Retool

- Click on Transactions

- Enter the Transaction ID in the search box and click Search, you can also search by Card ID or Cardholder

- Scroll down to the "Events timeline" to see the decline reason

A fully processed transaction shows these events in Retool's “Events” timeline:

- Relayed Authorization Processed: Checkout processed and sent the authorization to the relay

- Authorization Approved: customer approved the authorization request

- Presentment Received: clearing presentment sent

A transaction that has been declined will also be visible in Retool - the system will provide you with the decline reason as seen below in red:

 ESCALATION ⬆️

Raise a [Jira ticket](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277) If you are unable to find the reason why the transaction was declined after following all the steps, please raise a Jira ticket for further assistance
