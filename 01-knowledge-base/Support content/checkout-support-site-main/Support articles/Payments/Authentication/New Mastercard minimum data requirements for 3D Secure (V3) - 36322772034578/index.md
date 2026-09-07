---
id: 36322772034578
section_id: 14321741911442
title: "New Mastercard minimum data requirements for 3D Secure (V3)"
url: "https://support.checkout.com/hc/en-us/articles/36322772034578-New-Mastercard-minimum-data-requirements-for-3D-Secure-V3"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-06-11T08:50:39Z"
permission_group_id: 11003577394706
content_tag_ids: ["01JZ88GPVA5D0SPHG3JNW36TE8"]
label_names: []
user_segment_ids: []
archive: false
---

Mastercard updated its minimum data requirements for 3D Secure earlier this year.

At this time, Mastercard has not announced any non-compliance fees or plans to decline transactions that don’t include the minimum data. We recommend providing this data to improve authentication performance across all supported schemes.

## What new data does Mastercard require?

Mastercard now requires at least one field from three minimum data categories to be sent when making an authentication request.

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
<td>source.home_phone*<br><em>object </em>
</td>
<td> </td>
</tr>
<tr>
<td>source.home_phone.country_code*<br><em>string [1..3] characters </em>
</td>
<td>“44”</td>
</tr>
<tr>
<td>source.home_phone.number*<br><em>string &lt;= 15 characters</em>
</td>
<td>“204567895” </td>
</tr>
<tr>
<td>source.mobile_phone*<br><em>object </em>
</td>
<td> </td>
</tr>
<tr>
<td>source.mobile_phone.country_code*<br><em>string [1..3] characters </em>
</td>
<td>“44”</td>
</tr>
<tr>
<td>source.mobile_phone.number*<br><em>string &lt;= 15 characters</em>
</td>
<td>“204567895” </td>
</tr>
<tr>
<td>source.work_phone*<br><em>object </em>
</td>
<td> </td>
</tr>
<tr>
<td>source.work_phone.country_code*<br><em>string [1..3] characters </em>
</td>
<td>“44”</td>
</tr>
<tr>
<td>source.work_phone.number*<br><em>string &lt;= 15 characters</em>
</td>
<td>“204567895” </td>
</tr>
</tbody></table></figure>

* You can provide one or more of the three phone fields (home phone, mobile phone, or work phone).

**Address / delivery**

You must provide at least one of the following data elements:

<figure class="wysiwyg-table" style="width: 100%;"><table class="wysiwyg-table-resized" style="margin-left: 0px; margin-right: auto;">
<colgroup>
<col style="width: 58.45%;">
<col style="width: 41.55%;">
</colgroup>
<tbody>
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
</tbody>
</table></figure>

**Technical information**

<figure class="wysiwyg-table" style="width: 100%;"><table class="wysiwyg-table-resized">
<colgroup>
<col style="width: 58.6%;">
<col style="width: 41.4%;">
</colgroup>
<tbody>
<tr>
<td><strong>Required field</strong></td>
<td><strong>Example input</strong></td>
</tr>
<tr>
<td>risk.device.network.ipv4* or risk.device.network.ipv6*<br><em>string</em>
</td>
<td>“1.12.123.255”</td>
</tr>
</tbody>
</table></figure>

* Only for Mobile SDK App flow transactions using Common Device Identification. If you use our Mobile SDK solution, we’ll collect and submit the device_ip_address on your behalf.
