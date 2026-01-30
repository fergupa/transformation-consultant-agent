# Employee Onboarding - Activity Mapping

## Overview

This document maps the detailed Employee Onboarding steps (from transcript analysis) to APQC Level 4 activities for BPMN diagram generation.

**Source Analysis:** `outputs/analysis/example-02-onboarding-analysis-test.md`

**Detailed Steps:** 20 main steps + 6 decision points

**APQC Level 4 Activities:** 9 activities

---

## Activity Mapping Table

| APQC Level 4 Activity | Source Steps | Actor | Rationale |
|----------------------|--------------|-------|-----------|
| **4.1.1 Initiate New Hire Process** | Step 1 | HR Coordinator | Trigger event that begins entire onboarding workflow |
| **4.1.2 Conduct Background Verification** | Steps 2-3 | HR Coordinator, HR Director, Hiring Manager | Complete background check process from initiation through decision |
| **4.1.3 Set Up Employee Record** | Step 4 | HR Coordinator | Single activity to create HRIS record |
| **4.1.4 Provision IT Access and Equipment** | Steps 5-6, 11 | HR Coordinator, IT Department | IT setup from notification through account completion and equipment delivery |
| **4.1.5 Assign Workspace** | Steps 7-8 | HR Coordinator, Facilities Department | Workspace assignment from request through setup (on-site only) |
| **4.1.6 Conduct Orientation** | Steps 9, 12-13 | HR Coordinator, Manager, New Hire | Scheduling, first-day arrival, and orientation activities |
| **4.1.7 Enroll in Benefits** | Steps 10, 15 | HR Coordinator, New Hire | Pre-orientation checklist assignment and completion (includes benefits) |
| **4.1.8 Complete Compliance Training** | Steps 16-17 | HR Coordinator, Manager, New Hire | Both compliance and role-specific training enrollment and completion |
| **4.1.9 Perform Check-Ins** | Steps 14, 18-20 | HR Coordinator, Manager, New Hire | Buddy assignment, check-ins, and ongoing follow-up |

---

## Detailed Activity Breakdown

### Activity 1: Initiate New Hire Process

**APQC Code:** 4.1.1

**Consolidated Steps:**
- Step 1: Receive Signed Offer Letter

**Actor:** HR Coordinator (Michelle Rodriguez)

**Description:** Begin onboarding workflow upon receipt of signed offer letter from candidate

**Input:**
- Signed offer letter from candidate

**Output:**
- Official confirmation that candidate is joining
- Trigger to begin onboarding activities

**Decision Point Preserved:**
- No decision points at this stage

**Rationale for Not Consolidating:**
This is a distinct trigger event that starts the entire process. Represents the formal commitment to onboard.

**Pain Points Rolled Up:**
- Sometimes insufficient lead time if candidate needs to start quickly (ideally 2 weeks before start date)

---

### Activity 2: Conduct Background Verification

**APQC Code:** 4.1.2

**Consolidated Steps:**
- Step 2: Initiate Background Check
- Step 3: Background Check Review and Decision

**Actor:** HR Coordinator, HR Director, Hiring Manager (for escalations)

**Description:** Perform background checks and review results; escalate problematic results for decision

**Input:**
- Signed offer letter, candidate personal information

**Output:**
- Decision to proceed with onboarding, rescind offer, or request additional information

**Decision Point Preserved:**
- Yes - Decision Point 1 (Background Check Results) determines if escalation is needed

**Rationale for Consolidation:**
Both steps are part of the background verification process. Step 3 is the decision subprocess when issues are found. Together they represent the complete verification activity.

**Pain Points Rolled Up:**
- Variable completion time (3-5 days, sometimes longer)
- Delays when candidate lived in multiple states or issues found
- Escalation process required for problematic results (~5% of cases)

---

### Activity 3: Set Up Employee Record

**APQC Code:** 4.1.3

**Consolidated Steps:**
- Step 4: Create Employee Record in HRIS

**Actor:** HR Coordinator

**Description:** Create new hire's employee record in Workday with all required information

**Input:**
- Candidate information, offer details

**Output:**
- Employee record in Workday with auto-generated employee ID

**Decision Point Preserved:**
- Yes - Decision Point 2 (Employment Type) determines full vs contractor onboarding path

**Rationale for Not Consolidating:**
This is a distinct, single-actor activity that stands alone. Creates the foundational record for all subsequent activities.

**Pain Points Rolled Up:**
- None specific to this step (though downstream impacts exist)

---

### Activity 4: Provision IT Access and Equipment

**APQC Code:** 4.1.4

**Consolidated Steps:**
- Step 5: Notify IT for Account and Equipment Setup
- Step 6: Equipment Provisioning (On-site vs Remote)
- Step 11: IT Account Setup Completion

