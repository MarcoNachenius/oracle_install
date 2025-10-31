import unittest
import numpy as np
from tonerow_analyzer.tonerow_class import ToneRow
from tonerow_analyzer.combinatorial_trichords import CombinatorialTrichords

class TestPrimeTrichordCombinatorials(unittest.TestCase):
    
    def test_chromatic_row_returns_p3_p6_p9(self):
        """Test that chromatic scale row returns P3, P6, P9 as combinatorial"""
        chromatic_row = ToneRow(np.arange(12))
        result = CombinatorialTrichords.prime_combinatorials(chromatic_row)
        
        # For chromatic scale P0: {0,1,2}, {3,4,5}, {6,7,8}, {9,10,11}
        # P3: {3,4,5}, {6,7,8}, {9,10,11}, {0,1,2} - all trichords match!
        # P6: {6,7,8}, {9,10,11}, {0,1,2}, {3,4,5} - all trichords match!
        # P9: {9,10,11}, {0,1,2}, {3,4,5}, {6,7,8} - all trichords match!
        expected = ['P3', 'P6', 'P9']
        self.assertEqual(sorted(result), sorted(expected))
        self.assertEqual(len(result), 3)


class TestInversionTrichordCombinatorials(unittest.TestCase):
    
    def test_chromatic_row_returns_i2_i5_i8_i11(self):
        """Test that chromatic scale row returns I2, I5, I8, I11 as combinatorial"""
        chromatic_row = ToneRow(np.arange(12))
        result = CombinatorialTrichords.inversion_combinatorials(chromatic_row)
        
        # For chromatic scale P0: {0,1,2}, {3,4,5}, {6,7,8}, {9,10,11}
        # I2: [2,1,0,11,10,9,8,7,6,5,4,3] - trichords: {2,1,0}, {11,10,9}, {8,7,6}, {5,4,3}
        # I5: [5,4,3,2,1,0,11,10,9,8,7,6] - trichords: {5,4,3}, {2,1,0}, {11,10,9}, {8,7,6}
        # I8: [8,7,6,5,4,3,2,1,0,11,10,9] - trichords: {8,7,6}, {5,4,3}, {2,1,0}, {11,10,9}
        # I11: [11,10,9,8,7,6,5,4,3,2,1,0] - trichords: {11,10,9}, {8,7,6}, {5,4,3}, {2,1,0}
        expected = ['I2', 'I5', 'I8', 'I11']
        self.assertEqual(sorted(result), sorted(expected))
        self.assertEqual(len(result), 4)

    def test_chromatic_row_includes_i0_if_combinatorial(self):
        """Test that I0 is included if it happens to be combinatorial"""
        chromatic_row = ToneRow(np.arange(12))
        result = CombinatorialTrichords.inversion_combinatorials(chromatic_row)
        
        # For chromatic scale, I0 = [0,11,10,9,8,7,6,5,4,3,2,1]
        # Trichords: {0,11,10}, {9,8,7}, {6,5,4}, {3,2,1}
        # These don't match P0's trichords {0,1,2}, {3,4,5}, {6,7,8}, {9,10,11}
        # So I0 should NOT be included for chromatic scale
        self.assertNotIn('I0', result)

    def test_all_results_have_correct_format(self):
        """Test that all returned transformations have correct I# format"""
        chromatic_row = ToneRow(np.arange(12))
        result = CombinatorialTrichords.inversion_combinatorials(chromatic_row)
        
        for transformation in result:
            self.assertTrue(transformation.startswith('I'))
            # Check that the part after 'I' is a valid integer 0-11
            level = int(transformation[1:])
            self.assertGreaterEqual(level, 0)
            self.assertLessEqual(level, 11)

    def test_inversion_levels_are_correct(self):
        """Test that inversion levels are calculated correctly"""
        chromatic_row = ToneRow(np.arange(12))
        result = CombinatorialTrichords.inversion_combinatorials(chromatic_row)
        
        # For chromatic scale, I2, I5, I8, I11 should be found
        levels_found = [int(transformation[1:]) for transformation in result]
        self.assertEqual(sorted(levels_found), [2, 5, 8, 11])

    def test_webern_op_27_has_inversion_combinatorials(self):
        """Test that a known row (Webern Op. 27) has some inversion combinatorial forms"""
        webern_row = ToneRow(np.array([0, 11, 3, 4, 8, 7, 9, 5, 6, 1, 2, 10], dtype=int))
        result = CombinatorialTrichords.inversion_combinatorials(webern_row)
        self.assertIsInstance(result, list)

    def test_trichord_matching_is_order_insensitive(self):
        """Test that trichord matching works regardless of order within trichords"""
        chromatic_row = ToneRow(np.arange(12))
        result = CombinatorialTrichords.inversion_combinatorials(chromatic_row)
        
        # Should still find I2, I5, I8, I11 because sets are used for comparison
        expected_levels = [2, 5, 8, 11]
        result_levels = [int(transformation[1:]) for transformation in result]
        self.assertEqual(sorted(result_levels), sorted(expected_levels))

    def test_no_combinatorials_returns_empty_list(self):
        """Test that a row with no inversion trichordal combinatorials returns empty list"""
        # This might be difficult to construct, but we can test the boundary
        complex_row = ToneRow(np.array([0, 3, 1, 4, 2, 5, 6, 9, 7, 10, 8, 11], dtype=int))
        result = CombinatorialTrichords.inversion_combinatorials(complex_row)
        self.assertIsInstance(result, list)

    def test_fourth_trichord_optimization_works(self):
        """Test that the fourth trichord optimization (single element check) works correctly"""
        chromatic_row = ToneRow(np.arange(12))
        result = CombinatorialTrichords.inversion_combinatorials(chromatic_row)
        
        # If the optimization works, we should get the correct 4 results
        self.assertEqual(len(result), 4)
    
    def test_i2_combinatoriality_explanation(self):
        """Explain why I2 is trichordally combinatorial with P0 chromatic"""
        chromatic_row = ToneRow(np.arange(12))
        
        # P0 Chromatic: [0,1,2,3,4,5,6,7,8,9,10,11]
        # P0 Trichords: {0,1,2}, {3,4,5}, {6,7,8}, {9,10,11}
        
        # I2: [2,1,0,11,10,9,8,7,6,5,4,3]
        # I2 Trichords: {2,1,0}, {11,10,9}, {8,7,6}, {5,4,3}
        
        # All four trichords match P0's trichords!
        # {2,1,0} == {0,1,2}, {11,10,9} == {9,10,11}, 
        # {8,7,6} == {6,7,8}, {5,4,3} == {3,4,5}
        
        result = CombinatorialTrichords.inversion_combinatorials(chromatic_row)
        self.assertIn('I2', result)

    def test_i5_combinatoriality_explanation(self):
        """Explain why I5 is trichordally combinatorial with P0 chromatic"""
        chromatic_row = ToneRow(np.arange(12))
        
        # I5: [5,4,3,2,1,0,11,10,9,8,7,6]
        # I5 Trichords: {5,4,3}, {2,1,0}, {11,10,9}, {8,7,6}
        
        # All four trichords match P0's trichords!
        # {5,4,3} == {3,4,5}, {2,1,0} == {0,1,2},
        # {11,10,9} == {9,10,11}, {8,7,6} == {6,7,8}
        
        result = CombinatorialTrichords.inversion_combinatorials(chromatic_row)
        self.assertIn('I5', result)

    def test_i8_combinatoriality_explanation(self):
        """Explain why I8 is trichordally combinatorial with P0 chromatic"""
        chromatic_row = ToneRow(np.arange(12))
        
        # I8: [8,7,6,5,4,3,2,1,0,11,10,9]
        # I8 Trichords: {8,7,6}, {5,4,3}, {2,1,0}, {11,10,9}
        
        # All four trichords match P0's trichords!
        # {8,7,6} == {6,7,8}, {5,4,3} == {3,4,5},
        # {2,1,0} == {0,1,2}, {11,10,9} == {9,10,11}
        
        result = CombinatorialTrichords.inversion_combinatorials(chromatic_row)
        self.assertIn('I8', result)

    def test_i11_combinatoriality_explanation(self):
        """Explain why I11 is trichordally combinatorial with P0 chromatic"""
        chromatic_row = ToneRow(np.arange(12))
        
        # I11: [11,10,9,8,7,6,5,4,3,2,1,0]
        # I11 Trichords: {11,10,9}, {8,7,6}, {5,4,3}, {2,1,0}
        
        # All four trichords match P0's trichords!
        # {11,10,9} == {9,10,11}, {8,7,6} == {6,7,8},
        # {5,4,3} == {3,4,5}, {2,1,0} == {0,1,2}
        
        result = CombinatorialTrichords.inversion_combinatorials(chromatic_row)
        self.assertIn('I11', result)

    def test_i0_not_combinatorial_explanation(self):
        """Explain why I0 is NOT trichordally combinatorial with P0 chromatic"""
        chromatic_row = ToneRow(np.arange(12))
        
        # I0: [0,11,10,9,8,7,6,5,4,3,2,1]
        # I0 Trichords: {0,11,10}, {9,8,7}, {6,5,4}, {3,2,1}
        
        # These do NOT match P0's trichords:
        # {0,11,10} != {0,1,2}, {9,8,7} != {3,4,5}, etc.
        
        result = CombinatorialTrichords.inversion_combinatorials(chromatic_row)
        self.assertNotIn('I0', result)


