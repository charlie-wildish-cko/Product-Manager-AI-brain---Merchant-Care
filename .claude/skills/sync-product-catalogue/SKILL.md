---
name: sync-product-catalogue
description: Sync the Airtable Product Catalogue to local files. Updates Checkout Products and teams.csv and adds new product definitions with Fin classification guides to product-definitions.md. Invoke with /sync-product-catalogue.
tools: Read, Write, Edit, Bash, Agent, mcp__airtable__search_bases, mcp__airtable__list_records_for_table
---

# Sync Product Catalogue

Pull live data from Airtable and update both local product files. Run whenever Airtable has changed and you need local files in sync.

**Target files:**
- `01-knowledge-base/Checkout Products and teams.csv` — full product list (Zendesk source of truth)
- `01-knowledge-base/products/product-definitions.md` — enriched definitions with Fin classification guides

---

## Step 1 — Pull from Airtable

Call `mcp__airtable__list_records_for_table` with:
- `baseId`: `appZ6DXTS8h8ZCile`
- `tableId`: `tblstpkxGEakiB7o6`
- `fieldIds`: `["fldfws8lOo3RPMYpp", "fld59M8yoenMGgOU6", "fldIXlbCnIR8yNBG5", "fldfebF9QVwucmDM1", "fldmC0SuZBj4ulqvO", "fld9KEfZODl0bpTlH", "fldp7lqGXxQPn1LqR", "fld00lOOsadW9Vhvs"]`
- `pageSize`: 8000

The result will be saved to a file path. Use that path in Step 2.

Field ID reference:
| Field ID | Name |
|---|---|
| fldfws8lOo3RPMYpp | Product name |
| fld59M8yoenMGgOU6 | Product category (array of {name}) |
| fldIXlbCnIR8yNBG5 | Product Team (multipleLookupValues) |
| fldfebF9QVwucmDM1 | Product Pillar (multipleLookupValues) |
| fldmC0SuZBj4ulqvO | Product State (multipleLookupValues) |
| fld9KEfZODl0bpTlH | Marketecture (multipleLookupValues) |
| fldp7lqGXxQPn1LqR | Product Configuration last modified (ISO datetime) |
| fld00lOOsadW9Vhvs | Overview (richText string) |

For multipleLookupValues fields, extract names via `valuesByLinkedRecordId` → each value array → `.name`. Deduplicate, join with ", ".

---

## Step 2 — Process and update CSV

Run the following Python script via Bash, substituting `AIRTABLE_FILE` with the actual path from Step 1:

