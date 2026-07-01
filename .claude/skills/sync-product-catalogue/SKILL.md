---
name: sync-product-catalogue
description: Sync the Airtable Product Catalogue to local files. Updates Checkout Products and teams.csv, adds new product definitions with Fin classification guides to product-definitions.md, and — if given a Zendesk product field export — produces a practical implementation sheet for Zendesk admins. Invoke with /sync-product-catalogue.
tools: Read, Write, Edit, Bash, Agent, mcp__airtable__search_bases, mcp__airtable__list_records_for_table
---

# Sync Product Catalogue

Pull live data from Airtable and update both local product files. Run whenever Airtable has changed and you need local files in sync.

**Target files:**
- `01-knowledge-base/Checkout Products and teams.csv` — full product list (Zendesk source of truth)
- `01-knowledge-base/products/product-definitions.md` — enriched definitions with Fin classification guides
- `04-active-work/working-files/zendesk-product-field-changes-[date].csv` — practical change sheet for Zendesk admins, only produced if a Zendesk product field export is available (Step 3)

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

## Step 2 — Process, update CSV, and generate change report

Before running the script, check `git status` on the CSV. If it has uncommitted local edits, warn the user that the diff baseline is the last **committed** version (`git show HEAD:...`), not any uncommitted state — ask whether to proceed, commit first, or stash.

Run the following Python script via Bash, substituting `AIRTABLE_FILE` with the actual path from Step 1:

