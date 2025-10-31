from tonerow_analyzer.tonerow_class import ToneRow

class CombinatorialTrichords:

    @staticmethod
    def all_trichordal_combinatorials(toneRow: ToneRow) -> list[str]:
        """
        Finds all transformation forms that are trichordally combinatorial with P0.

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
        prime_combinatorials = CombinatorialTrichords.prime_combinatorials(toneRow)
        retrograde_combinatorials = CombinatorialTrichords.retrograde_combinatorials(toneRow)
        inversion_combinatorials = CombinatorialTrichords.inversion_combinatorials(toneRow)
        retrograde_inversion_combinatorials = CombinatorialTrichords.retrograde_inversion_combinatorials(toneRow)

        # Combine all results into a single list
        all_combinatorials.extend(prime_combinatorials)
        all_combinatorials.extend(retrograde_combinatorials)
        all_combinatorials.extend(inversion_combinatorials)
        all_combinatorials.extend(retrograde_inversion_combinatorials)

        return all_combinatorials

    @staticmethod
    def all_trichordal_combinatorials(toneRow: ToneRow) -> list[str]:
        """
        Finds all transformation forms that are trichordally combinatorial with P0.

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
        prime_combinatorials = CombinatorialTrichords.prime_combinatorials(toneRow)
        retrograde_combinatorials = CombinatorialTrichords.retrograde_combinatorials(toneRow)
        inversion_combinatorials = CombinatorialTrichords.inversion_combinatorials(toneRow)
        retrograde_inversion_combinatorials = CombinatorialTrichords.retrograde_inversion_combinatorials(toneRow)

        # Combine all results into a single list
        all_combinatorials.extend(prime_combinatorials)
        all_combinatorials.extend(retrograde_combinatorials)
        all_combinatorials.extend(inversion_combinatorials)
        all_combinatorials.extend(retrograde_inversion_combinatorials)

        return all_combinatorials
    
    @staticmethod
    def prime_combinatorials(toneRow: ToneRow) -> list[str]:
        """
        Finds all prime forms that are trichordally combinatorial with P0.

        Args:
            toneRow (ToneRow): A twelve-tone row object containing the matrix

        Returns:
            list[str]: List of combinatorial prime transformations in format ['P1', 'P5', etc.]
                       Excludes P0 as it's the reference row.
        """
        combinatorials_list = []
        matrix = toneRow.matrix()

        first_note_p0 = toneRow.prime_row()[0]

        # First trichord and first note of P0
        first_trichord_p0 = set(matrix[0][:3])
        second_trichord_p0 = set(matrix[0][3:6])
        third_trichord_p0 = set(matrix[0][6:9])
        fourth_trichord_p0 = set(matrix[0][9:12])

        for prime_row_transposition in matrix:
            first_trichord_prime_row_transposition = set(prime_row_transposition[:3])
            second_trichord_prime_row_transposition = set(prime_row_transposition[3:6])
            third_trichord_prime_row_transposition = set(prime_row_transposition[6:9])
            fourth_trichord_prime_row_transposition = set(prime_row_transposition[9:12])

            prime_row_transposition_trichords: list[set] = [
                first_trichord_prime_row_transposition,
                second_trichord_prime_row_transposition,
                third_trichord_prime_row_transposition,
                fourth_trichord_prime_row_transposition
            ]

            # Find note-group match for FIRST P0 trichord (order unimportant)
            found_first_trichord_p0_match: bool = False
            for pr_trichord in prime_row_transposition_trichords:
                if first_trichord_p0 == pr_trichord:
                    found_first_trichord_p0_match = True
                    # Because we have found a match for the FIRST P0 trichord,
                    # we no longer require to iterate through it for finding
                    # other trichord matches.
                    prime_row_transposition_trichords.remove(first_trichord_p0)
                    break
            # Suspend search if no match for FIRST P0 trichord has not been found
            if not found_first_trichord_p0_match:
                continue
            
            # Find note-group match for SECOND P0 trichord (order unimportant)
            found_second_trichord_p0_match: bool = False
            for pr_trichord in prime_row_transposition_trichords:
                if second_trichord_p0 == pr_trichord:
                    found_second_trichord_p0_match = True
                    # Because we have found a match for the SECOND P0 trichord,
                    # we no longer require to iterate through it for finding
                    # other trichord matches.
                    prime_row_transposition_trichords.remove(second_trichord_p0)
                    break
            # Suspend search if no match for SECOND P0 trichord has not been found
            if not found_second_trichord_p0_match:
                continue

            # Find note-group match for THIRD P0 trichord (order unimportant)
            found_third_trichord_p0_match: bool = False
            for pr_trichord in prime_row_transposition_trichords:
                if third_trichord_p0 == pr_trichord:
                    found_third_trichord_p0_match = True
                    # Because we have found a match for the THIRD P0 trichord,
                    # we no longer require to iterate through it for finding
                    # other trichord matches.
                    prime_row_transposition_trichords.remove(third_trichord_p0)
                    break
            # Suspend search if no match for THIRD P0 trichord has not been found
            if not found_third_trichord_p0_match:
                continue
            
            # For the FOURTH P0 trichord, we can simply check if there's only one trichord left
            # and if it matches the fourth trichord
            if len(prime_row_transposition_trichords) != 1:
                continue
            
            found_fourth_trichord_p0_match = (fourth_trichord_p0 == prime_row_transposition_trichords[0])
            if not found_fourth_trichord_p0_match:
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
        Finds all retrograde forms that are trichordally combinatorial with P0.

        Args:
            toneRow (ToneRow): A twelve-tone row object containing the matrix

        Returns:
            list[str]: List of combinatorial retrograde transformations in format ['R1', 'R5', etc.]
                       Excludes R0 as it's the reference row's retrograde.
        """
        combinatorials_list = []
        matrix = toneRow.matrix()

        first_note_r0 = toneRow.retrograde()[0]

        # First trichord and first note of P0
        first_trichord_p0 = set(matrix[0][:3])
        second_trichord_p0 = set(matrix[0][3:6])
        third_trichord_p0 = set(matrix[0][6:9])
        fourth_trichord_p0 = set(matrix[0][9:12])

        for prime_row_transposition in matrix:
            # CREATE RETROGRADE FORM by reversing the prime row
            retrograde_form = prime_row_transposition[::-1]

            # Get trichords from the RETROGRADE FORM, not the prime form
            first_trichord_retrograde = set(retrograde_form[:3])
            second_trichord_retrograde = set(retrograde_form[3:6])
            third_trichord_retrograde = set(retrograde_form[6:9])
            fourth_trichord_retrograde = set(retrograde_form[9:12])

            retrograde_form_trichords: list[set] = [
                first_trichord_retrograde,
                second_trichord_retrograde,
                third_trichord_retrograde,
                fourth_trichord_retrograde
            ]

            # Find note-group match for FIRST P0 trichord (order unimportant)
            found_first_trichord_p0_match: bool = False
            for retro_trichord in retrograde_form_trichords:
                if first_trichord_p0 == retro_trichord:
                    found_first_trichord_p0_match = True
                    retrograde_form_trichords.remove(first_trichord_p0)
                    break
            if not found_first_trichord_p0_match:
                continue
            
            # Find note-group match for SECOND P0 trichord (order unimportant)
            found_second_trichord_p0_match: bool = False
            for retro_trichord in retrograde_form_trichords:
                if second_trichord_p0 == retro_trichord:
                    found_second_trichord_p0_match = True
                    retrograde_form_trichords.remove(second_trichord_p0)
                    break
            if not found_second_trichord_p0_match:
                continue

            # Find note-group match for THIRD P0 trichord (order unimportant)
            found_third_trichord_p0_match: bool = False
            for retro_trichord in retrograde_form_trichords:
                if third_trichord_p0 == retro_trichord:
                    found_third_trichord_p0_match = True
                    retrograde_form_trichords.remove(third_trichord_p0)
                    break
            if not found_third_trichord_p0_match:
                continue
            
            # For the FOURTH P0 trichord, check if the remaining trichord matches
            if len(retrograde_form_trichords) != 1:
                continue
            
            found_fourth_trichord_p0_match = (fourth_trichord_p0 == retrograde_form_trichords[0])
            if not found_fourth_trichord_p0_match:
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
        Finds all inversion forms that are trichordally combinatorial with P0.

        Args:
            toneRow (ToneRow): A twelve-tone row object containing the matrix

        Returns:
            list[str]: List of combinatorial inversion transformations in format ['I1', 'I5', etc.]
        """
        combinatorials_list = []
        matrix = toneRow.matrix()

        # First note of I0 (inversion of P0)
        first_note_i0 = toneRow.inversion()[0]

        # First trichord and first note of P0
        first_trichord_p0 = set(matrix[0][:3])
        second_trichord_p0 = set(matrix[0][3:6])
        third_trichord_p0 = set(matrix[0][6:9])
        fourth_trichord_p0 = set(matrix[0][9:12])

        # Iterate through columns of the matrix (inversion forms)
        for col_index in range(len(matrix)):
            # Get inversion form (column of matrix)
            inversion_form = matrix[:, col_index]

            # Get trichords from the inversion form
            first_trichord_inversion = set(inversion_form[:3])
            second_trichord_inversion = set(inversion_form[3:6])
            third_trichord_inversion = set(inversion_form[6:9])
            fourth_trichord_inversion = set(inversion_form[9:12])

            inversion_form_trichords: list[set] = [
                first_trichord_inversion,
                second_trichord_inversion,
                third_trichord_inversion,
                fourth_trichord_inversion
            ]

            # Find note-group match for FIRST P0 trichord (order unimportant)
            found_first_trichord_p0_match: bool = False
            for inv_trichord in inversion_form_trichords:
                if first_trichord_p0 == inv_trichord:
                    found_first_trichord_p0_match = True
                    # Because we have found a match for the FIRST P0 trichord,
                    # we no longer require to iterate through it for finding
                    # other trichord matches.
                    inversion_form_trichords.remove(first_trichord_p0)
                    break
            # Suspend search if no match for FIRST P0 trichord has not been found
            if not found_first_trichord_p0_match:
                continue
            
            # Find note-group match for SECOND P0 trichord (order unimportant)
            found_second_trichord_p0_match: bool = False
            for inv_trichord in inversion_form_trichords:
                if second_trichord_p0 == inv_trichord:
                    found_second_trichord_p0_match = True
                    # Because we have found a match for the SECOND P0 trichord,
                    # we no longer require to iterate through it for finding
                    # other trichord matches.
                    inversion_form_trichords.remove(second_trichord_p0)
                    break
            # Suspend search if no match for SECOND P0 trichord has not been found
            if not found_second_trichord_p0_match:
                continue

            # Find note-group match for THIRD P0 trichord (order unimportant)
            found_third_trichord_p0_match: bool = False
            for inv_trichord in inversion_form_trichords:
                if third_trichord_p0 == inv_trichord:
                    found_third_trichord_p0_match = True
                    # Because we have found a match for the THIRD P0 trichord,
                    # we no longer require to iterate through it for finding
                    # other trichord matches.
                    inversion_form_trichords.remove(third_trichord_p0)
                    break
            # Suspend search if no match for THIRD P0 trichord has not been found
            if not found_third_trichord_p0_match:
                continue
            
            # For the FOURTH P0 trichord, we can simply check if there's only one trichord left
            # and if it matches the fourth trichord
            if len(inversion_form_trichords) != 1:
                continue
            
            found_fourth_trichord_p0_match = (fourth_trichord_p0 == inversion_form_trichords[0])
            if not found_fourth_trichord_p0_match:
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
        Finds all retrograde inversion forms that are trichordally combinatorial with P0.

        Args:
            toneRow (ToneRow): A twelve-tone row object containing the matrix

        Returns:
            list[str]: List of combinatorial retrograde inversion transformations in format ['RI1', 'RI5', etc.]
        """
        combinatorials_list = []
        matrix = toneRow.matrix()

        # First note of RI0 (retrograde inversion of P0)
        first_note_ri0 = toneRow.retrograde_inversion()[0]

        # First trichord and first note of P0
        first_trichord_p0 = set(matrix[0][:3])
        second_trichord_p0 = set(matrix[0][3:6])
        third_trichord_p0 = set(matrix[0][6:9])
        fourth_trichord_p0 = set(matrix[0][9:12])

        # Iterate through columns of the matrix (inversion forms)
        for col_index in range(len(matrix)):
            # Get inversion form (column of matrix)
            inversion_form = matrix[:, col_index]

            # CREATE RETROGRADE INVERSION FORM by reversing the inversion form
            retrograde_inversion_form = inversion_form[::-1]

            # Get trichords from the RETROGRADE INVERSION FORM
            first_trichord_ri = set(retrograde_inversion_form[:3])
            second_trichord_ri = set(retrograde_inversion_form[3:6])
            third_trichord_ri = set(retrograde_inversion_form[6:9])
            fourth_trichord_ri = set(retrograde_inversion_form[9:12])

            retrograde_inversion_form_trichords: list[set] = [
                first_trichord_ri,
                second_trichord_ri,
                third_trichord_ri,
                fourth_trichord_ri
            ]

            # Find note-group match for FIRST P0 trichord (order unimportant)
            found_first_trichord_p0_match: bool = False
            for ri_trichord in retrograde_inversion_form_trichords:
                if first_trichord_p0 == ri_trichord:
                    found_first_trichord_p0_match = True
                    # Because we have found a match for the FIRST P0 trichord,
                    # we no longer require to iterate through it for finding
                    # other trichord matches.
                    retrograde_inversion_form_trichords.remove(first_trichord_p0)
                    break
            # Suspend search if no match for FIRST P0 trichord has not been found
            if not found_first_trichord_p0_match:
                continue
            
            # Find note-group match for SECOND P0 trichord (order unimportant)
            found_second_trichord_p0_match: bool = False
            for ri_trichord in retrograde_inversion_form_trichords:
                if second_trichord_p0 == ri_trichord:
                    found_second_trichord_p0_match = True
                    # Because we have found a match for the SECOND P0 trichord,
                    # we no longer require to iterate through it for finding
                    # other trichord matches.
                    retrograde_inversion_form_trichords.remove(second_trichord_p0)
                    break
            # Suspend search if no match for SECOND P0 trichord has not been found
            if not found_second_trichord_p0_match:
                continue

            # Find note-group match for THIRD P0 trichord (order unimportant)
            found_third_trichord_p0_match: bool = False
            for ri_trichord in retrograde_inversion_form_trichords:
                if third_trichord_p0 == ri_trichord:
                    found_third_trichord_p0_match = True
                    # Because we have found a match for the THIRD P0 trichord,
                    # we no longer require to iterate through it for finding
                    # other trichord matches.
                    retrograde_inversion_form_trichords.remove(third_trichord_p0)
                    break
            # Suspend search if no match for THIRD P0 trichord has not been found
            if not found_third_trichord_p0_match:
                continue
            
            # For the FOURTH P0 trichord, we can simply check if there's only one trichord left
            # and if it matches the fourth trichord
            if len(retrograde_inversion_form_trichords) != 1:
                continue
            
            found_fourth_trichord_p0_match = (fourth_trichord_p0 == retrograde_inversion_form_trichords[0])
            if not found_fourth_trichord_p0_match:
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