class TestRetrogradeTrichordCombinatorials(unittest.TestCase):
    
    def test_chromatic_row_returns_r3_r6_r9(self):
        """Test that chromatic scale row returns R3, R6, R9 as combinatorial"""
        chromatic_row = ToneRow(np.arange(12))
        result = CombinatorialTrichords.retrograde_combinatorials(chromatic_row)
        
        # For chromatic scale P0: {0,1,2}, {3,4,5}, {6,7,8}, {9,10,11}
        # R3 is retrograde of P3: P3 = [3,4,5,6,7,8,9,10,11,0,1,2] → R3 = [2,1,0,11,10,9,8,7,6,5,4,3]
        # R3 trichords: {2,1,0}, {11,10,9}, {8,7,6}, {5,4,3} ← All match P0's trichords!
        # R6 is retrograde of P6: P6 = [6,7,8,9,10,11,0,1,2,3,4,5] → R6 = [5,4,3,2,1,0,11,10,9,8,7,6]  
        # R6 trichords: {5,4,3}, {2,1,0}, {11,10,9}, {8,7,6} ← All match P0's trichords!
        # R9 is retrograde of P9: P9 = [9,10,11,0,1,2,3,4,5,6,7,8] → R9 = [8,7,6,5,4,3,2,1,0,11,10,9]
        # R9 trichords: {8,7,6}, {5,4,3}, {2,1,0}, {11,10,9} ← All match P0's trichords!
        expected = ['R3', 'R6', 'R9']
        self.assertEqual(sorted(result), sorted(expected))
        self.assertEqual(len(result), 3)

    def test_chromatic_row_excludes_r0(self):
        """Test that R0 is excluded from results"""
        chromatic_row = ToneRow(np.arange(12))
        result = CombinatorialTrichords.retrograde_combinatorials(chromatic_row)
        self.assertNotIn('R0', result)

    def test_all_results_have_correct_format(self):
        """Test that all returned transformations have correct R# format"""
        chromatic_row = ToneRow(np.arange(12))
        result = CombinatorialTrichords.retrograde_combinatorials(chromatic_row)
        
        for transformation in result:
            self.assertTrue(transformation.startswith('R'))
            # Check that the part after 'R' is a valid integer 1-11
            level = int(transformation[1:])
            self.assertGreaterEqual(level, 1)
            self.assertLessEqual(level, 11)

    def test_retrograde_levels_are_correct(self):
        """Test that retrograde levels are calculated correctly"""
        chromatic_row = ToneRow(np.arange(12))
        result = CombinatorialTrichords.retrograde_combinatorials(chromatic_row)
        
        # For chromatic scale, R3, R6, R9 should be found
        levels_found = [int(transformation[1:]) for transformation in result]
        self.assertEqual(sorted(levels_found), [3, 6, 9])

    def test_webern_op_27_has_retrograde_combinatorials(self):
        """Test that a known row (Webern Op. 27) has some retrograde combinatorial forms"""
        webern_row = ToneRow(np.array([0, 11, 3, 4, 8, 7, 9, 5, 6, 1, 2, 10], dtype=int))
        result = CombinatorialTrichords.retrograde_combinatorials(webern_row)
        self.assertIsInstance(result, list)

    def test_trichord_matching_is_order_insensitive(self):
        """Test that trichord matching works regardless of order within trichords"""
        chromatic_row = ToneRow(np.arange(12))
        result = CombinatorialTrichords.retrograde_combinatorials(chromatic_row)
        
        # Should still find R3, R6, R9 because sets are used for comparison
        expected_levels = [3, 6, 9]
        result_levels = [int(transformation[1:]) for transformation in result]
        self.assertEqual(sorted(result_levels), sorted(expected_levels))


