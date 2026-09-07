---
id: 22435576035090
section_id: 22329315187858
title: "Getting Your Reports"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22435576035090-Getting-Your-Reports"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-23T10:37:06Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQBAM2Q5EGSKD3634VFBT"]
label_names: ["global", "case_reports", "alternative_solutions_for_report_downloads", "report_download"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

To see the various ways you can retrieve transactional or financial data, including internal tools (Looker, Datadog) and a merchant-facing API method (Postman) that bypasses the dashboard's one-month download limit.

**Problem:** Merchants or internal teams need to retrieve transactional data, potentially beyond the dashboard's one-month limit.

## DESCRIBE THE ISSUE 💬

A merchant or agent needs access to large volumes of transactional, financial, or historical data/reports that they cannot easily get directly from Dashboard. This is often because the dashboard download is limited to one month of data. 

## KEY TAKEAWAYS 🔑

- Reports from the dashboard are limited to **one month of data** and are downloaded in **CSV format**.

- 
**Postman (API)** is the primary non-dashboard method for **merchants** (especially T1-T3) and internal users to retrieve data, offering **no one-month data limitation**.

- 
**Looker** is an internal tool best for accessing **historical data**.

- 
**Datadog** is an internal tool primarily used in **incident scenarios** to extract and share "affected transaction" data with merchants.

- Key reports available via internal tools (Looker/Datadog) include Pay to Card, Reconciliation, Cost of Sales, and Financial Action Reports.

**INTRODUCTION TO API 💬**

An **Application Programming Interface** (API) allows different software systems to communicate with each other. It sets the rules and protocols for accessing a web-based software application or tool.

Postman is a useful tool for developing and testing APIs. It helps developers create, test, document, and monitor APIs by making it easier to send HTTP requests and check responses.

Using an API with Postman means working with an Application Programming Interface through Postman, a popular tool for testing and managing APIs.POSTMAN ✉️

🎓 Postman Training Links

- [Postman Self-paced Learning](https://academy.postman.com/page/self-study-learning)
Using Postman to Interact with an API

- Sending Requests:

  - GET Requests: Used to retrieve data from an API

  - POST Requests: Used to send data to an API

  - PUT/PATCH Requests: Used to update an existing resource on the server

  - DELETE Requests: Used to delete a resource on the server

- Building a Request:

  - URL: Enter the endpoint (URL) of the API.

  - Method: Select the HTTP method (GET, POST, etc.).

  - Headers: Include any necessary headers (e.g., Authorization, Content-Type).

  - Body: For POST/PUT requests, include the data payload (JSON, form data, etc.).

- Running the Request:

  - Click "Send" to execute the request. Postman will display the response, including the status code, headers, and body.

- Analyzing the Response:

  - Check the status code (e.g., 200 OK, 404 Not Found).

  - Review the response body to see the data returned by the API.

  - Inspect headers for additional information (e.g., content type, caching).

Advanced Features in Postman

- Collections: Organize your requests into collections for better management and documentation.

- Environments: Set up environments (e.g., Development, Production) to easily switch between API setups.

- Testing and Automation: Write tests in JavaScript to automate the validation of API responses.

- Mock Servers: Create mock APIs to simulate API responses for testing purposes.

- Collaboration: Share collections and environments with team members for collaborative development.

See how to [download reports via Postman](https://api-reference.checkout.com/#tag/Reports) by taking the following API Reference  
 **CREATE A PROJECT VIA API ☑️**

| **Procedure** | **Screenshot** |
| --- | --- |
| - Contact IT and Download [Postman](https://www.postman.com/downloads/) on your laptop. |  |
| Create a payload request on Postman and name it.   - Click on the **+ sign** and select **Blank Collection**   - Name the project |  |
| A “New Collection” will pop under. |  |
| - Click in the request 3 dots (setting) and Add the request  - Name the request |  |
| This is Project creation steps. You can create as many requests as per your project |  |

### **Create a Request under a Project**

Please refer to the [API Documentation reference](https://api-reference.checkout.com/#tag/Reports) to build your project

| Documentation | Guide |
| --- | --- |
| - Rename your Request |  |
| - Type of Method = “Get” |  |
| Refer to [API Documentation reference](https://api-reference.checkout.com/#tag/Reports) to look for the API URL.       - [Sandbox](https://api.sandbox.checkout.com/reports)  - [Production](https://api.checkout.com/reports) |  |
| Under Headers, configure the following: **Key: Authorisation** **Value: (Your account secret key generated).** |  |
| Once you have set the details, you run the request by clicking on Send. You will retrieve all report IDs and file IDs from the beginning of the merchant’s processing. |  |
| You can download a particular report file id as follows in CSV format. |  |
| You can now download the report in CSV format |  |

**LOOKER 👀**

Looker is a business intelligence (BI) and data analytics platform that helps organizations explore, analyze, and visualize their data. It’s built to help businesses better understand their data and support making informed decisions based on that data.

## 🎓 Looker Training Links

- [Looker Basics](http://checkout.csod.com/samldefault.aspx?ReturnURL=%252fDeepLink%252fProcessRedirect.aspx%253fmodule%253dlodetails%2526lo%253dea1ebb19-a193-4957-9b07-52ed35e6b75f)

- [Internal Looker Guides](https://checkout.atlassian.net/wiki/spaces/BI/pages/4795532234/Looker)

- [Using Custom Fields in Looker Explores](https://www.cloudskillsboost.google/focuses/22212?parent=catalog&path=28)

- [Creating a Looker Modeled Query and Working with Quick Start](https://www.cloudskillsboost.google/focuses/22176?parent=catalog&path=28)

- [Optimizing Performance of LookML Queries](https://www.cloudskillsboost.google/focuses/22355?parent=catalog&path=28)

- [Prepare Data for Looker Dashboards and Reports](https://www.cloudskillsboost.google/paths/28/course_templates/628)

- [Understanding LookML in Looker](https://www.cloudskillsboost.google/paths/28/course_templates/774)

- [Applying Advanced LookML Concepts in Looker](https://www.cloudskillsboost.google/paths/28/course_templates/665)

- [Analyzing and Visualizing Data in Looker](https://www.cloudskillsboost.google/paths/28/course_templates/323)

- [Developing Data Models with LookML](https://www.cloudskillsboost.google/paths/28/course_templates/327)

|  |
| --- |
| [Extract Payments IDs via Client details (NAS)](https://checkoutinternal.eu.looker.com/explore/payment_lifecycle/fct_payin_event?qid=bH7xSSsTmEyp6cgofjWR7D&origin_space=undefined&toggle=fil) |
| Cost of Sales - Async & NAS Adjustment##    **Purpose:** These two interconnected tools, **Cost of Sales - Async** and **NAS adjustment**, are used to investigate the underlying reasons for manual billing and adjustments.   -  **Cost of Sales - Async:** This report focuses on asynchronous billing fees, helping to pinpoint scenarios where automated billing processes may have been bypassed or where specific fee structures apply that require manual intervention.  -  **NAS Adjustment:** This tool provides insights into adjustments allowing for a detailed examination of why these adjustments were necessary. This helps in identifying process gaps or system limitations that lead to manual interventions.  This tool offers detailed insights into adjustments, helping identify process gaps or system limitations that necessitate manual interventions.  -  **Access:** [Cost of Sales - Async](https://checkoutinternal.eu.looker.com/explore/oracle_prod/async_billing_fee_report?qid=pqI3A3utsPLHyYOTjwd70H&origin_space=1797&toggle=fil) and [NAS adjustment](https://checkoutinternal.eu.looker.com/explore/nas_adjustments/lightning_adjustments_aggregate) |
| [Decline Analysis](https://checkoutinternal.eu.looker.com/dashboards/10013?Requested+Date=2+week&PoP+Visualisation=week&Alias=&Decline+Code=) |
| Financial Action Report##    **Purpose:** This report offers a detailed financial breakdown, helping merchants understand transaction charges and credits. It's ideal for large transaction volumes that are difficult to manage directly from the Dashboard.  -  **Access:** [Financial action report](https://checkoutinternal.eu.looker.com/explore/nas_adjustments/lightning_adjustments_aggregate) |
| NAS: Processing Channel Settings##    **Purpose: **This tool verifies configuration settings across processing channels, good for troubleshooting transaction routing, fee application, and other processing parameters.  **Access:** [NAS: Processing Channel Settings](https://checkoutinternal.eu.looker.com/explore/client_admin_tool/processing_channel_settings) |
| Pay to Card##    **Purpose:** It allows users to identify critical trends, anomalies, and specific data points concerning Pay to Card transactions. This is essential for fraud detection and understanding the performance of these payment methods.  -  **Access:** [Pay to card](https://checkoutinternal.eu.looker.com/explore/payment_lifecycle/fct_pay_to_card) |
| Reconciliation Report##      -  **Purpose:** The **Reconciliation Report** is vital for confirming the successful receipt of funds and the completion of refunds, particularly for Alternative Payment Methods (APMs) such as Sofort and PPRO.  -  **Access:** [Reconciliation report](https://checkoutinternal.eu.looker.com/explore/bank-integrations/reconciliation_report) |

**NAVIGATING LOOKER 👀**

| - Access Looker Dashboard: [https://checkoutinternal.eu.looker.com/browse](https://checkoutinternal.eu.looker.com/browse)   - Always build your dashboard for reports in your “My Folder” to keep it clean. |  |
| --- | --- |
| - Click on New to create new project > Edit > Add > Visualisations  - You get to explore the various report themes you can create  - Choose any Report Theme   - Example: Payin Event |  |
| - Red - you can rename the dashboard  - Green - These are the fields you can populate in your report columns and use as filters to streamline your research |  |
| - A single click on the field would populate the same as a column in the dashboard - Data  - A single click on the field inverse triangle  sets this field as criteria to filter.     [Build your customised report](https://checkoutinternal.eu.looker.com/explore/payment_lifecycle/fct_payin_event?qid=bH7xSSsTmEyp6cgofjWR7D&origin_space=undefined&toggle=fil) |  |
| Once your report has populated the Data and is ready for extraction, you can download the same in a CSV format   - Click on Settings (Top Right corner)    - Download  - Format > per your requirement  - Filename > Rename  - Results > As displayed in the data table  - Unformatted  - All Results |  |

DATADOG 👨🏼‍💻Datadog is used to monitor cloud-based applications alongside allowing the ability to monitor servers, databases, tools and services we provide.

## 🎓Datadog Training Links

-  [Datadog Cheatsheet](https://checkout.atlassian.net/wiki/spaces/SE1/pages/5912070037/Datadog+Cheat+Sheet)

- [Datadog Foundation](https://learn.datadoghq.com/courses/datadog-foundation)

- [All Datadog Courses](https://learn.datadoghq.com/collections)

| **Documentation** | **Process** |
| --- | --- |
| On your Okta, look for Datadog |  |
| Click on “Go to…” and select “Logs” |  |
| The Log Explorer will populate where you can begin your investigation. |  |
| You can now build your Datadog extract dashboard. |  |
| **Template Hyperlink** | **Resource** |
| [Template Via Payment ID](https://app.datadoghq.com/logs?query=%40Properties.CkoClientId%3Acli_xmtkoehlt45epamy7fvurswone%20%40Properties.ApplicationName%3A%22Gateway%20API%22&agg_m=count&agg_m_source=base&agg_t=count&cols=%40Properties.CkoClientId%2C%40Properties.MerchantName%2C%40Properties.MerchantId%2C%40Properties.PaymentId%2C%40GatewayResponseCode%2C%40GatewayResponseCodeDetails.Description%2C%40Properties.Response.Status%2C%40Properties.AcquirerId&fromUser=true&index=processing&messageDisplay=inline&refresh_mode=sliding&saved-view-id=88535&storage=hot&stream_sort=%40Properties.CkoClientId%2Casc&viz=stream&from_ts=1721665298408&to_ts=1722270098408&live=true) | You can extract the details via a Payment ID. |
| [Template Via Client ID](https://app.datadoghq.com/logs?query=%40Properties.CkoClientId%3Acli_4fzzcmoq5sru7oo6owfeqt5vcm%20%40Properties.StatusCode%3A200&agg_m=count&agg_m_source=base&agg_t=count&cols=service%2Cenv%2C%40http.status_code%2C%40ActionName%2C%40PaymentId%2C%40Properties.Response.source.scheme&fromUser=true&index=processing&messageDisplay=inline&refresh_mode=sliding&saved-view-id=88535&storage=hot&stream_sort=%40PaymentId%2Casc&viz=stream&from_ts=1604422833802&to_ts=1607014833802&live=true) | You can extract the details via a Client ID. |
| Once your report is populated, you can download it in CSV format. |  |
