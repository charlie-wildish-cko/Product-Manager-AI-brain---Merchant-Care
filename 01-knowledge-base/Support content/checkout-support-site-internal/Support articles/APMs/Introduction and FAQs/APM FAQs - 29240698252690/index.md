---
id: 29240698252690
section_id: 29240636424594
title: "APM FAQs"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/29240698252690-APM-FAQs"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-02-04T17:04:09Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JVW5V7B7TZ05VVPPCG5ZEHCF"]
label_names: ["APM", "tamara", "knet", "declined_apm", "amp_troubleshooting"]
user_segment_ids: [11003606966930]
archive: false
---

Use this article for frequently asked questions about Alternative Payment Methods APMs.

## GENERAL APM FAQs** ❓**

 

[📹 Knowledge Sharing Expert Video Link](https://drive.google.com/file/d/1KJN0kM42P_YLRg8KhnsSZTtSx5q5inZs/view?usp=sharing)What is the first step to investigate a declined APM refund?

The first step is to check the transaction status in **Retool** to confirm that it's "declined".

Then, copy the `correlation_id` from the most recent failed refund event. Use this ID to search for the specific error logs in **Datadog**, which will tell you why the refund failed. 

The error message will help you decide what to do next, whether it's telling the merchant to retry, escalating the issue, or identifying a configuration problem.

 What's an APM?

An **Alternative Payment Method (APM)** is a type of payment that is not a traditional card payment. APMs offer consumers various preferences and regional needs. APMs can be categorized into four broad categories:
• **Digital Wallets** or e-Wallets

• **Bank Transfers**

• **Buy Now Pay Later (BNPL)** options

• **Cash & ATM Payments**

 

Merchants need APMs for several reasons, including regional popularity, customer loyalty, familiarity and trust, market competitiveness, reducing friction, cost benefits, and **risk mitigation**. 

 
The popularity of APMs varies significantly by region, with Digital Wallets and Cards being prominent globally, while bank transfers and BNPL also hold considerable shares in specific regions like the UK & EEA, NORAM, MEA, APAC, and LATAM

 

 **TROUBLESHOOTING ⚒️**

This table provides direct links to our Standard Operating Procedures (SOPs) for handling Alternative Payment Method (APM) inquiries. These steps should be followed **regardless of the specific APM method** being used.

### 💳 Payment Processing Issues

| **If the merchant reports...** | **Action to Take** |
| --- | --- |
| **Failed Payments** | Follow this article: [APM payment declined](https://checkoutint.zendesk.com/hc/en-us/articles/29346766886162-APM-Payments-Declined) to identify the root cause. |
| **Stuck in "Deferred" or "Pending"** | Consult this article: [payments stuck in a deferred state](https://checkoutint.zendesk.com/hc/en-us/articles/30549693756946-APM-Payments-stuck-in-Deferred-status) to resolve processing delays. |

### 🔄 Refund Issues

| **If the merchant reports...** | **Action to Take** |
| --- | --- |
| **Declined Refunds** | Follow the troubleshooting steps for [APM refund status showing as "Declined".](https://checkoutint.zendesk.com/hc/en-us/articles/30547685596818-APM-Refund-Status-Shows-Declined) |
| **Refunds stuck in "Deferred" or "Pending"** | Refer to [APM refunds stuck in a deferred state](https://checkoutint.zendesk.com/hc/en-us/articles/30478859398290-APM-Refund-stuck-in-Deferred-status). |

### ⚠️ Technical & Service Errors

- **Error Code 422: **`**apm_service_unavailable**` If a merchant reports that all payments are failing with this specific error, please follow the [service unavailability](https://checkoutint.zendesk.com/hc/en-us/articles/30550800650130-APM-Payment-failed-with-422-apm-service-unavailable) article immediately.

## TAMARA FAQs** ❓**

 What should be done when a Tamara refund fails with a 500 internal server error?

If a Tamara refund fails with a **500 internal server error**, it means there was a temporary problem on Tamara's end. The best course of action is to tell the merchant to **retry the refund**. This type of error doesn't usually require you to escalate the issue.

To investigate, you can use the `correlation_id` from the declined refund in **Retool** and search for it in **Datadog**. The logs will show the 500 error coming from Tamara's service.

If the merchant tells you the retry failed again, then you should escalate the ticket to L2.

 What if a Tamara refund continues to fail with a "payment state not refundable" error?

If a refund repeatedly fails with a **"payment state not refundable"** error, it likely means there's a status mismatch between our system and Tamara's. This often happens when a payment is marked incorrectly as "approved" instead of "captured" on Tamara's end, which prevents the refund.

You need to **escalate this to L2** so they can contact Tamara to fix the status. The merchant should wait for a confirmation that the issue is resolved before trying the refund again.

Before escalating, you can check the transaction status on the

**Tamara portal**. If the portal shows the order as captured but the refund is still failing, it confirms that Tamara's team needs to investigate.

 How can we verify that a customer received their refund from Tamara?

The way you verify a refund depends on the type of transaction model:

- For **collecting** model transactions, the APM reconciliation team can be contacted to provide proof of the refund transfer.

- For **gateway** model transactions, we do not have visibility over the fund flow, and the merchant must check their own bank accounts and provide the refund proof to the customer.

## 

What is the process if a Tamara refund bounces back?

If a refund bounces back (for example, due to a closed bank account), the APM reconciliation team will be notified first and will create a ticket to figure out the next steps.

The resolution could be one of the following:

- Get new bank details from the customer to try the transfer again.

- Adjust the merchant's account settlement, and the merchant will then refund the customer using a different method.

The final decision often depends on the merchant's preference and their standard procedures for these situations.

 How can I access the Tamara portal to investigate a transaction?

You can access the Tamara portal through **LastPass**. However, you'll need a six-digit One-Time Password (OTP) that is sent to a shared APM team email group. You'll have to contact a member of that group to get the current OTP.

The portal can be used to check transaction statuses, like confirming if an order is "approved and settled" (captured), which is helpful for troubleshooting. To search for a specific order, you'll need the merchant's name and the payment ID.

 **KNET FAQs ❓**

 Why are some Knet payments failing with an "expired" status and a "transaction not found" error?

This specific error means the payment was never successfully created on Knet's side. The "transaction not found" message confirms that Knet has no record of the payment attempt.

This can happen if there was a temporary issue with Knet or if the customer closed the payment page before the transaction was fully started. 

The status will show as "Expired" in our system because the payment was never completed. Since the transaction never existed on Knet's end, these failures can't be fixed. The customer must start a new transaction.

 

###
