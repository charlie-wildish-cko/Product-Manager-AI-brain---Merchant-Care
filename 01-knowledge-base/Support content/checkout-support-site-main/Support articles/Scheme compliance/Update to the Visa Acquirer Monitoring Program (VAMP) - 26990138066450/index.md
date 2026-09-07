---
id: 26990138066450
section_id: 36678206237714
title: "Update to the Visa Acquirer Monitoring Program (VAMP)"
url: "https://support.checkout.com/hc/en-us/articles/26990138066450-Update-to-the-Visa-Acquirer-Monitoring-Program-VAMP"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-07-03T08:44:15Z"
permission_group_id: 11003577394706
content_tag_ids: []
label_names: ["Accepting payments - Transaction status (non 3DS & refunds) - Stuck in status / status enquiry"]
user_segment_ids: []
archive: false
---

Visa retired its previous monitoring programs for disputes and fraud on April 1, 2025, and launched a new, combined dispute and fraud program – the Visa Acquirer Monitoring Program (VAMP) – to replace these programs.

As payment service providers and their merchants continue to feed back on the program, Visa has made several updates to VAMP in 2026. Most recently, they made a significant update to how they will calculate the program ratios, with corresponding increases to the thresholds at which these ratios will result in scheme fees.

Visa has also reduced the fee levels to account for these changes.

## Overview

### Acquirer and merchant ratios for disputes and fraud

Under the VAMP, merchants and acquirers must keep fraud and disputes below a ratio of their settled transactions. Visa updated this ratio to include **fraud and non-fraud disputes** in addition to the number of transactions reported as fraud.

Previously, Visa only included **non-fraud disputes** in this ratio:

**(Monthly # of transactions reported as fraud + # of fraud disputes + non-fraud disputes)**

**--------------------------------------------**

**(Monthly # of settled transactions)**

If an acquirer or merchant’s ratio breaches certain thresholds, Visa will place them under the VAMP, and fines will apply from **October 1, 2025**, with acquirers being notified of non-compliance from June 1, 2025, onwards.

As the inclusion of fraud disputes may increase merchants’ ratios, Visa has also increased the VAMP thresholds as part of their latest update, and extended the date when lowered thresholds will take effect to **April 1, 2026** (previously January 1, 2026):

<figure class="wysiwyg-table wysiwyg-table-align-left"><table><tbody>
<tr>
<td><strong>Effective date</strong></td>
<td><strong>Acquirer above standard ratio</strong></td>
<td><strong>Acquirer excessive ratio</strong></td>
<td><strong>Merchant excessive ratio</strong></td>
</tr>
<tr>
<td>June 1, 2025</td>
<td>N/A</td>
<td>&gt;=0.70%</td>
<td>&gt;=2.20%</td>
</tr>
<tr>
<td>January 1, 2026</td>
<td>&gt;=0.50% to &lt;0.70%</td>
<td>&gt;=0.70%</td>
<td>&gt;=2.20%</td>
</tr>
<tr>
<td>April 1, 2026  (Global, excluding MENA)</td>
<td>&gt;=0.50% to &lt;0.70%</td>
<td>&gt;=0.70%</td>
<td>&gt;=1.50%</td>
</tr>
</tbody></table></figure>

For merchants, these thresholds only apply where the total number of transactions reported as fraud plus disputes is:

- **Outside of MENA:** Greater than 1,500 (updated from 1,000 previously)
- **In MENA:** Greater than 100 and over 75,000 USD in value (unchanged)

All disputes (fraud **and** non-fraud disputes) resolved through [Rapid Dispute Resolution](https://www.checkout.com/docs/payments/process-disputes/pre-dispute-resolution) will continue to be excluded from the VAMP ratio. However, Visa will include TC40 fraud reports as these are reported fraud and not disputes. 

TC40 fraud qualified for [Compelling Evidence 3.0](https://support.checkout.com/hc/en-us/articles/14323750143634-Visa-Compelling-Evidence-3-0-Overview) will also continue to be excluded from the VAMP ratio.

### Merchant ratios for enumerated transactions

Visa’s excessive enumeration ratio is unchanged. This will apply to [enumeration attacks](https://www.linkedin.com/pulse/what-enumeration-attack-visa-cac2c/) identified by Visa’s Account Attack Intelligence system.

If you have more than 300,000 Visa-identified enumeration attacks in a month that are more than or equal to 20% of your transaction volume, you’ll fall under the excessive enumeration program.

## Enforcement fees under the VAMP

For first-time identifications within a rolling 12-month period and during the advisory period ending October 1, 2025, Visa will apply a grace period before assessing fees.

After October 1, if you or your acquirer breaches a VAMP threshold more than once in 12 months, Visa will place you in the program and assess fees for subsequent fraud reports or disputes.

Note that Visa has decreased the VAMP fees following its recent update:

<figure class="wysiwyg-table wysiwyg-table-align-left"><table><tbody>
<tr>
<td><strong>Effective date</strong></td>
<td><strong>Acquirer breaches above standard ratio</strong></td>
<td><strong>Merchant breaches excessive ratio</strong></td>
<td><strong>Acquirer breaches excessive ratio and merchant ratio is &gt;=0.5%</strong></td>
<td><strong>Merchant breaches excessive enumeration ratio</strong></td>
</tr>
<tr>
<td>April 1, 2025</td>
<td>Not applicable</td>
<td>8 USD per dispute or transaction reported as fraud</td>
<td>8 USD per dispute or transaction reported as fraud</td>
<td>8 USD per dispute or transaction reported as fraud</td>
</tr>
<tr>
<td>January 1, 2026</td>
<td>4 USD per dispute or transaction reported as fraud</td>
<td>8 USD per dispute or transaction reported as fraud</td>
<td>8 USD per dispute or transaction reported as fraud</td>
<td>8 USD per dispute or transaction reported as fraud</td>
</tr>
</tbody></table></figure>

**Note:** In the AP and Europe regions, VAMP fees will not apply where a chargeback also incurs an unsecured dispute fee. Visa applies unsecured dispute fees to fraud chargebacks where the merchant did not authenticate the disputed transaction.
