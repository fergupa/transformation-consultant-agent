# Process Analysis: Accounts Payable Invoice Matching and Payment Processing

## Executive Summary
The accounts payable invoice matching and payment processing workflow involves receiving vendor invoices via email or portal, performing manual three-way matching (invoice, purchase order, receiving report) in Oracle ERP, resolving discrepancies through stakeholder communication, obtaining approvals, and executing payment runs three times weekly via ACH or check. The process is heavily manual, relies on Excel tracking outside the ERP system, and experiences significant delays due to data inconsistencies, duplicate invoice issues, and stakeholder response times.

## Process Steps

### Step 1: Receive Invoice
- **Actor/Role**: Vendor / AP Specialist
- **Description**: Invoices arrive primarily through AP email mailbox or vendor portal
- **Input**: Vendor invoice (electronic or paper)
- **Output**: Invoice available for processing
- **Duration/Timing**: Continuous - invoices arrive throughout the month
- **Pain Points**: Multiple channels for invoice receipt (email and portal) with no centralized intake

### Step 2: Log Invoice in Tracking Spreadsheet
- **Actor/Role**: AP Specialist (Jennifer Park)
- **Description**: Manually enter invoice details into Excel tracking spreadsheet including invoice number, vendor, amount, date received, and current status
- **Input**: Received invoice from Step 1
- **Output**: Invoice logged in Excel tracking system
- **Duration/Timing**: Not specified, but must be done for every invoice
- **Pain Points**: Manual data entry required; ERP system lacks adequate tracking visibility for invoices in progress; dependency on personal Excel file for queue management

### Step 3: Check for PO Number
- **Actor/Role**: AP Specialist
- **Description**: Review invoice to determine if it contains a purchase order (PO) number
- **Input**: Invoice from Step 2
- **Output**: Determination of PO vs. non-PO invoice routing
- **Duration/Timing**: Immediate during invoice review
- **Pain Points**: None mentioned for this specific step

### Step 4a: Three-Way Match (PO Invoices) - Retrieve PO Details
- **Actor/Role**: AP Specialist
- **Description**: Search for and retrieve PO in Oracle ERP system using PO number from invoice
- **Input**: Invoice with PO number from Step 3
- **Output**: PO details displayed in Oracle
- **Duration/Timing**: Not specified
- **Pain Points**: None mentioned for this specific step

### Step 5a: Three-Way Match - Compare Invoice to PO and Receiving Report
- **Actor/Role**: AP Specialist
- **Description**: Compare invoice line items (descriptions, quantities, prices) against PO details and receiving report in Oracle to verify match
- **Input**: Invoice, PO details, and receiving report from Oracle
- **Output**: Match verification or identification of discrepancies
- **Duration/Timing**: Variable depending on complexity; descriptions mismatch 30-40% of time requiring investigation
- **Pain Points**: Critical issues with data inconsistency across three documents - descriptions almost never match exactly (invoice says "Widget Model X", PO says "Widget X", receiving says "WGT-X"); requires judgment calls to determine if items are actually the same; quantity mismatches are common (ordered vs. shipped vs. received); price discrepancies require extensive investigation

### Step 6a: Resolve Description Discrepancies
- **Actor/Role**: AP Specialist, Buyer, Warehouse Staff
- **Description**: When descriptions don't match exactly across invoice/PO/receiving, email buyer who created PO or warehouse to confirm items are the same
- **Input**: Mismatched descriptions from Step 5a
- **Output**: Confirmation that items match or identification of actual mismatch
- **Duration/Timing**: Variable - depends on response time from buyer or warehouse (can take days)
- **Pain Points**: Occurs 30-40% of the time; requires manual verification via email; time-consuming waiting for responses; risk of payment error if not verified

