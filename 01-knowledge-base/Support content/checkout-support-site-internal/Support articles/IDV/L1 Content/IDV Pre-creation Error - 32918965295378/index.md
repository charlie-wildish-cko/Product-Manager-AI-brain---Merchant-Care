---
id: 32918965295378
section_id: 32304308299922
title: "IDV: Pre-creation Error"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/32918965295378-IDV-Pre-creation-Error"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-02-10T10:30:41Z"
permission_group_id: 26838654181266
content_tag_ids: ["01KE6V773EPR1K1MSSMYWHJ6T4"]
label_names: ["IDV"]
user_segment_ids: [11003606966930]
archive: false
---

**Use this article when**

A "Pre-creation" error occurs when a user is blocked _before_ an IDV session is generated. No record of the attempt will exist in the IDV logs.

Category: Technical Error**How to identify a Pre-creation issue 👀**

 

- **The Error:** Usually "A faster login is required" or a generic "Session expired."

- **The Log Gap:** You search the customer ID/email in the IDV dashboard and see **no activity** for the time they reported the error.

- **The Stage:** The customer is stuck at the very first click, before they see the document upload screen.

[Case Example](https://checkout1360.zendesk.com/agent/tickets/103345?brand_id=10986732715922)  **Resolution ✅**

 

Escalate to the IDV Debug slack channel by using this macro:

| Use this macro: IDV>Transfer>Ask IDV Debug |
| --- |

### **Note Template**

**Issue:** Technical error occurring during **Pre-creation** (before an IDV ID is generated). **Error Message:** _example: _"A faster login is required" 

**Context:**

- **Log Status:** Confirmed **no IDV ID exists** for this attempt in the dashboard/logs.

- **Troubleshooting Done:** User attempted _[details here]_.

Can you please investigate why this is failing at the pre-creation stage for this account?

### **Decision Tree 🔀**
