---
id: 22059072514194
section_id: 22057285830034
title: "3DS Response Code 20159: ACS Malfunction Error"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22059072514194-3DS-Response-Code-20159-ACS-Malfunction-Error"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-30T17:07:45Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRP1QGWAFPTEP0CSMC1WBV"]
label_names: ["global", "case_3ds_issue_response_code_20151_-_20156", "case_3ds_issue_response_code_20151_-_20159", "response_code_20159", "case_3ds_issues"]
user_segment_ids: [11003606966930]
archive: false
---

**Use this article when**

Troubleshooting a 20159 response code, which is related to an "ACS Malfunction" error.INTRODUCTION TO RESPONSE CODE 20159 💬

A 20159 error means that the payment failed due to a technical issue with the Access Control Server (ACS) that was used for 3DS authentication.

The ACS is a system used by the card issuer (the customer's bank) to authenticate online card transactions, often by prompting the cardholder for a password or one-time code.

⚠️ This response code is returned by the Issuing Bank when they decline a transaction.

## KEY TAKEAWAYS 🔑

- The error, **Response Code 20159**, specifically means the payment failed due to a technical issue with the **Access Control Server (ACS)** used for 3DS authentication.

- The transaction logs should show the **ResponseCode** as **'20159'**, the **ResponseSummary** as **'ACS Malfunction'**, and the **AuthenticationStatusReason** as **'22'**.

- The response code originates from the **Issuing Bank** when they decline the transaction.

- If the issue is isolated, you should **liaise with the Issuing Bank** to understand the decline.

- If the issue is widespread, or the cause is unclear, it must be **escalated to the OC Team** for clarification, as it could be an issuing bank issue or a Checkout.com outage.

PROCESS FOR TROUBLESHOOTING RESPONSE CODE 20159 🖊️

- 
**Obtain Necessary Information: **Ensure the merchant has provided the required payment information, such as the Payment ID, Session ID, Correlation ID, and Action ID.

- 
**Access Retool: **Open Retool and input the Payment ID into the "Give me an ID" field.

- 
**Query the Payment: **Click "Query" to search for the payment details.

- 
**Review the Event: **Under "Event type," select the `ChargeAuthenticationFailed` event:

- 
**Verify the Response: **Check the logs to confirm the following values are present:

  - 
`AuthenticationStatusReason`: '22'

  - 
`ResponseCode`: '20159'

  - 
`ResponseSummary`: 'ACS Malfunction'

ESCALATION ⬆️If you have confirmed that the error is an "ACS Malfunction" (Response Code 20159), you can escalate the issue:

- 
**Contact the Issuing Bank**: Coordinate with the Issuing Bank to gain a deeper understanding of why the transaction was declined.

- 
**Check for Broader Incidents**: If several merchants report Response Code 20159, check the OC Slack Channel for ongoing incidents. The failure could be due to a Checkout.com outage or an issuing bank issue, and the OC Team can help identify the cause.

- 
**Create a Ticket**: If no incident has been raised on the OC Slack Channel, create a ticket for the OC Team to get clarification on the ACS Malfunction.

  - 
****[Raise a Ticket to L3 OC Engineering Team](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277)[:](https://checkoutsupport.freshservice.com/support/catalog/items/406)

  - Once the ticket is created via Jira, update the Jira ticket with the Zendesk ticket ID

  - Ensure you provide regular updates to the merchant, informing them that this issue has been escalated to the engineering team.

RESOURCES 📍

| Case Examples |
| --- |
| - Zendesk ****[ticket](https://checkout1360.zendesk.com/agent/tickets/60356) example  - OC Team Escalation ****[ticket](https://checkoutsupport.freshservice.com/a/tickets/280211?current_tab=details) example |
