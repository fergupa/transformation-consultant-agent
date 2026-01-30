# Sample Transcripts

This directory contains sample business process transcripts for testing the transcript-analysis skill in real-world scenarios.

## Purpose

These sample transcripts are used for:
- **End-to-end testing** of the complete transformation-consultant-agent pipeline
- **Quality validation** of the transcript-analysis skill output
- **Integration testing** with downstream skills (BPMN generation, process optimization)
- **Demonstration** of the agent's capabilities with realistic business scenarios

## Difference from Domain Knowledge Examples

Unlike the domain knowledge examples in [skills/transcript-analysis/domain-knowledge](../../skills/transcript-analysis/domain-knowledge/), these sample transcripts:
- Do **NOT** have pre-created analysis files
- Represent **different scenarios** than the domain examples
- Are meant to test **generalization** of the skill beyond training examples
- Are used in **end-to-end workflow testing** as shown in the main project README

## Current Samples

### ap-process.txt
**Process:** Accounts Payable - Invoice Matching and Payment Processing

**Interviewee:** Jennifer Park, Senior AP Specialist

**Focus Areas:**
- Invoice three-way matching (invoice, PO, receiving report)
- Description, quantity, and price discrepancy handling
- Duplicate invoice detection and prevention
- Manual tracking with external spreadsheets
- Payment approval and processing
- Aging invoice management

**Key Characteristics:**
- Approximately 1,800 words
- 200 invoices processed monthly
- Emphasis on matching problems (30-40% description discrepancies)
- Duplicate payment issues (1-2 per month)
- Manual Excel-based tracking
- Three-way matching as core complexity
- ACH and check payment methods

**Unique Pain Points:**
- System inability to recognize description variations
- Manual judgment required for matching decisions
- Duplicate invoice detection gaps
- Communication delays with buyers
- Unreliable payment remittance notifications
- Manual status tracking outside the system

**Different From Domain Example 01 (AP):**
While both are Accounts Payable processes, this sample focuses specifically on invoice matching challenges and duplicate payments, whereas the domain example emphasized the end-to-end workflow with printing/scanning, approvals, and payment runs. This provides a different perspective on AP pain points.

## Using Sample Transcripts

### Basic Usage

```python
from anthropic import Anthropic
from pathlib import Path

client = Anthropic()

# Load the sample transcript
transcript = Path("data/sample-transcripts/ap-process.txt").read_text()

# Analyze with transcript-analysis skill
analysis = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=4000,
    system=Path("skills/transcript-analysis/SKILL.md").read_text(),
    messages=[{"role": "user", "content": transcript}]
)

# Output the analysis
print(analysis.content[0].text)
```

### Expected Output Validation

When testing with sample transcripts, verify the analysis output contains:

**Required Sections:**
- [ ] Process Analysis title with process name
- [ ] Executive Summary (2-3 sentences)
- [ ] Process Steps (numbered, with all required fields)
- [ ] Actors and Roles (table format)
- [ ] Decision Points (if any exist in the process)
- [ ] Systems and Tools (table format)
- [ ] Pain Points and Inefficiencies (categorized)
- [ ] Process Metrics (counts and statistics)
- [ ] Notes and Observations

**Content Quality Checks:**
- [ ] All major steps from transcript are extracted
- [ ] All actors mentioned in transcript are listed
- [ ] Pain points accurately reflect what interviewee described
- [ ] Metrics match numbers given in transcript (volume, percentages, timing)
- [ ] Decision points capture conditional logic described
- [ ] Systems mentioned in transcript are documented

**BPMN Readiness:**
- [ ] Process steps can map to BPMN tasks
- [ ] Decision points can map to BPMN gateways
- [ ] Actors can map to BPMN swimlanes
- [ ] Sequential flow is clear from step numbering

### Integration Testing

Use sample transcripts to test the complete pipeline:

```python
# Step 1: Transcript Analysis
analysis = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=4000,
    system=Path("skills/transcript-analysis/SKILL.md").read_text(),
    messages=[{"role": "user", "content": transcript}]
)

# Step 2: BPMN Generation (when implemented)
bpmn = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=4000,
    system=Path("skills/bpmn-generation/SKILL.md").read_text(),
    messages=[{"role": "user", "content": analysis.content[0].text}]
)

# Step 3: Process Optimization (when implemented)
recommendations = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=4000,
    system=Path("skills/process-optimization/SKILL.md").read_text(),
    messages=[{"role": "user", "content": analysis.content[0].text}]
)
```

## Adding New Sample Transcripts

When adding new sample transcripts to this directory:

1. **Create realistic content** (1,500-2,500 words)
2. **Use interview format** with interviewer questions and interviewee responses
3. **Include process metadata** at the top (process name, interviewee, date)
4. **Focus on a specific business process** (procurement, HR, finance, operations, IT, etc.)
5. **Naturally incorporate key elements:**
   - Multiple process steps (8-15 steps)
   - Different actors/roles (3-6 actors)
   - Decision points and conditional logic
   - Systems and tools used
   - Pain points and challenges (4-8 pain points)
   - Timing and volume metrics
   - Natural speech patterns (fillers, clarifications, examples)

6. **Make it distinct** from existing domain examples and samples
7. **Name files descriptively** (e.g., `expense-reimbursement-process.txt`, `customer-onboarding.txt`)
8. **Update this README** with details about the new sample

## Sample Transcript Quality Standards

Good sample transcripts should:
- Sound like real conversations (not stilted or overly formal)
- Include specific details and examples from the interviewee
- Naturally reveal pain points through frustration or complaints
- Provide numbers and metrics organically in conversation
- Include some ambiguity or complexity that tests the skill's extraction capabilities
- Cover the full process from start to end
- Mention exceptions, edge cases, or variations when relevant

## Current Gaps

Sample transcripts we don't yet have but could add:
- Customer service/support processes
- Sales order to cash processes
- IT service request handling
- Travel and expense reimbursement
- Contract management and renewal
- Supply chain/inventory management
- Quality assurance and testing
- Marketing campaign management
- Recruiting and hiring
- Facilities management

## Testing Results

When you test the transcript-analysis skill with these samples, document findings:
- What worked well in the extraction
- What was missed or incorrectly extracted
- How output could be improved
- Whether output successfully feeds into downstream skills (BPMN, optimization)

This feedback helps improve both the skill system prompt and the quality of sample data.
