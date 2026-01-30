# Transcript Analysis Skill

A Claude skill that extracts structured process information from business process interview transcripts, producing markdown-formatted analysis suitable for downstream process modeling and optimization.

## Overview

The transcript-analysis skill is the first stage in the transformation-consultant-agent pipeline. It takes conversational interview transcripts where subject matter experts describe their work processes and extracts:

- Sequential process steps with details
- Actors and their roles
- Decision points and conditional logic
- Systems and tools used
- Pain points and inefficiencies
- Process metrics and timing information

## Purpose

This skill enables:
1. **Structured extraction** from unstructured conversational data
2. **Process documentation** from tribal knowledge
3. **BPMN diagram generation** through standardized output format
4. **Process optimization** by identifying pain points and bottlenecks
5. **Scalable analysis** of multiple process interviews

## Input Specification

**Format:** Plain text transcript

**Structure:** Interview format with interviewer questions and interviewee responses

**Typical Length:** 1,000-3,000 words (10-25 minute interview)

**Content Requirements:**
- Clear process description from start to end
- Mentions of actors/roles involved
- Description of steps and their sequence
- Systems or tools used
- Challenges, pain points, or inefficiencies (ideally)
- Timing, volume, or frequency information (ideally)

**Example Input:**
```
Business Process Interview Transcript
Process: Expense Report Approval
Interviewee: John Smith, Finance Manager
Date: January 15, 2026

Interviewer: Walk me through your expense report process...

John: Sure. Employees submit their reports through our portal...
[continues with process description]
```

## Output Specification

**Format:** Structured markdown document

**Schema:**
- Process Analysis title with process name
- Executive Summary (2-3 sentences)
- Process Steps (numbered, with actor, description, input, output, timing, pain points)
- Actors and Roles (table)
- Decision Points (with conditions and outcomes)
- Systems and Tools (table)
- Pain Points and Inefficiencies (categorized)
- Process Metrics (counts and statistics)
- Notes and Observations

**Output Length:** 1,500-4,000 words depending on process complexity

**See:** [domain-knowledge/example-01-ap-analysis.md](domain-knowledge/example-01-ap-analysis.md) for full example

## Usage

### Basic Usage

```python
from anthropic import Anthropic
from pathlib import Path

# Initialize client
client = Anthropic()

# Load transcript
transcript_path = Path("data/sample-transcripts/ap-process.txt")
transcript = transcript_path.read_text()

# Load skill system prompt
skill_path = Path("skills/transcript-analysis/SKILL.md")
system_prompt = skill_path.read_text()

# Analyze transcript
response = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=4000,
    system=system_prompt,
    messages=[
        {
            "role": "user",
            "content": transcript
        }
    ]
)

# Extract analysis
analysis = response.content[0].text
print(analysis)

# Optionally save analysis
output_path = Path("outputs/analysis/ap-process-analysis.md")
output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_text(analysis)
```

### Batch Processing Multiple Transcripts

```python
from anthropic import Anthropic
from pathlib import Path

client = Anthropic()
system_prompt = Path("skills/transcript-analysis/SKILL.md").read_text()

# Process all transcripts in a directory
transcript_dir = Path("data/sample-transcripts")
output_dir = Path("outputs/analysis")
output_dir.mkdir(parents=True, exist_ok=True)

for transcript_file in transcript_dir.glob("*.txt"):
    if transcript_file.name == "README.md":
        continue

    print(f"Analyzing {transcript_file.name}...")

    transcript = transcript_file.read_text()

    response = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=4000,
        system=system_prompt,
        messages=[{"role": "user", "content": transcript}]
    )

    analysis = response.content[0].text

    # Save with corresponding name
    output_file = output_dir / f"{transcript_file.stem}-analysis.md"
    output_file.write_text(analysis)
    print(f"  ✓ Saved to {output_file}")
```

### Integration with BPMN Generation

