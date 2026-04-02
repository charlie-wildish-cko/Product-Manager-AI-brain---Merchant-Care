# Taxonomy Mapping: New → Old (new as master)

**Purpose**: Same mapping as the change doc, but ordered by the **new** taxonomy so you can work from the target structure when updating Zendesk.
**Source**: New taxonomy = [`Taxonomy - ZD work - New taxonomy.csv`](Taxonomy%20-%20ZD%20work%20-%20New%20taxonomy.csv). Mapping derived from [`taxonomy-change-mapping.csv`](taxonomy-change-mapping.csv).

**Full table**: [`taxonomy-new-to-old-mapping.csv`](taxonomy-new-to-old-mapping.csv) (99 rows, one per new Case Type + Issue Type + Reason).

**Columns**:
- **New Case Type**, **New Issue Type**, **New Reason** — master (target) values
- **Old Case Type**, **Old Issue Type**, **Old Tag** — previous Zendesk values that map here (multiple separated by ` | ` when several old values merge into one new)
- **Source** — New | Renamed | Moved | Merged etc.; blank old columns + Source = "New" means no old equivalent

Use this when you want to: set up new dropdowns from the new taxonomy and see which old values to remap or retire.
