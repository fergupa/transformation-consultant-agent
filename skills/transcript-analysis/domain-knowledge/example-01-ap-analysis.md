# Process Analysis: Accounts Payable Invoice Processing

## Executive Summary
The Accounts Payable invoice processing workflow handles 300-400 invoices monthly across a team of three AP staff members. Invoices arrive through multiple channels (email, mail, vendor portal) and undergo data entry, PO matching, approval routing based on amount thresholds, and bi-weekly payment runs, with significant manual intervention and system integration challenges throughout.

## Process Steps

### Step 1: Receive Invoice
- **Actor/Role**: AP Clerk (Sarah), Vendors
- **Description**: Invoices arrive through multiple channels: 60% via email to shared AP inbox (ap@company.com), 25% via regular mail, 10-15% through vendor portal in ERP system, and remaining via hand-delivery or forwarding from purchasing team
- **Input**: Vendor invoice (various formats and channels)
- **Output**: Invoice received by AP team
- **Duration/Timing**: Continuous/daily
- **Pain Points**: Multiple disparate channels create complexity and inconsistency in intake process

### Step 2: Download and Print Invoice
- **Actor/Role**: AP Clerk
- **Description**: For email invoices, download the PDF attachment and print it to paper (required for subsequent scanning step)
- **Input**: Email invoice PDF attachment
- **Output**: Printed paper invoice
- **Duration/Timing**: A few minutes per invoice
- **Pain Points**: ERP system cannot accept PDF uploads directly, forcing unnecessary print step; wasteful and inefficient process that has been requested to be fixed for two years

### Step 3: Scan Invoice
- **Actor/Role**: AP Clerk
- **Description**: Scan the printed invoice (or directly scan mailed invoices) using document scanner to import into document management system integrated with ERP
- **Input**: Printed invoice (from email) or mailed invoice
- **Output**: Scanned invoice in document management system
- **Duration/Timing**: A few minutes per invoice
- **Pain Points**: Manual scanning required for all email and mail invoices; only vendor portal invoices bypass this step

### Step 4: Manual Data Entry
- **Actor/Role**: AP Clerk
- **Description**: Open SAP ERP system and manually type all invoice details including vendor name, invoice number, invoice date, due date, line items, amounts, tax, and total
- **Input**: Scanned invoice document
- **Output**: Invoice record created in SAP with all fields populated
- **Duration/Timing**: 5-10 minutes per invoice depending on number of line items
- **Pain Points**: Highly manual and time-consuming (10-15 hours per week for AP Clerk); error-prone with mistakes occurring approximately once per week; data already exists in scanned document but must be retyped

### Step 5: Search for Purchase Order
- **Actor/Role**: AP Clerk
- **Description**: Search in SAP for the corresponding purchase order number; if PO number is on invoice, search by that; otherwise search by vendor name and date range and manually review open POs
- **Input**: Invoice data and vendor information
- **Output**: Matching PO identified (or not found)
- **Duration/Timing**: Variable - quick if PO number provided, longer if must search manually
- **Pain Points**: PO number often not on invoice; SAP search functionality is poor; vendors with multiple POs require manual review of each; 10-15% of invoices cannot find matching PO

### Step 6: Handle Missing PO
- **Actor/Role**: AP Clerk, Purchasing Team
- **Description**: If PO cannot be found, email purchasing team to investigate; purchasing either provides PO number, confirms it's a non-PO purchase, or creates PO retroactively
- **Input**: Invoice without matching PO
- **Output**: PO number provided, non-PO confirmation, or retroactive PO creation
- **Duration/Timing**: Can take days; invoice sits in queue waiting
- **Pain Points**: Significant delays while waiting for purchasing response; vendors call asking about payment status; occurs 10-15% of the time

### Step 7: Link Invoice to PO and Perform Three-Way Match
- **Actor/Role**: AP Clerk, SAP System
- **Description**: Link the invoice to the PO in SAP; system automatically performs three-way match checking that invoice quantities and amounts match PO and receiving report within tolerance (5% or $50, whichever is less)
- **Input**: Invoice and PO in SAP
- **Output**: Automatic approval if match successful, or exception flag if mismatch detected
- **Duration/Timing**: Automatic/immediate
- **Pain Points**: When mismatch occurs, requires investigation and resolution which can take days or weeks; mismatches are biggest source of payment delays

