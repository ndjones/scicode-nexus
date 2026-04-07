#!/usr/bin/env python3
"""
Cognify Initialization Script

This script triggers the first ECL (Entity-Contrast-Learning) pipeline on the
/src and /papers directories using cognee.

Prerequisites:
1. Install dependencies: pip install -r requirements.txt
2. Start required services: docker-compose up (for cognee and postgres)

Usage:
    python cognify_init.py
"""

import os
import sys
from pathlib import Path

def main():
    # Ensure we are in the workspace root
    workspace_root = Path(__file__).parent
    src_dir = workspace_root / "src"
    papers_dir = workspace_root / "papers"

    # Check if directories exist
    if not src_dir.exists():
        print(f"Error: Source directory not found at {src_dir}")
        sys.exit(1)
    if not papers_dir.exists():
        print(f"Error: Papers directory not found at {papers_dir}")
        sys.exit(1)

    try:
        import cognee
        from cognee.api.v1.add import add
        from cognee.api.v1.cognify import cognify
    except ImportError as e:
        print(f"Error importing cognee: {e}")
        print("Please install dependencies with: pip install -r requirements.txt")
        sys.exit(1)

    print("Starting ECL pipeline on src and papers directories...")
    print(f"Source directory: {src_dir}")
    print(f"Papers directory: {papers_dir}")

    import asyncio

    # Add the files in the directories to cognee
    print("\nAdding source directory...")
    for file_path in src_dir.rglob("*"):
        if file_path.is_file():
            print(f"Adding {file_path}...")
            asyncio.run(add(str(file_path)))

    print("\nAdding papers directory...")
    for file_path in papers_dir.rglob("*"):
        if file_path.is_file():
            print(f"Adding {file_path}...")
            asyncio.run(add(str(file_path)))

    # Run the ECL pipeline (cognify)
    print("\nRunning ECL pipeline (cognify)...")
    asyncio.run(cognify())

    print("\nECL pipeline completed successfully!")

if __name__ == "__main__":
    main()