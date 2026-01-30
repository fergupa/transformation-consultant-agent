# APQC Level 4 Activities Reference

This document defines standard APQC Level 4 activities for common business process domains. Use these as reference when consolidating detailed process steps into BPMN activities.

## Purpose

APQC (American Productivity & Quality Center) provides a standard process classification framework. Level 4 represents **Activities** - the key building blocks of processes that group related tasks together.

**Benefits:**
- Standardized process language across organizations
- Enables benchmarking and comparison
- Simplifies process diagrams
- Focuses on what is done, not how

## Finance - Accounts Payable

### 3.2.1 Receive Vendor Invoice
**Description:** Obtain invoice from vendor through various channels (email, mail, portal, etc.)

**Typical Inputs:**
- Vendor invoice (electronic or paper)
- Purchase order reference (if applicable)

**Typical Outputs:**
- Invoice received and available for processing
- Invoice registered in system

**Common Variations:**
- Email receipt
- Mail receipt
- Vendor portal download
- Hand-delivery
- EDI transmission

---

### 3.2.2 Capture Invoice Data
**Description:** Extract and enter invoice information into accounts payable system

**Typical Inputs:**
- Received invoice (physical or electronic)

**Typical Outputs:**
- Invoice data entered in AP system
- Digital invoice image/record

**Common Variations:**
- Manual data entry
- OCR/automated capture
- Portal direct entry
- EDI automated load

---

### 3.2.3 Match Invoice to Purchase Order
**Description:** Locate and associate invoice with corresponding purchase order

**Typical Inputs:**
- Invoice data
- PO number or supplier information

**Typical Outputs:**
- Invoice matched to PO
- Matching status documented

**Common Variations:**
- 2-way match (invoice + PO)
- 3-way match (invoice + PO + receipt)
- 4-way match (+ inspection)

---

### 3.2.4 Verify Invoice Accuracy
**Description:** Validate invoice amounts, quantities, pricing, and calculations

**Typical Inputs:**
- Invoice details
- PO details (if matched)
- Receipt/delivery confirmation
- Contract pricing

**Typical Outputs:**
- Verification result (approved/exception)
- Documented variances if any

**Common Variations:**
- Quantity verification
- Price verification
- Calculation verification
- Tax verification
- Tolerance checking

---

### 3.2.5 Route Invoice for Approval
**Description:** Send invoice to appropriate approver(s) based on amount thresholds and business rules

**Typical Inputs:**
- Verified invoice
- Approval workflow rules
- Amount thresholds

**Typical Outputs:**
- Invoice submitted for approval
- Approver notified

**Common Variations:**
- Single-level approval
- Multi-level approval
- Parallel approval
- Sequential approval
- Amount-based routing

---

### 3.2.6 Process Payment
**Description:** Execute payment to vendor according to terms

**Typical Inputs:**
- Approved invoice
- Payment terms
- Vendor payment method

**Typical Outputs:**
- Payment initiated
- Payment confirmation
- Accounts updated

**Common Variations:**
- ACH/wire transfer
- Check payment
- Credit card payment
- Batch payment run
- Individual payment

---

### 3.2.7 Handle Exceptions
**Description:** Resolve invoice discrepancies, holds, and issues

**Typical Inputs:**
- Exception notice
- Invoice details
- Problem description

**Typical Outputs:**
- Exception resolved or escalated
- Corrective action taken

**Common Variations:**
- Quantity variance resolution
- Price dispute
- Missing documentation
- Duplicate invoice check
- Vendor inquiry

---

### 3.2.8 Close Invoice
**Description:** Finalize invoice processing and update accounting records

**Typical Inputs:**
- Paid invoice
- Payment confirmation

**Typical Outputs:**
- Invoice closed in system
- GL entries completed
- Records archived

---

## Human Resources - Onboarding

### 4.1.1 Initiate New Hire Process
**Description:** Begin onboarding workflow upon offer acceptance

**Typical Inputs:**
- Signed offer letter
- Candidate information
- Start date

**Typical Outputs:**
- Onboarding case created
- Stakeholders notified
- Timeline established

---

### 4.1.2 Conduct Background Verification
**Description:** Perform background checks, reference checks, and screening

**Typical Inputs:**
- Candidate consent
- Personal information
- Reference contacts

**Typical Outputs:**
- Background check results
- Decision to proceed or not

**Common Variations:**
- Criminal background check
- Credit check
- Employment verification
- Education verification
- Reference checks

---

### 4.1.3 Set Up Employee Record
**Description:** Create employee profile in HRIS with all required information

**Typical Inputs:**
- New hire personal information
- Job details (title, department, manager)
- Employment type and compensation

**Typical Outputs:**
- Employee record created
- Employee ID assigned
- Profile available in HRIS

---

### 4.1.4 Provision IT Access and Equipment
**Description:** Set up user accounts, provide computer and technology equipment

**Typical Inputs:**
- Employee information
- Role/department
- Work location (remote vs. on-site)

**Typical Outputs:**
- User accounts created
- Equipment provisioned
- Access credentials provided

**Common Variations:**
- On-site equipment pickup
- Remote equipment shipment
- BYOD setup
- System access provisioning
- Software license assignment

---

### 4.1.5 Assign Workspace
**Description:** Allocate and prepare physical workspace for on-site employees

