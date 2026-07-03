# Support Contacts Flat Table 2025 — Metric Definitions

**Scope:** Definitions apply to the full-year export (`support_contacts_flat_table_2025.csv`), still canonical for Fin involvement rate, segment, sales_territory, and billing_region. The last-6m view (`support_contacts_flat_table_2025_last_6m.csv`) is archived as of 2026-07-02 (`05-archive/2026/data-exports/`) — for case-type/issue-type volume, use `04-active-work/working-files/Contact breakdown since April 2026.md` instead.


## Count Metrics

### zendesk_tickets
Count of support tickets created in Zendesk (solved or closed, from specified forms). Excludes test tickets, deleted tickets, no-action-required cases, and follow-ups.

### fin_only_resolved
Count of support conversations that Fin AI resolved without creating a Zendesk ticket. Excludes any chat that was later escalated or created a ticket.

### support_contacts
Total support interactions per segment. Sum of Zendesk tickets + Fin-only resolved, with no double-counting (each contact counted once).


## Dimensions

### case_type
High-level category of the support request (e.g. PAYMENTS IN, TECHNICAL ISSUE, ACCOUNT MANAGEMENT & ACCESS).

### issue_type
More specific category within case_type (e.g. Refunds, API Credentials, Login & Access).

### support_segment
Customer tier: Premium, Enterprise, or Standard. (Unmapped exists in the source data but is omitted from segment reporting in this doc set.)

### zendesk_tier
Alias tier: Tier 1, Tier 2, Tier 3, Tier 4, or Unknown.

### channel
How the merchant initiated contact:
- **Email (Merchant)** — Submitted via email by the merchant
- **Email (Internal)** — Submitted via email by CKO (internal; `raised_by_cko` tag). Not Fin-eligible; structurally unreachable by Fin.
- **Webform & API** — Submitted via web form or API
- **Fin (Dashboard)** — Started in Fin (Dashboard chat)
- **Account unlock form** — In the flat table, the subset of contacts where *channel = Other* AND *case_type = ACCOUNT MANAGEMENT & ACCESS* AND *issue_type = Login & Access*. These are the account unlock web form; Fin-eligible.
- **Other** — All other channels not listed above (phone, Slack/IM, AM/TAM, etc.). Excludes Account unlock form, which is identified by case_type = ACCOUNT MANAGEMENT & ACCESS and issue_type = Login & Access.

**Unreachable channel** — A channel where Fin cannot be the first touchpoint (by design or constraint). Contacts on these channels count in the involvement-rate denominator but cannot become Fin-involved. In this taxonomy: Email (Internal) in full; and within Other, phone P1s, Dedicated Slack/IM, AM/TAM-submitted. Tag as `fin_unreachable` in reporting.

### sales_territory
Salesforce Account Owner territory (e.g. UK, NORAM, UAE, Crypto).

### billing_region
Account billing region (e.g. EEA, APAC, Crypto).


## Derived Metrics

- **Fin involvement rate:** Share of total support contacts that went through Fin (Dashboard).
- **Fin involved:** Contacts where Fin AI participated (either resolved or escalated). In the flat table, channel = Fin (Dashboard) represents this.