**Actor:** HR Coordinator (initiation), IT Department (execution)

**Description:** Set up user accounts, provide computer and technology equipment

**Input:**
- Employee record information, work location, role requirements

**Output:**
- User accounts created (email, Slack, systems)
- Equipment provisioned (on-site pickup or remote shipment)
- Access credentials provided

**Decision Point Preserved:**
- Yes - Decision Point 3 (Remote vs On-site) determines equipment provisioning path
- Yes - Decision Point 5 (IT Account Setup Status) determines if new hire can begin work

**Rationale for Consolidation:**
All three steps relate to IT provisioning. Steps 5 and 11 are request and completion of account setup. Step 6 is equipment provisioning. Together they represent the complete IT readiness activity.

**Pain Points Rolled Up:**
- Email-based manual process; timing critical for remote employees
- Equipment delays for ~10% of remote hires (late ordering, shipping delays, stock shortages)
- Emergency overnight shipping increases costs when delays occur
- IT account setup failure rate of 15-20% on day one (insufficient lead time, licensing issues, pending manager approvals)
- New hires cannot access systems; poor first impression; sometimes sent home early

---

### Activity 5: Assign Workspace

**APQC Code:** 4.1.5

**Consolidated Steps:**
- Step 7: Notify Facilities for Workspace Assignment
- Step 8: Workspace Setup

**Actor:** HR Coordinator (initiation), Facilities Department (execution)

**Description:** Allocate and prepare physical workspace for on-site employees

**Input:**
- Employee information for on-site employees (department, manager, start date)

**Output:**
- Assigned and equipped workspace (desk, chair, phone, office supplies)

**Decision Point Preserved:**
- No decision points within this activity (though triggered by on-site location from DP3)

**Rationale for Consolidation:**
Both steps are part of workspace provisioning. Request and setup are two parts of the same activity - providing physical workspace.

**Pain Points Rolled Up:**
- Email-based manual process
- Desk unavailability approximately once every couple months during high-volume hiring
- New hires forced to wait for space or sit temporarily in conference rooms
- Fast company growth outpaces office space planning

---

### Activity 6: Conduct Orientation

**APQC Code:** 4.1.6

**Consolidated Steps:**
- Step 9: Schedule Orientation Session
- Step 12: First Day Arrival
- Step 13: Manager First-Day Welcome and Orientation

**Actor:** HR Coordinator (scheduling), Manager, New Hire

**Description:** Provide company overview, policies, culture, and first-day welcome

**Input:**
- New hire schedule, orientation materials, start date

**Output:**
- Orientation completed
- Team introductions
- Office tour
- Initial job overview

**Decision Point Preserved:**
- Yes - Decision Point 4 (Start Date Alignment with Orientation) determines immediate vs delayed formal orientation

**Rationale for Consolidation:**
All three steps relate to orientation and first-day activities. Scheduling, arrival, and orientation/welcome are parts of the same onboarding phase - initial integration.

**Pain Points Rolled Up:**
- Orientation only offered every other Monday (half-day sessions)
- If start date doesn't align, new hire waits up to two weeks and misses critical information
- Highly inconsistent quality of manager preparation
- Some managers have structured plans while others are unprepared
- HR has created first-day/first-week checklists but adoption is poor
- New hires left sitting idle, not knowing basic information, or missing lunch plans

---

### Activity 7: Enroll in Benefits

**APQC Code:** 4.1.7

**Consolidated Steps:**
- Step 10: Assign Pre-Orientation Checklist
- Step 15: Complete Remaining Pre-Orientation Paperwork

**Actor:** HR Coordinator, New Hire

**Description:** Complete benefits selection and enrollment via pre-orientation checklist

**Input:**
- Employee record, benefits options

**Output:**
- Completed direct deposit, emergency contacts, benefits elections, handbook acknowledgment

**Decision Point Preserved:**
- Yes - Decision Point 6 (Pre-Orientation Checklist Completion) determines if follow-up needed

**Rationale for Consolidation:**
Both steps are part of benefits/paperwork enrollment. Step 10 is assignment, Step 15 is completion for those who didn't finish on time. Together they represent the complete enrollment activity.

**Pain Points Rolled Up:**
- Approximately 50% of new hires don't complete checklist before first day
- New hires forget or too busy at previous job
- Requires chasing paperwork during first day/week
- Slows down onboarding and diverts attention from learning job

---

### Activity 8: Complete Compliance Training

**APQC Code:** 4.1.8

**Consolidated Steps:**
- Step 16: Compliance Training Enrollment
- Step 17: Role-Specific Training Enrollment

**Actor:** HR Coordinator, Hiring Manager, New Hire

**Description:** Assign and track mandatory compliance and role-specific training

**Input:**
- Training requirements by role, employee learning profile

**Output:**
- Training assigned, enrolled, and completed
- Certificates issued