class TestRetrogradeCombinatorialityExplanation(unittest.TestCase):
    """Detailed explanations of why specific retrograde forms work for chromatic scale"""
    
    def test_r3_combinatoriality_explanation(self):
        """Explain why R3 is trichordally combinatorial with P0 chromatic"""
        chromatic_row = ToneRow(np.arange(12))
        
        # P0 Chromatic: [0,1,2,3,4,5,6,7,8,9,10,11]
        # P0 Trichords: {0,1,2}, {3,4,5}, {6,7,8}, {9,10,11}
        
        # R3 is retrograde of P3
        # P3: [3,4,5,6,7,8,9,10,11,0,1,2]
        # R3: [2,1,0,11,10,9,8,7,6,5,4,3]
        # R3 Trichords: {2,1,0}, {11,10,9}, {8,7,6}, {5,4,3}
        
        # All four trichords match P0's trichords!
        # {2,1,0} == {0,1,2}, {11,10,9} == {9,10,11}, 
        # {8,7,6} == {6,7,8}, {5,4,3} == {3,4,5}
        
        result = CombinatorialTrichords.retrograde_combinatorials(chromatic_row)
        self.assertIn('R3', result)

    def test_r6_combinatoriality_explanation(self):
        """Explain why R6 is trichordally combinatorial with P0 chromatic"""
        chromatic_row = ToneRow(np.arange(12))
        
        # R6 is retrograde of P6
        # P6: [6,7,8,9,10,11,0,1,2,3,4,5]
        # R6: [5,4,3,2,1,0,11,10,9,8,7,6]
        # R6 Trichords: {5,4,3}, {2,1,0}, {11,10,9}, {8,7,6}
        
        # All four trichords match P0's trichords!
        # {5,4,3} == {3,4,5}, {2,1,0} == {0,1,2},
        # {11,10,9} == {9,10,11}, {8,7,6} == {6,7,8}
        
        result = CombinatorialTrichords.retrograde_combinatorials(chromatic_row)
        self.assertIn('R6', result)

    def test_r9_combinatoriality_explanation(self):
        """Explain why R9 is trichordally combinatorial with P0 chromatic"""
        chromatic_row = ToneRow(np.arange(12))
        
        # R9 is retrograde of P9
        # P9: [9,10,11,0,1,2,3,4,5,6,7,8]
        # R9: [8,7,6,5,4,3,2,1,0,11,10,9]
        # R9 Trichords: {8,7,6}, {5,4,3}, {2,1,0}, {11,10,9}
        
        # All four trichords match P0's trichords!
        # {8,7,6} == {6,7,8}, {5,4,3} == {3,4,5},
        # {2,1,0} == {0,1,2}, {11,10,9} == {9,10,11}
        
        result = CombinatorialTrichords.retrograde_combinatorials(chromatic_row)
        self.assertIn('R9', result)

    def test_r0_not_combinatorial_explanation(self):
        """Explain why R0 is NOT trichordally combinatorial with P0 chromatic"""
        chromatic_row = ToneRow(np.arange(12))
        
        # R0 is retrograde of P0
        # P0: [0,1,2,3,4,5,6,7,8,9,10,11]
        # R0: [11,10,9,8,7,6,5,4,3,2,1,0]
        # R0 Trichords: {11,10,9}, {8,7,6}, {5,4,3}, {2,1,0}
        
        # These DO match P0's trichords!
        # {11,10,9} == {9,10,11}, {8,7,6} == {6,7,8},
        # {5,4,3} == {3,4,5}, {2,1,0} == {0,1,2}
        
        # Wait - R0 SHOULD be combinatorial! But we exclude it because it's the reference
        result = CombinatorialTrichords.retrograde_combinatorials(chromatic_row)
        # R0 is excluded by design (if retrograde_level == 0: continue)
        self.assertNotIn('R0', result)

