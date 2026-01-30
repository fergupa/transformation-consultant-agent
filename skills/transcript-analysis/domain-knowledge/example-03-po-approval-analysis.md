# Process Analysis: Purchase Order Approval Process

## Executive Summary
The purchase order approval process handles 200-250 POs monthly through a multi-tier approval system with automated budget checks and amount-based routing thresholds. Processing time ranges from same-day for small purchases under $1,000 to 2-3 weeks for complex large purchases, with significant delays caused by incomplete requests, vendor verification requirements, approval bottlenecks, and lack of process visibility.

## Process Steps

### Step 1: Submit PO Request
- **Actor/Role**: Requester (Employee)
- **Description**: Employee logs into procurement portal (ERP module) and fills out request form with purchase details: item description, quantity, estimated cost, vendor name (if known), business justification, budget code, and urgency flag (routine, urgent, or emergency)
- **Input**: Purchase need and details
- **Output**: PO request submitted to procurement queue
- **Duration/Timing**: Initial submission
- **Pain Points**: 20-25% of requests are incomplete (missing product details, model numbers, vendor name, or vague business justification); requesters don't read guidelines; creates delays when procurement must request more information

### Step 2: Automatic Budget Check
- **Actor/Role**: ERP System
- **Description**: System automatically checks the budget code entered against department's remaining budget to verify sufficient funds available for the purchase
- **Input**: PO request with budget code and amount
- **Output**: Budget check pass or fail
- **Duration/Timing**: Automatic/immediate
- **Pain Points**: None mentioned - automated check saves manual review time

### Step 3: Budget Rejection Handling
- **Actor/Role**: ERP System, Requester
- **Description**: If budget check fails, request is automatically rejected and requester receives email notification of insufficient budget; requester must wait for next fiscal period or request budget reallocation from department head
- **Input**: Failed budget check
- **Output**: Request rejected with notification
- **Duration/Timing**: Immediate
- **Pain Points**: Occurs 5-10% of the time; forces requester to restart process later or seek budget reallocation

### Step 4: Approval Routing
- **Actor/Role**: ERP System
- **Description**: System routes approved budget requests to appropriate approvers based on amount tiers: under $1,000 requires manager only; $1,000-$10,000 requires manager and department head; over $10,000 requires manager, department head, and Finance
- **Input**: Budget-approved PO request
- **Output**: Request routed to appropriate approval queue(s)
- **Duration/Timing**: Automatic/immediate
- **Pain Points**: None in routing itself, but tiered structure creates escalating delays

### Step 5: Manager Approval
- **Actor/Role**: Requester's Direct Manager
- **Description**: Manager receives email notification, logs into procurement portal, reviews request details, and approves or rejects
- **Input**: Routed PO request
- **Output**: Manager approval or rejection
- **Duration/Timing**: Usually same-day or next-day for under $1,000 requests
- **Pain Points**: Delays if manager is out of office or busy

### Step 6: Department Head Approval
- **Actor/Role**: Department Head
- **Description**: For requests $1,000+, department head receives notification after manager approval, logs into portal, reviews, and approves or rejects
- **Input**: Manager-approved PO request
- **Output**: Department head approval or rejection
- **Duration/Timing**: Adds 1-2 days to process; total 2-3 days for $1K-$10K requests
- **Pain Points**: Sequential approval (must wait for manager first) extends timeline; delays if department head unavailable

### Step 7: Finance Approval
- **Actor/Role**: Finance Approvers (2 people)
- **Description**: For requests over $10,000, Finance team must approve after manager and department head approvals
- **Input**: Manager and department head approved PO request
- **Output**: Finance approval or rejection
- **Duration/Timing**: 3-5 days, sometimes up to a week
- **Pain Points**: Major bottleneck - only 2 Finance approvers handling POs plus expense reports and invoices; requests sit in queue for days; can take up to a week; procurement has requested more approvers or higher threshold ($25K instead of $10K) without success

