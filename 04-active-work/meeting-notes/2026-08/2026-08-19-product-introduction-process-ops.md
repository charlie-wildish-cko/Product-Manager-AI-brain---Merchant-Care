# Designing the Product Introduction Process for Ops

**Date:** 2026-08-19
**Attendees:** Caoimhe McEnallay, Alex Jordan, Charlie Wildish, Joel Petrosino, Daniel Kliza, Bernard Ryan
**Drive source:** 1pWizHtYQYnGwbS90XkXUNvqfuCRmmh0Ja--v1C2WU_0

## Context

Follow-on from the 12 August session: design a semi-automated process for introducing product changes into Operations, replacing today's reactive workflow.

## Key Points

- Charlie presented a Care operational model: customers interact via dashboard, mobile apps, web APIs and webhooks, reports and documentation. Care is engaged when self-serve fails. Required inputs are customer identity and context, their question, and the product involved. Derived outputs are knowledge, training, root cause, data required to solve, and resolution route (AI versus human). Enterprise has a white-glove route before Care; SMB and consumer hit Care directly.
- Charlie's ask: each ops domain defines the specific inputs it needs from a PM's scope or PRD, so all downstream requirements are derivable.
- Bernard: the unanswered question is what to ask product to determine whether a change materially alters how an analyst does their job. PMs often judge a change innocuous and ops discovers problems later, sometimes region-specific. He wants this done via AI, not spreadsheet questionnaires, and will retrieve his Ignis before/after impact assessment as a template.
- Daniel: does not expect PMs to know downstream ops impact. Minimum asks are a 30-second demo video and sandbox access. Impact varies hugely: routine risk-assessment-tool updates are easy to size, while Ray is a different order of magnitude ("we're at version three and nowhere close to figuring out the downstream impact"). Change management is a dedicated function at other companies; Checkout has no such role. His single biggest requirement is advance notice.
- Alex: sandbox scenarios are the gold standard for both process discovery and pre-go-live training. Proposed a tiered service model (essentials, standard, full service) so a minor wording change does not get heavyweight intake. Also flagged that regulation changes need to fit, so V1 scope needs deciding.
- MCAP (Managed Change Assessment Process): new initiative from Thomas's Strategy and Ops team, led by Orin. Covers major change, features, existing product and deprecation, using a new system called Hive that standardises information across four stages. Currently in pilot. Caoimhe: at scoping, Hive requires only a one-pager, too light for a real impact assessment. The pilot window is the opportunity to get additional mandatory fields added. MCAP assigns approvers who can reject a change with reasons, creating an audit trail.
- Enforcement debate: Daniel noted adoption of the existing OE intake form is poor even among ops leaders and ops has no authority over product teams. Charlie's position is to treat MCAP as mandatory, and if the process is not followed the change does not go live. The friction is desirable because it forces a conversation.
- AI-assisted intake: Alan is building an AI layer over the existing OE intake form that puts the onus on the requester to check whether they have supplied enough information. Charlie wants that validation baked into the product intake tool, blocking submission where mandatory fields are unanswered.
- Capacity: Joel raised that ops is treated as a dumping ground for initiatives that do not advance operational goals. Alex and Bernard flagged sizing as their hardest problem, plus scheduling collisions. Alex noted most go-lives slip and ops currently relies on that. Caoimhe proposed connecting MCAP to the intake form to OE Jira with sizing, delivery confidence and 3-6 month forward capacity visibility.

## Decisions

- MCAP is the standardised, mandatory mechanism for product-to-ops intake, with domain-specific documentation requirements and formal rejection rights for incomplete submissions.
- Each domain documents its own required inputs, fed into MCAP and Hive while the pilot is open.
- Charlie to brief Orin and get ops requirements embedded into MCAP.

## Insights

- MCAP plus Hive is the leverage point for Care's product-launch readiness, and it is in pilot now. Orin is the owner to influence; Thomas's Strategy and Ops team is the sponsor.
- Rejection rights give Care a hard gate with an audit trail: the first real enforcement mechanism Care has had.
- The ambition is machine-readable intake outputs so downstream artefacts (KB articles, training, taxonomy updates, SLA setup) can be automated. Output format standardisation is the prerequisite.
- Ray is the acknowledged worst case for ops impact assessment: still unclear internally at v3.
