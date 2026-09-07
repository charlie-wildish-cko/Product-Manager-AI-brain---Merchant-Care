---
id: 22197327548562
section_id: 22188552840594
title: "Troubleshooting Hosted Payment Pages"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22197327548562-Troubleshooting-Hosted-Payment-Pages"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:33:41Z"
permission_group_id: 26838654181266
content_tag_ids: ["01H8EDHC0MTG4YFD7E4B42CE0V"]
label_names: ["global", "case_integration", "case_integration_issue_hosted_payment_page", "case_integration_issue_payment_links", "hosted_payments_and_payment_links_troubleshooting"]
user_segment_ids: [11003606966930]
archive: false
---

## Process Steps

**Check Onboarding **

1. For both Hosted Payments and Payment Links, please check whether the merchant is onboarded correctly via [retool](https://retoolprod.mgmt.ckotech.co/apps/launchpad/Merchant%20Hosted%20Pages%20Enablement)

2. Select the following:

  1. Environment = _**Sbox**_ (or Prod, whichever applies to your request)

  2. Merchant platform = _**NAS**_

  3. Entity ID = The entity ID from step 2 above (the entity you want to enable HPP/PLink for)

  4. Submit [Onboard/update merchant]

  5. If the merchant is not onboarded, you will see the following message:

To onboard the merchant, please follow the steps listed [here](https://checkout.atlassian.net/wiki/spaces/SE1/pages/5912102398/How+to+enable+HPP+and+PLink).**Check API Keys**

1. If a merchant is unable to request payment for payment links, please verify that they are using the correct API keys (secret key for requesting payments)

  1. We may need to request the merchant to share the request body that is being sent, along with a screenshot of the endpoint link, in case we cannot identify this via the logs

  2. In the below example, we can see the request body in the screenshot as well as the endpoint and saying that they are using the Public key

    1. The merchant is using the public key when requesting a payment while this should be the secret key, so in this case, you should inform the merchant that they are using the wrong keys, and to try again using secret keys

  3. If they are using the correct key, verify the logs in Datadog to find any errors ([DD Link](https://app.datadoghq.com/logs?query=trace_id%3Acd9f4555-e918-4ad5-b953-ec4a1d46c569&cols=service%2Csource&event=AQAAAYZzax0SIa_1gwAAAABBWVp6YXlLRkFBQW14c3k5ODdXMWJRQUk&index=&messageDisplay=inline&stream_sort=time%2Cdesc&viz=stream&from_ts=1626016547911&to_ts=1628608547911&live=true))

    1. Use the merchant's processing channel ID in the filter, search for the request that was launched and verify the Gateway API log. 

    2. In the example below we can see that we got the error ‘payment_method_not_supported’

 Please refer to the following [confluence](https://checkout.atlassian.net/wiki/spaces/GW/pages/5624430773/Investigating+payment+errors) page which details the different types of payment errors merchants may encounter. If you are unable to resolve any issues, please use the Slack support channel for further assistance: **#payment-interfaces**.

## Glossaries and Definitions:

For **Key Terms and Definitions** on Integration Issues, please see ****[Integrations Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22198412339346-Integrations-Glossary-Introduction)  For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Integration Issues articles, please see ****[Integrations Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22198326164754-Integrations-Tools-Permissions)
