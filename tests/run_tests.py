#!/usr/bin/env python3
"""
Test runner for bootstrap scripts
"""

import subprocess
import sys
import os

def run_tests():
    """Run all tests using pytest"""
    # Change to the project root directory
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(project_root)
    
    # Run pytest on the tests directory
    result = subprocess.run([
        sys.executable, "-m", "pytest", 
        "tests/", 
        "-v"
    ], capture_output=True, text=True)
    
    print("STDOUT:")
    print(result.stdout)
    print("\nSTDERR:")
    print(result.stderr)
    print(f"\nReturn code: {result.returncode}")
    
    return result.returncode == 0

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)