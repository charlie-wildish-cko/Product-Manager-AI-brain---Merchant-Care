# Payment Code Definitions — AI Reference Table

Reference table for the Support API data layer. Maps payment field values to plain-language AI summaries for use by Fin and Agent Consultant.

**Matching logic:** Most specific row wins. `*` = wildcard fallback — every lookup resolves to a message.

---

## Status

| Field Name | Field Value | Payment type | Payment method | Region | AI Summary |
|---|---|---|---|---|---|
| Status | Authorization | * | * | * | The payment was authorised — funds are held but not yet taken from the cardholder. |
| Status | Capture | * | * | * | The merchant has requested the funds — the cardholder will be charged. |
| Status | Partial Capture | * | * | * | The merchant captured only part of the authorised amount — the remainder was released. |
| Status | Refund | * | * | * | A refund was issued to the cardholder against a previous charge. |
| Status | Void | * | * | * | The authorisation was cancelled before the merchant took the funds — the cardholder was not charged. |
| Status | Card Verification | * | * | * | The card was verified without any charge being made. |
| Status | Payout | * | * | * | Funds were sent to the cardholder's card — this is not a refund but a standalone payment out. |
| Status | Return | * | * | * | Funds were returned to the cardholder outside the standard refund process. |
| Status | Chargeback | * | * | * | The cardholder's bank has reversed this payment as part of a dispute. |
| Status | Fraud Detection - Pre-auth - Accept | * | * | * | The fraud engine reviewed this payment before authorisation and passed it as low risk. |
| Status | Fraud Detection - Pre-auth - Decline | * | * | * | The fraud engine blocked this payment before authorisation due to high risk signals. The cardholder was not charged. |
| Status | Fraud Detection - Post-auth - Capture | * | * | * | The fraud engine reviewed this payment after authorisation and cleared it for capture. |
| Status | 3DS - Authentication Approved | * | * | * | The cardholder passed 3D Secure authentication successfully. |
| Status | Authentication Requested | * | * | * | A 3D Secure authentication challenge was sent to the cardholder. |
| Status | Pending | * | * | * | The payment is in progress — waiting for the customer to complete their action or the bank to respond. |
| Status | Capture Pending | * | * | * | The customer approved the payment and funds are being collected — confirmation is pending. |
| Status | Approved | * | * | * | The customer approved this payment — the merchant still needs to capture the funds. |
| Status | Context Approved | * | * | * | The BNPL provider has pre-approved this transaction — the customer still needs to complete checkout. |
| Status | Cancelled | * | * | * | The customer cancelled this payment before completing it. |
| Status | Expired | * | * | * | This payment expired before the customer completed it or the merchant captured it — no charge was made. |
| Status | Expired | APM | PayPal | * | The PayPal request was not completed and has expired. The customer needs to retry their order. |
| Status | Expired | APM | Sofort | * | The Sofort redirect expired (2-hour window). The customer needs to restart checkout. |
| Status | Returned | * | * | * | This payment was reversed after it had already been collected — funds have been returned to the customer. |
| Status | Returned | * | SEPA Direct Debit | * | This SEPA direct debit was reversed after collection. This can happen up to 5 days post-settlement (bank return), 8 weeks (authorised refund), or 13 months (unauthorised dispute). |
| Status | Returned | * | ACH | * | This ACH direct debit was reversed after collection. Common reasons include insufficient funds, account closed, or a dispute by the account holder. |
| Status | Voided | * | * | * | The payment was voided after approval — the customer will not be charged for the remaining amount. |
| Status | Capture Declined | * | * | * | The attempt to collect funds failed after the customer approved — the payment was not completed. |
| Status | Refund Pending | * | * | * | A refund has been requested and is being processed — it has not yet been confirmed. |
| Status | Refund Declined | * | * | * | The refund attempt was rejected — the funds have not been returned to the customer. |
| Status | Refund Declined | * | Mada | MENA | MADA refunds are not permitted after the 30-day expiry period. The original transaction is too old to refund via this method. |
| Status | Void Declined | * | * | * | The attempt to void this payment was rejected — the payment remains active. |

---

## Network Token Available

| Field Name | Field Value | Payment type | Payment method | Region | AI Summary |
|---|---|---|---|---|---|
| Network token available | Yes | * | * | * | A network token is available for this card — this can improve authorisation rates and reduce fraud risk. |
| Network token available | No | * | * | * | No network token is available for this card — it was charged using the raw card details. |

