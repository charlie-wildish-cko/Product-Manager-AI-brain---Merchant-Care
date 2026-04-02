# Taxonomy Change Mapping: Old → New

**Purpose**: Reference for updating Zendesk fields and values.
**Source files**: `Taxonomy - ZD work - Case & Issue Type - References.csv` (old) · `Taxonomy - ZD work - New taxonomy.csv` (new)

**Structural change**: Old = 2 levels (Case Type → Issue Type). New = 3 levels (Case Type → Issue Type → Reason). A new **Reason** field must be created in Zendesk.

**Change types**: Renamed · Merged · Moved · New · Retired · Confirm (no clear equivalent — agree treatment before updating)

---

| Old Case Type | Old Issue Type | Old Tag | New Case Type | New Issue Type | New Reason | Change |
|---|---|---|---|---|---|---|
| Transactions | Payment confirmation | case_transactions_issue_status_proof | Payments in | Transaction status (non 3DS & refunds) | Stuck in status / status enquiry | Renamed + Moved |
| Transactions | Proof of payment | case_transactions_issue_refund_proof_schemes | Payments in | Transaction status (non 3DS & refunds) | Proof of payment (ARN, RNN, bulk) | Renamed + Moved |
| Transactions | Authorization failed | case_transactions_issue_authorization_failure | Payments in | Transaction status (non 3DS & refunds) | Declined / failed action | Renamed + Moved |
| Transactions | Void failed | case_transactions_issue_unable_to_void_payment | Payments in | Transaction status (non 3DS & refunds) | Declined / failed action | Merged + Moved |
| Transactions | Capture failed | case_transactions_issue_unable_to_capture_payment | Payments in | Transaction status (non 3DS & refunds) | Declined / failed action | Merged + Moved |
| Transactions | Customer charged after payment expired | case_transactions_issue_customer_charged_after_payment_expired | Payments in | Transaction status (non 3DS & refunds) | Failed but customer charged | Renamed + Moved |
| Transactions | Customer charged twice | case_transactions_issue_duplicate_transactions | Payments in | Transaction status (non 3DS & refunds) | Customer charged twice | Moved |
| Transactions | Refund failed | case_transactions_issue_refund | Payments in | Refunds | Refund failed / manual refund | Renamed + Moved |
| Transactions | Refund or payout reversal | case_transactions_issue_incorrect_refund | Payments in | Refunds | Refund reversal | Renamed + Moved |
| Transactions | Disputes | case_transactions_issue_dispute | Payments in | Disputes / chargebacks | Dispute status | Renamed + Moved |
| Transactions | All payments failed | case_transactions_issue_all_transactions_failing | Payments in | Performance | All payments failing | Moved |
| Transactions | Payout pending or declined | case_transactions_issue_payout_pending_or_declined | Payouts | Bank payouts | Declined / failed bank payout | Moved to new case type |
| Transactions | Other | case_transactions_issue_other | — | — | — | Retired |
| — | — | — | Payments in | Transaction status (non 3DS & refunds) | Missing or unrecognised transaction | New |
| — | — | — | Payments in | Refunds | Refund proof | New |
| — | — | — | Payments in | Refunds | Refund status enquiry | New |
| — | — | — | Payments in | Authentication (3DS) | Liability shift status | New |
| — | — | — | Payments in | Disputes / chargebacks | Dispute adjustment | New |
| — | — | — | Payments in | Disputes / chargebacks | Evidence help and submission | New |
| — | — | — | Payments in | Fraud & risk controls | AVS / CVV mismatch | New |
| — | — | — | Payments in | Fraud & risk controls | Velocity limit reached | New |
| — | — | — | Payments in | Performance | Acceptance rate issue / optimisation | New (merged from Acceptance rate case type) |
| — | — | — | Payouts | Bank payouts | Proof of bank payout | New |
| — | — | — | Payouts | Bank payouts | Bank payout stuck in pending or status inquiry | New |
| — | — | — | Payouts | Bank payouts | Bank payout returns | New |
| — | — | — | Payouts | Card payouts | Card payout stuck in pending or status inquiry | New |
| — | — | — | Payouts | Card payouts | Declined / failed card payout | New |
| — | — | — | Payouts | Card payouts | Proof of card payout | New |
| — | — | — | Payouts | Card payouts | Card payout reversal | New |
| 3D Secure (3DS) issues | 3DS authentication failed | case_3ds_issue_response_code_20151_-_20156 | Payments in | Authentication (3DS) | 3DS decline | Moved to Payments in |
| 3D Secure (3DS) issues | 3DS Page not loading | case_3ds_issue_page_not_loading | Payments in | Authentication (3DS) | 3DS decline | Moved to Payments in |
| 3D Secure (3DS) issues | 3DS exemptions | case_3ds_issue_3ds_exemptions | Payments in | Authentication (3DS) | SCA / exemption issue | Moved to Payments in |
| 3D Secure (3DS) issues | Unintended 3DS upgrade | case_3ds_issue_unintended_3ds_upgrade | Payments in | Authentication (3DS) | SCA / exemption issue | Moved to Payments in |
| 3D Secure (3DS) issues | 3DS integration | case_3ds_issue_sdk_integration | Payments in | Authentication (3DS) | 3DS decline | Moved to Payments in |
| 3D Secure (3DS) issues | 3DS test card issues | case_3ds_issue_issues_with_test_cards_sandbox | Technical issue | Environment | Sandbox issue | Moved to Technical issue |
| 3D Secure (3DS) issues | Other | case_3ds_issue_other | — | — | — | Retired |
| Fraud detection | Risk strategy/ rules | case_fraud_issue_decline_list_risk_rules | Payments in | Fraud & risk controls | Risk rules | Moved to Payments in |
| Fraud detection | Risk lists | case_fraud_issue_whitelist | Payments in | Fraud & risk controls | Trustlist & decline list | Moved to Payments in |
| Fraud detection | Risk declines | case_fraud_issue_risk_declines | Payments in | Fraud & risk controls | Risk rules | Moved to Payments in |
| Fraud detection | Fraud Performance | case_fraud_issue_fraud_performance | Payments in | Fraud & risk controls | Risk rules | Moved to Payments in |
| Fraud detection | Other | case_fraud_issue_other | — | — | — | Retired |
| Acceptance rate | Low Approval Rate | case_acceptance_performance_low_approval_rate | Payments in | Performance | Acceptance rate issue / optimisation | Moved to Payments in |
| Acceptance rate | Intelligent Acceptance | case_acceptance_performance_intelligent_acceptance | Payments in | Performance | Acceptance rate issue / optimisation | Moved to Payments in |
| Acceptance rate | Other | case_acceptance_performance_other | — | — | — | Retired |
| Settlements, invoices and fees | Settlement not received | case_settlements_issue_settlement_not_received | Funds and fees | Settlements | Delayed / missing settlement | Renamed |
| Settlements, invoices and fees | Payment not settled | case_settlements_issue_have_i_been_settled_for_this_payment | Funds and fees | Settlements | Delayed / missing settlement | Renamed + Merged |
| Settlements, invoices and fees | Reconciliation mismatch | case_settlements_issue_mismatch_in_reconciliation | Funds and fees | Settlements | Reconciliation issue | Renamed |
| Settlements, invoices and fees | Balance confirmation | case_settlements_issue_balance_confirmation | Funds and fees | Balance | Balance confirmation | Renamed |
| Settlements, invoices and fees | Transfer or hold of funds | case_settlements_issue_transfer_or_hold_of_funds | Funds and fees | Balance | Balance explanation | Renamed |
| Settlements, invoices and fees | Invoice requests | case_settlements_issue_general_adjustments | Funds and fees | Billing & fees | Invoice request | Renamed |
| Settlements, invoices and fees | Adjustments and fees | case_settlements_issue_fees_charged_for_transaction | Funds and fees | Billing & fees | Fee inquiry | Renamed |
| Settlements, invoices and fees | Other | case_settlements_issue_other | — | — | — | Retired |
| — | — | — | Funds and fees | Balance | Negative balance | New |
| — | — | — | Funds and fees | Balance | Balance top up | New |
| Integration issues | Access or API keys | case_integration_issue_access_and_api_keys_issues | Technical issue | API credentials | Create / edit keys | Renamed |
| Integration issues | API or payload error | case_integration_issue_api | Technical issue | API integration | API error 4XX / logic error | Renamed |
| Integration issues | Webhooks | case_integration_issue_webhook_not_working | Technical issue | Webhooks | Webhook setup | Renamed |
| Integration issues | SDK integration | case_integration_issue_sdk_integration | Technical issue | Integration methods | SDK issue | Renamed |
| Integration issues | Ecommerce plugins | case_integration_issue_ecommerce_integration | Technical issue | Integration methods | E-commerce plugin | Renamed |
| Integration issues | Flow or frames | case_integration_issue_flow | Technical issue | Integration methods | Flow / frames | Renamed |
| Integration issues | HPP or payment links | case_integration_issue_hosted_payment_page | Technical issue | Integration methods | Payment links / hosted payment pages | Renamed |
| Integration issues | Network token requests | case_integration_issue_network_token_requests | Technical issue | Tokens | Network tokens | Renamed |
| Integration issues | Token migration | case_integration_issue_token_migration | Technical issue | Tokens | Token migration | Renamed |
| Integration issues | Test data errors (sandbox) | case_integration_issue_test_account_error | Technical issue | Environment | Sandbox issue | Renamed |
| Integration issues | SFTP requests | case_integration_issue_sftp_requests | Data and analytics | Reporting | SFTP configuration | Moved to Data and analytics |
| Integration issues | Other | case_integration_issue_other | — | — | — | Retired |
| — | — | — | Technical issue | API credentials | Key scopes | New |
| — | — | — | Technical issue | API integration | API error 5XX | New |
| — | — | — | Technical issue | API integration | Idempotency / timeout | New |
| — | — | — | Technical issue | Integration methods | Apple Pay / Google Pay | New |
| — | — | — | Technical issue | Webhooks | Signature verification or delivery failure | New |
| — | — | — | Technical issue | Webhooks | Missing webhook data | New |
| Reports | Custom reports | case_reports_issue_custom_report_needed | Data and analytics | Reporting | Custom report request | Renamed |
| Reports | Data mismatch | case_reports_issue_mismatch_missing_data | Data and analytics | Reporting | Data mismatch / missing | Renamed |
| Reports | Report not generated | case_reports_issue_report_not_generated | Data and analytics | Reporting | Report not generated / missing | Renamed |
| Reports | Downloading reports | case_reports_issue_downloading_reports | Data and analytics | Reporting | — | Absorbed into Reporting |
| Reports | Report insights | case_reports_issue_report_insights | Data and analytics | Reporting | — | Absorbed into Reporting |
| Reports | Other | case_reports_issue_other | — | — | — | Retired |
| — | — | — | Platforms | Sub-merchant onboarding | Merchant activation and verification | New |
| — | — | — | Platforms | Sub-merchant onboarding | Doc upload error | New |
| — | — | — | Platforms | Transfers & splits | Transfer or split failed | New |
| Access and permissions | Unable to log in | case_access_issue_account_locked_out | Account management & access | Login & access | Login error / MFA / SSO | Renamed + Merged |
| Access and permissions | Single sign-on (SSO) | case_access_issue_sso | Account management & access | Login & access | Login error / MFA / SSO | Merged |
| Access and permissions | User management | case_access_issue_issue_with_adding_or_remove_user | Account management & access | Login & access | User permissions | Renamed + Merged |
| Access and permissions | Permissions | case_access_issue_change_permissions | Account management & access | Login & access | User permissions | Merged |
| Access and permissions | Dashboard error | case_access_issue_dashboard_error | Account management & access | Login & access | Dashboard error | Renamed |
| Access and permissions | Status page | case_access_issue_status_page | — | — | — | Confirm |
| Access and permissions | Other | case_access_issue__other | — | — | — | Retired |
| Configuration Changes | Pricing change request | case_configuration_issue_pricing_plan_changes | Account management & access | Account changes | Pricing change | Renamed + Merged |
| Configuration Changes | Terminations | case_configuration_issue_account_termination_related | Account management & access | Account changes | Terminations | Merged |
| Configuration Changes | Account settings change | case_configuration_issue_operational_change_request | Account management & access | Account changes | Account settings update | Renamed + Merged |
| Configuration Changes | Enable account feature | case_configuration_issue_enable_account_feature | — | — | — | Confirm |
| Configuration Changes | Sandbox change request | case_configuration_issue_sandbox_change_request | — | — | — | Confirm |
| Configuration Changes | Other | case_configuration_issue_other | — | — | — | Retired |
| — | — | — | Account management & access | Login & access | Dashboard user audit evidence | New |
| Request for documentation | Audit requests | case_rfd_issue_audit_requests | Compliance & audit | Compliance evidence | Audit request | Renamed |
| Request for documentation | PCI requests, contracts and pricing | case_rfd_issue_pci_dss_docs | Compliance & audit | Compliance evidence | PCI / AOC request | Renamed |
| Request for documentation | Other | case_rfd_issue_other_documents | Compliance & audit | Other compliance | Other compliance docs | Renamed |
| Request for documentation | Additional Customer Information | case_rfd_issue_additional_customer_information | — | — | — | Confirm |
| — | — | — | Compliance & audit | Compliance evidence | Sensitive data request | New |
| General enquiry | New feature request | case_feedback_new_feature_requests | Feedback | Product feedback | Feature request | Renamed |
| General enquiry | Existing feature insights | case_feedback_existing_feature_insights | Feedback | Product feedback | Feature usage | Renamed |
| General enquiry | Account configuration details | case_feedback_account_configuration_details | — | — | — | Confirm |
| General enquiry | Update contact details | case_feedback_update_contact_details | — | — | — | Confirm |
| General enquiry | Planned outages | case_feedback_planned_outages | — | — | — | Confirm |
| General enquiry | Other | case_feedback_other | — | — | — | Retired |
| No action required | No action required by Merchant Care | case_no_action_required_issue_by_merchant_care | General | Inquiries | Spam / duplicate / no action / follow ups | Merged |
| No action required | Duplicate | case_no_action_required_issue_duplicate | General | Inquiries | Spam / duplicate / no action / follow ups | Merged |
| No action required | Spam | case_no_action_required_issue_spam | General | Inquiries | Spam / duplicate / no action / follow ups | Merged |
| No action required | Sales Enquiry | case_no_action_required_issue_sales_enquiry | General | Inquiries | Sales inquiry | Renamed + Merged |
| Card issuing | Create or activate card | case_issuing_create_or_activate_card | Card issuing | Card management | Create / activate card | Renamed |
| Card issuing | Manage card | case_issuing_manage_card | Card issuing | Card management | — | Absorbed into Card management |
| Card issuing | Revoke or suspend cards | case_issuing_revoke_or_suspend_cards | Card issuing | Card management | Revoke / suspend | Renamed |
| Card issuing | Physical cards | case_issuing_physical_cards | Card issuing | Logistics | Physical card delivery | Renamed |
| Card issuing | Reporting and invoices | case_issuing_reporting_and_invoices | Card issuing | Issuing transactions, money & reports | Issuing fees | Renamed |
| Card issuing | Funding currency account | case_issuing_funding_currency_account | Card issuing | Issuing transactions, money & reports | Issuing balance | Renamed |
| Card issuing | Card security | case_issuing_card_security | — | — | — | Confirm |
| Card issuing | Refund delays | case_issuing_refund_delays | — | — | — | Confirm |
| Card issuing | Payment declines | case_issuing_payment_declines | — | — | — | Confirm |
| Card issuing | Card fraud | case_issuing_card_fraud | — | — | — | Confirm |
| Card issuing | Other | case_issuing_other | — | — | — | Retired |
| — | — | — | Card issuing | Card management | Spend controls | New |
| — | — | — | Card issuing | Issuing digital wallets | Apple Pay / Google Pay | New |
| — | — | — | Card issuing | Mobile app / SDK | Issuing SDK integration / upgrade | New |
| — | — | — | Card issuing | Issuing transactions, money & reports | Issuing balance | New |
| — | — | — | Card issuing | Issuing transactions, money & reports | Issuing settlement & reconciliation | New |
| — | — | — | Card issuing | Issuing transactions, money & reports | Issuing transaction declined / unexpected behavior | New |
| Identity Verification | Verification Inquiry | case_idv_issue_idv | Identity verification | Verification and technical support | Verification inquiry | Renamed (casing) |
| Identity Verification | Technical & Platform | case_idv_issue_tech | Identity verification | Verification and technical support | Technical & platform | Renamed (casing) |
| Identity Verification | Setup Support | case_idv_issue_setup_support | Identity verification | Verification and technical support | Setup support | Renamed (casing) |
| Identity Verification | Account & Compliance | case_idv_issue_account_management | Identity verification | Security, privacy and compliance | Account & compliance | Renamed (casing) |
| Identity Verification | Data Privacy | case_idv_issue_data_privacy | Identity verification | Security, privacy and compliance | Data privacy | Renamed (casing) |
| Identity Verification | Formal Complaint | case_idv_issue_formal_complaint | Identity verification | Formal complaint | Formal complaint | Renamed (casing) |
| Identity Verification | N/A::3rd Party | case_idv_issue_na_3rd_party | Identity verification | N/A | 3rd party | Renamed (casing) |
| Identity Verification | N/A::Automated | case_idv_issue_na_automated | Identity verification | N/A | Automated | Renamed (casing) |
| Identity Verification | N/A::Follow Up | case_idv_issue_na_follow_up | Identity verification | N/A | Follow up | Renamed (casing) |
| Identity Verification | N/A::Sales Lead | case_idv_issue_na_sales_lead | Identity verification | N/A | Sales lead | Renamed (casing) |
| Identity Verification | N/A::Self Resolved | case_idv_issue_na_self_resolved | Identity verification | N/A | Self resolved | Renamed (casing) |
| Identity Verification | N/A::Spam | case_idv_issue_na_spam | Identity verification | N/A | Spam | Renamed (casing) |
| — | — | — | Identity verification | Security, privacy and compliance | Security | New |
| Non-merchant requests | Cardholder Complaints | case_nmr_issue_cardholder_complaints | — | — | — | Confirm |
| Non-merchant requests | Issuing Bank Requests | case_nmr_issue_issuing_bank_requests | — | — | — | Confirm |
| Non-merchant requests | Authorities | case_nmr_issue_authorities | — | — | — | Confirm |
| Non-merchant requests | Schemes | case_nmr_issue_schemes | — | — | — | Confirm |
| Non-merchant requests | TPA Requests | case_nmr_issue_tpa_requests | — | — | — | Confirm |
| Non-merchant requests | Other | case_nmr_issue_other | — | — | — | Confirm |
