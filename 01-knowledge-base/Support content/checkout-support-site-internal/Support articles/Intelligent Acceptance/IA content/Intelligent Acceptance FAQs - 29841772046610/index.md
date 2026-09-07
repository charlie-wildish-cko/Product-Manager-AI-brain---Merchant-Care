---
id: 29841772046610
section_id: 29824613373714
title: "Intelligent Acceptance FAQs"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/29841772046610-Intelligent-Acceptance-FAQs"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-12-02T13:18:44Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTZ6WEQ3S7TQ9KW35WKJXPDX", "01K6AASRZ015NW9D6WTY6VAF3X"]
label_names: ["FAQ", "Intelligence_acceptance"]
user_segment_ids: [11003606966930]
archive: false
---

Use this article for frequently asked questions on the** Intelligent Acceptance **product

## 

## GENERAL FAQs⁉️

What types of optimizations does Intelligent Acceptance apply? 

Intelligent Acceptance applies and combines multiple types of optimizations, which can be broken down into two categories:

- 
**Pre-processing features** modify payments before they are sent to schemes and issuers. These include:

- 
**Messaging**: Optimizing data and formatting to meet the latest scheme and issuer preferences.

- 
**Routing**: Finding the best path for each transaction based on your business goals, cost, and conversion.

- 
**Network Tokens**: Continuously testing for issuer token adoption and balancing cost and conversion.

- 
**SCA 3DS**: Determining if Strong Customer Authentication (SCA) is needed, including relevant information, and selecting the best-performing protocol and exemptions

- 
**Post-processing features** happen in case of a decline

- 
**Retries**: Automatically recovering lost transactions in real time based on the probability of success.

What criteria must a merchant meet to be eligible for Intelligent Acceptance?

To be considered a strong candidate for Intelligent Acceptance, your merchant needs to meet several key criteria: they should process **more than 50,000 transaction payments per month**; at least **70% of their acquire volume** should be processed by Checkout; they need a **70% geographical concentration** outside of the **MENA**, APAC, and North America regions; and **less than 30% of their transactions** should be Merchant-Initiated Transactions (MIT) or recurring. You should be aware that low transaction volume makes statistical measurement difficult, regional concentration affects performance, and high recurring volume limits optimization opportunities.Which tools should I use to check a merchant's eligibility for Intelligent Acceptance?

You can use any tool you are comfortable with, such as **Looker** or the merchant dashboard, but **Data Explorer** is the recommended tool as it allows you to check all the criteria within a single platform. You check eligibility using the **merchant's name** (not their ID) and by selecting a relevant period to retrieve the data. The tool allows you to check **acquisition volume** (e.g., transactions acquired by Checkout) and the issuing region.What is Merchant Care's role regarding Intelligent Acceptance eligibility?

Checking eligibility is primarily the **commercial stakeholders' responsibility**. Your role in Merchant Care is mainly **advisory** or to conduct **sanity checks**. You might receive tickets from commercial teams needing confirmation before onboarding a merchant. Checking a merchant’s eligibility can also help you determine if missing dashboard data (like the first attempt metric) is because the merchant was never eligible for the program.Can I give a merchant an estimate of the performance boost they will receive from Intelligent Acceptance?

No, you should not provide performance estimates or benchmarks, as the results are highly variable for every merchant. When a ticket requests estimates, your primary action should be to explain the **unpredictability** or suggest a **risk-free trial**. If a commercial partner strongly insists, you can escalate the request to the **IA team**. You can, however, explain the different strategies (e.g., 3DS, network tokens) but must avoid providing specific estimates due to the high variability and risk of misrepresenting potential gains.What is the recommended configuration strategy for Intelligent Acceptance?

The recommended strategy is to set Intelligent Acceptance to **100% of the merchant's traffic**. The available strategies include a **default AI** for simple needs and **custom options** for scenarios like a 3DS upgrade or no 3DS. Any changes to the configuration require a **Merchant Change Request (MCR)**.How do I validate a merchant's bill for Intelligent Acceptance?

Billing issues should primarily be addressed by the Billing team, but you can perform a basic validation. Intelligent Acceptance is billed **per transaction**, regardless of the number of optimizations applied. You should use the **Intelligent Acceptance Retool app** to check the number of optimized transactions. You can then locate the **unit price** (fee) in **CAT** (often at the entity level) and multiply it by the number of optimized transactions to validate the bill statement. If your validation shows an incorrect amount, the ticket should be escalated to the Billing team.Which transactions are charged for Intelligent Acceptance?

You are charged for transactions as long as **one optimization has been applied**. Transactions that were part of the **control group** are **not charged**. Additionally, transactions that are not eligible for optimization are also **not charged**.What data can I share with merchants from the Intelligent Acceptance dashboard?