The output of transcript-analysis feeds directly into the BPMN generation skill:

```python
from anthropic import Anthropic
from pathlib import Path

client = Anthropic()

# Step 1: Analyze transcript
transcript = Path("data/sample-transcripts/ap-process.txt").read_text()
analysis_response = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=4000,
    system=Path("skills/transcript-analysis/SKILL.md").read_text(),
    messages=[{"role": "user", "content": transcript}]
)
analysis = analysis_response.content[0].text

# Step 2: Generate BPMN diagram from analysis
bpmn_response = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=4000,
    system=Path("skills/bpmn-generation/SKILL.md").read_text(),  # When implemented
    messages=[{"role": "user", "content": analysis}]
)
bpmn_diagram = bpmn_response.content[0].text

# Save outputs
Path("outputs/analysis/ap-process-analysis.md").write_text(analysis)
Path("outputs/bpmn-diagrams/ap-process.bpmn").write_text(bpmn_diagram)
```

## Integration Notes

### For BPMN Generation Skill

The analysis output provides all necessary elements for BPMN diagram generation:

| Analysis Element | BPMN Element | Mapping |
|-----------------|--------------|---------|
| Process Steps | Tasks | Each step becomes a task with actor assignment |
| Decision Points | Gateways | Conditions map to exclusive/inclusive gateways |
| Actors/Roles | Swimlanes | Each actor becomes a lane in the diagram |
| First Step | Start Event | Process beginning |
| Last Step | End Event | Process conclusion |
| Step Sequence | Sequence Flows | Implied by numbering and decision outcomes |

### For Process Optimization Skill

The analysis output provides optimization inputs:

| Analysis Element | Optimization Use |
|-----------------|------------------|
| Pain Points | Direct improvement targets |
| Manual Steps | Automation candidates |
| Timing Information | Performance improvement opportunities |
| Decision Points | Simplification candidates |
| System Integration | Integration opportunities |
| Process Metrics | Baseline for improvement measurement |

## Testing

### Unit Testing

Test the skill with domain knowledge examples (expected outputs provided):

```python
from pathlib import Path
from anthropic import Anthropic

client = Anthropic()
system_prompt = Path("skills/transcript-analysis/SKILL.md").read_text()

# Test with Example 1 (AP Process)
transcript = Path("skills/transcript-analysis/domain-knowledge/example-01-ap-transcript.txt").read_text()
expected = Path("skills/transcript-analysis/domain-knowledge/example-01-ap-analysis.md").read_text()

response = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=4000,
    system=system_prompt,
    messages=[{"role": "user", "content": transcript}]
)

actual = response.content[0].text

# Manual comparison
# Compare actual vs expected for:
# - All required sections present
# - Similar number of steps extracted
# - Key actors identified
# - Major pain points captured
# - Process metrics calculated correctly
```

### Validation Checklist

For each analysis output, verify:

**Structure:**
- [ ] Contains all required markdown sections
- [ ] Process steps are numbered sequentially
- [ ] Tables are properly formatted
- [ ] Decision points reference valid step numbers

**Completeness:**
- [ ] 95%+ of steps from transcript captured
- [ ] All actors mentioned in transcript listed
- [ ] All decision points identified
- [ ] All pain points extracted
- [ ] Process metrics match transcript numbers

**Quality:**
- [ ] Uses exact terminology from transcript
- [ ] Step descriptions are clear and concise
- [ ] Pain point impacts are documented
- [ ] Notes section captures important context

**BPMN Readiness:**
- [ ] Steps can map to tasks
- [ ] Decision points can map to gateways
- [ ] Actors can map to swimlanes
- [ ] Flow is unambiguous

### Sample Data Testing

Test with sample transcripts (no expected output provided):

