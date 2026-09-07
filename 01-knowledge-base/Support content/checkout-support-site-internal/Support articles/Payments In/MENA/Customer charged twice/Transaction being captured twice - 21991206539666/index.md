---
id: 21991206539666
section_id: 21991160739346
title: "Transaction being captured twice"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/21991206539666-Transaction-being-captured-twice"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:37:31Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQT889RQXXSG27BB4ZJ0M"]
label_names: ["case_transactions", "case_transactions_issue_duplicate_transactions", "MENA", "transaction_being_captured_twice"]
user_segment_ids: [11003606966930]
archive: false
---

## Process Steps

1. Email from a merchant which states customer has claimed they have been charged twice

2. Take payment ID and check on Looker or datadog to know if this was cascaded or not

3. Then go into MPGS and CyberSource

**MPGS API**

1. 
From DataDog we can get this information from MPGS logs: 

2. Once we have the MID/Token and order ID, From MPGS we can verify the transaction status 

3. If it is not possible to get the transaction status from the MPGS API then verify from the MPGS portal if the transaction has been captured. Log into the portal using the relevant acquirer portal link in the below table:

4. 

| **Acquirer Name** | **Acquirer Portal** |
| --- | --- |
| SABB MPGS | [https://ap-gateway.mastercard.com/ma/login.s](https://ap-gateway.mastercard.com/ma/login.s) |
| Mashreq MPGS | [https://ap-gateway.mastercard.com/ma/login.s](https://ap-gateway.mastercard.com/ma/login.s) |
| Mashreq Cybersource | [https://ebc.cybersource.com/ebc2/](https://ebc.cybersource.com/ebc2/) |
| Mashreq MIGS | [https://migs.mastercard.com.au/ma/login.s](https://migs.mastercard.com.au/ma/login.s) |
| Network International Cybersource | [https://network.ubc.cybersource.com/ebc2/](https://network.ubc.cybersource.com/ebc2/) |
| Doha Bank | [https://dohabank.gateway.mastercard.com/ma/login.s](https://dohabank.gateway.mastercard.com/ma/login.s) |
| Bank Muscat | [https://bankmuscat.gateway.mastercard.com/ma/login.s](https://bankmuscat.gateway.mastercard.com/ma/login.s) |
| MEPS | [https://mepspay.gateway.mastercard.com/ma/login.s](https://mepspay.gateway.mastercard.com/ma/login.s) |
| Bank Muscat Cybersource | [https://bankmuscat.ubc.cybersource.com/ebc2/](https://bankmuscat.ubc.cybersource.com/ebc2/) |
| National Bank of Kuwait | [https://nbk.ubc.cybersource.com/ebc2/](https://nbk.ubc.cybersource.com/ebc2/) |
| AESA MPGS | [https://aesa.gateway.mastercard.com/ma/login.s](https://aesa.gateway.mastercard.com/ma/login.s) |
| NBE MPGS | [https://nbe.gateway.mastercard.com/ma/login.s](https://nbe.gateway.mastercard.com/ma/login.s) |
| ANB | [https://anb.gateway.mastercard.com/ma/login.s](https://anb.gateway.mastercard.com/ma/login.s) |

  1. To log into the MPGS portal the credentials are required, to obtain this you have to reach out to the acquirer and ask them to provide the credentials for that particular MID. _Please check the Active MID credentials Gsheet before reaching out to the acquirer to verify if we already have the information._

  2. Once provided, log in and look for the transaction (with reference, most cases the RRN) and take a screenshot from the portal which shows the transaction has been deducted.

  3. An example of the screenshot can be seen below:

If the merchant does not want to give access to the MPGS Portal, follow the below process:

1. Reach out to the acquirer with the full transaction details e.g. RNN, Auth code transaction date, amount of transaction and Masked number.

2. The acquirer will be able to check if there has been a duplicate transaction.

3. Get back to the merchant based on the acquirer's response.

 

### Cybersource

1. All acquirers can follow the below process

2. Check transaction status via the Cybersource portal

3. Log into the [Cybersource porta](https://ebc2.cybersource.com/ebc2/app/TransactionManagement/details?requestId=6809402917066418304276&merchantId=mashreq_8108771_aed&fromSimilarSearch=false&goBackCount=-2)l with the available credentials

  1. Locate the MID from Cybersource authorisation API from datadog

  2. 
Refer to this [sheet](https://docs.google.com/spreadsheets/d/1x-6_2QW8a7U9yyzUabGLS8ajxCYMuS8qfI300kc_EZE/edit#gid=0) to locate the password to the MID and log in to [Cybersource](https://ebc2.cybersource.com/ebc2/app/TransactionManagement/details?requestId=6809402917066418304276&merchantId=mashreq_8108771_aed&fromSimilarSearch=false&goBackCount=-2) using the new password

  3. Go to the option Transaction Management. Select Transactions

  4. Click on add filter. Choose the option Merchant Reference Number.

  5. Enter the reference number and adjust the date range accordingly. **Note**: If using the AcquirerReferenceID from Hermes, add the filter RequestID.

  6. Click on the Request ID to open the transaction

4. If the transaction is successful on both tools then this means it was captured twice

5. If the transaction was only captured on one tool this means it was not captured twice

6. 
If it is captured twice then Care will have to:

  1. Attempt to refund the captured transaction on MPGS by following the steps

  2. Log into the [portal](https://ap-gateway.mastercard.com/ma/login.s) and attempt the refund from the portal.

    1. Acquirer portal credentials can be obtained by emailing the acquirer and requesting credentials to the particular MID.

  3. If the refund is successful from the portal, manual adjustment will have to be done:

    1. If this is Gateway, refund the transaction by logging into the portal, look for ‘transaction Order ID’ and click on ‘Refund transaction’

    2. Share proof of refund by taking a screenshot on the portal and emailing this to the merchant whilst ensuring you include the below information:

      1. _‘ Hi, xxx. Please see the attached screenshot showing the manual refund which has been completed via the portal. Thank you, Kind regards xxx’_

    3. If this is Non-Gateway, refund the transaction by logging into the portal, look for ‘transaction Order ID’ and click on ‘Refund transaction.’

    4. Inform the internal Payments team by creating a side conversion on ZD and ensuring you include the below information:

      1. _‘ Hi xxx, Please note that we have manually refunded the transaction xxx via the MPGS portal. The transaction details are as follows: xxx. This has been captured on HUB/Dashboard. Please proceed to create the adjustment and confirm once it has been completed. Thank you, Kind regards xxx’_

    5. If the refund is unsuccessful via the portal:

      1. Share the request-response code and screenshot to the acquirer and show the failure reason.

      2. Either the acquirer will process it from their side or will share a file with us and ask us to fill in the transaction details so they can process it. The acquirer will confirm once completed and will send a refund proof.

      3. If you are required to fill in the transaction details, once added you will then go back and inform the acquirer.

## Glossaries and Definitions:

For **Key Terms and Definitions** on Transactions as well as an **introduction into MENA Gateway and non-Gateway merchants**, please see ****[Transactions Glossary](https://checkoutint.zendesk.com/hc/en-us/articles/21991201065106-Transactions-Glossary-Introduction)**.  **
 
 
 
 
 
 
 
 
 
For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Transactions articles, please see ****[Transactions Tools & Permissions](https://checkoutint.zendesk.com/hc/en-us/articles/21991176883474-Transactions-Tools-Permissions)**.**
