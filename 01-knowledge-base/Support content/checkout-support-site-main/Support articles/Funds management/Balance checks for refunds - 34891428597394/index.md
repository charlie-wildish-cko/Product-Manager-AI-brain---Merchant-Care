---
id: 34891428597394
section_id: 22325749323794
title: "Balance checks for refunds"
url: "https://support.checkout.com/hc/en-us/articles/34891428597394-Balance-checks-for-refunds"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-06-08T09:11:26Z"
permission_group_id: 11003577394706
content_tag_ids: ["01J7GY96BWKSSREV7Y3CTPJYW5", "01K6G51YBRXMXEGM7SB6T16MW7"]
label_names: ["Accepting payments - Refunds - Refund failed / manual refund"]
user_segment_ids: []
archive: false
---

To help you avoid the complications of negative balances and align our refund practices with other providers, we’re introducing **refund balance checks** for your Europe, Singapore, UK, and US entities later this year.

Once we’ve made this change, we will verify that your account has the necessary funds before processing a refund. As long as your account has sufficient funds across your available, pending, and operational balances, we will process your refund as normal.

However, if your balances are insufficient, the refund will be declined. If this happens, you’ll receive a [webhook](https://www.checkout.com/docs/developer-resources/event-notifications/event-types/payment_refund_declined) with the code 50003 - Balance reservation insufficient funds.

**Important: Please ensure your systems are processing failed refund webhooks correctly before we make this change.**

## **How to prepare**

You can use our Business Account features to keep a positive balance on your account:

- [Balance minimum](https://www.checkout.com/docs/funds-management/manage-funds/balances/manage-balances#Set_a_balance_minimum_)**:** lets you hold a configurable amount in your Available balance to ensure you always have sufficient balances to cover refund amounts.
- [Balance top-ups](https://www.checkout.com/docs/funds-management/move-funds/add-funds)**:** lets you add one-off funding top-ups to your Available or Operational balances, ensuring you can process refunds if you expect your refund requests to increase.
- [Balance notifications](https://www.checkout.com/docs/funds-management/manage-funds/balances/manage-balances#Configure_balance_notifications_)**:** notifies you when your Available balance falls below a specified threshold, helping you to take action before your balance goes negative
- [Update your settlement schedule](https://www.checkout.com/docs/funds-management/receive-settlements/manage-settlements#Update_settlement_schedule)**:** using a slower settlement frequency can help ensure that your Available balance is sufficient to cover your refund requests

## **Frequently Asked Questions**

### **Why are you making this change now?**

We’re making this change to help you proactively manage your cash flow and avoid the burden of negative account balances. It also aligns us with other payment services providers, providing you with a more predictable processing flow.

### **When do the changes go live?**

We’re rolling the change out in phases. You’ll have received a communication with the specific go-live dates for your business at least 60 days before we make the change.

### **Will this affect all my payment methods?**

Yes. Balance checks will apply to all refund requests processed through your Checkout.com account.

### **What will my customers see if a refund is declined?**

Nothing. We won’t notify your customer if we decline a refund, but we’ll send you a 50003 - Balance reservation insufficient funds webhook so you can retry the refund once you have enough balance on your account to do so.

### **Which of the Business Account features should I use to resolve a situation where a refund is declined?**

For quickest resolution, use the [balance top-up](https://www.checkout.com/docs/funds-management/move-funds/add-funds) feature. Once you’ve added funds to your Available or Operational balance, you can reattempt the refund request.

### **Can I set different balance notification alerts for different entities?**

Yes. You can configure [balance notifications](https://www.checkout.com/docs/funds-management/manage-funds/balances/manage-balances#Configure_balance_notifications_) for each of your entities, or across all of your entities using the client view.

### **What do I do if I expect a high volume of refunds following a sale?**

We recommend using [balance top-ups](https://www.checkout.com/docs/funds-management/move-funds/add-funds) a few days before you expect a surge in refund requests. This ensures your customer experience avoids interruptions, even during your busiest periods.
