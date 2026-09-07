---
id: 30281528533010
section_id: 23045937114898
title: "Proof of Payout for Mastercard CRB"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/30281528533010-Proof-of-Payout-for-Mastercard-CRB"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-03-18T13:39:25Z"
permission_group_id: 26838654181266
content_tag_ids: []
label_names: []
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

To verify a successful Mastercard payout and generate proof of the settled transaction using the **Retool clearing event app** and **Mastercard Connect**. 

**Problem: **A cardholder or merchant is requesting proof that a **payout** transaction to a Mastercard has successfully cleared and settled.

**Case type: **Payments in

**Issue Type: **Transaction status (Non 3DS & Refunds)

Reason: Stuck in status / status enquiry

## DESCRIBE THE ISSUE 💬

An agent needs to confirm the final status of a Mastercard payout and obtain an official document (proof) to share with the merchant or cardholder to address a CRB inquiry. The process involves checking the internal system for clearing status and then the Mastercard network for final settlement details.

 

## RESOURCES 📍

| Tools | Case Examples | Related |
| --- | --- | --- |
| Links to tools needed to diagnose or solve [See Ops Tools Library](https://checkout.atlassian.net/wiki/spaces/LL/database/6990364784?atl_f=PAGETREE) | Similar case examples and solutions | - [Refund Proof for Mastercard](https://checkoutint.zendesk.com/hc/en-us/articles/21991182445074-Refund-proof-for-Mastercard) |

## PROCESS FOR PROOF OF PAYOUT-MASTERCARD CRB🖊️

## Step 1. Check Payout Clearing and Settlement Status in Retool

- Confirm if the payout has been successfully **cleared** and **settled** using the **clearing event app on Retool**.

- This initial check confirms the internal system status before checking the network.

### Step 2. Access Mastercard Connect

- 
 
**Log in to Mastercard Connect** using the **UK profile**.

  - 
 
If this is your first time logging into the UK profile, refer to ****[steps 4 to 9 in the SOP Refund proof for Mastercard](https://checkoutint.zendesk.com/hc/en-us/articles/21991182445074-Refund-proof-for-Mastercard) for detailed instructions.

- Click on **'Mastercard Move'** in the 'MY FAVORITES' section.

## Step 3. Search for the Payout Transaction

- In the 'CREATE SEARCH' section, select **'Checkout - P2P ESI'** from the **'Transaction Initiator'** dropdown list.

- Paste the **Payment ID** into the **'Reference ID'** field.

- Choose **'Custom date range'** under 'Transaction date range UTC Time Zone'.

- Set a date range that covers both the payout date and the clearing date you found in Step 1.

- Click **'Apply search'**.

### Step 4. Generate Proof of Payout

- Once the search results appear, click on **'See more details'** for the relevant entry.

- Take a **screenshot** of the **DETAILED TRANSACTION INFORMATION** as the proof of payout

## RESOLUTION ⚒️

**Expected Result:** The screenshot of the detailed transaction information from Mastercard Connect confirms the payout transaction was successfully approved and provides network-level details (e.g., Transaction ID, Current Status: **Approved**).

**Remediation Steps:** If the status in Retool or Mastercard Connect is _not_ settled/approved, follow standard **payout failure** or **settlement delay** troubleshooting guides.

 

## FAQs** ****❓**

Why do I need to check both Retool and Mastercard Connect?

- Retool confirms the internal system status and when the funds were cleared. 

- Mastercard Connect confirms the final status as processed by the Mastercard network, providing the official proof needed for the CRB inquiry.
