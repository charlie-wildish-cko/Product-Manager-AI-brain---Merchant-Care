---
id: 28126400866706
section_id: 28126448037650
title: "Card Processing FAQs"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/28126400866706-Card-Processing-FAQs"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-01-19T15:53:58Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JVS26PBA73NGJJETCPWS3SPE", "01K0A5YPGNJY8TA7DKSEEPG6G2"]
label_names: ["faqs", "card_processing", "2068"]
user_segment_ids: [11003606966930]
archive: false
---

Use this article for frequently asked questions oncard processing

## GENERAL TROUBLESHOOTING FAQs**❓ **

What should I do if I see a Card Processing (CP) internal error with code 20068?

This specific error message: "object reference not set to an instance of an object," is technical and requires an engineer to investigate its cause. 

The best course of action is to report the issue to the engineering team by creating a ticket. They will then investigate the root cause, which may be a missing piece of information or another internal system issue.Why might a merchant receive a "Successful" response (202) for a capture attempt, but the transaction later fails during clearing?

You should understand that this is normal because the capture success response (202) is returned by the platform to the gateway based on the **acquiring side**. The subsequent **clearing platform operates disconnectedly**, often in batch processing. If the transaction fails during this later clearing stage (e.g., due to L2/L3 data validation errors), the merchant will not be automatically notified. The Card Processing team is then responsible for investigating and **manually re-triggering the clearing**.Is there a looker report we can use to check scheme declines and trends?

