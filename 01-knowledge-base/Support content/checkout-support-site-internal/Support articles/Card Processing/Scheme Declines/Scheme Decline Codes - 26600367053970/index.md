---
id: 26600367053970
section_id: 26832912736274
title: "Scheme Decline Codes"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/26600367053970-Scheme-Decline-Codes"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:34:12Z"
permission_group_id: 26838654181266
content_tag_ids: []
label_names: ["transaction_has_been_declined"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article:**

Any time a payment fails due to it being declined by the scheme or bank the merchant will see the decline code, use the table below to see the decline reasons and potential solutions. 

**PROBLEM 🤔 **

Merchants receive decline codes but don’t always know what they mean or how to resolve the issue.

 

**SOLUTION 🛠️**

View the ****[decline code reasons](https://docs.google.com/spreadsheets/d/1ZSpPQCkDZm6lfQBPFyL_WrpAShqvb4UivnMZlX5xu3k/edit?usp=sharing) and use the decline codes to help them identify the problem and offer recommendations to solve the issue.
Click to see the **Visa Scheme Decline Codes**

| Scheme | Decline code | Description | Explanation | Solutions |
| --- | --- | --- | --- | --- |
| Visa | 30004 | Pick up card (no fraud) | Issuer will never approve    Do not try again | The Issuer will never approve the transaction. Here are some recovery strategies for the merchant:  1. Avoid retrying the transaction with the same card to prevent Visa Integrity and gateway fees.  2. Prompt the shopper to retry with a different card (ensure this aligns with the merchant's risk tolerance, as it may increase fraud).  3. Show alternative payment methods for the shopper to retry the transaction. |
| Visa | 30007 | Pickup card, special conditions | Issuer will never approve    Do not try again | The Issuer will not approve the transaction. Here are recovery strategies for the merchant:  1. Avoid retrying the transaction with the same card to prevent Visa Integrity and gateway fees.  2. Prompt the shopper to use a different card (consider the merchant's risk appetite, as this may increase fraud).  3. Show alternative payment methods for the shopper to retry the transaction. |
| Visa | 20012 | Invalid transaction | Issuer will never approve    Do not try again | The transaction will never be approved by the Issuer. Some recovery strategies you can recommend to the merchant:  1. Do not retry the transaction with the same card to avoid accrueing Visa Integrity Fees and gateway fees  2. Display a message asking the shopper to retry the transaction with a different card (NB: please align with merchant's risk appetite, as this could lead to increased fraud)  3. Display alternative payment methods the shopper can use to retry the transaction |
| Visa | 20014 | Invalid card number | Issuer will never approve    Do not try again |  |
| Visa | 30015 | No such issuer | Issuer will never approve    Do not try again | [https://checkoutinternal.eu.looker.com/explore/payment_lifecycle/fct_payin?qid=Usg3B2KpLRrygHWtiGnYYQ&toggle=fil,vis](https://checkoutinternal.eu.looker.com/explore/payment_lifecycle/fct_payin?qid=Usg3B2KpLRrygHWtiGnYYQ&toggle=fil,vis) |
| Visa | 30041 | Lost card - pick up | Issuer will never approve   Do not try again | The transaction will never be approved by the Issuer. Some recovery strategies you can recommend to the merchant:  1. Do not retry the transaction with the same card to avoid accrueing Visa Integrity Fees and gateway fees  2. Display a message asking the shopper to retry the transaction with a different card (NB: please align with merchant's risk appetite, as this could lead to increased fraud)  3. Display alternative payment methods the shopper can use to retry the transaction |
| Visa | 30043 | Stolen card - pick up | Issuer will never approve    Do not try again | The transaction will never be approved by the Issuer. Some recovery strategies you can recommend to the merchant:  1. Do not retry the transaction with the same card to avoid accrueing Visa Integrity Fees and gateway fees  2. Display a message asking the shopper to retry the transaction with a different card (NB: please align with merchant's risk appetite, as this could lead to increased fraud)  3. Display alternative payment methods the shopper can use to retry the transaction |
| Visa | 30046 | Closed Account | Issuer will never approve    Do not try again | The transaction will never be approved by the Issuer. Some recovery strategies you can recommend to the merchant:  1. Do not retry the transaction with the same card to avoid accrueing Visa Integrity Fees and gateway fees  2. Display a message asking the shopper to retry the transaction with a different card  3. Display alternative payment methods the shopper can use to retry the transaction (NB: please align with merchant's risk appetite, as this could lead to increased fraud)  4. Upsell opp: RTAU  5. Upsell opp: NTs |
| Visa | 20057 | Transaction not permitted to cardholder | Issuer will never approve    Do not try again | 1. Cardholder communications |
| Visa | 200R1 | Issuer initiated a stop payment (revocation order) for the Authorization | Issuer will never approve    Do not try again |  |
| Visa | 200R3 | Issuer initiated a stop payment (revocation order) for all Authorizations | Issuer will never approve    Do not try again |  |
| Visa | 20003 | Invalid merchant | 20151 | This transaction is typically declined due to a configuration issue most likely due to a restriction placed at Issuer level either on the MCC or for a specific merchant. Some recommendations on how these tranactions can be recovered:  1. Ask merchants to display a message encouraging their shoppers to re-attempt the transaction with a diferrent card or alternative payment method.  2. Issuer Outreach |
| Visa | 20019 | Re-enter transaction | Issuer cannot approve at this time    Try again later |  |
| Visa | 20051 | Insufficient funds | Issuer cannot approve at this time    Try again later | 1. If either CIT or MIT: (1) cardholder communcations  2. If MIT: (1) change day to align to local pay day (2) change time of day MIT is processed to align with local bank opening hours, considered higher AR, (3) consider payment retries pilot (Gateway product) (4) consume MAC codes for Mastercard to advise merchant how/if to retry  3. If CIT: (1) APM upsell, depending on local availability/features (e.g., recurring functionalities may not be available) NB: 20051 are considered Cat 2 fees under Visa System Integrity Monitoring. Excessive retries could increase scheme fees |
| Visa | 20059 | Suspected fraud | Issuer cannot approve at this time    Try again later | 1. Upsell for fraud reduction:    (1) FD Pro   (2) CE 3.0 - reduce overall fraud rate   (3) Wallet pays - ECI 05 fraud liability shift  1. Upsell for performance improvemnt:    (1) NT - help reduce fraud,   (2) IA - manage NTs effectively + utilise 3DS intelligently for CIT traffic   (3) Authentication upsell - provides security against fraud   1. Increase/improve quality of data in authorisation message  2. Check recommendation codes for best course of action  3. Check fraud rates for individual issuer. Generally anything >35bps is too high. Issuers have machine learning that will cause false declines if fraud rates are too high  4. If MIT traffic:     (1) consider 3RI to reduce fraud rates (only supported with Mastercard for recurring trnxs)   (2) restart MIT chain with authentication (challenge_request_mandate indicator)   NB:    (1) 20051 are considered Cat 2 fees under Visa System Integrity Monitoring. Excessive retries could increase scheme fees   (2) Excessive retries may cause issuers to increase false declines |
| Visa | 20061 | Exceeds withdrawal amount limits | Issuer cannot approve at this time    Try again later | See "20051 - Insufficient Funds" |
| Visa | 20062 | Restricted card | Issuer cannot approve at this time    Try again later |  |
| Visa | 20065 | Exceeds withdrawal frequency limit | Issuer cannot approve at this time    Try again later | See "20051 - Insufficient Funds" |
| Visa | 20075 | Allowable PIN tries exceeded | Issuer cannot approve at this time    Try again later |  |
| Visa | 20078 | Blocked card, first time card usage | Issuer cannot approve at this time    Try again later | 1. Cardholder communications to unblock card  2. For MIT transactions, check BIN/issuer. Some BINs (e.g. Sutton Bank Cash App BINs) need unblocking by the customer via the app. Cardholder communications could then be used once identified. |
| Visa | 20091 | Issuer or switch is inoperative | Issuer cannot approve at this time    Try again later |  |
| Visa | 20093 | Transaction cannot be completed | Issuer cannot approve at this time    Try again later |  |
| Visa | 20096 | System malfunction | Issuer cannot approve at this time   Try again later |  |
| Visa | 20054 | Expired card | Issuer cannot approve based on details provided    Updated or additional information required | 1. RTAU upsell  2. NT upsell (expired card is tokenised and updated) |
| Visa | 20055 | Incorrect PIN | Issuer cannot approve based on details provided    Updated or additional information required |  |
| Visa | 20082 | No security model | Issuer cannot approve based on details provided    Updated or additional information required |  |
| Visa | 2006P | Cardholder ID verification failed | Issuer cannot approve based on details provided    Updated or additional information required |  |
| Visa | 20063 | Security violation | Issuer cannot approve based on details provided    Updated or additional information required |  |

 
Click to see **all other Decline Codes **

| **Scheme** | **Decline code** | **Description** | **Explanation** |
| --- | --- | --- | --- |
| 20001 | Refer to card issuer | The payment has been declined by your bank.  Please try a different card or contact your bank for further support. | This transaction is typically declined due to a risk assessment on the Issuer's side. Some strategies you could recommend to merchants:  1. Display a message asking the shopper to retry the transaction using a different card  2. Display alternative payment mefhods the shopper can use to retry the transaction  3. Display a message asking the shopper to contact their Issuing bank to understand why their transaction is declined and how they can successfuly complete it going forward. NB - please check risk appetite as this could potentially increase fraud |
|  |  | Contact card issuer |  |
|  | 20002 | Refer to card issuer - Special conditions | The payment has been declined by your bank.  Please try a different card or contact your bank for further support. |
|  | 20003 | Invalid merchant or service provider | The payment failed due to a technical issue.  If the issue persists please contact us. |
|  | 20005 | Declined - Do not honour | [The payment has been declined by your bank. Please try a different card or contact your bank for further support. Refer to our recommendation codes](https://www.checkout.com/docs/resources/codes/recommendation-codes) documentation. |
|  | 20006 | Error / Invalid request parameters |  |
|  | 20009 | Request in progress |  |
|  | 20010 | Partial value approved |  |
|  | 20012 | Invalid transaction | The payment has been declined by your bank.  Please try a different card or contact your bank for further support. |
|  | 20013 | Invalid value/amount | The payment failed due to a technical issue.  If the issue persists please contact us. |
|  | 20014 | Invalid account number (no such number) | The payment failed, please check your card details and try again with the same or another card. |
|  | 20017 | Customer cancellation |  |
|  | 20018 | Customer dispute |  |
|  | 20019 | Re-enter transaction |  |
|  | 20019 | Transaction has expired |  |
|  | 20020 | Invalid response |  |
|  | 20021 | No action taken (unable to back out prior transaction) |  |
|  | 20022 | Suspected malfunction |  |
|  | 20023 | Unacceptable transaction fee |  |
|  | 20024 | File update not supported by the receiver |  |
|  | 20025 | Unable to locate record on file |  |
|  | 20025 | Account number is missing from the inquiry |  |
|  | 20026 | Duplicate file update record |  |
|  | 20027 | File update field edit error |  |
|  | 20028 | File is temporarily unavailable |  |
|  | 20029 | File update not successful |  |
|  | 20030 | Format error | The payment failed due to a technical issue. Please try again with the same card, or use a different card. |
|  | 20031 | Bank not supported by Switch |  |
|  | 20032 | Completed partially |  |
|  | 20033 | Previous scheme transaction ID invalid |  |
|  | 20038 | Allowable PIN tries exceeded |  |
|  | 20039 | No credit account |  |
|  | 20040 | Requested function not supported |  |
|  | 20042 | No universal value/amount |  |
|  | 20044 | No investment account |  |
|  | 20046 | Bank decline | [The payment has been declined by your bank. Please try a different card or contact your bank for further support. Refer to our recommendation codes](https://www.checkout.com/docs/resources/codes/recommendation-codes) documentation. |
|  | 20051 | Insufficient funds | The payment has been declined by your bank. Please try a different card or contact your bank for further support. |
|  | 20052 | No current (checking) account |  |
|  | 20053 | No savings account |  |
|  | 20054 | Expired card |  |
|  | 20055 | Incorrect PIN/ PIN validation not possible |  |
|  | 20056 | No card record |  |
|  | 20057 | Transaction not permitted to cardholder | The payment has been declined by your bank.  Please try a different card or contact your bank for further support. |
|  | 20057 | Domestic debit transaction not allowed (Regional use only) |  |
|  | 20058 | Transaction not permitted to terminal |  |
|  | 20059 | Suspected fraud | [The payment has been declined by your bank. Please try a different card or contact your bank for further support. Refer to our recommendation codes](https://www.checkout.com/docs/resources/codes/recommendation-codes) documentation. |
|  | 20060 | Card acceptor contact acquirer |  |
|  | 20061 | Activity amount limit exceeded | [Occurs if the defined amount is exceeded for the account or card. Refer to the page on recommendation codes](https://www.checkout.com/docs/resources/codes/recommendation-codes) for suggested action. |
|  | 20062 | Restricted card | [The payment has been declined by your bank. Please try a different card or contact your bank for further support. Refer to our recommendation codes](https://www.checkout.com/docs/resources/codes/recommendation-codes) documentation. |
|  | 20063 | Security violation |  |
|  | 20064 | Transaction does not fulfil AML requirement | The payment has been declined by your bank. Please try a different card or contact your bank for further support. |
|  | 20065 | Exceeds Withdrawal Frequency Limit | The payment has been declined by your bank. Please try a different card or contact your bank for further support. |
|  | 20066 | Card acceptor call acquirer security |  |
|  | 20067 | Hard capture - Pick up card at ATM |  |
|  | 20068 | Response received too late / Timeout | The payment failed due to a technical issue. Please try again with the same card, or use a different card. |
|  | 20068 | Internal error |  |
|  | 20075 | Allowable PIN-entry tries exceeded | The payment has been declined by your bank. Please try a different card or contact your bank for further support. |
|  | 20078 | Blocked at first use - transaction from new or replacement card that is not properly unblocked | [The payment has been declined by your bank. Please try a different card or contact your bank for further support. Refer to our recommendation codes](https://www.checkout.com/docs/resources/codes/recommendation-codes) documentation. |
|  | 20082 | No security model |  |
|  | 20082 | PIN cryptographic error found (error found by VIC security module during PIN decryption) |  |
|  | 20082 | Negative CAM, dCVV, iCVV, or CVV results |  |
|  | 20083 | No accounts |  |
|  | 20084 | No PBF |  |
|  | 20085 | PBF update error |  |
|  | 20086 | ATM malfunction |  |
|  | 20086 | Invalid authorization type |  |
|  | 20087 | Bad track data (invalid CVV and/or expiry date) | The payment failed, please check your card details and try again with the same or another card. |
|  | 20088 | Unable to dispense/process |  |
|  | 20089 | Administration error |  |
|  | 20090 | Cut-off in progress |  |
|  | 20091 | Issuer unavailable or switch is inoperative | The payment failed due to a technical issue. Please try again with the same card, or use a different card. |
|  | 20092 | Destination cannot be found for routing |  |
|  | 20093 | Transaction cannot be completed; violation of law | [The payment has been declined by your bank. Please try a different card or contact your bank for further support. Refer to our recommendation codes](https://www.checkout.com/docs/resources/codes/recommendation-codes) documentation. |
|  | 20094 | Duplicate transmission / invoice |  |
|  | 20095 | Reconcile error |  |
|  | 20096 | System malfunction | The payment failed due to a technical issue. Please try again with the same card, or use a different card. |
|  | 20097 | Reconciliation totals reset |  |
|  | 20098 | MAC error |  |
|  | 20099 | Other / Unidentified responses | The payment failed due to a technical issue. If the issue persists please contact us. |
|  | 2006P | Cardholder ID verification failed | Cardholder could not be identified from their ID documentation as part of Know Your Customer (KYC) checks. The cardholder should contact their issuing bank to resolve. |
|  | 200N0 | Force STIP |  |
|  | 200N7 | Decline for CVV2 failure |  |
|  | 200O5 | PIN required |  |
|  | 200P1 | Over daily limit |  |
|  | 200P9 | Limit exceeded. Enter a lesser value. |  |
|  | 200R1 | Issuer initiated a stop payment (revocation order) for this authorization | The cardholder has canceled this subscription |
|  | 200R3 | Issuer initiated a stop payment (revocation order) for all authorizations | The cardholder has canceled all subscriptions |
|  | 200S4 | PTLF full |  |
|  | 200T2 | Invalid transaction date |  |
|  | 200T3 | Card not supported |  |
|  | 200T5 | CAF status = 0 or 9 |  |
|  | 20100 | Invalid expiry date format | The payment failed due to invalid expiry date. Please try again providing the correct value. |
|  | 20101 | No Account / No Customer (Token is incorrect or invalid) |  |
|  | 20102 | Invalid merchant / wallet ID | The payment failed due to a technical issue. If the issue persists please contact us. |
|  | 20103 | Card type / payment method not supported | The payment has been declined by your bank. Please try again with a different card or contact your bank for further support. |
|  | 20104 | Gateway reject - Invalid transaction | The payment failed due to a technical issue. Please try again with the same card, or use a different card. |
|  | 20105 | Gateway reject - Violation | The payment failed due to a technical issue. Please try again with the same card, or use a different card. |
|  | 20106 | Unsupported currency |  |
|  | 20107 | Billing address is missing |  |
|  | 20108 | Declined - Updated cardholder available |  |
|  | 20109 | Transaction already reversed (voided) |  |
|  | 20109 | Previous message located for a repeat or reversal, but repeat or reversal data is inconsistent with the original message |  |
|  | 20109 | Capture is larger than initial authorized value |  |
|  | 20110 | Authorization completed |  |
|  | 20111 | Transaction already reversed | The payment reversal has already been processed. |
|  | 20112 | Merchant not Mastercard SecureCode enabled | The payment failed due to a technical issue. Please contact us with the payment reference number. |
|  | 20113 | Invalid property |  |
|  | 20114 | Token is incorrect |  |
|  | 20115 | Missing / Invalid lifetime |  |
|  | 20116 | Invalid encoding |  |
|  | 20117 | Invalid API version | The payment failed due to a technical issue. If the issue persists please contact us. |
|  | 20118 | Transaction pending | The payment failed due to a technical issue. If the issue persists please contact us. |
|  | 20119 | Invalid batch data and/or batch data is missing | The payment failed due to a technical issue. If the issue persists please contact us. |
|  | 20120 | Invalid customer/user | The payment failed due to a technical issue. If the issue persists please contact us. |
|  | 20121 | Transaction limit for merchant/terminal exceeded |  |
|  | 20122 | Mastercard installments not supported |  |
|  | 20123 | Missing basic data: zip, addr, member | The payment failed due to a technical issue. If the issue persists please contact us. |
|  | 20124 | Missing CVV value, required for ecommerce transaction |  |
|  | 20150 | Card not 3D Secure (3DS) enabled |  |
|  | 20151 | Cardholder failed 3DS authentication |  |
|  | 20152 | Initial 3DS transaction not completed within 15 minutes | The payment has expired due to inactivity. Please try again with the same card, or use a different card. |
|  | 20153 | 3DS system malfunction | The payment failed due to a technical issue. Please try again with the same card, or use a different card. |
|  | 20154 | 3DS authentication required | The payment declined due to Strong Customer Authentication (3DS). Please try again with the same card, or use a different card. |
|  | 20155 | 3DS authentication service provided invalid authentication result |  |
|  | 20156 | Requested function not supported by the acquirer |  |
|  | 20157 | Invalid merchant configurations - Contact Support |  |
|  | 20158 | Refund validity period has expired |  |
|  | 20179 | Lifecycle | [Occurs when transaction has invalid card data. Refer to the page on recommendation codes](https://www.checkout.com/docs/resources/codes/recommendation-codes) for suggested action. |
|  | 20182 | Policy | [Occurs when a transaction does not comply with card policy. Refer to the page on recommendation codes](https://www.checkout.com/docs/resources/codes/recommendation-codes) for suggested action. |
|  | 20183 | Security | [Occurs when a transaction is suspected to be fraudulent. Refer to the page on recommendation codes](https://www.checkout.com/docs/resources/codes/recommendation-codes) for suggested action. |
|  | 20193 | Invalid country code |  |
|  | 30004 | Pick up card (No fraud) | The payment has been declined by your bank. Please try a different card or contact your bank for further support. |
|  | 30007 | Pick up card - Special conditions | The payment has been declined by your bank. Please try a different card or contact your bank for further support. |
|  | 30015 | No such issuer | The payment has been declined due to incorrect details. Please try again with updated details. |
|  | 30016 | Issuer does not allow online gambling payout | The payment has been declined by your bank. Please try a different card or contact your bank for further support. |
|  | 30017 | Issuer does not allow original credit transaction | The payment has been declined by your bank. Please try a different card or contact your bank for further support. |
|  | 30018 | Issuer does not allow money transfer payout | The payment has been declined by your bank. Please try a different card or contact your bank for further support. |
|  | 30019 | Issuer does not allow non-money transfer payout | The payment has been declined by your bank. Please try a different card or contact your bank for further support. |
|  | 30020 | Invalid amount | The payment failed due to a technical issue. If the issue persists please contact us. |
|  | 30021 | Total amount limit reached | The payment has been declined by your bank. Please try a different card or contact your bank for further support. |
|  | 30022 | Total transaction count limit reached | The payment has been declined by your bank. Please try a different card or contact your bank for further support. |
|  | 30033 | Expired card - Pick up | The payment has been declined by your bank. Please try a different card or contact your bank for further support. |
|  | 30034 | Suspected fraud - Pick up | The payment has been declined by your bank. Please contact your bank for further support. |
|  | 30035 | Contact acquirer - Pick up | The payment has been declined by your bank. Please try a different card or contact your bank for further support. |
|  | 30036 | Restricted card - Pick up | The payment has been declined by your bank. Please try a different card or contact your bank for further support. |
|  | 30037 | Call acquirer security - Pick up | The payment has been declined by your bank. Please try a different card or contact your bank for further support. |
|  | 30038 | Allowable PIN tries exceeded - Pick up | The payment has been declined by your bank. Please try a different card or contact your bank for further support. |
|  | 30041 | Lost card - Pick up | The payment has been declined by your bank. Please try a different card or contact your bank for further support. |
|  | 30043 | Stolen card - Pick up | The cardholder’s bank has declined the payment because the card has been reported stolen.   For a one-off transaction, do not attempt the transaction again. If possible, do not provide goods or services to the person attempting the transaction.   For a recurring or scheduled transaction, it's possible the card was lost after the last successfully processed payment, or after the scheduled payment's authorization. In either scenario, contact your customer and request that they update their payment method. Replace the account number for their lost card with the account number for their new card. |
|  | 30044 | Transaction rejected - AMLD5 | Transaction was initiated from an anonymous, non-reloadable prepaid card and for an amount greater than 50 EUR. Due to the AMLD5 directive, it cannot be fulfilled. |
|  | 30045 | Invalid payout fund transfer type | If the fund transfer type is not among the list that was configured for allowed funds transfer types, the transaction would fail. |
|  | 30046 | Closed account | The payment has been declined by your bank. Please contact your bank for further support. |
|  | 2005C | 5C (Transaction not supported /   blocked by issuer) |  |

 

 

**ENVIRONMENT 💻**

| Applies to: | Card Processing |
| --- | --- |
| Who uses this: | Merchant Care Agents, Commercial & Merchants |
| Where to find decline codes: | Dashboard, webhooks, API, reports |
