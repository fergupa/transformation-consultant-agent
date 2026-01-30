# BPMN Generation Skill

## Overview

The BPMN Generation skill converts structured process analysis (markdown format) into BPMN 2.0 XML diagrams. It uses **APQC Level 4 activity consolidation** to create clean, standardized process diagrams suitable for visualization and analysis.

**Key Features:**
- Converts detailed process steps to APQC Level 4 activities (5-10 activities instead of 15-20 steps)
- Generates valid BPMN 2.0 XML compatible with all BPMN tools
- Preserves all decision points, actors, and exception paths
- Uses industry-standard APQC activity naming
- Produces diagrams optimized for visualization in bpmn.io, Camunda Modeler, etc.

## Role in Pipeline

```
Transcript → [Transcript Analysis] → Analysis.md → [BPMN Generation] → BPMN.xml → [Visualization/Optimization]
```

**Upstream:** Transcript Analysis skill (`skills/transcript-analysis/`)
- Input: Structured markdown with process steps, actors, decision points, pain points

**Downstream:**
- Process Optimization skill (analyzes BPMN for improvement recommendations)
- Microsoft Teams Bot (shares visual diagrams with stakeholders)
- Voice Walkthrough skill (generates audio explanations of diagrams)
- Manual visualization in BPMN tools (bpmn.io, Camunda Modeler, Visio)

## APQC Level 4 Consolidation Approach

### Why APQC Level 4?

**Traditional Approach** (detailed mapping):
- 21 AP process steps → 21 BPMN tasks
- Result: Cluttered, hard-to-read diagram
- Different processes use different terminology
- Difficult to benchmark or compare

**APQC Level 4 Approach** (activity consolidation):
- 21 AP process steps → 8 APQC activities
- Result: Clean, standardized diagram
- Uses industry-standard activity names (3.2.1, 3.2.2, etc.)
- Enables cross-organization comparison

### Consolidation Principles

**DO consolidate:**
- ✅ Steps that accomplish the same business activity (e.g., "Receive", "Download", "Scan" → "Receive Vendor Invoice")
- ✅ Related sub-steps within a process phase (e.g., "Search PO", "Resolve Missing PO", "Link to PO" → "Match Invoice to PO")
- ✅ Exception handling within an activity (e.g., "Verify", "Investigate Discrepancies" → "Verify Invoice Accuracy")

**DON'T consolidate:**
- ❌ Steps separated by decision points (preserve decision logic)
- ❌ Steps with different actors unless coordinated (respect actor boundaries)
- ❌ Steps from different process phases (maintain logical flow)

### Example Consolidation

**Input** (detailed steps from analysis):
1. Receive invoice from email
2. Download invoice attachment
3. Print and scan invoice
4. Manual data entry into SAP
5. Search for matching purchase order

**Output** (APQC Level 4 activities):
- **Activity 1: Receive Vendor Invoice** (Steps 1-3)
  - APQC Code: 3.2.1
- **Activity 2: Capture Invoice Data** (Step 4)
  - APQC Code: 3.2.2
- **Activity 3: Match Invoice to Purchase Order** (Step 5)
  - APQC Code: 3.2.3

## Input Specification

### Required Input Format

The skill expects **structured markdown** from the transcript-analysis skill containing these sections:

#### 1. Process Steps
```markdown
### Step 1: Receive Invoice
- **Actor/Role**: AP Clerk
- **Description**: Download invoice from vendor email or portal
- **Input**: Vendor invoice (PDF or paper)
- **Output**: Invoice in document management system
- **Duration/Timing**: Immediate upon receipt
- **Pain Points**: Multiple intake channels create inconsistent handling
```

#### 2. Actors and Roles
```markdown
| Role | Responsibilities | Systems Used |
|------|-----------------|--------------|
| AP Clerk | Receive and process invoices | SAP ERP, Email |
| AP Manager | Approve invoices over $5,000 | SAP ERP, Approval Portal |
```

#### 3. Decision Points
```markdown
### Decision Point 1: PO Match Result
- **Location in Process**: After Step 5
- **Condition**: Does invoice match a purchase order?
- **Outcomes**:
  - **Path A**: Match found → Continue to verification (95% of cases)
  - **Path B**: No match → Route for manual approval (5% of cases)
- **Decision Maker**: SAP System (automated)
```

