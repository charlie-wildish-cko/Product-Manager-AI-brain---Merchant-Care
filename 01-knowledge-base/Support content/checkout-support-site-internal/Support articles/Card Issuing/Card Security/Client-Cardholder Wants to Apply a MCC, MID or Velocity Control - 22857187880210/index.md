---
id: 22857187880210
section_id: 28482798009874
title: "Client/Cardholder Wants to Apply a MCC, MID or Velocity Control"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22857187880210-Client-Cardholder-Wants-to-Apply-a-MCC-MID-or-Velocity-Control"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:34:42Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JNGXCVNHFQB2TX90T7Z1YKMZ"]
label_names: ["global", "issuing", "case_card_issuing", "case_card_issuing_cardholder_wants_to_apply_mcc_mid_velocity_control"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

Clients or cardholders can apply Merchant Category Code (MCC), Merchant ID (MID), or Velocity Controls (e.g. whitelist an MCC) to manage spending and enhance fraud prevention. Below are the steps to set up these controls via the Dashboard or API, along with troubleshooting steps for issues they may face with each.

As Merchant Care cannot solve this request directly, the correct actions are to guide the client or cardholder to self-serve as per the below steps (or visit the [Controls](https://www.checkout.com/docs/card-issuing/manage-controls/card-controls) support page). Alternatively, if the below steps are unsuccessful, direct the client to their Account Manager, or send an email on behalf of the client to the [Issuing Operations](issuing_operations@checkout.com) team who will be able to assist the merchant

## Process Steps

### Applying a Control via Dashboard

1. Log in to the Dashboard

2. Go to Issuing > Cards, and select the card

3. Navigate to the Controls tab and open the Controls section for the card

4. Click "Add control" and choose the relevant control type:

  1. MCC Control: Select "Allow" or "Block" based on your preference

  2. MID Control: Select "Allow" or "Block" based on your preference

  3. Velocity Control: Enter the maximum transaction amount, choose the applicable period (Daily, Weekly, Monthly), and specify the transaction scope (e.g., all spending or specific categories)

5. Click Confirm to apply the control

### Apply a Control via API

MCC Control API Endpoint: POST [https://api.checkout.com/issuing/controls](https://api.checkout.com/issuing/controls)

Example request:

```{
  "control_type": "mcc_limit",
  "target_id": "crd_123456789abcdef",
  "mcc_limit": {
    "type": "block",
    "mcc_list": ["5411", "5812"]  // MCC codes for grocery stores and restaurants
  }
}
```

 

MID Control API Endpoint: POST [https://api.checkout.com/issuing/controls](https://api.checkout.com/issuing/controls)

Example request:

```{
  "control_type": "mid_limit",
  "target_id": "crd_123456789abcdef",
  "mid_limit": {
    "type": "allow",
    "mid_list": ["mid_123456", "mid_987654"]  // Allowed Merchant IDs
  }
}
```

 

Velocity Control API Endpoint: POST https://api.checkout.com/issuing/controls

Example request:

```{
  "control_type": "velocity_limit",
  "target_id": "crd_123456789abcdef",
  "velocity_limit": {
    "amount_limit": 1000,  // Maximum spend in minor units (e.g., cents)
    "velocity_window": {
      "type": "weekly"
    }
  }
}
```

 

Apply the Control Using cURL:

```curl -X POST https://api.checkout.com/issuing/controls \
-H "Authorization: Bearer sk_test_1234567890abcdef" \
-H "Content-Type: application/json" \
-d '{ "control_type": "velocity_limit", "target_id": "crd_123456789abcdef", "velocity_limit": { "amount_limit": 1000, "velocity_window": { "type": "weekly" } } }'
```

 

## Troubleshooting MCC, MID, and Velocity Controls

### Dashboard Troubleshooting

| Issue | Troubleshooting Steps |
| --- | --- |
| Cannot find "Add Control" option | Ensure you have the correct user permissions to modify controls |
| MCC or MID list not applying | Verify that the MCC or MID values entered are correct and supported |
| Control changes are not saving | Refresh the page and try again. If the issue persists, clear browser cache or use an incognito window |
| Existing control prevents changes | Check for conflicting controls (e.g., a block control that overrides an allow control) |
| Transactions not following control rules | Wait for the control to take effect, which can take a few minutes. If still not working, verify if the transaction details match the applied control |
| Unexpected transactions getting blocked | Ensure that the control is set to "Allow" rather than "Block" for permitted merchants or spending categories |

### API Troubleshooting

| Error Code | Error Message | Cause | Resolution |
| --- | --- | --- | --- |
| **401** | Unauthorized | Invalid API key or missing authentication. | Ensure API key is correct and has permissions. |
| **404** | Target Not Found | Invalid card_id or missing data in request. | Verify that the card ID exists using the Retrieve Card API. |
| **400** | Invalid Request | Incorrect JSON format or missing required fields. | Check API documentation and correct request payload. |
| **409** | Conflict | Conflicting control already exists. | Remove the conflicting control before applying a new one. |
| **500** | Internal Server Error | Temporary issue on Checkout.com’s end. | Retry the request after a few minutes or contact support. |

 

If the client/cardholder is still experiencing issues with MCC, MID, or Velocity Controls, they should:

1. Verify the API request or Dashboard configuration

2. Check if the card program supports the requested control types

3. Contact Checkout.com support with:

  - Card ID (target_id)

  - The attempted control settings

  - API request and response (if applicable)

  - Any error messages received

Additional Considerations

- If multiple controls apply to a card, the strictest control always overrides any others

- Checkout.com may apply certain [immutable controls](https://www.checkout.com/docs/card-issuing/manage-controls/card-controls#Immutable_controls) to a card for fraud protection. The client cannot update or delete these but can apply stricter controls within their limits

## Glossaries and Definitions

For **Key Terms and Definitions** on Card Issuing Issues, please see ****[Card Issuing Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22857173195794-Issuing-Glossary-Introduction) 

 

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Card Issuing articles, please see ****[Card Issuing Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22857178933394-Issuing-Tools-Permissions)
