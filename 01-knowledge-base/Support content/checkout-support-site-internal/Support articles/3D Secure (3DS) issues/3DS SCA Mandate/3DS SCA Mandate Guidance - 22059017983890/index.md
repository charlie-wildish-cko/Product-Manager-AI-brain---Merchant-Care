---
id: 22059017983890
section_id: 22057286878482
title: "3DS SCA Mandate Guidance"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22059017983890-3DS-SCA-Mandate-Guidance"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:39:57Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRP1QGWAFPTEP0CSMC1WBV"]
label_names: ["global", "3ds_sca_mandate_guidelines", "case_3ds_issues", "case_3ds_issue_sca_mandate"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

SCA or Strong Customer Authentication is a European regulatory requirement aimed at reducing fraud and making online payments more secure. It requires multi-factor authentication for electronic payments, meaning that two out of three elements are required to verify the identity of the person making the transaction. They are:-

1. Something the customer knows (password or PIN)

2. Something the customer has (mobile phone or wearable device)

3. Something the customer is (fingerprint or facial recognition)

## Process Steps

**Scope**

For online card payments, SCA applies only to transactions **where both business and cardholder bank accounts are located in the EEA and UK**.
  
**Exemptions** 

For transactions that are in the scope of SCA, you can request exemptions from strong authentication if the transactions meet certain criteria. However, the customer's bank has the final say on whether the requested exemption applies. 

The bank will

1. Assess the risk of the payment

2. Decide whether to accept the exemption or reject it

  1. 
**Accept**: If the customer’s bank accepts the requested exemption, the transaction can be completed without strong authentication

  2. 
**Reject**: If the customer’s bank does not allow the exemption, you will receive a 20154 response code, meaning you will need to apply 3DS authentication to the transaction to meet SCA requirements

The 3DS 2.1 and 2.2 protocols support exemptions. Aside from allowing you to remain SCA-compliant in PSD2-mandated regions, exemptions can also help to provide customers with a seamless experience. This is because more transactions can be approved through frictionless authentication.

Additionally, if an issuer declines an exemption, the customer will have to go through the challenge flow instead of having their transaction declined, resulting in a higher acceptance rate.

1. You can request exemptions during authentication with "3ds.enabled": true, or during authorization with **"3ds.enabled": false**

2. If the bank accepts the exemption, whether it was requested during authentication or authorisation, then the transaction can be completed without SCA

3. If the bank rejects an exemption requested during authentication, the transaction is not declined, but the customer will have to go through SCA

4. If the bank rejects an exemption requested during authorisation, you will receive a 20154 response code. 

  1. The payment will need to be retried with 3DS authentication applied and the **"3ds.challenge_indicator"** field set to **"challenge_requested"** or **"challenge_requested_mandate"**

If you request an exemption, and the customer’s bank approves it, you do not benefit from the liability shift. This means you would be liable if the transaction turned out to be fraudulent.

This means that if the exemption is applied and approved by the customer bank. The liability shift would still be with the merchant and not the issuing bank or CKO. If a transaction turns out to be fraudulent. 

- For further guidance on SCA, please see [SCA compliance guide - Docs](https://www.checkout.com/docs/payments/ensure-regulatory-compliance/sca-compliance-guide#What_is_Strong_Customer_Authentication)

- For further guidance on exemptions, please see [SCA compliance guide - Docs](https://www.checkout.com/docs/payments/ensure-regulatory-compliance/sca-compliance-guide#Authentication_exemptions_summary)

Please refer to the [response code 20154](https://docs.google.com/document/d/1YlFtrqETeILqHfQ0yS2A-acR2OXz8ZX9mBP-MYrYMCg/edit#heading=h.vpfnc5val18k) for examples of how to investigate this issue

## Glossaries and Definitions:

For **Key Terms and Definitions** on 3DS, please see ****[3DS Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22059673420818-3DS-Glossary-Introduction)   

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the 3DS articles, please see ****[3DS Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22059810908306-3DS-Tools-Permissions)