```python
import json, csv, subprocess, io
from collections import defaultdict
from datetime import date, datetime

AIRTABLE_FILE = "SUBSTITUTE_PATH_HERE"
REPO_DIR = "/Users/charlie.wildish/Charlie PM brain"
CSV_PATH = f"{REPO_DIR}/01-knowledge-base/Checkout Products and teams.csv"

def get_lookup_names(field):
    if not field or not isinstance(field, dict):
        return ""
    names = []
    for vals in field.get("valuesByLinkedRecordId", {}).values():
        for v in vals:
            if isinstance(v, dict) and "name" in v:
                names.append(v["name"])
    return ", ".join(dict.fromkeys(names))

# Baseline = last committed version, for a full field-level diff (not just add/remove by name)
old_content = subprocess.run(
    ["git", "-C", REPO_DIR, "show", f"HEAD:01-knowledge-base/Checkout Products and teams.csv"],
    capture_output=True, text=True
).stdout
old_rows_by_name = {r["Product name"]: r for r in csv.DictReader(io.StringIO(old_content))} if old_content else {}
old_names = set(old_rows_by_name)

with open(AIRTABLE_FILE) as f:
    data = json.load(f)

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
        try:
            lm = datetime.fromisoformat(lm.replace("Z","+00:00")).strftime("%-m/%-d/%Y %-I:%M%p").lower()
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
new_rows_by_name = {r["Product name"]: r for r in rows}

# Write CSV (without _overview)
fieldnames = ["Product name","Product category","Product State","Product Pillar","Product Team","Product Configuration last modified","Marketecture"]
with open(CSV_PATH, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
    writer.writeheader()
    writer.writerows(rows)

# --- Diff: added / removed / field-level changes ---
added = sorted(new_names - old_names)
removed = sorted(old_names - new_names)
common = sorted(new_names & old_names)

DIFF_FIELDS = ["Product category", "Product State", "Product Pillar", "Product Team", "Marketecture"]
field_changes = []  # (name, field, old_value, new_value)
for name in common:
    o, n = old_rows_by_name[name], new_rows_by_name[name]
    for col in DIFF_FIELDS:
        ov, nv = (o.get(col) or "").strip(), (n.get(col) or "").strip()
        if ov != nv:
            field_changes.append((name, col, ov, nv))

# Group renames on dropdown-style fields into distinct (old -> new) value pairs —
# these are the fields most likely to be Zendesk custom field values, so a value
# rename in Zendesk covers every affected product in one edit instead of N edits.
BULK_RENAME_FIELDS = ("Product Team", "Product Pillar", "Product State")
grouped = defaultdict(lambda: defaultdict(list))  # field -> (old,new) -> [names]
other_changes = []
for name, col, ov, nv in field_changes:
    if col in BULK_RENAME_FIELDS:
        grouped[col][(ov, nv)].append(name)
    else:
        other_changes.append((name, col, ov, nv))

# Flag old values that split into more than one new value — these are NOT clean
# bulk renames and must be reviewed product-by-product instead.
split_warnings = []  # (field, old_value, [(new_value, [names]), ...])
for field, pairs in grouped.items():
    old_to_news = defaultdict(list)
    for (ov, nv), names in pairs.items():
        old_to_news[ov].append((nv, names))
    for ov, variants in old_to_news.items():
        if len(variants) > 1:
            split_warnings.append((field, ov, variants))

# --- Write full change log for Zendesk updates ---
sync_date = date.today().isoformat()
out_path = f"{REPO_DIR}/04-active-work/working-files/product-catalogue-changes-{sync_date}.csv"
with open(out_path, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Change type", "Product name", "Field", "Old value", "New value"])
    for name in added:
        w.writerow(["ADDED", name, "", "", ""])
    for name in removed:
        w.writerow(["REMOVED", name, "", "", ""])
    for name, col, ov, nv in field_changes:
        w.writerow(["CHANGED", name, col, ov, nv])

print(f"CSV updated: {len(rows)} products")
print(f"Added: {len(added)} | Removed: {len(removed)} | Field-level changes: {len(field_changes)}")
if added:
    print("ADDED:", added)
if removed:
    print("REMOVED:", removed)

print("\n--- Bulk value renames (safe to apply as a single Zendesk field-value edit) ---")
for field in BULK_RENAME_FIELDS:
    pairs = grouped.get(field, {})
    split_old_values = {w[1] for w in split_warnings if w[0] == field}
    clean_pairs = {k: v for k, v in pairs.items() if k[0] not in split_old_values}
    if clean_pairs:
        print(f"\n{field}:")
        for (ov, nv), names in sorted(clean_pairs.items(), key=lambda x: -len(x[1])):
            print(f"  '{ov}' -> '{nv}'  ({len(names)} products)")

if split_warnings:
    print("\n--- SPLIT VALUES: review individually, do not bulk rename ---")
    for field, ov, variants in split_warnings:
        print(f"\n{field}: '{ov}' split into {len(variants)} values —")
        for nv, names in variants:
            print(f"  -> '{nv}': {', '.join(names)}")

if other_changes:
    print("\n--- Other field changes (not on a bulk-rename field) ---")
    for name, col, ov, nv in other_changes:
        print(f"  {name} | {col}: '{ov}' -> '{nv}'")

print(f"\nFull change log saved to: {out_path}")

# Active states for definitions work — includes products with NO overview too;
# Step 4 decides how to handle missing overview instead of silently dropping them here.
ACTIVE_STATES = {"General availability", "Beta", "Mixed availability", "Pilot", "Live", "Coming soon"}
new_active = [
    r for r in rows
    if r["Product name"] in new_names - old_names
    and r["Product State"] in ACTIVE_STATES
]

print(f"\nNew active products (candidates for definitions): {len(new_active)}")
for p in new_active:
    has_ov = "has overview" if p["_overview"].strip() else "NO OVERVIEW"
    print(f"  - {p['Product name']} ({p['Product category']}, {p['Product State']}) [{has_ov}]")

# Save candidates for next step
import json as _json
with open("/tmp/new_products_for_definitions.json", "w") as f:
    _json.dump(new_active, f, indent=2)
```

---

## Step 3 — Cross-reference against a Zendesk product field export (optional)

Run this step only if the user has provided (or references) a Zendesk ticket field export for the product field — a CSV with columns `value`, `tag`, `default`, where `value` is `Category::Product Name` (or just `Product Name` for uncategorized values like `Unclassified Product`). If no such file is available, ask once whether the user has one; if not, skip to Step 4 using Step 2's candidate list directly.

This step produces a practical, action-oriented sheet for whoever implements the change in Zendesk (ZD admins) — it is not the same as Step 2's Airtable-vs-git change log.

