# Process Analysis: Accounts Payable Invoice Processing

## Executive Summary
The Accounts Payable Invoice Processing process involves receiving invoices through multiple channels (email, mail, vendor portal), manual data entry into SAP, PO matching and three-way matching validation, approval workflows for high-value and non-PO invoices, and payment processing via bi-weekly payment runs. The process is heavily manual, involving three AP team members processing 300-400 invoices monthly, with significant pain points around document handling, data entry, PO matching, and approval bottlenecks that result in an average 25-day payment cycle.

## Process Steps

### Step 1: Receive Invoice
- **Actor/Role**: AP Clerk (Sarah Mitchell)
- **Description**: Invoices arrive through multiple channels: shared AP email inbox (60%), postal mail (25%), ERP vendor portal (10-15%), and other channels including hand-delivery or forwarding from purchasing team
- **Input**: Invoice from vendor via various channels
- **Output**: Invoice available for processing
- **Duration/Timing**: Continuous/as received
- **Pain Points**: Multiple intake channels create inconsistent handling and complexity; no centralized receipt process

### Step 2: Download Email Attachments
- **Actor/Role**: AP Clerk
- **Description**: For email-received invoices, download PDF attachments from the shared AP inbox (ap@company.com)
- **Input**: Email invoice in shared inbox
- **Output**: PDF invoice file downloaded locally
- **Duration/Timing**: Not specified
- **Pain Points**: None mentioned for this specific step

### Step 3: Print and Scan Invoice
- **Actor/Role**: AP Clerk
- **Description**: Print downloaded PDF invoices and scan them back in using document scanner to get them into the document management system integrated with ERP. For mailed invoices, scan directly without printing. Vendor portal invoices skip this step as they are already in the system.
- **Input**: Downloaded PDF (email invoices) or physical mail invoice
- **Output**: Scanned invoice in document management system
- **Duration/Timing**: Not specified per invoice
- **Pain Points**: Extremely inefficient workaround required because ERP system cannot accept direct PDF uploads; requires printing digital documents and scanning them back in; team has been requesting IT to fix this for two years

### Step 4: Manual Data Entry
- **Actor/Role**: AP Clerk
- **Description**: Open SAP ERP system and manually type in all invoice details including vendor name, invoice number, invoice date, due date, line items, amounts, tax, and total
- **Input**: Scanned invoice in document management system
- **Output**: Invoice data entered into SAP
- **Duration/Timing**: 5-10 minutes per invoice depending on number of line items
- **Pain Points**: Completely manual data entry despite information being visible in scanned document; time-consuming (100-150 invoices per clerk monthly); error-prone with mistakes occurring approximately once per week; requires reprocessing and credit memos when errors reach payment stage

### Step 5: Search for Matching Purchase Order
- **Actor/Role**: AP Clerk
- **Description**: Search in SAP for the corresponding PO number. If PO number is on invoice, search by that number. If not, search by vendor name and date range and manually review open POs to find the correct match. Approximately 80% of invoices have corresponding POs.
- **Input**: Invoice data entered in SAP
- **Output**: Located PO number or determination that PO cannot be found
- **Duration/Timing**: Variable; can take significant time if vendor has multiple POs and PO number not on invoice
- **Pain Points**: Poor search functionality in SAP; PO numbers often not included on invoices requiring time-consuming manual searching through multiple open POs; process slows significantly when searching vendors with multiple POs

### Step 6: Resolve Missing PO (Exception Path)
- **Actor/Role**: AP Clerk, Purchasing Team
- **Description**: When PO cannot be found, email purchasing team to investigate. Purchasing team either provides PO number, indicates it's a non-PO purchase requiring different processing, or creates PO retroactively
- **Input**: Invoice without matching PO
- **Output**: PO number provided, non-PO designation confirmed, or retroactive PO created
- **Duration/Timing**: Can take days; invoice sits in queue during this time
- **Frequency**: 10-15% of invoices
- **Pain Points**: Creates significant delays; invoices sit in queue waiting for response; vendors begin calling to inquire about payment; retroactive PO creation can take days