### Step 8: Investigate Match Discrepancies
- **Actor/Role**: AP Clerk, Purchasing Team, Vendor
- **Description**: When three-way match fails, check receiving report to identify discrepancy (quantity differences, price differences); contact purchasing or vendor or both to resolve
- **Input**: Failed match with discrepancy details
- **Output**: Resolution and corrected invoice or PO
- **Duration/Timing**: Days to weeks
- **Pain Points**: Major source of payment delays; vendors frustrated by extended timeline; requires coordination across multiple parties

### Step 9: Approval Routing
- **Actor/Role**: SAP System
- **Description**: Route invoice for approval based on amount and PO status; invoices under $5,000 with PO go directly to payment queue; invoices $5,000+ require manager approval; all non-PO invoices require manager approval regardless of amount
- **Input**: Matched and verified invoice
- **Output**: Invoice sent to payment queue or routed to approval portal
- **Duration/Timing**: Automatic/immediate
- **Pain Points**: All non-PO invoices requiring approval creates bottleneck even for small amounts like $50

### Step 10: Manager Approval
- **Actor/Role**: AP Manager (Linda)
- **Description**: For invoices requiring approval, SAP sends notification to third-party approval portal, which emails manager; manager logs into portal, reviews scanned invoice and PO, and clicks approve or reject; approval sends back to SAP to move to payment queue; rejection returns to AP Clerk with comments
- **Input**: Invoice flagged for approval
- **Output**: Approved invoice moves to payment queue, or rejected invoice returns to AP Clerk
- **Duration/Timing**: Supposed to be 24 hours, realistically 2-3 days
- **Pain Points**: Separate approval portal system creates friction; manager email notifications get buried; approval delays cause vendor complaints; particularly bad at month-end when manager is swamped

### Step 11: Payment Run Execution
- **Actor/Role**: AP Specialist (Marcus)
- **Description**: Twice weekly (Tuesdays and Fridays), run payment batch in SAP; system groups all approved invoices due within next 5 days and generates payments
- **Input**: Approved invoices in payment queue
- **Output**: Payment batch generated
- **Duration/Timing**: Twice weekly on fixed schedule
- **Pain Points**: Invoices sometimes get stuck or fail validation requiring troubleshooting; incorrect or missing vendor banking information causes payment failures and delays payment by at least another week

### Step 12: Export to Banking System
- **Actor/Role**: SAP System, Banking System
- **Description**: Export generated payments to banking system; most payments are ACH, some are checks for vendors that don't accept electronic payment
- **Input**: Payment batch from SAP
- **Output**: Payments transmitted to bank
- **Duration/Timing**: Part of payment run process
- **Pain Points**: Vendor banking information errors cause failures at this stage

### Step 13: Vendor Payment Notification
- **Actor/Role**: SAP System, AP Clerk
- **Description**: SAP is configured to automatically send payment remittance emails to vendors, but feature is unreliable and only works about 50% of the time; when automated email fails, vendors call to ask if payment was made, and AP Clerk must look up payment in SAP and manually email vendor the payment number and date
- **Input**: Completed payment
- **Output**: Vendor notified of payment (automatically or manually)
- **Duration/Timing**: Should be automatic; manual followup as needed
- **Pain Points**: Automated notification is "flaky" and only works half the time; results in many vendor calls and manual email responses; time-consuming workaround

## Actors and Roles

| Role | Responsibilities | Systems Used |
|------|-----------------|--------------|
| AP Clerk (Sarah) | Primary invoice processor; receives invoices, performs data entry, matches to POs, investigates discrepancies, handles vendor inquiries; processes 100-150 invoices monthly | Email, Scanner, SAP ERP, Document Management System |
| AP Manager (Linda) | Approves invoices over $5,000 and all non-PO invoices; reviews invoice and PO documentation | Approval Portal, Email |
| AP Specialist (Marcus) | Runs bi-weekly payment batches, troubleshoots payment failures | SAP ERP, Banking System |
| Purchasing Team | Assists with missing or incorrect PO issues, creates retroactive POs | SAP ERP, Email |
| Vendors | Submit invoices through various channels, provide banking information, follow up on payment status | Email, Mail, Vendor Portal, Phone |

## Decision Points

### Decision Point 1: Invoice Receipt Channel
- **Location in Process**: Step 1 (Receive Invoice)
- **Condition**: How vendor chooses to submit invoice
- **Outcomes**:
  - **Path A**: Email (60%) → Proceed to Step 2 (Download and Print)
  - **Path B**: Mail (25%) → Proceed directly to Step 3 (Scan)
  - **Path C**: Vendor Portal (10-15%) → Skip to Step 4 (already in system, no scan needed)
  - **Path D**: Other (hand-delivery, forwarded) → Proceed to Step 3 (Scan)
