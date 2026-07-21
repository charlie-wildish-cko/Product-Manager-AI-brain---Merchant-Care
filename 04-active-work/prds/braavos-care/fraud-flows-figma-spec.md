# Fraud & Compliance Flows — Figma Build Spec

Maps consumer fraud use cases (`01-knowledge-base/processes/consumer-app-care-taxonomy.md`, Sections 6–7) and Fin escalation rules (`fin-fraud-risk-escalation.md`) into step-by-step flows for Figma flow diagrams. Two flow families, each with its own swimlane set.

**Swimlanes used throughout:**
- **Consumer** — actions and messages the consumer sees/does
- **App / Fin** — automated detection, routing, capture
- **Human Agent (L1 Care)** — first human touchpoint
- **Fraud / Compliance Ops** — investigation, MLRO, redress
- **Regulator / External** — FOS, OFSI, scheme (where applicable)

---

## Flow Family A: Consumer-Reported Fraud (Victim)

Covers: unauthorised CNP fraud, APP fraud, phishing/vishing/smishing, ATO (consumer-reported), investment/romance/recruitment/impersonation scams, card-present fraud, third-party reporting for a vulnerable consumer.

### A1. Unauthorised Transaction / Card-Present Fraud

| Step | Swimlane | Action | Notes for Figma |
|---|---|---|---|
| 1 | Consumer | Reports unrecognised transaction or lost/stolen card via app chat | Entry point: chat bubble or "Report a problem" CTA |
| 2 | App/Fin | Detects fraud-report trigger signals ("I don't recognize this transaction", "someone used my card") | Decision diamond: matches trigger signal set → route, else continue self-service |
| 3 | App/Fin | Captures transaction reference, date, amount, brief description | Form/card capture UI — no liability language shown |
| 4 | App/Fin | Freezes card immediately if approved Procedure exists | Parallel action, not blocking — freeze happens same step as capture |
| 5 | App/Fin | Escalates to human agent — **no autonomous resolution** | Hard stop, no AI resolution branch |
| 6 | Human Agent | Reviews captured evidence, opens investigation case | Handoff card showing captured data |
| 7 | Fraud Ops | Investigates, determines liability under PSR Art. 73 | 15-business-day clock starts on report — show as SLA timer element |
| 8 | Fraud Ops | Reimbursement decision: uphold / decline / partial | Decision diamond, 3 branches |
| 9a | Consumer | Notified of reimbursement — funds returned | End state, positive |
| 9b | Consumer | Notified of decline with reason + FOS referral rights | End state, must include DISP-compliant reason + escalation path |

### A2. APP Fraud / Scam Claims

| Step | Swimlane | Action | Notes for Figma |
|---|---|---|---|
| 1 | Consumer | Reports being deceived into authorising a payment | Trigger phrases: "I sent money and think it was a scam", "I was tricked into making a payment" |
| 2 | App/Fin | Matches trigger signal → **immediate hand-off, zero resolution attempt** | No self-service branch at all for this path — show as direct line, no decision diamond |
| 3 | Human Agent | Takes claim, no liability language used | Callout: "must not indicate whether reimbursement will/won't be given" |
| 4 | Fraud Ops | Investigates under PSR mandatory reimbursement rules | 50/50 liability split determination between sending/receiving PSP |
| 5 | Fraud Ops | Liaises with receiving PSP (external) | Cross-org swimlane — show as dashed line to "Receiving PSP" actor |
| 6 | Fraud Ops | Reimbursement decision (up to £85,000) | Decision diamond |
| 7 | Consumer | Notified of outcome | End state |

### A3. Account Takeover (ATO) — Consumer-Reported

