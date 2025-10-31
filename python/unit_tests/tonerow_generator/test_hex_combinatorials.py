import unittest
import numpy as np
from tonerow_analyzer.tonerow_class import ToneRow
from tonerow_analyzer.combinatorial_hexachords import CombinatorialHexachords

class TestPrimeCombinatorials(unittest.TestCase):
    
    def test_chromatic_row_returns_p6(self):
        """Test that chromatic scale row returns only P6 as combinatorial"""
        chromatic_row = ToneRow(np.arange(12))  # [0,1,2,3,4,5,6,7,8,9,10,11]
        result = CombinatorialHexachords.prime_combinatorials(chromatic_row)
        # P0 first hexachord: {0,1,2,3,4,5}
        # P6 first hexachord: {6,7,8,9,10,11} ← Perfect complement of P0's first hexachord
        # No other transposition produces this exact complement set
        self.assertEqual(result, ['P6'])


    def test_6_20_hexachord_row_returns_multiple_combinatorials(self):
        """Test that 6-20 hexachord type returns P2, P6, P10"""
        # Row with first hexachord {0,1,4,5,8,9} (6-20)
        row_6_20 = ToneRow(np.array([0, 1, 4, 5, 8, 9, 2, 3, 6, 7, 10, 11]))
        result = CombinatorialHexachords.prime_combinatorials(row_6_20)
        # P0 first hexachord: {0,1,4,5,8,9}
        # P2 first hexachord: {2,3,6,7,10,11} ← Complement of P0's first hexachord
        # P6 first hexachord: {6,7,10,11,2,3} ← Complement of P0's first hexachord (reordered)
        # P10 first hexachord: {10,11,2,3,6,7} ← Complement of P0's first hexachord (reordered)
        expected = ['P2', 'P6', 'P10']
        self.assertEqual(sorted(result), sorted(expected))
        self.assertEqual(len(result), 3)
    

    def test_chromatic_row_retrograde_returns_empty_list(self):
        """Test that chromatic scale row returns empty list for retrograde combinatorials (only R0 is combinatorial)"""
        chromatic_row = ToneRow(np.arange(12))  # [0,1,2,3,4,5,6,7,8,9,10,11]
        result = CombinatorialHexachords.retrograde_combinatorials(chromatic_row)
        # P0 first hexachord: {0,1,2,3,4,5}
        # R0 first hexachord: {11,10,9,8,7,6} ← Only retrograde form that complements P0's first hexachord
        # Since we exclude R0, result should be empty
        self.assertEqual(result, [])


    def test_6_20_hexachord_row_returns_multiple_retrograde_combinatorials(self):
        """Test that 6-20 hexachord type returns R4 and R8 as retrograde combinatorials"""
        # Row with first hexachord {0,1,4,5,8,9} (6-20)
        row_6_20 = ToneRow(np.array([0, 1, 4, 5, 8, 9, 2, 3, 6, 7, 10, 11]))
        result = CombinatorialHexachords.retrograde_combinatorials(row_6_20)
        # P0 first hexachord: {0,1,4,5,8,9}
        # R4 first hexachord: {7,10,11,2,3,6} ← Complement of P0's first hexachord
        # R8 first hexachord: {11,2,3,6,7,10} ← Complement of P0's first hexachord (reordered)
        expected = ['R4', 'R8']
        self.assertEqual(sorted(result), sorted(expected))
        self.assertEqual(len(result), 2)

    def test_chromatic_row_inversion_returns_i11(self):
        """Test that chromatic scale row returns only I11 as inversion combinatorial"""
        chromatic_row = ToneRow(np.arange(12))  # [0,1,2,3,4,5,6,7,8,9,10,11]
        result = CombinatorialHexachords.inversion_combinatorials(chromatic_row)
        # P0 first hexachord: {0,1,2,3,4,5}
        # I11 first hexachord: {11,10,9,8,7,6} ← Only inversion form that complements P0's first hexachord
        self.assertEqual(result, ['I11'])
    
    def test_6_20_hexachord_row_returns_multiple_inversion_combinatorials(self):
        """Test that 6-20 hexachord type returns I3, I7, and I11 as inversion combinatorials"""
        # Row with first hexachord {0,1,4,5,8,9} (6-20)
        row_6_20 = ToneRow(np.array([0, 1, 4, 5, 8, 9, 2, 3, 6, 7, 10, 11]))
        result = CombinatorialHexachords.inversion_combinatorials(row_6_20)
        # P0 first hexachord: {0,1,4,5,8,9}
        # I3 first hexachord: {3,2,11,10,7,6} ← Complement of P0's first hexachord
        # I7 first hexachord: {7,6,3,2,11,10} ← Complement of P0's first hexachord (reordered)
        # I11 first hexachord: {11,10,7,6,3,2} ← Complement of P0's first hexachord (reordered)
        expected = ['I3', 'I7', 'I11']
        self.assertEqual(sorted(result), sorted(expected))
        self.assertEqual(len(result), 3)
    
    def test_chromatic_row_retrograde_inversion_returns_ri5(self):
        """Test that chromatic scale row returns only RI5 as retrograde inversion combinatorial"""
        chromatic_row = ToneRow(np.arange(12))  # [0,1,2,3,4,5,6,7,8,9,10,11]
        result = CombinatorialHexachords.retrograde_inversion_combinatorials(chromatic_row)
        # P0 first hexachord: {0,1,2,3,4,5}
        # RI5 first hexachord: {5,4,3,2,1,0} ← Only retrograde inversion form that complements P0's first hexachord
        self.assertEqual(result, ['RI5'])
    
    def test_6_20_hexachord_row_returns_multiple_retrograde_inversion_combinatorials(self):
        """Test that 6-20 hexachord type returns RI1, RI5, and RI9 as retrograde inversion combinatorials"""
        # Row with first hexachord {0,1,4,5,8,9} (6-20)
        row_6_20 = ToneRow(np.array([0, 1, 4, 5, 8, 9, 2, 3, 6, 7, 10, 11]))
        result = CombinatorialHexachords.retrograde_inversion_combinatorials(row_6_20)
        # P0 first hexachord: {0,1,4,5,8,9}
        # RI1 first hexachord: {1,0,9,8,5,4} ← Complement of P0's first hexachord
        # RI5 first hexachord: {5,4,1,0,9,8} ← Complement of P0's first hexachord (reordered)
        # RI9 first hexachord: {9,8,5,4,1,0} ← Complement of P0's first hexachord (reordered)
        expected = ['RI1', 'RI5', 'RI9']
        self.assertEqual(sorted(result), sorted(expected))
        self.assertEqual(len(result), 3)
    
if __name__ == '__main__':
    unittest.main()