---

## Payment Method

| Field Name | Field Value | Payment type | Payment method | Region | AI Summary |
|---|---|---|---|---|---|
| Payment method | Visa | * | * | * | The cardholder paid by Visa card. |
| Payment method | Mastercard | * | * | * | The cardholder paid by Mastercard. |
| Payment method | American Express | * | * | * | The cardholder paid by American Express. |
| Payment method | Klarna | * | * | * | The customer paid using Klarna — a buy now pay later method. |
| Payment method | PayPal | * | * | * | The customer paid using PayPal. |
| Payment method | iDEAL | * | * | * | The customer paid using iDEAL — a Dutch bank redirect method. |
| Payment method | Sofort | * | * | * | The customer paid using Sofort — a European bank redirect method. |
| Payment method | Bancontact | * | * | * | The customer paid using Bancontact — the Belgian domestic payment scheme. |
| Payment method | SEPA Direct Debit | * | * | * | The customer paid via SEPA Direct Debit — a bank debit across the SEPA region. |
| Payment method | ACH | * | * | * | The customer paid via ACH Direct Debit — a US bank debit method. |

---

## Scheme

| Field Name | Field Value | Payment type | Payment method | Region | AI Summary |
|---|---|---|---|---|---|
| Scheme | Visa | * | * | * | This transaction was acquired and settled under the Visa scheme rules. |
| Scheme | Mastercard | * | * | * | This transaction was acquired and settled under the Mastercard scheme rules. |
| Scheme | American Express | * | * | * | This transaction was acquired and settled under the American Express scheme rules. |
| Scheme | Diners Club International | * | * | * | This transaction was acquired and settled under the Diners Club International scheme rules. |
| Scheme | Discover | * | * | * | This transaction was acquired and settled under the Discover scheme rules. |
| Scheme | JCB | * | * | * | This transaction was acquired and settled under the JCB scheme rules. |

---

## CVV Check

| Field Name | Field Value | Payment type | Payment method | Region | AI Summary |
|---|---|---|---|---|---|
| CVV check | Y - CVV matched | * | * | * | The CVV was correct — the security code matched the issuer's record. |
| CVV check | D - CVV did not match | * | * | * | The CVV provided did not match — the security code was incorrect. This is a common reason for issuer declines. |
| CVV check | N - CVV not present | * | * | * | The CVV was not provided by the merchant even though it should be on the card. |
| CVV check | P - Check not performed | * | * | * | No CVV check was run on this transaction. |
| CVV check | U - Issuer does not support CVV | * | * | * | The issuing bank does not support CVV checks — this is expected for some issuers. |
| CVV check | X - CVV not available | * | * | * | CVV information was unavailable for this transaction. |

---

## AVS Check

| Field Name | Field Value | Payment type | Payment method | Region | AI Summary |
|---|---|---|---|---|---|
| AVS check | A | * | * | * | The street address matched but the postcode did not — partial AVS match. |
| AVS check | B | * | * | * | The street address matched but the postcode could not be verified — common for international cards. |
| AVS check | D | * | * | * | Both street address and postcode matched — full AVS match on a Visa international card. |
| AVS check | N | * | * | * | Neither the address nor the postcode matched — AVS failed. |
| AVS check | S | * | * | * | The issuer does not support AVS checks. |
| AVS check | U | * | * | * | The issuer does not participate in AVS — no address check was performed. |
| AVS check | W | * | * | * | The postcode matched but the street address did not — partial AVS match. |
| AVS check | X | * | * | * | Both street address and nine-digit ZIP code matched — full AVS match (US cards). |
| AVS check | Y | * | * | * | Both street address and postcode matched — full AVS match. |
| AVS check | Z | * | * | * | The postcode matched but the street address did not — partial AVS match. |

---

## Payment Type

| Field Name | Field Value | Payment type | Payment method | Region | AI Summary |
|---|---|---|---|---|---|
| Payment type | Regular | * | * | * | This is a standard one-off payment. |
| Payment type | MOTO | * | * | * | The card details were provided by phone or post — not entered online by the cardholder. |
| Payment type | Recurring | * | * | * | This is a recurring charge — the cardholder's card is billed automatically on a schedule. |
| Payment type | Installment | * | * | * | This is one instalment in a series of scheduled charges. |
| Payment type | Account_Funding | * | * | * | This is a funds transfer to a card — not a purchase. Common for wallet top-ups or P2P transfers. |