Run the following Python script via Bash, substituting `ZD_PATH` with the actual Zendesk export path:

```python
import csv, re, subprocess, io
from collections import defaultdict
from datetime import date

ZD_PATH = "SUBSTITUTE_ZENDESK_EXPORT_PATH_HERE"
REPO_DIR = "/Users/charlie.wildish/Charlie PM brain"
CSV_PATH = f"{REPO_DIR}/01-knowledge-base/Checkout Products and teams.csv"
OUT_PATH = f"{REPO_DIR}/04-active-work/working-files/zendesk-product-field-changes-{date.today().isoformat()}.csv"

def norm(s):
    s = s.lower().strip().replace("'", "").replace("’", "")
    s = re.sub(r"[\(\)\-:,]", " ", s)
    return re.sub(r"\s+", " ", s).strip()

def snake(s):
    return re.sub(r"[^a-z0-9]+", "_", s.lower()).strip("_")

def make_tag(category, name):
    return f"product_name_{snake(category)}_{snake(name)}"

# Parse Zendesk export
zd_rows = []
with open(ZD_PATH) as f:
    for row in csv.DictReader(f):
        val = row["value"]
        if "::" in val:
            cat, prod = val.split("::", 1)
        else:
            cat, prod = "", val
        zd_rows.append({"category": cat, "product": prod, "tag": row["tag"]})

# Self-check: does the tag pattern reproduce every existing tag exactly? If not, stop and
# tell the user the convention has drifted rather than silently generating wrong tags.
mismatches = []
for r in zd_rows:
    expected = make_tag(r["category"], r["product"]) if r["category"] else f"product_name_{snake(r['product'])}"
    if expected != r["tag"]:
        mismatches.append((r["category"], r["product"], r["tag"], expected))
print(f"Tag pattern self-check: {len(zd_rows) - len(mismatches)}/{len(zd_rows)} existing tags reproduced exactly")
if mismatches:
    print("MISMATCHES — do not trust generated tags below without checking these first:")
    for m in mismatches:
        print(f"  {m}")

zd_by_norm = defaultdict(list)
for r in zd_rows:
    zd_by_norm[norm(r["product"])].append(r)

with open(CSV_PATH) as f:
    cat_rows = list(csv.DictReader(f))

old_content = subprocess.run(
    ["git", "-C", REPO_DIR, "show", "HEAD:01-knowledge-base/Checkout Products and teams.csv"],
    capture_output=True, text=True
).stdout
old_by_name = {r["Product name"]: r for r in csv.DictReader(io.StringIO(old_content))} if old_content else {}

in_scope = [r for r in cat_rows if r["Product State"] != "Not on roadmap"]

# Token-overlap check to catch renames the exact/normalized match would miss
# (e.g. catalogue "Analytics AI Assistant" vs Zendesk's existing "Analytics Assistant").
zd_all_names = {r["product"] for r in zd_rows}
in_scope_names = {r["Product name"] for r in in_scope}
def tokens(s):
    return set(re.sub(r"[^a-z0-9\s]", " ", s.lower()).split())
rename_candidates = {}  # catalogue name -> matched zendesk row
for cr in in_scope:
    name = cr["Product name"]
    if norm(name) in zd_by_norm:
        continue  # already an exact/near match, not a rename case
    ct = tokens(name)
    for zr in zd_rows:
        zt = tokens(zr["product"])
        if not ct or not zt or zr["product"] in in_scope_names:
            continue
        overlap = ct & zt
        if overlap and len(overlap) >= min(len(ct), len(zt)) and len(overlap) >= 2:
            rename_candidates[name] = zr
            break

out_rows = []
for cr in in_scope:
    name = cr["Product name"]
    matches = zd_by_norm.get(norm(name), [])
    if name in rename_candidates:
        zr = rename_candidates[name]
        action = "RENAME VALUE"
        tag = zr["tag"]
        note = f"Likely a rename of existing Zendesk value '{zr['product']}' (same tag) — rename in place rather than creating a new value, to preserve historical ticket tagging. Verify before applying."
    elif not matches:
        action = "ADD NEW VALUE"
        tag = make_tag(cr["Product category"], name)
        note = "Not currently in Zendesk product field"
        if "," in cr["Product category"]:
            note += " — multiple categories in catalogue, confirm which one Zendesk should use before creating the value/tag"
    else:
        exact = [m for m in matches if m["product"] == name]
        if exact:
            action, tag, note = "NO CHANGE", exact[0]["tag"], ""
        else:
            action = "NO CHANGE — verify spelling"
            tag = matches[0]["tag"]
            note = f"Zendesk currently shows '{matches[0]['product']}' vs catalogue '{name}' — cosmetic difference only, or confirm they're the same thing"

    old = old_by_name.get(name)
    if old is None:
        cat_flag = pillar_flag = team_flag = state_flag = "N/A (new product)"
    else:
        cat_flag = "YES" if (old.get("Product category") or "").strip() != cr["Product category"].strip() else "NO"
        pillar_flag = "YES" if (old.get("Product Pillar") or "").strip() != cr["Product Pillar"].strip() else "NO"
        team_flag = "YES" if (old.get("Product Team") or "").strip() != cr["Product Team"].strip() else "NO"
        state_flag = "YES" if (old.get("Product State") or "").strip() != cr["Product State"].strip() else "NO"
    any_changed = "YES" if action in ("ADD NEW VALUE", "RENAME VALUE") or "YES" in (cat_flag, pillar_flag, team_flag, state_flag) else "NO"

    out_rows.append({
        "Zendesk product field action": action,
        "Catalogue metadata changed (informational only)": any_changed,
        "Product category": cr["Product category"], "Category changed": cat_flag,
        "Product name": name,
        "Product pillar": cr["Product Pillar"], "Pillar changed": pillar_flag,
        "Product team": cr["Product Team"], "Team changed": team_flag,
        "Product state": cr["Product State"], "State changed": state_flag,
        "Zendesk tag": tag, "Note": note,
    })

order = {"ADD NEW VALUE": 0, "RENAME VALUE": 1, "NO CHANGE — verify spelling": 2, "NO CHANGE": 3}
out_rows.sort(key=lambda r: (order.get(r["Zendesk product field action"], 9), r["Product category"], r["Product name"]))

fieldnames = list(out_rows[0].keys())
with open(OUT_PATH, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(out_rows)

from collections import Counter
print(f"\n{Counter(r['Zendesk product field action'] for r in out_rows)}")
print(f"Saved to: {OUT_PATH}")

# Zendesk values with no catalogue match at all — usually finer-grained sub-features
# (e.g. Zendesk splits "Issuing" into many sub-values the catalogue tracks as one product).
# Informational only: these have no catalogue fields, so they don't belong in the sheet above.
zendesk_only = [r for r in zd_rows if norm(r["product"]) not in {norm(n) for n in in_scope_names} and r["product"] not in {zr["product"] for zr in rename_candidates.values()}]
print(f"\nZendesk values with no catalogue match ({len(zendesk_only)}) — review separately, likely sub-features not missing products:")
for r in zendesk_only:
    print(f"  - {r['product']} [{r['category']}]")

# Save the ADD NEW VALUE + RENAME VALUE candidates for Step 4 (Fin definitions)
import json as _json
with open("/tmp/zendesk_add_candidates.json", "w") as f:
    _json.dump([r for r in out_rows if r["Zendesk product field action"] in ("ADD NEW VALUE", "RENAME VALUE")], f, indent=2)
```

