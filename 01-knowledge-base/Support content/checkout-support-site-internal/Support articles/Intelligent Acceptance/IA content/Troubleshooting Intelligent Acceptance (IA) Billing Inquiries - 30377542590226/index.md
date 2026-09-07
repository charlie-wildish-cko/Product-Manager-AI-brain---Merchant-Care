---
id: 30377542590226
section_id: 29824613373714
title: "Troubleshooting Intelligent Acceptance (IA) Billing Inquiries"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/30377542590226-Troubleshooting-Intelligent-Acceptance-IA-Billing-Inquiries"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-11-18T11:22:34Z"
permission_group_id: 26838654181266
content_tag_ids: ["01K6AASRZ015NW9D6WTY6VAF3X", "01K88KP6JD4E6GDQCYNDAPRMJX", "01KA9E8NW80D6VKJSA437SB9TK"]
label_names: ["billing", "L2", "IA"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

Use this guide to understand the standard per-transaction billing model for Intelligent Acceptance (IA) and to investigate and escalate merchant inquiries regarding discrepancies in their final IA bill.

## DESCRIBE THE ISSUE 💬

A merchant's final bill for Intelligent Acceptance appears incorrect or the number of billed transactions is higher than expected. The core issue is a lack of clarity regarding IA's per-transaction billing model and the potential for special commercial agreements to affect the final cost.

 

## KEY TAKEAWAYS 🔑

- **IA is billed per optimized transaction**, not per individual optimization event. A single transaction is only billed once, regardless of how many optimizations it receives.

- **Pricing is Commercial-Owned:** Final costs, special pricing, and agreements are set exclusively by the **Commercial team**. IA and Payment Performance teams do not set pricing.

- **Performance Exclusions are DEPRECATED:** All merchants are charged for all optimized transactions. The previous performance-based billing exclusion was deprecated on August 1, 2025, and is no longer active.

## TOOLING**📍**

| Data Explorer | CAT | Dashboard |
| --- | --- | --- |
| ** ******[Data Explorer](https://retoolprod.mgmt.ckotech.co/apps/81c167c4-7d39-11ec-86c4-73d37fb76d07/payment-performance-shared-support/Data%20Explorer) Application : Retool prod  Role: Data-Explorer-Editors | **Client Admin tool (CAT)**** **Sandbox and Production  Role:** **   - Super User (both environments)   - Super Admin ( sandbox only) | ****[Dashboard](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274) Application Checkout -  Dashboard Sandbox & Production Role:    - Super User (both environments)  - Super Admin (Only sandbox environment) |

## PROCESS FOR IA BILLING INQUIRY RESOLUTION 🖊️

The primary goal is to **clarify the billing model** and, if the discrepancy persists, use the correct **escalation path**.

### Step 1: Confirm the General IA Billing Rule

Explain the fundamental billing model to the merchant:

- IA charges are on a per-transaction basis

- A transaction is billed only once, even if it receives multiple optimization services

- The final cost per transaction includes any special agreements and is set by the Commercial team

- Merchants are charged for all optimized transactions (performance-based exclusions are obsolete)

### Step 2: Investigate Billing Discrepancy

If the merchant still believes the bill is incorrect, use the tools to troubleshoot:
Issue A: Bill does not match formula: (Optimized Transactions) x (Agreed Cost)

**Verify Optimized Transactions:**

- Open **Data Explorer** and select the merchant and billing period.

- Navigate to **Acceptance exploration** and enter the entity name.

- Note the "Transactions optimized" count.

 

**Check Pricing Profile (Reference only):**

- Open **CAT** and select the merchant

- Navigate to **Pricing Profile** > **Vas pricing profile**

**💡 Conclusion:** If the invoice still doesn't match the formula based on the verified count, the cause is likely a **Special Commercial Agreement** or an **Issuance Error**. Both require **Escalation**.

 
Issue B: Number of Billed Transactions appears too high

**Verify Calculation Basis:** Confirm the merchant is **not** comparing the billed count against only **approved** transactions.

**Verify Against Total Transactions:** Advise the merchant to check the billed count against the **Total Transactions** (approved and unapproved) for the period. The number of billed IA transactions will **never exceed** this total.

 

## ESCALATION ⏫

All questions, investigations, or discrepancies related to the final amount charged on a merchant's invoice must be escalated.

| Escalation Reason | First Step (Internal Check) | Final Escalation Path |
| --- | --- | --- |
| **Final amount discrepancy** (cost/formula mismatch) | Check with **Product Analytics** via Slack on **#ask-analytics** for data verification | **Billing team** via Zendesk Macro |
| **Inquiries regarding special pricing, costs or agreements** | N/A (Owned by Commercial) | **Billing team** via Zendesk Macro |

**Required Information for Escalation:**

- Merchant Name/ID

- Invoice ID(s) and Period(s) in question

- The exact nature of the discrepancy (e.g., formula mismatch, transactions too high)

- The merchant's agreed cost per transaction (if known)

## RELATED ARTICLES ⭐

| -  [Intelligent Acceptance: Strategy & Add-On Reference](https://checkoutint.zendesk.com/hc/en-us/articles/31061908424210-Intelligent-Acceptance-Strategy-Add-On-Reference)  - [Step-by-Step Guide: Configuring a Merchant for Intelligent Acceptance (IA)](https://checkout.atlassian.net/wiki/spaces/ARM/pages/7360249982/How+to+best+configure+a+merchant+on+Intelligent+Acceptance) |
| --- |
