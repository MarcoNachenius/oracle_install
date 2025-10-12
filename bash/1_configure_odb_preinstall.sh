#!/usr/bin/bash

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  CONSTANTS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ORACLE USER
readonly ORACLE_USER_NAME="oracle"
readonly ORACLE_USER_PASSWORD="hello"
readonly ORACLE_USER_GROUP="oinstall"
# EXIT CODES
readonly GENERAL_ERROR_EXIT_CODE=1


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  HELPER FUNCTIONS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●
# Purpose:  Terminate script execution immediately with an error message and
#           non-zero exit status.
#
# Behavior: - Prints formatted error message to STDERR (not STDOUT)
#           - Ensures errors are visible even when output is redirected
#           - Exits script with status code 1 (general error exit code)
#           - Supports dynamic error messages via function arguments
#
# Usage:    die "Database connection failed"
#           die "File not found: ${filename}"
#           die "Expected 2 arguments, got $#"
# ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●
die() {
    # All die print messages contain '[ERROR]' as a prefix.
    #
    # Why $* instead of $1?
    # - Flexibility: Allows callers to pass multiple arguments that get automatically
    #   concatenated into a single error message.
    # - Natural syntax: die "File" $filename "not found" works without
    #   manual string concatenation or quoting.
    # - Future-proof: Accommodates complex error messages that might need to
    #   combine literals and variables naturally.
    #
    # The '>&2' syntax redirects output from STDOUT (file descriptor 1)
    # to STDERR (file descriptor 2). This ensures error messages are
    # properly separated from normal program output streams.
    echo "[ERROR] $*" >&2
    
    # Exit with relevant code
    exit $GENERAL_ERROR_EXIT_CODE
}

set_oracle_user_password() {
    echo "Setting password for user '$ORACLE_USER_NAME'"
    echo "$ORACLE_USER_NAME:$ORACLE_USER_PASSWORD" | sudo chpasswd || die "Password change failed for user '$ORACLE_USER_NAME'"
    
}

create_oracle_user_home_dir() {
    echo "Creating home directory for user '$ORACLE_USER_NAME'"
    mkdir -p /u01/app/oracle/product/19c/dbhome_1 || die "Oracle DB home directory could not be created"
}

create_oracle_user_privileges() {
    echo "Creating user privileges for user '$ORACLE_USER_NAME'"
    chown -R $ORACLE_USER_NAME:$ORACLE_USER_GROUP /u01
    chmod -R 775 /u01
}

create_oracle_user_bash_profile() {
    echo "Creating bash profile for user '$ORACLE_USER_NAME'"

    # Copy pre-built bash profile to oracle user
    cp config_files/.bash_profile /home/oracle/.bash_profile

    # Set correct ownership
    chown $ORACLE_USER_NAME:$ORACLE_USER_GROUP /home/oracle/.bash_profile

    # Enable bash profile for oracle user
    su -l $ORACLE_USER_NAME -c "source .bash_profile"
}


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  MAIN EXECUTION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
main() {
    set_oracle_user_password || die "Oracle user password could not be set."
    create_oracle_user_home_dir || die "Oracle user home dir could not be created."
    create_oracle_user_privileges || die "Oracle user privileges could not be assigned."
    create_oracle_user_bash_profile || die "Oracle user bash profile could not be created."
}

main || die "Configuration for oracle database unsuccessfull."

echo "[SUCCESS] Configuration for Oracle Database 19c has been implemented successfully!"