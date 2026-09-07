---
id: 22857164222610
section_id: 28482812438674
title: "Cardholder hasn't received their Physical Card"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22857164222610-Cardholder-hasn-t-received-their-Physical-Card"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:34:41Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JNGXCVNHFQB2TX90T7Z1YKMZ"]
label_names: ["global", "issuing", "case_card_issuing", "case_card_issuing_cardholder_has_not_received_physical_card"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

For clients or cardholders who are awaiting delivery of their physically issued card, you can check the status of shipping via daily card reports, or escalate to Thales. Please see below the steps to follow.

## Process Steps

1. For this query, obtain the following:- 

  1. Card ID

  2. Cardholder name

2. Consider/determine the following: 

  1. Check the Dashboard to see if the card has been created (Dashboard > Issuing > Cards > Search by Card ID)

  2. Check if the cardholder received confirmation that the card had been created (either through an API response or on Dashboard)

3. Actions to take:

    1. Open the following [drive](https://drive.google.com/drive/folders/18vD8Ur7y2CuyuC9Rbb5UeSC7PWz-6a3s?usp=drive_link) to see the daily card reports

    2. Open the relevant report and filter by client

    3. Locate the respective card on the report using the last 4 digits of the card

    4. Review the Status (e.g. shipped, received, in transit with the carrier) and Tracking ID, to determine the card(s) dispatch status, and share with the client/cardholder so they can track it directly with the carrier

    5. For any issues with daily card reports, please contact the Issuing Operations team, on Slack [#Issuing-Onboarding-Operations](https://checkout.enterprise.slack.com/archives/C08HBJ361TR)

    6. If the required information is not on the card report, raise a ticket via Thales:-

      1. Log in to the [Thales Portal](https://supportportal.thalesgroup.com/csm?id=csm_login)

      2. Click “Create a Case”

      3. Select “Product Technical Issue”

      4. Under **Options**, tick “Show all Thales products”

      5. In the **Product** dropdown, select “D1 Physical Card”

      6. Select an appropriate **Priority**

      7. Set the **Type of issue** to “Incident”

      8. In the Subject box, enter the issue title e.g. Cannot find card dispatch status

      9. In the Description box, be specific but concise about the issue. Provide the necessary details and exactly what you need

      10. Click “Submit”

    7. If there is a link to the Thales ticket you create, note it on your ticket on Zendesk for reference

## Glossaries and Definitions:

For **Key Terms and Definitions** on Card Issuing Issues, please see ****[Card Issuing Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22857173195794-Issuing-Glossary-Introduction) 

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Card Issuing articles, please see ****[Card Issuing Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22857178933394-Issuing-Tools-Permissions)