If this step ran, Step 4's candidate list is the `ADD NEW VALUE` rows from this sheet (the RENAME VALUE ones already have a home in Zendesk and don't need a fresh definition unless the product also lacks one). If this step did NOT run, Step 4 falls back to Step 2's `new_active` list.

---

## Step 4 — Update product-definitions.md

Build the candidate list:
- If Step 3 ran: read `/tmp/zendesk_add_candidates.json`, take the `ADD NEW VALUE` entries. Look up each product's Airtable overview from Step 2's in-memory `rows` data (or re-derive from the Airtable export file) since the Zendesk sheet doesn't carry overview text.
- If Step 3 did not run: read `/tmp/new_products_for_definitions.json` from Step 2.

Read `/Users/charlie.wildish/Charlie PM brain/01-knowledge-base/products/product-definitions.md` to understand the current state.

**Filter out** any products already present in product-definitions.md — check by exact product name against markdown table rows (first column), not a raw substring search against the whole file (substring matching produces false positives on short/common names).

**Filter out** internal/meta products (category = "Internal products") — flag them in the report instead of silently dropping them, since they may still need a Zendesk field value even without a merchant-facing Fin definition.

For each remaining candidate, classify by information available before writing anything:

1. **Has an Airtable overview** → write the definition grounded in that text.
2. **No overview, but a well-known real-world company/product** (verifiable from general knowledge, e.g. a named payment orchestration vendor or ecommerce platform) → write a definition using that public knowledge, but explicitly flag it in the report as "based on public knowledge, not an Airtable overview — verify before relying on it for Fin classification." Do not assert integration specifics you can't verify (e.g. exactly how the partner routes to Checkout.com) — describe what the company/product is generically instead.
3. **No overview, name is vague/internal-sounding, or ambiguous** (e.g. a bare noun phrase that could mean several things, or overlaps with an existing documented sub-feature under a different name) → **do not fabricate a definition.** List it under "Needs review" in the final report with the reason, and don't insert a row. Getting this wrong pollutes a file Fin uses for classification.

