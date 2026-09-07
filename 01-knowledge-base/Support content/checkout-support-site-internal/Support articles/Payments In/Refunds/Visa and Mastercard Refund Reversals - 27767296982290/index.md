---
id: 27767296982290
section_id: 21991163953810
title: "Visa and Mastercard Refund Reversals"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/27767296982290-Visa-and-Mastercard-Refund-Reversals"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-03-18T14:21:29Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQT889RQXXSG27BB4ZJ0M"]
label_names: ["case_transactions_issue_refund", "mastercard_reversal_via_api", "visa_reversal_via_api", "case_transactions_issue_incorrect_refund. reversal_requests", "performing_reversals_on_mc_visa_clearing_platform"]
user_segment_ids: [11003606966930]
archive: false
---

**When to use this article**

Use this article when a merchant reports an incorrect refund amount for a Visa or Mastercard transaction and requests it to be reversed. It explains the conditions, risks, and full procedure for carrying out a refund reversal securely. 

Reversing an incorrect refund is time-sensitive and carries compliance risks for the merchant. This SOP ensures reversals are handled consistently, within network limits, and in coordination with relevant internal teams such as Payments and Disputes.

The scope of this procedure applies to Merchant Care teammates and covers reversals for Visa and Mastercard globally.  **It is not applicable for the 'VISA payout reversal' process.**

**Case type: **Payments in

**Issue Type: **Transaction status (Non 3DS & Refunds)

**Reason: **Refund reversal

## INTRODUCTION 💬

The disputes team reaches out to Merchant Care to request a reversal on CAPTURED transactions that were disputed and accepted by the Merchant (Dispute LOST). This applies only to Mastercard transactions acquired in Japan. 

In these situations, you don’t need to follow the adjustment process with the Payment team, since the funds are already debited from the merchant account to Checkout.com once the transaction is marked as “disputed”. 

  
For these requests, please handle the reversals and respond or resolve them as needed. This is part of the dispute team’s process- they submit these requests because they don’t have access to the reversal tools.

## KEY TIMELINES & CONDITIONS ⚠️

Reversals are only possible for Visa and Mastercard transactions, each with distinct timeframes and conditions.

**Visa**: A reversal can be performed if the refund transaction was initiated less than 30 days ago

**Mastercard:** A reversal can be performed within 24 hours (one calendar day) of the refund being initiated.

- 
**Important Note for Mastercard Payouts:** Mastercard Payout Transactions with a "Moneysend" message type on Hermes _**cannot**_ be reversed. This will be declined by the scheme. To check if a Mastercard transaction has a "Moneysend" message type, you can use the SQL query:
`select clearingstatus, *from INTEGRATION.mc.OutgoingTransaction where arn = 'YOUR_ARN'` and look for "Moneysend" under the `MessageType` in the clearing results navigation bar

