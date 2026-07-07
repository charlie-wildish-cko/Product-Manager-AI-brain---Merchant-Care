# Support Platform Migration Sequencing — Decision Options

**Status**: Draft
**Created**: 2026-07-06
**Author**: Charlie Wildish
**Decision needed by**: Aligned to Zendesk RFC decision timeline (end Q4 2026)
**Depends on**: `zendesk-platform-decision-rfc.md` — this doc assumes that RFC concludes in favour of replacing Zendesk with a new platform. "New platform" is a placeholder pending that vendor decision.
**Blocked on**: Migration effort for each option is unknown until POCs complete (expected August 2026). Effort is a direct input to this decision, not a detail to fill in after — see Open Question below.

---

## Problem Statement

If the RFC decision is to replace Zendesk, we still need to decide the migration sequence: which segment (Consumer B2C, B2B) moves first, and whether Consumer lands on Zendesk as an interim step or goes straight to the new platform. Segment order affects risk, cost, and how much rework is done twice.

This doc lays out the sequencing options and their qualitative tradeoffs (risk, duplicate build, timeline shape). It does not yet size the effort behind each option — that depends on POC findings due August 2026.

---

## Options

### Option 1: Keep Zendesk
Renew and stay on Zendesk indefinitely. No migration.

**Not the preferred option** — carries forward the capability gaps and pricing risk identified in the Zendesk RFC (AI workflow execution, AR billing auditability, Platform merchant data).

---

### Option 2: Consumer on Zendesk (2026) → Consumer + B2B on new platform (2027)
Onboard Consumer support onto Zendesk by end of 2026. Migrate both Consumer and B2B onto the new platform in 2027.

- **Pro**: Consumer launches on a platform we already operate — no new-vendor risk on the B2C wallet launch critical path.
- **Con**: Consumer is built twice — once on Zendesk, once on the new platform, within about 12 months. Duplicate configuration cost (Consumer Duty flows, vulnerable customer flags, phone/IVR) for a short-lived Zendesk build.
- **Con**: Both segments migrate to the new platform simultaneously in 2027 — concentrates migration risk into one window, alongside wallet launch.

---

### Option 3: Consumer on new platform first (late 2026/early 2027) → B2B on new platform (2027)
Onboard Consumer directly onto the new platform first. Migrate B2B onto the new platform afterward, later in 2027.

- **Pro**: No duplicate build — Consumer is configured once, on the platform it will run on long-term.
- **Con**: Consumer becomes the pilot segment for an unproven platform, at the same time as the B2C wallet launch and its Consumer Duty obligations (day-one requirement). Highest-consequence segment carries the highest platform risk.
- **Pro**: B2B migrates second, benefiting from lessons learned on Consumer, while continuing to run on stable Zendesk in the meantime.

---

### Option 4: Consumer on Zendesk (12 months) → B2B on new platform → Consumer on new platform (later)
Onboard Consumer onto Zendesk and keep it there for 12 months. Migrate B2B onto the new platform. Migrate Consumer onto the new platform afterward.

- **Pro**: B2B — the segment with deeper Zendesk integration (Jira, Salesforce, Reflex, Agent Consultant) today — becomes the pilot for the new platform instead of Consumer. Lower-consequence segment absorbs the migration risk.
- **Pro**: Consumer launches on a stable, already-operating platform for its first 12 months, insulating the B2C wallet launch from new-platform risk.
- **Con**: Consumer is still built twice (Zendesk, then new platform) — same duplicate-cost issue as Option 2, deferred rather than removed.
- **Con**: Longest total timeline to a single unified platform across both segments.

---

## Comparison

| | Option 1: Keep | Option 2: Consumer→ZD, both→New (2027) | Option 3: Consumer→New first | Option 4: Consumer→ZD (12mo), B2B→New, Consumer→New later |
|---|---|---|---|---|
| Duplicate Consumer build | N/A | Yes | No | Yes |
| Wallet launch risk (new platform unproven) | None | Medium (concurrent w/ B2B) | High (Consumer is pilot) | Low (Consumer stays on Zendesk through launch) |
| Migration pilot segment | N/A | Both, same time | Consumer | B2B |
| Time to single unified platform | Never | Fastest | Fast | Slowest |
| Carries forward Zendesk RFC gaps | Yes, indefinitely | No | No | No |

---

## Key Tension

The decision is which segment should absorb new-platform risk first: **B2B** (Option 4 — lower consequence if something breaks, but slowest to unify) or **Consumer** (Option 3 — fastest to unify, but the pilot lands directly on the B2C wallet launch and its Consumer Duty obligations).

Options 2 and 4 both pay a duplicate-build cost for Consumer on Zendesk; they differ only in when B2B moves relative to that.

---

## Open Question: Effort Sizing (blocks final decision)

**Q**: What is the actual migration effort for Consumer and B2B onto the new platform — for each segment independently, and combined?

- **Why it matters**: The comparison above is qualitative (risk, duplicate build, timeline shape). It says nothing about whether any option is feasible within team capacity (4 engineers + 1 EM) or how long each segment's build actually takes. Effort could make an option currently ranked favourably (e.g. Option 3, fastest to unify) impractical if Consumer's new-platform build turns out to be heavier than B2B's, or vice versa.
- **Who can answer**: POC results
- **Deadline**: August 2026

Until this lands, treat the options above as the shortlist of viable sequences, not a ranked recommendation. Re-run the Comparison table with effort estimates once POCs complete.

---

## Next Step

1. **Now**: Circulate this doc to VP of Product, Director of Operations, and Director of Operations Excellence to align on the two sequencing questions in play — which segment pilots the new platform, and whether Consumer takes an interim Zendesk build — so the tradeoffs are understood ahead of data.
2. **August 2026**: Once POCs complete, add effort estimates per segment/option to the Comparison table above and convert this into a recommendation.
3. Sequencing decision should land alongside, not before, the Zendesk RFC recommendation — it depends on which platform is chosen and that vendor's readiness timeline.

---

## Related Documents

- `04-active-work/research/zendesk-platform-decision-rfc.md` — Build/Buy/Keep decision this sequencing depends on
- `01-knowledge-base/products/platform-embedded-ai-support-vision.md` — B2C wallet launch Consumer Duty obligations
- `2026 deliverables.md` — current roadmap dependencies on Zendesk