---

## Card Type

| Field Name | Field Value | Payment type | Payment method | Region | AI Summary |
|---|---|---|---|---|---|
| Card type | Credit | * | * | * | The cardholder paid with a credit card — funds are drawn from a credit line. |
| Card type | Debit | * | * | * | The cardholder paid with a debit card — funds come directly from their bank account. |
| Card type | Prepaid | * | * | * | The cardholder paid with a prepaid card — funds come from a pre-loaded balance. |

---

## Is AFT

| Field Name | Field Value | Payment type | Payment method | Region | AI Summary |
|---|---|---|---|---|---|
| Is AFT | Yes | * | * | * | This is an Account Funding Transaction — funds are being sent to the card rather than collected from it. |
| Is AFT | No | * | * | * | This is a standard payment — not an Account Funding Transaction. |

---

## Authentication Experience (3DS)

| Field Name | Field Value | Payment type | Payment method | Region | AI Summary |
|---|---|---|---|---|---|
| Authentication experience | 3DS | * | * | * | 3D Secure authentication was used for this payment. |
| Authentication experience | Frictionless | * | * | * | The cardholder was authenticated silently in the background — no action was required from them. |
| Authentication experience | Challenge | * | * | * | The cardholder was asked to actively verify their identity — for example via a one-time passcode. |
| Authentication experience | Decoupled | * | * | * | The cardholder authenticated separately from the checkout — for example via a notification in their banking app. |

---

## Authentication Status (3DS)

| Field Name | Field Value | Payment type | Payment method | Region | AI Summary |
|---|---|---|---|---|---|
| Authentication status | Y | * | * | * | The cardholder was successfully authenticated via 3D Secure. |
| Authentication status | N | * | * | * | 3DS authentication failed — the cardholder could not be verified and the transaction was denied. |
| Authentication status | U | * | * | * | 3DS authentication could not be completed — the issuer or authentication system was temporarily unavailable. |
| Authentication status | A | * | * | * | Authentication was attempted but the card is not enrolled in 3DS — a partial liability shift may still apply. |
| Authentication status | C | * | * | * | The issuer is requesting the cardholder completes a challenge before authentication can finish. |
| Authentication status | R | * | * | * | Authentication was rejected by the issuer — this transaction should not be retried. |

---

## ECI

| Field Name | Field Value | Payment type | Payment method | Region | AI Summary |
|---|---|---|---|---|---|
| ECI | 02 | * | Mastercard | * | 3DS authentication was successful on Mastercard — liability for fraud shifts to the issuer. |
| ECI | 01 | * | Mastercard | * | Authentication was handled by a stand-in service on Mastercard — liability shifts to the issuer. |
| ECI | 07 | * | Mastercard | * | Authentication succeeded for this recurring Mastercard transaction — liability shifts to the issuer. |
| ECI | 04 | * | Mastercard | * | Frictionless authentication via Mastercard Identity Check — the merchant retains liability. |
| ECI | 06 | * | Mastercard | * | This transaction was exempt from SCA on Mastercard — the merchant retains liability. |
| ECI | 00 | * | Mastercard | * | Authentication failed or could not be attempted on Mastercard — the merchant retains liability. |
| ECI | N0/N2 | * | Mastercard | * | This was a non-payment authentication on Mastercard — no charge was processed. |
| ECI | 05 | * | Visa | * | 3DS authentication was successful on Visa — liability for fraud shifts to the issuer. |
| ECI | 06 | * | Visa | * | Authentication was handled by a stand-in service on Visa — liability shifts to the issuer. |
| ECI | 07 | * | Visa | * | Authentication used an exemption or was unsuccessful on Visa — the merchant retains liability. |
| ECI | 05 | * | American Express | * | 3DS authentication was successful on Amex — liability for fraud shifts to the issuer. |
| ECI | 06 | * | American Express | * | Authentication was handled by a stand-in service on Amex — liability shifts to the issuer. |
| ECI | 07 | * | American Express | * | Authentication used an exemption or was unsuccessful on Amex — the merchant retains liability. |
| ECI | 05 | * | Discover | * | 3DS authentication was successful on Discover — liability for fraud shifts to the issuer. |
| ECI | 06 | * | Discover | * | Authentication was handled by a stand-in service on Discover — liability shifts to the issuer. |
| ECI | 07 | * | Discover | * | Authentication used an exemption or was unsuccessful on Discover — the merchant retains liability. |
| ECI | 05 | * | JCB | * | 3DS authentication was successful on JCB — liability for fraud shifts to the issuer. |
| ECI | 06 | * | JCB | * | Authentication was handled by a stand-in service on JCB — liability shifts to the issuer. |
| ECI | 07 | * | JCB | * | Authentication used an exemption or was unsuccessful on JCB — the merchant retains liability. |
| ECI | 05 | * | Diners Club International | * | 3DS authentication was successful on Diners Club — liability for fraud shifts to the issuer. |
| ECI | 06 | * | Diners Club International | * | Authentication was handled by a stand-in service on Diners Club — liability shifts to the issuer. |
| ECI | 07 | * | Diners Club International | * | Authentication used an exemption or was unsuccessful on Diners Club — the merchant retains liability. |

