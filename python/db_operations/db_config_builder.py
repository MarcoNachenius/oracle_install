import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Environment variable name constants
class EnvVars:
    """Environment variable names"""
    USERNAME = 'ORACLE_USERNAME'
    PASSWORD = 'ORACLE_PASSWORD'
    HOST = 'ORACLE_HOST'
    PORT = 'ORACLE_PORT'
    SERVICE_NAME = 'ORACLE_SERVICE_NAME'
    SID = 'ORACLE_SID'


class OracleConfig:
    """Oracle Database Configuration"""
    def __init__(self):
        # Required environment variables - no defaults, will raise errors if missing
        self.USERNAME = self._get_required_env(EnvVars.USERNAME)
        self.PASSWORD = self._get_required_env(EnvVars.PASSWORD)
        self.HOST = self._get_required_env(EnvVars.HOST)
        self.PORT = self._get_required_env(EnvVars.PORT)
        self.SERVICE_NAME = self._get_required_env(EnvVars.SERVICE_NAME)
        self.SID = self._get_required_env(EnvVars.SID)
    
    def _get_required_env(self, var_name):
        """Get required environment variable or raise informative error"""
        value = os.getenv(var_name)
        if value is None:
            raise ValueError(
                f"Required environment variable '{var_name}' is not set in .env file. "
                f"Please add '{var_name}=your_value' to your .env file."
            )
        return value
    
    @property
    def DSN(self) -> str:
        """
        Oracle Database Data Source Name (DSN) for connection.

        Returns DSN as string in 'host:port/service_name' format.
        
        Uses Service Name format for Pluggable Database connections.
        Both SERVICE_NAME and SID are available, but Service Name format
        is preferred for Oracle 19c multitenant architecture.
        """
        return f"{self.HOST}:{self.PORT}/{self.SERVICE_NAME}"

    @property
    def CONNECTION_PARAMS(self) -> dict:
        """
        Complete connection parameters for oracledb.connect().
        
        Returns a dictionary with user, password, and dsn parameters
        ready to be passed to oracledb.connect().
        
        Example:
            connection = oracledb.connect(**DB_CONFIG.CONNECTION_PARAMS)
        """
        return {
            'user': self.USERNAME,
            'password': self.PASSWORD,
            'dsn': self.DSN
        }
    
    def display_configuration(self, show_password=False):
        """Display current configuration (for verification)"""
        print("=========================")
        print("Retrieved .env Variables:")
        print("=========================")
        print(f"  -Username: {self.USERNAME}")
        if show_password and self.PASSWORD:
            print(f"  -Password (visible): {self.PASSWORD}")
        else:
            print(f"  -Password (hidden): {'*' * 8 if self.PASSWORD else 'NOT SET'}")
        print(f"  -Host: {self.HOST}")
        print(f"  -Port: {self.PORT}")
        print(f"  -Service Name: {self.SERVICE_NAME}")
        print(f"  -SID: {self.SID}\n")



###############################################################################
# CONFIGURATION SINGLETON INITIALIZATION
###############################################################################
# This section attempts to create the DB_CONFIG singleton instance.
# 
# The singleton pattern ensures:
# - Single instance of OracleConfig throughout the application
# - Immediate validation of all required environment variables
# - Fail-fast behavior if configuration is incomplete
###############################################################################

# Create config singleton instance
# OracleConfig constructor validates all required environment variables
# and provides detailed error messages if any are missing
DB_CONFIG = OracleConfig()
print("[SUCCESS] Database configuration singleton successfully created")
DB_CONFIG.display_configuration()