### Step 7a: Resolve Quantity Variances
- **Actor/Role**: AP Specialist, potentially Vendor and Buyer
- **Description**: When quantities don't match (ordered vs. shipped vs. received), determine appropriate action - for variances under 5% or under $50, AP specialist adjusts invoice amount and notes it; for larger variances, must contact vendor and buyer for clarification
- **Input**: Quantity mismatch from Step 5a
- **Output**: Adjusted invoice amount or clarification on variance
- **Duration/Timing**: Small variances handled immediately; larger variances can take days awaiting responses
- **Pain Points**: Common occurrence; policy requires clarification for all variances, but following this strictly would prevent completing work; judgment calls made on small variances; invoice sits in queue while waiting for responses on larger variances; vendor pressure for payment during investigation

### Step 8a: Resolve Price Discrepancies
- **Actor/Role**: AP Specialist, Buyer, potentially Contract Manager
- **Description**: Investigate price differences between PO and invoice - verify if legitimate price increase, check for contracts with locked pricing, confirm volume discounts, verify tax and shipping charges
- **Input**: Price mismatch from Step 5a
- **Output**: Approval of price or correction required
- **Duration/Timing**: Can take days waiting for buyer response
- **Pain Points**: Requires investigation of contracts, approved price increases, discounts; invoice held in queue pending investigation; must wait for buyer response; vendor frustration over payment delays, especially for small differences; internal control restrictions prevent paying and adjusting later

### Step 9a: Hold Invoice Pending Resolution
- **Actor/Role**: AP Specialist
- **Description**: Mark invoice in Excel spreadsheet as "on hold - pending buyer response" while awaiting discrepancy resolution; follow up every couple of days
- **Input**: Invoice with unresolved discrepancy from Steps 6a, 7a, or 8a
- **Output**: Invoice status updated; periodic follow-up communications sent
- **Duration/Timing**: Days to weeks depending on response time; follow-ups every couple of days
- **Pain Points**: Invoices accumulate in queue; causes aging and potential late fees; vendor calls and complaints about payment delays; inability to process payment due to internal controls

### Step 4b: Non-PO Invoice Verification
- **Actor/Role**: AP Specialist, Requester/Budget Owner
- **Description**: For invoices without PO, email the requester (person named on invoice) or budget owner for cost center to confirm receipt of goods/services and verify amount is correct
- **Input**: Invoice without PO from Step 3
- **Output**: Confirmation from requester that invoice is valid and amount correct
- **Duration/Timing**: Variable - ranges from immediate response to week or more with multiple reminders
- **Pain Points**: Requires manual email verification; response delays common requiring multiple reminder emails; 15-20% of total invoice volume

### Step 10: Check for Duplicate Invoices
- **Actor/Role**: AP Specialist
- **Description**: Search Oracle for vendor invoices with same amount and date to identify potential duplicates; relies on AP specialist's memory to catch duplicates with different invoice numbers or dates
- **Input**: Invoice being processed
- **Output**: Duplicate identified or invoice cleared for processing
- **Duration/Timing**: Performed during invoice entry
- **Pain Points**: System does not automatically flag duplicates if invoice number or date differs; relies on manual memory; vendors send same invoice multiple times via different channels (email, mail) or with slight variations (different invoice number, changed date); duplicates slip through approximately 1% of time (1-2 per month out of 200 invoices)

### Step 11: Process Duplicate Invoice Detection Failure
- **Actor/Role**: AP Specialist, Vendor
- **Description**: When duplicate payment occurs, identify during month-end reconciliation or when vendor reports it; coordinate with vendor for refund or credit application
- **Input**: Duplicate payment discovered
- **Output**: Refund received or credit applied to future invoice
- **Duration/Timing**: Variable - depends on vendor responsiveness
- **Pain Points**: Embarrassing; ties up company cash; vendors slow to refund or insist on credit to next invoice which complicates accounting

### Step 12: Code Invoice to General Ledger
- **Actor/Role**: AP Specialist
- **Description**: Enter general ledger account codes based on expense type (office supplies, IT expenses, etc.) for financial reporting purposes
- **Input**: Verified and matched invoice
- **Output**: Invoice with GL coding assigned
- **Duration/Timing**: Not specified
- **Pain Points**: None mentioned

