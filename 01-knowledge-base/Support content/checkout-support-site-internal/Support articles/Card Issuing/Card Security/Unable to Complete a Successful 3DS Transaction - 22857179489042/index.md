---
id: 22857179489042
section_id: 28482798009874
title: "Unable to Complete a Successful 3DS Transaction"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22857179489042-Unable-to-Complete-a-Successful-3DS-Transaction"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-31T16:55:43Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JNGXCVNHFQB2TX90T7Z1YKMZ"]
label_names: ["global", "issuing", "case_card_issuing", "case_card_issuing_unable_to_complete_a_successful_3DS_transaction"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

There are two types of 3D Secure authentication: 

- 
**Zero-touch frictionless authentication: **is usually used for B2B transactions in direct issuing. This means that the Mastercard secure screen may flash for a second, however, the screen then shortly changes and goes straight into the authorisation for the transaction. In these cases, cardholders do not need to take any action and we should not get any queries from these clients

- 
**Strong Customer Authentication (SCA)**: tends to be used for consumer card clients. In these cases, cardholders get a challenge screen and then have to enter a one-time password (OTP) and answer a security question

## Process Steps

1. For this issue, the client should provide you with: 

  1. The Card ID

  2. The Transaction ID

2. Explore the following with the client or cardholder: 

  1. 
**Has the cardholder been registered for 3D Secure within Netcetera?**

    1. Log in to Dashboard

    2. Go to the Issuing > Cardholders section and select the specific cardholder

    3. Within the cardholder's profile, confirm if they are enrolled in 3D Secure. If not, they can initiate enrollment by following the steps outlined in the [Enroll a Card in 3D Secure guide](https://www.checkout.com/docs/card-issuing/manage-cards/enroll-a-card-in-3d-secure)

  2. 
**Did the Cardholder get a challenge screen?**

    1. In the Dashboard, access the Payments section to locate the specific transaction

    2. Within the transaction details, look for the 3DS authentication status. A status indicating "Challenge Required" suggests that a challenge screen was presented to the cardholder

  3. 
**Did they enter a One Time Password (OTP) and a security question?**

    1. In the transaction's 3DS authentication section, review the method used for authentication. If the cardholder was required to enter a One-Time Password (OTP) and answer a security question, this information should be recorded here

    2. The cardholder can check whether they completed the authentication by entering the correct OTP and security question answer. An unsuccessful attempt may indicate issues such as incorrect information entry or technical problems

3. If the answer to all of the above is yes, check the dashboard to see if the authorisation transaction has been generated (follow the guidance [here](https://checkout.lightning.force.com/lightning/r/Knowledge__kav/ka008000000I0jeAAC/view))

  1. If the authorisation transaction has come through on the dashboard, this means that the issue is elsewhere rather than with 3D Secure. In this case, please [raise a Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277)

4. If the answer to any of the above is no, [raise a Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277) will need to be raised with the Issuing Processing team.

5. If the authorisation cannot be seen on the dashboard, please check the [Netcetera Admin UI](https://iam.netcetera-payment.ch/authentication.html#/login)

  1. Please note this needs to be done through a secure static IP address, such as Cloud Fare (access request details [here](https://checkout.atlassian.net/wiki/spaces/IE/pages/5621188578/Accessing+Issuing+Retool#1.-Request-access-to-Cloudflare)

  2. In Netcetera, you can check why the authorisation has failed by using the card number. If Netcetera says that the authorisation has gone through without any issues, please [raise a Jira](https://checkout.atlassian.net/servicedesk/customer/portal/111/group/462/create/277)

## Glossaries and Definitions:

For **Key Terms and Definitions** on Card Issuing Issues, please see ****[Card Issuing Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22857173195794-Issuing-Glossary-Introduction) 

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Card Issuing articles, please see ****[Card Issuing Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22857178933394-Issuing-Tools-Permissions)
