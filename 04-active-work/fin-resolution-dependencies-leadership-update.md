---
source: https://docs.google.com/document/d/1l9yOZ5jGtYshPk_YLBREckyisQQ2QaI8y9JSocLKjQY/edit
---

# Fin AI Resolution: Dependency Status Update

## Leadership note (send this version)

**2026 AI resolution rate is tracking close to plan, despite two strategic dependencies slipping to 2027, because Care built tactical workarounds for both.**

- **Q3 overall AI resolution: ~22-26% vs. ~32% planned.** The gap is real but smaller than the raw dependency slippage suggests. Analytics' Portal Connect → PLC replacement slipped to H1 2027; Care's own Agent now serves payment data to Fin directly instead, recovering most of that lift under our control.
- **Q4 overall AI resolution: ~48-52% vs. ~50% planned if the TPA fix lands — essentially on plan.** Falls to ~40-44% if it slips. Cleared/Settled payment status, worth +8% on its own, now lands in Q4 and offsets the loss of Accurate Settlement status, which is fully lost for 2026 (slipped to H1 2027, no workaround).
- **One open risk left: TPA integration (Card Processing).** Nominally on schedule for end Q4 but tied to NPG migration volume and explicitly flagged as unproven by the team delivering it. This is now the single largest lever we don't control.
- **Ask:** decide whether to escalate the TPA/NPG migration timeline with Card Processing now, or hold and re-review once NPG volume data is in.

*(Full dependency-by-dependency detail and calculation below for reference.)*

---

**Recommendation:** Involvement rate stays on plan. Resolution rate is close to plan for both Q3 and Q4 — Care's own tactical payment-data Agent covers the Q3 gap, and Cleared/Settled status (now valued at +8% on its own, not the "low single digits" first assumed) largely offsets the Q4 slip. TPA integration is the one lever left that could still move the Q4 number materially.

- Overall AI resolution: revised Q3 estimate ~22-26% vs. ~32% planned. Q4 revised estimate ~48-52% vs. ~50% planned if TPA lands as scheduled — essentially on plan; ~40-44% if it slips.
- Biggest risk: TPA integration fix (Card Processing, +~10pts) is the single largest lever still outside Care's control and is explicitly flagged unproven. Accurate Settlement status (+5pts) has slipped to H1 2027 and is fully lost for 2026 regardless of what Care does, but its impact is now largely absorbed by the bigger-than-expected Cleared/Settled lift.
- Ask: no escalation needed on payment data — Care's tactical solution covers Q3, and Cleared/Settled covers most of the Q4 gap. Decision needed on whether to escalate the TPA/NPG migration timeline with Card Processing given it's now the largest single risk left to the Q4 target.

*(Draft — adjust the recommendation and ask to match what you actually want from leadership.)*

---

## Dependency status

| Dependency | Team | Resolution uplift | Status | Landing |
|---|---|---|---|---|
| Portal Connect → PLC source-of-truth data | Analytics | +~10% (core Payin/PLC) | 🔴 Slipped to H1 2027 | Lost for 2026 |
| Care payment-data Agent (offsets the above) | Care | Recovers +~8% of the above | 🟢 On track | Q3 |
| Cleared/Settled status into Payin | Payments Processing | +8% | 🟡 Low confidence for Q4 — capacity trade-off vs. Consumer/Platform work if Care needs to offset | Q4 (at risk) |
| TPA integration issues (MENA) | Card Processing | +~10% | 🟡 Dependent on NPG migration volume — unproven whether it fixes or creates status mismatches | Q4 (at risk) |
| Accurate Settlement status | Client Settlements (FEX) | +5% | 🔴 Slipped to H1 2027 | Lost for 2026 |
| Balance statements/SoA self serve | Client Reporting (FEX) | +2-3% | 🟢 On track | Q4 |
| User management status API | — (workaround delivered) | +3-5% | 🟢 Secured via alternative AI procedure | Q3 |
| RFIs linked to Pending payouts | Card Payouts / Payments Infrastructure | included in Payin/PLC bundle | 🟢 Delivered | Delivered |

**Legend:** 🟢 on track · 🟡 at risk / low confidence · 🔴 slipped, lost for 2026

---

## What this means for the resolution rate forecast

The original Q3 resolution rate (~40%) assumed four lifts landing together: Payin/PLC data (+~10%), Accurate Settlement status (+5%), Balance statements/SoA (+2-3%), User management API (+3-5%). Of those:

- **Payin/PLC data (+~10%): recovered tactically, not strategically.** Analytics' own fix — replacing Portal Connect with PLC as source of truth — has slipped to H1 2027. But Care is building its own Agent to serve payment data to Fin directly, sidestepping that dependency. It won't be as clean as the strategic fix, so apply a modest haircut: treat this lift as **+~8%** rather than the full +10%, landing in Q3 as planned and now under Care's own control.
- **Accurate Settlement status (+5%): not landing in 2026.** Slipped to H1 2027 alongside the Settlement pipeline rebuild. No workaround identified — this lift is lost for the year.
- **Balance statements/SoA (+2-3%): on track, but for Q4, not Q3.** This dependency's ETA has always been Q4 — the original quarterly plan table over-assigned it to Q3.
- **User management API (+3-5%): secured for Q3.** Landing via an alternative steps-based AI procedure instead of the API team's deliverable, so this lift holds regardless of the API team's own timeline.

