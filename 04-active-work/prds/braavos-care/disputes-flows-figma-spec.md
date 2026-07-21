# Disputes Flows — Figma Build Spec (Care-Owned Only)

Maps the consumer dispute case types owned by **Care** — from the [Consumer Disputes PRD](https://docs.google.com/document/d/1VQB-41sSKCkx_O6Km2pn2VbE_IysQs8sJ0hGkoZnuks/edit) (Braavos Consumer Disputes & Buyer Protection, v1.3, target Q1 2027 external launch) — into step-by-step flows for Figma. Companion to [fraud-flows-figma-spec.md](fraud-flows-figma-spec.md) — same format, same swimlane convention.

Of the five buyer-protection case types in the source PRD, only two involve Care: **Item Not Received (INR)** and **Significantly Not As Described (SNAD)**. Unauthorised and Not Recognised are owned by Disputes Resolution; Duplicate is fully automated; all top-up/funding disputes (Section 7) are owned by Disputes Resolution or automated. None of those are included here — see the source PRD directly if they're needed later.

**Swimlanes used:**
- **Consumer** — buyer-side actions and messages
- **App / Automated Decision Engine** — tracking lookups, rules checks, auto-decisions
- **Seller** — Checkout merchant
- **Care Agent** — manual exceptions and judgment calls

---

## C1. Item Not Received (INR) — Owner: Care

| Step | Swimlane | Action | Notes for Figma |
|---|---|---|---|
| 1 | Consumer | Taps "Something wrong with this purchase?" → "Didn't arrive" | Entry point, per Section 13.2 |
| 2 | App/Decision Engine | Physical goods: carrier tracking API lookup against cardholder's verified address | Decision diamond |
| 3a | App/Decision Engine | Delivered & address matches → **auto-close in seller's favour** | End state, no human touch |
| 3b | App/Decision Engine | Not delivered / no tracking / wrong address → **auto-close in buyer's favour** | End state, no human touch |
| 3c | App/Decision Engine | Digital goods/services: check redemption/access logs, login IP/device of redemption | Parallel branch for digital — separate lane path, not a sub-step of 3a/3b |
| 4 | Care Agent | Ambiguous tracking, partial delivery, carrier dispute → manual exception | **Only step where Care is involved** |
| 5 | Consumer | Can switch case to SNAD if item arrived but wasn't as described | Connector arrow to C2 — annotate as a mid-flow reclassification, not a new filing |
| — | — | High-value orders (≥£150) require signature/Proof of Delivery before auto-close in seller's favour | Callout box on step 2 |

## C2. Significantly Not As Described (SNAD) — Owner: Care

Care owns this case type end to end — every step below is a Care touchpoint.

| Step | Swimlane | Action | Notes for Figma |
|---|---|---|---|
| 1 | Consumer | Structured intake: expected vs received, photos, item category, product link | Form UI |
| 2 | App/Decision Engine | Rules engine checks seller return policy, eligibility, prior SNAD rate of both parties | Decision diamond |
| 3 | Seller | Stage 1 option: pre-empt with partial refund offer | Optional branch, can short-circuit the flow before Care ever sees it |
| 4 | Care Agent | Manual judgement — weighs buyer evidence vs seller rebuttal/ToS, AI evidence-completeness scoring as assist only | Annotate: "hardest to fully automate" — this is the PRD's own framing, not a design choice to challenge |
| 5 | Care Agent | Default policy: buyer must return item (tracked) before refund, for tangible goods | Hard rule — "no party can hold both merchandise and funds" |
| 6 | Care Agent | Category-specific sub-branch (e.g. counterfeit) may require additional evidence — signed affidavit, police report | Show as a swim-lane widening, not a separate flow |
| 7 | Care Agent | Outcome: refund issued / claim denied / partial resolution | End states |

## Two-Stage Flow Shell (Section 6.1 / 13.2) — Care-relevant portion only

INR and SNAD both run through this state machine when the seller is a Checkout merchant. Only Stage 2's decision step is Care-owned; Stage 1 is consumer-and-seller messaging with no Care involvement.

| Stage | Swimlane | Action | Notes for Figma |
|---|---|---|---|
| Entry | Consumer | Files INR or SNAD case (Checkout-seller only) | External-merchant cards skip straight to triage — not Care's path |
| Stage 1 | Consumer + Seller | "Resolve with seller" — messaging thread, file/screenshot upload, 20-day countdown, nudges at day 3/7/14 | No Care touchpoint — include only as context leading into Stage 2 |
| Stage 2 | Consumer | "Ask Checkout to step in" — evidence upload, attestation | — |
| Stage 2 | Care Agent | Decides the outcome (INR exception / SNAD) | Feeds into C1 step 4 / C2 steps 4–7 above |
| Tracker | App | Case Progress Tracker states visible to consumer throughout | Not a Care action, but the states Care's decision feeds into: Filed → Talking to seller → Escalated to Checkout → More info needed → Resolved |

---

## Open items relevant to Care's scope

1. **Care capacity**: BPO strategy for scale (source PRD Section 19, item 3) — gates how much of SNAD can stay agent-owned vs needs automation investment.
2. **Absorbed-loss / "both parties win" path (Section 8.3)**: low-value goodwill path applies to INR and SNAD claims where investigation cost exceeds disputed value. Value ceiling (£10–£15) and frequency cap (2–3) are TBC in the source PRD — add as a branch off C1/C2 once thresholds are confirmed.
3. **Seller Protection Policy (Section 11) and Buyer Abuse Policy (Section 10)** feed into C2 step 2 (seller/buyer SNAD-rate check) but aren't documented as their own flows yet in the source PRD.