### Step 7: Link Invoice to PO
- **Actor/Role**: AP Clerk
- **Description**: Link the invoice to the corresponding PO in SAP system
- **Input**: Invoice data in SAP and confirmed PO number
- **Output**: Invoice linked to PO in system
- **Duration/Timing**: Not specified
- **Pain Points**: None mentioned for this specific step

### Step 8: Three-Way Match Validation
- **Actor/Role**: SAP System (automated)
- **Description**: System automatically performs three-way match checking that invoice quantities and amounts match the PO and receiving report within tolerance (5% or $50, whichever is less)
- **Input**: Linked invoice and PO with receiving report
- **Output**: Match successful or match failure with discrepancies identified
- **Duration/Timing**: Immediate/automated
- **Pain Points**: Discrepancies are the biggest source of payment delays

### Step 9: Investigate and Resolve Discrepancies (Exception Path)
- **Actor/Role**: AP Clerk, Purchasing Team, Vendor
- **Description**: When three-way match fails, check receiving report to identify discrepancy (quantity mismatch, price difference, etc.). Contact purchasing team and/or vendor to resolve the issue
- **Input**: Failed three-way match with identified discrepancies
- **Output**: Resolved discrepancy with corrected information
- **Duration/Timing**: Can take days or weeks to resolve
- **Pain Points**: Single biggest source of payment delays; resolution requires coordination between multiple parties; vendors frustrated by delays; can take weeks to resolve complex discrepancies

### Step 10: Route for Additional Approval (High-Value Invoices)
- **Actor/Role**: SAP System, AP Clerk
- **Description**: For invoices $5,000 or more, or any non-PO invoices regardless of amount, flag invoice in SAP as requiring approval. SAP sends notification to third-party approval portal, which sends email notification to AP Manager (Linda)
- **Input**: Successfully matched invoice meeting approval threshold criteria
- **Output**: Approval request sent to AP Manager
- **Duration/Timing**: Immediate system notification
- **Pain Points**: Separate third-party approval portal adds system complexity; non-PO invoices always require approval regardless of small amounts; creates bottleneck

### Step 11: Manager Approval Review
- **Actor/Role**: AP Manager (Linda)
- **Description**: AP Manager logs into approval portal, reviews scanned invoice and PO, and clicks to approve or reject. If rejected, returns to AP Clerk with comments for correction
- **Input**: Approval request in portal with invoice and PO documentation
- **Output**: Approved invoice returned to SAP payment queue, or rejected invoice returned to AP Clerk
- **Duration/Timing**: Supposed to take 24 hours but realistically takes 2-3 days
- **Pain Points**: Manager is busy and approval emails get buried in inbox; creates significant bottleneck especially at month-end during close; vendor complaints about stuck invoices; approval delays are embarrassing for team

### Step 12: Move to Payment Queue (Auto-Approved)
- **Actor/Role**: SAP System (automated)
- **Description**: Invoices under $5,000 with successful PO three-way match move automatically to payment queue without additional approval
- **Input**: Successfully matched invoice under $5,000 threshold
- **Output**: Invoice in payment queue
- **Duration/Timing**: Immediate/automated
- **Pain Points**: None mentioned for this specific step

### Step 13: Payment Batch Processing
- **Actor/Role**: AP Specialist (Marcus)
- **Description**: Run payment batch in SAP. System groups all approved invoices due within next 5 days, generates payments, and exports to banking system. Payments are primarily ACH with some checks for vendors not accepting electronic payment.
- **Input**: Approved invoices in payment queue
- **Output**: Payment batch exported to banking system
- **Duration/Timing**: Runs twice weekly on Tuesdays and Fridays
- **Pain Points**: Invoices sometimes get stuck or fail validation; incorrect or missing vendor banking information causes payment failures requiring vendor contact and delays payment by at least another week