Before writing content for anything in bucket 3, check whether it might already be documented under a different name (e.g. a near-synonym of an existing row, like a product renamed in Airtable but not yet reflected in the docs, or a granular sub-feature already covered by a broader existing row). Flag suspected duplicates/renames instead of creating a parallel entry.

For each product to add, generate a definitions table row following this format:

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

## Step 5 — Report

Output a summary structured for someone updating Zendesk fields, not just a prose recap. Pull the numbers and groupings straight from Step 2's (and, if it ran, Step 3's) script output.

```
## Product Catalogue Sync — [date]

**CSV updated**: [N] products ([+N added] [−N removed] [N field-level changes])

**Bulk field-value renames** — one edit per row covers all listed products:
| Field | Old value | New value | # products |
|---|---|---|---|
| [Product Team/Pillar/State] | [old] | [new] | [N] |
...

**Split values — review individually, do NOT bulk rename**:
- [Field] '[old value]' now maps to multiple new values: '[new value A]' ([products]), '[new value B]' ([products])

**Other field changes** (not on a bulk-rename field, e.g. Product category / Marketecture):
- [Product name] | [field]: '[old]' → '[new]'

[If Step 3 ran, include this block — otherwise use the simpler "Add/Remove to Zendesk product field" lists from the old format:]

**Zendesk product field changes needed** ([N] add, [N] rename, [N] verify spelling):
- ADD: [Product name] → tag `[generated tag]`
- RENAME: [Product name] — likely renames existing Zendesk value '[old value]', same tag `[tag]`
- VERIFY SPELLING: [Product name] vs Zendesk's '[value]'

Full sheet (every in-scope product, all 5 catalogue fields, action + tag + change flags): `04-active-work/working-files/zendesk-product-field-changes-[date].csv`

**Definitions updated**: [N new entries added]
- [Product name] ([category]) [— flag "public knowledge, unverified" if applicable]
- ...

**Skipped** (already documented, internal, or insufficient information to write reliably):
- [Product name] — [reason]

**Needs review**:
- [Product name] — [flag e.g. possible rename/duplicate of an existing row, ambiguous name, Airtable category/naming inconsistency worth flagging to the Product team]

Full catalogue change log (every added/removed/changed row from the Airtable sync itself): `04-active-work/working-files/product-catalogue-changes-[date].csv`
```

Omit any section with zero entries rather than printing it empty. If nothing changed at all (no added/removed products, no field-level changes, no new definitions needed), say so clearly and skip the rest of the template.