| Step | Swimlane | Action | Notes for Figma |
|---|---|---|---|
| 1 | Consumer | Reports "someone has got into my account" / password changed without them / device they don't recognise | Trigger signals per escalation doc |
| 2 | App/Fin | Immediate escalation — **do not continue self-service, do not attempt ID verification** | Hard stop — annotate clearly, this is the one case where normal auth flows must NOT run |
| 3 | Human Agent | Triggers account security review workflow | Parallel action: freeze login, force re-auth |
| 4 | Fraud Ops | Reviews account activity, confirms compromise scope | — |
| 5 | Fraud Ops | Restores access via out-of-band verification, reverses unauthorised actions | — |
| 6 | Consumer | Regains access, notified of security review outcome | End state |

### A4. Phishing / Vishing / Smishing Report

| Step | Swimlane | Action | Notes for Figma |
|---|---|---|---|
| 1 | Consumer | Reports suspicious email/call/SMS claiming to be Checkout/Braavos | Lower urgency than A1–A3 — no funds necessarily moved yet |
| 2 | App/Fin | Captures details (channel, content, sender), checks if consumer acted on it | Decision diamond: "did consumer share credentials/make a payment?" |
| 3a | — | If no action taken → log for threat intel, consumer reassured, no case opened | End state, low-touch |
| 3b | Human Agent | If consumer acted on it → branch into A1 (unauthorised transaction) or A3 (ATO) as appropriate | Connector arrow to A1/A3 flow |

### A5. Third-Party Reporting for a Vulnerable Consumer

| Step | Swimlane | Action | Notes for Figma |
|---|---|---|---|
| 1 | Consumer (3rd party) | Reports fraud on behalf of a vulnerable consumer | Entry differs: identity of reporter ≠ account holder |
| 2 | App/Fin | Vulnerability trigger signals detected regardless of fraud type | Cross-cutting flag, not a separate fraud type — show as an overlay/badge applied to any A1–A4 flow |
| 3 | Human Agent | Escalates with vulnerability flag, trained agent only | Do not continue transactional resolution — same hard stop pattern as A2/A3 |
| 4 | Fraud/Compliance Ops | Handles case with Consumer Duty FG21/1 considerations (capacity, consent, safeguarding) | — |

**Design note for Figma:** build the vulnerability flag as a reusable component/overlay applied across A1–A5, not a standalone flow — any fraud report can carry it.

---

## Flow Family B: Ops-Flagged Compliance Action

Covers: AML/TM freeze, sanctions match, PEP post-onboarding, adverse media, suspected money mule, velocity alert, capability limits, account closure (compliance-driven).

**Key structural difference from Family A:** the flow *starts* in the Fraud/Compliance Ops lane, not the Consumer lane. The consumer only enters reactively.

### B1. AML/TM Alert → Account Freeze

| Step | Swimlane | Action | Notes for Figma |
|---|---|---|---|
| 1 | Fraud/Compliance Ops | TM system raises velocity or pattern alert | Entry point is a system trigger, not a chat message — draw as a system event icon |
| 2 | Fraud/Compliance Ops | Investigates alert internally | No consumer visibility at this stage |
| 3 | Fraud/Compliance Ops | Decision: freeze / restrict / clear | Decision diamond |
| 4a | — | Cleared — no consumer-facing action, alert closed silently | End state, consumer never knows |
| 4b | Fraud/Compliance Ops | Account frozen/restricted | Triggers consumer-facing lock — this is where Consumer lane activates |
| 5 | Consumer | Attempts app action, hits restriction | First consumer touchpoint — show as a blocked-state screen |
| 6 | Consumer | Contacts care asking why | — |
| 7 | Human Agent | Delivers **tipping-off-safe script only** | Critical annotation: agent has NO discretion, must use approved script, cannot confirm investigation exists |
| 8 | Human Agent | No resolution authority — escalates status query to Compliance | Dead-end for the agent by design |
| 9 | Fraud/Compliance Ops | Resolves investigation (unrelated timeline to consumer contact) | May take significantly longer than a normal support SLA — flag this as an SLA mismatch to design around (e.g., "we're reviewing your account" holding state, no ETA) |
| 10 | Fraud/Compliance Ops | Lifts restriction or proceeds to closure/SAR | Branches to B2 or B3 |

