---
name: sync-product-catalogue
description: Sync the Airtable Product Catalogue to local files. Updates Checkout Products and teams.csv, reconciles product-definitions.md against the latest catalogue pull (adds missing definitions, flags anything not eligible for Fin classification, un-flags anything that's gone live), re-sorts the definitions file alphabetically by category, and — if given a Zendesk product field export — produces a practical implementation sheet for Zendesk admins. Invoke with /sync-product-catalogue.
tools: Read, Write, Edit, Bash, Agent, mcp__airtable__search_bases, mcp__airtable__list_records_for_table
---

# Sync Product Catalogue

Pull live data from Airtable and update both local product files. Run whenever Airtable has changed and you need local files in sync.

**Target files:**
- `01-knowledge-base/Checkout Products and teams.csv` — full product list (Zendesk source of truth)
- `01-knowledge-base/products/product-definitions.md` — Fin classification definitions, one entry per catalogue product
- `04-active-work/working-files/zendesk-product-field-changes-[date].csv` — practical change sheet for Zendesk admins, only produced if a Zendesk product field export is available (Step 3)

**Ground rules learned the hard way — don't relitigate these mid-run:**
- **Completeness over curation.** Every product in the catalogue gets an entry in `product-definitions.md`, full stop — including Roadmap, Not on roadmap, Deprecated, Don't sell, and internal/meta products. Never omit a product because it "isn't ready" or "won't get contacts" — that judgment call belongs to a human, not to whether the entry exists. If a product shouldn't be classified, say so *in the entry* (see below), don't leave it out.
- **Never delete an entry**, even one that's disappeared from the latest catalogue pull. Flag it. The catalogue dropping a row often just means Airtable stopped tracking it as a separate product (see Known mappings below) — the underlying support topic (Settlements, Transfers, bank/card payout rails) is usually still real.
- **Classification eligibility is a single, mechanical rule**, applied uniformly: a product is eligible for Fin classification only if **(1)** it has a matching row in the current catalogue pull (directly, or via an entry in Known mappings below), **(2)** that row's Product State is `General availability`, `Beta`, or `Mixed availability`, and **(3)** it isn't an internal/meta product (category `Internal products`, or self-evidently internal like anything prefixed `Internal - `). Everything else gets flagged NOT FOR CLASSIFICATION — no exceptions for "but it's probably fine."
- Do not fabricate a definition for a product with no Airtable overview and no way to verify what it is from public knowledge. Flag it under "Needs review" instead. A wrong definition actively harms Fin; a missing one is just a gap.

---

## Step 1 — Pull from Airtable

Call `mcp__airtable__list_records_for_table` with:
- `baseId`: `appZ6DXTS8h8ZCile`
- `tableId`: `tblstpkxGEakiB7o6`
- `fieldIds`: `["fldfws8lOo3RPMYpp", "fld59M8yoenMGgOU6", "fldIXlbCnIR8yNBG5", "fldfebF9QVwucmDM1", "fldmC0SuZBj4ulqvO", "fld9KEfZODl0bpTlH", "fldp7lqGXxQPn1LqR", "fld00lOOsadW9Vhvs"]`
- `pageSize`: 8000

The result will be saved to a file path (it's too large to inline — read it with Bash/Python, not the Read tool). Use that path in Step 2.

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

# Save the full current catalogue rows for Step 4 (needs every row, not just new ones)
import json as _json
with open("/tmp/catalogue_rows_full.json", "w") as f:
    _json.dump(rows, f, indent=2)
```

---

## Step 3 — Cross-reference against a Zendesk product field export (optional)

Run this step only if the user has provided (or references) a Zendesk ticket field export for the product field — a CSV with columns `value`, `tag`, `default`, where `value` is `Category::Product Name` (or just `Product Name` for uncategorized values like `Unclassified Product`), or a Google Sheet containing the same. If no such file is available, skip straight to Step 4 — Step 4 covers every catalogue product regardless.

This step produces a practical, action-oriented sheet for whoever implements the change in Zendesk (ZD admins) — it is not the same as Step 2's Airtable-vs-git change log, and it is not required for Step 4 to run.

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
        zd_rows.append({"category": cat, "product": prod, "tag": row.get("tag", "")})

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
in_scope_names = {r["Product name"] for r in in_scope}

out_rows = []
for cr in in_scope:
    name = cr["Product name"]
    matches = zd_by_norm.get(norm(name), [])
    if not matches:
        action = "ADD NEW VALUE"
        tag = make_tag(cr["Product category"], name)
        note = "Not currently in Zendesk product field"
    else:
        exact = [m for m in matches if m["product"] == name]
        if exact:
            action, tag, note = "NO CHANGE", exact[0]["tag"], ""
        else:
            action = "NO CHANGE — verify spelling"
            tag = matches[0]["tag"]
            note = f"Zendesk currently shows '{matches[0]['product']}' vs catalogue '{name}' — cosmetic difference only, or confirm they're the same thing"
    out_rows.append({"Zendesk product field action": action, "Product category": cr["Product category"],
                      "Product name": name, "Product state": cr["Product State"], "Zendesk tag": tag, "Note": note})

# Zendesk values with no catalogue match at all — this is the list Step 4's reconciliation
# pass also produces independently (from product-definitions.md's own headings), but cross-checking
# against the live Zendesk export catches values that were never added to product-definitions.md
# at all, not just ones that are there but now stale.
zendesk_only = [r for r in zd_rows if norm(r["product"]) not in {norm(n) for n in in_scope_names} and r["product"] != "Unclassified Product"]

order = {"ADD NEW VALUE": 0, "NO CHANGE — verify spelling": 1, "NO CHANGE": 2}
out_rows.sort(key=lambda r: (order.get(r["Zendesk product field action"], 9), r["Product category"], r["Product name"]))

with open(OUT_PATH, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(out_rows[0].keys()))
    w.writeheader()
    w.writerows(out_rows)

from collections import Counter
print(Counter(r['Zendesk product field action'] for r in out_rows))
print(f"Saved to: {OUT_PATH}")
print(f"\nZendesk values with no catalogue match ({len(zendesk_only)}) — feed these into Step 4's reconciliation pass as extra 'live in Zendesk' names to check:")
for r in zendesk_only:
    print(f"  - {r['category']}::{r['product']}")

import json as _json
with open("/tmp/zendesk_export_names.json", "w") as f:
    _json.dump([{"category": r["category"], "product": r["product"]} for r in zd_rows], f, indent=2)
```

If this ran, pass `/tmp/zendesk_export_names.json` into Step 4 so it also reconciles the live Zendesk field values (not just what's already in `product-definitions.md`) — this is how the Stablecoin Settlement / Dashboard Reports naming gaps got caught in practice: they were live in Zendesk but had drifted out of sync with both the catalogue and the definitions file.

---

## Step 4 — Reconcile product-definitions.md against the latest catalogue

This is the core step. It has three jobs, in order: **(a)** add an entry for every catalogue product that doesn't have one, **(b)** re-flag classification eligibility on every existing entry (not just new ones) based on the current catalogue state, **(c)** surface anything that needs a human judgment call rather than guessing.

### Known mappings (maintain this list across runs)

The catalogue periodically renames or consolidates products in ways that break a naive exact-name match. Do not re-derive these from scratch every run — extend this table when you find a new one (verify via Airtable overview text matching, as done historically), and use it going forward:

```python
# doc heading name -> catalogue product name it should be treated as (still eligible if that row is live)
RENAMED_TO = {
    "Authentication (Issuing)": "Authentication",
    "Reporting (Issuing)": "Reporting",
    "Spending Controls": "Control spending",
}
# doc heading name -> catalogue umbrella row it's folded into (still eligible if that row is live)
FOLDED_INTO = {
    "BIN Management": "Configuration", "Card Product": "Configuration", "Cardholder": "Configuration",
    "Entity Structure": "Configuration", "Issuing Region": "Configuration",
    "Transactions (Issuing)": "Developer needs", "Simulation (Issuing)": "Developer needs",
}
# doc heading name -> catalogue product it has been superseded by (NOT eligible — classify under the replacement instead)
SUPERSEDED_BY = {
    "Bank Payouts": "Third Party Payouts",
    "Card Payouts": "Third Party Payouts",
    "Stablecoin Settlement": "Stablecoin Acceptance (via Coinbase)",
}
# doc heading names with genuinely no catalogue match (kept for completeness/context, not eligible)
NO_CATALOGUE_MATCH = {
    "Settlements", "Transfers", "Business Screening", "Business Verification",
    "Digital Wallets (Issuing)", "Fraud (Issuing)", "Physical card PIN",
    "SCA Exemptions (Issuing)", "SCA Out of Scope (Issuing)",
    "Dashboard Reports", "Dashboard Reports (non-financial reports)",
    "Reports API", "Reports API (non-financial reports)",
    "SFTP Reports", "SFTP (non-financial reports)",
}
# doc heading names that are internal/meta tools, never eligible regardless of state
INTERNAL_META = {
    "Airtable Product Catalogue", "Website Screening",
    "Internal - Cash ladder reporting", "Internal - FX Blotter reporting",
}
```

If Step 3 ran and produced `zendesk_only` names not in this table and not in `product-definitions.md`, treat them the same way `Stablecoin Settlement` was handled: check the catalogue for the obvious successor by category + keyword overlap, and if found, add it to `SUPERSEDED_BY`; if not, add it to `NO_CATALOGUE_MATCH` and give it a minimal entry.

### 4a — Add missing entries

Load `/tmp/catalogue_rows_full.json` (every current catalogue row, from Step 2) and the current `product-definitions.md`. For every catalogue product with no matching `###` heading:

**Eligibility check** — a product is eligible for a full, rich Fin classification entry only if all of:
1. Product State is `General availability`, `Beta`, or `Mixed availability`
2. Category is not `Internal products` and the name doesn't start with `Internal - `

**If eligible:**
- Has an Airtable overview → write the definition grounded in that text.
- No overview, but a well-known real-world company/product (verifiable from general knowledge — e.g. a named payment orchestration vendor or ecommerce platform) → write from that public knowledge, flagged in the report as "based on public knowledge, not an Airtable overview — verify before relying on it." Don't assert integration specifics you can't verify.
- No overview, name is vague/internal-sounding, or overlaps with an existing documented sub-feature under a different name → **do not fabricate.** List under "Needs review" and skip.

Full entry format (Applies-if / Does-not-apply-if / Example / Likely-keywords), matching the style of surrounding entries in that section. Payment Methods entries carry `**Geography:**` and `**Payment type:**` fields — infer from the overview text (country/region names, product-type keywords: BNPL, wallet, debit card, bank transfer, direct debit, card scheme, etc.); if genuinely unclear, write "Not specified in catalogue — verify" rather than guessing. Contact risk guidance: Payment Methods match the risk of similar payment types (BNPL = high, wallets = medium/low, card schemes = low); Partner Integrations = medium unless it's an orchestration layer (low); Business Account = medium; Payouts = medium.

**If NOT eligible** (fails the check above), still add an entry — don't skip it — using this minimal stub:

```
### [Product name]
**What it is:** [overview text if available, else a one-line description from public knowledge, else "Catalogue entry for [category] — no Airtable overview text available."]
**Classification status:** NOT FOR CLASSIFICATION — [catalogue state is 'X', not yet live | internal/meta, not merchant-facing | superseded by [Y]]. Retained for completeness against the catalogue.
**Fin instruction:** DO NOT DETECT AND CLASSIFY THIS[ — classify under [Y] instead, if superseded]
**Contact risk:** n/a — not live

**Applies if the merchant:**
- Should not currently apply — [not yet live | not merchant-facing]

**Does not apply if the merchant:**
- [Cross-reference to the nearest live sibling/replacement entry, if one exists]

**Example:** N/A — [not yet live | internal tool, not merchant-facing].

**Likely keywords:** [product name], [1-2 category-relevant terms]
```

Insert every new entry (eligible or not) alphabetically within its `##` category section. If the category section doesn't exist yet, create it (heading only — category-level sort happens in Step 5, so don't worry about where in the file it lands).

### 4b — Re-flag every existing entry

This is what catches drift on products that already have an entry but whose catalogue status has since changed (gone Deprecated, dropped off the roadmap, superseded, or — just as importantly — gone *live* after being flagged not-for-classification).

For every existing `###` entry in `product-definitions.md`:
1. Resolve its catalogue status: exact name match → check state directly; else check `RENAMED_TO` / `FOLDED_INTO` (eligible if the target row is live) / `SUPERSEDED_BY` (never eligible, note the replacement) / `NO_CATALOGUE_MATCH` / `INTERNAL_META` (never eligible) → else genuinely new drift, treat as `NO_CATALOGUE_MATCH` and flag for review.
2. If **not eligible** and the entry has no `**Classification status:**` line yet, or has one with a now-outdated reason → insert/update `**Classification status:**` and `**Fin instruction:** DO NOT DETECT AND CLASSIFY THIS` right after the risk/capability lines (before `**Applies if the merchant:**`). Never touch the Applies-if/Does-not-apply-if/Example/Likely-keywords content — those stay as historical/context documentation.
3. If **eligible** and the entry still carries a `**Classification status:**` / `**Fin instruction:**` pair from a previous run → remove both lines. The product has gone live; it's eligible for classification again.
4. Never delete an entry. Never touch entries whose status hasn't changed.

Write a short diff of what changed in this pass (newly flagged, newly un-flagged, still-flagged-same-reason) — this is the most useful part of the report, since it's the part a one-off manual check would miss.

---

## Step 5 — Re-sort product-definitions.md alphabetically by category

Category sections (`## Heading`) go A→Z. The `## How to read this file` intro section stays first, exempt from sorting. Entries within each category keep their existing order (don't re-sort `###` headings within a section — that's a separate, larger change and not part of this skill).

```python
import re

path = "01-knowledge-base/products/product-definitions.md"
with open(path) as f:
    content = f.read()

parts = re.split(r'(?m)^(## .+)$', content)
preamble = parts[0]
sections = [(parts[i].strip(), parts[i] + parts[i+1]) for i in range(1, len(parts), 2)]

intro = next((body for h, body in sections if h == "## How to read this file"), "")
cat_sections = [(h, b) for h, b in sections if h != "## How to read this file"]
cat_sections.sort(key=lambda hb: hb[0][3:].strip().lower())

new_content = preamble + intro + "".join(b for _, b in cat_sections)
with open(path, "w") as f:
    f.write(new_content)

print("Sorted", len(cat_sections), "category sections A-Z.")
```

---

## Step 6 — Report

Structure the summary so someone can act on it without re-reading the whole diff.

```
## Product Catalogue Sync — [date]

**CSV updated**: [N] products ([+N added] [−N removed] [N field-level changes])

**Bulk field-value renames** — one edit per row covers all listed products:
| Field | Old value | New value | # products |
|---|---|---|---|
...

**Split values — review individually, do NOT bulk rename**:
- [Field] '[old value]' now maps to multiple new values: ...

[If Step 3 ran:]
**Zendesk product field changes needed** ([N] add, [N] verify spelling):
- ADD: [Product name] → tag `[generated tag]`
- VERIFY SPELLING: [Product name] vs Zendesk's '[value]'
Full sheet: `04-active-work/working-files/zendesk-product-field-changes-[date].csv`

**Definitions added** ([N] eligible, [N] not-for-classification stubs):
- [Product name] ([category]) [— flag "public knowledge, unverified" if applicable]

**Newly flagged NOT FOR CLASSIFICATION this run** ([N]):
- [Product name] — [reason, e.g. "went Deprecated" / "dropped from catalogue"]

**Newly un-flagged this run — now eligible** ([N]):
- [Product name] — [now General availability / Beta / Mixed availability]

**Needs review** (not added — insufficient information, or ambiguous vs. an existing entry):
- [Product name] — [reason]

**Category sections re-sorted A-Z.**

Full catalogue change log: `04-active-work/working-files/product-catalogue-changes-[date].csv`
```

Omit any section with zero entries. If nothing changed anywhere (CSV, definitions, sort already correct), say so and stop — don't pad the report.