### Step 14: Resolve Failed Payments (Exception Path)
- **Actor/Role**: AP Specialist (Marcus), AP Clerk
- **Description**: When payments fail validation (typically due to incorrect/missing vendor banking information), contact vendor to obtain updated information and update SAP system
- **Input**: Failed payment validation
- **Output**: Updated vendor banking information in SAP
- **Duration/Timing**: At least one week delay to next payment run
- **Pain Points**: Delays payment by minimum of one week until next payment run; requires vendor outreach and coordination

### Step 15: Vendor Payment Notification
- **Actor/Role**: SAP System (automated with failures), AP Clerk (manual workaround)
- **Description**: SAP automatically sends payment remittance emails to vendors. However, system is unreliable and only approximately 50% of vendors receive these emails. AP Clerk manually looks up payment details in SAP and emails vendors upon inquiry.
- **Input**: Processed payment
- **Output**: Vendor notified of payment details
- **Duration/Timing**: Should be immediate but manual follow-up required frequently
- **Pain Points**: Automated notification feature is "flaky" and fails about 50% of the time; generates high volume of vendor inquiry calls; requires manual lookup and email follow-up; another time-consuming manual workaround

### Step 16: Duplicate Invoice Check (Ongoing/Preventative)
- **Actor/Role**: AP Clerk
- **Description**: Check for duplicate invoices during entry process. Duplicates can occur when vendors send same invoice via multiple channels (email and mail) or resend thinking original wasn't received
- **Input**: Invoice being entered
- **Output**: Confirmation that invoice is not a duplicate
- **Duration/Timing**: During Step 4 (data entry)
- **Pain Points**: Duplicates sometimes slip through, especially with slightly different invoice numbers or dates; has resulted in paying same invoice twice requiring awkward refund requests from vendors

## Actors and Roles

| Role | Responsibilities | Systems Used |
|------|-----------------|--------------|
| AP Clerk (Sarah Mitchell) | Receive and download invoices; print and scan documents; manual data entry; PO searching and matching; linking invoices to POs; discrepancy investigation; duplicate checking; vendor communication for banking info and payment details | Email (shared AP inbox), Document Scanner, SAP ERP, Document Management System |
| AP Manager (Linda) | Approve invoices $5,000+ and all non-PO invoices; review and approve/reject in approval portal | Third-party Approval Portal, Email |
| AP Specialist (Marcus) | Run bi-weekly payment batches; troubleshoot failed payments | SAP ERP, Banking System |
| Purchasing Team | Provide PO numbers for invoices; create retroactive POs; assist with discrepancy resolution | SAP ERP (implied), Email |
| Vendor | Submit invoices; provide corrected invoices for discrepancies; provide updated banking information | Email, Mail, ERP Vendor Portal, Phone |
| SAP System | Three-way match validation; approval routing; payment remittance notifications (unreliable) | N/A (is the system) |
| Approval Portal System | Route approval requests; send notifications; capture approvals/rejections | N/A (is the system) |
| Banking System | Process ACH and check payments | N/A (is the system) |

## Decision Points

### Decision Point 1: Invoice Channel Routing
- **Location in Process**: After Step 1 (Receive Invoice)
- **Condition**: Method by which invoice was received
- **Outcomes**:
  - **Path A**: Email (60%) → Proceed to Step 2 (Download attachment) then Step 3 (Print and scan)
  - **Path B**: Mail (25%) → Proceed directly to Step 3 (Scan only, no printing)
  - **Path C**: Vendor Portal (10-15%) → Skip to Step 4 (Manual data entry) - already in system
  - **Path D**: Other channels (hand-delivery, purchasing forward) → [Process not fully specified but likely follows email or mail path]
- **Decision Maker**: Inherent in invoice delivery channel

### Decision Point 2: PO Matching Success
- **Location in Process**: After Step 5 (Search for PO)
- **Condition**: Whether matching PO can be found
- **Outcomes**:
  - **Path A**: PO found → Proceed to Step 7 (Link invoice to PO)
  - **Path B**: PO not found (10-15% of cases) → Proceed to Step 6 (Resolve missing PO) then return to Step 7
