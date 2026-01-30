# AP Invoice Processing - Activity Mapping

## Overview

This document maps the detailed AP Invoice Processing steps (from transcript analysis) to APQC Level 4 activities for BPMN diagram generation.

**Source Analysis:** `outputs/analysis/example-01-ap-analysis-test.md`

**Detailed Steps:** 16 main steps + 6 decision points

**APQC Level 4 Activities:** 8 activities

---

## Activity Mapping Table

| APQC Level 4 Activity | Source Steps | Actor | Rationale |
|----------------------|--------------|-------|-----------|
| **3.2.1 Receive Vendor Invoice** | Steps 1-3 | AP Clerk | All steps relate to physically obtaining and preparing invoice for processing (receive → download → scan) |
| **3.2.2 Capture Invoice Data** | Step 4 | AP Clerk | Manual data entry activity - entering invoice information into system |
| **3.2.3 Match Invoice to Purchase Order** | Steps 5-7 | AP Clerk, Purchasing Team (exception) | PO search, resolution of missing POs, and linking invoice to PO |
| **3.2.4 Verify Invoice Accuracy** | Steps 8-9 | SAP System, AP Clerk, Purchasing, Vendor | Three-way match validation and resolution of discrepancies |
| **3.2.5 Route Invoice for Approval** | Steps 10-11 | SAP System, AP Manager | Approval workflow including routing and manager review |
| **3.2.6 Process Payment** | Steps 12-14 | SAP System, AP Specialist | Moving to payment queue, batch processing, and resolving failed payments |
| **3.2.7 Handle Exceptions** | Step 16 | AP Clerk | Duplicate invoice checking (ongoing preventative activity) |
| **3.2.8 Vendor Notification** | Step 15 | SAP System, AP Clerk | Payment notification to vendor |

---

## Detailed Activity Breakdown

### Activity 1: Receive Vendor Invoice

**APQC Code:** 3.2.1

**Consolidated Steps:**
- Step 1: Receive Invoice
- Step 2: Download Email Attachments
- Step 3: Print and Scan Invoice

**Actor:** AP Clerk (Sarah Mitchell)

**Description:** Obtain invoice from vendor through various channels and prepare for processing

**Input:**
- Invoice from vendor (email, mail, portal)

**Output:**
- Invoice in document management system, ready for data entry

**Decision Point Preserved:**
- Yes - Decision Point 1 (Invoice Channel Routing) determines which sub-steps occur

**Rationale for Consolidation:**
All three steps relate to physically receiving and preparing the invoice document. They represent different handling paths for the same high-level activity of "getting the invoice into a processable form."

**Pain Points Rolled Up:**
- Multiple intake channels create inconsistent handling
- Inefficient print-scan workaround due to ERP limitation
- No centralized receipt process

---

### Activity 2: Capture Invoice Data

**APQC Code:** 3.2.2

**Consolidated Steps:**
- Step 4: Manual Data Entry

**Actor:** AP Clerk

**Description:** Extract and enter invoice information into SAP ERP system

**Input:**
- Scanned invoice in document management system

**Output:**
- Invoice data entered into SAP

**Decision Point Preserved:**
- No decision points within this activity

**Rationale for Not Consolidating:**
This is a distinct, single-actor activity that stands alone. 5-10 minutes per invoice, 100-150 invoices per clerk monthly.

**Pain Points Rolled Up:**
- Completely manual despite information being visible in scanned document
- Time-consuming and error-prone (~1 error per week)
- Requires reprocessing when errors reach payment stage

---

### Activity 3: Match Invoice to Purchase Order

**APQC Code:** 3.2.3

**Consolidated Steps:**
- Step 5: Search for Matching Purchase Order
- Step 6: Resolve Missing PO (Exception Path)
- Step 7: Link Invoice to PO

**Actor:** AP Clerk, Purchasing Team (for exceptions)

**Description:** Locate corresponding purchase order and associate with invoice

