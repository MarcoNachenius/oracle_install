from db_operations.db_connection_validator import DBConnectionValidator
from db_operations.combinatorial_table_entry_generator import CombinatorialTableEntry
from tonerow_analyzer.tonerow_class import ToneRow
from typing import Iterator
import oracledb
from db_operations.db_config_builder import DB_CONFIG
from math import factorial

class DatabaseWriter:
    COMBINATORIAL_TABLE_NAME = 'twelvetone_combinatorials'

    def __init__(self):
        if not DBConnectionValidator.can_connect_and_write():
            raise ConnectionError(
                "Cannot connect to database. Please run the connection validator "
                "and follow the instructions to start the PDB."
            )
        
    
    def populate_combinatorials_table(self, batchSize: int = 100, limitForTesting: int = 0):
        """
        Populates the combinatorials table with all twelve-tone row permutations
        starting with 0, along with their combinatorial transformations.

        If table already exists, it will be cleared before populating.
        """
        self.create_combinatorials_table()

        # Create tonerow iterator
        permutation_iterator: Iterator = ToneRow.tonerows_starting_with_zero_iterator()

        iteration_range: int

        if limitForTesting:
            iteration_range = limitForTesting
        else:
            from math import factorial
            iteration_range = factorial(11)

        connection = None
        batch_count = 0
        total_processed = 0

        try:
            connection = oracledb.connect(**DB_CONFIG.CONNECTION_PARAMS)

            for _ in range(iteration_range):
            
                # Get next tone row from iterator
                prime_row_array = next(permutation_iterator)
                new_tonerow = ToneRow(prime_row_array)
                new_table_entry = CombinatorialTableEntry(new_tonerow)

                # Insert into database
                with connection.cursor() as cursor:
                    cursor.execute(f"""
                        INSERT INTO {self.COMBINATORIAL_TABLE_NAME} 
                        (tone_row, hexachordal_combinatorials, tetrachordal_combinatorials, trichordal_combinatorials)
                        VALUES (:1, :2, :3, :4)
                    """, [
                        new_table_entry.prime_row_string,
                        new_table_entry.hexachordal_combinatorials_string,
                        new_table_entry.tetrachordal_combinatorials_string,
                        new_table_entry.trichordal_combinatorials_string
                    ])

                batch_count += 1
                total_processed += 1

                # Commit in batches for performance
                if batch_count >= batchSize:
                    connection.commit()
                    batch_count = 0
                
                # Update every row but only show 1 decimal place for smoother progress
                percentage = (total_processed / iteration_range) * 100
                print(f"\r[PROGRESS] {percentage:.1f}% complete ({total_processed} rows processed)", end="", flush=True)
                
            # Commit any remaining rows
            if batch_count > 0:
                connection.commit()

            print(f"[SUCCESS] 100% complete - Processed all {total_processed} tone rows")

        except Exception as e:
            print(f"[ERROR] Failed to populate combinatorials table: {e}")
            if connection:
                connection.rollback()
            raise

        finally:
            if connection:
                connection.close()

    def create_combinatorials_table(self):
        """
        Creates a table for storing twelve-tone row permutations with strict size limits.

        The table stores:
        - Primary key: tone row as string (max 25 chars)
        - Combinatorial transformations for hexachordal, tetrachordal, trichordal
        - Counts of combinatorial rows for each type
        """
        connection = None

        try:
            connection = oracledb.connect(**DB_CONFIG.CONNECTION_PARAMS)

            with connection.cursor() as cursor:
                # Drop table if exists
                cursor.execute(f"""
                    BEGIN
                        EXECUTE IMMEDIATE 'DROP TABLE {self.COMBINATORIAL_TABLE_NAME}';
                    EXCEPTION
                        WHEN OTHERS THEN NULL;
                    END;
                """)

                # Create table with strict size limits
                cursor.execute(f"""
                    CREATE TABLE {self.COMBINATORIAL_TABLE_NAME} (
                        -- Primary key: tone row as string "0 1 2 3 4 5 6 7 8 9 10 11"
                        tone_row VARCHAR2(25) PRIMARY KEY,

                        -- Combinatorial transformations (e.g., 'R1 RI5 I6')
                        hexachordal_combinatorials VARCHAR2(250),
                        tetrachordal_combinatorials VARCHAR2(250),
                        trichordal_combinatorials VARCHAR2(250)
                    )
                """)
                connection.commit()
                print(f"[SUCCESS] Twelve-tone permutations table created successfully!")

        except Exception as e:
            print(f"[ERROR] Failed to create permutations table: {e}")
            if connection:
                connection.rollback()
            raise
        
        finally:
            if connection:
                connection.close()
    
    def remove_combinatorials_table(self):
        """
        Removes the combinatorials table if it exists.
        Safe to call even if the table doesn't exist.
        """
        connection = None

        try:
            connection = oracledb.connect(**DB_CONFIG.CONNECTION_PARAMS)

            with connection.cursor() as cursor:
                # Drop table if exists
                cursor.execute(f"""
                    BEGIN
                        EXECUTE IMMEDIATE 'DROP TABLE {self.COMBINATORIAL_TABLE_NAME}';
                    EXCEPTION
                        WHEN OTHERS THEN NULL;
                    END;
                """)

                connection.commit()
                print(f"[SUCCESS] Combinatorials table '{self.COMBINATORIAL_TABLE_NAME}' removed successfully!")

        except Exception as e:
            print(f"[ERROR] Failed to remove combinatorials table: {e}")
            if connection:
                connection.rollback()
            raise
        
        finally:
            if connection:
                connection.close()