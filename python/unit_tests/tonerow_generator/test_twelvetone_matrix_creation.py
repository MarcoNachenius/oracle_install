import unittest
import numpy as np

from tonerow_analyzer.tonerow_class import ToneRow

class TestTwelveToneMatrixKnownValues(unittest.TestCase):
    """Tests with known, pre-calculated twelve-tone matrices"""
    
    def test_webern_symphony_op21_matrix(self):
        """Test Webern's Symphony, Op. 21 with known matrix"""
        # Webern: [0, 11, 3, 4, 8, 7, 9, 5, 6, 1, 2, 10]
        webern_row = np.array([0, 11, 3, 4, 8, 7, 9, 5, 6, 1, 2, 10])
        
        # Known matrix for Webern's Symphony, Op. 21
        expected_matrix = np.array([
            [ 0, 11,  3,  4,  8,  7,  9,  5,  6,  1,  2, 10],
            [ 1,  0,  4,  5,  9,  8, 10,  6,  7,  2,  3, 11],
            [ 9,  8,  0,  1,  5,  4,  6,  2,  3, 10, 11,  7],
            [ 8,  7, 11,  0,  4,  3,  5,  1,  2,  9, 10,  6],
            [ 4,  3,  7,  8,  0, 11,  1,  9, 10,  5,  6,  2],
            [ 5,  4,  8,  9,  1,  0,  2, 10, 11,  6,  7,  3],
            [ 3,  2,  6,  7, 11, 10,  0,  8,  9,  4,  5,  1],
            [ 7,  6, 10, 11,  3,  2,  4,  0,  1,  8,  9,  5],
            [ 6,  5,  9, 10,  2,  1,  3, 11,  0,  7,  8,  4],
            [11, 10,  2,  3,  7,  6,  8,  4,  5,  0,  1,  9],
            [10,  9,  1,  2,  6,  5,  7,  3,  4, 11,  0,  8],
            [ 2,  1,  5,  6, 10,  9, 11,  7,  8,  3,  4,  0]
        ])
        
        matrix = ToneRow.twelvetone_matrix(webern_row)
        self.assertTrue(np.array_equal(matrix, expected_matrix))

    def test_berg_lyric_suite_matrix(self):
        """Test Berg's Lyric Suite with known matrix"""
        # Berg Lyric Suite: [0, 11, 7, 4, 2, 9, 3, 8, 10, 1, 5, 6]
        berg_row = np.array([0, 11, 7, 4, 2, 9, 3, 8, 10, 1, 5, 6])
        
        # Known matrix for Berg's Lyric Suite
        expected_matrix = np.array([
            [ 0, 11,  7,  4,  2,  9,  3,  8, 10,  1,  5,  6],
            [ 1,  0,  8,  5,  3, 10,  4,  9, 11,  2,  6,  7],
            [ 5,  4,  0,  9,  7,  2,  8,  1,  3,  6, 10, 11],
            [ 8,  7,  3,  0, 10,  5, 11,  4,  6,  9,  1,  2],
            [10,  9,  5,  2,  0,  7,  1,  6,  8, 11,  3,  4],
            [ 3,  2, 10,  7,  5,  0,  6, 11,  1,  4,  8,  9],
            [ 9,  8,  4,  1, 11,  6,  0,  5,  7, 10,  2,  3],
            [ 4,  3, 11,  8,  6,  1,  7,  0,  2,  5,  9, 10],
            [ 2,  1,  9,  6,  4, 11,  5, 10,  0,  3,  7,  8],
            [11, 10,  6,  3,  1,  8,  2,  7,  9,  0,  4,  5],
            [ 7,  6,  2, 11,  9,  4, 10,  3,  5,  8,  0,  1],
            [ 6,  5,  1, 10,  8,  3,  9,  2,  4,  7, 11,  0]
        ])
        
        matrix = ToneRow.twelvetone_matrix(berg_row)
        self.assertTrue(np.array_equal(matrix, expected_matrix))

    def test_schoenberg_woodwind_quintet_matrix(self):
        """Test Schoenberg's Woodwind Quintet with known matrix"""
        # Schoenberg: [0, 11, 9, 10, 6, 7, 5, 4, 2, 3, 1, 8]
        schoenberg_row = np.array([0, 11, 9, 10, 6, 7, 5, 4, 2, 3, 1, 8])
        
        # Known matrix for Schoenberg's Woodwind Quintet
        expected_matrix = np.array([
            [ 0, 11,  9, 10,  6,  7,  5,  4,  2,  3,  1,  8],
            [ 1,  0, 10, 11,  7,  8,  6,  5,  3,  4,  2,  9],
            [ 3,  2,  0,  1,  9, 10,  8,  7,  5,  6,  4, 11],
            [ 2,  1, 11,  0,  8,  9,  7,  6,  4,  5,  3, 10],
            [ 6,  5,  3,  4,  0,  1, 11, 10,  8,  9,  7,  2],
            [ 5,  4,  2,  3, 11,  0, 10,  9,  7,  8,  6,  1],
            [ 7,  6,  4,  5,  1,  2,  0, 11,  9, 10,  8,  3],
            [ 8,  7,  5,  6,  2,  3,  1,  0, 10, 11,  9,  4],
            [10,  9,  7,  8,  4,  5,  3,  2,  0,  1, 11,  6],
            [ 9,  8,  6,  7,  3,  4,  2,  1, 11,  0, 10,  5],
            [11, 10,  8,  9,  5,  6,  4,  3,  1,  2,  0,  7],
            [ 4,  3,  1,  2, 10, 11,  9,  8,  6,  7,  5,  0]
        ])
        
        matrix = ToneRow.twelvetone_matrix(schoenberg_row)
        self.assertTrue(np.array_equal(matrix, expected_matrix))

    def test_babbitt_composition_matrix(self):
        """Test Babbitt's composition with known matrix"""
        # Babbitt: [0, 3, 5, 4, 7, 8, 11, 10, 1, 2, 9, 6]
        babbitt_row = np.array([0, 3, 5, 4, 7, 8, 11, 10, 1, 2, 9, 6])
        
        # Known matrix for Babbitt's row
        expected_matrix = np.array([
            [ 0,  3,  5,  4,  7,  8, 11, 10,  1,  2,  9,  6],
            [ 9,  0,  2,  1,  4,  5,  8,  7, 10, 11,  6,  3],
            [ 7, 10,  0, 11,  2,  3,  6,  5,  8,  9,  4,  1],
            [ 8, 11,  1,  0,  3,  4,  7,  6,  9, 10,  5,  2],
            [ 5,  8, 10,  9,  0,  1,  4,  3,  6,  7,  2, 11],
            [ 4,  7,  9,  8, 11,  0,  3,  2,  5,  6,  1, 10],
            [ 1,  4,  6,  5,  8,  9,  0, 11,  2,  3, 10,  7],
            [ 2,  5,  7,  6,  9, 10,  1,  0,  3,  4, 11,  8],
            [11,  2,  4,  3,  6,  7, 10,  9,  0,  1,  8,  5],
            [10,  1,  3,  2,  5,  6,  9,  8, 11,  0,  7,  4],
            [ 3,  6,  8,  7, 10, 11,  2,  1,  4,  5,  0,  9],
            [ 6,  9, 11, 10,  1,  2,  5,  4,  7,  8,  3,  0]
        ])
        
        matrix = ToneRow.twelvetone_matrix(babbitt_row)
        self.assertTrue(np.array_equal(matrix, expected_matrix))

    def test_stravinsky_elegy_matrix(self):
        """Test Stravinsky's Elegy with known matrix"""
        # Stravinsky: [0, 1, 2, 3, 5, 4, 6, 7, 9, 8, 10, 11]
        stravinsky_row = np.array([0, 1, 2, 3, 5, 4, 6, 7, 9, 8, 10, 11])
        
        # Known matrix for Stravinsky's Elegy
        expected_matrix = np.array([
            [ 0,  1,  2,  3,  5,  4,  6,  7,  9,  8, 10, 11],
            [11,  0,  1,  2,  4,  3,  5,  6,  8,  7,  9, 10],
            [10, 11,  0,  1,  3,  2,  4,  5,  7,  6,  8,  9],
            [ 9, 10, 11,  0,  2,  1,  3,  4,  6,  5,  7,  8],
            [ 7,  8,  9, 10,  0, 11,  1,  2,  4,  3,  5,  6],
            [ 8,  9, 10, 11,  1,  0,  2,  3,  5,  4,  6,  7],
            [ 6,  7,  8,  9, 11, 10,  0,  1,  3,  2,  4,  5],
            [ 5,  6,  7,  8, 10,  9, 11,  0,  2,  1,  3,  4],
            [ 3,  4,  5,  6,  8,  7,  9, 10,  0, 11,  1,  2],
            [ 4,  5,  6,  7,  9,  8, 10, 11,  1,  0,  2,  3],
            [ 2,  3,  4,  5,  7,  6,  8,  9, 11, 10,  0,  1],
            [ 1,  2,  3,  4,  6,  5,  7,  8, 10,  9, 11,  0]
        ])
        
        matrix = ToneRow.twelvetone_matrix(stravinsky_row)
        self.assertTrue(np.array_equal(matrix, expected_matrix))

    def test_identity_row_matrix(self):
        """Test with identity row [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]"""
        identity_row = np.arange(12)
        
        # For identity row, matrix is simple transposition table
        expected_matrix = np.array([
            [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11],
            [11,  0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10],
            [10, 11,  0,  1,  2,  3,  4,  5,  6,  7,  8,  9],
            [ 9, 10, 11,  0,  1,  2,  3,  4,  5,  6,  7,  8],
            [ 8,  9, 10, 11,  0,  1,  2,  3,  4,  5,  6,  7],
            [ 7,  8,  9, 10, 11,  0,  1,  2,  3,  4,  5,  6],
            [ 6,  7,  8,  9, 10, 11,  0,  1,  2,  3,  4,  5],
            [ 5,  6,  7,  8,  9, 10, 11,  0,  1,  2,  3,  4],
            [ 4,  5,  6,  7,  8,  9, 10, 11,  0,  1,  2,  3],
            [ 3,  4,  5,  6,  7,  8,  9, 10, 11,  0,  1,  2],
            [ 2,  3,  4,  5,  6,  7,  8,  9, 10, 11,  0,  1],
            [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11,  0]
        ])
        
        matrix = ToneRow.twelvetone_matrix(identity_row)
        self.assertTrue(np.array_equal(matrix, expected_matrix))


if __name__ == '__main__':
    unittest.main(verbosity=2)