### Step 13: Enter Invoice for Payment
- **Actor/Role**: AP Specialist
- **Description**: Enter invoice details into Oracle including invoice number, date, amount, GL codes, payment terms; verify vendor payment method (ACH or check) is set up in system
- **Input**: GL-coded invoice from Step 12
- **Output**: Invoice entered in system and queued for approval
- **Duration/Timing**: Not specified
- **Pain Points**: Some vendors still insist on checks despite preference for ACH

### Step 14: Payment Approval Routing
- **Actor/Role**: AP Manager
- **Description**: AP manager reviews invoices over $10,000 including backup documentation (invoice, PO, receiving report); invoices under $10,000 are automatically approved; all non-PO invoices require manager approval regardless of amount
- **Input**: Invoice entered for payment from Step 13
- **Output**: Approved or rejected invoice
- **Duration/Timing**: Usually 1-2 days; longer during month-end or quarter-end close activities
- **Pain Points**: Approval delays during close periods; some view sub-$50 non-PO approvals as overkill but required by policy

### Step 15: Add to Payment Batch
- **Actor/Role**: System (Oracle)
- **Description**: Approved invoices are added to payment batch for next scheduled payment run
- **Input**: Approved invoices from Step 14
- **Output**: Invoices in payment batch queue
- **Duration/Timing**: Batched until next payment run (Monday, Wednesday, or Friday)
- **Pain Points**: None mentioned

### Step 16: Execute Payment Run
- **Actor/Role**: System (Oracle), AP Specialist
- **Description**: System generates ACH file or prints checks three times per week (Monday, Wednesday, Friday); ACH payments transmitted to bank; checks prepared for mailing
- **Input**: Payment batch from Step 15
- **Output**: ACH file transmitted or checks printed
- **Duration/Timing**: Three times per week - Monday, Wednesday, Friday
- **Pain Points**: None mentioned for this step

### Step 17: Payment Delivery
- **Actor/Role**: Bank (for ACH), Mail Service (for checks)
- **Description**: ACH payments hit vendor bank accounts; checks sent via mail to vendors
- **Input**: ACH file or checks from Step 16
- **Output**: Payment received by vendor
- **Duration/Timing**: ACH - next business day; Checks - variable based on mail delivery time
- **Pain Points**: Check delivery time unpredictable depending on postal service

### Step 18: Send Remittance Advice
- **Actor/Role**: System (Oracle)
- **Description**: System automatically sends email remittance advice to vendors with invoice number and payment amount
- **Input**: Payment processed from Step 16
- **Output**: Remittance advice email sent to vendor
- **Duration/Timing**: Should be automatic upon payment
- **Pain Points**: System feature works unreliably - only approximately 50% of vendors receive automatic remittance advice

### Step 19: Manual Remittance Communication
- **Actor/Role**: AP Specialist
- **Description**: When vendors don't receive automatic remittance advice, they call or email to inquire about payment; AP specialist must manually look up payment details and send to vendor
- **Input**: Vendor inquiry about payment status
- **Output**: Manual remittance details sent to vendor
- **Duration/Timing**: Occurs for approximately 50% of payments
- **Pain Points**: Time-consuming manual process; system automation failure creates extra work

### Step 20: Review Aging Report
- **Actor/Role**: AP Specialist
- **Description**: Weekly review of aging report showing invoices at 30, 60, 90, and over 90 days old; attempt to clear out old invoices by following up on pending items
- **Input**: System-generated aging report
- **Output**: Priority list for follow-up and resolution
- **Duration/Timing**: Weekly review
- **Pain Points**: Invoices typically aged due to pending buyer responses, complicated invoices not yet processed, or vendor disputes; vendors charge late fees and interest past Net 30 terms; frustrating when delays caused by internal response times

### Step 21: Prioritize by Due Date
- **Actor/Role**: AP Specialist
- **Description**: Sort tracking spreadsheet by due date column to prioritize invoices coming due soonest
- **Input**: Excel tracking spreadsheet
- **Output**: Prioritized work queue
- **Duration/Timing**: Ongoing throughout work period
- **Pain Points**: Imperfect system as new invoices constantly arrive; limited ability to prevent late payments when waiting on others for information; requires constant juggling of priorities

