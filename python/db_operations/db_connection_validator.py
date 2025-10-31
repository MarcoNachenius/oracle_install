from db_operations.db_config_builder import DB_CONFIG
import oracledb
import socket

# Initialize Oracle client
try:
    oracledb.init_oracle_client(lib_dir=None)
except Exception:
    pass

class DBConnectionValidator:

    @classmethod
    def can_connect_and_write(cls) -> bool:
        """
        Practical test: Can we connect to ANY accessible database and write data?
        This is what matters for your writer class.
        """
        print("Database Connectivity Test Results")
        print("==================================")
        print(f"Target: {DB_CONFIG.DSN}")
        
        # Test 1: Server reachability
        if not cls._is_server_reachable():
            return False
            
        # Test 2: Try to connect to any accessible database
        accessible_db = cls._find_accessible_database()
        if not accessible_db:
            return False
            
        # Test 3: Can we write data?
        return cls._test_write_operations(accessible_db)
    
    @classmethod
    def _is_server_reachable(cls) -> bool:
        """Check if we can reach the database server"""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(5)
                result = sock.connect_ex((DB_CONFIG.HOST, int(DB_CONFIG.PORT)))
                if result == 0:
                    print("[PASS] Database server is reachable")
                    return True
                else:
                    print("[FAILURE] Cannot reach database server")
                    return False
        except Exception as e:
            print(f"[FAILURE] Network error: {e}")
            return False

    @classmethod
    def _find_accessible_database(cls):
        """
        Simple connection test to configured database.
        Returns connection if successful, None if failed.
        """
        try:
            connection = oracledb.connect(**DB_CONFIG.CONNECTION_PARAMS)
            print(f"[PASS] Connection to {DB_CONFIG.DSN} is possible")
            return connection
        except Exception as e:
            print(f"[FAILURE] Cannot connect to {DB_CONFIG.DSN}: {e}")
            return None
    

    @classmethod
    def _test_write_operations(cls, connection):
        """Test if we can actually write data"""
        try:
            with connection.cursor() as cursor:
                # Create a simple test table
                cursor.execute("""
                    BEGIN
                        EXECUTE IMMEDIATE 'DROP TABLE practical_test';
                    EXCEPTION
                        WHEN OTHERS THEN NULL;
                    END;
                """)
                
                cursor.execute("""
                    CREATE TABLE practical_test (
                        id NUMBER PRIMARY KEY,
                        message VARCHAR2(100),
                        test_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """)
                
                # Insert test data
                cursor.execute("""
                    INSERT INTO practical_test (id, message) 
                    VALUES (1, '[PASS] Can write to database')
                """)
                connection.commit()
                
                # Verify the data
                cursor.execute("SELECT message FROM practical_test WHERE id = 1")
                result = cursor.fetchone()[0]
                
                # Clean up
                cursor.execute("DROP TABLE practical_test")
                connection.commit()

                print(result, "\n")
                return True
                
        except Exception as e:
            print(f"[FAILURE] Write test failed: {e}")
            return False
        
        finally:
            connection.close()