---

## Challenge Indicator

| Field Name | Field Value | Payment type | Payment method | Region | AI Summary |
|---|---|---|---|---|---|
| Challenge indicator | No_preference | * | * | * | No challenge preference was set — the issuer decided whether to challenge the cardholder. |
| Challenge indicator | Challenge_requested | * | * | * | The merchant requested a challenge — the cardholder was asked to actively verify their identity. |
| Challenge indicator | Challenge_requested_mandate | * | * | * | A challenge was mandated — the cardholder was required to verify their identity by policy. |
| Challenge indicator | No_challenge_requested | * | * | * | The merchant requested no challenge — an exemption was applied to skip cardholder verification. |

---

## Authentication Method Completion (3DS)

| Field Name | Field Value | Payment type | Payment method | Region | AI Summary |
|---|---|---|---|---|---|
| Authentication method completion | Y | * | * | * | Device data was successfully collected before authentication — this supports a stronger risk assessment. |
| Authentication method completion | N | * | * | * | Device data could not be collected before authentication — the issuer had less data to assess risk. |
| Authentication method completion | U | * | * | * | It is unknown whether device data was collected before authentication. |

---

## ACS Challenge Mandated

| Field Name | Field Value | Payment type | Payment method | Region | AI Summary |
|---|---|---|---|---|---|
| ACS challenge mandated | Yes | * | * | * | The issuer required the cardholder to complete a challenge — for example a one-time passcode. |
| ACS challenge mandated | No | * | * | * | No challenge was required — the cardholder was authenticated silently. |

---

## Authentication Status Reason (3DS)

| Field Name | Field Value | Payment type | Payment method | Region | AI Summary |
|---|---|---|---|---|---|
| Authentication status reason | 14 | * | * | * | Authentication timed out at the issuer's system — the session expired before the cardholder responded. |
| Authentication status reason | 22 | * | * | * | The issuer's authentication system encountered an error during processing. |

---

## Message Category (3DS)

| Field Name | Field Value | Payment type | Payment method | Region | AI Summary |
|---|---|---|---|---|---|
| Message category | 01 | * | * | * | This was a standard payment authentication using 3DS. |
| Message category | 02 | * | * | * | This was a card verification — no payment was processed. |

---

## Risk Score

| Field Name | Field Value | Payment type | Payment method | Region | AI Summary |
|---|---|---|---|---|---|
| Risk score | 0–30 | * | * | * | This payment has a low risk score — the fraud engine considers it unlikely to be fraudulent. |
| Risk score | 31–69 | * | * | * | This payment has a medium risk score — some fraud signals are present and it may warrant review. |
| Risk score | 70–100 | * | * | * | This payment has a high risk score — strong fraud signals were detected and it may have been blocked. |

---

## Risk Score Contributors