### Step 8: Rejection Handling
- **Actor/Role**: Any Approver, Requester
- **Description**: If any approver rejects request, it returns to requester with rejection reason; requester can cancel or modify (reduce quantity, find cheaper vendor) and resubmit, starting approval process over from beginning
- **Input**: Rejection from any approval tier
- **Output**: Modified and resubmitted request, or cancelled request
- **Duration/Timing**: Variable based on requester response
- **Pain Points**: Frustrating for requesters; entire approval chain restarts from scratch after modifications

### Step 9: Procurement Team Review
- **Actor/Role**: Procurement Manager (David), Procurement Specialists (2)
- **Description**: After all approvals obtained, procurement team reviews request for reasonableness: is purchase appropriate for company, is vendor legitimate, is price competitive
- **Input**: Fully approved PO request
- **Output**: Procurement validation complete
- **Duration/Timing**: Part of PO processing
- **Pain Points**: Manual review required for each request

### Step 10: Vendor Verification
- **Actor/Role**: Procurement Team
- **Description**: Check if vendor is on approved vendor list; approved vendors have been pre-vetted for business license, tax ID, insurance, etc.
- **Input**: Vendor name from request
- **Output**: Vendor status determination (approved vs new)
- **Duration/Timing**: Quick lookup if vendor approved
- **Pain Points**: 20-30% of requests are for vendors not on approved list, especially from Engineering, IT, and Marketing departments for SaaS vendors and specialized suppliers

### Step 11: New Vendor Vetting
- **Actor/Role**: Procurement Team, Vendor
- **Description**: For vendors not on approved list, request business information, conduct credit check, verify legitimate business operation
- **Input**: New vendor information
- **Output**: Vendor added to approved list or request rejected
- **Duration/Timing**: Adds 3-5 days to process
- **Pain Points**: Significant delay for 20-30% of requests; common with specialized or new technology vendors

### Step 12: Price Negotiation
- **Actor/Role**: Procurement Team, Vendor
- **Description**: For purchases over $5,000, attempt to negotiate better pricing (volume discounts, payment terms, free shipping); below $5,000 not worth the time and vendors typically won't negotiate
- **Input**: PO request over $5,000
- **Output**: Final negotiated price and terms
- **Duration/Timing**: Few hours to few days depending on vendor responsiveness and purchase complexity
- **Pain Points**: Timeline variability based on vendor response time; delays waiting for vendor quotes

### Step 13: Legal Review
- **Actor/Role**: Legal Team
- **Description**: For purchases over $50,000 or service contracts with ongoing commitments, legal reviews vendor's terms and conditions to ensure company protection
- **Input**: Large purchase or service contract
- **Output**: Legal approval of terms
- **Duration/Timing**: Adds a week or more depending on legal team backlog
- **Pain Points**: Occurs only on 5% of POs but significantly extends timeline; legal team backlog causes delays

### Step 14: Create Official Purchase Order
- **Actor/Role**: Procurement Team
- **Description**: Enter final negotiated price, terms and conditions, delivery date, payment terms, and shipping address into system; system generates PO number
- **Input**: Approved and verified request with final pricing
- **Output**: Official PO created with PO number
- **Duration/Timing**: Part of PO processing
- **Pain Points**: None mentioned

### Step 15: Send PO to Vendor
- **Actor/Role**: ERP System, Procurement Team
- **Description**: System automatically sends PO to vendor via email with PDF attachment; vendor should acknowledge receipt and confirm fulfillment on requested timeline
- **Input**: Created PO
- **Output**: PO transmitted to vendor
- **Duration/Timing**: Automatic email
- **Pain Points**: 40% of vendors don't respond to acknowledge PO; procurement must manually follow up by phone; vendors poor at acknowledging POs; 10% of vendors indicate they cannot fulfill on requested timeline, requiring procurement to notify requester of delay

### Step 16: Urgency Verification
- **Actor/Role**: Procurement Team, Requester's Manager
- **Description**: For requests flagged as urgent or emergency, procurement spot-checks with requester's manager to confirm legitimacy before expediting; prevents abuse of urgency flags
- **Input**: PO request marked urgent or emergency
- **Output**: Confirmed urgency or downgraded priority
- **Duration/Timing**: Adds time to verification
- **Pain Points**: Urgency flags abused approximately once per week by requesters trying to expedite non-urgent requests; adds verification step that slows process

