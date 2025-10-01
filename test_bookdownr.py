# test_bookdownr.py
"""
Tests for BookdownR module.
"""

import unittest
from bookdownr import BookdownR

class TestBookdownR(unittest.TestCase):
    """Test cases for BookdownR class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BookdownR()
        self.assertIsInstance(instance, BookdownR)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BookdownR()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
