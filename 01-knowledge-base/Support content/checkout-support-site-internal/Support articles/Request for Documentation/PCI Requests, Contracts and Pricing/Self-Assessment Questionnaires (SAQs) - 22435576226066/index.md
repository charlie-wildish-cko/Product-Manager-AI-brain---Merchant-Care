---
id: 22435576226066
section_id: 22435357361426
title: "Self-Assessment Questionnaires (SAQs)"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22435576226066-Self-Assessment-Questionnaires-SAQs"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:36:40Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JBHFK1FTRFHHXXN4PTQS8A0A"]
label_names: ["global", "case_request_for_documentation", "case_rfd_issue_pci_dss_docs", "self_assessment_questionnaires_saqs"]
user_segment_ids: [11003606966930]
archive: false
---

## Process Steps

Types of Self-Assessment Questionnaires (SAQs)

The Self-Assessment Questionnaire (SAQ) is a key component of PCI DSS (Payment Card Industry Data Security Standard) compliance. It is used by businesses to assess their adherence to PCI DSS requirements based on their specific cardholder data handling scenarios. The type of SAQ a business needs to complete depends on how it processes, stores, or transmits payment card information.

Each SAQ is tailored to different cardholder data environments and processing methods. Merchants must select the appropriate SAQ based on their specific card-handling practices to assess their PCI DSS compliance accurately. 

_As of **Mar 31, 2024**, the PCI Security Standard Councils updated their security requirements. As a result of this change, merchants filling out an SAQ will need to use the new PCI v4.0 standard._ _The previous one was v3.2.1._

Here’s a recap:

| **Types** | **Recipients** | **Eligibility** | **Conditions** | **Examples** | **Template** |
| --- | --- | --- | --- | --- | --- |
| **SAQ A** | Fully outsourced card processing, no cardholder data storage or transmission | For eCommerce merchants who fully outsource all cardholder data functions to a PCI DSS-compliant third-party service provider. | The merchant’s website does not store, process, or transmit cardholder data. The payment process is handled completely by a third-party service provider. | Using a fully hosted payment page or an iframe from a third-party payment gateway where the merchant does not touch the cardholder data. | [Here](https://docs-prv.pcisecuritystandards.org/SAQ%20(Assessment)/SAQ/PCI-DSS-v4-0-SAQ-A-r2.pdf) |
| **SAQ B** | Standalone terminals or imprint machines, no electronic cardholder data storage. | For merchants who process cardholder data only through standalone, dial-out terminals or through imprint machines, and do not store cardholder data electronically. | Cardholder data is captured via physical card reading devices and not stored electronically. It’s typically used by merchants who handle card swipes or imprints in person. | A retail store using standalone point-of-sale (POS) terminals that do not store cardholder data. | [Here](https://docs-prv.pcisecuritystandards.org/SAQ%20(Assessment)/SAQ/PCI-DSS-v4-0-SAQ-B-r1.pdf) |
| **SAQ C** | Internet-connected payment application, no electronic cardholder data storage. | For merchants who process cardholder data through a payment application connected to the internet but do not store cardholder data electronically. | Cardholder data is processed through a web-based payment application that is connected to the internet, but data is not stored. This applies to merchants with more complex cardholder data. | An eCommerce site with a payment application that processes transactions directly but does not store any cardholder data. | [Here](https://docs-prv.pcisecuritystandards.org/SAQ%20(Assessment)/SAQ/PCI-DSS-v4-0-SAQ-C-r1.pdf) |
| **SAQ C-VT** | Virtual terminals only, no electronic cardholder data storage. | For merchants who process cardholder data using only virtual terminals (manually entered transactions) and do not store cardholder data electronically. | Cardholder data is entered manually into a virtual terminal (a web-based application), and the merchant does not store cardholder data electronically. | A business uses a web-based virtual terminal to process payments manually entered by employees. | [Here](https://docs-prv.pcisecuritystandards.org/SAQ%20(Assessment)/SAQ/PCI-DSS-v4-0-SAQ-C-VT-r1.pdf) |
| **SAQ D** | More complex cardholder data environments, including those that store, process, or transmit cardholder data. | For all other merchants that do not meet the criteria for SAQ A, B, C, or C-VT. This includes merchants who store, process, or transmit cardholder data electronically and are therefore subject to the full set of PCI DSS requirements. | Applicable to any merchant with more complex or extensive cardholder data environments. This includes businesses that store cardholder data, use integrated payment systems, or handle sensitive payment data in multiple ways. | Merchants with custom payment processing systems, businesses that store cardholder data for recurring billing, or merchants that handle cardholder data in various ways. | [Here](https://docs-prv.pcisecuritystandards.org/SAQ%20(Assessment)/SAQ/PCI-DSS-v4-0-SAQ-D-Merchant-r1.pdf) |
| **SAQ P2PE-HW** | Hardware payment terminals within a PCI-approved Point-to-Point Encryption solution, no cardholder data storage. | For merchants who use only hardware payment terminals that are part of a PCI-approved Point-to-Point Encryption (P2PE) solution and do not store cardholder data. | The merchant uses PCI-approved hardware terminals that encrypt cardholder data at the point of entry and does not store cardholder data. | A business using approved P2PE hardware terminals to securely capture cardholder data. | [Here](https://docs-prv.pcisecuritystandards.org/SAQ%20(Assessment)/SAQ/PCI-DSS-v4-0-SAQ-P2PE-r1.pdf) |

  
Which SAQ should a merchant provide?

Checkout.com may be more vulnerable to credit card theft if incomplete submissions invalidate a merchant's compliance. In light of this, Checkout.com needs to make sure that retailers are giving the appropriate SAQ in line with its features or integration philosophy. A few examples of the kinds of integrations that merchants may use and the associated SAQs that they need to supply are given below:

| **Integration** | **SAQs required** |
| --- | --- |
| Frames, Hosted Payments Page, Payment Links, Mobile Kits | SAQ A |
| MOTO | SAQ C-VT |
| Full API | SAQ D + ASV Scan |
| Full API using an e-commerce platform integration (eg: Shopify, Magento, WooCommerce) | SAQ A [from merchant] + AoC [Of service provider completed by a QSA or ISA] [Please refer to confluence](https://checkout.atlassian.net/wiki/spaces/CHEC/pages/5119089802/PCI+Compliance+-+documents+to+request+from+merchants#Is-the-merchant-asking-for-Full-API-to-be-enabled%3F) |

| **Resource** | **Link** |
| --- | --- |
| Confluence | [https://checkout.atlassian.net/wiki/spaces/CHEC/pages/5119089765/PCI+DSS+-+Requirements+for+merchants#II.-Which-SAQ-should-a-merchant-provide%3F](https://checkout.atlassian.net/wiki/spaces/CHEC/pages/5119089765/PCI+DSS+-+Requirements+for+merchants#II.-Which-SAQ-should-a-merchant-provide%3F) |

## Glossaries and Definitions:

For **Key Terms and Definitions** on PCI DSS Issues, please see ****[PCI DSS Glossary & Introduction.](https://checkoutint.zendesk.com/hc/en-us/articles/22435569863826-PCI-DSS-Glossary-Introduction) 

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the PCI DSS articles, please see ****[PCI DSS Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22435576095250-PCI-DSS-Tools-Permissions)
