import unittest
import numpy as np
from tonerow_analyzer.tonerow_class import ToneRow

class TestToneRowValidation(unittest.TestCase):
    """Tests for tone row validation"""
    
    def test_valid_tonerow(self):
        valid_row = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
        tone_row = ToneRow(valid_row)
        self.assertIsInstance(tone_row, ToneRow)
    
    def test_invalid_short_row(self):
        short_row = np.array([0, 1, 2, 3])
        with self.assertRaises(ValueError):
            ToneRow(short_row)
    
    def test_invalid_duplicate_row(self):
        duplicate_row = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10])  # Duplicate 10
        with self.assertRaises(ValueError):
            ToneRow(duplicate_row)


if __name__ == '__main__':
    unittest.main()