### Step 17: Vendor Delivery Confirmation
- **Actor/Role**: Vendor, Requester
- **Description**: Vendor fulfills order and delivers to specified address based on PO terms; if vendor cannot meet timeline, procurement notifies requester who decides whether to wait or find alternative vendor
- **Input**: PO from vendor
- **Output**: Order fulfilled or timeline issue identified
- **Duration/Timing**: Per vendor lead time
- **Pain Points**: 10% of vendors cannot fulfill on requested timeline

## Actors and Roles

| Role | Responsibilities | Systems Used |
|------|-----------------|--------------|
| Requester (Employee) | Submits PO requests with purchase details, budget code, and business justification; responds to incomplete request follow-ups | Procurement Portal (ERP module), Email |
| Requester's Direct Manager | First-tier approval for all PO requests; reviews and approves/rejects | Procurement Portal, Email |
| Department Head | Second-tier approval for requests $1,000+; reviews and approves/rejects | Procurement Portal, Email |
| Finance Approvers (2 people) | Third-tier approval for requests over $10,000; reviews and approves/rejects; also handles expense reports and invoices | Procurement Portal, Email |
| Procurement Manager (David) | Manages procurement team; reviews approved requests; verifies vendors; negotiates pricing; creates POs; handles vendor communication | Procurement Portal, ERP, Email, Phone |
| Procurement Specialists (2) | Assist with procurement reviews, vendor verification, and PO creation | Procurement Portal, ERP, Email |
| Vendor | Receives PO, acknowledges receipt, confirms delivery timeline, fulfills order | Email |
| Legal Team | Reviews large purchases (>$50K) and service contracts to ensure favorable terms | Contract review systems |

## Decision Points

### Decision Point 1: Budget Check Result
- **Location in Process**: Step 2 (Automatic Budget Check)
- **Condition**: Whether department has sufficient remaining budget for purchase
- **Outcomes**:
  - **Path A**: Budget available (90-95%) → Proceed to Step 4 (Approval Routing)
  - **Path B**: Insufficient budget (5-10%) → Proceed to Step 3 (Budget Rejection), request ends or requires budget reallocation
- **Decision Maker**: ERP system automated budget check

### Decision Point 2: Approval Amount Threshold
- **Location in Process**: Step 4 (Approval Routing)
- **Condition**: Total dollar amount of purchase request
- **Outcomes**:
  - **Path A**: Under $1,000 → Manager approval only (Step 5) → Proceed to Step 9
  - **Path B**: $1,000 to $10,000 → Manager (Step 5) + Department Head (Step 6) → Proceed to Step 9
  - **Path C**: Over $10,000 → Manager (Step 5) + Department Head (Step 6) + Finance (Step 7) → Proceed to Step 9
- **Decision Maker**: ERP system automated routing based on amount

### Decision Point 3: Approval or Rejection at Each Tier
- **Location in Process**: Steps 5, 6, 7 (Manager, Department Head, Finance Approval)
- **Condition**: Approver's assessment of purchase necessity, appropriateness, and budget alignment
- **Outcomes**:
  - **Path A**: Approve → Proceed to next approval tier or to Step 9 (Procurement Review) if final approval
  - **Path B**: Reject → Proceed to Step 8 (Rejection Handling), requester modifies and resubmits or cancels
- **Decision Maker**: Manager, Department Head, or Finance depending on tier

### Decision Point 4: Vendor Approved Status
- **Location in Process**: Step 10 (Vendor Verification)
- **Condition**: Whether vendor exists on approved vendor list
- **Outcomes**:
  - **Path A**: Vendor on approved list (70-80%) → Proceed to Step 12 (Price Negotiation or PO Creation)
  - **Path B**: Vendor not on approved list (20-30%) → Proceed to Step 11 (New Vendor Vetting), adds 3-5 days
