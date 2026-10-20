# Harlie / Charlie goal setting: grad AI project

**Date:** 2026-09-22  
**Attendees:** Charlie Wildish, Harlie Patel (graduate, working with fellow graduate Pragia)  
**Drive source:** 1mDIipmnN-EmNF9enc965Z5ybpNvcW61BZNT_V-OE7BM

## Context

Goal-setting session to scope Harlie's graduate "AI Hero" project and adjust goals.

## Key Points

**Scope**
- No fixed scope as long as value is quantified. Customer-facing work is in scope and has higher impact than saving an internal team an hour a week.

**Option 1: manual refunds (Charlie's first choice)**
- Flagged by Christos and Caddy. Harlie cited it as about 7% of Care volume.
- End state: customer requests refund, Fin triggers backend data collection and processing, customer is told it is done. Saves at least 5-10 minutes per case. Agent receives a spreadsheet line item for light QA.
- Constraint: no Fin capacity this year. Depends on Javad's customer bot and backend data sources not yet connected, landing Q4 (likely December).
- Guidance: optimise the non-Fin workflow now, building on Joel's earlier work, and link into Fin or Agent Consultant where possible. Questions to answer: how to identify the payment, what data the refund needs, where it lives, how to collect it, where to put it.

**Option 2: knowledge retro agent**
- Seb's content team already runs Claude/GitHub workflows for content review and generation. They lack inputs.
- Existing input: Fin-used content with resolution under 50%. Missing input: Zendesk agent threads showing knowledge gaps.
- The agent reads the thread and knowledge sources and classifies each problem as knowledge gap, training issue (agents not using existing content), or availability issue (content not available to Fin).
- Distinct from Anish's summary tool (Reflex) and Shri's QA judge. Charlie framed all three as skills of one agent.

**Option 3: AI evals**
- Pragia proposed evals on customer and consultant bots. Shri already built an early judge for the consultant bot, so extend it rather than duplicate. Shri is out until October.

**Deliverable and goals**
- Short PRD on Charlie's template ("no one reads long things"). Harlie's 3DS analysis is an ad hoc task, not a PRD.
- Removed: "operational data on bottlenecks" goal. Added: stakeholder map of people who affect Care (e.g. Oliver's Ops Excellence team, PMs) and a launch communication process so ops partners know when the team ships.
- Seb Garcia Cardona leads content: former senior technical writer. His vision is a weekly or bi-weekly loop where AI triages conversations and hands writers a list of what to check and why.

## Insights

- Manual refunds are about 7% of Care volume. Full Fin automation depends on the customer bot and backend data access, so realistically 2027.
- Agent-thread-derived knowledge gaps are not an input to the content loop today. The retro agent fills that gap.
- Summary, QA judge and knowledge retro as skills of one agent is a useful architecture framing for Reflex and Agent Consultant.
- Final choice between manual refunds and knowledge retro is pending Harlie's stakeholder validation (Joel, Anish, Shri).
