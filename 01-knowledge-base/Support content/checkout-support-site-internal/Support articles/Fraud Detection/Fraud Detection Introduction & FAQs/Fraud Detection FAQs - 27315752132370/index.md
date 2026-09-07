---
id: 27315752132370
section_id: 27310328238098
title: "Fraud Detection FAQs"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/27315752132370-Fraud-Detection-FAQs"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-03-18T16:18:45Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRPZZM25CJTKMYW0WZXMXX"]
label_names: ["faqs", "Fraud Detection"]
user_segment_ids: [11003606966930]
archive: false
---

Use this article for frequently asked questions about fraud Detection, you can head to the **#ask-fraud-detection** channel on slack if your question is not here

**General & Product Questions 📦**What is the difference between the basic Fraud Detection and Fraud Detection Pro?

| Feature | Fraud Detection (Basic) | Fraud Detection Pro |
| --- | --- | --- |
| **Cost** | Free | Paid |
| **Primary Audience** | SMEs and merchants without a tangible fraud problem. | Enterprise merchants with internal fraud teams. |
| **Strategy Control** | Comes with a pre-configured risk strategy. Merchants can make limited changes to rules. Basic merchants can only add or remove pre-set rules. | Provides full control to create and modify the risk strategy. Pro merchants can create rules, lists, and risk profiles. |
| **Rule Customization** | Some rule changes, like velocities and blocked countries, are locked and require contacting the risk team to modify. | Unlocks greater customization and allows for the creation of free form custom rules. |
| **Strategy Builder** | Cannot perform segmentation in the risk strategy. | Features a decision tree strategy builder for segmentation. |
| **Advanced Features** | Does not include features like weighted rules (Risk Profiles) or back-testing. | Includes exclusive features such as Backtesting Weighted rules (also known as Risk Profiles) Advanced velocity rules like "Network count velocity" and "Cumulative spent velocity" Shadow-mode for testing strategies |

What types of transactions do these services apply to?

Fraud Detection and Fraud Detection Pro can only be used for transactions processed by Checkout.com. The solution works exclusively for online card payments, which includes all card schemes as well as Apple and Google Pay.Which regions is this product available in?

In all regions where Checkout.com processes transactions.Can Fraud Detection be sold as a standalone product?

No. Fraud Detection only works for transactions processed by Checkout.comWhat payment methods does Fraud Detection work for?

Online card payments only (all schemes, including Apple Pay and Google Pay).How should you respond if a merchant's fraud rate appears unexpectedly high despite a normal total fraud amount?

You should look for transactions that were seen by the fraud detection system but rejected before a payment was created (e.g., 422 errors due to unconfigured payment methods). If the variance remains unexplained, you must raise a ticket for a detailed investigation into the specific calculation.

 

**Access & User Permissions 🔓**How can a merchant test Fraud Detection Pro?

- Merchants are on Pro on Sandbox by default so can test the product there.

- They can access Fraud Detection Pro in sandbox, via dashboard or Hub.

How many team members can have an account?

- Merchants can have as many accounts as they want. An admin can specify which accounts have permission to edit the risk strategy.
Where can I view an audit log of a merchant's rule changes?

An **audit log** exists for client-level rule changes in the **Prism Audit Tool**. This log records when a rule was added, updated, or deleted, as well as when a **'live strategy updated'** event occurred (which is when a change is promoted from a test to a live environment).What does the padlock icon signify next to a rule or list in the merchant dashboard?

You should inform the merchant that a padlock means the associated list or rule cannot be removed from their strategy without internal intervention or compliance approval. However, the merchant can still typically update or edit the entries within that list itself.

 

**Webhooks & Integrations ⚙️**What issues have been identified with the fraud reported webhooks?

You may encounter two known bugs with the fraud reported webhooks: an **incorrect currency display** (e.g., USD amounts incorrectly showing as SGD) and **switched values** where the fraud amount appears in the payment object and the payment amount appears in the fraud object.Where does the data for the `fraud_reported` webhooks originate?

The data for the fraud reported webhooks is sourced from the **"core.fraud" table in Snowflake** which is owned by the **Data Analytics team**.Why might iOS integration not work in sandbox, even though web integration works for `risk.js`?

The issue appears to be related to the **configuration endpoint** for the iOS integration in the sandbox environment. This could be due to a change in the configuration endpoint which may have unintentionally affected the iOS package. You can raise a ticket to **Fraud Detection L3** to check further.What is the purpose of the 'Device Provider ID' in the API, and does it validate device details?

You should understand that this ID is purely used for collecting analytical data to identify which third-party providers (like Riskified) your merchants are using. It does not retrieve or validate device details; the only validation performed is a string length limit of 128 characters.What should you do if a risk.js standalone integration intermittently fails to retrieve the device session id?

You are advised not to block payments solely because a risk.js retrieval fails intermittently, as browser behaviours can be unpredictable. You should inform the merchant that stopping a transaction because the risk.js response is empty is not recommended integration logic and will likely lead to unnecessary payment friction.

 

**Strategy & Rules 🎯**What are Checkout.com Risk Scores and how are they calculated?