- **Decision Maker**: Procurement team lookup in approved vendor database

### Decision Point 5: Price Negotiation Threshold
- **Location in Process**: Step 12 (Price Negotiation)
- **Condition**: Purchase amount
- **Outcomes**:
  - **Path A**: Over $5,000 → Attempt price negotiation with vendor
  - **Path B**: $5,000 or less → Skip negotiation, proceed to Step 13/14
- **Decision Maker**: Procurement team policy based on amount

### Decision Point 6: Legal Review Requirement
- **Location in Process**: Step 13 (Legal Review)
- **Condition**: Purchase amount over $50,000 OR service contract with ongoing commitments
- **Outcomes**:
  - **Path A**: Over $50K or service contract (5% of POs) → Legal review required, adds week+
  - **Path B**: Under threshold and not service contract (95%) → Skip legal review, proceed to Step 14
- **Decision Maker**: Procurement team assessment of amount and contract type

### Decision Point 7: Vendor Delivery Capability
- **Location in Process**: Step 17 (Vendor Delivery Confirmation)
- **Condition**: Whether vendor can fulfill on requested timeline
- **Outcomes**:
  - **Path A**: Vendor can fulfill (90%) → Order proceeds
  - **Path B**: Vendor cannot fulfill on time (10%) → Notify requester, requester decides to wait or find alternative vendor
- **Decision Maker**: Vendor capability; final decision by requester

## Systems and Tools

| System | Purpose | Integration Points |
|--------|---------|-------------------|
| Procurement Portal (ERP Module) | Submit PO requests, approval workflows, vendor management | Steps 1, 4, 5, 6, 7, 14 |
| ERP System | Budget checking, PO creation, overall procurement management | Steps 2, 14 |
| Email | Notifications to approvers, vendor communication, status updates | Steps 3, 5, 6, 7, 8, 15 |
| Phone | Manual vendor follow-up for PO acknowledgments | Step 15 |
| Contract Review Systems | Legal team tools for reviewing terms | Step 13 |
| Approved Vendor Database | Track vetted vendors | Step 10, 11 |

## Pain Points and Inefficiencies

### Critical Issues

1. **Finance Approval Bottleneck**: Only 2 Finance approvers for all POs over $10,000 plus other approval responsibilities
   - **Impact**: POs sit in queue 3-5 days, sometimes up to a week; requests to add approvers or raise threshold to $25K denied
   - **Frequency**: Every PO over $10,000
   - **Affected Steps**: Step 7

2. **No Process Visibility Dashboard**: No centralized view of all POs and their status; no self-service for requesters
   - **Impact**: Procurement must manually look up each request when asked for status; requesters email for updates instead of checking themselves; wastes 5-10 hours per week on status emails; requested from IT for over a year
   - **Frequency**: Continuous issue
   - **Affected Steps**: All steps - affects monitoring and communication

3. **Incomplete PO Requests**: 20-25% of requests missing critical details (product specs, model numbers, vendor, clear justification)
   - **Impact**: Procurement must request additional information, delaying process; frustrating for both sides; requesters don't read guidelines
   - **Frequency**: 20-25% of 200-250 monthly POs (40-60 requests per month)
   - **Affected Steps**: Step 1, causes delays throughout

4. **Manual Vendor Acknowledgment Follow-Up**: 40% of vendors don't respond to PO emails, requiring manual phone calls
   - **Impact**: Procurement must manually track and chase vendor confirmations; time-consuming
   - **Frequency**: 40% of all POs (80-100 per month)
   - **Affected Steps**: Step 15

5. **New Vendor Vetting Delays**: 20-30% of requests are for non-approved vendors requiring 3-5 day vetting process
   - **Impact**: Adds significant delay for new technology purchases, SaaS vendors, specialized suppliers
   - **Frequency**: 20-30% of requests, especially from Engineering, IT, and Marketing
   - **Affected Steps**: Steps 10-11

### Inefficiencies

