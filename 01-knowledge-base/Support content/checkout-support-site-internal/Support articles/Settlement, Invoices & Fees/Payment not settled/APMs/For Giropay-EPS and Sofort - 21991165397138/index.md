---
id: 21991165397138
section_id: 21991120231954
title: "For Giropay/EPS and Sofort"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/21991165397138-For-Giropay-EPS-and-Sofort"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:36:44Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHQKPVKA7XAZRYSRWE7JRH4"]
label_names: ["row", "apms", "case_settlements", "case_settlements_issue_have_i_been_settled_for_this_payment", "for_giropay_eps_and_sofort"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

APM/Card Schemes

Before checking if the merchant has been settled, agents must first search Retool with the provided payment ID to determine whether the settlement is for an APM or a Card Scheme payment.

Steps to take to search Retool using payment ID and find if the transaction is an APM or Card Scheme payment:

- Insert Payment ID in Retool and click on “Query”

- Once the page gives you the query’s results, you can see if the transaction was done with an APM or a Card Scheme (and which scheme) by looking at “Last Acquirer Name”. E.g. in the below example, the payment ID in question was for an AMEX transaction
APMs

Merchants contact CKO to check whether they have been settled for specific APM transactions.

Most of the time, these queries arise due to the transactions being declined or expiring in our platform but CKO still receives the money for them.

**Note**: From Retool Traffic Insights’ main query results page, it is not possible to see which APM has been used, however, this can be checked by clicking on “View Event Details” which will provide further Payment Method information, as seen below.

## Process Steps

For Giropay/EPS and Sofort, agents can check if CKO has received the funds for the transactions. To do this, please follow the relevant steps in the [Confirmation of Received Funds SOP](https://checkout.atlassian.net/wiki/spaces/CHEC/pages/5951555264/Confirmation+of+Received+Funds+-+SOP#Confirmation-of-Received-Funds-Procedure)

If the above step confirms that CKO has received the funds and the merchant has indeed not received the settlement, a manual refund needs to be done - this can be requested in two ways, depending on whether a reconciliation break or a technical issue has occurred. Follow the below guidelines to assist the merchant accordingly:

1. Check whether a reconciliation break or a technical issue has happened:

  1. Reconciliation break: If a reconciliation break has happened, the payment will show as expired on the Dashboard but the customer will have been charged for the transaction

  2. Technical issue: an example of a technical issue would be a cardholder proving that the refund has not been received, but the Dashboard showing the transaction as refunded

2. If a reconciliation break happens: The APM Reconciliation team contacts the Payments team to request the manual refund

  1. The APM recon team will update the [manual refund tracker](https://docs.google.com/spreadsheets/d/13xCWhxBD-Zmeh9dxnNrek8xCHnpXaHA9snFLPUHUKSc/edit?gid=1723819250#gid=1723819250) where the merchant care team can check on the status too. When in doubt, agents can always check with the APM team.

3. If a technical issue has happened: Merchant Care must contact the Payments team to request a manual refund

  1. To contact the Payments team, use the relevant regional “Treasury Payments” macro to create a side conversation in Zendesk from your merchant’s ticket. For further information, please see [here](https://checkout.atlassian.net/wiki/spaces/CHEC/pages/5991727266/Case+Handling+-+SOP#Emailing-internal-partner-teams%3A)

- Regardless of which method is used for requesting the manual refund, the Merchant Care agent is then responsible for advising the merchant of the case’s outcome and closing the loop with the merchant

**Note**: If the above steps show that CKO has not received the funds, the agent should inform the merchant accordingly. No refund is required

## Glossaries and Definitions:

For **Key Terms and Definitions** on Transactions as well as an **introduction into MENA Gateway and non-Gateway merchants**, please see ****[Settlements Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/21991207693458-Settlements-Glossary-Introduction)   

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Transactions articles, please see ****[Settlements Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/21991176789266-Settlements-Tools-Permissions)
