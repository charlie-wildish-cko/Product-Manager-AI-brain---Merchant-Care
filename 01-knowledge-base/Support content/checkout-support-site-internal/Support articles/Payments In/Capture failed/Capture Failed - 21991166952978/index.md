---
id: 21991166952978
section_id: 21991151338770
title: "Capture Failed"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/21991166952978-Capture-Failed"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:33:44Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQT889RQXXSG27BB4ZJ0M"]
label_names: ["case_transactions", "ROW", "unable_to_capture", "case_transactions_issue_unable_to_capture_payment"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

**Note:** This case type also overlaps with the below procedures, so it would be advisable to refer to these to aid your investigation:

- 6.2.7. API error unclear

- 6.2.3. Response code unclear

- 6.2.13. Unable to refund  
 

This issue type should be used for when the capture attempt is failing unexpectedly and requires us to investigate the root cause (either on the merchant side, product side or CKO side). A merchant can either capture through dashboard, manually call our capture endpoint API using their own logic or enable auto-capture whereby CKO performs the capture on behalf of the merchant.If the root cause is related to a bug or we’re unable to identify the reason why the merchant is unable to refund, this might lead to an escalation to the product/Engineering team to investigate further and fix as necessary.

1. Transactions whereby the merchant is unable to capture (i.e payment status is not captured) and typically stuck in authorised or pending states.

2. The possible root causes are:

  1. Merchant is not sending the correct or valid fields in the request

  2. Refunds are disabled in their configuration (eg. Client Admin Tool)

  3. API or Dashboard bug preventing the transaction to be refunded

  4. Incident leading to the transaction failing to be refunded (eg. scheme or internal outage)

## Process Steps

1. Identify the payment ID by the information shared by the merchant.

2. Once you have the Payment ID, put the Payment ID into traffic insights:

  1. If there is a successful chargeCaptured event in traffic insights then this means the payment has been successfully captured and no further action is required.

  2. If there is a chargeCaptureDeclined event in traffic insights then this means the capture was requested but declined by either the scheme or issuing bank or internal - please refer to 6.2.3. Response code unclear SOP for further information on these.

  3. If there is no captured event, proceed to the next step.

3. Check the logs in [Datadog](https://app.datadoghq.com/logs?query=%40PaymentId%3Apay_wykl5vo2mdb23fk6v7bae4cg3m&ag[%E2%80%A6]z=stream&from_ts=1649747918643&to_ts=1651043918643&live=true) and search by Payment ID (@PaymentId):

  1. Using the above link you can paste the payment ID and get the logs based on this ID

  2. Verify the http status code returned on the refund endpoint from the logs ([https://api.checkout.com/payments/pay_xxx/captures](https://api.checkout.com/payments/%7Bid%7D/captures)).

    1. If http status code is 422, this implies it is to do with invalid data the merchant has sent in which case refer to below doc for most common 422 error codes and reason: [https://checkout.atlassian.net/wiki/spaces/GW/pages/5624430773/Investigating+payment+errors#Common-422-Validation-Errors-and-Investigating](https://checkout.atlassian.net/wiki/spaces/GW/pages/5624430773/Investigating+payment+errors#Common-422-Validation-Errors-and-Investigating)

    2. If http status code is any other 4XX or 5XX (eg. 401, 403, 404, 502) the please refer to below doc for most common reasons: [https://checkout.atlassian.net/wiki/spaces/GW/pages/5624430773/Investigating+payment+errors#Other-Common-HTTP-Codes](https://checkout.atlassian.net/wiki/spaces/GW/pages/5624430773/Investigating+payment+errors#Other-Common-HTTP-Codes)

    3. There might be also the possibility of the merchant reaching the rate limit.you can check this by following the step below : 

    4. Head to your private Slack channel.

    5. Type “/” and choose “Rate-Limit.”

    6. Enter this: <Client ID>/ payments POST. (make sure to include a space in front of Payments)

      1. It’ll format like this:

      2. /rate-limit cli_sb645tfemioencawx6dtqgstxm /payments POST

    7. If the rate per limit need to be increased you can post in the slack channel rate_limiting

4. Check if there are any other errors or exceptions in the logs that might help to further troubleshoot why the captures are failing.

5. Check if there were any incidents or outages on the OC slack channel to confirm whether the failures were related to any reported incidents.

6. If all the above has been checked but it is still not clear what the root cause is, escalate to L2.

## Glossaries and Definitions:

For **Key Terms and Definitions** on Transactions as well as an **introduction into MENA Gateway and non-Gateway merchants**, please see ****[Transactions Glossary](https://checkoutint.zendesk.com/hc/en-us/articles/21991201065106-Transactions-Glossary-Introduction)**.  **
 
 
 
 
 
 
 
 
 
For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Transactions articles, please see ****[Transactions Tools & Permissions](https://checkoutint.zendesk.com/hc/en-us/articles/21991176883474-Transactions-Tools-Permissions)**.**