| Field Name | Field Value | Payment type | Payment method | Region | AI Summary |
|---|---|---|---|---|---|
| Device activity | Increase value | * | * | * | The device used for this payment looks unfamiliar or unusual — this is raising the risk score. |
| Device activity | Decrease value | * | * | * | The device used looks legitimate and familiar — this is lowering the risk score. |
| Card activity | Increase value | * | * | * | This card's recent activity looks unusual — for example high transaction velocity — which is raising the risk score. |
| Card activity | Decrease value | * | * | * | This card's recent activity looks normal — this is lowering the risk score. |
| Fraud history | Increase value | * | * | * | Prior fraud signals have been detected for this card or customer — this is raising the risk score. |
| Fraud history | Decrease value | * | * | * | No prior fraud history is linked to this card or customer — this is lowering the risk score. |
| Identity | Increase value | * | * | * | Identity details such as name or email show inconsistencies — this is raising the risk score. |
| Identity | Decrease value | * | * | * | Identity details are consistent and recognisable — this is lowering the risk score. |
| Locations | Increase value | * | * | * | The payment location doesn't match the card's home country or billing address — this is raising the risk score. |
| Locations | Decrease value | * | * | * | Location signals are consistent — the IP matches the expected geography for this card. |
| Payment details | Increase value | * | * | * | Something about this payment — such as the amount or currency — looks atypical and is raising the risk score. |
| Payment details | Decrease value | * | * | * | The payment amount and details look normal for this card and merchant — this is lowering the risk score. |
| Business risk | Increase value | * | * | * | Merchant-level risk factors such as a high chargeback rate are raising the risk score for this payment. |
| Business risk | Decrease value | * | * | * | Merchant-level signals indicate low risk — this is lowering the overall risk score. |

---

## Response Code

