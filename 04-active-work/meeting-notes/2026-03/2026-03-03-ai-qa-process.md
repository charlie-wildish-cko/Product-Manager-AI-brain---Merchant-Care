# AI-Enabled QA Process

**Date:** 2026-03-03  
**Attendees:** Charlie Wildish, Alex Jordan, Imran Khan, Robert Braam, Joel Petrosino  
**Drive source:** 1JklRyZ7Tzy6bv1Zv0XEpnada9esJw1jBzP6PLjutmhQ

## Context

Working session to design the QA corpus needed to train and evaluate the Agent Consultant AI model. The immediate problem: low QA adoption among agents is blocking creation of the training dataset.

## Key Points

- QA adoption is low — agents are not proactively sampling and curating tickets, blocking the AI training dataset.
- Decision: QA should focus on ticket quality outcomes, not agent toolkit adoption (toolkit adoption will eventually be automated by the Agent Consultant itself).
- Proposed fix: issue agents a pre-selected mandatory sample list, removing the sampling burden and enabling completion tracking ("1 of 40 done this week"). Escalation to Ashin (head of operations/care) required.
- Target dataset: at least 100 representative tickets across all case and issue types. The Agent Consultant uses this corpus to score new tickets — larger and more representative = better.
- A prior proposal to dedicate a permanent care agent to QA had stalled. Re-pitched by framing continuous scoring as a short-term necessity to enable long-term automation.
- QA bias concern noted: scoring from within merchant care tends to pass familiar processes. Counter: scoring against SOPs will surface SOP errors and force knowledge base updates. QA improvement and knowledge improvement are coupled.

## Insights

- The QA corpus is the foundational dataset for autonomous AI ticket scoring. Without it, the Agent Consultant's QA mode cannot be built.
- The B2C volume argument was used to justify the QA investment — high future volumes make manual QA untenable, strengthening the automation case.
- This is architecturally consistent with the Agent Consultant's autonomous QA mode (see `01-knowledge-base/products/agent-consultant.md`).
