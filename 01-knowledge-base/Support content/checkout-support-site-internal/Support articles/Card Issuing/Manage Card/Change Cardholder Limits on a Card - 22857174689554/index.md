---
id: 22857174689554
section_id: 28482671122194
title: "Change Cardholder Limits on a Card"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22857174689554-Change-Cardholder-Limits-on-a-Card"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:34:43Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JNGXCVNHFQB2TX90T7Z1YKMZ"]
label_names: ["global", "issuing", "case_card_issuing", "case_card_issuing_change_cardholder_limits_on_a_card"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

To modify the spending limits on a card issued through Checkout.com, the client can implement [velocity controls](https://www.checkout.com/docs/card-issuing/manage-controls/card-controls#Apply_velocity_controls_in_the_Dashboard). These controls allow them to set specific spending thresholds over defined timeframes, enhancing budget management and fraud prevention. Below is what you can advise the client when modifying [cardholder limits](https://www.checkout.com/docs/card-issuing/manage-controls/card-controls).

## Process Steps

1. Using the Checkout.com Dashboard:

  1. Log in to Dashboard

  2. Navigate to Issuing > Cards

  3. Locate and select the card you wish to modify by searching or applying filters

  4. In the card's details screen, go to the Controls tab, click on “Add control” and choose the type of control to apply:-

    1. Add a velocity control (set spending thresholds)

    2. Add an allow/block control (restrict or allow transitions for specific MCCs or MIDs

  5. In the Velocity Control window:

    1. Enter the desired amount in the “Amount limit” field

    2. Select the appropriate timeframe from the “Time period” dropdown (e.g. Daily, Weekly, Monthly)

    3. Specify the scope under “Applies to” (e.g. All spending or Specific categories)

  6. In the ALLOW/BLOCK control window:

    1. Choose whether the control should ALLOW or BLOCK transactions

    2. Specify the scope:

      1. Enter the MCC codes to allow/block specific types of merchants (e.g., restaurants, retail stores)

      2. Enter the MID(s) to allow/block specific merchants. 

      3. Optionally, include a description of the control for easier identification

  7. Click “Confirm” to apply the new control settings

2. Additional considerations for the client

  1. 
[Control Profiles](https://www.checkout.com/docs/card-issuing/manage-controls/card-control-profiles): For managing multiple cards with similar limit requirements, consider creating a control profile (Dashboard > Issuing > Cards > Controls > Card control profiles). This allows the client to apply a set of controls to multiple cards efficiently

  2. Monitoring and Adjustments: Regularly review and adjust controls as needed to align with changing spending patterns or risk assessments

## Glossaries and Definitions:

For **Key Terms and Definitions** on Card Issuing Issues, please see ****[Card Issuing Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22857173195794-Issuing-Glossary-Introduction) 

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Card Issuing articles, please see ****[Card Issuing Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22857178933394-Issuing-Tools-Permissions)
