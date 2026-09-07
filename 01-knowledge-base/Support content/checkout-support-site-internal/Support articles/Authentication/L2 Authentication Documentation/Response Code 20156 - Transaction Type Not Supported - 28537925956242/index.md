---
id: 28537925956242
section_id: 27822398640530
title: "Response Code 20156 - Transaction Type Not Supported"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/28537925956242-Response-Code-20156-Transaction-Type-Not-Supported"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-09-19T11:35:18Z"
permission_group_id: 26838654181266
content_tag_ids: ["01K1WK7DZX5XXYDJ740NKEFSS0"]
label_names: ["response_code_20150_card_not_3ds_enabled", "response_code_20156", "L2", "Troubleshooting", "20156"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

Investigate error code 20156: "Transaction Type Not Supported by Acquirer." This happens when the acquiring bank doesn't support the transaction type or due to technical issues on MPGS.

## DESCRIBE THE ISSUE 💬

20156 is a transaction Processing Error. This is usually caused by a specific type of transaction (e.g. a refund, a void, a wallet transaction, an account verification) not being enabled or supported by the merchant's payment processor (MPGS).

 

## KEY TAKEAWAYS 🔑

**20156 = Transaction Type Not Supported:** This error means the acquiring bank (MPGS) declined the payment because the specific transaction type is not allowed on that particular acquirer link/setup.
 

**Resolution:** Contact the relevant acquirer to understand the merchant's set up on their side or for assistance with refunding/voiding the specific transaction.

## RESOURCES 📍

| Tools | Case Examples | Related |
| --- | --- | --- |
| [Datadog](https://app.datadoghq.com/logs?query=%40Properties.ResponseCode%3A156&agg_m=count&agg_m_source=base&agg_t=count&clustering_pattern_field_path=message&cols=service%2C%40http.status_code%2C%40PaymentAction&event=AwAAAZh0h8V-SQB4BQAAABhBWmgwaDh3bEFBRDZaaEZEVTJzcUZ3QU4AAAAkZjE5ODc0OTMtY2M5NS00ZTE3LTlkNGItZGFlYTU3OWU0YTBlAAx3Aw&fromUser=true&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=time%2Cdesc&viz=stream&from_ts=1712658031337&to_ts=1715250031337&live=true) | [63201](https://checkout1360.zendesk.com/agent/tickets/63201) [24639](https://checkout1360.zendesk.com/agent/tickets/24639) | [Financial Partnership Directory](https://docs.google.com/spreadsheets/d/1ipGueNYij7yEEr1y9S-0Ba0lqS9Ia3Wbsnm6YuvwoaQ/edit?gid=1771915325#gid=1771915325) - Acquirer contact details |

## 20156 FAILURE INVESTIGATION PROCESS 🖊️

Step 1. Search for 20156 Failures in Datadog

- Navigate to the **Search Logs** tab in Datadog

- Use the following search query to filter for the relevant logs, this will narrow down the search to logs with the `20156` response code and a specific Merchant ID:

```
@Properties.ResponseCode:156
@Properties.Request.RequestDetails.MerchantId: <MerchantID>

```

**Example in use:**

```@Properties.ResponseCode:156 
@Properties.Request.RequestDetails.MerchantId:900120501 
```

 
Step 2. Analyse Log Explorer Results

- Once the logs are displayed in the **Log Explorer**, select a specific log message for further investigation

- 
Look for an error message from the acquirer (In MPGS Authorisation API), such as:

  -  `"INVALID_REQUEST - The acquirer does not support this transaction type"`

  - "INVALID_REQUEST - Missing merchant privilege 'Device Payments'"

  - "INVALID_REQUEST - Value 'AUTHORIZE' is invalid. Authorization request not permitted for this merchant."

  - "INVALID_REQUEST - Value 'REFUND' is invalid. Missing merchant privilege 'Excessive Refund'"

  - "INVALID_REQUEST - Value 'PAY' is invalid. Pay request not permitted for this merchant."

 

 
Step 3. Identify the Unsupported Transaction Type

- Check the log details to identify the transaction type attempted, e.g., INVALID_REQUEST - Value 'REFUND' is invalid due to missing 'Excessive Refund' privilege.

- This may indicate the transaction was already refunded but the status isn't updated in our logs or Dashboard; the acquirer can provide better insight.

## RESOLUTION ⚒️

This issue requires direct communication with the acquirer

- Review the endpoint in the logs to identify the acquirer processing the transaction

In the screenshot above, the acquirer is NBK

- Reach out to the relevant acquirer (e.g., SAB, NBK, SNB, etc) with the details of the failed transaction, the acquirer contact details are available [here](https://docs.google.com/spreadsheets/d/1ipGueNYij7yEEr1y9S-0Ba0lqS9Ia3Wbsnm6YuvwoaQ/edit?gid=1771915325#gid=1771915325)

- Provide them with the Merchant ID, MPGS request and response

- 
**Example email to the acquirer :**

```Hello Team,

I hope you are doing well. 

Appreciate your assistance in understanding the transaction failures with 
"Value 'AUTHORIZE' is invalid. Authorization request not permitted for this merchant."
Merchant ID : 900128001

Request -
{
  "apiOperation": "AUTHORIZE",
  "order": {
    "amount": 0.520,
    "currency": "KWD",
    "description": "HNKWHDE0000474",
    "reference": "HNKWHDE0000474"
  },
  "partnerSolutionId": "EMCKO1027",
  "sourceOfFunds": {
    "provided": {
      "card": {
        "devicePayment": {
          "eciIndicator": "07",
          "onlinePaymentCryptogram": "AQAAAAAAeV8X\u002BMUAmbLlgtgAAAA="
        },
        "expiry": {
          "month": "**",
          "year": "**"
        },
        "number": "****************",
        "storedOnFile": "TO_BE_STORED"
      }
    },
    "type": "SCHEME_TOKEN"
  },
  "transaction": {
    "reference": "HNKWHDE0000474",
    "source": "INTERNET"
  }
}

Response -
{"error":
{"cause":"INVALID_REQUEST","explanation":"Value 'AUTHORIZE' is invalid. 
Authorization request not permitted for this merchant.","field":"apiOperation","validationType":"INVALID"},
"result":"ERROR"}

Please let us know if you require any information.

Thank you.

```

**Communicate with the Merchant:**

- Once you receive a response from the acquirer, update the merchant with the information

- Provide a clear explanation of why the transaction failed and what actions were taken

## ESCALATION** ⏫**

- A high volume or recurring pattern of 20156 failures for a specific merchant ID suggests a misconfiguration or a limitation from the acquirer

- The acquirer is not responding to the email or provides unclear/contradictory information regarding the supported transaction types

- Loop in our escalation points from the partnerships team [ibrahim.alhusine@checkout.com]((ibrahim.alhusine@checkout.com) and [Karam.Makki@checkout.com](mailto:Karam.Makki@checkout.com)

## FAQs** ****❓**

 
Is this a problem with our system or the merchant's setup?This issue originates directly from the **acquiring bank**. Our system receives and passes on their decline message. It indicates a mismatch between the transaction type sent and what the acquirer's specific link/configuration allows.

 
Can we change the transaction type on our end to fix this?Our system sends the transaction type as requested by the merchant's integration. If the acquirer declines with a 20156, it means their system does not permit that type of transaction on that specific link. The solution involves either the acquirer adjusting their configuration (unlikely for specific link restrictions) or the merchant adjusting their transaction type requests for that acquirer.