- A new payload has been shared by the PEO team to reverse Mastercard Refunds, and this can be found [here](https://checkout.atlassian.net/wiki/spaces/PEO/pages/6525027078/Mastercard+reversal+via+API)

- After 24 hours, reversals may still be possible but it requires getting approval from the card issuer first. To do this:

  - Identify the card's Bank Identification Number (BIN), which is the first six digits of the card number.

  - Use the "Issuer Database" in Looker to find the issuer's contact information by searching for the BIN. (Looker > payment-performance-shared-support > Issuer Database > search for the BIN in the search bar > the contact details will be displayed)

  - It is critical to verify that the issuer's name in the database matches the one on the dashboard

  - Contact the issuer to request approval for the reversal

- 
**Note**: The likelihood of receiving feedback or approval from the issuer is low.

## PROCESS STEPS 🖊️

The following steps outline the complete process for executing a refund reversal.**Part 1: Check if the Refund Has Cleared**

1. 
From agent tool kit, check if the original refund transaction has been cleared.   

If you want to get the result in bulk, access the database (via Hermes) to check. Use the following SQL query, inserting the Acquirer Reference Number (ARN) of the refund. In the query results, check the **CLEARINGSTATUS** field. You can only proceed if the status is 'CLEARED'

```//Visa
Select clearingstatus,paymentid,VisaTransactionId, * from VisaOutgoingTransactionRecord where AcquirerReferenceNumber = 'ARN OF THE REFUND'
//Mastercard
select Clearingstatus,Messagetype,Paymentid,MastercardTransactionId, *from INTEGRATION.mc.OutgoingTransaction
where arn in ('ARN OF THE REFUND')
```

⚠️ **Warning:** If the status is not 'CLEARED':

- 
**For Middle East and North Africa (MENA) merchants:** Wait 24 hours before rechecking the status

- 
**For Rest of World (ROW) merchants:** Wait about three hours before checking the status again

Once the status shows as 'CLEARED', you may proceed.**Part 2: Execute the Reversal**💡 **Tip:** Reversals for Visa and Mastercard have different time limits- see key timelines above

1. From the results of the successful SQL query, obtain the VisaTransactionId and DecodedPaymentId

2. A Remote Desktop connection via **Apache Guacamole** is required to perform the reversal

  1. Open Guacamole from your Okta dashboard ([Access](https://checkoutsupport.freshservice.com/a/catalog/request-items/728) can be requested if you do not have it)

  2. Connect using the **SAML** option:-

1. Select the connection named nc-jumpbox-broker.mgmt.checkout.internal

****

1. Log in using your Jumpbox credentials (if you need to password reset, click [here](https://adselfsvc.mgmt.ckotech.co/))

1. Click 'OK' on the warning screen to access the Remote Desktop:-

2. Inside the Remote Desktop, open **Postman**

3. Set up a **POST** request to the [Visa reversal API link](http://internal-cp-clearing-alb-ecs-prod-482749207.eu-west-1.elb.amazonaws.com/new-visa-clearing/api/clearing/reverse)

4. In the 'Body' tab of the request, select **'raw'** and **'JSON'** format.

5. 
Input the VisaTransactionId and PaymentId obtained in Step 1 into the payload as follows: 

```{
  "ReversalTransactions": [
    {
      "VisaTransactionId": YOUR_TRANSACTION_ID,
      "PaymentId": "YOUR_PAYMENT_ID"
    }
  ]
}
```

6. Click **'Send' **(a successful request will return a "message": "OK" with a status of 200 OK)

 **Part 3: Verify the Reversal**

1. Wait 1-2 hours for the reversal to be generated in the agent tool kit or the outgoing table on [Hermes](https://data-access-tool.cko-prod.ckotech.co/data-access-tool-web)  
*The clearing_status for this new reversal transaction will initially be 'Pending'

2. 
Check agent tool kit or run the same SQL query from Part 1. You should now see a new transaction record for the reversal  

*If the reversal is for Visa, confirm that the TransactionCode for the new record is 26, which indicates a reversal of a refund

**Part 4: Complete the Adjustment**

1. The 'Pending' status will change to **'Cleared'** once the settlement files are received. You can re-check the status in the afternoon or the following day. If the reversal is performed before the [cut-off time](https://checkout.atlassian.net/wiki/spaces/CNO/pages/5283742595/PROCESS+Performing+reversals+on+MC+VISA+clearing+platform#VISA), it may be cleared on the same day.

2. Once cleared, open this [Looker Report](https://checkoutinternal.eu.looker.com/explore/finance_treasury/unified_schemes_settlement?toggle=fil,pik&qid=XHr62HUIgcmoBkpW74GFhJ) to check if the reversal has been ‘Settled’

3. Insert the **ARN**, select the **date range** of the reversal, and run the query

  - If it returns an entry, this means that we have already been settled

  - If there is no entry, we have not been settled yet. You must wait for the settlement to be confirmed before sending an adjustment request to the Payments Team

4. Once the settlement has been confirmed, go to Zendesk, and using the original reversal ticket, start a side conversation with the Payments team (select the appropriate region)

5. Provide the following information in the side conversation:

  - Client Name and ID

  - Entity Name and ID

  - Date

  - Amount

  - Scheme

  - ARN

  - Screenshot of the cleared reversal

  - Looker Report of the settled amount

6. After the Payments team confirms the adjustment has been made, inform the merchant and provide them with the **adjustment ID**

 

## ESCALATIONS 🔺

**Mastercard Reversal After 24 Hours:**If a Mastercard refund reversal is requested after the 24-hour window, you must seek approval from the card issuer (see [key timelines and conditions](#h_01JQEN536JGWGHRM3EAW23B1ET) above for steps to take).⚠️**Warning:** The likelihood of receiving a response or approval from the issuer is low. If you do not receive approval, the reversal cannot be processed.**Reversal Not Settled in Looker:**If the Looker report does not show the reversal as 'Settled' after a reasonable amount of time (2-3 business days) do not proceed with the adjustment request.

- 
**Action:** Continue to monitor the Looker report. If the settlement is unusually delayed, raise a ticket with the Payments team for investigation, providing the ARN and transaction details.

## FAQs ❓

 What are the time limits for processing a refund reversal?

- For Visa, a reversal can be performed if the refund was initiated less than 30 days ago

- For Mastercard, the reversal must be done within 24 hours of the refund

  - After 24 hours, you must get approval from the card-issuing bank before you can proceed with the reversal. However, getting this approval is often difficult.

  What does the `TransactionCode` '26' mean?A `TransactionCode` of '26' confirms that the transaction is a reversal of a refund. What do I do if the refund's `CLEARINGSTATUS` is not 'CLEARED'?You cannot proceed. 

- For ROW merchants, you should recheck the status in about three hours

- For MENA merchants, you need to wait 24 hours before checking again
