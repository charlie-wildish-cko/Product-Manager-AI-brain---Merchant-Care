---
id: 32868997585938
section_id: 32861561879314
title: "IM: What is the transactions per second (TSP) limit? "
url: "https://checkoutint.zendesk.com/hc/en-us/articles/32868997585938-IM-What-is-the-transactions-per-second-TSP-limit"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-01-27T15:13:36Z"
permission_group_id: 26838654181266
content_tag_ids: ["01K2H6FT8DVD34RFN5CK2JMGG5"]
label_names: ["IM"]
user_segment_ids: [11003606966930]
archive: false
---

**Use this article when:**

The merchant asks what the transactions per second limit is.**OVERVIEW 💬**

Think of **TPS** (Transactions Per Second) or **RPS** (Requests Per Second) as the "speed limit" for how fast software can talk to Checkout.com's servers.

Here is the breakdown of what those specific limits mean for a merchant's integration:

Checkout.com categorizes activity into two different buckets, each with its own allowance of **100 requests per second**:

- **Read Operations (GET):** This includes things like looking up a payment's status or retrieving customer details. You get 100 per second.

- **Write/Action Operations (POST, PUT, DELETE):** This includes creating a new payment, updating a customer, or deleting a card token. You get a separate 100 per second for these.

| **Feature** | **Limit Details** |
| --- | --- |
| **GET Operations** | 100 Requests Per Second (RPS) |
| **POST/PUT/DELETE** | 100 Requests Per Second (RPS) |
| **Scope** | Global (Across all API endpoints) |
| **Customization** | Available upon request |

**MERCHANT RESPONSE 🗣️**

The TPS (transactions per second) limit for the Checkout.com API is set at 100 requests per second (RPS) for GET operations and 100 RPS for POST, PUT and DELETE operations. 

These limits apply across the entire API, regardless of which endpoint is used. If different rate limits are required, this can be arranged separately.

 

提问：系统的每秒事务处理量 (TPS) 限制是多少？  
答:  
Checkout.com API 的 TPS 限制设定为：GET 操作 100 RPS（每秒请求数），以及 POST、PUT、DELETE 操作共计 100 RPS 。  
这些限制适用于整个 API，无论使用哪个端点 。  
如果您需要不同的速率限制，可以另行安排 。