You can share **anything visible on the merchant dashboard**. For more specific reports, such as transaction optimization data, you should direct the account manager to use the **Retool app**. It is advisable to share "**reattempt gains**" with merchants as this data is considered more confident than the overall Acceptance Rate (AR) boost. The **IA team** plans to show first attempt and retries separately on the dashboard, possibly in Q1.

## INTELLIGENT ACCEPTANCE TRIAL FAQs ⁉️

How does a merchant know how the trial is going?

- If the merchant has recently been onboarded (within the last day or week), there might not be enough volume processed through IA yet to fully assess how the process is going.

- While it's understandable to want to display data as soon as possible, showing information before we’re confident that the results are relevant and consistent has sometimes led to merchants feeling unsure when the data changes frequently.

- If you need a report of transactions optimized since onboarding, you can get it through the [Intelligent Acceptance Retool](https://retoolprod.mgmt.ckotech.co/apps/4ae2daa2-093e-11ee-a791-974ccad006a0/payment-performance-shared-support/Intelligent%20Acceptance).

- The FAQ document offers detailed information on how to use and interpret the Intelligent Acceptance Retool. 

## TECHNICAL/STRATEGY FAQs ⁉️

What is the difference between Intelligent Acceptance (IA) and Integration Health?

**Integration Health** is a separate product that focuses on issues related to **data quality, poorly-formed payment requests, and API integration problems**, assigning a score based on error types. Its goal is to help merchants fix the health of their payload integration. **Intelligent Acceptance (IA)**, conversely, uses algorithms to **learn what works** for different payment types, making decisions and changes to the payment payload to increase the acceptance rate. They are two distinct approaches, both aiming to increase the Acceptance Rate (AR).How is the Acceptance Rate (AR) defined within the Intelligent Acceptance product?

The Acceptance Rate (AR) for Intelligent Acceptance is defined as **accepted payments divided by the total payments that went through the gateway**. This is the standard company and merchant-level measurement. You should be aware that merchants may occasionally exclude specific decline codes or flows from their own AR calculations.Why are not all of a merchant's transactions eligible for Intelligent Acceptance optimization?

Not all transactions are eligible for IA optimization because the system is **unable to "touch" or change certain payments** at the routing, ISO, or 3DS level. A key exclusion is **Third-Party Acquiring (TPA) transactions**. If a merchant has too high a proportion of TPA traffic, they are generally not considered eligible for IA. Even if a merchant permits 100% of their traffic to be charged by IA, only the eligible percentage will actually be optimized, and a **10% control group** is maintained from the eligible traffic.How is the 'boost' calculated and displayed on the Intelligent Acceptance dashboard?

The IA tab on the dashboard only shows the traffic that was **optimized by IA**. The displayed boost is calculated **relative to the merchant's total traffic Acceptance Rate (AR)** over a period (e.g., a year). The boost indicates the specific percentage increase of the total AR for which IA was responsible.What is the significance of the 10% control group in Intelligent Acceptance?

The control group is essential for measuring the impact of IA. Ideally, a test group and a control group should have the same size for accurate comparison. However, as merchants want most of their traffic optimized, the control group is kept small (typically 10% of eligible traffic). When the control group is very small, especially with low-volume merchants, it introduces more variation, making it difficult to measure the impact accurately.What information about optimized transactions can I share with Account Managers using the Retool extract?

The Retool extract provides a payment-level list of transactions that went through IA. The data includes the processing channel, entity, whether it used network tokens, if it was a retry, and the gateway response codes. It also includes a **'services' column** listing the general name of the IA service performed, such as "routing" or "adaptive messaging". You should **not share specific optimization names, actions, or IDs** as this constitutes backend intellectual property.Are transactions that only go through fraud optimization considered IA-optimized?

No. If a transaction only goes through a **tenet** fraud optimization, it does **not count as an Intelligent Acceptance-optimized transaction**. These are baseline services for all merchants to ensure fraud is contained. Therefore, they will not be included in the transaction extraction list, nor will they be charged. If a transaction goes through both fraud optimization and an IA service (like routing), it is counted as an optimized transaction, but only the IA service name (e.g., "routing") will be listed in the extract.Why is the Retool transaction extract limited to the last 7 days?

The limit is in place to manage the **Retool application's data volume limitations** (specifically, a 500-megabyte limit). For large merchants, requesting a longer period would often cause the extract to fail. By default, it is limited to the last 7 days to ensure users can get at least a partial extract. For data requests exceeding 7 days, you should advise the account manager to break the request into smaller chunks or use tools like **Snowflake or BigQuery** for bulk extraction.ADDITIONAL FAQs ⁉️

[IA Product Team FAQs](https://checkout.atlassian.net/wiki/spaces/ARM/pages/6217596945/Intelligent+Acceptance+Frequently+Asked+Questions+from+Account+Managers)
