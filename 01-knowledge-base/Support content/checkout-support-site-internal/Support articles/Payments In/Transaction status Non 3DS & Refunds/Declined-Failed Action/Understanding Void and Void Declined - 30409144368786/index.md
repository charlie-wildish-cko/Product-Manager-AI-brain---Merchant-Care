---
id: 30409144368786
section_id: 21991120809362
title: "Understanding Void and Void Declined"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/30409144368786-Understanding-Void-and-Void-Declined"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-12-11T07:25:15Z"
permission_group_id: 26838654181266
content_tag_ids: []
label_names: []
user_segment_ids: [11003606966930]
archive: false
---

**Use this article**

To understand the difference between 'void' and 'void declined'.

💡MADA does not support voids

## INTRODUCTION TO VOID & VOID DECLINED 💬

Merchants often need to cancel or reverse a transaction and this is where the terms "void" and "void declined" come into play. These terms are sometimes confused or used interchangeably by merchants, so this is to clarify their meanings and address related queries from merchants.

For detailed troubleshooting, see the [Scheme Declines](https://checkoutint.zendesk.com/hc/en-us/sections/26832912736274-Scheme-Declines) articles.

## Void: A Successful Cancellation ✅

A void happens when a merchant cancels a payment that was authorized but not yet captured. This means the merchant decides _not_ to complete the transaction after the customer's funds were initially held (authorized).

- Process: Voiding cancels the transaction before it’s finalized.

- Outcome: The funds that were held during authorization are released and returned to the cardholder’s available balance.

When a transaction is voided, the cardholder’s account isn’t charged. The pending authorization (hold on funds) is removed, making the funds available again.

  
⚠️ Voids take approximately 7-15 business days, depending on the customer’s issuing bank.

## Void Declined: An Unsuccessful Cancellation Attempt ❌

A void declined status means that an attempt to void a transaction didn’t go through. When a void request is declined, the cancellation isn’t completed, and the funds either stay on hold or are captured by the merchant, depending on where the original transaction is in the process.

- Process: The system wasn’t able to finish the void request due to an issue behind the scenes.

- Outcome: The transaction remains active, and the funds aren’t immediately returned to the cardholder’s available balance.

Often, merchants cannot fix the issue as the failure may be on the issuer’s or acquirer’s side. Therefore, if you see a "void declined" status, we need to check the transaction logs. Usually, the merchant can identify the cause from the decline code and advise the cardholder to contact their bank to understand the decline reason or to remove any hold on funds. The RRN can also be provided to the cardholder.

A void declined means the transaction stays in its current state, usually authorized or pending. Funds remain held but will eventually be released by the issuer to the cardholder or captured since the transaction is still authorized, depending on the situation.

A transaction with a "void declined" status cannot be refunded because it has not been captured.

### Common Causes for a "Void Declined" Status 🤔

| Category | Common Causes |
| --- | --- |
| Bank/Fraud | The card-issuing bank's fraud rules were triggered. The bank may have placed a temporary hold on the customer's card. |
| Card/Customer | The customer's card may have expired. There may be insufficient funds available to complete the reversal (in some edge cases). |
| Transaction Data | Issues with retrieving the original authorization transaction or incorrect/incomplete card details. |
| System Errors | System malfunctions or internal errors, sometimes labeled as 'SystemMalfunction.' A locked purchase session due to multiple previous declines. |
| Geographic | A geographical mismatch where the seller is located in a different country from the card-issuing bank. |

⚠️ MENA transactions: Contact the acquirer to understand why a void was declined if logs lack sufficient information.

## What does a successful vs declined void look like?

### **Successful void ✅**

- **Event Name:** `Voided`, `ChargeVoided`, or `Void`

- **Description:** Indicates the authorized funds have been released (either by merchant request or authorization expiry).

- 
**Event Flow:** You’ll see a clear event in the payment timeline labeled as “Voided” or “PaymentVoided'', along with the RRN.
 

**How it looks on the Dashboard ****How it looks in Events (Traffic Insights / Payments Tool)**

**Payments tool:**

**Traffic Insights:**

  

When you click on ChargeVoided, you'll see the RRN:

  

The above should be sufficient but if you need to search in Datadog as well, it will look like below in the Gateway API logs:

  

From there, you can delve in the CP logs for more information should it be required.

 

## **Unsuccessful Void ‼️**

- **Event Name:** `ChargeVoidDeclined`, `VoidDeclined`, or `payment_void_declined`

- **Description:** Occurs when a void attempt is declined with the most common reasons being by the acquirer or due to a timeout.

- 
**Event Flow:** You’ll see an event labeled as “Void Declined” or “ChargeVoidDeclined.”
 

## **How it looks on the Dashboard**

  

## **How it looks in Events (Traffic Insights / Payments Tool)**

**Payments tool:**  
  
  
  
**Traffic Insights:**  

 

You can click on the ChargeVoidDeclined event for more details:

  

You can also delve into Datadog for more information in the Gateway API and CP logs. RESOURCES ⭐️

| Related Articles |
| --- |
| [Response code 20012/20030](https://checkoutint.zendesk.com/hc/en-us/articles/21991182344850-Response-code-20012-20030) [Response Code 20005_Declined - Do not honour](https://checkoutint.zendesk.com/hc/en-us/articles/26859702975250-Response-Code-20005-Declined-Do-not-honour) |
