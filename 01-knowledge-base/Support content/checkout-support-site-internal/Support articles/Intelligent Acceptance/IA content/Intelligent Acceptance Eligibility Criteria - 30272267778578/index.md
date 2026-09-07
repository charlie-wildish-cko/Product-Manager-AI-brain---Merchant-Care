---
id: 30272267778578
section_id: 29824613373714
title: "Intelligent Acceptance Eligibility Criteria"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/30272267778578-Intelligent-Acceptance-Eligibility-Criteria"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-11-19T12:05:05Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTZ6WEQ3S7TQ9KW35WKJXPDX", "01K6AASRZ015NW9D6WTY6VAF3X", "01KA9DTZP6CXGRSSBYCJDZAZ1R", "01KA9DV5RV8QWF541JD3DXCVE0"]
label_names: ["IA", "intelligent_acceptance", "elegibility", "requirements"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

Use this guide to understand the specific criteria a merchant must meet to be eligible for the **Intelligent Acceptance** (IA) solution. Following these guidelines ensures that onboarded merchants are likely to see a measurable benefit and return on investment (ROI) from IA.INTELLIGENT ACCEPTANCE CRITERIA 💬

Merchants should meet the following criteria to be considered a good candidate for Intelligent Acceptance:

- 
**Processing Volume:** Must have **more than 50,000 payments per month**.

- 
**CKO Acquired Volume:** **At least 70%** of the merchant's payment volume must be acquired by Checkout.com.

- 
**Geographic Concentration:** **Less than 70%** of the merchant's traffic should be concentrated in the **MENA, APAC, or NORAM** regions.

- 
**Traffic Type:** **Less than 30%** of the merchant's traffic should be Merchant-Initiated (MIT) or recurring.

**Rationale (Why) 🤔**

| Criteria | Rationale |
| --- | --- |
| **Low Volume** | Makes it difficult to gather statistically significant data, delaying the proof of IA's value and ROI. |
| **High Regional Concentration** | Limits the ability to drive ROI in regions where historical performance has been less optimized. |
| **High Recurring Volume** | Currently, fewer optimizations are applicable to MIT/recurring traffic, making a measurable impact difficult. |

TOOLING**📍**

| Tool | Access |
| --- | --- |
| ****[Data explorer](https://retoolprod.mgmt.ckotech.co/apps/81c167c4-7d39-11ec-86c4-73d37fb76d07/payment-performance-shared-support/Data%20Explorer) is used to analyze merchant processing volume and traffic breakdown | - Access granted via [Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/296/create/274)   - Application : Retool prod   - Environment: Data-Explorer-Editors |

 

**How to Check Eligibility 👀**

Use the criteria above for initial merchant qualification, Account Managers (AMs) should carry out due diligence as they have the best understanding of their merchants' requirements.

Use **Data Explorer** to check the merchant's current traffic breakdown:**Processing Volume (Transaction Count)**

- Open Data Explorer and select the merchant 

- Select a monthly date range

- Click “Get Data” and analyze the **"Transaction Count"** metric

 

 ** Checkout.com Acquired Volume**

- Go to the **"Acceptance Exploration"** tab

- Select **ACQUIRER_SETUP**.

- Click **"Update"**, then select **"Show percentages"** below the chart

 ** Geographic Region Eligibility**

- In **"Acceptance Exploration,"** select **"Issuing region"** from the breakdown dropdown

- Click **"Update"**, then select **"Show percentages"** to check the distribution

**Check MIT traffic**

- In **"Acceptance Exploration,"** select **"IS_MERCHANT_INITIATED"** from the breakdown dropdown

- Click **"Update"**, then select **"Show percentages"** to check the MIT distribution

## Intelligent Acceptance Eligibility FAQs ❓

Here are the answers to common questions about merchant eligibility for Intelligent Acceptance (IA), additional FAQs can be found [here](https://checkout.atlassian.net/wiki/spaces/ARM/pages/6519193782/Documentation+for+Intelligent+Acceptance#3.-Eligibility-for-IA%3A-which-merchants-benefit-the-most-from-being-on-IA%3F).

 

### What happens if I onboard an ineligible merchant?

It's highly likely you won't be able to report on any Acceptance Rate (AR) boost data due to a lack of statistical confidence.

- This results in a poor merchant experience and jeopardises future conversion and retention.

- The Intelligent Acceptance team will also be limited in the support they can provide for these merchants.

 

### Does meeting the criteria guarantee IA will perform well?

No. Passing the eligibility check is an initial sanity check, not a guarantee of performance. A merchant's specific payment setup can still prevent their traffic from being optimised by the IA solution.

 

### Can a merchant's eligibility change over time?

Yes. A merchant's eligibility can change due to shifts in their business:

- Volume: Changes in monthly payment volume.

- Traffic Mix: A shift in their regional traffic mix (e.g., more or less MENA/APAC/NAM traffic).

- Business Model: Changes to their business model (e.g., higher or lower percentage of MIT/recurring traffic).

Eligibility criteria may also be updated by the IA team as the solution's optimization capabilities expand to cover more types of traffic.

 

### RELATED ARTICLES ⭐

- [Intelligent Acceptance: Product Overview](https://checkoutint.zendesk.com/hc/en-us/articles/29824626205202-Intelligent-Acceptance-IA-Product-Introduction)

- [Troubleshooting: Data Explorer Access and Usage](https://checkout.atlassian.net/wiki/spaces/ARM/pages/7361527859/Who+can+be+on+Intelligent+Acceptance)

- [Guide: Best Practices for High-ROI Merchant Onboarding](https://checkoutint.zendesk.com/hc/en-us/articles/29835307864338-Configuring-a-Merchant-for-Intelligent-Acceptance-IA)
