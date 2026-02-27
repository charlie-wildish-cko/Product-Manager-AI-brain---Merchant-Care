# Common Payment Issues

> This document catalogs typical payment processing issues that surface through customer support, their causes, and resolution approaches.

## Integration Issues

### Authentication Errors

**Symptoms**:
- 401 Unauthorized responses
- "Invalid API key" errors
- "Signature validation failed"

**Common Causes**:
- Using test API keys in production (or vice versa)
- API key not properly configured in headers
- Secret key exposed in client-side code (security risk!)
- Key was rotated but merchant didn't update

**Resolution**:
- Verify correct API keys for environment
- Check authentication headers format
- Regenerate keys if compromised
- Review integration documentation

### Webhook Issues

**Symptoms**:
- Merchant not receiving payment notifications
- Duplicate webhook events
- Webhook signature validation failing

**Common Causes**:
- Incorrect webhook URL configured
- Endpoint not publicly accessible (localhost, firewall)
- Not responding with 200 OK quickly enough (timeout)
- Signature verification logic incorrect
- Not handling retries properly (duplicates)

**Resolution**:
- Verify webhook URL is correct and accessible
- Test endpoint with webhook testing tool
- Implement idempotency handling
- Review signature verification code
- Ensure quick response (defer processing)

### API Request Errors

**Symptoms**:
- 400 Bad Request
- "Missing required field" errors
- "Invalid format" errors

**Common Causes**:
- Missing required parameters
- Wrong data types (string instead of number)
- Invalid values (expired date, negative amount)
- API version mismatch

**Resolution**:
- Review API documentation for required fields
- Validate request payload format
- Check API version being used
- Use API sandbox for testing

## Payment Processing Issues

### High Decline Rates

**Symptoms**:
- Large percentage of payments rejected
- "Card declined" errors
- Frustrated merchants reporting lost sales

**Common Causes**:
- Fraud rules too strict
- Insufficient funds (customer issue)
- Card expired or invalid
- Incorrect billing information
- 3DS/SCA authentication failing
- Issuer-side issues

**Resolution**:
- Analyze decline reasons (soft vs hard declines)
- Review and adjust fraud rules
- Implement retry logic for soft declines
- Add more payment methods
- Improve checkout UX for card entry
- Merchant education on common customer issues

### Settlement Delays

**Symptoms**:
- Merchant expecting funds but not received
- Payouts not arriving on schedule
- Discrepancies between captured amount and settled amount

**Common Causes**:
- Hold or reserve on account (risk-based)
- Bank details incorrect or verification pending
- Holiday or weekend (no settlement processing)
- Recent chargebacks or disputes
- Account under review

**Resolution**:
- Check account status and holds
- Verify bank details are correct
- Review settlement schedule
- Check for recent disputes
- Escalate to finance team if discrepancy

### Transaction Timeouts

**Symptoms**:
- Payment requests taking too long
- "Request timeout" errors
- Payment status unclear (succeeded or failed?)

**Common Causes**:
- Issuer bank slow to respond
- Network connectivity issues
- 3DS authentication taking too long
- High system load

**Resolution**:
- Implement proper timeout handling
- Use idempotency keys to prevent duplicates
- Query transaction status endpoint
- Implement retry logic with backoff
- Monitor and alert on timeout rates

### Failed Captures

**Symptoms**:
- Authorization successful but capture fails
- "Authorization expired" errors
- "Insufficient funds" on capture

**Common Causes**:
- Too much time between auth and capture (>7 days typically)
- Funds no longer available
- Card was canceled after authorization
- Partial capture for more than authorized

**Resolution**:
- Capture sooner after authorization
- Implement authorization extension if needed
- Better inventory management to avoid delays
- Clear communication with customers about holds

## Refund & Dispute Issues

### Refund Processing Problems

**Symptoms**:
- Refund requests failing
- Customer says refund not received
- Refund taking longer than expected

**Common Causes**:
- Original transaction not yet settled
- Insufficient balance in merchant account
- Incorrect refund amount (exceeds original)
- Card expired or closed since original payment

**Resolution**:
- Wait for settlement before refunding
- Verify merchant account balance
- Check refund amount vs original transaction
- Customer may need to contact their bank
- Typical timing: 5-10 business days

### Chargeback Management

**Symptoms**:
- Customer disputed charge with bank
- Funds reversed from merchant account
- Chargeback fees applied

**Common Causes**:
- Fraud (unauthorized transaction)
- Customer doesn't recognize charge
- Product not received or not as described
- Subscription not canceled as requested
- Duplicate charge

**Resolution**:
- Merchant provides evidence (proof of delivery, customer communications)
- Review fraud indicators on original transaction
- Improve billing descriptor for recognition
- Better customer service to resolve before chargeback
- Clear cancellation process for subscriptions

## Account & Access Issues

### Dashboard Access Problems

**Symptoms**:
- Can't log in to merchant dashboard
- Password reset not working
- Multi-factor authentication issues
- "Account locked" messages

**Common Causes**:
- Forgotten password
- Too many failed login attempts (account locked)
- MFA device lost or changed
- Email address changed
- Account permissions issue

**Resolution**:
- Standard password reset flow
- Account unlock after verification
- MFA reset with proper identity verification
- Update email address with authentication
- Review user roles and permissions

### User Management

**Symptoms**:
- Can't add new users
- Users don't have proper permissions
- Former employee still has access

**Common Causes**:
- Insufficient permissions to manage users
- User limit reached on account plan
- Incorrect role assigned
- No offboarding process

**Resolution**:
- Verify admin permissions
- Check account plan limits
- Review and assign correct roles
- Implement user audit and offboarding process

## Reporting & Reconciliation Issues

### Reporting Discrepancies

**Symptoms**:
- Transaction report totals don't match expectations
- Missing transactions in reports
- Settlement report doesn't match bank deposit

**Common Causes**:
- Timezone differences in date filters
- Refunds or chargebacks deducted
- Fees not accounted for
- Report filtered incorrectly
- Looking at different time periods (capture vs settlement)

**Resolution**:
- Use UTC timezone consistently
- Account for refunds and fees
- Compare capture date vs settlement date reports
- Use transaction ID to trace specific discrepancies
- Provide reconciliation guide

### Data Export Issues

**Symptoms**:
- Can't export transaction data
- Export file incomplete or corrupted
- Export taking too long or timing out

**Common Causes**:
- Date range too large
- Too many records to export
- File format issue
- Browser timeout

**Resolution**:
- Break into smaller date ranges
- Use API for large data exports
- Try different file format
- Provide direct database export for large volumes

## Pattern Identification

### When Support Should Escalate

**Red Flags**:
- Same issue reported by multiple merchants
- Issue appeared after recent deployment
- Error rates suddenly increasing
- Specific merchant segment affected (e.g., all using certain feature)
- Workaround exists but root cause unclear

**Escalation Path**:
1. Document pattern with specific examples
2. Include error rates and merchant impact
3. File bug report with engineering
4. Alert product management if significant impact
5. Prepare merchant communication if needed


**Last Updated**: [Date]
**Owner**: Charlie Wildish

**Note**: This document should be updated regularly as new patterns emerge from support tickets.