**Revised Q3 resolution rate: ~28-32%** (was ~40%) — the tactical payment-data Agent plus User management API largely offset the loss of Settlement status and the Q3-to-Q4 shift of Balance statements. **Revised Q3 overall AI resolution: ~22-26%** (was ~32%), assuming involvement rate holds at ~80%.

**Q4 is harder to call precisely.** The original Q4 jump to 60-70% resolution rate was only ever partially itemized (TPA integration +~10%, plus BAU/tutorials) — the plan document flags these as ballpark estimates. Three changes affect it, on top of the Q3 base carrying forward:

- **Balance statements/SoA (+2-3%)**: lands in Q4 as originally scheduled.
- **Cleared/Settled status into Payin (+8%): now its own line item, not a bundled estimate.** Originally folded into the Q3 Payin/PLC +10% figure with no standalone breakout. Split out on its own merit, it's worth +8% — a materially bigger Q4 lift than the "low single digits" placeholder previously assumed here. Slipped from Q3 to end Q4 (Brazil trade-off), so it lands a quarter late but at full value.
- **TPA integration fix**: still nominally on schedule for end Q4, but contingent on NPG migration volume and explicitly flagged as unproven ("NPG is still young... not fully proven if this solves existing issues or creates new"). Treat the +~10% as at-risk, not committed — this is now the single largest lever outside Care's control.

**Revised Q4 resolution rate: ~60-65%** (was ~60-70%) if TPA lands as scheduled, or **~50-55%** if it slips — the larger Cleared/Settled contribution brings Q4 close to the original plan even with Settlement status and (possibly) TPA lost. **Revised Q4 overall AI resolution: ~48-52%** (was ~50%, essentially back on plan) if TPA lands, or **~40-44%** if it slips, assuming involvement rate holds at ~80%.

*(These ranges are my calculation from the plan's stated lift sizes and your status updates — check the Payin/PLC haircut and the TPA assumption in particular, since the source plan didn't cleanly separate those bundled figures.)*

## Next step

[FILL IN — e.g. escalate Portal Connect/PLC timeline with Analytics leadership, decide whether to re-baseline the 2026 target, or hold and re-review after the Analytics POC lands end September]

---

## Resolution rate forecast model (for recalculation)

Each dependency maps to a stated resolution-rate lift in the original plan. If a dependency's ETA slips a quarter, its lift moves with it; if a dependency is dropped, its lift is removed from every quarter it was assumed in.

| Dependency                                    | Plan quarter | Stated resolution rate lift          | Status this update                                                                                                |
| --------------------------------------------- | ------------ | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| Payin/PLC data in API (core, strategic)       | Q3 2026      | +~10%                                | Analytics' strategic fix slipped to H1 2027. **Recovered tactically** by a Care-owned Agent serving payment data directly to Fin — landing in Q3, haircut to +~8% since it's an interim solution, not the clean strategic fix. |
| Cleared/Settled status into Payin             | Q4 2026 (own line, split from bundle above) | +8% | Slipped from Q3 to end Q4 (Brazil trade-off). Split out from the Payin/PLC bundle as its own line — worth +8% on its own, materially more than the earlier "low single digits" placeholder. |
| Accurate Settlement status                    | Q3 2026      | +5% (removes contacts from volume)   | Slipped to H1 2027. Not landing in 2026 — no workaround identified.                                                |
| Balance statements/SoA self serve             | Q3 2026      | +2-3% (removes contacts from volume) | On track, but for Q4 — always was; the quarterly plan table over-assigned it to Q3.                                |
| User management status API                    | Q3 2026      | +3-5%                                | Secured via alternative steps-based AI procedure — delivered, independent of API team.                             |
| TPA integration issues fixed                  | Q4 2026      | +~10% (removes contacts from volume) | Nominally on schedule for Q4 but contingent on NPG migration volume — flagged unproven, now the largest lever outside Care's control. |

**Formula:**

`Resolution rate (quarter) = prior quarter resolution rate + sum of lifts from dependencies landing in that quarter (mid-point of stated range) + tutorials/BAU content baseline`

`Overall AI resolution (quarter) = Involvement rate (quarter) × Resolution rate (quarter)`

**Recalculated against the original plan (Q1 9% → Q2 15% → Q3 32% → Q4 ~50%):**

| Quarter | Involvement (unchanged) | Resolution: plan → revised | Overall AI resolution: plan → revised |
|---|---|---|---|
| Q3 2026 | ~80% | 40% → ~28-32% | 32% → ~22-26% |
| Q4 2026 | ~80% sustained | 60-70% → ~60-65% (TPA lands) / ~50-55% (TPA slips) | ~50% → ~48-52% (TPA lands) / ~40-44% (TPA slips) |

If you get updated numbers on the Analytics POC (end Sept) or the NPG migration volume, send them over and I'll tighten these ranges.
