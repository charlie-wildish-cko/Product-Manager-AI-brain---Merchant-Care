---
id: 22197311564178
section_id: 22188524004882
title: "E-Commerce Plugins - Initial Troubleshooting"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22197311564178-E-Commerce-Plugins-Initial-Troubleshooting"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:37:33Z"
permission_group_id: 26838654181266
content_tag_ids: ["01H8EDHC0MTG4YFD7E4B42CE0V"]
label_names: ["global", "case_integration", "case_integration_issue_ecommerce_integration", "ecommerce_plugins_troubleshooting", "ecommerce_plugins_initial_troubleshooting"]
user_segment_ids: [11003606966930]
archive: false
---

## Process Steps

1. Verify that the merchant has followed all the steps in the [integration documentation](https://www.checkout.com/docs/payments/accept-payments/connect-to-an-ecommerce-platform)

2. Ensure that the merchant’s platform is supported by Checkout.com

3. Check the plugin version the merchant is using.** **Ensure their e-commerce platform version is compatible with the Checkout.com plugin. To check this, you can use the following steps:

  1. Open datadog logs [here](https://app.datadoghq.com/logs?query=%28%28service%3AMerchant.Api%20OR%20service%3A%22Gateway%20API%22%29%29%20%40PaymentId%3Apay_jj7iofqc5oqebogmlhk6ty4atm&agg_m=count&agg_m_source=base&agg_t=count&cols=service%2Cenv%2C%40http.status_code%2C%40PaymentAction%2C%40Properties.Request.Source.type%2C%40Properties.Request.Source.Number%2C%40Properties.Request.MerchantInitiated%2C%40Properties.Request.Currency%2C%40Properties.Request.3ds.Enabled%2C%40Properties.MerchantId&event=AgAAAZDaENp7wEMKDwAAAAAAAAAYAAAAAEFaRGFFT0JTQUFCRldnNUxpT1dMUmdBUgAAACQAAAAAMDE5MGRhMTMtM2YwZi00ZWYxLWJlOGMtYzhjNjU1NGY5ZTEz&fromUser=true&index=processing&messageDisplay=inline&refresh_mode=sliding&saved-view-id=88535&storage=hot&stream_sort=time%2Cdesc&viz=stream&from_ts=1664101251355&to_ts=1666693251355&live=true) with a payment ID from the merchant

  2. View the Request.Metadata.udf5 parameter, see below screenshot

  3. Inside this parameter, there will be the plugin version

  4. The udf5 parameter will show all e-commerce versions e.g Shopify offsite or onsite module

## Glossaries and Definitions:

For **Key Terms and Definitions** on Integration Issues, please see ****[Integrations Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22198412339346-Integrations-Glossary-Introduction)  

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Integration Issues articles, please see ****[Integrations Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22198326164754-Integrations-Tools-Permissions)
