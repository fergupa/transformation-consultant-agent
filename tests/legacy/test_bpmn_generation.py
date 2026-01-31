"""
Test script for BPMN generation skill.

This script:
1. Reads the BPMN generation SKILL.md system prompt
2. Reads the APQC activities reference (cached context)
3. Reads a process analysis file
4. Calls Claude API to generate BPMN XML
5. Saves and validates the output
"""

import os
from pathlib import Path
from anthropic import Anthropic
import xml.etree.ElementTree as ET
from dotenv import load_dotenv

# Load environment variables
load_dotenv("config/.env")

def validate_bpmn_xml(bpmn_file):
    """
    Basic BPMN XML validation.

    Checks:
    - XML is well-formed
    - Has BPMN namespace
    - Contains process, start event, end event
    - Has diagram section
    """
    try:
        tree = ET.parse(bpmn_file)
        root = tree.getroot()

        # Check namespace
        bpmn_ns = "http://www.omg.org/spec/BPMN/20100524/MODEL"
        if bpmn_ns not in root.tag:
            print(f"[ERROR] Invalid BPMN namespace. Root tag: {root.tag}")
            return False

        # Check for process
        process = root.find(f".//{{{bpmn_ns}}}process")
        if process is None:
            print("[ERROR] No process element found")
            return False

        # Check for start event
        start_events = root.findall(f".//{{{bpmn_ns}}}startEvent")
        if not start_events:
            print("[ERROR] No start event found")
            return False

        # Check for end event
        end_events = root.findall(f".//{{{bpmn_ns}}}endEvent")
        if not end_events:
            print("[ERROR] No end event found")
            return False

        # Check for diagram section
        bpmndi_ns = "http://www.omg.org/spec/BPMN/20100524/DI"
        diagram = root.find(f".//{{{bpmndi_ns}}}BPMNDiagram")
        if diagram is None:
            print("[WARNING] No diagram section found (optional but recommended)")

        # Count elements
        tasks = root.findall(f".//{{{bpmn_ns}}}task")
        gateways = root.findall(f".//{{{bpmn_ns}}}exclusiveGateway")
        lanes = root.findall(f".//{{{bpmn_ns}}}lane")
        flows = root.findall(f".//{{{bpmn_ns}}}sequenceFlow")

        print(f"[VALID] BPMN XML is valid")
        print(f"   - Tasks: {len(tasks)}")
        print(f"   - Gateways: {len(gateways)}")
        print(f"   - Lanes: {len(lanes)}")
        print(f"   - Sequence Flows: {len(flows)}")
        print(f"   - Start Events: {len(start_events)}")
        print(f"   - End Events: {len(end_events)}")

        return True

    except ET.ParseError as e:
        print(f"[ERROR] XML parsing error: {e}")
        return False
    except Exception as e:
        print(f"[ERROR] Validation error: {e}")
        return False