| Field Name | Field Value | Payment type | Payment method | Region | AI Summary |
|---|---|---|---|---|---|
| Response code | 10000 | * | * | * | The payment was approved. |
| Response code | 10008 | * | * | * | The payment was approved — the issuer requires the cardholder to show ID. |
| Response code | 10010 | * | * | * | A partial amount was approved — not the full requested amount. |
| Response code | 10100 | * | * | * | The payment was approved but flagged by the risk engine for review. |
| Response code | 10200 | * | * | * | The payment was authorised and capture has been deferred. |
| Response code | 20001 | * | * | * | The issuer declined and is asking the cardholder to contact their bank. |
| Response code | 20003 | * | * | * | The issuer does not recognise this merchant — may require configuration review. |
| Response code | 20005 | * | * | * | The issuer declined without giving a specific reason — the cardholder should contact their bank. |
| Response code | 20012 | * | * | * | The transaction was invalid — for example an invalid action type or configuration. |
| Response code | 20013 | * | * | * | The payment amount is invalid — for example zero or formatted incorrectly. |
| Response code | 20014 | * | * | * | The card number is not recognised — the cardholder may need to use a different card. |
| Response code | 20017 | * | * | * | The cardholder cancelled the transaction. |
| Response code | 20019 | * | * | * | The transaction expired or failed — the merchant should retry. |
| Response code | 20030 | * | * | * | The void failed because the authorisation has already expired — the issuing bank released the funds automatically. The merchant should confirm with the customer that the funds are available in their account. If a refund is needed, it must be processed separately. |
| Response code | 20030 | * | Mada | MENA | The refund failed because MADA transactions must be refunded within 30 days of the original transaction. If the window has passed, the refund must be processed manually through the acquirer. |
| Response code | 20038 | * | * | * | The cardholder exceeded the allowed PIN attempts — the card may be temporarily blocked. |
| Response code | 20040 | * | * | * | The requested operation is not supported for this card or issuer. |
| Response code | 20051 | * | * | * | The cardholder does not have enough funds — they should top up their account and retry. |
| Response code | 20054 | * | * | * | The card has expired — the cardholder should use a new card. |
| Response code | 20055 | * | * | * | The PIN entered was incorrect or could not be validated. |
| Response code | 20056 | * | * | * | The issuer has no record of this card — it may be cancelled or invalid. |
| Response code | 20057 | * | * | * | The cardholder's card has a restriction blocking this transaction type — they should contact their bank. |
| Response code | 20058 | * | * | * | This transaction type is not permitted on this terminal or processing configuration. |
| Response code | 20059 | * | * | * | The issuer's fraud system flagged this payment — the cardholder should contact their bank. |
| Response code | 20061 | * | * | * | The transaction exceeds the cardholder's spend limit — they should contact their bank. |
| Response code | 20062 | * | * | * | The card is restricted from making this type of payment. |
| Response code | 20063 | * | * | * | A security check failed — the cardholder should contact their bank. |
| Response code | 20065 | * | * | * | The cardholder has made too many transactions in the allowed period — they should try again later. |
| Response code | 20068 | * | * | * | The transaction timed out — this is typically a temporary issue. The merchant can retry. |
| Response code | 20075 | * | * | * | The cardholder exceeded the allowed PIN attempts — the card may be temporarily blocked. |
| Response code | 20078 | * | * | * | The card has not been activated — the cardholder should contact their bank to activate it. |
| Response code | 20082 | * | * | * | A security check on the card data failed — the cardholder should contact their bank. |
| Response code | 20087 | * | * | * | The card data submitted was invalid — the CVV or expiry date may be incorrect. |
| Response code | 20091 | * | * | * | The issuer's system was temporarily unavailable — this is a transient issue. The merchant can retry. |
| Response code | 20092 | * | * | * | The payment could not be routed to the issuer — may be a temporary network issue. The merchant can retry. |
| Response code | 20094 | * | * | * | This transaction appears to be a duplicate of one already submitted. |
| Response code | 20096 | * | * | * | A system error occurred — this is typically temporary. The merchant can retry. |
| Response code | 20099 | * | * | * | The decline reason could not be identified — the cardholder should contact their bank. |
| Response code | 200N7 | card | * | * | The CVV2 security code did not match — the cardholder should check their card details and retry. |
| Response code | 200R1 | * | * | * | The issuer has placed a stop on this specific payment — the cardholder should contact their bank. |
| Response code | 200R3 | * | * | * | The issuer has revoked all authorisations for this card — the cardholder must contact their bank. |
| Response code | 20100 | * | * | * | The expiry date submitted was in an invalid format. |
| Response code | 20103 | * | * | * | This card type or payment method is not supported for this transaction. |
| Response code | 20106 | * | * | * | The currency used is not supported for this card or merchant configuration. |
| Response code | 30004 | * | * | * | The issuer is requesting the card be retained — not fraud-related. The cardholder should contact their bank. |
| Response code | 30007 | * | * | * | The issuer is requesting the card be retained under special conditions. The cardholder should contact their bank. |
| Response code | 30015 | * | * | * | The issuer identified by the card's BIN does not exist — the card number may be invalid. |
| Response code | 30033 | * | * | * | The card has expired and the issuer is requesting it be retained. The cardholder should contact their bank. |
| Response code | 30034 | * | * | * | The issuer suspects fraud and is requesting the card be retained. The cardholder should contact their bank. |
| Response code | 30041 | * | * | * | This card has been reported lost — the issuer is requesting it be retained. The cardholder should contact their bank. |
| Response code | 30043 | * | * | * | This card has been reported stolen — the issuer is requesting it be retained. The cardholder should contact their bank. |
| Response code | 30046 | * | * | * | The account linked to this card has been closed — the cardholder should use a different card. |
| Response code | 41101 | * | * | * | This payment was blocked by a merchant-level risk rule configured in Checkout.com. |
| Response code | 41201 | * | * | * | This card number is on the merchant's decline list — the payment was blocked. |
| Response code | 41202 | * | * | * | This card's BIN is on the merchant's decline list — the payment was blocked. |
| Response code | 41203 | * | * | * | This email address is on the merchant's decline list — the payment was blocked. |
| Response code | 41204 | * | * | * | This phone number is on the merchant's decline list — the payment was blocked. |
| Response code | 41205 | * | * | * | This IP address is on the merchant's decline list — the payment was blocked. |
| Response code | 41301 | * | * | * | The fraud score for this payment exceeded the merchant's configured threshold — it was blocked by their risk settings. |
| Response code | 43101 | * | * | * | Checkout.com's risk engine flagged this payment as potentially fraudulent. |
| Response code | 43102 | * | * | * | This payment was blocked by a Checkout.com platform-level risk rule — the rule group name appears in the response summary. |
| Response code | 43201 | * | * | * | This card number is on Checkout.com's platform-level decline list — the payment was blocked. |
| Response code | 43202 | * | * | * | This card's BIN is on Checkout.com's platform-level decline list — the payment was blocked. |
| Response code | 43203 | * | * | * | This email address is on Checkout.com's platform-level decline list — the payment was blocked. |
| Response code | 43204 | * | * | * | This phone number is on Checkout.com's platform-level decline list — the payment was blocked. |
| Response code | 43205 | * | * | * | This IP address is on Checkout.com's platform-level decline list — the payment was blocked. |
| Response code | 43206 | * | * | * | This email domain is on Checkout.com's platform-level decline list — the payment was blocked. |
| Response code | 43301 | * | * | * | The fraud score exceeded Checkout.com's platform-level threshold — the payment was blocked automatically. |
| Response code | 43401 | * | * | * | This payment requires 3DS authentication — it cannot proceed without it. |

