---
id: 33739087125650
section_id: 21991160900754
title: "How to Perform a Reversal"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/33739087125650-How-to-Perform-a-Reversal"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-03-30T15:36:29Z"
permission_group_id: 26838654181266
content_tag_ids: []
label_names: []
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

This guide covers the technical steps for Merchant Care agents to process a reversal via the internal jumpbox.

For introductory information on [Transaction Reversal 101](https://checkoutint.zendesk.com/hc/en-us/articles/33733206953874-Transaction-Reversals-101) visit the article.

⚠️ Capture reversals are **only** for internal Checkout.com errors (e.g., duplicate captures caused by a system bug).

If a merchant wants to undo a legitimate capture because they changed their mind, **do not** perform a reversal. Advise them to process a **Standard Refund** instead.**Requesting a Reversal 💬**

Before starting a reversal, you must verify that the transaction meets **all** the following criteria:

| ** Feature** | ** Visa** | ** Mastercard** |
| --- | --- | --- |
| ** Time Limit** | Up to **30 calendar days** from the refund cleared date. | Within **24 hours** (1 calendar day) of initiation. ⚠️ If the 24-hour window has passed, a reversal is only possible if the issuer explicitly approves it in writing - which has a very low chance of success. |
| ** Required Status** | Must be `CLEARED` in Agent Toolkit or Hermes | Must be `CLEARED` in Agent Toolkit or Hermes |
| ** Exclusions** | **Payouts** (SMS/Visa Direct) cannot be reversed. | **"Moneysend"** MessageTypes cannot be reversed. |

**Demo Video 🎥**

 

### Step 1: Data Gathering 🔢

Locate the specific IDs needed for the API call by searching the ARN in Hermes and scrolling to the far right:

- **Visa:** `VisaTransactionId` and `PaymentId (GUID)`.

- **Mastercard:** `MastercardTransactionId` and `PaymentId (GUID)`.

### Step 2: Access the Environment 👨🏼‍💻

- Log in to **Guacamole** via Okta.

- Connect to: `nc-jumpbox-broker.mgmt.checkout.internal`.

- 
Open **Postman** from the desktop.

  - If you see a version error, run the **FixPostman.bat** script on the desktop first.

### Step 3: API Submission ▶️

Submit a **POST** request using the relevant endpoint:

- **Visa Endpoint**: `http://internal-cp-clearing-alb-ecs-prod-482749207.eu-west-1.elb.amazonaws.com/new-visa-clearing/api/clearing/reverse`

- **Mastercard Endpoint**: `http://internal-cp-clearing-alb-ecs-prod-482749207.eu-west-1.elb.amazonaws.com/mastercard-clearing/api/clearing/reverse`

**Example JSON Body:**

JSON

```
{
  "ReversalTransactions": [
    {
      "visaTransactionId": Enter_ID_Here,
      "PaymentId": "Enter_GUID_Here"
    }
  ]
}
```

**✅ Success Indicator:** You must receive a **200 OK** response with the message `"OK"`.**Post-Reversal: Monitoring & Account Adjustments 💬**

After successfully submitting a reversal, follow these steps to ensure the merchant is settled correctly and the case is closed.

### Step 4. Verification Timeline 📆

- **Sync Time:** It takes **4–6 hours** for the reversal to appear in Hermes.

- **Status Check:** Wait until the new transaction status is **CLEARED**.

- 
**Identifying the Reversal:**

  - **Visa:** Look for `TransactionCode` **26** (Reversal of Refund)

  - **Mastercard:** Look for `MessageType` **PresentmentReversal**.

_Example:_

### Step 5. Requesting a Financial Adjustment 💰

Because the reversal cancels the refund at the scheme level, you must notify the Payments team to correct the merchant's internal balance.

- Open the **Zendesk Ticket** for the request.

- Use the **Payment Team Macro** to start a side conversation.

- Provide the transaction details and a **screenshot from Hermes** confirming the reversal is `CLEARED`.

- Request a **positive adjustment** and ask for the **Adjustment ID**.

Use [Looker](https://checkoutinternal.eu.looker.com/looks/8998?toggle=dat,fil,vis&qid=Gv4R2SsRFwjPkZdr8MDeyS) to check if the adjustment has been made.

### Step 6. Closing the Case ☑️

- Once you receive the **Adjustment ID** from the Payments team, share it with the merchant.

- Confirm that the funds have been adjusted back to their account.

- 
Solve the ticket.
 

**FAQs ⁇**

**Q. What is a capture reversal?**

A. At scheme level, a **capture reversal** is a clearing message that cancels a previously submitted **capture** (or “presentment”). It makes it as if the capture never happened from Visa/Mastercard’s perspective.

- Capture reversal is treated as a **special / exceptional** operation.

 

**Q. When should we do a capture reversal?**

A. Capture reversals are for internal Checkout errors only. If a merchant requests a reversal, advise them to issue a refund instead.

 

**Q.** _**What is not a capture reversal use case?**_

_**A. **_In these cases, merchants must issue a normal refund, not a capture reversal:

- Merchant changed their mind (order cancelled) after capture.

- Customer no longer wants the goods/services.

- Price/offer changed and merchant wants to undo original capture.

Capture reversals must be done quickly within scheme windows and are handled by Card Processing/PEO, not Merchant Care.

If a merchant wants to undo a legitimate capture, we advise them to issue a refund, which is standard and supported longer-term.
