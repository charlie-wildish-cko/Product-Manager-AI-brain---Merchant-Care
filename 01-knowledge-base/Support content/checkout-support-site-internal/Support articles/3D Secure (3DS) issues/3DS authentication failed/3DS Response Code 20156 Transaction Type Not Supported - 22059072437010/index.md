---
id: 22059072437010
section_id: 22057285830034
title: "3DS Response Code 20156: Transaction Type Not Supported"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22059072437010-3DS-Response-Code-20156-Transaction-Type-Not-Supported"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:34:10Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRP1QGWAFPTEP0CSMC1WBV"]
label_names: ["global", "case_3ds_issue_response_code_20151_-_20156", "case_3ds_issue_response_code_20151_-_20159", "case_3ds_issues", "response_code_20156"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

The below article explains when a payment has failed with a 20156 issue error: transaction type not supported.

## Process Steps

1. Open [Datadog](https://app.datadoghq.com/logs?query=%40PaymentId%3A%28pay_xsj37yvkfu2ezewtvphv74jx2a%29&agg_m=count&agg_m_source=base&agg_t=count&cols=service%2C%40http.status_code%2C%40PaymentAction&fromUser=true&index=processing&messageDisplay=inline&refresh_mode=sliding&saved-view-id=88535&storage=hot&stream_sort=time%2Cdesc&viz=stream&from_ts=1712658031337&to_ts=1715250031337&live=true), go to the **Search Logs **tab and search the response code ‘156’, the processing profile, and the acquirer name

2. 
Using the following code

```@Properties.ResponseCode: 
@Properties.Request.MerchantAcquirerConfiguration.ProcessingProfile.Id 
@Properties.Request.MerchantAcquirerConfiguration.Acquirer.AcquirerName:
```

An example of this in use:

```@Properties.ResponseCode:156
@Properties.Request.MerchantAcquirerConfiguration.ProcessingProfile.Id:pp_43i4ym4qyziexj4go3zqmrgjky
@Properties.Request.MerchantAcquirerConfiguration.Acquirer.AcquirerName:sabb-mpgs
```

1. When the results are displayed on the **Log Explorer**, please select a message to investigate this issue further

1. If you see the logs on the right-hand side display the error message of the acquirer MPGS not supporting the transaction type, check the logs and identify if the payment had failed due to the transaction type:-

 

In the above example, this looks like a decline coming from the acquirer MPGS "INVALID_REQUEST - The acquirer does not support this transaction type. AcquirerId=MADA_SABB_ALLTXNS". Please see the [logs](https://app.datadoghq.com/logs?query=%40Properties.ResponseCode%3A156%20%40Properties.Request.MerchantAcquirerConfiguration.ProcessingProfile.Id%3App_43i4ym4qyziexj4go3zqmrgjky%20%40Properties.Request.MerchantAcquirerConfiguration.Acquirer.AcquirerName%3Asabb-mpgs%20&cols=service%2C%40http.status_code&fromUser=true&index=&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=time%2Cdesc&viz=stream&from_ts=1709824195995&to_ts=1710428995995&live=true) for 156 declines during the past seven days.

1. This issue can be resolved by contacting the relevant acquirer and asking them to refund or void the transactions.   
 

2. When the acquirer has provided an update on the transaction, please respond to the merchant with the information from the acquirer and close the ticket. Please see an example below:   
 

| _Hello Team,_ _Please find below the response from SAB for the error 20156._ _The original transaction in order 74808da1-cd80-4442-bcea-335c390cf57c was a Pay (Purchase) request.  Voiding a Pay request is not possible on the Acquirer link MADA_SABB_ALLTXNS.  It is not an approved transaction type, which is why the merchant is receiving the message "The acquirer does not support this transaction type. AcquirerId=MADA_SABB_ALLTXNS".  We can see that the Order was eventually refunded.  In the future, void requests will not be successful for Pay requests on the acquirer link MADA_SABB_ALLTXNS. _ _Kindly let us know if there is any further information we can provide. _ |
| --- |

Please see this [ticket](https://checkout.lightning.force.com/lightning/r/Case/500Ts000004EVQ3IAO/view) on Salesforce as an example of the issue above.

## Glossaries and Definitions:

For **Key Terms and Definitions** on 3DS, please see ****[3DS Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22059673420818-3DS-Glossary-Introduction)   For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the 3DS articles, please see ****[3DS Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22059810908306-3DS-Tools-Permissions)
