#!/usr/bin/env python3
"""
Verify connectivity to the OpenHands API.
This script attempts to connect to the OpenHands service running on localhost:8080.
It is intended to be run after starting the services with `docker-compose up`.
"""

import sys
import requests

def main():
    url = "http://localhost:3000"
    try:
        # Try to get a response from the OpenHands service
        # We'll try the root endpoint; adjust if there's a specific health check endpoint
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print(f"SUCCESS: OpenHands API is reachable at {url}")
            print(f"Response status: {response.status_code}")
            # Optionally, print a snippet of the response
            print(f"Response preview: {response.text[:200]}")
            return 0
        else:
            print(f"WARNING: OpenHands API returned status {response.status_code}")
            print(f"Response: {response.text[:200]}")
            return 1
    except requests.exceptions.ConnectionError as e:
        print(f"ERROR: Failed to connect to OpenHands API at {url}")
        print(f"Details: {e}")
        print("Make sure the OpenHands service is running (docker-compose up openhands)")
        return 1
    except requests.exceptions.Timeout:
        print(f"ERROR: Timeout connecting to OpenHands API at {url}")
        return 1
    except Exception as e:
        print(f"ERROR: Unexpected error: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())