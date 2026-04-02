# SOP to AI Runbook Conversion Process

A six-stage process for converting a human agent SOP into a structured AI runbook. Work through stages in order. Each stage produces a concrete output carried into the next.

---

## Stage 1: Candidate Screening

**Goal:** Decide which SOPs to convert. Not every SOP warrants a runbook. Spend 30 minutes here before committing.

### Scoring criteria

Score each SOP on these four criteria. Score 3 or 4 out of 4 = strong candidate.

| Criterion | Question | Score 1 if... |
|---|---|---|
| Volume | How often does this contact type arrive? | > 50 contacts/month (cross-reference `support-taxonomy.md`) |
| Repeatability | Is the resolution path the same every time? | Same steps apply on > 80% of contacts of this type |
| Data dependency | Does the task require external data retrieval? | Yes — payment status, account info, TPA data, etc. |
| Risk / consistency | Does inconsistent execution cause harm or compliance exposure? | Yes — reversals, account changes, dispute submissions, access changes |

### The critical filter: can Fin do it?

If Fin can handle this contact type, it is a lower priority for Agent Consultant Runbooks. Agent Consultant Runbooks are highest value for tasks Fin cannot do: third-party API calls (TPA/scheme queries), write operations requiring multi-step human judgment, treasury interactions, or complex multi-system workflows.

Cross-reference the Agent Consultant task automation backlog (Confluence, MTC space, page 7847149938) before screening manually.

### Red flags — do not convert yet

- Resolution path varies widely case by case (use Contextual AI Tools mode instead)
- SOP is out of date or known to contain incorrect steps
- Required Data Connectors do not exist and are not on the near-term backlog
- SOP covers a compliance-sensitive action requiring legal/compliance review before automation

### Priority first-wave candidates (as of Q2 2026)

| Task | Frequency | Notes |
|---|---|---|
| Query TPA status (MPGS/Cybersource) | Very high | Fin cannot do — third-party API |
| Refund reversals | High | Fin cannot do — Visa/MC reversal + Treasury adjustment |
| Bulk TPA payment captures | High | Fin cannot do — MPGS API write action |
| Manual refund to TPA | High | Fin cannot do — TPA refund API |
| APM manual refunds | Medium | Fin cannot do — APM refund API |

---

## Stage 2: SOP Decomposition

**Goal:** Break the narrative SOP into a flat, ordered list of atomic steps.

### Step 2.1 — Read end to end first

Do not annotate on a first pass. Read to understand the full shape: how many paths exist, what data is touched, where does human judgment appear?

### Step 2.2 — Identify the spine

Find the happy-path sequence: the steps an agent takes when everything goes as expected. Write as a numbered list in plain imperative sentences. One action per step. Ignore branches and exceptions for now.

Example:
```
1. Extract payment ID from ticket
2. Retrieve payment record
3. Check payment eligibility (status, age, account standing)
4. Confirm merchant intent
5. Trigger action via API
6. Post internal note
7. Send merchant confirmation
```

### Step 2.3 — Assign step types

For each step, assign a type: `retrieve` (read), `decide` (evaluate), `act` (write/execute), or `communicate` (draft + send).

If a step does two things (e.g. "retrieve the payment and check eligibility"), split it into two steps.

### Step 2.4 — Map branches and exceptions

Go through the SOP and identify every conditional: "if X, do Y". For each branch, determine:
- Is this a **pre-condition** (must be true before the runbook starts)?
- Is this an **exit condition** (the runbook cannot proceed and should stop)?
- Is this an **in-flow branch** (the runbook continues down a different path)?

### Step 2.5 — Separate policy from process

SOPs often embed policy in the procedure. Separate them:
- **Policy** = a rule the step enforces (e.g. "payment must be under 90 days old"). Goes in `decide` step logic or Pre-Conditions.
- **Process** = what the agent does (e.g. "retrieve the payment record"). Goes in the step itself.

