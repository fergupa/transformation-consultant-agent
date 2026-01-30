# BPMN Generation - Domain Knowledge

## Overview

This directory contains reference materials and example mappings for the BPMN Generation skill:

1. **APQC Activities Reference** - Standard Level 4 activities by domain
2. **Activity Mappings** - Detailed step → APQC activity consolidation for 3 examples
3. **Example BPMN Files** - Reference implementations (future)

These materials demonstrate how to consolidate detailed process steps into APQC Level 4 activities for cleaner, standardized BPMN diagrams.

## Files in This Directory

### 1. apqc-activities.md

**Purpose:** Reference catalog of standard APQC Level 4 activities

**Content:**
- **Finance - Accounts Payable (3.2.x)**: 8 activities
- **Human Resources - Onboarding (4.1.x)**: 9 activities
- **Procurement - Purchase Order Management (5.1.x)**: 7 activities

**Each Activity Includes:**
- APQC code and description
- Typical inputs and outputs
- Common variations
- Usage guidelines

**Usage:**
- Include in system prompt when calling BPMN generation skill
- Reference when mapping detailed steps to activities
- Use standard activity names for consistency

**Example Entry:**
```
### 3.2.1 Receive Vendor Invoice
**Description:** Obtain invoice from vendor through various channels

**Typical Inputs:**
- Vendor invoice (electronic or paper)
- Purchase order reference (if applicable)

**Typical Outputs:**
- Invoice received and available for processing
- Invoice registered in system

**Common Variations:**
- Email receipt, Mail receipt, Vendor portal download, EDI transmission
```

---

### 2. example-01-ap-mapping.md

**Process:** AP Invoice Processing
**Source:** `outputs/analysis/example-01-ap-analysis-test.md`

**Consolidation:**
- **Detailed Steps:** 16 main steps + 6 decision points
- **APQC Activities:** 8 activities
- **Actors:** 8 (AP Clerk, AP Manager, AP Specialist, Purchasing, Vendor, SAP System, Approval Portal, Banking System)
- **Complexity:** Medium-high (multiple exception paths, external systems)

**Key Consolidations:**

| APQC Activity | Consolidated Steps | Rationale |
|--------------|-------------------|-----------|
| **3.2.1 Receive Vendor Invoice** | Steps 1-3 (Receive, Download, Scan) | All relate to obtaining invoice in processable form |
| **3.2.3 Match Invoice to PO** | Steps 5-7 (Search PO, Resolve Missing, Link) | Complete PO matching including exception handling |
| **3.2.4 Verify Invoice Accuracy** | Steps 8-9 (Three-Way Match, Resolve Discrepancies) | Verification with exception path |
| **3.2.5 Route Invoice for Approval** | Steps 10-11 (Route, Manager Review) | Approval workflow with decision point |
| **3.2.6 Process Payment** | Steps 12-14 (Queue, Batch, Failed Payments) | Payment execution including failures |

**Decision Points Preserved:** All 6 (Invoice Channel, PO Found, Match Result, Approval Threshold, Manager Decision, Payment Validation)

**BPMN Patterns Demonstrated:**
- Multiple intake channels (email/mail/portal routing)
- Exception path handling (missing PO, discrepancies, failed payments)
- Loop-backs (resolution → retry)
- External system integration (Banking, Approval Portal)
- Automated vs manual tasks

**Use This Example For:**
- Finance/AP process mapping
- Processes with exception handling
- Multi-actor workflows
- System integration patterns

---

### 3. example-02-onboarding-mapping.md

**Process:** Employee Onboarding
**Source:** `outputs/analysis/example-02-onboarding-analysis-test.md`

**Consolidation:**
- **Detailed Steps:** 20 main steps + 6 decision points
- **APQC Activities:** 9 activities
- **Actors:** 7 (HR Coordinator, New Hire, HR Director, Hiring Manager, IT Department, Facilities, CheckPoint)
- **Complexity:** High (many actors, parallel activities, conditional paths)

**Key Consolidations:**

| APQC Activity | Consolidated Steps | Rationale |
|--------------|-------------------|-----------|
| **4.1.2 Conduct Background Verification** | Steps 2-3 (Initiate Check, Review Results) | Complete background check process with escalation |
| **4.1.4 Provision IT Access and Equipment** | Steps 5-6, 11 (Notify IT, Equipment Provisioning, Account Setup) | All IT-related setup coordinated by HR and IT |
| **4.1.5 Assign Workspace** | Steps 7-8 (Notify Facilities, Workspace Setup) | Workspace assignment from request through completion |
| **4.1.6 Conduct Orientation** | Steps 9, 12-13 (Schedule, First Day, Manager Welcome) | Orientation and first-day activities |
| **4.1.9 Perform Check-Ins** | Steps 14, 18-20 (Buddy Assignment, Check-ins, Follow-up) | Ongoing monitoring and support |

