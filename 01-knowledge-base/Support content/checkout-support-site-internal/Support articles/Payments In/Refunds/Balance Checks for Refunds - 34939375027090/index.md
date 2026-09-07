---
id: 34939375027090
section_id: 21991163953810
title: "Balance Checks for Refunds"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/34939375027090-Balance-Checks-for-Refunds"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-04-20T07:01:05Z"
permission_group_id: 26838654181266
content_tag_ids: []
label_names: []
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

This guide explains the introduction of refund balance checks for merchants in Stored Funds Value (SFV) regions. Use it to help merchants manage their cash flow and resolve declined refund requests.

Code **50003 - Balance reservation insufficient funds**.INTRODUCTION 💬

We are introducing balance checks to align with industry standards and help merchants avoid negative account balances. By verifying funds before a refund is processed, we provide a more predictable cash flow for our merchants.

### **Impacted regions and timelines**

This change applies to merchants with entities in **France (SAS)**, **Singapore**, the **UK**, and the **US**.

- **Initial notice:** April 13, 2026

- **Minimum balance feature live:** May 8, 2026

- **Final reminder:** May 25, 2026

### **How balance checks work**

Before processing a refund, the system verifies that the merchant has sufficient funds across three balance types:

- Available

- Pending

- Operational

If the total balance is insufficient, **the refund will be declined**. We do not notify the customer of the decline; however, the merchant receives a webhook with code **50003 - Balance reservation insufficient funds**.

### **How to help merchants prepare**

Recommend these Business Account features to ensure uninterrupted refund processing:

- **Balance top-ups:** Add one-off funds to **Available** or **Operational** balances.

- **Balance notifications:** Set alerts to trigger when the **Available** balance falls below a specific threshold.

- **Minimum balance:** Configure a set amount to remain in the **Available** balance specifically for refunds and payouts.

- **Update settlement schedule:** Slowing down settlement frequency helps keep more funds in the **Available** balance.

TROUBLESHOOTING REFUND DECLINED ⚒️

If a merchant reports a declined refund with error **50003**, follow these steps:

- **Verify balance:** Check if the merchant's combined balances cover the refund amount.

- **Suggest a top-up:** Advise the merchant to use the balance top-up feature for the quickest resolution.

- **Reattempt refund:** Once funds are added to the **Available** or **Operational** balance, the merchant can retry the request.

- **Long-term fix:** Recommend setting a **Minimum balance** or **Balance notifications** to prevent future declines.

ESCALATION ⬆️

- Issue: Technical webhook failure

- Contact: Integration Support

- channel: Slack #support-tech

- Include: Merchant ID, Webhook ID, Timestamp

FAQs ⁇

 

**Will this affect all payment methods?** Yes, balance checks apply to every refund request processed through the Checkout.com account. 

**Can merchants set different notification alerts for different entities?** Yes, merchants can configure notifications for individual entities or use the client view for an aggregate alert. 

**What should a merchant do before a major sale?** We recommend they use **Balance top-ups** a few days before an expected surge in refunds to maintain a positive customer experience.
