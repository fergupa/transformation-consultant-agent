# Purchase Order Approval - Activity Mapping

## Overview

This document maps the detailed Purchase Order Approval Process steps (from transcript analysis) to APQC Level 4 activities for BPMN diagram generation.

**Source Analysis:** `outputs/analysis/example-03-po-approval-analysis-test.md`

**Detailed Steps:** 10 main steps (plus conditional/exception paths)

**APQC Level 4 Activities:** 6 activities

---

## Activity Mapping Table

| APQC Level 4 Activity | Source Steps | Actor | Rationale |
|----------------------|--------------|-------|-----------|
| **5.1.1 Initiate Purchase Request** | Steps 1-2, 2a | Employee, ERP System | Request submission with automated budget validation |
| **5.1.3 Route for Approval** | Steps 3, 3a | Manager, Department Head, Finance, Employee | Multi-tier approval workflow with rejection handling |
| **5.1.2 Review Requisition** | Steps 4, 10 | Procurement Team | Procurement review of approved requests and urgency verification |
| **5.1.5 Conduct Vendor Evaluation** | Steps 5-6 | Procurement Team | Vendor verification, vetting, and price negotiation |
| **5.1.4 Obtain Legal Review** | Step 7 | Legal Team | Legal review for high-value purchases and service contracts (conditional) |
| **5.1.6 Issue Purchase Order** | Steps 8-9 | Procurement Team, ERP System, Vendor | PO creation and vendor notification |

**Note on Activity Order:** APQC standard order is 5.1.1 → 5.1.2 → 5.1.3, but actual process flow is Initiate (5.1.1) → Route for Approval (5.1.3) → Review Requisition (5.1.2). We preserve actual flow in BPMN while using standard APQC codes.

---

## Detailed Activity Breakdown

### Activity 1: Initiate Purchase Request

**APQC Code:** 5.1.1

**Consolidated Steps:**
- Step 1: Submit Purchase Order Request
- Step 2: Automated Budget Verification
- Step 2a: Budget Rejection (Exception Path)

**Actor:** Employee (Requester), ERP System (automated)

**Description:** Create and submit requisition for goods or services with automated budget validation

**Input:**
- Need to purchase item or service
- Budget code, item description, quantity, estimated cost, vendor name, business justification

**Output:**
- Budget-verified PO request ready for approval routing, or
- Rejected request with notification if insufficient budget

**Decision Point Preserved:**
- Yes - Decision Point 1 (Budget Verification Check) determines pass/fail outcome

**Rationale for Consolidation:**
Request submission and budget verification are tightly coupled. Budget check is automated and immediate, serving as validation gate before approval routing begins.

**Pain Points Rolled Up:**
- 20-25% of requests incomplete when first submitted (missing product details, model numbers, vendor names, vague justification)
- Requesters don't read provided checklists and guidelines
- Month-end submission spikes create workload concentration
- Automated budget rejection viewed positively (saves procurement team time)

---

### Activity 2: Route for Approval

**APQC Code:** 5.1.3

**Consolidated Steps:**
- Step 3: Approval Routing (Tier 1 - Under $1,000; Tier 2 - $1,000-$10,000; Tier 3 - Over $10,000)
- Step 3a: Rejection and Resubmission (Exception Path)

**Actor:** Direct Manager, Department Head, Finance, Employee (for resubmission)

**Description:** Send requisition through approval workflow based on amount thresholds; handle rejections

**Input:**
- Budget-verified PO request
- Approval thresholds ($1,000, $10,000)

**Output:**
- Approved requisition ready for procurement review, or
- Rejected request returned to requester (with option to modify and resubmit or cancel)

**Decision Point Preserved:**
- Yes - Decision Point 2 (Approval Tier Determination) routes to correct approval tier
- Yes - Decision Point 3 (Approval or Rejection) at each approval level
- Yes - Decision Point 4 (Resubmission Decision) if rejected

**Rationale for Consolidation:**
All three approval tiers are variants of the same activity - obtaining management authorization. Exception path (rejection/resubmission) is part of the approval activity flow.

**Pain Points Rolled Up:**
- Tier 1 (under $1k): Works well, same-day or next-day approval
- Tier 2 ($1k-$10k): Delays occur when approvers out of office or busy; sequential nature means one delay holds up entire process (2-3 days typical)
- Tier 3 (over $10k): Finance approval bottleneck - only 2 people authorized, handle multiple approval types, POs sit in queue for days (3-7+ days typical)
- Sequential approvals create dependency chains; one person's absence delays entire process
- Rejection requires complete resubmission starting from beginning (frustrating, significantly extends timeline)

---

### Activity 3: Review Requisition

**APQC Code:** 5.1.2

**Consolidated Steps:**
- Step 4: Procurement Team Review
- Step 10: Urgency Flag Verification (Conditional)

**Actor:** Procurement Team (David Park + 2 specialists)

**Description:** Validate requisition for completeness, reasonableness, and accurate urgency classification

