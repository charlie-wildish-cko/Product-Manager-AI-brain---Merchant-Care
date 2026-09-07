---
id: 24729067247506
section_id: 21991164304274
title: "TPA Escalation (MENA)"
url: "https://checkoutint.zendesk.com/hc/en-us/articles/24729067247506-TPA-Escalation-MENA"
locale: "en-us"
draft: false
promoted: false
updated_at: "2026-01-15T13:55:08Z"
permission_group_id: 26838654181266
content_tag_ids: ["01HTHRQT889RQXXSG27BB4ZJ0M"]
label_names: ["case_transactions", "MENA", "tpa_escalation", "case_transactions_issue_transaction_status"]
user_segment_ids: [11003606966930]
archive: false
---

## Introduction

In the case of MENA tickets, there will be multiple instances where we will need to depend on Third-Party Acquirers (TPAs) for resolution. 

While there is no defined SLA for their response, we can escalate this. Please note that the only channel for escalations regarding TPAs in the MENA region is through the Financial Partnership Team. This ensures timely resolution of issues when direct TPA interaction is required.

## Process Steps

1. Identify tickets where TPA involvement is necessary. Examples include:

  - Transaction decline reasons

  - Manual refunds (excluding SAB, which follows a separate process)

  - Proof of refunds

2. Collect all relevant data to provide to the TPA. For transaction queries, include:

  - Auth RRN

  - MID

  - Card details

  - Auth Code

  - Transaction Date

  - Transaction Amount

  - Refund Amount (for manual refunds, excluding SAB, follow the [TPA refund process documentation](https://docs.google.com/spreadsheets/d/1g1I4-FixwMxsF07SLu_3mtin_650uVW-0MVOzS84xg8/edit?gid=1623614344#gid=1623614344))

  - Include relevant CP logs for potential issue identification

3. Use specific and detailed subject lines in side conversations with the TPA. Avoid generic terms like "Refund Failed." Include Merchant Name, MID, or Authorisation RRN for tracking purposes

4. Reach out to the TPA with the identified issue and collated details. Be clear and concise in your communication. Refer to the this [directory](https://docs.google.com/spreadsheets/d/1ipGueNYij7yEEr1y9S-0Ba0lqS9Ia3Wbsnm6YuvwoaQ/edit?gid=1771915325#gid=1771915325) for MENA TPA contact details

5. If no response is received from the TPA within 3 business days, escalate the ticket

  - Please note that business days in MENA run from Sunday to Thursday

  - Add the Financial Partnership's team to the thread (notably, [Ibrahim Al Husine](ibrahim.alhusine@checkout.com))

  - Fill out the [TPA Escalation Tracker](https://docs.google.com/spreadsheets/d/17q9rdlgQ20nvDq_BoV8M8qiX5QnGontQLa7iGxJvTRo/edit?gid=0#gid=0), with the following details:-

    - 
**Ticket Number:** ZenDesk Ticket URL

    - 
**Status:** Pending

    - 
**Agent Name:** Your Name

    - 
**Email Subject:** Subject of the TPA side conversation (be specific)

    - 
**Merchant Name:** Client Name from ZenDesk

    - 
**Acquirer Name:** TPA name

    - 
**Tier:** Tier from ZenDesk

    - 
**Query Type:** Issue type (e.g., Transaction Decline)

    - 
**Number of Days:** Days elapsed since the initial request

**Notes and Tips for Effective Escalation**

- Maintain a respectful tone

- Follow up regularly (every two business days, unless urgent)

- Do not escalate without adding to the [tracker](https://docs.google.com/spreadsheets/d/17q9rdlgQ20nvDq_BoV8M8qiX5QnGontQLa7iGxJvTRo/edit?gid=0#gid=0), and do not remove existing entries

- Escalations must go through the Financial Partnership Team (notably,  [Ibrahim Al Husine](ibrahim.alhusine@checkout.com) or [Karam Makki](Karam.Makki@checkout.com))

## Glossaries and Definitions

For **Key Terms and Definitions** on Transactions as well as an **introduction into MENA Gateway and non-Gateway merchants**, please see ****[Transactions Glossary](https://checkoutint.zendesk.com/hc/en-us/articles/21991201065106-Transactions-Glossary-Introduction)**.  **
 
 
 
 
 
 
 
 
 

For guidance on the** tools and permissions** that you need to be able to perform the tasks detailed in the Transactions articles, please see ****[Transactions Tools & Permissions](https://checkoutint.zendesk.com/hc/en-us/articles/21991176883474-Transactions-Tools-Permissions)**.**
