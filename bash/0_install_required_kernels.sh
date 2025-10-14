#!/usr/bin/bash

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  CONSTANTS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# EXIT CODES
readonly GENERAL_ERROR_EXIT_CODE=1
readonly PACKAGE_ERROR_EXIT_CODE=2


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


# ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●
# Purpose:  Terminate script execution immediately with an error message and
#           non-zero exit status.
#
# Behavior: - Prints formatted error message to STDERR (not STDOUT)
#           - Ensures errors are visible even when output is redirected
#           - Exits script with status code 2 (package failure exit code)
#           - Supports dynamic error messages via function arguments
#
# Usage:    die_package "File not found: ${filename}"
#           die_package "Expected 2 arguments, got $#"
#           
# ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●
die_package() {
    # All die print messages contain '[PACKAGE_ERROR]' as a prefix.
    #
    # Why $* instead of $1?
    # - Flexibility: Allows callers to pass multiple arguments that get automatically
    #   concatenated into a single error message.
    # - Natural syntax: die "File" $filename "not found" works without
    #   manual string concatenation or quoting.
    # - Future-proof: Accommodates complex error messages that might need to
    #   combine literals and variables naturally.
    #
    # '>&2' redirects output from STDOUT (file descriptor 1)
    # to STDERR (file descriptor 2). This ensures error messages are
    # properly separated from normal program output streams.
    echo "[PACKAGE_ERROR] $*" >&2
    
    # Exit with relevant code
    exit $PACKAGE_ERROR_EXIT_CODE
}


# ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●
# Purpose:  Install kernel UEK development package matching current kernel version
# ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●
install_kernel_uek_devel() {
    # Retrieve current kernel version to construct package name
    local kernel_version
    kernel_version=$(uname -r)

    # Construct full package name
    local package_name="kernel-uek-devel-${kernel_version}"
    
    echo "Installing kernel UEK development package: ${package_name}"
    
    dnf install -y "$package_name" || return 1
    return 0
}


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  MAIN EXECUTION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
main() {
    install_kernel_uek_devel || die_package "Kernel UEK development package could not be installed"
}

main || die "Kernel UEK development package installation script failed unexpectedly"

echo "[SUCCESS] Oracle Database 19c preinstall package has been successfully downloaded and installed!"