**Decision Points Preserved:** All 6 (Background Check Results, Employment Type, Remote vs On-site, Orientation Alignment, IT Setup Status, Checklist Completion)

**BPMN Patterns Demonstrated:**
- Parallel activities (IT + Facilities provisioning simultaneously for on-site employees)
- Remote vs on-site branching
- Multi-department coordination
- Escalation handling (background check issues)
- Ongoing/recurring activities (check-ins, follow-up)

**Use This Example For:**
- HR onboarding processes
- Multi-department workflows
- Parallel provisioning patterns
- Location-based routing (remote/on-site)

---

### 4. example-03-po-approval-mapping.md

**Process:** Purchase Order Approval
**Source:** `outputs/analysis/example-03-po-approval-analysis-test.md`

**Consolidation:**
- **Detailed Steps:** 10 main steps (plus conditional/exception paths)
- **APQC Activities:** 6 activities
- **Actors:** 8 (Employee, Manager, Department Head, Finance, Procurement, Legal, ERP System, Vendor)
- **Complexity:** Very High (9 decision points, multi-tier sequential approvals, conditional activities)

**Key Consolidations:**

| APQC Activity | Consolidated Steps | Rationale |
|--------------|-------------------|-----------|
| **5.1.1 Initiate Purchase Request** | Steps 1-2, 2a (Submit, Budget Verify, Rejection) | Request submission with automated budget validation |
| **5.1.3 Route for Approval** | Steps 3, 3a (All approval tiers, Rejection/Resubmission) | Multi-tier approval workflow with exception handling |
| **5.1.2 Review Requisition** | Steps 4, 10 (Procurement Review, Urgency Verification) | Procurement validation activities |
| **5.1.5 Conduct Vendor Evaluation** | Steps 5-6 (Vendor Verification, Price Negotiation) | Vendor assessment and pricing |

**Decision Points Preserved:** All 9 (Budget Check, Approval Tier, 3x Approval Decisions, Resubmission, Vendor Status, Negotiation Threshold, Legal Review, Vendor Fulfillment, Urgency)

**BPMN Patterns Demonstrated:**
- Multi-tier sequential approvals (NOT parallel)
- Amount-based routing ($1k, $10k, $50k thresholds)
- Conditional activities (negotiation if >$5k, legal if >$50k)
- Complete process restart on rejection
- Urgency flag verification (exception handling)

**Use This Example For:**
- Procurement/purchasing processes
- Amount-based approval tiers
- Sequential (not parallel) approval chains
- Conditional activity execution
- Complete process restart patterns

---

## APQC Consolidation Patterns

### Pattern 1: Intake/Receipt Consolidation
**When:** Multiple steps to get input into processable form
**Example:** Receive (email) → Download → Scan → Upload
**Consolidate To:** "Receive [Item]" or "Capture [Item]"
**Applies To:** AP Invoice Receipt, Document Intake, Request Submission

### Pattern 2: Verification with Exception Handling
**When:** Automated check + exception investigation
**Example:** Three-way match → Investigate discrepancies
**Consolidate To:** "Verify [Item] Accuracy"
**Applies To:** Invoice Verification, Background Checks, Quality Checks

### Pattern 3: Multi-Step Approvals
**When:** Routing + review + decision
**Example:** Route to manager → Manager reviews → Approve/Reject
**Consolidate To:** "Route for Approval" or "[Level] Approval"
**Applies To:** Any approval workflow

### Pattern 4: Provisioning/Setup Activities
**When:** Request + execution + confirmation
**Example:** Request IT setup → Provision accounts → Deliver credentials
**Consolidate To:** "Provision [Resource]"
**Applies To:** IT Setup, Workspace Assignment, Equipment Provisioning

### Pattern 5: Issuance/Notification
**When:** Creation + sending + acknowledgment
**Example:** Create PO → Send to vendor → Vendor confirms
**Consolidate To:** "Issue [Item]"
**Applies To:** PO Issuance, Payment Processing, Document Distribution