## Actors and Roles

| Role | Responsibilities | Systems Used |
|------|-----------------|--------------|
| AP Specialist (Jennifer Park) | Log invoices, perform three-way matching, resolve discrepancies, code to GL, enter for payment, follow up on aging invoices, manual remittance communication, duplicate detection | Excel (tracking spreadsheet), Oracle ERP, Email |
| Vendor | Send invoices, respond to discrepancy inquiries, receive payments, issue refunds for duplicates | Email, Vendor Portal |
| Buyer | Create purchase orders, respond to AP inquiries about PO discrepancies and price differences, verify match issues | Oracle ERP (for PO creation), Email |
| Warehouse Staff | Receive goods, create receiving reports, respond to description verification requests | Oracle ERP (receiving module), Email |
| Requester/Budget Owner | Confirm receipt of goods/services for non-PO invoices, verify invoice amounts | Email |
| AP Manager | Approve payments over $10,000 and all non-PO invoices, review backup documentation | Oracle ERP, Email |
| Bank | Process ACH payments | ACH system |
| Mail Service | Deliver checks to vendors | Not applicable |
| Contract Manager | Provide contract pricing information for price discrepancy resolution (implied, not explicitly mentioned) | Email (implied) |

## Decision Points

### Decision Point 1: PO vs. Non-PO Invoice Routing
- **Location in Process**: After Step 3 (Check for PO Number)
- **Condition**: Presence of purchase order number on invoice
- **Outcomes**:
  - **Path A**: Invoice has PO number → Proceed to Step 4a (Three-Way Match Process)
  - **Path B**: Invoice has no PO number → Proceed to Step 4b (Non-PO Verification)
- **Decision Maker**: AP Specialist based on invoice content

### Decision Point 2: Quantity Variance Threshold
- **Location in Process**: During Step 7a (Resolve Quantity Variances)
- **Condition**: Size of quantity variance (percentage and dollar amount)
- **Outcomes**:
  - **Path A**: Variance under 5% OR under $50 → AP specialist adjusts invoice amount and notes it (immediate resolution)
  - **Path B**: Variance 5% or more AND $50 or more → Contact vendor and buyer for clarification (proceed to Step 9a - Hold Invoice)
- **Decision Maker**: AP Specialist using judgment (policy states all variances should be clarified, but practical necessity drives threshold decision)

### Decision Point 3: Payment Approval Threshold
- **Location in Process**: After Step 13 (Enter Invoice for Payment)
- **Condition**: Invoice amount and PO status
- **Outcomes**:
  - **Path A**: Invoice under $10,000 with PO → Automatically approved, proceed to Step 15
  - **Path B**: Invoice over $10,000 OR non-PO invoice regardless of amount → Requires manager approval (Step 14)
- **Decision Maker**: System-enforced based on amount threshold and PO presence

### Decision Point 4: Payment Method
- **Location in Process**: During Step 16 (Execute Payment Run)
- **Condition**: Vendor payment method setup in system
- **Outcomes**:
  - **Path A**: Vendor set up for ACH → Generate ACH file
  - **Path B**: Vendor set up for check → Print check
- **Decision Maker**: System-based on vendor master data configuration

### Decision Point 5: Remittance Advice Delivery
- **Location in Process**: After Step 18 (Send Remittance Advice)
- **Condition**: Whether automatic system email successfully delivers
- **Outcomes**:
  - **Path A**: System successfully sends remittance advice (approximately 50% of cases) → No further action needed
  - **Path B**: System fails to send or vendor doesn't receive (approximately 50% of cases) → Vendor contacts AP, proceed to Step 19 (Manual Remittance Communication)
- **Decision Maker**: System functionality (unreliable); vendor initiates manual path through inquiry

## Systems and Tools