```python
# Test generalization with sample data
sample_transcript = Path("data/sample-transcripts/ap-process.txt").read_text()

response = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=4000,
    system=Path("skills/transcript-analysis/SKILL.md").read_text(),
    messages=[{"role": "user", "content": sample_transcript}]
)

# Validate structure and content manually
analysis = response.content[0].text
print(analysis)
```

## Domain Knowledge

The skill includes domain knowledge examples demonstrating different process complexity patterns:

1. **[Example 1: Accounts Payable](domain-knowledge/example-01-ap-transcript.txt)** - Multi-system integration complexity
2. **[Example 2: Employee Onboarding](domain-knowledge/example-02-onboarding-transcript.txt)** - Multi-party coordination complexity
3. **[Example 3: Purchase Order Approval](domain-knowledge/example-03-po-approval-transcript.txt)** - Multi-tier approval complexity

See [domain-knowledge/README.md](domain-knowledge/README.md) for details on what each example demonstrates.

## Limitations

**Current Limitations:**
- Works best with 1-1 interviews (single interviewee describing a process)
- Assumes sequential or decision-based processes (may struggle with highly parallel processes)
- Relies on interviewee explicitly mentioning pain points (doesn't infer unstated problems)
- Limited to information present in transcript (doesn't add external knowledge)

**Input Quality Dependencies:**
- Better transcripts (clear, detailed, complete) produce better analyses
- Vague or incomplete transcripts result in gaps in analysis
- Highly technical jargon may be preserved but not explained

**Known Edge Cases:**
- Multiple people describing same process with conflicting information
- Processes with extensive parallelism
- Processes with many exception paths
- Highly technical processes requiring domain expertise

## Model Configuration

**Recommended Model:** `claude-sonnet-4-5-20250929`

**Max Tokens:** 4000 (sufficient for most processes; increase to 8000 for very complex processes)

**Temperature:** Default (not specified, uses model default for balanced output)

**System Prompt:** The [SKILL.md](SKILL.md) file in this directory

## File Structure

```
skills/transcript-analysis/
├── SKILL.md                              # System prompt (core skill definition)
├── README.md                             # This file (developer documentation)
├── domain-knowledge/                     # Training examples
│   ├── README.md                        # Examples overview
│   ├── example-01-ap-transcript.txt     # AP process transcript
│   ├── example-01-ap-analysis.md        # Expected AP analysis
│   ├── example-02-onboarding-transcript.txt
│   ├── example-02-onboarding-analysis.md
│   ├── example-03-po-approval-transcript.txt
│   └── example-03-po-approval-analysis.md
└── examples/                            # (Reserved for future examples)
```

## Troubleshooting

**Problem:** Analysis missing steps from transcript
- **Solution:** Check if steps were described vaguely or implicitly; may need clearer transcript

**Problem:** Decision points not identified
- **Solution:** Ensure transcript uses conditional language ("if", "when", "depends on")

**Problem:** Pain points section empty
- **Solution:** Transcript may not mention problems; prompt interviewee about challenges

**Problem:** Output exceeds max_tokens
- **Solution:** Increase max_tokens to 8000, or simplify/shorten transcript

**Problem:** Actor assignments incorrect
- **Solution:** Check if transcript clearly states who performs each step

## Future Enhancements

Potential improvements for future versions:

1. **Multi-interview synthesis:** Combine insights from multiple people describing same process
2. **Automatic diagram generation:** Direct BPMN XML output instead of just markdown
3. **Metric calculation:** Auto-calculate process efficiency metrics (cycle time, touch time, etc.)
4. **Gap detection:** Identify missing information and suggest follow-up questions
5. **Process comparison:** Compare multiple processes to identify common patterns
6. **Confidence scoring:** Rate confidence in each extracted element

## Support

For questions or issues:
- Review domain knowledge examples for expected format
- Check sample data testing results
- Validate input transcript quality
- Ensure using recommended model and token limits

## Version History

- **v1.0** (January 2026): Initial implementation with 3 domain examples, markdown output schema, integration with BPMN generation