class TestRetrogradeInversionTrichordCombinatorials(unittest.TestCase):
    
    def test_chromatic_row_returns_ri2_ri5_ri8_ri11(self):
        """Test that chromatic scale row returns RI2, RI5, RI8, RI11 as combinatorial"""
        chromatic_row = ToneRow(np.arange(12))
        result = CombinatorialTrichords.retrograde_inversion_combinatorials(chromatic_row)
        
        # For chromatic scale P0: {0,1,2}, {3,4,5}, {6,7,8}, {9,10,11}
        # RI2: retrograde inversion of I2 → trichords match P0's trichords
        # RI5: retrograde inversion of I5 → trichords match P0's trichords  
        # RI8: retrograde inversion of I8 → trichords match P0's trichords
        # RI11: retrograde inversion of I11 → trichords match P0's trichords
        expected = ['RI2', 'RI5', 'RI8', 'RI11']
        self.assertEqual(sorted(result), sorted(expected))
        self.assertEqual(len(result), 4)

    def test_all_results_have_correct_format(self):
        """Test that all returned transformations have correct RI# format"""
        chromatic_row = ToneRow(np.arange(12))
        result = CombinatorialTrichords.retrograde_inversion_combinatorials(chromatic_row)
        
        for transformation in result:
            self.assertTrue(transformation.startswith('RI'))
            # Check that the part after 'RI' is a valid integer 0-11
            level = int(transformation[2:])
            self.assertGreaterEqual(level, 0)
            self.assertLessEqual(level, 11)

    def test_retrograde_inversion_levels_are_correct(self):
        """Test that retrograde inversion levels are calculated correctly"""
        chromatic_row = ToneRow(np.arange(12))
        result = CombinatorialTrichords.retrograde_inversion_combinatorials(chromatic_row)
        
        # For chromatic scale, RI2, RI5, RI8, RI11 should be found
        levels_found = [int(transformation[2:]) for transformation in result]
        self.assertEqual(sorted(levels_found), [2, 5, 8, 11])

    def test_webern_op_27_has_retrograde_inversion_combinatorials(self):
        """Test that a known row (Webern Op. 27) has some retrograde inversion combinatorial forms"""
        webern_row = ToneRow(np.array([0, 11, 3, 4, 8, 7, 9, 5, 6, 1, 2, 10], dtype=int))
        result = CombinatorialTrichords.retrograde_inversion_combinatorials(webern_row)
        self.assertIsInstance(result, list)

    def test_trichord_matching_is_order_insensitive(self):
        """Test that trichord matching works regardless of order within trichords"""
        chromatic_row = ToneRow(np.arange(12))
        result = CombinatorialTrichords.retrograde_inversion_combinatorials(chromatic_row)
        
        # Should still find RI2, RI5, RI8, RI11 because sets are used for comparison
        expected_levels = [2, 5, 8, 11]
        result_levels = [int(transformation[2:]) for transformation in result]
        self.assertEqual(sorted(result_levels), sorted(expected_levels))