- **Decision Maker**: Vendor submission method

### Decision Point 2: PO Match Result
- **Location in Process**: Step 5 (Search for Purchase Order)
- **Condition**: Whether matching PO can be found
- **Outcomes**:
  - **Path A**: PO found (85-90%) → Proceed to Step 7 (Link and Three-Way Match)
  - **Path B**: PO not found (10-15%) → Proceed to Step 6 (Handle Missing PO), then return to Step 7
- **Decision Maker**: AP Clerk search results

### Decision Point 3: Three-Way Match Success
- **Location in Process**: Step 7 (Three-Way Match)
- **Condition**: Whether invoice quantities and amounts match PO and receiving report within tolerance (5% or $50)
- **Outcomes**:
  - **Path A**: Match successful → Proceed to Step 9 (Approval Routing)
  - **Path B**: Match fails due to discrepancy → Proceed to Step 8 (Investigate Discrepancies), then return to Step 7 after resolution
- **Decision Maker**: SAP automated matching logic

### Decision Point 4: Approval Requirement - Amount Threshold
- **Location in Process**: Step 9 (Approval Routing)
- **Condition**: Invoice amount and PO status
- **Outcomes**:
  - **Path A**: Invoice has PO and is under $5,000 → Skip approval, proceed directly to Step 11 (Payment Queue)
  - **Path B**: Invoice has PO and is $5,000 or more → Proceed to Step 10 (Manager Approval)
  - **Path C**: Invoice has no PO (any amount) → Proceed to Step 10 (Manager Approval)
- **Decision Maker**: SAP automated routing based on amount threshold and PO presence

### Decision Point 5: Approval Decision
- **Location in Process**: Step 10 (Manager Approval)
- **Condition**: Manager's review of invoice and supporting documentation
- **Outcomes**:
  - **Path A**: Manager approves → Proceed to Step 11 (Payment Queue)
  - **Path B**: Manager rejects → Return to AP Clerk (Step 4 or earlier) with comments for correction
- **Decision Maker**: AP Manager (Linda)

## Systems and Tools

| System | Purpose | Integration Points |
|--------|---------|-------------------|
| Email (ap@company.com) | Receive invoice submissions and communicate with purchasing team and vendors | Steps 1, 6, 8, 13 |
| Document Scanner | Scan paper invoices into digital format | Step 3 |
| Document Management System | Store scanned invoice images, integrated with ERP | Step 3 |
| SAP ERP | Core system for invoice data entry, PO matching, three-way match, approval routing, payment processing | Steps 4, 5, 6, 7, 8, 9, 11, 12, 13 |
| Approval Portal (third-party) | Workflow tool for manager approvals | Steps 9, 10 |
| Banking System | Process ACH and check payments | Step 12 |
| Vendor Portal | Some vendors submit invoices directly into ERP | Step 1 (10-15% of invoices) |

## Pain Points and Inefficiencies

### Critical Issues

1. **Manual PDF Print-Scan Workaround**: ERP system cannot accept PDF uploads directly, forcing AP Clerk to print email invoices and then scan them back in
   - **Impact**: Wasteful process, adds unnecessary steps, time-consuming
   - **Frequency**: Every email invoice (60% of all invoices)
   - **Affected Steps**: Steps 2-3

2. **Extensive Manual Data Entry**: All invoice details must be manually typed into SAP despite being present in scanned document
   - **Impact**: 5-10 minutes per invoice, 10-15 hours per week for AP Clerk; error-prone with mistakes occurring weekly; errors cause payment issues requiring credit memos and reprocessing
   - **Frequency**: Every invoice (100% except vendor portal invoices)
   - **Affected Steps**: Step 4

3. **Poor PO Search Functionality**: SAP search is inadequate, especially when PO number not on invoice
   - **Impact**: Time-consuming manual review of multiple open POs; 10-15% of invoices cannot find matching PO
   - **Frequency**: Frequent - occurs when PO number not provided on invoice
   - **Affected Steps**: Step 5

4. **Missing PO Delays**: When PO cannot be found, invoice waits in queue while purchasing team investigates
   - **Impact**: Multi-day delays, vendor complaints about payment status
   - **Frequency**: 10-15% of invoices
   - **Affected Steps**: Step 6