**Input:**
- Fully approved PO request
- Urgency flag (if marked urgent/emergency)

**Output:**
- Procurement-verified request ready for vendor evaluation
- Verified urgency status

**Decision Point Preserved:**
- Yes - Decision Point 9 (Urgency Flag Verification) determines if manager confirmation needed

**Rationale for Consolidation:**
Both steps are part of procurement's review activities. Urgency verification is a conditional check that occurs during procurement review to prevent abuse.

**Pain Points Rolled Up:**
- Manual review process
- Lack of dashboard visibility makes tracking difficult - must manually look up individual requests
- Status update emails consume 5-10 hours per week
- Urgency flag abuse (~once per week); requesters misuse flags to expedite non-urgent requests
- Verification process added to combat abuse but slows genuinely urgent requests

---

### Activity 4: Conduct Vendor Evaluation

**APQC Code:** 5.1.5

**Consolidated Steps:**
- Step 5: Vendor Verification
- Step 6: Price Negotiation (Conditional)

**Actor:** Procurement Team

**Description:** Assess vendor qualifications and negotiate pricing/terms

**Input:**
- Procurement-verified request
- Approved vendor list
- Purchase amount (for negotiation threshold)

**Output:**
- Verified vendor (existing or newly vetted)
- Final negotiated price and terms (if applicable)

**Decision Point Preserved:**
- Yes - Decision Point 5 (Vendor Approved Status) determines if vetting needed
- Yes - Decision Point 6 (Price Negotiation Threshold) determines if negotiation attempted

**Rationale for Consolidation:**
Vendor verification and price negotiation are both vendor-related evaluation activities performed by procurement. Together they ensure vendor legitimacy and optimal pricing.

**Pain Points Rolled Up:**
- 20-30% of requests involve vendors not on approved list (particularly Engineering, IT, Marketing)
- New vendor vetting adds 3-5 days to process timeline
- New vendor vetting requires business information, credit check, legitimacy verification
- Price negotiation timeline variability (few hours to few days) depends on vendor responsiveness
- May require waiting on vendor quotes

---

### Activity 5: Obtain Legal Review

**APQC Code:** 5.1.4

**Consolidated Steps:**
- Step 7: Legal Review (Conditional)

**Actor:** Legal Team

**Description:** Review contracts, terms, and conditions for legal compliance

**Input:**
- Purchase over $50,000 OR service contract with ongoing commitments
- Vendor's terms and conditions

**Output:**
- Legal approval
- Risk assessment documented

**Decision Point Preserved:**
- Yes - Decision Point 7 (Legal Review Required) determines if review needed

**Rationale for Not Consolidating:**
This is a distinct, specialized activity performed by separate department. Only applies to ~5% of POs but has significant impact on timeline.

**Pain Points Rolled Up:**
- Can add a week or more depending on legal team backlog
- Significant timeline extension for high-value purchases
- Affects approximately 5% of POs (10-13 per month at current volume)

---

### Activity 6: Issue Purchase Order

**APQC Code:** 5.1.6

**Consolidated Steps:**
- Step 8: Create Official Purchase Order
- Step 9: Send PO to Vendor

**Actor:** Procurement Team, ERP System (automated sending), Vendor (acknowledgment)

**Description:** Create and send formal purchase order to vendor

**Input:**
- Completed negotiations and approvals
- Final price, terms, delivery date, payment terms, shipping address

**Output:**
- PO created with assigned PO number
- PO sent to vendor
- Vendor acknowledgment (ideally)

**Decision Point Preserved:**
- Yes - Decision Point 8 (Vendor Fulfillment Capability) determines if vendor can fulfill or rework needed

**Rationale for Consolidation:**
PO creation and sending are two parts of the same activity - issuing the formal purchase authorization to vendor. Sending is automated but includes vendor acknowledgment loop.

**Pain Points Rolled Up:**
- Vendors poor at acknowledging POs - approximately 40% require manual follow-up by phone
- Uncertainty about vendor receipt
- Time spent tracking down vendors (80-100 POs per month require follow-up)
- 10% of vendors report inability to fulfill on requested timeline requiring rework with requester

---

## Exception Handling Patterns

**Note:** Exception handling is cross-cutting, not a sequential activity. Key exception patterns:

### Budget Rejection (Step 2a)
- Automated rejection with email notification
- Process terminates unless requester finds budget or reduces amount

### Approval Rejection (Step 3a)
- Can occur at any approval tier
- Returns to requester with rejection reason
- Requester can cancel or modify and completely restart process

### New Vendor Vetting (Step 5 variation)
- Adds 3-5 days for vendors not on approved list
- Affects 20-30% of requests

### Vendor Fulfillment Issues (after Step 9)
- 10% of vendors cannot fulfill on requested timeline
- Requires requester decision: wait for delayed delivery or find new vendor

### Urgency Flag Abuse (Step 10)
- Conditional verification when urgent/emergency flag present
- Manager confirmation required before expediting