```python
import json, csv
from datetime import date

AIRTABLE_FILE = "SUBSTITUTE_PATH_HERE"
CSV_PATH = "/Users/charlie.wildish/Charlie PM brain/01-knowledge-base/Checkout Products and teams.csv"

def get_lookup_names(field):
    if not field or not isinstance(field, dict):
        return ""
    names = []
    for vals in field.get("valuesByLinkedRecordId", {}).values():
        for v in vals:
            if isinstance(v, dict) and "name" in v:
                names.append(v["name"])
    return ", ".join(dict.fromkeys(names))

with open(AIRTABLE_FILE) as f:
    data = json.load(f)

# Read existing CSV for diff
with open(CSV_PATH) as f:
    old_names = {row["Product name"] for row in csv.DictReader(f) if row.get("Product name")}

rows = []
for rec in data["records"]:
    f = rec.get("cellValuesByFieldId", {})
    name = f.get("fldfws8lOo3RPMYpp", "") or ""
    if not name:
        continue
    cat_raw = f.get("fld59M8yoenMGgOU6", [])
    category = ", ".join(c["name"] for c in cat_raw if isinstance(c, dict)) if cat_raw else ""
    lm = f.get("fldp7lqGXxQPn1LqR", "") or ""
    if lm and "T" in lm:
        from datetime import datetime
        try:
            lm = datetime.fromisoformat(lm.replace("Z","+00:00")).strftime("%-m/%-d/%Y %-I:%M%p").lower().replace("am","am").replace("pm","pm")
        except:
            pass
    rows.append({
        "Product name": name,
        "Product category": category,
        "Product State": get_lookup_names(f.get("fldmC0SuZBj4ulqvO")),
        "Product Pillar": get_lookup_names(f.get("fldfebF9QVwucmDM1")),
        "Product Team": get_lookup_names(f.get("fldIXlbCnIR8yNBG5")),
        "Product Configuration last modified": lm,
        "Marketecture": get_lookup_names(f.get("fld9KEfZODl0bpTlH")),
        "_overview": f.get("fld00lOOsadW9Vhvs", "") or "",
    })

rows.sort(key=lambda r: (r["Product category"], r["Product name"]))
new_names = {r["Product name"] for r in rows}

# Write CSV (without _overview)
fieldnames = ["Product name","Product category","Product State","Product Pillar","Product Team","Product Configuration last modified","Marketecture"]
with open(CSV_PATH, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
    writer.writeheader()
    writer.writerows(rows)

# Diff
added = sorted(new_names - old_names)
removed = sorted(old_names - new_names)

# Active states for definitions work
ACTIVE_STATES = {"General availability", "Beta", "Mixed availability", "Pilot", "Live", "Coming soon"}
new_active_with_overview = [
    r for r in rows
    if r["Product name"] in new_names - old_names
    and r["Product State"] in ACTIVE_STATES
    and r["_overview"].strip()
]

print(f"CSV updated: {len(rows)} products")
print(f"Added: {len(added)} | Removed: {len(removed)}")
if added:
    print("ADDED:", added)
if removed:
    print("REMOVED:", removed)
print(f"\nNew active products with overview (candidates for definitions): {len(new_active_with_overview)}")
for p in new_active_with_overview:
    print(f"  - {p['Product name']} ({p['Product category']}, {p['Product State']})")
    print(f"    Overview: {p['_overview'][:120]}")

# Save candidates for next step
import json as _json
with open("/tmp/new_products_for_definitions.json", "w") as f:
    _json.dump(new_active_with_overview, f, indent=2)
```

---

## Step 3 — Update product-definitions.md

Only do this step if there are new active products with overviews (identified in Step 2).

Read `/Users/charlie.wildish/Charlie PM brain/01-knowledge-base/products/product-definitions.md` to understand the current state.

Read `/tmp/new_products_for_definitions.json` to get the candidate products.

**Filter out** any products already present in product-definitions.md (by name match).

**Filter out** internal/meta products (category = "Internal products").

For each remaining new product, generate a definitions table row following this format:

```
| [Product name] | [One-sentence definition based on overview] | [Key capabilities from overview, semicolon-separated] | [contact risk level] — [reason] | Merchant references [product name], [2-3 key terms a merchant would use], or [scenario-based phrase]. |
```

Contact risk guidance:
- Payment Methods: match risk level of similar payment type (BNPL = high, wallets = medium/low, card schemes = low)
- Partner Integrations: medium — plugin setup queries (unless orchestration layer = low)
- New platform APIs: medium — integration complexity
- Business Account products: medium — financial query risk
- Payouts: medium

Fin classification guide guidance — write phrases a merchant would actually say, not internal product names alone. Include:
- The product name and common abbreviations/aliases
- Scenario phrases ("payment failing via X", "X not appearing at checkout")
- Disambiguation where needed ("distinct from X")

Insert each new row into the correct section in product-definitions.md, in alphabetical order within its section. If the section doesn't exist, create it with a heading and table header before the Vault section.

Use table headers from existing sections as a reference for column order — Payment Methods sections have Geography and Payment type columns; other sections do not.

---

## Step 4 — Report

Output a clean summary:

```
## Product Catalogue Sync — [date]

**CSV updated**: [N] products ([+N added] [−N removed])

**Definitions updated**: [N new entries added]
- [Product name] ([category])
- ...

**Skipped** (no overview or internal):
- [Product name] — [reason]

**Needs review**:
- [Product name] — [flag e.g. possible rename of existing product, unclear product name]
```

If nothing changed (no added/removed products, no new definitions needed), say so clearly.
