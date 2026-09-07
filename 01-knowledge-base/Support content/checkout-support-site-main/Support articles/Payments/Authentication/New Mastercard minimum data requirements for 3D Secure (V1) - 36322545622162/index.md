---
id: 36322545622162
section_id: 14321741911442
title: "New Mastercard minimum data requirements for 3D Secure (V1)"
url: "https://support.checkout.com/hc/en-us/articles/36322545622162-New-Mastercard-minimum-data-requirements-for-3D-Secure-V1"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-07-01T17:27:00Z"
permission_group_id: 11003577394706
content_tag_ids: ["01JZ88GPVA5D0SPHG3JNW36TE8"]
label_names: []
user_segment_ids: []
archive: false
---

Mastercard updated its minimum data requirements for 3D Secure earlier this year.

At this time, Mastercard has not announced any non-compliance fees or plans to decline transactions that don’t include the minimum data. We recommend providing this data to improve authentication performance across all supported schemes.

Mastercard now requires at least one field from three minimum data categories to be sent when making an authentication request.

## **For our** ****[Flow API integration](https://api-reference.checkout.com/tag/Flow)

**Cardholder identifier**

You must provide at least one of the following data elements - name, email, or all phone fields:

<figure class="wysiwyg-table" style="width: 100%;"><table style="margin-left: 0px; margin-right: auto;"><tbody>
<tr>
<td><strong>Required field</strong></td>
<td><strong>Example input</strong></td>
</tr>
<tr>
<td>customer.name<br><em>string &lt;= 254 characters </em>
</td>
<td>“John Smith”</td>
</tr>
<tr>
<td>customer.email<br><em>string [2..45 characters] </em>
</td>
<td>“john.smith@email.com” </td>
</tr>
<tr>
<td>customer.phone<br><em>object </em>
</td>
<td> </td>
</tr>
<tr>
<td>customer.phone.country_code<br><em>string [1..3] characters </em>
</td>
<td>“44”</td>
</tr>
<tr>
<td>customer.phone.number<br><em>string &lt;= 15 characters</em>
</td>
<td>“204567895” </td>
</tr>
</tbody></table></figure>

**Address / delivery**

You must provide at least one of the following data elements:

<figure class="wysiwyg-table" style="width: 100%;"><table style="margin-left: 0px; margin-right: auto;"><tbody>
<tr>
<td><strong>Required field</strong></td>
<td><strong>Example input</strong></td>
</tr>
<tr>
<td>billing.address.address.address_line1<br><em>string &lt;= 200 characters </em>
</td>
<td>“Wenlock Works”</td>
</tr>
<tr>
<td>shipping.address.address_line1<br><em>string &lt;= 200 characters </em>
</td>
<td>“Wenlock Works”</td>
</tr>
</tbody></table></figure>

**Technical information**

Checkout.com will collect this information on your behalf due to your integration.

## **For our** ****[payments API integration](https://api-reference.checkout.com/tag/Payments)

**Cardholder identifier**

You must provide at least one of the following data elements - name, email, or all phone fields:

<figure class="wysiwyg-table" style="width: 100%;"><table><tbody>
<tr>
<td><strong>Required field</strong></td>
<td><strong>Example input</strong></td>
</tr>
<tr>
<td>source.name<br><em>string &lt;= 254 characters </em>
</td>
<td>“John Smith”</td>
</tr>
<tr>
<td>source.email<br><em>string [2..45 characters] </em>
</td>
<td>“john.smith@email.com” </td>
</tr>
<tr>
<td>source.phone<br><em>object </em>
</td>
<td> </td>
</tr>
<tr>
<td>source.phone.country_code<br><em>string [1..3] characters </em>
</td>
<td>“44”</td>
</tr>
<tr>
<td>source.phone.number<br><em>string &lt;= 15 characters</em>
</td>
<td>“204567895” </td>
</tr>
</tbody></table></figure>

**Address / delivery**

You must provide at least one of the following data elements:

<figure class="wysiwyg-table" style="width: 100%;"><table style="margin-left: 0px; margin-right: auto;"><tbody>
<tr>
<td><strong>Required field</strong></td>
<td><strong>Example input</strong></td>
</tr>
<tr>
<td>source.billing_address.address_line1<br><em>string &lt;= 200 characters </em>
</td>
<td>“Wenlock Works”</td>
</tr>
<tr>
<td>shipping.address.address_line1<br><em>string &lt;= 200 characters </em>
</td>
<td>“Wenlock Works”</td>
</tr>
</tbody></table></figure>

**Technical information**

Checkout.com will collect this information on your behalf due to your integration.