- **Decision Maker**: AP Clerk based on search results

### Decision Point 3: Three-Way Match Result
- **Location in Process**: After Step 8 (Three-way match validation)
- **Condition**: Whether invoice matches PO and receiving report within tolerance (5% or $50)
- **Outcomes**:
  - **Path A**: Match successful → Proceed to Decision Point 4 (Approval threshold check)
  - **Path B**: Match fails due to discrepancies → Proceed to Step 9 (Investigate and resolve discrepancies) then return to Step 8
- **Decision Maker**: SAP system automated validation

### Decision Point 4: Approval Threshold Check
- **Location in Process**: After Step 8 (successful three-way match) or after Step 6 (for non-PO invoices)
- **Condition**: Invoice amount and whether invoice has PO
- **Outcomes**:
  - **Path A**: Invoice under $5,000 with PO → Proceed to Step 12 (Auto-approve to payment queue)
  - **Path B**: Invoice $5,000 or more with PO → Proceed to Step 10 (Route for manager approval)
  - **Path C**: Any non-PO invoice regardless of amount → Proceed to Step 10 (Route for manager approval)
- **Decision Maker**: SAP system based on configured rules

### Decision Point 5: Manager Approval Decision
- **Location in Process**: After Step 11 (Manager review)
- **Condition**: Manager's assessment of invoice validity and completeness
- **Outcomes**:
  - **Path A**: Approved → Proceed to Step 12 (Move to payment queue)
  - **Path B**: Rejected → Return to AP Clerk (Step 4 or Step 7) with comments for correction
- **Decision Maker**: AP Manager (Linda)

### Decision Point 6: Payment Validation Success
- **Location in Process**: After Step 13 (Payment batch processing)
- **Condition**: Whether payment passes system validation (primarily vendor banking information)
- **Outcomes**:
  - **Path A**: Validation successful → Proceed to Step 15 (Vendor notification)
  - **Path B**: Validation fails → Proceed to Step 14 (Resolve failed payment) then wait until next payment run (Step 13)
- **Decision Maker**: Banking system automated validation

### Decision Point 7: Payment Notification Success
- **Location in Process**: After Step 15 (automated notification attempt)
- **Condition**: Whether automated payment remittance email successfully delivers to vendor
- **Outcomes**:
  - **Path A**: Email delivers successfully (approximately 50% of cases) → Process complete
  - **Path B**: Email fails or vendor doesn't receive (approximately 50% of cases) → Vendor calls, AP Clerk performs manual lookup and email (Step 15 manual workaround)
- **Decision Maker**: System reliability/vendor receipt (somewhat random)

## Systems and Tools

| System | Purpose | Integration Points |
|--------|---------|-------------------|
| Email (shared AP inbox: ap@company.com) | Receive invoice PDF attachments; team communication | Steps 1, 2, 6, 9, 15 |
| Document Scanner | Scan physical and printed invoices into document management system | Step 3 |
| Document Management System | Store scanned invoice images; integrated with SAP | Step 3, 4, 11 |
| SAP ERP | Core invoice processing system; data entry; PO matching; three-way match; payment processing; vendor management | Steps 4, 5, 6, 7, 8, 10, 12, 13, 14, 15 |
| ERP Vendor Portal | Alternative invoice submission channel for vendors | Step 1 (10-15% of invoices) |
| Third-party Approval Portal | Route and manage invoice approvals; send notifications | Steps 10, 11 |
| Banking System | Process ACH and check payments | Step 13 |
| Printer | Print digital invoices for scanning workaround | Step 3 |
| Phone | Vendor inquiries and communication | Steps 9, 14, 15 |
| Postal Mail | Receive physical invoices | Step 1 |

## Pain Points and Inefficiencies

### Critical Issues

1. **Manual Print-and-Scan Workaround**: ERP system cannot accept direct PDF uploads requiring digital invoices to be printed and scanned back in
   - **Impact**: Waste of time, paper, and equipment; inefficient use of clerk time; unnecessary steps in process
   - **Frequency**: Approximately 60% of invoices (all email invoices)
   - **Affected Steps**: Step 3
   - **Duration**: IT has been requested to fix this for two years with no resolution