### B2. Suspected Money Mule

| Step | Swimlane | Action | Notes for Figma |
|---|---|---|---|
| 1 | Fraud/Compliance Ops | Detects pattern consistent with mule activity | System-triggered, same as B1 |
| 2 | Fraud/Compliance Ops | **Mandatory MLRO escalation** — SAR obligation | Hard branch — no path back to normal support, annotate as compliance-only |
| 3 | Fraud/Compliance Ops | Account restricted pending SAR outcome | — |
| 4 | Consumer | Contacts care re: restriction | Same tipping-off-safe script pattern as B1 step 7 |
| 5 | Human Agent | Delivers script, escalates, **cannot disclose SAR/MLRO involvement** | Reuse tipping-off-safe script component from B1 |
| 6 | Fraud/Compliance Ops | SAR filed, outcome determines account fate (close / restrict / clear) | External regulator (NCA) sits outside this diagram but can be shown as a dashed off-page reference |

### B3. Sanctions Match

| Step | Swimlane | Action | Notes for Figma |
|---|---|---|---|
| 1 | Fraud/Compliance Ops | Sanctions screening hit (onboarding or ongoing) | System-triggered |
| 2 | Fraud/Compliance Ops | **Immediate freeze** — no investigation delay, unlike B1/B2 | Annotate: this is the only branch with zero discretion on timing |
| 3 | Fraud/Compliance Ops | OFSI report filed | External regulator swimlane |
| 4 | Consumer | Contacts care re: frozen account | Same tipping-off-safe script — reuse component |
| 5 | Human Agent | Delivers script, escalates — **cannot confirm sanctions match** | — |
| 6 | Fraud/Compliance Ops | Outcome per OFSI licence/instruction | End state determined externally, not by Checkout |

### B4. Account Closure (Compliance-Driven)

| Step | Swimlane | Action | Notes for Figma |
|---|---|---|---|
| 1 | Fraud/Compliance Ops | Decision to close account (AML/risk-driven) | — |
| 2 | Fraud/Compliance Ops | Decision: standard closure (90-day PSR notice) vs. immediate (sanctions/fraud exception) | Decision diamond — two very different consumer experiences |
| 3a | Consumer | Receives 90-day notice, can query/appeal via care | Standard path — human agent can engage more normally here, no tipping-off constraint |
| 3b | Consumer | Immediate closure notice, tipping-off-safe script applies | Reuse component from B1/B2/B3 |

---

## Reusable Figma Components (build once, reuse across flows)

| Component | Used in | Purpose |
|---|---|---|
| **Tipping-off-safe script card** | B1, B2, B3, B4b | Standard agent response block — no discretion, same wording pattern each time |
| **Vulnerability flag overlay** | A1–A5 | Cross-cutting badge, not a separate flow |
| **No-AI hard-stop connector** | A1–A3, A5 | Visually distinct arrow style (e.g., thick red) showing "must reach human, no branch back to self-service" |
| **SLA timer element** | A1 (15 business days), B4a (90 days) | Shows regulatory clock start point |
| **System-triggered entry point icon** | B1, B2, B3 | Distinguishes ops-initiated flows from consumer-initiated ones at a glance |

---

## Open items before Figma build starts

1. Exact tipping-off-safe script wording — not yet drafted; Legal/Compliance sign-off needed before this becomes a real component vs. a placeholder.
2. FOS referral process for Braavos B2C doesn't exist yet — [financial-ombudsman-service-fos-handling-guidelines.md](../../../01-knowledge-base/processes/Care%20Agent%20SOPs/zendesk-kb/complaints/financial-ombudsman-service-fos-handling-guidelines.md) is B2B/merchant-only; A1 step 9b and B4a assume a consumer equivalent that needs to be written.
3. Confirm against `2026 deliverables.md` — "Complaint handling workflow (Consumer Duty compliant)" is listed under Future phases (2027), so Flow A's FOS/DISP branches may be ahead of the current build schedule.