### Pattern 6: Exception Handling (Cross-Cutting)
**When:** Checks and resolutions throughout process
**Example:** Duplicate check, Urgency verification
**Consolidate To:** Separate "Handle Exceptions" activity OR integrate into relevant activities
**Applies To:** Any process with recurring validation

## Decision Point Preservation

**CRITICAL:** Never consolidate steps that are separated by decision points.

**Example - DON'T DO THIS:**
```
❌ BAD: Consolidate Steps 5-9 into "Process Invoice"
  Step 5: Search for PO
  [Decision Point: PO Found?]
    → If No: Step 6: Resolve missing PO
  Step 7: Link to PO
  Step 8: Three-way match
  [Decision Point: Match Successful?]
    → If No: Step 9: Investigate discrepancies
```

**Example - DO THIS:**
```
✓ GOOD: Respect decision boundaries
  Activity 1: "Match Invoice to PO" (Steps 5-7)
    - Search, Resolve (if needed), Link
    - Ends with Decision Point: Match Successful?

  Activity 2: "Verify Invoice Accuracy" (Steps 8-9)
    - Three-way match, Investigate (if needed)
    - Follows after Match Successful decision
```

## Actor Boundary Respect

**GUIDELINE:** Activities should generally be single-actor OR clearly coordinated multi-actor.

**Single-Actor Examples:**
- ✅ "Capture Invoice Data" (AP Clerk only)
- ✅ "Manager Approval" (Manager only)

**Coordinated Multi-Actor Examples:**
- ✅ "Provision IT Access and Equipment" (HR initiates → IT executes)
- ✅ "Conduct Background Verification" (HR initiates → CheckPoint executes → HR reviews)

**DON'T Consolidate:**
- ❌ Steps by different uncoordinated actors
- ❌ Steps where actors work independently (should be parallel activities, not consolidated)

## Usage Guidelines

### When to Use These Examples

**Use example-01-ap-mapping.md when:**
- Mapping Finance/AP processes
- Process has exception paths and rework loops
- Process integrates with external systems
- Need to understand multi-channel intake patterns

**Use example-02-onboarding-mapping.md when:**
- Mapping HR/onboarding processes
- Process has parallel activities (IT + Facilities)
- Process has location-based branching (remote/on-site)
- Multi-department coordination required

**Use example-03-po-approval-mapping.md when:**
- Mapping procurement/purchasing processes
- Process has amount-based routing
- Process has sequential (not parallel) multi-tier approvals
- Process has conditional activities based on thresholds

### How to Apply to New Processes

1. **Read the full process analysis** (all steps, decision points, actors)
2. **Identify APQC domain** (Finance 3.2.x, HR 4.1.x, Procurement 5.1.x, or custom)
3. **Review APQC activities reference** for standard activity names
4. **Look at similar example mapping** for consolidation patterns
5. **Group related steps** into activities following patterns
6. **Verify decision points preserved** (never consolidate across decisions)
7. **Check actor boundaries** (single-actor or coordinated multi-actor)
8. **Document consolidation rationale** in mapping table
9. **Create BPMN** using SKILL.md system prompt

## Future Example BPMN Files

*Planned for after testing phase:*

### example-01-ap-bpmn.xml
- Generated BPMN for AP Invoice Processing
- Demonstrates 8 APQC activities (from 16 steps)
- Shows exception paths, loop-backs, external systems
- Reference implementation for Finance domain

### example-02-onboarding-bpmn.xml
- Generated BPMN for Employee Onboarding
- Demonstrates 9 APQC activities (from 20 steps)
- Shows parallel activities, branching, multi-department flow
- Reference implementation for HR domain

### example-03-po-approval-bpmn.xml
- Generated BPMN for Purchase Order Approval
- Demonstrates 6 APQC activities (from 10 steps)
- Shows sequential approvals, conditional activities, thresholds
- Reference implementation for Procurement domain

## Validation Against Examples

When generating new BPMN diagrams, compare against these examples:

**Structure:**
- Similar step count → similar activity count (8-10 activities per 15-20 steps)
- All decision points preserved as gateways
- All actors mapped to lanes

**Quality:**
- Activity names use APQC standard terminology
- Consolidation rationale is clear
- Decision boundaries respected
- Actor boundaries respected

**Completeness:**
- Exception paths visible
- Loop-backs shown
- Start and end events present
- Flow is traceable

---

**Related Files:**
- `../SKILL.md` - BPMN generation system prompt (uses these references)
- `../README.md` - Developer documentation and usage examples
- `../../transcript-analysis/` - Upstream skill that produces analysis markdown

**Last Updated:** 2026-01-25
