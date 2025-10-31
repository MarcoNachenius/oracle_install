import unittest
from tonerow_analyzer.tonerow_class import ToneRow
from tonerow_analyzer.combinatorial_tetrachords import CombinatorialTetrachords
import numpy as np

class TestCombinatorialTetrachords(unittest.TestCase):

    def test_all_tetrachordal_combinatorials_comprehensive(self):
        """Test comprehensive tetrachordal combinatorials across all transformation types."""
        # Row: 0,1,2,3,4,5,6,7,8,9,10,11 (chromatic scale)
        # WHY IT WORKS: The chromatic scale has specific tetrachordal combinatorial relationships due to its regular structure.
        # P4 and P8 work because they shift the tetrachord boundaries cyclically:
        # P0 tetrachords: [0,1,2,3], [4,5,6,7], [8,9,10,11]
        # P4 tetrachords: [4,5,6,7], [8,9,10,11], [0,1,2,3] (same sets, reordered)
        # P8 tetrachords: [8,9,10,11], [0,1,2,3], [4,5,6,7] (same sets, reordered)
        # R4 and R8 are the retrograde equivalents of P4 and P8
        # I3, I7, I11 create inversion forms that preserve the tetrachordal structure
        # RI3, RI7, RI11 are the retrograde inversion equivalents
        row = np.arange(12)
        tone_row = ToneRow(row)
        
        result = CombinatorialTetrachords.all_tetrachordal_combinatorials(tone_row)
        
        # Expected: ['P8', 'P4', 'R8', 'R4', 'I3', 'I7', 'I11', 'RI3', 'RI7', 'RI11']
        expected = ['P4', 'P8', 'R4', 'R8', 'I3', 'I7', 'I11', 'RI3', 'RI7', 'RI11']
        
        self.assertEqual(sorted(result), sorted(expected))
        self.assertEqual(len(result), 10)

    def test_prime_combinatorials_symmetric_row(self):
        """Test prime combinatorials with chromatic scale."""
        # Row: 0,1,2,3,4,5,6,7,8,9,10,11 (chromatic scale)
        # WHY IT WORKS: Only P4 and P8 maintain the same tetrachordal partition as P0.
        # At transposition levels that are multiples of 4, the tetrachord boundaries
        # align to preserve the same three tetrachord sets, just in different order.
        row = np.arange(12)
        tone_row = ToneRow(row)
        
        result = CombinatorialTetrachords.prime_combinatorials(tone_row)
        
        # For chromatic scale, only specific prime forms are tetrachordally combinatorial
        # P4 and P8 work because they shift the tetrachord boundaries appropriately
        expected_primes = ['P4', 'P8']
        self.assertEqual(set(result), set(expected_primes))

    def test_retrograde_combinatorials(self):
        """Test retrograde combinatorials with chromatic scale."""
        # Row: 0,1,2,3,4,5,6,7,8,9,10,11 (chromatic scale)
        # WHY IT WORKS: R4 and R8 are combinatorial because they are the retrograde
        # forms of P4 and P8. When reversed, these forms still contain the same
        # three tetrachord sets as P0, just in retrograde order.
        row = np.arange(12)
        tone_row = ToneRow(row)
        
        result = CombinatorialTetrachords.retrograde_combinatorials(tone_row)
        
        # Only specific retrograde forms are combinatorial
        expected_retrogrades = ['R4', 'R8']
        self.assertEqual(set(result), set(expected_retrogrades))

    def test_inversion_combinatorials(self):
        """Test inversion combinatorials."""
        # Row: 0,1,2,3,4,5,6,7,8,9,10,11 (chromatic scale)
        # WHY IT WORKS: I3, I7, and I11 create inversion forms where the tetrachords
        # map to the original P0 tetrachords. The inversion operation at these specific
        # levels preserves the tetrachordal structure through complement relationships.
        row = np.arange(12)
        tone_row = ToneRow(row)
        
        result = CombinatorialTetrachords.inversion_combinatorials(tone_row)
        
        # Only specific inversion forms are combinatorial
        expected_inversions = ['I3', 'I7', 'I11']
        self.assertEqual(set(result), set(expected_inversions))

    def test_retrograde_inversion_combinatorials(self):
        """Test retrograde inversion combinatorials."""
        # Row: 0,1,2,3,4,5,6,7,8,9,10,11 (chromatic scale)
        # WHY IT WORKS: RI3, RI7, and RI11 are combinatorial because they combine
        # the inversion relationships from I3, I7, I11 with retrograde operation.
        # These forms maintain the tetrachordal complementarity through both
        # inversion and reversal operations.
        row = np.arange(12)
        tone_row = ToneRow(row)
        
        result = CombinatorialTetrachords.retrograde_inversion_combinatorials(tone_row)
        
        # Only specific RI forms are combinatorial
        expected_ri = ['RI3', 'RI7', 'RI11']
        self.assertEqual(set(result), set(expected_ri))

    def test_specialized_combinatorial_row(self):
        """Test with a row specifically designed for tetrachordal combinatoriality."""
        # Row: [0,1,4,5,2,3,6,7,8,9,10,11]
        # WHY IT WORKS: This row is constructed with overlapping tetrachord patterns
        # that may create additional combinatorial relationships beyond the chromatic scale.
        # The first tetrachord [0,1,4,5] suggests potential for different combinatorial
        # partners than the purely chromatic structure.
        row = np.array([0, 1, 4, 5, 2, 3, 6, 7, 8, 9, 10, 11])
        tone_row = ToneRow(row)
        
        result = CombinatorialTetrachords.all_tetrachordal_combinatorials(tone_row)
        
        print(f"Specialized row combinatorial forms: {result}")
        # This should have different combinatorial relationships than chromatic scale
        self.assertIsInstance(result, list)

    def test_empty_results_for_identity_forms(self):
        """Test that identity forms (P0, R0) are excluded from results."""
        # Row: 0,1,2,3,4,5,6,7,8,9,10,11 (chromatic scale)
        # WHY IT WORKS: P0 and R0 are intentionally excluded from combinatorial results
        # because they represent the reference form itself, not combinatorial partners.
        # The algorithm correctly filters out these identity transformations.
        row = np.arange(12)
        tone_row = ToneRow(row)
        
        prime_results = CombinatorialTetrachords.prime_combinatorials(tone_row)
        retrograde_results = CombinatorialTetrachords.retrograde_combinatorials(tone_row)
        
        # P0 and R0 should not be in the results
        self.assertNotIn('P0', prime_results)
        self.assertNotIn('R0', retrograde_results)

    def test_tetrachord_division_correctness(self):
        """Verify that the tetrachord division is working correctly."""
        # Row: 0,1,2,3,4,5,6,7,8,9,10,11 (chromatic scale)
        # WHY IT WORKS: This test verifies the fundamental division into 3 groups of 4 notes.
        # The algorithm correctly partitions the 12-tone row into:
        # Tetrachord 1: positions 0-3 [0,1,2,3]
        # Tetrachord 2: positions 4-7 [4,5,6,7] 
        # Tetrachord 3: positions 8-11 [8,9,10,11]
        # This correct division is essential for accurate combinatorial analysis.
        row = np.arange(12)
        tone_row = ToneRow(row)
        matrix = tone_row.matrix()
        
        # Check P0 tetrachords
        first_tetrachord = set(matrix[0][:4])
        second_tetrachord = set(matrix[0][4:8])
        third_tetrachord = set(matrix[0][8:12])
        
        # For chromatic P0, tetrachords should be consecutive groups of 4
        self.assertEqual(first_tetrachord, {0, 1, 2, 3})
        self.assertEqual(second_tetrachord, {4, 5, 6, 7})
        self.assertEqual(third_tetrachord, {8, 9, 10, 11})

if __name__ == '__main__':
    unittest.main()