2. **Complete Manual Data Entry**: All invoice data must be manually typed into SAP despite being visible in scanned documents
   - **Impact**: 5-10 minutes per invoice; 100-150 invoices per clerk monthly = 10-15 hours per week per clerk; high error rate with mistakes approximately once per week; errors require reprocessing, credit memos, and vendor relationship damage
   - **Frequency**: Every invoice except vendor portal submissions (85-90% of invoices)
   - **Affected Steps**: Step 4
   - **Priority**: Identified by Sarah as #1 fix priority

3. **Three-Way Match Discrepancies**: Failed matches requiring investigation and multi-party resolution
   - **Impact**: Identified as "biggest source of payment delays"; can take days to weeks to resolve; creates vendor frustration; requires coordination between AP, purchasing, and vendors
   - **Frequency**: Specific percentage not provided but described as significant
   - **Affected Steps**: Steps 8, 9

4. **Manager Approval Bottleneck**: Single point of approval creates delays and process backup
   - **Impact**: Supposed to take 24 hours but realistically takes 2-3 days; approval emails get buried; vendor complaints about stuck invoices; especially problematic at month-end; described as "embarrassing"; affects all invoices $5,000+ and all non-PO invoices
   - **Frequency**: All invoices ≥$5,000 with PO + all non-PO invoices
   - **Affected Steps**: Steps 10, 11
   - **Contributing Factors**: Manager workload; separate approval portal system

5. **Poor PO Search Functionality**: Difficult to locate matching POs in SAP
   - **Impact**: Time-consuming searches especially for vendors with multiple POs; slows process; contributes to overall inefficiency
   - **Frequency**: 80% of invoices require PO matching; worse when PO number not on invoice
   - **Affected Steps**: Step 5

6. **Missing PO Resolution Delays**: Process stalls waiting for purchasing team response
   - **Impact**: Invoices sit in queue for days; vendors begin calling about payment status; retroactive PO creation can take days; creates backlog
   - **Frequency**: 10-15% of invoices
   - **Affected Steps**: Step 6

### Inefficiencies

1. **Multiple Invoice Receipt Channels**: No centralized intake process
   - **Current State**: 60% email, 25% mail, 10-15% vendor portal, remaining through various ad-hoc methods
   - **Impact**: Inconsistent handling; complexity in process; different workflows for different channels

2. **Separate Approval Portal System**: Third-party tool not integrated with SAP
   - **Current State**: Requires separate login; SAP sends notification to portal which sends email; approval must be returned from portal to SAP
   - **Impact**: System complexity; additional point of failure; contributes to approval delays

3. **Non-PO Invoice Approval Policy**: All non-PO invoices require manager approval regardless of amount
   - **Current State**: Even $50 office supply invoice requires manager approval
   - **Impact**: Unnecessary approvals burden manager; creates bottleneck for low-risk, low-value invoices; especially problematic at month-end

4. **Payment Frequency**: Bi-weekly payment runs only
   - **Current State**: Payments run only Tuesdays and Fridays
   - **Impact**: Failed payments must wait at least one week until next run; inflexible schedule may delay payments unnecessarily

5. **Unreliable Payment Notification System**: Automated remittance emails fail 50% of the time
   - **Current State**: SAP feature described as "flaky"; only half of vendors receive automated notifications
   - **Impact**: High volume of vendor inquiry calls; manual lookup and email follow-up required; poor vendor experience; wastes clerk time

6. **Vendor Banking Information Management**: Missing or incorrect information causes payment failures
   - **Current State**: Payment failures occur due to incorrect/missing banking details
   - **Impact**: Minimum one-week delay to next payment run; requires vendor outreach; poor vendor experience

7. **Duplicate Invoice Processing**: Inadequate duplicate detection
   - **Current State**: Duplicates slip through when invoice numbers or dates slightly different
   - **Impact**: Occasional double payments requiring awkward refund requests; potential financial loss; vendor relationship issues

