#!/usr/bin/env python3
"""
Automated tests for BIG6 game.
Compares actual output with expected output for deterministic test cases.
"""

import subprocess
import sys
import os
from pathlib import Path


def run_test(test_name: str) -> bool:
    """Run a single test case and return True if passed."""
    tests_dir = Path(__file__).parent / "tests"
    input_file = tests_dir / f"{test_name}.input"
    expected_file = tests_dir / f"{test_name}.expected"

    if not input_file.exists():
        print(f"SKIP {test_name}: input file not found")
        return True

    if not expected_file.exists():
        print(f"SKIP {test_name}: expected file not found")
        return True

    env = os.environ.copy()
    env["BIG6_SEED"] = "42"

    with open(input_file, "r") as f:
        input_data = f.read()

    result = subprocess.run(
        [sys.executable, "big6.py"],
        input=input_data,
        capture_output=True,
        text=True,
        env=env,
    )

    actual = result.stdout
    with open(expected_file, "r") as f:
        expected = f.read()

    if actual == expected:
        print(f"PASS {test_name}")
        return True
    else:
        print(f"FAIL {test_name}")
        print("--- Expected ---")
        print(expected)
        print("--- Actual ---")
        print(actual)
        return False


def main() -> int:
    tests_dir = Path(__file__).parent / "tests"
    test_names = sorted(
        set(p.stem for p in tests_dir.glob("*.input"))
    )

    if not test_names:
        print("No tests found in tests/ directory")
        return 1

    passed = 0
    failed = 0

    for test_name in test_names:
        if run_test(test_name):
            passed += 1
        else:
            failed += 1

    print()
    print(f"Results: {passed} passed, {failed} failed")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
