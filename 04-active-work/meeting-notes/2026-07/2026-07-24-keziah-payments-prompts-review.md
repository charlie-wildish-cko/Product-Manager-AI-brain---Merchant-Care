# Keziah / Charlie — payments prompts review

**Date:** 2026-07-24
**Attendees:** Charlie Wildish (PM, Merchant Care), Keziah Zhou (payments SME)
**Drive source:** 1YMHj_omDIt7QqfjlZNgX5vjx-CCiYLYTBhCnCX01Fp0

## Context

First SME review of the payments diagnostic agent instruction docs (main analyzer plus decline debugger), ahead of Keziah's maternity leave from mid-September 2026.

## Key Points

**Agent doc structure**
- Sections: role, data sources, tools, reasoning framework, workflow, escalation scenarios, output, rules. Assembled by merging the payment performance analyzer prompt, an existing AML prompt, and Charlie's notes.
- Payouts logic is a placeholder, not implemented.
- Escalation contract: when the diagnosis finds the issue is not self-servable, the agent sets an escalation attribute Fin reads (escalate: yes) and routes to the right team.
- Merchant-facing output condensed to what happened / why / what to do next, plus a reasoning trace kept in logs only. Hard rules: no PII, no PCI, no padding.

**Decline debugger (secondary doc)**
- Activates when a decline is detected. Checks response code, recommendation code, authentication, payload, cross-border categories, recurring status, then runs a checklist and returns a rationale to the main agent for validation. Positioned as level 2 troubleshooting.

**Scope decision**
- Agent scope restricted to the payment search API response. Anything outside that response is unavailable to it. Payment search is expected to align with pay-in and pay-out data over time, which closes the gap. The dashboard payment search API is not fully aligned with the merchant-facing one and is incomplete.

**NPG / TPA**
- New TPA (Transaction Processing Analysis) process under Checkout's NPG replaces phased-out MPG/Cybersource paths. Only a handful of merchants on it, limited information available.
- Standard TPA cases escalate to the TPA team. Under NPG, Care debugs these itself. It arrives via the existing global acquiring ID data point, so it is a new scenario in the decline debugger rather than a new field.

**ISO Guru premise challenged**
- A hackathon project pitched that Care takes a long time to resolve ISO code issues. Keziah rejected the premise: she uses gems and performance bots to decipher ISO messages and rarely raises tickets to Card Processing. Anyone can submit the level 3 / level 4 form, so volume attributed to "merchant care" is likely misattributed. Care has no direct line to the level 4 / CP London team; escalations route through Maitius's team. Same misattribution complaint previously raised on APMs.

**Hackathon**
- 60 teams. Winner: Agentic Commerce in Braavos (purchase from Checkout merchants inside the consumer app launching 2027).
- Charlie's team built automated documentation updates triggered by code changes (e.g. a gateway API change auto-updates docs). Scored 4/5 business value, 2/5 demo quality, missed the top 10. VP feedback: build it into infrastructure anyway. Keziah's view: it would remove load from the docs team and #ask-docs.

## Insights

- Keziah's maternity leave starts mid-September 2026. Armi Mujica is the payments SME cover. The transaction analyzer needs Keziah's input banked before then.
- Charlie's SME review instruction is the useful pattern: don't review the AI wording, write down how you actually debug a payment and check whether the doc matches, then flag missing knowledge and where to source it.
- Planned artefact: a reference doc of real ticket examples showing correct vs incorrect debugging, given to the agent as few-shot reference.
- Verbosity vs guardrails is a live tension. Keziah found the docs long; Charlie defended tight instruction because loose guardrails let the agent invent.
- Review deadline is soft. Nothing downstream depends on it yet, so the constraint is Keziah's leave date, not a delivery date. Estimated review effort ~2 hours.
