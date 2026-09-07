---
id: 22857180166034
section_id: 28482798009874
title: "How to Register/Enroll in 3D Secure (3DS)"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22857180166034-How-to-Register-Enroll-in-3D-Secure-3DS"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:35:13Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JNGXCVNHFQB2TX90T7Z1YKMZ"]
label_names: ["global", "issuing", "case_card_issuing", "case_card_issuing_how_to_register_enroll_in_3d_secure_3ds"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

Clients must enroll physical cards and multi-use virtual cards in 3DS if 

- They have issued the card within the European Economic Area (EEA) or the UK, and 

- the card that they issued can be used for online payments within the EEA or the UK.

## Process Steps

Steps the client can take:-

1. Have the client log into Dashboard

2. Navigate to Issuing > Cards to locate the card they want to register

3. Once the card is selected, look for the option to set up or enrol in 3D Secure

4. Enter any necessary details, such as:

  1. Cardholder name and contact details

  2. Mobile phone number for OTP delivery

  3. Locale or preferred language for the cardholder

5. Follow the prompts to complete the registration process

6. Alternatively, the client can make an API call, using the [Enroll Card in 3D Secure API Endpoint](https://api-reference.checkout.com/#operation/EnrollCardIn3DS)

7. Verify Enrollment Success: have the client conduct a small test transaction at a 3D Secure-enabled merchant to confirm the registration. The cardholder should be prompted for a verification step, such as entering a One-Time Password (OTP)

8. Educate the Cardholder:** **inform the cardholder on how 3D Secure works and what to expect during online transactions (e.g., receiving an OTP or completing a challenge screen).

9. If any troubleshooting is required, please consider the below:-

  1. Ensure the card supports 3D Secure

  2. Validate that all required information (e.g., mobile number, locale) is correctly provided during the enrollment process

  3. If enrollment fails, have the client provide details of the card and error codes received during the process. Escalate to the Issuing team if needed

10. If a client wants to make a change to enrollment detail for a card, go to Dashvard > Issuing > Cards, search for and select the card that needs updating, select “Edit” (only visible if the card i already enrolled), update the card details and select “Save”

## Glossaries and Definitions:

For **Key Terms and Definitions** on Card Issuing Issues, please see ****[Card Issuing Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22857173195794-Issuing-Glossary-Introduction) 

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Card Issuing articles, please see ****[Card Issuing Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22857178933394-Issuing-Tools-Permissions)
