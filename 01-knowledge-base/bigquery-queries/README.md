# BigQuery Saved Queries

Store your frequently-used SQL queries here for easy reuse and sharing.

## Organization

Save queries as `.sql` files with descriptive names:
- `contact-rate-monthly.sql`
- `top-categories-weekly.sql`
- `ai-resolution-daily.sql`
- `channel-breakdown.sql`

## Naming Convention

```
[metric/topic]-[timeframe]-[optional-filter].sql
```

Examples:
- `ticket-volume-weekly.sql`
- `escalations-by-topic-monthly.sql`
- `resolution-time-p95-weekly.sql`

## Template Query File

Each query file should include:

```sql
-- QUERY NAME: [Descriptive name]
-- PURPOSE: [What this query answers]
-- FREQUENCY: [How often to run: daily/weekly/monthly]
-- OWNER: Charlie Wildish
-- LAST UPDATED: [Date]
-- NOTES: [Any important context]

-- [Your SQL query here]
```

## Common Queries

See `data-sources.md` for example queries:
1. Contact Rate per 1M Transactions
2. Top Ticket Categories
3. AI Agent Containment Rate
4. Tickets by Channel
5. Weekly Ticket Trends

## Tips

- Test queries on small date ranges first
- Comment your queries for future reference
- Include LIMIT for exploratory queries
- Version your queries (v1, v2) if making major changes
- Share useful queries with team

## Integration with Workflows

Reference these queries in:
- `02-workflows/ticket-analysis.md`
- `02-workflows/integrated-analysis.md`
- Your weekly/monthly analysis routines


**Pro Tip**: Create a Google Sheet with scheduled queries that auto-refresh daily/weekly for always-current dashboards!
