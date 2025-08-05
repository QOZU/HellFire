# test_hellfire.py
"""
Tests for HellFire module.
"""

import unittest
from hellfire import HellFire

class TestHellFire(unittest.TestCase):
    """Test cases for HellFire class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HellFire()
        self.assertIsInstance(instance, HellFire)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HellFire()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
