# Process Analysis: Purchase Order Approval Process

## Executive Summary
The Purchase Order Approval process involves employees submitting purchase requests through an ERP procurement portal, followed by automated budget verification and multi-tier approvals based on purchase amount, procurement team review and vendor verification, and finally PO creation and vendor notification. The process involves 4-7 actors depending on the purchase amount and can take anywhere from 1 day to 3 weeks depending on complexity, approval delays, and vendor status.

## Process Steps

### Step 1: Submit Purchase Order Request
- **Actor/Role**: Employee (Requester)
- **Description**: Employee logs into procurement portal (ERP module) and completes request form with purchase details including item description, quantity, estimated cost, vendor name (if known), business justification, and budget code
- **Input**: Need to purchase item or service
- **Output**: Submitted PO request in procurement queue
- **Duration/Timing**: Not specified
- **Pain Points**: 20-25% of requests are incomplete when first submitted (missing product details, model numbers, vendor names, or vague business justification); requesters don't read provided checklists and guidelines; many requests submitted at month-end creating workload spikes

### Step 2: Automated Budget Verification
- **Actor/Role**: ERP System (automated)
- **Description**: System automatically checks the budget code entered against department's remaining budget to verify sufficient funds are available for the purchase
- **Input**: Submitted PO request with budget code
- **Output**: Budget verification pass/fail result
- **Duration/Timing**: Automated/immediate
- **Pain Points**: None mentioned for this specific step

### Step 2a: Budget Rejection (Exception Path)
- **Actor/Role**: ERP System (automated)
- **Description**: If insufficient budget, system automatically rejects the request and sends email notification to requester explaining insufficient budget
- **Input**: Failed budget verification
- **Output**: Rejected request with notification
- **Duration/Timing**: Immediate/automated
- **Pain Points**: None mentioned; this automated rejection is viewed positively as it saves procurement team time

### Step 3: Approval Routing (Tier 1 - Under $1,000)
- **Actor/Role**: Direct Manager
- **Description**: Manager receives email notification, logs into portal, reviews request, and approves
- **Input**: Budget-verified PO request under $1,000
- **Output**: Manager approval
- **Duration/Timing**: Same-day or next-day typically
- **Pain Points**: None mentioned for this tier

### Step 3: Approval Routing (Tier 2 - $1,000 to $10,000)
- **Actor/Role**: Direct Manager, then Department Head
- **Description**: Request requires sequential approval from both direct manager and department head; each receives email notification, logs into portal, and approves
- **Input**: Budget-verified PO request between $1,000 and $10,000
- **Output**: Manager and Department Head approvals
- **Duration/Timing**: 2-3 days typically
- **Pain Points**: Delays occur when either approver is out of office or busy; sequential nature means one delay holds up the entire process

### Step 3: Approval Routing (Tier 3 - Over $10,000)
- **Actor/Role**: Direct Manager, Department Head, and Finance
- **Description**: Request requires sequential approval from manager, department head, and Finance department
- **Input**: Budget-verified PO request over $10,000
- **Output**: Manager, Department Head, and Finance approvals
- **Duration/Timing**: 3-5 days, sometimes up to a week
- **Pain Points**: Finance approvals create significant bottleneck - only two people authorized to approve, they handle multiple types of approvals (expense reports, invoices, POs), POs can sit in Finance queue for days; David has requested additional approvers or raising the threshold to $25,000 but no changes made yet

### Step 3a: Rejection and Resubmission (Exception Path)
- **Actor/Role**: Any Approver, then Requester
- **Description**: If any approver rejects the request, it returns to requester with rejection reason; requester can either cancel or modify the request (reduce quantity, find cheaper vendor, etc.) and resubmit, starting the approval process over from scratch
- **Input**: Rejected request
- **Output**: Cancelled request or modified resubmission
- **Duration/Timing**: Not specified, but restarts entire approval process
- **Pain Points**: Frustrating for requesters; entire approval process must start over from beginning

