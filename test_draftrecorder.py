# test_draftrecorder.py
"""
Tests for DraftRecorder module.
"""

import unittest
from draftrecorder import DraftRecorder

class TestDraftRecorder(unittest.TestCase):
    """Test cases for DraftRecorder class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DraftRecorder()
        self.assertIsInstance(instance, DraftRecorder)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DraftRecorder()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
