# Keziah / Charlie - AI persona interview

**Date:** 2026-07-09
**Attendees:** Charlie Wildish (PM), Keziah Zhou (L2 support specialist)
**Drive source:** 1fIu4CNmtx0G1ttXh_eiNJWxh-hWMQTOuRVlGC_hPKgA

## Context

First test of a new initiative: interview each L2 specialist to translate tacit triage/troubleshooting knowledge into AI guidance scripts. Keziah picked first as she covers the broadest and most frequent payments issues. Model: the AI Consultant reads an incoming ticket, decides which sub-agent and script to run, then follows a product-specific script to resolve. Transcript to be fed into Claude to generate the guidance script.

## Key Points

**Keziah's domain coverage**
- Payment declines, payment/integration errors, data discrepancies (missing data in gateway events), Gateway (internal + public events), Fraud Detection (risk rules, shadow/back testing), Card Processing (scheme declines, internal CP declines), Payouts / Pay to Card, Intelligent Acceptance (IA) — mostly product questions on why a transaction was optimized and pulling IA stats.
- Go-to specialisms: debugging payment/integration errors (refund, capture, void, payments endpoint), fraud detection (few others cover it), internal card-processing errors (e.g. internal 12, validation errors).
- Comfort ranking: Gateway highest (longest tenure, overlaps many downstream teams), then Card Processing, then Fraud Detection (higher volume = more exposure).

**Triage methods**
- Research method: strong internal knowledge of payment flows; consults public docs for new features and specific risk-rule properties. Always checks logs and events (requested/authorized). Needs a payment ID to investigate most issues.
- Scheme declines: logs first (gateway + card processing). Compares a successful vs failed payment on the same merchant to find missing fields (uses a "gem" that compares good/bad). Traces where a missing field originates (Gateway, CAT, or merchant not sending it).
- Spike vs one-off: a spike in declines from specific issuers goes to issuer outreach or the performance team (now has a bot), not treated as a bug. One or two payments = analyze in-house.
- Integration errors (e.g. 422): logs first; determines if Gateway-generated or from another product team. Uses correlation IDs to trace (e.g. Gateway 422 "card metadata invalid" often stems from Vault). Checks internal events (rejections aren't in public events). Now also uses Claude (scrapes the GitHub repo) for unfamiliar 422s.

**L1 (junior agent) failure modes**
- Can't navigate/interpret logs in Datadog; don't know which logs they're looking at or where an error stems from.
- Lack product knowledge to interpret data.
- Can't verify AI/bot (Rosslack) output — never exposed to the product, so they either over-escalate or reply with answers that don't make sense.
- Send issuer-decline tickets to L2 expecting a definitive root cause; issuer declines are advisory/recommendation only unless the scheme/issuer gives explicit feedback that Checkout omitted a specific data element. Card Processing has no more info on issuer declines than L2 does.
- Don't reliably follow the TPA (Third Party Acquirer) escalation process; some don't know the doc exists. Per Sid and Raina, ~95% of TPA declines (e.g. Omanet, Cyber Source) can't be resolved internally and must go directly to the TPA.
- Struggle to distinguish internal vs acquirer declines despite it being easy from event data: "internal 12" = Card Processing validation before it reaches the scheme; plain "12" = a straight issuer/scheme decline.

**Escalation criteria (to L3 / Card Processing engineering)**
- L3 = Payment Engineering Ops team in Mauritius.
- Escalate only for: sandbox failures (clearly CP-owned), explicit scheme/issuer feedback of a genuine bug, or persistent internal decline codes (internal 1, internal 12) which CP owns. If Claude/GitHub can't resolve an internal decline, send to L3.
- Otherwise, for issuer/scheme declines, L2 gives advisory/recommendation only.

## Insights

- Pilot of a scalable "persona capture" method: L2 specialist interview → Claude → sub-agent routing script. Keziah is the template/proof of concept, feeding the Agent Consultant sub-agent model and the L2 agent-persona-capture template.
- The core barrier to automating L2 is tacit knowledge — troubleshooting is learned through complex/edge cases, not written SOPs. Concrete, documentable gaps exist that could be scripted immediately: TPA escalation routing, internal-vs-acquirer decline distinction, spike-vs-one-off routing.
- Reusable classification rules for scripts: internal "12" vs plain "12"; correlation-ID tracing for cross-service errors; good-vs-bad payment comparison as the primary decline diagnostic.
- Next: Charlie runs the transcript through Claude to generate an AI guidance script, shares draft with Keziah; group refines with more product detail and edge-case examples in a follow-up session.
