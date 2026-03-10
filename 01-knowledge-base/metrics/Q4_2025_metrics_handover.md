# Q4 2025 Fin Metrics — Handover

**File:** `support_contacts_flat_table_2025_q4.csv`  
**Period:** Q4 2025 (Oct–Dec)

## Task

Compute the same metrics as for Last 6 Months 2025:

| Metric | Formula |
|--------|---------|
| Total support contacts | Sum of `support_contacts` column |
| Fin involved | Sum of `support_contacts` where `channel == "Fin (Dashboard)"` |
| Fin-only resolved | Sum of `fin_only_resolved` column |
| Fin involvement rate | `Fin involved / Total support contacts × 100` |
| Fin resolution rate | `Fin-only resolved / Fin involved × 100` |
| Overall Fin resolution | `Fin-only resolved / Total support contacts × 100` |

---

## Prompt for Python (pandas)

> I have a CSV file `support_contacts_flat_table_2025_q4.csv` with columns: case_type, issue_type, support_segment, zendesk_tier, channel, sales_territory, billing_region, zendesk_tickets, fin_only_resolved, support_contacts.
>
> Please write Python code (using pandas) to calculate these metrics and print them in a table:
> - Total support contacts (sum of support_contacts)
> - Fin involved (sum of support_contacts where channel is "Fin (Dashboard)")
> - Fin-only resolved (sum of fin_only_resolved)
> - Fin involvement rate (Fin involved / Total × 100, as percentage)
> - Fin resolution rate (Fin-only resolved / Fin involved × 100, as percentage)
> - Overall Fin resolution (Fin-only resolved / Total × 100, as percentage)
>
> Round percentages to 2 decimal places. Show the output in a simple metric name / value table.