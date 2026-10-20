# ISV Launch Readiness - Operations Stream

**Date:** 2026-09-10
**Attendees:** Henrik Takacs (organiser), Ayoola Alabi, Hector Becerra, Andre Verhaeg, John Raw, Alex Jordan, Mirabel Tay, Joel Petrosino, Gabriele Usonyte, Daniel Kliza, Charlie Wildish, John Odeke, Jamie Sims, Sebastian Chmielinski, Bernard Ryan, Gilles Beausseron, Pooja Lutchmun, Sunil Mudaliar
**Drive source:** 1m7AGhCW5gMiPBkFC_ipNBSSQF0kExGWPJbBvmovnDPk

## Context

Operations-stream readiness review for the US ISV launch, focused on onboarding automation performance and risk controls.

## Key Points

**Referral model risk**
- Platforms operating referral models have zero incentive to filter businesses before submission, shifting credit and verification risk onto Checkout.
- Contrast with platforms that retain liability and verify entities themselves, such as those onboarding schools.
- John Raw noted compliance training has landed the message that risk sits with the platform and the seller, but debated the practical need to contact sellers directly on sanctions or money owed, which is likely unavoidable if funds are outstanding. He also flagged communication gaps with sellers on sanctions and collections.

**Automation is not working**
- Automation is at 0% full pass: of roughly 20 cases processed, zero passed with full automation.
- Root cause named: agents cannot override incorrect platform or merchant-submitted data. Example given: a platform submitted annual processing volume as $5,000 instead of millions because of a formatting misunderstanding. Agent override capability is with the product team for timeline assessment.
- Automation logic also wrongly passes high-risk cases: a beneficial owner living in India passed KYC checks, and foreign UBO addresses are being permitted.

**Block list gap**
- The Mexico team found two separate businesses applying simultaneously with the same company address and the same UBO. The block list did not flag them because it only tracks previously declined or terminated merchants.
- John Raw noted identical addresses are not automatically fraud, so these need human review rather than auto-approval.
- Competitive angle: high-risk processors have similar risk profiles, so merchants declined on one platform can reappear via a competitor. Robust block-list management is therefore critical.

**Process**
- The Mexico team runs daily stand-ups with Hector's team, reviewing 2-3 cases a day with active leadership involvement.

**Decisions**
- Build a case and content library from real onboarding scenarios, sourced from meeting transcripts and caught exceptions in a spreadsheet. John Raw's use cases: performance monitoring, quality scoring, recruitment assessment, and training scenarios.

## Insights

- ISV onboarding automation is currently delivering nothing (0 of 20 full pass), and the binding constraint is a missing agent override capability. That is a product gap owned by another team which will drive Care contact volume at ISV launch.
- The block-list design flaw is a concrete product requirement worth capturing: it tracks declined and terminated merchants only, with no same-UBO or same-address matching across live applications.
- Automation failing open on high-risk cases (foreign UBO addresses passing KYC) is the more serious of the two failure modes, since a false pass is harder to detect than a false block.
- The case and content library being built from real onboarding scenarios is a reusable Care asset: it doubles as agent training material and as source content for procedures.
