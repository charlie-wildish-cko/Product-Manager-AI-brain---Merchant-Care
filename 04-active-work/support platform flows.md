# Support platform flows we want by 2030

Support platform = the platform human agents work from and everything connects to. Today in 2026, its Zendesk.

Desired platform architecture: modular, flexible and lets us plug in our data, AI agents and other services without building for the platform - we build around the platform.

## Entry points into the platform & AI involvement

We will support these channels, which are defined by the success plans:

B2B

- Email from customers
- AI Agent with escalation path
- Live chat with human agent
- Instant messaging channels
- Phone
- Internal ticket submissions from our Account teams (e.g. Account manager)

B2C

- Mobile app chat
- Phone

We will apply an AI Agent on most of these as triage, before they reach a human agent. This is how we push to 80% ai resolution goal. Solved AI Agent chats then go into Reflex data.

We aim to auto classify any contact escalated to a human agent to our taxonomy for efficient routing.

## If AI Agent doesn't solve and routes to human agent

We expect the remaining volume of 20% to end up with a human agent to solve.

This is where the support platform kicks in as the primary agent interface. Therefore its goals are:

1. Create the ticket and enrich with the customer data
2. Read the classification and enable routing to matched skills for the human agent team (level 1)
3. Human agent gets assigned ticket, our Agent consultant suggests solutions to the agent - Runbook or Contextual support
4. Agent then approves the Consultant to act and complete task
5. Replies to customer
6. On occasion, the issue may need to go to another team, either the next Agent team (level 2) or another business team (e.g. Treasury) or an engineering team (e.g. Card processing). This would easily be done using an integration into their ticketing system and trackable in the support system ticket so the agent can update the customer.
7. On close of the ticket, the data gets passed into Reflex for analytics

## Routing logic in the support platform

Based on the support plan, which dictates the SLA and priority of the issue from the customer.

So we'd need:

1. Support plans/tier which dictate the SLA and priority levels
2. Customisable company and individual customer fields
3. a flexible tagging system to map our taxonomy and other use cases for analytics
4. SLAs which can map to taxonomy values
5. priority levels which map to taxonomy values
6. Customisable ticket fields

## Integrations to the platform

1. Custom apps which we can embed into the Agent UI to use, such as Agent consultant, which uses AI to intelligently solve tickets
2. We can present live customer data from our CRM and user data sources in the Agent UI
3. JIRA and custom API integrations to other systems to read/write into there for other team involvement in tickets
4. Data extract of ticket data over API to our analytics

## Numbers of agents & teams

Needs to support our B2B and B2C customers, which are virtually separated by the channels they contact us from and the agents who pick up the tickets in the platform. Consider this a walled permissions system, for example we may use a BPO for B2C who should never see B2B information in the platform.

We expect 500 agents in 2030 using this platform.

## **Support contact interaction experience**

Our customers:

- Visibility of their previous AI agent chats and chats with human agents
- Tickets page they can see support tickets picked up by humans

Checkout Account teams:

* Visibility of ticket threads between Checkout and customers
* Ability to reply to these threads over email and get updates on ticket progress

Checkout teams which we need to solve contacts:

* Can see ticket threads and leave internal comments
* Can see the metadata of the support ticket, the customer/priority etc
