#!/usr/bin/env python3
"""
Unit tests for cognify_init.py
"""

import os
import sys
import tempfile
from pathlib import Path
from unittest.mock import patch, MagicMock, AsyncMock

def test_imports():
    """Test that we can import the module"""
    # Add the project root to the path
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
    try:
        import cognify_init
        return True
    except Exception as e:
        print(f"Import failed: {e}")
        return False

def test_main_function_exists():
    """Test that main function exists"""
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
    import cognify_init
    assert hasattr(cognify_init, 'main')
    assert callable(cognify_init.main)

def test_missing_src_dir_exits_early():
    """Test that cognify_init exits early when src directory is missing"""
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
    
    # Create a temporary directory structure for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        src_dir = temp_path / "src"
        papers_dir = temp_path / "papers"
        # Create papers dir but not src dir
        papers_dir.mkdir()
        
        with patch('cognify_init.Path') as mock_path:
            # Mock the __file__ attribute to return our temp directory
            mock_path.return_value.parent = temp_path
            mock_path.return_value.__truediv__.side_effect = lambda x: temp_path / x
            
            # Mock exists to return appropriate values
            def exists_side_effect(self):
                if str(self).endswith('src'):
                    return False
                elif str(self).endswith('papers'):
                    return True
                return True  # For the path itself
            
            mock_path.return_value.exists = exists_side_effect
            
            import cognify_init
            with patch('sys.exit') as mock_exit:
                mock_exit.side_effect = SystemExit
                with patch('builtins.print'):
                    try:
                        cognify_init.main()
                    except SystemExit:
                        pass  # Expected
                    mock_exit.assert_called_with(1)
                    # Check that the error message was printed
                    # Note: We can't easily check print calls with the SystemExit approach
                    # but we know the exit happened

def test_missing_papers_dir_exits_early():
    """Test that cognify_init exits early when papers directory is missing"""
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
    
    # Create a temporary directory structure for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        src_dir = temp_path / "src"
        papers_dir = temp_path / "papers"
        # Create src dir but not papers dir
        src_dir.mkdir()
        
        with patch('cognify_init.Path') as mock_path:
            # Mock the __file__ attribute to return our temp directory
            mock_path.return_value.parent = temp_path
            mock_path.return_value.__truediv__.side_effect = lambda x: temp_path / x
            
            # Mock exists to return appropriate values
            def exists_side_effect(self):
                if str(self).endswith('src'):
                    return True
                elif str(self).endswith('papers'):
                    return False
                return True  # For the path itself
            
            mock_path.return_value.exists = exists_side_effect
            
            import cognify_init
            with patch('sys.exit') as mock_exit:
                mock_exit.side_effect = SystemExit
                with patch('builtins.print'):
                    try:
                        cognify_init.main()
                    except SystemExit:
                        pass  # Expected
                    mock_exit.assert_called_with(1)

def test_import_error_exits_early():
    """Test that cognify_init exits early when cognee import fails"""
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
    
    with patch('cognify_init.Path') as mock_path:
        # Mock directories to exist
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            src_dir = temp_path / "src"
            papers_dir = temp_path / "papers"
            src_dir.mkdir()
            papers_dir.mkdir()
            
            mock_path.return_value.parent = temp_path
            mock_path.return_value.__truediv__.side_effect = lambda x: temp_path / x
            mock_path.return_value.exists.return_value = True
            
            # Mock the import to fail by making cognee not have api attribute
            mock_cognee = MagicMock()
            type(mock_cognee).api = MagicMock(side_effect=AttributeError("'NoneType' object has no attribute 'api'"))
            
            with patch.dict('sys.modules', {'cognee': mock_cognee}):
                import cognify_init
                with patch('sys.exit') as mock_exit:
                    mock_exit.side_effect = SystemExit
                    with patch('builtins.print'):
                        try:
                            cognify_init.main()
                        except SystemExit:
                            pass  # Expected
                        mock_exit.assert_called_with(1)

def test_successful_run_calls_expected_functions():
    """Test that cognify_init calls the expected functions when everything works"""
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
    
    with patch('cognify_init.Path') as mock_path:
        # Mock directories to exist
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            src_dir = temp_path / "src"
            papers_dir = temp_path / "papers"
            src_dir.mkdir()
            papers_dir.mkdir()
            
            # Create some dummy files
            (src_dir / "dummy1.txt").touch()
            (src_dir / "dummy2.txt").touch()
            (papers_dir / "dummy3.txt").touch()
            (papers_dir / "dummy4.txt").touch()
            
            mock_path.return_value.parent = temp_path
            mock_path.return_value.__truediv__.side_effect = lambda x: temp_path / x
            mock_path.return_value.exists.return_value = True
            
            # Mock the cognee imports and functions at the source
            mock_add = AsyncMock()
            mock_cognify = AsyncMock()
            
            with patch('cognee.api.v1.add.add', mock_add):
                with patch('cognee.api.v1.cognify.cognify', mock_cognify):
                    import cognify_init
                    with patch('builtins.print'):
                        cognify_init.main()
                        
                        # Check that add was called for each file (4 files total)
                        assert mock_add.call_count == 4
                        
                        # Check that cognify was called once
                        mock_cognify.assert_called_once()

if __name__ == "__main__":
    print("Running cognify_init tests...")
    assert test_imports(), "Import test failed"
    test_main_function_exists()
    print("Main function test passed")
    test_missing_src_dir_exits_early()
    print("Missing src dir test passed")
    test_missing_papers_dir_exits_early()
    print("Missing papers dir test passed")
    test_import_error_exits_early()
    print("Import error test passed")
    test_successful_run_calls_expected_functions()
    print("Successful run test passed")
    print("All tests passed!")