---
id: 22857186805650
section_id: 28482948435346
title: "Transaction Declined due to Timeout"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22857186805650-Transaction-Declined-due-to-Timeout"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-31T16:59:08Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JNGXCVNHFQB2TX90T7Z1YKMZ"]
label_names: ["global", "issuing", "case_card_issuing", "case_card_issuing_transaction_declined_due_to_timeout"]
user_segment_ids: [11003606966930]
archive: false
---

## Process Steps

1. The information that you require from the client for this issue is:

  1. A description of what has happened in Dashboard

  2. The Card ID

  3. The Transaction ID (if possible)

2. Explore the following with the client or cardholder:

  1. Understanding the error message shown on the website

    1. Request the cardholder to provide the exact error message they saw on the website or terminal (e.g. "Transaction Timeout" or "Request Timed Out")

    2. Log in to Dashboard and navigate to Issuing > Transactions or the Payments section to locate the declined transaction

    3. Look for any error codes or notes in the logs indicating a timeout. Timeout issues may show up as a specific error message in the transaction details

  2. How many times did the client try the transaction?

    1. Use the Transaction Logs in Dashboard to identify how many times the cardholder attempted the transaction. Each attempt will be recorded with a unique timestamp

    2. Look for repeated attempts within a short period, which may indicate a timeout or retry issue. Note if these retries happened with the same merchant or across different merchants.

3. Further troubleshooting can be done using Retool and DataDog:-

  1. DataDog

    1. Log in to [Datadog](https://app.datadoghq.com/logs?query=source%3Aissuing%20env%3Aprod%20-status%3Adebug%[%E2%80%A6]=stream&from_ts=1685348700811&to_ts=1685424008919&live=false), insert the Transaction ID into the "Search for" tab and run the query to see transaction details such as status and reasons

  2. Retool

    1. Log in to [Retool](https://retoolprod.mgmt.ckotech.co/apps/issuing/Issuing%20internal%20tool%20prod), click on "Transactions", enter the transaction ID in the search box and click on "Search" to see the transaction status

    2. Scroll down to “Events timeline” to see the decline reason. If you would like to check the transaction in DataDog (provided it is less than 2 weeks old) click the "View in DataDog" button and it will take you to the specific transaction automatically

4. If the authorisation relay (response back from the client end) has timed out, that is why the transaction is declined. Check with the client if there are any issues on their end

  1. Steps the client could take:-

    1. Check System Response Time: Ensure the client’s system is configured to respond to authorisation requests within the required timeframe (typically less than 5 seconds)

    2. Monitor and Resolve Latency: Identify any network latency or server performance issues that might delay responses. Recommend the use of |loggin and monitoring tools to pinpoint bottlenecks

    3. Retry Mechanism: Implement a retry mechanism in case the initial relay fails or times out. Ensure retries comply with card scheme rules to avoid duplicate authorisations.

    4. Review Endpoint Configuration: Confirm that the endpoint receiving Checkout’s authorisation requests is configured correctly and can handle the expected load.

    5. Enable Logging for Debugging: Log all incoming authorisation requests and responses to debug and identify the root cause of the timeout

    6. Ensure High Availability: Use a load balancer or failover mechanism to ensure high availability of the client’s endpoint during peak times or maintenance

  2. Steps we could take at Checkout:-

    1. Review logs for the affected transactions to confirm if the authorisation request was successfully sent and if a timeout occurred due to no response from the client

    2. Share detailed error codes or timeouts logged on Checkout's system to help the client pinpoint the issue

    3. Collaborate with the client to review their endpoint and identify misconfigurations or response delays

    4. Depending on the nature of the timeout, it might be possible to slightly adjust the timeout threshold for specific clients (though this is usually not recommended or necessary unless approved by the card schemes)

5. Notes & Tips:

  1. If the client says that there are no issues on their end, please [raise a Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277)

  2. If you see multiple queries about transactions timing out, please raise a [raise a Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277) as it could be an internal Checkout issue

  3. Other possible reasons for transactions timing out e.g. a time-out issue between CKO and Mastercard. If this happened, Checkout would receive automated emails about this and IT would start working on this immediately

## Glossaries and Definitions:

For **Key Terms and Definitions** on Card Issuing Issues, please see ****[Card Issuing Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22857173195794-Issuing-Glossary-Introduction) 

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Card Issuing articles, please see ****[Card Issuing Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22857178933394-Issuing-Tools-Permissions)