#### 4. Systems and Tools
```markdown
| System | Purpose | Integration Points |
|--------|---------|-------------------|
| SAP ERP | Invoice processing | Steps 2, 4, 5, 8 |
| Email | Invoice receipt, notifications | Steps 1, 15 |
```

#### 5. Pain Points and Inefficiencies
```markdown
### Critical Issues
1. **Duplicate Invoice Payments**: System doesn't catch duplicates
   - Impact: Paid same invoice twice requiring refund
   - Frequency: Happens 2-3 times per year
```

### Validation

Before calling the BPMN generation skill, ensure the analysis markdown has:
- ✅ At least 5 process steps
- ✅ At least 2 actors
- ✅ At least 1 decision point (most processes have 3-6)
- ✅ Process metrics section with volume/duration

## Output Specification

### BPMN 2.0 XML Format

The skill outputs complete, valid BPMN 2.0 XML with:

#### Structure
```xml
<?xml version="1.0" encoding="UTF-8"?>
<bpmn:definitions ...>
  <bpmn:process id="Process_APInvoice" name="AP Invoice Processing" isExecutable="false">
    <bpmn:laneSet>...</bpmn:laneSet>
    <bpmn:startEvent>...</bpmn:startEvent>
    <bpmn:task>...</bpmn:task>
    <bpmn:exclusiveGateway>...</bpmn:exclusiveGateway>
    <bpmn:sequenceFlow>...</bpmn:sequenceFlow>
    <bpmn:endEvent>...</bpmn:endEvent>
  </bpmn:process>
  <bpmndi:BPMNDiagram>
    <!-- Visual positioning -->
  </bpmndi:BPMNDiagram>
</bpmn:definitions>
```

#### Key Elements
- **Process**: Container for all process elements
- **LaneSet/Lanes**: Swimlanes for each actor
- **StartEvent**: Process trigger
- **Tasks**: APQC Level 4 activities (consolidated from detailed steps)
- **ExclusiveGateways**: Decision points (XOR logic)
- **ParallelGateways**: Simultaneous activities (AND logic) - used sparingly
- **SequenceFlows**: Connections between elements
- **EndEvent**: Process completion or termination
- **BPMNDiagram**: Visual layout with coordinates

### Output Characteristics

**APQC Consolidation:**
- Typical process: 15-20 detailed steps → 5-10 APQC activities
- Finance/AP: Usually 8-10 activities
- HR/Onboarding: Usually 9 activities
- Procurement/PO: Usually 6-7 activities

**Preserved Elements:**
- All decision points from analysis (100%)
- All actors as swimlanes (100%)
- All exception paths (rejections, failures, escalations)
- Loop-back flows (e.g., rejection → resubmission)

**Positioning:**
- Grid-based layout (150 units horizontal spacing, 100 units vertical)
- Left-to-right process flow
- Tasks: 100x80 rectangles
- Gateways: 50x50 diamonds
- Swimlanes: 250 units height per lane

## Usage Examples

### Example 1: Basic Usage (Python)

```python
from anthropic import Anthropic
from pathlib import Path

# Initialize client
client = Anthropic(api_key="your_api_key")

# Read analysis and skill files
analysis = Path("outputs/analysis/ap-process-analysis.md").read_text()
skill = Path("skills/bpmn-generation/SKILL.md").read_text()
apqc_ref = Path("skills/bpmn-generation/domain-knowledge/apqc-activities.md").read_text()

# Call Claude with BPMN generation skill
response = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=8000,
    system=[
        {"type": "text", "text": skill},
        {"type": "text", "text": f"APQC Reference Activities:\n\n{apqc_ref}", "cache_control": {"type": "ephemeral"}}
    ],
    messages=[
        {
            "role": "user",
            "content": f"Generate BPMN 2.0 XML for this process analysis:\n\n{analysis}"
        }
    ]
)

# Save BPMN XML
bpmn_xml = response.content[0].text
Path("outputs/bpmn-diagrams/ap-process.bpmn").write_text(bpmn_xml)
print("BPMN diagram generated: ap-process.bpmn")
```

### Example 2: Batch Processing