**Input:**
- Invoice data in SAP

**Output:**
- Invoice linked to PO in system

**Decision Point Preserved:**
- Yes - Decision Point 2 (PO Matching Success) determines if exception path is needed

**Rationale for Consolidation:**
All three steps are part of the PO matching process. Step 6 is an exception handling subprocess within the overall matching activity. The end goal is to have invoice linked to PO.

**Pain Points Rolled Up:**
- Poor SAP search functionality
- PO numbers often not on invoices
- Resolution delays (can take days)
- Invoices sit in queue waiting for response

---

### Activity 4: Verify Invoice Accuracy

**APQC Code:** 3.2.4

**Consolidated Steps:**
- Step 8: Three-Way Match Validation
- Step 9: Investigate and Resolve Discrepancies (Exception Path)

**Actor:** SAP System (automated), AP Clerk, Purchasing Team, Vendor (for exceptions)

**Description:** Validate invoice quantities, amounts, and pricing against PO and receiving report

**Input:**
- Linked invoice and PO with receiving report

**Output:**
- Verified invoice ready for approval routing

**Decision Point Preserved:**
- Yes - Decision Point 3 (Three-Way Match Result) determines if exception path is needed

**Rationale for Consolidation:**
Both steps are part of the verification process. Step 9 is exception handling when automatic verification fails. Together they represent the complete verification activity.

**Pain Points Rolled Up:**
- Discrepancies are biggest source of payment delays
- Resolution can take days or weeks
- Requires coordination between multiple parties
- Vendor frustration due to delays

---

### Activity 5: Route Invoice for Approval

**APQC Code:** 3.2.5

**Consolidated Steps:**
- Step 10: Route for Additional Approval
- Step 11: Manager Approval Review

**Actor:** SAP System, AP Manager (Linda)

**Description:** Send invoice to AP Manager for approval based on amount thresholds

**Input:**
- Successfully matched invoice meeting approval criteria

**Output:**
- Approved invoice or rejected invoice with comments

**Decision Point Preserved:**
- Yes - Decision Point 4 (Approval Threshold Check) determines if this activity is needed
- Yes - Decision Point 5 (Manager Approval Decision) determines approval outcome

**Rationale for Consolidation:**
Both steps are part of the approval workflow. Routing and reviewing are two parts of a single business activity - obtaining management approval.

**Pain Points Rolled Up:**
- Separate third-party approval portal adds complexity
- Manager busy, approval emails buried (2-3 day delays vs. 24-hour target)
- Creates bottleneck, especially at month-end
- All non-PO invoices require approval regardless of amount

---

### Activity 6: Process Payment

**APQC Code:** 3.2.6

**Consolidated Steps:**
- Step 12: Move to Payment Queue (Auto-Approved)
- Step 13: Payment Batch Processing
- Step 14: Resolve Failed Payments (Exception Path)

**Actor:** SAP System (automated), AP Specialist (Marcus)

**Description:** Execute payment to vendor via bi-weekly payment batch

**Input:**
- Approved invoices in payment queue

**Output:**
- Payment processed and exported to banking system

**Decision Point Preserved:**
- Yes - Decision Point 6 (Payment Validation Success) determines if exception path is needed

**Rationale for Consolidation:**
All three steps are part of the payment execution process. Auto-approval and batch processing are the happy path, with failed payment resolution as the exception subprocess.

**Pain Points Rolled Up:**
- Invoices sometimes get stuck or fail validation
- Incorrect/missing vendor banking information causes failures
- Failed payments delay by minimum one week to next batch run
- Requires vendor outreach and coordination

---

### Activity 7: Handle Exceptions

**APQC Code:** 3.2.7

**Consolidated Steps:**
- Step 16: Duplicate Invoice Check

**Actor:** AP Clerk

**Description:** Check for and prevent duplicate invoice processing

**Input:**
- Invoice being entered (during Step 4)