5. **Match Discrepancy Resolution Time**: Three-way match failures require cross-team investigation
   - **Impact**: Days to weeks delay; identified as "biggest source of payment delays"; vendor frustration
   - **Frequency**: Not specified, but described as significant
   - **Affected Steps**: Step 8

6. **Separate Approval Portal System**: Approval workflow uses third-party system instead of being integrated into SAP
   - **Impact**: Additional system to maintain, extra login required, context switching
   - **Frequency**: Every invoice requiring approval ($5,000+ or no-PO)
   - **Affected Steps**: Steps 9-10

7. **Manager Approval Bottleneck**: Single manager must approve all large and non-PO invoices
   - **Impact**: 2-3 day delays instead of target 24 hours; email notifications get buried; vendor complaints; especially severe at month-end
   - **Frequency**: Every invoice $5,000+ and every non-PO invoice
   - **Affected Steps**: Step 10

8. **Unreliable Payment Notifications**: Automated remittance emails only work 50% of the time
   - **Impact**: Frequent vendor calls asking about payment status; manual lookup and email response required; time-consuming and embarrassing
   - **Frequency**: 50% of all payments
   - **Affected Steps**: Step 13

9. **Payment Failures Due to Banking Information**: Incorrect or missing vendor banking info causes payment failures
   - **Impact**: Delays payment by at least another week; requires vendor contact and system update
   - **Frequency**: Not specified but described as recurring issue
   - **Affected Steps**: Steps 11-12

### Inefficiencies

1. **All Non-PO Invoices Require Approval**: Even small amounts like $50 must go through manager approval if there's no PO
   - **Current State**: Blanket approval requirement regardless of amount
   - **Impact**: Creates unnecessary bottleneck for low-risk, low-value transactions

2. **Duplicate Invoice Detection Failures**: Manual check for duplicates sometimes misses invoices with slightly different numbers or dates
   - **Current State**: Manual detection during data entry
   - **Impact**: Occasional duplicate payments requiring vendor refund; "always awkward"

3. **Multiple Invoice Intake Channels**: Four different channels (email, mail, portal, other) create inconsistency
   - **Current State**: 60% email, 25% mail, 10-15% portal, rest miscellaneous
   - **Impact**: Different handling procedures, complexity in process

4. **Long Average Days to Pay**: Average 25 days with Net 30 terms leaves little buffer
   - **Current State**: Paying right at deadline
   - **Impact**: Any delays cause late payments, vendor holds, late fees

5. **Worst-Case Processing Time**: When multiple issues occur, single invoice can take 3-4 weeks
   - **Current State**: Print/scan issue + missing PO + price discrepancy + approval delay + banking info problem + manual notification
   - **Impact**: Severe vendor relationship damage, frequent occurrence

## Process Metrics
- **Total Steps**: 13 main process steps
- **Number of Decision Points**: 5
- **Number of Actors**: 5 (plus vendors)
- **Identified Pain Points**: 9 critical issues, 5 inefficiencies
- **Manual Steps**: 11 out of 13 steps involve manual intervention
- **Systems Involved**: 7
- **Volume**: 300-400 invoices per month across team; 100-150 per AP Clerk
- **Processing Time**: 5-10 minutes data entry per invoice; average 25 days to pay; worst case 3-4 weeks
- **Error Rate**: Approximately 1 error per week in data entry
- **Match Failure Rate**: 10-15% cannot find PO; additional unknown percentage fail three-way match
- **Approval Delay**: Target 24 hours, actual 2-3 days
- **Notification Failure Rate**: 50% of automated payment notifications fail

## Notes and Observations

- The AP team consists of three people handling 300-400 invoices monthly
- Payment terms are Net 30 with most vendors, but average days to pay is 25, leaving minimal buffer for delays
- Two years of requesting IT to fix PDF upload issue with no resolution
- Vendor portal adoption is only 10-15%, representing opportunity for improvement if expanded
- Payment runs occur on fixed schedule (Tuesdays and Fridays) which may contribute to timing pressures
- Month-end creates particular strain on approval process when manager is busiest
- The process has multiple single points of failure: AP Clerk for data entry, AP Manager for approvals, AP Specialist for payment runs
- If one improvement had to be prioritized, AP Clerk identified eliminating manual data entry as having highest impact (would save 10-15 hours per week and reduce errors significantly)
- Vendor relationship management is negatively impacted throughout: payment status inquiries, late payment concerns, duplicate payment embarrassment
- The combination of manual processes, system integration gaps, and approval bottlenecks creates compounding delays
