from tonerow_analyzer.tonerow_class import ToneRow

class CombinatorialTetrachords:

    @staticmethod
    def all_tetrachordal_combinatorials(toneRow: ToneRow) -> list[str]:
        """
        Finds all transformation forms that are tetrachordally combinatorial with P0.

        Combines prime, retrograde, inversion, and retrograde inversion combinatorial relationships
        into a single comprehensive list.

        Args:
            toneRow (ToneRow): A twelve-tone row object containing the matrix

        Returns:
            list[str]: Combined list of all combinatorial transformations across all four types.
                       Format includes 'P', 'R', 'I', and 'RI' prefixes with their respective levels.
                       Example: ['P2', 'P6', 'R4', 'I3', 'RI5', ...]
        """
        all_combinatorials = []

        # Get combinatorial relationships from all four transformation types
        prime_combinatorials = CombinatorialTetrachords.prime_combinatorials(toneRow)
        retrograde_combinatorials = CombinatorialTetrachords.retrograde_combinatorials(toneRow)
        inversion_combinatorials = CombinatorialTetrachords.inversion_combinatorials(toneRow)
        retrograde_inversion_combinatorials = CombinatorialTetrachords.retrograde_inversion_combinatorials(toneRow)

        # Combine all results into a single list
        all_combinatorials.extend(prime_combinatorials)
        all_combinatorials.extend(retrograde_combinatorials)
        all_combinatorials.extend(inversion_combinatorials)
        all_combinatorials.extend(retrograde_inversion_combinatorials)

        return all_combinatorials
    
    @staticmethod
    def prime_combinatorials(toneRow: ToneRow) -> list[str]:
        """
        Finds all prime forms that are tetrachordally combinatorial with P0.

        Args:
            toneRow (ToneRow): A twelve-tone row object containing the matrix

        Returns:
            list[str]: List of combinatorial prime transformations in format ['P1', 'P5', etc.]
                       Excludes P0 as it's the reference row.
        """
        combinatorials_list = []
        matrix = toneRow.matrix()

        first_note_p0 = toneRow.prime_row()[0]

        # Tetrachords of P0 (3 groups of 4)
        first_tetrachord_p0 = set(matrix[0][:4])
        second_tetrachord_p0 = set(matrix[0][4:8])
        third_tetrachord_p0 = set(matrix[0][8:12])

        for prime_row_transposition in matrix:
            first_tetrachord_prime_row_transposition = set(prime_row_transposition[:4])
            second_tetrachord_prime_row_transposition = set(prime_row_transposition[4:8])
            third_tetrachord_prime_row_transposition = set(prime_row_transposition[8:12])

            prime_row_transposition_tetrachords: list[set] = [
                first_tetrachord_prime_row_transposition,
                second_tetrachord_prime_row_transposition,
                third_tetrachord_prime_row_transposition
            ]

            # Find note-group match for FIRST P0 tetrachord (order unimportant)
            found_first_tetrachord_p0_match: bool = False
            for pr_tetrachord in prime_row_transposition_tetrachords:
                if first_tetrachord_p0 == pr_tetrachord:
                    found_first_tetrachord_p0_match = True
                    prime_row_transposition_tetrachords.remove(first_tetrachord_p0)
                    break
            # Suspend search if no match for FIRST P0 tetrachord has not been found
            if not found_first_tetrachord_p0_match:
                continue
            
            # Find note-group match for SECOND P0 tetrachord (order unimportant)
            found_second_tetrachord_p0_match: bool = False
            for pr_tetrachord in prime_row_transposition_tetrachords:
                if second_tetrachord_p0 == pr_tetrachord:
                    found_second_tetrachord_p0_match = True
                    prime_row_transposition_tetrachords.remove(second_tetrachord_p0)
                    break
            # Suspend search if no match for SECOND P0 tetrachord has not been found
            if not found_second_tetrachord_p0_match:
                continue
            
            # For the THIRD P0 tetrachord, we can simply check if there's only one tetrachord left
            # and if it matches the third tetrachord
            if len(prime_row_transposition_tetrachords) != 1:
                continue
            
            found_third_tetrachord_p0_match = (third_tetrachord_p0 == prime_row_transposition_tetrachords[0])
            if not found_third_tetrachord_p0_match:
                continue
            
            # Calculate transposition level
            first_note_current = prime_row_transposition[0]
            transposition_level = first_note_current - first_note_p0
            # Ensure transposition level is a positive number
            transposition_level += 12
            # Ensure transposition number between 0 and 11
            transposition_level %= 12

            # Skip P0
            if transposition_level == 0:
                continue

            transformation = f"P{transposition_level}"
            combinatorials_list.append(transformation)

        return combinatorials_list


    @staticmethod
    def retrograde_combinatorials(toneRow: ToneRow) -> list[str]:
        """
        Finds all retrograde forms that are tetrachordally combinatorial with P0.

        Args:
            toneRow (ToneRow): A twelve-tone row object containing the matrix

        Returns:
            list[str]: List of combinatorial retrograde transformations in format ['R1', 'R5', etc.]
                       Excludes R0 as it's the reference row's retrograde.
        """
        combinatorials_list = []
        matrix = toneRow.matrix()

        first_note_r0 = toneRow.retrograde()[0]

        # Tetrachords of P0 (3 groups of 4)
        first_tetrachord_p0 = set(matrix[0][:4])
        second_tetrachord_p0 = set(matrix[0][4:8])
        third_tetrachord_p0 = set(matrix[0][8:12])

        for prime_row_transposition in matrix:
            # CREATE RETROGRADE FORM by reversing the prime row
            retrograde_form = prime_row_transposition[::-1]

            # Get tetrachords from the RETROGRADE FORM, not the prime form
            first_tetrachord_retrograde = set(retrograde_form[:4])
            second_tetrachord_retrograde = set(retrograde_form[4:8])
            third_tetrachord_retrograde = set(retrograde_form[8:12])

            retrograde_form_tetrachords: list[set] = [
                first_tetrachord_retrograde,
                second_tetrachord_retrograde,
                third_tetrachord_retrograde
            ]

            # Find note-group match for FIRST P0 tetrachord (order unimportant)
            found_first_tetrachord_p0_match: bool = False
            for retro_tetrachord in retrograde_form_tetrachords:
                if first_tetrachord_p0 == retro_tetrachord:
                    found_first_tetrachord_p0_match = True
                    retrograde_form_tetrachords.remove(first_tetrachord_p0)
                    break
            if not found_first_tetrachord_p0_match:
                continue
            
            # Find note-group match for SECOND P0 tetrachord (order unimportant)
            found_second_tetrachord_p0_match: bool = False
            for retro_tetrachord in retrograde_form_tetrachords:
                if second_tetrachord_p0 == retro_tetrachord:
                    found_second_tetrachord_p0_match = True
                    retrograde_form_tetrachords.remove(second_tetrachord_p0)
                    break
            if not found_second_tetrachord_p0_match:
                continue
            
            # For the THIRD P0 tetrachord, check if the remaining tetrachord matches
            if len(retrograde_form_tetrachords) != 1:
                continue
            
            found_third_tetrachord_p0_match = (third_tetrachord_p0 == retrograde_form_tetrachords[0])
            if not found_third_tetrachord_p0_match:
                continue
            
            # Calculate retrograde level using FIRST NOTE of RETROGRADE FORM
            first_note_current_retrograde = retrograde_form[0]
            retrograde_level = first_note_current_retrograde - first_note_r0
            retrograde_level = (retrograde_level + 12) % 12

            # Skip R0
            if retrograde_level == 0:
                continue

            transformation = f"R{retrograde_level}"
            combinatorials_list.append(transformation)

        return combinatorials_list


    @staticmethod
    def inversion_combinatorials(toneRow: ToneRow) -> list[str]:
        """
        Finds all inversion forms that are tetrachordally combinatorial with P0.

        Args:
            toneRow (ToneRow): A twelve-tone row object containing the matrix

        Returns:
            list[str]: List of combinatorial inversion transformations in format ['I1', 'I5', etc.]
        """
        combinatorials_list = []
        matrix = toneRow.matrix()

        # First note of I0 (inversion of P0)
        first_note_i0 = toneRow.inversion()[0]

        # Tetrachords of P0 (3 groups of 4)
        first_tetrachord_p0 = set(matrix[0][:4])
        second_tetrachord_p0 = set(matrix[0][4:8])
        third_tetrachord_p0 = set(matrix[0][8:12])

        # Iterate through columns of the matrix (inversion forms)
        for col_index in range(len(matrix)):
            # Get inversion form (column of matrix)
            inversion_form = matrix[:, col_index]

            # Get tetrachords from the inversion form
            first_tetrachord_inversion = set(inversion_form[:4])
            second_tetrachord_inversion = set(inversion_form[4:8])
            third_tetrachord_inversion = set(inversion_form[8:12])

            inversion_form_tetrachords: list[set] = [
                first_tetrachord_inversion,
                second_tetrachord_inversion,
                third_tetrachord_inversion
            ]

            # Find note-group match for FIRST P0 tetrachord (order unimportant)
            found_first_tetrachord_p0_match: bool = False
            for inv_tetrachord in inversion_form_tetrachords:
                if first_tetrachord_p0 == inv_tetrachord:
                    found_first_tetrachord_p0_match = True
                    inversion_form_tetrachords.remove(first_tetrachord_p0)
                    break
            # Suspend search if no match for FIRST P0 tetrachord has not been found
            if not found_first_tetrachord_p0_match:
                continue
            
            # Find note-group match for SECOND P0 tetrachord (order unimportant)
            found_second_tetrachord_p0_match: bool = False
            for inv_tetrachord in inversion_form_tetrachords:
                if second_tetrachord_p0 == inv_tetrachord:
                    found_second_tetrachord_p0_match = True
                    inversion_form_tetrachords.remove(second_tetrachord_p0)
                    break
            # Suspend search if no match for SECOND P0 tetrachord has not been found
            if not found_second_tetrachord_p0_match:
                continue
            
            # For the THIRD P0 tetrachord, we can simply check if there's only one tetrachord left
            # and if it matches the third tetrachord
            if len(inversion_form_tetrachords) != 1:
                continue
            
            found_third_tetrachord_p0_match = (third_tetrachord_p0 == inversion_form_tetrachords[0])
            if not found_third_tetrachord_p0_match:
                continue
            
            # Calculate inversion level using first note of inversion form
            first_note_current_inversion = inversion_form[0]
            inversion_level = first_note_current_inversion - first_note_i0
            # Ensure inversion level is a positive number
            inversion_level += 12
            # Ensure inversion number between 0 and 11
            inversion_level %= 12

            transformation = f"I{inversion_level}"
            combinatorials_list.append(transformation)

        return combinatorials_list

    @staticmethod
    def retrograde_inversion_combinatorials(toneRow: ToneRow) -> list[str]:
        """
        Finds all retrograde inversion forms that are tetrachordally combinatorial with P0.

        Args:
            toneRow (ToneRow): A twelve-tone row object containing the matrix

        Returns:
            list[str]: List of combinatorial retrograde inversion transformations in format ['RI1', 'RI5', etc.]
        """
        combinatorials_list = []
        matrix = toneRow.matrix()

        # First note of RI0 (retrograde inversion of P0)
        first_note_ri0 = toneRow.retrograde_inversion()[0]

        # Tetrachords of P0 (3 groups of 4)
        first_tetrachord_p0 = set(matrix[0][:4])
        second_tetrachord_p0 = set(matrix[0][4:8])
        third_tetrachord_p0 = set(matrix[0][8:12])

        # Iterate through columns of the matrix (inversion forms)
        for col_index in range(len(matrix)):
            # Get inversion form (column of matrix)
            inversion_form = matrix[:, col_index]

            # CREATE RETROGRADE INVERSION FORM by reversing the inversion form
            retrograde_inversion_form = inversion_form[::-1]

            # Get tetrachords from the RETROGRADE INVERSION FORM
            first_tetrachord_ri = set(retrograde_inversion_form[:4])
            second_tetrachord_ri = set(retrograde_inversion_form[4:8])
            third_tetrachord_ri = set(retrograde_inversion_form[8:12])

            retrograde_inversion_form_tetrachords: list[set] = [
                first_tetrachord_ri,
                second_tetrachord_ri,
                third_tetrachord_ri
            ]

            # Find note-group match for FIRST P0 tetrachord (order unimportant)
            found_first_tetrachord_p0_match: bool = False
            for ri_tetrachord in retrograde_inversion_form_tetrachords:
                if first_tetrachord_p0 == ri_tetrachord:
                    found_first_tetrachord_p0_match = True
                    retrograde_inversion_form_tetrachords.remove(first_tetrachord_p0)
                    break
            # Suspend search if no match for FIRST P0 tetrachord has not been found
            if not found_first_tetrachord_p0_match:
                continue
            
            # Find note-group match for SECOND P0 tetrachord (order unimportant)
            found_second_tetrachord_p0_match: bool = False
            for ri_tetrachord in retrograde_inversion_form_tetrachords:
                if second_tetrachord_p0 == ri_tetrachord:
                    found_second_tetrachord_p0_match = True
                    retrograde_inversion_form_tetrachords.remove(second_tetrachord_p0)
                    break
            # Suspend search if no match for SECOND P0 tetrachord has not been found
            if not found_second_tetrachord_p0_match:
                continue
            
            # For the THIRD P0 tetrachord, we can simply check if there's only one tetrachord left
            # and if it matches the third tetrachord
            if len(retrograde_inversion_form_tetrachords) != 1:
                continue
            
            found_third_tetrachord_p0_match = (third_tetrachord_p0 == retrograde_inversion_form_tetrachords[0])
            if not found_third_tetrachord_p0_match:
                continue
            
            # Calculate retrograde inversion level using first note of retrograde inversion form
            first_note_current_ri = retrograde_inversion_form[0]
            ri_level = first_note_current_ri - first_note_ri0
            # Ensure RI level is a positive number
            ri_level += 12
            # Ensure RI number between 0 and 11
            ri_level %= 12

            transformation = f"RI{ri_level}"
            combinatorials_list.append(transformation)

        return combinatorials_list