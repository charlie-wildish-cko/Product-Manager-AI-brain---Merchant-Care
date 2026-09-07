---
id: 32094100042130
section_id: 22197990418450
title: "Understanding AMEX SE numbers"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/32094100042130-Understanding-AMEX-SE-numbers"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-12-29T09:01:41Z"
permission_group_id: 26838654181266
content_tag_ids: []
label_names: ["amex", "mid", "SE numbers"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

When a merchant asks to be provided with their Amex SE Number(s) or when you need to identify the AMEX equivalent of a Merchant Identification Number (MID) for a client and when you need to verify which SE numbers are currently active for specific processing or configuration tasks.

## INTRODUCTION **💬**

In the context of American Express (AMEX) processing, an **SE Number (Service Establishment Number)** is a unique identifier assigned by AMEX to merchants. It functions similarly to a **Merchant Identification Number (MID)** used by other card schemes (Visa/Mastercard).

 

## PROCESS 🖊️

### **Key Characteristics**

- **Three-Party Model:** Since AMEX often operates on a three-party model (acting as both the issuer and the acquirer), they onboard merchants directly and assign these specific SE numbers.

- **Format:** SE numbers are typically **10 digits** long. They can begin with any digit, including **zero (0)**.

- **Currency Mapping:** Each SE number is tied to specific processing and settlement currencies. A single merchant may have **multiple SE numbers** if they accept payments in multiple currencies (e.g., one SE for JPY, another for USD).

### **How to Retrieve Amex SE Numbers**

To ensure you provide the correct information to a merchant, follow these steps:
**Step 1: Looker Reporting (Internal Search)**

You can find the raw mapping of merchants to their respective processor details via this Looker report:

- **Report Link:** [Merchant Processor Mapping NAS](https://checkoutinternal.eu.looker.com/explore/client_admin_tool/finance_merchant_processor_mapping_nas_non_apm?qid=jIxuR2fYel0ZBecq71XC7H&toggle=fil)  
_Note: This report provides a list of all mappings associated with the merchant account._

**Step 2: Verification via Config Team (Required)**
Because the Looker report may show multiple entries (including legacy, testing, or deactivated IDs), you must confirm the status before replying to the merchant.

- **Action:** Reach out to the **Config Team**.

- **Purpose:** The Config Team will review the backend configuration to identify which SE numbers are **Active** and which are **Deactivated**.

- **Importance:** This prevents providing the merchant with an incorrect or inactive ID.

## RESOURCES **📍**

| Tools | Case Examples |
| --- | --- |
| [Merchant Processor Mapping NAS](https://checkoutinternal.eu.looker.com/explore/client_admin_tool/finance_merchant_processor_mapping_nas_non_apm?qid=jIxuR2fYel0ZBecq71XC7H&toggle=fil) | [Case 43056](https://checkout1360.zendesk.com/agent/tickets/43056) |
