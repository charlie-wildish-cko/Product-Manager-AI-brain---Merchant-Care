---
id: 35005587950098
section_id: 34976600416658
title: "Platforms: Sub-Entity Status"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/35005587950098-Platforms-Sub-Entity-Status"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-04-22T09:57:58Z"
permission_group_id: 26838654181266
content_tag_ids: []
label_names: []
user_segment_ids: [11003606966930]
archive: false
---

This article explains every possible sub-entity status, what each one means, what the sub-entity can and cannot do at that status, how to check status, and what actions are available.**All possible sub-entity statuses**

| **Status** | **What it means** | **Can accept payments** | **Can receive payouts** | **What to do** |
| --- | --- | --- | --- | --- |
| Draft | Onboarding started but not completed.  Not all required information has been submitted yet. | No | No | The platform needs to complete and submit the application |
| Pending | All required information has been submitted and Checkout.com is running verification checks. | No (not yet) | No (not yet) | Wait for verification to complete. Track via API or webhooks |
| Requirements due | Checkout.com needs additional information before verification can proceed.  Some information may be missing, incorrect, or unverifiable. | No | No | Check the requirements_due field in the API response. Correct and resubmit the information. See Article 2 for reason codes |
| Active | The sub-entity has passed all verification checks. Payment and payout capabilities are enabled. | Yes | Yes | No action needed. The sub-entity is fully operational |
| Restricted | The sub-entity's capabilities have been restricted. They cannot process or receive funds. | No | No | Escalate - this is not self-serviceable. |
| Rejected | The sub-entity has failed verification. This is final. | No | No | To challenge the decision, [raise a support request](https://dashboard.checkout.com/support/new) |
| Inactive | The sub-entity is no longer active - due to offboarding or contract termination. | No | No | Check the status_reason field for the cause. Escalate if unexpected |

**How to check a sub-entity's status**

### **Via the Dashboard**

Log in to the Checkout.com Dashboard and navigate to the sub-entity record. The status is shown directly on the sub-entity's profile.

### **Via the API**

Status is returned in the response of three API calls:

- Onboard an entity (POST — when submitting a new application)

- Retrieve a sub-entity's details (GET)

- Update a sub-entity's details (PUT)

The status field in the API response contains the current status. If additional information is required, the requirements_due array lists the specific fields and reason codes.

[Technical docs.](https://www.checkout.com/docs/platforms/for-saas/manage-sub-entities/sub-entity-status)
**What triggers a status change?**

| **Trigger** | **Status change** |
| --- | --- |
| Platform submits onboarding application with all required information | Draft → Pending |
| Required information is missing or incomplete | Pending or Draft → Requirements due |
| All verification checks pass | Pending → Active |
| Verification fails (missing or incorrect documents) | Pending → Requirements due |
| Verification fails definitively | Pending → Rejected |
| Platform updates sub-entity information after Active status | Active → Pending (re-verification begins) |
| Re-verification after an update fails | Active → Requirements due or Restricted |
| Sub-entity is offboarded or contract ends | Active → Inactive |

**Troubleshooting / common questions**

**Q: A customer says their sub-entity went back to Pending after being Active.**

If a platform updates any required information on an Active sub-entity, Checkout.com re-runs verification automatically. The status moves to Pending. This is expected behaviour.

**Q: A customer has a Restricted sub-entity and doesn't know why.**

Restricted status is not self-serviceable. Do not speculate on the reason. Escalate to Checkout.com support immediately, providing the sub-entity ID and any relevant context.

**Q: The sub-entity shows as Inactive but the platform didn't deactivate them.**

Check the status_reason field for more detail. If the platform did not action this, escalate immediately.
