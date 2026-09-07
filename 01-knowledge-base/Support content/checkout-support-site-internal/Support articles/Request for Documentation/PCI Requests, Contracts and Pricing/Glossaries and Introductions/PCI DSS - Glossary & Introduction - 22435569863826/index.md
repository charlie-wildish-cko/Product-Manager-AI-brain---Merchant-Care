---
id: 22435569863826
section_id: 22435322952978
title: "PCI DSS - Glossary & Introduction"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/22435569863826-PCI-DSS-Glossary-Introduction"
locale: "en-us"
draft: false
promoted: false
updated_at: "2025-10-22T08:36:40Z"
permission_group_id: 26838654181266
content_tag_ids: ["01JBHFK1FTRFHHXXN4PTQS8A0A"]
label_names: ["global", "glossaries_and_introductions", "case_request_for_documentation", "case_rfd_issue_pci_dss_docs", "pci_dss_glossary_and_introduction"]
user_segment_ids: [11003606966930]
archive: false
---

## Key Terms & Definitions

| **Term** | **Definition** |
| --- | --- |
| **PCI DSS** | Payment Card Industry Data Security Standard |
| **PCI SSC** | Payment Card Industry Security Standards Council |
| **CKO** | Checkout Ltd |
| **AOC** | Attestation of Compliance |
| **PAN** | Primary Account Number |
| **SAD** | Sensitive Authentication Data |

## **Introduction**

### **Purpose **

This SOP will serve the Merchant Care team as a tool to ensure consistency, quality and efficiency in responding to merchant’s queries without the need to escalate. This would facilitate knowledge retention and promote continuous improvement. This SOP serves to standardise operations, improve efficiency, ensure accountability, support compliance, retain knowledge, and foster continuous improvement within a team. It acts as a foundational document that guides the team’s day-to-day activities and long-term growth. 