### Step 4: Procurement Team Review
- **Actor/Role**: Procurement Team (David Park and 2 procurement specialists)
- **Description**: Procurement team reviews the fully-approved request to verify it's reasonable for the company, vendor is legitimate, and price is competitive
- **Input**: Fully approved PO request
- **Output**: Procurement verification complete
- **Duration/Timing**: Not specified for this step alone
- **Pain Points**: Manual review process; lack of dashboard visibility makes tracking difficult - must manually look up individual requests to check status; status update emails consume 5-10 hours per week

### Step 5: Vendor Verification
- **Actor/Role**: Procurement Team
- **Description**: Procurement team checks if vendor is on the approved vendor list; if yes, proceed; if no, must vet new vendor by requesting business information, conducting credit check, and verifying legitimacy
- **Input**: Procurement-verified request
- **Output**: Vendor verification complete or new vendor vetting complete
- **Duration/Timing**: Immediate if vendor on approved list; 3-5 days for new vendor vetting
- **Pain Points**: 20-30% of requests involve vendors not on approved list (particularly from Engineering, IT, and Marketing departments); new vendor vetting adds significant time to process

### Step 6: Price Negotiation (Conditional)
- **Actor/Role**: Procurement Team
- **Description**: For purchases over $5,000, procurement team attempts to negotiate better terms with vendor (better price, volume discounts, improved payment terms, free shipping, etc.)
- **Input**: Vendor-verified request over $5,000
- **Output**: Final negotiated price and terms
- **Duration/Timing**: A few hours to a few days, depending on vendor responsiveness and purchase complexity
- **Pain Points**: Timeline variability depends on vendor responsiveness; may require waiting on vendor quotes

### Step 7: Legal Review (Conditional - Over $50,000 or Service Contracts)
- **Actor/Role**: Legal Team
- **Description**: For purchases over $50,000 or service contracts with ongoing commitments, legal team reviews vendor's terms and conditions to ensure company protection
- **Input**: High-value purchase or service contract
- **Output**: Legal approval
- **Duration/Timing**: Can add a week or more depending on legal team backlog
- **Pain Points**: Adds significant time; legal team backlog creates delays; occurs in approximately 5% of POs

### Step 8: Create Official Purchase Order
- **Actor/Role**: Procurement Team
- **Description**: Procurement team creates official PO in the system, entering final negotiated price, terms and conditions, delivery date, payment terms, and shipping address; system generates PO number
- **Input**: Completed negotiations and approvals
- **Output**: Official PO with PO number
- **Duration/Timing**: Not specified
- **Pain Points**: None mentioned for this specific step

### Step 9: Send PO to Vendor
- **Actor/Role**: ERP System (automated) and Procurement Team
- **Description**: System automatically sends email to vendor with PO attached as PDF; vendor is expected to acknowledge receipt and confirm ability to fulfill order on requested timeline
- **Input**: Created PO
- **Output**: PO sent to vendor
- **Duration/Timing**: Automated email sending
- **Pain Points**: Vendors poor at acknowledging POs - approximately 40% require manual follow-up by phone; 10% of vendors report inability to fulfill on requested timeline requiring rework with requester

### Step 10: Urgency Flag Verification (Conditional)
- **Actor/Role**: Procurement Team
- **Description**: For requests marked as "urgent" or "emergency," procurement team emails requester's manager to confirm the urgency level is accurate before expediting
- **Input**: PO request flagged as urgent or emergency
- **Output**: Verified urgency status
- **Duration/Timing**: Not specified, but slows down processing
- **Pain Points**: Requesters abuse urgency flags (urgent/emergency) to expedite non-urgent POs; happens approximately once per week; verification process added to combat abuse but adds delay

## Actors and Roles