1. **Urgency Flag Abuse**: Requesters misuse urgent/emergency flags to expedite non-urgent requests
   - **Current State**: Occurs approximately once per week
   - **Impact**: Procurement must spot-check with managers to verify legitimacy, adding time; scrambling to expedite when not truly urgent

2. **Month-End Surge**: Most requesters submit POs at end of month when budget about to expire
   - **Current State**: Volume concentration creates processing delays
   - **Impact**: Compounds all other delays; overwhelms approval queues and procurement team

3. **Approval Chain Restart After Rejection**: Any rejection sends request back to beginning
   - **Current State**: Modified requests restart entire approval sequence
   - **Impact**: Frustrating for requesters; extends timeline significantly

4. **Limited Price Negotiation**: Only attempted on purchases over $5,000
   - **Current State**: Smaller purchases accepted at list price
   - **Impact**: Potential savings missed on cumulative smaller purchases

5. **Sequential Approval Flow**: Approvals must happen in sequence (manager → department head → finance)
   - **Current State**: Cannot parallelize approvals
   - **Impact**: Each tier adds time; delays compound

6. **Manual Status Checking**: Requester questions require manual portal lookups
   - **Current State**: No self-service visibility for requesters
   - **Impact**: Time waste for procurement team; requester frustration

## Process Metrics
- **Total Steps**: 17 (including conditional and exception handling steps)
- **Number of Decision Points**: 7
- **Number of Actors**: 8 (including vendor and legal)
- **Identified Pain Points**: 5 critical issues, 6 inefficiencies
- **Manual Steps**: 9 steps require manual intervention
- **Systems Involved**: 6
- **Volume**: 200-250 POs per month
- **Processing Time**:
  - Best case (under $1K, approved vendor, complete request): Same-day to 2 days
  - Typical case ($1K-$10K): 2-5 days
  - Complex case (over $10K, new vendor, negotiation): 1-2 weeks
  - Worst case (rejections, incomplete, new vendor, legal review): 2-3 weeks
- **Budget Rejection Rate**: 5-10%
- **Incomplete Request Rate**: 20-25%
- **New Vendor Rate**: 20-30% (higher for Engineering, IT, Marketing)
- **Vendor Non-Response Rate**: 40%
- **Vendor Cannot Fulfill Rate**: 10%
- **Urgency Flag Abuse**: ~Once per week
- **Legal Review Required**: 5% of POs
- **Approval Tiers**: <$1K (manager), $1K-$10K (manager + dept head), >$10K (manager + dept head + finance)
- **Negotiation Threshold**: >$5K
- **Finance Team Capacity**: 2 approvers
- **Procurement Team Size**: 1 manager + 2 specialists

## Notes and Observations

- Procurement team consists of 3 people (1 manager, 2 specialists) handling 200-250 POs monthly
- Most process pain points relate to visibility and communication rather than approval policy itself
- Multi-tier approval structure is intentional for spending oversight; changing thresholds has been rejected
- Budget check automation (5-10% rejection rate) successfully prevents wasted approval effort on unfunded requests
- Engineering, IT, and Marketing departments disproportionately request new vendors (20-30% overall rate, likely higher for these departments specifically)
- Requesters advised to submit 2+ weeks before need date but many don't, especially at month-end
- Month-end surge driven by budget expiration creates predictable capacity constraint
- Legal review only impacts 5% of POs but adds week+ when triggered
- Price negotiation attempted on >$5K purchases with variable success and timeline
- Urgency flag abuse reduced but not eliminated by manager verification process
- If one improvement had to be prioritized, Procurement Manager identified visibility dashboard as highest impact (save 5-10 hours/week, enable requester self-service, better workflow management)
- Portal guidelines and checklists exist but requesters don't consistently use them
- Approval bottleneck is at Finance level for large purchases (3-5+ days)
- Vendor responsiveness is poor (40% don't acknowledge, 10% can't meet timeline)
- Sequential approval flow prevents parallel processing, compounding delays
- Rejection requires complete restart of approval chain, no ability to resume from last approver
- No integration between procurement portal and vendor communication systems
