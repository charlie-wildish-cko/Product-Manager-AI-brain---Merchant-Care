---
id: 29734895329042
section_id: 21991145641234
title: "MENA TPA Response Codes"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/29734895329042-MENA-TPA-Response-Codes"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-09-25T11:36:04Z"
permission_group_id: 26838654181266
content_tag_ids: []
label_names: []
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

David - please help here as well

**Problem/Solution**
 
MENA TPA INTRODUCTION 💬

**MENA TPA** refers to Third Party Acquirers (TPAs) operating in the Middle East and North Africa (MENA) region. A TPA is a financial institution or another authorized entity that helps facilitate the use of a Payment Method through a Payment Scheme. This includes accepting transactions submitted through a payment gateway, routing them to the Payment Scheme and/or issuers, and handling the collection and payout of funds directly to the merchant.

RESOURCES 📍

| Related |
| --- |
| - [Mastercard Response Codes and Error Codes](https://developer.mastercard.com/mastercard-merchant-presented-qr/documentation/server-apis/response-error-codes/#network-response-codes)  - [Cybersource Simple Order API Reason Codes](https://developer.cybersource.com/docs/cybs/en-us/reason-codes-so/reference/all/so/reason-codes-so/reason-codes-so.html)  - [MPGS API and Cybersource Status](https://checkoutint.zendesk.com/hc/en-us/articles/21991193197970-MPGS-API-Cybersource) |

 
MASTERCARD MPGS RESPONSE CODES ⏫

 

## HTTP Response Codes

Successfully processed API requests will result in an **HTTP code 200 (OK)**. A transaction is considered successful when its status is **"APPROVED."** Declined transactions will return an **HTTP code 402** with a **"ReasonCode": "DECLINE."**

Other successful response codes include:

- 
**201 CREATED:** Indicates a successful creation via a POST request. The response will include a link to the newly created resource.

- 
**202 ACCEPTED:** The request was accepted but is still processing asynchronously.

## Client-Side Error Codes (4xx)

These codes indicate that the client made an error in the request.

- 
**400 BAD REQUEST:** General error due to validation errors or missing data.

- 
**401 UNAUTHORIZED:** Missing or invalid authentication token.

- 
**403 FORBIDDEN:** The user is not authorized to perform the operation.

- 
**404 NOT FOUND:** The requested resource does not exist.

- 
**405 METHOD NOT ALLOWED:** The requested URL exists, but the HTTP method (e.g., GET, POST) is not supported for that resource. The response will include an **"Allow"** header listing the supported methods.

- 
**409 CONFLICT:** The request would cause a resource conflict, such as creating a duplicate entry.

- 
**429 TOO MANY REQUESTS:** The user has exceeded the rate limit. The response will include a **"Retry-After"** header.

## Server-Side Error Codes (5xx)

These codes indicate an issue on the server side.

- 
**500 INTERNAL SERVER ERROR:** The server encountered an unexpected condition that prevented it from fulfilling the request.

- 
**Other 5xx codes:** Typically indicate network or infrastructure issues between the client and the API server.

**⚠️See a full list of Mastercard MPGS Response Codes here**

| Acquirer Response Code | Gateway Code | Summary |
| --- | --- | --- |
| 0 | 10000 | Transaction Approved |
| 1 | 20001 | Refer to Issuer |
| 2 | 20002 | Refer to Issuer, special |
| 3 | 20003 | No Merchant |
| 4 | 30004 | Pick Up Card |
| 5 | 20005 | Do Not Honour |
| 6 | 20006 | Error |
| 7 | 30007 | Pick Up Card, Special |
| 8 | 10008 | Honor With Identification |
| 9 | 20009 | Request In Progress |
| 10 | 20010 | Approved For Partial Amount |
| 11 | 10011 | Approved, VIP |
| 12 | 20012 | Invalid Transaction |
| 13 | 20013 | Invalid Amount |
| 14 | 20014 | Invalid Card Number |
| 15 | 30015 | No Issuer |
| 16 | 10000 | Approved, Update Track 3 |
| 19 | 20019 | Re-enter Last Transaction |
| 21 | 20021 | No Action Taken |
| 22 | 20022 | Suspected Malfunction |
| 23 | 20023 | Unacceptable Transaction Fee |
| 25 | 20025 | Unable to Locate Record On File |
| 30 | 20030 | Format Error |
| 31 | 20031 | Bank Not Supported By Switch |
| 33 | 30033 | Expired Card, Capture |
| 34 | 30034 | Suspected Fraud, Retain Card |
| 35 | 30035 | Card Acceptor, Contact Acquirer, Retain Card |
| 36 | 30036 | Restricted Card, Retain Card |
| 37 | 30037 | Contact Acquirer Security Department, Retain Card |
| 38 | 20038 | PIN Tries Exceeded, Capture |
| 39 | 20039 | No Credit Account |
| 40 | 20040 | Function Not Supported |
| 41 | 30041 | Lost Card |
| 42 | 20042 | No Universal Account |
| 43 | 30043 | Stolen Card |
| 44 | 20044 | No Investment Account |
| 51 | 20051 | Insufficient Funds |
| 52 | 20052 | No Cheque Account |
| 53 | 20053 | No Savings Account |
| 54 | 20054 | Expired Card |
| 55 | 20055 | Incorrect PIN |
| 56 | 20056 | No Card Record |
| 57 | 20057 | Function Not Permitted to Cardholder |
| 58 | 20058 | Function Not Permitted to Terminal |
| 59 | 20059 | Suspected Fraud |
| 60 | 20060 | Acceptor Contact Acquirer |
| 61 | 20061 | Exceeds Withdrawal Limit |
| 62 | 20062 | Restricted Card |
| 63 | 20063 | Security Violation |
| 64 | 20064 | Original Amount Incorrect |
| 65 | 20065 | Exceeds withdrawal |
| 66 | 20066 | Acceptor Contact Acquirer, Security |
| 67 | 20067 | Capture Card |
| 75 | 20075 | PIN Tries Exceeded |
| 82 | 20082 | No security model / Negative CAM, dCVV, iCVV, or CVV results / PIN cryptographic error found (error found by VIC security module during PIN decryption) |
| 85 | 10000 | No reason to decline request for address verification, CVV2 verification, or credit voucher or merchandise return |
| 90 | 20090 | Cutoff In Progress |
| 91 | 20091 | Card Issuer Unavailable |
| 92 | 20092 | Unable To Route Transaction |
| 93 | 20093 | Cannot Complete, Violation Of The Law |
| 94 | 20094 | Duplicate Transaction |
| 96 | 20096 | System Error |
| 124 | 20124 | Missing CVV value, required for Ecommerce Transaction |
| 155 | 20155 | 3DS authentication service provided invalid authentication result |
| 156 | 20156 | Requested Function not Supported by the Acquirer |
| 157 | 20157 | Invalid Merchant Configurations - Contact support |
| INTERNAL0 | 10000 | Internal Success Capture |
| INTERNAL1 | 20012 | Internal Invalid Transaction |
| INTERNAL2 | 20012 | Invalid Transaction |
| INTERNALERR | 20068 | Application Error |

 

**CYBERSOURCE RESPONSE CODES ⏫**

## Successful Transaction Codes

A decision of **ACCEPT** indicates a successful transaction. The reason code provides additional detail on the type of success.

- 
**100:** The request was successful.

- 
**101:** The request was successful, but the order was flagged for review by the payment gateway.

- 
**102:** The request was successful, but the transaction was a duplicate.

## Client-Side Error Codes

A decision of **DECLINE** often accompanies these codes, which are related to issues with the request or the cardholder's information.

- 
**150:** The request contains one or more missing or invalid fields.

- 
**151:** The request contains an invalid field.

- 
**152:** The request contains a missing field.

- 
**200:** The authorization has been declined by the card-issuing bank.

- 
**201:** The card has expired.

- 
**202:** The card has been declined due to insufficient funds.

- 
**203:** The card is a pickup card (stolen or lost card).

- 
**204:** The account number is invalid.

- 
**205:** The card is a pickup card, and a fraud alert has been issued.

- 
**207:** The card's issuing bank does not allow this type of transaction.

- 
**208:** The card has been flagged as lost or stolen.

- 
**210:** The card's credit limit has been exceeded.

- 
**211:** The card's card verification value (CVV) is invalid.

## System-Side Error Codes

A decision of **ERROR** or **REVIEW** can accompany these codes, which are related to system or processing issues.

- 
**250:** The request was not processed due to a general system error.

- 
**251:** The request timed out.

- 
**252:** The request was a duplicate.

- 
**253:** The transaction has been declined due to a security violation.

- 
**480:** The transaction was flagged as high-risk and is being reviewed.

**⚠️ See a full list of Cybersource Response Codes here**

| Acquirer Response Code | GatewayCode | Summary |
| --- | --- | --- |
| 100 | 10000 | Successful transaction |
| 101 | 20123 | Declined - The request is missing one or more fields |
| 102 | 20006 | Declined - One or more fields in the request contains invalid data |
| 104 | 20026 | Declined - The merchantReferenceCode sent with this authorization request matches the merchantReferenceCode of another authorization request that you sent in the last 15 minutes. |
| 105 | 20094 | Declined - Merchant transaction identifier (MTI) sent with this request has already been used in the past 60 days. |
| 110 | 20010 | Partial amount was approved |
| 150 | 20096 | Error - General system failure. |
| 151 | 20068 | Error - The request was received but there was a server timeout. This error does not include timeouts between the client and the server |
| 152 | 20068 | Error: The request was received, but a service did not finish running in time. |
| 200 | 10100 | Soft Decline - The authorization request was approved by the issuing bank but declined by CyberSource because it did not pass the Address Verification Service (AVS) check. |
| 201 | 20001 | Decline - The issuing bank has questions about the request. You do not receive an authorization code programmatically, but you might receive one verbally by calling the processor. |
| 202 | 20054 | Decline - Expired card. You might also receive this if the expiration date you provided does not match the date the issuing bank has on file. |
| 203 | 20005 | Decline - General decline of the card. No other information provided by the issuing bank. |
| 204 | 20051 | Decline - Insufficient funds in the account. |
| 205 | 30041 | Decline - Stolen or lost card. |
| 207 | 20091 | Decline - Issuing bank unavailable. |
| 208 | 20057 | Decline - Inactive card or card not authorized for card-not-present transactions. |
| 209 | 200N7 | Decline - card verification number (CVN) did not match. |
| 210 | 20061 | Decline - The card has reached the credit limit. |
| 211 | 20087 | Decline - Invalid Card Verification Number (CVN). |
| 213 | 20059 | Decline - Account is in fraud watch status. |
| 220 | 20005 | Decline - Generic Decline. |
| 221 | 20059 | Decline - The customer matched an entry on the processor's negative file. |
| 222 | 90010 | Decline - customer's account is frozen |
| 230 | 10100 | Soft Decline - The authorization request was approved by the issuing bank but declined by CyberSource because it did not pass the card verification number (CVN) check. |
| 231 | 20083 | Decline - Invalid account number |
| 232 | 20103 | Decline - The card type is not accepted by the payment processor. |
| 233 | 20046 | Decline - General decline by the processor. |
| 234 | 20120 | Decline - There is a problem with your CyberSource merchant configuration. |
| 235 | 20109 | Decline - The requested amount exceeds the originally authorized amount. Occurs, for example, if you try to capture an amount larger than the original authorization amount. |
| 236 | 20046 | Decline - Processor failure. |
| 237 | 20109 | Decline - The authorization has already been reversed. |
| 238 | 20111 | Decline - The transaction has already been settled. |
| 239 | 20013 | Decline - The requested transaction amount must match the previous transaction amount. |
| 240 | 20103 | Decline - The card type sent is invalid or does not correlate with the credit card number. |
| 241 | 20012 | Decline - The referenced request id is invalid for all follow-on transactions. |
| 242 | 20012 | Decline - The request ID is invalid. |
| 243 | 20109 | Decline - The transaction has already been settled or reversed. |
| 244 | 2006P | Account number did not pass a verification check |
| 246 | 20012 | Decline - The capture or credit is not voidable because the capture or credit information has already been submitted to your processor. |
| 247 | 20012 | Decline - You requested a credit for a capture that was previously voided. |
| 248 | 20012 | Decline - The boleto request was declined by your processor. |
| 250 | 20068 | Error - The request was received, but there was a timeout at the payment processor. |
| 251 | 20038 | Decline - The Pinless Debit card's use frequency or maximum amount per use has been exceeded. |
| 254 | 20012 | Decline - Account is prohibited from processing stand-alone refunds. |
| 256 | 20012 | Decline - Credit amount exceeds the maximum allowed for your account. |
| 262 | 20009 | Decline - Request is still in progress. |
| 428 | 20154 | Decline - Your request for a strong customer authentication (SCA) exemption was declined. SCA is required for this transaction. |
| 461 | 20006 | Unsupported character set |
| 475 | 40110 | The cardholder is enrolled in Payer Authentication. Please authenticate the cardholder before continuing with the transaction. |
| 476 | 40110 | Encountered a Payer Authentication problem. Payer could not be authenticated. |
| 520 | 10100 | Soft Decline - The authorization request was approved by the issuing bank but declined by CyberSource based on your Smart Authorization settings. |
| CS001 | 20068 | Timeout from CyberSource |
| CS002 | 20006 | Generic Error from CyberSource |
| CS003 | 20058 | Transaction not supported on CyberSource |