```python
from pathlib import Path
from anthropic import Anthropic

client = Anthropic(api_key="your_api_key")

# Load skill once
skill = Path("skills/bpmn-generation/SKILL.md").read_text()
apqc_ref = Path("skills/bpmn-generation/domain-knowledge/apqc-activities.md").read_text()

# Process all analysis files
analysis_dir = Path("outputs/analysis")
output_dir = Path("outputs/bpmn-diagrams")
output_dir.mkdir(exist_ok=True)

for analysis_file in analysis_dir.glob("*-analysis.md"):
    print(f"Processing {analysis_file.name}...")

    analysis = analysis_file.read_text()

    response = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=8000,
        system=[
            {"type": "text", "text": skill},
            {"type": "text", "text": f"APQC Reference:\n\n{apqc_ref}", "cache_control": {"type": "ephemeral"}}
        ],
        messages=[{"role": "user", "content": f"Generate BPMN:\n\n{analysis}"}]
    )

    # Save with matching filename
    output_file = output_dir / analysis_file.name.replace("-analysis.md", ".bpmn")
    output_file.write_text(response.content[0].text)
    print(f"  → {output_file.name}")

print("Batch processing complete!")
```

## Integration Notes

### Upstream: Transcript Analysis Skill

**File Location:** `skills/transcript-analysis/SKILL.md`

**Integration Points:**
- Analysis markdown is direct input to BPMN generation
- No transformation needed
- All sections (steps, actors, decision points) map to BPMN elements

**Quality Checks:**
- Transcript analysis completeness affects BPMN quality
- Missing decision points → incomplete BPMN flow
- Vague actor descriptions → unclear swimlane assignment
- Run validation before BPMN generation

### Downstream: Visualization Tools

**bpmn.io (Recommended):**
1. Go to https://demo.bpmn.io/
2. Click "Open Diagram" or drag .bpmn file
3. View and edit generated diagram
4. Export as PNG/SVG for documentation

**Camunda Modeler:**
1. Download from https://camunda.com/download/modeler/
2. Open .bpmn file
3. View diagram with full BPMN 2.0 support
4. Validate XML structure

**Microsoft Visio:**
- Import .bpmn files via BPMN add-in
- May require manual positioning adjustments

### Downstream: Process Optimization Skill

**File Location:** `skills/process-optimization/` (future implementation)

**Integration:**
- BPMN XML is input to optimization analysis
- AI reads BPMN structure to understand flow
- Identifies bottlenecks from gateway paths and pain points
- Generates improvement recommendations

## Element Mapping Table

| Analysis Element | BPMN Element | Notes |
|-----------------|--------------|-------|
| Process Steps (consolidated) | `<bpmn:task>` | Grouped into APQC Level 4 activities (5-10 tasks) |
| Actors and Roles | `<bpmn:lane>` | One lane per actor |
| Decision Points | `<bpmn:exclusiveGateway>` | XOR gateway with named outgoing flows |
| Parallel Activities | `<bpmn:parallelGateway>` | AND gateway (used sparingly) |
| Process Start | `<bpmn:startEvent>` | Named with trigger event |
| Process End | `<bpmn:endEvent>` | May have multiple ends (success, rejection, etc.) |
| Exception Paths | Gateway alternative flows | Shown as branches from decision gateways |
| Loop-backs | `<bpmn:sequenceFlow>` | Flow returning to earlier task |
| Systems/Tools | Task descriptions or separate lane | Often shown as automated tasks |

## Testing and Validation

### XML Validation

```python
import xml.etree.ElementTree as ET

def validate_bpmn_xml(bpmn_file):
    """Basic BPMN XML validation."""
    try:
        tree = ET.parse(bpmn_file)
        root = tree.getroot()

        # Check namespace
        if "http://www.omg.org/spec/BPMN/20100524/MODEL" not in root.tag:
            print("❌ Invalid BPMN namespace")
            return False

        # Check for process element
        process = root.find(".//{http://www.omg.org/spec/BPMN/20100524/MODEL}process")
        if process is None:
            print("❌ No process element found")
            return False

        # Check for start event
        start_events = root.findall(".//{http://www.omg.org/spec/BPMN/20100524/MODEL}startEvent")
        if not start_events:
            print("❌ No start event found")
            return False

        # Check for end event
        end_events = root.findall(".//{http://www.omg.org/spec/BPMN/20100524/MODEL}endEvent")
        if not end_events:
            print("❌ No end event found")
            return False

        print("✓ BPMN XML is valid")
        return True

    except ET.ParseError as e:
        print(f"❌ XML parsing error: {e}")
        return False

# Usage
validate_bpmn_xml("outputs/bpmn-diagrams/ap-process.bpmn")
```

