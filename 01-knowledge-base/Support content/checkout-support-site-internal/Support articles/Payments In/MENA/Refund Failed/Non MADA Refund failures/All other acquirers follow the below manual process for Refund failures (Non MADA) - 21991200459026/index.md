---
id: 21991200459026
section_id: 21991152036114
title: "All other acquirers follow the below manual process for Refund failures (Non MADA)"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/21991200459026-All-other-acquirers-follow-the-below-manual-process-for-Refund-failures-Non-MADA"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:40:24Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQT889RQXXSG27BB4ZJ0M"]
label_names: ["case_transactions", "MENA", "case_transactions_issue_refund", "All_other_acquirers_follow_the_below_manual_process_for_Refund_failures_(Non_MADA)", "Non_MADA_20030_Refund_failures"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

**Important: **KSA has a manual refund process due to the 30 day limitation for MADA. All other acquirers outside of KSA can be done directly from the Dashboard. For manual refunds please refer to this [highspot page](https://docs.google.com/spreadsheets/d/1g1I4-FixwMxsF07SLu_3mtin_650uVW-0MVOzS84xg8/edit#gid=1386391676) which gives you a breakdown of the process for KSA acquirers.

## Process Steps

1. 
A quick resolution would be to ask the merchant to reattempt the refund (in most cases this would go through) by using the email template below:

  1. _‘ Hi xxx Please can you reattempt the refund for the transaction xxx. If this does not go through then do let us know so we can look into resolving this. Thank you, Kind regards xxx’_

  2. Verify that the merchant has reattempted the refund by using Retool. For each refund attempt the retool will have a corresponding gateway event. Further refund attempts can be verified from here. This will be recorded on Dashboard too.

  3. 
If it still does not go through, you would need to reach out to the acquirer (via email) and explain that the recent refund is still not going through even after asking the merchant to try on their side. Use the email template below:

    1. _‘ Hi xxx. This is a request for xxx Please see the transaction details (response code and the response log) xxx. As the merchant is unable to successfully reattempt the refund, please can you attempt to refund from your side. Do let us know if you have any questions. Thank you, Kind regards xxx’_

  4. 
It is important to firstly identify the acquirer before reaching out. This can be done by going to [Datadog](https://app.datadoghq.com/account/login?next=%2Flogs%3Fquery%3D%2540PaymentId%253Apay_wykl5vo2mdb23fk6v7bae4cg3m%26agg_m%3Dcount%26agg_m_source%3Dbase%26agg_t%3Dcount%26cols%3Dpool%252Cservice%252C%2540error%252C%2540Properties.ActionType%252C%2540Properties.AcceptorName%252C%2540Properties.Response.ResponseDetails.AcquirerResponse%252C%2540Properties.Response.ResponseDetails.AcquirerResponseCode%252C%2540Properties.Request.RequestDetails.TransactionType%26fromUser%3Dtrue%26index%3Dprocessing%26messageDisplay%3Dinline%26refresh_mode%3Dsliding%26saved-view-id%3D749868%26storage%3Dhot%26stream_sort%3Dtime%252Cdesc%26viz%3Dstream%26from_ts%3D1649747918643%26to_ts%3D1651043918643%26live%3Dtrue) and [Retool](https://retoolprod.mgmt.ckotech.co/apps/payment-performance-shared-debug/Traffic%20Insights#payment_id=). You can find out which acquirer this refund was processed from. 

  5. Once confirmed, write the email to the acquirer and using the above template:

  6. 
The acquirer may ask Care to log into the [portal](https://ap-gateway.mastercard.com/ma/login.s) and attempt the refund from the portal or attempt again through [HUB](https://hub.checkout.com/login)/[NAS](https://dashboard.checkout.com/). 

    1. Acquirer portal credentials can be obtained by emailing the acquirer and requesting credentials to the particular MID.

  7. 
If the refund is successful from the portal, manual adjustment will have to be done:

    1. If this is Gateway, refund the transaction by logging into the portal, look for ‘transaction Order ID’ and click on ‘Refund transaction’ 

    2. 
Share proof of refund by taking a screenshot on the portal and email this to the merchant whilst ensuring you include the below information:

      1. _‘ Hi xxx. Please see the attached screenshot showing the manual refund which has been completed via the portal. Thank you, Kind regards xxx’_

    3. If this is Non Gateway, refund the transaction by logging into the portal, look for ‘transaction Order ID’ and click on ‘Refund transaction.’ 

    4. 
Inform the internal Payments team by creating a side conversation on ZD and ensuring you include the below information:

      1. _‘ Hi xxx, Please note that we have manually refunded the transaction xxx via the MPGS portal. The transaction details are as follows: xxx. This has been captured on HUB/Dashboard. Please proceed to creating the adjustment and confirm once it has been completed. Thank you, Kind regards xxx’_

    5. 
If the refund is unsuccessful via the portal:

      1. Share the request response code and screenshot to the acquirer and show the failure reason. 

      2. Either the acquirer will process it from their side or will share a file with us and ask us to fill in the transaction details so they can process it. The acquirer will confirm once completed and will send a refund proof. 

      3. If you are required to fill in the transaction details, once added you will then go back and inform the acquirer.

    6. 
If the refund is successful via [HUB](https://hub.checkout.com/login)/[NAS](https://dashboard.checkout.com/). 

      1. No action needed as the status will reflect on HUB/dashboard and MPGS for the acquirer to see

    7. 
If the refund is unsuccessful via [HUB](https://hub.checkout.com/login)/[NAS](https://dashboard.checkout.com/). 

      1. Send an email and explain that the refund is still failing on our side, share the request response code. 

      2. Either the acquirer will process it from their side or will share a file with us and ask us to fill in the transaction details so they can process it. The acquirer will confirm once completed and will send a refund proof. 

### 

## Glossaries and Definitions:

For **Key Terms and Definitions** on Transactions as well as an **introduction into MENA Gateway and non-Gateway merchants**, please see ****[Transactions Glossary](https://checkoutint.zendesk.com/hc/en-us/articles/21991201065106-Transactions-Glossary-Introduction)**.  **
 
 
 
 
 
 
 
 
 

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Transactions articles, please see ****[Transactions Tools & Permissions](https://checkoutint.zendesk.com/hc/en-us/articles/21991176883474-Transactions-Tools-Permissions)**.**