8. **Average Payment Timing**: 25-day average against Net 30 terms
   - **Current State**: Little buffer before hitting payment terms; regular delays push past terms
   - **Impact**: Vendors putting company on hold; late fees charged; damaged vendor relationships

## Process Metrics

- **Total Steps**: 16 (including exception paths)
- **Number of Decision Points**: 7
- **Number of Actors**: 8 (3 internal staff roles, plus vendors, purchasing team, and 3 systems)
- **Identified Pain Points**: 13 (7 critical issues, 6 inefficiencies)
- **Manual Steps**: 11 (Steps 2, 3, 4, 5, 6, 7, 9, 11, 14, 15 manual workaround, 16)
- **Systems Involved**: 8 distinct systems/tools
- **Processing Volume**: 300-400 invoices per month across 3-person team (100-150 per clerk)
- **Invoice Channels**: 4 primary channels (email 60%, mail 25%, vendor portal 10-15%, other 5-10%)
- **PO Match Rate**: 80% of invoices have corresponding POs
- **PO Not Found Rate**: 10-15% of invoices
- **Average Days to Pay**: Approximately 25 days (against Net 30 terms)
- **Payment Frequency**: Bi-weekly (Tuesdays and Fridays)
- **Error Rate**: Approximately 1 data entry error per week per clerk
- **Manager Approval SLA**: 24 hours (target) vs. 2-3 days (actual)
- **Automated Notification Success Rate**: Approximately 50%
- **Approval Threshold**: $5,000 (with PO); any amount (without PO)
- **Three-Way Match Tolerance**: 5% or $50, whichever is less

## Notes and Observations

**Worst-Case Scenario Timeline**: Sarah described a worst-case invoice that hits multiple issues: vendor emails invoice → print and scan → data entry → PO not found (3-day delay) → retroactive PO created → price discrepancy → corrected invoice requested (4-day delay) → corrected invoice entered → matches but over $5,000 → approval submitted → manager approval (3-day delay) → payment queue → payment fails due to old banking info → vendor contacted for banking update (few days) → SAP updated → next payment run → remittance notification fails → vendor calls → manual payment details email. **Total timeline: 3-4 weeks.**

**Process Variations**:
- Vendor portal invoices skip print/scan step entirely (already in system)
- Mailed invoices skip printing step (scanned directly)
- Invoices under $5,000 with successful PO match skip manager approval
- Non-PO invoices always require manager approval regardless of amount

**Team Structure**: Three-person AP team with role differentiation:
- AP Clerks (including Sarah): Invoice receipt, data entry, PO matching, vendor communication (100-150 invoices each/month)
- AP Manager (Linda): Approvals for high-value and non-PO invoices
- AP Specialist (Marcus): Payment batch processing, failed payment troubleshooting

**System Integration Gaps**:
- Document management system integrated with SAP but cannot accept direct PDF uploads
- Approval portal is separate third-party system requiring notifications between SAP and portal
- Banking system separate from SAP requiring export process

**Month-End Impact**: Approval bottleneck especially problematic during month-end close when manager is busiest and volume may be higher

**Vendor Relationship Impact**: Multiple pain points damage vendor relationships:
- Long payment timelines with little buffer
- Frequent payment delays past Net 30 terms
- Vendors putting company on hold
- Late fees being charged
- High volume of "where's my payment?" inquiry calls
- Unreliable payment notifications
- Need for refunds when duplicates processed

**Technology Age**: SAP described as "pretty old" - contributing factor to limitations like no direct PDF upload

**Process Improvement Requests**: Team has been requesting IT fixes (specifically print/scan workaround) for two years with no resolution, suggesting organizational challenges beyond the AP process itself

**Risk Areas**:
- Manual data entry errors requiring reprocessing
- Duplicate payments requiring refunds
- Late payment fees and vendor holds
- Single point of failure in manager approval
- Data loss risk in multi-system handoffs