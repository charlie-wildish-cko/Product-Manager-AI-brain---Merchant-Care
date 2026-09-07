---
id: 30665677714450
section_id: 30665400135058
title: "Pay to Bank - Returns"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/30665677714450-Pay-to-Bank-Returns"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-12-04T14:02:16Z"
permission_group_id: 26838654181266
content_tag_ids: []
label_names: []
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article:**This procedure is for **Merchant Care teammates** to manage and resolve queries regarding **Payout Returns**, which happen when a payout is sent back from the beneficiary bank (e.g., due to invalid details or a closed account).

### **INTRODUCTION TO TOPIC 💬**

This procedure is specifically designed to manage **Payout Returns** that are sent back from the beneficiary bank. When a payout is returned, the merchant is credited back in their Controlled Account (CA). Merchants typically contact us when their clients have not received the funds, and the respective bank confirms the non-settlement. This SOP is also a guide to clarify queries such as "Why is my Payout Returned?".

**Contact Details for Thunes & LHV:**

****[operations@lhv.com](mailto:operations@lhv.com)  
****[support@thunes.com](mailto:support@thunes.com)** **  
  
Further escalation contacts can be found in this document [here](https://checkout.atlassian.net/wiki/spaces/BP/pages/6965526768/Banking+Partners+-+Contact+details+escalation+paths)

### **PROCESS STEPS FOR MANAGING PAYOUT RETURNS**

**1. Identify Payout Return**

Follow these steps to identify a payout with a **Returned** status:

1. Open the **Payouts Search Tool**.

  - Note: The Payouts Search Tool is a Retool app used to investigate payout status and rejection reason.

2. Enter the **payout ID** provided by the merchant in the request

3. Identify the **Bank Partner** (currently Thunes or LHV) that processed the payout.

  - Do this by checking the routing_name from the latest **PayoutDispatched** Event. Identify the **returned** status on the Payouts Search Tool. Cross-verify the status on the **Banking Partner's Portal**.

  - For **Thunes**: Follow the procedure to check that the status is **Reversed** on the **Thunes Portal**.

  - For **LHV**: Use the ****[DataDog Link](https://app.datadoghq.eu/logs?query=env%3Aprod%20service%3ACheckout.FXP.PaymentControls%20%40Properties.MessageType%3APayoutReturnReceived%20%40Properties.Rails%3ALhv&agg_m=count&agg_m_source=base&agg_t=count&clustering_pattern_field_path=message&cols=host%2Cservice%2C%40Properties.Rails&fromUser=true&link_source=monitor_notif&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=desc&viz=stream&from_ts=1759141874221&to_ts=1760437874221&live=true) to get the payouts that are reversed. (Note: The LHV Portal is not yet available)

4. Once you confirm the payout is **Returned/Reversed**, the ticket can be marked as solved.

**2. Merchant Claims Payment Hasn’t Settled To Beneficiary Account**

For the scenario where the merchant is claiming that payment was not settled to the beneficiary bank account, it may relate to an **Unreferenced Return**. This happens when the Beneficiary Bank sends an unreferenced payout instead of an actual "Return Command," which can cause the Partner to miss correlating the transaction and consequently miss raising the Return.

This explains why some PayoutReturned might be missed from the partner.  
Here're some ways to confirm the status of missing transaction/resolve the inquiry:

**2.1 Check Banking Partner's Portal and Request Proof of Payment**  
We sometimes get requests from merchants claiming the fund was not transferred to the beneficiary bank account, the reason why we request a Proof of Payment from the Banking Partner.

1. Check the **Banking Partner's Portal** to ensure the Status is **REVERSED**.

2. Contact the **Banking Partner** (Thunes or LHV) to request a **Proof of Payment** for that specific transaction.

**2.2 Check for PayoutReturned Event internally**

1. Follow **Procedure 1.1** (Identify Payout Return) to identify the Payout.

2. Check the events generated for the Payout and ensure the **PayoutReturned** Event is present.

**2.3 Ensure Thunes Updates Status to Reversed**

If the merchant is claiming the payment was not settled, confirm that the **Reversed** status is reflected on the **Thunes Portal**.

- If the status is not up to date, you must **contact the Banking Partner** to notify them to update the status to **Reversed**. This ensures it is reflected in the Events, allowing the money movement to occur.

__Note: From a PTB perspective, Reversed and Return would mean the same(As opposed to Payins where Credit Return probably mean a Refund while Reversal can imply reversing a Capture/Refund after it was cleared/settled). On the Thunes Portal the status is REVERSED.__

__Note: To be able to process a Payout Reversal, we need to get the PayoutReversal Event and for that, we rely on the transaction being in REVERSED Status on Thunes Portal. It may happen that Thunes did not update the status of the transaction to REVERSED. __  
__If we do not get the Payout Reversal Event, we will not be able to release the fund back to the beneficiary account (=merchant account).__

__Note: When the transaction status is “Reversed' on Thunes portal, this means the funds are back from Thunes to Checkout, but not back to the merchant account.__
**3. Identify the Reason for Payout Return**

Bank Payouts may be Returned/Reversed due to but not limited only to the following reasons described in ['RESOLUTION' section](https://checkoutint.zendesk.com/hc/en-us/articles/30665677714450--Pay-to-Bank-Returns#:~:text=provide%20more%20context.-,RESOLUTION%20%F0%9F%9B%A0%EF%B8%8F,-Once%20you%20confirm).   
For any Payout that has been **Returned**, a **PayoutReturned Event** is generated.

1. Within the Event Details of the **PayoutReturned Event**, look for the **third_party_return_code** and **third_party_return_description**. These usually provide more context on the reason for the Return.

2. If you receive a **generic response** (e.g., third_party_return_code: "8 - 80000" mapped to internal code 50499, or a generic third_party_return_description: "REVERSED - REVERSED") , the **Banking Partner should be contacted** to provide more context.

### **RESOLUTION 🛠️**

Once you confirm the Payout status is **Returned/Reversed** on the Payouts Search Tool and cross-verified on the Banking Partner's Portal, the merchant's account will be credited. The ticket can then be marked as **resolved**.

Possible reasons for a Payout to be Returned/Reversed include, but are not limited to:

- 
**Incorrect Account Details:** Invalid account number, name mismatch, or typo errors in account details.

- 
**Account is Closed or Dormant**.

- 
**Fraudulent/Unauthorized Activity**.

- 
**Compliance or Regulatory Issues:** AML Checks, Sanctions lists, or KYC Requirements.

- 
**Bank Errors:** Double Payment or wrong recipient.

- 
**Recipient Bank Rejection:** Internal bank policy, technical failure, etc.

- 
**Payment Canceled/Recalled:** Sender request to cancel payout before it gets settled.

- 
**Returned by Intermediary Bank:** Missing/incorrect info or compliance issues.

### **ESCALATION ⏫**

**Merchant Care teammates** are responsible for identifying Payout Returns and contacting **Thunes or LHV** for further assistance on the matter.

If you are unable to determine the reason for the Payout Return from the **PayoutReturned Event** (due to a generic code like "8 - 80000"), the **Banking Partner should be contacted** to provide more context.