Yes, we can use the looker report [here](https://checkoutinternal.eu.looker.com/dashboards/10013?Requested+Date=2+month+ago+for+2+month&PoP+Visualisation=week&Alias=Swapp&Decline+Code=40101%2C10000&Issuing+Country=)Why might I see a 20019 decline from Card Processing for an Omannet payment when Omannet's own logs show no decline?

This discrepancy occurs because Card Processing initially sends a **timeout response (219)** to the gateway. While an inquiry is then sent to Omannet for the final status, the new response code isn't always updated back to the gateway, resulting in the original 219 timeout response being displayed. If failures for a specific BIN continue, the issue may lie with the **issuer** (e.g., Bank Muscat), and you should reach out to the Issuer Outreach team for assistance, as it is likely not an internal Card Processing issue.How should we handle DCI Apple Pay test cards on the sandbox environment that return a "missing acquirer CVV mapping for code D" error?

You must escalate this to the relevant engineering team (Michael Roberg's team). Since this involves modifying the sandbox environment, you will need to liaise with the **product person** to provide the scenario, the specific test cards, and the expected response so the engineers can update the internal simulator.

## SCHEME DECLINES FAQs**❓**

What does the void decline "Format data format error" (code `20030`) mean?

This error means a piece of data sent for the transaction was in the wrong format.

- The error message specifically points to a problem with the **Electronic Commerce Indicator (ECI)**.

- This can be caused by a failed 3D Secure authentication or if an internal optimization rule changed the original ECI value.

- To fix this, you must consult the card scheme's technical documentation (e.g., the Mastercard Customer Interface Specification) to find the correct format for the ECI value.

If I get a 20002 decline on an older API version (v1.0/v1.5) for a token transaction without a CVV, what is the cause?

This is a known issue on older API versions (v1.0 and v1.5). It occurs because a `**token_indicator**`** flag** is set to `true` in our system (taken from the BIN Visa table) for that card number, which incorrectly triggers a validation that requires token details like the CVV. Since the engineering team is no longer making changes to the older APIs, the **only solution is to migrate the merchant to API v2.0**, where this validation has been relaxed.How should we handle payments declined with 20003 for scheme Discover and currency TRY?

Response code 20003 indicates an invalid or inactive merchant. Check other merchants in the logs to see if they also have low approval rates for Discover and TRY and also check if there’s a trend with specific bins. If further assistance is needed, escalate to issuer outreachWhat is the correct escalation process for pinless debit declines, and should merchants contact the card network directly?

Merchants should not contact the card network directly, as our platform is the intermediary. You should first investigate if the issue is within our scope, and if the information is vague, you should engage **Fiserv**, who acts as the intermediary between our platform and the pinless debit card networks (like NYCE or Pulse). For complex or infrequent cases (edge cases), you will likely need to escalate the issue up to Level 4, which involves the **Product team**, as they handle direct communication with these card networks.Are merchants required to be registered for Visa Level 2 or Level 3 transaction classification in the US?

While the request must contain all required fields, it is currently being verified whether a merchant must also be specifically registered in internal systems to qualify for Level 2 or Level 3 interchange fees. You should consult a payment specialist if a business card transaction is incorrectly classified, as this impacts the interchange fees charged to the merchant.

## TOKENISATION & NETWORK PROCESSING FAQs**❓**

Does the token requestor ID get included in the payload sent to card processors or schemes for network tokens?

No, the network token payload you send to the card processor or scheme generally **does not include the token requestor ID**. It only includes the tokenised card number and the cryptogram.

## TRANSACTION CLEARING & RETRIES FAQs**❓**

What are the three types of clearing failures, and how should you respond to each?

There are three main types of clearing failures:

- 
**Pre-clearing failures:** These occur when a transaction is **not set for clearing** (e.g., the BIN is inactive), meaning the money has not been received from the scheme. No event is emitted, and you must send the transaction to the Payment Team for a **manual adjustment**.

- 
**Rejected transactions:** These are transactions that were sent for clearing but were **rejected by the scheme** (e.g., due to incorrect format or special characters). They are fixable and can be corrected and resubmitted. You **must not perform a manual adjustment** for these, as it would result in the merchant being double-credited.

- 
**'Present Fail' events:** This is the **final state** for non-fixable transactions (e.g., a hardcoded reject for timeliness issues). These transactions are **automatically adjusted** by the payment team, so you do not need to take any action.

When should you perform a manual adjustment for a failed transaction?

You should only perform a manual adjustment for the following scenarios:

- 
**Reversals**.

- 
**Chargebacks** (if not handled by the Dispute team).

- 
**Pre-clearing failures** (transactions that never generated an event because they weren't set for clearing).

You must **never** perform a manual adjustment for transactions marked as 'Presentment Rejected' or 'Present Fail', as this will cause double-crediting if the transaction is later corrected and resubmitted, or if the system auto-adjusts.If you observe a 'Present Fail' event, should you perform a manual adjustment?

No, you should not. The 'Present Fail' event signifies the final state for a transaction that cannot be fixed and is **automatically adjusted** by the payment team. Performing a manual adjustment would result in the merchant being credited twice.How long does it take for rejected transactions to be corrected and resubmitted?

The timeline depends on the complexity of the rejection.

- For simple corrections, such as removing a **special character** that an acquirer like AX rejected, the process can take **one to two days**.

- For more complex issues that require escalation to the engineering team or Product team, the resolution time may extend to **two weeks or even a month**, depending on their capacity and sprint schedules.

What action should you take if a merchant is persistently inquiring about a delayed, rejected transaction?

You should **raise a ticket to the internal CP team** and specify that the merchant's query is urgent. While the team tries to correct and resubmit rejected transactions as part of their regular backlog, urgent queries raised via a ticket will be handled as a **priority** to address the merchant's concerns quickly.How should you handle transactions where the capture fails on the gateway but clears downstream in Card Processing (CP)?

This scenario is a **known, rare issue** where the transaction is genuinely approved and cleared downstream, but the missing event (capture/refund) prevents the financial experience system from crediting the merchant. In this case, because the gateway event does not match the clearing event, the auto-adjustment system fails. You must continue to raise a ticket for a manual adjustment to ensure the merchant is credited.How often do you retry failed transaction clearings?

Retrying failed clearings is a manual process that does not follow a fixed schedule. The frequency of these retries can vary from daily to weekly. 

It depends on the specific card scheme (e.g. Visa, Mastercard) and the team's current workload.What should I tell a merchant about the timeline for a clearing retry?

You can inform the merchant that the team checks daily to update rejects and a retry attempt will be made within **1-3 business days**. However, you should also note that retries are not always guaranteed to happen daily, as the frequency is manual and depends on workload.When a failed clearing is successfully retried, what system event shows this success?

An initial failure generates a `clearing_failed` or `presentment_rejected` event. When the manual retry is successful, a `**presentment_cleared**` event should be created. If you note a successful retry but the `presentment_cleared` event is missing, you must create a jira ticket with the payment ID for the engineering team to investigate the system glitch.What is the immediate action when we see a Clearing Rejected Event but dashboard/Gateway events shows the capture as successful?

Do not raise a manual adjustment. This scenario requires correction by the CP L3 team. You must raise these rejected events directly to the L3 team via jira so they can fix and re-submit the clearing event. If this fails, it will be automatically adjusted so no action is required from merchant care.Why should we avoid manual adjustments for Rejected Events?

 If L3 team successfully re-triggers and clears the transaction later, the merchant's balance will reflect the successful clearing plus the prior debit. This results in the merchant being under-credited or over-debited relative to the final settled amount, causing a new reconciliation error.How should we manage the merchant's expectations regarding rejected events?

Inform the merchant that the funds are secure (as the capture succeeded), but the final settlement reporting is delayed due to a clearing error. Assure them that your team will escalate the re-submission to the internal team (L3) responsible for fixing and clearing the transaction.

## THIRD-PARTY ACQUIRERS (TPAs) 🌍

How do you distinguish between a standard gateway setup and a TPA (Third-Party Acquirer) setup?

In a TPA setup, the merchant must first obtain Merchant Identification Numbers (MIDs) from a local acquiring bank, which handles the settlement, whereas in a standard setup, the gateway handles currencies and settlements directly.Which two primary schemes should you be familiar with when supporting the MENA region?

You should be familiar with MPGS (Mastercard Payment Gateway System) and Cybersource (Visa’s service), as these are the main platforms used for third-party acquisitions.How can you find the exact reason for a rejection in the MPGS logs?

You should search the logs for the word "reject" and examine the specific message located between the "rejected" and "recommendation" fields.What should you do if an MPGS transaction shows a status mismatch between the dashboard and the customer's bank?

You can perform a GET request to the MPGS API via Postman using the merchant ID, order ID, and token found in the logs to verify the final transaction status.How do you investigate the failure reason for a Cybersource transaction?

You must locate the response code in the logs and search for that specific code online, as Cybersource logs are generally less detailed than those for MPGS.What is the protocol for contacting an acquirer regarding Cybersource status mismatches?

This should be done by L1 support who are responsible for contacting the acquirer for status updates, though merchants may also contact them directly as they hold a direct agreement.What is the Omannet transaction flow and who can use it?

Omannet is exclusive to the Oman region; it redirects customers to a hosted page and uses a recovery inquiry to update the transaction status in the event of a timeout.Where can you find the final status for an Omannet transaction in the logs?

You should look for the "Omannet external authorization API" entry in the logs to find the definitive status of the transaction.Are clearing files sent for transactions in the MENA region, such as Muscat?

No, you should be aware that clearing files are generally not shared for Muscat or other MENA countries, with the exception of Saudi Arabia. In Saudi Arabia, clearing only occurs for specific types of transactions processed through a Third-Party Acquirer (TPA). For standard gateway transactions, merchant references are sent to Acquirers only when specifically configured.

## CAPTURE REVERSAL FAQs**❓**

How do I investigate a capture reversal event when I lack visibility?

The difficulty arises because a capture reversal event may be visible, but the **duplicate capture event** that was reversed is missing from the clearing event log. This scenario often occurs due to an **incident** (e.g., a duplicate capture sent for clearing was reversed via a manual incident action). Since the visibility is poor, you should look for the original request and provide the full context to the L3 team, as they may need to investigate how the Financial Infrastructure (FI) team initially identified the duplicate capture.

## SCHEME STATUS CHECK FAQs**❓**

How can you check the clearing status for schemes like DCI, MX, Maestro, and JCN now that they have moved to SDP (Settlement and Reconciliation Tool)?

You will **no longer see the clearing status** for DCI, MX, Maestro, and JCN in the Retool application. You must now run a query on Snowflake to check their status, as these schemes are moving away from the traditional event-based reporting (like `presentment_submitted`, `cleared`, or `rejected`).

## ACCOUNT FUNDING TRANSACTION (AFT) FAQs**❓**

Why would a payment to fund an account (an Account Funding Transaction or AFT) be declined when a normal purchase with the same card goes through?

This is typically an issue with the cardholder's bank. A bank may decline an AFT because that feature is not enabled for that specific card account, often as a security measure. 

Even if standard purchases work fine, services like AFT may be disabled by default. Nothing can be done on our end to force the transaction through. The cardholder must contact their bank and request that the AFT feature be enabled for their card.What does the response code "INTERNAL12" mean for AFT transactions? 

An "INTERNAL12" response code usually indicates that required sender or recipient fields are missing from the payment request. Depending on the type of AFT transaction made, different fields are required as per public docs [here](https://www.checkout.com/docs/payments/manage-payments/perform-an-account-funding-transaction).Why might domestic Europe AFT transactions still fail even when all mandatory fields are included? 

Even though current documentation for domestic Europe transactions only lists the recipient's first name, last name, and account number as mandatory, some card issuers may have stricter requirements and need more sender and recipient information to approve the transaction. Sending more information than the minimum documented requirements can help improve approval rates.What is the best practice to improve approval rates for AFT transactions? 

To improve approval rates, merchants should send the maximum possible recipient and sender details, even if the current documentation doesn't explicitly require them. This approach helps counter fraud and improves authentication and approval rates.What is the recommended next step if AFT transaction failures continue? 

If transactions continue to fail then the issue should be raised on the AFT channel [#-visa-and-mastercard-aft-requirements-queries](https://checkout.enterprise.slack.com/archives/C04AB2Z1XMX) and we can tag Omair Mirza (scheme relationships) if needed. They can contact schemes like Visa or Mastercard directly if the approval rates remain low.Why was my Account Funding Transaction (AFT) declined, even though regular payments work on the same card?

There are a couple of common reasons for this:

- 
**Issuer Doesn't Support It**: The card-issuing bank may not have enabled Account Funding Transactions (AFTs) for that card, even if they allow standard purchases. It is best to check with the issuer first.

- 
**Missing Information**: AFTs require specific sender or recipient information that might be missing or incorrect.

- 
**Unclear Decline Code**: The decline code tells you if the problem came from the issuer or the card scheme (Visa, Mastercard, etc.). However, be aware that response codes starting with a `2` (like `20005`) can come from either source, so you will need to analyze the full response to be sure.

Where can I find the latest information on AFTs internally which includes which MCC's are in scope for each scheme/region?

See doc [here](https://docs.google.com/document/d/19xLEwWkC3h0uJFHgvc1hRL6QzlfsZg8O/edit) 

## DOCUMENTATION FAQs**❓**

Who is responsible for updating the help documents for API (Application Programming Interface) response codes?

The Product team, in collaboration with the Technical Writing team is responsible for updating all merchant-facing documentation, including making API response codes clearer. The Card Processing operations team does not edit this documentation. If you find that a response code is not well-explained, you should provide specific examples to the Product team, who will work to get the documentation updated.What is the correct process for requesting documentation updates for new API response codes?

You should know that Card Processing (CP) Product is not automatically aware of all new response codes that might cause the gateway to default to 220. If a code is missing from the **Gateway to CP mapping on GitHub**, you need to **raise it with the CP Product team** on a case-by-case basis. The Product team is responsible for liaising with the Technical Writing team to add the appropriate wording and documentation for merchant-facing updates.

## REFUND FAQs❓

A refund failed in our system due to a timeout, but it looks successful elsewhere. What should I do?

This happens when a response from the card scheme takes longer than 30 seconds. Our Gateway will time out and mark the transaction as failed, even if our Card Processing (CP) system receives a success message moments later. In this situation, the refund is considered successful and settled by the CP system. ⚠️**Warning**: **Do not** attempt to reverse the refund. Since the transaction was actually successful from a settlement perspective, a reversal would be incorrect and cause reconciliation problems. The correct action is to contact the Gateway team. They must manually trigger the successful refund events to make sure the Gateway's status matches the final status in the Card Processing system.Why did my refund fail with a "card no longer active" error, even though it was approved initially?

This can happen when there is a long period of time between the original purchase and the refund.

- 
**Cause**: Over time, a card's Bank Identification Number (BIN) can be deactivated by the card scheme. Our system checks an internal list of active BINs during the clearing process. If the card's BIN is no longer on that list, the refund will be declined at this final stage, even if the initial authorization was successful.

- 
**How to Confirm**: You can verify this was the cause by looking up the transaction ID in the `clearing_request_table` in Snowflake. The error message will be in the table if this was the reason for the failure.

 Why might a rejected refund event not be returned in the clearing tool?

You should know that a rejection event is not generated if the refund is rejected by the **edit package** (which is common for Visa transactions) before it reaches the card scheme. A rejected clearing event is typically only raised if the transaction is rejected by the card **scheme** itself.What should you do if a successful refund on the dashboard does not generate a clearing event?

You should investigate if the refund is being processed against a capture that is six months to a year old. This is a known recurring issue that requires investigation by the CP L3 team (MRU - Batcave). You should provide the specific examples to them so they can add comments and investigate the lack of clearing events for these older transactions.
