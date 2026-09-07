---
id: 22857163360018
section_id: 28483258495890
title: "Unable to Load Funds to Checkout Currency Account"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22857163360018-Unable-to-Load-Funds-to-Checkout-Currency-Account"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:33:44Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JNGXCVNHFQB2TX90T7Z1YKMZ"]
label_names: ["global", "unable_to_load_funds", "issuing", "case_card_issuing", "case_card_issuing_unable_to_load_funds_to_currency_account"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

Clients can use any of the following sources to fund their issuing balance

- Funds from a bank account, i.e. top up the issuing balance by transferring money from another bank account

- Funds collected via acquiring: If the client uses Checkout.com for both Acquiring and Issuing, they can merge accounts and automatically fund their issuing balance using acquired funds. Clients should discuss this with their Account Manager if they would like to do this.

- Funds from sub-entity accounts

Please note: There are no amount limits when funding the balance. The updated balance will be reflected in their account and usable by cardholders within 24 hours. If there are insufficient funds in the balance, cardholders’ transactions will be declined

## Process Steps

1. 
**For this issue, the client needs to provide us with:** 

  1. The account information that they are sending the funds to

2. 
**Explore the following with the client or cardholder:**

  1. Check that balance notifications are enabled for the client

    1. Details can be found [here](https://www.checkout.com/docs/funds-management/manage-funds/balances/view-balances#Configure_balance_notifications_) (Dashboard > Profile Icon > Notifications > Balances tab > Enable balance notifications toggle)

  2. Have funds been sent to the correct Checkout account, and if so, when?

    1. Request the date and time the payment was made from the client’s bank account.

    2. Log in to [Dashboard](https://dashboard.checkout.com/) and review the funding logs under the Issuing > Funding

    3. Look for incoming funds for the date and reference provided by the client

    4. Request a copy/screenshot of the bank transfer confirmation/receipt

    5. Verify the account number, IBAN, and reference number used

    6. Confirm the client included the correct reference/identifier when transferring

    7. Check if the top-up reference has been processed

      1. If the reference has been provided, please validate that the reference was passed correctly (Dashboard > Funds > CA > Top up > Reference)

      2. If the top-up reference is correct, please review the FAR (financial actions report) to review top-ups in actions. 

        1. If not located, please raise the issue in the Slack channel #ask-issuing

    8. If there is any doubt, provide the bank details again to the client for verification. Use the bank details provided at the time of go-live or reconfirm with the Issuing Operations team

  3. 
**Is there an error in paying funds into this account?**

    1. Confirm with the client’s bank if the payment was successfully processed and not returned due to:

      1. Incorrect bank details

      2. Insufficient funds in the client’s account

      3. Payment blocked by the sending or receiving bank

    2. Request a bank confirmation or SWIFT message (if applicable) to verify the transaction status

    3. If the funds were sent to Checkout's account but cannot be matched due to a missing or incorrect reference, you may need to escalate to locate unallocated funds via Slack: #ask-issuing

  4. Does the client require the bank details again?

    1. Revisit the original communication sent at the time of go-live to confirm the client received and used the right details

    2. SAS: Clients can [self-serve](https://www.checkout.com/docs/funds-management/move-funds/add-funds) to obtain the bank details for issuing

    3. LTD: Each client has a [folder](https://drive.google.com/drive/u/0/folders/1H-ylJtRhNv9V5CLlo5JXQpA1gI9c0fEP) from onboarding and should contain a Statement of Work (SOW) with the necessary details, including Account number/IBAN, SWIFT/BIC code, and Reference number. To obtain information from the SOW, contact the Issuing Operations team on the Slack channel, [#issuing-onboarding-operations](https://checkout.enterprise.slack.com/archives/C08HBJ361TR)

3. 
**Action Steps:**

  1. If the client is unable to load funds, it could be because funds have not yet been sent to the Checkout account using the bank account details provided to the client by Issuing Operations at the time of go-live

  2. Check if the account details that the client sent the funds to are correct, and take the below actions accordingly:

    1. If the account details are incorrect or missing, follow the steps in 2.4

    2. If the account details are correct but the payment has still not been applied, check if it has been 24 hrs or more since the transaction was initiated and ask for a screenshot of the transfer to confirm the transaction details. If details are correct and it is more than 24 hrs, reach out to the slack channel #issuing-payments for assistance

    3. If the payment was sent to the correct account details, you should notify the team on the slack channel #issuing-payments 

  3. If a merchant notifies us that they are re-sending the money to pre-fund their account:

    1. Alert the team on the #issuing-payments Slack channel so that they can look out for it. Once the team receives the funds, they will process them and provide you with a screenshot of the funds that have been received. If the pre-funding amount has not been received, this is the reason why the client is unable to load funds

    2. Check the live balance for NAS accounts using [Retool](https://retoolprod.mgmt.ckotech.co/apps/6840ab28-c4b7-11ec-909b-bf9c18a51b41/techfinance-finlab/Currency%20Account%20Balances)

  4. If the client says that they have sent the funds and we have not yet received them:

    1. Check with the client when the funds were sent as it can take up to 24 hours for the funds to come into Checkout

If Checkout still does not see this payment after 24 hours of it being sent, you should send an email to the Issuing Operations team at [issuing_operations@checkout.com](mailto:issuing_operations@checkout.com)

## 

For **Key Terms and Definitions** on Card Issuing Issues, please see ****[Card Issuing Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22857173195794-Issuing-Glossary-Introduction) 

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Card Issuing articles, please see ****[Card Issuing Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22857178933394-Issuing-Tools-Permissions)
