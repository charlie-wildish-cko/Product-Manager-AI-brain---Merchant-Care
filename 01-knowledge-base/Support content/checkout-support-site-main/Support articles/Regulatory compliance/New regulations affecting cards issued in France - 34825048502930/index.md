---
id: 34825048502930
section_id: 16339888329362
title: "New regulations affecting cards issued in France"
url: "https://support.checkout.com/hc/en-us/articles/34825048502930-New-regulations-affecting-cards-issued-in-France"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-06-12T13:20:29Z"
permission_group_id: 11003577394706
content_tag_ids: ["01KP89MRRWB6YW3TMZ0SWQ1MZF", "01KP89N6ZH3KXJCKVA0TQS3JDW", "01KP89NG39EP46MNB7ZHCNWST3"]
label_names: ["Accepting payments - Authentication (3DS) - SCA / exemption issue"]
user_segment_ids: []
archive: false
---

Banque de France – the French payments regulator, recently made new recommendations for French issuers.

These recommendations mean you may need to [authenticate](https://www.checkout.com/docs/payments/authenticate-payments) online transactions above a certain amount for French cardholders, even if you’re based outside the SCA regions of the EEA, United Kingdom, and Switzerland.

## **Overview**

Currently, Banque de France only recommends that issuers require authentication for a transaction made with a PSP outside of the SCA regions if the transaction amount is above 2,000 EUR.

Starting from April 13, 2026, Banque de France recommends that French issuers decrease their thresholds as follows:

<figure class="wysiwyg-table wysiwyg-table-align-left"><table><tbody>
<tr>
<td><strong>Merchant acquiring location</strong></td>
<td><strong>Threshold from April 13, 2026</strong></td>
<td><strong>Threshold from May 11, 2026</strong></td>
<td><strong>Threshold from June 10, 2026</strong></td>
<td><strong>Threshold from July 13, 2026</strong></td>
<td><strong>Threshold from September 13, 2026</strong></td>
</tr>
<tr>
<td><strong>Asia Pacific region</strong></td>
<td>2,000 EUR</td>
<td>2,000 EUR</td>
<td>1,000 EUR</td>
<td>1,000 EUR</td>
<td>500 EUR</td>
</tr>
<tr>
<td><strong>MENA region</strong></td>
<td>1,000 EUR</td>
<td>500 EUR</td>
<td>250 EUR</td>
<td>100 EUR</td>
<td>100 EUR</td>
</tr>
<tr>
<td><strong>North America region</strong></td>
<td>2,000 EUR</td>
<td>2,000 EUR</td>
<td>1,000 EUR</td>
<td>1,000 EUR</td>
<td>500 EUR</td>
</tr>
</tbody></table></figure>

## **How this affects you**

If you process amounts above these thresholds, we recommend [applying 3D Secure (3DS) authentication](https://www.checkout.com/docs/business-operations/ensure-regulatory-compliance/sca-compliance) to your French cardholders' transactions. If a French issuer declines a transaction due to a lack of authentication, we expect that you'll receive a **20154 - 3DS authentication required** response.

Alternatively, card-based digital wallets like [Apple Pay](https://www.checkout.com/docs/payments/payment-methods/apple-pay) and [Google Pay](https://www.checkout.com/docs/payments/payment-methods/google-pay) have multi-factor authentication built in to their payment flows, offering a frictionless checkout experience.

## **Frequently asked questions**

### **Why is Banque de France making these changes?**

The regulator is aiming to reduce fraud on cross-border transactions. By introducing these thresholds, they are bringing French cardholder protection for cross-border payments closer to the standards used in the European Economic Area and United Kingdom.

### **Why are the limits for the MENA region lower than the Asia Pacific and North America regions?**

The Banque de France has assigned different risk profiles to different regions. The MENA region has a more aggressive reduction schedule, reaching a 100 EUR threshold by July 2026.

### **Do the thresholds apply to the total transaction amount or the individual items?**

The thresholds apply to the total transaction amount you submit for authorization.

### **Can a transaction that gets declined for lack of authentication be retried?**

Yes, if you receive a 20154 response you can redirect the customer to a 3DS authentication flow and resubmit the payment.

### **Will this increase friction for my French customers?**

It adds a step to the checkout, but 3DS2 (EMV 3DS) is designed to be much smoother than old versions, and is familiar to European customers.

### **Does this affect recurring payments or subscriptions?**

Merchant Initiated Transactions (MITs) follow different rules once the first transaction is authenticated. The initial Customer Initiated Transaction (CIT) used to set up the MIT series must follow the new thresholds.

### **Are these rules final or just recommendations?**

While the Banque de France calls them "recommendations," French issuers (banks) almost always treat these as mandatory.
