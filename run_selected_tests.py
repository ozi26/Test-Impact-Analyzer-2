#!/usr/bin/env python3
# =============================================================================
# RUN SELECTED TESTS
# This script reads analyzer_result.json and runs ONLY the affected tests.
# Jenkins calls this script automatically.
# =============================================================================

import json
import sys
import subprocess
from pathlib import Path


def main():
    """Read analysis results and run only the affected tests."""
    
    # Step 1: Find the analysis result file
    result_file = Path("analyzer_result.json")
    
    if not result_file.exists():
        print("ERROR: analyzer_result.json not found!")
        print("Run the analyzer first: python scripts/run_analyzer.py")
        sys.exit(1)
    
    # Step 2: Read the analysis results
    with open(result_file, "r", encoding="utf-8") as f:
        result = json.load(f)
    
    # Step 3: Check if there are affected tests
    if not result.get("has_affected_tests", False):
        print("=" * 60)
        print("NO AFFECTED TESTS - Skipping test execution")
        print("=" * 60)
        sys.exit(0)  # Exit successfully (nothing to run)
    
    affected_tests = result["affected_tests"]
    
    print("=" * 60)
    print(f"Running {len(affected_tests)} affected test file(s):")
    for test in affected_tests:
        print(f"  - {test}")
    print("=" * 60)
    
    # Step 4: Build the pytest command
    # pytest is the test runner we use to execute the selected tests
    cmd = [sys.executable, "-m", "pytest"] + affected_tests + ["-v"]
    
    print(f"\nExecuting: {' '.join(cmd)}\n")
    
    # Step 5: Run the tests
    # subprocess.run() executes the command and waits for it to finish
    result = subprocess.run(cmd)
    
    # Step 6: Exit with pytest's return code
    # 0 = all tests passed, non-zero = some tests failed
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()