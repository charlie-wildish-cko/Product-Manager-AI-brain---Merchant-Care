---
id: 30313312456210
section_id: 21991163953810
title: "Mastercard Void Confirmation: How to Obtain Authorization Reversal Proof"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/30313312456210-Mastercard-Void-Confirmation-How-to-Obtain-Authorization-Reversal-Proof"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-03-18T14:22:57Z"
permission_group_id: 26838654181266
content_tag_ids: ["01J7GY96BWKSSREV7Y3CTPJYW5", "01JYS4X06G4P1FBXP4YZEWJKKH"]
label_names: ["refund"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

To verify a successful Mastercard void transaction and generate proof using the **Checkout Agent Toolkit** and **Mastercard Connect's Transaction Investigator**. This proof is required to confirm the cancellation of an authorization.

**Problem: **A cardholder or merchant is requesting proof that a transaction **void** has successfully been processed by the Mastercard network.

**Case type: **Payments in

**Issue Type: **Transaction status (Non 3DS & Refunds)

**Reason: **Refund proof

## DESCRIBE THE ISSUE 💬

An agent needs to confirm that a transaction (typically an authorization) was successfully voided and obtain an official document (proof) to share with the merchant or cardholder. The process involves checking the internal system for the void details and then the Mastercard network to confirm the **Authorization Reversal**.

## RESOURCES 📍

| Tools | Related |
| --- | --- |
| Checkout Agent Toolkit | ****[Refund proof for Mastercard](https://checkoutint.zendesk.com/hc/en-us/articles/21991182445074-Refund-proof-for-Mastercard) |

## PROCESS FOR MASTERCARD VOID CONFIRMATION 🖊️

### Step 1. Confirm Void and Locate Banknet Reference

- Confirm the transaction has been successfully **voided** in the **Checkout Agent Toolkit**.

- Copy the **Banknet reference number**.

**💡 Tip:** This is a **6-character** value found immediately before the action date in either the **Acquirer Transaction ID** or **Scheme Transaction ID** field.

 

### Step 2. Access Mastercard Connect Transaction Investigator

- 
**Log in to the Mastercard Connect** profile that matches the **acquirer’s BIN region**.
_💡 If you need help connecting, refer to the__****_[Refund proof for Mastercard SOP.](https://checkoutint.zendesk.com/hc/en-us/articles/21991182445074-Refund-proof-for-Mastercard)

- Navigate to **Transaction Investigator**.

- In the 'TRANSACTION TYPE' section, ensure **'Clearing'** is **unselected**. **'Authorization'** should be selected.

- Paste the copied **Banknet reference number** into the **'Banknet reference number'** field.

### Step 3. Search for the Void Transaction

- Select a **date range** that covers the Void date of the transaction.

- Click **Search**.

### Step 4. Confirm and Download Proof of Void

- In the search results summary, confirm the entry is the voided one by checking the following two network-level details:

  - 
**MTI field:** Should display **0410** (the Authorization Reversal code).

  - 
**Response Code:** Should display **'00'** (Approved and completed successfully)

- Once you confirm the correct void entry, click on **‘View’**.

- Click the **'Export'** button (typically available on the top right as an arrow).

- Select the **PDF** format and click **'Export'** to download the proof as a PDF.

 

## FAQs** ****❓**

What is the MTI 0410 and why is it important?**MTI** stands for **Message Type Identifier**. The **0410** code specifically signifies an **Authorization Reversal**. Seeing this code confirms that the transaction was successfully voided/cancelled on the Mastercard network level, which is the definitive proof required.
