

# **Merchant Care Requirement Document**

CheckOut

Exported on 2025-03-27 17:56:52

**Table of Contents**

**1	Key Stakeholders and Roles DISCOVERY WORKSHOP	[3](#key-stakeholders-and-roles-discovery-workshop)**

**2	Requirements and Functional Needs	[4](#requirements-and-functional-needs)**

**3	Integration Requirements DISCOVERY WORKSHOP	[7](#integration-requirements-discovery-workshop)**

1. # **Key Stakeholders and Roles DISCOVERY WORKSHOP** {#key-stakeholders-and-roles-discovery-workshop}

This section outlines the key stakeholders from the client teams, along with their roles and responsibilities in the discovery and design process.

| Name | Role |
| :---- | :---- |
| Charlie Wildish | Merchant Care |
| Oliver Westlake-Simm | Merchant Care |
| Ramyaa Ranganathan | Engineering Team |
| Marianne Vanlaecke | IT |
| Gareth Thomas | IT |

2. # **Requirements and Functional Needs** {#requirements-and-functional-needs}

This section outlines the functional and technical requirements to be addressed during the implementation, prioritised based on each workstream and team.

| Area | Requirement Category | Description | Owner | Question | Priority (To be completed by the Client) high   medium   low  |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **Merchant Care Process** | **Integration** | Would like to have agents to only rely on Zendesk for their work. Any information coming from Jira can also be viewed in Zendesk. This would help resolve the need for agents logging into 2 systems. Fields that will be sent to JSM Summary (Static) Description (Static) Priority (Static) SLA (Static) Comments (Bi-Directional) Client ID (Static) Client Name (Static) Teams (Jira to Zendesk) | Oliver | **Ramya**: Can you please share the current fields captured in Fresh Service. | ** high ** |
| **Merchant Care Process** | **SLA** | Would like to track the SLA in Zendesk as Static field in Jira as it will help the engineering team prioritise their work. Only time to resolution is tracked for now. Jira will have its own SLA’s (TBC) for Engineering teams | Ramyaa |  |  |
| **Merchant Care Process** | **Integration** | All comments from Jira to Zendesk will be displayed as an internal note. Merchant care agents will manually copy these internal notes to external notes if the customer needs to be updated. | Oliver |  |  |
| **Merchant Care Process** | **Integration** | Would like to be able to create a comment in Jira via Zendesk. This allows for ease of communication between Merchant Care and Engineering team. | Oliver |  |  |
| **Merchant Care Process** | **JSM** | Have a dedicated Jira project for the engineering team to manage merchant care tickets. This project can have multiple teams and the SLA for the tickets in this project will be carried over if the tickets are assigned to another team within the project. | Marianne |  |  |
| **Merchant Care Process** | **Integration** | When a ticket is closed in Zendesk, automatically close the ticket in Jira. | Ramyaa |  |  |
| **Merchant Care Process** | **Integration** | If there is a JSM ticket that would end up as a bug in Jira Software, Zendesk would also like to be able to track the progress of this bug ticket. | Oliver |  |  |
| **Merchant Care Process** | **Reporting** | Would like to be able to view reports on the Jira tickets that are created from Merchant Care. | Ramyaa |  |  |

3. # **Integration Requirements DISCOVERY WORKSHOP** {#integration-requirements-discovery-workshop}

This section identifies the tools and systems that must be integrated with JSM to ensure seamless operations.

 

| System/Tool | Integration Type | Purpose | Notes |
| :---- | :---- | :---- | :---- |
| **Zendesk** | Bi-directional | Create Jira tickets for the Engineering team to work on and track the progress of these tickets. | Relationship between Zendesk tickets to Jira tickets are One-to-One or Many-to-One. Zendesk manually triggers the Jira tickets creation. Zendesk tickets can also link to an existing Jira tickets. Comments are manually added from Zendesk to Jira. |
| **Slack** | One-directional | When a Jira ticket is created, would like to receive a slack notification for the ticket together with information on some specific Jira fields. | Would also like to separate these notifications based on products into separate channels.(TBC) |

