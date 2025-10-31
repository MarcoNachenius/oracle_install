from tonerow_analyzer.tonerow_class import ToneRow

class CombinatorialHexachords:

    @staticmethod
    def all_hexachordal_combinatorials(toneRow: ToneRow) -> list[str]:
        """
        Finds all transformation forms that are hexachordally combinatorial with P0.

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
        prime_combinatorials = CombinatorialHexachords.prime_combinatorials(toneRow)
        retrograde_combinatorials = CombinatorialHexachords.retrograde_combinatorials(toneRow)
        inversion_combinatorials = CombinatorialHexachords.inversion_combinatorials(toneRow)
        retrograde_inversion_combinatorials = CombinatorialHexachords.retrograde_inversion_combinatorials(toneRow)

        # Combine all results into a single list
        all_combinatorials.extend(prime_combinatorials)
        all_combinatorials.extend(retrograde_combinatorials)
        all_combinatorials.extend(inversion_combinatorials)
        all_combinatorials.extend(retrograde_inversion_combinatorials)

        return all_combinatorials
    
    @staticmethod
    def prime_combinatorials(toneRow: ToneRow) -> list[str]:
        """
        Finds all prime forms that are hexachordally combinatorial with P0.

        Args:
            toneRow (ToneRow): A twelve-tone row object containing the matrix

        Returns:
            list[str]: List of combinatorial prime transformations in format ['P1', 'P5', etc.]
                       Excludes P0 as it's the reference row.
        """
        combinatorials_list = []
        matrix = toneRow.matrix()

        first_note_p0 = toneRow.prime_row()[0]

        # First hexachord and first note of P0
        first_hexachord_p0 = set(matrix[0][:6])

        for prime_row in matrix:
            # Get first hexachord of prime row transposition
            first_hexachord_prime = set(prime_row[:6])

            # Check if current row complements P0's first hexachord
            if not first_hexachord_prime.isdisjoint(first_hexachord_p0):
                continue

            # Calculate transposition level
            first_note_current = prime_row[0]
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
        Finds all retrograde forms that are hexachordally combinatorial with P0.

        Args:
            toneRow (ToneRow): A twelve-tone row object containing the matrix

        Returns:
            list[str]: List of combinatorial retrograde transformations in format ['R1', 'R5', etc.]
                       Excludes R0 as it's the reference row's retrograde.
        """
        combinatorials_list = []
        matrix = toneRow.matrix()

        first_note_r0 = toneRow.retrograde()[0]

        # First hexachord and first note of P0
        first_hexachord_p0 = set(matrix[0][:6])

        for prime_row in matrix:
            # Get first hexachord of prime retrograde transposition
            first_hexachord_retrograde = set(prime_row[6:])

            # Check if current row retrograde complements P0's first hexachord
            if not first_hexachord_retrograde.isdisjoint(first_hexachord_p0):
                continue

            # Calculate transposition level
            first_note_current = prime_row[-1]
            transposition_level = first_note_current - first_note_r0
            # Ensure transposition level is a positive number
            transposition_level += 12
            # Ensure transposition number between 0 and 11
            transposition_level %= 12

            # Skip R0
            if transposition_level == 0:
                continue

            transformation = f"R{transposition_level}"
            combinatorials_list.append(transformation)

        return combinatorials_list


    @staticmethod
    def inversion_combinatorials(toneRow: ToneRow) -> list[str]:
        """
        Finds all inversion forms that are hexachordally combinatorial with P0.

        Args:
            toneRow (ToneRow): A twelve-tone row object containing the matrix

        Returns:
            list[str]: List of combinatorial inversion transformations in format ['I1', 'I5', etc.]
                       Excludes I0 as it's the reference row's inversion.
        """
        combinatorials_list = []
        matrix = toneRow.matrix()

        # First note of I0 (inversion of P0)
        first_note_i0 = toneRow.inversion()[0]

        # First hexachord of P0
        first_hexachord_p0 = set(matrix[0][:6])

        for col_index in range(len(matrix)):
            # Get inversion form (column of matrix)
            inversion_form = matrix[:, col_index]

            # Get first hexachord of inversion form
            first_hexachord_inversion = set(inversion_form[:6])

            # Check if current inversion form complements P0's first hexachord
            if not first_hexachord_inversion.isdisjoint(first_hexachord_p0):
                continue

            # Calculate inversion level using first note of inversion form
            first_note_current_inversion = inversion_form[0]
            inversion_level = first_note_current_inversion - first_note_i0
            # Ensure inversion level is a positive number
            inversion_level += 12
            # Ensure inversion number between 0 and 11
            inversion_level %= 12

            # Skip I0 because I0 and P0 share the same first note
            if inversion_level == 0:
                continue

            transformation = f"I{inversion_level}"
            combinatorials_list.append(transformation)

        return combinatorials_list


    @staticmethod
    def retrograde_inversion_combinatorials(toneRow: ToneRow) -> list[str]:
        """
        Finds all retrograde inversion forms that are hexachordally combinatorial with P0.

        Args:
            toneRow (ToneRow): A twelve-tone row object containing the matrix

        Returns:
            list[str]: List of combinatorial retrograde inversion transformations in format ['RI1', 'RI5', etc.]
                       Excludes RI0 as it's the reference row's retrograde inversion.
        """
        combinatorials_list = []
        matrix = toneRow.matrix()

        # First note of RI0 (retrograde inversion of P0)
        first_note_ri0 = toneRow.retrograde_inversion()[0]

        # First hexachord of P0
        first_hexachord_p0 = set(matrix[0][:6])

        for col_index in range(len(matrix)):
            # Get the inversion form from matrix column
            ri_form = matrix[:, col_index]

            # Reverse the inversion form using slicing.
            # Slicing syntax: [start:stop:step].
            # [::-1] means "take all elements with step -1" (backwards).
            ri_form = ri_form[::-1]         

            # Get first hexachord of retrograde inversion form
            first_hexachord_ri = set(ri_form[:6])

            # Check if current retrograde inversion form complements P0's first hexachord
            if not first_hexachord_ri.isdisjoint(first_hexachord_p0):
                continue

            # Calculate retrograde inversion level using first note of RI form
            first_note_current_ri = ri_form[0]
            ri_level = first_note_current_ri - first_note_ri0
            # Ensure RI level is a positive number
            ri_level += 12
            # Ensure RI number between 0 and 11
            ri_level %= 12

            # Skip RI0
            if ri_level == 0:
                continue

            transformation = f"RI{ri_level}"
            combinatorials_list.append(transformation)

        return combinatorials_list