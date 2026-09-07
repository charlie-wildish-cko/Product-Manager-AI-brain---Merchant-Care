---
id: 32931545339538
section_id: 28915801595794
title: "Merchant Idempotency Window Extensions"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/32931545339538-Merchant-Idempotency-Window-Extensions"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-02-04T17:47:14Z"
permission_group_id: 26838654181266
content_tag_ids: []
label_names: []
user_segment_ids: [11003606966930]
archive: false
---

**Use this article when**

A merchant requests an extension of their idempotency window.**Overview 👀**

Idempotency allows merchants to safely retry API requests without the risk of creating duplicate transactions or records. This is particularly useful during network errors or timeouts. By default, the idempotency window (the period during which a key is remembered) is **24 hours**.

Some merchants may require a longer window (e.g., up to 7 days max) based on their specific business logic or retry strategies.

**⚠️ The maximum number of days an idempotency window can be extended is 7 days****Key Information 🔑**

 

- Default Window: 24 hours.

- Maximum Recommended Extension: Up to 7 days.

- Escalate the request on slack channel: [#ask-gateway](https://checkout.enterprise.slack.com/archives/C2ZJRL7ED)

- Public Documentation: [Idempotency - Checkout.com Docs](https://www.checkout.com/docs/developer-resources/api/idempotency)

**Resolution ⚒️**

### Level 1 (Initial Triage)

When a merchant requests an extension of their idempotency window, the L1 agent must collect the following information:

- **Merchant Name:**

- **CLI_ID:** (Mandatory)

- **Requested Duration:** (e.g. up to 7 days)

- **Business Justification:** Why does the merchant need an extension? (e.g., "Long-running batch processes" or "Specific retry logic for network stability").

**✅ Action:** Once the info is gathered, escalate the request via slack to: [#ask-gateway](https://checkout.enterprise.slack.com/archives/C2ZJRL7ED)

### Finalization

- Once L3 confirms the change is live., you must inform the merchant that the window has been updated.