### Visual Validation Checklist

Open generated .bpmn file in bpmn.io and verify:

- [ ] Diagram loads without errors
- [ ] All swimlanes present (one per actor from analysis)
- [ ] Activities are APQC Level 4 (5-10 activities, not 15-20 steps)
- [ ] Start event present with descriptive name
- [ ] End event(s) present
- [ ] All decision points from analysis appear as gateways
- [ ] Gateway paths labeled (Yes/No, Path A/Path B, etc.)
- [ ] Exception paths visible (rejections, failures, escalations)
- [ ] Flow is traceable from start to end
- [ ] No orphaned elements (all elements connected)
- [ ] Activity names match APQC standards
- [ ] Task positioning is reasonable (left-to-right flow)

### Validation Script

```python
def check_bpmn_completeness(bpmn_file, analysis_file):
    """Compare BPMN output against analysis input."""
    # Load both files
    bpmn_xml = Path(bpmn_file).read_text()
    analysis_md = Path(analysis_file).read_text()

    # Extract decision points from analysis
    import re
    decision_points = re.findall(r"### Decision Point \d+:", analysis_md)

    # Count gateways in BPMN
    gateways = re.findall(r"<bpmn:exclusiveGateway", bpmn_xml)

    print(f"Analysis has {len(decision_points)} decision points")
    print(f"BPMN has {len(gateways)} exclusive gateways")

    if len(gateways) >= len(decision_points):
        print("✓ All decision points preserved")
    else:
        print("⚠ Some decision points may be missing")

    # Extract actors from analysis
    actors_match = re.search(r"\| Role \| Responsibilities.*?\n\|(.*?)\n\n", analysis_md, re.DOTALL)
    if actors_match:
        actors = len(re.findall(r"\|.*?\|", actors_match.group(1)))
        lanes = len(re.findall(r'<bpmn:lane id=', bpmn_xml))
        print(f"Analysis has ~{actors} actors")
        print(f"BPMN has {lanes} lanes")

    # Count consolidated activities
    tasks = len(re.findall(r'<bpmn:task id=', bpmn_xml))
    print(f"BPMN has {tasks} activities (consolidated from detailed steps)")

    if 5 <= tasks <= 12:
        print("✓ Good APQC consolidation (5-12 activities)")
    else:
        print("⚠ May need consolidation review")
```

## Domain Knowledge Examples

The `domain-knowledge/` directory contains:

1. **APQC Activities Reference** (`apqc-activities.md`)
   - Standard APQC Level 4 activities for Finance, HR, Procurement
   - Activity descriptions, inputs/outputs, common variations
   - Use as reference when calling BPMN generation skill

2. **Activity Mappings** (3 examples)
   - `example-01-ap-mapping.md` - AP Invoice Processing (21 steps → 8 activities)
   - `example-02-onboarding-mapping.md` - Employee Onboarding (20 steps → 9 activities)
   - `example-03-po-approval-mapping.md` - PO Approval (10 steps → 6 activities)
   - Show how detailed steps consolidate to APQC activities

3. **Example BPMN Files** (future - after testing)
   - `example-01-ap-bpmn.xml`
   - `example-02-onboarding-bpmn.xml`
   - `example-03-po-approval-bpmn.xml`
   - Reference implementations for each domain

See `domain-knowledge/README.md` for details.

## Model Configuration

**Recommended Settings:**

```python
model = "claude-sonnet-4-5-20250929"
max_tokens = 8000  # BPMN XML can be lengthy
temperature = 0    # Not used for deterministic output
```

**Why Sonnet 4.5:**
- Excellent at structured output generation
- Strong understanding of BPMN 2.0 specification
- Consistent APQC consolidation logic
- Handles complex decision flows reliably

**Token Usage:**
- Simple process (5-7 activities): ~3,000-4,000 tokens
- Medium process (8-10 activities): ~5,000-6,000 tokens
- Complex process (10-12 activities): ~6,000-8,000 tokens

**System Prompt Caching:**
- Cache SKILL.md and apqc-activities.md for batch processing
- Reduces cost and latency for multiple diagrams