Mixing them creates ambiguity the AI cannot resolve.

---

## Stage 3: Data Connector Specification

**Goal:** For every piece of data the runbook needs, specify exactly how to get it.

### Step 3.1 — List every data input

Work through spine steps and list every piece of information referenced. Include inputs from both `retrieve` steps and data used in `decide` logic.

| Input | Used in step(s) | Current source (human process) | Proposed source (automated) | API endpoint / query | Availability |
|---|---|---|---|---|---|
| Payment ID | Steps 1, 3, 5 | Agent reads from ticket body | Auto-extracted from ticket | — (NLP extraction) | Now |
| Payment status | Step 3 | Agent navigates to payment tool | Payments API | `GET /payments/{id}` | Now |
| Account status | Step 3 | Agent checks CRM | User Management API | `GET /accounts/{client_id}` | TBC |

### Step 3.2 — Check against the Data Connector backlog

For each input:
- **Connector already exists**: use canonical name, document the endpoint
- **In the backlog but not live**: note the dependency; flag as a gate for runbook activation
- **Not planned**: this is a new Data Connector requirement — raise with engineering before completing the runbook

### Step 3.3 — Flag data that cannot be automated

Some inputs require agent judgment (e.g. "is the merchant's request authorised?"). For these:
- Mark the step type as `decide`
- Write the question the agent must answer explicitly
- Set an approval gate at this step

Do not try to automate human judgment. Capture it as a deliberate gate.

---

## Stage 4: Approval Gate Design

**Goal:** Determine where human approval is required and what the agent approves.

### The rule

Every `act` step must have an approval gate. No exceptions.

For `decide` and `communicate` steps: apply a gate if the output is consequential or merchant-facing.

### Gate design questions

For each gate, answer:
1. What exactly is the agent approving? (Specific parameters, amounts, names — not just "the action")
2. What does the agent see before approving? (Design the confirmation view)
3. What happens if the agent rejects? (Define the exit path — do not leave implicit)
4. Is this gate avoidable in low-risk cases? (Document explicitly if a gate can be skipped)

### Gate types

| Gate type | When to apply | What agent sees |
|---|---|---|
| Data confirmation | After a `retrieve` where data drives a consequential decision | Retrieved data fields, clearly labelled |
| Eligibility sign-off | After a `decide` that gates whether the runbook proceeds | Eligibility result + criteria applied |
| Action authorisation | Before every `act` step | Exact API parameters: endpoint, amount, IDs, destination |
| Draft review | Before every `communicate` step | Full draft text with editable fields highlighted |
| Escalation handoff | At any exit requiring human escalation | Reason for exit + suggested escalation path |

### Escalation design

For each exit condition where the runbook cannot complete:
- Who the agent escalates to
- What information is pre-populated in the escalation note
- What Zendesk tag is applied (for routing and Reflex reporting)

Ambiguous escalation paths are the most common cause of runbook failure in production.

---

## Stage 5: Runbook Drafting

**Goal:** Populate the runbook template (`03-templates/ai-runbook-template.md`).

### Drafting order

Work through template sections in this order (faster than top-to-bottom):

1. **Metadata** — fill all fields; Contact Type and Source SOP anchor the runbook
2. **Data Inputs table** — paste from Stage 3 output
3. **Pre-Conditions table** — paste from Stage 2 branch extraction; add "how to verify" and "if not met" columns
4. **Steps** — one step block per step; use the correct type tag; for `act` steps, write the exact API call
5. **Approval Gate Summary** — create from Stage 4 output
6. **Exit Conditions** — list every exit path from Stage 2; every exit must have an outcome
7. **Trigger Conditions** — working backwards from completed steps, define what ticket or conversation signals should surface this runbook
8. **Reflex Tag** — define the tag string for each outcome: complete, escalated, ineligible
9. **Notes and Edge Cases** — add anything from the original SOP that does not fit the template

### Writing standard for steps