**Typical Inputs:**
- Employee information
- Department/team
- Start date

**Typical Outputs:**
- Workspace assigned
- Desk/office prepared
- Supplies provided

---

### 4.1.6 Conduct Orientation
**Description:** Provide company overview, policies, culture, and benefits information

**Typical Inputs:**
- New hire schedule
- Orientation materials
- Welcome packet

**Typical Outputs:**
- Orientation completed
- Key information communicated
- Acknowledgments signed

**Common Variations:**
- Group orientation session
- One-on-one orientation
- Virtual orientation
- Department orientation
- Buddy/mentor assignment

---

### 4.1.7 Enroll in Benefits
**Description:** Complete benefits selection and enrollment

**Typical Inputs:**
- Benefits options
- Employee elections
- Enrollment window

**Typical Outputs:**
- Benefits enrolled
- Deductions configured
- Confirmation provided

---

### 4.1.8 Complete Compliance Training
**Description:** Assign and track mandatory compliance and safety training

**Typical Inputs:**
- Training requirements by role
- Employee learning profile

**Typical Outputs:**
- Training assigned
- Completion tracked
- Certificates issued

**Common Variations:**
- Anti-harassment training
- Data security training
- Safety training
- Code of conduct
- Role-specific compliance

---

### 4.1.9 Perform Check-Ins
**Description:** Conduct regular check-ins to assess progress and address issues

**Typical Inputs:**
- Onboarding timeline
- Progress milestones
- Feedback

**Typical Outputs:**
- Check-in documented
- Issues identified
- Support provided

**Common Variations:**
- Day 1 check-in
- Week 1 check-in
- 30-day check-in
- 60-day check-in
- 90-day review

---

## Procurement - Purchase Order Management

### 5.1.1 Initiate Purchase Request
**Description:** Create and submit requisition for goods or services

**Typical Inputs:**
- Business need
- Item/service specifications
- Estimated cost

**Typical Outputs:**
- Purchase requisition created
- Requisition submitted

---

### 5.1.2 Review Requisition
**Description:** Validate requisition for completeness, accuracy, and business justification

**Typical Inputs:**
- Purchase requisition
- Budget availability
- Business case

**Typical Outputs:**
- Requisition reviewed
- Approved to proceed or rejected

**Common Variations:**
- Budget check
- Policy compliance review
- Technical specification review
- Substitute item suggestion

---

### 5.1.3 Route for Approval
**Description:** Send requisition through approval workflow based on amount and type

**Typical Inputs:**
- Requisition details
- Approval thresholds
- Routing rules

**Typical Outputs:**
- Approvals obtained
- Requisition authorized

**Common Variations:**
- Manager approval
- Director approval
- Executive approval
- Budget owner approval
- Parallel approvals

---

### 5.1.4 Obtain Legal Review
**Description:** Review contracts, terms, and conditions for legal compliance

**Typical Inputs:**
- Purchase agreement
- Contract terms
- Vendor information

**Typical Outputs:**
- Legal review completed
- Terms approved or revised
- Risk assessment documented

---

### 5.1.5 Conduct Vendor Evaluation
**Description:** Assess vendor qualifications, capabilities, and pricing

**Typical Inputs:**
- Vendor information
- Requirements
- Evaluation criteria

**Typical Outputs:**
- Vendor selected
- Justification documented

**Common Variations:**
- Existing vendor renewal
- New vendor vetting
- RFP/RFQ process
- Competitive bidding
- Single source justification

---

### 5.1.6 Issue Purchase Order
**Description:** Create and send formal purchase order to vendor

**Typical Inputs:**
- Approved requisition
- Vendor details
- Item specifications

**Typical Outputs:**
- PO created and sent
- PO number assigned
- Vendor acknowledged

---

### 5.1.7 Handle Exceptions
**Description:** Resolve issues with requisitions, approvals, or vendor concerns

**Typical Inputs:**
- Exception notice
- Problem details
- Stakeholder feedback

**Typical Outputs:**
- Exception resolved
- Process continued or canceled

**Common Variations:**
- Budget insufficient
- Vendor unavailable
- Specification changes
- Approval denied
- Compliance issues

---

## Usage Guidelines

### When to Use APQC Level 4 Activities

Use these standardized activities when:
1. Creating BPMN diagrams from process analysis
2. Consolidating detailed steps into meaningful activities
3. Comparing processes across organizations
4. Designing process improvements

### When to Adapt or Extend

You may need to adapt when:
- Organization-specific activities don't fit standard categories
- Industry-specific processes require specialized activities
- Process complexity warrants sub-activity breakdown
- Combining activities creates ambiguity

### Mapping Principles

1. **Preserve Decision Points**: Don't consolidate steps that are separated by decision points
2. **Respect Actor Boundaries**: Activities should generally be performed by a single actor
3. **Maintain Logical Flow**: Grouped steps should form a cohesive, related activity
4. **Use Standard Names**: Prefer APQC standard names over custom terminology
5. **Stay at Level 4**: Don't go too detailed (Level 5 tasks) or too high-level (Level 3 processes)

---

## References

- APQC Process Classification Framework (PCF)
- https://www.apqc.org/process-frameworks
- Version: Cross Industry PCF v7.x

---

*This reference is part of the transformation-consultant-agent BPMN Generation skill.*