**Output:**
- Confirmation that invoice is not a duplicate

**Decision Point Preserved:**
- No decision points

**Rationale for Not Consolidating:**
This is an ongoing preventative activity that occurs throughout the process. It's shown as a separate activity to highlight the exception handling concern.

**Note:** In BPMN, this could be represented as:
- Separate task in parallel with main flow
- Subprocess within Capture Invoice Data activity
- Annotation on Capture Invoice Data task

**Pain Points Rolled Up:**
- Duplicates sometimes slip through
- Has resulted in paying same invoice twice
- Requires awkward refund requests

---

### Activity 8: Vendor Notification

**APQC Code:** 3.2.8 (adapted - typically part of Process Payment, but separated due to pain points)

**Consolidated Steps:**
- Step 15: Vendor Payment Notification

**Actor:** SAP System (automated with failures), AP Clerk (manual workaround)

**Description:** Notify vendor of payment processing and remittance details

**Input:**
- Processed payment

**Output:**
- Vendor notified of payment details

**Decision Point Preserved:**
- No decision points

**Rationale for Not Consolidating:**
Separated from Process Payment (Activity 6) to highlight the significant pain point. The unreliable notification system (50% failure rate) and resulting manual workarounds justify treating this as a distinct activity.

**Pain Points Rolled Up:**
- Automated notification fails ~50% of the time
- Generates high volume of vendor inquiry calls
- Requires manual lookup and email follow-up
- Time-consuming manual workaround

---

## BPMN Mapping Notes

### Swimlanes (Actors)
1. AP Clerk (Sarah Mitchell)
2. AP Manager (Linda)
3. AP Specialist (Marcus)
4. Purchasing Team
5. Vendor
6. SAP System
7. Approval Portal System
8. Banking System

**Note:** System actors (SAP, Approval Portal, Banking) can be:
- Shown as separate swimlanes for clarity
- Consolidated into single "System" lane
- Represented as automated tasks within human actor lanes

### Start Event
- Process starts with "Invoice Received"

### End Event
- Process ends with "Vendor Notified" (after successful payment)
- Alternative end: "Invoice Rejected" (if manager rejects)

### Gateways
- Gateway 1: Invoice Channel (XOR - 3 paths: email, mail, portal)
- Gateway 2: PO Found? (XOR - yes/no)
- Gateway 3: Match Successful? (XOR - yes/no)
- Gateway 4: Approval Required? (XOR - based on amount and PO status)
- Gateway 5: Manager Approved? (XOR - yes/no)
- Gateway 6: Payment Validation? (XOR - success/failure)

### Loops
- Missing PO → Resolve → Return to Match
- Match Fails → Investigate → Return to Verify
- Payment Fails → Resolve → Return to Payment Queue
- Manager Rejects → Return to Capture or Match (depending on reason)

### Parallel Activities
None explicitly parallel in this process, though duplicate checking (Activity 7) happens concurrently with other activities

---

## Process Metrics (APQC Level 4)

**Original:** 16 detailed steps

**Consolidated:** 8 APQC Level 4 activities

**Actors:** 8 (reduced representation in BPMN)

**Decision Points:** 6 (all preserved)

**Pain Points:** 11 critical issues (rolled up into 8 activities)

**Average Duration:** 25 days end-to-end (unchanged)

**Volume:** 300-400 invoices/month (unchanged)

---

## Validation Checklist

When creating BPMN from this mapping:

- [ ] All 8 activities present as tasks
- [ ] All 8 actors represented (or consolidated appropriately)
- [ ] All 6 decision points as gateways
- [ ] Exception paths visible (missing PO, discrepancies, failed payments)
- [ ] Loop-back flows implemented
- [ ] Channel routing (email/mail/portal) shown
- [ ] Start and end events present
- [ ] Flow traceable from start to end
- [ ] Activity names match APQC standards

---

*This mapping is part of the transformation-consultant-agent BPMN Generation skill domain knowledge.*
