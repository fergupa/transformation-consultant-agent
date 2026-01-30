"""
Setup Verification Script
Run this script to verify your development environment is configured correctly.
"""

from pathlib import Path
import os
import sys

def test_imports():
    """Test that required packages can be imported."""
    print("Testing package imports...")

    try:
        import anthropic
        print("  ✓ anthropic")
    except ImportError:
        print("  ❌ anthropic - run: pip install anthropic")
        return False

    try:
        import dotenv
        print("  ✓ python-dotenv")
    except ImportError:
        print("  ❌ python-dotenv - run: pip install python-dotenv")
        return False

    try:
        import jupyter
        print("  ✓ jupyter")
    except ImportError:
        print("  ❌ jupyter - run: pip install jupyter")
        return False

    return True

def test_env_file():
    """Test that .env file exists and has required variables."""
    print("\nChecking environment configuration...")

    env_path = Path("config/.env")
    if not env_path.exists():
        print("  ❌ config/.env file not found")
        print("     Run: copy config\\.env.example config\\.env")
        return False

    print("  ✓ config/.env file exists")

    # Try loading environment variables
    from dotenv import load_dotenv
    load_dotenv(env_path)

    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key or api_key == "your_anthropic_api_key_here":
        print("  ⚠ ANTHROPIC_API_KEY not set or using placeholder")
        print("     Edit config/.env and add your API key from https://console.anthropic.com/")
        return False

    print("  ✓ ANTHROPIC_API_KEY is set")
    return True

def test_api_connection():
    """Test connection to Anthropic API."""
    print("\nTesting API connection...")

    from dotenv import load_dotenv
    from anthropic import Anthropic

    load_dotenv("config/.env")
    api_key = os.getenv("ANTHROPIC_API_KEY")

    if not api_key or api_key == "your_anthropic_api_key_here":
        print("  ⚠ Skipping API test (no valid API key)")
        return None

    try:
        client = Anthropic(api_key=api_key)
        response = client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=100,
            messages=[{"role": "user", "content": "Hello, Claude! Respond with just 'API test successful'."}]
        )
        print("  ✓ API connection successful")
        print(f"  ✓ Response: {response.content[0].text[:60]}...")
        return True
    except Exception as e:
        print(f"  ❌ API connection failed: {e}")
        return False

def test_directories():
    """Test that required directories exist."""
    print("\nChecking directory structure...")

    required_dirs = [
        "skills/transcript-analysis",
        "skills/transcript-analysis/domain-knowledge",
        "data/sample-transcripts",
        "outputs/analysis",
        "outputs/bpmn-diagrams",
        "outputs/recommendations",
        "notebooks",
        "config"
    ]

    all_exist = True
    for dir_path in required_dirs:
        path = Path(dir_path)
        if path.exists():
            print(f"  ✓ {dir_path}")
        else:
            print(f"  ❌ {dir_path} - directory missing")
            all_exist = False

    return all_exist

def test_skill_files():
    """Test that skill files exist."""
    print("\nChecking skill files...")

    required_files = [
        "skills/transcript-analysis/SKILL.md",
        "skills/transcript-analysis/README.md",
        "skills/transcript-analysis/domain-knowledge/example-01-ap-transcript.txt",
        "skills/transcript-analysis/domain-knowledge/example-01-ap-analysis.md"
    ]

    all_exist = True
    for file_path in required_files:
        path = Path(file_path)
        if path.exists():
            print(f"  ✓ {file_path}")
        else:
            print(f"  ❌ {file_path} - file missing")
            all_exist = False

    return all_exist

def main():
    """Run all verification tests."""
    print("=" * 70)
    print("TRANSFORMATION CONSULTANT AGENT - SETUP VERIFICATION")
    print("=" * 70)

    # Change to project root if we're not already there
    script_dir = Path(__file__).parent
    os.chdir(script_dir)

    results = {
        "imports": test_imports(),
        "env": test_env_file(),
        "directories": test_directories(),
        "skill_files": test_skill_files()
    }

    # API test is optional if no key is set
    api_result = test_api_connection()
    if api_result is not None:
        results["api"] = api_result

    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)

    passed = sum(1 for v in results.values() if v is True)
    total = len(results)

    for test_name, result in results.items():
        status = "✓ PASS" if result else "❌ FAIL"
        print(f"{status}: {test_name}")

    print(f"\n{passed}/{total} tests passed")

    if all(results.values()):
        print("\n✅ All tests passed! Your environment is ready.")
        print("\nNext steps:")
        print("  1. Create notebooks/01-transcript-analysis-prototype.ipynb")
        print("  2. Test the transcript analysis skill")
        print("  3. See skills/transcript-analysis/README.md for usage examples")
        return 0
    else:
        print("\n⚠ Some tests failed. Please fix the issues above and run again.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
