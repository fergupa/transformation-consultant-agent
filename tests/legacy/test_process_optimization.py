"""
Test script for Process Optimization skill.

This script tests the process-optimization skill by:
1. Loading process analysis files from outputs/analysis/
2. Applying the optimization skill system prompt
3. Generating optimization recommendations
4. Saving output to outputs/recommendations/
"""

import anthropic
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Set UTF-8 encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Load environment variables from config/.env
load_dotenv('config/.env')

def main():
    print("="*70)
    print("Process Optimization Skill - Test Script")
    print("="*70)

    # Initialize Anthropic client
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY not found in config/.env")
        return

    client = anthropic.Anthropic(api_key=api_key)
    print(f"✓ Connected to Anthropic API")

    # Load system prompt
    skill_path = Path("skills/process-optimization/SKILL.md")
    if not skill_path.exists():
        print(f"ERROR: SKILL.md not found at {skill_path}")
        return

    with open(skill_path, "r", encoding="utf-8") as f:
        system_prompt = f.read()
    print(f"✓ Loaded system prompt ({len(system_prompt)} chars)")

    # Define test cases
    test_cases = [
        {
            "name": "AP Invoice Processing",
            "analysis_file": "outputs/analysis/example-01-ap-analysis-test.md",
            "output_file": "outputs/recommendations/example-01-ap-recommendations-generated.md",
            "context": """
Industry: Manufacturing/General Business Services
Budget: $200K available for process improvement initiatives this year
Strategic Priority: Reduce accounts payable cycle time and improve vendor relationships
Technology Constraints: Must integrate with SAP ERP (existing system)
"""
        },
        {
            "name": "Employee Onboarding",
            "analysis_file": "outputs/analysis/example-02-onboarding-analysis-test.md",
            "output_file": "outputs/recommendations/example-02-onboarding-recommendations-generated.md",
            "context": """
Industry: Technology/Professional Services
Budget: $150K available for HR technology improvements
Strategic Priority: Improve new hire experience and reduce HR administrative burden
Technology Constraints: Must integrate with Workday HRIS (existing system)
"""
        },
        {
            "name": "PO Approval Process",
            "analysis_file": "outputs/analysis/example-03-po-approval-analysis-test.md",
            "output_file": "outputs/recommendations/example-03-po-approval-recommendations-generated.md",
            "context": """
Industry: Manufacturing/General Business Services
Budget: $100K available for procurement process improvements
Strategic Priority: Reduce procurement cycle time and improve requester experience
Technology Constraints: Must integrate with existing ERP system
"""
        }
    ]

    # Create output directory if it doesn't exist
    output_dir = Path("outputs/recommendations")
    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"✓ Output directory ready: {output_dir}")

    print("\n" + "="*70)
    print("Generating Optimization Recommendations")
    print("="*70)

    # Process each test case
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n[{i}/{len(test_cases)}] Processing: {test_case['name']}")
        print("-"*70)

        # Check if analysis file exists
        analysis_path = Path(test_case['analysis_file'])
        if not analysis_path.exists():
            print(f"  ✗ Analysis file not found: {analysis_path}")
            print(f"    Skipping this test case")
            continue

        # Load analysis file
        with open(analysis_path, "r", encoding="utf-8") as f:
            analysis_content = f.read()
        print(f"  ✓ Loaded analysis ({len(analysis_content)} chars)")

        # Prepare user message
        user_message = f"""Please analyze this process and generate comprehensive optimization recommendations.

Process Analysis Document:
{analysis_content}

Additional Context:
{test_case['context']}

Please provide specific technology recommendations, detailed ROI calculations, and a phased implementation roadmap."""

        print(f"  ⟳ Calling Claude API (Opus)...")

        # Retry logic for API calls
        max_retries = 3
        retry_delay = 5  # seconds

        for attempt in range(max_retries):
            try:
                if attempt > 0:
                    print(f"  ⟳ Retry attempt {attempt + 1}/{max_retries}...")
                    import time
                    time.sleep(retry_delay)

                # Call API with Opus for complex analysis
                response = client.messages.create(
                    model="claude-opus-4-5-20251101",  # Use Opus for comprehensive analysis
                    max_tokens=16000,
                    system=system_prompt,
                    messages=[{"role": "user", "content": user_message}]
                )

                # Extract response
                recommendations = response.content[0].text

                # Save to output file
                output_path = Path(test_case['output_file'])
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(recommendations)

                print(f"  ✓ Generated recommendations ({len(recommendations)} chars)")
                print(f"  ✓ Saved to: {output_path}")

                # Basic validation
                if "Executive Summary" in recommendations:
                    print(f"  ✓ Contains Executive Summary")
                if "Quick Wins" in recommendations:
                    print(f"  ✓ Contains Quick Wins section")
                if "ROI Estimate" in recommendations or "ROI estimate" in recommendations:
                    print(f"  ✓ Contains ROI estimates")
                if "Implementation Roadmap" in recommendations:
                    print(f"  ✓ Contains Implementation Roadmap")

                # Success - break out of retry loop
                break

            except anthropic.APIConnectionError as e:
                print(f"  ✗ API Connection Error: {str(e)}")
                if attempt == max_retries - 1:
                    print(f"  ✗ Failed after {max_retries} attempts")
            except anthropic.RateLimitError as e:
                print(f"  ✗ Rate Limit Error: {str(e)}")
                if attempt == max_retries - 1:
                    print(f"  ✗ Failed after {max_retries} attempts")
            except Exception as e:
                print(f"  ✗ Error ({type(e).__name__}): {str(e)}")
                if attempt == max_retries - 1:
                    print(f"  ✗ Failed after {max_retries} attempts")
                    import traceback
                    print(f"  ✗ Traceback: {traceback.format_exc()}")

    print("\n" + "="*70)
    print("Test Complete")
    print("="*70)
    print(f"\nRecommendations saved to: {output_dir}/")
    print("\nNext steps:")
    print("1. Review generated recommendations for quality and completeness")
    print("2. Compare with domain-knowledge examples")
    print("3. Validate ROI calculations and technology suggestions")
    print("4. Test recommendations with stakeholders")

if __name__ == "__main__":
    main()
