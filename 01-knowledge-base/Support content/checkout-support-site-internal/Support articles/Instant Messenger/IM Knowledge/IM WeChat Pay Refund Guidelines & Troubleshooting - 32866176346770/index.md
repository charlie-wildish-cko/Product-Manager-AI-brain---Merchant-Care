---
id: 32866176346770
section_id: 32861561879314
title: "IM: WeChat Pay Refund Guidelines & Troubleshooting"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/32866176346770-IM-WeChat-Pay-Refund-Guidelines-Troubleshooting"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-01-27T16:40:53Z"
permission_group_id: 26838654181266
content_tag_ids: ["01K2H6FT8DVD34RFN5CK2JMGG5"]
label_names: ["IM"]
user_segment_ids: [11003606966930]
archive: false
---

**Use this article when**

A merchant contacts with a query about refunds.Introduction 💬

WeChat Pay has specific time-based restrictions for processing refunds. When a merchant reports that a refund is failing, the first step is always to check the **original transaction date**.

See [WeChatPay FAQs](https://checkout.atlassian.net/wiki/spaces/APM/pages/4901961800/WeChat+FAQ)Troubleshooting Tree: WeChat Pay Refund Failures 🤔

Use this flow to diagnose the issue during a merchant chat:

1. 
**Check the Transaction Age:** How many days have passed since the transaction was _completed_?

  - 
**Over 365 Days:** ➔ **Status: Hard Block.**

    - _Solution:_ Inform the merchant that WCP does not support system refunds after 1 year. They must refund the customer via bank transfer or other external methods.

  - **Under 365 Days:** ➔ _Proceed to Step 2._

2. 
**Identify the Error Code:** Did the merchant receive an error?

  - **Error Code: **`**FREQUENCY_LIMITED**`**?** ➔ _Proceed to Step 3._

  - **Other Error:** ➔ Check for standard API errors (e.g., insufficient balance).

3. 
**Check for "Older" Transaction Constraints (60+ Days):**

  - 
**Is the transaction between 61 and 365 days old?**

    - _Context:_ These orders have strict frequency limits.

    - _Solution:_ Advise the merchant to stop attempting the refund for a few minutes. They should **decrease the frequency** of their requests and try again once.

Quick reference table ✅

| **Time Since Completion** | **Refund Capability** | **Support Agent Action/Script** |
| --- | --- | --- |
| **0 – 60 Days** | **Standard** | Proceed with standard refund troubleshooting. |
| **61 – 365 Days** | **Limited Frequency** | "Please slow down your refund attempts and retry. Older orders have frequency limits." |
| **365+ Days** | **Prohibited** | "System refunds are not possible after 365 days. Please use an alternative payment method." |

Merchant Response 🗣️

**For orders over 365 days:**

"I’ve checked the transaction details. Because this WeChat Pay order was completed more than 365 days ago, it has passed the maximum refund window allowed by the provider. To return funds to your customer, you will need to process this refund via an alternative method (such as a direct bank transfer) outside of the Dashboard."

**For **`**FREQUENCY_LIMITED**`** errors (60+ days)**

"I see you are receiving a `FREQUENCY_LIMITED` error. For WeChat Pay transactions older than 60 days, there are stricter limits on how often a refund can be attempted. Please wait a few moments and try the request again at a lower frequency."

 

**提问****：微信支付 (WeChat Pay) 支持退款的最长期限是多少？**

**答:**  
-  **退款期限**：仅支持对过去 365 天内完成的交易订单进行退款 。  
-  **过期订单**：对于完成超过 365 天的订单，请通过其他方式处理退款 。  
-  **频率限制**：此外，对于完成超过 60 天的订单，退款频率也存在限制 。  
-  **错误处理**：如果返回错误代码 FREQUENCY_LIMITED，请降低退款尝试频率后重试 。
