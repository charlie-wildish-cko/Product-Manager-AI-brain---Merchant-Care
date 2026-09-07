---
id: 32769695348114
section_id: 32304308299922
title: "IDV: Incorrect IDV ID (Looker Returns No Results)"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/32769695348114-IDV-Incorrect-IDV-ID-Looker-Returns-No-Results"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-02-02T16:22:50Z"
permission_group_id: 26838654181266
content_tag_ids: ["01KE6V773EPR1K1MSSMYWHJ6T4"]
label_names: ["IDV"]
user_segment_ids: [11003606966930]
archive: false
---

**Use this article when **

A merchant contacts us to support with an IDV query but they have not sent a correct ID.**INTRODUCTION TO THE ISSUE 💬**

When a merchant provides an Identity Verification (IDV) ID that cannot be located in Looker, this usually indicates:

- The merchant has submitted a typo or an ID from a different system

- The solution is to request a valid ID from the merchant

⚠️ **NOTE:** IDV IDs are not available in **Looker** for same-day checks (there is a sync delay in this being created)

When a merchant provides an ID that cannot be located in Looker, follow this logic:

| **IF...** | **THEN...** |
| --- | --- |
| **The IDV ID was created TODAY** | **Do NOT use Looker.** Looker has a T+1 sync delay. Go directly to the **Personal Data Dashboard (O Dash)** to find the ID. |
| **The ****IDV ID **** was created YESTERDAY or earlier** | **Use Looker.** Search using the `Verification ID` or `Identification Uuid` fields as usual. |
| **The ID is still missing in both** | Request a valid ID from the merchant; it is likely a typo or from a different system. |

**PROCESS STEPS 🖊️**

When a merchant contacts us with a query but the IDV shared** **returns no results in Looker:

- 
Double-check that you are searching in the correct filter field

  - If the ID begins with: idv_XXX it's a verification ID and needs to be entered into the `Verification ID` field in Looker.

  - If it doesn't start with idv_XXX it needs to be entered in the `Identification Uuid` field.

- If the field is correct and the result is still empty, the ID provided is incorrect/invalid.

| Use this macro to respond: IDV > Invalid IDV ID |
| --- |

- Customize the macro to include the ID they provided, so they can see what was incorrect.
**DECISION TREE 🔀**
