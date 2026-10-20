# Care AI agent monthly review

**Date:** 2026-09-23  
**Attendees:** Charlie Wildish, Sebastian Garcia Cardona, Janny Chow, Ling Wong. Preethy Sundaresan invited, declined.  
**Drive source:** 1xdfPXrm7pq5VbvgbwvgBXWFEjxt4q0yu9DbguDezsZs

## Context

Monthly review of Fin escalations and negative experiences. Gemini notes only, no transcript. Attached analysis: "Chatbot Escalation Analysis" (Drive 1VxPaTqyyPlptd12zXWmMrk4IN4dV5fUEgqHLKaBlZPk).

## Key Points

**Review queue misrouting**
- Fin chat escalations were routed to Preethy, not Janny, so Janny's review queue was nearly empty.
- Charlie archived the incorrect monitor rule, unassigned the affected queues and manually assigned 16 review items to Janny.

**Fin behaviour findings**
- Email with the Account Manager CC'd: Fin generated an unexpected answer before escalating. Cause: conflict between content and recent guidance. Emails with more than 2 CCs trigger automatic routing rules. Charlie to investigate with Operator.
- Explicit chat escalation guidance caused confusing side effects in replies, so Charlie removed it. Preference: Fin handles escalation silently.
- Payouts: after rule changes, Fin no longer gives wrong pay-in instructions. Remaining gap: Fin asks for a payment ID even when the merchant gives a reference number. Janny to watch for tickets closed early when merchants do not reply.
- Mastercard payout incident (crypto and gambling merchants): Fin misdetected it as a standard payout query. Fix: on email, similar patterns auto-escalate. On chat, Fin calls the incident API and offers escalation. Fin cannot surface outage data on email.
- Japanese merchant loop: Fin escalates only after a request is repeated more than twice unless confidence is high. Repeated user messages produced repeated answers. Fin did respond correctly in Japanese.
- Charlie's read: low negative and escalated counts reflect Fin performing well overall.

**Decision**
- Dashboard web forms will be removed in most cases, making Fin the mandatory default channel before escalation.

## Insights

- Web form removal is the main lever for the end-of-year Fin resolution target.
- Incident detection on email is the largest known Fin gap, because outage data is not available to Fin on that channel.
- Explicit escalation instructions in guidance caused regressions. Silent handling works better.
- The repeat-more-than-twice escalation rule creates loops, especially in non-English conversations.
- The misrouting means the review sample was understated before 2026-09-23. Treat earlier negative-case counts as low.