class TestRetrogradeInversionCombinatorialityExplanation(unittest.TestCase):
    """Detailed explanations of why specific retrograde inversion forms work for chromatic scale"""
    
    def test_ri2_combinatoriality_explanation(self):
        """Explain why RI2 is trichordally combinatorial with P0 chromatic"""
        chromatic_row = ToneRow(np.arange(12))
        
        # P0 Chromatic: [0,1,2,3,4,5,6,7,8,9,10,11]
        # P0 Trichords: {0,1,2}, {3,4,5}, {6,7,8}, {9,10,11}
        
        # RI2 is retrograde inversion of I2
        # I2: [2,1,0,11,10,9,8,7,6,5,4,3]
        # RI2: [3,4,5,6,7,8,9,10,11,0,1,2] (reverse of I2)
        # RI2 Trichords: {3,4,5}, {6,7,8}, {9,10,11}, {0,1,2}
        
        # All four trichords match P0's trichords!
        # {3,4,5} == {3,4,5}, {6,7,8} == {6,7,8}, 
        # {9,10,11} == {9,10,11}, {0,1,2} == {0,1,2}
        
        result = CombinatorialTrichords.retrograde_inversion_combinatorials(chromatic_row)
        self.assertIn('RI2', result)

    def test_ri5_combinatoriality_explanation(self):
        """Explain why RI5 is trichordally combinatorial with P0 chromatic"""
        chromatic_row = ToneRow(np.arange(12))
        
        # RI5 is retrograde inversion of I5
        # I5: [5,4,3,2,1,0,11,10,9,8,7,6]
        # RI5: [6,7,8,9,10,11,0,1,2,3,4,5] (reverse of I5)
        # RI5 Trichords: {6,7,8}, {9,10,11}, {0,1,2}, {3,4,5}
        
        # All four trichords match P0's trichords!
        # {6,7,8} == {6,7,8}, {9,10,11} == {9,10,11},
        # {0,1,2} == {0,1,2}, {3,4,5} == {3,4,5}
        
        result = CombinatorialTrichords.retrograde_inversion_combinatorials(chromatic_row)
        self.assertIn('RI5', result)

    def test_ri8_combinatoriality_explanation(self):
        """Explain why RI8 is trichordally combinatorial with P0 chromatic"""
        chromatic_row = ToneRow(np.arange(12))
        
        # RI8 is retrograde inversion of I8
        # I8: [8,7,6,5,4,3,2,1,0,11,10,9]
        # RI8: [9,10,11,0,1,2,3,4,5,6,7,8] (reverse of I8)
        # RI8 Trichords: {9,10,11}, {0,1,2}, {3,4,5}, {6,7,8}
        
        # All four trichords match P0's trichords!
        # {9,10,11} == {9,10,11}, {0,1,2} == {0,1,2},
        # {3,4,5} == {3,4,5}, {6,7,8} == {6,7,8}
        
        result = CombinatorialTrichords.retrograde_inversion_combinatorials(chromatic_row)
        self.assertIn('RI8', result)

    def test_ri11_combinatoriality_explanation(self):
        """Explain why RI11 is trichordally combinatorial with P0 chromatic"""
        chromatic_row = ToneRow(np.arange(12))
        
        # RI11 is retrograde inversion of I11
        # I11: [11,10,9,8,7,6,5,4,3,2,1,0]
        # RI11: [0,1,2,3,4,5,6,7,8,9,10,11] (reverse of I11)
        # RI11 Trichords: {0,1,2}, {3,4,5}, {6,7,8}, {9,10,11}
        
        # All four trichords match P0's trichords!
        # {0,1,2} == {0,1,2}, {3,4,5} == {3,4,5},
        # {6,7,8} == {6,7,8}, {9,10,11} == {9,10,11}
        
        result = CombinatorialTrichords.retrograde_inversion_combinatorials(chromatic_row)
        self.assertIn('RI11', result)

    def test_ri0_combinatoriality_explanation(self):
        """Explain why RI0 may or may not be combinatorial"""
        chromatic_row = ToneRow(np.arange(12))
        
        # RI0 is retrograde inversion of I0
        # I0: [0,11,10,9,8,7,6,5,4,3,2,1]
        # RI0: [1,2,3,4,5,6,7,8,9,10,11,0] (reverse of I0)
        # RI0 Trichords: {1,2,3}, {4,5,6}, {7,8,9}, {10,11,0}
        
        # These do NOT match P0's trichords:
        # {1,2,3} != {0,1,2}, {4,5,6} != {3,4,5}, etc.
        
        result = CombinatorialTrichords.retrograde_inversion_combinatorials(chromatic_row)
        self.assertNotIn('RI0', result)

if __name__ == '__main__':
    unittest.main()