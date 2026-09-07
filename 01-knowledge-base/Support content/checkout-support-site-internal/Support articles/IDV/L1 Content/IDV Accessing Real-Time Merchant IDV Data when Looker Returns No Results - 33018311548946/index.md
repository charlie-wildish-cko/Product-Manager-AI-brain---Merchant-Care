---
id: 33018311548946
section_id: 32304308299922
title: "IDV: Accessing Real-Time Merchant IDV Data when Looker Returns No Results"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/33018311548946-IDV-Accessing-Real-Time-Merchant-IDV-Data-when-Looker-Returns-No-Results"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-02-02T16:23:14Z"
permission_group_id: 26838654181266
content_tag_ids: ["01KE6V773EPR1K1MSSMYWHJ6T4"]
label_names: ["IDV"]
user_segment_ids: [11003606966930]
archive: false
---

**Use this article when**

You're handling an IDV case where the IDV ID number looks correct, but Looker isn't showing any results.**Issue  ⚠️**
  
Merchants may contact us about an Identity Verification (IDV) case on the same day the ID was processed. Agents checking Looker for the associated ID or UUID may not find it, leading to confusion and delayed resolution.  
  
There is a synchronization delay (approximately one day) for IDV data to be fully reflected from the primary data system (Personal Data Dashboard/O Dash) into the Looker data platform.

When a merchant provides an ID that cannot be located in Looker, follow this logic:

| **IF...** | **THEN...** |
| --- | --- |
| **The IDV ID  was created TODAY** | **Do NOT use Looker.** Looker has a T+1 sync delay. Go directly to the **Personal Data Dashboard (O Dash)** to find the ID. |
| **The ****IDV ID **** was created YESTERDAY or earlier** | **Use Looker.** Search using the `Verification ID` or `Identification Uuid` fields as usual. |
| **The ID is still missing in both** | Request a valid ID from the merchant; it is likely a typo or from a different system. [See Incorrect IDV ID](https://checkoutint.zendesk.com/hc/en-us/articles/32769695348114-IDV-Incorrect-IDV-ID-Looker-Returns-No-Results) |

 

**Resolution ✅**  
  
To find a merchant’s IDV details when the merchant has contacted us on the same day, agents **must not** rely solely on Looker.  
 

- 
**Action:** Retrieve the ID or UUID from the email and check this from the ****[Personal Data Dashboard](https://odash.ubble.ai/verifications) (also referred to as the **O Dash**).

- 
**Reasoning:** The Personal Data Dashboard reflects the most up-to-date information, while Looker will only display the data on the following day.