## Limitations

### Current Limitations

1. **No Subprocess Support**
   - Current implementation uses flat task structure
   - Subprocesses (embedded or call activities) not generated
   - Future enhancement for complex processes

2. **Basic Positioning**
   - Grid-based layout with fixed spacing
   - Manual adjustment may be needed in BPMN editor
   - No auto-layout or optimization algorithms

3. **Standard BPMN 2.0 Only**
   - No vendor extensions (Camunda, Flowable, etc.)
   - `isExecutable="false"` - diagrams are for visualization/analysis
   - No runtime variables, delegates, or execution logic

4. **Limited Event Types**
   - Currently generates: Start Event (None), End Event (None)
   - Future: Timer events, message events, error events

5. **No Data Objects**
   - Process data flow not explicitly modeled
   - Inputs/outputs described in task names, not data objects

6. **APQC Coverage**
   - Strong coverage for Finance, HR, Procurement
   - Other domains may need custom activity definitions

### Known Issues

- **Long process names** may overflow in some BPMN viewers (use abbreviations)
- **Many swimlanes** (>8) can make diagram tall (consider consolidating actors)
- **Complex branching** with 4+ decision paths can be hard to visualize (consider decomposition)

### Workarounds

**For complex processes:**
- Consider breaking into multiple diagrams (e.g., happy path + exception paths)
- Use annotations for additional context
- Manually refine positioning in BPMN editor

**For non-standard domains:**
- Define custom APQC-style activities in analysis
- Document custom activity taxonomy
- Update apqc-activities.md reference with new domain

## Future Enhancements

**Planned Features:**
1. Subprocess generation for complex process sections
2. Timer and message event support
3. Data object modeling
4. Collaboration diagrams (multiple processes/pools)
5. Advanced positioning algorithms
6. BPMN validation against Camunda/Flowable engines
7. Integration with process mining tools
8. Automated APQC activity suggestion

## Troubleshooting

### Issue: Empty or Truncated BPMN Output

**Symptoms:** Generated .bpmn file is empty or cuts off mid-element

**Causes:**
- max_tokens too low
- API timeout

**Solutions:**
```python
# Increase max_tokens
max_tokens = 8000  # Up from 4000

# Check for truncation in response
if response.stop_reason == "max_tokens":
    print("⚠ Output truncated - increase max_tokens")
```

### Issue: Invalid XML

**Symptoms:** BPMN file won't open in bpmn.io or Camunda Modeler

**Causes:**
- Malformed XML (unclosed tags, unescaped characters)
- Invalid BPMN structure

**Solutions:**
```python
# Validate before saving
import xml.etree.ElementTree as ET
try:
    ET.fromstring(bpmn_xml)
    print("✓ Valid XML")
except ET.ParseError as e:
    print(f"❌ Invalid XML: {e}")
    # Inspect response for issues
```

### Issue: Missing Decision Points

**Symptoms:** Fewer gateways in BPMN than decision points in analysis

**Causes:**
- APQC consolidation overly aggressive
- Analysis decision points unclear

**Solutions:**
- Review activity mapping - ensure decision points preserved
- Check analysis markdown - decision points must be clearly documented
- Manually add gateways in BPMN editor if needed

### Issue: Too Many Activities

**Symptoms:** BPMN has 15-20 tasks instead of 5-10

**Causes:**
- APQC consolidation not applied
- Analysis steps too granular

**Solutions:**
- Verify APQC reference is included in system prompt
- Review mapping examples to understand consolidation patterns
- Explicitly instruct: "Consolidate to APQC Level 4 activities"

## Support and Feedback

**Documentation:**
- This README
- SKILL.md (system prompt with detailed rules)
- domain-knowledge/README.md (examples and references)

**Testing:**
- Run validation scripts on generated BPMN
- Visual inspection in bpmn.io
- Compare against domain-knowledge examples

**Issues:**
- Check generated BPMN against validation checklist
- Review activity mappings for consolidation patterns
- Verify analysis markdown completeness

## License

Part of the transformation-consultant-agent system.

---

**Next Steps:**
1. Load SKILL.md and apqc-activities.md
2. Generate BPMN from analysis markdown
3. Validate XML and visual output
4. Iterate on mapping if needed
5. Save to `outputs/bpmn-diagrams/`
