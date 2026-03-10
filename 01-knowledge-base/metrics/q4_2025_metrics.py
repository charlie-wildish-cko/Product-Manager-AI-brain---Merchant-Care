#!/usr/bin/env python3
"""Q4 2025 Fin metrics from support_contacts_flat_table_2025_q4.csv"""
import pandas as pd

path = "support_contacts_flat_table_2025_q4.csv"
df = pd.read_csv(path)

total = df["support_contacts"].sum()
fin_involved = df.loc[df["channel"] == "Fin (Dashboard)", "support_contacts"].sum()
fin_only_resolved = df["fin_only_resolved"].sum()

fin_involvement_pct = (fin_involved / total * 100) if total else 0
fin_resolution_pct = (fin_only_resolved / fin_involved * 100) if fin_involved else 0
overall_fin_resolution_pct = (fin_only_resolved / total * 100) if total else 0

metrics = [
    ("Total support contacts", int(total)),
    ("Fin involved", int(fin_involved)),
    ("Fin-only resolved", int(fin_only_resolved)),
    ("Fin involvement rate (%)", round(fin_involvement_pct, 2)),
    ("Fin resolution rate (%)", round(fin_resolution_pct, 2)),
    ("Overall Fin resolution (%)", round(overall_fin_resolution_pct, 2)),
]

print("Q4 2025 Fin Metrics")
print("-" * 40)
for name, value in metrics:
    print(f"{name:<30} {value}")