**Decision Point Preserved:**
- No decision points (though content varies by role)

**Rationale for Consolidation:**
Both steps are part of training enrollment process. Compliance and role-specific training are different types but same activity pattern - enroll and track completion.

**Pain Points Rolled Up:**
- Manual enrollment process for each new hire
- HR must track completion and send follow-up emails
- Manual coordination between HR and managers
- No automated system; requires emails and tracking

---

### Activity 9: Perform Check-Ins

**APQC Code:** 4.1.9

**Consolidated Steps:**
- Step 14: Buddy/Mentor Assignment
- Step 18: First Week Manager Check-in
- Step 19: 30-Day Check-in Meeting
- Step 20: Ongoing Follow-up and Tracking

**Actor:** HR Coordinator, Hiring Manager, New Hire

**Description:** Conduct regular check-ins to assess progress, provide support, and address issues

**Input:**
- Onboarding timeline, progress milestones, feedback

**Output:**
- Check-ins documented
- Issues identified
- Support provided
- Task tracking and follow-up

**Decision Point Preserved:**
- No decision points

**Rationale for Consolidation:**
All four steps relate to ongoing monitoring and support. Buddy assignment, check-ins, and follow-up are all parts of the integration and tracking activity throughout the onboarding period.

**Pain Points Rolled Up:**
- Buddy/mentor assignment inconsistent across managers
- First-week check-in inconsistent implementation
- 30-day check-ins cancelled by busy managers or those claiming it's not needed
- Issues with struggling/unhappy new hires discovered too late
- HR spends ~50% of time sending manual follow-up emails
- Manual tracking in head or spreadsheet
- No centralized system showing completed, pending, or overdue tasks
- Things fall through the cracks

---

## BPMN Mapping Notes

### Swimlanes (Actors)
1. HR Coordinator (Michelle Rodriguez)
2. New Hire/Candidate
3. HR Director
4. Hiring Manager
5. IT Department
6. Facilities Department
7. CheckPoint (Third-party Service)

**Note:** CheckPoint could be represented as external participant or consolidated into HR Coordinator lane with annotation.

### Start Event
- Process starts with "Offer Letter Received"

### End Event
- Process ends with "30-Day Check-in Complete" or "Onboarding Complete"

### Gateways
- Gateway 1: Background Check Results (XOR - clean/issues)
- Gateway 2: Employment Type (XOR - full-time/contractor) *May exclude contractor path if focusing on full-time*
- Gateway 3: Work Location (XOR - on-site/remote)
- Gateway 4: Orientation Alignment (XOR - start on orientation Monday/other day)
- Gateway 5: IT Setup Status (XOR - systems accessible/not accessible)
- Gateway 6: Checklist Completion (XOR - completed before day 1/not completed)

### Parallel Activities
- Steps 5-8 can occur in parallel: IT provisioning (Steps 5-6, 11) and Facilities workspace assignment (Steps 7-8) happen simultaneously for on-site employees
- Could use parallel gateway after Step 4 to show concurrent IT and Facilities activities

### Loops
- Background Check Issues → Escalation → Decision → May return to verification or terminate
- IT Setup Failure → Troubleshooting → Return to attempt access
- Incomplete Checklist → Follow-up → Return to completion

### Exception Paths
- Background check issues requiring escalation
- IT setup failures requiring troubleshooting or sending new hire home
- Equipment delays requiring overnight shipping
- Desk unavailability requiring temporary seating
- Incomplete paperwork requiring follow-up

---

## Process Metrics (APQC Level 4)

**Original:** 20 detailed steps

**Consolidated:** 9 APQC Level 4 activities

**Actors:** 7 (may consolidate to 6 if CheckPoint shown as external)

**Decision Points:** 6 (all preserved)

**Pain Points:** 12 critical issues (rolled up into 9 activities)

**Volume:** 15-20 new hires per month

**Key Timing:**
- Background check: 3-5 days
- IT equipment lead time (remote): minimum 10 days
- Orientation: every other Monday half-day sessions
- Check-ins: First week, 30 days

---

## Validation Checklist

When creating BPMN from this mapping:

- [ ] All 9 activities present as tasks
- [ ] All 7 actors represented (or 6 if CheckPoint external)
- [ ] All 6 decision points as gateways
- [ ] Exception paths visible (background issues, IT failures, equipment delays, desk unavailability)
- [ ] Parallel flow for IT and Facilities provisioning (on-site path)
- [ ] Loop-back flows implemented (escalations, troubleshooting, follow-ups)
- [ ] Location routing (remote vs on-site) shown
- [ ] Start and end events present
- [ ] Flow traceable from start to end
- [ ] Activity names match APQC standards

---

*This mapping is part of the transformation-consultant-agent BPMN Generation skill domain knowledge.*
