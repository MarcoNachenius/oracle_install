import numpy as np
import itertools
from typing import Iterator

class ToneRow:
    def __init__(self, primeRow: np.ndarray[int]):
        if not self.is_valid_tonerow(primeRow):
            raise ValueError("provided tone row is not valid")
        self.__matrix: np.ndarray[int] = self.twelvetone_matrix(primeRow)

    def prime_row(self) -> np.ndarray[int]:
        """Return the prime row (P0) - first row of matrix."""
        return self.__matrix[0].copy()

    def inversion(self) -> np.ndarray[int]:
        """Return the prime inversion (I0) - first column of matrix."""
        return self.__matrix[:, 0].copy()

    def retrograde(self) -> np.ndarray[int]:
        """Return the retrograde of prime (R0) - first row of matrix backwards."""
        # R0 is the first row read backwards
        return self.__matrix[0, ::-1].copy()

    def retrograde_inversion(self) -> np.ndarray[int]:
        """Return the retrograde inversion of prime (RI0) - first column of matrix backwards."""
        # RI0 is the first column read backwards  
        return self.__matrix[::-1, 0].copy()

    def matrix(self) -> np.ndarray[int]:
        return self.__matrix
    
    # STATIC METHODS
    @staticmethod
    def twelvetone_matrix(primeRow: np.ndarray[int]) -> np.ndarray[int]:
        tt_matrix: np.ndarray[int] = np.zeros(shape=(12, 12), dtype=int)

        # Place prime row into first row of matrix - THIS MUST BE PRESERVED
        tt_matrix[0] = primeRow.copy()

        # Calculate inversion of the prime row (I0)
        inversion_row = (-primeRow) % 12

        # Build the matrix properly - each row is a transposition starting from inversion_row[0]
        for i in range(1, 12):
            # Calculate the transposition interval from the inversion
            transposition_interval = (inversion_row[i] - inversion_row[0]) % 12
            # Transpose the prime row by this interval
            tt_matrix[i] = (primeRow + transposition_interval) % 12

        return tt_matrix
    


    
    @staticmethod
    def is_valid_tonerow(toneRow: np.ndarray[int]) -> bool:
        """
        Validate whether a given array represents a valid twelve-tone row.

        A valid twelve-tone row must satisfy two conditions:
        1. Contain exactly 12 elements
        2. Contain all pitch classes 0-11 exactly once (all integers from 0 to 11)

        This follows the fundamental principle of twelve-tone composition where
        all twelve pitch classes must be used in a series without repetition.

        Args:
            toneRow: A numpy array of integers representing a potential tone row

        Returns:
            bool: True if the array is a valid twelve-tone row, False otherwise

        Examples:
            >>> ToneRow.is_valid_tonerow(np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])) # Valid row
            True

            >>> ToneRow.is_valid_tonerow(np.array([0, 1, 2, 3]))  # Too short
            False

            >>> ToneRow.is_valid_tonerow(np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]))  # Duplicate
            False

            >>> ToneRow.is_valid_tonerow(np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]))  # Out of range
            False
        """
        # Check if array has exactly 12 elements
        # This ensures we have a complete twelve-tone series
        has_correct_length = toneRow.size == 12

        # Check if array contains all integers from 0 to 11 exactly once
        # This ensures no pitch class is repeated or missing
        # The set comparison handles both completeness and uniqueness
        contains_all_pitch_classes = set(toneRow) == set(range(12))

        # Both conditions must be satisfied for a valid tone row
        return has_correct_length and contains_all_pitch_classes


    @staticmethod
    def transpose_row(primeRow: np.ndarray[int], intervalSize: int) -> np.ndarray[int]:
        if not ToneRow.is_valid_tonerow(primeRow):
            raise ValueError("provided tone row is not valid")
        
        if intervalSize < -11 or intervalSize > 11:
            raise ValueError("Interval size must be between -11 and 11")

        # Ensure interval size is positive integer between 1 and 11
        converted_interval_size: int = intervalSize
        converted_interval_size += 12
        converted_interval_size %= 12
        

        transposed_tonerow: np.ndarray = primeRow
        # Transpose all notes of prime row upwards by converted interval size
        transposed_tonerow += converted_interval_size
        # Ensure all notes in transposed row are positive ints between 0 and 11
        transposed_tonerow %= 12

        return transposed_tonerow

    @staticmethod
    def tonerows_starting_with_zero_iterator() -> Iterator[np.ndarray]:
        """
        Generate all valid twelve-tone rows that begin with pitch class 0.

        This method efficiently produces every possible twelve-tone series where the 
        first element is fixed as 0, and the remaining 11 pitch classes (1-11) are 
        arranged in all possible permutations. This covers all prime forms starting 
        on pitch class 0, which is the standard reference point in twelve-tone theory.

        The optimization works by:
        1. Fixing the first element as 0 (establishing the prime form's starting pitch)
        2. Generating all permutations of the remaining 11 pitch classes (1-11)
        3. Using NumPy array pre-allocation for memory efficiency

        Mathematical Basis:
        - Total twelve-tone permutations: 12! = 479,001,600
        - With fixed starting 0: 11! = 39,916,800 (12x reduction)
        - This represents all P0 forms (prime forms starting on pitch class 0)

        Yields:
            numpy.ndarray: A valid twelve-tone row starting with 0, shaped as (12,)

        Examples:
            >>> generator = ToneRow.generate_tonerows_starting_with_zero_optimized()
            >>> first_row = next(generator)
            >>> print(first_row)
            [0 1 2 3 4 5 6 7 8 9 10 11]  # Identity row starting with 0

            >>> second_row = next(generator)  
            >>> print(second_row)
            [0 1 2 3 4 5 6 7 8 9 11 10]  # Second permutation

            >>> generator = ToneRow.generate_tonerows_starting_with_zero_optimized()
            >>> first_row = next(generator)
            >>> print(first_row)
            [0 1 2 3 4 5 6 7 8 9 10 11]
            >>> print(type(first_row))
            <class 'numpy.ndarray'>

        Notes:
            - This is a generator function - it yields rows one at a time
            - Memory efficient: only one row exists in memory at any time
            - The complete set represents all possible tone rows in prime form (P0)
            - Each output is guaranteed to be a valid twelve-tone row
        """
        # Create list of pitch classes 1 through 11 (all except the fixed starting 0)
        # This represents the 11 elements that need to be permuted after the fixed start
        remaining_pitches = list(range(1, 12))

        # Iterate through all possible arrangements of the 11 remaining pitch classes
        # itertools.permutations() generates each unique ordering exactly once
        for perm in itertools.permutations(remaining_pitches):
            # Pre-allocate a 12-element integer array filled with zeros
            # This is more efficient than building arrays from scratch each iteration
            row = np.zeros(12, dtype=int)

            # Set the first element to 0 - this establishes our prime form starting pitch
            # In twelve-tone terminology, this is P0 (prime form starting on pitch class 0)
            row[0] = 0  # Fixed first element

            # Assign the current permutation to positions 1 through 11 (the remaining slots)
            # This fills the array with a unique ordering of pitch classes 1-11
            row[1:] = perm  # Fill the rest with permutation

            # Yield the completed twelve-tone row to the caller
            # This allows processing one row at a time without storing all in memory
            yield row