| Role | Responsibilities | Systems Used |
|------|-----------------|--------------|
| Employee (Requester) | Submit PO requests with complete details; modify and resubmit rejected requests | ERP System - Procurement Portal |
| Direct Manager | Review and approve PO requests under direct reports; confirm urgency flags when needed | ERP System - Procurement Portal, Email |
| Department Head | Review and approve PO requests $1,000-$10,000 and over $10,000 | ERP System - Procurement Portal, Email |
| Finance | Review and approve PO requests over $10,000 | ERP System - Procurement Portal, Email |
| Procurement Team (David Park + 2 specialists) | Review all approved requests; verify vendors; negotiate prices; create official POs; follow up with vendors; manage 200-250 POs monthly | ERP System - Procurement Portal, Email, Phone |
| Legal Team | Review terms and conditions for purchases over $50,000 or service contracts | Not specified |
| ERP System | Automated budget verification; automated PO email distribution | ERP System |
| Vendor | Acknowledge PO receipt; confirm fulfillment capability and timeline | Email |

## Decision Points

### Decision Point 1: Budget Verification Check
- **Location in Process**: After Step 1 (Submit Request)
- **Condition**: Does department have sufficient remaining budget for the purchase amount?
- **Outcomes**:
  - **Path A**: Sufficient budget → Proceed to Step 3 (Approval Routing)
  - **Path B**: Insufficient budget → Step 2a (Automatic rejection with email notification)
- **Decision Maker**: ERP System (automated)

### Decision Point 2: Approval Tier Determination
- **Location in Process**: After Step 2 (Budget Verification passes)
- **Condition**: Purchase amount
- **Outcomes**:
  - **Path A**: Under $1,000 → Manager approval only
  - **Path B**: $1,000 to $10,000 → Manager + Department Head approval
  - **Path C**: Over $10,000 → Manager + Department Head + Finance approval
- **Decision Maker**: ERP System (automated routing based on amount)

### Decision Point 3: Approval or Rejection
- **Location in Process**: During Step 3 (any approval tier)
- **Condition**: Does approver accept or reject the request?
- **Outcomes**:
  - **Path A**: Approved → Continue to next approver or proceed to Step 4 (Procurement Review)
  - **Path B**: Rejected → Step 3a (Return to requester with reason)
- **Decision Maker**: Individual approvers (Manager, Department Head, Finance)

### Decision Point 4: Resubmission Decision
- **Location in Process**: After Step 3a (Rejection)
- **Condition**: Requester's decision on how to handle rejection
- **Outcomes**:
  - **Path A**: Cancel request → Process ends
  - **Path B**: Modify and resubmit → Return to Step 1 (entire process restarts)
- **Decision Maker**: Requester

### Decision Point 5: Vendor Approved Status
- **Location in Process**: After Step 5 (Vendor Verification)
- **Condition**: Is vendor on approved vendor list?
- **Outcomes**:
  - **Path A**: Vendor on approved list → Proceed to Step 6
  - **Path B**: Vendor not on approved list → Complete new vendor vetting (3-5 days) then proceed to Step 6
- **Decision Maker**: Procurement Team verification

### Decision Point 6: Price Negotiation Threshold
- **Location in Process**: After Step 5 (Vendor Verification)
- **Condition**: Is purchase amount over $5,000?
- **Outcomes**:
  - **Path A**: Over $5,000 → Attempt price negotiation (Step 6)
  - **Path B**: $5,000 or under → Skip negotiation, proceed to Step 8 (Create PO)
- **Decision Maker**: Procurement Team (standard practice)

### Decision Point 7: Legal Review Required
- **Location in Process**: After Step 6 (Negotiation) or Step 5 (if no negotiation)
- **Condition**: Is purchase over $50,000 OR is it a service contract with ongoing commitments?
- **Outcomes**:
  - **Path A**: Yes (over $50k or service contract) → Step 7 (Legal Review)
  - **Path B**: No → Proceed to Step 8 (Create PO)
- **Decision Maker**: Procurement Team (standard practice)