| System | Purpose | Integration Points |
|--------|---------|-------------------|
| Excel Spreadsheet | Manual tracking of invoice status, queue management, prioritization by due date | Steps 2, 9a, 21 - maintained outside ERP due to system limitations |
| Oracle ERP | Purchase order management, receiving reports, invoice entry, payment processing, vendor master data, GL coding, aging reports | Steps 4a, 5a, 10, 13, 14, 15, 16, 20 |
| Email | Invoice receipt, communication with buyers/warehouse/requesters for discrepancy resolution, vendor inquiries | Steps 1, 6a, 7a, 8a, 9a, 4b, 19 |
| Vendor Portal | Invoice submission channel | Step 1 |
| ACH System | Electronic payment transmission to vendor banks | Steps 16, 17 |
| Mail Service | Physical delivery of checks | Step 17 |
| Remittance Advice Email System | Automatic notification to vendors of payment details (unreliable) | Steps 18, 19 |

## Pain Points and Inefficiencies

### Critical Issues

1. **Three-Way Match Data Inconsistencies**: Descriptions, quantities, and prices rarely match exactly across invoice, PO, and receiving report
   - **Impact**: 30-40% of invoices require manual investigation and judgment calls; significant time consumption (approximately 50% of AP specialist's time); risk of payment errors; delays in payment processing; vendor relationship strain
   - **Frequency**: Occurs in 30-40% of all invoices for description mismatches; quantity and price mismatches also frequent
   - **Affected Steps**: Steps 5a, 6a, 7a, 8a, 9a

2. **Manual Excel Tracking Outside ERP**: AP specialist maintains separate Excel spreadsheet for invoice tracking and status
   - **Impact**: Double data entry; no system visibility into invoice queue and status; process doesn't scale; dependency on individual knowledge; risk of spreadsheet loss or error
   - **Frequency**: Every invoice, continuously
   - **Affected Steps**: Steps 2, 9a, 21

3. **Inadequate Duplicate Invoice Detection**: System doesn't flag duplicates if invoice number or date differs; relies on AP specialist memory
   - **Impact**: 1-2 duplicate payments monthly (1% of volume); cash tied up unnecessarily; embarrassment; time spent recovering funds; accounting complications when vendors apply credits instead of refunds
   - **Frequency**: 1-2 occurrences per month
   - **Affected Steps**: Steps 10, 11

4. **Communication Response Delays**: Waiting for buyers, warehouse staff, and requesters to respond to inquiries
   - **Impact**: Invoice aging; late payment fees and interest charges; vendor frustration and relationship damage; inability to meet payment timelines despite internal control compliance
   - **Frequency**: Common throughout process; delays of days to weeks
   - **Affected Steps**: Steps 6a, 7a, 8a, 9a, 4b, 20

5. **Unreliable Remittance Advice System**: Automatic email remittance advice only works 50% of the time
   - **Impact**: Manual work for approximately 50% of payments; vendor calls and emails; time-consuming lookup and communication
   - **Frequency**: Approximately 50% of all payments
   - **Affected Steps**: Steps 18, 19

### Inefficiencies

1. **Small Variance Policy vs. Practice Gap**: Policy requires clarification of all variances, but practical necessity leads to approval of small variances (under 5% or $50) without verification
   - **Current State**: AP specialist makes judgment calls to adjust small variances without formal approval to maintain productivity
   - **Impact**: Policy non-compliance; potential audit risk; inconsistent application of controls

2. **Multiple Invoice Receipt Channels**: Invoices arrive via email and vendor portal with no centralized intake
   - **Current State**: AP specialist must monitor multiple channels
   - **Impact**: Potential for missed invoices; no single source of truth for invoice receipt

3. **Manual GL Coding**: AP specialist must manually determine and enter GL codes for each invoice
   - **Current State**: Manual selection of account codes based on expense type
   - **Impact**: Time-consuming; potential for coding errors; dependency on specialist knowledge

4. **Fixed Payment Run Schedule**: Payments only processed three times per week
   - **Current State**: Monday, Wednesday, Friday payment runs
   - **Impact**: Potential delays in vendor payment; inability to expedite urgent payments between scheduled runs

5. **Persistent Check Payments**: Some vendors still require checks despite ACH preference
   - **Current State**: Dual payment methods maintained
   - **Impact**: Higher processing costs; unpredictable delivery times; additional administrative overhead

6. **Manual Non-PO Approval Requirement**: All non-PO invoices require manager approval regardless of amount
   - **Current State**: Even $50 invoices without PO must go through approval queue
   - **Impact**: Manager time spent on low-value approvals; processing delays; perceived as overkill by some stakeholders

7. **Lack of Scalability**: Process heavily dependent on manual work and personal knowledge
   - **Current State**: 200 invoices per month manageable with current manual approach
   - **Impact**: Company growth will require additional headcount without process automation; knowledge risk concentrated in individual specialist

## Process Metrics
- **Total Steps**: 21 main process steps (with branching paths for PO vs. non-PO)
- **Number of Decision Points**: 5
- **Number of Actors**: 9 (AP Specialist, Vendor, Buyer, Warehouse Staff, Requester/Budget Owner, AP Manager, Bank, Mail Service, Contract Manager)
- **Identified Pain Points**: 12 (5 critical issues, 7 inefficiencies)
- **Manual Steps**: 17 steps requiring manual intervention
- **Systems Involved**: 7 (Excel, Oracle ERP, Email, Vendor Portal, ACH System, Mail Service, Remittance Advice Email)
- **Monthly Volume**: Approximately 200 invoices
- **PO Invoice Percentage**: 80-85%
- **Non-PO Invoice Percentage**: 15-20%
- **Description Mismatch Rate**: 30-40%
- **Duplicate Payment Rate**: Approximately 1% (1-2 per month)
- **Remittance Advice Failure Rate**: Approximately 50%
- **Payment Frequency**: 3 times per week (Monday, Wednesday, Friday)
- **Approval Threshold**: $10,000 for PO invoices; $0 for non-PO invoices
- **Small Variance Threshold**: Under 5% or under $50 (informal)
- **Standard Payment Terms**: Net 30

## Notes and Observations

- **Time Allocation**: AP specialist estimates approximately 50% of time spent investigating and resolving matching discrepancies, indicating this is the dominant bottleneck in the process

- **Volume and Scaling Concerns**: Current volume of 200 invoices/month is manageable, but Jennifer explicitly notes the process will not scale well with company growth due to manual nature and dependency on individual knowledge

- **Policy vs. Practice**: Acknowledged gap between policy (clarify all variances) and practice (approve small variances under 5%/$50 without verification) driven by practical necessity to maintain productivity

- **System Limitations**: Oracle ERP system has significant gaps: no adequate in-process tracking (requiring Excel workaround), poor duplicate detection, unreliable remittance advice automation, and inability to intelligently match similar but not identical descriptions

- **Vendor Relationship Impact**: Multiple process issues (payment delays, duplicate payments, lack of remittance advice) negatively impact vendor relationships and create unnecessary vendor service burden

- **Control Environment**: Strong control culture (three-way matching, approval thresholds, verification requirements) but controls create processing friction and delays

- **Improvement Priority**: Jennifer identifies intelligent/AI-based matching as #1 desired improvement - system that could recognize variant descriptions as same items and auto-approve small variances would eliminate approximately 50% of manual effort

- **Month-End/Quarter-End Impact**: Approval delays worsen during close periods when AP Manager is focused on other activities

- **Training and Documentation**: No mention of standard operating procedures, training materials, or formal process documentation - suggests knowledge concentrated in individual practitioner

- **Technology Adoption**: Preference for ACH over checks, but incomplete vendor adoption; suggests opportunity for vendor enablement initiative

- **Audit and Compliance Risk**: Duplicate payments, policy deviations on small variances, and manual tracking outside system all represent potential audit findings

- **Financial Impact of Late Payments**: Late fees and interest charges mentioned but not quantified; represents measurable cost of process inefficiencies

- **Seasonal or Cyclical Variations**: No mention of volume fluctuations, seasonality, or year-end spikes that might exist