---

## BPMN Mapping Notes

### Swimlanes (Actors)
1. Employee/Requester
2. Direct Manager
3. Department Head
4. Finance
5. Procurement Team (David Park + 2 specialists)
6. Legal Team
7. ERP System
8. Vendor

**Note:** Could consolidate Managers into single "Approvers" lane or keep separate for clarity of approval tiers.

### Start Event
- Process starts with "Purchase Need Identified"

### End Events
- Primary end: "Purchase Order Issued to Vendor"
- Alternative ends: "Request Cancelled" (budget rejection or requester cancellation)

### Gateways
- Gateway 1: Budget Verification (XOR - pass/fail)
- Gateway 2: Approval Tier (XOR - 3 paths based on amount: <$1k, $1k-$10k, >$10k)
- Gateway 3: Manager Approval Decision (XOR - approve/reject) - Tier 1
- Gateway 4: Department Head Approval Decision (XOR - approve/reject) - Tier 2
- Gateway 5: Finance Approval Decision (XOR - approve/reject) - Tier 3
- Gateway 6: Resubmission Decision (XOR - cancel/modify-resubmit)
- Gateway 7: Urgency Flag Check (XOR - urgent/normal)
- Gateway 8: Vendor on Approved List (XOR - yes/no, determines 3-5 day delay)
- Gateway 9: Negotiation Threshold (XOR - over $5k/under $5k)
- Gateway 10: Legal Review Required (XOR - over $50k or service contract/neither)
- Gateway 11: Vendor Fulfillment Capability (XOR - can fulfill/cannot fulfill)

### Sequential Approval Flow
Important: Tier 2 and Tier 3 approvals are **sequential** (not parallel)
- Tier 2: Manager approves → THEN Department Head approves
- Tier 3: Manager approves → THEN Department Head approves → THEN Finance approves
- Sequential nature is source of significant delays

### Loops
- Budget Fail → Process End (no loop, must start new request)
- Approval Rejection → Modify Request → Return to Step 1 (complete restart)
- Vendor Cannot Fulfill → Find New Vendor → Return to Vendor Verification (Step 5)

### Conditional Paths
- Urgency verification: Conditional check during procurement review (Step 10)
- Price negotiation: Only if purchase over $5,000 (Step 6)
- Legal review: Only if over $50,000 OR service contract (Step 7)
- New vendor vetting: Only if vendor not on approved list (Step 5 variation)

---

## Process Metrics (APQC Level 4)

**Original:** 10 detailed steps (plus conditional/exception paths)

**Consolidated:** 6 APQC Level 4 activities

**Actors:** 8

**Decision Points:** 9 (all preserved)

**Pain Points:** 11 critical issues (6 critical, 5 inefficiencies)

**Volume:** 200-250 POs per month

**Duration Range:**
- Simple (under $1k): 1-2 days
- Medium ($1k-$10k): 2-3 days
- Complex (over $10k): 3-7+ days
- With legal review: Add 1+ week

**Key Rates:**
- Incomplete requests: 20-25%
- New vendor vetting: 20-30%
- Budget rejection: 5-10%
- Vendor non-acknowledgment: 40%
- Vendor fulfillment issues: 10%
- Legal review required: 5%

---

## Validation Checklist

When creating BPMN from this mapping:

- [ ] All 6 activities present as tasks
- [ ] All 8 actors represented (or consolidated appropriately)
- [ ] All 9 decision points as gateways
- [ ] Three approval tier paths clearly shown (Tier 1, 2, 3)
- [ ] Sequential approval flow (not parallel) for Tier 2 and Tier 3
- [ ] Exception paths visible (budget rejection, approval rejection, vendor issues)
- [ ] Loop-back flow for rejected requests (returns to Step 1)
- [ ] Conditional paths for urgency, negotiation, legal review, new vendor vetting
- [ ] Start and end events present (including alternative end for cancellation)
- [ ] Flow traceable from start to end through all paths
- [ ] Activity names match APQC standards

---

## Key BPMN Design Decisions

### Sequential vs Parallel Approvals
Approvals must be shown as **sequential** (using sequence flows) not parallel:
- Tier 2: Manager → Department Head (one after the other)
- Tier 3: Manager → Department Head → Finance (one after the other)
- This sequential dependency is the source of delays

### Amount-Based Routing
Gateway 2 (Approval Tier) routes to three different paths based on purchase amount. Each path has different approval chains before converging back to procurement review.

### Conditional Activities
Steps 6, 7, and 10 are conditional:
- Could be shown as tasks with XOR gateways to bypass
- Or could be shown in separate paths that rejoin

### Exception Handling
- Budget rejection: Direct path to End Event
- Approval rejection: Loop back to Start Event (complete restart)
- Vendor issues: Loop back to Vendor Evaluation activity

---

*This mapping is part of the transformation-consultant-agent BPMN Generation skill domain knowledge.*