Risk scores are Checkout.com's **assessment of the fraud risk** level for a **customer-initiated transaction (CIT)**. They are numerical values ranging from **0 to 100**. The scores are generated by **powerful machine learning models** trained on our extensive global payments and fraud data, allowing them to accurately predict the likelihood of a transaction being fraudulent.How should I interpret the risk score scale?

The score you receive indicates the risk level according to these standard thresholds:

| **Risk Category** | **Score Range** |
| --- | --- |
| **Low Risk** | 0 – 30 |
| **Medium Risk** | 31 – 69 |
| **High Risk** | 70 – 100 |

Is it possible to test changes to a strategy before they go live?

- Yes, all merchants are encouraged to use the "Test Strategy" feature. This allows a user to run a different risk strategy in shadow mode to compare its results with the live strategy.
Is there a limit on the number of rules in a strategy?

The maximum length for a single branch in the decision tree is 30 rules, but the tree can have more than 30 as long as they're on separate branches. Alternatively, using ‘OR’ will allow you to combine multiple rules into a single one, but will mean less precision when analysing what triggered a decline for a given transaction.What should you do if a merchant removes an entry from a blocking list, but payments are still being blocked?

You should investigate if there is a discrepancy in the entry count between the portal database and the read-optimized database used at payment time. This can be caused by a broken replication queue or legacy case-sensitive values remaining in the system. You must raise a ticket for an engineer to manually remove the legacy entries.Is it recommended for merchants to use their own cards for testing in the production environment?

You should advise merchants that while testing in production is possible, they must accept that their cards may be blocked by global security rules, such as scheme compliance or bin attack prevention. Relaxing these rules for test cards is generally avoided as it creates security vulnerabilities.Can a merchant use specific properties to differentiate Google Pay transactions (e.g. 'pan type')?

No, there are currently no plans to add new properties for differentiating Google Pay transactions based on FPAN. You should inform the merchant that all currently planned properties have already been implemented, and they should rely on existing fields for their risk strategy.How are time intervals calculated for velocity rules (e.g. a 24-hour rule)?

You should understand that velocity rule intervals are not fixed; they are specific to each payment. The count begins from the moment the first payment is made that triggers the rule, and the system then buckets subsequent payments into blocks (such as 10-minute intervals) based on that initial start time.

 

**Machine Learning 🤖**What data is the Machine Learning model trained on?

- The model is trained on captured transactions where CKO is the acquirer, which is about 70% of all transactions.

- This data includes "chargebacks incorrectly allowed through" (false-negatives) as well as transactions that were retried and eventually captured.

Why is the machine learning (ML) fraud score low when a specific fraud rule declined the transaction?

The ML model currently does not incorporate all the complex features and velocity checks that are used in the main rule sets. Therefore, a rule can decline a transaction based on a criterion that the ML model is not yet trained to assess, resulting in a discrepancy between the rule decision and the ML score.

 

**Analytics & Reporting 📊**How frequently is the data in analytics and reporting updated?

- The data is refreshed every day at 00:00 UTC. The product team is working to reduce this refresh time to one-hour intervals.
Why might a merchant see a 404 error or a lack of events in 'Fraud Insights' for a recent payment?

You should first check for ongoing data pipeline incidents, specifically regarding Snowflake or BigQuery. If an incident is active, the data required for Fraud Insights may be delayed or missing. You should advise the merchant that data will be backfilled once the incident is resolved.Why are Fraud Detection reports appearing empty via SFTP?

You should first check for broader data incidents (such as BigQuery or Snowflake loading issues) which can cause missing chargeback or refund events. While the underlying data is managed by the product team, the SFTP upload mechanism itself is handled by Data Analytics; you should check the active incident channels if reports remain empty.

 

**Back Testing and Shadow Testing 🧪**What is back testing?

Back testing involves applying a new rule to past traffic, typically from the last three months, to evaluate its potential impact. While you can specify a time frame, this method may not be entirely accurate because it doesn't account for real-time system changes like velocity shifts.What is shadow testing?

Shadow testing is a more accurate method where a new strategy runs simultaneously with the current live strategy. The two strategies are then compared to see the difference in outcomes. This method provides a more accurate representation of how the new rule will perform, although it cannot predict future changes like seasonal shifts.What does the "unchanged" status mean in the shadow testing dashboard?

The "unchanged" status indicates that the outcome of a transaction (e.g., accepted or blocked) is the same under both the live strategy and the new test strategy.Why are inactive rules appearing to trigger during a back test?

You should verify if the rule is currently present in one of the merchant’s test strategies. The backtesting system may include rules that are part of their test strategy on both a client and entity level, even if they are not currently active in the live production environment.Why is the data in the sandbox environment not matching production results during back testing?

You should advise the merchant that the sandbox environment is intended only to demonstrate the user experience of the testing tools. It uses mock data and does not store information in the same source tables used for production backtesting, so the results will not be accurate for data analysis.

 

**Risk Response Codes ℹ️**When were descriptive risk response codes implemented?

Descriptive response codes were implemented on July 11, 2025 for all merchants; instead of receiving risk decline response code 40101, merchants will now see more granular response codes such as 43201.Why are merchants seeing an increase in transactions declined with 43102?

The increase in 43102 declines is expected behaviour and is directly related to the change to have more descriptive response codes rather than just 40101. Transactions that were previously declined with a 40101 code are now being declined with the more specific 43102 code, which shows the true reason for the decline.