def generate_bpmn(analysis_file, output_file, example_name):
    """
    Generate BPMN XML from analysis file using Claude API.

    Args:
        analysis_file: Path to analysis markdown file
        output_file: Path to save generated BPMN XML
        example_name: Name of example for logging
    """
    print(f"\n{'='*60}")
    print(f"Generating BPMN for: {example_name}")
    print(f"{'='*60}\n")

    # Initialize Anthropic client
    client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    # Read files
    print("Reading files...")
    skill_path = Path("skills/bpmn-generation/SKILL.md")
    apqc_path = Path("skills/bpmn-generation/domain-knowledge/apqc-activities.md")
    analysis_path = Path(analysis_file)

    if not all([skill_path.exists(), apqc_path.exists(), analysis_path.exists()]):
        print("[ERROR] Required files not found")
        return False

    skill = skill_path.read_text(encoding='utf-8')
    apqc_ref = apqc_path.read_text(encoding='utf-8')
    analysis = analysis_path.read_text(encoding='utf-8')

    print(f"   [OK] SKILL.md ({len(skill)} chars)")
    print(f"   [OK] apqc-activities.md ({len(apqc_ref)} chars)")
    print(f"   [OK] {analysis_file} ({len(analysis)} chars)")

    # Call Claude API
    print("\nCalling Claude API...")
    try:
        response = client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=16000,
            temperature=0,
            system=[
                {
                    "type": "text",
                    "text": skill
                },
                {
                    "type": "text",
                    "text": f"# APQC Level 4 Activities Reference\n\n{apqc_ref}",
                    "cache_control": {"type": "ephemeral"}
                }
            ],
            messages=[
                {
                    "role": "user",
                    "content": f"Generate BPMN 2.0 XML for the following process analysis:\n\n{analysis}"
                }
            ]
        )

        # Extract BPMN XML from response
        bpmn_xml = response.content[0].text

        # Check if response contains XML
        if not bpmn_xml.strip().startswith('<?xml'):
            print("[WARNING] Response doesn't start with XML declaration, looking for XML content...")
            # Try to extract XML from markdown code blocks if present
            if '```xml' in bpmn_xml:
                bpmn_xml = bpmn_xml.split('```xml')[1].split('```')[0].strip()
            elif '```' in bpmn_xml:
                bpmn_xml = bpmn_xml.split('```')[1].split('```')[0].strip()

        print(f"   [OK] Response received ({len(bpmn_xml)} chars)")
        print(f"   [OK] Tokens used: {response.usage.input_tokens} input, {response.usage.output_tokens} output")

        # Save BPMN XML
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(bpmn_xml, encoding='utf-8')
        print(f"\nSaved to: {output_file}")

        # Validate BPMN XML
        print("\nValidating BPMN XML...")
        is_valid = validate_bpmn_xml(output_path)

        if is_valid:
            print(f"\nSuccess! Open in bpmn.io to visualize:")
            print(f"   https://demo.bpmn.io/new")
            print(f"   Then: File > Open > {output_path.absolute()}")

        return is_valid

    except Exception as e:
        print(f"[ERROR] API error: {e}")
        return False


def main():
    """Run BPMN generation tests for all examples."""

    print("\n" + "="*60)
    print("BPMN Generation Skill - Test Suite")
    print("="*60)

    # Test cases
    test_cases = [
        {
            "name": "AP Invoice Processing",
            "analysis": "outputs/analysis/example-01-ap-analysis-test.md",
            "output": "outputs/bpmn-diagrams/example-01-ap.bpmn"
        },
        {
            "name": "Employee Onboarding",
            "analysis": "outputs/analysis/example-02-onboarding-analysis-test.md",
            "output": "outputs/bpmn-diagrams/example-02-onboarding.bpmn"
        },
        {
            "name": "Purchase Order Approval",
            "analysis": "outputs/analysis/example-03-po-approval-analysis-test.md",
            "output": "outputs/bpmn-diagrams/example-03-po-approval.bpmn"
        }
    ]

    results = []

    # Run tests
    for test in test_cases:
        success = generate_bpmn(
            test["analysis"],
            test["output"],
            test["name"]
        )
        results.append({
            "name": test["name"],
            "success": success,
            "output": test["output"]
        })

    # Summary
    print("\n" + "="*60)
    print("Test Summary")
    print("="*60)

    for result in results:
        status = "[PASS]" if result["success"] else "[FAIL]"
        print(f"{status} - {result['name']}")
        if result["success"]:
            print(f"         {result['output']}")

    passed = sum(1 for r in results if r["success"])
    total = len(results)
    print(f"\n{passed}/{total} tests passed")

    if passed == total:
        print("\nAll tests passed! BPMN generation skill is working correctly.")
        print("\nNext steps:")
        print("   1. Open generated .bpmn files in bpmn.io or Camunda Modeler")
        print("   2. Verify APQC consolidation (5-10 activities, not 15-20 steps)")
        print("   3. Check that all decision points are preserved as gateways")
        print("   4. Verify all actors are represented as swimlanes")
        print("   5. Validate flow is complete and traceable")
    else:
        print("\n[WARNING] Some tests failed. Review errors above.")

    return passed == total


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
