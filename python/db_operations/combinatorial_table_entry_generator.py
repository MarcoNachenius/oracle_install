from tonerow_analyzer.tonerow_class import ToneRow
from tonerow_analyzer.combinatorial_hexachords import CombinatorialHexachords
from tonerow_analyzer.combinatorial_tetrachords import CombinatorialTetrachords
from tonerow_analyzer.combinatorial_trichords import CombinatorialTrichords

class CombinatorialTableEntry:
    """
    Generates processed string values for database entries from a ToneRow object.
    """
    
    def __init__(self, tone_row: ToneRow):
        """
        Initialize with a ToneRow object.
        
        Args:
            tone_row (ToneRow): The tone row to analyze
        """
        self.tone_row: ToneRow = tone_row
    
    @property
    def prime_row_string(self) -> str:
        """
        Gets the prime row as a formatted string: '0 1 2 etc..'
        
        Returns:
            str: Comma-separated string of pitch classes
        """
        prime_array = self.tone_row.prime_row()
        return ' '.join(str(pitch) for pitch in prime_array)
    
    @property
    def hexachordal_combinatorials_string(self) -> str:
        """
        Gets hexachordal combinatorials as formatted string: 'P1 RI2 etc..'
        
        Returns:
            str: Space-separated string of combinatorial transformations
        """
        combinatorials = CombinatorialHexachords.all_hexachordal_combinatorials(self.tone_row)
        return ' '.join(sorted(combinatorials))
    
    @property
    def tetrachordal_combinatorials_string(self) -> str:
        """
        Gets tetrachordal combinatorials as formatted string: 'P1 RI2 etc..'
        
        Returns:
            str: Space-separated string of combinatorial transformations
        """
        combinatorials = CombinatorialTetrachords.all_tetrachordal_combinatorials(self.tone_row)
        return ' '.join(sorted(combinatorials))
        
    
    @property
    def trichordal_combinatorials_string(self) -> str:
        """
        Gets trichordal combinatorials as formatted string: 'P1 RI2 etc..'
        
        Returns:
            str: Space-separated string of combinatorial transformations
        """
        combinatorials = CombinatorialTrichords.all_trichordal_combinatorials(self.tone_row)
        return ' '.join(sorted(combinatorials))
    
    def to_dict(self) -> dict:
        """
        Returns all database fields as a dictionary.
        
        Returns:
            dict: Dictionary with all processed string values
        """
        return {
            'prime_row': self.prime_row_string,
            'hexachordal_combinatorials': self.hexachordal_combinatorials_string,
            'tetrachordal_combinatorials': self.tetrachordal_combinatorials_string,
            'trichordal_combinatorials': self.trichordal_combinatorials_string
        }
    
    def to_csv_row(self) -> str:
        """
        Returns all database fields as a CSV row.
        
        Returns:
            str: CSV formatted row with all fields
        """
        fields = [
            f'"{self.prime_row_string}"',
            f'"{self.hexachordal_combinatorials_string}"',
            f'"{self.tetrachordal_combinatorials_string}"', 
            f'"{self.trichordal_combinatorials_string}"'
        ]
        return ','.join(fields)
    
    def get_csv_header(self) -> str:
        """
        Returns CSV header row.
        
        Returns:
            str: CSV header
        """
        return 'prime_row,hexachordal_combinatorials,tetrachordal_combinatorials,trichordal_combinatorials'
    
    def __str__(self) -> str:
        """
        Returns formatted string representation.
        
        Returns:
            str: Human-readable string representation
        """
        return f"""ToneRow Database Entry:
Prime Row: {self.prime_row_string}
Hexachordal Combinatorials: {self.hexachordal_combinatorials_string}
Tetrachordal Combinatorials: {self.tetrachordal_combinatorials_string}
Trichordal Combinatorials: {self.trichordal_combinatorials_string}"""