# Domain Knowledge Examples

This directory contains example transcript-analysis pairs that demonstrate the expected input format and output structure for the transcript-analysis skill. These examples serve as reference implementations showing how the skill should extract and structure process information from conversational interviews.

## Purpose

These examples help the transcript-analysis skill understand:
- What realistic business process transcripts look like
- How to identify and extract key process elements
- The expected markdown output format and level of detail
- How to handle different types of process complexity

## Examples Overview

### Example 1: Accounts Payable Invoice Processing
**Files:** `example-01-ap-transcript.txt`, `example-01-ap-analysis.md`

**Process Type:** Complex, Multi-Actor Process

**Characteristics:**
- Multiple systems and integration points (7 systems)
- 13 process steps with extensive manual intervention
- Multiple actors (AP Clerk, Manager, Specialist, Purchasing, Vendors)
- Several decision points (receipt channel, PO matching, amount thresholds, three-way match)
- Numerous pain points throughout (manual data entry, system limitations, approval delays)
- High volume (300-400 invoices/month)

**What This Example Demonstrates:**
- Handling transcripts with many systems and actors
- Extracting extensive pain points and inefficiencies
- Capturing detailed workflow with multiple exception paths
- Documenting process metrics and timing information
- Identifying both critical issues and minor inefficiencies
- Analyzing worst-case scenarios described by interviewees

**Key Learning Points:**
- Extract all pain points mentioned, even when interviewee casually mentions them ("kind of annoying")
- Capture timing information when provided ("5-10 minutes per invoice", "2-3 days")
- Document frequency and volume metrics
- Note when systems don't integrate well
- Identify single points of failure (manager approval bottleneck)

### Example 2: Employee Onboarding
**Files:** `example-02-onboarding-transcript.txt`, `example-02-onboarding-analysis.md`

**Process Type:** Sequential, Coordination-Heavy Process

**Characteristics:**
- 14 sequential process steps from offer acceptance to 30-day check-in
- Multiple departments coordinating (HR, IT, Facilities, Hiring Manager)
- Parallel track differences (full-time vs contractor, remote vs on-site)
- Inconsistency in execution quality across managers
- Manual coordination via email with no centralized tracking

**What This Example Demonstrates:**
- Handling processes with strong sequential flow
- Identifying decision points that create process variations (remote vs on-site, FTE vs contractor)
- Capturing coordination challenges across departments
- Documenting inconsistency as a pain point
- Extracting pre-process, during-process, and post-process steps
- Noting time-based milestones (2 weeks before start, first day, first week, 30 days)

**Key Learning Points:**
- Sequential processes still have decision points that branch the workflow
- Consistency (or lack thereof) is an important process characteristic
- Manual coordination and lack of automation are common pain points
- Timing is often specified relative to milestones rather than durations
- Single person handling high volume is a scalability concern

### Example 3: Purchase Order Approval
**Files:** `example-03-po-approval-transcript.txt`, `example-03-po-approval-analysis.md`

**Process Type:** Decision-Heavy, Multi-Tier Approval Process

**Characteristics:**
- 17 process steps including many conditional paths
- 7 major decision points determining process flow
- Amount-based routing with 3 approval tiers (<$1K, $1K-$10K, >$10K)
- Multiple conditional thresholds (negotiation, legal review, vendor vetting)
- Clear timeline differences based on process path (same-day to 2-3 weeks)

**What This Example Demonstrates:**
- Handling processes dominated by conditional logic
- Extracting multiple amount-based and condition-based decision points
- Documenting approval hierarchies and escalation paths
- Capturing percentage-based metrics (budget rejection rate, incomplete requests, vendor issues)
- Identifying bottlenecks at specific approval tiers
- Extracting information about flag abuse and workarounds

**Key Learning Points:**
- Decision-heavy processes require careful extraction of all conditions and thresholds
- Approval processes often have tiered structures based on amount or risk
- Bottlenecks at specific approval levels are common pain points
- Users sometimes game the system (urgency flag abuse)
- Timeline variability is important to capture (best case vs worst case)

## Process Complexity Patterns

Each example represents a different complexity pattern commonly found in business processes:

| Pattern | Example | Key Features |
|---------|---------|--------------|
| **Multi-System Integration** | Accounts Payable | Many systems that don't integrate well; manual workarounds; data re-entry |
| **Multi-Party Coordination** | Employee Onboarding | Multiple departments; email-based coordination; lack of centralized tracking |
| **Multi-Tier Approval** | Purchase Order Approval | Amount-based routing; sequential approvals; escalating timelines |

## Common Themes Across Examples

### Pain Points
All three examples demonstrate common business process pain points:
- Manual data entry and lack of automation
- Poor system integration requiring workarounds
- Approval bottlenecks (single approver or small team)
- Lack of visibility and tracking dashboards
- Email-based coordination without workflow tools
- Incomplete requests/information causing delays
- Inconsistent execution across different people

### Process Metrics
All examples include quantifiable metrics:
- Volume (invoices/month, new hires/month, POs/month)
- Timing (processing time, delays, target vs actual)
- Error/failure rates (data entry errors, account setup failures)
- Percentages (what portion experiences which path)

### Decision Points
All examples show different types of decisions:
- System-automated (budget checks, amount routing)
- Human judgment (manager approvals, exception handling)
- Business rule-based (thresholds, eligibility criteria)

## Using These Examples

When developing or testing the transcript-analysis skill:

1. **Input Testing**: Feed each transcript through the skill and compare output to the expected analysis
2. **Format Validation**: Ensure output follows the same markdown structure and level of detail
3. **Completeness Check**: Verify all steps, actors, decision points, and pain points are extracted
4. **Pattern Recognition**: Use these as templates for analyzing similar process types

## Quality Standards

These examples set the quality bar for transcript analysis:
- **Completeness**: Every step mentioned in transcript should appear in analysis
- **Accuracy**: Use exact terminology from transcript, don't paraphrase unnecessarily
- **Structure**: Follow the defined markdown schema precisely
- **Detail**: Include timing, frequency, impact for pain points
- **Metrics**: Extract and calculate process metrics (counts, percentages, timelines)
- **Context**: Capture notes and observations that don't fit other sections

## What's NOT Included

These examples intentionally don't include:
- Highly technical/specialized processes (manufacturing, laboratory, etc.)
- Processes with extensive regulatory compliance requirements
- International processes with multi-country complexity
- Processes with significant system-to-system automation (low human intervention)

These were excluded to keep examples focused on common business processes where human coordination, approval workflows, and manual steps dominate.
