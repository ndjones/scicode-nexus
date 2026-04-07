#!/usr/bin/env python3
"""
Unit tests for verify_openhands.py
"""

import os
import sys
from unittest.mock import patch, MagicMock

def test_imports():
    """Test that we can import the module"""
    # Add the project root to the path
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
    try:
        import verify_openhands
        return True
    except Exception as e:
        print(f"Import failed: {e}")
        return False

def test_main_function_exists():
    """Test that main function exists"""
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
    import verify_openhands
    assert hasattr(verify_openhands, 'main')
    assert callable(verify_openhands.main)

def test_successful_connection():
    """Test successful connection scenario"""
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
    
    with patch('verify_openhands.requests.get') as mock_get:
        # Mock a successful response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = "<html>OpenHands</html>"
        mock_get.return_value = mock_response
        
        import verify_openhands
        # Call main and check return value
        ret = verify_openhands.main()
        assert ret == 0

def test_non_200_response():
    """Test non-200 response scenario"""
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
    
    with patch('verify_openhands.requests.get') as mock_get:
        # Mock a non-200 response
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.text = "Not Found"
        mock_get.return_value = mock_response
        
        import verify_openhands
        # Call main and check return value
        ret = verify_openhands.main()
        assert ret == 1

def test_connection_error():
    """Test connection error scenario"""
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
    
    with patch('verify_openhands.requests.get') as mock_get:
        # Mock a connection error
        import requests
        mock_get.side_effect = requests.exceptions.ConnectionError("Failed to connect")
        
        import verify_openhands
        # Call main and check return value
        ret = verify_openhands.main()
        assert ret == 1

def test_timeout():
    """Test timeout scenario"""
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
    
    with patch('verify_openhands.requests.get') as mock_get:
        # Mock a timeout
        import requests
        mock_get.side_effect = requests.exceptions.Timeout("Timeout")
        
        import verify_openhands
        # Call main and check return value
        ret = verify_openhands.main()
        assert ret == 1

def test_unexpected_error():
    """Test unexpected error scenario"""
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
    
    with patch('verify_openhands.requests.get') as mock_get:
        # Mock an unexpected error
        mock_get.side_effect = Exception("Unexpected error")
        
        import verify_openhands
        # Call main and check return value
        ret = verify_openhands.main()
        assert ret == 1

if __name__ == "__main__":
    print("Running verify_openhands tests...")
    assert test_imports(), "Import test failed"
    test_main_function_exists()
    print("Main function test passed")
    test_successful_connection()
    print("Successful connection test passed")
    test_non_200_response()
    print("Non-200 response test passed")
    test_connection_error()
    print("Connection error test passed")
    test_timeout()
    print("Timeout test passed")
    test_unexpected_error()
    print("Unexpected error test passed")
    print("All tests passed!")