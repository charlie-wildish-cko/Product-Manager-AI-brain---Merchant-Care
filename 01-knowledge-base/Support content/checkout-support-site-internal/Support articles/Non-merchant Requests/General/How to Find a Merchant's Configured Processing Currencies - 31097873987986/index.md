---
id: 31097873987986
section_id: 28544539846802
title: "How to Find a Merchant's Configured Processing Currencies"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/31097873987986-How-to-Find-a-Merchant-s-Configured-Processing-Currencies"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-12-09T12:10:08Z"
permission_group_id: 26838654181266
content_tag_ids: []
label_names: []
user_segment_ids: [11003606966930]
archive: false
---

Use this article when you need to list all processing currencies for a merchant account or entity or processing channel, especially where there are multiple entities or several processing channels and doing it manually would be slow.INTRODUCTION 💬

A processing Currency is the currency that ends up in the recipient cardholder’s account, it is set by the recipient’s card issuer bank- not by [Checkout.com](http://checkout.com/).

- Synonyms: Recipient currency, card currency.

[Checkout.com](http://checkout.com/) supports processing to the default currency for each card issuer country, but the actual currency may differ (e.g., a UK-issued card could have USD as its processing currency).  
  
In short, processing currencies define in which currencies a processor can accept and process transactions.

### LOCATING PROCESSING CURRENCIES ON CAT 🖊️

  
1. Search for the **Client** (merchant) using:

- Client name, or

- Client ID

2. Click the **Entity** you need to check

3. Go to the **Processing channels** section and click on Gateway

 

4. Find the specific channel you need and click on it

5. Open the **Processors** tab/section

- You’ll see one or more processors (e.g. __Checkout Visa__, __Checkout MC__, __DCI__, __Amex__, etc.).

6. Click the processor you want to inspect

Within the processor configuration you will find:

- The list of **enabled processing currencies** for that processor, typically shown as a multi-select / list of ISO currency codes (e.g. `EUR`, `GBP`, `USD`, etc.)

An example is shown as per below:  
  
  
  
 

### REQUEST FOR A LIST OF PROCESSING CURRENCIES

At times, we receive requests from merchants or Account Managers (AMs) to provide a complete list of **processing currencies** for a specific account or entity.

  
When there are multiple entities and/or several processing channels per entity, this becomes challenging: you need to open each channel, check each processor, and manually compile all the currencies.   
  
Hence, for such requests, you can just use the following [Looker Link](https://checkoutinternal.eu.looker.com/explore/client_admin_tool/processing_channel_settings?toggle=fil&qid=uG4dwBQnOiQHYvjVW9VuMe) which simplifies the task.  
  
The above link filters by processing channel but you can also filter by Client ID/Entity ID for a full list, depending on your query.
