---
id: 35010773917842
section_id: 24470497362962
title: "Update to your invoice file names"
url: "https://support.checkout.com/hc/en-us/articles/35010773917842-Update-to-your-invoice-file-names"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-06-03T10:49:51Z"
permission_group_id: 11003577394706
content_tag_ids: ["01K22NYQP6QBETF4NRGEXJXKBA", "01K22P1B0HTTRPKRMJJNZJ3NXA"]
label_names: ["Funds and fees - Billing & fees - Invoice request"]
user_segment_ids: []
archive: false
---

From July 1, 2026, we’re updating the file name format of your Checkout.com invoices to include your invoice number. This change is part of ongoing improvements to how we manage invoices internally.

If your automated systems ingest invoices using the file name, you’ll need to update them to process this new file name format before July 1, 2026.

## **What’s changing?**

We’re replacing the currency field in the invoice file name with the invoice number:

- **Current format:** invoice_{Entity-Id}**{Currency}**{Start Date:YYYYMMDD}_{End Date:YYYYMMDD}.pdf
- **New format:** invoice_{Entity-Id}**{Invoice Number}**{Start Date:YYYYMMDD}_{End Date:YYYYMMDD}.pdf

### **Example**

- **Before:** invoice_ent_vympslwa8fhcq2pg4rn9it5k_usd_20260601_20260630.pdf
- **After:** invoice_ent_vympslwa8fhcq2pg4rn9it5k_827143123USD003_20260601_20260630.pdf