_**Refer to section the **__****_[Merchant Care PCI DSS FAQ article](https://checkoutint.zendesk.com/hc/en-us/articles/22435536881042-Merchant-Care-PCI-DSS-FAQs)_** for frequently asked questions by Merchants **_

## **Context**

PCI DSS compliance refers to adhering to the _Payment Card Industry Data Security Standard_, a set of security standards designed to ensure that all companies that accept, process, store, or transmit credit card information maintain a secure environment. 

PCI DSS was established by the Payment Card Industry Security Standards Council (PCI SSC), founded by major credit card companies including Visa, MasterCard, American Express, Discover, and JCB.

As a payment service provider, Checkout.com is PCI compliant and adheres to these standards to protect cardholder data throughout the payment process.

| **Resource** | **Link** |
| --- | --- |
| **Certificate** | [https://checkout.atlassian.net/wiki/spaces/SEC/pages/5339906049/PCI+Payment+Card+Industry](https://checkout.atlassian.net/wiki/spaces/SEC/pages/5339906049/PCI+Payment+Card+Industry) |
| **High Spot Doc** | [https://checkout.highspot.com/items/63498c53ef3dffd5b67ee0cc](https://checkout.highspot.com/items/63498c53ef3dffd5b67ee0cc) |
| **Confluence** | [https://checkout.atlassian.net/wiki/x/ZRwfMQE](https://checkout.atlassian.net/wiki/x/ZRwfMQE) |

 

### **Who is Security Metrics?**

Checkout Ltd places significant emphasis on ensuring the security of its payment systems, particularly given the sensitive nature of the financial data it handles. It is common for payment processors like Checkout Ltd to engage with third-party security firms such as Security Metrics Ltd to validate their compliance with standards like PCI-DSS (Payment Card Industry Data Security Standard)​.

Security Metrics Ltd and Checkout Ltd are connected through third-party security management practices. Both companies are involved in ensuring secure business transactions, given the heightened focus on cybersecurity across various industries. 

Security Metrics is a company that specialises in providing security solutions, particularly focused on compliance, risk management, and data security for businesses. Their services often include compliance with the payment card industry (PCI), vulnerability scanning, penetration testing, and other cybersecurity measures to help organisations protect their sensitive data and meet regulatory requirements. More information can be found [here](https://checkout.atlassian.net/wiki/spaces/CHEC/pages/5232885761/PCI+DSS+compliance+validation+with+SecurityMetrics).

 

### **Aspects of PCI Compliance**

**Here are the key aspects of PCI compliance:****Data Security**

PCI DSS outlines specific technical and operational requirements to protect cardholder data, including measures for secure storage and transmission of this data.**Risk Management**

It involves continuous risk assessment, vulnerability management, and implementing appropriate measures to mitigate identified risks.**Access Control**

Strict access control measures ensure that only authorised personnel can access cardholder data. This includes maintaining a secure network, protecting against unauthorised access, and ensuring secure access to systems.**Monitoring and Testing**

Regular monitoring and testing of networks and systems are required to ensure security controls are working effectively. This includes logging and tracking access to network resources and cardholder data.**Policy Implementation**

Organisations must establish, maintain, and enforce information security policies, including policies for protecting cardholder data.

### **Control Objectives**

****

| **Protect Cardholder Data** | - Install and maintain a firewall configuration to protect cardholder data.  - Do not use vendor-supplied defaults for system passwords and other security parameters. |
| --- | --- |
| **Build and Maintain a Secure Network and Systems** | - Install and maintain a firewall configuration to protect cardholder data.  - Do not use vendor-supplied defaults for system passwords and other security parameters. |
| **Protect Cardholder Data** | - Protect stored cardholder data.  - Encrypt transmission of cardholder data across open, public networks. |
| **Maintain a Vulnerability Management Program** | - Protect all systems against malware and regularly update anti-virus software or programs.  - Develop and maintain secure systems and applications |
| **Implement Strong Access Control Measures** | - Restrict access to cardholder data by business need to know.  - Identify and authenticate access to system components.  - Restrict physical access to cardholder data. |
| **Regularly Monitor and Test Networks** | - Track and monitor all access to network resources and cardholder data.  - Regularly test security systems and processes |
| **Maintain an Information Security Policy** | - Maintain a policy that addresses information security for employees and contractors. |

### **Compliance Levels**

Merchants are organized under 4 levels of PCI compliance, based on their card transaction count over 12 months. Merchants’ PCI level and integration method will determine the compliance requirements they must meet.

The level of PCI compliance required depends on the volume of credit card transactions an organization processes annually:

- Level 1: Merchants processing over 6 million card transactions per year.

- Level 2: Merchants processing 1 to 6 million transactions per year.

- Level 3: Merchants processing 20,000 to 1 million transactions annually.

- Level 4: Merchants processing fewer than 20,000 transactions annually.

Organizations must undergo regular assessments to validate their compliance, which can include self-assessment questionnaires (SAQs), vulnerability scans by an Approved Scanning Vendor (ASV), and audits by a Qualified Security Assessor (QSA).

| **Name** | **Description** |
| --- | --- |
| **Checkout Documentation: PCI compliance levels** | [https://www.checkout.com/docs/payments/ensure-regulatory-compliance/pci-compliance#PCI_compliance_levels](https://www.checkout.com/docs/payments/ensure-regulatory-compliance/pci-compliance#PCI_compliance_levels) |
| **PCI Blog** | [https://www.checkout.com/blog/what-is-pci-compliance](https://www.checkout.com/blog/what-is-pci-compliance) |
| **PCI confluence** | [https://checkout.atlassian.net/wiki/spaces/CHEC/pages/5119089765/PCI+DSS+-+Requirements+for+merchants#C.-PCI-Compliance](https://checkout.atlassian.net/wiki/spaces/CHEC/pages/5119089765/PCI+DSS+-+Requirements+for+merchants#C.-PCI-Compliance) |

 

### **Importance**

- Security: Guarantees that private cardholder information is kept safe.

- Trust: Increases customers' trust by assuring them that their payment information is safe.

- Financial and Legal Consequences: Failing to comply with regulations may result in penalties, elevated transaction costs, and possibly the inability to accept credit card payments. Organisations that uphold PCI compliance safeguard not only the data of their clients but also their own good name and internal operations.

 

### **Associated Risks**

- Assume that a Checkout merchant experiences an account data compromise (ADC) or any other negative event (such as a high fraud ratio or issuer complaints). If so, the Schemes will look into this to determine the cause of the incident. Checkout.com would be held directly liable and subject to fines if it failed to report the merchant or reported the merchant incorrectly.   
 

- More information can be found [here](https://checkout.atlassian.net/wiki/spaces/CHEC/pages/5232885761/PCI+DSS+compliance+validation+with+SecurityMetrics#Risks-associated-with-non-compliance-of-PCI-DSS-requirements).

## **Roles, Levels and Responsibilities**

| **Role** | **Responsibility** |
| --- | --- |
| **Merchant Care L1** | - Responsible for acting as the first point of contact in PCI DSS queries and providing merchants with the details required to fill out the PCI DSS SAQ Assessment. |
| **Scheme Registration and Reporting** | - Ensure merchants are compliant with PCI requirements via annual assessments (more details [here](https://checkout.atlassian.net/wiki/spaces/CHEC/pages/5505450012/PCI+Compliance))  - The Team will assist Merchant Care in answering their queries. |

 

## **PCI Compliance Reporting Timeframe**

| **Scheme** | **Reporting Time Frame** | **Report Due Date** |
| --- | --- | --- |
| **VISA** **(VISA has 2 reporting timeframes within a year giving flexibility to merchants whose financial years differ)** | 1st of Jan – 31st of Dec | 31st of March |
| 1st July – 30th of June | Global (Except APAC) - 1st of November APAC - _30th  of September_ |  |
| **MASTERCARD** | 1st of Jan – 31st of Dec | 31st of March |
| 1st July – 30th of June | 30th of September |  |
| **For US Merchant** |  | 1st June & 1 December |

For more information, please click [here](https://checkout.atlassian.net/wiki/spaces/CHEC/pages/5119089765/PCI+DSS+-+Requirements+for+merchants#III.-When-do-we-need-to-report-our-merchants'-compliance-status-to-Schemes%3F)For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the PCI DSS articles, please see ****[PCI DSS Tools & Permissions.](https://checkoutint.zendesk.com/hc/en-us/articles/22435576095250-PCI-DSS-Tools-Permissions)
