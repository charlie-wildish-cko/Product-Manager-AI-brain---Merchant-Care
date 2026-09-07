# Braavos & Care design — fortnightly sync

**Date:** 2026-08-06
**Attendees:** Charlie Wildish, Umang Sota, Philip Mueller, Georgios Maninis, Nikhil Chandrashekhar, Fabio Marques, Daniel Kliza. Invited: Fraser Bryant, Sammie Spector, Joel Petrosino, Oliver Westlake-Simm, Jithin Radhakrishnan
**Drive source:** 1L3fnUZOLe2tp_-vqQBUW1TQzNfgH67qnfriqWFraiTg

## Context

Second instance of a fortnightly design touchpoint for Braavos (B2C consumer), set up roughly six weeks ago. Covered consumer content hosting, Care design scope timing, Fin widget constraints, and the consumer agent toolkit.

## Key Points

**Content hosting**

- Merchant content today is authored in GitHub and published to Zendesk. Zendesk will not serve the consumer support site, and content sitting in Zendesk is not available to Fin.
- Options were a service that posts content into Fin, or the new GitHub sync offering. Care already built GitHub sync.
- Decision: content lives in a GitHub repo and syncs directly to consumer interfaces, decoupling content from third-party platforms like Zendesk.
- Umang: GitHub gives access control, which matters for internal launches where content must not be public.
- Zendesk stays in place for the merchant side until next summer. Care is separately working out the consumer-side replacement plan.
- Philip and Seb built an automated content pipeline. The tech writing team already has much of the machinery. Next step is filling MVP gaps and testing with V2 content.

**Design timeline and scope**

- Charlie needs scope visibility for his engineering team within the next month.
- Umang expects core features (chat, forms) in good shape for review in 2-3 weeks. Comp analysis is done; the differentiating work is picking up context in different places.
- Nikhil, Jithin and Philip run a design jam the following day covering care considerations on the end-to-end consumer flow, benchmarked against competitors.

**Scope of "care"**

- Definition deliberately widened. From a consumer's point of view, care means "I need support with anything", so flows must not be bounded by Checkout's internal ownership lines.
- Some paths route outside Care (fraud, AML, risk), which is why Fabio's team matters. Brian joins future sessions as optional for the AML perspective.

**Fin widget constraints**

- V1 uses the existing Intercom Fin Messenger widget. Customisation is limited to avatar, icon, colours, and dark/light mode.
- Charlie is considering an abstraction/wrapper layer but the customisation impact is unknown.
- Georgios raised this explicitly so the design jam does not produce something unbuildable.
- V1 escalation is an asynchronous ticket flow triggered on defined conditions, not live chat handoff.

**Consumer agent toolkit**

- Georgios has a task to design it and has not started. Charlie will pick it up with him, likely looping in Joel for scoping. This group is the review forum for the designs.
- Umang pushed on agent experience, not just user experience: acting on behalf of a user (e.g. terminating an account) is a materially different problem from advising them. Amelia and Paloma cover payment queries; other areas such as risk platform access are unmapped.
- Umang's reality check: there will be no single system for all of this. Account suspension happens in Array, not at consumer level. Joel and Gabby have started a spreadsheet mapping each control to the system that will execute it.
- Charlie's counter-vision: consolidate into one permissioned system so it is less fragmented and easier to see who does what.

**Data requirements**

- The data requirements document is the master source for scope. Application-layer modelling follows from it.
- Braavos owns the data and services. The Care shell cannot modify data without permissioning.
- Umang will schedule a dedicated data requirements session once Eugenia is back from leave, walking through each scenario and the agent experience the same way they walk through user experience.

## Insights

- Two hard V1 constraints to design and scope against: Fin Messenger widget customisation is cosmetic only, and escalation is async ticket-based, not live handoff.
- Content strategy is now platform-agnostic by decision. That decouples the consumer content roadmap from the Zendesk replacement timeline, where merchant Zendesk runs to next summer.
- The agent-side toolkit is the least-scoped and highest-risk piece. Nobody has designed it, actioning on behalf of consumers spans multiple systems (Array for suspensions), and the only current artefact is Joel and Gabby's control-to-system spreadsheet.
- The data requirements document being the single master source governs everything downstream. If a control or use case is missing there, it will be missing from the app.