### Decision Point 8: Vendor Fulfillment Capability
- **Location in Process**: After Step 9 (Send PO to Vendor)
- **Condition**: Can vendor fulfill order on requested timeline?
- **Outcomes**:
  - **Path A**: Yes, vendor can fulfill → Process continues/completes
  - **Path B**: No, delivery delay → Procurement contacts requester for decision (wait or find new vendor)
- **Decision Maker**: Vendor, then Requester

### Decision Point 9: Urgency Flag Verification
- **Location in Process**: During Step 4 or throughout process (parallel check)
- **Condition**: Is request marked as "urgent" or "emergency"?
- **Outcomes**:
  - **Path A**: Not urgent → Normal processing
  - **Path B**: Marked urgent/emergency → Step 10 (Verify urgency with requester's manager before expediting)
- **Decision Maker**: Procurement Team initiates verification; Manager confirms urgency

## Systems and Tools

| System | Purpose | Integration Points |
|--------|---------|-------------------|
| ERP System - Procurement Portal | Submit requests, approval workflow, PO creation and tracking | Steps 1, 2, 2a, 3, 4, 8, 9 |
| Email | Notifications for approvals, vendor PO delivery, status communications | Steps 2a, 3, 9, 10, status inquiries |
| Phone | Manual vendor follow-up when email acknowledgment not received | Step 9 follow-up (40% of POs) |
| Approved Vendor List | Vendor verification and vetting | Step 5 |
| Credit Check System | New vendor vetting | Step 5 (for new vendors) |

## Pain Points and Inefficiencies

### Critical Issues

1. **Finance Approval Bottleneck**: Only two people authorized to approve POs over $10,000, handling multiple approval types
   - **Impact**: POs sit in Finance queue for days; Tier 3 approvals can take up to a week; significant delay for higher-value purchases
   - **Frequency**: Every PO over $10,000 (significant portion of monthly volume)
   - **Affected Steps**: Step 3 (Tier 3 approval routing)

2. **Lack of Process Visibility/Dashboard**: No centralized view of all POs and their status
   - **Impact**: Manual lookup required for status checks; 5-10 hours per week spent responding to status update emails; inability to proactively manage workflow
   - **Frequency**: Continuous issue affecting daily operations
   - **Affected Steps**: Steps 4-9 (all procurement team activities)
   - **Note**: Requested from IT for over a year with no resolution

3. **Incomplete Purchase Requests**: 20-25% of requests missing critical information
   - **Impact**: Delays while procurement requests additional information from requesters; requester frustration about timeline
   - **Frequency**: 20-25% of all requests (40-63 POs per month)
   - **Affected Steps**: Step 1 and impacts Steps 4-8
   - **Root Cause**: Requesters in a hurry, don't understand requirements, or not detail-oriented; don't read provided checklists/guidelines

4. **Poor Vendor PO Acknowledgment**: 40% of vendors don't acknowledge PO receipt
   - **Impact**: Uncertainty about vendor receipt; manual follow-up required via phone; time spent tracking down vendors
   - **Frequency**: Approximately 40% of all POs (80-100 POs per month)
   - **Affected Steps**: Step 9

5. **Sequential Approval Delays**: Multi-tier sequential approvals create dependency chains
   - **Impact**: One person's absence or delay holds up entire process; 2-3 day delays for Tier 2; 3-5+ day delays for Tier 3
   - **Frequency**: Every PO over $1,000 (majority of POs)
   - **Affected Steps**: Step 3 (all approval tiers)

### Inefficiencies

1. **Urgency Flag Abuse**: Requesters misuse urgent/emergency flags to expedite non-urgent purchases
   - **Current State**: Happens approximately once per week; procurement now spot-checks by emailing requester's manager to verify
   - **Impact**: Wasted time expediting non-urgent requests; verification process slows down genuinely urgent requests

2. **New Vendor Vetting Delays**: 20-30% of requests require new vendor vetting
   - **Current State**: Adds 3-5 days to process timeline
   - **Impact**: Particularly affects Engineering, IT, and Marketing departments who frequently use new vendors; extends overall cycle time
   - **Frequency**: 20-30% of requests (40-75 POs per month)

3. **Month-End Request Spike**: Most requesters submit POs at month-end before budget expires
   - **Current State**: Creates workload concentration at month-end
   - **Impact**: Exacerbates delays during peak period; uneven workload distribution
   - **Frequency**: Monthly pattern

4. **Vendor Delivery Mismatches**: 10% of vendors cannot fulfill on requested timeline
   - **Current State**: Requires rework with requester to decide whether to wait or find new vendor
   - **Impact**: Process restart or extended timeline; requester frustration
   - **Frequency**: 10% of POs (20-25 POs per month)

5. **Legal Review Delays**: Required for 5% of POs (over $50k or service contracts)
   - **Current State**: Can add a week or more depending on legal team backlog
   - **Impact**: Significant timeline extension for high-value purchases
   - **Frequency**: 5% of POs (10-13 POs per month)

6. **Request Rejection and Full Process Restart**: Any rejection requires complete resubmission starting from beginning
   - **Current State**: Rejected requests must go through entire approval chain again
   - **Impact**: Frustrating for requesters; significantly extends timeline
   - **Frequency**: Includes 5-10% budget rejections plus approval rejections (frequency not specified)

## Process Metrics

- **Total Steps**: 10 (excluding conditional/exception paths)
- **Number of Decision Points**: 9
- **Number of Actors**: 8 (Employee, Manager, Department Head, Finance, Procurement Team, Legal, ERP System, Vendor)
- **Identified Pain Points**: 11 (6 critical issues, 5 inefficiencies)
- **Manual Steps**: 8 (Steps 1, 3 all tiers, 4, 5, 6, 7, 8, 10)
- **Systems Involved**: 5 (ERP/Procurement Portal, Email, Phone, Approved Vendor List, Credit Check System)
- **Monthly Volume**: 200-250 POs per month
- **Process Duration Range**: 1 day (simple, under $1k) to 2-3 weeks (complex with delays)
- **Incomplete Request Rate**: 20-25%
- **New Vendor Rate**: 20-30%
- **Budget Rejection Rate**: 5-10%
- **Vendor Non-Acknowledgment Rate**: 40%
- **Vendor Fulfillment Issue Rate**: 10%
- **Legal Review Rate**: 5%
- **Urgency Flag Abuse**: Approximately once per week

## Notes and Observations

### Process Variations by Purchase Amount
- **Under $1,000**: Fastest path (1-2 days) - Manager approval only
- **$1,000-$10,000**: Medium complexity (2-3 days) - Manager + Department Head
- **Over $10,000**: Longest path (3-7+ days) - Manager + Department Head + Finance
- **Over $50,000 or service contracts**: Add legal review (additional week+)

### Improvement Priorities Identified by Interviewee
1. **System Enhancement**: Dashboard for PO visibility and status tracking (highest impact - would save 5-10 hours/week)
2. **Process/Policy**: Better requester training and clearer policies to reduce incomplete requests and urgency flag abuse
3. **Organizational**: Additional Finance approvers or raised approval threshold from $10,000 to $25,000 (already requested, not approved)

### Department-Specific Patterns
- **Engineering, IT, Marketing**: Higher rate of new vendor requests (20-30% overall driven by these departments)
- All departments: Month-end submission spike due to budget expiration concerns

### Control vs. Efficiency Trade-offs
David acknowledges multi-tier approvals make sense from control/oversight perspective but create friction when combined with:
- Vendor verification requirements
- Manual tracking limitations
- Incomplete request rework
- Sequential (not parallel) approval routing

### Positive Aspects
- Automated budget verification (Step 2) viewed positively - saves procurement team time by rejecting unfunded requests immediately
- Under $1,000 approval tier works well (same-day or next-day)
- Price negotiation capability for purchases over $5,000 provides value

### Timeline Expectations
David recommends requesters submit POs at least 2 weeks before item needed, but acknowledges not everyone follows this guidance, contributing to frustration when process takes longer than expected.