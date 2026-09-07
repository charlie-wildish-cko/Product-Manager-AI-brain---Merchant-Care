# Care AI agent monthly reviews

**Date:** 2026-07-29
**Attendees:** Charlie Wildish (PM, Merchant Care), Preethy Sundaresan, Janny Chow, Ling Wong, Sebastian Garcia Cardona
**Drive source:** 1PHgsXXQddBKQy2Ll_lhNFOLRfzQQhZ0fuBqKQVG7Jkk
**Linked doc:** Chatbot Escalation Analysis (1VxPaTqyyPlptd12zXWmMrk4IN4dV5fUEgqHLKaBlZPk)

## Context

Monthly review of Fin conversation quality. Two Intercom dashboard bugs surfaced and blocked reliable measurement, and the group agreed a new rule for scoring auto-escalated tickets.

## Key Points

**Dashboard count bug**
- The "Assign to Me" view showed 7 items while the actual count exceeded 29, over the same seven-day period, despite Janny having cleared the queue.
- Preethy's hypothesis: tickets surface under older dates because they closed later than they were initiated. Janny's counter-evidence: the queue was empty before her leave, yet tickets dated 9 July reappeared on her return. Root cause unresolved.

**Review visibility bug**
- Completed reviews do not update the "Reviews Received" count. Workaround found in the meeting: set Period and Reviewer filters to "Submitted" to locate completed reviews. Root cause unknown.

**Escalation drivers**
- Manual refunds, bank payouts, and card payouts escalate frequently. Manual refunds legitimately need a human (manual worksheets).
- Automated payouts escalating is the anomaly. Fin has payment lookup integrations, but email-originated queries cannot share data with Fin, so they auto-escalate to a live agent.

**Fin capability gaps**
- Cannot look up merchant reference numbers or payment reference numbers, only payment IDs. Many merchant queries are reference-based. Charlie confirmed this is a known limitation in progress.
- No contextual memory of a merchant's historical questions.

**Merchant behaviour**
- A segment of merchants insists on a human even where Fin could resolve the issue. Janny to log the specific question and stated reason in Zendesk ticket notes when this happens.

**Roadmap**
- Upcoming Fin features will allow automated scans across conversation history to surface themes, replacing manual one-by-one reviews.

## Insights

- Decision: auto-escalated tickets are marked "not applicable" in reviews. Tickets escalated by system rules rather than customer intent are not scored, so review effort focuses on queries Fin should be solving but isn't.
- The email channel is the structural blocker on payout deflection. Without data sharing to Fin over email, payout queries auto-escalate regardless of Fin's lookup capability. This is a channel-architecture problem, not a knowledge problem.
- Reference-number lookup is a named Fin gap with direct deflection impact.
- Manual conversation QA is a stopgap. The target is automated theme extraction across conversation history.
- Charlie to raise a support ticket with Intercom for the inaccurate dashboard counts and the missing submitted reviews. Both bugs undermine review metrics until fixed.
