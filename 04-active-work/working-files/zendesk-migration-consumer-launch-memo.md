# Consumer launch date vs. platform migration: a decision only leadership can make

**To**: [VP of Product] / [VP Engineering]
**From**: Charlie Wildish
**Date**: 2026-07-14
**Topic**: The Braavos consumer public launch (Jan 2027) and the Zendesk replacement decision (Q4 2026) can't both land on their current dates — need alignment before this goes to CPO/COO.

## Summary

No realistic vendor-selection timeline gets a new support platform engineering-ready before January 2027 — procurement and build alone run Feb–Apr 2027 at the earliest. That leaves two options: launch consumer support on Zendesk in January and migrate later in 2027 once a vendor is chosen, or delay the public launch to Q2 2027 to avoid building twice. We need your view on which way to lean before this goes to CPO/COO, since it's ultimately their call on the launch date.

## Background

Checkout's Zendesk contract ends June 2027, and the RFC evaluating replacement platforms (Plain, Fin suite, others) concludes with a decision in September 2026. Separately, the Braavos consumer wallet has two launch milestones: an internal staff-only launch (end Oct 2026) and a public consumer launch (Jan 2027). Consumer support config is already being built on Zendesk for the internal launch. The public launch additionally needs CRM API integration and agent tooling for ticket judgment — work that hasn't started and is unvalidated at an estimated 2–3 months.

## What we found

- **The dates don't fit together, regardless of which vendor wins**: vendor assessment runs July–Sept 2026, decision in September, procurement takes 2–3 months and only starts after the decision (Sept/Oct–Nov/Dec 2026), and platform build takes 2–3 months after contract signing. Earliest realistic finish is Feb–Apr 2027 — after the January launch under every scenario we've modelled.
- **The internal launch (Oct 2026) is not at risk**: that work is already scoped and in progress on Zendesk with no engineering gap. The exposure is entirely on the public launch's CRM integration and agent tooling.
- **B2B and consumer support are separate teams**: this decision can be made for consumer in isolation without forcing B2B's migration timeline to move.

## What this means

- **If January is fixed**: we launch on Zendesk, start the CRM/agent-tooling engineering now decoupled from vendor selection, and accept a bounded, known amount of rework when consumer migrates to the new platform alongside B2B later in 2027.
- **If January is flexible**: we delay the public launch to Q2 2027, consumer is built once on its permanent platform, and we avoid the rework entirely — at the cost of missing the original date.
- **This is a business call, not an engineering one**: engineering can execute either path. What we need from you is a view on whether the January date is truly fixed (commercial commitments, marketing, board messaging) or has real flex — that answer picks the option.

## Recommendation

1. **Confirm your lean before CPO/COO**: tell us whether you'd advocate for Option 1 (launch Jan on Zendesk, rework later) or Option 2 (delay to Q2 2027, no rework) — or whether you think the CPO/COO should decide with no steer from us.
2. **Flag if the rework estimate needs more rigor before this goes up**: right now "bounded, known rework" is a qualitative claim; if you want it sized before the CPO/COO conversation, we can get a rough engineering estimate this week, but it will push the timeline for having this conversation.
3. **Align on how to frame the ask upward**: presented as a binary (fixed date → Option 1; flexible date → Option 2), not as a menu — the CPO/COO's answer to "is January fixed" determines the outcome, so that's the one question we should be asking them.

**Key risk if we don't decide soon**: every week the CRM/agent-tooling engineering doesn't start is a week closer to January with no path to make that date even under Option 1.

**Owner**: Charlie Wildish
**Next update**: After this conversation, ahead of CPO/COO session
**Questions to**: Charlie Wildish
