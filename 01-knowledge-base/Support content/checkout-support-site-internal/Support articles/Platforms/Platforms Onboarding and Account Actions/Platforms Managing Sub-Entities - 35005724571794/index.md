---
id: 35005724571794
section_id: 34976600416658
title: "Platforms: Managing Sub-Entities"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/35005724571794-Platforms-Managing-Sub-Entities"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-04-22T10:01:58Z"
permission_group_id: 26838654181266
content_tag_ids: []
label_names: []
user_segment_ids: [11003606966930]
archive: false
---

This article explains how to retrieve sub-entity information, how to update a sub-entity's details, and the most common reasons a record may need updating.**How to retrieve sub-entity details**

The platform can look up a sub-entity's details at any time using the API. They need the sub-entity's ID (a unique identifier assigned at creation, beginning with 'ent_').

They call the Retrieve Sub-Entity Details endpoint (GET). The response includes:

- The sub-entity's current status

- Their contact and business details

- Their payment instrument (bank account or card)

- Their capabilities (payments enabled, payouts enabled)

- Any outstanding requirements (if status is requirements_due)

[Technical docs.](https://www.checkout.com/docs/platforms/for-saas/manage-sub-entities/retrieve-sub-entity-details)**How to update a sub-entity's information**

The platform can update a sub-entity's record using the Update Sub-Entity endpoint (PUT). They provide the sub-entity ID and the fields they want to change.

**⚠️ Important: Any update to required fields on an Active sub-entity will trigger re-verification. The sub-entity's status moves to Pending and their capabilities may be temporarily disabled until checks complete.**

[Technical docs.](https://www.checkout.com/docs/platforms/for-saas/manage-sub-entities/update-a-sub-entity)**Common reasons a sub-entity record may need updating**

The most common scenarios where a platform needs to update sub-entity details:

| **Scenario** | **What to update** |
| --- | --- |
| A document has expired (for example, a representative's passport) | The identity document field for the affected representative |
| The sub-entity's business address has changed | The registered address or principal address field |
| A company representative has changed (new director, etc.) | The representatives array with new individual details |
| A company document was rejected as unreadable or mismatched | Upload a new, clearer document or correct the matching field |
| Bank account details have changed | The payment instrument (bank account) linked to the sub-entity |
| Missing beneficial owner information | Add details for all Ultimate Beneficial Owners (UBOs) |

**Troubleshooting / common questions**

**Q: The platform updated a sub-entity but they're still showing Requirements due.**

Make sure all flagged fields have been corrected and resubmitted. Check the requirements_due list in the API response — there may be more than one issue. Re-verification only runs if the submitted data is complete.

**Q: Can a Rejected sub-entity be updated?**

No. Attempting to update a Rejected sub-entity via the API returns a 442 error. To challenge the rejection, raise a support ticket.
