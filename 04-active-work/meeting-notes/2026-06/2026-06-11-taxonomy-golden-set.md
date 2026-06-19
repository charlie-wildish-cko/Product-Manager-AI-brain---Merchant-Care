# Care Taxonomy Golden Set

**Date:** 2026-06-11  
**Attendees:** Charlie Wildish, Imran Khan (Data), Francisco Goncalves, Karan Jagmohansing  
**Drive source:** 1K2R9l_on_s2h1mEJn6IXvv3wuYnQBNs46fZpkRO5nWQ

## Context

Quarterly taxonomy review process finalised. H2 product direction for the agent toolkit discussed.

## Key Points

**Bug fix**
- Web form submissions arriving as compressed plain text — API stripped HTML. Previous fix for internal forms broke web form format. Jiro owns the fix. Workaround: Gemini to expand for agents.

**Fast loop (ongoing)**
- Looker dashboard flags cases where Fin's classification and the agent's Zendesk classification differ. Claude used to analyse discrepancies and improve Fin's taxonomy descriptions.

**Slow loop (quarterly, formalised)**
- Sample: 115 tickets (representative by taxonomy prevalence + emerging topics).
- Process: reviewers classify independently without seeing original labels (eliminates anchoring bias). Human Zendesk classification is ground truth.
- Output: retune Fin's descriptions.
- Francisco and Karan to split the 115-ticket review, targeting completion by Jun 16.

**Classification accuracy**
- Fin vs. human agent case type agreement currently above 80% (excluding broken attributes bug). Target: 90%. Case type is primary metric — issue type and reason cascade from it.
- "General" case type to be added to Fin performance filters — agents use it as catch-all when no other type fits.

**H2 product direction**
- Strategic shift: away from raw data UI toward AI-generated summaries.
- Agent Consultant moving into the toolkit directly.
- QA agent to be scoped — evaluates Consultant answers against the same knowledge sources.
- Thumbs up/down feedback mechanism to be added to the toolkit for in-context agent feedback capture.

**Consultant-as-Fin-data-layer architecture**
- Internal consultant that Fin calls to look up and analyse payment data, returning a summary to Fin rather than raw data.
- Fin acts as the communication layer; the consultant handles interpretation.
- Isolates domain knowledge; improves quality control.
- Strategic option: if Checkout ever moves away from Fin, the consultant layer (and all embedded knowledge) survives the vendor switch.

**Team update**
- Team now has 5 engineers (2 new) — more H2 capacity.

## Insights

- The consultant-as-data-layer architecture is the most significant H2 architectural decision. It decouples Checkout's domain knowledge from Fin — positioning Checkout to switch AI agent vendors without losing accumulated capability.
- Tool adoption will cap at ~80–90% (some case types out of current toolkit scope) — a realistic ceiling, not a gap.
- The thumbs up/down feedback loop is a foundational data collection mechanism for model improvement and should be treated as a data product, not just a UX feature.
- The fast loop (Looker disagreement dashboard + Claude analysis) is operationally important — it makes taxonomy quality self-improving between quarterly reviews.
