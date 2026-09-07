# Fin Escalation Guidance — Fraud & Risk (B2C)

Defines the scenarios where Fin must escalate to a human agent rather than attempt resolution. Applies to the Braavos consumer app from launch (2027). All six scenario types are human-only — Fin's role is detection and routing, not resolution.

**Regulatory anchors**: PSR (APP fraud, unauthorized transactions), AML MLRs 2017 (suspicious activity), Consumer Duty (vulnerability), FCA DISP (complaints)

---

## Escalation Scenarios

### 1. APP Fraud / Scam Claims

**Trigger signals**
- "I sent money to someone and I think it was a scam"
- "I was tricked into making a payment — how do I get it back?"
- "Someone called pretending to be my bank and I transferred money to them"
- "I invested money on a site and now I can't withdraw it or contact them"

**Escalation action**: Immediate hand-off to human agent. Do not attempt resolution.

**Regulatory basis**: PSR mandatory reimbursement. Fin must not make reimbursement determinations or delay the claim.

---

### 2. Unauthorized Transaction Disputes

**Trigger signals**
- "There's a payment on my account I didn't make"
- "I don't recognize this transaction — can you tell me what it is?"
- "Someone has used my card without my permission"
- "I never authorized this charge"

**Escalation action**: Capture transaction reference, date, and amount, then escalate to human. Fin may freeze the card if that action is an approved Procedure.

**Regulatory basis**: PSR Article 73 — liability determination requires human review. 15-business-day resolution clock starts on report.

---

### 3. Account Takeover (ATO) Suspicion

**Trigger signals**
- "I can't log in — someone has changed my password"
- "I got an alert that my account was accessed from a device I don't recognize"
- "Someone has got into my account"
- "My email address on the account has been changed and it wasn't me"

**Escalation action**: Immediate escalation and trigger account security review workflow. Do not continue self-service flows or attempt identity verification.

**Regulatory basis**: Active account compromise is a live security event.

---

### 4. Suspicious Activity / AML

**Trigger signals**
- "Why was my transfer blocked?"
- "I'm trying to send a large payment and it keeps failing"
- "Can I split this into multiple smaller payments?"

**Escalation action**: Silent escalation to compliance queue. Do not inform the customer that a report may be filed.

**Regulatory basis**: AML MLRs 2017 Reg 38 — tipping-off prohibition applies.

---

### 5. Vulnerable Customer Indicators

**Trigger signals**
- "I'm really struggling financially and I don't know what to do"
- "My partner has just died and I need to sort out the account"
- "Someone is telling me I have to do this — I don't really understand it"
- "I'm being pressured to send this money"

**Escalation action**: Escalate to a trained human agent with a vulnerability flag. Do not continue transactional resolution.

**Regulatory basis**: Consumer Duty — firms must identify and act on vulnerability. Must be live at launch, not added post-launch.

---

### 6. Formal Complaints

**Trigger signals**
- "I want to make a formal complaint"
- "I am not happy and I want this logged as a complaint"
- "Who do I complain to about this?"
- "I want to escalate this — this is unacceptable"

**Escalation action**: Escalate immediately. Do not attempt to resolve as a service query.

**Regulatory basis**: FCA DISP — 8-week resolution window, written acknowledgement required, must be logged as a complaint not a query.

---

## Design Principles

| Principle | Detail |
|---|---|
| No autonomous resolution | All six scenario types must reach a human |
| Capture before escalating | Collect transaction reference, date, amount, and brief description before hand-off (except AML — escalate silently) |
| No liability language | Fin must not indicate whether reimbursement will or won't be given |
| False positives preferred | For vulnerability especially — err on the side of escalation |
| Escalation SLA | P0: ATO and active fraud claims. P1: complaints and unauthorized disputes |
