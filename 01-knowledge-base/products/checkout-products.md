# Checkout.com Products & Services

> For full business context, company overview, and product details sourced from the public website, see `01-knowledge-base/checkout-business-context.md`. This file is for internal product detail you add over time.

## Core Payment Products

### Payment Gateway
- **Description**: Core payment processing infrastructure
- **Key Features**:
  - Multi-currency support
  - Multiple payment methods (cards, wallets, local payments)
  - Real-time authorization and settlement
  - Smart payment routing
  - Fraud detection and risk management
- **Use Cases**: E-commerce, marketplaces, subscription businesses
- **Documentation**: [Link to internal/external docs]

### Payment APIs
- **REST API**: Modern API for payment integration
- **Checkout SDK**: Client-side payment collection
- **Server SDKs**: Libraries for various programming languages
- **Webhooks**: Event notifications for payment updates

### Payment Methods Supported
- **Cards**: Visa, Mastercard, Amex, Discover, etc.
- **Digital Wallets**: Apple Pay, Google Pay, PayPal
- **Alternative Payment Methods**: Local payment methods by region
- **Bank Transfers**: Direct debit, SEPA, ACH

## Value-Added Services

### Fraud & Risk Management
- Real-time fraud detection
- Customizable risk rules
- 3D Secure / SCA support
- Chargeback protection

### Reporting & Analytics
- Transaction reporting
- Settlement reports
- Analytics dashboard
- Custom report generation

### Merchant Dashboard
- Self-service portal for merchants
- Transaction search and details
- Configuration management
- User and permission management
- **Support Ticket Inbox**: Merchants can view, filter, and reply to their Zendesk support tickets directly within the Dashboard (see below)

## Customer Support Tools

### Internal Tools
**Ticketing & Case Management**:
- **Zendesk**: Primary ticketing system for all support contacts
  - Email tickets from support@checkout.com
  - Dashboard webform submissions
  - Escalated cases from Intercom Fin AI Agent

**Investigation & Troubleshooting**:
- Merchant lookup tools
- Transaction investigation dashboards
- Log access and debugging tools
- Internal knowledge base

### Merchant-Facing Tools

**AI & Automated Support**:
- **Intercom Fin AI Agent**: In-dashboard AI assistant
  - First line of support for merchant questions
  - Resolves queries without human intervention when possible
  - Seamless handoff to Zendesk when escalation needed
  - Key metric: AI resolution rate

**Self-Service Resources**:
- **support.checkout.com**: 
  - FAQs and help articles
  - Step-by-step guides
  - Common issue troubleshooting
  - Best for: General product questions, onboarding help
  
- **checkout.com/docs**: 
  - Technical and integration documentation
  - Implementation guides
  - Best practices
  - Best for: Developers integrating Checkout.com
  
- **api-reference.checkout.com**: 
  - API endpoint specifications
  - Request/response examples
  - Authentication guides
  - Best for: Technical API implementation details

**Support Ticket Inbox (Merchant Dashboard)**:
- Dedicated page within the merchant Dashboard for viewing and managing support tickets
- Integrated with Zendesk, linked to the merchant's account as the requester
- Surfaces tickets from all inbound channels: email, Dashboard webform, and Fin AI Agent escalations
- Merchants can filter tickets by status (e.g. open, pending, solved)
- Merchants can reply to tickets directly from the Dashboard without leaving to email
- Provides a single self-service hub for tracking the status of ongoing support cases

**Contact Channels**:
- **Dashboard Webform**: Structured support form
  - Fields: Topic, Subject, Payment ID, Description
  - Routes to Zendesk
  - Provides context for faster resolution
  
- **Email**: support@checkout.com
  - Traditional support channel
  - Routes to Zendesk

## Product Roadmap Areas

### Current Focus (2026)
**Support Experience - B2B Optimization**:
- [ ] Reduce contact rate per 1M transactions
- [ ] Improve AI Agent resolution rate
- [ ] Root cause elimination for top contact drivers
- [ ] Agent efficiency tools and automation
- [ ] Enhanced self-service documentation

**Core Product Improvements**:
- [ ] Enhancing fraud detection capabilities
- [ ] Expanding payment method coverage
- [ ] Improving merchant self-service tools
- [ ] Analytics and reporting enhancements

### Future Focus (2027+)
**B2C Support Expansion**:
- [ ] Mobile support channel
- [ ] Phone support channel
- [ ] Consumer-focused help resources
- [ ] Scaled AI capabilities for higher volume
- [ ] Multi-language support
- [ ] Consumer payment dispute handling

## Common Product Questions

> Add FAQs as they come up:

**Q: How long does settlement take?**
A: [Add answer based on actual timing]

**Q: What currencies are supported?**
A: [Add list of supported currencies]

**Q: How are disputes handled?**
A: [Add dispute resolution process]


**Last Updated**: [Date]
**Owner**: Charlie Wildish
