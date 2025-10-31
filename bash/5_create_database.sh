#!/usr/bin/bash

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  CONSTANTS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# EXIT CODES
readonly GENERAL_ERROR_EXIT_CODE=1

# NEW DATABASE CONFIGURATION
readonly TEMPLATE_NAME="General_Purpose.dbc"
readonly GDB_NAME="ORCLCDB"
readonly DB_SID="ORCLCDB"
readonly CHARACTER_SET="AL32UTF8"
readonly SYS_PASSWORD="hello"
readonly SYSTEM_PASSWORD="hello"
readonly PDB_ADMIN_PASSWORD="hello"
readonly CREATE_AS_CONTAINER_DATABASE="true"
readonly NUMBER_OF_PDBS=1
readonly PDB_NAME="ORCLPDB1"
readonly DATABASE_TYPE="MULTIPURPOSE"
readonly MEMORY_MGMT_TYPE="auto_sga"
readonly TOTAL_MEMORY=1024
readonly STORAGE_TYPE="FS"
readonly DATAFILE_DESTINATION="/u01/app/oracle/oradata"
readonly ENABLE_ARCHIVE="false"
readonly RECOVERY_AREA_DESTINATION="/u01/app/oracle/fast_recovery_area"
readonly RECOVERY_AREA_SIZE=1024
readonly REDO_LOG_FILE_SIZE=100
readonly EM_CONFIGURATION="NONE"

# PYTHON ENV FILE CONFIGURATION
readonly PYTHON_DIR="python"
readonly ENV_FILE=".env"

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  HELPER FUNCTIONS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
die() {
    echo "[ERROR] $*" >&2
    exit $GENERAL_ERROR_EXIT_CODE
}

create_database() {
    echo "Creating Oracle database with custom configuration..."
    
    # Create database using dbca with custom parameters
    su - oracle -c "
        dbca -silent -createDatabase \
            -templateName '$TEMPLATE_NAME' \
            -gdbname '$GDB_NAME' \
            -sid '$DB_SID' \
            -responseFile NO_VALUE \
            -characterSet '$CHARACTER_SET' \
            -sysPassword '$SYS_PASSWORD' \
            -systemPassword '$SYSTEM_PASSWORD' \
            -createAsContainerDatabase '$CREATE_AS_CONTAINER_DATABASE' \
            -numberOfPDBs '$NUMBER_OF_PDBS' \
            -pdbName '$PDB_NAME' \
            -pdbAdminPassword '$PDB_ADMIN_PASSWORD' \
            -databaseType '$DATABASE_TYPE' \
            -memoryMgmtType '$MEMORY_MGMT_TYPE' \
            -totalMemory '$TOTAL_MEMORY' \
            -storageType '$STORAGE_TYPE' \
            -datafileDestination '$DATAFILE_DESTINATION' \
            -enableArchive '$ENABLE_ARCHIVE' \
            -recoveryAreaDestination '$RECOVERY_AREA_DESTINATION' \
            -recoveryAreaSize '$RECOVERY_AREA_SIZE' \
            -redoLogFileSize '$REDO_LOG_FILE_SIZE' \
            -emConfiguration '$EM_CONFIGURATION' \
            -ignorePreReqs
    " || die "Database creation failed"
    
    echo "Database created successfully"
}

create_python_env_file() {
    echo "Creating Python .env file..."
    
    # Create python directory if it doesn't exist
    mkdir -p "$PYTHON_DIR" || die "Failed to create python directory"
    
    # Create .env file with database configuration
    cat > "${PYTHON_DIR}/${ENV_FILE}" << EOF
# Oracle Database Configuration
ORACLE_USERNAME=system
ORACLE_PASSWORD=$SYSTEM_PASSWORD
ORACLE_HOST=localhost
ORACLE_PORT=1521
ORACLE_SERVICE_NAME=$PDB_NAME
ORACLE_SID=$DB_SID

# Application Settings
APP_ENV=development
DEBUG=True
EOF

    # Set appropriate permissions for the .env file
    chmod 600 "${PYTHON_DIR}/${ENV_FILE}" || die "Failed to set permissions on .env file"
    
    echo "Python .env file created successfully at ${PYTHON_DIR}/${ENV_FILE}"
}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  MAIN EXECUTION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
main() {
    create_database 
    create_python_env_file
}

main || die "Database creation process failed"

echo "[SUCCESS] Oracle Database has been created successfully with custom configuration!"
echo "[SUCCESS] Python .env file has been created in the ${PYTHON_DIR}/ directory!"