- Present tense, active voice: "Retrieve the payment record" — not "The payment record should be retrieved"
- Name the data field, source, and API endpoint explicitly
- State what the agent sees after the step completes
- Do not embed policy in process steps — policy belongs in `decide` logic or Pre-Conditions
- No vague instructions: "check the payment" is not a step; "Retrieve payment status from `GET /payments/{id}`" is

---

## Stage 6: Review, Simulation, and Activation

**Goal:** Validate the runbook before activating. A runbook that activates incorrectly erodes agent trust.

### Step 6.1 — Peer review with an experienced agent

Walk through the runbook with an agent who handles this contact type regularly. Ask:
- Does the spine match how you actually handle this today?
- Are there edge cases missing?
- Are approval gates at the right level? (Too many slows agents; too few creates risk)
- Are the draft templates in `communicate` steps correct in tone and content?

Target: no more than two rounds of revision.

### Step 6.2 — Trigger condition testing

For Fin Procedures: run 20–30 historical conversations through Fin's Simulation feature. Verify trigger conditions correctly identify real contacts and do not fire on unrelated ones.

For Agent Consultant: test trigger conditions against a sample of Zendesk tickets. Confirm the right tickets surface the runbook suggestion.

If false positive rate > 10%, tighten trigger conditions before activating.

### Step 6.3 — Data Connector validation

For each Data Connector:
- Confirm the connector is live in the target environment
- Run API calls against test payment IDs or accounts
- Confirm the data fields the runbook uses are populated in the response
- Document what happens when the API returns null or an error code

### Step 6.4 — Dry run with a real ticket

Run a supervised dry run with a willing agent on a real low-risk ticket. Pause at each `act` gate on the first dry run and confirm what would have been executed without actually executing.

### Step 6.5 — Activation and monitoring

Activate in restricted mode first (one team or queue). Monitor for two weeks before broader rollout:

| Metric | Watch for |
|---|---|
| Trigger accuracy | Is the runbook surfaced on the right tickets? |
| Gate behaviour | Are agents approving, or rejecting and going manual? |
| Exit rate | What % complete successfully vs exit early? |
| AHT delta | Is handle time lower for runbook-assisted contacts vs manual? |

If exit rate > 30% in the first two weeks, investigate the primary exit condition. This usually indicates a missing pre-condition check or an API availability gap.

---

## Conversion Checklist

Use as a final quality gate before marking a runbook Active.

**Completeness**
- [ ] All metadata fields populated
- [ ] Source SOP linked
- [ ] All data inputs have a specified source and API endpoint, or a flagged gap
- [ ] Every spine step has a type assigned
- [ ] Every `act` step has an approval gate with agent-visible parameters
- [ ] Every exit condition has a defined outcome
- [ ] Reflex tags defined for all outcome types
- [ ] Trigger conditions specified and tested

**Quality**
- [ ] Steps written in plain English with no ambiguous instructions
- [ ] Policy separated from process — no policy embedded in step instructions without a `decide` block
- [ ] Draft templates in `communicate` steps are correct in tone and contain accurate placeholders
- [ ] Edge cases documented in Notes section
- [ ] Experienced agent has reviewed and signed off

**Technical readiness**
- [ ] All required Data Connectors are live — or runbook is marked Draft pending connector availability
- [ ] Trigger conditions tested against sample tickets or conversations
- [ ] Dry run completed with no critical issues
- [ ] Escalation paths validated with the receiving team (L2, engineering, risk)

---

## Reference: Step Types

| Type | What it does | Side-effects? | Auto-execute? | Approval gate? |
|---|---|---|---|---|
| `retrieve` | Read data from external system | None | Yes | No |
| `decide` | Evaluate data, surface result | None | Yes | Yes — agent confirms before next step |
| `act` | Execute write operation | Yes — potentially irreversible | No | Yes — always, before execution |
| `communicate` | Draft message for agent review | Yes — sends to merchant or posts to ticket | No | Yes — agent approves draft |
