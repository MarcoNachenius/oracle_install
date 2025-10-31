import unittest
import numpy as np

from tonerow_analyzer.tonerow_class import ToneRow

class TestBasicRowAttributes(unittest.TestCase):
    """Simple tests for the four basic row transformation methods"""
    
    def test_prime_row_identity(self):
        """Test prime_row() with identity row [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]"""
        test_row = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
        tone_row = ToneRow(test_row)
        
        expected_prime = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
        result = tone_row.prime_row()
        
        np.testing.assert_array_equal(result, expected_prime)

    def test_inversion_identity(self):
        """Test inversion() with identity row"""
        test_row = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
        tone_row = ToneRow(test_row)
        
        expected_inversion = np.array([0, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
        result = tone_row.inversion()
        
        np.testing.assert_array_equal(result, expected_inversion)

    def test_retrograde_identity(self):
        """Test retrograde() with identity row"""
        test_row = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
        tone_row = ToneRow(test_row)
        
        # R0 = reverse of P0 = reverse of [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        expected_retrograde = np.array([11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
        result = tone_row.retrograde()
        
        np.testing.assert_array_equal(result, expected_retrograde)

    def test_retrograde_inversion_identity(self):
        """Test retrograde_inversion() with identity row"""
        test_row = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
        tone_row = ToneRow(test_row)

        # RI0 = reverse of I0 = reverse of [0, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        expected_retrograde_inversion = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0])
        result = tone_row.retrograde_inversion()

        np.testing.assert_array_equal(result, expected_retrograde_inversion)

    def test_prime_row_webern(self):
        """Test prime_row() with Webern's row"""
        test_row = np.array([0, 11, 3, 4, 8, 7, 9, 5, 6, 1, 2, 10])
        tone_row = ToneRow(test_row)
        
        expected_prime = np.array([0, 11, 3, 4, 8, 7, 9, 5, 6, 1, 2, 10])
        result = tone_row.prime_row()
        
        np.testing.assert_array_equal(result, expected_prime)

    def test_inversion_webern(self):
        """Test inversion() with Webern's row"""
        test_row = np.array([0, 11, 3, 4, 8, 7, 9, 5, 6, 1, 2, 10])
        tone_row = ToneRow(test_row)
        
        expected_inversion = np.array([0, 1, 9, 8, 4, 5, 3, 7, 6, 11, 10, 2])
        result = tone_row.inversion()
        
        np.testing.assert_array_equal(result, expected_inversion)

    def test_retrograde_webern(self):
        """Test retrograde() with Webern's row"""
        test_row = np.array([0, 11, 3, 4, 8, 7, 9, 5, 6, 1, 2, 10])
        tone_row = ToneRow(test_row)
        
        expected_retrograde = np.array([10, 2, 1, 6, 5, 9, 7, 8, 4, 3, 11, 0])
        result = tone_row.retrograde()
        
        np.testing.assert_array_equal(result, expected_retrograde)

    def test_retrograde_inversion_webern(self):
        """Test retrograde_inversion() with Webern's row"""
        test_row = np.array([0, 11, 3, 4, 8, 7, 9, 5, 6, 1, 2, 10])
        tone_row = ToneRow(test_row)
        
        expected_retrograde_inversion = np.array([2, 10, 11, 6, 7, 3, 5, 4, 8, 9, 1, 0])
        result = tone_row.retrograde_inversion()
        
        np.testing.assert_array_equal(result, expected_retrograde_inversion)

    def test_prime_row_berg(self):
        """Test prime_row() with Berg's row"""
        test_row = np.array([0, 11, 7, 4, 2, 9, 3, 8, 10, 1, 5, 6])
        tone_row = ToneRow(test_row)
        
        expected_prime = np.array([0, 11, 7, 4, 2, 9, 3, 8, 10, 1, 5, 6])
        result = tone_row.prime_row()
        
        np.testing.assert_array_equal(result, expected_prime)

    def test_inversion_berg(self):
        """Test inversion() with Berg's row"""
        test_row = np.array([0, 11, 7, 4, 2, 9, 3, 8, 10, 1, 5, 6])
        tone_row = ToneRow(test_row)
        
        expected_inversion = np.array([0, 1, 5, 8, 10, 3, 9, 4, 2, 11, 7, 6])
        result = tone_row.inversion()
        
        np.testing.assert_array_equal(result, expected_inversion)

    def test_relationships_identity_row(self):
        """Test mathematical relationships between forms with identity row"""
        test_row = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
        tone_row = ToneRow(test_row)
        
        p0 = tone_row.prime_row()
        i0 = tone_row.inversion()
        r0 = tone_row.retrograde()
        ri0 = tone_row.retrograde_inversion()
        
        # R0 should be reverse of P0
        expected_r0 = p0[::-1]
        np.testing.assert_array_equal(r0, expected_r0)
        
        # RI0 should be reverse of I0
        expected_ri0 = i0[::-1]
        np.testing.assert_array_equal(ri0, expected_ri0)
        
        # P0 and I0 should start on same pitch
        self.assertEqual(p0[0], i0[0])

    def test_relationships_webern_row(self):
        """Test mathematical relationships between forms with Webern's row"""
        test_row = np.array([0, 11, 3, 4, 8, 7, 9, 5, 6, 1, 2, 10])
        tone_row = ToneRow(test_row)
        
        p0 = tone_row.prime_row()
        i0 = tone_row.inversion()
        r0 = tone_row.retrograde()
        ri0 = tone_row.retrograde_inversion()
        
        # R0 should be reverse of P0
        expected_r0 = p0[::-1]
        np.testing.assert_array_equal(r0, expected_r0)
        
        # RI0 should be reverse of I0
        expected_ri0 = i0[::-1]
        np.testing.assert_array_equal(ri0, expected_ri0)
        
        # P0 and I0 should start on same pitch
        self.assertEqual(p0[0], i0[0])

if __name__ == '__main__':
    unittest.main(verbosity=2)